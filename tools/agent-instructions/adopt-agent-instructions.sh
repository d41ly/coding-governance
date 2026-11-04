#!/usr/bin/env bash
# adopt-agent-instructions.sh — install ONE canonical agent-instruction file in a target repo and
# wire every AI coding tool's expected filename to it, so a single source drives them all.
#
# Canonical = AGENTS.md (the Linux-Foundation cross-tool standard: read natively by Codex/Copilot/
# Cursor/Windsurf/Amp/Devin/Zed/Aider/Jules and Gemini CLI via .gemini config). Claude Code reads
# CLAUDE.md; from 2.1.277 it also reads AGENTS.md, but only in a project with no CLAUDE.md
# (anthropics/claude-code#6235, closed) — so CLAUDE.md stays a `@AGENTS.md` import (or symlink/copy),
# which serves a CLI older than 2.1.277 and a project whose CLAUDE.md exists for another reason.
# A canonical over CODEX_MAX bytes is announced (Codex reads only that much by default); exit unchanged.
#
#   adopt-agent-instructions.sh [--source <file>] [--aliases "claude gemini copilot cursor windsurf"]
#       [--mode symlink|pointer|copy] [--check] [--force]
#
# --source   file whose CONTENT becomes AGENTS.md (default: reuse an existing AGENTS.md; error if neither).
# --aliases  which tool files to wire (default: "claude gemini copilot"). Names: claude gemini copilot cursor windsurf.
# --mode     symlink: real symlinks → AGENTS.md (needs Developer Mode/elevation on Windows; auto-falls back);
#            pointer (DEFAULT): native indirection where one exists (CLAUDE.md = `@AGENTS.md` import;
#              Gemini = .gemini/settings.json context.fileName); others fall back to a synced copy;
#            copy: real duplicate files kept honest by --check (drift needs --force to re-sync).
# --check    verify wiring only (symlinks resolve / pointers intact / copies match AGENTS.md); exit 1 on drift.
# --force    overwrite an existing alias (file OR symlink) that isn't already correct wiring.
#
# THE ALIASES ARE THE RENDERER'S (PLAY-dOrderedCharter-20): this adopter installs the canonical and calls
# the playbook-render kit's `entry-files` scope, which writes them and records each one's lock row. It keeps
# no fallback, so with no renderer it exits 2 and writes nothing.
#
# Exit 0 clean · 1 a wiring/check failure · 2 environment/usage error. Idempotent: re-running converges
# (copy-mode drift is the one exception — it needs --force). Needs git, coreutils, python at the floor
# below and the playbook-render kit.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)   # before the cd: $0 may be relative
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || ROOT=$PWD
cd "$ROOT" || { echo "AGENT-INSTR env ERROR — cannot enter repo root"; exit 2; }

CANON="AGENTS.md"
CODEX_MAX=32768   # Codex's default project_doc_max_bytes (32 KiB); a file of exactly this size is read whole
SOURCE=""; ALIASES="claude gemini copilot"; MODE="pointer"; CHECK=0; FORCE=0
need_val() { [ "$1" -ge 2 ] || { echo "AGENT-INSTR env ERROR — $2 needs a value"; exit 2; }; }
while [ $# -gt 0 ]; do
  case "$1" in
    --source)  need_val $# --source;  SOURCE=$2; shift 2;;
    --aliases) need_val $# --aliases; ALIASES=$2; shift 2;;
    --mode)    need_val $# --mode;    MODE=$2; shift 2;;
    --check)   CHECK=1; shift;;
    --force)   FORCE=1; shift;;
    *) echo "AGENT-INSTR env ERROR — unknown arg: $1"; exit 2;;
  esac
done
case "$MODE" in symlink|pointer|copy) ;; *) echo "AGENT-INSTR env ERROR — --mode must be symlink|pointer|copy (got '$MODE')"; exit 2;; esac

# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  # THE FLOOR is declared once, in python-floor.txt in gov's lib dir. The literal below is its
  # generated copy, held equal to it by the floor module's `check` and by these blocks' parity rows,
  # because a copy-installed kit has no lib dir to read. A candidate that runs below it is passed
  # over and named, exactly as a candidate that does not run.
  _rp_floor="3.15"
  _rp_fv=$(( ${_rp_floor%%.*} * 1000 + ${_rp_floor#*.} ))
  _rp_tried=""; _rp_seen=""; _rp_best=""; _rp_bv=0; _rp_bver=""; _rp_o1=""; _rp_og=""; _rp_i=0
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    _rp_i=$((_rp_i + 1))
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    # ONE spawn per candidate, isolated: its major.minor and its own executable, forward-slashed,
    # because a backslashed C:\ path handed to MSYS bash loses its separators.
    _rp_out=$("$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))' 2>/dev/null) || _rp_out=""
    _rp_out=${_rp_out%$'\r'}
    if [[ ${_rp_out%% *} =~ ^([0-9]+)\.([0-9]+)$ ]]; then
      _rp_cv=$(( 10#${BASH_REMATCH[1]} * 1000 + 10#${BASH_REMATCH[2]} ))
      if [ "$_rp_cv" -ge "$_rp_fv" ]; then
        # An override, the caller's or GOV_PYTHON, names the command a consumer spawns, a wrapper
        # or a venv launcher included, and is echoed as given. Only the three launcher names give
        # way to the direct executable where the probe named a file; the launcher's own name
        # otherwise. The `[ -f ]` HOLDS on a Windows App Execution Alias, so a Store Python whose
        # own sys.executable is an alias is echoed as printed: a gap the run-gates kit's
        # check_app_alias closes for the legs it measures, and this block does not.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_i" -gt 2 ] && [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
        return 0
      fi
      _rp_why="ran ${_rp_out%% *}, below the floor $_rp_floor"
      if [ "$_rp_cv" -gt "$_rp_bv" ]; then _rp_best=$_rp_c; _rp_bv=$_rp_cv; _rp_bver=${_rp_out%% *}; fi
    else
      _rp_why="did not run"
    fi
    _rp_seen="${_rp_seen}resolve_python:   $_rp_c: $_rp_why"$'\n'
    [ "$_rp_i" != 1 ] || _rp_o1=$_rp_why
    [ "$_rp_i" != 2 ] || _rp_og=$_rp_why
  done
  {
    echo "resolve_python: no usable python launcher at the floor $_rp_floor (python-floor.txt in gov's lib dir)."
    echo "resolve_python: Each candidate was RUN with -I -c — being on PATH is not evidence (the Microsoft Store"
    echo "resolve_python: python3 stub answers \`command -v\` and exits 9009 without running anything)."
    printf '%s' "$_rp_seen"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and $_rp_o1."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and $_rp_og. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
    # THE INSTALL COMMAND, as platforms.provision says. The policy kit's own reader answers it at the
    # landed revision, run by the newest candidate that ran, since its tomllib needs 3.11, and never
    # through the policy shim, which resolves a launcher itself and would re-enter this refusal.
    _rp_prov=name; _rp_pwhy=""
    if [ -z "$_rp_best" ]; then
      _rp_pwhy="no reader ran, because no candidate ran"
    elif [ "$_rp_bv" -lt 3011 ]; then
      _rp_pwhy="no reader ran, because the newest candidate that ran, $_rp_best, is $_rp_bver, below the 3.11 the reader needs"
    else
      IFS= read -r -d '' _rp_rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
      case "${BASH_SOURCE[0]:-}" in */*) _rp_here=${BASH_SOURCE[0]%/*} ;; *) _rp_here=. ;; esac
      _rp_kit=$("$_rp_best" -I -c "${_rp_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("policy", "policy.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$_rp_here" 2>&1) || _rp_pwhy="no reader ran, because ${_rp_kit%$'\r'}"
      if [ -z "$_rp_pwhy" ]; then
        _rp_kit=${_rp_kit%$'\r'}
        _rp_val=$("$_rp_best" "$_rp_kit/policy.py" get platforms.provision 2>/dev/null) || _rp_pwhy="the reader, policy.py get, exited $?"
        _rp_val=${_rp_val%$'\r'}
        case "$_rp_pwhy:$_rp_val" in
          :name|:uv|:off) _rp_prov=$_rp_val ;;
          :*) _rp_pwhy="the reader, policy.py get, printed '$_rp_val', which is no value of the key" ;;
        esac
      fi
    fi
    [ -z "$_rp_pwhy" ] || echo "resolve_python: platforms.provision reads its catalogue default, name: $_rp_pwhy."
    if [ "$_rp_prov" = uv ]; then
      if [ ! -t 2 ]; then _rp_no="not offered, because stderr is not a terminal"
      elif ! uv --version >/dev/null 2>&1; then _rp_no="not offered, because uv does not run"
      else
        printf 'resolve_python: platforms.provision is uv. Run `uv python install %s` now? [y/N] ' "$_rp_floor"
        _rp_a=""; read -r _rp_a </dev/tty || :
        if [ "$_rp_a" = y ]; then
          uv python install "$_rp_floor" || :
          echo "resolve_python: re-run once the floor is on PATH, or name it in GOV_PYTHON."
          _rp_prov=offered
        else
          _rp_no="declined at the prompt"
        fi
      fi
      [ "$_rp_prov" = offered ] || echo "resolve_python: platforms.provision is uv, and the install was $_rp_no."
    fi
    case "$_rp_prov" in
      off) echo "resolve_python: platforms.provision is off, so this refusal names no install command." ;;
      name|uv)
        echo "resolve_python: install the floor with: uv python install $_rp_floor"
        case "${OSTYPE:-}" in msys*|cygwin*|win*) echo "resolve_python: or, on Windows: py install $_rp_floor" ;; esac ;;
    esac
    # LAST, verbatim: the first line names the refusal and this one the candidates, and the lines
    # between them carry the outcomes, the overrides and the install (TOOL-dSafePassage-26 S20).
    echo "resolve_python: tried:$_rp_tried"
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver, INLINED byte-identically from the canonical copy named on its marker line
# and gated by the resolve-python self-test's parity table. `resolve_renderer <python> <here>` prints
# the playbook-render kit's directory, or the resolver's named refusal on stderr and exits 1.
resolve_renderer() {
  local _rkd
  IFS= read -r -d '' _rkd <<'RKD' || :
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
  "$1" -I -c "${_rkd%$'\n'}"'
import sys
try:
    print(resolve_kit_dir("playbook", "render_playbook.py", sys.argv[1]).as_posix())
except LookupError as e:
    sys.exit(str(e))' "$2"
}
PY=$(resolve_python) || { echo "AGENT-INSTR env ERROR — no python, and the playbook-render kit's renderer needs one"; exit 2; }
KIT=$(resolve_renderer "$PY" "$HERE") || { echo "AGENT-INSTR env ERROR — no render_playbook.py: install the playbook-render kit, this adopter's renderer"; exit 2; }
RENDERER=${KIT%$'\r'}/render_playbook.py

# announce, never refuse: the size is the adopter's choice, and Codex can be configured past it.
print_size_note() {
  local n; n=$(wc -c < "$CANON"); n=$((n))
  [ "$n" -gt "$CODEX_MAX" ] && echo "  ! $CANON is $n bytes, over $CODEX_MAX: Codex reads at most 32 KiB of project instructions by default (project_doc_max_bytes) - trim it, or raise that key in the Codex config"
  return 0
}

# ---- --check: verify only ----------------------------------------------
if [ "$CHECK" = 1 ]; then
  [ -f "$CANON" ] || { echo "AGENT-INSTR CHECK FAILED — no canonical $CANON"; exit 1; }
  print_size_note
  exec "$PY" "$RENDERER" --check-render --scope entry-files --target "$ROOT" --aliases "$ALIASES"
fi

# ---- install the canonical ---------------------------------------------
if [ -n "$SOURCE" ]; then
  [ -f "$SOURCE" ] || { echo "AGENT-INSTR env ERROR — --source not found: $SOURCE"; exit 2; }
  if [ -f "$CANON" ] && [ "$FORCE" != 1 ] && ! cmp -s "$SOURCE" "$CANON"; then
    echo "AGENT-INSTR env ERROR — $CANON exists and differs from --source; pass --force to overwrite."; exit 2
  fi
  cp "$SOURCE" "$CANON"
fi
[ -f "$CANON" ] || { echo "AGENT-INSTR env ERROR — no $CANON and no --source to create it from."; exit 2; }

echo "canonical: $CANON ($(wc -c < "$CANON") bytes) · mode: $MODE · aliases: $ALIASES"
print_size_note
if [ "$FORCE" = 1 ]; then set -- --force; else set --; fi
exec "$PY" "$RENDERER" --render-scope entry-files --target "$ROOT" --aliases "$ALIASES" --mode "$MODE" "$@"

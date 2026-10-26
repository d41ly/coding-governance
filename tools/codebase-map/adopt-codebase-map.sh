#!/usr/bin/env bash
# Adopt the codebase-map kit into a project. Run from anywhere INSIDE the target repo, after
# copying this kit dir into it and filling map_extractors.py:
#
#   <kit-dir>/adopt-codebase-map.sh --scaffold
#
# The kit dir's NAME is fixed (`codebase-map` — the gate template resolves the kit by it), but its
# PREFIX under the repo root is free: `<root>/codebase-map/` and `<root>/<prefix>/codebase-map/` are
# both supported, matching map_lib.resolve_root. One segment, though — see the depth check below.
#
# Steps: conf (copy example if absent) -> extractors sanity -> python scaffold (map tree +
# FOUNDATION skeleton + seeded baseline + generated artifacts) -> gate template copied to
# GATE_FILE -> gate executed once (expect PASS on the freshly seeded tree).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)" || exit 2
# ROOT + KIT_REL, resolved LOGICALLY from the kit dir by walking up for `.codebase-map.conf` (an
# already-adopted root) or `.git` (the repo root this run will CREATE the conf at). This is
# deliberately NOT `git rev-parse --show-toplevel`: git answers with the PHYSICAL path, so a
# junctioned/symlinked kit dir resolves to the LINK TARGET's repo — and this script WRITES a conf, a
# whole map tree and a gate file. Measured before this was fixed: adoption landed in the kit's own
# source repository and still printed `Adopted.`. map_lib.resolve_root rejects git for the same
# reason and says so in its docstring; the two must agree, and both spellings here come from the one
# logical `pwd` above, which is also what the MSYS two-spellings problem actually needs.
#
# The conf-or-.git boundary is one step wider than resolve_root's, on purpose: before adoption there
# is no conf, so resolve_root would still answer `kit_dir.parent`. The adopter must reach the .git
# root because it is CREATING the marker resolve_root will find from then on.
ROOT=""; KIT_REL=""; _p="$HERE"
while : ; do
  _parent="$(dirname "$_p")"
  [ "$_parent" = "$_p" ] && break                       # filesystem root; no boundary found
  KIT_REL="$(basename "$_p")${KIT_REL:+/$KIT_REL}"
  if [ -f "$_parent/.codebase-map.conf" ] || [ -e "$_parent/.git" ]; then ROOT="$_parent"; break; fi
  _p="$_parent"
done
[ -n "$ROOT" ] || {
  echo "no repo root above $HERE — expected a .git or a .codebase-map.conf in some ancestor"; exit 2; }
# The operator's tree must BE the tree being adopted. Without this, running the adopter by path from
# another repo silently adopts the KIT's repo (measured: conf + map tree + gate written to a
# repository nobody named, exit 0). The pre-1.1 `-ef` check bound these together; it is restored
# here as an inode compare, because MSYS and symlinks spell one directory two ways.
_CWD_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$_CWD_ROOT" ] || {
  echo "not inside a git repository — cd into the repo you mean to adopt, then re-run"; exit 2; }
[ "$_CWD_ROOT" -ef "$ROOT" ] || {
  echo "refusing: this kit dir belongs to the repo at"
  echo "    $ROOT"
  echo "but you are standing in"
  echo "    $_CWD_ROOT"
  echo "This script WRITES (.codebase-map.conf, the map tree, the gate). Copy the kit INTO the repo"
  echo "you mean to adopt and run that copy, or cd into $ROOT first."
  exit 1; }
cd "$ROOT" || exit 2
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does
# not exist in an adopting repo. The block below is byte-identical to resolve-python.sh in gov's lib dir,
# and that dir's resolve-python.test.sh reds if any copy drifts.
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
        # The direct executable where the probe named a file, so a consumer never spawns the
        # Windows App Execution Alias again; the candidate's own name otherwise.
        _rp_exe=${_rp_out#* }
        if [ "$_rp_exe" != "$_rp_out" ] && [ -f "$_rp_exe" ]; then printf '%s\n' "$_rp_exe"; else printf '%s\n' "$_rp_c"; fi
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
    echo "resolve_python: tried:$_rp_tried"
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
  } >&2
  return 1
}
# <<< resolve_python
# MAP_PY is this kit's published override (named in its usage line below and in
# WIRE-INTO-PROJECT.md), so it is the first candidate. Its old bare-`python` default was the
# weakest of the three detectors: on a python3-only host it named a launcher that does not exist.
PY=$(resolve_python "${MAP_PY:-}") || exit 2

[ "${1:-}" = "--scaffold" ] || { echo "usage: $0 --scaffold   (MAP_PY=python3 to override the launcher)"; exit 2; }   # gov:literal-python — inside a usage string

# Only the kit dir's NAME is load-bearing (the gate template resolves the kit by it); the prefix is
# free. The kit must also be INSIDE the repo, not be the repo root itself.
[ -n "$KIT_REL" ] || {
  echo "the kit dir is the repo root itself ($ROOT) — copy the kit in as a directory named codebase-map/"; exit 1; }
case "$KIT_REL" in
  codebase-map|*/codebase-map) ;;
  *) echo "the kit dir must be NAMED codebase-map (found: $KIT_REL) — the gate template resolves it by that name; a one-segment prefix above it is fine"; exit 1;;
esac
# Depth check, BEFORE anything is written. `*/codebase-map` matches slashes, so the name check alone
# accepted <root>/a/b/codebase-map — which the gate template cannot resolve (it probes <ancestor>,
# <ancestor>/codebase-map and <ancestor>/*/codebase-map). Discovering that AFTER the conf, the whole
# map tree and the gate are on disk leaves a half-adopted repo and reports it as a gate failure,
# sending the operator hunting a coverage violation that does not exist. Advertise the real limit.
case "$KIT_REL" in
  */*/codebase-map)
    echo "install prefix is deeper than one segment: $KIT_REL"
    echo "the gate template resolves only <root>/codebase-map or <root>/<one-segment>/codebase-map."
    echo "Move the kit up, or keep it here and point GATE_FILE INSIDE the kit dir."
    exit 1;;
esac

# Stamp MAP_DIFF_CMD with THIS install's prefix so the value is right by construction rather than
# right if the operator remembers. NO `sed`: `&` in a replacement means "the whole match" and `\`
# starts an escape, so a kit under `R&D/` silently produced a mangled line that sed still exited 0
# on — and this script SOURCES that file below, so the corruption became executable. A `case`
# rewrite has no replacement grammar at all, keeps the line in place beside its comment, and drops
# sed's BSD/GNU `-i` divergence with it. The charset guard is belt-and-braces: a prefix that cannot
# be expressed in the conf's restricted grammar is declined, never half-written.
stamp_map_diff_cmd() {  # $1 = conf path; echoes nothing, returns 1 if it did not land
  case "$KIT_REL" in
    *[!A-Za-z0-9._/-]*) return 1;;
  esac
  _want="MAP_DIFF_CMD=\"python $KIT_REL/map_diff.py\""
  _hit=0
  while IFS= read -r _line || [ -n "$_line" ]; do
    case "$_line" in
      MAP_DIFF_CMD=*) printf '%s\n' "$_want"; _hit=1;;
      *) printf '%s\n' "$_line";;
    esac
  done < "$1" > "$1.new" || { rm -f "$1.new"; return 1; }
  [ "$_hit" = 1 ] || { rm -f "$1.new"; return 1; }
  mv "$1.new" "$1" || { rm -f "$1.new"; return 1; }
  # Claim nothing until it is READ BACK: a success message printed from the write path is exactly
  # the fail-open the DEAD PROBE doctrine bans.
  grep -qxF "$_want" "$1"
}

if [ ! -f "$ROOT/.codebase-map.conf" ]; then
  cp "$HERE/.codebase-map.conf.example" "$ROOT/.codebase-map.conf"
  if stamp_map_diff_cmd "$ROOT/.codebase-map.conf"; then
    echo "MAP_DIFF_CMD stamped for this install prefix: python $KIT_REL/map_diff.py"
  else
    echo "note: could NOT stamp MAP_DIFF_CMD — set it to \"python $KIT_REL/map_diff.py\" by hand."
  fi
  echo "created .codebase-map.conf from the example — EDIT IT (MAP_ROOT, GATE_FILE), then re-run."
  exit 1
fi
. "$ROOT/.codebase-map.conf"
# The stamp above only fires on the branch that CREATES the conf — but the kit README and
# WIRE-INTO-PROJECT both tell the operator to `cp` the example first, so on the DOCUMENTED path that
# branch never runs and the example's root-spelled map_diff path survives at a prefixed install.
# Measured: adoption reached `Adopted.` at exit 0 and the scaffolded map README shipped a digest
# command naming a file that does not exist. Validate the configured value on EVERY run: pull the
# `…/map_diff.py` token out of it and re-stamp when it does not resolve from the root. A value that
# resolves is left exactly as the operator wrote it (`uv run python …` and friends still work).
_MDC="$(printf '%s' "${MAP_DIFF_CMD:-}" | tr -d '\r')"
_MDC_PATH=""
for _tok in $_MDC; do
  case "$_tok" in *map_diff.py) _MDC_PATH="$_tok";; esac
done
if [ -z "$_MDC_PATH" ] || [ ! -f "$ROOT/$_MDC_PATH" ]; then
  if stamp_map_diff_cmd "$ROOT/.codebase-map.conf"; then
    echo "MAP_DIFF_CMD named ${_MDC_PATH:-no map_diff.py}, which does not resolve from $ROOT —"
    echo "  re-stamped for this install prefix: python $KIT_REL/map_diff.py"
    . "$ROOT/.codebase-map.conf"
  else
    echo "WARNING: MAP_DIFF_CMD names ${_MDC_PATH:-no map_diff.py}, which does not resolve from"
    echo "  $ROOT — the scaffolded map README will carry a dead path. Set it to"
    echo "  \"python $KIT_REL/map_diff.py\" by hand."
  fi
fi
# CR-strip: a CRLF-committed conf on Linux keeps \r in sourced values (MSYS masks this)
MAP_ROOT="$(printf '%s' "${MAP_ROOT:-}" | tr -d '\r')"
GATE_FILE="$(printf '%s' "${GATE_FILE:-}" | tr -d '\r')"

[ -f "$HERE/map_extractors.py" ] || {
  cp "$HERE/map_extractors.template.py" "$HERE/map_extractors.py"
  echo "created $KIT_REL/map_extractors.py from the template — declare your inventories"
  echo "(see $KIT_REL/INVENTORY-DERIVATION.md), then re-run."
  exit 1; }

# Idempotent: an already-scaffolded map reconverges via --write (re-renders generated/ so a bumped
# version marker lands) instead of the gen_map.py --scaffold refuse-if-present wedge on re-run.
if [ -f "${MAP_ROOT:-memory/map}/FOUNDATION.md" ]; then
  "$PY" "$HERE/gen_map.py" --write || exit 1
else
  "$PY" "$HERE/gen_map.py" --scaffold || exit 1
fi

# Seed the affordance grace list ONCE (seed-if-absent): a fresh scaffold gets `exempt = []`; a repo
# re-adopting from a pre-affordance kit version gets its existing dossiers graced — green by
# construction either way. NOT re-seeded when present: the list is shrink-only, so re-seeding a
# repo with a real (non-exempt) violation would mask it.
if [ ! -f "${MAP_ROOT:-memory/map}/affordance-exempt.toml" ]; then
  "$PY" "$HERE/gen_map.py" --seed-affordance-baseline || exit 1
fi

GATE="${GATE_FILE:-tests/test_codebase_map.py}"
if [ -f "$GATE" ]; then
  echo "gate already present at $GATE — left untouched"
else
  mkdir -p "$(dirname "$GATE")"
  cp "$HERE/test_codebase_map.template.py" "$GATE"
  echo "gate installed at $GATE"
fi

echo "--- running the gate once (standalone mode) ---"
"$PY" "$GATE" || { echo "gate FAILED on the freshly seeded tree — fix before committing"; exit 1; }

echo "Adopted. Next:"
echo "  1. git add $KIT_REL/ .codebase-map.conf $GATE ${MAP_ROOT:-memory/map}/ && commit."
echo "  2. Verify your test suite collects the gate (it now enforces on every run/CI)."
echo "  3. Add the map section to your kickoff manifest (see MANIFEST-TEMPLATE.md) and the"
echo "     DoD line to your governance doc/CLAUDE.md."
echo "  4. Claim as you touch: the baseline only shrinks."

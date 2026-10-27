#!/usr/bin/env bash
# adopt-process-monitor.sh — wire the process-monitor kit into a project.
#
# gov:kit process-monitor@0.20
#
# Run from anywhere INSIDE the target repo AFTER copying this kit dir in as `<prefix>/process-monitor/`.
# The kit dir's NAME is load-bearing; the one-segment prefix is free and every path below is DERIVED
# from it, so a root install still works.
#
#   <prefix>/process-monitor/adopt-process-monitor.sh           # grade the declaration
#   <prefix>/process-monitor/adopt-process-monitor.sh --check   # grade it again; REPAIRS NOTHING
#
# WHAT IT DOES NOT DO, said here because the header used to claim both: it does NOT create
# `.process-monitor.conf` (the roots are yours and a placeholder root is worse than none), and it
# does NOT write `.claude/settings.json`. It REPORTS whether the hook is wired; wiring it is
# `python <tool-root>/settings-merge.py --fragment <kit-dir>/procmon-hook.fragment.json`, and both
# halves are DERIVED below rather than spelled: this kit installs under whatever prefix the target
# chose, and a header naming `tools/` strands every adopter that chose another one.
#
# `--check` is the merge-bar arm and it is deliberately non-repairing, the same split
# `.unattended.conf` records for its own WIRING_CHECK: a repairing mode on a bar rewrites the thing
# it was asked to grade.
#
#   Exit 0 = adopted / wired · 1 = unwired or refused · 2 = wrong invocation or not a repo.
set -u

KIT_PROCESS_MONITOR_VERSION="0.20"   # gov:kit process-monitor@0.20 — the deployer's read (kit.toml version_from)

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

MODE=""
for _a in "${@:-}"; do
  case "$_a" in
    "") ;;
    --check) MODE="--check" ;;
    --version) echo "process-monitor $KIT_PROCESS_MONITOR_VERSION"; exit 0 ;;
    *) echo "usage: $0 [--check|--version]"; exit 2 ;;
  esac
done

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(unset GIT_DIR GIT_WORK_TREE; git -C "$KIT_DIR" rev-parse --show-toplevel 2>/dev/null)" || {
  echo "process-monitor: not a git repo" >&2; exit 2; }
# The kit's own directory, repo-relative and DERIVED. No literal prefix appears in this file: a
# `tools/` literal in shipped bytes resolves to nothing in an adopter installed elsewhere, and an
# empty derivation must REFUSE rather than silently mean the repo root.
#
# `--show-prefix` rather than stripping $ROOT off $KIT_DIR, and the reason is measured: on MSYS
# `git rev-parse --show-toplevel` answers `C:/projects/...` while `cd && pwd` answers
# `/c/projects/...`, so the prefix strip never matches and every invocation refused. Two spellings
# of one path is the bug class this whole kit exists to reason about; git is asked the question
# instead of two answers being compared.
KIT_REL="$(unset GIT_DIR GIT_WORK_TREE; cd "$KIT_DIR" && git rev-parse --show-prefix 2>/dev/null)"
KIT_REL="${KIT_REL%/}"
[ -n "$KIT_REL" ] || {
  echo "process-monitor: cannot derive this kit's directory relative to $ROOT" >&2; exit 2; }
PY=$(resolve_python "${GOV_PYTHON:-}" 2>/dev/null) || PY=""
# The tool root this kit was installed under — `tools` in gov, `scripts` at an adopter that chose
# that prefix, empty at a root install. DERIVED from KIT_REL, which is this kit's own directory
# relative to the repo root, because the remedy below names a SIBLING file and a hardcoded `tools/`
# there is an instruction pointing at a path the operator does not have. TOOL-cMendedVintage-4, whose
# own subject was that the remedy used to spell `$ROOT/tools/` and disagreed with the fragment paths
# two lines above it. ONE route, and that is load bearing: the 2026-09-21 reconcile kept both sides'
# derivation and they disagreed about the trailing slash, so anything inserted between them would
# have read a different value from anything after — with TOOL_ROOT="tools" the slash-less form
# renders `toolssettings-merge.py`. The separator is supplied HERE, by SMERGE_REL, and nowhere else.
TOOL_ROOT="${KIT_REL%/*}"; [ "$TOOL_ROOT" = "$KIT_REL" ] && TOOL_ROOT=""
SMERGE_REL="${TOOL_ROOT:+$TOOL_ROOT/}settings-merge.py"
CONF="$ROOT/.process-monitor.conf"
FAIL=0
print_note() { printf 'process-monitor: %s\n' "$1"; }
add_problem() { printf 'process-monitor: %s\n' "$1" >&2; FAIL=1; }

# ---------------------------------------------------------------- 1. the conf must exist
# REFUSED, never created. The roots are the adopter's own paths and this kit cannot guess them; a
# seeded conf with a placeholder root is worse than none, because it looks configured.
if [ ! -f "$CONF" ]; then
  add_problem ".process-monitor.conf is absent at $CONF — copy it from $KIT_REL/process-monitor.template.conf and declare PROCMON_ROOTS"
  exit 1
fi

# shellcheck disable=SC1090
PROCMON_ROOTS=""; PROCMON_AGE_CEILING=""; PROCMON_REAP_MODE=""; PROCMON_THROTTLE_S=""
. "$CONF"

# ---------------------------------------------------------------- 2. PROCMON_ROOTS is the hole
# BLANK IS A REFUSAL. An unconfigured monitor reports a clean tree it never examined, which is the
# green-by-absence class. This is the `[[hole]]` govkit declares, and its discharge probe is this
# exact test.
if [ -z "${PROCMON_ROOTS// /}" ]; then
  add_problem "PROCMON_ROOTS is blank — a blank roots list is a REFUSAL, not an empty set: the fence would match nothing and every report would read as a clean tree"
fi

# ---------------------------------------------------------------- 3. no root may claim everything
# Both directions of the containment test. A root of `/`, a drive root, or anything under the
# declared minimum length is refused: the failure mode of an over-broad root is that the reaper's
# blast radius becomes the whole machine.
# Compared case-folded with separators normalised, because one directory has three spellings.
build_normalized() { printf '%s' "$1" | tr 'A-Z\\' 'a-z/' | sed 's://*:/:g; s:/*$::'; }

MIN_ROOT_LEN=8
for _r in $PROCMON_ROOTS; do
  case "$_r" in
    /|//|[A-Za-z]:|[A-Za-z]:/|[A-Za-z]:\\)
      add_problem "PROCMON_ROOTS entry '$_r' is a filesystem root — it would admit every process on the machine" ;;
  esac
  if [ "${#_r}" -lt "$MIN_ROOT_LEN" ]; then
    add_problem "PROCMON_ROOTS entry '$_r' is shorter than $MIN_ROOT_LEN characters — too broad to be a declaration"
  fi
  # IT MUST BE A REAL DIRECTORY. Half of the split-root defect: `C:/Users/John Doe/proj` becomes
  # `C:/Users/John` plus `Doe/proj`, and the first is absolute and long enough.
  if [ ! -d "$_r" ]; then
    add_problem "PROCMON_ROOTS entry '$_r' is not a directory. If your path contains a SPACE, the declaration split it in two: a root may not contain whitespace, because both readers are whitespace-delimited"
  fi
  # AND IT MUST NOT BE A HOME-ADJACENT ANCESTOR. The `-d` test alone does NOT close the split-root
  # case, and the first fold claimed it did: `C:/Users` is absolute, is exactly MIN_ROOT_LEN, and IS
  # a directory, so `C:/Users/John Doe/x` splitting to `C:/Users` passes every test above. A root at
  # or above the users container, or equal to $HOME, admits every account on the machine.
  _rn=$(build_normalized "$_r")
  _hn=$(build_normalized "${HOME:-/nonexistent-home}")
  case "$_rn" in
    /users|/home|[a-z]:/users|[a-z]:/home|/|[a-z]:)
      add_problem "PROCMON_ROOTS entry '$_r' is the accounts container. It admits every user on this machine — and it is what a path with a SPACE in it collapses to" ;;
  esac
  if [ -n "$_hn" ] && [ "$_rn" = "$_hn" ]; then
    add_problem "PROCMON_ROOTS entry '$_r' is your HOME directory. Declare the repository, not the account"
  fi
  case "$_hn/" in
    "$_rn"/*) [ "$_rn" = "$_hn" ] || add_problem "PROCMON_ROOTS entry '$_r' is an ANCESTOR of your home directory, so it admits every process you own" ;;
  esac
done

# ---------------------------------------------------------------- 4. no root may be the temp root
# The measured rule. Every agent shell on a Windows box carries an `export TEMP=` assignment naming
# this directory, and mktemp resolves under it, so a root here admits every session on the machine.
_TMP_CANDIDATES="${TMPDIR:-} ${TMP:-} ${TEMP:-} /tmp"
for _r in $PROCMON_ROOTS; do
  _rn="$(build_normalized "$_r")"
  for _t in $_TMP_CANDIDATES; do
    [ -n "$_t" ] || continue
    _tn="$(build_normalized "$_t")"
    [ -n "$_tn" ] || continue
    # refuse the temp root itself AND any ancestor of it
    case "$_tn/" in
      "$_rn"/*) add_problem "PROCMON_ROOTS entry '$_r' is the system temp directory or an ancestor of it ('$_t') — that admits every agent session on this machine, in every repository" ;;
    esac
  done
done

# ---------------------------------------------------------------- 5. the closed value sets
case "${PROCMON_REAP_MODE:-}" in
  report|reap-orphans|reap-all) ;;
  "") add_problem "PROCMON_REAP_MODE is unset — it has no default here, because a defaulted kill policy is a policy nobody chose" ;;
  *)  add_problem "PROCMON_REAP_MODE='$PROCMON_REAP_MODE' is outside the closed set report|reap-orphans|reap-all" ;;
esac
case "${PROCMON_AGE_CEILING:-}" in
  ''|*[!0-9]*) add_problem "PROCMON_AGE_CEILING must be a whole number of seconds, got '${PROCMON_AGE_CEILING:-}'" ;;
esac
case "${PROCMON_THROTTLE_S:-}" in
  ''|*[!0-9]*) add_problem "PROCMON_THROTTLE_S must be a whole number of seconds, got '${PROCMON_THROTTLE_S:-}'" ;;
esac

# ---------------------------------------------------------------- 6. report
if [ "$FAIL" -ne 0 ]; then
  [ "$MODE" = "--check" ] && print_note "wiring NOT ok — the lines above name what is unmet"
  exit 1
fi

_roots_n=0; for _r in $PROCMON_ROOTS; do _roots_n=$((_roots_n + 1)); done
# ---------------------------------------------------------------- 6b. is the hook actually wired?
# The leg is named "process-monitor wiring" and until now it graded the CONF and nothing else, while
# printing "wiring ok". A leg whose name overstates what it checks is worse than no leg.
#
# PER EVENT, since TOOL-aReplayedCard-2. The hook is wired twice — the PostToolUse report and the
# SessionStart one — by two fragments, and a file-wide count of `procmon-hook` reads 2 for the
# right wiring AND for one event wired twice, so it could not tell an adopter which fragment they
# had not applied. Read without a JSON parser (this runs where no python may be): flattened, every
# `"<Key>":[` opens an event or a group's `hooks` array, so each line below is one array and the
# event it belongs to is the last non-`hooks` key seen.
measure_hook_entries() { # event -> how many procmon-hook commands sit under that event
  [ -f "$ROOT/.claude/settings.json" ] || { echo 0; return; }
  tr -d ' \t\r\n' < "$ROOT/.claude/settings.json" \
    | sed 's/"\([A-Za-z]*\)":\[/\n\1 /g' \
    | awk -v ev="$1" '$1 != "hooks" { cur = $1 } cur == ev { n += gsub(/procmon-hook/, "") } END { print n + 0 }'
}
_hook_post=$(measure_hook_entries PostToolUse); _hook_start=$(measure_hook_entries SessionStart)
case "$_hook_post" in ''|*[!0-9]*) _hook_post=0 ;; esac
case "$_hook_start" in ''|*[!0-9]*) _hook_start=0 ;; esac
_hook_n=$((_hook_post + _hook_start))

if [ "$MODE" = "--check" ]; then
  # IT DECIDES, it does not merely report. The first fold printed this and exited 0, which is the
  # could-not-fail shape on a leg whose NAME is "process-monitor wiring": an unwired kit reports
  # nothing to any session, and a green leg over that is worse than no leg. The file's own exit
  # contract at the top says 1 = unwired. Each event is decided on its own, and the remedy names
  # the fragment for the event that is missing — the merger takes one fragment per run.
  if [ "$_hook_post" -eq 0 ] || [ "$_hook_start" -eq 0 ]; then
    _missing=""
    [ "$_hook_post" -eq 0 ] && _missing="$_missing PostToolUse (--fragment $KIT_REL/procmon-hook.fragment.json)"
    [ "$_hook_start" -eq 0 ] && _missing="$_missing SessionStart (--fragment $KIT_REL/procmon-session.fragment.json)"
    add_problem "the engine is configured but the HOOK IS NOT WIRED for:$_missing — nothing will report a hung process on that event. Wire each with: $PY $SMERGE_REL <that --fragment>"
    print_note "wiring NOT ok — the hook is absent from .claude/settings.json for:$_missing"
    exit 1
  fi
  print_note "declaration ok — conf at .process-monitor.conf, $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s, hook entries PostToolUse $_hook_post, SessionStart $_hook_start"
  # ONE DECLARATION, ONE READER. This script SOURCES the conf; the engine parses it literally. Two
  # readers of one file is the class this repo gates against everywhere else, so the roots question
  # is delegated to the engine's own reader, which also gives `--check-conf` its first caller.
  if [ -f "$KIT_DIR/scope.py" ] && [ -n "$PY" ]; then
    # THE STATUS IS READ, NOT COLLAPSED INTO true/false. The engine separates a declaration fault
    # (1) from a well-formed declaration nothing live matches (3), and folding those back together
    # here is how a correctly installed kit gets rolled back for the time of day. `set -e` is not in
    # force, so capturing `$?` on the next line is the whole mechanism.
    PROCMON_ROOT="$ROOT" "$PY" "$KIT_DIR/scope.py" --check-conf >/dev/null 2>&1
    _scope_rc=$?
    case "$_scope_rc" in
      0) print_note "the engine's own reader agrees, and those roots admit live work on this machine" ;;
      3) print_note "SKIP: the engine's reader ACCEPTED this conf and nothing live matches those roots right now — the live-admission arm went UNEXERCISED, not passed. Re-run while this repo's own work is running: PROCMON_ROOT=\"$ROOT\" $PY $KIT_REL/scope.py --check-conf" ;;
      *) print_note "the engine's reader REFUSES this conf — run: PROCMON_ROOT=\"$ROOT\" $PY $KIT_REL/scope.py --check-conf"
         exit 1 ;;
    esac
  else
    print_note "NOT CHECKED: whether those roots admit this repo's own work — no engine or no runnable python here, so the declaration is all this can grade."
  fi
  exit 0
fi
print_note "adopted — $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s, hook entries $_hook_n (PostToolUse $_hook_post, SessionStart $_hook_start)"
print_note "next: $KIT_REL/adopt-process-monitor.sh --check"
exit 0

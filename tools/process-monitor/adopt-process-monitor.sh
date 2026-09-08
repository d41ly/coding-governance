#!/usr/bin/env bash
# adopt-process-monitor.sh — wire the process-monitor kit into a project.
#
# gov:kit process-monitor@0.1
#
# Run from anywhere INSIDE the target repo AFTER copying this kit dir in as `tools/process-monitor/`.
# The kit dir's NAME is load-bearing; the one-segment prefix is free and every path below is DERIVED
# from it, so a root install still works.
#
#   tools/process-monitor/adopt-process-monitor.sh           # grade the declaration
#   tools/process-monitor/adopt-process-monitor.sh --check   # grade it again; REPAIRS NOTHING
#
# WHAT IT DOES NOT DO, said here because the header used to claim both: it does NOT create
# `.process-monitor.conf` (the roots are yours and a placeholder root is worse than none), and it
# does NOT write `.claude/settings.json`. It REPORTS whether the hook is wired; wiring it is
# `python tools/settings-merge.py --fragment tools/process-monitor/procmon-hook.fragment.json`.
#
# `--check` is the merge-bar arm and it is deliberately non-repairing, the same split
# `.unattended.conf` records for its own WIRING_CHECK: a repairing mode on a bar rewrites the thing
# it was asked to grade.
#
#   Exit 0 = adopted / wired · 1 = unwired or refused · 2 = wrong invocation or not a repo.
set -u

KIT_PROCESS_MONITOR_VERSION="0.1"   # gov:kit process-monitor@0.1 — the deployer's read (kit.toml version_from)

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
ROOT="$(git -C "$KIT_DIR" rev-parse --show-toplevel 2>/dev/null)" || {
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
KIT_REL="$(cd "$KIT_DIR" && git rev-parse --show-prefix 2>/dev/null)"
KIT_REL="${KIT_REL%/}"
[ -n "$KIT_REL" ] || {
  echo "process-monitor: cannot derive this kit's directory relative to $ROOT" >&2; exit 2; }

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
MIN_ROOT_LEN=8
for _r in $PROCMON_ROOTS; do
  case "$_r" in
    /|//|[A-Za-z]:|[A-Za-z]:/|[A-Za-z]:\\)
      add_problem "PROCMON_ROOTS entry '$_r' is a filesystem root — it would admit every process on the machine" ;;
  esac
  if [ "${#_r}" -lt "$MIN_ROOT_LEN" ]; then
    add_problem "PROCMON_ROOTS entry '$_r' is shorter than $MIN_ROOT_LEN characters — too broad to be a declaration"
  fi
  # IT MUST BE A REAL DIRECTORY, and this is the half of the split-root defect no test over the
  # STRING can catch. `PROCMON_ROOTS` is whitespace-delimited, so `C:/Users/John Doe/proj` becomes
  # `C:/Users/John` plus `Doe/proj` — the first is absolute and long enough and would widen the
  # fence to the whole user profile. It is not a directory, and that is what refuses it.
  if [ ! -d "$_r" ]; then
    add_problem "PROCMON_ROOTS entry '$_r' is not a directory. If your path contains a SPACE, the declaration split it in two: a root may not contain whitespace, because both readers are whitespace-delimited"
  fi
done

# ---------------------------------------------------------------- 4. no root may be the temp root
# The measured rule. Every agent shell on a Windows box carries an `export TEMP=` assignment naming
# this directory, and mktemp resolves under it, so a root here admits every session on the machine.
# Compared case-folded with separators normalised, because one directory has three spellings.
build_normalized() { printf '%s' "$1" | tr 'A-Z\\' 'a-z/' | sed 's://*:/:g; s:/*$::'; }
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
_hook_n=0
if [ -f "$ROOT/.claude/settings.json" ]; then
  _hook_n=$(grep -c 'procmon-hook' "$ROOT/.claude/settings.json" 2>/dev/null || true)
fi
case "$_hook_n" in ''|*[!0-9]*) _hook_n=0 ;; esac

if [ "$MODE" = "--check" ]; then
  if [ "$_hook_n" -eq 0 ]; then
    print_note "the engine is configured but the HOOK IS NOT WIRED — nothing will report a hung process to a session. Wire it: python tools/settings-merge.py --fragment $KIT_REL/procmon-hook.fragment.json"
  fi
  print_note "declaration ok — conf at .process-monitor.conf, $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s, hook entries $_hook_n"
  # ONE DECLARATION, ONE READER. This script SOURCES the conf; the engine parses it literally. Two
  # readers of one file is the class this repo gates against everywhere else, so the roots question
  # is delegated to the engine's own reader, which also gives `--check-conf` its first caller.
  if [ -f "$KIT_DIR/scope.py" ] && command -v python >/dev/null 2>&1; then
    if PROCMON_ROOT="$ROOT" python "$KIT_DIR/scope.py" --check-conf >/dev/null 2>&1; then
      print_note "the engine's own reader agrees, and those roots admit live work on this machine"
    else
      print_note "the engine's reader REFUSES this conf, or its roots admit nothing live here — run: PROCMON_ROOT=\"$ROOT\" python $KIT_REL/scope.py --check-conf"
      exit 1
    fi
  else
    print_note "NOT CHECKED: whether those roots admit this repo's own work — the engine is not installed here, so the declaration is all this can grade."
  fi
  exit 0
fi
print_note "adopted — $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s, hook entries $_hook_n"
print_note "next: $KIT_REL/adopt-process-monitor.sh --check"
exit 0

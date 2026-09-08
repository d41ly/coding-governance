#!/usr/bin/env bash
# adopt-process-monitor.sh — wire the process-monitor kit into a project.
#
# gov:kit process-monitor@0.1
#
# Run from anywhere INSIDE the target repo AFTER copying this kit dir in as `tools/process-monitor/`.
# The kit dir's NAME is load-bearing; the one-segment prefix is free and every path below is DERIVED
# from it, so a root install still works.
#
#   tools/process-monitor/adopt-process-monitor.sh           # seed .process-monitor.conf, wire hooks
#   tools/process-monitor/adopt-process-monitor.sh --check   # verify wiring; REPAIRS NOTHING
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
say() { printf 'process-monitor: %s\n' "$1"; }
bad() { printf 'process-monitor: %s\n' "$1" >&2; FAIL=1; }

# ---------------------------------------------------------------- 1. the conf must exist
# REFUSED, never created. The roots are the adopter's own paths and this kit cannot guess them; a
# seeded conf with a placeholder root is worse than none, because it looks configured.
if [ ! -f "$CONF" ]; then
  bad ".process-monitor.conf is absent at $CONF — copy it from $KIT_REL/process-monitor.conf.template and declare PROCMON_ROOTS"
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
  bad "PROCMON_ROOTS is blank — a blank roots list is a REFUSAL, not an empty set: the fence would match nothing and every report would read as a clean tree"
fi

# ---------------------------------------------------------------- 3. no root may claim everything
# Both directions of the containment test. A root of `/`, a drive root, or anything under the
# declared minimum length is refused: the failure mode of an over-broad root is that the reaper's
# blast radius becomes the whole machine.
MIN_ROOT_LEN=8
for _r in $PROCMON_ROOTS; do
  case "$_r" in
    /|//|[A-Za-z]:|[A-Za-z]:/|[A-Za-z]:\\)
      bad "PROCMON_ROOTS entry '$_r' is a filesystem root — it would admit every process on the machine" ;;
  esac
  if [ "${#_r}" -lt "$MIN_ROOT_LEN" ]; then
    bad "PROCMON_ROOTS entry '$_r' is shorter than $MIN_ROOT_LEN characters — too broad to be a declaration"
  fi
done

# ---------------------------------------------------------------- 4. no root may be the temp root
# The measured rule. Every agent shell on a Windows box carries an `export TEMP=` assignment naming
# this directory, and mktemp resolves under it, so a root here admits every session on the machine.
# Compared case-folded with separators normalised, because one directory has three spellings.
_norm() { printf '%s' "$1" | tr 'A-Z\\' 'a-z/' | sed 's://*:/:g; s:/*$::'; }
_TMP_CANDIDATES="${TMPDIR:-} ${TMP:-} ${TEMP:-} /tmp"
for _r in $PROCMON_ROOTS; do
  _rn="$(_norm "$_r")"
  for _t in $_TMP_CANDIDATES; do
    [ -n "$_t" ] || continue
    _tn="$(_norm "$_t")"
    [ -n "$_tn" ] || continue
    # refuse the temp root itself AND any ancestor of it
    case "$_tn/" in
      "$_rn"/*) bad "PROCMON_ROOTS entry '$_r' is the system temp directory or an ancestor of it ('$_t') — that admits every agent session on this machine, in every repository" ;;
    esac
  done
done

# ---------------------------------------------------------------- 5. the closed value sets
case "${PROCMON_REAP_MODE:-}" in
  report|reap-orphans|reap-all) ;;
  "") bad "PROCMON_REAP_MODE is unset — it has no default here, because a defaulted kill policy is a policy nobody chose" ;;
  *)  bad "PROCMON_REAP_MODE='$PROCMON_REAP_MODE' is outside the closed set report|reap-orphans|reap-all" ;;
esac
case "${PROCMON_AGE_CEILING:-}" in
  ''|*[!0-9]*) bad "PROCMON_AGE_CEILING must be a whole number of seconds, got '${PROCMON_AGE_CEILING:-}'" ;;
esac
case "${PROCMON_THROTTLE_S:-}" in
  ''|*[!0-9]*) bad "PROCMON_THROTTLE_S must be a whole number of seconds, got '${PROCMON_THROTTLE_S:-}'" ;;
esac

# ---------------------------------------------------------------- 6. report
if [ "$FAIL" -ne 0 ]; then
  [ "$MODE" = "--check" ] && say "wiring NOT ok — the lines above name what is unmet"
  exit 1
fi

_roots_n=0; for _r in $PROCMON_ROOTS; do _roots_n=$((_roots_n + 1)); done
if [ "$MODE" = "--check" ]; then
  say "wiring ok — conf at .process-monitor.conf, $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s"
  say "NOT CHECKED HERE: whether those roots actually admit this repo's own work. That needs a census and a closure, so it is the scope unit's own arm; this script grades the DECLARATION only."
  exit 0
fi
say "adopted — $_roots_n declared root(s), mode $PROCMON_REAP_MODE, ceiling ${PROCMON_AGE_CEILING}s"
say "next: $KIT_REL/adopt-process-monitor.sh --check"
exit 0

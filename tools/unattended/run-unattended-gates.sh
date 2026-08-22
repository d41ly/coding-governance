#!/usr/bin/env bash
# run-unattended-gates.sh — this kit's SELF-TESTS, run on demand and nowhere else.
#
# THE SPLIT, which is the whole point of this file. Two kinds of check live in this directory and they
# have different subjects:
#
#   * the RECORD AND WIRING checks read the REPOSITORY — run-state records, the shipped skill's
#     wiring. They can go stale without anyone editing this kit, so they stay merge-bar legs:
#     `unattended kit gate`, `playbook validity gate`, `unattended skill wiring`. Nothing here
#     replaces them and they are listed below only so one command answers for the whole kit.
#   * the SELF-TESTS read THIS KIT. Each stages a break into a copy of a checker and asserts the
#     checker still catches it. Their subject is the checker, so they have a job only when the source
#     under this directory changes — and none at all in an adopter's repo that copy-installs the kit
#     and never edits it. Owner ruling, 2026-08-23: they run when the owner asks, never on the bar,
#     in this repo and in every adopter alike.
#
# MEASURED BEFORE THE RULING, node d, 2026-08-23: as bar legs the self-tests cost 3339 s of a 4926 s
# bar — 68% of all leg-seconds — and the largest put a 26-minute FLOOR under every full run, because
# wall clock cannot fall below the longest leg however wide the pool is. The record is
# memory/builds/dScriptedRepeat/build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md.
#
# WHAT IS THEREFORE NOT COVERED, said plainly because an exemption is not coverage (charter §7):
# nothing runs the self-tests automatically. A change under this directory that guts a check lands
# green. The compensating check is a person invoking this script, and the DoD for any work touching
# `tools/unattended/` is a GREEN verdict from `--selftests` pasted into the landing report.
#
# WHAT THIS DOES NOT CHECK: whether an unattended run was HONEST. These read records and stage
# fixtures; §9 of the protocol says what a check running under the run's own uid can and cannot buy,
# and that limit is unchanged by how this script is invoked.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "run-unattended-gates: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2

ONLY="${1:---selftests}"
case "$ONLY" in
  --all)       ONLY="" ;;
  --checks)    ONLY=checks ;;
  --selftests) ONLY=selftests ;;
  -h|--help)
    echo "usage: bash tools/unattended/run-unattended-gates.sh [--selftests|--checks|--all]"
    echo "  --selftests  the five suites that stage breaks into this kit (default), and the only"
    echo "               thing that exercises them since none is a bar leg."
    echo "               BUDGET ~60 MINUTES, measured node d 2026-08-23: the gate selftest alone is"
    echo "               ~38 min because it re-runs a 28-check leg once per arm. Do NOT wrap this in"
    echo "               a timeout under an hour - a killed suite prints no PASS and no FAIL, and"
    echo "               greping for a verdict then reads a kill as silence. This script reads the"
    echo "               EXIT CODE for that reason."
    echo "  --checks     the three record/wiring checks - about 35 s, and ALSO merge-bar legs"
    echo "  --all        both"
    echo ""
    echo "The suites are run UNSHARDED on purpose. Each carries its own note that a --shard run is"
    echo "evidence about its region and nothing else, so the whole-suite claim exists only here."
    exit 0 ;;
  *) echo "run-unattended-gates: unknown argument '$ONLY'"; exit 2 ;;
esac

st=0
ran=0
run_one() { # label · kind · argv...
  local label=$1 kind=$2; shift 2
  case "$ONLY" in ''|"$kind") ;; *) return 0 ;; esac
  ran=$((ran + 1))
  local s e out rc
  s=$(date +%s)
  out=$("$@" 2>&1); rc=$?
  e=$(date +%s)
  if [ "$rc" -eq 0 ]; then
    printf 'ok    %-30s %5ss  %s\n' "$label" "$((e - s))" "$(printf '%s\n' "$out" | grep -E '^PASS' | tail -1)"
  else
    st=1
    printf 'FAIL  %-30s %5ss  (exit %s)\n' "$label" "$((e - s))" "$rc"
    printf '%s\n' "$out" | grep -E '^FAIL|FAILED' | head -6 | sed 's/^/        /'
  fi
}

run_one "kit gate"                  checks bash "$HERE/check-unattended.sh"
run_one "playbook validity gate"    checks bash "$HERE/check-playbook.sh"
run_one "skill wiring"              checks bash "$HERE/adopt-unattended.sh" --check

run_one "gate selftest"             selftests bash "$HERE/check-unattended.test.sh"
run_one "driver selftest"           selftests bash "$HERE/unattended.test.sh"
run_one "playbook validity selftest" selftests bash "$HERE/check-playbook.test.sh"
run_one "cross-component"           selftests bash "$HERE/cross-component.test.sh"
run_one "adopter e2e"               selftests bash "$HERE/adopt-unattended.test.sh"

# LIVENESS. A run that executed nothing must not print a green line: an unknown filter and a clean
# sweep are indistinguishable from the outside, which is the class this kit has spent six review
# rounds on.
if [ "$ran" -eq 0 ]; then
  echo "run-unattended-gates: no check matched the filter, so this run graded nothing at all"
  exit 2
fi
echo "----"
if [ "$st" -eq 0 ]; then
  echo "unattended gates GREEN — $ran ran on demand; no self-test here runs on the merge bar"
else
  echo "unattended gates RED — $ran ran on demand"
fi
exit "$st"

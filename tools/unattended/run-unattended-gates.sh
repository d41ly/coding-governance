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

# ---- THE BUDGET, AND IT IS A VERDICT RATHER THAN A COMPLAINT. A check nobody can afford to run is a
# ---- check nobody runs, and this kit proved it: its suites were pulled off the merge bar for costing
# ---- 68% of it, and the compensating check that replaced them then took an hour, so it was re-run
# ---- across two days and repeatedly abandoned. Slowness that only annoys never gets fixed. Slowness
# ---- that REDS gets either fixed or re-declared with a reason, and both of those are progress.
# ----
# ---- These are CEILINGS in seconds, generous against the 2026-08-23 readings on node d and paired
# ---- with them so a raise is visibly a raise. Raising one is fine; raising one silently is not, which
# ---- is the same rule this repo applies to every other pin it owns.
BUDGET_kit_gate=120           # measured 28 s
BUDGET_playbook_validity_gate=120   # measured 13 s
BUDGET_skill_wiring=60        # measured 0 s
BUDGET_gate_selftest=1800     # derived 1342 s after TOOL-dScriptedRepeat-15 — see the note below
BUDGET_driver_selftest=900    # measured 841 s
BUDGET_playbook_validity_selftest=300  # measured 140 s
BUDGET_cross_component=300    # measured 92 s
BUDGET_adopter_e2e=120        # measured 7 s

ONLY="${1:---selftests}"
case "$ONLY" in
  --all)       ONLY="" ;;
  --checks)    ONLY=checks ;;
  --selftests) ONLY=selftests ;;
  -h|--help)
    echo "usage: bash tools/unattended/run-unattended-gates.sh [--selftests|--checks|--all]"
    echo "  --selftests  the five suites that stage breaks into this kit (default), and the only"
    echo "               thing that exercises them since none is a bar leg."
    # THE BUDGET IS DERIVED, NEVER TYPED. Round 7's low 2: this help text quoted ~60 minutes beside a
    # ceiling this same unit had just re-declared, in the same file - a value stated in prose beside
    # the source that owns it, broken inside the file that owns it. The sum below is the declarations.
    # ---- SUMMED OVER THE DECLARED SET, never over a hand-typed list of names. Round 8's low 4: the
    # ---- first cut derived the number but spelled five of the eight `BUDGET_*` identifiers by hand,
    # ---- so a ninth suite would have been silently outside the figure - a hand-kept inventory of a
    # ---- machine-enumerable set, which is the class this repo gates elsewhere.
    _bsum=0; for _bk in ${!BUDGET_@}; do _bsum=$(( _bsum + ${!_bk} )); done
    echo "               Budget: every BUDGET_* ceiling this file declares, summed - currently"
    echo "               $(( (_bsum + 59) / 60 )) minutes, dominated by the gate selftest. Do NOT wrap this"
    echo "               in a timeout below that - a killed suite prints no PASS and no FAIL, and"
    echo "               greping for a verdict then reads a kill as silence. This script reads the"
    echo "               EXIT CODE for that reason."
    echo "  --checks     the three record/wiring checks, which are ALSO merge-bar legs. Their own"
    echo "               ceilings are in the same BUDGET_* block; no wall figure is typed here,"
    echo "               because the one that was is what round 8 filed."
    echo "  --all        both"
    echo ""
    echo "The suites are run UNSHARDED on purpose. Each carries its own note that a --shard run is"
    echo "evidence about its region and nothing else, so the whole-suite claim exists only here."
    exit 0 ;;
  *) echo "run-unattended-gates: unknown argument '$ONLY'"; exit 2 ;;
esac

#
# THE GATE SELFTEST'S CEILING WAS RE-DECLARED RATHER THAN MET, which TOOL-dScriptedRepeat-15's own
# spec named as one of its two acceptable outcomes, and this note is the reason beside the number.
#
# WHAT THE COST ACTUALLY IS, measured on node d 2026-08-23 rather than reasoned about. The leg is not
# compute-bound and never was: one invocation inside the suite's own fixture reported `real 14.4s
# user 0.33s sys 0.62s`, so 93% of it is spent waiting rather than working. What it waits on is
# PROCESS CREATION - an on-access antivirus scanner sits in front of every exec on this node, and one
# spawn costs 0.019-0.039 s here against roughly a millisecond on a machine without one. The leg made
# 469 of them per invocation and the suite invokes it 243 times, so the suite's real unit of cost is
# about 114,000 process creations. 469 x 0.022 s = 10.3 s against a 10.7 s measured invocation, which
# is the whole of it.
#
# WHAT THE UNIT DID: cut the spawns, which is the only term in that product this repo owns. Three
# loops that ran a grep or a `bash -c` per (item, file) now read each file once - 469 spawns per
# invocation became 220, counted both ways from an execution trace rather than estimated. The suite's
# last recorded sharded pair was 846.0 + 2013.7 = 2859.7 s; scaled by 220/469 that is 1342 s, and
# 243 x 5.2 s + fixture overhead lands in the same place from the other direction.
#
# WHY 1800 AND NOT 1342: the same reading taken under ambient load on this node ran 2.4x slower, and a
# ceiling that reds on someone else's antivirus scan is a ceiling that gets ignored. 1800 has headroom
# for that and still reds long before the 3200 s this suite used to cost.
#
# WHAT IS NOT OBSERVED, said plainly: nobody has run the suite end to end at this commit. The owner
# stopped these suites after two days of re-runs and the instruction stands, so the 1342 s is DERIVED
# from a spawn count and a per-spawn cost, both measured, and not from a stopwatch on the whole thing.
# The equivalence that replaces it is 19 staged breaks, 18 of them red, whose output and exit status
# are byte-identical before and after the unit. To settle it, one command:
#   bash tools/unattended/run-unattended-gates.sh --selftests

st=0
ran=0
over=0
run_one() { # label · kind · argv...
  local label=$1 kind=$2; shift 2
  case "$ONLY" in ''|"$kind") ;; *) return 0 ;; esac
  ran=$((ran + 1))
  local s e out rc took bkey budget
  s=$(date +%s)
  out=$("$@" 2>&1); rc=$?
  e=$(date +%s)
  took=$((e - s))
  bkey="BUDGET_$(printf '%s' "$label" | tr ' -' '__')"
  eval "budget=\${$bkey:-}"
  if [ "$rc" -eq 0 ]; then
    printf 'ok    %-30s %5ss  %s\n' "$label" "$took" "$(printf '%s\n' "$out" | grep -E '^PASS' | tail -1)"
  else
    st=1
    printf 'FAIL  %-30s %5ss  (exit %s)\n' "$label" "$took" "$rc"
    printf '%s\n' "$out" | grep -E '^FAIL|FAILED' | head -6 | sed 's/^/        /'
  fi
  # A MISSING BUDGET IS ITSELF A FAILURE. A suite added here without one would be exempt from the rule
  # by the act of arriving, which is how every population in this repo has previously gone quiet.
  if [ -z "$budget" ]; then
    st=1; over=$((over + 1))
    printf '      OVER BUDGET  %s declares no ceiling, so its cost is unbounded by construction\n' "$label"
  elif [ "$took" -gt "$budget" ]; then
    st=1; over=$((over + 1))
    printf '      OVER BUDGET  %s took %ss against a declared %ss ceiling — fix it or raise the ceiling with a reason beside it\n' "$label" "$took" "$budget"
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
elif [ "$over" -gt 0 ]; then
  echo "unattended gates RED — $ran ran on demand, $over over budget"
else
  echo "unattended gates RED — $ran ran on demand"
fi
exit "$st"

#!/usr/bin/env bash
# run-selftests.sh — the self-tests, ON DEMAND, and a cost verdict for each. TOOL-aQuenchedHarness-4.
#
# THE SPLIT THIS RESTS ON, owner ruling 2026-08-23. Two kinds of check live in this repo's kits and
# they have different subjects. A RECORD-OR-WIRING check reads the REPOSITORY and can go stale with
# nobody editing a kit, so it stays a merge-bar leg. A SELF-TEST reads the KIT — it stages a break
# into a copy of a checker and asserts the checker still catches it — so it has a job only when the
# source under that kit changes, and none at all in a tree that copy-installs the kit and never edits
# it. `tools/unattended/run-unattended-gates.sh` took that ruling for ONE kit. This is the same thing
# for every kit, which is what the ruling always implied and nobody had built.
#
# WHAT IS THEREFORE NOT COVERED, said plainly because an exemption is not coverage (charter §7):
# nothing runs these automatically. A change under a kit that guts a check lands green. The
# compensating check is a person invoking this script, and the Definition of Done for any work
# touching a kit is a GREEN verdict from it pasted into the landing report.
#
# AND THE COST OF THAT, said just as plainly, because it is the argument for units 5 and 6 rather
# than an aside: the declared budgets sum to about ELEVEN AND A HALF HOURS of leg-seconds. Nobody
# runs an eleven-hour check, which is why `TOOL-aQuenchedHarness-9` exists — `govkit selftest` sat
# with two arms red for long enough that nobody can say when they broke.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null) || {
  echo "run-selftests: not a git work tree"; exit 2; }
cd "$ROOT" || exit 2

BUDGETS="$HERE/selftest-budgets.txt"
LEGS="${GATE_LEGS:-$ROOT/tools/gate-legs.json}"
PYBIN=$(command -v python3 || command -v python) || { echo "run-selftests: no python"; exit 2; }

print_usage() {
  cat <<'USAGE'
usage: bash tools/run-gates/run-selftests.sh [--kit <dir>] [--check] [--list]
  (no flag)   run the declared population, time each suite, RED on a breach
  --kit <dir> only the suites whose argv lies under <dir>; a filter matching
              nothing is a REFUSAL, because an unknown filter and a clean sweep
              are indistinguishable from outside
  --check     the gate: assert the declaration against tools/gate-legs.json in
              BOTH directions, run nothing
  --list      print the population and the derived total, run nothing
USAGE
}

MODE=run; FILTER=""
while [ $# -gt 0 ]; do
  case "$1" in
    --kit)   FILTER=${2:-}; shift 2 ;;
    --check) MODE=check; shift ;;
    --list)  MODE=list; shift ;;
    -h|--help) print_usage; exit 0 ;;
    *) echo "run-selftests: unknown argument '$1'"; print_usage; exit 2 ;;
  esac
done

[ -f "$BUDGETS" ] || { echo "run-selftests: no declaration at $BUDGETS"; exit 2; }

# ---- the declaration, read once. Fields: name, budget, argv (empty = from the manifest), reading.
# ---- A row whose argv is empty takes it from `tools/gate-legs.json`, so the manifest stays the one
# ---- place a held leg's command is written and this file carries only what the manifest cannot.
read_population() {
  "$PYBIN" - "$BUDGETS" "$LEGS" "$FILTER" <<'PY'
import json, sys
budgets, legs_path, filt = sys.argv[1], sys.argv[2], sys.argv[3]
legs = {l["name"]: l for l in json.load(open(legs_path, encoding="utf-8"))}
for line in open(budgets, encoding="utf-8"):
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    f = line.rstrip("\n").split("\t")
    if len(f) < 2:
        continue
    name, budget, argv = f[0], f[1], (f[2] if len(f) > 2 else "")
    if not argv:
        leg = legs.get(name)
        if not leg:
            print("\t".join([name, budget, "", "UNRESOLVED"]))
            continue
        argv = " ".join(leg.get("argv", []))
    if filt and filt not in argv:
        continue
    print("\t".join([name, budget, argv, "ok"]))
PY
}

# ---- THE WIDTH IS RESOLVED ONCE, BY THE BAR'S OWN RESOLVER. Detection, the profile table, the clamp
# ---- and the GATE_JOBS override are 200 lines inside `run-gates.sh`; re-implementing them here is
# ---- the two-spellings drift this repo gates elsewhere. `--print-profile` exits before the
# ---- turnstile, so asking costs nothing and takes no beacon.
W=$(bash "$HERE/run-gates.sh" --print-profile 2>/dev/null | awk -F'\t' '$1=="width"{print $2}')
case "${W:-}" in ''|*[!0-9]*) W=2 ;; esac
# THE COMPOSITE BOUND. A spec audit caught this unit and the harness unit each reading the same
# declared width, which at width 8 is 8 suites x 8 arms = 64 concurrent processes on a host where a
# bare spawn costs 319 ms — during exactly the sweep this exists to make affordable. The outer pool
# takes at most 4 and EXPORTS what is left, so the product never exceeds the row's declared width.
OUTER=$(( W < 4 ? W : 4 )); [ "$OUTER" -ge 1 ] || OUTER=1
export SELFTEST_INNER_WIDTH=$(( W / OUTER )); [ "$SELFTEST_INNER_WIDTH" -ge 1 ] || SELFTEST_INNER_WIDTH=1

POP=$(read_population)
NROWS=$(printf '%s' "$POP" | grep -c . || true)

# ---- --check: the gate. BOTH DIRECTIONS, because one alone cannot fail usefully -----------------
if [ "$MODE" = check ]; then
  fails=0
  # FORWARD: every leg the bar holds carries a row. A suite that arrives without one would be exempt
  # from the budget rule by the act of arriving.
  missing=$("$PYBIN" - "$BUDGETS" "$LEGS" <<'PY'
import json, sys
declared = set()
for line in open(sys.argv[1], encoding="utf-8"):
    if line.strip() and not line.lstrip().startswith("#"):
        declared.add(line.split("\t")[0])
for l in json.load(open(sys.argv[2], encoding="utf-8")):
    if (l.get("subject") == "kit" or l.get("chunk") == "selftests") and l["name"] not in declared:
        print(l["name"])
PY
)
  if [ -n "$missing" ]; then
    echo "run-selftests: these HELD legs carry no budget row, so their cost is unbounded by declaration:" >&2
    # QUOTED, and printed line-wise: a leg name has spaces in it, so an unquoted $missing
    # word-splits and reports `agent-cap self-test` as two missing legs.
    printf '%s\n' "$missing" | sed 's/^/  /' >&2
    fails=1
  fi
  # REVERSE: a row that is not a held leg must name a TRACKED file, or the declaration is a way to
  # name a suite that does not exist — and a population nobody can execute grades nothing.
  while IFS=$'\t' read -r name budget argv state; do
    [ -n "${name:-}" ] || continue
    if [ "$state" = UNRESOLVED ]; then
      echo "run-selftests: row '$name' has no argv and no leg of that name in the manifest" >&2
      fails=1; continue
    fi
    for tok in $argv; do
      case "$tok" in
        */*) git ls-files --error-unmatch -- "$tok" >/dev/null 2>&1 \
               || { echo "run-selftests: row '$name' names '$tok', which git does not track" >&2; fails=1; } ;;
      esac
    done
  done <<EOF
$POP
EOF
  [ "$NROWS" -gt 0 ] || { echo "run-selftests: the declaration is EMPTY, so both directions above passed by finding nothing" >&2; fails=1; }
  [ "$fails" = 0 ] && echo "run-selftests: declaration clean — $NROWS row(s), every held leg budgeted, every row resolvable"
  exit "$fails"
fi

# ---- the derived total. NEVER typed: a figure beside the declarations that own it goes stale on the
# ---- next edit and nobody notices.
TOTAL=$(printf '%s' "$POP" | awk -F'\t' '{s+=$2} END{print s+0}')
if [ "$MODE" = list ]; then
  printf '%s\n' "$POP" | awk -F'\t' '{printf "  %-46s %6ss  %s\n", $1, $2, $3}'
  printf 'run-selftests: %s row(s), declared total %ss (%s minutes) at width %s (outer %s, inner %s)\n' \
    "$NROWS" "$TOTAL" "$(( (TOTAL + 59) / 60 ))" "$W" "$OUTER" "$SELFTEST_INNER_WIDTH"
  exit 0
fi

# ---- LIVENESS. A run that executed nothing must not print a green line: an unknown filter and a
# ---- clean sweep are indistinguishable from the outside, which is the class this kit's sibling
# ---- spent six review rounds on.
if [ "$NROWS" -eq 0 ]; then
  echo "run-selftests: no suite matched${FILTER:+ --kit $FILTER}, so this run graded NOTHING at all" >&2
  exit 2
fi

echo "run-selftests: $NROWS suite(s), declared total $(( (TOTAL + 59) / 60 )) minutes, width $W (outer $OUTER, inner $SELFTEST_INNER_WIDTH)"
st=0; ran=0; over=0
while IFS=$'\t' read -r name budget argv state; do
  [ -n "${name:-}" ] || continue
  ran=$((ran + 1))
  s=$(date +%s)
  out=$(eval "$argv" 2>&1); rc=$?
  e=$(date +%s); took=$(( e - s ))
  if [ "$rc" -eq 0 ]; then
    printf 'ok    %-46s %5ss\n' "$name" "$took"
  else
    st=1
    printf 'FAIL  %-46s %5ss  (exit %s)\n' "$name" "$took" "$rc"
    printf '%s\n' "$out" | grep -E '^(FAIL|nope|.*FAILED)' | head -4 | sed 's/^/        /'
  fi
  if [ "$took" -gt "$budget" ]; then
    st=1; over=$((over + 1))
    printf '      OVER BUDGET  %s took %ss against a declared %ss — fix it, or re-declare it with a reason beside the number\n' "$name" "$took" "$budget"
  fi
done <<EOF
$POP
EOF

echo "----"
if [ "$st" -eq 0 ]; then
  echo "self-tests GREEN — $ran ran on demand; none of them runs on the merge bar"
elif [ "$over" -gt 0 ]; then
  echo "self-tests RED — $ran ran on demand, $over over budget"
else
  echo "self-tests RED — $ran ran on demand"
fi
exit "$st"

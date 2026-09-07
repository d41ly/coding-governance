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
# than an aside: the declared budgets sum to more leg-seconds than anyone will sit through, and
# `--list` prints the figure rather than this comment carrying one -- a number typed beside the
# declarations that own it is the defect this same file names sixty lines down, and it had
# already gone 30% stale before the closing review caught it. Nobody runs a check measured in
# hours, which is why `TOOL-aQuenchedHarness-9` exists — `govkit selftest` sat
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
  --rank      rank the population by its RECORDED seconds and mark the set that
              carries the declared majority share; REFUSES if any row's reading
              states no condition, because ranking two conditions together ranks
              the conditions
USAGE
}

MODE=run; FILTER=""
while [ $# -gt 0 ]; do
  case "$1" in
    --kit)   FILTER=${2:-}; shift 2 ;;
    --check) MODE=check; shift ;;
    --list)  MODE=list; shift ;;
    --rank)  MODE=rank; shift ;;
    -h|--help) print_usage; exit 0 ;;
    *) echo "run-selftests: unknown argument '$1'"; print_usage; exit 2 ;;
  esac
done

[ -f "$BUDGETS" ] || { echo "run-selftests: no declaration at $BUDGETS"; exit 2; }

# ---- --rank: which suites carry the cost, and therefore which are worth rebuilding -------------
# ---- It runs BEFORE the width resolution below, because ranking is a read of a text file and has
# ---- no business paying for a profile probe.
if [ "$MODE" = rank ]; then
  "$PYBIN" - "$BUDGETS" <<'PY'
import re, sys

# THE CONDITION VOCABULARY IS CLOSED, and that is the whole point of this verb. Spec 6 S3a: the
# readings in this file come from two sources under two conditions — retained `gate-run` windows for
# a held leg, and a direct timed invocation for a suite with no manifest row — so sorting them
# together ranks the CONDITIONS as much as the suites. A phrasing not listed here is not ranked
# leniently; it is reported as unbacked. Adding one is a deliberate edit, which is the point.
CONDS = [
    (re.compile(r"worst of (\d+) readings (\d+)s"),
     lambda m: (int(m.group(2)), "worst of %s gate-run windows" % m.group(1))),
    (re.compile(r"measured (\d+)s (?:on )?(.+?)(?:,|$)"),
     lambda m: (int(m.group(1)), "direct, %s" % m.group(2).strip())),
]

share = factor = None
rows, unbacked = [], []
for line in open(sys.argv[1], encoding="utf-8"):
    s = line.strip()
    if s.startswith("#"):
        m = re.match(r"#\s*port-majority-share:\s*([0-9.]+)", s)
        if m:
            share = float(m.group(1))
        m = re.match(r"#\s*port-minimum-factor:\s*([0-9.]+)", s)
        if m:
            factor = float(m.group(1))
        continue
    if not s:
        continue
    f = line.rstrip("\r\n").split("\t")
    if len(f) < 2:
        continue
    name, reading = f[0], (f[3] if len(f) > 3 else "")
    for rx, take in CONDS:
        m = rx.search(reading)
        if m:
            secs, cond = take(m)
            rows.append((secs, cond, name))
            break
    else:
        unbacked.append((name, reading))

# A THRESHOLD THAT IS NOT DECLARED IS NOT A THRESHOLD. Defaulting it here would let the file lose its
# declaration and the ranking carry on reporting a selected set against a number nobody wrote.
missing = [k for k, v in (("port-majority-share", share), ("port-minimum-factor", factor)) if v is None]
if missing:
    print("run-selftests: the declaration states no " + " and no ".join(missing) + ", so a selected")
    print("run-selftests: set could not be computed against anything. Declare them in the header of")
    print("run-selftests: %s beside the reading each was taken from." % sys.argv[1])
    raise SystemExit(1)

if unbacked:
    print("run-selftests: these row(s) carry no reading whose CONDITION this verb recognises, so they")
    print("run-selftests: cannot be ranked against rows that do — and a denominator missing its")
    print("run-selftests: largest members is not a majority of anything. NO share was computed.")
    for name, reading in unbacked:
        print("  %-46s %s" % (name, reading or "(no reading at all)"))
    print("run-selftests: produce them with  GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh")
    print("run-selftests: and, for a row with no manifest leg, a direct timed run of its argv; then")
    print("run-selftests: write the seconds and the condition into this file's fourth column.")
    raise SystemExit(1)

if not rows:
    print("run-selftests: the declaration ranked NO row at all, so this verb graded nothing")
    raise SystemExit(2)

total = sum(r[0] for r in rows)
rows.sort(key=lambda r: (-r[0], r[2]))
print("run-selftests: %d row(s), %d s of recorded time; the declared majority share is %.0f%% and"
      % (len(rows), total, share * 100))
print("run-selftests: the declared minimum port factor is %.2fx." % factor)
cum, cut = 0, None
for i, (secs, cond, name) in enumerate(rows, 1):
    cum += secs
    frac = cum / float(total)
    mark = " "
    if cut is None and frac >= share:
        cut, mark = i, "<"
    print("  %2d  %6d s  cum %5.1f%% %s  %-30s  %s" % (i, secs, frac * 100, mark, cond, name))
print("----")
print("run-selftests: the declared share is carried by the TOP %d suite(s) — %d s of %d, %.1f%%."
      % (cut, sum(r[0] for r in rows[:cut]), total, sum(r[0] for r in rows[:cut]) / float(total) * 100))
PY
  exit $?
fi

# ---- the declaration, read once. Emitted as: STATE, name, budget, argv -- in that order.
# ---- A row whose argv is empty takes it from `tools/gate-legs.json`, so the manifest stays the one
# ---- place a held leg's command is written and this file carries only what the manifest cannot.
read_population() {
  "$PYBIN" - "$BUDGETS" "$LEGS" "$FILTER" <<'PY'
import json, sys

# LF, NOT CRLF, and this is a bug fix rather than tidiness. On Windows `print` translates every
# newline to CR LF, so each row below reached the shell with a trailing CR. It was INVISIBLE while
# the state was the LAST field -- `state` merely became "ok<CR>", and nothing compared it
# successfully anyway -- and it turned fatal the moment the argv moved last, because the final
# path token then carried the CR into `git ls-files` and every row read as untracked. Two defects
# hiding each other, and `run-selftests.test.sh` surfaced both on its first run.
sys.stdout.reconfigure(newline="")
budgets, legs_path, filt = sys.argv[1], sys.argv[2], sys.argv[3]
legs = {l["name"]: l for l in json.load(open(legs_path, encoding="utf-8"))}
for line in open(budgets, encoding="utf-8"):
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    f = line.rstrip("\r\n").split("\t")
    if len(f) < 2:
        continue
    name, budget, argv = f[0], f[1], (f[2] if len(f) > 2 else "")
    # A BUDGET NOBODY CAN COMPARE IS NOT A BUDGET. An empty second column emitted `ok` for a row
    # whose argv then read back EMPTY -- the run loop `eval`'d nothing, got rc 0, and printed a
    # green line at 0s for a suite it never executed; and `[ "$took" -gt "$budget" ]` on a
    # non-number errors with `integer expression expected`, returns 2, and reads as "not over
    # budget", so the cost verdict went quiet too. Neither direction of `--check` could see it:
    # the forward one matches names and the reverse one iterates an empty argv zero times.
    if not budget.isdigit():
        print("\t".join(["BADBUDGET", name, budget, argv]))
        continue
    if not argv:
        leg = legs.get(name)
        if not leg:
            print("\t".join(["UNRESOLVED", name, budget, ""]))
            continue
        argv = " ".join(leg.get("argv", []))
    if filt and filt not in argv:
        continue
    print("\t".join(["ok", name, budget, argv]))
PY
}

# ---- THE WIDTH IS RESOLVED ONCE, BY THE BAR'S OWN RESOLVER. Detection, the profile table, the clamp
# ---- and the GATE_JOBS override are 200 lines inside `run-gates.sh`; re-implementing them here is
# ---- the two-spellings drift this repo gates elsewhere. `--print-profile` exits before the
# ---- turnstile, so asking costs nothing and takes no beacon.
W=$(bash "$HERE/run-gates.sh" --print-profile 2>/dev/null | awk -F'\t' '$1=="width"{print $2}')
case "${W:-}" in ''|*[!0-9]*) W=2 ;; esac
# THE COMPOSITE BOUND: outer x inner never exceeds the profile row's declared width. A spec audit
# caught this unit and the harness unit each reading that width independently, which at width 8 would
# be 8 suites x 8 arms = 64 concurrent processes on a host where a bare spawn costs 319 ms.
#
# THE OUTER POOL IS 1 BECAUSE THE RUN LOOP BELOW IS SERIAL, and it is serial on purpose: this runner
# grades each suite against its OWN declared budget, so two suites racing would charge each of them
# the other's contention and a breach would name the wrong one. An earlier draft divided by a pool of
# 4 that does not exist, which handed every ported suite a quarter of the width it was entitled to —
# measured on `check-line-length.test.sh`: 13.6 s at the width that division produced against 7.9 s
# at the declared one. RE-DIVIDE HERE if the loop ever runs suites concurrently; the invariant is the
# product, not this constant.
OUTER=1
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
  while IFS=$'\t' read -r state name budget argv; do
    [ -n "${name:-}" ] || continue
    if [ "$state" = UNRESOLVED ]; then
      echo "run-selftests: row '$name' has no argv and no leg of that name in the manifest" >&2
      fails=1; continue
    fi
    if [ "$state" = BADBUDGET ]; then
      echo "run-selftests: row '$name' declares a budget that is not a number ('$budget'), so its cost verdict could never fire" >&2
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
TOTAL=$(printf '%s' "$POP" | awk -F'\t' '{s+=$3} END{print s+0}')
if [ "$MODE" = list ]; then
  printf '%s\n' "$POP" | awk -F'\t' '{printf "  %-46s %6ss  %s\n", $2, $3, $4}'
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
while IFS=$'\t' read -r state name budget argv; do
  [ -n "${name:-}" ] || continue
  # THE STATE IS READ HERE TOO. This loop used to ignore it entirely, so an UNRESOLVED row -- whose
  # argv is empty by construction -- was `eval`'d as the empty string, returned 0, and printed a
  # green line for a suite that does not exist. `--check` is a separate leg and a separate run; a
  # runner that trusts it has two answers to one question.
  if [ "$state" != ok ]; then
    st=1
    printf 'FAIL  %-46s        (%s: this row could not be resolved into a runnable suite)\n' "$name" "$state"
    continue
  fi
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

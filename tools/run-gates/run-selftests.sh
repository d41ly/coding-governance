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
# THIS SCRIPT'S OWN REPO-RELATIVE PATH, DERIVED. Spelling it as a literal would ship gov's
# prefix into an adopter installed elsewhere, where it resolves to nothing -- the install-prefix
# ban, which this file is graded by. An empty derivation REFUSES rather than printing `bash `.
SELF="$(git -C "$(dirname -- "$0")" rev-parse --show-prefix 2>/dev/null)$(basename -- "$0")"
[ -n "$SELF" ] || { echo "run-selftests: cannot derive this script's own path" >&2; exit 2; }

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
  --sweep     the same population through a bounded OUTER pool, so the wall clock
              falls toward the longest suite instead of the sum of all of them.
              It answers ONE question -- did any suite fail -- and issues NO cost
              verdict at all: every reading it takes is contended by the other
              suites, and a contended clock cannot grade a budget. Use the no-flag
              mode for that. SELFTEST_OUTER_WIDTH overrides the outer width
              (clamped to the resolved one); SELFTEST_WALL overrides the run bound
              and is REFUSED below the largest per-suite bound.
              IT PAYS IN PROPORTION TO HOW UNDOMINATED THE POPULATION IS. The wall
              clock cannot fall below the longest member, so a selection of three
              suites where one holds most of the time is a LOSS — measured at 56s
              serial against 62s pooled. Nine suites measured 1692s against 981s.
USAGE
}

MODE=run; FILTER=""
while [ $# -gt 0 ]; do
  case "$1" in
    --kit)   FILTER=${2:-}; shift 2 ;;
    --check) MODE=check; shift ;;
    --list)  MODE=list; shift ;;
    --rank)  MODE=rank; shift ;;
    --sweep) MODE=sweep; shift ;;
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
# CONTENDED READINGS ARE REFUSED, NOT RANKED. `--sweep` composes this token, so the emitter and this
# reader share one spelling; `run-selftests.test.sh` captures the tag from a real sweep and feeds it
# here, because a fixture that hand-types it on both sides observes nothing about the join.
REFUSED = [re.compile(r"pooled@")]

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
    # REFUSED BEFORE THE RANKERS ARE OFFERED THE ROW, and the order is the whole mechanism. A CONDS
    # match is what RANKS a row -- the loop below breaks on the first hit and appends to `rows`, and
    # only the for/else fall-through reaches `unbacked`. So a pooled pattern added to CONDS would
    # make a contended reading RANK, the exact inverse of the intent; and the lenient `measured`
    # entry accepts any text after the seconds, so it would match `measured 42s pooled@8x1 on node
    # a` first anyway. Eleven rows in this file already use that spelling, three of them with a
    # width clause, so it is the likely spelling rather than a contrived one.
    #
    # What it buys: `--sweep` states its own condition and a reading taken under it can be pasted
    # into this file by any hand. Ranking it against serial ones is the ranking-the-conditions
    # defect TOOL-aQuenchedHarness-6 S3a exists to prevent, and nothing refused it until now.
    if any(rx.search(reading) for rx in REFUSED):
        unbacked.append((name, reading))
        continue
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
# THE OUTER POOL IS 1 IN THE DEFAULT MODE, because that loop is serial on purpose: it grades each
# suite against its OWN declared budget, so two suites racing would charge each of them the other's
# contention and a breach would name the wrong one. An earlier draft divided by a pool of 4 that does
# not exist, which handed every ported suite a quarter of the width it was entitled to — measured on
# `check-line-length.test.sh`: 13.6 s at the width that division produced against 7.9 s at the
# declared one. The invariant is the PRODUCT, not the constant.
#
# `--sweep` IS THE RE-DIVISION that comment always anticipated (TOOL-aPooledSweep-1). It runs the
# suites concurrently and therefore issues no cost verdict at all, which is what makes the trade
# sound rather than a shortcut: the contention that would have misattributed a breach is admitted,
# and the breach is simply not claimed. Outer takes the whole width there and inner falls to 1,
# because THREE of the population's suites source the selftest harness and the other
# fifty-six have no inner width to spend — so inner parallelism buys 3/59ths of the work and outer
# buys all of it.
OUTER=1
if [ "$MODE" = sweep ]; then
  OUTER=$W
  # THE OVERRIDE IS CLAMPED. The invariant is the product, so a knob that could exceed it would be a
  # knob for breaking the one rule this block exists to keep.
  case "${SELFTEST_OUTER_WIDTH:-}" in
    '') : ;;
    *[!0-9]*|0)
      # NOT SILENTLY DISCARDED. An ignored knob leaves the operator believing a width they never
      # got, and the run then prints a pair that agrees with itself and with nothing they asked for.
      echo "run-selftests: SELFTEST_OUTER_WIDTH is '$SELFTEST_OUTER_WIDTH', which is not a positive" >&2
      echo "run-selftests: integer, so the width you asked for could not be applied. Nothing was run." >&2
      exit 2 ;;
    *) # BASE TEN, FORCED. `08` and `007` pass the digit test above and then read as OCTAL in
       # arithmetic, where `08` is not a number at all — the refusal is bypassed and the failure
       # lands somewhere else entirely.
       OUTER=$((10#$SELFTEST_OUTER_WIDTH))
       [ "$OUTER" -ge 1 ] || { echo "run-selftests: SELFTEST_OUTER_WIDTH resolves to $OUTER" >&2; exit 2; }
       [ "$OUTER" -le "$W" ] || OUTER=$W ;;
  esac
fi
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

# ---- --sweep: the population through a bounded OUTER pool. TOOL-aPooledSweep-1 -----------------
# ---- It answers "did any suite fail" and NOTHING about cost. The serial loop below is the only
# ---- mode that grades a budget, and that division is the whole reason this one is admissible.
if [ "$MODE" = sweep ]; then
  # THE BOUND IS A PROBED CAPABILITY, NOT AN ASSUMPTION, and its absence REFUSES rather than
  # degrading quietly. the selftest harness probes for `timeout` the same way and runs its
  # arms UNBOUNDED when it is missing, which is right for arms that are seconds long. Here the
  # missing binary deletes the whole property: this mode renders every verdict AFTER the pool
  # drains, so one non-returning suite suppresses all of them, which is strictly worse than the
  # serial loop it replaces.
  # RESOLVED BY NAME, over a candidate list, because coreutils ships as `gtimeout` under a prefix on
  # more than one platform and a hard-coded `timeout` would refuse those hosts for a spelling. The
  # list is overridable so an adopter can name a third; that override is also what gives this
  # refusal its failing case, which a hard-coded name has no honest way to stage.
  SWEEP_TIMEOUT=""
  for _cand in ${SELFTEST_TIMEOUT_BIN:-timeout gtimeout}; do
    command -v "$_cand" >/dev/null 2>&1 && { SWEEP_TIMEOUT=$_cand; break; }
  done
  [ -n "$SWEEP_TIMEOUT" ] || {
    echo "run-selftests: --sweep needs a 'timeout' binary to bound each suite and found none of:" >&2
    echo "run-selftests:   ${SELFTEST_TIMEOUT_BIN:-timeout gtimeout}" >&2
    echo "run-selftests: without one every suite below would run unbounded while this mode claims" >&2
    echo "run-selftests: each one is bounded, and a single hang would suppress all $NROWS verdict" >&2
    echo "run-selftests: lines. Use the no-flag mode, which reports each suite as it finishes." >&2
    exit 2; }

  # THE PER-SUITE BOUND IS DERIVED FROM THE ROW'S OWN BUDGET, and the declaration is refused when
  # absent — a factor nobody wrote is not a factor, which is the rule `--rank` already applies to
  # its share. This does NOT make the budget a hang bound: it derives one from it, exactly as the
  # manifest ceilings this file's header points at are themselves derived from recorded seconds.
  SWEEP_FACTOR=$(sed -n 's/^#[[:space:]]*sweep-ceiling-factor:[[:space:]]*\([0-9][0-9]*\).*/\1/p' "$BUDGETS" | head -1)
  case "${SWEEP_FACTOR:-}" in ''|*[!0-9]*|0)
    echo "run-selftests: $BUDGETS declares no sweep-ceiling-factor, so no suite could be bounded" >&2
    echo "run-selftests: and --sweep would background $NROWS unbounded processes. Declare it in" >&2
    echo "run-selftests: that file's header, beside the reading it was set against." >&2
    exit 2 ;;
  esac

  # THE ROWS, INDEXED. Declaration order is the reporting order whatever the pool does with them,
  # so the output is byte-stable against the serial mode's and against itself at another width.
  SW_N=0; SW_STATE=(); SW_NAME=(); SW_BUDGET=(); SW_ARGV=()
  SWEEP_LARGEST=0
  while IFS=$'\t' read -r state name budget argv; do
    [ -n "${name:-}" ] || continue
    SW_N=$((SW_N + 1))
    SW_STATE+=("$state"); SW_NAME+=("$name"); SW_BUDGET+=("$budget"); SW_ARGV+=("$argv")
    if [ "$state" = ok ]; then
      b=$(( budget * SWEEP_FACTOR ))
      [ "$b" -gt "$SWEEP_LARGEST" ] && SWEEP_LARGEST=$b
    fi
  done <<EOF
$POP
EOF

  # THE RUN WALL IS THE LARGEST PER-SUITE BOUND, and it is DERIVED here rather than borrowed from
  # `run-gates.sh --print-profile`. That row declares 10800s while this population declares 13600s
  # for `unattended gate selftest` alone, so a borrowed wall would sit BELOW the largest bound and
  # kill every sweep for arriving on time. A pool cannot finish before its longest member's own
  # bound expires; any smaller wall is an error, not a policy.
  # THE WALL COVERS EVERY WAVE. `largest bound` alone is the wall for a pool wide enough to run the
  # whole population at once, and this one is not: at `SELFTEST_OUTER_WIDTH=1` -- a documented
  # setting -- fifty-nine suites run one after another and a one-suite wall kills a perfectly clean
  # run. Waves is the honest denominator, and it is derived from the population and the width rather
  # than guessed.
  # THE STRUCTURAL CEILING, not a multiple of the worst suite. `largest x waves` assumes every wave
  # is as slow as the slowest suite, which over this population is 2x to 15x the real maximum -- a
  # wall that large can never fire, and a backstop that cannot fire is not one. The true ceiling is
  # the total bounded work spread over the pool, and it can never be below the longest single suite.
  SW_RUNNABLE=0; SWEEP_TOTAL=0
  _sx=0
  while [ "$_sx" -lt "$SW_N" ]; do
    if [ "${SW_STATE[$_sx]}" = ok ]; then
      SW_RUNNABLE=$((SW_RUNNABLE + 1))
      SWEEP_TOTAL=$(( SWEEP_TOTAL + ${SW_BUDGET[$_sx]} * SWEEP_FACTOR ))
    fi
    _sx=$((_sx + 1))
  done
  SWEEP_WALL=$(( (SWEEP_TOTAL + OUTER - 1) / OUTER ))
  [ "$SWEEP_WALL" -ge "$SWEEP_LARGEST" ] || SWEEP_WALL=$SWEEP_LARGEST
  SWEEP_DERIVED=$SWEEP_WALL
  case "${SELFTEST_WALL:-}" in
    '') : ;;
    *[!0-9]*)
      # D5: A KNOB WITH A TYPO IN IT MUST NOT BE SILENTLY IGNORED. Discarding the value leaves the
      # operator believing a bound they never set, which is the same shape as a gate that reports a
      # reassuring zero when it is broken.
      echo "run-selftests: SELFTEST_WALL is '$SELFTEST_WALL', which is not a number of seconds," >&2
      echo "run-selftests: so the run bound you asked for could not be applied. Nothing was run." >&2
      exit 2 ;;
    *) SWEEP_WALL=$((10#$SELFTEST_WALL))
       if [ "$SWEEP_WALL" -lt "$SWEEP_DERIVED" ]; then
         echo "run-selftests: NOTE — the wall you set (${SWEEP_WALL}s) is below the derived one"
         echo "run-selftests: (${SWEEP_DERIVED}s, the bounded work over $OUTER slot(s)), so a legitimately slow run can be killed."
       fi ;;
  esac
  if [ "$SWEEP_WALL" -lt "$SWEEP_LARGEST" ]; then
    echo "run-selftests: the run wall is ${SWEEP_WALL}s but the largest per-suite bound in this" >&2
    echo "run-selftests: population is ${SWEEP_LARGEST}s, so the run would be killed before its" >&2
    echo "run-selftests: longest suite could legitimately finish. Raise SELFTEST_WALL, or lower" >&2
    echo "run-selftests: the budget the bound derives from." >&2
    exit 2
  fi

  SWEEP_ROOT=$(mktemp -d) || { echo "run-selftests: cannot create a scratch root" >&2; exit 2; }
  trap 'rm -rf "$SWEEP_ROOT" 2>/dev/null' EXIT

  # ---- POOL SAFETY IS OBSERVED, NOT ASSUMED. TOOL-aPooledSweep-3 -------------------------------
  # Running 59 suites together is sound only if each confines its writes to its own scratch. The
  # private TMPDIR below is the redirection; this is the observation that it held.
  #
  # ONE ARM, over the TRACKED working tree. It listed the git common dir too and that arm is DELETED
  # rather than narrowed: that directory is shared by every worktree of the repository and the bar
  # itself writes `gate-bar-beacon` and `gate-bar-queue` at its top level when it claims the
  # turnstile, alongside `gate-ledger.tsv`, `gate-logs`, `index`, `logs` and `refs`. The sweep's
  # floor is its longest suite, so the window between the two readings is tens of minutes wide: any
  # sibling session running a bar flips the listing, and a whole-run fingerprint cannot name a
  # culprit. An instrument that reds on innocent runs is ignored within two sightings.
  #
  # `--untracked-files=no` IS LOAD-BEARING. Plain `--porcelain` lists untracked paths as `??`, so
  # without it every build artifact and freshly written record flips the reading -- this build's own
  # sweep would red on the review report it had just written.
  read_tree_fingerprint() { git status --porcelain --untracked-files=no 2>/dev/null; }

  # THE LIVENESS ASSERTION, and it is NOT emptiness: `git status --porcelain` is EMPTY on a clean
  # tree, so an empty reading is the ordinary case and cannot distinguish a working probe from a
  # broken one. What is asserted is that the command SUCCEEDED.
  if ! FP_BEFORE=$(read_tree_fingerprint) || ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "run-selftests: the tree fingerprint could not be taken, so a sweep would be UNGRADED —" >&2
    echo "run-selftests: a failed reading and a clean tree are the same empty string, and this mode" >&2
    echo "run-selftests: would report the second while meaning the first. Nothing was run." >&2
    exit 2
  fi

  # THE CONDITION, COMPOSED ONCE. Not re-derived per row: the same fact spelled twice in a file
  # whose own header names that defect. It is printed in a stable shape because the `--rank` refusal
  # matches this exact token, and the arm that proves they agree captures it from here.
  SWEEP_CONDITION="pooled@${OUTER}x${SELFTEST_INNER_WIDTH}"
  echo "run-selftests: SWEEP of $SW_N suite(s), width $W (outer $OUTER, inner $SELFTEST_INNER_WIDTH)"
  echo "run-selftests: condition: $SWEEP_CONDITION"
  echo "run-selftests: per-suite bound = budget x ${SWEEP_FACTOR}; run wall ${SWEEP_WALL}s; NO cost verdict is issued"

  # THE REAP IS PROBED ONCE, OUTSIDE THE LOOP. `wait -n` returns the exit STATUS of the job that
  # finished, so `wait -n || wait` reads a RED suite as "this shell has no wait -n" and falls back
  # to waiting for all of them — the pool silently degenerates to a barrier per suite, which is
  # serial with extra steps and still prints a width. The selftest harness records the same trap.
  _rs_waitn=0; ( : & wait -n ) >/dev/null 2>&1 && _rs_waitn=1

  # AND SO IS SUB-SECOND `date`. `%N` is a GNU extension: BSD `date` prints the literal `N`, so
  # `$(( $(date +%s%N) / 1000000 ))` is an arithmetic syntax error that aborts EVERY worker before
  # it runs its suite -- a total false RED blaming each suite for the runner's own arithmetic. This
  # script already advertises the platform it cannot run on, by probing for `gtimeout`. Probed once,
  # outside the loop, and the fallback is whole seconds with the resolution SAID rather than
  # silently lost: the peak figure is then blind to a handoff inside one second.
  _rs_ns=0
  case "$(date +%N 2>/dev/null)" in ''|*[!0-9]*) : ;; *) _rs_ns=1 ;; esac
  if [ "$_rs_ns" = 1 ]; then
    read_now_ms() { echo $(( $(date +%s%N) / 1000000 )); }
  else
    read_now_ms() { echo $(( $(date +%s) * 1000 )); }
    echo "run-selftests: this date has no sub-second %N, so stamps are whole seconds and the peak"
    echo "run-selftests: figure below cannot separate a pool handoff from a real overlap."
  fi

  # ONE SUITE, BOUNDED, ITS OWN SCRATCH. The verdict file carries the status, the two stamps and
  # nothing else; the captured output is its own file because a pooled FAIL that printed only an
  # exit code would be a mode you cannot debug without the serial re-run it exists to avoid.
  run_sweep_one() {
    # TWO STATEMENTS, NOT ONE. `local k=$1 d="$SWEEP_ROOT/$k"` expands the whole line BEFORE `local`
    # assigns anything, so `$k` is unbound and `set -u` kills the arm — silently, in a background
    # job, leaving no verdict file. `lib-selftest.sh` sidesteps the same trap by writing `$1` twice.
    local k=$1
    local d="$SWEEP_ROOT/$k"
    mkdir -p "$d/tmp" || return
    local bound=$(( ${SW_BUDGET[$((k - 1))]} * SWEEP_FACTOR ))
    local s e rc tp
    s=$(read_now_ms)
    # THE WORKER'S OWN PID, NOT `$$`. A subshell INHERITS `$$` from its parent, so `echo $$` here
    # wrote the RUNNER's pid into every pid file and the wall watchdog SIGTERMed run-selftests.sh
    # itself — exit 143, no verdicts rendered, the suites orphaned and the scratch root deleted from
    # under them. The whole WALL rendering path below was unreachable dead code as a result.
    # Recording the `timeout` child rather than this subshell is what makes the kill reach the work:
    # `timeout` forwards the signal to its own child, and killing the subshell would leave both.
    TMPDIR="$d/tmp" "$SWEEP_TIMEOUT" -k 5 "$bound" bash -c "${SW_ARGV[$((k - 1))]}" > "$d/out" 2>&1 &
    tp=$!
    echo "$tp" > "$d/pid"
    wait "$tp"
    rc=$?
    e=$(read_now_ms)
    rm -f "$d/pid"
    printf '%s\t%s\t%s\n' "$rc" "$s" "$e" > "$d/v"
  }

  # THE WALL WATCHDOG. It records the breach in a FILE before killing anything, so the renderer can
  # tell "this suite was killed by the wall" from "this suite never wrote a verdict" — two states
  # that look identical from a missing file alone.
  # ITS OUTPUT GOES TO /dev/null, AND THAT IS NOT TIDINESS. A background job inherits the caller's
  # stdout, so under `out=$(... --sweep ...)` the watchdog holds the command substitution's pipe open
  # and the CAPTURE blocks for the whole wall even though the sweep finished in seconds. Measured:
  # the round-trip arm below hit its 120s bound against a fixture whose suites take two. It is the
  # same class the selftest harness records for `timeout` and a surviving grandchild.
  #
  # AND ITS SLEEP IS RECORDED, because killing the subshell orphans the sleep rather than ending it.
  ( sleep "$SWEEP_WALL" & echo $! > "$SWEEP_ROOT/dog.sleep"; wait $!
    : > "$SWEEP_ROOT/wall-breached"
    for pf in "$SWEEP_ROOT"/*/pid; do
      [ -r "$pf" ] || continue
      read -r wp < "$pf" 2>/dev/null && kill -TERM "$wp" 2>/dev/null
    done ) >/dev/null 2>&1 &
  SWEEP_DOG=$!
  # DISOWNED, and this is load-bearing rather than tidy: the watchdog sleeps for the whole wall, so
  # a `wait` that can see it blocks until the wall fires even when every suite finished in seconds.
  disown "$SWEEP_DOG" 2>/dev/null || true

  i=1; live=0
  while [ "$i" -le "$SW_N" ]; do
    # THE BREACH STOPS THE DISPATCH, and this line is the whole wall. Before the pid fix the
    # watchdog SIGTERMed the RUNNER, which stopped the run by accident; pointing the kill at the
    # workers -- correct in itself -- removed the only thing that ended it, so the pool kept
    # launching the rest of the population after the wall had fired. Reproduced three times at
    # 16 s, 17 s and 23 s against a 10 s wall. `run-gates.sh` carries the identical guard at the top
    # of its own walk, and this is that line rather than a second invention.
    [ -e "$SWEEP_ROOT/wall-breached" ] && break
    if [ "${SW_STATE[$((i - 1))]}" = ok ]; then
      run_sweep_one "$i" &
      live=$((live + 1))
      if [ "$live" -ge "$OUTER" ]; then
        if [ "$_rs_waitn" = 1 ]; then wait -n; live=$((live - 1)); else wait; live=0; fi
      fi
    fi
    i=$((i + 1))
  done
  wait
  kill "$SWEEP_DOG" 2>/dev/null || true
  if [ -r "$SWEEP_ROOT/dog.sleep" ]; then
    read -r _ds < "$SWEEP_ROOT/dog.sleep" 2>/dev/null && kill "$_ds" 2>/dev/null
  fi

  WALL_BREACHED=0; [ -e "$SWEEP_ROOT/wall-breached" ] && WALL_BREACHED=1

  # RENDERED IN DECLARATION ORDER, by builtins, off the arrays. A suite's position in the output
  # never depends on when the pool happened to free its slot.
  st=0; ran=0; killed=0; walled=""; unrun=""; withheld=0
  j=1
  while [ "$j" -le "$SW_N" ]; do
    name=${SW_NAME[$((j - 1))]}; state=${SW_STATE[$((j - 1))]}; d="$SWEEP_ROOT/$j"
    if [ "$state" != ok ]; then
      st=1
      printf 'FAIL  %-46s        (%s: this row could not be resolved into a runnable suite)\n' "$name" "$state"
      j=$((j + 1)); continue
    fi
    if [ ! -r "$d/v" ]; then
      st=1
      if [ ! -d "$d" ] && [ "$WALL_BREACHED" = 1 ]; then
        # NEVER LAUNCHED. The wall stopped the dispatch, so this suite has no result of any kind —
        # which is a different fact from a suite that started and was killed, and reporting both as
        # "killed" would tell an operator this suite had been tried.
        unrun="$unrun $name"
        printf 'UNRUN %-46s        (the %ss run wall stopped the dispatch before this suite started)\n' "$name" "$SWEEP_WALL"
      elif [ "$WALL_BREACHED" = 1 ]; then
        ran=$((ran + 1)); walled="$walled $name"
        printf 'WALL  %-46s        (killed by the %ss run wall before it finished)\n' "$name" "$SWEEP_WALL"
      else
        ran=$((ran + 1))
        printf 'FAIL  %-46s        (no verdict was written, so this suite could not start)\n' "$name"
      fi
      j=$((j + 1)); continue
    fi
    ran=$((ran + 1))
    IFS=$'\t' read -r rc s e < "$d/v"
    took=$(( (e - s) / 1000 ))
    # EVERY ROW THAT RAN CARRIES ITS COST VERDICT, and that verdict is `withheld`. Printing the
    # seconds and nothing else would be a budget silently not graded, which is the green-by-absence
    # class; printing `ok` for the cost would be a verdict taken from a clock this run contended.
    withheld=$((withheld + 1))
    if [ "$rc" = 0 ]; then
      printf 'ok    %-46s %5ss  cost withheld\n' "$name" "$took"
    elif [ "$WALL_BREACHED" = 1 ] && [ "$rc" = 143 ]; then
      # KILLED BY THE WALL, not by its own bound, and the two are different facts. `timeout` exits
      # 124 when ITS bound expires; the watchdog sends TERM, so the worker exits 143. Rendering both
      # as one lost the distinction, and the WALL branch below -- which only fires on a MISSING
      # verdict -- was unreachable, because a TERMed worker still writes its verdict file. Observed
      # by running it: a 12s wall over an 18s run rendered the killed suite as an ordinary FAIL.
      st=1; walled="$walled $name"
      printf 'WALL  %-46s %5ss  cost withheld  (killed by the %ss run wall, not by its own bound)
'         "$name" "$took" "$SWEEP_WALL"
    elif [ "$rc" = 124 ] || [ "$rc" = 137 ]; then
      st=1; killed=$((killed + 1))
      printf 'TIMEOUT %-44s %5ss  (killed at its %ss bound — it did not fail, it did not finish)\n' \
        "$name" "$took" "$(( ${SW_BUDGET[$((j - 1))]} * SWEEP_FACTOR ))"
    else
      st=1
      printf 'FAIL  %-46s %5ss  cost withheld  (exit %s)\n' "$name" "$took" "$rc"
      grep -E '^(FAIL|nope|.*FAILED)' "$d/out" 2>/dev/null | head -4 | sed 's/^/        /'
    fi
    j=$((j + 1))
  done

  echo "----"
  [ -n "$walled" ] && echo "run-selftests: the ${SWEEP_WALL}s run wall killed:$walled"
  # AN UNRUN SUITE IS AN UNGRADED SUITE, said separately because it is the fact an operator acts on:
  # the sweep has no verdict for these at all, and a wall that stops a dispatch leaves more of them
  # the wider the population is.
  [ -n "$unrun" ] && echo "run-selftests: the wall stopped the dispatch, so these were NEVER RUN and are UNGRADED:$unrun"
  # THE PEAK, COMPUTED FROM THE STAMPS BEFORE THE SCRATCH IS REMOVED. The printed width pair says
  # what the pool was ASKED for; this says what it reached. They are different claims, and only the
  # second can catch a pool that ran wide when it was told not to. It is also the number a reader
  # actually wants: "peak 8 of outer 8" says the width was spent, "peak 1" says it was not.
  SWEEP_PEAK=$(
    for vf in "$SWEEP_ROOT"/*/v; do [ -r "$vf" ] && cut -f2,3 "$vf"; done 2>/dev/null | awk '
      { s[NR]=$1; e[NR]=$2 }
      # HALF-OPEN, and the strict `>` is the whole correctness of this figure. Stamps are whole
      # seconds, so with `>=` a suite ENDING at second T and its replacement STARTING at T both
      # count at T -- every pool handoff double-counts. Measured: a strictly serial fixture reported
      # peak 2, and the real 59-row population at outer 8 makes about fifty handoffs, so the guard
      # below would have redded every green sweep.
      END { peak=0
            for (i=1; i<=NR; i++) { c=0
              for (j=1; j<=NR; j++) if (s[j] <= s[i] && e[j] > s[i]) c++
              if (c > peak) peak=c }
            print peak+0 }')
  case "${SWEEP_PEAK:-}" in ''|*[!0-9]*) SWEEP_PEAK=0 ;; esac
  echo "run-selftests: peak concurrency $SWEEP_PEAK of outer $OUTER"
  # AND IT IS A GUARD, not a statistic. The composite invariant is outer x inner within the declared
  # width; a pool that ran wider than its own outer bound has broken it, and the printed pair cannot
  # notice because the pair is what the pool was ASKED for.
  if [ "$SWEEP_PEAK" -gt "$OUTER" ]; then
    st=1
    echo "run-selftests: THE POOL RAN WIDER THAN ITS BOUND — peak $SWEEP_PEAK against an outer width"
    echo "run-selftests: of $OUTER. The composite invariant (outer x inner <= the declared width) is"
    echo "run-selftests: broken, so this run oversubscribed the box and every reading above is suspect."
  fi

  # THE AFTER READING, once the pool has DRAINED. Taken mid-pool it would race fifty-eight writers,
  # which is why this instrument is whole-run and says so rather than pretending to attribute.
  # THE SAME LIVENESS THE BEFORE READING HAS. Without it a `git status` that FAILS here returns the
  # empty string, which on a dirty tree compares unequal and reports the sweep UNSOUND -- a real
  # verdict for a reason that never happened -- and on a clean tree compares equal and reports a
  # match the probe never made.
  if ! FP_AFTER=$(read_tree_fingerprint); then
    st=1
    echo "run-selftests: the closing tree fingerprint could not be TAKEN, so this sweep is UNGRADED"
    echo "run-selftests: for pool safety. That is not the same as a clean tree and is not reported"
    echo "run-selftests: as one."
  elif [ "$FP_BEFORE" != "$FP_AFTER" ]; then
    st=1
    echo "run-selftests: THE SWEEP IS UNSOUND — the tracked working tree changed while it ran, so a"
    echo "run-selftests: suite wrote outside its own scratch. This cannot name which one: a whole-run"
    echo "run-selftests: fingerprint has no way to attribute, and guessing would be worse than saying"
    echo "run-selftests: so. Re-run the SERIAL mode, which can. What changed:"
    printf '%s\n' "$FP_AFTER" | grep -vxF "$FP_BEFORE" 2>/dev/null | sed 's/^/  /' | head -20
  else
    echo "run-selftests: tree fingerprint MATCHED before and after — no suite wrote outside its scratch"
  fi

  # THE COUNT IS WHAT STOPS THE WITHHOLDING BEING A SILENT PASS. A green sweep announces on every
  # run how many budgets it did not grade, so it can never be mistaken for a budget-clean run.
  echo "run-selftests: $withheld cost verdict(s) WITHHELD under $SWEEP_CONDITION — a contended clock cannot grade a budget"
  echo "run-selftests: for a cost verdict, run the serial mode: bash $SELF"
  if [ "$st" -eq 0 ]; then
    echo "sweep GREEN — $ran suite(s) ran concurrently; NO cost verdict was issued for any of them"
  else
    echo "sweep RED — $ran suite(s) ran concurrently, $killed killed at their own bound; NO cost verdict was issued"
    # A POOLED RED IS AMBIGUOUS BY CONSTRUCTION and the summary says which step resolves it.
    # TOOL-dSpentCeiling-8 measured `run-gates turnstile` and `row-keyed merge driver replay` —
    # both rows of this population — redding under the bar's own concurrency and green standalone,
    # with no commit and no working-tree change between the runs. So a red here cannot separate "the
    # mechanism is broken" from "this machine was too busy", and an operator handed that verdict
    # with no next step will either re-run at random or stop trusting the mode.
    echo "run-selftests: a pooled RED cannot tell a broken mechanism from a busy box. Confirm it with"
    echo "run-selftests: the serial re-run: bash $SELF"
  fi
  exit "$st"
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

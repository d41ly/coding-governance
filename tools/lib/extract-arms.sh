#!/usr/bin/env bash
# extract-arms.sh — a suite's ARM INVENTORY, taken from what it RAN. TOOL-aQuenchedHarness-6.
#
# The safety property for a port: the set of arms a suite executes must be identical before and
# after. A port that drops an arm is faster AND greener, which is the one way a speed-up can be a
# regression wearing a speed-up's clothes.
#
# FROM OUTPUT, NOT FROM SOURCE, and that is a survey result rather than a preference. The suites use
# at least FIVE unrelated idioms — `arm "label" rc want`, `ok`/`nope`, `check(...)`,
# `say_ok`/`say_fail`, and `arm ok    <label>` with the suite's own word before the verdict — and
# several use none this survey could name. A parser for all of them is a large investment in a
# safety property, and it would grade what the source SAYS rather than what the suite RAN: an arm
# lost to a mis-scoped `if` still has its call site.
#
# So: run the suite, keep the lines carrying a per-arm verdict, strip the verdict token and any
# timing, sort what is left. That set is the inventory. The fifth idiom above turned up the first
# time this was pointed at a real suite and cost ONE alternation to absorb, which is the whole
# argument for this shape over a parser.
#
# UNEXTRACTABLE IS A NAMED STATE. A suite whose output carries no per-arm line cannot be ported under
# this unit, because its inventory cannot be compared and the port's claim would be unfalsifiable.
# It is REPORTED, never treated as an empty inventory — an empty set compares equal to an empty set,
# which is the vacuous-selector class at the altitude of a whole suite.
#
# AND SO IS PARTIAL EXTRACTION, which is the same defect one degree less obvious and which this file
# CLAIMED to cover while guarding only the zero. A portability survey pointed the extractor at
# `tools/memory-tree/check-memory-hygiene.test.sh`: 289 executed assertions, 31 output lines, and
# exactly 14 matching the grammar below. The old code returned those 14 at exit 0 — a confident
# inventory over 4.8% of the population — so a port that silently dropped 275 assertions would have
# diffed EMPTY and been certified by the very guard written to prevent it. Zero was never the
# dangerous number; the dangerous number is "some".
#
# THE FIX IS A LIVENESS ASSERTION, not a bigger grammar. The suite already reports its own executed
# total — `PASS (N assertions)` is required of every bar self-test by
# `tools/check-testsuite-counts.sh`, and the harness prints `PASS (N arms, width W)` — so the
# extractor COMPARES what it recovered against what the suite says it ran, and refuses on any
# inequality in either direction. A suite reporting no total at all is refused too: an inventory whose
# coverage cannot be checked is exactly the unfalsifiable claim above, and "I found some" is not a
# measurement. This is the same rule the charter states for every other probe in this tree — a probe
# that cannot verify itself says so rather than reporting a reassuring number.
set -u

print_usage() { echo "usage: bash tools/lib/extract-arms.sh <suite.sh> [--out <file>]"; }

[ $# -ge 1 ] || { print_usage; exit 2; }
SUITE=$1; shift
OUT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT=${2:-}; shift 2 ;;
    -h|--help) print_usage; exit 0 ;;
    *) echo "extract-arms: unknown argument '$1'"; exit 2 ;;
  esac
done
[ -f "$SUITE" ] || { echo "extract-arms: no suite at $SUITE"; exit 2; }

RAW=$(mktemp) || exit 2
trap 'rm -f "$RAW" 2>/dev/null' EXIT
bash "$SUITE" > "$RAW" 2>&1
RC=$?

# THE VERDICT VOCABULARY, in one place. A leading marker, optionally preceded by ONE word of the
# suite's own, plus whitespace — that is the entire grammar, which is why this needs no parser.
# The timing strip exists because a suite that prints seconds beside an arm would otherwise report a
# different inventory on every run, and the diff would be noise rather than a safety property.
MARK='^[[:space:]]*([A-Za-z_-]+[[:space:]]+)?(ok|nope|FAIL|SKIP)[[:space:]]+'
# A SUMMARY IS NOT AN ARM. `FAIL (1 of 2 arms, width 1)` — the harness's own verdict line — satisfies
# the grammar above, so a RED suite counted its summary as a nineteenth arm and its inventory moved
# with its verdict. A label is prose and never opens with a bracket, so the exclusion is exact rather
# than heuristic; found by this file's own arms, which is the whole argument for writing them.
SUMMARY='^[[:space:]]*(PASS|FAIL|FAILED|nope)[[:space:]]*\('
INV=$(grep -aE "$MARK" "$RAW" | grep -avE "$SUMMARY" \
      | sed -E "s/$MARK//" \
      | sed -E 's/[[:space:]]+[0-9]+(\.[0-9]+)?s([[:space:]]|$)/ /g' \
      | sed -E 's/[[:space:]]+$//' \
      | sort)
N=$(printf '%s' "$INV" | grep -c . || true)

# THE SUITE'S OWN EXECUTED TOTAL. Four spellings, all of them already in this tree: the classic
# `PASS (N assertions)` the testsuite-counts leg mandates, the harness's `PASS (N arms, width W)`,
# and the two failing forms, because a suite that RED-ed still ran a population and its inventory is
# still comparable. Taken from the LAST match, so a suite echoing an example line earlier in its
# output does not win over its own verdict.
TOTAL=$(grep -aoE '(PASS \(([0-9]+) (assertions|arms)|FAIL \([0-9]+ of ([0-9]+) arms|FAILED — ran ([0-9]+) assertion)' "$RAW" \
        | grep -aoE '[0-9]+' | tail -1)

if [ "$N" -eq 0 ]; then
  echo "extract-arms: UNEXTRACTABLE — $SUITE printed no per-arm verdict line (exit $RC), so its"
  echo "extract-arms: inventory cannot be compared and it must not be ported under this unit."
  echo "extract-arms: An empty inventory compares equal to an empty inventory, which would certify"
  echo "extract-arms: a port that dropped every arm."
  exit 3
fi

# COVERAGE, and it is a refusal rather than a note. See the header: partial extraction is the class
# this file exists to prevent and the one it used to wave through.
if [ -z "$TOTAL" ]; then
  echo "extract-arms: UNVERIFIABLE — $SUITE printed $N per-arm line(s) but reports no executed total,"
  echo "extract-arms: so nothing here can say whether those $N are the whole population or a fraction"
  echo "extract-arms: of it. An inventory of unknown coverage compares equal for a port that dropped"
  echo "extract-arms: everything it did not cover. The suite needs a PASS (n assertions) line, which"
  echo "extract-arms: tools/check-testsuite-counts.sh already requires of every self-test on the bar."
  exit 4
fi
if [ "$N" != "$TOTAL" ]; then
  echo "extract-arms: PARTIAL — $SUITE reports $TOTAL executed assertion(s) and printed $N line(s)"
  echo "extract-arms: this extractor can read, so the recovered inventory covers only part of what the"
  echo "extract-arms: suite graded. Comparing it across a port would certify every assertion it cannot"
  echo "extract-arms: see. Either the suite prints one readable verdict line per assertion, or it is"
  echo "extract-arms: named in the unported remainder — it is NOT ported on this inventory."
  exit 5
fi

if [ -n "$OUT" ]; then
  printf '%s\n' "$INV" > "$OUT"
  echo "extract-arms: $N arm(s) from $SUITE (suite exit $RC, its own total $TOTAL) -> $OUT"
else
  printf '%s\n' "$INV"
fi
exit 0

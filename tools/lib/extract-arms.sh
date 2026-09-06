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
INV=$(grep -aE "$MARK" "$RAW" \
      | sed -E "s/$MARK//" \
      | sed -E 's/[[:space:]]+[0-9]+(\.[0-9]+)?s([[:space:]]|$)/ /g' \
      | sed -E 's/[[:space:]]+$//' \
      | sort)
N=$(printf '%s' "$INV" | grep -c . || true)

if [ "$N" -eq 0 ]; then
  echo "extract-arms: UNEXTRACTABLE — $SUITE printed no per-arm verdict line (exit $RC), so its"
  echo "extract-arms: inventory cannot be compared and it must not be ported under this unit."
  echo "extract-arms: An empty inventory compares equal to an empty inventory, which would certify"
  echo "extract-arms: a port that dropped every arm."
  exit 3
fi

if [ -n "$OUT" ]; then
  printf '%s\n' "$INV" > "$OUT"
  echo "extract-arms: $N arm(s) from $SUITE (suite exit $RC) -> $OUT"
else
  printf '%s\n' "$INV"
fi
exit 0

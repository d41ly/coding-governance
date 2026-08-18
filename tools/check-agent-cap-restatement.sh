#!/usr/bin/env bash
# check-agent-cap-restatement — no live prose ASSERTS a fan-out bound as a bare number.
#
# The number the hook enforces is adjustable per repo (TOOL-aDeclaredBound-4). A document that
# states it as a digit is a second answer to a question that has a declared first one, and this repo
# already ruled on that shape for the kit version: a version written in prose rots between bumps.
#
#   bash tools/check-agent-cap-restatement.sh          # the gate
#
# WHAT THIS CANNOT SEE, stated rather than left for a reader to assume complete:
#
#   * The NOUN LIST IS A LIST. A carrier phrased outside it -- "no more than five reviewers", a
#     bound implied without a noun -- is invisible. This was OBSERVED, not imagined: the first
#     tightening of this pattern silently dropped `≤5 batched default-refute skeptics` from the
#     review protocol, twice, because `skeptics` was not yet in the list.
#     It happened AGAIN while this gate was being built: the list carried `are verify-stage` but
#     not the bare `verify-stage`, so it missed `≤5 verify-stage agents TOTAL` — the single line
#     `check-protocol-parity.test.sh` freezes, and the most important carrier in the corpus. Two
#     misses in one unit is the measurement behind this warning, not a hypothetical.
#   * EXECUTABLE FILES ARE OUT OF SCOPE. A bound stated in a comment inside a harness is not seen.
#     Also observed: `tools/workflows/tier2-review.js` says `≤5 concurrent` on one line and
#     `ONE ≤6-wide wave` on another while its code fans at 5, and this gate cannot arbitrate that.
#     Filed as TOOL-aDeclaredBound-6. Widening to source is what took the false-positive rate to
#     64% when it was measured, which is why the scope stops at markdown.
#
# A BOUND WORD must be adjacent to the number. That is what separates an ASSERTION from a
# MEASUREMENT: this corpus records four runaway reviews at "79 / 54 / 48 / 37 agents" and a tier
# table reading "~22 agents", and none of those becomes wrong when the cap moves.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "agent-cap-restatement: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

WAIVERS=${WAIVERS:-tools/agent-cap-restatement-waivers.txt}

# FROZEN trees, excluded by PATH PREFIX rather than by matched text. These are append-only records
# of past or pending state: a build record, an archive, a bug-class record and a backlog row each
# QUOTE a carrier to describe what was true or what is outstanding. Keying their exclusion on text
# would silence the live carriers that share their sentences, which is why it is a prefix.
FROZEN='^memory/(builds|archive|gotchas|backlog)/'

BOUND='(≤|<=|at most|never more than|no more than|up to|maximum of|max of|capped at|only)'
NOUN='(agents?|verifiers?|lens(es)?|skeptics?|concurrent|verify-stage|per verify stage|are verify-stage|ever run|batched)'
PAT="$BOUND ?[0-9]+ ?$NOUN"

pop=$(git ls-files '*.md' | grep -vE "$FROZEN" || true)
# VACUITY: a scanner whose population is empty passes by finding nothing, which is this repo's own
# named class. An empty selection is a refusal, never a green.
[ -n "$pop" ] && [ "$(printf '%s\n' "$pop" | grep -c .)" -gt 0 ] || {
  echo "agent-cap-restatement: the markdown population is EMPTY, so this gate would pass by finding nothing"
  exit 2
}

hits=$(printf '%s\n' "$pop" | xargs grep -InE "$PAT" 2>/dev/null || true)

# WAIVERS key on the MATCHED TEXT, never on <path>:<line>. A line-keyed registry unpins itself
# whenever anything above it grows, which happened twice in one build to a sibling registry
# (TOOL-aLoosenedCeiling-5). Rows are `<matched text><TAB><reason>`; a row whose text no longer
# appears anywhere is STALE and reds, because a waiver outliving its hit silently widens the gate.
waived=$(grep -vE '^\s*(#|$)' "$WAIVERS" 2>/dev/null | cut -f1 || true)

status=0
bad=""
while IFS= read -r h; do
  [ -n "$h" ] || continue
  keep=1
  while IFS= read -r w; do
    [ -n "$w" ] || continue
    case "$h" in *"$w"*) keep=0; break ;; esac
  done <<EOF
$waived
EOF
  [ "$keep" = 1 ] && bad="$bad$h
"
done <<EOF
$hits
EOF

if [ -n "${bad%$'\n'}" ]; then
  echo "AGENT-CAP-RESTATEMENT FAILED — live prose asserts a fan-out bound as a bare number."
  echo "  The bound is DECLARED and adjustable; a digit here is a second answer that goes stale the"
  echo "  day someone turns the knob. Point at the file that resolves it, or add a row to $WAIVERS"
  echo "  with the reason it must stay (rows key on the matched TEXT, not on a line number)."
  printf '%s' "$bad" | sed 's/^/  /'
  status=1
fi

# STALE WAIVERS: a row whose text matches nothing in the live population.
while IFS= read -r w; do
  [ -n "$w" ] || continue
  case "$hits" in
    *"$w"*) ;;
    *) echo "AGENT-CAP-RESTATEMENT FAILED — a waiver row matches nothing, so it excuses a hit that is gone: '$w'"; status=1 ;;
  esac
done <<EOF
$waived
EOF

[ "$status" = 0 ] && echo "agent-cap-restatement: clean — $(printf '%s\n' "$pop" | grep -c .) markdown file(s) scanned, $(printf '%s\n' "$waived" | grep -c . || true) waiver(s)"
exit "$status"

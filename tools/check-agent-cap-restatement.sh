#!/usr/bin/env bash
# check-agent-cap-restatement — no live prose ASSERTS a fan-out bound as a bare number.
#
# The number the hook enforces is the hook's to state, and it is the only carrier a run actually
# obeys. A document that states it as a digit is a second answer to a question that already has an
# executable first one, and this repo has ruled on that shape before: a kit version written in prose
# rots between bumps. The digit is what rots; the pointer is what does not.
#
#   bash tools/check-agent-cap-restatement.sh [<waiver-registry>]
#
# The registry is a POSITIONAL, never an environment read. An env-settable registry path is a gate
# neutralised with no diff and no committed evidence -- the exact channel this build RETIRED one
# file over -- and a bare `WAIVERS` collides with any wrapper that exports one. A leg cannot set an
# env var anyway: the runner execs argv with no shell. Same reasoning as `check-template-size.sh`.
#
# WHAT THIS CANNOT SEE, stated rather than left for a reader to assume complete:
#
#   * The NOUN LIST IS A LIST. A carrier phrased outside it -- "no more than five reviewers" -- is
#     invisible. This was OBSERVED, not imagined, and it has now happened THREE times. The first
#     tightening silently dropped `<=5 batched default-refute skeptics`, because `skeptics` was not
#     yet listed. The second missed `<=5 verify-stage agents TOTAL` -- the single line
#     `check-protocol-parity.test.sh` freezes, and the most important carrier in the corpus. The
#     third was found by the build's closing review, which measured the shipped tree and found SIX
#     live carriers this gate reported clean over: `at most 5 verify agents TOTAL` (the canonical
#     target shape, missed because `verify` sat between the digit and `agents`), `the <=5 cap`,
#     `the <=5-verifier arity rule` and three `cap-5` spellings. Every one of those shapes is now
#     frozen as a fixture in the self-test, which is the only control that has ever caught this.
#   * A BOUND WITH NO NOUN AT ALL is invisible, and that is deliberate. `protocol's <=5`,
#     `resolve to an integer <= 5 is denied`, `The lens allowance is 5` -- each states the number
#     with nothing this gate can key on. Matching a bare `<=[0-9]+` would fire on every size,
#     timeout and byte budget in the corpus. These are found by a reader, not by this program; the
#     ones the closing review found were fixed at the source rather than pattern-matched.
#   * EXECUTABLE FILES ARE OUT OF SCOPE. A bound stated in a comment inside a harness is not seen.
#     Also observed: `tools/workflows/tier2-review.js` says `<=5 concurrent` on one line and
#     `ONE <=6-wide wave` on another while its code fans at 5, and this gate cannot arbitrate that.
#     Filed as TOOL-aDeclaredBound-6. Widening to source is what took the false-positive rate to
#     64% when it was measured, which is why the scope stops at markdown. The one carrier this cost
#     the build was a REMEDY STRING inside `tools/hooks/agent-cap.js`; it was fixed by reading, and
#     it is the standing argument for widening the population when someone has the budget.
#
# A BOUND WORD must be adjacent to the number. That is what separates an ASSERTION from a
# MEASUREMENT: this corpus records four runaway reviews at "79 / 54 / 48 / 37 agents" and a tier
# table reading "~22 agents", and none of those becomes wrong when the cap moves.
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "agent-cap-restatement: not a git repo"; exit 2; }
cd "$ROOT" || exit 2

WAIVERS=${1:-tools/agent-cap-restatement-waivers.txt}

# FROZEN trees, excluded by PATH PREFIX rather than by matched text. These are append-only records
# of past or pending state: a build record, an archive, a bug-class record and a backlog row each
# QUOTE a carrier to describe what was true or what is outstanding. Keying their exclusion on text
# would silence the live carriers that share their sentences, which is why it is a prefix.
#
# MEMORY_ROOT is READ, not assumed: the memory-tree kit makes the tree's location an adopter's
# choice and its own adopter tells them to edit it. A hardcoded `memory/` turns every record in a
# relocated tree into a live carrier, so the gate would red an adopter's whole history on install.
# Extracted rather than sourced -- sourcing a conf into this script would let it set PAT.
MEMORY_ROOT=$(sed -n 's/^MEMORY_ROOT=\(.*\)$/\1/p' .memory-tree.conf 2>/dev/null | head -1)
: "${MEMORY_ROOT:=memory}"
FROZEN="^$MEMORY_ROOT/(builds|archive|gotchas|backlog)/"

# PARITY-OWNED files, excluded by PATH because a STRONGER control already binds their numbers, and
# kept SEPARATE from FROZEN because the two exclusions are not the same claim. The shipped playbook
# is an operating ruleset an adopter reads standalone: "the total the hook resolves" is worse for
# them than a number they can act on. Its bounds are declared pairs in `check-playbook-parity.sh`,
# which asserts every stated digit equals the constant in `tools/hooks/agent-cap.js` that owns it --
# a CHECKED COPY, not a second answer, and a stronger guarantee than deletion.
#
# Two gates demanded opposite things here: the parity pair `lens-array bound` REQUIRES the playbook
# to spell `array LITERAL of ≤5 elements` and reds when that extraction matches nothing, while this
# gate banned the same digit. Resolved in favour of the gate that CHECKS the number over the gate
# that removes it, and the other three playbook bounds were given pairs of their own in the same
# commit so the exclusion covers nothing that is merely unwatched.
PARITY_OWNED='^parallel-coding-governance\.template\.md$'
PARITY_GATE=tools/check-playbook-parity.sh

# The exclusion is only honest while those pairs exist. ASSERT it rather than trusting the comment
# above: an excluded file whose pairs were deleted is a hole that reports as a boundary, and this
# gate's whole subject is a claim that stopped being true while its carrier still said it.
# Asserted only when the exclusion actually EXCLUDED something. A tree that ships no playbook has
# no hole to open, and demanding the pairs there would make every adopter and every scratch fixture
# refuse over a file they do not have.
_excluded=$(git ls-files -z '*.md' | tr '\0' '\n' | grep -cE "$PARITY_OWNED" || true)
# `grep -c` PRINTS 0 and EXITS 1 when it matches nothing, so `|| echo 0` appended a second line
# and made `[` compare a two-line string. An absent file prints nothing at all, hence the default
# below rather than a second echo.
_pairs=$(grep -cE '^[^~]+~\$TEMPLATE~.*\[0-9\]' "$PARITY_GATE" 2>/dev/null || true)
: "${_pairs:=0}"
[ "$_excluded" -eq 0 ] || [ "$_pairs" -ge 1 ] || {
  echo "agent-cap-restatement: the playbook is excluded here because $PARITY_GATE binds its numbers,"
  echo "  and that file now declares NO digit-extracting pair over it. The exclusion has become a hole:"
  echo "  either restore the pairs or delete PARITY_OWNED and let this gate scan the playbook again."
  exit 2
}

BOUND='(≤|<=|at most|never more than|no more than|up to|maximum of|max of|capped at|only)'
NOUN='(agents?|verifiers?|lens(es)?|skeptics?|helpers?|verify|cap|concurrency|concurrent|verify-stage|per verify stage|are verify-stage|arity|ever run|batched)'
# THREE shapes, because the corpus writes it three ways and a pattern derived from one of them
# certified the other two green. Each was MEASURED against this tree, not imagined:
#   FWD  bound then number then noun -- `≤5 agents`, `at most 5 verify agents`, `≤5-verifier`.
#        The separator is `[ -]?` and not ` ?` because `≤5-verifier` hyphenates it.
#   REV  `cap-5`. Deliberately ONLY `cap`, not the whole noun list: `agents?-[0-9]+` matched the
#        node-registry hostname `agent-0` in AGENTS.md, a false positive measured and removed.
#   NB   noun then bound then number -- `CONCURRENCY ≤ 5, ALWAYS`, where the noun leads.
FWD="$BOUND[ -]?[0-9]+[ -]?$NOUN"
REV="cap-[0-9]+"
NB="$NOUN,? ?$BOUND ?[0-9]+"
PAT="($FWD)|($REV)|($NB)"

# The SCAN opens one file at a time and checks grep's exit code on each. The batched form
# (`xargs grep`) was three defects at once: newline-delimited paths split any filename holding a
# space, `2>/dev/null || true` ate both the error text and the exit code so a failed scan read as
# no hits, and the file count was taken from the LIST rather than from what grep opened -- a count
# reported for files never read. `-H` is forced because a single-file batch otherwise prints a
# line number under a remedy telling the reader to go look at a file it does not name, and a fresh
# adopter tree is exactly the single-file case.
hits=""
scanned=0
while IFS= read -r -d '' f; do
  scanned=$((scanned+1))
  out=$(grep -HIniE "$PAT" -- "$f"); rc=$?
  [ "$rc" -le 1 ] || {
    echo "agent-cap-restatement: the SCAN FAILED on '$f' (grep exit $rc), so a clean verdict here would mean 'not looked at'"
    exit 2
  }
  [ -n "$out" ] && hits="$hits$out
"
done < <(git ls-files -z '*.md' | grep -zvE "$FROZEN" | grep -zvE "$PARITY_OWNED")

# VACUITY: a scanner whose population is empty passes by finding nothing, which is this repo's own
# named class. An empty selection is a refusal, never a green. Asserted on what was SCANNED.
[ "$scanned" -gt 0 ] || {
  echo "agent-cap-restatement: the markdown population is EMPTY, so this gate would pass by finding nothing"
  exit 2
}

# WAIVERS key on the MATCHED TEXT, never on <path>:<line>. A line-keyed registry unpins itself
# whenever anything above it grows, which happened twice in one build to a sibling registry
# (TOOL-aLoosenedCeiling-5). Rows are `<matched text><TAB><reason>`; a row whose text no longer
# appears anywhere is STALE and reds, because a waiver outliving its hit silently widens the gate.
waived=$(grep -vE '^\s*(#|$)' "$WAIVERS" 2>/dev/null | cut -f1 || true)

# The hit's TEXT, with `<path>:<line>:` stripped. Matching a row against the whole hit line let a
# row reading `docs/` waive an entire subtree -- a path key accepted as a wildcard, by a registry
# whose own contract says it never keys on a path. The staleness arm reads the same stripped set,
# or a path-only row would be excused from the check that is supposed to drain it.
texts=$(printf '%s' "$hits" | sed 's/^[^:]*:[0-9]*://')

status=0
bad=""
while IFS= read -r h; do
  [ -n "$h" ] || continue
  htext=${h#*:}; htext=${htext#*:}
  keep=1
  while IFS= read -r w; do
    [ -n "$w" ] || continue
    case "$htext" in *"$w"*) keep=0; break ;; esac
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
  echo "  The hook is the carrier a run obeys; a digit here is a second answer that goes stale the"
  echo "  day the hook's value changes. Point at the file that resolves it, or add a row to $WAIVERS"
  echo "  with the reason it must stay (rows key on the matched TEXT, not on a line number)."
  printf '%s' "$bad" | sed 's/^/  /'
  status=1
fi

# STALE WAIVERS: a row whose text matches nothing in the live population.
while IFS= read -r w; do
  [ -n "$w" ] || continue
  case "$texts" in
    *"$w"*) ;;
    *) echo "AGENT-CAP-RESTATEMENT FAILED — a waiver row matches nothing, so it excuses a hit that is gone: '$w'"; status=1 ;;
  esac
done <<EOF
$waived
EOF

[ "$status" = 0 ] && echo "agent-cap-restatement: clean — $scanned markdown file(s) scanned, $(printf '%s
' "$waived" | grep -c . || true) waiver(s)"
exit "$status"

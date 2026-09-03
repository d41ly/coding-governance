# Build brief — TOOL-dRetiredFork-7

**Serves:** journal TOOL-dRetiredFork-7

## What the unit is

inCMS's registry declares its `check-review-join.sh` row a POPULATION REPATH. It is not: it is +117
residual lines carrying a whole second arm plus two helpers, armed by a 550-line suite gov has never
reviewed and inCMS re-merges every pull.

ARM 2 catches the stage BEFORE arm 1: a harness fans out to N lens agents, drops the dead ones with
a falsy filter, and an all-dead wave arrives downstream as `[]` — identical to an all-clean wave. It
was observed LIVE in gov's own tier2-review: `clean: 0 findings` with agents_done 0 and four
ENOTFOUND errors, from a run that read no code at all. That is the charter's "a guard that shares a
variable with the thing it guards is not a guard": `allFindings.length === 0` was the proxy both for
"the diff is clean" and for "nothing ran".

## What ARM 2 honestly claims, and what it does not

The source comment is worth reading before widening anything. An earlier version keyed on an
identifier matching `\w*Dead` and told the reader to "refuse to report clean while that count is
non-zero" — a sentence about a property it never checked. Measured consequences: a harness that kept
the counter and hard-coded `note: 'clean: 0 findings'` PASSED; a correct harness whose counter was
named `deadLenses` went RED; and `.filter((r) => r)` was not judged at all.

So it decides only two things a source scan CAN decide: the wave's arity is taken by a length
SUBTRACTION into a named variable, with the name CAPTURED rather than matched; and that variable is
READ elsewhere in the file. The falsy drop is recognised as a FAMILY by balancing the filter
argument's parentheses, not by matching one spelling.

## What this pass does

1. S1 — absorb ARM 2, `isfalsy` and `falsydrop`, keeping gov's message shapes and its ONE exit-code
   contract (ratified F1: share arm 1's code rather than widen the contract every adopter inherits).
2. S2 — absorb only the arms not keyed on inCMS record ids. An arm keyed on a foreign corpus reds on
   absence rather than on behaviour and must not ship.
3. S3 — a liveness assertion on ARM 2's own population: an arm that scanned nothing reports the same
   zero as one that scanned everything.
4. S4 — bump the review-harness version and its `gov:kit` markers.

## THE PRE-WIRING RUN IS NOT OPTIONAL HERE

§4 Migration and AC4: gov gains an arm it does not have, so gov's own harnesses may trip it. Run the
predicate over the tree FIRST, print hits AND near-misses, and fix what it legitimately catches in
its own commit. F2 is a FACT-QUESTION whose answer is that run.

## AC5 is deliberately two-sided

A bare post-bump green cannot fail — the gate is already green before the unit starts. So the RED is
observed too, by reverting the review-harness marker and confirming the gate names that carrier.

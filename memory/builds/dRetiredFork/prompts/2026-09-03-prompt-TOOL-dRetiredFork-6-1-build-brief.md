# Build brief — TOOL-dRetiredFork-6

**Serves:** journal TOOL-dRetiredFork-6

## What the unit is

Both drift-audit harnesses build their `note` from a hand-written ternary. inCMS re-derives it from
the counters the run already computed. The two are MECHANICALLY incompatible — a consumer gate that
re-derives the expected sentence cannot be satisfied by a hand-written one — so one un-taken gov
decision generates two registry rows at that adopter. That is the argument, not a wording preference.

## The defect the ternary carries

It has three outcomes but conflates two of them. `!synth` gives UNVERIFIED, anything non-zero gives
PARTIAL, and everything else gives the bare string `complete`. "Nothing moved" and "the probe could
not run" both land in that last branch, and `complete` is a reassuring word for a run that measured
nothing. §7 requires every signal to carry a LIVENESS assertion, so a probe that cannot move says
DEAD PROBE instead of a zero.

## What this pass does

1. S1/S2 — `deriveLiveness(counters)` returning one of THREE states, and `renderLivenessNote(state)`
   rendering exactly one sentence per state, in both harnesses.
2. S3 — the dead-probe state prints DEAD PROBE.
3. S4 — three arms, one per state, with the DEAD PROBE arm observed RED against the ternary first.
4. S5 — bump `KIT_DRIFT_AUDIT_VERSION` and the FOUR places `check-kit-versions.sh` pairs it:
   `drift_report.py`, the README marker, and BOTH harnesses' `meta.version`.

## A DIVERGENCE from the spec's names, decided before coding

§2 names the helpers `livenessOf` and `livenessNote`. gov's lexicon table declares no `liveness`
verb and its offender pin is shrink-only, so both spellings would red the naming gate — the same
trade `TOOL-dRetiredFork-2` made one unit ago. They are `deriveLiveness` and `renderLivenessNote`:
`derive` is declared as "compute a value from a source so it never has to be authored", which is
precisely what replacing the hand-written ternary means, and `render` as "turn structure into text".
The spec is amended first with its section 9 line, per M2.

## Ratified fork, folded

F1 — the sentence BECOMES a declared contract; `tools/drift-audit/README.md` states the three states
and their sentences so a later editor knows the cost, and the version bump carries it.

## Acceptance

AC1-AC5, run rather than asserted. Then `--check-format` before committing.

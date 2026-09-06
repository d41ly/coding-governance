**Serves:** spec-audit TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-6

# Spec audit round 2 — the fold's own defects, and the scope gap nobody had noticed

Tier-2 spec audit, round 2 · 2026-09-04 · node `a` · build `aSurfacedLexicon` · streams tooling ·
designs only, no code exists yet.

Round 1 is `2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md`: BLOCKED, 23 confirmed
findings — four blockers, thirteen highs, six mediums.

## Verdict: CLEAN WITH FIXES

**Confirmed-blocker count, by subject.** Unit 5: 4 to 0. Unit 6: 7 to 0. Unit 9: 8 to 0. Strictly
smaller and zero in all three, so the loop CONVERGED for each.

**Shape of the round, stated because it was not one pass.** The fold closed 22 of 23. An adversarial
verifier then graded every finding against the file and found the FOLD had introduced or exposed
seven more — the `fold-text-is-unreviewed-surface` class, where a round's fixes become fresh prose
nobody has reviewed and that prose is where the next findings are. A second fold closed all seven.
A third pass, single-writer, closed what the second fold's concurrency had produced.

## The scope gap, which is the finding worth reading

Two specs routed the `CELLS` matrix paste and the promotion of the undeclared-cell arm from
report-only to refusal at `TOOL-aSurfacedLexicon-12`. **That unit had never heard of either.** A grep
for `CELLS` over it returned zero, and its declaration-rewrite scope item touches only the pin region.

Unit 6 found it and did the right thing rather than the convenient one: it refused to call a deferral
a routing, wrote out the exact paragraph a receiving unit must carry, and left the item explicitly
UNOWNED for the orchestrator to route. That is what got it fixed. A spec that had quietly said "unit
12 handles this" would have shipped a build whose last unit silently dropped an arm it never knew it
was supposed to flip on.

Unit 12 now accepts it. The acceptance criterion asserts the matrix and the arming constant land in
the SAME COMMIT, evaluated over the commit rather than over the tree, because the two landing
separately is precisely the failure the item exists to prevent and a tree-scoped check cannot see it.

## The constraint that reaches every remaining unit

`VERB_OFFENDER_PIN` stands at 461 with EXACTLY ZERO headroom, and offenders are counted per
OCCURRENCE, not per distinct name. Any unit minting a function whose leading verb the declared table
refuses reds `lexicon naming predicates` — which is the same leg several of these units nominate for
observing their own criteria.

Unit 5's `classify` does exactly that: staged, `graded` moves 1045 to 1049 and `offenders` 461 to
462, exit 1. It now budgets the raise as a criterion naming `classify` as the sole arrival.

The distinction that stops this being over-budgeted was measured rather than assumed: `graded` moved
by four while `offenders` moved by one, because module-body assignments are not graded by a predicate
that reads function definitions. Unit 6 staged its own four names on the same basis and measured a
ZERO offender delta, so it raises no pin at all. A spec that reasoned from the finding instead of
re-running it would have budgeted a raise it does not need.

## What the concurrency cost, and the rule that comes out of it

Three of the seven round-2 defects, and five more found after them, were all one shape: **prose
asserting what a sibling spec says, written without opening it — or written correctly and then
falsified when the sibling moved under it.** One fold wrote that two siblings "are amended to name
this row as the exception"; one was untouched and the other had never carried the sentence it was
quoted as saying.

Concurrent agents editing documents that cite each other cannot fix this by trying harder. The
reconciliation was therefore done in a single-writer pass over the whole set, which is the shape this
class actually needs.

Residual, recorded rather than chased: four specs cite a sibling by REV NUMBER, and every one of
those labels is already stale. The claims they attach to were re-verified and hold. Citing a sibling's
rev is a rotting reference by construction and the specs should cite the id alone; that is a habit to
fix at authoring time, not a defect to patch in each carrier.

## The limit of this round

As in batch A: the staged experiments were observed once by the agent that staged them and confirmed
here by reading the code that decides them, not by re-staging. Every observed-RED obligation these
specs carry is owed AGAIN at build time, against real code. No spec-audit round can pay it early.

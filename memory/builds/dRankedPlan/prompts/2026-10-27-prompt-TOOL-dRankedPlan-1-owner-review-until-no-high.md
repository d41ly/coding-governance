**Serves:** research TOOL-dRankedPlan-1

# Owner instruction — stop the audit chain at the first round confirming no HIGH

## The prompt

> Cap the dRankedPlan spec-audit chain at the first round confirming no BLOCKER and no HIGH, as for dPlacedRequest,
> dDeclaredLoop and dKeptSession; close the rest under a recorded override, defer every unit, close and land.

— owner, 2026-10-27, answering the run's hand-off `owner-decision` at `3d57d3f16`, which parked the chain cap after
round 7.

> next round is the last review round

— owner, 2026-10-27, a second instruction while the run recorded the first, at `09158f565`. It bounds the cap: round 8
ends the chain whatever it confirms.

## What the run was doing

- Rounds 1 to 7 confirmed 1 blocker and then 9, 7, 7, 6, 9, 4 and 9 highs, at precision 1.00, 0.91, 0.93, 0.86,
  0.94, 0.92 and 0.93. M4 bounds the promotion chain only by precision, so with every round above the review
  protocol's floor the chain had no end; the run handed off rather than spend round 8 without a ruling.
- Round 7's promotions, `TOOL-dRankedPlan-68` to `-77`, are committed and not yet audited.

## How the run applies it

- Round 8, over `TOOL-dRankedPlan-68` to `-77`, is the last audit round, per the second instruction; no round 9 runs
  whatever round 8 confirms.
- Round 8's promotions, highs and minors batch alike, are kept, since a promoted unit is never retired, and close
  under a recorded override of `specs-audited` citing this record.
- Every unit is then deferred to the build run, the spec run closes by carry-forward (README rule 1), lands and is
  marked landed.
- The second park's alternative, re-scoping `TOOL-dRankedPlan-22`'s static caller check, is not taken: the owner
  chose the cap.

## The hand-off answer

> Raise the spec-tokens leg's ceiling in tools/gate-legs.json enough for the live chain's packet join, then resume
> dRankedPlan, re-run the close and land it.

— owner, 2026-10-27, answering the run's hand-off `owner-decision` at `be042d1e2`, which parked the close's red
spec tokens leg. The run adds `TOOL-dRankedPlan-82`, a Tier-1 micro-unit built in this run as `TOOL-dGroundRules-87`
was, sizes the ceiling through `derive-ceilings.py --observed`, and then re-closes and lands.

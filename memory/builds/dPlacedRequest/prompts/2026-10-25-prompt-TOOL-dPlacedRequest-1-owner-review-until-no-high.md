**Serves:** research TOOL-dPlacedRequest-1

# Owner instruction — audit until a round confirms no HIGH, then stop

## The prompt

> stop auditing specs once there are no more highs left

— owner, 2026-10-25, while the spec audit's round 5 (run `wf_c4676d9d-71e`, `TOOL-dPlacedRequest-50` to `-52`) was
in its lens stage, after round 4's promotions were committed (`d0ea82ecc`).

## What the run was doing

- Rounds 1 to 4 confirmed 11, 8, 4 (with 1 BLOCKER) and 2 HIGHs, at precision 0.96, 0.98, 1.00 and 0.83, and
  promoted 12, 9, 6 and 3 units (`TOOL-dPlacedRequest-23` to `-52`). M4 bounds the promotion chain only by
  precision, so with every round above the review protocol's 0.5 floor the chain had no end in sight.

## How the run applies it

- The chain stops at the first round whose audit confirms no HIGH and no BLOCKER. Round 5 runs to its end; if it
  confirms a HIGH or a BLOCKER, its promotions are audited in round 6, and so on.
- That last round's findings are still disposed by severity: its MEDIUM and LOW findings are promoted to one batch
  unit, two only across disjoint write sets. Those last promotions are specced and carried forward unaudited,
  closing under a recorded override of `specs-audited` citing this record.
- Every unit is then deferred to the build run, and the spec run closes by carry-forward (README rule 1).
- The spec run's closing review over its spec commits is not run: the audit chain is the review of this spec-only
  diff, and the build run's closing diff review is unaffected.

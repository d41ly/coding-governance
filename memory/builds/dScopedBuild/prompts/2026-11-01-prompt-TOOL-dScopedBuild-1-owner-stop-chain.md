**Serves:** research TOOL-dScopedBuild-1

# Owner ruling — stop the audit chain at round 4

## The prompt

> This is the last audit round

— owner, 2026-11-01, in this run's session while spec-audit round 4 (`wf_5f827d4b-b03`, over
`TOOL-dScopedBuild-40` and `-41`) was at its disposal stage.

## What the run was doing

- Rounds 1 to 3 confirmed 48, 32 and 23 findings with no blocker, their highs 10, 3 and 1, at precision 0.96, 1.00
  and 0.88, and promoted 11, 4 and 2 units. M4 ends a chain only below the review protocol's 0.5 precision floor, so
  that bound was not in reach.

## How the run applies it

- The chain ends at round 4. Round 4's own promotions, if it makes any, are the only specs no spec-audit record names;
  they are kept, since a promoted unit is never retired, and close under a recorded override of `specs-audited`
  citing this record. Round 4's record and its folds are committed as every earlier round's were.
- Every unit, the 15 roster units and those the four audit rounds added, is deferred to the build run, and the spec
  run closes by carry-forward (README rule 1), lands and is marked landed.
- The spec run's closing review over its spec commits is not run, and `closing-review-recorded` closes under a
  recorded override citing this record: the audit chain is the review of this spec-only diff, as for dMindYourWords,
  dKeptSession, dLinkedLibrary and dIndexedDesign, and the build run's closing diff review is unaffected.

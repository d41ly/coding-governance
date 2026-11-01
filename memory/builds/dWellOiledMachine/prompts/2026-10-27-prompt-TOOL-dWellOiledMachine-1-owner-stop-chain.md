**Serves:** research TOOL-dWellOiledMachine-1

# Owner ruling — stop the audit chain at round 8

## The prompt

> this is the last review round

— owner, 2026-10-27, mid-run, after the round-8 spec audit had promoted `TOOL-dWellOiledMachine-122` to `-126`
and before round 9 was launched; it answers the question RUN.md parked after round 5, whether the stop rule ruled
for dPlacedRequest, dDeclaredLoop and dKeptSession applies here.

## What the run was doing

- Eight spec-audit rounds confirmed highs of 15, 10, 3, 2, 10, 5, 5 and 4, at precision 0.79 to 0.97. M4 ends the
  chain only below the precision floor of 0.5, and no round confirmed no HIGH, so neither bound had been reached.

## How the run applies it

- The run reads "this" as the round just finished: the chain ends at round 8 and no round 9 is launched. Its
  promotions `TOOL-dWellOiledMachine-122` to `-126`, the only specs no spec-audit record names, are kept, since a
  promoted unit is never retired, and close under a recorded override of `specs-audited` citing this record.
- Every unit, the 61 roster units and the 64 the eight audit rounds added, is deferred to the build run, and the spec
  run closes by carry-forward (README rule 1), lands and is marked landed.
- The spec run's closing review over its spec commits is not run: the audit chain is the review of this spec-only
  diff, as for dKeptSession and dLinkedLibrary, and the build run's closing diff review is unaffected.

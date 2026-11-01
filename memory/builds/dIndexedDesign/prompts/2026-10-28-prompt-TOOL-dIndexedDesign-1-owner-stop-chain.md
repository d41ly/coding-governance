**Serves:** research TOOL-dIndexedDesign-1

# Owner ruling — stop the audit chain at round 3

## The prompt

> Stop the audit chain as for dKeptSession and dLinkedLibrary: units 47-53 close under a recorded specs-audited
> override, override closing-review-recorded, defer every unit to the build run, then close and land.

— owner, 2026-10-28, answering the question RUN.md parked after round 3 (the run HELD `host-owner-action` until owner
at `6afe06d0`), which offered: run round 4, stop the chain as for dKeptSession and dLinkedLibrary, or re-scope the
refusal-site units.

## What the run was doing

- Three spec-audit rounds confirmed high findings of 6, 7 and 6, at precision 0.96, 0.85 and 0.84, with one blocker
  in round 1 and none after. Round 3's highs returned to TOOL-dIndexedDesign-41's refusal-site surface and to order
  slips between promoted units. The owner's standing rule stops a chain only at a round confirming no HIGH, and M4
  ends it only below the precision floor, so neither bound was in reach.

## How the run applies it

- The chain ends at round 3. Its promotions `TOOL-dIndexedDesign-47` to `-53`, the only specs no spec-audit record
  names, are kept, since a promoted unit is never retired, and close under a recorded override of `specs-audited`
  citing this record.
- Every unit, the 17 roster units and the 23 the three audit rounds added, is deferred to the build run, and the spec
  run closes by carry-forward (README rule 1), lands and is marked landed.
- The spec run's closing review over its spec commits is not run, and `closing-review-recorded` closes under a
  recorded override citing this record: the audit chain is the review of this spec-only diff, as for dKeptSession and
  dLinkedLibrary, and the build run's closing diff review is unaffected.
- TOOL-dIndexedDesign-38 §8 F1, parked for the owner, stays parked: the build run meets it at its fork sweep before
  its first unit.

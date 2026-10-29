**Serves:** research TOOL-dMindYourWords-1

# Owner ruling — stop the audit chain at round 3

## The prompt

> Stop as for dKeptSession

— owner, 2026-10-30, answering the question RUN.md parked after round 3 (the run HELD `host-owner-action` until owner
at `611d6388`), which offered: run round 4 over units 38-52, stop the chain as for dKeptSession, dLinkedLibrary and
dIndexedDesign, or re-scope the history-reading and provenance units.

## What the run was doing

- Three spec-audit rounds confirmed high findings of 7, 7 and 13, at precision 0.97, 0.90 and 0.89, with no blocker.
  Round 3's highs landed on git-history hardening the earlier promotions added (grafts, replace objects,
  `blame.ignoreRevsFile`, rename detection), and each round promoted more units than the last (8, 8, 15). The owner's
  standing rule stops a chain without asking only at a round confirming no HIGH, and M4 ends it only below the
  precision floor, so neither bound was in reach.

## How the run applies it

- The chain ends at round 3. Its promotions `TOOL-dMindYourWords-38` to `-52`, the only specs no spec-audit record
  names, are kept, since a promoted unit is never retired, and close under a recorded override of `specs-audited`
  citing this record.
- Every unit, the 17 roster units and the 31 the three audit rounds added, is deferred to the build run, and the spec
  run closes by carry-forward (README rule 1), lands and is marked landed.
- The spec run's closing review over its spec commits is not run, and `closing-review-recorded` closes under a
  recorded override citing this record: the audit chain is the review of this spec-only diff, as for dKeptSession,
  dLinkedLibrary and dIndexedDesign, and the build run's closing diff review is unaffected.

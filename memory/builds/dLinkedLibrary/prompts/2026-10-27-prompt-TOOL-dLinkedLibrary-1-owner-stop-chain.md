**Serves:** research TOOL-dLinkedLibrary-1

# Owner ruling — stop the audit chain at round 8

## The prompt

> Stop the audit chain now, as for dKeptSession: close TOOL-dLinkedLibrary-97 to -102 under a recorded override of
> specs-audited, defer every unit, close and land the spec run.

— owner, 2026-10-27, answering the question RUN.md parked after round 8 (the run HELD `host-owner-action` until
owner at `a28d77ad1`), which offered: keep auditing, stop the chain as for dKeptSession, or re-scope the CI census.

## What the run was doing

- Eight spec-audit rounds confirmed highs of 15, 10, 9, 5, 5, 4, 4 and 5, at precision 0.83 to 0.98. Every high since
  round 3 fell on TOOL-dLinkedLibrary-8's CI census, which reads CI YAML and its byte decoding by hand. The ruling of
  2026-10-27 (`2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-review-until-no-high.md`) stopped the chain only at a round
  confirming no HIGH, and M4 ends it only below the precision floor, so neither bound was reachable.

## How the run applies it

- The chain ends at round 8. Its promotions `TOOL-dLinkedLibrary-97` to `-102`, the only specs no spec-audit record
  names, are kept, since a promoted unit is never retired, and close under a recorded override of `specs-audited`
  citing this record.
- Every unit, the 25 roster units and the 66 the eight audit rounds added, is deferred to the build run, and the spec
  run closes by carry-forward (README rule 1), lands and is marked landed.
- The spec run's closing review over its spec commits is not run: the audit chain is the review of this spec-only
  diff, as for dKeptSession, and the build run's closing diff review is unaffected.
- The CI census's recurring class of finding is not re-scoped here; the build run meets it in TOOL-dLinkedLibrary-8
  and its promotions.

---
slug: aLiftedCeiling
node: a
opened: 2026-11-12
streams: tooling
roster: TOOL
ids: TOOL-aLiftedCeiling-1
authorized-by: prompt
status: OPEN
---

# aLiftedCeiling — the instruction-edits leg's ceiling covers its wait on the tag index

## The problem this build exists to solve

Since aQueuedIndex, a second writer of the shared tag index waits for the first instead of failing. The `instruction edits
(manifest checks)` leg declares a 180 s ceiling, under its partner `tags (the resolver's checks)` at 420 s, so on a loaded host
its wait runs past the ceiling and the bar retries it; that happened at both of aQueuedIndex's bars on 2026-11-12. The owner
asked to raise it; the prompt is in `prompts/`.

## Expected improvements

- A bar no longer pays a timed-out run and a retry of the instruction-edits leg when it waits on the tag index.

## Detriments if this is not built

- Every loaded parallel bar can spend the leg's whole ceiling, then run it again.
- A retried leg reads as a timeout in the bar's records, which hides a real one.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-1: one declared value in the bar's manifest.
- Ceilings carry evidence; the raise is argued from the leg's own readings.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aLiftedCeiling-1` | the instruction-edits leg's declared ceiling rises to cover a wait on the other tag-index writer's tree build |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-12 · streams tooling
ids TOOL-aLiftedCeiling-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

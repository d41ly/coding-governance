---
slug: aLiftedCeiling
node: a
opened: 2026-11-12
streams: tooling
roster: TOOL
ids: TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-2
authorized-by: prompt
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
| 2 | `TOOL-aLiftedCeiling-2` | the closing review's minor: the evidence row's source names the host load and the commit its race ran at |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node a · opened 2026-11-12 · streams tooling
ids TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aLiftedCeiling-1 — the instruction-edits leg's ceiling covers its wait on the tag index](spec/2026-11-12-spec-TOOL-aLiftedCeiling-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-11-12 |
| [TOOL-aLiftedCeiling-2 — the instruction-edits evidence row names its host load and its clone's commit](spec/2026-11-12-spec-TOOL-aLiftedCeiling-2.md) | 2 | 1 | CLOSED | rev-1 | 2026-11-12 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aLiftedCeiling-1 TOOL-aLiftedCeiling-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aLiftedCeiling-1` | no |
| 2 | `TOOL-aLiftedCeiling-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

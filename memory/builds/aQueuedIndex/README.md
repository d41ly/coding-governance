---
slug: aQueuedIndex
node: a
opened: 2026-11-12
streams: tooling
roster: TOOL
ids: TOOL-aQueuedIndex-1
authorized-by: prompt
---

# aQueuedIndex — writers of the shared tag index queue instead of failing

## The problem this build exists to solve

Two bar legs, `tags (the resolver's checks)` and `instruction edits (manifest checks)`, both write the node's shared tag index.
When they meet an unbuilt tree in one bar, one of them reds with `database is locked`, and the bar reads the red as the
run's own. dOrderedCharter's close lost a leg this way in four bars of five on 2026-11-12, two of them pre-push bars that
blocked its landing. The owner asked to fix it; the prompt is in `prompts/`.

## Expected improvements

- A bar no longer reds on the tag index when its two writers meet one unbuilt tree.
- A writer that waited reuses the tree the other writer built instead of rebuilding it.

## Detriments if this is not built

- Every parallel bar keeps a coin-flip red on one of the two legs, and every landing pays a serial bar to get past it.
- Each flake reads OWN, so the inherited-red policy cannot wave it through.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: it changes how every kit reader opens the shared index.
- The race is reproduced in a scratch clone at BASE before the fix and observed green after it.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aQueuedIndex-1` | every write to the shared tag index takes its lock first and waits past a full tree build, and a writer that waited re-reads whether the tree was built before building it |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 1 unit(s) · node a · opened 2026-11-12 · streams tooling
ids TOOL-aQueuedIndex-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aQueuedIndex-1 — writers of the shared tag index queue instead of failing](spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md) | 1 | 2 | DEFERRED | rev-2 | 2026-11-12 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aQueuedIndex-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aQueuedIndex-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

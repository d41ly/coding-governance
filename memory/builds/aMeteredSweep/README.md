---
slug: aMeteredSweep
node: a
opened: 2026-10-08
streams: tooling
roster: TOOL
ids: TOOL-aMeteredSweep-1
---

# aMeteredSweep — a profiled full bar with every self-test, its reds fixed, its cost read

## The problem this build exists to solve

Nobody had run the whole bar with every self-test since aGraftedHelix and aMendedFleet landed, and
the owner asked for one over local `main` reconciled with `origin/main`: profiled, every red fixed,
then the runner and each slow leg researched for how to reach their goals faster. A bar holding the
self-tests runs for hours on node `a`, so its reds accumulate unseen between such runs.

## Expected improvements

- The bar with every self-test runs green on the reconciled `main`.
- The unattended driver's `--claims` answers inside the orientation card's bound on a loaded node.
- Every slow leg has a measured, ranked lever, so the next speed build starts from a reading.

## Detriments if this is not built

- Nine reds keep riding `main`, each hiding the next red in the same leg.
- Every session card keeps printing `--claims did not answer`, so remote run claims stay unknown.
- Speed work keeps raising ceilings instead of removing the spawns that cost the time.

## Build-level rules

One Tier-1 unit fixes the reds; the speed findings are a research record and are proposed, not
built. Every timing names the load it was taken under: the bar ran beside another repository's bar
with used memory at 94 to 96 percent, and a contended number is reported as one.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aMeteredSweep-1` | OPEN | the nine reds of the profiled full bar, each fixed at its cause |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-10-08 · streams tooling
ids TOOL-aMeteredSweep-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aMeteredSweep-1 — every red of a full bar with self-tests on the reconciled main, fixed](spec/2026-10-08-spec-TOOL-aMeteredSweep-1.md) | 1 | 1 | OPEN | rev-4 | 2026-10-08 |
<!-- /gen:build-units -->

Records: 9 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aMeteredSweep-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aMeteredSweep-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

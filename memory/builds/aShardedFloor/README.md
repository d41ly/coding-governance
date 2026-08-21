---
slug: aShardedFloor
node: a
opened: 2026-08-21
streams: tooling
roster: TOOL
ids: TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4
---

# aShardedFloor — move the floor, then see the queue

Node `a` · opened 2026-08-21 · streams tooling.

`aScannedThrottle` measured this repo's merge bar and landed a report; it changed nothing, by design.
This build lands the recommendations that report ranked. Its own headline finding binds everything
here: **the bar is FLOOR-bound.** One leg exceeds leg-seconds ÷ width on every reconstructed bar, so
no width change, no extra worker and no faster sibling leg moves the span. Only the floor moves it.

## What this build does

Sharding the two `unattended` selftests is the whole win — 292 s (27.6 %) on one measured bar and
282 s (30.5 %) on another. **Both must move together**: sharding the driver alone buys 3.7 %, because
the gate selftest simply becomes the new floor. Two shards each is sufficient, and past that the bar
is throughput-bound at ~766 s and further splitting buys exactly zero.

The queue key buys **0 s of span** and ships anyway: a lander queueing behind one peer experiences
~31–35 min where every span the report measured reads ~16, and today that wait is printed to stdout
and recorded nowhere.

The design, its measurements and every gate pin each unit moves are in
[the research record](build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md). The specs cite it rather
than restating it.

## What this build does NOT do

It does not widen the pool, shard a third time, or touch `gate-profiles.txt` — all three are measured
dead ends in that report. It does not fix `input_key`'s tree-not-commit hole, which
`TOOL-aShardedFloor-4` would make routine rather than rare; that is its own unit and its own risk.

<!-- gen:build-index -->
**Build status:** BLOCKED · 4 unit(s) · node a · opened 2026-08-21 · streams tooling
ids TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aShardedFloor-1 — record the turnstile queue wait in the run record](spec/2026-08-21-spec-TOOL-aShardedFloor-1.md) | OPEN | rev-1 | 2026-08-21 |
| [TOOL-aShardedFloor-2 — the shard contract, and the driver selftest split by it](spec/2026-08-21-spec-TOOL-aShardedFloor-2.md) | OPEN | rev-1 | 2026-08-21 |
| [TOOL-aShardedFloor-3 — the gate selftest, split by the same contract](spec/2026-08-21-spec-TOOL-aShardedFloor-3.md) | OPEN | rev-1 | 2026-08-21 |
| [TOOL-aShardedFloor-4 — the dispatch hint reads a repository-wide store](spec/2026-08-21-spec-TOOL-aShardedFloor-4.md) | BLOCKED | rev-1 | 2026-08-21 |
<!-- /gen:build-units -->

Records live under `spec/` and `build/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md](build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md) | research | TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4 |

Ids no `spec-audit` record has ever named: TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4.
<!-- /gen:build-index -->


<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-21-spec-TOOL-aShardedFloor-1.md](spec/2026-08-21-spec-TOOL-aShardedFloor-1.md)
  - [2026-08-21-spec-TOOL-aShardedFloor-2.md](spec/2026-08-21-spec-TOOL-aShardedFloor-2.md)
  - [2026-08-21-spec-TOOL-aShardedFloor-3.md](spec/2026-08-21-spec-TOOL-aShardedFloor-3.md)
  - [2026-08-21-spec-TOOL-aShardedFloor-4.md](spec/2026-08-21-spec-TOOL-aShardedFloor-4.md)
- **`build/`**
  - [2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md](build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md)
<!-- /gen:build-docs -->

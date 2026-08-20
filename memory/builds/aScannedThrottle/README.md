---
slug: aScannedThrottle
node: a
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-aScannedThrottle-1 TOOL-aScannedThrottle-2 TOOL-aScannedThrottle-3 TOOL-aScannedThrottle-4 TOOL-aScannedThrottle-5 TOOL-aScannedThrottle-6 TOOL-aScannedThrottle-7
---

# aScannedThrottle — the lander is floor-bound, and the canary is not the floor

Node `a` · opened 2026-08-20 · streams tooling.

The owner reports the lander is extremely slow and does not use the machine, and names the canary
gates as a congestion target. This build measures rather than theorises, and it does so from
artifacts the bar already writes: `aMeteredTurnstile` gave the runner a per-leg run record whose
rows carry each leg's own start and end in nanoseconds, so a bar's entire schedule can be
reconstructed after the fact without running anything.

## What the measurement says

Four real `GATE_FULL=1` width-8 bars on node `a` reconstruct to spans of 925–1051 s at 60–70 %
pool utilization. Every one is FLOOR-bound: the single longest leg exceeds leg-seconds over width,
so no amount of width moves the span. `run-gates canary` is the third-largest leg at 466–587 s and
sits entirely in the shadow of the two `unattended` selftests. Deleting it outright moves the
bar's wall clock by 0.0 %.

The genuinely new finding is upstream of all of that: the dispatch hint is stored per WORKTREE and
was renamed without migrating the old file, so 24 of 26 worktrees on this node have none. A bar with
no hint dispatches in MANIFEST order and starts its 900-second floor leg 158–164 s late — measured
as a controlled pair, two consecutive runs in one worktree, hint absent then present.

## What this build does NOT do

It changes no scheduling, shards no leg and edits no runner. Every improvement is emitted as a
recommendation against an existing backlog id or a new one; landing any of them is a separate unit.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-20 · streams tooling
ids TOOL-aScannedThrottle-1 TOOL-aScannedThrottle-2 TOOL-aScannedThrottle-3 TOOL-aScannedThrottle-4 TOOL-aScannedThrottle-5 TOOL-aScannedThrottle-6 TOOL-aScannedThrottle-7

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aScannedThrottle-1 — measure the lander, find what actually binds its wall clock](spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md) | OPEN | rev-1 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/` and `build/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-20-build-TOOL-aScannedThrottle-1.md](build/2026-08-20-build-TOOL-aScannedThrottle-1.md) | journal | TOOL-aScannedThrottle-1 |

Ids no `spec-audit` record has ever named: TOOL-aScannedThrottle-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-TOOL-aScannedThrottle-1.md](spec/2026-08-20-spec-TOOL-aScannedThrottle-1.md)
- **`build/`**
  - [2026-08-20-build-TOOL-aScannedThrottle-1.md](build/2026-08-20-build-TOOL-aScannedThrottle-1.md)
<!-- /gen:build-docs -->

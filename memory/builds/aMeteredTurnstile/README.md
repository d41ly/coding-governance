---
slug: aMeteredTurnstile
node: a
opened: 2026-08-20
streams: tooling
roster: TOOL
ids: TOOL-aMeteredTurnstile-1 TOOL-aMeteredTurnstile-2 TOOL-aMeteredTurnstile-3 TOOL-aMeteredTurnstile-4 TOOL-aMeteredTurnstile-5 TOOL-aMeteredTurnstile-6
---

# aMeteredTurnstile — the bar gets an instrument before it gets another fix

Node `a` · opened 2026-08-20 · streams tooling.

Two builds have already made this bar faster. `aTimedTurnstile` replaced the serial loop with a
bounded pool, and `aPacedTurnstile` carries seven specs on scheduling discipline. Both were designed
against a measurement taken by hand, once, and never repeated. The owner now reports the bar is
extremely slow and getting slower, and this repo cannot answer whether that is true.

## Why it cannot answer

The only longitudinal artifact is `<git-dir>/gate-timings.tsv`, and it is a dispatch hint that was
never designed to be a performance record. It is last-write-wins across runs taken at different pool
widths under different concurrent load. It carries no run identity, no timestamp, no width, no
commit, and no host. It never evicts a renamed leg, so it accumulates rows for legs that no longer
exist. Measured on node `a` at commit `56b945c`: 88 rows against 85 manifest legs.

Reading that file as a profile is how a stale number becomes a plan.

## What this build does

It adds one instrument to the `run-gates` kit and uses it once, properly. The instrument records a
run rather than a leg, classifies the bar into a regime, and appends rather than overwrites, so a
second measurement next month is comparable to this one. Adopters get the same instrument, because
the regime classification is a property of any bounded-pool gate bar and not of this repo's legs.

## What this build does NOT do

It changes no scheduling and fixes no leg. It does not modify `tools/run-gates/run-gates.sh`, which
`aPacedTurnstile` is actively editing. Every improvement it identifies is emitted as a recommendation
against an existing backlog id or a new one, and landing any of them is a separate unit.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-08-20 · streams tooling
ids TOOL-aMeteredTurnstile-1 TOOL-aMeteredTurnstile-2 TOOL-aMeteredTurnstile-3 TOOL-aMeteredTurnstile-4 TOOL-aMeteredTurnstile-5 TOOL-aMeteredTurnstile-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aMeteredTurnstile-1 — the merge bar gets an instrument, not another guess](spec/2026-08-20-spec-TOOL-aMeteredTurnstile-1.md) | INPROGRESS | rev-3 | 2026-08-20 |

Records live under `spec/` and `build/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-TOOL-aMeteredTurnstile-1.md](spec/2026-08-20-spec-TOOL-aMeteredTurnstile-1.md)
- **`build/`**
  - [2026-08-20-build-TOOL-aMeteredTurnstile-1.md](build/2026-08-20-build-TOOL-aMeteredTurnstile-1.md)
<!-- /gen:build-docs -->

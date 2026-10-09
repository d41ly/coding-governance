---
slug: aSparedSpawn
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
parents: aMeteredSweep
status: OPEN
ids:
---

# aSparedSpawn — the bar and its self-tests, rebuilt around the cost of a process

## The problem this build exists to solve

On node `a` the full bar with every self-test costs 4 to 7 hours and the unattended suites more,
and every earlier speed build moved that cost around without lowering it. aMeteredSweep measured why:
the cost is process creation, 21 ms a spawn quiet and up to 0.8 s loaded under MSYS against 1.2 ms
in WSL2 on the same machine, multiplied by arms that each launch a whole checker, and the arms
roughly doubled in six weeks while nothing retires one.

## Expected improvements

- A self-test arm costs milliseconds, not a process.
- The self-test tier runs where a spawn is cheap.
- The bar runs only what a change can affect.
- The refusal surface has a budget and a retirement path.

## Detriments if this is not built

- Kit work stays unverifiable in practice: its suites cost a working day each.
- Every new refusal keeps adding minutes the next build has to win back.
- Clock-bound arms keep redding on a loaded host and teach people to re-run.

## Build-level rules

- Measure before and after every unit, quiet and loaded, and record the instrument beside it.
- A rebuilt suite keeps its arm inventory and every staged break, compared before and after.
- The bar's authority does not move: no unit lets a reused or relocated verdict stamp a full green.

## Parked decisions

- Which units this build carries is the owner's call, from the menu in aMeteredSweep's round-two research,
  `memory/builds/aMeteredSweep/build/2026-10-09-build-TOOL-aMeteredSweep-1-research2-menu.md`.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-09 · streams tooling

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 0 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aMeteredSweep](../aMeteredSweep/README.md)
<!-- /gen:build-edges -->

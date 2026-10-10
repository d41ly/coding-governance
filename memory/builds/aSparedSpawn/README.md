---
slug: aSparedSpawn
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
parents: aMeteredSweep
ids: TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-7 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15
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

- The owner took all four tracks of the menu on 2026-10-09, with no spec audit. The forks the specs
  raise remain the owner's, each in its spec's open questions.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aSparedSpawn-1` | OPEN | the reuse key hashes what a dirty guarded file holds, and the toolchain it ran under |
| 2 | `TOOL-aSparedSpawn-2` | OPEN | the pool width comes from a measured spawn calibration, and dispatch pauses on spawn pressure |
| 3 | `TOOL-aSparedSpawn-3` | OPEN | a ceiling-killed leg retries in the pool's drain tail, and a bar with no ledger dispatches longest-first |
| 4 | `TOOL-aSparedSpawn-4` | OPEN | the runner's own spawns: a handful per leg, two git calls per bar, and a fork count with a ceiling |
| 5 | `TOOL-aSparedSpawn-5` | OPEN | the held self-test tier in WSL2, from an ext4 mirror, with combined verdicts |
| 6 | `TOOL-aSparedSpawn-6` | OPEN | the unattended driver as a library, called in process by its suite |
| 7 | `TOOL-aSparedSpawn-7` | OPEN | `--only` selectors for the unattended gate and the hygiene gate, each naming what ran |
| 8 | `TOOL-aSparedSpawn-8` | OPEN | fork-free readers, a spawn-idiom lint that stops regrowth, and a fork-count arm |
| 9 | `TOOL-aSparedSpawn-9` | OPEN | fixture templates and environment git identity across the named suites |
| 10 | `TOOL-aSparedSpawn-10` | OPEN | foreign-prefix parity probes one shard per sharded suite and pools its whole runs |
| 11 | `TOOL-aSparedSpawn-11` | OPEN | per-suite levers: five suites stop paying a process for a question they ask once |
| 12 | `TOOL-aSparedSpawn-12` | OPEN | the held self-test tier, selected by the kit whose shipped bytes moved |
| 13 | `TOOL-aSparedSpawn-13` | OPEN | content-addressed reuse: declared read classes, a shared cache, a soundness sample |
| 14 | `TOOL-aSparedSpawn-14` | OPEN | a refusal retirement review, and a growth budget beside the floors |
| 15 | `TOOL-aSparedSpawn-15` | OPEN | the remaining clock-bound arms on the flake list, ordered or calibrated |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 15 unit(s) · node a · opened 2026-10-09 · streams tooling
ids TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-7 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14
ids TOOL-aSparedSpawn-15

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSparedSpawn-1 — the reuse key hashes what a dirty guarded file holds, and the toolchain it ran under](spec/2026-10-09-spec-TOOL-aSparedSpawn-1.md) | 1 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-2 — the pool width comes from a measured spawn calibration, and dispatch pauses on spawn pressure](spec/2026-10-09-spec-TOOL-aSparedSpawn-2.md) | 1 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-5 — the held self-test tier in WSL2, from an ext4 mirror, with combined verdicts](spec/2026-10-09-spec-TOOL-aSparedSpawn-5.md) | 1 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-6 — the unattended driver as a library, called in process by its suite](spec/2026-10-09-spec-TOOL-aSparedSpawn-6.md) | 1 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-8 — fork-free readers, a spawn-idiom lint that stops regrowth, and a fork-count arm](spec/2026-10-09-spec-TOOL-aSparedSpawn-8.md) | 1 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-10 — foreign-prefix parity probes one shard per sharded suite and pools its whole runs](spec/2026-10-09-spec-TOOL-aSparedSpawn-10.md) | 2 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-11 — per-suite levers: five suites stop paying a process for a question they ask once](spec/2026-10-09-spec-TOOL-aSparedSpawn-11.md) | 2 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-15 — the remaining clock-bound arms on the flake list, ordered or calibrated](spec/2026-10-09-spec-TOOL-aSparedSpawn-15.md) | 2 | 1 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-3 — a ceiling-killed leg retries in the pool's drain tail, and a bar with no ledger dispatches longest-first](spec/2026-10-09-spec-TOOL-aSparedSpawn-3.md) | 2 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-4 — the runner's own spawns: a handful per leg, two git calls per bar, and a fork count with a ceiling](spec/2026-10-09-spec-TOOL-aSparedSpawn-4.md) | 2 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-7 — `--only` selectors for the unattended gate and the hygiene gate, each naming what ran](spec/2026-10-09-spec-TOOL-aSparedSpawn-7.md) | 2 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-9 — fixture templates and environment git identity across the named suites](spec/2026-10-09-spec-TOOL-aSparedSpawn-9.md) | 2 | 1 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-12 — the held self-test tier, selected by the kit whose shipped bytes moved](spec/2026-10-09-spec-TOOL-aSparedSpawn-12.md) | 3 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-13 — content-addressed reuse: declared read classes, a shared cache, a soundness sample](spec/2026-10-09-spec-TOOL-aSparedSpawn-13.md) | 3 | 2 | OPEN | rev-1 | 2026-10-09 |
| [TOOL-aSparedSpawn-14 — a refusal retirement review, and a growth budget beside the floors](spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md) | 3 | 2 | OPEN | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-7
TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9.

Ids no `spec-audit` record has ever named: TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6
TOOL-aSparedSpawn-7 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSparedSpawn-1`, `TOOL-aSparedSpawn-2`, `TOOL-aSparedSpawn-5`, `TOOL-aSparedSpawn-6`, `TOOL-aSparedSpawn-8` | yes |
| 2 | `TOOL-aSparedSpawn-10`, `TOOL-aSparedSpawn-11`, `TOOL-aSparedSpawn-15`, `TOOL-aSparedSpawn-3`, `TOOL-aSparedSpawn-4`, `TOOL-aSparedSpawn-7`, `TOOL-aSparedSpawn-9` | yes |
| 3 | `TOOL-aSparedSpawn-12`, `TOOL-aSparedSpawn-13`, `TOOL-aSparedSpawn-14` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aMeteredSweep](../aMeteredSweep/README.md)
<!-- /gen:build-edges -->

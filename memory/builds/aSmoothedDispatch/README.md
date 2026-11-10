---
slug: aSmoothedDispatch
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
ids: TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9 TOOL-aSmoothedDispatch-10 TOOL-aSmoothedDispatch-11 TOOL-aSmoothedDispatch-12 TOOL-aSmoothedDispatch-13 TOOL-aSmoothedDispatch-14 TOOL-aSmoothedDispatch-15 TOOL-aSmoothedDispatch-16 TOOL-aSmoothedDispatch-17 TOOL-aSmoothedDispatch-18 TOOL-aSmoothedDispatch-19 TOOL-aSmoothedDispatch-20
---

# aSmoothedDispatch — five mechanical refusals that cost every unattended run turns and re-dispatches

## The problem this build exists to solve

The driver journal across 38 runs logs 287 `--dispatch` refusals from the spec-token checker (947 min
of check time) and 197 "unknown argument" refusals, most of them bare paths after `--writes`. In
dFairHearing, builders' product edits were blocked 63 times by a card route still naming a closed unit.
Agents also declared the run-state file and asked for `--help`, and both were refused. Each refusal costs
a turn, a spec rewrite or a fresh builder. The analysis is in the brief under `prompts/`.

## Expected improvements

- `--dispatch` refuses only on this build's own spec-token reds, and re-checks only when its inputs move.
- `--writes a b c` and a quoted list declare every path.
- A dispatched unit's builder can write without a hand-appended route.
- `--help` answers, and a declared run-state file is dropped with a note.

## Detriments if this is not built

- Every run keeps paying ~12 min per spec-token refusal and a re-dispatch per miss.
- Agents keep losing turns to argument-shape refusals that carry no information.

## Build-level rules

- **Classification (M2)**: six units, each MISSING at open, Tier-2: each changes a shipped kit's contract.
- Units 1 to 4 edit `tools/unattended/unattended.sh`, unit 6 went into `tools/hooks/scratch-guard.js`, and every pass re-renders this README's index, so all units built one at a time (M6 clause 3).
- Units 8 and 9 were PROMOTED at the close: 8 batches the closing review's mediums and lows, 9 the three suite arms unit 1's split left red.
- Unit 7 was ADDED at spec time (M2): unit 5's writer found the hook already admits a one-spec run, so the writer's prompt must ask for it.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: the owner declined one.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aSmoothedDispatch-1` | `--writes` takes every path up to the next flag, and a whitespace-joined value splits into its paths |
| 2 | `TOOL-aSmoothedDispatch-2` | `--dispatch` drops the run-state file from its declared writes with a note instead of refusing |
| 3 | `TOOL-aSmoothedDispatch-3` | `unattended.sh --help` prints the verb list and exits 0 |
| 4 | `TOOL-aSmoothedDispatch-4` | `--dispatch`'s spec-token check grades the dispatching build's specs, and skips when its inputs match the last green check |
| 5 | `TOOL-aSmoothedDispatch-5` | scratch-guard lets `gov-spec-writer` run the spec-token checker over the spec it wrote |
| 6 | `TOOL-aSmoothedDispatch-6` | a dispatched unit counts as routed, so its builder's product writes are not refused on a stale card route |
| 7 | `TOOL-aSmoothedDispatch-7` | the `gov-spec-writer` role prompt has the writer run the spec-token checker's one-spec mode over its spec before returning |
| 8 | `TOOL-aSmoothedDispatch-8` | promoted from the closing review: round 1's three mediums and two lows, batched with the carried scratch-guard leg guard gap |
| 9 | `TOOL-aSmoothedDispatch-9` | the three driver-suite arms unit 1's split left red at the close: the stale `--dispatch` hostile-value exemption, and two carriage-return arms moved to a vertical tab |
| 10 | `TOOL-aSmoothedDispatch-18` | the three bar legs this build turned red: the driver's split without a here-string, four test lines respelled off kit paths, and `--help` anchored on its help page |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 10 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9 TOOL-aSmoothedDispatch-10 TOOL-aSmoothedDispatch-11
ids TOOL-aSmoothedDispatch-12 TOOL-aSmoothedDispatch-13 TOOL-aSmoothedDispatch-14 TOOL-aSmoothedDispatch-15 TOOL-aSmoothedDispatch-16 TOOL-aSmoothedDispatch-17 TOOL-aSmoothedDispatch-18 TOOL-aSmoothedDispatch-19 TOOL-aSmoothedDispatch-20

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSmoothedDispatch-1 — `--writes` takes every path up to the next flag, and splits a whitespace-joined value](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-2 — `--dispatch` removes the run-state file from its declared writes with a note instead of refusing](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-2.md) | 2 | 2 | CLOSED | rev-3 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-3 — `unattended.sh --help` prints the verb list and exits 0](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-4 — `--dispatch`'s spec-token check grades the dispatching build's specs, and skips when its inputs match the last admitted check](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-4.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-5 — the spec-token checker grades one named spec, so a spec writer can run it over its own](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-5.md) | 5 | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-6 — a dispatched unit counts as routed, so its builder's product writes are not refused on a stale card route](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-6.md) | 6 | 2 | CLOSED | rev-1 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-7 — the `gov-spec-writer` house overlay has the writer run the spec-token checker's one-spec mode over each spec before it returns](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-7.md) | 7 | 2 | CLOSED | rev-1 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-8 — the closing review's mediums and lows: the writer's row shape, an arm per admit clause and cache key, the no-field `--writes` arms, the context's step-9b read, and the hook leg's driver guard](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-8.md) | 8 | 2 | CLOSED | rev-1 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-9 — the three driver-suite arms unit 1's split left red: the stale `--dispatch` hostile-value exemption, and two carriage-return arms whose byte the substitution drops](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-9.md) | 9 | 1 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aSmoothedDispatch-18 — the three bar legs this build turned red: unit 4's loop read off a one-name local, four test lines respelled off kit paths, and `--help` anchored on a help page](spec/2026-11-10-spec-TOOL-aSmoothedDispatch-18.md) | 10 | 1 | CLOSED | rev-2 | 2026-11-10 |
<!-- /gen:build-units -->

Records: 21 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-18 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9.

Ids whose spec moved past its audited revision: none — 0 of 10 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSmoothedDispatch-1` | no |
| 2 | `TOOL-aSmoothedDispatch-2` | no |
| 3 | `TOOL-aSmoothedDispatch-3` | no |
| 4 | `TOOL-aSmoothedDispatch-4` | no |
| 5 | `TOOL-aSmoothedDispatch-5` | no |
| 6 | `TOOL-aSmoothedDispatch-6` | no |
| 7 | `TOOL-aSmoothedDispatch-7` | no |
| 8 | `TOOL-aSmoothedDispatch-8` | no |
| 9 | `TOOL-aSmoothedDispatch-9` | no |
| 10 | `TOOL-aSmoothedDispatch-18` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

---
slug: dTrackedAtlas
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4
---

# dTrackedAtlas — the Closed Loop Atlas states the project's and the chain's actual state, and knows when it is stale

## The problem this build exists to solve

The owner reads the Closed Loop Atlas as the design's current state. Regenerated at origin/main
`9e21ac760` it is byte-identical to the page of 2026-11-03, because its generator reads only
dClosedLoop's own records. It shows none of the six landed build runs, the fork picks, the re-grounds,
the deviation records or the as-built view, and its "today" side is the 2026-10-14 measurement. The
schedule script's build-state read counts 4 landed builds where 6 have landed, because a DEFERRED spec
blocks "done". The owner's prompt and the measurements are recorded under `prompts/`.

## Expected improvements

- The Atlas states each chain build's spec run, build run, landing, units, forks and deviations.
- The schedule and the Atlas read one build-state derivation, and both count 6 landed.
- A page the tree has moved past reds its own `--check`.
- The page regenerates on node d after a landing, with nobody remembering to.

## Detriments if this is not built

- The owner keeps reading a design page that omits every landed build run.
- "What can start next" keeps being answered by hand, against a script that says otherwise.
- A stale page keeps looking current, with nothing to say it is not.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, specced by the spec-writer role.
- **Nothing under `tools/`**: a touch there owes a `GATE_SELFTESTS=1` bar this run may not run.
- **No new file under `memory/builds/dClosedLoop/build/`**: each one grows dClosedLoop's held spec and
  reds spec tokens `[size]`. New code lives in this build's folder or in an existing instrument.
- The page is never committed or published; v2's text and the chain builds' specs stay as they are.
- No spec audit: the prompt asks for none, and a run may not opt itself in.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dTrackedAtlas-1` | one chain build-state derivation (spec run, build run, landing merge, unit counts, forks, revisions, deviations, claims, what can start), read by the schedule script in place of `tree_state` |
| 2 | `TOOL-dTrackedAtlas-2` | the Atlas renders the actual state: a view per chain build, and per comparison area the landed builds that moved "today" past the 2026-10-14 baseline, the as-built view beside v2's `[chain]` |
| 3 | `TOOL-dTrackedAtlas-3` | the page embeds its generation commit and input digest, and `--check` reds a page the tree has moved past |
| 4 | `TOOL-dTrackedAtlas-4` | the page regenerates on node d after a landing onto main, a switch whose default is on |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 4 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTrackedAtlas-1 — one chain build-state derivation, read by the schedule and the Atlas](spec/2026-11-19-spec-TOOL-dTrackedAtlas-1.md) | 1 | 1 | SPECCED | rev-2 | 2026-11-19 |
| [TOOL-dTrackedAtlas-2 — the Atlas renders the actual state of each chain build and each area](spec/2026-11-19-spec-TOOL-dTrackedAtlas-2.md) | 2 | 1 | SPECCED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-3 — the page carries the commit and input digest it was generated from, and `--check` reds a stale one](spec/2026-11-19-spec-TOOL-dTrackedAtlas-3.md) | 3 | 1 | SPECCED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-4 — the Atlas page regenerates on node d after main moves, behind a switch whose default is on](spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md) | 4 | 1 | SPECCED | rev-1 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 9 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4.

Ids whose spec moved past its audited revision: none — 0 of 4 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTrackedAtlas-1` | no |
| 2 | `TOOL-dTrackedAtlas-2` | no |
| 3 | `TOOL-dTrackedAtlas-3` | no |
| 4 | `TOOL-dTrackedAtlas-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

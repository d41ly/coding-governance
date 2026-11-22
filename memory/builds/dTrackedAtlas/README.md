---
slug: dTrackedAtlas
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-5 TOOL-dTrackedAtlas-6 TOOL-dTrackedAtlas-7 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 TOOL-dTrackedAtlas-12 TOOL-dTrackedAtlas-13 TOOL-dTrackedAtlas-14 TOOL-dTrackedAtlas-15 TOOL-dTrackedAtlas-16 TOOL-dTrackedAtlas-17 TOOL-dTrackedAtlas-18 TOOL-dTrackedAtlas-19
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
- **Nothing under `tools/`** but two rows the owner approved on 2026-11-19: unit 4's `[[hook]]` row in
  `tools/loop/loop.toml` and unit 18's schedule pin in `tools/chain-packet.py`.
- **No new file under `memory/builds/dClosedLoop/build/`**: each one grows dClosedLoop's held spec and
  reds spec tokens `[size]`. New code lives in this build's folder or in an existing instrument.
- The page is never committed or published; v2's text and the chain builds' specs stay as they are.
- No spec audit: the prompt asks for none, and a run may not opt itself in.

## Parked decisions

- **Unit 4 resumed** on the owner's word of 2026-11-19, which picked its fork F3's option (a).
- **The flagged bar** its `tools/` row owes stays unrun: the owner's standing rule forbids the unattended suites.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dTrackedAtlas-1` | one chain build-state derivation (spec run, build run, landing merge, unit counts, forks, revisions, deviations, claims, what can start), read by the schedule script in place of `tree_state` |
| 2 | `TOOL-dTrackedAtlas-2` | the Atlas renders the actual state: a view per chain build, and per comparison area the landed builds that moved "today" past the 2026-10-14 baseline, the as-built view beside v2's `[chain]` |
| 3 | `TOOL-dTrackedAtlas-3` | the page embeds its generation commit and input digest, and `--check` reds a page the tree has moved past |
| 4 | `TOOL-dTrackedAtlas-4` | the page regenerates on node d after a landing onto main, a switch whose default is on |
| 5 | `TOOL-dTrackedAtlas-8` | the fork scan passes no tree-derived text through shell source (closing review H1, promoted) |
| 6 | `TOOL-dTrackedAtlas-9` | a landing counts only on the default branch's first-parent line, never a run branch's prepared merge (closing review H2, promoted) |
| 7 | `TOOL-dTrackedAtlas-10` | the page's staleness digest covers the merge history the landed predicate reads (closing review H3, promoted) |
| 8 | `TOOL-dTrackedAtlas-11` | the closing review's minors: the owed pane observations recorded, one reader for valued options, the stale ledger line cleared (M1, L1, L2, promoted) |
| 9 | `TOOL-dTrackedAtlas-12` | the closing review's round-2 minors: one stamp-rules table for writer and reader, the Atlas takes the `--default-ref` it advises, the dead `--ref` guard removed, and the pane observations re-recorded (M1, M2, L1, L2, L3, promoted) |
| 10 | `TOOL-dTrackedAtlas-18` | the schedule instrument re-pinned, in every chain packet and in the chain-packet door, on the owner's word |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 10 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-5 TOOL-dTrackedAtlas-6 TOOL-dTrackedAtlas-7 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 TOOL-dTrackedAtlas-12 TOOL-dTrackedAtlas-13
ids TOOL-dTrackedAtlas-14 TOOL-dTrackedAtlas-15 TOOL-dTrackedAtlas-16 TOOL-dTrackedAtlas-17 TOOL-dTrackedAtlas-18 TOOL-dTrackedAtlas-19

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTrackedAtlas-1 — one chain build-state derivation, read by the schedule and the Atlas](spec/2026-11-19-spec-TOOL-dTrackedAtlas-1.md) | 1 | 1 | CLOSED | rev-3 | 2026-11-19 |
| [TOOL-dTrackedAtlas-2 — the Atlas renders the actual state of each chain build and each area](spec/2026-11-19-spec-TOOL-dTrackedAtlas-2.md) | 2 | 1 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dTrackedAtlas-3 — the page carries the commit and input digest it was generated from, and `--check` reds a stale one](spec/2026-11-19-spec-TOOL-dTrackedAtlas-3.md) | 3 | 1 | CLOSED | rev-3 | 2026-11-19 |
| [TOOL-dTrackedAtlas-4 — the Atlas page regenerates on node d after main moves, behind a switch whose default is on](spec/2026-11-19-spec-TOOL-dTrackedAtlas-4.md) | 4 | 2 | CLOSED | rev-7 | 2026-11-19 |
| [TOOL-dTrackedAtlas-8 — the fork scan passes no tree-derived text through shell source](spec/2026-11-19-spec-TOOL-dTrackedAtlas-8.md) | 5 | 1 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-9 — a landing counts only on the default branch's first-parent line, never a run branch's prepared merge](spec/2026-11-19-spec-TOOL-dTrackedAtlas-9.md) | 6 | 1 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-10 — the page's staleness digest covers the merge history the landed predicate reads](spec/2026-11-19-spec-TOOL-dTrackedAtlas-10.md) | 7 | 1 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-11 — the closing review's minors: one reader for valued options, the stale ledger line cleared, the owed pane looks recorded](spec/2026-11-19-spec-TOOL-dTrackedAtlas-11.md) | 8 | 1 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-12 — the closing review's round-2 minors: one stamp-rules table for writer and reader, a relayed refusal the Atlas can act on, one `--ref` rule, the pane reds re-recorded](spec/2026-11-19-spec-TOOL-dTrackedAtlas-12.md) | 9 | 1 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dTrackedAtlas-18 — the schedule instrument re-pinned in every chain packet and in the chain-packet door](spec/2026-11-19-spec-TOOL-dTrackedAtlas-18.md) | 11 | 2 | CLOSED | rev-1 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 54 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 TOOL-dTrackedAtlas-12 TOOL-dTrackedAtlas-18 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9.

Ids whose spec moved past its audited revision: none — 0 of 10 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTrackedAtlas-1` | no |
| 2 | `TOOL-dTrackedAtlas-2` | no |
| 3 | `TOOL-dTrackedAtlas-3` | no |
| 4 | `TOOL-dTrackedAtlas-4` | no |
| 5 | `TOOL-dTrackedAtlas-8` | no |
| 6 | `TOOL-dTrackedAtlas-9` | no |
| 7 | `TOOL-dTrackedAtlas-10` | no |
| 8 | `TOOL-dTrackedAtlas-11` | no |
| 9 | `TOOL-dTrackedAtlas-12` | no |
| 11 | `TOOL-dTrackedAtlas-18` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| run state | `RUN.md` |
| the units | the units table above |
| briefs | `2026-11-19-prompt-TOOL-dTrackedAtlas-9-build-brief.md`, `2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md` and 31 more under prompts/ |
| reviews | `2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md`, `2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-9.md`, `2026-11-19-build-TOOL-dTrackedAtlas-8-red-fix-8.md` and 2 more under build/ |
| research | `2026-11-19-build-TOOL-dTrackedAtlas-4-regen.json`, `2026-11-19-build-TOOL-dTrackedAtlas-4-regen.js` and 2 more under build/ |
| logs | `2026-11-19-build-TOOL-dTrackedAtlas-9-ledger.md`, `2026-11-19-build-TOOL-dTrackedAtlas-8-ledger.md` and 9 more under build/ |
| open asks | `BACKLOG.md`, 5 open |
| card ref | `refs/gov/builds/dTrackedAtlas/card` |
<!-- /gen:build-routes -->

---
slug: aAnsweredPark
node: a
opened: 2026-11-25
streams: tooling
roster: TOOL
ids: TOOL-aAnsweredPark-1 TOOL-aAnsweredPark-2 TOOL-aAnsweredPark-3 TOOL-aAnsweredPark-4 TOOL-aAnsweredPark-5 TOOL-aAnsweredPark-6
authorized-by: slug
---

# aAnsweredPark — an answered owner decision no longer interrupts its build

## The problem this build exists to solve

The position engine counts every owed parked row of a run as an open owner decision, and no record can
settle one. It also counts a hold the run already resumed from. A run that ever parked therefore answers
`awaiting` until it lands, its card reads no item, and the `actions.free` guard refuses its writes.

## Expected improvements

- A parked decision the owner answered stops interrupting, through a record that quotes the answer.
- A released hold, and a row that asks no question, no longer interrupt.

## Detriments if this is not built

- A run that parked once is refused its own commits for the rest of its life.
- The only ways past the guard are its skip window or a policy change.

## Build-level rules

- Classification (M2): TOOL-aAnsweredPark-1 MISSING at open, specced by the spec-writer role.
- The closing review converged; its mediums and lows are TOOL-aAnsweredPark-5, MISSING when promoted (M4).
- Attended, opened by a session another session started; the owner's words are in the brief.
- `actions.free`, `.governance/policy.toml`, every hook and the card's read bound stay as they are.
- `tools/memory-tree/routed_commits.py`, and everything of the dBoundRoles run, is not written here.
- No spec audit: the README declares none and the owner was not asked for one.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aAnsweredPark-1` | the position engine's owner-decision interrupt: a decision row settled by its own disposition record, only decision rows and a live hold counted |
| 2 | `TOOL-aAnsweredPark-5` | the closing review's five minors, batched: the missing fixture variants, the documents' re-ask limit and the ledger's contradiction |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aAnsweredPark-1 TOOL-aAnsweredPark-2 TOOL-aAnsweredPark-3 TOOL-aAnsweredPark-4 TOOL-aAnsweredPark-5 TOOL-aAnsweredPark-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aAnsweredPark-1 — an owner decision settles by its own answer record, and only an open decision or a live hold interrupts](spec/2026-11-25-spec-TOOL-aAnsweredPark-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-25 |
| [TOOL-aAnsweredPark-5 — the closing review's five minors: six fixture variants, the re-ask limit in three documents, the ledger's contradiction](spec/2026-11-25-spec-TOOL-aAnsweredPark-5.md) | 2 | 1 | CLOSED | rev-1 | 2026-11-25 |
<!-- /gen:build-units -->

Records: 8 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aAnsweredPark-1 TOOL-aAnsweredPark-5.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aAnsweredPark-1` | no |
| 2 | `TOOL-aAnsweredPark-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

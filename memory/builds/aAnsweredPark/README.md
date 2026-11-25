---
slug: aAnsweredPark
node: a
opened: 2026-11-25
streams: tooling
roster: TOOL
ids: TOOL-aAnsweredPark-1 TOOL-aAnsweredPark-2 TOOL-aAnsweredPark-3 TOOL-aAnsweredPark-4
status: OPEN
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aAnsweredPark-1 TOOL-aAnsweredPark-2 TOOL-aAnsweredPark-3 TOOL-aAnsweredPark-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

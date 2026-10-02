---
slug: aHalvedInstall
node: a
opened: 2026-10-02
streams: deployer
roster: DEPL
authorized-by: prompt
ids: DEPL-aHalvedInstall-1 DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4
---

# aHalvedInstall — three kit-deploy defects, closed as classes

## The problem this build exists to solve

A session re-rendering the kits over several adopters hit three defects. A hole meant to catch
undeclared keys passes when they are absent. `playbook-render` declares no `[[regenerate]]`, so every
renderer change rolls it back. And `update` lands a kit half-way across a conflict, which nothing
rolls back for a kit with no `[check]`. The owner's prompt is in `prompts/`.

## Expected improvements

- An absent required key is named by govkit before a render refuses on it.
- A hole probe that passes on an empty tree cannot ship.
- A kit with an adopter decides, in its descriptor, whether `update` re-renders it.
- A kit with a refused row lands none of its bytes in that run.

## Detriments if this is not built

- Every renderer change rolls `playbook-render` back at every adopter.
- A conflict leaves an adopter with a kit whose files disagree, and a red render nobody rolls back.
- A hole keeps reporting "discharged" for a key nobody declared.

## Build-level rules

- Fix where gov authors the defect: a descriptor rule or a govkit arm, never an adopter-side note.
- Reuse first: the hole probe runner, `canonical_ctx`, the verify pass's restore, and the 3b-ii arm.
- Every new arm is observed RED on a staged break before it lands, and its header says what it does
  not check.
- No spec audit: none is owed, and the closing diff review is the specs' first review.
- Classified at kickoff (M2): all four units MISSING. Authored and built inline, in order, because
  units 1, 2 and 4 all write `tools/govkit/govkit.py`.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `DEPL-aHalvedInstall-1` | 2 | govkit reads each kit's declared required conf keys and names an absent or placeholder one |
| 2 | `DEPL-aHalvedInstall-2` | 1 | selfcheck refuses a hole discharge that exits 0 on an empty tree |
| 3 | `DEPL-aHalvedInstall-3` | 1 | a kit with an adopter declares `[[regenerate]]` or a reason; playbook-render declares one |
| 4 | `DEPL-aHalvedInstall-4` | 2 | `update` installs a kit whole or not at all across a refused row |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 4 unit(s) · node a · opened 2026-10-02 · streams deployer
ids DEPL-aHalvedInstall-1 DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-aHalvedInstall-1 — govkit reads each kit's declared required conf keys and names a gap](spec/2026-10-02-spec-DEPL-aHalvedInstall-1.md) | 1 | 2 | OPEN | rev-1 | 2026-10-02 |
| [DEPL-aHalvedInstall-2 — selfcheck refuses a hole discharge that exits 0 on an empty tree](spec/2026-10-02-spec-DEPL-aHalvedInstall-2.md) | 2 | 1 | OPEN | rev-1 | 2026-10-02 |
| [DEPL-aHalvedInstall-3 — every kit with an adopter decides whether `update` re-renders it](spec/2026-10-02-spec-DEPL-aHalvedInstall-3.md) | 3 | 1 | OPEN | rev-1 | 2026-10-02 |
| [DEPL-aHalvedInstall-4 — `update` installs a kit whole or not at all across a refused row](spec/2026-10-02-spec-DEPL-aHalvedInstall-4.md) | 4 | 2 | OPEN | rev-1 | 2026-10-02 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4.

Ids no `spec-audit` record has ever named: DEPL-aHalvedInstall-1 DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-aHalvedInstall-1` | no |
| 2 | `DEPL-aHalvedInstall-2` | no |
| 3 | `DEPL-aHalvedInstall-3` | no |
| 4 | `DEPL-aHalvedInstall-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

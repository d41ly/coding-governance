---
slug: aHoistedPass
node: a
opened: 2026-09-04
streams: tooling+deployer
roster: TOOL+DEPL
parents: dBriefedPass dRatifiedSeam
ids: DEPL-aHoistedPass-1 DEPL-aHoistedPass-2 DEPL-aHoistedPass-3 DEPL-aHoistedPass-4 DEPL-aHoistedPass-5 DEPL-aHoistedPass-6 DEPL-aHoistedPass-7 DEPL-aHoistedPass-8 DEPL-aHoistedPass-9 DEPL-aHoistedPass-10 TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 TOOL-aHoistedPass-10 TOOL-aHoistedPass-11 TOOL-aHoistedPass-12 TOOL-aHoistedPass-13 TOOL-aHoistedPass-14 TOOL-aHoistedPass-15 TOOL-aHoistedPass-16 TOOL-aHoistedPass-17 TOOL-aHoistedPass-18 TOOL-aHoistedPass-19 TOOL-aHoistedPass-20 TOOL-aHoistedPass-21 TOOL-aHoistedPass-22 TOOL-aHoistedPass-23 TOOL-aHoistedPass-24 TOOL-aHoistedPass-25 TOOL-aHoistedPass-26 TOOL-aHoistedPass-27 TOOL-aHoistedPass-28 TOOL-aHoistedPass-29 TOOL-aHoistedPass-30 TOOL-aHoistedPass-31 TOOL-aHoistedPass-32
---

# aHoistedPass — the harnessed build pass, actually reachable, actually per-unit, and a ratchet that keeps it reachable

## The problem this build exists to solve

`dBriefedPass` built the harness that makes a build's pass order a property of a program;
`dRatifiedSeam` repaired its AUDIT stage, which had asked a sidechain agent for a tool a sidechain
does not hold. Both landed. No run has used either, for three measured reasons.

**No route.** 0 of 17 core directive handles appear in `memory/guides/BUILD-METHOD.md`, and check 16
arm B asserts only that the cited section EXISTS. A run resolving `passes-harnessed` reads M6, finds
nothing, and builds inline. Filed as M9 of `dBriefedPass`'s own closing review; never landed.

**Wrong shape.** BUILD is one `agent()` holding the whole roster — median 4 units, maximum 30.

**No witness.** The harness writes nothing. `dRetiredFork` ran without it and produced byte-identical
`brief` rows.

## Expected improvements

- A run finds the harness rule where its bound directive says it is.
- Each unit is built by an agent holding that unit's spec and brief, not the roster.
- Every per-unit dispatch is a main-loop call, so the fan-out guard sees it at all.
- The pointer gate stops passing a section that says nothing.
- An adopter without the harness is told, at install and on every bar.

## Detriments if this is not built

- The directive keeps binding every run to a route no run can find, and the gate keeps passing it.
- The one-agent BUILD stage keeps handing 30 units to a single context.
- The next carrier edit reintroduces the same mispointer, because nothing reads a section's body.

## Build-level rules

Every rule below is argued in the design record; this slot is the index, not the argument.

- **Route and ratchet land in ONE commit.** The anchor term reds 17 of 17 handles today, so a ratchet before its anchors reds the bar and anchors before it are unguarded prose.
- **The budget raise precedes the anchors** — 289 B of anchors against 12 B of headroom.
- **The comment strip is BLOCK-wise.** A line-prefix filter passes a multi-line comment carrying the anchor; measured on four fixtures.
- **The hoist's headline was false.** It does not protect the child's content. It takes each dispatch from ZERO hook checks to four, and deletes a clause set, a unit and two rulings.
- **No spec may claim `--dispatch` backstops the loop.** Completeness rests on `build-complete` alone; its escape is a recorded override.
- **`pass-order history` grades spec-before-code only** — not the declared unit order, not completeness.
- **Termination needs the spec status flip**, which the child performs in the same commit as the code.
- **Recipe mode is measured, not decided.** A live carrier/registry disagreement ships until `TOOL-aHoistedPass-8` reports, and no unit takes a side.
- **The Skill template is veto-2** per ruling D1, so every unit touching it is an owner turn.


## Parked decisions

- **`TOOL-aHoistedPass-8` AC7 was corrected in claim, not in path**, because its original named a hit
  at a sha where this build's folder does not exist. The unit's finding is unchanged; confirm the new
  observation is the one that unit should own.
- **`check 23` of the unattended leg reports 30 findings against `dRetiredFork`** and is non-gating:
  identical counts pre-merge and post-merge, with the pre-merge run green. Not this build's to fix.
- **A landing attempt swept an untracked root-level log into a commit** via `git add -A`, and the next
  bar wrote into it, dirtying the tree and making the lander refuse. Removed. The lesson is the `-A`,
  not the log.


<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aHoistedPass-1` | SPECCED | the record catches up with the verdicts that superseded it |
| 2 | `TOOL-aHoistedPass-4` | SPECCED | the loop ban learns the two spellings that walk past it |
| 3 | `TOOL-aHoistedPass-8` | SPECCED | the recipe-mode question, measured instead of argued |
| 4 | `TOOL-aHoistedPass-3` | SPECCED | the build-method budget becomes a number a gate reads |
| 5 | `DEPL-aHoistedPass-1` | SPECCED | a declared kit dependency that is actually checked |
| 6 | `TOOL-aHoistedPass-2` | SPECCED | the route a run can find, and the ratchet that keeps it findable |
| 7 | `TOOL-aHoistedPass-5` | SPECCED | the child that builds one unit and holds nothing else |
| 8 | `TOOL-aHoistedPass-6` | SPECCED | the harness hands out a roster and stops driving the build |
| 9 | `TOOL-aHoistedPass-9` | SPECCED | the adopter without the harness is told, on every bar |
| 10 | `TOOL-aHoistedPass-7` | SPECCED | a brief on disk before the code that cites it |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 10 unit(s) · node a · opened 2026-09-04 · streams tooling+deployer
ids DEPL-aHoistedPass-1 DEPL-aHoistedPass-2 DEPL-aHoistedPass-3 DEPL-aHoistedPass-4 DEPL-aHoistedPass-5 DEPL-aHoistedPass-6 DEPL-aHoistedPass-7 DEPL-aHoistedPass-8 DEPL-aHoistedPass-9 DEPL-aHoistedPass-10 TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4
ids TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 TOOL-aHoistedPass-10 TOOL-aHoistedPass-11 TOOL-aHoistedPass-12 TOOL-aHoistedPass-13 TOOL-aHoistedPass-14 TOOL-aHoistedPass-15 TOOL-aHoistedPass-16 TOOL-aHoistedPass-17 TOOL-aHoistedPass-18
ids TOOL-aHoistedPass-19 TOOL-aHoistedPass-20 TOOL-aHoistedPass-21 TOOL-aHoistedPass-22 TOOL-aHoistedPass-23 TOOL-aHoistedPass-24 TOOL-aHoistedPass-25 TOOL-aHoistedPass-26 TOOL-aHoistedPass-27 TOOL-aHoistedPass-28 TOOL-aHoistedPass-29 TOOL-aHoistedPass-30 TOOL-aHoistedPass-31 TOOL-aHoistedPass-32

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHoistedPass-1 — the record catches up with the verdicts that superseded it](spec/2026-09-04-spec-TOOL-aHoistedPass-1.md) | 1 | 1 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-aHoistedPass-4 — the loop ban learns the two spellings that walk past it](spec/2026-09-04-spec-TOOL-aHoistedPass-4.md) | 1 | 1 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aHoistedPass-8 — the recipe-mode question, measured instead of argued](spec/2026-09-04-spec-TOOL-aHoistedPass-8.md) | 1 | 1 | SPECCED | rev-4 | 2026-09-05 |
| [DEPL-aHoistedPass-1 — a declared kit dependency that is actually checked](spec/2026-09-04-spec-DEPL-aHoistedPass-1.md) | 2 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aHoistedPass-3 — the build-method budget becomes a number a gate reads](spec/2026-09-04-spec-TOOL-aHoistedPass-3.md) | 2 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-aHoistedPass-2 — the route a run can find, and the ratchet that keeps it findable](spec/2026-09-04-spec-TOOL-aHoistedPass-2.md) | 3 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-aHoistedPass-5 — the child that builds one unit and holds nothing else](spec/2026-09-04-spec-TOOL-aHoistedPass-5.md) | 4 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-aHoistedPass-6 — the harness hands out a roster and stops driving the build](spec/2026-09-04-spec-TOOL-aHoistedPass-6.md) | 5 | 2 | SPECCED | rev-5 | 2026-09-05 |
| [TOOL-aHoistedPass-9 — the adopter without the harness is told, on every bar](spec/2026-09-04-spec-TOOL-aHoistedPass-9.md) | 6 | 2 | SPECCED | rev-3 | 2026-09-05 |
| [TOOL-aHoistedPass-7 — a brief on disk before the code that cites it](spec/2026-09-04-spec-TOOL-aHoistedPass-7.md) | 7 | 2 | SPECCED | rev-5 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHoistedPass-1`, `TOOL-aHoistedPass-4`, `TOOL-aHoistedPass-8` | yes |
| 2 | `DEPL-aHoistedPass-1`, `TOOL-aHoistedPass-3` | yes |
| 3 | `TOOL-aHoistedPass-2` | no |
| 4 | `TOOL-aHoistedPass-5` | no |
| 5 | `TOOL-aHoistedPass-6` | no |
| 6 | `TOOL-aHoistedPass-9` | no |
| 7 | `TOOL-aHoistedPass-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBriefedPass](../dBriefedPass/README.md), [dRatifiedSeam](../dRatifiedSeam/README.md)
<!-- /gen:build-edges -->

---
slug: dFurnishedOrders
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-21
spec-audit: 2026-10-21
parents: dBoundRoles
may: PLAY-dClosedLoop-3
---

# dFurnishedOrders — the Orders build of the dClosedLoop chain

## The problem this build exists to solve

dFurnishedOrders owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-roles-09,
gap-roles-10, gap-roles-12, gap-roles-13, gap-roles-15, gap-roles-16, gap-roles-17, gap-orient-15, gap-roles-21,
gap-roles-22, gap-roles-29, gap-conc-10, gap-mem-44. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 20 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 4 child builds wait on it: dMindYourWords, dScopedBuild, dShippedRelease, dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dFurnishedOrders` green before the first pass; a moved instrument
  blob is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dFurnishedOrders`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-18.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dFurnishedOrders-1` | `cl-dClosedLoop-0192@e52307f5` | the orientation scout composing the card in a sidechain at session start |
| 2 | `TOOL-dFurnishedOrders-2` | `cl-dClosedLoop-0193@a564937b` | prompt-writer calls batched by `prompts.batch` |
| 3 | `TOOL-dFurnishedOrders-3` | `cl-dClosedLoop-0194@48cbc488` | a return's harness notices persisted with it |
| 4 | `TOOL-dFurnishedOrders-4` | `cl-dClosedLoop-0195@d3ad9dda` | work-order fields an optional component or an expansion fills (the map's dossiers) declared as optional slots in their three states |
| 5 | `TOOL-dFurnishedOrders-5` | `cl-dClosedLoop-0196@f158a89c` | each role's trust profile and context temperature declared and rendered (`roles.trust` |
| 6 | `TOOL-dFurnishedOrders-6` | `cl-dClosedLoop-0197@ced122c4` | the answered-call hook (`roles.answered-calls`) |
| 7 | `TOOL-dFurnishedOrders-7` | `cl-dClosedLoop-0198@9197dfef` | repairs recorded in returns and filed as asks against the producer's record (`roles.on-contradiction`) |
| 8 | `TOOL-dFurnishedOrders-8` | `cl-dClosedLoop-0199@871337bc` | the role files' re-verification orders and protocol pointers replaced by rendered slices |
| 9 | `TOOL-dFurnishedOrders-9` | `cl-dClosedLoop-0200@89a5045e` | the role-by-step matrix derived from the item declarations and joined both ways |
| 10 | `TOOL-dFurnishedOrders-10` | `cl-dClosedLoop-0201@53144abb` | role metrics per role and item into the value ledger |
| 11 | `TOOL-dFurnishedOrders-11` | `cl-dClosedLoop-0202@504bb58f` | the work order's memory slices |
| 12 | `TOOL-dFurnishedOrders-12` | `cl-dClosedLoop-0203@325cbb22` | the work order's `map` slot for the roles `memory.project-map` names |
| 13 | `TOOL-dFurnishedOrders-13` | `cl-dClosedLoop-0204@34f664ed` | the orientation scout composing the card's map cell |
| 14 | `TOOL-dFurnishedOrders-14` | `cl-dClosedLoop-0205@5bbb1b2c` | the answered-call hook's range matching |
| 15 | `TOOL-dFurnishedOrders-15` | `cl-dClosedLoop-0206@e18404dd` | the tester agent |
| 16 | `TOOL-dFurnishedOrders-16` | `cl-dClosedLoop-0207@770af750` | owner questions asked live while the build is attended |
| 17 | `TOOL-dFurnishedOrders-17` | `cl-dClosedLoop-0208@b6c1dedb` | the `code` slot rendered per item from its declared seed: the seed's definitions with their ranges |
| 18 | `TOOL-dFurnishedOrders-18` | `cl-dClosedLoop-0209@97727c41` | the work order selecting instruction units by `feature.*` once dLinkedLibrary arms that selector |
| 19 | `TOOL-dFurnishedOrders-19` | `cl-dClosedLoop-0210@c44de500` | every role return declaring the rows it establishes (seams |
| 20 | `TOOL-dFurnishedOrders-20` | `cl-dClosedLoop-0211@6b17e1fe` | the problems whose subject intersects an item's seed handed in its work order as rows |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 20 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12
ids TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFurnishedOrders-8 — the role files' protocol pointers and re-verification orders replaced by rendered slices](spec/2026-10-26-spec-TOOL-dFurnishedOrders-8.md) | 1 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-5 — each role's trust profile and context temperature declared and rendered](spec/2026-10-26-spec-TOOL-dFurnishedOrders-5.md) | 2 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-15 — the tester re-founded with its allowance, and the `probe` outcome on every role's return template](spec/2026-10-26-spec-TOOL-dFurnishedOrders-15.md) | 3 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-4 — the work order's optional slots in three states, and bug classes as a core field the spec names](spec/2026-10-26-spec-TOOL-dFurnishedOrders-4.md) | 4 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-1 — the orientation scout composing the card in a sidechain at session start, its recall re-verified once at entry and a moved-source record handed as stale](spec/2026-10-26-spec-TOOL-dFurnishedOrders-1.md) | 5 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-13 — the orientation scout composing the card's project-map cell, placed and shape-checked at the append, not installed until the map renderer lands](spec/2026-10-26-spec-TOOL-dFurnishedOrders-13.md) | 6 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-3 — a return's harness notices persisted with it, as runlog `notice` events and on the agent ledger's returned line, by `notices.record`](spec/2026-10-26-spec-TOOL-dFurnishedOrders-3.md) | 7 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-19 — every role return declaring the rows it establishes, and each work order's return schema rendered from its own rows, so a dropped, invented or doubled row fails the return and is retried](spec/2026-10-26-spec-TOOL-dFurnishedOrders-19.md) | 8 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-7 — a false handed fact repaired in the return and filed as an ask against its producer's record, routed by `roles.on-contradiction` through the refusal outcome table](spec/2026-10-26-spec-TOOL-dFurnishedOrders-7.md) | 9 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-14 — the answered-call hook's range matching, the excerpt keys it matches and a repair's carry, designed as RC-7 asks](spec/2026-10-26-spec-TOOL-dFurnishedOrders-14.md) | 10 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-6 — the answered-call hook: a role agent's call its work order already answers refused, warned or recorded by `roles.answered-calls`, a verifier's read of its subject exempt, and each hook failure recorded](spec/2026-10-26-spec-TOOL-dFurnishedOrders-6.md) | 11 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-9 — the role-by-step matrix derived from the item declarations, joined both ways, and rendered to each role as its own row](spec/2026-10-26-spec-TOOL-dFurnishedOrders-9.md) | 12 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-10 — role metrics per role and item, classed by runlog's extractor and kept in this build's metrics file](spec/2026-10-26-spec-TOOL-dFurnishedOrders-10.md) | 13 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-11 — the work order's memory, code-notes, legacy and house-index slots, each under its own budget and its own answer](spec/2026-10-26-spec-TOOL-dFurnishedOrders-11.md) | 14 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-12 — the work order's `map` slot for the roles `memory.project-map` names, with each item's unfolds](spec/2026-10-26-spec-TOOL-dFurnishedOrders-12.md) | 15 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-17 — the `code` slot rendered per item from its declared seed, as ranges under `memory.code-budget`](spec/2026-10-26-spec-TOOL-dFurnishedOrders-17.md) | 16 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-20 — the problems whose subject meets an item's seed, read from the register when the order is cut and handed as rows](spec/2026-10-26-spec-TOOL-dFurnishedOrders-20.md) | 17 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-18 — the work order selecting instruction units by `feature.*`, and its code-notes slot filled from the tag's bundle as `annotations.delivery` says](spec/2026-10-26-spec-TOOL-dFurnishedOrders-18.md) | 18 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-2 — prompt-writer calls batched by `prompts.batch`: one call frames a step's tasks of one role, split per task at render](spec/2026-10-26-spec-TOOL-dFurnishedOrders-2.md) | 19 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dFurnishedOrders-16 — owner questions asked live while the build is attended, never decided at raise, and a late answer placed as an amendment that re-enters its item](spec/2026-10-26-spec-TOOL-dFurnishedOrders-16.md) | 20 | 2 | OPEN | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18
TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9.

Ids whose spec moved past its audited revision: none — 0 of 20 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dFurnishedOrders's 20 clause(s) and 14 owned node(s), over 20 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 20
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0192, cl-dClosedLoop-0195, cl-dClosedLoop-0200, cl-dClosedLoop-0204, cl-dClosedLoop-0205, cl-dClosedLoop-0211
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dFurnishedOrders-8` | no |
| 2 | `TOOL-dFurnishedOrders-5` | no |
| 3 | `TOOL-dFurnishedOrders-15` | no |
| 4 | `TOOL-dFurnishedOrders-4` | no |
| 5 | `TOOL-dFurnishedOrders-1` | no |
| 6 | `TOOL-dFurnishedOrders-13` | no |
| 7 | `TOOL-dFurnishedOrders-3` | no |
| 8 | `TOOL-dFurnishedOrders-19` | no |
| 9 | `TOOL-dFurnishedOrders-7` | no |
| 10 | `TOOL-dFurnishedOrders-14` | no |
| 11 | `TOOL-dFurnishedOrders-6` | no |
| 12 | `TOOL-dFurnishedOrders-9` | no |
| 13 | `TOOL-dFurnishedOrders-10` | no |
| 14 | `TOOL-dFurnishedOrders-11` | no |
| 15 | `TOOL-dFurnishedOrders-12` | no |
| 16 | `TOOL-dFurnishedOrders-17` | no |
| 17 | `TOOL-dFurnishedOrders-20` | no |
| 18 | `TOOL-dFurnishedOrders-18` | no |
| 19 | `TOOL-dFurnishedOrders-2` | no |
| 20 | `TOOL-dFurnishedOrders-16` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md)
- **Child builds:** [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

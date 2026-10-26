---
slug: dBoundRoles
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-27 TOOL-dBoundRoles-28 TOOL-dBoundRoles-29 TOOL-dBoundRoles-30 TOOL-dBoundRoles-31 TOOL-dBoundRoles-32 TOOL-dBoundRoles-33 TOOL-dBoundRoles-34 TOOL-dBoundRoles-35 TOOL-dBoundRoles-36 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69
spec-audit: 2026-10-21
parents: dDeclaredLoop dWitnessedBar dPlacedRequest
may: PLAY-dClosedLoop-3
---

# dBoundRoles — the Roles build of the dClosedLoop chain

## The problem this build exists to solve

dBoundRoles owns 22 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-roles-01,
gap-roles-02, gap-roles-03, gap-roles-04, gap-roles-05, gap-roles-06, gap-roles-07, gap-roles-08, gap-orient-07,
gap-orient-09, gap-roles-11, gap-roles-14, gap-roles-18, gap-roles-19, gap-roles-20, gap-roles-23, gap-roles-24,
gap-roles-25, gap-roles-27, gap-roles-28, gap-roles-30, gap-roles-31. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 26 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 22 owned gaps above close.

## Detriments if this is not built

- Its 22 owned gaps stay open.
- Its 5 child builds wait on it: dFurnishedOrders, dWellOiledMachine, dRankedPlan, dIndexedDesign, dShippedRelease.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dBoundRoles` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dBoundRoles`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dBoundRoles-1` | `cl-dClosedLoop-0166@83615023` | the roster sorted by layer: twelve core roles (orientation scout |
| 2 | `TOOL-dBoundRoles-2` | `cl-dClosedLoop-0167@0ec2ea97` | each role's static instructions as structured fields |
| 3 | `TOOL-dBoundRoles-3` | `cl-dClosedLoop-0168@abfd5f4f` | the work order rendered per item (the item |
| 4 | `TOOL-dBoundRoles-4` | `cl-dClosedLoop-0169@cdc1b7f9` | the prompt writer composing every role's task from the driver's details |
| 5 | `TOOL-dBoundRoles-5` | `cl-dClosedLoop-0170@d33b224b` | returns through a schema-forced channel |
| 6 | `TOOL-dBoundRoles-6` | `cl-dClosedLoop-0171@efd80f4f` | the role index and agent files beyond every worker's reach |
| 7 | `TOOL-dBoundRoles-7` | `cl-dClosedLoop-0172@b73b4974` | shell writes held to the allowance |
| 8 | `TOOL-dBoundRoles-8` | `cl-dClosedLoop-0173@a66af889` | the role-gate arm's field escape explained and closed |
| 9 | `TOOL-dBoundRoles-9` | `cl-dClosedLoop-0174@b2c09e04` | the `none` and `review` write classes enforced |
| 10 | `TOOL-dBoundRoles-10` | `cl-dClosedLoop-0175@79a1c7d0` | `driver.reads` |
| 11 | `TOOL-dBoundRoles-11` | `cl-dClosedLoop-0176@6a45e0b7` | every fork resolved by the role that meets it and recorded |
| 12 | `TOOL-dBoundRoles-12` | `cl-dClosedLoop-0177@4a09db23` | the orientation scout's return carrying the placement disposition and its reason |
| 13 | `TOOL-dBoundRoles-13` | `cl-dClosedLoop-0178@f3b0d6ea` | the trust mechanism (P29): inputs handed as content |
| 14 | `TOOL-dBoundRoles-14` | `cl-dClosedLoop-0179@f74e2fff` | the `role` and `field` tag namespaces |
| 15 | `TOOL-dBoundRoles-15` | `cl-dClosedLoop-0180@145f826e` | the role static block carried once per spawn |
| 16 | `TOOL-dBoundRoles-16` | `cl-dClosedLoop-0181@6ebedcff` | the shapes |
| 17 | `TOOL-dBoundRoles-17` | `cl-dClosedLoop-0182@0cc5ed88` | every work order carrying its marker with `item=` |
| 18 | `TOOL-dBoundRoles-18` | `cl-dClosedLoop-0183@46564bcb` | its own upgrade steps: an adopter's rendered agents renamed as the two reviewer roles merge |
| 19 | `TOOL-dBoundRoles-19` | `cl-dClosedLoop-0184@923d7266` | the roles kit's house text files |
| 20 | `TOOL-dBoundRoles-20` | `cl-dClosedLoop-0185@ce70dc70` | a repository's roles and workflow entries |
| 21 | `TOOL-dBoundRoles-21` | `cl-dClosedLoop-0186@e356242a` | `roles.effort.<role>` |
| 22 | `TOOL-dBoundRoles-22` | `cl-dClosedLoop-0187@5afc67cc` | workflow entries as data: each entry's ordered stages |
| 23 | `TOOL-dBoundRoles-23` | `cl-dClosedLoop-0188@23b122f8` | the prompt writer's default frame for a role item |
| 24 | `TOOL-dBoundRoles-24` | `cl-dClosedLoop-0189@8d7be499` | the prompt writer's framing checked at render |
| 25 | `TOOL-dBoundRoles-25` | `cl-dClosedLoop-0190@03bbbf1e` | agent-cap's spawn guard and harness admission moved into the roles pack |
| 26 | `TOOL-dBoundRoles-26` | `cl-dClosedLoop-0191@66acd199` | the typed refusal return in every role's template |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 59 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15
ids TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-27 TOOL-dBoundRoles-28 TOOL-dBoundRoles-29
ids TOOL-dBoundRoles-30 TOOL-dBoundRoles-31 TOOL-dBoundRoles-32 TOOL-dBoundRoles-33 TOOL-dBoundRoles-34 TOOL-dBoundRoles-35 TOOL-dBoundRoles-36 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43
ids TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57
ids TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dBoundRoles-14 — the `role` and `field` tag namespaces, their extractors and the role binding join](spec/2026-10-25-spec-TOOL-dBoundRoles-14.md) | 1 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-2 — each role's static instructions as structured fields: the never list with its enforcers, the ceiling and the typed return](spec/2026-10-25-spec-TOOL-dBoundRoles-2.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-1 — the roster sorted by layer: twelve core roles, two expansion roles registered, and core items kept to core roles](spec/2026-10-25-spec-TOOL-dBoundRoles-1.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-21 — the effort and model keys, `default` reserved, and the gate grant a role field, every reader re-pointed](spec/2026-10-25-spec-TOOL-dBoundRoles-21.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-37 — govkit's roles install case derives the agent types and house overlays it expects from the roster and the seed rows, so no roster change leaves a typed count to red](spec/2026-10-26-spec-TOOL-dBoundRoles-37.md) | 4 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-22 — workflow entries as data: ordered stages, each naming its role, fan, cap, effort and rows, every cap under the agent limit](spec/2026-10-25-spec-TOOL-dBoundRoles-22.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-49 — govkit's default plan derives the seed rows it expects to preview from the plan model and the roles roster, so the third typed roles count cannot red late](spec/2026-10-26-spec-TOOL-dBoundRoles-49.md) | 5 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-16 — the shapes: each workflow entry's kind, checklist, orientation, merge and twin rule, the five kinds as defaults over the stage rows](spec/2026-10-25-spec-TOOL-dBoundRoles-16.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-54 — unit 49's overlay check reads its expected side from the roster, one `house/<slot>.md` per role slot, never from the seed rule it is compared with](spec/2026-10-26-spec-TOOL-dBoundRoles-54.md) | 6 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-55 — unit 49's overlay check refuses an empty expected set, and ends where unit 19 moves the house files out of the kit](spec/2026-10-26-spec-TOOL-dBoundRoles-55.md) | 6 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-15 — the role static block carried once per spawn, and its budget over the whole rendered block](spec/2026-10-25-spec-TOOL-dBoundRoles-15.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-17 — every work order's marker carrying `item=`, every return naming the work order it `answers`, today's population seeded](spec/2026-10-25-spec-TOOL-dBoundRoles-17.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-6 — the role index and agent files beyond every worker's reach, a tree with no index refused, `role-sha` compared at spawn](spec/2026-10-25-spec-TOOL-dBoundRoles-6.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-13 — inputs handed as content, each fact keyed and classed by the executor and re-cut fresh at act launch](spec/2026-10-25-spec-TOOL-dBoundRoles-13.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-3 — the work order rendered per item, hashed into the spawn marker and bound to its act](spec/2026-10-25-spec-TOOL-dBoundRoles-3.md) | 11 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-38 — handed content fenced inside the work order, and every reader of a fact line or a marker line skips what a fence holds](spec/2026-10-26-spec-TOOL-dBoundRoles-38.md) | 11 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-45 — a typed `--input` value is authored text: written unfenced, refused when a line would stand as an executor line, so the anchor check grades it](spec/2026-10-26-spec-TOOL-dBoundRoles-45.md) | 12 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-46 — the spawn guard holds a typed block to the authored-line rule: a fact, marker or `Framed by:` line in `input:question` or `input:diff`, or a fence left open there, is denied](spec/2026-10-26-spec-TOOL-dBoundRoles-46.md) | 12 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-48 — the composed task section checked block by block: every block opens outside a fence, and each handed block's content lies inside its own, at render and at spawn](spec/2026-10-26-spec-TOOL-dBoundRoles-48.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-8 — the role-gate arm's field escape explained and closed](spec/2026-10-25-spec-TOOL-dBoundRoles-8.md) | 12 | 2 | DEFERRED | rev-1 | 2026-10-25 |
| [TOOL-dBoundRoles-9 — the `none` and `review` write classes enforced in the role arm](spec/2026-10-25-spec-TOOL-dBoundRoles-9.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-7 — shell writes held to the work order's allowance](spec/2026-10-25-spec-TOOL-dBoundRoles-7.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-5 — returns through a schema-forced channel on both routes, residual failures retried by `roles.retries`](spec/2026-10-25-spec-TOOL-dBoundRoles-5.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-10 — `driver.reads`, `prompts.author` and `roles.no-spawn`, each read and enforced at its seam](spec/2026-10-25-spec-TOOL-dBoundRoles-10.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-39 — the return check grades a direct spawn only: a stop whose transcript is a harness stage's, or whose first record carries no handoff marker, passes untouched](spec/2026-10-26-spec-TOOL-dBoundRoles-39.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-40 — a recorded harness-stage stop replayed against every `SubagentStop` hook a default install registers, red on any output, any block or any record](spec/2026-10-26-spec-TOOL-dBoundRoles-40.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-4 — the prompt writer composing every role's task from the driver's details](spec/2026-10-25-spec-TOOL-dBoundRoles-4.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-23 — the prompt writer's default frame, bounded lists, upstream rows, and the medium effort floor](spec/2026-10-25-spec-TOOL-dBoundRoles-23.md) | 18 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-24 — the framing checked at render: every anchor a work order points at resolves to a fact it hands](spec/2026-10-25-spec-TOOL-dBoundRoles-24.md) | 19 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-12 — the orientation scout's placement return through the typed channel, recorded and checked by the driver](spec/2026-10-25-spec-TOOL-dBoundRoles-12.md) | 20 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-41 — the anchor check grades the text a work order authors, never the content it hands, by the block extents the render assembled](spec/2026-10-26-spec-TOOL-dBoundRoles-41.md) | 20 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-11 — every fork resolved by the role that meets it with its full record, or held as `run.on-owner-question` says](spec/2026-10-25-spec-TOOL-dBoundRoles-11.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-47 — one criterion across the fence, the strip and the graded text: with units 38, 45, 24 and 41 landed, an anchor planted in a typed `--input` value is refused](spec/2026-10-26-spec-TOOL-dBoundRoles-47.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-26 — the typed refusal return: its rule, its remedy and the remedy's actor, routed at once and never re-offered](spec/2026-10-25-spec-TOOL-dBoundRoles-26.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-52 — unit 47's cross-unit render pair runs on a role that reads both of its inputs: `gov-orienter`, the span typed in `input:question` and handed in `input:prompt`](spec/2026-10-26-spec-TOOL-dBoundRoles-52.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-53 — unit 47's case proves its render arguments are read before it relies on them, so neither half can pass or fail on argument parsing](spec/2026-10-26-spec-TOOL-dBoundRoles-53.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-20 — a repository's roles and workflow entries composed beside gov's, with the role kind's fixed set, widening directions and step-gate classes](spec/2026-10-25-spec-TOOL-dBoundRoles-20.md) | 23 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-59 — unit 53's read check folds each `reads` entry through `roles_lib.parse_read_key`, so the tag spelling unit 14 writes passes and the read-key grammar keeps one owner](spec/2026-10-26-spec-TOOL-dBoundRoles-59.md) | 23 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-19 — the roles kit's house text files moved into the overlay as level-5 units selecting their role, by their own upgrade step](spec/2026-10-25-spec-TOOL-dBoundRoles-19.md) | 24 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [TOOL-dBoundRoles-61 — unit 59's read check fails on its slice's exit status, so a slice that crashes can no longer pass for a read it never checked](spec/2026-10-26-spec-TOOL-dBoundRoles-61.md) | 24 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-18 — the reviewers' merge as an upgrade step: an adopter's reviewer agents renamed to `gov-reviewer`, the role index re-rendered, every key the merge touches re-keyed](spec/2026-10-25-spec-TOOL-dBoundRoles-18.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-25 — the spawn guard and harness admission moved into the roles pack, admission held to the landed blob, `tools/hooks/agent-cap.js` retired with an upgrade step](spec/2026-10-25-spec-TOOL-dBoundRoles-25.md) | 26 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dBoundRoles-42 — the retired hook's readers under `memory/` classed, append-only records left as written, and the live-carrier check scoped to what a reader can still be misled by](spec/2026-10-26-spec-TOOL-dBoundRoles-42.md) | 27 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-43 — the round-1 audit's 46 roles-code minors: one grammar each for returns, shapes and slots, one reader and writer each, bounded readers, resumable steps, and the registries they feed](spec/2026-10-26-spec-TOOL-dBoundRoles-43.md) | 28 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dBoundRoles-44 — the round-1 audit's 11 docs-and-records minors: memory readers re-derived, frozen receipt waived, gotcha pages re-pointed, two Skills fitted, legacy registry named, workflow suites re-keyed and the close's harness swap checked](spec/2026-10-26-spec-TOOL-dBoundRoles-44.md) | 29 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-50 — the round-1 audit of units 37 to 44, its 24 roles-code minors: one fence walker per language, fence-aware marker readers, live leg names, waiver and registry rows kept true, and criteria that can fail](spec/2026-10-26-spec-TOOL-dBoundRoles-50.md) | 30 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dBoundRoles-51 — the round-1 audit of units 37 to 44, its 8 records-and-Skills minors: build order verified, the policy mirror's net diff, append-only records observed by class, one owner per ledger verdict, and the recall Skill off a refused tool](spec/2026-10-26-spec-TOOL-dBoundRoles-51.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-56 — the three readers of a spec's H1 share one fence rule: `parse_spec_h1` and KICK R4 move with `checkBuildable` onto the length rule, and one fixture set sees one id from all three](spec/2026-10-26-spec-TOOL-dBoundRoles-56.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-57 — the memory-recall kit's description invariant follows the Skill off the refused tools: augments shell `grep` and `git grep`, and names neither search tool](spec/2026-10-26-spec-TOOL-dBoundRoles-57.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-58 — the 35 minors of auditing units 45 to 51: criteria passable on a correct build, one typed set and one block reader at spawn, one extents record at render, the H1 parity's consumers, and AMENDED answers naming a revision](spec/2026-10-26-spec-TOOL-dBoundRoles-58.md) | 32 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-60 — the round-1 audit of units 52 to 58, its 37 minors: criteria that can fail and can pass, arms observed where their code lives, one read-key parse, floors moved with their arms, and write sets that name every file a pass writes](spec/2026-10-26-spec-TOOL-dBoundRoles-60.md) | 33 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [TOOL-dBoundRoles-62 — the spawn guard's suite carries the floor unit 60's AC15 checks, and AC15 refuses a suite with no floor and names its units suite by suite](spec/2026-10-26-spec-TOOL-dBoundRoles-62.md) | 34 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-63 — the round-1 audit of units 59 and 60, its 19 minors: a floor sum that counts its base, criteria that can fail on the text they retire, observations on a tree that imports, and write sets that name every file](spec/2026-10-26-spec-TOOL-dBoundRoles-63.md) | 35 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [TOOL-dBoundRoles-64 — the round-1 audit of units 61 to 63, its 32 minors: floors at the executed count naming every unit, a negative case inverting its verdict, criteria failing on the text they retire, no stray worktree, and an edge per bumped spec](spec/2026-10-26-spec-TOOL-dBoundRoles-64.md) | 36 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [TOOL-dBoundRoles-65 — the observation worktree's cleanup check compares normalised paths under a named root, and a positive control proves it sees a leftover](spec/2026-10-26-spec-TOOL-dBoundRoles-65.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-66 — the round-1 audit of unit 64, its 23 minors: skip lines by a pinned predicate, loops swept by class, unit terms tied to their arms, absence checks on joined prose, and the observation's failure path staged](spec/2026-10-26-spec-TOOL-dBoundRoles-66.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [TOOL-dBoundRoles-67 — unit 65's leftover sweep also selects the observation's worktrees by what they checked out, so a leftover at an unnamed `%TEMP%` path is found](spec/2026-10-26-spec-TOOL-dBoundRoles-67.md) | 38 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dBoundRoles-68 — unit 65's AC4 says it is green by construction over `dbr63obs` alone, and a positive control proves the signature selection sees a leftover outside that root](spec/2026-10-26-spec-TOOL-dBoundRoles-68.md) | 38 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [TOOL-dBoundRoles-69 — the round-1 audit of units 65 and 66, its 18 minors: ledger criteria read through the revision arm, one root source, printed operands, one cleanup rule, loops swept by a pinned class, and a hard kill recovered](spec/2026-10-26-spec-TOOL-dBoundRoles-69.md) | 39 | 2 | DEFERRED | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 137 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69.

Ids whose spec moved past its audited revision: TOOL-dBoundRoles-1@rev-1 TOOL-dBoundRoles-10@rev-1 TOOL-dBoundRoles-11@rev-1 TOOL-dBoundRoles-12@rev-1 TOOL-dBoundRoles-13@rev-1 TOOL-dBoundRoles-14@rev-1 TOOL-dBoundRoles-15@rev-1 TOOL-dBoundRoles-16@rev-1 TOOL-dBoundRoles-17@rev-1
TOOL-dBoundRoles-18@rev-1 TOOL-dBoundRoles-19@rev-1 TOOL-dBoundRoles-2@rev-1 TOOL-dBoundRoles-20@rev-1 TOOL-dBoundRoles-21@rev-1 TOOL-dBoundRoles-22@rev-1 TOOL-dBoundRoles-23@rev-1 TOOL-dBoundRoles-24@rev-1 TOOL-dBoundRoles-25@rev-1 TOOL-dBoundRoles-26@rev-1 TOOL-dBoundRoles-3@rev-1
TOOL-dBoundRoles-4@rev-1 TOOL-dBoundRoles-5@rev-1 TOOL-dBoundRoles-6@rev-1 TOOL-dBoundRoles-7@rev-1 TOOL-dBoundRoles-9@rev-1 TOOL-dBoundRoles-37@rev-1 TOOL-dBoundRoles-38@rev-1 TOOL-dBoundRoles-39@rev-1 TOOL-dBoundRoles-40@rev-1 TOOL-dBoundRoles-41@rev-1 TOOL-dBoundRoles-42@rev-1
TOOL-dBoundRoles-43@rev-1 TOOL-dBoundRoles-44@rev-1 TOOL-dBoundRoles-45@rev-1 TOOL-dBoundRoles-46@rev-1 TOOL-dBoundRoles-47@rev-1 TOOL-dBoundRoles-48@rev-1 TOOL-dBoundRoles-49@rev-1 TOOL-dBoundRoles-50@rev-1 TOOL-dBoundRoles-51@rev-1 TOOL-dBoundRoles-52@rev-1 TOOL-dBoundRoles-53@rev-1
TOOL-dBoundRoles-54@rev-1 TOOL-dBoundRoles-55@rev-1 TOOL-dBoundRoles-56@rev-1 TOOL-dBoundRoles-57@rev-1 TOOL-dBoundRoles-58@rev-1 TOOL-dBoundRoles-59@rev-1 TOOL-dBoundRoles-60@rev-1 TOOL-dBoundRoles-61@rev-1 TOOL-dBoundRoles-62@rev-1 TOOL-dBoundRoles-63@rev-1 TOOL-dBoundRoles-64@rev-1
TOOL-dBoundRoles-65@rev-1 TOOL-dBoundRoles-66@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dBoundRoles's 26 clause(s) and 15 owned node(s), over 59 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 26
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-26-spec-TOOL-dBoundRoles-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-39.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-41.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-43.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-45.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-47.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-51.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-55.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-59.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-61.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-63.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-64.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-65.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-66.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-67.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-TOOL-dBoundRoles-68.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-TOOL-dBoundRoles-69.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0166, cl-dClosedLoop-0167, cl-dClosedLoop-0168, cl-dClosedLoop-0173, cl-dClosedLoop-0178, cl-dClosedLoop-0187, cl-dClosedLoop-0189
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dBoundRoles-14` | no |
| 2 | `TOOL-dBoundRoles-2` | no |
| 3 | `TOOL-dBoundRoles-1` | no |
| 4 | `TOOL-dBoundRoles-21`, `TOOL-dBoundRoles-37` | yes |
| 5 | `TOOL-dBoundRoles-22`, `TOOL-dBoundRoles-49` | yes |
| 6 | `TOOL-dBoundRoles-16`, `TOOL-dBoundRoles-54`, `TOOL-dBoundRoles-55` | no |
| 7 | `TOOL-dBoundRoles-15` | no |
| 8 | `TOOL-dBoundRoles-17` | no |
| 9 | `TOOL-dBoundRoles-6` | no |
| 10 | `TOOL-dBoundRoles-13` | no |
| 11 | `TOOL-dBoundRoles-3`, `TOOL-dBoundRoles-38` | no |
| 12 | `TOOL-dBoundRoles-45`, `TOOL-dBoundRoles-46`, `TOOL-dBoundRoles-48`, `TOOL-dBoundRoles-8` | no |
| 13 | `TOOL-dBoundRoles-9` | no |
| 14 | `TOOL-dBoundRoles-7` | no |
| 15 | `TOOL-dBoundRoles-5` | no |
| 16 | `TOOL-dBoundRoles-10`, `TOOL-dBoundRoles-39`, `TOOL-dBoundRoles-40` | no |
| 17 | `TOOL-dBoundRoles-4` | no |
| 18 | `TOOL-dBoundRoles-23` | no |
| 19 | `TOOL-dBoundRoles-24` | no |
| 20 | `TOOL-dBoundRoles-12`, `TOOL-dBoundRoles-41` | yes |
| 21 | `TOOL-dBoundRoles-11`, `TOOL-dBoundRoles-47` | no |
| 22 | `TOOL-dBoundRoles-26`, `TOOL-dBoundRoles-52`, `TOOL-dBoundRoles-53` | no |
| 23 | `TOOL-dBoundRoles-20`, `TOOL-dBoundRoles-59` | no |
| 24 | `TOOL-dBoundRoles-19`, `TOOL-dBoundRoles-61` | no |
| 25 | `TOOL-dBoundRoles-18` | no |
| 26 | `TOOL-dBoundRoles-25` | no |
| 27 | `TOOL-dBoundRoles-42` | no |
| 28 | `TOOL-dBoundRoles-43` | no |
| 29 | `TOOL-dBoundRoles-44` | no |
| 30 | `TOOL-dBoundRoles-50`, `TOOL-dBoundRoles-51` | yes |
| 31 | `TOOL-dBoundRoles-56`, `TOOL-dBoundRoles-57` | yes |
| 32 | `TOOL-dBoundRoles-58` | no |
| 33 | `TOOL-dBoundRoles-60` | no |
| 34 | `TOOL-dBoundRoles-62` | no |
| 35 | `TOOL-dBoundRoles-63` | no |
| 36 | `TOOL-dBoundRoles-64` | no |
| 37 | `TOOL-dBoundRoles-65`, `TOOL-dBoundRoles-66` | yes |
| 38 | `TOOL-dBoundRoles-67`, `TOOL-dBoundRoles-68` | yes |
| 39 | `TOOL-dBoundRoles-69` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dFurnishedOrders](../dFurnishedOrders/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dRankedPlan](../dRankedPlan/README.md), [dShippedRelease](../dShippedRelease/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->

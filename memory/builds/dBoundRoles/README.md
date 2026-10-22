---
slug: dBoundRoles
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-27
status: OPEN
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
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15
ids TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-27

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dBoundRoles's 26 clause(s) and 15 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 26 (cl-dClosedLoop-0166, cl-dClosedLoop-0167, cl-dClosedLoop-0168, cl-dClosedLoop-0169, cl-dClosedLoop-0170, cl-dClosedLoop-0171, cl-dClosedLoop-0172, cl-dClosedLoop-0173, cl-dClosedLoop-0174, cl-dClosedLoop-0175, cl-dClosedLoop-0176, cl-dClosedLoop-0177, cl-dClosedLoop-0178,
  cl-dClosedLoop-0179, cl-dClosedLoop-0180, cl-dClosedLoop-0181, cl-dClosedLoop-0182, cl-dClosedLoop-0183, cl-dClosedLoop-0184, cl-dClosedLoop-0185, cl-dClosedLoop-0186, cl-dClosedLoop-0187, cl-dClosedLoop-0188, cl-dClosedLoop-0189, cl-dClosedLoop-0190, cl-dClosedLoop-0191)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: policy-key.driver.reads, policy-key.instructions.task-charter, policy-key.prompts.author, policy-key.roles.effort.<role>, policy-key.roles.effort.<workflow>.<stage>, policy-key.roles.effort.default, policy-key.roles.model.<role>.<harness>, policy-key.roles.no-spawn,
  policy-key.roles.retries, policy-key.run.on-owner-question, record-kind.work-order, system.role-shapes, tag-namespace.field, tag-namespace.role, tag-namespace.workflow
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0166, cl-dClosedLoop-0167, cl-dClosedLoop-0168, cl-dClosedLoop-0169, cl-dClosedLoop-0172, cl-dClosedLoop-0173, cl-dClosedLoop-0178, cl-dClosedLoop-0187, cl-dClosedLoop-0189
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dFurnishedOrders](../dFurnishedOrders/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dRankedPlan](../dRankedPlan/README.md), [dShippedRelease](../dShippedRelease/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->

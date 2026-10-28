---
slug: dIndexedDesign
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-21 TOOL-dIndexedDesign-22 TOOL-dIndexedDesign-23 TOOL-dIndexedDesign-24 TOOL-dIndexedDesign-25 TOOL-dIndexedDesign-26 TOOL-dIndexedDesign-27 TOOL-dIndexedDesign-28 TOOL-dIndexedDesign-29 TOOL-dIndexedDesign-30
spec-audit: 2026-10-21
parents: dDeclaredLoop dTotalRecall dKeptSession dBoundRoles dLinkedLibrary
may: PLAY-dClosedLoop-3
---

# dIndexedDesign — the Design build of the dClosedLoop chain

## The problem this build exists to solve

dIndexedDesign owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-flow-01,
gap-design-02, gap-design-03, gap-design-04, gap-design-05, gap-design-06, gap-design-07, gap-design-09,
gap-design-10, gap-flow-17, gap-design-11, gap-design-12, gap-flow-25. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 16 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 2 child builds wait on it: dScopedBuild, dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dIndexedDesign` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dIndexedDesign`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
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
| 1 | `TOOL-dIndexedDesign-1` | `cl-dClosedLoop-0383@77f2882f` | the Design-to-Build hand-off as `design.handoff` says |
| 2 | `TOOL-dIndexedDesign-2` | `cl-dClosedLoop-0384@372bd58d` | the design index |
| 3 | `TOOL-dIndexedDesign-3` | `cl-dClosedLoop-0385@7bdb7329` | design review by policy |
| 4 | `TOOL-dIndexedDesign-4` | `cl-dClosedLoop-0386@1f72161f` | reuse and alternatives backed by recorded probes |
| 5 | `TOOL-dIndexedDesign-5` | `cl-dClosedLoop-0387@f264e3f3` | the research harness |
| 6 | `TOOL-dIndexedDesign-6` | `cl-dClosedLoop-0388@deaac21c` | agreement and tier checks |
| 7 | `TOOL-dIndexedDesign-7` | `cl-dClosedLoop-0389@158d7ac4` | the spec measured |
| 8 | `TOOL-dIndexedDesign-8` | `cl-dClosedLoop-0390@a096f77c` | the feature level (build |
| 9 | `TOOL-dIndexedDesign-9` | `cl-dClosedLoop-0391@17b40187` | spec sections named by tag across tiers |
| 10 | `TOOL-dIndexedDesign-10` | `cl-dClosedLoop-0392@c9f3c2f0` | the playbook record kind: dScriptedRepeat's canon |
| 11 | `TOOL-dIndexedDesign-11` | `cl-dClosedLoop-0393@c8409a33` | the playbook set record and its set check |
| 12 | `TOOL-dIndexedDesign-12` | `cl-dClosedLoop-0394@97e00df6` | the structured spec declaring `implements=` and `decides=` edges |
| 13 | `TOOL-dIndexedDesign-13` | `cl-dClosedLoop-0395@07a81090` | the reuse scout's return under aScoutedSeam's M1c contract: needs and a concrete sketch before the search |
| 14 | `TOOL-dIndexedDesign-14` | `cl-dClosedLoop-0396@bf718415` | the reuse scout's return also naming at most five bug classes by intent |
| 15 | `TOOL-dIndexedDesign-15` | `cl-dClosedLoop-0397@155d665e` | the planner's `design.streams` item after `design.overlaps` |
| 16 | `TOOL-dIndexedDesign-16` | `cl-dClosedLoop-0398@f6f6546a` | the design coverage under `design.coverage` and `design.coverage.semantic`: dTrueNorth's join read at each Design exit and at each spec's revision |
| 17 | `TOOL-dIndexedDesign-20` | `cl-dClosedLoop-0390@a096f77c` part 2/2 | the feature level's re-entry by `design.reentry`, the additive-versus-breaking diff, `design.input` and the re-design inventory |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 17 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13
ids TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-21 TOOL-dIndexedDesign-22 TOOL-dIndexedDesign-23 TOOL-dIndexedDesign-24 TOOL-dIndexedDesign-25
ids TOOL-dIndexedDesign-26 TOOL-dIndexedDesign-27 TOOL-dIndexedDesign-28 TOOL-dIndexedDesign-29 TOOL-dIndexedDesign-30

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dIndexedDesign-9 — spec sections named by tag across tiers: one heading rule, one reader and its twins, and the tagged canon behind a cutoff](spec/2026-10-28-spec-TOOL-dIndexedDesign-9.md) | 1 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-12 — the structured spec's typed edges: `implements=` and `decides=` read through one spec-site adapter, and `design.seams` reading a tag's bundle](spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md) | 2 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-16 — design coverage by policy: the carries join read at each Design exit and each spec revision, `UNCARRIED`, and the coverage lens](spec/2026-10-28-spec-TOOL-dIndexedDesign-16.md) | 3 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-1 — the Design-to-Build hand-off as `design.handoff` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-1.md) | 4 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-7 — the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract](spec/2026-10-28-spec-TOOL-dIndexedDesign-7.md) | 5 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-2 — the design index: overlaps between live designs, as `design.overlap` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-2.md) | 6 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-6 — agreement and tier checks: the interface and scope axes, the tier rule as a predicate, and sibling specs read from unmerged refs](spec/2026-10-28-spec-TOOL-dIndexedDesign-6.md) | 7 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-8 — the feature level: `design.decompose`'s feature designs, roster and fork records, forks resolved as `design.forks` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-8.md) | 8 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-13 — the reuse scout's return under M1c's contract: the `seams` record, its caps and MUST definition, read once and its seams handed on as rows](spec/2026-10-28-spec-TOOL-dIndexedDesign-13.md) | 9 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-20 — two-level re-entry: `design.input`'s pin, `design.reentry`'s additive-versus-breaking diff record, and the re-design inventory](spec/2026-10-28-spec-TOOL-dIndexedDesign-20.md) | 9 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-5 — the research harness: one experiment factory on dBoundRoles' `experiment` shape, the reuse bench its first entry](spec/2026-10-28-spec-TOOL-dIndexedDesign-5.md) | 10 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-4 — reuse and alternatives backed by recorded probes: the §10 outcome joined to its scout record, each rejected candidate to its test](spec/2026-10-28-spec-TOOL-dIndexedDesign-4.md) | 11 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-14 — the scout's bug classes by intent: at most five from the catalogue's index, armed only by a replay that beats the anchor ranking's top five](spec/2026-10-28-spec-TOOL-dIndexedDesign-14.md) | 12 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-10 — the playbook record kind: its row, its one resolver, the `repeat` route resolving through it, and `check-playbook` as Design's pack](spec/2026-10-28-spec-TOOL-dIndexedDesign-10.md) | 13 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-11 — the playbook set record as a kind, its identity derived once, and a set check that reds at the bar, registered at Test's leg-pack point](spec/2026-10-28-spec-TOOL-dIndexedDesign-11.md) | 14 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-15 — the planner's `design.streams` item: the planning workflow, its run decision under `design.streams-when`, and the stream plan checked against order, write sets and the overlap record](spec/2026-10-28-spec-TOOL-dIndexedDesign-15.md) | 15 | 2 | OPEN | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-3 — design review by policy: `review.design` read at the guarded revision, its effort, and the opt-in guard](spec/2026-10-28-spec-TOOL-dIndexedDesign-3.md) | 16 | 2 | OPEN | rev-1 | 2026-10-28 |
<!-- /gen:build-units -->

Records: 15 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-3
TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9.

Ids whose spec moved past its audited revision: none — 0 of 17 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dIndexedDesign's 16 clause(s) and 28 owned node(s), over 17 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 15
- carried in parts: 1 (cl-dClosedLoop-0390)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0385, cl-dClosedLoop-0386, cl-dClosedLoop-0388, cl-dClosedLoop-0389, cl-dClosedLoop-0391, cl-dClosedLoop-0393, cl-dClosedLoop-0395, cl-dClosedLoop-0396
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dIndexedDesign-9` | no |
| 2 | `TOOL-dIndexedDesign-12` | no |
| 3 | `TOOL-dIndexedDesign-16` | no |
| 4 | `TOOL-dIndexedDesign-1` | no |
| 5 | `TOOL-dIndexedDesign-7` | no |
| 6 | `TOOL-dIndexedDesign-2` | no |
| 7 | `TOOL-dIndexedDesign-6` | no |
| 8 | `TOOL-dIndexedDesign-8` | no |
| 9 | `TOOL-dIndexedDesign-13`, `TOOL-dIndexedDesign-20` | no |
| 10 | `TOOL-dIndexedDesign-5` | no |
| 11 | `TOOL-dIndexedDesign-4` | no |
| 12 | `TOOL-dIndexedDesign-14` | no |
| 13 | `TOOL-dIndexedDesign-10` | no |
| 14 | `TOOL-dIndexedDesign-11` | no |
| 15 | `TOOL-dIndexedDesign-15` | no |
| 16 | `TOOL-dIndexedDesign-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md), [dKeptSession](../dKeptSession/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dScopedBuild](../dScopedBuild/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

---
slug: dIndexedDesign
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19
status: OPEN
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13
ids TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dIndexedDesign's 16 clause(s) and 28 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 16 (cl-dClosedLoop-0383, cl-dClosedLoop-0384, cl-dClosedLoop-0385, cl-dClosedLoop-0386, cl-dClosedLoop-0387, cl-dClosedLoop-0388, cl-dClosedLoop-0389, cl-dClosedLoop-0390, cl-dClosedLoop-0391, cl-dClosedLoop-0392, cl-dClosedLoop-0393, cl-dClosedLoop-0394, cl-dClosedLoop-0395,
  cl-dClosedLoop-0396, cl-dClosedLoop-0397, cl-dClosedLoop-0398)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.design.decompose, item.design.exit, item.design.input, item.design.inventory, item.design.overlaps, item.design.ready, item.design.reentry, item.design.research, item.design.seams, item.design.streams, item.design.unit-spec, policy-key.design.coverage,
  policy-key.design.coverage.semantic, policy-key.design.forks, policy-key.design.handoff, policy-key.design.overlap, policy-key.design.reentry, policy-key.design.streams-when, record-kind.diff, record-kind.feature-design, record-kind.fork, record-kind.inventory, record-kind.overlap,
  record-kind.playbook, record-kind.playbook-set, record-kind.roster, record-kind.seams, record-kind.spec
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0385, cl-dClosedLoop-0386, cl-dClosedLoop-0388, cl-dClosedLoop-0389, cl-dClosedLoop-0391, cl-dClosedLoop-0393, cl-dClosedLoop-0395, cl-dClosedLoop-0396
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md), [dKeptSession](../dKeptSession/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dScopedBuild](../dScopedBuild/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

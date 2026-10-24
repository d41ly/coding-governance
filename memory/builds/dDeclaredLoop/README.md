---
slug: dDeclaredLoop
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35
status: OPEN
spec-audit: 2026-10-21
parents: dOrderedCharter dFairHearing
may: PLAY-dClosedLoop-3
---

# dDeclaredLoop — the Spine build of the dClosedLoop chain

## The problem this build exists to solve

dDeclaredLoop owns 17 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-spine-01,
gap-spine-02, gap-orient-03, gap-orient-05, gap-flow-13, gap-flow-14, gap-flow-15, gap-spine-07, gap-flow-11,
gap-flow-12, gap-spine-08, gap-spine-09, gap-flow-19, gap-flow-20, gap-flow-21, gap-flow-23, gap-flow-24. Closing
every one is this build's goal bound.

## Expected improvements

- Each of the 34 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 17 owned gaps above close.

## Detriments if this is not built

- Its 17 owned gaps stay open.
- Its 7 child builds wait on it: dPlacedRequest, dKeptSession, dBoundRoles, dTotalRecall, dWitnessedBar, dRankedPlan,
  dIndexedDesign.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dDeclaredLoop` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dDeclaredLoop`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-13.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dDeclaredLoop-1` | `cl-dClosedLoop-0086@76547911` | the loop kit and definition keyed by the stage tags |
| 2 | `TOOL-dDeclaredLoop-2` | `cl-dClosedLoop-0087@5eb8d36a` | the guard |
| 3 | `TOOL-dDeclaredLoop-3` | `cl-dClosedLoop-0088@b1722a1e` | the transition record three ways |
| 4 | `TOOL-dDeclaredLoop-4` | `cl-dClosedLoop-0089@66b8552a` | stage claims and the coverage gate |
| 5 | `TOOL-dDeclaredLoop-5` | `cl-dClosedLoop-0090@e3f362f0` | the witness-class rule |
| 6 | `TOOL-dDeclaredLoop-6` | `cl-dClosedLoop-0091@48218b99` | the factories and conformance gates for commands |
| 7 | `TOOL-dDeclaredLoop-7` | `cl-dClosedLoop-0092@0abbde28` | the position engine: deriving each unit's step |
| 8 | `TOOL-dDeclaredLoop-8` | `cl-dClosedLoop-0093@a21f7ad5` | claims keyed and trusted by key and source |
| 9 | `TOOL-dDeclaredLoop-9` | `cl-dClosedLoop-0094@c69a5ae1` | each step's items declared with actor |
| 10 | `TOOL-dDeclaredLoop-10` | `cl-dClosedLoop-0095@46379602` | backward transitions recorded like forward ones |
| 11 | `TOOL-dDeclaredLoop-11` | `cl-dClosedLoop-0096@18103ca9` | every checklist item named by a semantic tag |
| 12 | `TOOL-dDeclaredLoop-12` | `cl-dClosedLoop-0097@56655276` | each step a program of items with declared dependencies |
| 13 | `TOOL-dDeclaredLoop-13` | `cl-dClosedLoop-0098@89542705` | one transition table per level (build |
| 14 | `TOOL-dDeclaredLoop-14` | `cl-dClosedLoop-0099@60eee5d8` | a default failure route (the refusal recorded |
| 15 | `TOOL-dDeclaredLoop-15` | `cl-dClosedLoop-0100@4771709c` | the terminal states flow-steps' `[transitions]` declares |
| 16 | `TOOL-dDeclaredLoop-16` | `cl-dClosedLoop-0101@6e645e0e` | one closed disposition set |
| 17 | `TOOL-dDeclaredLoop-17` | `cl-dClosedLoop-0102@5579244a` | witnesses computed rather than typed by the acting agent (acceptance re-run by the executor |
| 18 | `TOOL-dDeclaredLoop-18` | `cl-dClosedLoop-0103@2d82c817` | the `step` |
| 19 | `TOOL-dDeclaredLoop-19` | `cl-dClosedLoop-0104@2c27f8f3` | breakpoints placeable at any item boundary (`review.breakpoints`) |
| 20 | `TOOL-dDeclaredLoop-20` | `cl-dClosedLoop-0105@cab8e16c` | the breakpoint program's own items |
| 21 | `TOOL-dDeclaredLoop-21` | `cl-dClosedLoop-0106@90aa01b6` | follow-up closing-review rounds by `review.follow-up` |
| 22 | `TOOL-dDeclaredLoop-22` | `cl-dClosedLoop-0107@a606d808` | the stage-exit recommendation: every step's recommend and reason items |
| 23 | `TOOL-dDeclaredLoop-23` | `cl-dClosedLoop-0108@df656363` | the commit node and its kind |
| 24 | `TOOL-dDeclaredLoop-24` | `cl-dClosedLoop-0109@48e119fc` | the `item` kind in the kinds register with its factory |
| 25 | `TOOL-dDeclaredLoop-25` | `cl-dClosedLoop-0110@c46e726a` | a repository's own stages |
| 26 | `TOOL-dDeclaredLoop-26` | `cl-dClosedLoop-0111@313dbc9c` | a build's composition pinned per step: the transition record into a step carrying the composition's revision |
| 27 | `TOOL-dDeclaredLoop-27` | `cl-dClosedLoop-0112@de8c6c54` | the `scenario` kind in the kinds register and its namespace: gov's shipped scenarios |
| 28 | `TOOL-dDeclaredLoop-28` | `cl-dClosedLoop-0113@11f77a79` | a build's recorded changes: rows a role proposes for its own build |
| 29 | `TOOL-dDeclaredLoop-29` | `cl-dClosedLoop-0114@f3e34c2f` | an item's `upstream` field naming the items whose commitments it must answer |
| 30 | `TOOL-dDeclaredLoop-30` | `cl-dClosedLoop-0115@cc7f99e5` | the rework budget: one per build in its transition record |
| 31 | `TOOL-dDeclaredLoop-31` | `cl-dClosedLoop-0116@d75a79f0` | `flow.on-exhausted`: a build whose budget is spent ends and never laps again |
| 32 | `TOOL-dDeclaredLoop-32` | `cl-dClosedLoop-0117@166df103` | the convergence routing: every `until-*` and `while-*` value |
| 33 | `TOOL-dDeclaredLoop-33` | `cl-dClosedLoop-0118@4c8ef789` | the static termination check on every composition |
| 34 | `TOOL-dDeclaredLoop-34` | `cl-dClosedLoop-0119@a9b53abc` | the deviation approval route under `deviation.approval`: by its risk |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13
ids TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26
ids TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 8 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dDeclaredLoop's 34 clause(s) and 49 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 34 (cl-dClosedLoop-0086, cl-dClosedLoop-0087, cl-dClosedLoop-0088, cl-dClosedLoop-0089, cl-dClosedLoop-0090, cl-dClosedLoop-0091, cl-dClosedLoop-0092, cl-dClosedLoop-0093, cl-dClosedLoop-0094, cl-dClosedLoop-0095, cl-dClosedLoop-0096, cl-dClosedLoop-0097, cl-dClosedLoop-0098,
  cl-dClosedLoop-0099, cl-dClosedLoop-0100, cl-dClosedLoop-0101, cl-dClosedLoop-0102, cl-dClosedLoop-0103, cl-dClosedLoop-0104, cl-dClosedLoop-0105, cl-dClosedLoop-0106, cl-dClosedLoop-0107, cl-dClosedLoop-0108, cl-dClosedLoop-0109, cl-dClosedLoop-0110, cl-dClosedLoop-0111, cl-dClosedLoop-0112,
  cl-dClosedLoop-0113, cl-dClosedLoop-0114, cl-dClosedLoop-0115, cl-dClosedLoop-0116, cl-dClosedLoop-0117, cl-dClosedLoop-0118, cl-dClosedLoop-0119)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.build.recommend, item.deploy.recommend, item.design.reason, item.design.recommend, item.plan.reason, item.plan.recommend, item.review.cost, item.review.dispose, item.review.fold, item.review.trigger, item.test.reason, item.test.recommend, policy-key.autonomy,
  policy-key.deps.on-parent-withdrawn, policy-key.deviation.approval, policy-key.floor, policy-key.flow.adapt, policy-key.flow.on-exhausted, policy-key.flow.rework-budget, policy-key.flow.route-backs, policy-key.flow.scenario-conflict, policy-key.flow.scenario-default, policy-key.flow.wait-ceiling,
  policy-key.policy-file.guard, policy-key.policy-file.on-missing-expansion, policy-key.policy-file.proof, policy-key.review.<stage>, policy-key.review.blocks, policy-key.review.breakpoints, policy-key.review.design.round-count, policy-key.review.design.rounds, policy-key.review.findings,
  policy-key.review.follow-up, policy-key.review.left-shift, policy-key.review.max-rounds, policy-key.review.recommendation, policy-key.review.recommendation.source, policy-key.review.unverified, policy-key.transitions.record, record-kind.acceptance, record-kind.commit, record-kind.disposition,
  record-kind.recommendation, record-kind.transition, tag-namespace.command, tag-namespace.item, tag-namespace.policy, tag-namespace.scenario, tag-namespace.step
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0086, cl-dClosedLoop-0089, cl-dClosedLoop-0090, cl-dClosedLoop-0091, cl-dClosedLoop-0092, cl-dClosedLoop-0093, cl-dClosedLoop-0094, cl-dClosedLoop-0095, cl-dClosedLoop-0096, cl-dClosedLoop-0097, cl-dClosedLoop-0098, cl-dClosedLoop-0101,
  cl-dClosedLoop-0102, cl-dClosedLoop-0111
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dOrderedCharter](../dOrderedCharter/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dKeptSession](../dKeptSession/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dRankedPlan](../dRankedPlan/README.md), [dTotalRecall](../dTotalRecall/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
<!-- /gen:build-edges -->

---
slug: dDeclaredLoop
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35
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
**Build status:** OPEN · 34 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13
ids TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26
ids TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dDeclaredLoop-18 — the `step`, `item`, `policy` and `command` tag namespaces, with their extractors](spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md) | 1 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-1 — the loop kit and its definition keyed by the stage tags, the roles kit's stage table moved into it](spec/2026-10-24-spec-TOOL-dDeclaredLoop-1.md) | 2 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-23 — the commit node and its kind, and one trailer reader with both views](spec/2026-10-24-spec-TOOL-dDeclaredLoop-23.md) | 3 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-16 — one closed disposition set, and the owner's disposition record](spec/2026-10-24-spec-TOOL-dDeclaredLoop-16.md) | 4 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-5 — the witness-class rule: every witness classed, the actor class refused](spec/2026-10-24-spec-TOOL-dDeclaredLoop-5.md) | 5 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-12 — each step a program of items with declared needs, outcomes and routes](spec/2026-10-24-spec-TOOL-dDeclaredLoop-12.md) | 6 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-9 — each step's items declared with one actor, inputs, allowance, return schema and witness](spec/2026-10-24-spec-TOOL-dDeclaredLoop-9.md) | 7 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-17 — witnesses computed rather than typed by the acting agent](spec/2026-10-24-spec-TOOL-dDeclaredLoop-17.md) | 8 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-11 — every checklist item named by a semantic tag, its number only display order](spec/2026-10-24-spec-TOOL-dDeclaredLoop-11.md) | 9 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-13 — one transition table per level, the engine refusing a move it lacks](spec/2026-10-24-spec-TOOL-dDeclaredLoop-13.md) | 10 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-24 — the `item` kind in the kinds register, its factory, and the checks over the composed items](spec/2026-10-24-spec-TOOL-dDeclaredLoop-24.md) | 11 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-15 — the build table's terminal states, and `deps.on-parent-withdrawn` routing a withdrawn parent](spec/2026-10-24-spec-TOOL-dDeclaredLoop-15.md) | 12 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-3 — the transition record three ways, its channels the set `transitions.record` selects](spec/2026-10-24-spec-TOOL-dDeclaredLoop-3.md) | 13 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-10 — backward transitions recorded like forward ones](spec/2026-10-24-spec-TOOL-dDeclaredLoop-10.md) | 14 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-2 — the guard, the TTY policy command and the default floor](spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md) | 15 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-8 — claims keyed and trusted by key and source](spec/2026-10-24-spec-TOOL-dDeclaredLoop-8.md) | 16 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-7 — the position engine: each unit's step, the build's step and the next item, from witnesses](spec/2026-10-24-spec-TOOL-dDeclaredLoop-7.md) | 17 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-14 — the default failure route: the refusal recorded and the frontier returned](spec/2026-10-24-spec-TOOL-dDeclaredLoop-14.md) | 18 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-4 — stage claims and the coverage gate](spec/2026-10-24-spec-TOOL-dDeclaredLoop-4.md) | 19 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-6 — the factories and conformance gates for commands, policy keys, stages, hooks, roles and workflows](spec/2026-10-24-spec-TOOL-dDeclaredLoop-6.md) | 20 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-25 — a repository's own stages, spliced between two adjacent gov stages](spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md) | 21 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-29 — an item's upstream field: commitment rows handed on, answered at the return, gating only a measured edge](spec/2026-10-24-spec-TOOL-dDeclaredLoop-29.md) | 22 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-26 — a build's composition pinned per step, its position read at the pin, and the move at the next step boundary](spec/2026-10-24-spec-TOOL-dDeclaredLoop-26.md) | 23 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-27 — the scenario kind and namespace: gov's five scenarios, admission, conflicts and the pin per step](spec/2026-10-24-spec-TOOL-dDeclaredLoop-27.md) | 24 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-28 — a build's recorded changes under flow.adapt, applied at its next step boundary, and its witnessed path held to its composition](spec/2026-10-24-spec-TOOL-dDeclaredLoop-28.md) | 25 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-21 — the review round bounds as policy keys: review.max-rounds, the design rounds and follow-ups, REVIEW_ROUNDS and RUNAWAY_CEILING retired](spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md) | 26 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-34 — the deviation approval route read from deviation.approval: by its risk, the owner for all, or its author recorded](spec/2026-10-24-spec-TOOL-dDeclaredLoop-34.md) | 27 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-30 — the rework budget: one per build on its transition record, frozen at Design's exit, drawn by every repetition and never by contention](spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md) | 28 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-32 — the convergence routing: every until and while loop ends on a non-decrease of its blocker and high count, its findings promoted by budget](spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md) | 29 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-31 — `flow.on-exhausted`: a build whose budget is spent ends by a transition row, and never laps again](spec/2026-10-24-spec-TOOL-dDeclaredLoop-31.md) | 30 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-20 — the breakpoint program's own items: trigger, dispose, fold and cost, and the four keys `review.dispose` reads](spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md) | 31 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-22 — the stage-exit recommendation: a command scores it, the producing role reasons it, one record carries both](spec/2026-10-24-spec-TOOL-dDeclaredLoop-22.md) | 32 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-19 — breakpoints at any item boundary: reviews and owner gates one mechanism under `review.breakpoints`, `review.<stage>` and `autonomy`](spec/2026-10-24-spec-TOOL-dDeclaredLoop-19.md) | 33 | 2 | OPEN | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-33 — the static termination check on every composition, at the push and at each step boundary](spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md) | 34 | 2 | OPEN | rev-1 | 2026-10-24 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19
TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-30
TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9.

Ids whose spec moved past its audited revision: none — 0 of 34 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dDeclaredLoop's 34 clause(s) and 49 owned node(s), over 34 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 34
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0086, cl-dClosedLoop-0089, cl-dClosedLoop-0090, cl-dClosedLoop-0091, cl-dClosedLoop-0092, cl-dClosedLoop-0093, cl-dClosedLoop-0094, cl-dClosedLoop-0095, cl-dClosedLoop-0096, cl-dClosedLoop-0097, cl-dClosedLoop-0098, cl-dClosedLoop-0101,
  cl-dClosedLoop-0102, cl-dClosedLoop-0111
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dDeclaredLoop-18` | no |
| 2 | `TOOL-dDeclaredLoop-1` | no |
| 3 | `TOOL-dDeclaredLoop-23` | no |
| 4 | `TOOL-dDeclaredLoop-16` | no |
| 5 | `TOOL-dDeclaredLoop-5` | no |
| 6 | `TOOL-dDeclaredLoop-12` | no |
| 7 | `TOOL-dDeclaredLoop-9` | no |
| 8 | `TOOL-dDeclaredLoop-17` | no |
| 9 | `TOOL-dDeclaredLoop-11` | no |
| 10 | `TOOL-dDeclaredLoop-13` | no |
| 11 | `TOOL-dDeclaredLoop-24` | no |
| 12 | `TOOL-dDeclaredLoop-15` | no |
| 13 | `TOOL-dDeclaredLoop-3` | no |
| 14 | `TOOL-dDeclaredLoop-10` | no |
| 15 | `TOOL-dDeclaredLoop-2` | no |
| 16 | `TOOL-dDeclaredLoop-8` | no |
| 17 | `TOOL-dDeclaredLoop-7` | no |
| 18 | `TOOL-dDeclaredLoop-14` | no |
| 19 | `TOOL-dDeclaredLoop-4` | no |
| 20 | `TOOL-dDeclaredLoop-6` | no |
| 21 | `TOOL-dDeclaredLoop-25` | no |
| 22 | `TOOL-dDeclaredLoop-29` | no |
| 23 | `TOOL-dDeclaredLoop-26` | no |
| 24 | `TOOL-dDeclaredLoop-27` | no |
| 25 | `TOOL-dDeclaredLoop-28` | no |
| 26 | `TOOL-dDeclaredLoop-21` | no |
| 27 | `TOOL-dDeclaredLoop-34` | no |
| 28 | `TOOL-dDeclaredLoop-30` | no |
| 29 | `TOOL-dDeclaredLoop-32` | no |
| 30 | `TOOL-dDeclaredLoop-31` | no |
| 31 | `TOOL-dDeclaredLoop-20` | no |
| 32 | `TOOL-dDeclaredLoop-22` | no |
| 33 | `TOOL-dDeclaredLoop-19` | no |
| 34 | `TOOL-dDeclaredLoop-33` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dOrderedCharter](../dOrderedCharter/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dKeptSession](../dKeptSession/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dRankedPlan](../dRankedPlan/README.md), [dTotalRecall](../dTotalRecall/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
<!-- /gen:build-edges -->

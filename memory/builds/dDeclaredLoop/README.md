---
slug: dDeclaredLoop
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-101 TOOL-dDeclaredLoop-102 TOOL-dDeclaredLoop-103 TOOL-dDeclaredLoop-104 TOOL-dDeclaredLoop-105 TOOL-dDeclaredLoop-106 TOOL-dDeclaredLoop-107
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
**Build status:** DEFERRED · 99 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13
ids TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26
ids TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-35 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39
ids TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52
ids TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65
ids TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78
ids TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91
ids TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-101 TOOL-dDeclaredLoop-102 TOOL-dDeclaredLoop-103 TOOL-dDeclaredLoop-104
ids TOOL-dDeclaredLoop-105 TOOL-dDeclaredLoop-106 TOOL-dDeclaredLoop-107

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dDeclaredLoop-18 — the `step`, `item`, `policy` and `command` tag namespaces, with their extractors](spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-25 |
| [TOOL-dDeclaredLoop-1 — the loop kit and its definition keyed by the stage tags, the roles kit's stage table moved into it](spec/2026-10-24-spec-TOOL-dDeclaredLoop-1.md) | 2 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [TOOL-dDeclaredLoop-23 — the commit node and its kind, and one trailer reader with both views](spec/2026-10-24-spec-TOOL-dDeclaredLoop-23.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-36 — the loop kit in govkit's default selection, so a default apply installs what roles requires](spec/2026-10-24-spec-TOOL-dDeclaredLoop-36.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-16 — one closed disposition set, and the owner's disposition record](spec/2026-10-24-spec-TOOL-dDeclaredLoop-16.md) | 4 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-37 — the trailer re-points observed at their call sites, red at base](spec/2026-10-24-spec-TOOL-dDeclaredLoop-37.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-38 — the trailer CLI writes LF only, so a shell loop never keeps a CR on its last token](spec/2026-10-24-spec-TOOL-dDeclaredLoop-38.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-39 — the one trailer reader carries the git pins of the readers it replaces](spec/2026-10-24-spec-TOOL-dDeclaredLoop-39.md) | 4 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-40 — the trailer reader finds the key table through the kit resolver, and reads a floor of keys where none is installed](spec/2026-10-24-spec-TOOL-dDeclaredLoop-40.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-57 — `update` refuses a claimed kit whose `requires` it leaves unmet, on every admission path](spec/2026-10-24-spec-TOOL-dDeclaredLoop-57.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-5 — the witness-class rule: every witness classed, the actor class refused](spec/2026-10-24-spec-TOOL-dDeclaredLoop-5.md) | 5 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-58 — the LF-only criterion reads a counted, non-empty CLI output before it looks for a CR](spec/2026-10-24-spec-TOOL-dDeclaredLoop-58.md) | 5 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-73 — the claimed-requires refusal grades each kit's `requires` at the vintage `update --to` installs](spec/2026-10-24-spec-TOOL-dDeclaredLoop-73.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-12 — each step a program of items with declared needs, outcomes and routes](spec/2026-10-24-spec-TOOL-dDeclaredLoop-12.md) | 6 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-41 — the actor-witness list graded where its builds live, and an adopter's own agent items its own](spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md) | 6 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [TOOL-dDeclaredLoop-9 — each step's items declared with one actor, inputs, allowance, return schema and witness](spec/2026-10-24-spec-TOOL-dDeclaredLoop-9.md) | 7 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-17 — witnesses computed rather than typed by the acting agent](spec/2026-10-24-spec-TOOL-dDeclaredLoop-17.md) | 8 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-11 — every checklist item named by a semantic tag, its number only display order](spec/2026-10-24-spec-TOOL-dDeclaredLoop-11.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-42 — the acceptance re-run bounded on the clock, its commands run by bash, never cmd.exe](spec/2026-10-24-spec-TOOL-dDeclaredLoop-42.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-13 — one transition table per level, the engine refusing a move it lacks](spec/2026-10-24-spec-TOOL-dDeclaredLoop-13.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-24 — the `item` kind in the kinds register, its factory, and the checks over the composed items](spec/2026-10-24-spec-TOOL-dDeclaredLoop-24.md) | 11 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-15 — the build table's terminal states, and `deps.on-parent-withdrawn` routing a withdrawn parent](spec/2026-10-24-spec-TOOL-dDeclaredLoop-15.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-3 — the transition record three ways, its channels the set `transitions.record` selects](spec/2026-10-24-spec-TOOL-dDeclaredLoop-3.md) | 13 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-10 — backward transitions recorded like forward ones](spec/2026-10-24-spec-TOOL-dDeclaredLoop-10.md) | 14 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-2 — the guard, the TTY policy command and the default floor](spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md) | 15 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-43 — the guarded write restores each path's prior bytes, and writes each through a sibling temp file](spec/2026-10-24-spec-TOOL-dDeclaredLoop-43.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-44 — the policy push arm grades a merge on its combined diff, and a new branch against the remote default tip](spec/2026-10-24-spec-TOOL-dDeclaredLoop-44.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-8 — claims keyed and trusted by key and source](spec/2026-10-24-spec-TOOL-dDeclaredLoop-8.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-59 — a merge owes a policy trailer only for a key its result sets that no parent and no clean re-merge set](spec/2026-10-24-spec-TOOL-dDeclaredLoop-59.md) | 17 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-7 — the position engine: each unit's step, the build's step and the next item, from witnesses](spec/2026-10-24-spec-TOOL-dDeclaredLoop-7.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-14 — the default failure route: the refusal recorded and the frontier returned](spec/2026-10-24-spec-TOOL-dDeclaredLoop-14.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-45 — a unit reads `built` from its pass commit while no acceptance writer is armed](spec/2026-10-24-spec-TOOL-dDeclaredLoop-45.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-69 — a merge whose clean re-merge is computable is graded against that re-merge alone](spec/2026-10-24-spec-TOOL-dDeclaredLoop-69.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-4 — stage claims and the coverage gate](spec/2026-10-24-spec-TOOL-dDeclaredLoop-4.md) | 19 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-78 — the clean re-merge has three states, and a re-merge that lacks the policy file is graded, never treated as none](spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md) | 19 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-46 — the `stage` claim follows the whole manifest-key path: descriptors, emitter, runner floor and selfcheck](spec/2026-10-24-spec-TOOL-dDeclaredLoop-46.md) | 20 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-6 — the factories and conformance gates for commands, policy keys, stages, hooks, roles and workflows](spec/2026-10-24-spec-TOOL-dDeclaredLoop-6.md) | 20 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-81 — a clean re-merge that fails is its own state and never takes the parent exemption; only a probed absence of the feature does](spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md) | 20 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [TOOL-dDeclaredLoop-25 — a repository's own stages, spliced between two adjacent gov stages](spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md) | 21 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-47 — the stage factory writes a whole conforming stage: its witness, exit item, state and table rows](spec/2026-10-24-spec-TOOL-dDeclaredLoop-47.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-83 — 75 S27 states 81's exit table, so no merge-tree exit but 0 and 1 falls to the parents](spec/2026-10-24-spec-TOOL-dDeclaredLoop-83.md) | 21 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-84 — the specs that restate the clean re-merge's non-zero exits read 81's exit table: 78's states and 82's S27 restatement](spec/2026-10-24-spec-TOOL-dDeclaredLoop-84.md) | 21 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-85 — the write-tree capability probe has three answers, and only a probed absence takes the parent exemption](spec/2026-10-24-spec-TOOL-dDeclaredLoop-85.md) | 21 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [TOOL-dDeclaredLoop-29 — an item's upstream field: commitment rows handed on, answered at the return, gating only a measured edge](spec/2026-10-24-spec-TOOL-dDeclaredLoop-29.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-26 — a build's composition pinned per step, its position read at the pin, and the move at the next step boundary](spec/2026-10-24-spec-TOOL-dDeclaredLoop-26.md) | 23 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-27 — the scenario kind and namespace: gov's five scenarios, admission, conflicts and the pin per step](spec/2026-10-24-spec-TOOL-dDeclaredLoop-27.md) | 24 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-28 — a build's recorded changes under flow.adapt, applied at its next step boundary, and its witnessed path held to its composition](spec/2026-10-24-spec-TOOL-dDeclaredLoop-28.md) | 25 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-21 — the review round bounds as policy keys: review.max-rounds, the design rounds and follow-ups, REVIEW_ROUNDS and RUNAWAY_CEILING retired](spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-34 — the deviation approval route read from deviation.approval: by its risk, the owner for all, or its author recorded](spec/2026-10-24-spec-TOOL-dDeclaredLoop-34.md) | 27 | 2 | DEFERRED | rev-2 | 2026-10-25 |
| [TOOL-dDeclaredLoop-30 — the rework budget: one per build on its transition record, frozen at Design's exit, drawn by every repetition and never by contention](spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md) | 28 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-32 — the convergence routing: every until and while loop ends on a non-decrease of its blocker and high count, its findings promoted by budget](spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-48 — the rework budget keeps a home under every channel set `transitions.record` admits](spec/2026-10-24-spec-TOOL-dDeclaredLoop-48.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-49 — the budget's `spent` counts every draw of the build, across every record, in commit order](spec/2026-10-24-spec-TOOL-dDeclaredLoop-49.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-31 — `flow.on-exhausted`: a build whose budget is spent ends by a transition row, and never laps again](spec/2026-10-24-spec-TOOL-dDeclaredLoop-31.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-60 — the budget reader counts draws in every run record, rotated archives included, under `MEMORY_ROOT`](spec/2026-10-24-spec-TOOL-dDeclaredLoop-60.md) | 30 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-61 — every draw row carries a draw id, so two identical parallel draws stay two rows](spec/2026-10-24-spec-TOOL-dDeclaredLoop-61.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-62 — the transition-record merge driver chosen against the recorded union measurement and the row driver's own refusal](spec/2026-10-24-spec-TOOL-dDeclaredLoop-62.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-20 — the breakpoint program's own items: trigger, dispose, fold and cost, and the four keys `review.dispose` reads](spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-22 — the stage-exit recommendation: a command scores it, the producing role reasons it, one record carries both](spec/2026-10-24-spec-TOOL-dDeclaredLoop-22.md) | 32 | 2 | DEFERRED | rev-3 | 2026-10-25 |
| [TOOL-dDeclaredLoop-50 — the review program's item rows pass the program and declaration checks](spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md) | 32 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-19 — breakpoints at any item boundary: reviews and owner gates one mechanism under `review.breakpoints`, `review.<stage>` and `autonomy`](spec/2026-10-24-spec-TOOL-dDeclaredLoop-19.md) | 33 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-51 — the eight recommendation rows amended in place, their actors in the declaration grammar](spec/2026-10-24-spec-TOOL-dDeclaredLoop-51.md) | 33 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-33 — the static termination check on every composition, at the push and at each step boundary](spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md) | 34 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [TOOL-dDeclaredLoop-52 — the phase-to-state-and-step map shipped as rows with one reader](spec/2026-10-24-spec-TOOL-dDeclaredLoop-52.md) | 34 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-53 — an owner gate holds only builds opened after the gate was placed](spec/2026-10-24-spec-TOOL-dDeclaredLoop-53.md) | 34 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-54 — a terminal set declared per level, and the termination rule run over each table with its own](spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-55 — the `loop termination` leg declares no guard, so no input it reads can skip it](spec/2026-10-24-spec-TOOL-dDeclaredLoop-55.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-63 — an adopter's extra phase reads as ungated through the driver's own phase set, never refused for lacking a row](spec/2026-10-24-spec-TOOL-dDeclaredLoop-63.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-64 — a build's opening commit is found under the resolved `MEMORY_ROOT`, never a literal `memory/`](spec/2026-10-24-spec-TOOL-dDeclaredLoop-64.md) | 35 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-56 — the round-1 spec audit's 47 minors: owed leg rows, one reader each, honest skew and failure paths, and the citations that drifted](spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md) | 36 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [TOOL-dDeclaredLoop-70 — every caller of the phase reading takes the adopter population from one driver-conf reader](spec/2026-10-24-spec-TOOL-dDeclaredLoop-70.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-71 — the breakpoints fixture runs under its own gate leg, so its plants are lasting coverage](spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md) | 36 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-72 — the loop kit reads the records root the driver reads, and refuses two confs that disagree](spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md) | 36 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-65 — the remote's freshness is the time of the last fetch, read from what a fetch and a clone write](spec/2026-10-24-spec-TOOL-dDeclaredLoop-65.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-68 — the witness normaliser has one owner, the run-gates program, before unit 67 reads it](spec/2026-10-24-spec-TOOL-dDeclaredLoop-68.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-76 — the loop readers' no-own-conf-read rule is graded on the syntax tree, and the root's source is a value](spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md) | 37 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-66 — the build-order region derives `Parallel` from the group's write sets and edges, never from a shared order alone](spec/2026-10-24-spec-TOOL-dDeclaredLoop-66.md) | 38 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-67 — the round-2 spec audit's 54 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md) | 38 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-74 — a FETCH_HEAD counts as a fetch only when it holds the default branch of the resolved remote](spec/2026-10-24-spec-TOOL-dDeclaredLoop-74.md) | 38 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-80 — the no-own-conf-read rule stops at a named fixture boundary, so the plants that write the confs are outside its population](spec/2026-10-24-spec-TOOL-dDeclaredLoop-80.md) | 38 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-75 — the round-3 spec audit's 36 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md) | 39 | 2 | DEFERRED | rev-8 | 2026-10-24 |
| [TOOL-dDeclaredLoop-77 — a FETCH_HEAD URL is compared in the spelling git writes it, its user part stripped from both sides](spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md) | 39 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-79 — the round-4 spec audit's 28 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md) | 40 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-82 — the round-5 spec audit's 23 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md) | 41 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-86 — the round-6 spec audit's 22 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md) | 42 | 2 | DEFERRED | rev-7 | 2026-10-24 |
| [TOOL-dDeclaredLoop-87 — the conf-constant kind is stated as a class: any module-level binding whose value holds a conf name, and every import that binds it](spec/2026-10-24-spec-TOOL-dDeclaredLoop-87.md) | 43 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-88 — the round-7 spec audit's 36 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-88.md) | 44 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-89 — the conf-constant class covers a module name a global loader rebinds, and module-level walrus, for and with targets](spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md) | 44 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [TOOL-dDeclaredLoop-90 — the round-8 spec audit's 22 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md) | 45 | 2 | DEFERRED | rev-5 | 2026-10-24 |
| [TOOL-dDeclaredLoop-91 — derive_conf_rebinds reads every position a module evaluates: class bodies, defaults, decorators and bases](spec/2026-10-24-spec-TOOL-dDeclaredLoop-91.md) | 45 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-92 — the round-9 spec audit's 17 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md) | 46 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [TOOL-dDeclaredLoop-93 — 92 AC16 states the push-merge-tree-fatal plant's exit as 1, the code every sibling states](spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md) | 47 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-94 — the round-10 spec audit's 24 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md) | 48 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [TOOL-dDeclaredLoop-95 — the loop kit reads `.memory-tree.conf` through `load_tree_lib`, so 94 AC1's route probe holds on the built tree](spec/2026-10-24-spec-TOOL-dDeclaredLoop-95.md) | 49 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-96 — the round-11 spec audit's 13 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-96.md) | 50 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [TOOL-dDeclaredLoop-97 — the no-own-conf-read rule reads its reader calls from one declared tuple, `CONF_READERS`, which holds `read_tree_conf`](spec/2026-10-24-spec-TOOL-dDeclaredLoop-97.md) | 50 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-98 — the `conf-read-forms` plant proves on every run that the rule answers a call of each declared conf reader](spec/2026-10-24-spec-TOOL-dDeclaredLoop-98.md) | 50 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-99 — every `loop_lib.py` function that opens a conf is in `CONF_READERS`, checked both ways by a definition plant](spec/2026-10-24-spec-TOOL-dDeclaredLoop-99.md) | 50 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [TOOL-dDeclaredLoop-100 — the round-12 spec audit's 21 minors, batched](spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md) | 51 | 2 | DEFERRED | rev-1 | 2026-10-24 |
<!-- /gen:build-units -->

Records: 172 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99.

Ids whose spec moved past its audited revision: TOOL-dDeclaredLoop-1@rev-1 TOOL-dDeclaredLoop-11@rev-1 TOOL-dDeclaredLoop-12@rev-1 TOOL-dDeclaredLoop-13@rev-1 TOOL-dDeclaredLoop-14@rev-1 TOOL-dDeclaredLoop-15@rev-1 TOOL-dDeclaredLoop-16@rev-1 TOOL-dDeclaredLoop-17@rev-1 TOOL-dDeclaredLoop-18@rev-1
TOOL-dDeclaredLoop-19@rev-1 TOOL-dDeclaredLoop-2@rev-1 TOOL-dDeclaredLoop-20@rev-1 TOOL-dDeclaredLoop-21@rev-1 TOOL-dDeclaredLoop-22@rev-1 TOOL-dDeclaredLoop-23@rev-1 TOOL-dDeclaredLoop-24@rev-1 TOOL-dDeclaredLoop-25@rev-1 TOOL-dDeclaredLoop-26@rev-1 TOOL-dDeclaredLoop-27@rev-1
TOOL-dDeclaredLoop-28@rev-1 TOOL-dDeclaredLoop-29@rev-1 TOOL-dDeclaredLoop-3@rev-1 TOOL-dDeclaredLoop-30@rev-1 TOOL-dDeclaredLoop-31@rev-1 TOOL-dDeclaredLoop-32@rev-1 TOOL-dDeclaredLoop-33@rev-1 TOOL-dDeclaredLoop-34@rev-1 TOOL-dDeclaredLoop-36@rev-1 TOOL-dDeclaredLoop-37@rev-1
TOOL-dDeclaredLoop-38@rev-1 TOOL-dDeclaredLoop-4@rev-1 TOOL-dDeclaredLoop-40@rev-1 TOOL-dDeclaredLoop-41@rev-1 TOOL-dDeclaredLoop-42@rev-1 TOOL-dDeclaredLoop-43@rev-1 TOOL-dDeclaredLoop-44@rev-1 TOOL-dDeclaredLoop-45@rev-1 TOOL-dDeclaredLoop-46@rev-1 TOOL-dDeclaredLoop-47@rev-1
TOOL-dDeclaredLoop-48@rev-1 TOOL-dDeclaredLoop-49@rev-1 TOOL-dDeclaredLoop-5@rev-1 TOOL-dDeclaredLoop-50@rev-1 TOOL-dDeclaredLoop-51@rev-1 TOOL-dDeclaredLoop-52@rev-1 TOOL-dDeclaredLoop-53@rev-1 TOOL-dDeclaredLoop-54@rev-1 TOOL-dDeclaredLoop-55@rev-1 TOOL-dDeclaredLoop-56@rev-1
TOOL-dDeclaredLoop-57@rev-1 TOOL-dDeclaredLoop-59@rev-1 TOOL-dDeclaredLoop-6@rev-1 TOOL-dDeclaredLoop-60@rev-1 TOOL-dDeclaredLoop-61@rev-1 TOOL-dDeclaredLoop-62@rev-1 TOOL-dDeclaredLoop-63@rev-1 TOOL-dDeclaredLoop-64@rev-1 TOOL-dDeclaredLoop-65@rev-1 TOOL-dDeclaredLoop-66@rev-1
TOOL-dDeclaredLoop-67@rev-1 TOOL-dDeclaredLoop-68@rev-1 TOOL-dDeclaredLoop-69@rev-1 TOOL-dDeclaredLoop-7@rev-1 TOOL-dDeclaredLoop-70@rev-1 TOOL-dDeclaredLoop-71@rev-1 TOOL-dDeclaredLoop-72@rev-1 TOOL-dDeclaredLoop-73@rev-1 TOOL-dDeclaredLoop-74@rev-1 TOOL-dDeclaredLoop-75@rev-1
TOOL-dDeclaredLoop-76@rev-1 TOOL-dDeclaredLoop-77@rev-1 TOOL-dDeclaredLoop-78@rev-1 TOOL-dDeclaredLoop-79@rev-1 TOOL-dDeclaredLoop-8@rev-1 TOOL-dDeclaredLoop-80@rev-1 TOOL-dDeclaredLoop-81@rev-1 TOOL-dDeclaredLoop-82@rev-1 TOOL-dDeclaredLoop-83@rev-1 TOOL-dDeclaredLoop-84@rev-1
TOOL-dDeclaredLoop-85@rev-1 TOOL-dDeclaredLoop-86@rev-1 TOOL-dDeclaredLoop-87@rev-1 TOOL-dDeclaredLoop-88@rev-1 TOOL-dDeclaredLoop-89@rev-1 TOOL-dDeclaredLoop-90@rev-1 TOOL-dDeclaredLoop-91@rev-1 TOOL-dDeclaredLoop-92@rev-1 TOOL-dDeclaredLoop-93@rev-1 TOOL-dDeclaredLoop-94@rev-1
TOOL-dDeclaredLoop-95@rev-1 TOOL-dDeclaredLoop-96@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dDeclaredLoop's 34 clause(s) and 49 owned node(s), over 99 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 34
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-49.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-53.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-55.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-57.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-59.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-61.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-63.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-64.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-65.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-66.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-67.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-68.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-69.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-70.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-71.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-72.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-73.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-74.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-76.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-80.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-83.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-84.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-85.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-86.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-87.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-88.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-91.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-93.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-94.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-95.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-96.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-97.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-TOOL-dDeclaredLoop-98.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-TOOL-dDeclaredLoop-99.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0086, cl-dClosedLoop-0089, cl-dClosedLoop-0090, cl-dClosedLoop-0091, cl-dClosedLoop-0092, cl-dClosedLoop-0093, cl-dClosedLoop-0094, cl-dClosedLoop-0095, cl-dClosedLoop-0096, cl-dClosedLoop-0097, cl-dClosedLoop-0098, cl-dClosedLoop-0101,
  cl-dClosedLoop-0102, cl-dClosedLoop-0111
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dDeclaredLoop-18` | no |
| 2 | `TOOL-dDeclaredLoop-1` | no |
| 3 | `TOOL-dDeclaredLoop-23`, `TOOL-dDeclaredLoop-36` | yes |
| 4 | `TOOL-dDeclaredLoop-16`, `TOOL-dDeclaredLoop-37`, `TOOL-dDeclaredLoop-38`, `TOOL-dDeclaredLoop-39`, `TOOL-dDeclaredLoop-40`, `TOOL-dDeclaredLoop-57` | no |
| 5 | `TOOL-dDeclaredLoop-5`, `TOOL-dDeclaredLoop-58`, `TOOL-dDeclaredLoop-73` | yes |
| 6 | `TOOL-dDeclaredLoop-12`, `TOOL-dDeclaredLoop-41` | no |
| 7 | `TOOL-dDeclaredLoop-9` | no |
| 8 | `TOOL-dDeclaredLoop-17` | no |
| 9 | `TOOL-dDeclaredLoop-11`, `TOOL-dDeclaredLoop-42` | yes |
| 10 | `TOOL-dDeclaredLoop-13` | no |
| 11 | `TOOL-dDeclaredLoop-24` | no |
| 12 | `TOOL-dDeclaredLoop-15` | no |
| 13 | `TOOL-dDeclaredLoop-3` | no |
| 14 | `TOOL-dDeclaredLoop-10` | no |
| 15 | `TOOL-dDeclaredLoop-2` | no |
| 16 | `TOOL-dDeclaredLoop-43`, `TOOL-dDeclaredLoop-44`, `TOOL-dDeclaredLoop-8` | yes |
| 17 | `TOOL-dDeclaredLoop-59`, `TOOL-dDeclaredLoop-7` | yes |
| 18 | `TOOL-dDeclaredLoop-14`, `TOOL-dDeclaredLoop-45`, `TOOL-dDeclaredLoop-69` | no |
| 19 | `TOOL-dDeclaredLoop-4`, `TOOL-dDeclaredLoop-78` | yes |
| 20 | `TOOL-dDeclaredLoop-46`, `TOOL-dDeclaredLoop-6`, `TOOL-dDeclaredLoop-81` | no |
| 21 | `TOOL-dDeclaredLoop-25`, `TOOL-dDeclaredLoop-47`, `TOOL-dDeclaredLoop-83`, `TOOL-dDeclaredLoop-84`, `TOOL-dDeclaredLoop-85` | yes |
| 22 | `TOOL-dDeclaredLoop-29` | no |
| 23 | `TOOL-dDeclaredLoop-26` | no |
| 24 | `TOOL-dDeclaredLoop-27` | no |
| 25 | `TOOL-dDeclaredLoop-28` | no |
| 26 | `TOOL-dDeclaredLoop-21` | no |
| 27 | `TOOL-dDeclaredLoop-34` | no |
| 28 | `TOOL-dDeclaredLoop-30` | no |
| 29 | `TOOL-dDeclaredLoop-32`, `TOOL-dDeclaredLoop-48`, `TOOL-dDeclaredLoop-49` | no |
| 30 | `TOOL-dDeclaredLoop-31`, `TOOL-dDeclaredLoop-60`, `TOOL-dDeclaredLoop-61`, `TOOL-dDeclaredLoop-62` | no |
| 31 | `TOOL-dDeclaredLoop-20` | no |
| 32 | `TOOL-dDeclaredLoop-22`, `TOOL-dDeclaredLoop-50` | no |
| 33 | `TOOL-dDeclaredLoop-19`, `TOOL-dDeclaredLoop-51` | yes |
| 34 | `TOOL-dDeclaredLoop-33`, `TOOL-dDeclaredLoop-52`, `TOOL-dDeclaredLoop-53` | no |
| 35 | `TOOL-dDeclaredLoop-54`, `TOOL-dDeclaredLoop-55`, `TOOL-dDeclaredLoop-63`, `TOOL-dDeclaredLoop-64` | no |
| 36 | `TOOL-dDeclaredLoop-56`, `TOOL-dDeclaredLoop-70`, `TOOL-dDeclaredLoop-71`, `TOOL-dDeclaredLoop-72` | no |
| 37 | `TOOL-dDeclaredLoop-65`, `TOOL-dDeclaredLoop-68`, `TOOL-dDeclaredLoop-76` | yes |
| 38 | `TOOL-dDeclaredLoop-66`, `TOOL-dDeclaredLoop-67`, `TOOL-dDeclaredLoop-74`, `TOOL-dDeclaredLoop-80` | no |
| 39 | `TOOL-dDeclaredLoop-75`, `TOOL-dDeclaredLoop-77` | no |
| 40 | `TOOL-dDeclaredLoop-79` | no |
| 41 | `TOOL-dDeclaredLoop-82` | no |
| 42 | `TOOL-dDeclaredLoop-86` | no |
| 43 | `TOOL-dDeclaredLoop-87` | no |
| 44 | `TOOL-dDeclaredLoop-88`, `TOOL-dDeclaredLoop-89` | no |
| 45 | `TOOL-dDeclaredLoop-90`, `TOOL-dDeclaredLoop-91` | no |
| 46 | `TOOL-dDeclaredLoop-92` | no |
| 47 | `TOOL-dDeclaredLoop-93` | no |
| 48 | `TOOL-dDeclaredLoop-94` | no |
| 49 | `TOOL-dDeclaredLoop-95` | no |
| 50 | `TOOL-dDeclaredLoop-96`, `TOOL-dDeclaredLoop-97`, `TOOL-dDeclaredLoop-98`, `TOOL-dDeclaredLoop-99` | no |
| 51 | `TOOL-dDeclaredLoop-100` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dOrderedCharter](../dOrderedCharter/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dKeptSession](../dKeptSession/README.md), [dPlacedRequest](../dPlacedRequest/README.md), [dRankedPlan](../dRankedPlan/README.md), [dTotalRecall](../dTotalRecall/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
<!-- /gen:build-edges -->

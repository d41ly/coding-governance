---
slug: dIndexedDesign
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-21 TOOL-dIndexedDesign-22 TOOL-dIndexedDesign-23 TOOL-dIndexedDesign-24 TOOL-dIndexedDesign-25 TOOL-dIndexedDesign-26 TOOL-dIndexedDesign-27 TOOL-dIndexedDesign-28 TOOL-dIndexedDesign-29 TOOL-dIndexedDesign-30 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53
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
**Build status:** DEFERRED · 40 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13
ids TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-17 TOOL-dIndexedDesign-18 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-21 TOOL-dIndexedDesign-22 TOOL-dIndexedDesign-23 TOOL-dIndexedDesign-24 TOOL-dIndexedDesign-25
ids TOOL-dIndexedDesign-26 TOOL-dIndexedDesign-27 TOOL-dIndexedDesign-28 TOOL-dIndexedDesign-29 TOOL-dIndexedDesign-30 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37
ids TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49
ids TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dIndexedDesign-9 — spec sections named by tag across tiers: one heading rule, one reader and its twins, and the tagged canon behind a cutoff](spec/2026-10-28-spec-TOOL-dIndexedDesign-9.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-12 — the structured spec's typed edges: `implements=` and `decides=` read through one spec-site adapter, and `design.seams` reading a tag's bundle](spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-16 — design coverage by policy: the carries join read at each Design exit and each spec revision, `UNCARRIED`, and the coverage lens](spec/2026-10-28-spec-TOOL-dIndexedDesign-16.md) | 3 | 2 | DEFERRED | rev-4 | 2026-10-28 |
| [TOOL-dIndexedDesign-1 — the Design-to-Build hand-off as `design.handoff` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-1.md) | 4 | 2 | DEFERRED | rev-4 | 2026-10-28 |
| [TOOL-dIndexedDesign-35 — the coverage lens runs as its own one-agent stage, so `SPEC_LENSES` stays at the agent-cap hook's five-lens bound and no checklist share reaches a lens that does not run](spec/2026-10-28-spec-TOOL-dIndexedDesign-35.md) | 4 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-36 — BUILD-METHOD M6 names the refusals `--dispatch` gained, and stops saying it refuses "on nothing else"](spec/2026-10-28-spec-TOOL-dIndexedDesign-36.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-39 — unit 35's coverage stage lands inside unit 16's pass, so no commit of the build holds a six-entry `SPEC_LENSES`](spec/2026-10-28-spec-TOOL-dIndexedDesign-39.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-44 — the coverage stage is a finder in every count, dead label, finding join and durable file the Find stage keeps](spec/2026-10-28-spec-TOOL-dIndexedDesign-44.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-7 — the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract](spec/2026-10-28-spec-TOOL-dIndexedDesign-7.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-2 — the design index: overlaps between live designs, as `design.overlap` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-2.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-45 — the unattended protocol stops saying `--dispatch` refuses only MISSING and THIN, with no byte added under its size row](spec/2026-10-28-spec-TOOL-dIndexedDesign-45.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-50 — unit 44's finder bookkeeping lands in unit 16's pass commit, so a `coverage: 'only'` run writes its record from unit 35's pass on](spec/2026-10-28-spec-TOOL-dIndexedDesign-50.md) | 6 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-6 — agreement and tier checks: the interface and scope axes, the tier rule as a predicate, and sibling specs read from unmerged refs](spec/2026-10-28-spec-TOOL-dIndexedDesign-6.md) | 7 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-8 — the feature level: `design.decompose`'s feature designs, roster and fork records, forks resolved as `design.forks` says](spec/2026-10-28-spec-TOOL-dIndexedDesign-8.md) | 8 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-13 — the reuse scout's return under M1c's contract: the `seams` record, its caps and MUST definition, read once and its seams handed on as rows](spec/2026-10-28-spec-TOOL-dIndexedDesign-13.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-20 — two-level re-entry: `design.input`'s pin, `design.reentry`'s additive-versus-breaking diff record, and the re-design inventory](spec/2026-10-28-spec-TOOL-dIndexedDesign-20.md) | 9 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-32 — the feature level's Serves kinds bind: `fork` a typed kind, `feature-design` an untyped one, and `roster` a region that binds nothing](spec/2026-10-28-spec-TOOL-dIndexedDesign-32.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-33 — the scout record's `seams` kind binds as an untyped kind, so its reader, check 31 and unit 4's outcome join read a real population](spec/2026-10-28-spec-TOOL-dIndexedDesign-33.md) | 10 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-34 — re-entry's `diff` and `inventory` kinds bind as typed kinds, and the diff record has one writer of the typed name](spec/2026-10-28-spec-TOOL-dIndexedDesign-34.md) | 10 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-42 — fork records are numbered within their build and joined by their `Fork` field, so two units' F1 forks never collide under the factory's per-build key](spec/2026-10-28-spec-TOOL-dIndexedDesign-42.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-5 — the research harness: one experiment factory on dBoundRoles' `experiment` shape, the reuse bench its first entry](spec/2026-10-28-spec-TOOL-dIndexedDesign-5.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-31 — the blinded scout's input as a true allow-list: `derive_scouted_seam_input` names the keys a scout may see, and a planted unknown key is withheld](spec/2026-10-28-spec-TOOL-dIndexedDesign-31.md) | 11 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-4 — reuse and alternatives backed by recorded probes: the §10 outcome joined to its scout record, each rejected candidate to its test](spec/2026-10-28-spec-TOOL-dIndexedDesign-4.md) | 11 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-43 — the typed record factory admits a field its kind declares repeatable, so an inventory with one `Of` and one `Verdict` line per row binds](spec/2026-10-28-spec-TOOL-dIndexedDesign-43.md) | 11 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-14 — the scout's bug classes by intent: at most five from the catalogue's index, armed only by a replay that beats the anchor ranking's top five](spec/2026-10-28-spec-TOOL-dIndexedDesign-14.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-10 — the playbook record kind: its row, its one resolver, the `repeat` route resolving through it, and `check-playbook` as Design's pack](spec/2026-10-28-spec-TOOL-dIndexedDesign-10.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-11 — the playbook set record as a kind, its identity derived once, and a set check that reds at the bar, registered at Test's leg-pack point](spec/2026-10-28-spec-TOOL-dIndexedDesign-11.md) | 14 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-15 — the planner's `design.streams` item: the planning workflow, its run decision under `design.streams-when`, and the stream plan checked against order, write sets and the overlap record](spec/2026-10-28-spec-TOOL-dIndexedDesign-15.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-3 — design review by policy: `review.design` read at the guarded revision, its effort, and the opt-in guard](spec/2026-10-28-spec-TOOL-dIndexedDesign-3.md) | 16 | 2 | DEFERRED | rev-4 | 2026-10-28 |
| [TOOL-dIndexedDesign-37 — one write-set path predicate, `check_meet_path`, that keeps root files, so the stream plan and the build order refuse two writers of one root file](spec/2026-10-28-spec-TOOL-dIndexedDesign-37.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-38 — the round-1 spec audit's 42 minors batched: shared budgets priced, one resolver and one path rule, readers that refuse what they cannot read, and every unbuildable criterion restated](spec/2026-10-28-spec-TOOL-dIndexedDesign-38.md) | 17 | 2 | DEFERRED | rev-3 | 2026-10-28 |
| [TOOL-dIndexedDesign-40 — the three new cutoff keys ship blank in the passes that add them, so `cutoff_keys_armed` holds its pin of 36 at every pass tip](spec/2026-10-28-spec-TOOL-dIndexedDesign-40.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-41 — the design-exit refusals add no net `fail` site, so `unattended.sh` stays within its refusal ceiling at every pass tip](spec/2026-10-28-spec-TOOL-dIndexedDesign-41.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-46 — the round-1 audit of units 31 to 38: its 27 minors batched, one writer and one allocator per typed name, one predicate per question, and every vacuous criterion made to observe](spec/2026-10-28-spec-TOOL-dIndexedDesign-46.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-28 |
| [TOOL-dIndexedDesign-47 — unit 41 AC2's armed half becomes a staged break: with the THIN arm deleted in a scratch clone, the composed THIN site reads UNARMED](spec/2026-10-28-spec-TOOL-dIndexedDesign-47.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-48 — the composed THIN site opens with a literal run no other `fail` message or arm line carries, and the THIN arm is re-pinned to it](spec/2026-10-28-spec-TOOL-dIndexedDesign-48.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-49 — every cause composed into the `--dispatch` refusal is armed by its own clause text, and the cause list is derived from the code](spec/2026-10-28-spec-TOOL-dIndexedDesign-49.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-51 — unit 38's one-site rule is restated at S22 and S35 before unit 38's pass, and the refusal census is read at every pass commit that changes `unattended.sh`](spec/2026-10-28-spec-TOOL-dIndexedDesign-51.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-52 — the standalone `--design-exit` opt-in reader refuses a present undated value and a conf it cannot evaluate, as the driver does](spec/2026-10-28-spec-TOOL-dIndexedDesign-52.md) | 20 | 2 | DEFERRED | rev-1 | 2026-10-28 |
| [TOOL-dIndexedDesign-53 — the round-1 audit of units 39 to 46: its 20 minors batched, one home for each record number, one reader per opt-in, and every criterion made to observe](spec/2026-10-28-spec-TOOL-dIndexedDesign-53.md) | 21 | 2 | DEFERRED | rev-1 | 2026-10-28 |
<!-- /gen:build-units -->

Records: 73 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53.

Ids whose spec moved past its audited revision: TOOL-dIndexedDesign-1@rev-1 TOOL-dIndexedDesign-10@rev-1 TOOL-dIndexedDesign-12@rev-1 TOOL-dIndexedDesign-13@rev-1 TOOL-dIndexedDesign-14@rev-1 TOOL-dIndexedDesign-15@rev-1 TOOL-dIndexedDesign-16@rev-1 TOOL-dIndexedDesign-2@rev-1
TOOL-dIndexedDesign-20@rev-1 TOOL-dIndexedDesign-3@rev-1 TOOL-dIndexedDesign-31@rev-1 TOOL-dIndexedDesign-32@rev-1 TOOL-dIndexedDesign-34@rev-1 TOOL-dIndexedDesign-35@rev-1 TOOL-dIndexedDesign-36@rev-1 TOOL-dIndexedDesign-37@rev-1 TOOL-dIndexedDesign-38@rev-1 TOOL-dIndexedDesign-39@rev-1
TOOL-dIndexedDesign-4@rev-1 TOOL-dIndexedDesign-41@rev-1 TOOL-dIndexedDesign-42@rev-1 TOOL-dIndexedDesign-43@rev-1 TOOL-dIndexedDesign-44@rev-1 TOOL-dIndexedDesign-45@rev-1 TOOL-dIndexedDesign-46@rev-1 TOOL-dIndexedDesign-5@rev-1 TOOL-dIndexedDesign-6@rev-1 TOOL-dIndexedDesign-7@rev-1
TOOL-dIndexedDesign-8@rev-1 TOOL-dIndexedDesign-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dIndexedDesign's 16 clause(s) and 28 owned node(s), over 40 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 15
- carried in parts: 1 (cl-dClosedLoop-0390)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-28-spec-TOOL-dIndexedDesign-31.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-32.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-33.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-28-spec-TOOL-dIndexedDesign-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-35.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-28-spec-TOOL-dIndexedDesign-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-28-spec-TOOL-dIndexedDesign-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-28-spec-TOOL-dIndexedDesign-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-49.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-28-spec-TOOL-dIndexedDesign-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-28-spec-TOOL-dIndexedDesign-53.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0385, cl-dClosedLoop-0386, cl-dClosedLoop-0388, cl-dClosedLoop-0389, cl-dClosedLoop-0391, cl-dClosedLoop-0393, cl-dClosedLoop-0395, cl-dClosedLoop-0396
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dIndexedDesign-9` | no |
| 2 | `TOOL-dIndexedDesign-12` | no |
| 3 | `TOOL-dIndexedDesign-16` | no |
| 4 | `TOOL-dIndexedDesign-1`, `TOOL-dIndexedDesign-35` | yes |
| 5 | `TOOL-dIndexedDesign-36`, `TOOL-dIndexedDesign-39`, `TOOL-dIndexedDesign-44`, `TOOL-dIndexedDesign-7` | no |
| 6 | `TOOL-dIndexedDesign-2`, `TOOL-dIndexedDesign-45`, `TOOL-dIndexedDesign-50` | yes |
| 7 | `TOOL-dIndexedDesign-6` | no |
| 8 | `TOOL-dIndexedDesign-8` | no |
| 9 | `TOOL-dIndexedDesign-13`, `TOOL-dIndexedDesign-20`, `TOOL-dIndexedDesign-32` | no |
| 10 | `TOOL-dIndexedDesign-33`, `TOOL-dIndexedDesign-34`, `TOOL-dIndexedDesign-42`, `TOOL-dIndexedDesign-5` | no |
| 11 | `TOOL-dIndexedDesign-31`, `TOOL-dIndexedDesign-4`, `TOOL-dIndexedDesign-43` | yes |
| 12 | `TOOL-dIndexedDesign-14` | no |
| 13 | `TOOL-dIndexedDesign-10` | no |
| 14 | `TOOL-dIndexedDesign-11` | no |
| 15 | `TOOL-dIndexedDesign-15` | no |
| 16 | `TOOL-dIndexedDesign-3`, `TOOL-dIndexedDesign-37` | yes |
| 17 | `TOOL-dIndexedDesign-38` | no |
| 18 | `TOOL-dIndexedDesign-40`, `TOOL-dIndexedDesign-41` | no |
| 19 | `TOOL-dIndexedDesign-46`, `TOOL-dIndexedDesign-47`, `TOOL-dIndexedDesign-48`, `TOOL-dIndexedDesign-49`, `TOOL-dIndexedDesign-51` | no |
| 20 | `TOOL-dIndexedDesign-52` | no |
| 21 | `TOOL-dIndexedDesign-53` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md), [dKeptSession](../dKeptSession/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dScopedBuild](../dScopedBuild/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

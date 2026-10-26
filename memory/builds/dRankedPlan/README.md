---
slug: dRankedPlan
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-17 TOOL-dRankedPlan-18
spec-audit: 2026-10-21
parents: dDeclaredLoop dTotalRecall dBoundRoles
may: PLAY-dClosedLoop-3
---

# dRankedPlan — the Plan build of the dClosedLoop chain

## The problem this build exists to solve

dRankedPlan owns 10 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-plan-01,
gap-plan-02, gap-plan-03, gap-plan-04, gap-plan-05, gap-plan-06, gap-plan-07, gap-flow-03, gap-flow-04, gap-plan-08.
Closing every one is this build's goal bound.

## Expected improvements

- Each of the 16 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 10 owned gaps above close.

## Detriments if this is not built

- Its 10 owned gaps stay open.
- Its 1 child build waits on it: dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dRankedPlan` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dRankedPlan`, a record per member "recorded by nobody", the same with `--write` (commit it
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
| 1 | `TOOL-dRankedPlan-1` | `cl-dClosedLoop-0369@9f2afd12` | priority beside `parents:` and the generated plan view |
| 2 | `TOOL-dRankedPlan-2` | `cl-dClosedLoop-0370@23b0ac8f` | the planner and triager role and Plan workflow |
| 3 | `TOOL-dRankedPlan-3` | `cl-dClosedLoop-0371@3ec4f25f` | triage as `plan.triage` says: by `plan.triage-rule`'s declared rules |
| 4 | `TOOL-dRankedPlan-4` | `cl-dClosedLoop-0372@5c733981` | dormancy disposal |
| 5 | `TOOL-dRankedPlan-5` | `cl-dClosedLoop-0373@70fb5631` | the live-build mapping carried out |
| 6 | `TOOL-dRankedPlan-6` | `cl-dClosedLoop-0374@c6143eda` | Plan Review |
| 7 | `TOOL-dRankedPlan-7` | `cl-dClosedLoop-0375@33084fbd` | kickoff using the plan as `plan.kickoff` says: offering the plan's next item under `offer-next` |
| 8 | `TOOL-dRankedPlan-8` | `cl-dClosedLoop-0376@f1c33063` | the full kickoff only where `kickoff.runs` says |
| 9 | `TOOL-dRankedPlan-9` | `cl-dClosedLoop-0377@fd363a7f` | the session's intake log |
| 10 | `TOOL-dRankedPlan-10` | `cl-dClosedLoop-0378@ed811c10` | until the intake kind lands and the harness's adapter declares the prompt-submit event in its capability table |
| 11 | `TOOL-dRankedPlan-11` | `cl-dClosedLoop-0379@f1807fe1` | each role item's memory read set sized at Plan |
| 12 | `TOOL-dRankedPlan-12` | `cl-dClosedLoop-0380@1e2f59a7` | `plan.record` declaring the probes owed before Design (night pass |
| 13 | `TOOL-dRankedPlan-13` | `cl-dClosedLoop-0381@634c7b47` | the plan record's intent fields: the affected systems derived from the `code` record and checked |
| 14 | `TOOL-dRankedPlan-14` | `cl-dClosedLoop-0382@182ba9ba` | the plan record's scenario field |
| 15 | `TOOL-dRankedPlan-15` | `cl-dClosedLoop-0497@2b8de50e` | the plan revision record: a fork the goal cannot survive moving the build from designing back to planning |
| 16 | `TOOL-dRankedPlan-16` | `cl-dClosedLoop-0498@e9d43f26` | the artifact levels declared as the owner confirmed them in the flow round: the card at the session's level above the plan |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 16 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15
ids TOOL-dRankedPlan-16 TOOL-dRankedPlan-17 TOOL-dRankedPlan-18

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRankedPlan-16 — the artifact levels: one plan record per build, and a brief that renders it and never types it](spec/2026-10-26-spec-TOOL-dRankedPlan-16.md) | 1 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-1 — `priority:` beside `parents:`, and the generated plan view `PLAN.md`](spec/2026-10-26-spec-TOOL-dRankedPlan-1.md) | 2 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-9 — the ratification predicate: the session's owner-origin intake read as the plan's ratification by `plan.ratification`](spec/2026-10-26-spec-TOOL-dRankedPlan-9.md) | 3 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-10 — `plan.exit` falls back to the owner gate while the intake is not installed for the harness](spec/2026-10-26-spec-TOOL-dRankedPlan-10.md) | 4 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-2 — the planner and triager role, the Plan workflow, and the plan's order as `plan.authority` says](spec/2026-10-26-spec-TOOL-dRankedPlan-2.md) | 5 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-14 — the plan record's scenario field, set from the placement and re-picked at Plan with its reason](spec/2026-10-26-spec-TOOL-dRankedPlan-14.md) | 6 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-13 — the plan record's intent fields: affected systems derived from the `code` record and checked, open questions as fork tags](spec/2026-10-26-spec-TOOL-dRankedPlan-13.md) | 7 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-11 — each role item's memory read set sized at Plan, as `id#tag` keys](spec/2026-10-26-spec-TOOL-dRankedPlan-11.md) | 8 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-12 — `plan.record` declaring the probes owed before Design](spec/2026-10-26-spec-TOOL-dRankedPlan-12.md) | 9 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-3 — triage as `plan.triage` says: declared rules, the planner judging the rest](spec/2026-10-26-spec-TOOL-dRankedPlan-3.md) | 10 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-4 — dormancy disposal: a dormant build moved by the owner's disposition, shown in the plan view](spec/2026-10-26-spec-TOOL-dRankedPlan-4.md) | 11 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-5 — the live-build mapping carried out: each live build kept or absorbed, recorded per build](spec/2026-10-26-spec-TOOL-dRankedPlan-5.md) | 12 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-15 — the plan revision record: a fork the goal cannot survive moves the build back to planning, and Design re-enters on the ratified revision](spec/2026-10-26-spec-TOOL-dRankedPlan-15.md) | 13 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-6 — Plan Review: the plan record a review subject, run with the lenses of the preset `review.pin` passes until dCalibratedLens's Plan lenses land](spec/2026-10-26-spec-TOOL-dRankedPlan-6.md) | 14 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-8 — the full kickoff only where `kickoff.runs` says: a `kickoff —` line beside the card](spec/2026-10-26-spec-TOOL-dRankedPlan-8.md) | 15 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dRankedPlan-7 — kickoff reads the plan as `plan.kickoff` says, and the attended brief is gated](spec/2026-10-26-spec-TOOL-dRankedPlan-7.md) | 16 | 2 | OPEN | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 15 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRankedPlan-1 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6
TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9.

Ids whose spec moved past its audited revision: none — 0 of 16 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dRankedPlan's 16 clause(s) and 18 owned node(s), over 16 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 16
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0372, cl-dClosedLoop-0382, cl-dClosedLoop-0497, cl-dClosedLoop-0498
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRankedPlan-16` | no |
| 2 | `TOOL-dRankedPlan-1` | no |
| 3 | `TOOL-dRankedPlan-9` | no |
| 4 | `TOOL-dRankedPlan-10` | no |
| 5 | `TOOL-dRankedPlan-2` | no |
| 6 | `TOOL-dRankedPlan-14` | no |
| 7 | `TOOL-dRankedPlan-13` | no |
| 8 | `TOOL-dRankedPlan-11` | no |
| 9 | `TOOL-dRankedPlan-12` | no |
| 10 | `TOOL-dRankedPlan-3` | no |
| 11 | `TOOL-dRankedPlan-4` | no |
| 12 | `TOOL-dRankedPlan-5` | no |
| 13 | `TOOL-dRankedPlan-15` | no |
| 14 | `TOOL-dRankedPlan-6` | no |
| 15 | `TOOL-dRankedPlan-8` | no |
| 16 | `TOOL-dRankedPlan-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

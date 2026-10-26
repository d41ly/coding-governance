---
slug: dRankedPlan
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-17
status: OPEN
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
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15
ids TOOL-dRankedPlan-16 TOOL-dRankedPlan-17

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 5 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dRankedPlan's 16 clause(s) and 18 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 16 (cl-dClosedLoop-0369, cl-dClosedLoop-0370, cl-dClosedLoop-0371, cl-dClosedLoop-0372, cl-dClosedLoop-0373, cl-dClosedLoop-0374, cl-dClosedLoop-0375, cl-dClosedLoop-0376, cl-dClosedLoop-0377, cl-dClosedLoop-0378, cl-dClosedLoop-0379, cl-dClosedLoop-0380, cl-dClosedLoop-0381,
  cl-dClosedLoop-0382, cl-dClosedLoop-0497, cl-dClosedLoop-0498)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.plan.dedupe, item.plan.exit, item.plan.input, item.plan.lease, item.plan.place, item.plan.record, item.plan.research, item.plan.triage-judge, item.plan.triage-rule, policy-key.kickoff.runs, policy-key.plan.authority, policy-key.plan.kickoff,
  policy-key.plan.ratification, policy-key.plan.triage, policy-key.plan.unplaced, record-kind.dupes, record-kind.plan, record-kind.triage
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0372, cl-dClosedLoop-0373, cl-dClosedLoop-0382, cl-dClosedLoop-0497, cl-dClosedLoop-0498
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->

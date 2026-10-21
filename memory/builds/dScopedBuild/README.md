---
slug: dScopedBuild
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-16
status: OPEN
spec-audit: 2026-10-21
parents: dIndexedDesign dWitnessedBar dWellOiledMachine dFurnishedOrders
may: PLAY-dClosedLoop-3
---

# dScopedBuild — the Build build of the dClosedLoop chain

## The problem this build exists to solve

dScopedBuild owns 10 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-spine-03,
gap-build-01, gap-build-02, gap-build-03, gap-build-04, gap-flow-05, gap-build-05, gap-build-06, gap-flow-22,
gap-mem-23. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 15 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 10 owned gaps above close.

## Detriments if this is not built

- Its 10 owned gaps stay open.
- Its 1 child build waits on it: dConvergedCharter.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dScopedBuild` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dScopedBuild`, a record per member "recorded by nobody", the same with `--write` (commit it
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
| 1 | `TOOL-dScopedBuild-1` | `cl-dClosedLoop-0399@182b9f2d` | one exit contract with a history-derived base |
| 2 | `TOOL-dScopedBuild-2` | `cl-dClosedLoop-0400@d5dcbafa` | built specs frozen |
| 3 | `TOOL-dScopedBuild-3` | `cl-dClosedLoop-0401@e53987d9` | scope at the push |
| 4 | `TOOL-dScopedBuild-4` | `cl-dClosedLoop-0402@19e9688b` | the closing review recorded |
| 5 | `TOOL-dScopedBuild-5` | `cl-dClosedLoop-0403@3c89f2a1` | a write gate reading derived state |
| 6 | `TOOL-dScopedBuild-6` | `cl-dClosedLoop-0404@f111410c` | the per-pass checklist's retirement witnessed at Build |
| 7 | `TOOL-dScopedBuild-7` | `cl-dClosedLoop-0405@431edacd` | the core checks run by the executor at Build's exit |
| 8 | `TOOL-dScopedBuild-8` | `cl-dClosedLoop-0406@c1850071` | `build.unit-pass` and `build.scope` draining the legacy a unit touches as `retrofit.drain` says |
| 9 | `TOOL-dScopedBuild-9` | `cl-dClosedLoop-0407@b6ab4b28` | the touch join as `build.scope`'s one check |
| 10 | `TOOL-dScopedBuild-10` | `cl-dClosedLoop-0408@e14d93bc` | a red-first reproduction |
| 11 | `TOOL-dScopedBuild-11` | `cl-dClosedLoop-0409@5b78cbe2` | a playbook's pieces built as units with piece records joined by hash |
| 12 | `TOOL-dScopedBuild-12` | `cl-dClosedLoop-0410@dce90a3a` | `build.reuse-check` |
| 13 | `TOOL-dScopedBuild-13` | `cl-dClosedLoop-0411@78cc90dd` | the closing review handed |
| 14 | `TOOL-dScopedBuild-14` | `cl-dClosedLoop-0412@021fa28b` | the deviation gate under `deviation.gate`: dTrueNorth's joins read at the commit and at the Build exit beside `build.scope` |
| 15 | `TOOL-dScopedBuild-15` | `cl-dClosedLoop-0506@2200c4c7` | `build.acceptance` writing the seen-red record: the executor re-running each new or changed gate's planted red beside the unit's acceptance commands |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14
ids TOOL-dScopedBuild-15 TOOL-dScopedBuild-16

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dScopedBuild's 15 clause(s) and 23 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 15 (cl-dClosedLoop-0399, cl-dClosedLoop-0400, cl-dClosedLoop-0401, cl-dClosedLoop-0402, cl-dClosedLoop-0403, cl-dClosedLoop-0404, cl-dClosedLoop-0405, cl-dClosedLoop-0406, cl-dClosedLoop-0407, cl-dClosedLoop-0408, cl-dClosedLoop-0409, cl-dClosedLoop-0410, cl-dClosedLoop-0411,
  cl-dClosedLoop-0412, cl-dClosedLoop-0506)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.build.acceptance, item.build.base, item.build.core, item.build.distill, item.build.exit, item.build.fix-pass, item.build.ratify, item.build.resolve, item.build.reuse-check, item.build.revert-pass, item.build.scope, item.build.unit-lease, item.build.unit-pass,
  policy-key.build.reuse-check.second-pass, policy-key.build.scope, policy-key.deviation.gate, policy-key.retrofit.claim-cap, policy-key.retrofit.claim-on-touch, policy-key.retrofit.drain, policy-key.retrofit.drain-cap, policy-key.review.build.when, record-kind.core-result, record-kind.scope
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0399, cl-dClosedLoop-0401, cl-dClosedLoop-0403, cl-dClosedLoop-0404, cl-dClosedLoop-0405, cl-dClosedLoop-0409, cl-dClosedLoop-0411
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFurnishedOrders](../dFurnishedOrders/README.md), [dIndexedDesign](../dIndexedDesign/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->

---
slug: dCalibratedLens
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18
status: OPEN
spec-audit: 2026-10-21
parents: dTendedCadence dFairHearing
may: PLAY-dClosedLoop-3
---

# dCalibratedLens — the Review build of the dClosedLoop chain

## The problem this build exists to solve

dCalibratedLens owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-review-01,
gap-review-02, gap-review-03, gap-maint-03, gap-design-08, gap-found-16, gap-review-11, gap-review-14, gap-review-15,
gap-review-16, gap-review-17, gap-review-18, gap-review-19. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 17 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 1 child build waits on it: dConvergedCharter.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dCalibratedLens` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dCalibratedLens`, a record per member "recorded by nobody", the same with `--write` (commit
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
| 1 | `TOOL-dCalibratedLens-1` | `cl-dClosedLoop-0458@5429e502` | each stage review's lenses and effort: lenses for Plan |
| 2 | `TOOL-dCalibratedLens-2` | `cl-dClosedLoop-0459@facc646b` | the shared value ledger |
| 3 | `TOOL-dCalibratedLens-3` | `cl-dClosedLoop-0460@401ecbd8` | the Loop Review |
| 4 | `TOOL-dCalibratedLens-4` | `cl-dClosedLoop-0461@ea09b304` | caps re-derived from evidence and review cost |
| 5 | `TOOL-dCalibratedLens-5` | `cl-dClosedLoop-0462@cad135ef` | instruction effectiveness measured from returns and findings that cite unit tags |
| 6 | `TOOL-dCalibratedLens-6` | `cl-dClosedLoop-0463@33710e39` | each role's `memory.item-budget` derived from its p90 over 30 sliced work orders under `measured` |
| 7 | `TOOL-dCalibratedLens-7` | `cl-dClosedLoop-0464@b1127f93` | the value ledger's shape rows |
| 8 | `TOOL-dCalibratedLens-8` | `cl-dClosedLoop-0465@4003d147` | the not-in-view cause added to `review.dispose`'s record |
| 9 | `TOOL-dCalibratedLens-9` | `cl-dClosedLoop-0466@f36d2aed` | probe cost priced in the value ledger |
| 10 | `TOOL-dCalibratedLens-10` | `cl-dClosedLoop-0467@58bd6ee5` | instruction evals: a replay suite of recorded items with known outcomes |
| 11 | `TOOL-dCalibratedLens-11` | `cl-dClosedLoop-0468@8f541e2a` | the Loop Review's delivery metrics: lead time |
| 12 | `TOOL-dCalibratedLens-12` | `cl-dClosedLoop-0469@653feb80` | the Loop Review pricing cost per item kind from trace rows (P35) |
| 13 | `TOOL-dCalibratedLens-13` | `cl-dClosedLoop-0470@dfafc75a` | the `lens` kind and namespace |
| 14 | `TOOL-dCalibratedLens-14` | `cl-dClosedLoop-0471@453f9872` | lens removal by a swap or by excluding a default lens |
| 15 | `TOOL-dCalibratedLens-15` | `cl-dClosedLoop-0472@bf8d8ee5` | each size breach priced in the value ledger by its bytes and its reads |
| 16 | `TOOL-dCalibratedLens-16` | `cl-dClosedLoop-0473@17126ed2` | the stall and loop classes Runtime journals |
| 17 | `TOOL-dCalibratedLens-17` | `cl-dClosedLoop-0474@b1852db0` | the node beats and the pools' ledgers trended |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12
ids TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dCalibratedLens's 17 clause(s) and 15 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 17 (cl-dClosedLoop-0458, cl-dClosedLoop-0459, cl-dClosedLoop-0460, cl-dClosedLoop-0461, cl-dClosedLoop-0462, cl-dClosedLoop-0463, cl-dClosedLoop-0464, cl-dClosedLoop-0465, cl-dClosedLoop-0466, cl-dClosedLoop-0467, cl-dClosedLoop-0468, cl-dClosedLoop-0469, cl-dClosedLoop-0470,
  cl-dClosedLoop-0471, cl-dClosedLoop-0472, cl-dClosedLoop-0473, cl-dClosedLoop-0474)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.loop.file, item.loop.gather, item.loop.lease, item.loop.price, item.loop.propose, item.loop.record, policy-key.flow.promote, policy-key.review.<stage>.effort, policy-key.review.loop.cadence, policy-key.review.loop.catch-source, policy-key.review.loop.retire,
  policy-key.review.loop.window-days, record-kind.loop-review, record-kind.value-ledger, tag-namespace.lens
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0459, cl-dClosedLoop-0462, cl-dClosedLoop-0466, cl-dClosedLoop-0467, cl-dClosedLoop-0468, cl-dClosedLoop-0469, cl-dClosedLoop-0472, cl-dClosedLoop-0473
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dTendedCadence](../dTendedCadence/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->

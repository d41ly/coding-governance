---
slug: dCalibratedLens
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18
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
**Build status:** OPEN · 17 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12
ids TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dCalibratedLens-2 — the shared value ledger: its snapshot, its view, its row grammar and the `price` verb](spec/2026-11-02-spec-TOOL-dCalibratedLens-2.md) | 1 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-3 — the Loop Review: a cadence step run as `review.loop.cadence` says, its lease keyed by the selected period, its walk and its record](spec/2026-11-02-spec-TOOL-dCalibratedLens-3.md) | 2 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-7 — the value ledger's shape rows, priced from the shape-run records `review.cost` and the journal reconcile write](spec/2026-11-02-spec-TOOL-dCalibratedLens-7.md) | 3 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-9 — probe cost priced in the value ledger, and compactions counted per item kind](spec/2026-11-02-spec-TOOL-dCalibratedLens-9.md) | 4 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-12 — the Loop Review pricing cost per item kind from trace rows](spec/2026-11-02-spec-TOOL-dCalibratedLens-12.md) | 5 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-15 — each size breach priced by its bytes and its reads, and a persisting or grown breach raised to the owner](spec/2026-11-02-spec-TOOL-dCalibratedLens-15.md) | 6 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-4 — the measured-value factory, and the `budgets.*` caps re-derived from evidence and review cost](spec/2026-11-02-spec-TOOL-dCalibratedLens-4.md) | 7 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-6 — each role's `memory.item-budget` derived from its p90 over 30 sliced work orders under `measured`](spec/2026-11-02-spec-TOOL-dCalibratedLens-6.md) | 8 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-16 — the stall and loop classes trended per scenario, item and rule, and their bounds re-derived once 30 builds have run under them](spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md) | 9 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-17 — the node beats and the pools' ledgers trended, and the reservation estimate per item kind re-derived from `trace.cost`](spec/2026-11-02-spec-TOOL-dCalibratedLens-17.md) | 10 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-5 — instruction effectiveness from returns and findings that cite unit tags, and the Loop Review's proposals under `review.loop.retire`, with the keep record](spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md) | 11 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-10 — instruction evals: a replay suite of recorded items with known outcomes, scored through the scorer factory, owed again by a held leg when an instruction unit changes](spec/2026-11-02-spec-TOOL-dCalibratedLens-10.md) | 12 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-11 — the Loop Review's delivery metrics and the owner queue's depth, read with no bound](spec/2026-11-02-spec-TOOL-dCalibratedLens-11.md) | 13 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-8 — the not-in-view cause on every confirmed finding, and the Loop Review's 38-finding reading of its share](spec/2026-11-02-spec-TOOL-dCalibratedLens-8.md) | 14 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-13 — the `lens` kind and namespace: gov's lenses tagged, a repository's lenses from its overlay, the fixed set with the five slots, and lens tags joined to the step gate](spec/2026-11-02-spec-TOOL-dCalibratedLens-13.md) | 15 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-1 — each stage review's lenses and effort: four stage literals in the lens catalogue, chosen by the breakpoint's stage, run at `review.<stage>.effort`](spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md) | 16 | 2 | OPEN | rev-1 | 2026-11-02 |
| [TOOL-dCalibratedLens-14 — lens removal by a swap or an exclusion, a repository lens's replay result, and scenario promotion as `flow.promote` says](spec/2026-11-02-spec-TOOL-dCalibratedLens-14.md) | 17 | 2 | OPEN | rev-1 | 2026-11-02 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-2
TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9.

Ids whose spec moved past its audited revision: none — 0 of 17 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dCalibratedLens's 17 clause(s) and 15 owned node(s), over 17 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 17
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0459, cl-dClosedLoop-0462, cl-dClosedLoop-0466, cl-dClosedLoop-0467, cl-dClosedLoop-0468, cl-dClosedLoop-0469, cl-dClosedLoop-0472, cl-dClosedLoop-0473
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dCalibratedLens-2` | no |
| 2 | `TOOL-dCalibratedLens-3` | no |
| 3 | `TOOL-dCalibratedLens-7` | no |
| 4 | `TOOL-dCalibratedLens-9` | no |
| 5 | `TOOL-dCalibratedLens-12` | no |
| 6 | `TOOL-dCalibratedLens-15` | no |
| 7 | `TOOL-dCalibratedLens-4` | no |
| 8 | `TOOL-dCalibratedLens-6` | no |
| 9 | `TOOL-dCalibratedLens-16` | no |
| 10 | `TOOL-dCalibratedLens-17` | no |
| 11 | `TOOL-dCalibratedLens-5` | no |
| 12 | `TOOL-dCalibratedLens-10` | no |
| 13 | `TOOL-dCalibratedLens-11` | no |
| 14 | `TOOL-dCalibratedLens-8` | no |
| 15 | `TOOL-dCalibratedLens-13` | no |
| 16 | `TOOL-dCalibratedLens-1` | no |
| 17 | `TOOL-dCalibratedLens-14` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dTendedCadence](../dTendedCadence/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->

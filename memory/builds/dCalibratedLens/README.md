---
slug: dCalibratedLens
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 TOOL-dCalibratedLens-49 TOOL-dCalibratedLens-50 TOOL-dCalibratedLens-51 TOOL-dCalibratedLens-52 TOOL-dCalibratedLens-53 TOOL-dCalibratedLens-54 TOOL-dCalibratedLens-55
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
**Build status:** DEFERRED · 47 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12
ids TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-18 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24
ids TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36
ids TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48
ids TOOL-dCalibratedLens-49 TOOL-dCalibratedLens-50 TOOL-dCalibratedLens-51 TOOL-dCalibratedLens-52 TOOL-dCalibratedLens-53 TOOL-dCalibratedLens-54 TOOL-dCalibratedLens-55

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dCalibratedLens-2 — the shared value ledger: its snapshot, its view, its row grammar and the `price` verb](spec/2026-11-02-spec-TOOL-dCalibratedLens-2.md) | 1 | 2 | DEFERRED | rev-6 | 2026-11-03 |
| [TOOL-dCalibratedLens-26 — a catch source that observed no run of a leg reads `-`, never 0, so no unobserved leg is proposed for retirement](spec/2026-11-02-spec-TOOL-dCalibratedLens-26.md) | 2 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-3 — the Loop Review: a cadence step run as `review.loop.cadence` says, its lease keyed by the selected period, its walk and its record](spec/2026-11-02-spec-TOOL-dCalibratedLens-3.md) | 2 | 2 | DEFERRED | rev-6 | 2026-11-03 |
| [TOOL-dCalibratedLens-19 — the three Loop Review record kinds homed at their id-rules' globs, so no record sits under another kind's home](spec/2026-11-02-spec-TOOL-dCalibratedLens-19.md) | 3 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-20 — every Loop Review record carries a `**Serves:**` line naming its kind, so the registry's field check reaches it](spec/2026-11-02-spec-TOOL-dCalibratedLens-20.md) | 3 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-22 — one route from every item to `file`: the walk collects each item's proposals, and every producer spells the five fields](spec/2026-11-02-spec-TOOL-dCalibratedLens-22.md) | 3 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-27 — a failing reading or proposer becomes an `unread` line, and the record is checked before anything is filed, so no period re-runs forever](spec/2026-11-02-spec-TOOL-dCalibratedLens-27.md) | 3 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-43 — `read_loop_records` lists the loop-review folder by prefix and filters by its id rule in Python, and a plant proves the listing is never empty](spec/2026-11-03-spec-TOOL-dCalibratedLens-43.md) | 3 | 2 | DEFERRED | rev-1 | 2026-11-03 |
| [TOOL-dCalibratedLens-7 — the value ledger's shape rows, priced from the shape-run records `review.cost` and the journal reconcile write](spec/2026-11-02-spec-TOOL-dCalibratedLens-7.md) | 3 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-32 — the `three-homes` plant's red twin restaged as the real `loop-review` row reverted to the bare folder, which dTotalRecall's unit 42 refuses at its S4](spec/2026-11-02-spec-TOOL-dCalibratedLens-32.md) | 4 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-33 — the three Loop Review homes observed disjoint by listing each home, never inferred from the record-kind check](spec/2026-11-02-spec-TOOL-dCalibratedLens-33.md) | 4 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-34 — the bug class of a staged break whose red rests on an ancestor clause a newer revision replaced, recorded so a spec review is handed it](spec/2026-11-02-spec-TOOL-dCalibratedLens-34.md) | 4 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-35 — every record the `three-homes` plant writes is graded by a registry row, and the keep joins the plant when unit 5 lands its row](spec/2026-11-02-spec-TOOL-dCalibratedLens-35.md) | 4 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-40 — an isolated failure's `<why>` folded to one line with no field separator, and a reading the writer would refuse read as `unread · refused value`](spec/2026-11-02-spec-TOOL-dCalibratedLens-40.md) | 4 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-9 — probe cost priced in the value ledger, and compactions counted per item kind](spec/2026-11-02-spec-TOOL-dCalibratedLens-9.md) | 4 | 2 | DEFERRED | rev-4 | 2026-11-03 |
| [TOOL-dCalibratedLens-12 — the Loop Review pricing cost per item kind from trace rows](spec/2026-11-02-spec-TOOL-dCalibratedLens-12.md) | 5 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-28 — no population is read through `gov_record.py find`: probe records and Loop Review records are listed from the index, acts read through the paging act reader](spec/2026-11-02-spec-TOOL-dCalibratedLens-28.md) | 5 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-42 — the `graded-by-a-row` case calls `derive_record_kind` with the parameters dTotalRecall's unit 53 gives it at its S21, and refuses any other form by name](spec/2026-11-03-spec-TOOL-dCalibratedLens-42.md) | 5 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-15 — each size breach priced by its bytes and its reads, and a persisting or grown breach raised to the owner](spec/2026-11-02-spec-TOOL-dCalibratedLens-15.md) | 6 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-4 — the measured-value factory, and the `budgets.*` caps re-derived from evidence and review cost](spec/2026-11-02-spec-TOOL-dCalibratedLens-4.md) | 7 | 2 | DEFERRED | rev-6 | 2026-11-03 |
| [TOOL-dCalibratedLens-21 — one carrier for a multi-line reading: the record's Metrics lines, one per entry, never a `fields`-form field](spec/2026-11-02-spec-TOOL-dCalibratedLens-21.md) | 8 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-6 — each role's `memory.item-budget` derived from its p90 over 30 sliced work orders under `measured`](spec/2026-11-02-spec-TOOL-dCalibratedLens-6.md) | 8 | 2 | DEFERRED | rev-5 | 2026-11-03 |
| [TOOL-dCalibratedLens-16 — the stall and loop classes trended per scenario, item and rule, and their bounds re-derived once 30 builds have run under them](spec/2026-11-02-spec-TOOL-dCalibratedLens-16.md) | 9 | 2 | DEFERRED | rev-4 | 2026-11-03 |
| [TOOL-dCalibratedLens-29 — the work-order population read without argv: paths on stdin, one history pass, one policy read per policy revision, timed over the real tree](spec/2026-11-02-spec-TOOL-dCalibratedLens-29.md) | 9 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-39 — `read_metrics_lines` answers an ordered list of `(name, value, source)` triples with every repeated name kept, held by a plant against a dict-shaped splitter](spec/2026-11-02-spec-TOOL-dCalibratedLens-39.md) | 9 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-17 — the node beats and the pools' ledgers trended, and the reservation estimate per item kind re-derived from `trace.cost`](spec/2026-11-02-spec-TOOL-dCalibratedLens-17.md) | 10 | 2 | DEFERRED | rev-2 | 2026-11-02 |
| [TOOL-dCalibratedLens-38 — the work orders' adding commits read through `tree_lib.read_adding_commits` and their policy text through `read_blobs_at`, proved on a re-added and a renamed work order](spec/2026-11-02-spec-TOOL-dCalibratedLens-38.md) | 10 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-5 — instruction effectiveness from returns and findings that cite unit tags, and the Loop Review's proposals under `review.loop.retire`, with the keep record](spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md) | 11 | 2 | DEFERRED | rev-5 | 2026-11-03 |
| [TOOL-dCalibratedLens-10 — instruction evals: a replay suite of recorded items with known outcomes, scored through the scorer factory, owed again by a held leg when an instruction unit changes](spec/2026-11-02-spec-TOOL-dCalibratedLens-10.md) | 12 | 2 | DEFERRED | rev-5 | 2026-11-03 |
| [TOOL-dCalibratedLens-25 — the `returned` line's units field sits before the agent id, and the format guard's fixtures and guard follow the fence](spec/2026-11-02-spec-TOOL-dCalibratedLens-25.md) | 12 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-11 — the Loop Review's delivery metrics and the owner queue's depth, read with no bound](spec/2026-11-02-spec-TOOL-dCalibratedLens-11.md) | 13 | 2 | DEFERRED | rev-4 | 2026-11-03 |
| [TOOL-dCalibratedLens-23 — the instruction-eval seed lands held, and a guarded edit's owed replay is recorded before the close bar](spec/2026-11-02-spec-TOOL-dCalibratedLens-23.md) | 13 | 2 | DEFERRED | rev-4 | 2026-11-03 |
| [TOOL-dCalibratedLens-31 — a shape's optional `[ · …]` group rendered as its content or dropped, and every fenced shape's rendered line admitted by the format guard](spec/2026-11-02-spec-TOOL-dCalibratedLens-31.md) | 13 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-37 — a fence edit selects the format guard's suite through `AGENTS.md` alone, a guard pathspec check 7c classes exactly once](spec/2026-11-02-spec-TOOL-dCalibratedLens-37.md) | 13 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-36 — the eval seed's `**Loads:**` stated, every edit to them since its replay listed, and its `held` read only after the main loop's replay](spec/2026-11-02-spec-TOOL-dCalibratedLens-36.md) | 14 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-44 — every line the shape arm renders is held free of a literal bracket, apart from a markdown link, so a `SPEC` line that leaks its group reds](spec/2026-11-03-spec-TOOL-dCalibratedLens-44.md) | 14 | 2 | DEFERRED | rev-1 | 2026-11-03 |
| [TOOL-dCalibratedLens-45 — a render error in the shape arm is that form's FAIL line, and a shape with no distinct second form is rendered once and said so](spec/2026-11-03-spec-TOOL-dCalibratedLens-45.md) | 14 | 2 | DEFERRED | rev-1 | 2026-11-03 |
| [TOOL-dCalibratedLens-47 — the `format-guard self-test` guard gains `AGENTS.md` and the roles renderer in the leg's declaration, rendered where the manifest is a render](spec/2026-11-03-spec-TOOL-dCalibratedLens-47.md) | 14 | 2 | DEFERRED | rev-1 | 2026-11-03 |
| [TOOL-dCalibratedLens-8 — the not-in-view cause on every confirmed finding, and the Loop Review's 38-finding reading of its share](spec/2026-11-02-spec-TOOL-dCalibratedLens-8.md) | 14 | 2 | DEFERRED | rev-5 | 2026-11-03 |
| [TOOL-dCalibratedLens-13 — the `lens` kind and namespace: gov's lenses tagged, a repository's lenses from its overlay, the fixed set with the five slots, and lens tags joined to the step gate](spec/2026-11-02-spec-TOOL-dCalibratedLens-13.md) | 15 | 2 | DEFERRED | rev-4 | 2026-11-03 |
| [TOOL-dCalibratedLens-1 — each stage review's lenses and effort: four stage literals in the lens catalogue, chosen by the breakpoint's stage, run at `review.<stage>.effort`](spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md) | 16 | 2 | DEFERRED | rev-5 | 2026-11-03 |
| [TOOL-dCalibratedLens-14 — lens removal by a swap or an exclusion, a repository lens's replay result, and scenario promotion as `flow.promote` says](spec/2026-11-02-spec-TOOL-dCalibratedLens-14.md) | 17 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-24 — the stage receiver judged by rule 2 at its new home over the real harness, green on the shipped harness and red on a looped copy](spec/2026-11-02-spec-TOOL-dCalibratedLens-24.md) | 17 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-30 — the round-1 spec audit's 41 minors batched: each correction carried by the sibling it lands on, and six arms that hold the classes no sibling owns](spec/2026-11-02-spec-TOOL-dCalibratedLens-30.md) | 18 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-41 — the round-2 spec audit's 28 minors batched: each correction carried by the sibling it lands on, and the loop legs' guards widened to the files their plants read](spec/2026-11-02-spec-TOOL-dCalibratedLens-41.md) | 19 | 2 | DEFERRED | rev-3 | 2026-11-03 |
| [TOOL-dCalibratedLens-46 — the loop legs' and `tier2-review self-test`'s guards widened in every spelling the leg is declared in, and rendered where the manifest is a render](spec/2026-11-03-spec-TOOL-dCalibratedLens-46.md) | 20 | 2 | DEFERRED | rev-2 | 2026-11-03 |
| [TOOL-dCalibratedLens-48 — the round-3 spec audit's 25 minors batched: each correction carried by the sibling it lands on](spec/2026-11-03-spec-TOOL-dCalibratedLens-48.md) | 21 | 2 | DEFERRED | rev-1 | 2026-11-03 |
<!-- /gen:build-units -->

Records: 160 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48.

Ids whose spec moved past its audited revision: TOOL-dCalibratedLens-1@rev-1 TOOL-dCalibratedLens-10@rev-1 TOOL-dCalibratedLens-11@rev-1 TOOL-dCalibratedLens-13@rev-1 TOOL-dCalibratedLens-14@rev-1 TOOL-dCalibratedLens-15@rev-1 TOOL-dCalibratedLens-16@rev-1 TOOL-dCalibratedLens-19@rev-1
TOOL-dCalibratedLens-2@rev-1 TOOL-dCalibratedLens-20@rev-1 TOOL-dCalibratedLens-21@rev-1 TOOL-dCalibratedLens-23@rev-1 TOOL-dCalibratedLens-24@rev-1 TOOL-dCalibratedLens-25@rev-1 TOOL-dCalibratedLens-29@rev-1 TOOL-dCalibratedLens-3@rev-1 TOOL-dCalibratedLens-30@rev-1 TOOL-dCalibratedLens-36@rev-1
TOOL-dCalibratedLens-4@rev-1 TOOL-dCalibratedLens-41@rev-1 TOOL-dCalibratedLens-5@rev-1 TOOL-dCalibratedLens-6@rev-1 TOOL-dCalibratedLens-7@rev-1 TOOL-dCalibratedLens-8@rev-1 TOOL-dCalibratedLens-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dCalibratedLens's 17 clause(s) and 15 owned node(s), over 47 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 17
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-11-02-spec-TOOL-dCalibratedLens-19.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-20.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-21.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-02-spec-TOOL-dCalibratedLens-22.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-23.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-24.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-25.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-02-spec-TOOL-dCalibratedLens-26.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-27.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-28.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-29.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-02-spec-TOOL-dCalibratedLens-30.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-31.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-32.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-33.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-02-spec-TOOL-dCalibratedLens-34.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-35.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-36.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-37.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-02-spec-TOOL-dCalibratedLens-38.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-39.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-40.md` (PLAY-dClosedLoop-2), `spec/2026-11-02-spec-TOOL-dCalibratedLens-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-03-spec-TOOL-dCalibratedLens-42.md` (PLAY-dClosedLoop-2), `spec/2026-11-03-spec-TOOL-dCalibratedLens-43.md` (PLAY-dClosedLoop-2), `spec/2026-11-03-spec-TOOL-dCalibratedLens-44.md` (PLAY-dClosedLoop-2), `spec/2026-11-03-spec-TOOL-dCalibratedLens-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-11-03-spec-TOOL-dCalibratedLens-46.md` (PLAY-dClosedLoop-2), `spec/2026-11-03-spec-TOOL-dCalibratedLens-47.md` (PLAY-dClosedLoop-2), `spec/2026-11-03-spec-TOOL-dCalibratedLens-48.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0459, cl-dClosedLoop-0462, cl-dClosedLoop-0466, cl-dClosedLoop-0467, cl-dClosedLoop-0468, cl-dClosedLoop-0469, cl-dClosedLoop-0472, cl-dClosedLoop-0473
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dCalibratedLens-2` | no |
| 2 | `TOOL-dCalibratedLens-26`, `TOOL-dCalibratedLens-3` | no |
| 3 | `TOOL-dCalibratedLens-19`, `TOOL-dCalibratedLens-20`, `TOOL-dCalibratedLens-22`, `TOOL-dCalibratedLens-27`, `TOOL-dCalibratedLens-43`, `TOOL-dCalibratedLens-7` | no |
| 4 | `TOOL-dCalibratedLens-32`, `TOOL-dCalibratedLens-33`, `TOOL-dCalibratedLens-34`, `TOOL-dCalibratedLens-35`, `TOOL-dCalibratedLens-40`, `TOOL-dCalibratedLens-9` | no |
| 5 | `TOOL-dCalibratedLens-12`, `TOOL-dCalibratedLens-28`, `TOOL-dCalibratedLens-42` | no |
| 6 | `TOOL-dCalibratedLens-15` | no |
| 7 | `TOOL-dCalibratedLens-4` | no |
| 8 | `TOOL-dCalibratedLens-21`, `TOOL-dCalibratedLens-6` | no |
| 9 | `TOOL-dCalibratedLens-16`, `TOOL-dCalibratedLens-29`, `TOOL-dCalibratedLens-39` | no |
| 10 | `TOOL-dCalibratedLens-17`, `TOOL-dCalibratedLens-38` | yes |
| 11 | `TOOL-dCalibratedLens-5` | no |
| 12 | `TOOL-dCalibratedLens-10`, `TOOL-dCalibratedLens-25` | yes |
| 13 | `TOOL-dCalibratedLens-11`, `TOOL-dCalibratedLens-23`, `TOOL-dCalibratedLens-31`, `TOOL-dCalibratedLens-37` | yes |
| 14 | `TOOL-dCalibratedLens-36`, `TOOL-dCalibratedLens-44`, `TOOL-dCalibratedLens-45`, `TOOL-dCalibratedLens-47`, `TOOL-dCalibratedLens-8` | no |
| 15 | `TOOL-dCalibratedLens-13` | no |
| 16 | `TOOL-dCalibratedLens-1` | no |
| 17 | `TOOL-dCalibratedLens-14`, `TOOL-dCalibratedLens-24` | no |
| 18 | `TOOL-dCalibratedLens-30` | no |
| 19 | `TOOL-dCalibratedLens-41` | no |
| 20 | `TOOL-dCalibratedLens-46` | no |
| 21 | `TOOL-dCalibratedLens-48` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFairHearing](../dFairHearing/README.md), [dTendedCadence](../dTendedCadence/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->

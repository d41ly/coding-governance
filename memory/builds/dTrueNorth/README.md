---
slug: dTrueNorth
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-21
spec-audit: 2026-10-21
parents: dClosedLoop
may: PLAY-dClosedLoop-3 PLAY-dClosedLoop-2
---

# dTrueNorth — the Fidelity build of the dClosedLoop chain

## The problem this build exists to solve

dTrueNorth owns 3 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-design-13,
gap-build-07, gap-mem-47. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 6 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per clause.
- Each unit built and landed, so the 3 owned gaps above close.
- Its extra unit built: the carry-forward condition for every unit a spec run adds, once, and the starting-roster
  reading it rests on, which every later chain spec run closes with.

## Detriments if this is not built

- Its 3 owned gaps stay open.
- Its 1 child build waits on it: dGroundRules.

## Build-level rules

- Phase: one whole run specs, audits, builds and lands every unit, the extra unit last, and closes without
  carry-forward.
- Read in the packet's order, `packet.py --check dTrueNorth` green before the first pass; a moved instrument blob is a
  stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dTrueNorth`, a record per member "recorded by nobody", the same with `--write` (commit it as
  `…-departures-build.md`) and `--check`, then `--authorization` and `--close`; again after a re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-11.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dTrueNorth-1` | `cl-dClosedLoop-0001@83b6b117` | the clause ids: each clause of the design read with its minted `cl-` id and the hash of its text as the design's `[clause-ids]` section defines it |
| 2 | `TOOL-dTrueNorth-2` | `cl-dClosedLoop-0002@6acd9ea9` | the carries join |
| 3 | `TOOL-dTrueNorth-3` | `cl-dClosedLoop-0003@d2811290` | the coverage report rendered into each chain build's README beside its unit ids: the clauses carried whole and split |
| 4 | `TOOL-dTrueNorth-4` | `cl-dClosedLoop-0004@c374ccd0` | the deviation record |
| 5 | `TOOL-dTrueNorth-5` | `cl-dClosedLoop-0005@5417efbc` | every audit of a spec record pinning the revision it read as `@rev-N` on its Serves line |
| 6 | `TOOL-dTrueNorth-6` | `cl-dClosedLoop-0006@06ceb3cc` | the as-built view: the design at its baseline commit with each deviation's amends or supersedes row applied |
| 7 | `TOOL-dTrueNorth-7` | **Derived:** PLAY-dClosedLoop-2 | the carry-forward condition for every unit a spec run adds, once, and the starting-roster reading it rests on |
| 8 | `TOOL-dTrueNorth-8` | **Derived:** PLAY-dClosedLoop-2 | the as-built view re-rendered in the commit that changes its inputs, with an owner and a moment |
| 9 | `TOOL-dTrueNorth-9` | **Derived:** PLAY-dClosedLoop-2 | `_expand_ids` keeps its two-value return for all four callers, and the audit pins come from a sibling reader |
| 10 | `TOOL-dTrueNorth-10` | **Derived:** PLAY-dClosedLoop-2 | deviation records 2 and 3, written verbatim at kind `deviation`, the view re-rendered in their commit |
| 11 | `TOOL-dTrueNorth-11` | **Derived:** PLAY-dClosedLoop-2 | the build-index and memory-hygiene self-test legs guard the spec-token checker their arms load |
| 12 | `TOOL-dTrueNorth-12` | **Derived:** PLAY-dClosedLoop-2 | the routed-commits self-test reaches the strip through a resolver and builds its own design in the fixture |
| 13 | `TOOL-dTrueNorth-13` | **Derived:** PLAY-dClosedLoop-2 | a design-document subject of a spec audit: its id served bare, and no pin owed for it |
| 14 | `TOOL-dTrueNorth-14` | **Derived:** PLAY-dClosedLoop-2 | the audit-pin arm grades a record by the harness that wrote it, so a run in flight is not refused at its merge |
| 15 | `TOOL-dTrueNorth-15` | **Derived:** PLAY-dClosedLoop-2 | check 29 counts what it graded on every run, and says so when nothing was |
| 16 | `TOOL-dTrueNorth-16` | **Derived:** PLAY-dClosedLoop-2 | the round-1 spec audit's 37 minors: one key rule, one revision reader, one conf read, honest exits and the docs that name them |
| 17 | `TOOL-dTrueNorth-17` | **Derived:** PLAY-dClosedLoop-2 | the order-3 transition of the as-built view: the render's code is a view input, and the second of units 4 and 6 to land re-renders |
| 18 | `TOOL-dTrueNorth-18` | **Derived:** PLAY-dClosedLoop-2 | two amends of one clause are ordered by a declared supersession, never by path |
| 19 | `TOOL-dTrueNorth-19` | **Derived:** PLAY-dClosedLoop-2 | the audit-writer reader takes one glob pathspec, refuses a failed git call, and grades a record whose harness is missing |
| 20 | `TOOL-dTrueNorth-20` | **Derived:** PLAY-dClosedLoop-2 | the round-2 spec audit's 38 minors: declared keys, honest exits, bounded reads, one reader each, and the records that name them |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 20 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16
ids TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTrueNorth-1 — the clause ids and binding lines, parsed once, behind a cutoff](spec/2026-10-21-spec-TOOL-dTrueNorth-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-2 — the carries join, a further join of the spec tokens leg](spec/2026-10-21-spec-TOOL-dTrueNorth-2.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-3 — the coverage region in each chain build's README, and the INPROGRESS refusal](spec/2026-10-21-spec-TOOL-dTrueNorth-3.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-11 — the build-index and memory-hygiene self-test legs guard the spec-token checker their arms load](spec/2026-10-21-spec-TOOL-dTrueNorth-11.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-15 — check 29 counts what it graded on every run, and says so when nothing was](spec/2026-10-21-spec-TOOL-dTrueNorth-15.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-5 — every spec audit pins the revision it read](spec/2026-10-21-spec-TOOL-dTrueNorth-5.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-13 — a design-document subject of a spec audit: its id served bare, and no pin owed for it](spec/2026-10-21-spec-TOOL-dTrueNorth-13.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-14 — the audit-pin arm grades a record by the harness that wrote it, so a run in flight is not refused at its merge](spec/2026-10-21-spec-TOOL-dTrueNorth-14.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-4 — the deviation record, its population from history, and its join at the commit and at the close](spec/2026-10-21-spec-TOOL-dTrueNorth-4.md) | 3 | 2 | CLOSED | rev-4 | 2026-10-21 |
| [TOOL-dTrueNorth-6 — the as-built view, generated from the baseline and the deviation records, and its gate](spec/2026-10-21-spec-TOOL-dTrueNorth-6.md) | 3 | 2 | OPEN | rev-4 | 2026-10-21 |
| [TOOL-dTrueNorth-9 — `_expand_ids` keeps its two-value return for all four callers, and the audit pins come from a sibling reader](spec/2026-10-21-spec-TOOL-dTrueNorth-9.md) | 3 | 2 | OPEN | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-10 — deviation records 2 and 3, written verbatim at kind `deviation`, the view re-rendered in their commit](spec/2026-10-21-spec-TOOL-dTrueNorth-10.md) | 4 | 2 | OPEN | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-12 — the routed-commits self-test reaches the strip through a resolver and builds its own design in the fixture](spec/2026-10-21-spec-TOOL-dTrueNorth-12.md) | 4 | 2 | OPEN | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-19 — the audit-writer reader takes one glob pathspec, refuses a failed git call, and grades a record whose harness is missing](spec/2026-10-21-spec-TOOL-dTrueNorth-19.md) | 4 | 2 | OPEN | rev-1 | 2026-10-21 |
| [TOOL-dTrueNorth-8 — the as-built view re-rendered in the commit that changes its inputs, with an owner and a moment](spec/2026-10-21-spec-TOOL-dTrueNorth-8.md) | 4 | 2 | OPEN | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-16 — the round-1 spec audit's 37 minors: one key rule, one revision reader, one conf read, honest exits and the docs that name them](spec/2026-10-21-spec-TOOL-dTrueNorth-16.md) | 5 | 2 | OPEN | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-17 — the order-3 transition of the as-built view: the render's code is a view input, and the second of units 4 and 6 to land re-renders](spec/2026-10-21-spec-TOOL-dTrueNorth-17.md) | 5 | 2 | OPEN | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-18 — two amends of one clause are ordered by a declared supersession, never by path](spec/2026-10-21-spec-TOOL-dTrueNorth-18.md) | 5 | 2 | OPEN | rev-2 | 2026-10-21 |
| [TOOL-dTrueNorth-20 — the round-2 spec audit's 38 minors: declared keys, honest exits, bounded reads, one reader each, and the records that name them](spec/2026-10-21-spec-TOOL-dTrueNorth-20.md) | 7 | 2 | OPEN | rev-3 | 2026-10-21 |
| [TOOL-dTrueNorth-7 — the carry-forward of a unit a spec run adds, once, and the starting roster it rests on](spec/2026-10-21-spec-TOOL-dTrueNorth-7.md) | 8 | 2 | OPEN | rev-2 | 2026-10-21 |
<!-- /gen:build-units -->

Records: 38 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20.

Ids whose spec moved past its audited revision: none — 0 of 20 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dTrueNorth's 6 clause(s) and 1 owned node(s), over 20 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 6
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-21-spec-TOOL-dTrueNorth-10.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-11.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-12.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-13.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-21-spec-TOOL-dTrueNorth-14.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-15.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-16.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-17.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-21-spec-TOOL-dTrueNorth-18.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-19.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-20.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-7.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-21-spec-TOOL-dTrueNorth-8.md` (PLAY-dClosedLoop-2), `spec/2026-10-21-spec-TOOL-dTrueNorth-9.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0002
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTrueNorth-1`, `TOOL-dTrueNorth-2`, `TOOL-dTrueNorth-3` | yes |
| 2 | `TOOL-dTrueNorth-11`, `TOOL-dTrueNorth-15`, `TOOL-dTrueNorth-5` | yes |
| 3 | `TOOL-dTrueNorth-13`, `TOOL-dTrueNorth-14`, `TOOL-dTrueNorth-4`, `TOOL-dTrueNorth-6`, `TOOL-dTrueNorth-9` | yes |
| 4 | `TOOL-dTrueNorth-10`, `TOOL-dTrueNorth-12`, `TOOL-dTrueNorth-19`, `TOOL-dTrueNorth-8` | yes |
| 5 | `TOOL-dTrueNorth-16`, `TOOL-dTrueNorth-17`, `TOOL-dTrueNorth-18` | yes |
| 7 | `TOOL-dTrueNorth-20` | no |
| 8 | `TOOL-dTrueNorth-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dClosedLoop](../dClosedLoop/README.md)
- **Child builds:** [dGroundRules](../dGroundRules/README.md)
<!-- /gen:build-edges -->

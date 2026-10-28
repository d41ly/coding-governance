# TOOL-dIndexedDesign-50 — unit 44's finder bookkeeping lands in unit 16's pass commit, so a `coverage: 'only'` run writes its record from unit 35's pass on

**Status:** DEFERRED · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 6 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-50-deviation-501.md](../build/2026-10-28-build-TOOL-dIndexedDesign-50-deviation-501.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, report item **H2**, the item's only id.
`tools/workflows/tier2-review.template.js:890-892` derives `lensesRunning` from `LENS_KEYS` minus the
skipped lenses. Unit 35 S3 skips all five under `coverage: 'only'`, so `lensesRunning` and `lensesDead`
are both 0, and `:1301` returns `deferred-platform` with `report: null`. `TOOL-dIndexedDesign-44` fixes
those counts at order 5, after unit 35's pass at order 4, and its Rollout admits that an `only` run writes
no record before it lands. Yet unit 35 AC3, observed at unit 35's own pass, requires that record to
carry `**Serves:** coverage-lens`, and unit 38 S2 and AC2 require it committed after unit 35's pass
commit and before the next.

This unit takes the report's sound fix. Unit 44's S1 to S4 land in unit 16's pass commit, beside
`TOOL-dIndexedDesign-39` S1, the commit that first carries the coverage stage. Unit 44's own pass then
observes its criteria there. It repairs `TOOL-dIndexedDesign-44` and takes order 6, one above unit 44's 5.

## 2. Scope (IN)

- **S1** — The co-landing, an act ahead of this unit's order. Unit 16's pass commit carries unit 44's S1
  to S4 beside unit 39 S1's landing of unit 35's S1 to S4: the finder counts, the `find:coverage` dead
  label, the coverage findings joined to `allFindings`, and `find-coverage.json`. The pass's
  `--dispatch` row already declares the three workflow files, which unit 39 S1 names. Its commit subject
  names `TOOL-dIndexedDesign-16` and this unit's id. Observed by AC1 and AC3.
- **S2** — Unit 44's own pass, at order 5, builds only its §7 arm and observes its AC1 to AC4. It
  rewrites none of S1 to S4. Observed by AC2.
- **S3** — Two sentences superseded. Unit 44's Rollout sentence that an `only` run "takes the all-dead
  return and writes no record" before unit 44's pass, and unit 38's Edges claim that S2's reading runs
  after unit 44's pass, both read "from unit 16's pass tip". Unit 44's acceptance ledger carries the note
  `TOOL-dIndexedDesign-50 S3` under AC2's answer, and unit 38's under AC2's answer. Observed by AC4.

## 3. Non-goals (OUT)

- The bookkeeping itself, the counts, label, join and durable file: `TOOL-dIndexedDesign-44`'s design,
  unchanged. This unit moves when they land.
- Whether the returned `lensesRun`, `lensesDead` and `agents` count the coverage agent: report id 22,
  LOW, in `TOOL-dIndexedDesign-53`.
- How the run passes the reading window, unit 38 §8 F1: the owner's, parked.
- The report's left-shift checklist entry. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — S8's `coverage` argument and `coverage-lens` binding, in whose pass commit S1 lands unit 44's bookkeeping (id 3)
- **consumes-from** `TOOL-dIndexedDesign-35` — S2 and S3's coverage stage and its `only` mode, and AC3, which S1 makes reachable at that unit's own pass (id 3)
- **consumes-from** `TOOL-dIndexedDesign-44` — S1 to S4, which S1 lands in unit 16's pass, and the Rollout sentence S3 supersedes (id 3)
- **hands-off** `TOOL-dIndexedDesign-38` — S2's `coverage: 'only'` reading and AC2's window, both reachable from unit 35's pass commit once S1 lands (id 3)

## 4. Design

### Evidence

- `tools/workflows/tier2-review.template.js:890-892` derive `skippedLenses`, `runningLensKeys` and
  `lensesRunning`. `:1301` tests `lensesDead === lensesRunning` and `:1313` returns `report: null`.
  Read 2026-10-28.
- `TOOL-dIndexedDesign-39` S1 already lands unit 35's S1 to S4 in unit 16's pass, so the stage and its
  counts can share that commit.
- `tools/unattended/unattended.sh:13804` refuses a `--dispatch` whose `consumes-from` producer is neither
  CLOSED nor WONTDO. This unit's producers sit at orders 3, 4 and 5, all before its own.

### Inventory

Minted: no identifier. One sequencing act and two ledger notes.

### Migration

None: no commit of this build exists yet.

### Rollout

S1 lands in unit 16's pass, order 3. Unit 16's and unit 44's Edges blocks name it, and their builders
read it there. S2 is unit 44's pass, order 5. S3 and AC1 to AC4 are this unit's own pass at order 6,
beside `TOOL-dIndexedDesign-2` and `TOOL-dIndexedDesign-45`. This unit writes only ledgers, so its write
set meets neither of theirs.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js` its render by
  `check-protocol-parity.test.sh --render`: S1, in unit 16's pass
- `memory/builds/dIndexedDesign/build/`: S3's ledger notes and the recorded observations

### Alternatives rejected

- **Supersede unit 35 AC3's record clause and unit 38 S2 and AC2's window instead.** The report's second
  option. It gives up a criterion and a reading window to keep an ordering, and leaves an `only` run
  unable to record at unit 35's pass.
- **Move unit 44 to order 4.** Units sharing an order are still two passes and two commits, so unit 35's
  pass could still land first.

## 5. Production-readiness checklist

- security — N/A: no new agent or write path; the bookkeeping is unit 44's.
- perf / scale — none.
- error / empty / loading states — from unit 16's pass tip a dead coverage agent defers and a live one
  under `only` records, as unit 44 states.
- observability — AC1's commit list names where the bookkeeping first landed.
- risks — unit 16's builder must read S1 from its Edges block. AC1 reads the commit, so a missed
  co-landing is visible at this unit's pass.
- testing — AC1 and AC2 by `git`, AC3 by unit 35 AC3's own stub at that unit's commit, AC4 by a ledger grep.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git log --reverse --format=%H -S "find:coverage" <base>..HEAD -- tools/workflows/tier2-review.template.js`
  runs at this unit's pass, its first line is unit 16's pass commit, and `git show` of that commit adds
  `COVERAGE_BRIEF` too.
  Red when: the label first lands in a later commit than the coverage stage.
  figure: the list is DERIVED from the run's pinned BASE at this unit's pass.
- **AC2** — When `git diff <p>^ <p> -- tools/workflows/tier2-review.template.js` runs for unit 44's pass
  commit `<p>`, it prints nothing.
  Red when: unit 44's own pass rewrites the harness.
- **AC3** — When unit 35 AC3's `node -e` stub run with `coverage: 'only'` evaluates
  `tools/workflows/tier2-review.js` in a worktree at unit 35's pass commit, with a coverage agent returning
  one finding, it returns `exit: 'complete'` and a record carrying `**Serves:** coverage-lens`.
  Red when: it returns `deferred-platform`, or writes no record.
- **AC4** — When `grep -n "TOOL-dIndexedDesign-50 S3"` runs over the acceptance ledgers of units 44 and
  38, it prints one note under each AC2 answer.
  Red when: a note is missing or stands as its own `- AC` line.
  permission: unit 38's note is read at the close, after unit 38's pass.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `verifier fan-out` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 39 to 46, id 3
  (HIGH, item H2), on its sound fix, repairing TOOL-dIndexedDesign-44's Rollout and order.

## 10. Reuse audit

The seam is the act-ahead form `TOOL-dIndexedDesign-39` S1 already uses for unit 35's stage in the same
commit, so no new sequencing mechanism is written. The probe
`python tools/codebase-map/reuse_lookup.py "land two units' changes in one pass commit so an unguarded leg is never red at a pass tip"`
ranked `legs`, `leg`, `units`, `changed` and `build_commit`. None is a co-landing seam, so no existing
seam fits beyond the act-ahead form.

Recall terms used: `python tools/memory-recall/query.py "how does a repair land before the pass whose criterion it makes reachable" --terms "repair unit order act ahead pass commit coverage only record deferred-platform lensesRunning finder counts"`

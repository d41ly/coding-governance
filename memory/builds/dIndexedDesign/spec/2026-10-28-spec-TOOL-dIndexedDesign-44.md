# TOOL-dIndexedDesign-44 — the coverage stage is a finder in every count, dead label, finding join and durable file the Find stage keeps

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 5 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 31 to 38
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`)
confirmed finding **id 26 at HIGH**, report item **H6**, the item's only id. `TOOL-dIndexedDesign-35` S1
puts the coverage stage outside `LENSES`. Every piece of the Find stage's bookkeeping in
`tools/workflows/tier2-review.template.js` is keyed on `LENSES` or `runningLensKeys`, and unit 35 names
none of those sites. Under `coverage: 'only'` all five lenses are skipped, so `lensesRunning` is 0 and
`lensesDead` is 0, and the all-dead return at `:1301` fires before any coverage finding is verified. It
returns `deferred-platform` and writes no record. Under `coverage: 'with'` a coverage agent that dies is
in neither `lensesDead`, `deadLensLabels` nor `pending`. The run returns `complete`, and its record's
`coverage=with` certifies a sweep that never ran.

This unit counts the coverage stage as one more finder wherever the Find stage counts, labels, joins or
reuses a finder. The lens-yield row is report id 33, a MEDIUM, batched into `TOOL-dIndexedDesign-46`.
It repairs `TOOL-dIndexedDesign-35` and takes order 5, one above unit 35's 4.

## 2. Scope (IN)

Every site below is named at base, read 2026-10-28. Units 16 and 35 edit the file first, so the builder
finds each by the symbol named.

- **S1** — The counts. When the coverage stage dispatched, under `with` or `only`, it adds one to the
  running finder count and, when its agent returned null, one to the dead count. Both reads use these
  counts: the all-dead test (`if (lensesDead === lensesRunning)`, `:1301`) and the
  `allFindings.length === 0` branch (`:1321`). Their notes and `renderStageShape` totals use them too.
  Under `skip` nothing changes. Observed by AC1, AC2 and AC3.
- **S2** — The label. A coverage agent that returned null adds `find:coverage` to `deadLensLabels`
  (`:1238`), so `pending` names it at every deferred return and `pendingLabels` carries it to the
  partial-fan return (`:1689`). Observed by AC1 and AC3.
- **S3** — The findings. The coverage agent's findings join `allFindings` (`:1244-1246`) before ids are
  assigned, each tagged lens `coverage`, so they reach the Verify stage and the synthesis like any
  finder's. Observed by AC2.
- **S4** — The durable file. Under `workerType: 'none'` the coverage agent writes
  `find-coverage.json` under the review key as each lens writes `find-<lens>.json` (`:1218`). A present
  file whose `key` matches is reused and not dispatched, as the reuse loop does (`:1093-1098`).
  Observed by AC4.

## 3. Non-goals (OUT)

- The lens-yield row for `coverage` (`deriveLensYield`, `:1256-1276`): report id 33, MEDIUM, in
  `TOOL-dIndexedDesign-46`.
- The stage's existence, its brief and its modes: unit 35 S1 to S4, landed in unit 16's pass by
  `TOOL-dIndexedDesign-39` S1.
- `SPEC_LENSES`, `LENS_KEYS` and the checklist split: unchanged; `coverage` joins none of them.
- The report's left-shift arm, beyond AC1 and AC3's own arm in §7.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-35` — S2 and S3's coverage stage and its `only` mode, whose agent S1 to S4 count, label, join and make durable (id 26)
- **consumes-from** `TOOL-dIndexedDesign-16` — S8's `coverage` argument and `coverage-lens` binding, whose `only` record S1 lets a run reach (id 26)
- **hands-off** `TOOL-dIndexedDesign-38` — S2's first `coverage: 'only'` reading, which runs after this unit's pass, since before it an `only` run writes no record (id 26)
- **hands-off** `TOOL-dIndexedDesign-46` — the coverage stage's finder bookkeeping, beside which that unit's item for report id 33 adds the lens-yield row

## 4. Design

### Evidence

- `tools/workflows/tier2-review.template.js:890-892` derive `skippedLenses`, `runningLensKeys` and
  `lensesRunning` from `LENS_KEYS`. `:1176-1178` resolve a skipped lens to a non-null sentinel, so
  `lensesDead` (`:1234`) counts only nulls. `:1301` returns `deferred-platform` with `report: null` when
  `lensesDead === lensesRunning`, 0 equal to 0 under `only`.
- `:1238` builds `deadLensLabels` from `LENSES`. `:1312`, `:1337`, `:1667` and `:1701` return `pending`
  from it or from `pendingLabels` (`:1655`). `:1689` defers whenever `pendingLabels` is non-empty.
- `:1244-1246` build `allFindings` from `finderResults` by `LENSES` index. `:1093-1098` reuse a
  `find-<lens>.json` whose `key` matches the review key.

### Data model

```
finders running = lensesRunning + (coverage dispatched ? 1 : 0)
finders dead    = lensesDead    + (coverage dispatched && coverage result null ? 1 : 0)
deadLensLabels  = [...lens labels, ...(coverage dead ? ['find:coverage'] : [])]
allFindings     = lens findings ++ coverage findings (lens 'coverage'), then ids 1..N
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `find:coverage` | agent label | none |
| `find-coverage.json` | durable file name under the review key | none |
| `coverageResult` | local constant, `tier2-review.template.js` | none: locals are not graded |

### Migration

None: no review has run the coverage stage.

### Rollout

Live at its pass, order 5, beside `TOOL-dIndexedDesign-39`, `TOOL-dIndexedDesign-36` and
`TOOL-dIndexedDesign-7`, none of which writes a workflow file. The first `coverage: 'only'` reading,
unit 38 S2's act, runs after this pass. Before it, an `only` run takes the all-dead return and writes no
record, so a reading taken between unit 35's pass and this one would be lost. Unit 38's Edges block
names the order.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`: S1 to S4
- `tools/workflows/tier2-review.js`: its render, by `check-protocol-parity.test.sh --render`
- `tools/workflows/tier2-review.test.sh`: the arm §7 declares

### Alternatives rejected

- **Put `coverage` in `LENS_KEYS` so every site sees it.** Lost to unit 35 S1 and S4: the checklist
  split and the agent-cap receiver both read that list, and a sixth key brings back the denied harness.
- **A separate early return for `only`.** Lost to the `with` death: it would fix one mode and leave a
  dead coverage agent uncounted under the other.

## 5. Production-readiness checklist

- security — N/A: no new agent and no write path; one more durable file under the review key.
- perf / scale — none: one count, one label, one file.
- error / empty / loading states — a dead coverage agent now defers, naming `find:coverage`, under both
  modes. Under `only`, zero findings from a live coverage agent read `clean: 0 findings`.
- observability — the deferred note and the shape line count the coverage stage.
- risks — the coverage findings shift no lens finding's id, since they join after the lens findings.
- testing — AC1 to AC4 by stub runs under `node`; the arm §7 declares.
- migration — none.
- user docs — none under `help/`; `tools/workflows/README.md` is report id 29's.

## 6. Acceptance criteria

- **AC1** — When a `node -e` stub run evaluates `tier2-review.js` with `kind: 'spec-audit'`,
  `coverage: 'with'`, five lens agents returning findings and a coverage agent returning null, it
  returns `exit: 'deferred-platform'` and `pending` holds `find:coverage`.
  Red when: the run returns `complete`.
- **AC2** — When the same stub runs with `coverage: 'only'` and a coverage agent returning one finding,
  that finding reaches the Verify stage tagged lens `coverage`, and the run returns `complete` with a
  record carrying `**Serves:** coverage-lens`.
  Red when: the run takes the all-dead return, or the finding skips verification.
- **AC3** — When the stub runs with `coverage: 'only'` and a coverage agent returning null, it returns
  `deferred-platform` with `pending` equal to `['find:coverage']`, and its note counts 1 of 1 finders
  dead.
  Red when: the note counts 0 of 0, or `pending` is empty.
- **AC4** — When the stub runs under `workerType: 'none'` with a `find-coverage.json` present whose `key`
  matches, it dispatches no coverage agent and logs `reused find:coverage`.
  Red when: the file is ignored, or a stale `key` is reused.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 · each `coverage` mode with a stub coverage agent returning null and returning one finding, staged by leaving the coverage stage out of the finder counts · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of units 31 to 38, id 26
  (HIGH, item H6), on its sound fix, repairing TOOL-dIndexedDesign-35 S2, S3 and §5.

## 10. Reuse audit

The seams are the Find stage's own bookkeeping in `tools/workflows/tier2-review.template.js`: the
counts (`:890-892`, `:1234`), `deadLensLabels` (`:1238`), `allFindings` (`:1244`) and the durable reuse
loop (`:1093`). S1 to S4 extend each by one finder, and no parallel bookkeeping is written. The probe
`python tools/codebase-map/reuse_lookup.py "count a single extra review agent as a finder in the dead and pending bookkeeping"`
ranked `counts`, `measure_typed_counts`, `renderAgentLabel`, `build_baseline_findings` and
`build_counted_values`. Only `renderAgentLabel` is in the harness, and it labels an agent rather than
counting one, so no seam fits beyond the sites named.

Recall terms used: `python tools/memory-recall/query.py "how does the review harness count a dead finder and what it defers" --terms "tier2-review lensesDead lensesRunning deadLensLabels pending deferred-platform coverage stage finder durable find json"`

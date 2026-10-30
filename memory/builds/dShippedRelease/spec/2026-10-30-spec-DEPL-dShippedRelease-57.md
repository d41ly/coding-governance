# DEPL-dShippedRelease-57 — `ci_emit.py check`'s fixture states its green baseline, so unit 8's row criteria can fail

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 28 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 7 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`, HIGH,
item H2, which stands beside id 57 (DEPL-dShippedRelease-54). Under `--root <scratch copy>` the
unplanted state already exited 1, so the exit 1 of unit 8's AC2, AC3, AC4 and AC7 could not be told
from the baseline. Once the row arm is scoped, AC7's stale row and AC3's first half need a
`--workflow` to red at all. This unit makes every plant prove its own contrast.

## 2. Scope (IN)

- **S1** — The baseline. `check_fixture_baseline(argv)` in `tools/integrations/ci/ci_emit.py`, the
  in-file arms' first step per case, runs the case's command on the unplanted copy and fails the
  case unless it exits 0. Observed by AC1.
- **S2** — The row criteria. Unit 8 AC7's stale-row plant and AC3's first half pass
  `--workflow <copy of gov's workflow>`, the only form under which `check_rows_used` runs. Observed
  by AC2.
- **S3** — Each case prints `baseline 0 · planted <n>`, so a red names the contrast it rests on.
  Observed by AC3.

## 3. Non-goals (OUT)

- The arm's scope: DEPL-dShippedRelease-54.
- A baseline rule for other modules: the audit's left-shift item, which no clause of this build
  names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-8` — the criteria and in-file arms this unit restates
- **consumes-from** `DEPL-dShippedRelease-54` — `check_rows_used`, whose scope decides which plants pass `--workflow`

## 4. Design

### Evidence

- Unit 8's AC2, AC3, AC4 and AC7 each state an exit 1 with no statement of the unplanted exit.
- `--workflow` is the only input that names `actions/upload-artifact`, so a stale row with no workflow is ungraded by DEPL-dShippedRelease-54 S1.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_fixture_baseline` | function, `tools/integrations/ci/ci_emit.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/integrations/ci/ci_emit.py`: S1, S3

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — each case runs the check twice on a scratch copy, seconds in all.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py --fixture --case baseline-red` runs with the copy's unplanted
  state broken, it exits 1 naming `baseline`.
  Red when: a plant's exit 1 can stand on a red baseline, the defect of unit 8's four criteria.
- **AC2** — When `python ci_emit.py check --root <scratch copy> --workflow <copy of gov's workflow>`
  runs with a row no file uses, it exits 1 naming the row; with that row taken back out it exits 0.
  Red when: the stale-row plant reds by baseline and not by its row.
- **AC3** — When `python ci_emit.py --fixture` runs on the tree, every case line prints
  `baseline 0`.
  Red when: a case passes with no baseline read.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC2 AC3 · `baseline-red`, its failing case the baseline step cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 7 (HIGH, item H2) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-8's `ci_emit.py check`.
`python tools/codebase-map/reuse_lookup.py "pin third party action uses lines by sha in a workflow and check them"`
ranked name-stem helpers (`check`, `check_line`, `load_workflows`) and no pin reader, since the
module is specced and unbuilt, so no existing seam fits apart from that parent. The recall probe
surfaced unit 8 itself and the shape audit's row on gov's own workflow, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how are emitted ci action pins graded for an adopter that holds no workflow file" --terms "action pins uses sha workflow emitted ci adopter rendered outcome stopped_ok gate leg"`

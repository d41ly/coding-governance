# DEPL-dRemeasuredRender-4 — the closing review's mediums and lows: the hole verdict waits for the verify pass, and every KEPT reason has an arm

**Status:** CLOSED · rev-1 · 2026-10-11 · node d · Tier-2 · base 9a8777b8 · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-DEPL-dRemeasuredRender-4-1-acceptance-ledger.md](../build/2026-10-11-build-DEPL-dRemeasuredRender-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-DEPL-dRemeasuredRender-4-1-build-brief.md](../prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-4-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's three mediums and seven lows (round 1, ids 1, 3, 5, 6, 7, 9, 10,
11, 12 and 13), batched into one unit because every fix writes `tools/govkit/govkit.py` or its
self-test. The one behaviour change: the hole re-probe printed its verdict before the verify pass
could roll the render back. The rest are arms for branches no arm drove.

## 2. Scope (IN)

- **S1** — The post-render hole re-probe moves out of the regenerate loop to beside the re-measure
  step, after the verify pass and its rollbacks, so its verdict reads the bytes the target finally
  holds. A rolled-back kit's line says the render was rolled back. Ids 1, 5 and 11. Observed by AC1.
- **S2** — The re-probe's verdict-to-line mapping becomes a pure function, `render_hole_verdict`,
  unit-tested in-process for all three verdict kinds. Id 10. Observed by AC2.
- **S3** — Arms for the KEPT reasons no arm drove: `its kit was rolled back` (the existing rollback
  fixture), `its render did not run this time` (`GOVKIT_RERENDER=0`) and `its file is absent after
  the render`, each with the row unchanged. Ids 6, 9 and 13. Observed by AC3.
- **S4** — The re-measure fixture declares a file-read `version_from` that differs between its two
  vintages, and an arm asserts the row's `version` moved. Id 7. Observed by AC4.
- **S5** — A refused regenerate beside an undischarged hole: the hole is still re-probed and
  reported. Id 12. Observed by AC5.
- **S6** — The `[aHI-1 S3]` arm asserts the EARLY line, `probes undischarged before the render`,
  rather than a string only the re-probe prints. Id 3. Observed by AC6.

## 3. Non-goals (OUT)

- The review's proposed meta-gates over every `KEPT` literal and every "Observed by" clause: each
  is a new gate over the whole engine and the whole spec corpus, a unit of its own. The classes are
  recorded as gotchas instead (§7).

### Edges

- **consumes-from** `DEPL-dRemeasuredRender-3` — sequenced after it; both write
  `tools/govkit/govkit.py` and `tools/govkit/selftest.py`.

## 4. Design

### Evidence

Read at `bac1a4fb`. The re-probe sits inside the per-kit regenerate loop; the verify pass after it
adds a green-to-red kit to `_rolled_kits` and restores every `_rg_snap` path. The re-measure step
already sits after both and reads `_rolled_kits`. The rollback fixture `kit_rb` reaches the
rolled-back KEPT branch and nothing asserts it.

### Inventory

- `render_hole_verdict` — a function: given a kit id, a hole id, its verdict, its detail, its
  reason and whether the kit was rolled back, it returns the one line the run prints.
- `_hu_late` — a dict in `_cmd_update`, kit id to what the deferred re-probe needs.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/gotchas/verdict-printed-before-the-step-that-reverts-it.md`

### Alternatives rejected

- **Keep the re-probe in the loop and suppress its line for a kit later rolled back.** Rejected:
  the loop cannot know the verify pass's outcome, so the suppression would be a second print site
  deciding the same question after the fact.

## 5. Production-readiness checklist

- security — N/A — moves an existing gov-declared probe later in the same run.
- perf / scale — unchanged: the same probes, run once each.
- error / empty / loading states — a re-probe reading neither verdict prints its one line.
- observability — the after-render line names a rollback when there was one.
- risks — the hole lines now print after the verify lines; no reader parses their order.
- testing — seven new or repointed arms, each behaviour arm observed red against `bac1a4fb`.
- migration — none.
- user docs — N/A — the runbook sentence already says the hole is probed again after the render.

## 6. Acceptance criteria

- **AC1** — When a fixture kit's render discharges its hole and its `[check]` then goes green to
  red, `update --write` rolls it back and prints `is undischarged` for the hole, never
  `is discharged after the render`. Red when: the verdict prints before the rollback, which
  `bac1a4fb` does.
- **AC2** — When `render_hole_verdict` is called with `no-launch`, `discharged` and `undischarged`,
  each returns its own line, `neither verdict is confirmed` for the first. Red when: a verdict maps
  to another's line.
- **AC3** — When the rollback fixture, a `GOVKIT_RERENDER=0` run and a render that deletes its file
  each reach the re-measure step, each prints its own `KEPT` reason and leaves the row unchanged.
  Red when: a guard is dropped and the row is re-stamped.
- **AC4** — When the re-measure fixture's `version_from` file changes between its vintages, the
  re-measured row's `version` names the new value. Red when: the `version` re-stamp is deleted.
- **AC5** — When a regenerate is refused beside a hole its probe still fails, the run prints both
  `exited 5` and the hole's `is undischarged` line. Red when: the re-probe moves inside the
  accepted branch.
- **AC6** — When the `[aHI-1]` fixture updates, its arm finds `probes undischarged before the
  render (probe exit 3)` before the `ran` line. Red when: the early probe is removed.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `memory hygiene`

New arm: `tools/govkit/selftest.py` · covers AC1 AC3 AC4 AC5 AC6 · fixtures that roll back, decline, delete, version and refuse · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's mediums and lows (round 1).

## 10. Reuse audit

No existing seam fits beyond the build's own: the re-measure step after the verify pass, which
`DEPL-dRemeasuredRender-1` placed there for the reason S1 now applies to the hole, and the self-test's
`check_update_safety` fixtures, `kit_rb` among them. The recall query returned
`DEPL-aRepatriatedFork-17`, the unit that made the rollback restore what the regenerate rendered.

Recall terms used: hole discharge probe regenerate rendered row install.sums sha256 oid re-rendered CAP adopter update

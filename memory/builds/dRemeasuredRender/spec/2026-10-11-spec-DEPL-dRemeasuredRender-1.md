# DEPL-dRemeasuredRender-1 — `govkit update` re-measures a rendered row's receipt from the bytes its render landed

**Status:** CLOSED · rev-2 · 2026-10-11 · node d · Tier-2 · base 9a8777b8 · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-DEPL-dRemeasuredRender-1-1-acceptance-ledger.md](../build/2026-10-11-build-DEPL-dRemeasuredRender-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-DEPL-dRemeasuredRender-1-1-build-brief.md](../prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-1-1-build-brief.md) | journal | — |
| [2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md](../prompts/2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md) | research | TOOL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 |
| [2026-10-11-review-TOOL-dRemeasuredRender-1-closing-diff-round1.md](../reviews/2026-10-11-review-TOOL-dRemeasuredRender-1-closing-diff-round1.md) | diff-review | TOOL-dRemeasuredRender-1 DEPL-dRemeasuredRender-2 |

<!-- /gen:spec-records -->

## 1. Goal

`update` caps a `rendered` row's verdict at `re-rendered` and then runs the kit's `[[regenerate]]`
argv, which rewrites the file. The row's `sha256`, `oid`, `commit` and `version`, and its
`install.sums` line, keep the pre-pull bytes, because only rows `update` writes itself are stamped
from the bytes that landed. Re-measure each rendered row after its render, so the receipt names what
the target holds.

## 2. Scope (IN)

- **S1** — On `--write`, after the verify pass's rollbacks and the renormalize, every receipt row
  with `role == "rendered"` whose kit's declared regenerate argvs all ran and were accepted, and
  whose kit was not rolled back, is re-measured from its file on disk: `sha256` is the hash of the
  raw bytes, `oid` the blob the target's own clean filter makes of them (`git hash-object
  --path`), and `commit` and `version` the vintage this run rendered from, as written rows take
  them. `gov_oid` becomes gov's blob of the row's `source` at that commit, so it stays gov's.
  Observed by AC1, AC2.
- **S2** — A rendered row of a touched kit that is NOT re-measured keeps its record, and the run
  says so per row with the reason: its render did not run, its render refused, its kit was rolled
  back, or its file is absent. Observed by AC3.
- **S3** — One count line, printed on every `--write` that touched a kit, zeros included:
  `govkit update — rendered receipts: <n> re-measured · <m> kept`. Observed by AC1, AC3.
- **S4** — `install.sums` follows the re-measured rows, because both arms that write the receipt
  derive the sidecar from its rows. NOT OBSERVED — beyond AC1's sums assertion, which observes it.

## 3. Non-goals (OUT)

- `apply` and `adopt --re-adopt`, which record rendered rows by their own rules.
- Staging the render. Whether the regenerate stages its output stays the kit's business; `oid` names
  the blob the landed bytes make, staged or not.
- A rendered row of a kit this run did not touch: its render did not run and nothing changed it.

### Edges

- **hands-off** `DEPL-dRemeasuredRender-2` — the hole re-probe, sequenced after this unit because
  both write `tools/govkit/govkit.py` and its self-test.
- **hands-off** `DEPL-dRemeasuredRender-3` — the accepted no-render outcome this unit's re-measure
  stamped, promoted from the closing review's HIGH.
- **hands-off** external — nc and inCMS stop re-recording rendered rows by hand at their next pull.

## 4. Design

### Evidence

Read at base `9a8777b8`. The capping line is `v = "re-rendered"` in `_cmd_update`'s row loop; the
regenerate loop records accepted argvs in `_rr_ran` and refusals only as an `r.fail`; rolled-back
kits are `_rolled_kits`; both receipt writers derive `install.sums` from `receipt["files"]`. Measured
at inCMS, read-only: `.claude/skills/lexicon/SKILL.md`'s row records sha256 `6b008068…` and oid
`9dafc0ad…`, while the file hashes `2b09f41f…` and its index blob is `a0af86af…`.

### Inventory

- `_rr_refused` — a set of kit ids in `_cmd_update`, filled where a regenerate argv is refused.
- `measure_rendered_rows` — a function: given the target, the receipt rows of one kit and the
  vintage, it re-measures each rendered row and returns the rows it kept with their reasons.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **Read the index entry for `oid`.** Rejected: the regenerate may leave its output unstaged, and
  the index entry then names the pre-render blob, which is the defect itself.
- **Re-measure inside the regenerate loop.** Rejected: the verify pass after it can roll the kit's
  renders back, and a row stamped before the rollback names bytes the target no longer holds.

## 5. Production-readiness checklist

- security — N/A — reads files under the target `update` already writes; no new write path.
- perf / scale — one `git hash-object` per rendered row of a touched kit; ~20 at an adopter.
- error / empty / loading states — an absent file or a failed hash keeps the row and says why.
- observability — one line per row and one count line, zeros included.
- risks — a re-measured row advances `commit`, so the next run grades its template from this vintage.
- testing — a self-test fixture adopter with one rendered row, observed RED at base.
- migration — none: the next `update --write` re-measures every stale rendered row.
- user docs — the runbook's `update` paragraph in `WIRE-INTO-PROJECT.md` names the re-measure.

## 6. Acceptance criteria

- **AC1** — When `govkit update --write` runs over a fixture adopter whose kit renders one row and
  whose template changed, the row's `sha256` and `oid` in the receipt `install.json` and its
  `install.sums` line name the rendered file's bytes, and the run prints `rendered receipts: 1
  re-measured`. Red when: the row keeps its pre-render values, which base does.
- **AC2** — When `govkit check` runs over that fixture after the update, it exits 0. Red when: the
  sums and the receipt disagree.
- **AC3** — When the fixture's regenerate argv refuses, `update --write` keeps the row's record and
  prints a `KEPT` line naming the refusal. Red when: a refused render's row is re-measured.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: `tools/govkit/selftest.py` · covers AC1 AC2 AC3 · a fixture kit whose regenerate renders one row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the owner's prompt.
- rev-2 · 2026-10-11 · §3 · the hands-off edge to `DEPL-dRemeasuredRender-3`, which the closing
  review promoted out of this unit's re-measure.

## 10. Reuse audit

The seam is `_cmd_update`'s written-row stamping rule (`sha256` from the bytes that landed, `commit`
and `version` from `_resolve_ver_at`) and its regenerate snapshot, `_rg_snap`, which already names
each kit whose argv ran. `reuse_lookup.py` with "re-measure an install row's receipt after a
regenerate rewrites the file" returned no govkit seam, so no existing seam fits a re-measure, and the
function is new. The recall query returned `TOOL-bQuiltedLantern-1` and `DEPL-aRepatriatedFork-17`,
the regenerate declaration and its rollback.

Recall terms used: hole discharge probe regenerate rendered row install.sums sha256 oid re-rendered CAP adopter update

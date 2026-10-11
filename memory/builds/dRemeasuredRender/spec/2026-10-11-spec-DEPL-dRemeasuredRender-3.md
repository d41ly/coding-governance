# DEPL-dRemeasuredRender-3 — a render that stopped at an accepted outcome without rendering keeps its receipt

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node d · Tier-2 · base 9a8777b8 · streams deployer · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's one HIGH (round 1, id 4). `DEPL-dRemeasuredRender-1` re-measures
a rendered row whenever its kit's regenerate was not refused. But four shipped outcomes accept a
NON-ZERO exit that renders nothing: memory-tree `seed-and-stop` and `not-rendered-here`, lexicon
`no-project-layer` and codebase-map `seeded-conf`. Such a run stamped untouched bytes at `to_commit`,
a receipt certifying a render that never happened. Keep those rows, and say why.

## 2. Scope (IN)

- **S1** — A kit any of whose regenerate argvs exits non-zero, whether refused or accepted through a
  declared outcome, is recorded as not having rendered, beside `_rr_refused`. A kit whose argvs all
  exit 0 rendered. Observed by AC1.
- **S2** — Its rendered rows take the KEPT path with the reason
  `its render stopped at accepted outcome '<means>' without rendering`, and their record is
  untouched. Observed by AC1.
- **S3** — A refused argv keeps its existing reason, `its render was refused`, which wins over S2's
  when one kit has both. Observed by AC2.

## 3. Non-goals (OUT)

- A new `renders =` key on `[[outcome]]`: the exit code already separates the two populations in
  every shipped descriptor, so a schema key would be a second answer to one question.
- The minors the same review confirmed: `DEPL-dRemeasuredRender-4`.

### Edges

- **consumes-from** `DEPL-dRemeasuredRender-1` — the re-measure step and its KEPT path this unit
  narrows.
- **hands-off** `DEPL-dRemeasuredRender-4` — the remaining KEPT reasons' arms, sequenced after this
  unit because both write `tools/govkit/govkit.py` and `tools/govkit/selftest.py`.

## 4. Design

### Evidence

Read at `bac1a4fb`. In the regenerate loop `_rg_snap[_eid]` is set before any argv runs, and
`_rr_refused` is filled only when `_bad` is true. `outcome_accepted` returns True for a non-zero exit
whose matched outcome declares `ok`. memory-tree's descriptor records exit 3 `not-rendered-here` as
measured at an adopter holding hand-authored docs.

### Inventory

- `_rr_norender` — a dict in `_cmd_update`, kit id to the first accepted non-zero outcome's `means`.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Declare `renders = true|false` on every `ok` outcome.** Rejected: every shipped `ok` outcome
  with a non-zero exit is a stop, and every exit 0 is a render, so the key would restate the exit
  code, and a kit author could set it false over a real render.

## 5. Production-readiness checklist

- security — N/A — narrows which rows are re-stamped; no new write.
- perf / scale — none.
- error / empty / loading states — an accepted outcome with no `means` is named `(unnamed)`.
- observability — one KEPT line per row, naming the outcome.
- risks — none: the narrowed rows keep the record they had before `DEPL-dRemeasuredRender-1`.
- testing — one self-test arm, observed red against `bac1a4fb`.
- migration — none.
- user docs — the runbook's sentence on KEPT rows gains the accepted-stop reason.

## 6. Acceptance criteria

- **AC1** — When `govkit update --write` runs a fixture regenerate that exits 3 through a declared
  `ok = true` outcome without touching the rendered file, the row keeps its record and the run prints
  `stopped at accepted outcome`. Red when: the row is re-stamped at the new vintage, which
  `bac1a4fb` does.
- **AC2** — When the fixture's regenerate exits 5 with no outcome accepting it, the KEPT line still
  reads `its render was refused`. Red when: the accepted-stop reason replaces it.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: `tools/govkit/selftest.py` · covers AC1 · a fixture regenerate exiting 3 through an `ok = true` outcome · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's HIGH (round 1, id 4).

## 10. Reuse audit

The seam is `DEPL-dRemeasuredRender-1`'s KEPT path and `classify_outcome`, whose `means` the run
already prints on the `ran` line; no existing seam fits a new key, and none is added. The recall
query returned `DEPL-dRetiredFork-5`, which taught `check` that an accepted non-zero exit is not a
failure, the same exit this unit now reads as not a render.

Recall terms used: hole discharge probe regenerate rendered row install.sums sha256 oid re-rendered CAP adopter update

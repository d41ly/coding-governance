---
slug: dSkippedRecord
node: d
opened: 2026-11-20
streams: tooling
roster: TOOL
ids: TOOL-dSkippedRecord-1 TOOL-dSkippedRecord-2
---

# dSkippedRecord — the close's run-record commit is made only when staging left a diff

## The problem this build exists to solve

`write_run_record` in `tools/unattended/unattended.sh` stages the re-rendered run record and the
index paths its render moved, then, under `in-place` after `--close`, commits with nothing checking
that the stage holds a diff. A record re-rendered byte-identical stages nothing, the commit fails,
and the close prints "its commit failed" over git's own output. dSettledStage's stage-commit scan
found the site and registered it in `memory/project/stage-commit-sites.txt` as this follow-up. The
prompt is recorded verbatim under `prompts/`.

## Expected improvements

- A close whose run record is unchanged skips the commit with one line, and HEAD stays put.
- A stage or staged-diff test that fails refuses with one line, and no commit is attempted.
- The stage-commit leg reads `tools/unattended/unattended.sh` admitted, its registry row drained.

## Detriments if this is not built

- Every re-run close over an unchanged record prints a false commit failure.
- The registry keeps a true instance the gate cannot see past.

## Build-level rules

- Classified at kickoff (M2): one unit, MISSING. Tier-2, a shipped-kit edit.
- No spec audit: the owner answered "No audit" at kickoff (2026-11-19).
- Units run no gates. The RED-first observation of each new arm is the main loop's, at the close.
- No unattended `--selftests` without the owner's ask; landing on the owner's ask, through
  `bash tools/push-main.sh` from the primary tree.

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSkippedRecord-1` | 2 | `write_run_record` answers its stage 0, 1 or 2 the way `write_staged_change` does, skips the commit on 1 and refuses on 2, with an empty-stage and a failed-stage arm, and drains its registry row |
| 2 | `TOOL-dSkippedRecord-2` | 2 | the closing review's two LOW items, promoted: the `same` arm reads the skip line's commit hash, and the as-built failed-stage mechanism, a PATH `git` shim, recorded against unit 1's frozen spec |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node d · opened 2026-11-20 · streams tooling
ids TOOL-dSkippedRecord-1 TOOL-dSkippedRecord-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSkippedRecord-1 — the close's run-record commit is made only when staging left a diff](spec/2026-11-20-spec-TOOL-dSkippedRecord-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-20 |
| [TOOL-dSkippedRecord-2 — the `same` arm reads the skip line's commit hash, and the failed-stage modes are recorded as built](spec/2026-11-20-spec-TOOL-dSkippedRecord-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-20 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSkippedRecord-1 TOOL-dSkippedRecord-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSkippedRecord-1` | no |
| 2 | `TOOL-dSkippedRecord-2` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-20-prompt-TOOL-dSkippedRecord-2-promotion-brief.md`, `2026-11-20-prompt-TOOL-dSkippedRecord-2-pass-legs-fix.md` and 2 more under prompts/ |
| reviews | `2026-11-20-review-TOOL-dSkippedRecord-1-closing-diff-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-5.md`, `2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-4.md` and 3 more under build/ |
| logs | `2026-11-20-build-TOOL-dSkippedRecord-2-1-acceptance-ledger.md`, `2026-11-20-build-TOOL-dSkippedRecord-1-agent-ledger.md` and 1 more under build/ |
| card ref | `refs/gov/builds/dSkippedRecord/card` |
<!-- /gen:build-routes -->

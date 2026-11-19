---
slug: dSkippedRecord
node: d
opened: 2026-11-20
streams: tooling
roster: TOOL
ids: TOOL-dSkippedRecord-1
status: OPEN
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-11-20 · streams tooling
ids TOOL-dSkippedRecord-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

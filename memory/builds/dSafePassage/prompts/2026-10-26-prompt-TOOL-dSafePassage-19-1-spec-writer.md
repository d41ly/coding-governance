**Serves:** research TOOL-dSafePassage-19

# Brief: TOOL-dSafePassage-19's AC2 compares what a killed rollback's re-run can reproduce

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-19 back as a DIVERGENCE before writing code (`wf_7efb05c8-043`), and the run revises the spec under M2.

## The brief

### Goal

AC2 and S4's convergence claim observe what the re-run after a kill past the schema step's down actually reproduces — the receipt bytes, the target bytes and the record's finished shape, with the re-run's down lines reading `skipped (nothing applied)` — so the unit is buildable without amending the closed TOOL-dSafePassage-4 and -18.

**The defect.** AC2 requires the re-run's record bytes, times aside, to equal AC1's. Under S4 the re-run witness-probes every reverse row recorded nowhere and skips each whose witness fails. After the kill both rows are in that state: fx/s1's `rolled-back` row was recorded at schema 4 and then removed with `steps` by the schema step's down, and its witness (`s1.txt`) was deleted by its own down; the schema step's down already ran, so its witness fails too. `run_reverse_walk` (`tools/govkit/upgrade_steps.py` ~:1141) records each as `(id, "skipped (nothing applied)")` and `write_rollback_record` (S3, ~:1177) prints `down <id>: skipped (nothing applied)`, where AC1 prints `rolled-back`. The killed run's record was begun `not finished` with no down lines and is rewritten only at the finish, so no verdict survives the kill.

**The direction.** Option (a): AC2 (and S4's "converging to the bytes of an uninterrupted run") compare the receipt bytes, the target bytes, and the record's finished shape — its `files:` line, `gov_commit: moved to <to8>`, no `not finished` — and require the re-run's down lines to read `skipped (nothing applied)` for both rows, with one sentence saying why (their rows went with `steps` and their witnesses no longer hold). Option (b), carrying the killed run's verdicts forward by rewriting the record after each down, amends TOOL-dSafePassage-4 S6 and TOOL-dSafePassage-18, both CLOSED, and is not taken. Also check the brief's carried `carry` flag: if AC2's receipt comparison meets TOOL-dSafePassage-15's `carry` difference (DEPL-dCarriedReceipt-9 S2), exclude `carry` the way TOOL-dSafePassage-15 rev-2's AC4 does; the builder read that the kill lands before the write loop, so it probably does not.

### Items

1. **Revise TOOL-dSafePassage-19** as a rev bump dated 2026-10-26, still `DEFERRED`: AC2, its Red-when and S4's convergence sentence as above; one §9 line names this brief.
2. **Cross-read** TOOL-dSafePassage-4 and -18 (CLOSED: read-only, confirm nothing there now contradicts the revised AC2) and TOOL-dSafePassage-5 (its rollback-from-killed-state case) on M2's axes; a disagreement in a DEFERRED spec is fixed there with a rev bump and §9 line, one in a CLOSED spec is reported, not edited.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- AC2 names the three compared things, the two `skipped (nothing applied)` lines and why.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index, which the main loop re-renders.
- `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-19 READY.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no edit of a CLOSED spec.
- No commit, no stage into the real index, no deviation record.

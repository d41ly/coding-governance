**Serves:** journal TOOL-dSafePassage-70

# TOOL-dSafePassage-70 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/upgrade_steps.py`: `run_reverse_walk` reads
`held = test_steps_recordable(receipt)` before move 3, writes the `down interrupted:` mark only where
`held`, and fires `LOWERED_STOP` only where `held` and the re-read after the down reads false, the
docstring and the module's reverse-walk paragraph saying so (S1). `build_update_gov` gains
`down_exit`; the `rollback-update` family gains `schema-step-kill-shipped-rows`, a member of
`ROLLBACK_UPDATE_SCHEMA_PLANTS`, sharing the `schema-step-kill-before-stamp` branch with its own
down-line and record expectations and a count of `fx/s2`'s and `fx/s1`'s downs on `t` (S2).
`tools/govkit/selftest.py`: a `[dSP-70]` row of `check_step_rollback` (the §7 arm).
`help/upgrade-steps.md`: the new bullet, the "What runs" clause and the fixture line (S3).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each probe ran on node d
(Windows), from the worktree root.

**Evidences:** TOOL-dSafePassage-70
- AC1 — `python tools/govkit/upgrade_steps.py fixture rollback-update --plant schema-step-kill-shipped-rows` exited 0 in 28 s with no `rollback-update: FAILED` line, printing `the re-run exits 0 · its receipt's bytes equal the twin's · the target's bytes equal the twin's · the record has the twin's finished shape`, the re-run record `down fx/s2: rolled-back`, `down fx/s1: rolled-back`, `down govkit/receipt-schema-4: skipped (nothing applied)` where the twin's reads `rolled-back`, `the re-run's record equals the twin's line for line except started and the schema step`, and `on t fx/s2's down ran 2 time(s) · fx/s1's down ran 2 time(s)`. Red, both staged in scratch copies of `tools/govkit`, `tools/process-monitor` and `tools/lib`: move 3's `held` guard taken out, the re-run exited 2 with `govkit: a receipt at schema 3 has no `steps` to record 'fx/s2' in` and the fixture exited 1 with three `FAILED` lines; `LOWERED_STOP` unkeyed from `held`, the re-run stopped at `step fx/s2 · STOPPED · receipt below schema 4 before the last down` and the fixture exited 1. An ast probe of the new `check_step_rollback` row's four needles found all four in the green log and none in either red log.
- AC2 — `python tools/govkit/upgrade_steps.py fixture rollback --plant schema-step-early` exited 1 printing `step fx/s2 · STOPPED · receipt below schema 4 before the last down` and `rollback: 3 reached · stopped at fx/s2`, with no `step fx/s1` down line. `fixture rollback --plant schema-step` and `--plant schema-step-kill` exited 0, and `fixture rollback-update --plant schema-step-kill-before-stamp` and `--plant schema-step` exited 0 with no `FAILED` line.
- AC3 — `git grep -n -F "After a kill past the schema step" -- help/upgrade-steps.md` printed line 259, and `git grep -n -F "fixture rollback-update --plant schema-step-kill-shipped-rows" -- help/upgrade-steps.md` line 285.

Owed at the close: the `New arm:` line of the spec's §7 — the `[dSP-70]` row of `check_step_rollback`
red with move 3's `held` guard taken out of a working copy and green restored, through `govkit
selftest` — and the spec's §7 gates. `ast.parse` over the two edited Python files passed.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_rollback` row `schema-step-kill-shipped-rows`), the break was move 3's `if held:` guard made `if True:`: `FAIL [dSP-70] fixture rollback-update schema-step-kill-shipped-rows exits 0 …`, where the fixture prints `rollback-update: FAILED · fx/s2's and fx/s1's downs did not each run twice on t`. Restored, GREEN: 1 of 1 `ok`.

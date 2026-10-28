**Serves:** journal TOOL-dSafePassage-18

# TOOL-dSafePassage-18 — acceptance ledger

The unit as built, at spec rev-2. In `tools/govkit/upgrade_steps.py`: `run_reverse_walk` asks
`test_steps_recordable` once after each down's spawn and re-read, and where it does not hold makes
no `set_step_state` call for that row on any of the three records after the down (S1); the row's
verdict still reads `rolled-back` in the returned `downs`, the verdict list `write_rollback_record`
prints (S2); a lowered receipt before the last row stops the walk naming the row with
`LOWERED_STOP`, `receipt below schema 4 before the last down` (S3). The stop text is one module
constant beside `NOT_RECORDED_SUFFIX`, read by the walk and the fixture. The `rollback` family gains
the plants `schema-step`, `schema-step-kill` and `schema-step-early` (`ROLLBACK_SCHEMA_PLANTS`),
each over `build_walk_gov`'s copied schema step and a schema-3 target; the fixture step `fx.py`
gains `<slug>.down-lowers`, a down that then sets the receipt to schema 3 and takes `steps` out, and
the reverse child prints `rollback: verdicts <the list>`. `tools/govkit/selftest.py`'s
`check_step_rollback` gains the three plants' rows, labelled `[dSP-18]`: the `New arm:` line's arm.
`run_reverse_walk` keeps returning its dict; its `downs` entry is the verdict list S2 names.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture rollback --plant <case>` on node d (Windows,
Python 3.14); its repositories sit under `%TEMP%`. Reds were staged in a scratch copy of
`tools/govkit` with the predicate's answer replaced by `recordable = True`, the walk recording every
row whatever the predicate reads, and the fixture run from the copy. The plants `(base)`,
`down-fails`, `witness-stays` and `callers` of the same family, and `fixture walk --plant
schema-3`, re-ran with no `FAILED` line.

Owed at the close: `govkit selftest` (with `check_step_rollback`'s three `[dSP-18]` rows and their
RED-first observation, staged by the walk copy above), `govkit refusal join`, `govkit acceptance
matrix`, `govkit selfcheck`, `recall floor arms`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-18
- AC1 — `fixture rollback --plant schema-step`, rc 0: `step fx/s4` to `fx/s1 · rolled-back`, then `step govkit/receipt-schema-4 · rolled-back`, `rollback: verdicts [... ('govkit/receipt-schema-4', 'rolled-back')]`, `rollback: the receipt reads schema 3 without steps · last verdict ('govkit/receipt-schema-4', 'rolled-back')`. Red staged: `Refusal: a receipt at schema 3 has no steps to record 'govkit/receipt-schema-4' in`, rc 1, two `rollback: FAILED` lines.
- AC2 — `fixture rollback --plant schema-step-kill`, rc 0: `rollback: after the kill · the receipt reads schema 4 whole` (the schema step's row carrying its `down interrupted:` failure), the re-run `rollback: verdicts [('govkit/receipt-schema-4', 'rolled-back')]` and `the receipt reads schema 3 without steps`, then `rollback: the re-run's receipt equals an uninterrupted rollback's`. Red staged: the re-run and the uninterrupted run both raised `Refusal`, rc 1, `rollback: FAILED`.
- AC3 — `fixture rollback --plant schema-step-early`, rc 1: `step fx/s4 · rolled-back`, `step fx/s3 · rolled-back`, `step fx/s2 · STOPPED · receipt below schema 4 before the last down`, `rollback: 3 reached · stopped at fx/s2`, no `s1.down`, no traceback. Red staged: `Refusal: ... to record 'fx/s2' in`, `rollback: FAILED · the reverse walk did not stop at fx/s2 naming ...`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_rollback`, cut to `schema-step` and `schema-step-early`. Break: `run_reverse_walk` sets `recordable = True`. RED: `FAIL [dSP-18] fixture rollback schema-step exits 0 and names step fx/s1 · rolled-back` with `rollback: FAILED · the receipt is not schema 3 without `steps`, …`. Also `FAIL [dSP-18] fixture rollback schema-step-early exits 1 …` with `rollback: FAILED · the reverse walk did not stop at fx/s2 naming `receipt below schema 4 before the last down``. GREEN restored: FAILURES=0, 21 ok.

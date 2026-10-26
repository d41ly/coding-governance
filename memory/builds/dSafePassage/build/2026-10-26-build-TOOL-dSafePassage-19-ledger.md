**Serves:** journal TOOL-dSafePassage-19

# TOOL-dSafePassage-19 — acceptance ledger

The unit as built, at spec rev-4. S1 to S3 hold at HEAD (`run_step_reread`'s pop, the rollback
stamp, `write_rollback_record`), so no product code moved. In `tools/govkit/upgrade_steps.py`: the
`rollback-update` family gains the plants `schema-step` and `schema-step-kill-before-stamp`
(`ROLLBACK_UPDATE_SCHEMA_PLANTS`), built over `build_update_gov(..., schema3=True)`, the kill plant
installing the twin targets `t` and `t2` from one scratch gov; `FIXTURE_SCHEMA_STEP_PLANTS`'s
`os.replace` entry gains the `schema.block-after` trigger, which blocks the schema step after its
rename. `tools/govkit/selftest.py`'s `check_step_rollback` gains the two rows, tagged `[dSP-19]`:
the `New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture rollback-update --plant <case>` on node d
(Windows, Python 3.14); its repositories sit under `%TEMP%`. The reds were staged as §7 names: a
scratch copy of `tools/govkit` (with `tools/process-monitor`) whose `run_step_reread` keeps a key
the disk dropped (`receipt.pop(k, None)` replaced by `pass`), the fixture run from the copy. The
`[dSP-19]` rows' needles were matched against the green logs by a probe; the rows themselves run
only inside `govkit selftest`.

Owed at the close: `govkit selftest` (with `check_step_rollback`'s two `[dSP-19]` rows and their
RED-first observation, staged by the re-read break above), `govkit refusal join`, `govkit acceptance
matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture`, `spec tokens`.

**Evidences:** TOOL-dSafePassage-19
- AC1 — `fixture rollback-update --plant schema-step`, rc 0: `rollback-update: t exits 0 · schema 3 · no steps · gov_commit A`, `record · down fx/s1: rolled-back`, `record · down govkit/receipt-schema-4: rolled-back`, `record · files: wrote 1 · moved 0 · deleted 0 · withheld 0 · conflicts 0`, `record · gov_commit: moved to <to8>`, the `started … · finished …` line. Red staged: `t exits 0 · schema 3 · WITH steps · gov_commit A`, `rollback-update: FAILED · the rollback did not exit 0 with schema 3, no `steps` and gov_commit A`, rc 1.
- AC2 — `fixture rollback-update --plant schema-step-kill-before-stamp`, rc 0: the twin `t2 exits 0 · schema 3 · no steps · gov_commit A`; `after the kill · schema 3 · no steps · gov_commit B · record not finished with 0 down line(s)`; `the re-run exits 0 · its receipt's bytes equal the twin's · the target's bytes equal the twin's · the record has the twin's finished shape`; `re-run record · down fx/s1: skipped (nothing applied)` then `down govkit/receipt-schema-4: skipped (nothing applied)`, `gov_commit: moved to <to8>`. `carry` compared within the receipt bytes, no exclusion. Red staged: `the re-run exits 0 · its receipt's bytes DIFFER from the twin's · the target's bytes DIFFER from the twin's: ['.governance/install.json']`, two `rollback-update: FAILED` lines, rc 1.

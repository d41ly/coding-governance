**Serves:** journal TOOL-dSafePassage-40

# TOOL-dSafePassage-40 — acceptance ledger

The unit as built, at spec rev-2. `tools/govkit/upgrade_steps.py`: `run_step_walk` reads the
receipt it was handed into `began` before its first write, and move 1 passes `via="witness"` only
where `began` holds no record of the row and `derive_image_path` finds no before-image (S1). The
fixture step `fx.py` blocks a witness that holds on `<slug>.witness-block`, so a walk dies after the
up returned and before move 5 records it; the `walk` family gains `kill-after-up` (S2), the
`rollback` family `kill-after-up-image-lost` (S3), sharing `image-lost`'s verdict branch.
`help/upgrade-steps.md` states when the mark is set (S4). `tools/govkit/selftest.py` gains a row for
each plant. `tools/govkit/upgrade_walk.py`'s `kill` case expects the mark only under the same rule,
the consequence TOOL-dSafePassage-5's §5 risks line handed to this pass.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. The fixture families ran
through their own CLI on node d (Windows). The red cases ran the same CLI and probe from a scratch
copy of `tools/govkit/` whose move 1 passes `via="witness"` unconditionally, the pre-unit rule.

**Evidences:** TOOL-dSafePassage-40
- AC1 — `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant kill-after-up` exit 0, printing `walk: after the kill · last applied ['fx/s2'] · fx/s3 failed · interrupted: started <utc>, no exit recorded`, `walk: after the kill · s3.txt and its image present`, the re-run's `step fx/s3 · skipped (witness holds)` and `walk: the re-run · fx/s3 applied · via None`; `fixture walk --plant witness-holds` exit 0, printing `walk: fx/s2 up canary absent · row applied · via witness`. Red from the scratch copy, rc 1: `walk: the re-run · fx/s3 applied · via witness` and `walk: FAILED · s3, whose up ran before the kill, is marked applied via its witness`.
- AC2 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant kill-after-up-image-lost` exit 1, printing `rollback: the re-run · fx/s3 applied · via None · image present before the plant deletes it`, `step fx/s4 · rolled-back`, `step fx/s3 · STOPPED · witness still holds after down; before-image .governance/steps/fx/s3.before.json absent` and `rollback: fx/s3 (...) · s3.txt in place`, no `rollback: FAILED`. Red from the scratch copy: `step fx/s3 · rolled-back` with `s3.txt in place`, four `rollback: FAILED` lines.
- AC3 — a scratch probe imported `tools/govkit/upgrade_steps.py`, built the walk family's gov and three schema-4 targets with `s2.txt` present (s2's witness holds), and called `run_step_walk` over s2's pending row: a `failed` record and no image printed `AC3 t2: applied via None`; no record and an image present printed `AC3 t3: applied via None`; neither printed `AC3 t4: applied via witness`. The scratch copy printed `via witness` for all three. `fixture walk --plant kill-after-up` repeats the first two as `walk: failed record, no image · fx/s2 applied · via None` and `walk: no record, image present · fx/s2 applied · via None`.
- AC4 — `git grep -n -e "via" -e "no record" -- help/upgrade-steps.md` prints line 117, `carries "via": "witness", set only when the receipt held no record`, and lines 151 to 153 under "The skip", `only where the receipt held no record of it and no before-image of it exists`.

Owed at the close: the new arm in `tools/govkit/selftest.py` (the `[dSP-40]` rows `fixture walk
kill-after-up` and `fixture rollback kill-after-up-image-lost`) red on its staged break, a move-1
copy that marks every row whose witness holds, and green restored; the spec's §7 gates; and
`python tools/govkit/upgrade_walk.py --case kill --step <the floor step's id>`, the leg whose
expectation this pass moved, which no pass may run.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_walk` row `kill-after-up` and `check_step_rollback` row `kill-after-up-image-lost`), the break was a move-1 copy that marks every row whose witness holds (`fresh = True`): `FAIL [dSP-40] fixture walk kill-after-up exits 0 …`, where the fixture prints `walk: FAILED · s3, whose up ran before the kill, is marked applied via its witness`, and `FAIL [dSP-40] fixture rollback kill-after-up-image-lost exits 1 …` (both rows). Restored, GREEN: 1 of 1 `ok` each.

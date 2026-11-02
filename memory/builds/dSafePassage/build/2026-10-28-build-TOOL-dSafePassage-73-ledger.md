**Serves:** journal TOOL-dSafePassage-73

# TOOL-dSafePassage-73 — acceptance ledger

The unit as built, at spec rev-4. Product writes: `tools/govkit/upgrade_steps.py` (S1's
`test_up_unrecorded` beside `derive_down_verdict`; S2's move 1 of `run_step_walk` and S3's move 3 of
`run_reverse_walk` asking it; S4's docstrings; S5's `witness-only-reup` plant in `ROLLBACK_PLANTS`
and `run_rollback_fixture`), `tools/govkit/selftest.py` (the `witness-only-reup` row of
`check_step_rollback`'s table and the `[dSP-73]` predicate check beside the in-process verdict
table) and `help/upgrade-steps.md` (S4's two passages). `memory/map/generated/symbols.json`
regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree by the probe the spec names, run directly from the repository root.

Owed at the close: both `New arm:` lines' RED-first observations (the `witness-only-reup` row and
the `[dSP-73]` predicate check in `tools/govkit/selftest.py`), and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-73
- AC1 — the spec's `python -c` probe — printed `[True, False, True, False, False, False, False, False]`.
- AC2 — `git grep -n "test_up_unrecorded(" -- tools/govkit/upgrade_steps.py` — printed the `def` line and one call each in `run_step_walk` and `run_reverse_walk`; `git grep -n "row.id not in began"` printed nothing.
- AC3 — `python tools/govkit/upgrade_steps.py fixture rollback --plant witness-only-reup` — exit 0, printing `rollback: fx/s2 recorded via witness after a rollback`, the second reverse walk's `step fx/s4 · rolled-back` to `step fx/s1 · rolled-back` with `rollback: 4 reached · stopped at none`, and `rollback: the target's bytes equal their bytes before the walk`.
- AC4 — `--plant rolled-back-witness-holds` and `--plant unrecorded-witness-down-killed` — each exit 0, the first ending on the bytes-equal line, the second on `rollback: the re-run · fx/s2 rolled-back · bytes equal their bytes before the walk`.
- AC5 — `grep -c "or a \`rolled-back\` one" help/upgrade-steps.md` — printed `2`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `b634d60e5` (batch d, `2026-10-29-prompt-TOOL-dSafePassage-72-close-arms-d-researcher.md`), each break staged alone and restored. tools/govkit/upgrade_steps.py `witness-only-reup` (check_step_rollback cut to that plant), with move 1's `fresh` set back to `began.get(row.id) is None and not image`: `FAIL [dSP-73] fixture rollback witness-only-reup exits 0 and names rollback: fx/s2 recorded via witness after a rollback`. tools/govkit/selftest.py `[dSP-73]` table, with `test_up_unrecorded` set back to `state is None and not image_present`: `FAIL [dSP-73] test_up_unrecorded reads no record or rolled-back, with no image, as no up on record`. GREEN restored: `FAILURES 0`, both `[dSP-73]` arms `ok`.

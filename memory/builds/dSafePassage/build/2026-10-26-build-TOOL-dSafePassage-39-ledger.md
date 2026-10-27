**Serves:** journal TOOL-dSafePassage-39

# TOOL-dSafePassage-39 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py`: `set_step_state` called with no
`via` copies the old row's mark when the old row and the new state are both `applied` (S1); the
reverse walk's move 3 passes `via="witness"` for a row recorded nowhere with no before-image (S3);
the fixture step `fx.py` blocks in its down on `<slug>.down-block`; the `rollback` family gains the
plants `witness-only-down-killed` and `unrecorded-witness-down-killed` (`DOWN_KILLED_PLANTS`).
`tools/govkit/selftest.py`'s `check_step_rollback` gains the two plant rows and the writer probe.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. The fixture family was run
by its own CLI on node d (Windows); the red cases ran the same CLI from two scratch copies of
`tools/govkit/`, one with the carry line replaced by `pass`, one with move 3's mark argument
replaced by `None`.

**Evidences:** TOOL-dSafePassage-39
- AC1 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-only-down-killed` exit 0, printing `rollback: after the kill · fx/s2 applied · via witness · down interrupted`, then the re-run's `step fx/s2 · rolled-back`, `step fx/s1 · rolled-back` and `rollback: the re-run · fx/s2 rolled-back · bytes equal their bytes before the walk`. Red with the carry removed, rc 1: `after the kill · fx/s2 applied · via None`, then `step fx/s2 · STOPPED · witness still holds after down; before-image .governance/steps/fx/s2.before.json absent` and four `rollback: FAILED` lines.
- AC2 — a `python -c` probe loading `tools/govkit/upgrade_steps.py` by path called `set_step_state` on a schema-4 receipt whose row is `applied` with `via` `witness`: state `applied` with no failure and with `down interrupted: x` each printed `via witness`; state `failed` (`exit 1: x`) and `rolled-back` each printed `via None`; an unmarked `applied` row stayed unmarked.
- AC3 — `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant unrecorded-witness-down-killed` exit 0, printing `rollback: after the kill · fx/s2 applied · via witness · down interrupted` over a receipt with s2's row taken out and no image, then the re-run's `step fx/s2 · rolled-back` and `rollback: 2 reached · stopped at none`. Red with move 3's mark removed, rc 1: `after the kill · fx/s2 applied · via None` and the re-run `STOPPED · witness still holds after down; before-image ... absent`. The carry-only break leaves this plant green, as S3 alone writes the mark here.

Owed at the close: the new arm in `tools/govkit/selftest.py` (`check_step_rollback`'s two
`-down-killed` rows and the `[dSP-39 AC2]` writer checks), red on its staged break (a writer copy
replacing the row whole with no carry) and green restored, and the spec's §7 gates.

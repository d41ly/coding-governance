**Serves:** journal TOOL-dSafePassage-33

# TOOL-dSafePassage-33 — acceptance ledger

The unit as built, at spec rev-4. `tools/govkit/upgrade_steps.py`: `read_step_states` admits an
optional `"via": "witness"` on an `applied` row only, folded into its existing key-set refusal so no
refusal branch is added; `set_step_state` and `write_step_record` take `via=None` and write the key
only when given; `run_step_walk`'s move 1 passes `via="witness"` and its move 5 passes none.
`derive_down_verdict` takes the row's last record, read in `run_reverse_walk` before move 3 rewrites
it: with no `reverted` and no image the down's exit decides only for a record `applied` via its
witness or no record, and a witness that still holds over a row with no image stops with
`witness still holds after down; before-image <path> absent`. `fixture walk` asserts the mark under
`witness-holds` and its absence under `fail-k`; `fixture rollback` gains the plant `image-lost` and
asserts the mark under `witness-only`. `tools/govkit/selftest.py` carries those needles and an
in-process table of the writer's refusals and the verdict's no-image rows. `help/upgrade-steps.md`
names `via` and the stop.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by the
unit's own CLI (`python tools/govkit/upgrade_steps.py fixture ...`) over its scratch fixtures, and by
an in-process probe (scratch `probe33.py`) loading this worktree's `upgrade_steps.py`, on node d
(Windows, Git Bash). They stand in for the `govkit selftest` leg's `check_step_walk` and
`check_step_rollback` rows for this unit only.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `encoding posture`, `policy fixtures`, `spec tokens`; and
the new arm's RED-first observation (§7): a verdict copy that applies the no-image rule to every row
must red the `image-lost` row (`fixture rollback --plant image-lost` then records `rolled-back` with
`s4.txt` left, the fixture printing `rollback: FAILED`).

**Evidences:** TOOL-dSafePassage-33
- AC1 — `fixture walk --plant witness-holds` exited 0 printing `walk: fx/s2 up canary absent · row applied · via witness`; `fixture walk --plant fail-k` exited 1 (by design) printing `walk: rows whose up ran carrying via: none`, no `walk: FAILED`. The probe's `set_step_state(r, "a/one", None, "failed", "boom", "witness")` raised `Refusal`: ``steps` row 1 ('a/one') carries the keys ['failure', 'id', 'introduced', 'state', 'via'], where a 'failed' row carries [...]; `via` 'witness' is legal only as 'witness' on an applied row``, the field left `[]`; `rolled-back` with `witness` and `applied` with `up` refused likewise; `applied` with `witness` admitted.
- AC2 — `fixture rollback --plant image-lost` exited 1 printing `rollback: fx/s4 applied · via None · image present before the plant deletes it`, `step fx/s4 · STOPPED · witness still holds after down; before-image .governance/steps/fx/s4.before.json absent`, `rollback: 1 reached · stopped at fx/s4`, `rollback: fx/s4 ('applied', 'witness still holds after down; before-image .governance/steps/fx/s4.before.json absent') · s4.txt in place`, no `rollback: FAILED`.
- AC3 — `fixture rollback --plant witness-only` exited 0 printing `rollback: fx/s2 applied by witness alone, no before-image`, `rollback: fx/s2 recorded via witness`, the four `rolled-back` lines s4 to s1 and `rollback: the target's bytes equal their bytes before the walk`.
- AC4 — `fixture rollback-update --plant schema-step-kill-before-stamp` exited 0, no `FAILED`, printing `rollback-update: the re-run exits 0 · its receipt's bytes equal the twin's ...`. That re-run skips both its rows by their witness, so the no-record branch is observed by the probe instead: `derive_down_verdict(row, False, 0, None)` returned `(True, 'down')`, beside `(True, 'down')` for `applied` via `witness`, `(None, 'witness')` for `applied` with no `via` and for `failed`, and `(None, 'witness')` with an image present.
- AC5 — `git grep -n -e "via" -e "before-image" -- help/upgrade-steps.md` printed lines 103-104 (the receipt section names `"via": "witness"`), 135 (the skip records it) and 198-203 (Rolling back: a missing image stops a row whose up ran, naming `witness still holds after down; before-image <path> absent`).
- No regression in the plants the scoped rule reaches: `fixture rollback` under `after-fail`, `node-witness`, `schema-step` and `unrecorded` each exited 0 with no `rollback: FAILED`.

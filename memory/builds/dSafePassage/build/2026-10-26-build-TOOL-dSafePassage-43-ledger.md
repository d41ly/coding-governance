**Serves:** journal TOOL-dSafePassage-43

# TOOL-dSafePassage-43 — acceptance ledger

The unit as built: `DOWN_STOP_PREFIXES` in `tools/govkit/upgrade_steps.py`, beside `STEP_STATES`,
holding §4's four openings; `read_step_states` admitting a `failure` on an `applied` row only when
it is a string opening with one of them, and refusing any other by the row's existing `failure`
refusal, which now names the row and the text; `set_step_state` unchanged, since it already
refuses every row the reader refuses, so the writer inherits the rule and the two cannot disagree.
No `raise Refusal` site was added, so `refusal_join.py`'s `BRANCH_PIN` does not move (§4
Inventory). `tools/govkit/selftest.py`: the dSP-3 AC7 row for a `failure` on an `applied` row now
expects the down-stop refusal; a dSP-43 AC1 arm in `check_receipt_schema` runs §4's six rows
through the writer; the dSP-3 AC8 `check` loop gains the two AC2 receipts.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 was observed by a
scratch `python` probe importing `upgrade_steps.py` by path, first at the unit's base (every
`failure` on an `applied` row refused by "carries the keys", the RED) and then on the built tree.
AC2 was observed by `govkit.py check --target` over a scratch target with a hand-written schema-4
receipt. AC3 needs `upgrade_steps.py fixture rollback --plant`, which TOOL-dSafePassage-4 builds:
by this spec's §3 hands-off to TOOL-dSafePassage-49, AC3 and the rollback-plant half of the arm
are observed at TOOL-dSafePassage-4's pass, so here only its prefix half was read. The new arm's
RED-first observation and the `govkit selftest` and `govkit refusal join` legs are owed at the
close (the spec's `New arm:` line).

**Evidences:** TOOL-dSafePassage-43
- AC1 — `set_step_state({"schema": 4, "steps": []}, "a/one", None, state, failure)` per row — `applied` with each of `down interrupted: started 2026-10-23T00:00:00Z, no exit recorded`, `down exit 1: x`, `witness still holds after down`, `witness still holds after down; before-image a.txt absent` and `reverted check exits 1` printed `admitted` with the row carrying that `failure`; `applied` with `interrupted: started 2026-10-23T00:00:00Z, no exit recorded` and with `exit 1: x` each printed "Refusal: `steps` row 1 ('a/one'): an applied row's `failure` '<text>' opens with none of the down stops …"; `rolled-back` with `down exit 1: x` and `failed` with none each printed "Refusal: … carries the keys …"; `applied` with none and `failed` with `boom` printed `admitted`. At the base the five down-stop rows printed "Refusal: … carries the keys".
- AC2 — `govkit.py check --target <scratch>` over an `applied` row with `down exit 1: boom` — rc 0 and no "step record is malformed" line; with `exit 1: boom` — rc 1 and one line: "the receipt's step record is malformed: `steps` row 1 ('govkit/receipt-schema-4'): an applied row's `failure` 'exit 1: boom' opens with none of the down stops …".
- AC3 — owed at TOOL-dSafePassage-4's pass (the rollback fixture and its plants are that unit's); the prefix half: each of §4's full texts opens with an entry of `DOWN_STOP_PREFIXES`, read off the AC1 probe's admissions.

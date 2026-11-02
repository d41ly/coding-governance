**Serves:** journal TOOL-dSafePassage-16

# TOOL-dSafePassage-16 — acceptance ledger

The unit as built: `test_steps_recordable` in `tools/govkit/upgrade_steps.py`, beside
`set_step_state`, True exactly when the receipt's `schema` is an `int` of 4 or more and its `steps` a
list; `set_step_state` refusing by that predicate instead of a comparison of its own, its refusal
text naming the rule and the receipt's `schema`, and its docstring stating the schema-4 bootstrap;
the same bootstrap sentence in the receipt section of `help/upgrade-steps.md`; and the selftest arm
`check_steps_recordable` over the spec's five receipt shapes.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed
by a scratch `python` probe importing `upgrade_steps.py` by path, and by the new arm's BODY,
`check_steps_recordable`, called in process outside the suite (10 lines `ok`, 0 failures). That
arm's RED-first observation and the `govkit selftest` leg itself are the close's (the spec's
`New arm:` line). AC3 and AC4 were read off the tree by `git grep`.

**Evidences:** TOOL-dSafePassage-16
- AC1 — `test_steps_recordable` on the five shapes of §4 "Data model" — printed `[False, True, False, False, False]`.
- AC2 — `set_step_state(receipt, "govkit/receipt-schema-4", None, "applied")` on the same five — raised `Refusal` on shapes 1, 3, 4 and 5 (text: "a receipt at schema 3 has no `steps` to record 'govkit/receipt-schema-4' in: a step row is recorded only where `schema` is a number of 4 or more and `steps` is a list; ..."), and on shape 2 appended the one row `{"id": "govkit/receipt-schema-4", "introduced": null, "state": "applied"}`.
- AC3 — `git grep -n -e "def test_steps_recordable" -e "test_steps_recordable(" -- tools/govkit/upgrade_steps.py` — printed `543:def test_steps_recordable(receipt: dict) -> bool:` and `565:    if not test_steps_recordable(receipt):` inside `set_step_state`, which keeps no schema comparison of its own.
- AC4 — `git grep -n -e "Before schema 4" -e "govkit/receipt-schema-4" -- help/upgrade-steps.md` — printed line 49 "Before schema 4 no step row is written: ..." and line 50 "The `govkit/receipt-schema-4` row itself is written once ...", in the section `What the receipt records about steps`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_steps_recordable`, whole function. Break: `test_steps_recordable` reads `schema >= 3`. RED: `FAIL [dSP-16 AC1] test_steps_recordable reads False on schema 3 with `steps` [], writing nothing — True {'schema': 3, 'steps': []}`. GREEN restored: FAILURES=0, 10 ok.

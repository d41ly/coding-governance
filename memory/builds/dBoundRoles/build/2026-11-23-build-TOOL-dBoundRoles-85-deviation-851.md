# TOOL-dBoundRoles-85 deviation 851 — the builder's departures from the adopter-rule levels spec

**Serves:** deviation TOOL-dBoundRoles-85

- **Departs from:** `TOOL-dBoundRoles-85@rev-1` [S2, S3, §4]
- **Hand-off:** spec-to-code
- **Before:** §4 "Inventory" mints `ADOPTER_RULE_LEVELS` and the fixture plant `adopter-rule-levels` with its arm, and says the constant is asked of `python tools/lexicon/lexicon.py --suggest ADOPTER_RULE_LEVELS --as py.constant` at the pass; §4 "The check" elides the `type` red's remedy as `...`; S3 asks the `adopter-rule` paragraph of `help/overlay.md` to say the type sits on a level-0 `repo` unit, or a level-5 one under `budget = "block"`.
- **After:** the lexicon answered `py.constant` is an undeclared cell, no convention to answer in, so the constant keeps the spec's name; the arm `tools/playbook/instruction_units.py#arm_adopter_rule_levels` was asked as `py.function` and passed. The arm reads its rows from a table beside it, `tools/playbook/instruction_units.py#ADOPTER_LEVEL_CASES`, each case's level, budget, namespace, the field its red names and the words that red carries, in the shape `SCHEMA_ROWS` and `STATEMENT_ROWS` already take; each row is read by `parse_unit_rows` at `OVERLAY` and its tag spelled from its namespace's parts. The `type` red keeps the remedy it carried, the statement types other than `adopter-rule`. The schema plant's existing `unit.carried` row, a level-0 `adopter-rule` in the `unit` namespace, still reds `type`, its text now naming its namespace and its level. The help page's paragraph also says a level-5 row under `line` or no budget is refused naming `block`, which S2 states of the check.
- **Cause:** builder discovery
- **Reason:** the lexicon declares no constant cell, so its answer cannot move the name; a case table is how this module's plants already hold their rows; the design left the remedy to the pass ("the pass fits it to the function"); the help line tells an adopter what the budget red asks of a level-5 row.
- **Evidence:** the build brief `memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-85-build-brief.md` and the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-85-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-85

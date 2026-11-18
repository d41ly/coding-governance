# TOOL-dDeclaredLoop-13 deviation 132 — TOOL-dDeclaredLoop-13's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-13

- **Departs from:** `TOOL-dDeclaredLoop-13@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-13`'s spec as the revision at `TOOL-dDeclaredLoop-13@rev-3` reads it.
- **After:** the spec at rev-4: the rows B1 to B20 are re-keyed on the item and outcome pairs unit 12 declared, rows B21 to B25 cover the cross-step routes, the route join covers routes that skip transition, an owed-row list holds the five routes other units' rows answer (F6), U5 and U6 key on the step definitions (F7), the leg is the loop kit's own gate_leg (F8), and run_selftest_cases is shared with loop_checklist.py.
- **Cause:** design defect
- **Reason:** the spec predated unit 12's item rows and unit 11's checklist module, so its outcome words, its join and its leg placement no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-13-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-13-reground-brief

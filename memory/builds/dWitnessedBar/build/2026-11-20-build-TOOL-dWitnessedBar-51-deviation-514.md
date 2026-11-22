# TOOL-dWitnessedBar-51 deviation 514 — a green bar's flake record, written outside test.flakes' nondeterministic input

**Serves:** deviation TOOL-dWitnessedBar-51

- **Departs from:** `dClosedLoop` [test.flakes]
- **Hand-off:** spec-to-code
- **Before:** the `test.flakes` row takes as its input the nondeterministic reds of `test.route`, so the flake record is written only on a red bar's route, and the driver's `gates-green` called `verdict_flow.py flakes` from its red branch alone.
- **After:** `verdict_flow.py flakes --record-only --run <run dir> --build <slug> --unit <id>` writes the flake record, one row per executed leg, and its gate-health measurement, then prints no `hold` and no re-entry line; `gates-green` calls it after a green bar, where `verdict.flakes` is `record` or `quarantine`, `retry-only` writing nothing, and a red bar keeps its landed call.
- **Cause:** review finding
- **Reason:** the round-1 spec audit's id 10: with records written only on a red bar, a green run adds no verdict to any leg's window, so gate health never reaches its thirty verdicts and arms, and a quarantined leg's green streak is never recorded, so no quarantine releases. The call adds no refusal site: a miss rides `run_leg_records`' own lines and never moves the item.
- **Evidence:** the `test.flakes` row of `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`; `tools/run-gates/verdict_flow.py#cmd_flakes`, `tools/run-gates/verdict_flow.py#main`, `tools/unattended/unattended.sh#dod_met`, `tools/unattended/unattended.sh#run_leg_records`; S15 of `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-51

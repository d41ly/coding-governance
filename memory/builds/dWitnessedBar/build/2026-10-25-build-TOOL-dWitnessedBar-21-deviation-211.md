# TOOL-dWitnessedBar-21 deviation 211 — the acceptance commands' own files are the check files they name, not the product module they probe

**Serves:** deviation TOOL-dWitnessedBar-21

- **Departs from:** `cl-dClosedLoop-0359@390176b3` [the acceptance commands' own files]
- **Hand-off:** design-to-spec
- **Before:** a fix pass after a failed acceptance leaves "the acceptance commands' own files alone", which a reader can take to mean every tracked file an acceptance command names
- **After:** a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wrong-spec judgment to Design as a new unit, its arm seen red on a planted fix pass that writes the red leg's test file, and a fix pass after a failed acceptance leaving the acceptance commands' own check files alone, those being a `*.test.sh`, a name ending `selftest.py`, a `test_*.py` or a path under a `fixtures/` directory, each named by a backticked token of the spec's acceptance criteria (night pass, point 6; TOOL-dWitnessedBar-21 §2 S2, §8 F2)
- **Cause:** design defect
- **Reason:** In this repository an acceptance command usually probes the unit's own module, `python seen_red.py --fixture …` say, so the module is both the code under test and the command's file. Keeping every file a command names would keep the product out of the fix pass that must repair it, leaving `build.fix-pass` after a failed `build.acceptance` unable to act. A probe whose plants live inside the product module therefore keeps nothing, which TOOL-dWitnessedBar-21 §5 states.
- **Evidence:** TOOL-dWitnessedBar-21 §8 F2; flow-steps `build.fix-pass`, `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:291`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0359@390176b3
- **Caused-by:** TOOL-dWitnessedBar-21

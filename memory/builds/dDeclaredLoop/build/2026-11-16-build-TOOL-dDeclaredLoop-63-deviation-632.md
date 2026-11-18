# TOOL-dDeclaredLoop-63 deviation 632 — the plant's adopter-phase calls read the held design exit, and the row case reads past both markers

**Serves:** deviation TOOL-dDeclaredLoop-63

- **Departs from:** `TOOL-dDeclaredLoop-63@rev-3` [§4, §5]
- **Hand-off:** spec-to-code
- **Before:** §4 "The arms" places the `driver-plan` plant's `check_phase_gates tPos REVIEWING STAGING` and `check_phase_gates tPos STAGING BUILDING` after `TOOL-dDeclaredLoop-52`'s phase observations, and spells the fifth selftest case `--from REVIEWING --extra REVIEWING`; §4 "The consumer" spells the call through named locals; §5's sweep counts this spec's rows of the positional registry as two.
- **After:** the two calls sit after unit 52's held-gate observations and before the disposition record of `item.design.exit`, so the move out of `STAGING` is held there as AC2 owes; the fifth case runs `--from REVIEWING --to REVIEWING --extra REVIEWING` and owes the whole line `phase REVIEWING · state designing · step step.design · to REVIEWING · crosses none`; the call adds `"--extra=$PHASES_EXTRA"` beside unit 52's `"--from=$2" "--to=$3"`, which name no local, and nothing else in the function moves; the module docstring's not-checked list no longer says an extra phase is refused by name, and says the module never reads the driver's conf for `--extra`; the registry holds no row of this spec, the commit landing rev-3 having shrunk them.
- **Cause:** builder discovery
- **Reason:** after the disposition record, `item.design.exit` is released and `item.plan.exit` reads `authorization`, never `held`, so a move out of `STAGING` placed after every unit-52 observation exits 0 and AC2's refusal cannot hold; a selftest case matches a line's opening, so the spec's fifth case could not see a marker appended after its reading, and with `--to` a marker after either reading breaks the opening.
- **Evidence:** `tools/loop/breakpoints.py#run_breakpoint_plant` run alone with the calls placed last printed `MISSED check_phase_gates tPos STAGING BUILDING exited 0`, and placed before the record printed `held`; `tools/loop/breakpoints.py#derive_breakpoints` gives the plan gate the release `authorization`; `tools/loop/loop_lib.py#run_selftest_cases` matches by `startswith`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the close's `loop transition tables` and `loop breakpoint fixtures` legs run the case and the plant as built
- **Caused-by:** TOOL-dDeclaredLoop-52

# TOOL-dWitnessedBar-1 deviation 13 — the mode's extra refusals and skip lines, the bound's seam, and the window fixture's release case

**Serves:** deviation TOOL-dWitnessedBar-1

- **Departs from:** `TOOL-dWitnessedBar-1@rev-6`
- **Hand-off:** spec-to-code
- **Before:** §4 lists the mode's refusals as no factory, no manifest, a mode clash, `--write` without `--build` and `--unit`, a `--with` path that is no flake record and a write the factory refuses; it prints the measured or unarmed line and the wrote line alone; S5 bounds the measurement call by `HEALTH_BOUND` without naming how; S8 lists the `flakes-window` cases without saying what threshold its release case reads under.
- **After:** the mode also refuses `--write`, `--build`, `--unit`, `--with` or `--fixture` without `--gate-health`, `--build` or `--unit` without `--write`, and `--fixture` beside any of the four, each exit 2 writing nothing; a record it skips is named on stderr as `drift-report: gate-health skipped <path> · <why>`, stdout unchanged; `verdict_flow.py#run_kit` gains a `bound` argument, `BOUND` by default, which `write_gate_health` passes as `HEALTH_BOUND`; `derive_flake_holds` takes the factory first, for `derive_flaked`; the `flakes-window` fixture removes its gate-health records before the release case, so that case reads at 2/10 as it did; and `--fixture write` adds the `--with` arming case (§4 Rollout).
- **Cause:** builder discovery
- **Reason:** a flag the mode ignores reads as obeyed, and a skipped record no line names is the silent case drift exists to refuse; the bound reuses the one subprocess seam the kit has rather than a second runner; and with a measured 1/10 newest, B holds at the release case, which planted none.
- **Evidence:** `tools/drift-audit/drift_report.py#main`, `tools/drift-audit/drift_report.py#run_gate_health_fixture`, `tools/run-gates/verdict_flow.py#run_kit`, `tools/run-gates/verdict_flow.py#write_gate_health`, `tools/run-gates/verdict_flow.py#derive_flake_holds`, `tools/run-gates/verdict_flow.py#run_fixture_flakes_window`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-1

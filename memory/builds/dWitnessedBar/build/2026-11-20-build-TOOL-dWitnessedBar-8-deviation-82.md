# TOOL-dWitnessedBar-8 deviation 82 — the edges the spec leaves open: a walled bar re-runs nothing, a declared entry is the check's threshold, and the held ask's read-back line

**Serves:** deviation TOOL-dWitnessedBar-8

- **Departs from:** `TOOL-dWitnessedBar-8@rev-7`
- **Hand-off:** spec-to-code
- **Before:** S1 re-runs each red leg whose ceiling did not fire under `GATE_RERUN=1`, naming no wall case and no double `nondeterministic` line for a sampled leg; S7 names the threshold in force at an ask's filing as "the gate-health record newest at that date, else `2/10`"; S8 has `write_held_asks` file through `write_leg_ask`, whose arguments carry no sha for `write_ask_rows`' read-back line.
- **After:** the runner re-runs nothing on a bar whose wall fired, skips a leg with a `.defer` marker or a serial retry, and prints `nondeterministic` once, not again for a sampled leg whose look printed it; `flakes --check` takes a declared `verdict.flakes.entry` `<count>/<window>` as the threshold in force, and the gate-health record or `2/10` only under `measured`; `write_leg_ask` hands `write_ask_rows` the sha a held suite's text opens with (`red at <sha8>`), none for a flaky leg, and `write_ask_rows` drops `red at` from its line when it is given none. The held suite's views render once per filed ask, `write_leg_ask` rendering them as S8 says, where `write_held_asks` rendered them once per call.
- **Cause:** builder discovery
- **Reason:** the wall bounds the bar and its re-runs together, as it bounds the serial retry; a declared threshold is the threshold in force whatever any gate-health record says, so reading only the measured one would red a hold the declared value justified; and the read-back line must not claim a red sha the flaky-leg ask does not carry.
- **Evidence:** `tools/run-gates/run-gates.sh` (the re-run block before `run_attribution`), `tools/run-gates/verdict_flow.py#read_flake_threshold`, `tools/run-gates/verdict_flow.py#cmd_flakes_check`, `tools/unattended/unattended.sh#write_leg_ask`, `tools/unattended/unattended.sh#write_ask_rows`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-8

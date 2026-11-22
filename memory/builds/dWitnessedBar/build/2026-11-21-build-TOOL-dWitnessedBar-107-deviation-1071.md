# TOOL-dWitnessedBar-107 deviation 1071 — the plant's ref count runs as a scenario process, and S1's last re-read names an unreadable slot

**Serves:** deviation TOOL-dWitnessedBar-107

- **Departs from:** `TOOL-dWitnessedBar-107@rev-1 [S1]`
- **Hand-off:** spec-to-code
- **Before:** §4 Data model says scenario 4 appends `(name, rc, 0, needles, said)` to the plant's list "as the lander plants do", and that every verify-peer run passes `VB_STUB_BAR=<mode>`, the first row's mode being unset; S1 step 8 says what a changed re-read prints and names no read failure there.
- **After:** `run_stale_slot_plant` receives `run_scenario` and not the list, so scenario 4 is one `run_scenario` call over a `python -c` process that counts the lines of `git ls-remote origin refs/gov/verdict/*`, prints `verdict refs: <n>` and exits 0 only where `n` is 0, the shape `run_peer_plant`'s signer-temp scenario already takes; the tuple the list gains is the one the spec names. Scenario 1 passes `VB_STUB_BAR=""`, which the stub's `${VB_STUB_BAR:-}` reads as unset, so an operator's own value never reaches it. Step 8's `OSError` is read as the run_id `unreadable (<error>)`, so the candidate takes step 8's own `was rewritten while it was read` refusal rather than a traceback.
- **Cause:** builder discovery
- **Reason:** S3 fixes the helper's signature as `(top, work, run_scenario)`, which holds no handle on the list; an empty value is the one way `run_fixture_command`'s environment can state "unset" over an inherited one; and a slot that will not read before publishing is a slot this run cannot vouch for, so deny by default refuses it.
- **Evidence:** `python tools/run-gates/verdict_backends.py --fixture --plant peer-stale-slot` printed `no verdict published after three refusals · exit 0 · owed 0 naming ['verdict refs: 0'] · held` and `8 of 8 scenario(s) held · all held` (DERIVED from the builder's probe, 2026-11-21).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-107

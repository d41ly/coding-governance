# TOOL-dGroundRules-33 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-33

No merge bar, no gate leg and no self-test suite ran in this pass; scratch-guard refused the
`policy fixtures` leg's argv to the gov-builder role, so no `--fixture` case ran here. The trace was
probed instead by a `python` script under the run's scratchpad that imports the changed
`check_policy.py`, installs `add_source_read` with `sys.addaudithook` exactly as `run_fixture` does,
reads the named files in process, writes and reads a file in a `pol-` temporary directory, opens
`README.md` in `r+`, and calls `check_guard_trace`; the AC4 half ran on a `git clone --shared` of the
branch under `%TEMP%/g33` carrying the changed `check_policy.py`, removed afterwards. Owed at the close:
AC2 and AC4 as the new arm's red-first observations, AC3's full `--fixture` run with the paths it
reports added to the guard (deviation 78), and every §7 leg.

**Evidences:** TOOL-dGroundRules-33
- AC1 — `policy fixtures` — `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` on the built tree printed `policy fixtures <- tools/govkit/selftest.py [selftests/kit]`.
- AC2 — `README.md` — the probe, reading `README.md`, `tools/govkit/selftest.py` and `tools/policy/kit.toml` in process, printed `policy-fixture: guard-trace · 3 source read(s)` then `policy-fixture: guard-trace · WRONG README.md · not under the policy fixtures guard` and nothing for the other two; the temporary file and the `r+` open were not kept. The run of `python check_policy.py --fixture adopter-fresh-target` with an `open()` staged into `build_install_target` is owed at the close.
- AC3 — `guard-trace` — owed at the close: `python check_policy.py --fixture` is the `policy fixtures` leg, refused to this role; its count line and any `WRONG` it prints are the close's, the paths added there (deviation 78). The probe observed the empty case, `policy-fixture: guard-trace · 0 source read(s)` then `WRONG: no source read was traced`, and an absent checker, `WRONG: check-spec-tokens.py --legs-for exited 2`, each counted wrong.
- AC4 — `gate-legs.json` — on the scratch clone with `{prefix}/govkit/selftest.py` staged out of the `policy fixtures` row, the probe reading selftest.py in process printed `policy-fixture: guard-trace · WRONG tools/govkit/selftest.py · not under the policy fixtures guard`; with the row restored it printed no `WRONG` and returned `(3, 0)`. The staged `open()` in `build_install_target` under `--fixture` is owed at the close.

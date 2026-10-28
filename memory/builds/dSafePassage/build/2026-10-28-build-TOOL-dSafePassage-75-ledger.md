**Serves:** journal TOOL-dSafePassage-75

# TOOL-dSafePassage-75 — acceptance ledger

The unit as built, at spec rev-3. Product writes: `tools/govkit/upgrade_steps.py` (S1, `GOV_PYTHON`
joins `STEP_ENV_KEEP` with the comment saying why), `help/upgrade-steps.md` (S2, the clean-environment
bullet names it) and `tools/govkit/selftest.py` (S3, the `[dSP-75]` check in `check_step_isolation`).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11, Python 3.15.2) over this worktree, run directly from the repository root, with
`TMP`/`TEMP` pointed into the run's scratchpad.

Owed at the close: the `New arm:` line's RED-first observation (the `[dSP-75]` check in
`tools/govkit/selftest.py`), and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-75
- AC1 — the spec's `python -c` probe — printed `probe-py`.
- AC2 — the spec's probe, saved to the scratchpad — printed `ok 0` with the built keep list, and `failed 1 resolve_python: tried: python3 python py` with `GOV_PYTHON` dropped from `STEP_ENV_KEEP` in process. A second scratchpad probe exec'd the `[dSP-75]` arm's own lines from `selftest.py` outside the suite: `ok` with the built keep list, `FAIL` naming `ran 3.12, below the floor 3.15` for each fake with the name dropped, and `PATH`/`GOV_PYTHON` restored after both.
- AC3 — `sed -n '/A clean environment/,/^- \*\*No git config/p' help/upgrade-steps.md | grep -c GOV_PYTHON` — printed `1`.

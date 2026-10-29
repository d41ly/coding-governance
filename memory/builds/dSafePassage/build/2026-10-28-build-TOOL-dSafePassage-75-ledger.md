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

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `b634d60e5` (batch d, `2026-10-29-prompt-TOOL-dSafePassage-72-close-arms-d-researcher.md`), each break staged alone and restored. The `New arm:` line of this unit was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `b634d60e5`. tools/govkit/selftest.py `check_step_isolation`, with `"GOV_PYTHON"` removed from `STEP_ENV_KEEP`: `FAIL [dSP-75] the floor row's witness under the contract, 3.12 fakes on PATH and GOV_PYTHON at the floor, is ok` with verdict failed, `resolve_python: no usable python launcher at the floor 3.15` (the only red). GREEN restored: `FAILURES 0`, 138 `ok`.

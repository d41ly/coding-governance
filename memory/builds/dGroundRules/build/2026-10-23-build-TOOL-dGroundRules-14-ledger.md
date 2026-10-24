# TOOL-dGroundRules-14 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-14

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edit in the worktree: the case through the kit's own fixture CLI, its
repositories under the system temp directory, short-named and removed by the case; and the lander
once, in a `--shared` clone of the built tree under `%TEMP%`, removed afterwards. The New arm's
RED-first observation, `policy.py` itself staged to spell its revision in a file value's reason, is
the close's.

**Evidences:** TOOL-dGroundRules-14
- AC1 — `python check_policy.py --fixture mirror-landed-merge` — run from the repository root as `python tools/policy/check_policy.py --fixture mirror-landed-merge`, exit 0: `mirror --write` over the merge printed "policy: mirror written · 259 keys"; at the rewrite `mirror --check` printed "policy: mirror fresh", exit 0; `arm_mirror_parity` found 0 of 259 keys; the helper's `get budgets.enforce --explain` on the rewrite landed as L printed `refuse` and "policy: budgets.enforce · file · set in .governance/policy.toml at d2f1b2b6, the landed revision", no `mirror stale at`; `arm_mirror_landed` found nothing over the 4 keys the file sets; then the line `policy-fixture: mirror-landed-merge · fresh at the rewrite`. 5 assertions, 0 wrong, no `WRONG`.
- AC2 — `--fixture mirror-landed-merge` — a scratch probe ran the case through `check_policy.run_fixture("mirror-landed-merge")` with the in-process `policy` module's file-value step replaced by one formatting the revision's own sha8 in place of `read.rev_phrase`; the subprocess `policy.py` stayed unbroken, so only the arm's render carried the break. It printed "the rewrite · arm_mirror_parity · WRONG: 1 finding(s) · budgets.enforce: differs from the render at HEAD", left out the `fresh at the rewrite` line, and exited 1 with 1 wrong. The staged break of `policy.py` on disk, red and then restored, is the close's observation of the New arm line.
- AC3 — `bash tools/push-main.sh --prepare` — in a clone of the built tree (HEAD 5d49772d with this pass's `check_policy.py`, committed as fb33adfd) whose bare remote's `main` was that commit, branch `land14` set `runtime.agents-in-flight = 5` without regenerating the mirror, which `mirror --check` then called stale at `policy_blob`. `bash tools/push-main.sh --prepare --slug dGroundRules` regenerated `.governance/policy.json` and printed "push-main: prepared 324de4ad — first parent fb33adfd (the advertised tip) · second parent 5477e486", exit 0. At 324de4ad `python tools/run-gates/regen.py --check` printed "regen: 13 declared · 13 fresh · 0 stale", exit 0, and `policy.py mirror --check` printed "policy: mirror fresh".

# TOOL-dGroundRules-41 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-41

No merge bar, no gate leg and no self-test suite ran in this pass. AC1 ran in this worktree from the
policy kit's directory, over the working tree carrying the change. AC2 and AC3 ran on a `git clone`
of the branch under `%TEMP%/g41` carrying the changed `check_policy.py` and `gate-legs.json`, each
staging applied by a script to the clone's `help/policy.md`. A third staging in that clone, the
`help/policy.md` guard line dropped from `policy fixtures`, printed
`guard-trace · WRONG help/policy.md · not under the policy fixtures guard`, so S2's line is what keeps
the trace green. Owed at the close: the `policy fixtures` leg over the built tree, and the new arm's
red-first observation (AC2, AC3).

**Evidences:** TOOL-dGroundRules-41
- AC1 — `python check_policy.py --fixture adopter-fresh-target` — printed `every arm graded clean or announced`, `guard-trace · 8 source read(s)`, `52 guard line(s) checked` and `211 assertion(s) executed · 0 wrong`, no `WRONG`; exit 0.
- AC2 — `HELP_DRIFT`, then the AC1 command in the clone — printed `WRONG: help/policy.md has no line under` `## Install` `holding the deferral line the install-day --scaffold printed: adopt-policy: mirror deferred · .governance/policy.toml has uncommitted changes · commit, then re-run --scaffold`; `1 wrong`, exit 1.
- AC3 — `HELP_MOVED`, the line moved under `## How to use it`, then the AC1 command in the clone — `INSTALL_LINES` there printed `0`, and the case printed the same `WRONG` naming `help/policy.md` and carrying the printed `adopt-policy: mirror deferred` line; `1 wrong`, exit 1.
- AC4 — `INSTALL_LINES` — printed `1` on the built tree; this diff writes neither side of it.
- AC5 — `HELP_LEGS` — printed `policy fixtures <- help/policy.md [selftests/kit]`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: adopter-fresh-target: HELP_DRIFT and HELP_MOVED each -> `WRONG: help/policy.md has no line under `## Install` holding the deferral line ...`. GREEN `help/policy.md:103 carries the deferral line`, 0 wrong.

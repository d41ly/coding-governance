# TOOL-dGroundRules-65 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-65

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed before the
commit, with this unit's edits in the worktree, by the kit's own CLIs or by scratch probes: one
calling `check_policy.run_fixture("mirror-commit-rewrite")` in process, never the leg; one running
`get --explain` under HEAD's `policy.py` and under the edited one over nine reads; and one in a
`--shared` clone of the built tree under the system temp directory, removed afterwards. Every fixture
repository sat under the system temp directory, short-named. The re-rendered `.governance/policy.json`
is not in this commit (deviation 70), so AC2's `git show` form waits for TOOL-dGroundRules-19.

**Evidences:** TOOL-dGroundRules-65
- AC1 — `policy-fixture: mirror-commit-rewrite` — `run_fixture("mirror-commit-rewrite")`, the case `--fixture mirror-commit-rewrite` runs, printed its lines with no `WRONG`: `mirror --write` at A wrote 259 keys; B' 5f5a90ef differed from B 9ad7ff3c over B's tree and parents; `mirror --check` printed "policy: mirror fresh", exit 0, at B and again at B'; the helper reading B' as L printed "set in .governance/policy.toml at 5f5a90ef, the landed revision"; and `arm_mirror_landed` found nothing over the 4 keys the file sets. 6 assertions, 0 wrong.
- AC2 — `grep -c "{rev}"` — in the clone, with this unit's code committed as 7065de11 and `mirror --write` committed over it as 2f225039, `git show HEAD:.governance/policy.json | grep -c 7065de11` printed `0` and `grep -c "{rev}"` printed `259`, one per key; `mirror --check` there printed "policy: mirror fresh". `render_mirror` at the worktree's HEAD 0cfed8ae counted 0 of its sha8 and 259 placeholders; over a fixture whose HEAD is invalid after a valid revision, 0 of the HEAD sha8 and 518 placeholders, each `last-valid` reason keeping the valid revision's own sha8. This commit's own mirror is still TOOL-dGroundRules-5's render, so the `git show` form over this commit is the close's, after TOOL-dGroundRules-19.
- AC3 — `python policy.py get budgets.enforce --explain` — on the built tree it printed `warn` and "policy: budgets.enforce · default · .governance/policy.toml is absent at ed497191, origin/main, the landed revision; the catalogue default", with no `{rev}`, byte-identical to HEAD's `policy.py`. The same comparison held over nine reads, each identical: a file setting the key, a key unset, an absent file, a named preset, two `last-valid` reads, a remote-less local `main`, and the worktree at `--rev HEAD`.
- AC4 — `node policy-mirror.js get budgets.enforce --explain` — in the clone of the built tree, its mirror fresh at L 2f225039 with `GOV_DEFAULT_BRANCH=main` naming L, it printed `warn` and "policy: budgets.enforce · file · set in .governance/policy.toml at 2f225039, the landed revision" on stderr: `the landed revision` present, no `{rev}`. On the worktree itself the landed `origin/main` carries no mirror until this build lands, so the helper takes the shim path there.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: render_mirror rev_phrase staged out -> mirror-commit-rewrite `policy.py mirror --check · WRONG: exit 1 · stdout 'policy: mirror stale'` at each B and B' (9 wrong). GREEN `91 assertion(s) executed · 0 wrong`.

# TOOL-dGroundRules-38 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-38

No merge bar, no gate leg and no self-test suite ran in this pass. The criteria were probed on a
`git clone` of the branch under `%TEMP%/gr38` carrying the changed `check_policy.py`, a primary
checkout whose `.git` sits under its top level, by `python check_policy.py --fixture
adopter-fresh-target` run from the clone's policy kit, with the one staging applied by a script and
the file restored after it. The rev-parse deny branch was probed by replacing `read_source_git_dirs`
with one that raises and calling `run_fixture('adopter-fresh-target')`: it printed
`policy-fixture: guard-trace · WRONG: git rev-parse --git-dir --git-common-dir at x did not answer both, so no case ran`,
returned 1, and installed no hook. Owed at the close: the `policy fixtures` leg over the built tree,
and the new arm's red-first observation (AC1, AC2).

**Evidences:** TOOL-dGroundRules-38
- AC1 — `PRIMARY`, then `python check_policy.py --fixture adopter-fresh-target` — the run printed `policy-fixture: guard-trace · 7 source read(s)`, `0 ignored read(s) set aside`, `51 guard line(s) checked` and `208 assertion(s) executed · 0 wrong`, and no line naming `.git/`; exit 0.
- AC2 — `PRIMARY` and `UNEXCLUDE` — the run printed `policy-fixture: guard-trace · 9 source read(s)`, then `guard-trace · WRONG .git/index` · not under the policy fixtures guard, and `WRONG .git/info/exclude` beside it; `210 assertion(s) executed · 2 wrong`, exit 1.
- AC3 — `DIRS_PROBE` in this linked worktree printed `C:\projects\coding-governance\.git\worktrees\unattended-dgroundrules-e47ae1` and `C:\projects\coding-governance\.git`; inside the `PRIMARY` clone it printed `C:\Users\daily-agent\AppData\Local\Temp\gr38\.git` twice.
- AC4 — `--fixture adopter-fresh-target` run from `%TEMP%/gr38x`, where `git rev-parse --git-dir` printed `fatal: not a git repository`, with the clone's kit named by its absolute path, printed the same `7 source read(s)`, `51 guard line(s) checked` and `208 assertion(s) executed · 0 wrong` as AC1; exit 0.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: primary clone, read_source_git_dirs staged to () -> `guard-trace · WRONG .git/index` and `WRONG .git/info/exclude` (2 wrong). GREEN `223 assertion(s) executed · 0 wrong`.

# TOOL-aLevelledCopy-3 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-3

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a,
where `git config core.filemode` reads `false`. The new arms of `tools/check-wiring.test.sh` ran as
one slice: the suite's prologue, then the `TOOL-aLevelledCopy-3` block, from a scratch script
whose `HERE` named the kit directory. Its fixture repos came from `newrepo`. Against the built
checker the slice printed seven `ok` lines and one announced AC6 skip, and it exited 0. The RED
observation was the same slice pointed at a scratch copy of the checker with both
`check_hook_modes` calls removed, and with `newrepo` put back to `git add -A`. All seven arms
printed `FAIL` and the slice exited 1. AC6 ran on WSL, not in the slice. The close still owes
`check-wiring self-test` run whole, plus the `branch-guard self-test`, `pre-push self-test`,
`pre-push bar self-test`, `lexicon naming predicates`, `codebase-map coverage + freshness`,
`memory hygiene`, `spec tokens`, `kit version markers`, `kit epoch`, `transition-audit arms`,
`straggler-guard arms`, `recall floor` and `recall floor arms` legs. One probe was skipped:
`bash tools/check-wiring.sh --check` in gov's own worktree, run to see the rollout's `note` lines,
did not return within its 300 s bound and was killed.

**Evidences:** TOOL-aLevelledCopy-3
- AC1 — `mode change 100644 => 100755` — before the commit, `git diff --cached --summary -- .githooks` printed four `mode change 100644 => 100755` lines, for `commit-msg`, `pre-commit`, `pre-push` and `pre-rebase`. `git diff --cached --numstat -- .githooks` printed `0 0` for each. The `awk '$1=="100755"{print $4}'` filter printed exactly those four paths, and `gate-env.sh`, `straggler-guard.sh`, the `*.test.sh` suites and `pre_push_bar_selftest.py` stayed 100644.
- AC2 — `grep '^UNWIRED  hooks.*tracked 100644'` — in the mode fixture it matched two lines, `.githooks/pre-commit` and `.githooks/post-merge`. It matched none for `pre-push`, `gate-env.sh` or `pre-commit.test.sh`. Break, the arm's calls removed: `FAIL`.
- AC3 — `hookmode-set` — `--fix` over a `pre-commit` carrying an unstaged appended line staged 100755 for both hooks. Their oids did not move, `git diff --cached --numstat` printed `0 0` for both, and `git diff --numstat` still showed `1 0` for the edit. The health log held two `hookmode-set` lines. A second `--fix` printed no `FIXED    hooks` line and the count stayed 2. Break: `FAIL` on both lines.
- AC4 — `--session` — a fresh mode fixture under `--session` printed the two `UNWIRED` lines and exited 0. `git ls-files -s .githooks/pre-commit` still read 100644, and no `hookmode-set` line was written. The first slice run printed `FAIL` here because the arm counted `grep -c` over an absent log as a non-zero answer. The arm now defaults that count to 0, and the next run printed `ok`. Break: `FAIL`.
- AC5 — `note     hooks` — in a `git worktree add` checkout whose `core.hooksPath` named the primary's `.githooks` by absolute path, `--check` printed a `note     hooks` line naming the primary's toplevel and `pre-commit is tracked 100644`. The `UNWIRED  hooks.*tracked 100644` grep matched nothing. Break: `FAIL`.
- AC6 — `git commit` — run through `wsl.exe -e sh -s` with the script on stdin, in a `mktemp -d` fixture on WSL's own `/tmp`, which `df -T` reported as tmpfs and not ext4. That filesystem honours the exec bit, which is the property the criterion needs. The index read 100644 for a `.githooks/pre-commit` that echoes and exits 1. `git commit --allow-empty` printed git's `hint: The '.githooks/pre-commit' hook was ignored because it's not set as executable.` and exited 0. `bash /mnt/c/.../tools/check-wiring.sh --fix` printed `FIXED    hooks     — .githooks/pre-commit staged 100755 (blob unchanged); commit it`, and the index then read 100755. The same commit printed `HOOK-RAN` and exited 1. That is WSL git 2.53.0. The self-test's AC6 arm printed `skip LC3 AC6 — MINGW64_NT-10.0-26200 runs a 100644 hook anyway` on node a and counted no pass.
- AC7 — `skip     hooks     — ... tracked by no checkout` — with `core.hooksPath` naming a `mktemp -d` directory that holds a `pre-commit`, `--check` printed `skip     hooks     — ... tracked by no checkout` and no `ok` line about modes. Break: `FAIL`.
- AC8 — `grep -n 'hookmode-set' tools/check-wiring.sh` — it matched header line 32, the health-event sentence, and line 606, the `add_health_event` call. `grep -n 'GIT_HOOK_NAMES'` matched the constant on line 568 and its one reader on line 575.
- AC9 — `git ls-files -s .githooks/pre-commit` — after the `newrepo` commands on node a, where `core.filemode` reads `false`, it read 100755. Break, `newrepo` put back to `git add -A`: `FAIL`, because it read 100644.

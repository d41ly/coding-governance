# TOOL-dDeclaredLoop-39 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-39

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on
node `d` (win32) over repositories `commit_trailers.build_fixture` planted from `tools/lib/`, under a
short scratch directory, each probe run once at the pass base `06495138` and once on the built tree.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of its one
`New arm:` line in `tools/memory-tree/routed_commits.py#run_selftest`, staged by removing one name
from the `git_env_leaks_py` block of the memory-tree copy of the reader for one run and restoring it.

**Evidences:** TOOL-dDeclaredLoop-39
- AC1 — `derive_attribution(c, "replace")` — a `git replace` of the fixture's newest commit by one
  carrying `Pass: TOOL-tFix-9`, then `read_commits` over that sha from the canonical copy: at base
  `['TOOL-tFix-9']`, on the built tree `['TOOL-tFix-2']`.
- AC2 — `.git/info/grafts` — the newest sha alone as a graft line, then
  `read_commits(repo, ["HEAD"], ("Pass",))`: at base the newest commit alone, on the built tree as
  many as `_FIXTURE` plants.
  figure: PINNED, measured 2026-11-14: 1 of 3 at base, 3 of 3 on the built tree.
- AC3 — `GIT_DIR` — `python tools/lib/commit_trailers.py --fixture` with `GIT_DIR` exported to this
  worktree's git directory: at base it printed this worktree's own subjects, on the built tree the
  fixture's three alone; `grep -c "NOT here: the git pins" tools/lib/commit_trailers.py` printed `0`.
- AC4 — `GIT_ENV_LEAKS` — a scratch `python -c`: the memory-tree copy's `commit_trailers.GIT_ENV_LEAKS`
  equals `tree_lib.GIT_ENV_LEAKS` (ok), and a scratch copy of that file with `GIT_PREFIX` removed
  from its block compares unequal (FAIL). The arm itself runs under the `routed-commits selftest`
  leg at the close.
- AC5 — `PASSTRAILER TOOL-tFix-2` — `python tools/unattended/commit_trailers.py tokens -1 HEAD` inside
  AC1's fixture, its replace ref in place, no git variable exported: at base `PASSTRAILER TOOL-tFix-9`,
  on the built tree `PASSTRAILER TOOL-tFix-2`; `grep -c GIT_NO_REPLACE_OBJECTS tools/unattended/lib-unattended.sh` printed `0`.

Also probed on the built tree: the `commit_trailers_py` and `git_env_leaks_py` blocks read
byte-identical across the three copies of the reader, and the second matches `tools/lib/git_env_leaks.py`.

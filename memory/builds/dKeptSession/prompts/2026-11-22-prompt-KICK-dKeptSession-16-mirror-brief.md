**Serves:** journal KICK-dKeptSession-16

# Brief — dKeptSession: KICK-dKeptSession-16's pass carries its policy mirror

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-16's pass, commit `8426252e03e127d2d6f60a3a473282bf08f74a43` on branch `worktree-wf_ce213496-950-1`,
changes `tools/policy/catalogue.toml`. The JSON mirror `.governance/policy.json` records that file's blob, so it is
stale at the pass tip. `pass-tree.sh --merge` refused the pass: its stage-2 regen ran `policy.py mirror --write`,
and over the merge's uncommitted tree the verb refuses ("uncommitted changes; the mirror renders a revision,
commit first"). The pass has to carry its own re-rendered mirror.

### Items

1. In the pass worktree `C:/projects/coding-governance/.claude/worktrees/wf_ce213496-950-1`, which is clean at
   `8426252e0`: run `python tools/policy/policy.py mirror --write`, then `python tools/policy/policy.py mirror --check`.
2. Commit `.governance/policy.json` alone on that branch, with the trailers `Pass: KICK-dKeptSession-16` and
   `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. It is a generated output, which `--check-commit`
   admits undeclared.

### Acceptance

`mirror --check` prints `policy: mirror fresh` at the new commit, `git status --porcelain` in the pass worktree
prints nothing, and `git diff --name-only 8426252e0 HEAD` there prints only `.governance/policy.json`.

### Gates

None. No gate, suite or bar runs here; the main loop re-runs the pass legs.

### Non-goals

This pass is one follow-up commit, and the whole recipe is here: in the pass worktree `C:/projects/coding-governance/.claude/worktrees/wf_ce213496-950-1`, which is clean at `8426252e0`, run `python tools/policy/policy.py mirror --write` and then `python tools/policy/policy.py mirror --check`, which must print `policy: mirror fresh`. Commit `.governance/policy.json` alone on branch `worktree-wf_ce213496-950-1`, with the trailers `Pass: KICK-dKeptSession-16` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, and return the new sha. No other file, no change to the spec or its status, no gate or suite, and no write in any other worktree, the run worktree included.

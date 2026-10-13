# branch-reconcile — which branches and worktrees landed, and which still hold work

```toml
feature = "branch-reconcile"
title = "One read-only report giving every worktree, branch and stash entry a verdict with its evidence, so a cleanup removes only what landed"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dSweptBranches-1", "TOOL-dSweptBranches-2", "TOOL-dSweptBranches-4"]

[claims]
gate-legs = ["branch-reconcile selftest"]
kits = ["branch-reconcile"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = ["tools/branch-reconcile/*"]
```

The kit exists because owners keep asking agents to clean up branches and worktrees, and each
session re-derived the method by hand. On 2026-10-13 one inCMS session spent hours on 71 local
branches, 33 remote branches and 60 worktrees: 60 merged, 9 superseded by later landings, 1 live and
1 closed, reviewed and never landed, which fixed a live production bug.

## Constraints & why

**The report is byte-stable.** The age column counts days to the default tip's commit date, never
to the clock, and every list is sorted. A report that moves between two runs over the same repository
cannot be diffed, and a diff is how an owner sees what a cleanup changed.

**It fetches nothing.** A read-only tool that wrote refs would change what it measures. The skill
fetches first.

**Untracked content that is another worktree is not the primary's.** A nested harness worktree is a
directory its primary lists as untracked; counting it would make every primary read dirty.

**GNU `rm -rf` is the only fallback deleter.** It never follows a link, so it removes the empty
skeletons of MSYS-made pnpm links that .NET `Directory.Delete` and `cmd rmdir /s /q` refuse. A
skeleton goes only when a link-blind walk finds no regular file in it.

**It does not consume the straggler inventory.** `migrate_backlog.py --stragglers` lists the refs
owing a backlog relocation, a narrower population answering a different question. The kit README
states the difference.

## Shared seams

- `resolve_remote` — the remote ladder, inlined byte-identically from `tools/lib/resolve_remote.py`
  and held to it by the resolve-python parity arm.
- `derive_verdict` — the ladder over the predicate functions in `PREDICATES`, the seam the verdict
  unit fills.

## Reuse affordance

seam: `branch_reconcile.read_inventory` — reuse for any tool that must list a repository's worktrees,
refs and stash with each worktree's dirty state; extend via a new field on the worktree record, never
a second worktree parser.

seam: `branch_reconcile.derive_verdict` — reuse for any question of whether a ref's work landed;
extend via one predicate function in `PREDICATES`, at the rung its verdict belongs.

## Gaps

- `landing` trusts a merge that names the unit and touched the same files; it does not compare
  bytes, so a pre-fold edit the fold then reverted reads covered. The prompt that commissioned the
  kit chose that rule.
- A worktree whose path git reports in a form `os.path.normcase` does not fold, such as an 8.3 short
  name, compares unequal to its long form.

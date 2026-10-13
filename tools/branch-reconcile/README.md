# branch-reconcile — which branches and worktrees landed, and which still hold work

<!-- gov:kit branch-reconcile@1.0 -->

One read-only command that answers the question an owner keeps asking an agent to answer by hand:
which of this repository's worktrees, local branches, remote branches and stash entries can go, and
which still hold work nobody has landed. Every row carries one verdict and the evidence for it.

```bash
python <this kit>/branch_reconcile.py [--root <path>]
```

Fetch first: the tool reads the remote-tracking refs as this clone last saw them, and fetches
nothing itself.

## The report

```
branch-reconcile — <remote>/<default> at <tip12> · <n> worktree(s) · <n> local · <n> remote · <n> stash
skipped — <predicate> · <why>
<VERDICT> · <kind> · <name> · <tip12> · <tip date> · age <n>d · <action> · <evidence>
```

- **The remote and the default branch** come from the ladder every kit inlines: `GOV_REMOTE`, the
  current branch's configured remote, the only remote; then `GOV_DEFAULT_BRANCH`, the remote's
  `HEAD`, `main`, `master`. A ladder that cannot choose refuses with exit 2 and names `GOV_REMOTE`.
  The default ref is the remote-tracking branch when it exists, else the local branch, announced in
  a `note —` line.
- **Kinds.** A worktree is `worktree/primary`, `worktree/nested` (under `.claude/worktrees/`),
  `worktree/sibling` (beside the primary), `worktree/temp` (under the system temp directory) or
  `worktree/elsewhere`. Its evidence carries `detached`, `prunable`, `locked`, `invoking` (the tree
  the tool was run from), its branch, and its dirty state: staged, unstaged, unmerged and untracked
  counts, a merge in progress (`merging <sha>`), a rebase in progress and submodule-pointer drift.
  A prunable worktree's state is not read, and the row says so. Refs are `local`, `remote` and
  `stash`.
- **Untracked content that is another worktree is not counted.** A nested harness worktree is a
  directory its primary's status lists as untracked, so counting it would make every primary dirty.
- **Order.** Rows sort by verdict — `UNMERGED-LIVE`, `UNKNOWN`, `IN-PROGRESS`, `SUPERSEDED`,
  `EQUIVALENT`, `MERGED` — so the owner's decisions come first, then by kind and name.
- **Byte-stable.** Every list is sorted, and the age is whole days from the tip's commit date to the
  default tip's, not to the clock. Two runs over an unchanged repository print the same bytes.

Exit 0 with the report printed; exit 2 on a refusal.

## Why this is not the straggler inventory

The relocation engine's `migrate_backlog.py --stragglers`, which `check-wiring.sh` reports, lists the
refs that still carry an unaccounted backlog-row change against the default branch: the refs that owe
a relocation before they merge. That is a narrower population asking a different question, and a ref
with no backlog edit is invisible to it however much unlanded work it holds. This kit asks whether a
ref's or a worktree's work has landed at all, so it reads every ref and every worktree, and it does
not consume that inventory.

## Files

- `branch_reconcile.py` — the CLI. Stdlib and git only.
- `selftest.py` — the self-test, withheld from adopters. Each fixture is a repository it builds
  under a temporary directory, with a remote named `upstream`.

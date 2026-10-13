# branch-reconcile — which branches and worktrees landed, and which still hold work

<!-- gov:kit branch-reconcile@1.0 -->

One command that answers the question an owner keeps asking an agent to answer by hand: which of
this repository's worktrees, local branches, remote branches and stash entries can go, and which
still hold work nobody has landed. Every row carries one verdict and the evidence for it. It is
read-only unless `--write` is passed.

```bash
python <this kit>/branch_reconcile.py [--root <path>] [--fresh-hours <n>] [--write [--remote]]
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

## The verdicts

A ref's ladder, first match wins, for a local branch, a remote branch or a worktree's `HEAD`:

| Verdict | Decided by |
|---|---|
| `MERGED` | the tip is an ancestor of the default branch |
| `EQUIVALENT` | `git cherry` lists commits and marks every one `-`, already applied |
| `SUPERSEDED` | `git merge-tree --write-tree` yields the default's own tree, or every unique commit is covered (below) |
| `IN-PROGRESS` | a run record at the tip with a non-terminal phase and a lease inside the freshness bound; a build README at the tip whose status is not `CLOSED` or `WONTDO` while the default's copy is not terminal either; or a tip committed inside the bound |
| `UNMERGED-LIVE` | unique commits remain uncovered |
| `UNKNOWN` | a predicate the answer depended on could not run |

**A unique commit is covered** when `git cherry` marks it applied (`patch-id`); when a commit on the
default branch carries the identical subject and the two patches' `+`/`-` lines differ by at most 4
(`patch`: a rebased copy that drifted by a line or two, which `git cherry` misses); when a later
merge on the default branch names the same unit id or slug and touched every file it did
(`landing`: a pre-fold or pre-squash variant); when it touches only run-state files of a build the
default branch shows landed (`records`); or when it adds only rows whose ids head a row somewhere in
the default's memory tree, archives included (`rotated`). A line that merely cites an id is never a
row: run over gov's own tree, an earlier version of that rule called a 250-line spec rewrite
superseded. A merge commit is covered when each parent is landed or itself unique.

**Merge-tree is only a positive proof.** Its conflict count is never read: a stale branch whose
every commit landed conflicts heavily.

**A worktree is graded before its `HEAD`.** It is `IN-PROGRESS` when it is the tree the report runs
from, or when its `HEAD` commit, its index or any dirty path moved inside the freshness bound
(`--fresh-hours`, 24 by default). Otherwise each piece of its content must already exist on the
default branch: an in-progress merge whose other side landed, an untracked file whose blob is in the
default tree or whose every test case (`def test_…`, `it("…")`, `test("…")`, `arm "…"`) exists there,
a changed path whose bytes equal the default's. Uncovered content makes it `UNMERGED-LIVE`; a rebase
in progress, submodule drift or an untracked directory makes it `UNKNOWN`. Covered content is named
in the evidence and the `HEAD`'s verdict decides the row.

**A stash entry** is `SUPERSEDED` when every path it changed already holds its bytes on the default
branch, else `UNKNOWN`.

Run records are read at a tip, as data, and never written: the unattended kit's `--settle` and
`--preflight` own them. The memory root is `MEMORY_ROOT` from `.memory-tree.conf`, else `memory`.

## Write mode — deletes only, of what landed

```bash
python <this kit>/branch_reconcile.py --write             # worktrees, then local branches
python <this kit>/branch_reconcile.py --write --remote    # and the remote branches, in one push
```

`--write` prints the same report, then acts on its action column:

1. **The recovery manifest first.** Every local branch, remote branch and stash tip and every
   worktree's path and `HEAD` go to `<git common dir>/branch-reconcile/recovery-<UTC stamp>.txt`,
   flushed to disk before anything is deleted. A manifest that cannot be written refuses the run
   with exit 2. Restoring is by hand: `git branch <name> <sha>`, `git worktree add <path> <sha>`.
2. **Worktrees**, whose action is `remove worktree`, through the remover below; then
   `git worktree prune`.
3. **Local branches**, whose action is `delete branch`, with `git branch -D`. A branch some kept
   worktree still has checked out is kept and reported.
4. **Remote branches** only under `--remote`, all in ONE `git push <remote> --delete`. Without it
   the report counts them and leaves them.

Only `MERGED`, `EQUIVALENT` and `SUPERSEDED` rows are ever acted on. The default branch is excluded
by name before its verdict is read, and so are the primary worktree and every stash entry. A
worktree is acted on only when its content was graded covered: dirty content with no counterpart on
the default branch makes it `UNMERGED-LIVE` before its `HEAD` is read. The tool never merges into,
commits on, checks out or pushes the default branch, and passes no hook-bypass flag; pre-push hooks
skip deletes on their own.

Exit 0 when every action succeeded or ended `busy`, 1 when any failed. Each action prints one line:
`removed`, `busy`, `kept`, `deleted` or `failed`, then what and why.

## Removing a worktree, on Windows too

`remove_worktree` is the one remover, and every rule in it was measured on adopter ic's node on
2026-10-13:

- **git first.** `git worktree remove --force --force`. It fails with "Result too large" on deep
  `node_modules`, and then GNU `rm -rf` removes the directory and `git worktree prune` drops the
  record.
- **A surviving skeleton.** After a clean removal the directory often survives as an empty skeleton
  of pnpm links made under MSYS, whose targets are POSIX paths (`/c/...`). It is removed with
  `rm -rf` only when a walk that follows no link and no junction finds no regular file beneath it; a
  reparse point is neither descended nor counted, and an unreadable entry keeps the directory.
- **Never another deleter.** .NET `Directory.Delete` and `cmd rmdir /s /q` both refuse those links
  ("The parameter is incorrect"), and a guard hook once misread `rmdir`'s `/s` as a path. GNU
  `rm -rf` never follows a link. With no `rm` on `PATH` the row fails and says so.
- **No link is resolved.** One spawned `readlink` per link timed out at 600 s over 40 directories.
- **Busy is a result, not a failure.** A directory an idle desktop session holds as its working
  directory stays "Device or resource busy"; the row reports `busy`.

## The skill

`/branch-reconcile` triggers on asks like "clean up branches", "reconcile worktrees", "stale
branches" and "is any unmerged work left", and routes them through the CLI. Attended, it fetches,
runs the report, puts the `UNMERGED-LIVE` and `UNKNOWN` rows first as the owner's decisions, runs
`--write` on the owner's yes and `--remote` only on its own yes, and offers to merge the default
branch into a live branch in that branch's own worktree, re-rendering generated artifacts, unioning
append-only logs and gating the result. Landing stays the owner's explicit ask, through the
repository's own lander. Unattended, it runs the report and `--write`, never `--remote` without its
own grant, and never a merge.

The Skill is rendered, because it names the CLI by where this kit is installed:

```bash
bash <this kit>/adopt-branch-reconcile.sh --scaffold   # render .claude/skills/branch-reconcile/SKILL.md
bash <this kit>/adopt-branch-reconcile.sh --check      # the wiring leg: is the render fresh?
```

`--check` re-renders the template and compares, stripping CR from the working copy, so a template
edit nobody re-rendered reds the `branch-reconcile skill wiring` leg. `govkit update` re-renders it
through the kit's `[[regenerate]]`.

## Why this is not the straggler inventory

The relocation engine's `migrate_backlog.py --stragglers`, which `check-wiring.sh` reports, lists the
refs that still carry an unaccounted backlog-row change against the default branch: the refs that owe
a relocation before they merge. That is a narrower population asking a different question, and a ref
with no backlog edit is invisible to it however much unlanded work it holds. This kit asks whether a
ref's or a worktree's work has landed at all, so it reads every ref and every worktree, and it does
not consume that inventory.

## Files

- `branch_reconcile.py` — the CLI. Stdlib and git only.
- `SKILL.template.md` and `adopt-branch-reconcile.sh` — the skill's template and its renderer.
- `selftest.py` — the self-test, withheld from adopters. Each fixture is a repository it builds
  under a temporary directory, with a remote named `upstream`.

---
name: cleanup
description: >-
  Reconcile and clean up this repository's branches and worktrees: which landed, which still hold
  work, and remove only what landed. Use whenever the ask is "clean up branches", "clean up
  worktrees", "reconcile worktrees", "prune stale branches", "stale branches",
  "is any unmerged work left", "what can I delete", or a session finds dozens of worktrees and
  branches nobody can account for. Routes through the branch-reconcile CLI, python {{KIT_DIR}}/branch_reconcile.py, which gives
  every worktree, local branch, remote branch and stash entry a verdict with its evidence and deletes
  only MERGED, EQUIVALENT and SUPERSEDED rows, after writing a recovery manifest. Do NOT use to land,
  merge or push the default branch — the repository's own lander does that — nor for a single
  `git branch -d` the owner named.
---

# Reconcile branches and worktrees

Never re-derive by hand what the CLI answers: `git cherry` misses rebased copies, merge-tree conflict
counts mislead, decision rows rotate into archives, and Windows worktree directories survive their
removal. The CLI carries those rules; the README beside it states them.

Rendered from `{{KIT_DIR}}/SKILL.template.md` by `adopt-branch-reconcile.sh`. Edit the template and
re-render; a hand-edited copy reds the adopter's `--check` arm.

## Attended — the owner is present

1. **Fetch**, so the remote-tracking refs are current: `git fetch --prune <remote>`. The CLI fetches
   nothing.
2. **Report**: `python {{KIT_DIR}}/branch_reconcile.py`. It is read-only. Each row reads
   `<VERDICT> · <kind> · <name> · <tip> · <date> · age · <action> · <evidence>`, and a `skipped —`
   line names any predicate that could not run.
3. **Surface the decisions first.** Every `UNMERGED-LIVE` and `UNKNOWN` row goes to the top of your
   answer, one line each with its evidence: these hold work nobody has landed, or work the
   predicates could not decide, and only the owner disposes of them. Then the `IN-PROGRESS` rows,
   which are kept. Then a count of what `--write` would remove.
4. **Delete on the owner's yes, and only then**:
   `python {{KIT_DIR}}/branch_reconcile.py --write`. It writes a recovery manifest under the git
   common directory before its first deletion, then removes the deletable worktrees and local
   branches. Remote branches need their own yes: `--write --remote`, one push. Relay every
   `failed`, `kept` and `busy` line; a `busy` directory is held by an idle session and is not an
   error.
5. **Offer to bring an `UNMERGED-LIVE` branch up to date**, one branch at a time, on the owner's yes:
   - work in that branch's own worktree, never the primary tree;
   - merge the default branch INTO it — never the reverse;
   - a generated artifact in conflict is re-rendered by its generator, never resolved by picking a
     side; an append-only log is unioned;
   - gate the result with the repository's own merge bar;
   - stop there. Landing it needs the owner's explicit ask and goes through the repository's own
     landing path.

## Unattended — no owner turn

Run the report and `--write`, and nothing else. Never `--remote` unless the run's own grant names
it. Never merge, rebase or land a branch. The `UNMERGED-LIVE` and `UNKNOWN` rows go into the run's
parked decisions for the owner, each with its evidence.

## If it refuses

Exit 2 names the reason on stderr. A ladder that cannot choose a remote names `GOV_REMOTE`: set it,
or `GOV_DEFAULT_BRANCH`, and re-run. A manifest that cannot be written deletes nothing.

---
name: a-merge-of-the-default-branch-read-as-additions
description: a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot
kind: class
universal: false
---

# A merge of the default branch is not new work

## Symptom

A check that grades "the files this branch adds" reds, or attributes work, on a feature branch the
moment it merges the default branch in: every file the default branch gained since the branch point
now reads as added by the feature. inCMS's memory-local check 21 did this (2026-10-13), while its
sibling check 29 already skipped merge commits.

## Cause

Whether a merge's files appear depends only on the git invocation's shape, measured over a real gov
merge (`TOOL-dSweptBranches-20`, seven `memory/` files gained by the default branch):

| Shape | Reads the merged-in files |
|---|---|
| `git diff --cached --diff-filter=A` while a merge is in progress | yes, all of them |
| `git log --diff-filter=A <frozen base>..HEAD`, the base older than the merge | yes |
| `git log -m`, or `git diff-tree -m` on the merge | yes |
| `git log --first-parent`: it diffs a merge against its first parent | yes |
| `git log <current default>..HEAD`, no `-m` | no |
| `git diff <default>...HEAD`, three dots from the merge base | no |
| `git diff-tree` on a merge, no `-m`, `-c` or `--cc` | no |
| `git log --ancestry-path ^<start> <tip>` | no |

`--first-parent` is the trap inside the trap: it reads as the fix and is not one.

## The fix

Skip merge commits (`--no-merges`), or measure from the CURRENT default tip or the merge base (three
dots), or walk `--ancestry-path` from the branch's own start. Never `--first-parent` alone.

## Where it applies

The sites `TOOL-dSweptBranches-20` classified, with their verdicts in that build's audit record:

- `.githooks/pre-commit` and `tools/memory-tree/check-memory-hygiene.sh` read the staged set, so a
  merge commit grades every merged-in `memory/` file; measured harmless, because they grade content
  the default branch already holds.
- `tools/hooks/scratch-guard.js` exempts a commit that adds a prompt-authorized build README, and a
  merge that brings one in is read as adding it.
- `tools/unattended/unattended.sh` reads a staged run-state archive in `read_pinned_base`, which a
  merge can stage; it fails closed, as a doubt.
- `tools/runlog/model.py`, `tools/memory-tree/row_grammar.py` and `tools/memory-tree/check-verdict-epoch.sh`
  read ranges in shapes the table marks safe.

## Related

- It coexists-with `a-gate-that-walks-the-repo-root-reads-other-worktrees`: both make a check read
  files that are not the subject's own, but there the walk reaches other worktrees' files, and here a
  range reads files the default branch added as the branch's own.

## Gate

No machine gate: the class is a property of an invocation, and the shape table above is the check a reviewer
runs. The audit record's probe rebuilds the measurement in seconds.

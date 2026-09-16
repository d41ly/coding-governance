---
name: git-rm-cached-refuses-a-diverged-index-blob
description: `git rm --cached` refuses a path whose index blob differs from both HEAD and the worktree, so a fixture cleanup without `-f` silently leaves the file staged and the next arm measures the wrong fixture
kind: class
universal: false
---

# `git rm --cached` refuses the one state a fixture cleanup meets

## Symptom

A self-test arm that stages a file, feeds a hook or a checker, and then unstages it to reset the
fixture passes on its own and fails, or passes for the wrong reason, when the next arm runs. The
cleanup printed `error: the following file has staged content different from both the file and
the HEAD` and the arm's `|| true` swallowed it.

## Where it bit

`TOOL-aReplayedCard-1`'s self-test stages a `README.md` carrying `authorized-by: prompt`, feeds the
deny, then overwrites the worktree copy without the key for the next state. At that point the
index blob differs from HEAD, which lacks the file, AND from the worktree, which lost the key —
exactly the state `git rm --cached` refuses without `-f`, to protect staged work. The AC8 fixture
stayed staged, and the untracked-README arm that followed measured a staged file instead. Found
red on the first full run of the suite, not by reasoning.

## The fix

Reset a fixture's index with `git rm --cached -f -- <path>` or `git reset -q -- <path>`, and never
hide a cleanup's exit code behind `|| true`: a cleanup that can refuse is an arm whose failure
must be visible. Gated in `tools/hooks/scratch-guard.test.sh` by the arm that asserts the AC8
fixture is untracked before it is fed; elsewhere a documented check.

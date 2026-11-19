---
name: failed-stage-reads-as-nothing-staged
description: a stager that never reads the exit status of its `git add` reads a stage that failed as a stage that held nothing new, so its caller skips the commit or the fold without a word and goes on to push
kind: class
---

# A failed stage reads as nothing staged

## Symptom

A commit step reports nothing to commit, or a fold reports the tree unchanged, while `git status`
still shows the change, and the run goes on to push. Nothing printed but git's own error from the
stage, which a caller reading only the staged-diff test never sees as a verdict.

## Where it bit

The closing review of the dSettledStage build, item 1, on the lander's helper `write_staged_change`
in `tools/push-main.sh` at the review head 41e57fca5. With an empty `index.lock` in the git dir,
`git add -A` exited 128 and `git diff --cached --quiet` exited 0, so the helper answered "nothing
staged": the attended landing skipped its regen commit, pushed and exited 0 with the change still in
the tree, and `write_merge_fold` answered success with HEAD unmoved. With `.git/index` overwritten by
garbage bytes, `git status` exited 128 and the helper read the failure as a clean tree.
Reproduced on node d with Git 2.54.0.windows.1 on 2026-11-19 (TOOL-dSettledStage-3).

## Why

A staged-diff test cannot tell "the stage holds nothing new" from "the stage never happened",
because a failed `git add` leaves the index equal to HEAD. A status probe that fails reads the same
way when its output is tested for emptiness rather than its exit status read.

## The fix

Read the stage's own exit status, and the status probe's, before the staged-diff test, and give the
failure its own answer that every caller refuses on. The lander's helper answers 2 for a failed
status or stage, each attended commit site refuses on it with its own stage's line before the push,
and the fold returns 1 on it (TOOL-dSettledStage-3).

## Gate

The lander's instance is gated by arms 44 and 45 of `tools/push-main.test.sh`, on the `push-main
self-test` leg: the attended landing over a regeneration that holds the index lock, and the helper and
the fold cut from the lander under the lock with an unlocked control. The class has no machine gate
elsewhere: `tools/gate-lint/sh_hygiene.py`'s
stage-commit mode reads whether a staged test follows a stage, never whether the stage's exit status
was read.

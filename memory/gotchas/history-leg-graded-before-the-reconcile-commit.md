---
name: history-leg-graded-before-the-reconcile-commit
description: a history-wide leg graded before the reconcile commit is graded on the wrong history, because the merge adds commits to the population without touching a file the fix touched
kind: class
---

# A history-wide leg graded before the reconcile commit was graded on the wrong history

## Symptom

A leg that grades HISTORY rather than files was observed green, the waiver or fix was committed, and
the leg is red at that commit. Between the observation and the commit a reconcile merge was
committed. The merge touched none of the fix's files, but it added commits to the population the leg
grades, and some of them are violations nobody waived.

## Where it bit

aRoutedQuill, node `a`, 2026-10-10. Commit 5b4f964d5 says the routed-commits leg
(`tools/memory-tree/routed_commits.py`) "now exits 0 (graded 39, 8 waived)". At that commit it grades
45 and fails on three version mints the reconcile 8f493d467 of origin/main e6585db4 brought in, none
of them listed in `ROUTED_COMMIT_WAIVED` in `.memory-tree.conf`. Closing review round 2 confirmed it
with all three lenses, and `TOOL-aRoutedQuill-9` added the three shas.

## The fix

**A history-graded observation names the tip it was taken at, and is re-taken after the LAST merge,
at the commit that ships it.** A waiver set for such a leg is derived from the leg's own output at
that tip, never from a review's list: blank the value, run the leg in WHOLE mode with
`GATE_PUSH_BASE` unset, and list exactly the shas it names under FAILED. The comment above the key in
`.memory-tree.conf` carries that sentence, so the close re-derives it after its last reconcile.

## What it is not

Not `observation-before-the-last-fold-of-the-same-commit`. That class's remedy is to re-run the
observations that count over the files the last fold touched. A reconcile merge touches none of
those files, so that remedy selects nothing here: the population is the commit graph, not a file
set.

## The gate

There is **no machine gate** for this class. The documented check is the derivation above, run at
the final tip after the last reconcile. `TOOL-aRoutedQuill-10` is specced to make the landing push
grade the leg as remote CI does; it is not the gate until that unit is CLOSED, and this record is
to point at it only then.

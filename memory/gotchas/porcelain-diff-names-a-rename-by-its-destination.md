---
name: porcelain-diff-names-a-rename-by-its-destination
description: a touched-set read built on porcelain `git diff --name-only` names a renamed file by its destination alone, so a prefix match misses a file moved OUT of the prefix
kind: class
universal: false
---

# A porcelain `diff --name-only` names a rename by its destination alone

## Symptom

A script decides whether a range TOUCHED some declared set of paths: it runs
`git diff --name-only <base> HEAD`, and prefix-matches each line against the set. It is right for
every add, edit and delete. It is wrong for one shape: a range whose only touch on the set is moving a
file OUT of it. The diff prints the destination and nothing else, the destination is outside the set,
and the range reads as untouched. The script's promise — typically "more than owed, never fewer" —
is broken in the one direction it said it could not be.

## Why

Porcelain `git diff` detects renames by default (`diff.renames` has defaulted on since git 2.9), and
with `--name-only` a detected rename is ONE line, the new path. Plumbing (`git diff-tree`,
`git diff-index`) has rename detection off unless asked, which is why the same read written with
plumbing never showed the gap, and why the gap goes unseen by anyone who tested with edits.

Two quieter arms of the same read: a path outside ASCII is printed QUOTED under the default
`core.quotePath`, so it cannot prefix-match anything, and `core.quotePath=off` does not cure that
whole, because git still C-quotes a path holding a tab, a double quote, a backslash or a newline;
and a `$(git diff ...)` that FAILS yields the empty string, which reads exactly like a range that
touched nothing.

## Where it bit

`print_selftests_owed` in `tools/unattended/unattended.sh`, the owed flagged-bar notice built by
TOOL-dAlignedCarrier-6. Its closing diff review, round 1, finding L1, reproduced it: after a
git mv of tools/k/a.sh to memory/a.sh, the default name-only diff printed the destination alone, and
`--no-renames` printed the source too. The round-1 fold made the read
`GIT -c core.quotepath=off diff --no-renames --name-only`, and a failed diff now announces the
answer is unknown instead of reading as untouched. Round 2, finding L2, showed the quoting half was
overclaimed: a committed file under the declared prefix whose name held a tab printed as a quoted
string under `quotepath=off` and matched no prefix. The read is now `GIT diff --no-renames --name-only -z`, split NUL-delimited and
matched inside a `pipefail` pipeline.

## The fix

A touched-set read that is PREFIX-MATCHED passes `--no-renames` (so both sides of a rename are named)
and `-z` (so every path prints verbatim, NUL-terminated, and is matched whole; `quotepath=off` is
inert beside it), and treats a failed diff, across the pipe, as "unknown", never as an empty range. A read that only asks "did anything change besides these two
named paths" does not need it: a rename still surfaces its destination, which is a change.

## The gate

There is **no machine gate** for this class. The predicate the review proposed — "a porcelain
`diff --name-only` whose output is prefix-matched carries `--no-renames`" — cannot be decided by a
line scan, because whether the output is prefix-matched is decided lines or functions away, and the
review's own sweep of the kit found the defect and one benign near-miss (`resolve_hold_streak`), plus
four plumbing `diff-tree` sites that are correct as written. A regex over the call site alone would
red the near-miss or pass the defect. It is a documented check instead: a reviewer of a diff that
adds a `diff --name-only` feeding a `case` or prefix match asks the rename question. The one live
instance is held by a suite arm, the rename-out arm in `tools/unattended/unattended.test.sh`.

## What this does NOT say

It does not say every porcelain diff wants `--no-renames`: a human-facing `git diff --stat` or a
review diff is better WITH rename detection. The class is a MACHINE reading a touched set.

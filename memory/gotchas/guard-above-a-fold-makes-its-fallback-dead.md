---
name: guard-above-a-fold-makes-its-fallback-dead
description: a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage
kind: class
universal: true
---

# The fallback that survived the guard that replaced it

## Symptom

A function grows a guard — `if not X: return` — and further down a ternary or an `or` still tests
`X` and supplies a fallback for the case the guard now refuses. Nothing between the two can change
`X`. The fallback arm is unreachable.

## Why

The guard is added to close a hole, in a review or a fix, and the fold beneath it is left alone
because it is not wrong — it is merely no longer reachable. Dead code in a conditional is invisible
to coverage in the way dead code in a function is not: the line runs, the branch does not.

The cost is not the wasted test. It is that the next reader concludes the fold still handles the
absent case, and deletes the guard as redundant — reopening exactly the hole the guard was added to
close.

## Where it bit

Twice in one diff, cMendedVintage closing review round 3. `tools/govkit/govkit.py`'s
`check_region_only` gained an unconditional `if not (target / path).is_file(): return False`, and
the ternary fourteen lines below still read `... if (target / path).is_file() else None`; only two
read-only git calls sat between them. The same shape had already been found and removed in
`tools/memory-tree/adopt-memory-tree.sh`, where a merge left an exit-1 refusal re-testing the
identical condition an exit-3 gate above it had just answered.

## The rule

**When you add a guard, read the whole function for the predicate you just settled.** Collapse every
fallback the guard makes unreachable, or write beside it why it stays — a deliberate TOCTOU arm is
legitimate, an accidental one is a trap for the next reader.

## Gate

**There is no machine gate for this class and none earns its cost.** An AST rule for "a ternary re-tests a predicate an earlier `return` already
settled" is more machinery than the defect. This is a documented check: it belongs to the reading a
Tier-2 review already does, and it prints into the bug-class checklist through
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>`.

---
name: budget-row-not-remeasured-after-added-arms
description: a suite gains arms and its assertion floor is raised, while its row in the budgets file keeps the reading taken before them, so the margin shrinks unseen until a loaded node cuts the suite as a timeout
kind: class
universal: false
---

# A budget row not re-measured after arms were added

## Symptom

A held suite's wall-clock budget is a row of a tracked file, written from one measurement at a
stated margin. A unit adds arms to the suite and raises its assertion floor in the same commit. The
budgets file is not in that unit's write set, so the row still names the earlier reading. Each such
unit spends some of the margin. The first sign is a timeout on a loaded node, reported as the
suite's red, at a commit that changed nothing in the suite.

## Where it bit

aNimbleMend added two end-to-end cases to the `policy fixtures` suite, four fixture repositories
to the commit grader's self-test and nineteen rows to the scratch-guard suite, and left
`tools/run-gates/selftest-budgets.txt` untouched. The `policy fixtures` row was written from a
reading taken before the two cases, which the builders measured at a large part of its margin
(PINNED, 2026-11-12). The closing review's round 1 found it as L3
(`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

A commit that raises a suite's `FLOOR_ASSERTIONS` re-measures that suite's budget row, or says why
not. The reading is the tool's: time the leg alone by its own argv, rewrite the row from that
reading at the file's stated margin, then run `derive-ceilings.py --write`. No hand types a reading.
Where the row cannot hold, the added cases move behind a leg of their own.

No machine gate: nothing compares a floor's history with a row's date. This record is the checklist
entry, selected by `gotchas.py --for-paths` for a diff touching the budgets file, and a reviewer of
any diff that raises a floor asks whether the row moved with it.

---
name: comment-claims-a-check-the-case-does-not-run
description: a comment credits a test case with checks it does not run, so a reader takes a rule for exercised there and a later edit that drops the real arm looks covered
kind: class
universal: false
---

# A comment claims a check the case does not run

## Symptom

A comment beside a test says another case runs a set of checks, and that case runs fewer. Nothing
reds, because a comment executes nothing. A reader then believes the rule is exercised here, so a
later edit that removes the one arm really holding it looks safe.

## Where it bit

The closing diff review of the dFairHearing build,
2026-11-04-review-TOOL-dFairHearing-1-40-diff-review, id 8. A comment in
`tools/policy/check_policy.py` said rules 2 and 5 left the hook for the review kit, whose checks the
writer-split case runs. That case ran the fan-out checker alone, and the same edit had flipped the
ref-keyed join row to an admission.

## The fix

Turn the claim into an executed check, a row of the case that runs the named checker and wants its
finding, or narrow the comment to what runs. Then name each checker the case runs, so the sentence
can be compared with the rows.

## Its gate

There is no machine gate for the class; the row the unit added to the writer-split case executes
this instance.

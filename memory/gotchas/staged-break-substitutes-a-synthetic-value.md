---
name: staged-break-substitutes-a-synthetic-value
description: an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value
kind: class
universal: true
---

# A staged break that mutates the constant instead of the subject

## Symptom

A gate is armed the right way — stage the failing case, confirm RED, unstage — and the arm still
proves nothing, because the staged break did not mutate the SUBJECT. It replaced the value the subject
reads with a simpler stand-in, and the mechanism was then exercised only for the stand-in. The arm is
green, the RED was observed, and the shipped construct is vacuous.

This is the sharper cousin of [fixture-passes-by-finding-nothing](fixture-passes-by-finding-nothing.md):
there the fixture never reaches the branch; here it reaches it carrying an input that cannot exhibit
the defect.

## Where it bit

`tools/unattended/check-unattended.test.sh`, the arm covering check 28b's exemption-freshness rule.
The shipped exemption row is `key|file|<a grep invocation with spaces in it>`, and the rule reads it
with an unquoted `for`, which word-splits. The arm staged
`KEY_EXEMPT="legs|check-playbook.sh|THIS_LITERAL_IS_GONE"` — a value with no spaces — so the split it
was meant to expose could not happen, the arm went RED for the right message for the wrong reason, and
the rule shipped unable to fail. Found in round 6 of the `dScriptedRepeat` diff review, one round after
the rule landed with a green arm beside it.

## The rule

**A staged break mutates the subject, never the constant the subject is measured against.** Break the
CODE and leave the shipped data alone; where the arm must alter data, alter it in place — retarget one
field of the real record rather than substituting a whole simpler one.

In practice that is the difference between `KEY_EXEMPT="legs|f|SIMPLE"` and
`sed 's@^legs|check-playbook.sh|@legsX|check-playbook.sh|@'`, which keeps every byte of the row's real
spacing and moves only the key.

## No gate

There is NO MACHINE GATE for this and there cannot usefully be one: a predicate cannot tell a
simplified constant from a legitimate one. It is a documented check, run at the moment an arm is
written. The
question to ask of every staged break is *what property of the shipped value did I just remove* — and
if the answer is "none, it is a different value", the arm covers a different mechanism.

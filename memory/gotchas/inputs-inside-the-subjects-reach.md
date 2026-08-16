---
name: inputs-inside-the-subjects-reach
description: a check whose inputs are all supplied by the thing it distrusts is not a check, however sound its logic
kind: class
universal: false
---

# A check is only as honest as the inputs the subject cannot reach

## Symptom

The logic is right. The branches are right. Someone reads it, agrees, and it ships. Then the thing it
was written to distrust defeats it — not by finding a flaw in the reasoning, but by supplying the
answer. Every input the check consulted was writable by its own subject.

## Where it bit

`tools/unattended/check-unattended.sh`, on the mandate check. The design was sound and it was defeated
three ways at once, because all three of its inputs were reachable by the run it distrusts:

- a value read back from the run-state file that the run itself writes;
- an anchor ref the run can move with `git branch -f`;
- an error signal dropped on the floor with `|| true`, so a failed probe read as a passing one.

The fix was not better logic. It was moving the inputs out of reach: the BASE is observed from the
remote's own advertisement rather than read from a local ref, and the mandate is asserted by the merge
bar rather than only by the driver that benefits from it.

## Cause

Writing a check is an act of reasoning about LOGIC, and the logic is usually fine. Provenance is a
different question, asked about each input separately, and nothing in the act of writing the check
prompts it. "Is this true?" and "who could have made this true?" feel like the same question and are
not.

## The fix

Enumerate the inputs before the branches. For each one, name what SUPPLIES it, and ask whether the
subject of the check can influence that supplier. An input the subject controls is not evidence; it is
testimony.

Then reproduce each defeat with a control, before and after. A review finding that has not been
reproduced is a hypothesis, and a hardening that has not been shown to close a specific reproduced
defeat is a hope.

## How to see it before shipping

For each input, write one line: `<input> ← <who supplies it> ← can the subject reach that?` Three
lines is usually the whole audit, and it is the audit that does not happen by itself.

Related: `second-implementation-is-not-a-second-opinion.md` — two implementations reading the same
poisoned input agree with each other and are both wrong.

## Detection

No machine gate. Provenance is a property of the design, not of the text, and no scan can tell which
inputs a subject can reach. This is a review question, asked deliberately, on any check whose subject
has write access to anything the check reads.

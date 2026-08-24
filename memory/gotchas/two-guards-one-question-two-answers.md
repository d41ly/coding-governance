---
name: two-guards-one-question-two-answers
description: two guards that ask one question different ways become jointly unsatisfiable, and the tree they wedge has no legal move left
kind: class
universal: false
---

# One question, two derivations, no legal move

## Symptom

A checker demands a record. A writer refuses to write it. Both are correct in isolation, both have
sensible messages, and the tree is red forever with nothing an operator can do about it. The verdict
looks like a bug in whichever half was run last, so the diagnosis lands on the wrong file.

The tell is that the two guards NAME the same thing and DERIVE it differently.

## Where it bit

`TOOL-dUnstalledConvoy-33`. The unattended kit's check 24 asked *was this unit in the roster the run
entered its live phase with*, deriving that roster from the run-state file's first live-phase commit.
The driver's check 48 asked *is this unit in the units region*, deriving it from the working tree.

Both were reasonable. Together they were unsatisfiable: the units region is RENDERED from the specs
that exist, so the moment a run authors a spec the id is in the region, and a rescope row for it is
refused forever — while the checker keeps demanding one. Four units on one build were in exactly that
state, every one of them added by an explicit owner turn mid-run.

The driver's own source carried a comment saying it had removed "the wedge shape this build exists
to remove" — for the *idempotent* case, where a byte-identical row already exists. The general case
was still wedged, one branch below the comment claiming otherwise.

## Why it survives review

Each guard reads correctly on its own, and a reviewer reading one is not reading the other. Nothing
about the two messages hints that they are about one question — check 24 speaks of a roster, check 48
of a region, and the two words are different enough that the collision is invisible in prose.

It also cannot be found by running either half. Check 24 is green until a roster grows; check 48 is
green until somebody records one. Only the sequence reds, and only on a run that both grew and tried
to record — which is a run that did the right thing twice.

## What to do

**Derive the shared question ONCE and have both callers ask it.** Not "keep the two in sync": a
second implementation is a second answer, and the pair only has to disagree once.

Where the two callers need different behaviour on a derivation FAILURE — and they usually do, because
one is reporting and the other is writing a permanent record — pass that difference in as a
parameter rather than forking the derivation. In this case the checker hands a fallback commit so a
comparison it cannot make is one it SKIPS, and the writer hands none so the same case REFUSES.

**When you meet the wedge, check whether the record is late-but-true rather than false.** A guard
written to stop fabricated records will also stop honest ones filed after the fact, and honest-late
beats absent. The fix is to make the guard ask the question that separates them, not to relax it.

## Related

[[second-implementation-is-not-a-second-opinion]] is the same family from the other side: there, a
second derivation CONFIRMS the first instead of checking it. Here it CONTRADICTS it. Both come from
one question having two implementations, and both are removed the same way.

## Its gate

**No machine gate, and the reason is the class itself.** A checker that found two guards asking one
question would have to recognise the question — which is semantics, not shape — and a predicate over
names or call sites would either miss the pair (different words for one thing, which is how this one
hid) or red on every pair of guards that merely mention the same file. Either shape is worse than
nothing: the first is a green that proves it, the second gets waived until it is ignored.

What replaces it is a **documented check**, run whenever a guard refuses something a sibling guard
demands: name the question both are deciding, then find where each derives its answer. If the two
derivations are different code, one of them is wrong even when both are green today.

Where this bit, the derivation now lives once in `tools/unattended/lib-unattended.sh` and is called
by `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`, with an arm asserting
neither defines its own — that arm is the closest thing to a gate this class has, and it is specific
to the one pair rather than to the class.

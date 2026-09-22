---
name: spec-names-code-its-base-lacks
description: a spec written from review records instead of from the code names machinery a commit ancestral to its own base already deleted
kind: class
universal: false
---

# The records describe the tree that was wrong, not the tree you are changing

## Symptom

A spec pins a BASE sha, reads coherently, passes every gate in the repo, and is committed. Its Scope
names functions, branches and variables that do not exist at that base — because they were deleted by
a commit the base already contains. A builder taking the scope literally must first RE-INTRODUCE the
thing that was removed, usually with a recorded verdict explaining why removing it was right.

## Where it bit

`TOOL-dUnstalledConvoy-23` rev-1. Four adversarial review rounds had produced a precise fix list, and
the spec was written from that list. Between the last round and the spec, `e42cb5a` deleted the whole
re-declaration and widening branch — and `git merge-base --is-ancestor e42cb5a d9728f8` succeeds, so
the spec's own base carried the deletion.

Four of seven scope items and three of eleven acceptance criteria had no subject. The spec's §9 said
outright that it was "written against the four review records rather than against the code, because
the code is the thing those records found wrong". That sentence was offered as a virtue and was the
defect: a review record describes the tree it reviewed, and repairs land after it.

Two things made it invisible. The driver still carried a comment block describing the deleted rule,
sitting directly above the code that replaced it, and `lib-unattended.sh`'s header still advertised
"the driver's re-declaration rule" as a caller. Stale prose is where a stale mental model comes from.

## The check, and why there is no gate

**At spec time: open the code at the BASE you are about to pin, and read the function you are
scoping.** Not the review that found it wrong — the function. `git show <base>:<path>` is the whole
technique.

**At review time: for each backticked identifier in Scope and Design, grep the file the spec co-names
at the declared base.** This is what caught it.

**No machine gate**, and the attempt is recorded because it was made twice. The broad predicate — every
backticked slash-bearing token in sections 2–4 resolved at the base — covers 3853 tokens across 236
specs and reds 151 of 225 based specs, including the spec that proposed it; a spec whose Scope adds new
files reds on its own scope, so no cutoff rescues it. The narrow predicate — paths only, Scope only,
new specs only — examines 4 tokens across 7 specs, and is blind to this class anyway, because the four
dead items here were shell identifiers and two of them were unbackticked prose. Cheap enough to ship
and useless; useful and unshippable. `TOOL-dUnstalledConvoy-25` was retired on those measurements.

## How this one is delivered

NOT by `gotchas.py --for-diff`. Measured over the commit that created this record: 0 anchored classes
selected. The anchors a record derives are its backticked paths, and the only one here is a shell
library — so a diff that touches SPECS, which is the only diff this class can occur in, never selects
it. Marking it universal would put it on every checklist and the universal budget is already at its
declared cap.

It is delivered at SPEC-AUTHORING time instead, by the build method's spec step, which is where the
check has to happen anyway: you cannot verify a spec against its base after the spec is written from
something else. That is the AC2 this record's retired unit carries.

## The rule that generalises

A record is evidence about a moment. When you write from one, date it against the tree you are
changing — and when you delete machinery, delete the prose describing it in the same commit, because
the prose is what the next author will believe. That is [[two-answers-to-one-question]] with a delay
fuse: the two answers do not disagree until somebody deletes one of them.

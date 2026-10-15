---
name: owner-item-without-its-reject-outcome
description: a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch
kind: class
universal: false
---

# The owner can say no

## Symptom

A design makes something wait for the owner's disposition: a proposal, a gate or a ruling. It routes
the acceptance in detail and says nothing of the refusal. Work that landed while the item was open,
such as an anchor, a stub or a pointer, stays behind when the owner declines, and a both-ways check
that accepted the open item turns red for everyone after.

## Where it bit

The memory layer's fold, 2026-10-16, in
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`. Under LR-6 a
build proposes its reuse entry and lands its `gov:feature` anchor while the entry is only proposed.
The fold's closing review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`,
M8) found no outcome for a rejected proposal. The anchor would stay, the check would red on the
default branch, and every later build would inherit the red.

## The fix

List every owner item's dispositions, the refusal included, and say what each leaves on the default
branch and which item cleans it up. For the reuse entry: accept, and the entry renders; reject and
remove, and a patch build removes the anchor; reject and keep, and the entry stays `rejected`, which
the check accepts.

It has no machine gate yet. Once owner items are declared as data, their disposition sets can be
checked for a refusal outcome.

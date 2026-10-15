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
default branch, and every later build would inherit the red. The follow-up round
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`, M7)
found the fix's own reject-and-remove left the entry `rejected` until the patch build landed, a state
the check refuses, so the red stood for that whole window.

## The fix

List every owner item's dispositions, the refusal included, and say what each leaves on the default
branch and which item cleans it up. Each disposition states the entry state it leaves, and every
check that reads that state accepts it for as long as it persists. For the reuse entry: accept, and
the entry renders; reject and remove, and the entry is `removal-pending` until one patch build
removes the anchor and the entry; reject and keep, and the entry stays `rejected`, which the check
accepts.

The class lives where owner items are designed: unit specs under `/spec/`, written from
`memory/TEMPLATE-SPEC.md`, and a build's design records under `/build/`. It has no machine gate yet. Once owner items are declared as data, their disposition sets can be
checked for a refusal outcome.

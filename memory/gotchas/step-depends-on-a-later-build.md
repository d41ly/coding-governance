---
name: step-depends-on-a-later-build
description: a step's item, a route into a shared mechanism or an expansion's registration needs a node only a later build in the chain builds, so the step cannot run between the two landings, and a check that reads only backticked citations never sees it
kind: class
universal: false
---

# A step depends on a build that lands after it

## Symptom

A chain of builds lands in order. A stage's own build lands, but something its step needs belongs to a build that
lands later: an item on the step's main path, the mechanism it routes into, or the point its programs register at.
Between the two landings the step names work no landed code does. It cannot exit, or its build hand-builds a second
copy of the mechanism. The dependency hides in prose ("falls back to an owner breakpoint"), in a route cell, or in a
contract's "extension points used" row. So a reconciliation that reads only a row's backticked citations reports
green over it.

## Where it bit

dClosedLoop's whole-design audit, 2026-10-18
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, H1 and H2), and the main
loop's C1 (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md`).

- An ownership decision gave every step's recommend and reason items to the Review build, which lands after every
  step build.
- RC-9's fallback needed an owner breakpoint that only the same late build built.
- dShippedRelease's programs register at Runtime's points, and Runtime was not among its ancestors.

The build-order review and the ancestor probe both read green over all three.

It bit again in dClosedLoop's night pass, 2026-10-18
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`, H2). Five new
clauses named a later build's playbook kind, tester role, experiment shape or announcement in plain words. The
hardened reconciliation probe read green, because its cites rule reads only backticked tokens.

## The fix

- Check every kind of dependency, not only citations:
  - each item of a stage step is built by the stage's build or an ancestor of it;
  - a route into a shared mechanism needs the whole mechanism from an ancestor;
  - an expansion's registrations need each point's owner to be an ancestor of the expansion's owners;
  - a key an item's cells name is owned by the item's owner or an ancestor of it.
- See the check red on today's tree before the fix, and red again on a planted dropped edge after it.
- Fix by moving the mechanism to an ancestor, by adding the edge, or by declaring a tolerance the check reads.
- Cite a dependency on another build's node backticked, so the check can read it. Widening the check to plain words
  was measured at 47 hits over 27 record kinds, mostly homonyms such as "landing" and "scope", so the check prints
  that count as unread instead of reading it. Roles, shapes and commands are not owned nodes. A clause that rests on
  one states its stand-in until that build lands.

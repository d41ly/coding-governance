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

It bit again in the answers fold, 2026-10-18 (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-answers-reviews-compared.md`). dSafePassage, the chain's
second build, raised the interpreter floor and retired the PEP 701 ban, while the resolver's refusal below the floor and
gov's own CI interpreter sat on dWitnessedBar, 81 units later, and a sentence credited dSafePassage with the self-run
that dShippedRelease's lander brings. Each now lands in dSafePassage itself.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Five more: `record`
refused a missing cause before any root kind existed; dKeptSession's live owner questions were dFurnishedOrders'
mechanism; steps landed before dShippedRelease never ran on gov first; adopter surfaces changed before their recovery
(hook unwiring, retired-edit orders, the stale lock) existed; and a deprecation window counted releases before the first
was cut.

It bit again in the last three folds' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-folds-reviews-compared.md`). Two more:
dSafePassage's walk and gov first read the receipt's `steps` field, which only dShippedRelease's schema 4 added, and
dOrderedCharter's native-id edge named only classes three later builds register. The field now moves with the clauses
that read it, and dOrderedCharter plants the edge on the FAMILY ids it owns.

It bit again in the night pass two's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`).
dFairHearing's checklist cut read a gate status only dLinkedLibrary creates, dKeptSession keyed message ids on acts
Runtime mints, and dPlacedRequest keyed decisions on work-order slots dBoundRoles brings.

It bit again in the flow and roles adoption's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`).
dBoundRoles named a widening in the update's report, which only dShippedRelease, a later build, extends to rows.

It bit again in the parked debt's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`).
dPlacedRequest's expiry read a clock offset dWellOiledMachine records, its default renewal mode was armed only
by a later build's ledger, its pushed request record waited on a later build's scan, and its fence's red case
planted a landing only later builds can stage.

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

## Gate

No machine gate holds this class on the merge bar. The documented check is dClosedLoop's reconciliation
probe, the instrument in its build folder that reads every route, key and registration of a chain row and
reds a dependency on a later build that no tolerance row names.

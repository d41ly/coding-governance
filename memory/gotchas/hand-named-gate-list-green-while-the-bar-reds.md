---
name: hand-named-gate-list-green-while-the-bar-reds
description: a spec names the legs its author expects the change to move, the unit is green on exactly those, and the bar is red on an unguarded leg the list never named
kind: class
universal: false
---

# A spec's gate list is a guess, and green on the guess is not green on the bar

## Symptom

A unit runs every gate its spec names, and all of them are green. Then the closing review or the push
boundary finds the full bar red on a leg the list never named. Nothing about the named legs was
wrong. The list was an author's guess about which legs the change reaches, and the bar's list is
derived.

## Where it bit

Five builds hit the same leg for the same reason. aBranchedMandate (2026-08-17), dPromptedSeam
(2026-08-25), dSealedTally (2026-09-04) and dBackdatedFixture (2026-09-16) each added a module-level
Python function. aProbedUnit (2026-09-14) added a top-level JavaScript function in a review fold. None
of them re-rendered the codebase map. Each spec named the suite the function lived in and not
`codebase-map coverage + freshness`, which has no guard, so every bar runs it. Every time, a diff
review filed `STALE` on `memory/map/generated/symbols.json` as a blocker.

Three of those reviews proposed the same left-shift in their prose, which was to run the leg at
commit time. None of the three became a backlog row. A left-shift written only into a review record
does not get built, and the class kept recurring after each proposal.

## What is gated, and what is not

Gated by `.githooks/pre-commit` for the instance that recurred. A commit staging a `.py` or `.js`
path runs `tools/codebase-map/test_codebase_map.py`. The commit is refused when an artifact is stale,
and also when the artifacts were regenerated but left unstaged. The arms live in
`.githooks/pre-commit.test.sh`.

That leg does not close the class, so the rest is a documented check:

- The hook does not trigger on the map's other inventory inputs or on a dossier claim edit.
- It grades the worktree, not the index.
- A worktree's commits run the primary tree's copy of the hook, per
  hookspath-resolves-into-another-checkout, so the leg binds only once it is on `main` there.
- Any other unguarded leg can red the same way.

Before calling a unit green, read the legs from `tools/gate-legs.json` rather than from the spec's
list. Ask which unguarded legs the diff's population reaches. Before the close, run the whole bar.
When a spec written from `memory/TEMPLATE-SPEC.md` names its gates, treat that list as a floor, not
the whole bar.

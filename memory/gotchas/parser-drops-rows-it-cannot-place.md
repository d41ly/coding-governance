---
name: parser-drops-rows-it-cannot-place
description: a record-parsing instrument skips rows under a heading or key it does not know and still prints a clean run, so its population shrinks without a word
kind: class
universal: false
---

# What the parser skips, it never grades

## Symptom

An instrument reads a record's tables and grades their rows. It keys rows by the section they sit in,
from a list it carries. A row under a heading that is not on the list is skipped, and nothing counts
what was skipped. Rename a section and its rows leave the population, and the run still prints
`findings 0`. Every planted red case edits a row inside a known section, so none of them sees it.

## Where it bit

The roles layer's matrix instrument, `role_matrix.py`, kept in
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` and run over the
step definitions in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`.
The fold's closing review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`,
M16) renamed `## [lifecycle]` in a copy. Six items dropped out of the population, and the run printed
`items 65; … findings 0`.

## The fix

Refuse what cannot be placed, and assert the population:
- a row under an unknown heading or key is a finding, not a skip;
- every expected section holds at least one row;
- one planted red case renames a section, beside the cases that edit rows.

It has no machine gate in the tree. `role_matrix.py`'s arm 0 does this now, seen red on the rename,
but that instrument lives in a design record, not in a gate leg. It is a sibling of
`vacuous-selector-empty-population`, where the selector matches nothing at all.

---
name: parser-drops-rows-it-cannot-place
description: a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word
kind: class
universal: false
---

# What the parser skips, it never grades

## Symptom

An instrument reads a record's tables and grades their rows. It keys rows by the section they sit in,
from a list it carries. A row under a heading that is not on the list is skipped, and nothing counts
what was skipped. Rename a section and its rows leave the population, and the run still prints
`findings 0`. A row under a known heading whose key the row pattern rejects, such as a tag with a
capital, a second dot or its backticks dropped, leaves the same way. Every planted red case edits a
well-formed row inside a known section, so none of them sees it.

## Where it bit

The roles layer's matrix instrument, role_matrix.py, kept in
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` and run over the
step definitions in `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`.
The fold's closing review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`,
M16) renamed `## [lifecycle]` in a copy. Six items dropped out of the population, and the run printed
`items 65; … findings 0`. The fix refused the unknown heading only. The follow-up round
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`, M10)
uppercased one tag, gave another a second dot and dropped a third's backticks: each run printed
`items 70; … findings 0`.

## The fix

Refuse what cannot be placed, and assert the population:
- a row under an unknown heading or key is a finding, not a skip;
- under a known heading, every table body row that is not a header or separator is a row to grade, and
  one the pattern cannot read is a finding;
- every expected section holds at least one row;
- the planted red cases rename a section and break a row's key, beside the cases that edit rows.

It has no machine gate in the tree. The record parsers it guards live under `tools/memory-tree/`, and
a build's own instruments live inside its records. role_matrix.py's arm 0 does both now, seen red on
a renamed section and on four malformed rows, but that instrument lives in a design record, not in a
gate leg. It is a sibling of
`vacuous-selector-empty-population`, where the selector matches nothing at all.

---
name: pipe-in-a-code-span-splits-a-table-cell
description: a markdown table cell holding a pipe, even inside backticks, splits into extra cells, so a reader that splits the row on its pipes reads the wrong cell as a column
kind: class
universal: false
---

# The backticks did not hide the pipe

## Symptom

A record's table cell names a command whose syntax holds a pipe, such as a verb list joined by pipes,
inside backticks. In a GitHub-flavored table a pipe splits the cell even inside a code span, unless it
is escaped as a backslash and a pipe. A reader that splits the row on its pipes finds extra cells, and
reads the wrong one as the last column. The rendered table shows a broken row, and a join over that
column reads a value that is not there.

## Where it bit

dClosedLoop's systems fold, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`). A clause
added to dOrderedCharter's chain row named the tag resolver's four verbs joined by pipes. The
gap-ownership join that the session log files
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`) then read 14 of
the 15 builds, and every gap dOrderedCharter owns read as unowned. A second join, which split rows on a
pipe with a space on each side, missed it.

## The fix

- Never write a bare pipe inside a table cell: escape it, or name the alternatives in words.
- Count each table row's cells against its header's, so an extra cell reds the record.

It has no machine gate yet. The per-table column-count check that
`insert-after-a-key-that-occurs-twice` proposes for `memory/` would catch this class too.

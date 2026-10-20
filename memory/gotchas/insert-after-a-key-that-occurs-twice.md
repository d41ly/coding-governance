---
name: insert-after-a-key-that-occurs-twice
description: a record edit inserts a row after the first match of a cell value that occurs in two tables, so the row lands in the wrong table and the right one never gains it
kind: class
universal: false
---

# The first match was the other table

## Symptom

A script adds an index row after an existing row, which it finds by searching for a distinctive cell
value. The same value also appears earlier in the file, in another table, as a cell of a different
shape. The search finds that one, and the row lands in a table whose column count it does not match.
The intended table never gains the row, and nothing reads the misplaced one.

## Where it bit

dClosedLoop's session log, 2026-10-16
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`). Its Dispatches
table names each review record in its last cell, and its Records index names the same paths. Three
commits inserted five two-column index rows after the first match, inside the seven-column Dispatches
table. The library round's review
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`, M14) caught it.
Its fold found a sixth: a check that the follow-up review's index row was present matched the same
path in the Dispatches table, so that row was never added.

## The fix

- Anchor an insertion on its section's heading first, then on the row inside that section.
- Assert that the anchor matches once within the section, and that the new row has its table's column
  count.
- Scope a presence check to the same section, or it finds the value elsewhere and skips the write.
- Keep the table's indent. An anchor that starts at a row's pipe, after the indent of the list the
  table sits in, makes the new row's line start at column 0, and the renderer ends the table there.
  dClosedLoop's runtime fold did this twice on 2026-10-17, and the folds' closing review caught it
  (`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`, L2).

It has no machine gate yet. A hygiene check that every table row under `memory/` has its header's
column count would catch the whole class.

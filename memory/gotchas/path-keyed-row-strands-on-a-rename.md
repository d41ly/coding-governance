---
name: path-keyed-row-strands-on-a-rename
description: a registry row keyed by a file's path breaks on a rename, so the old row reads as one no scan finds and every instance as one with no row, and a unit that only moved a file reds on legacy it did not write
kind: class
universal: false
---

# A rename strands every row keyed by its path

## Symptom

A tolerated population keys each row on a path: path, rule and identifier, with no line number. A unit
renames the file. The diff carries no content hunks, so nothing drains. But every old row now names a
path that no scan finds, and every instance appears under a path that has no row. Both arms of a
both-ways check red on a pure rename.

## Where it bit

dClosedLoop's retrofit design, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`, `[ledger]`).

The code-site key had dropped the line number, the lesson of line-keyed-registry-reds-on-a-file-that-grew.
It kept the path, with no rule for a rename. gov renamed 7 code files in the 90 days before
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`, M34).

## The fix

- Diff with rename detection over the unit's range.
- Carry each row from the old path to the new one, keeping its disposition.
- Treat a rename alone as neither a gain nor a drain.

It has no machine gate yet. The design owes a probe that stages a `git mv` of a baselined file and
expects the check green, with its rows re-keyed (the retrofit record's `[ratchet]`).

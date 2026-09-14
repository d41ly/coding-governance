---
name: suite-edited-while-bash-executes-it
description: bash reads a script incrementally by byte offset, so editing a suite file while a long run of it is executing corrupts the parse at the old offset and the run dies with a syntax error that names no edit
kind: class
universal: false
---

# Editing a suite while bash is running it

## Symptom

A long self-test run — minutes, sometimes twenty — dies partway with `syntax error near unexpected
token` at a line that parses fine when you open the file. Re-running passes. Nothing in the diff
looks wrong, because nothing in the diff is.

## Where it bit

`KICK-aReplayedCard-2`'s pass edited `skills/session-kickoff/manifest-check.test.sh` while a
seventeen-minute run of that same suite was still executing, to add the next arm while waiting.
Bash does not load a script whole: it reads and parses as it goes, by byte offset into the file it
opened. The edit shifted every later byte, the running shell resumed reading at the old offset in
the new bytes, and the mid-token garbage it found there is what the error named. The sibling class
`memory/gotchas/suite-invalidated-by-a-commit-under-it.md` is the same shape one level up, for a
commit made under a suite that pins its revision at import.

## The fix

Never edit a suite file, or a script it sources, while a run of it is live; edit a copy, or wait.
When a long suite must be developed under time pressure, run it from a `mktemp -d` copy of the
tree, as the hermetic legs do, so the working file is free to move. No machine gate — a shell
cannot tell a deliberate edit from a stray one — so this is a documented check, and the run's
ledger names the re-run it cost.

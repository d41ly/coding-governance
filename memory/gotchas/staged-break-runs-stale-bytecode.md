---
name: staged-break-runs-stale-bytecode
description: a harness that edits a Python module and re-runs its arm can execute the previous edit's cached bytecode, because two same-size edits inside one second pass the cache's check
kind: class
---

# A staged break judged by the previous break's bytecode

## Symptom

A harness stages breaks one after another against a Python module: edit it, run the arm that owns
the rule, record RED, restore the bytes. One break reports RED on a check that belongs to a
DIFFERENT break, or reports a RED its own edit could not cause.

Python validates a cached `.pyc` against the source's modification time in whole seconds and its
size. An edit that lands in the same second as the previous one and leaves the file the same length
passes that check, so the run executes the previous edit's bytecode, not the current one.

The dangerous direction is the false RED. A break whose own check stays green can pass for proven,
because a stale neighbour's check failed in its place and the exit status was all the harness read.

## Where it bit

`TOOL-dLoggedFlight-9`, node `d`, 2026-09-14. The harness staging the record's copied-set breaks in
`record.py` removed a ten-byte member from one list, then a ten-byte member from another, inside one
second. The second run failed the FIRST break's check, the push decisions, because the interpreter
loaded the stale cache from `__pycache__`. Run alone, the second break failed its own check. Every
break of that pass was re-run with the cache cleared before each run, thirty of them, and each failed
the check it aims at.

## The fix

**Clear the module's cache before each staged run and run the interpreter with `-B`**, so no break is
judged by bytecode it did not write. And match each RED against the check the break AIMS at, never
against the exit status alone: a run that fails somewhere else is evidence of nothing about this
break. This is the staging sibling of
[fixture-passes-by-finding-nothing](fixture-passes-by-finding-nothing.md), whose sub-shape is a
fixture tripping an earlier guard; here the harness trips an earlier edit.

No machine gate: a staging harness is scratch and untracked, so this is a documented check, run when
a harness that edits a `selftest.py` subject or its modules is written.

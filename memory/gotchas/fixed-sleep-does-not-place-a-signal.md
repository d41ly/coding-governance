---
name: fixed-sleep-does-not-place-a-signal
description: a test that sleeps a fixed time and then signals assumes the child it means to interrupt is already running; under load the signal lands before that child exists or after it ended
kind: class
universal: false
---

# A sleep is a guess about the scheduler

## Symptom

A test sends TERM to a process "while it is inside" some child, to see what an interrupted run
leaves behind. It passes on an idle box. Under load it fails, or it passes for the wrong reason: the
signal arrived before the child started, and the test observed an early kill, not an interruption.

## Cause

`sleep 1; kill -TERM "$pid"` places the signal at a moment of wall-clock time, not at a point in the
program. Process creation on this fleet varies severalfold with load, as
[[process-creation-is-the-suite-cost]] records, so no fixed delay is both safe and short.

## The fix

Make the child ANNOUNCE itself and signal only after the announcement. The child writes its pid to a
ready file as its first act, the test polls for that file under a BOUND, and it asserts the child is
alive before sending anything. Where the child should outlive the signalled parent, assert that
afterwards too: "the child is still running" is a verdict that does not depend on timing at all.

## Where it applies

`tools/unattended/runlog-writer.test.sh`, arm AC3, which interrupts `--close` of
`tools/unattended/unattended.sh` inside its gate command. That arm's first draft slept a fixed time
before the signal, and round 2 of the spec audit replaced the sleep with the ready file.

## Gate

No machine gate for the class. A sleep before a `kill` has no signature that separates it from a
legitimate pause, so this is a documented check at review time, and the AC3 arm is the worked example.

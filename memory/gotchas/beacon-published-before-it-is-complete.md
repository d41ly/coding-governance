---
name: beacon-published-before-it-is-complete
description: a lock or presence directory made visible before the files that let others judge it leaks forever when its writer dies in between, because every sweep needs those files
kind: class
universal: false
---

# Interrupted between the mkdir and the first write

## Symptom

A process announces itself with a directory, then writes its pid and heartbeat into it. Killed
between the two, it leaves a directory with neither, and the sweep that judges holders by pid or
heartbeat skips it on every run, so it never goes.

## The instance

The docs beacon in `tools/run-gates/run-gates.sh` was made with `mkdir` before its heartbeat and pid
writes, and `scan_dead_docs_beacons` passed over a beacon with no heartbeat (aPairedSlots closing
review, L2).

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). The upgrade walk
skipped a step when its witness held, and nothing said the witness is written last, so a step killed after its first
write would read as done on the re-run. The step kind now writes its witness last and the receipt advances per completed
step, with kill-midway arms.

## The remedy

Publish complete, writing under a temporary name and renaming into place, or sweep on the one clock an
incomplete beacon has, its directory's age, under the same guard as any other removal.

## Gating

Gated by `tools/run-gates/run-gates.turnstile.test.sh` arm 47, for the docs beacon only.

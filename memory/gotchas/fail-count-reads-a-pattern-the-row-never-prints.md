---
name: fail-count-reads-a-pattern-the-row-never-prints
description: a fails column counts one line shape, and a row whose script prints its failures in another shape always reads 0, so two different reds compare equal
kind: class
universal: false
---

# The fail count reads a shape the row never prints

## Symptom

A runner records a fails count beside rc, counting one line shape, and parity compares a run against
that recorded count. A row whose script reports its failures in a different shape always counts 0.
Its reading is then rc only, whatever the header says: a run with one failure and a run with twenty
read alike, and a new red that keeps the old rc matches the calibrated reading.

## Where it bit

The aShelvedLeg closing review, round 2 id 1. `tools/run-gates/run-selftests.sh` counts
`grep -c '^FAIL'`. `tools/unattended/check-unattended.sh` prints each failure as
`UNATTENDED check <n> FAILED`, never at column 0 as `FAIL`. TOOL-aShelvedLeg-1 declared the kit gate
row no-trailer in `tools/run-gates/selftest-pooled-evidence.txt` and said it was read "likewise",
that is rc plus FAIL count, which it is not. TOOL-aShelvedLeg-2 rewrote the header to say the row is
rc only and why.

## The fix

When a row joins a population read by a fixed pattern, check that the row's script prints that
pattern. Where it does not, state that the row's reading is narrower. Widening the pattern moves
every calibrated row whose fixtures print the other shape, so it is a calibrated change, not a fix
to make in passing.

## Gate

There is no machine gate for this. Nothing checks that a row's script can print the pattern its
fails column counts; that arm was deferred as an ask. A reviewer adding a row reads the script's
failure line against the runner's count.

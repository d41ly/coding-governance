---
name: sweep-issues-no-cost-verdict
description: the self-test sweep never grades a suite's wall clock against its budget, and that is the ruling, not a gap
kind: invariant
decision: TOOL-aPooledSweep-1
---

## Looks wrong
`--sweep` runs every self-test suite and never reports one that overran its declared wall-clock ceiling.

## Actually
The sweep runs its suites concurrently, and a contended clock cannot grade a budget, so it claims parity alone and says how many cost verdicts it withheld.

The serial loop is the only mode of `tools/run-gates/run-selftests.sh` that grades a budget, and that
division is what makes the concurrent sweep admissible: the contention that would misattribute a
breach is admitted, and the breach is simply not claimed.

## Do
Grade a suite's cost with the serial run of `tools/run-gates/run-selftests.sh`, one suite at a time.

## Do not
Add a ceiling check to the sweep, or read a sweep's per-suite wall times as a budget breach.

## Guarded by
`run-selftests self-test`

Its sweep arms assert the sweep says it graded no cost and states how many verdicts it withheld.

---
name: canary-waits-on-a-rendezvous-not-a-clock
description: the run-gates canary never compares elapsed times, and that is the ruling, not a gap
kind: invariant
decision: TOOL-cSteadyMetronome-1
---

## Looks wrong
The run-gates canary never compares a serial run's elapsed time with a concurrent run's, so it seems not to prove the pool runs legs at once.

## Actually
It counts the peers announced at once through a rendezvous, because an elapsed-time ratio measures the node and not the runner.

The retired ratio red three consecutive pushes on a machine running a second bar, over a tree it had
already passed. A rendezvous absorbs dispatch skew and load alike, so the verdict reads the runner.

## Do
Grade concurrency by the rendezvous peak the fixtures in `tools/run-gates/run-gates.test.sh` record before they sleep.

## Do not
Reintroduce an elapsed-time ratio or an interval intersection of leg start and end times.

The aPacedTurnstile build's spec audit caught a spec re-proposing the refuted interval form, which is
why this ruling is recorded where a reviewer is handed it.

## Guarded by
`run-gates canary`

That leg runs the suite whose rendezvous arms red on a pool collapsed to width 1.

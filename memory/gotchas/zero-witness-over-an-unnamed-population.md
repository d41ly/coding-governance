---
name: zero-witness-over-an-unnamed-population
description: a scan whose zero is the witness names no population, so a skipped scan and a scan over less than the guarded boundary publishes both read as clean
kind: class
universal: false
---

# A zero that names nothing it read

## Symptom

A gate certifies absence: no secret, no offender, no match. Its witness is a count, and zero passes.
The witness does not say what was read. A scan that resolved no value, read an empty set, or read a
narrower set than the boundary it guards prints the same zero as a clean scan, and nothing about that
zero looks wrong.

## Where it bit

The expansion round's secret value scan, in
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`, whose
witness was "a count and a salted id only. Zero is the witness." The round's two reviews found both
halves:
- the population left out what a push publishes: commits behind the tip, and the objects the core
  pushes under refs/gov (run A's M13, run B's M10);
- an adapter whose value did not resolve, or was `anonymous`, scanned for nothing and counted zero (run
  A's M14).

The fold moved the scan into Runtime's record,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`. The fold's
closing review then found the moved scan claiming a population its boundary never published. It bound
at the lander's prepare while the core pushes its mailbox, card and claim refs at other times, and its
fixture planted in three of its seven populations (H2 and M8 of `memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`).

## The fix

- A zero-count witness names its population: what it read, and how many of each.
- The population covers everything the guarded boundary publishes, enumerated from the boundary, not
  from where the value usually sits.
- An unresolved input or an empty population is a dead probe, never green, and "not applicable" is an
  answer of its own.
- A scan's population is what crosses the boundary it binds at. Every other boundary that publishes
  the same population registers its own scan.
- Each boundary enumerates its expected population from what it carries, so a zero against a
  non-empty expectation is a dead probe, and an empty expectation reads "none carried".
- A seen-red fixture plants the value in each population it names, one plant each, and adds one case
  per dead-probe arm.

It has no machine gate yet: dWellOiledMachine owes the secret scan built to this shape (`gap-rt-17`).

Related: `vacuous-selector-empty-population` is the same silence at a path selector.

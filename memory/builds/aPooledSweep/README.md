---
slug: aPooledSweep
node: a
opened: 2026-09-07
streams: tooling
roster: TOOL
parents: aQuenchedHarness
authorized-by: prompt
status: OPEN
ids: TOOL-aPooledSweep-1
---

# aPooledSweep — the on-demand sweep stops being serial, so the port programme stops being the only lever

## The problem this build exists to solve

`tools/run-gates/run-selftests.sh` runs 59 suites SERIALLY — `OUTER=1`, and its own header says
so deliberately — for 36146 s of declared time, about ten hours. Nobody runs it, which that file
also admits, so a kit change that guts a check lands green and `TOOL-aQuenchedHarness-9` records
suites red for an unknown length of time. The parent build's answer was to REBUILD each suite onto
a parallel harness, one suite at a time. It ported ONE of 59, carrying 208 s of the 36146, and
recorded AC5 not met. The serial loop was never the thing examined: the cost was attacked inside
each suite while the runner that adds them up ran them one after another.

## Expected improvements

- The sweep's wall clock falls toward its longest suite instead of the sum of all 59, over the
  WHOLE population rather than the 0.6% one port reached, and with no suite rewritten.
- A cost verdict is never issued from a contended reading, so a breach still names the right suite.
- Pool safety is a checked property of a suite rather than an assumption about it.

## Detriments if this is not built

- The self-tests stay a ten-hour serial run nobody executes, so kit regressions keep landing green
  and the compensating check this repo declared stays theoretical.
- The only remaining lever stays a 58-suite rewrite programme the parent build measured as
  unreachable, so the cost is never paid down at all.

## Build-level rules

- **The parent's finding is an INPUT, not prior art to re-derive.** Why the port could not finish
  is settled in this build's research record and is not re-litigated per unit.
- **No suite is rewritten in this build.** The parent's arm-inventory diff exists because a port
  that drops an arm is faster and greener at once. Touching no suite makes that risk zero by
  construction, and it is the reason this lever is cheaper than the one it supersedes.
- **A contended reading grades nothing.** This repo has measured one leg varying 5.5x median and
  47.1x worst under contention. Concurrency is admissible for the SWEEP verdict and inadmissible
  for the COST verdict, and the runner must say which it issued.
- **The composite width invariant is the runner's own**: outer x inner never exceeds the profile
  row's declared width. `run-selftests.sh` names it and instructs the re-division this build makes.
- **Withholding is not passing.** A budget nobody could grade is reported as withheld and named.
  A silently-passed budget is the green-by-absence class this repo gates in a dozen places.

## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aPooledSweep-1` | OPEN | the sweep runs its suites in a bounded outer pool |
| 2 | `TOOL-aPooledSweep-2` | OPEN | a contended reading grades no budget, and says so |
| 3 | `TOOL-aPooledSweep-3` | OPEN | pool safety is checked, not assumed |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-07 · streams tooling
ids TOOL-aPooledSweep-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aQuenchedHarness](../aQuenchedHarness/README.md)
<!-- /gen:build-edges -->

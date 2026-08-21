# Re-pricing TOOL-aShardedFloor-4 — the premise moved when the floor did

**Serves:** journal TOOL-aShardedFloor-4

Node `a` · 2026-08-21 · primary tree on `main` at `e78da2b` · two consecutive `GATE_FULL=1` bars,
width 8, profile row `capable`. Every figure below is reconstructed from `<git-dir>/gate-run/<id>/*.leg`
and its `header` — rows the bar already writes for its own reasons. No instrumentation was added.

## Why this was re-measured at all

`aScannedThrottle` priced this unit at **15.6–16.3 % of span (~160 s)**. That measurement was taken
when the bar was **FLOOR-bound**: one leg exceeded leg-seconds ÷ width, so the whole wall clock was
set by when that leg started, and a cold worktree started it 158 s late.

`TOOL-aShardedFloor-2` and `-3` sharded both `unattended` selftests and **removed that property.**
The longest leg is now below the throughput bound on every reading below. The number that justified
this unit was therefore measuring a machine that no longer exists, and re-using it would have been
building on a figure the build's own work invalidated.

## The controlled pair

Same tree, same box, consecutive, hint ABSENT then PRESENT — `aScannedThrottle` §3.1's method.

| | COLD (hint absent) | WARM (hint present) |
|---|---|---|
| span | **431.6 s** | **393.1 s** |
| leg-seconds | 3100 | 3085 |
| floor leg | 333.0 s | 335.9 s |
| its dispatch rank | 59 of 92 | **1 of 92** |
| it started at | +98.6 s | **+0.0 s** |
| throughput bound | 387.5 s | 385.6 s |
| what binds | THROUGHPUT | THROUGHPUT |
| utilization | 89.8 % | 98.1 % |
| packing | 0.90 | 0.98 |

**Delta: 38.5 s, or 8.9 % of the cold span.**

The two runs did the same work — leg-seconds differ by 0.5 % — so the comparison is between
schedules and not between workloads.

## What the numbers say

The MECHANISM is confirmed exactly as `aScannedThrottle` described it: with no hint every leg keys
0.0, the stable sort yields manifest order, and the floor leg lands at rank 59 and starts 98.6 s in.
With the hint it dispatches first, at +0.0 s. That half of the finding is untouched.

What changed is the PRICE. On a floor-bound bar, starting the floor leg 98.6 s late pushed the whole
wall clock out by nearly that much, because nothing else could fill the gap. On a throughput-bound
bar the pool absorbs most of it: packing recovers 0.90 → 0.98 and utilization 89.8 % → 98.1 %, and
what is left over is 38.5 s. **The win is real and it is roughly half of what it was.**

## Measurement hygiene, on the record

The WARM run reports `queued 621 from held` — it waited 621 s in the turnstile before dispatching.
Two things follow, and both are stated rather than assumed. First, **queue time is excluded from
span by construction**: span is reconstructed from per-leg start and end, and the wait happens before
the first leg dispatches, so neither figure above is inflated by it. Second, if anything was still
running during the warm bar, contention would have made that run SLOWER — so it biases against the
warm side, and 38.5 s is a conservative floor on the win rather than a generous reading.

That the wait is visible at all is `TOOL-aShardedFloor-1` working: before it, this run would have
been indistinguishable from an uncontended one after the fact.

## A figure this pass also corrects

`AGENTS.md` was landed at `e78da2b` stating **477 s of wall clock against a 2587 s leg-sum**. Two
full bars here do not reproduce it: 431.6 s / 3100 and 393.1 s / 3085. That reading came from a bar
run in a linked WORKTREE whose ledger did not yet know the new shard leg names, and which also went
RED on one leg — neither of which is what a landing runs. The charter now carries the warm
primary-tree reading, which is the one a `push-main` actually pays, with the cold figure beside it so
the pair is visible rather than averaged away.

Same class as everything else this build has caught: a number taken once, in the wrong conditions,
and written where it reads as authoritative.

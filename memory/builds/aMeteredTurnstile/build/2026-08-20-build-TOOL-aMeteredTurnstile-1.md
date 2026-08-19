# The merge bar, measured — what is actually slow, and what would move it

Node `a` · 2026-08-20 · base `56b945cb` · 86 legs · width 8 · `GATE_FULL=1`.

Every figure below was observed on this node in one run, or read from a file in this tree. Nothing
here is carried over from a prior build's prose. Where a number could not be captured, this report
says so rather than estimating it.

## 1. The measurement

**This run was NOT taken on a quiet machine, and the absolute figures below are inflated by an
unmeasured factor.** Process attribution during the run found at least two other worktrees running
their own bar work concurrently — `bookkeeping-convergence-build-slugs-f619ba` and
`temp-files-user-root-3e6e22` — on a node whose pool width is 8 per bar and whose core count is 16.
Legs dilate about 1.66x at 8-way even without competition (`TOOL-aTimedTurnstile-3`), and a leg has
been measured at 82s wall on 6s of CPU under four concurrent bars (`TOOL-aPromptedMandate-9`). What
survives contamination is the SHAPE — which legs dominate, and by how much relative to each other —
because every leg paid the same tax. The absolute minutes do not survive it and are not offered as a
baseline.

The run was started at 00:47 and stopped by hand at 01:35 because it had not finished. Per-leg
completion times survive as `<git-dir>/gate-logs/*.log` mtimes, which the runner writes at each leg's
end. That is the dataset below.

| Observation | Value |
|---|---|
| Legs in the manifest | 86 |
| First leg to report anything | **+9.3 min** |
| Legs finished at +25 min | 67 of 86 |
| Legs finished at +27.4 min | **84 of 86** |
| `unattended driver selftest` finished | **+47.7 min** |
| `unattended gate selftest` | **never finished**; killed at ~+48 min |

The completion curve, cumulative:

```
 +1 min    0/86      +15 min    7/86      +26 min   79/86
 +5 min    0/86      +20 min   17/86      +27 min   83/86
+10 min    2/86      +25 min   67/86      +28 min   84/86
```

**84 of 86 legs complete in 27 minutes. Two legs add at least another 21 minutes on top of that, and
one of them had still not finished after 48.** The bar is not uniformly slow. It is two legs.

Per-leg durations were not captured for this run: the runner writes `gate-timings.tsv` only after
every leg returns, and the run was killed before that point. The completion timeline above is the
measurement; the durations are not, and are not reported as if they were.

## 2. Why the repo could not already answer this

The only longitudinal artifact is `<git-dir>/gate-timings.tsv`, and it is a dispatch hint that was
correctly built as one and incorrectly read as a profile.

- Its schema is `name` and `seconds`. No run id, timestamp, width, sha, host, exit code or guard
  state. A row cannot be attributed to a run or ordered in time.
- It is last-write-wins into one slot per leg. A serial run and a width-8 run overwrite each other,
  and legs dilate about 1.66x at 8-way (`TOOL-aTimedTurnstile-3`), so one cell holds two different
  measurements of two different things.
- Orphan rows are never evicted. The carry-forward predicate is "did this run measure it", never
  "does the manifest still declare it". Measured on the primary tree: 88 rows against 85 legs at the
  time, 3 orphans holding 965s, which inflates a naive sum of that file by 12%.
- The comment at `run-gates.sh:287` says a dropped leg "falls out on its own". That is TRUE of the
  dispatch order, which iterates the manifest, and FALSE of the file, whose writer has no manifest
  knowledge. The claim about the write path is sourced from the read path, eight lines away.
- 49 of 86 legs carry a guard, so a diff-scoped run refreshes a minority and the rest age silently.
- The record is fragmented one-per-git-dir. This node has **24 worktrees**, so up to 24 divergent
  caches. This worktree's held 55 rows with 34 manifest legs unknown to it and an mtime four days
  old; the primary tree's held 88.

Consequence for the question that opened this session: the primary cache's 1997s and 1710s for the
two unattended legs, against 659.9s and 634.6s recorded two days earlier, are **not** evidence of a
3x regression. They are incomparable cells from different runs at different load.

## 3. What is actually making it slower over time

**The bar leaks scratch git repositories into `TMPDIR`, and never cleans them.**

Counted this session under `/tmp`:

| Created | Leaked scratch dirs |
|---|---|
| 2026-08-17 | 40 |
| 2026-08-18 | **531** |
| 2026-08-19 | 182 |
| 2026-08-20 | 33 |
| **Total** | **786** |

Sampled contents confirm the attribution — they hold `.git`, `.memory-tree.conf` and `tools/`, which
is the shape a gate self-test builds. `run-gates.sh` traps and removes its own `$WORK`, but a leg
killed or wedged mid-run leaves the scratch repo it built.

This is a compounding cost, not a tidiness complaint. `TMPDIR` on this node is
`C:\Users\...\AppData\Local\Temp`, every heavy leg calls `mktemp -d` there, and on Windows that
directory is scanned by real-time antivirus. **`du -sh /tmp` did not complete within four minutes**
during this session. Every leg that creates a scratch repo pays that traversal, every run, and the
cost grows with every leg that ever died.

That is the most credible mechanism for "it is getting slower", and it is the cheapest to fix.

## 4. The other structural findings

**Longest-first dispatch maximises time-to-first-signal.** The runner sorts legs longest-first from
the timing cache. With 8 slots filled by the 8 longest legs, no leg can report until the eighth
longest returns. Measured: **zero legs reported for the first 9.3 minutes**, and 17 of 86 at +20 min,
then 50 more in the following 5 minutes. The scheduling is near-optimal for makespan and near-worst
for an operator deciding whether to keep waiting.

**There is no per-leg deadline.** `TOOL-aBoundedVerdict-10` already records `unattended driver
selftest` wedging the whole bar with zero output past 240s. Reproduced here: it took 47.7 minutes,
and its sibling never returned. Because nothing bounds a leg, the bar's wall clock is unbounded, and
a wedge is indistinguishable from slow work in the timing cache afterwards.

**The bar is spawn-bound on this platform.** Recorded on node `a`: `python -c pass` at 103.7ms,
`bash -c true` at 22.5ms (`TOOL-aTimedTurnstile-4`). The two heavy legs are heavy because of fan-out,
not computation — `unattended.test.sh` issues about 118 full `--preflight` driver invocations, each
building its own scratch repo.

**`sum(leg seconds)` under-counts wall clock, systematically.** The runner brackets only the leg's own
argv. Excluded from every recorded duration: the python launcher probes, the manifest parse, the
serial guard pass of 49 `git diff` calls, the per-leg log write and redact pipeline at two processes
per leg, every `jobs -rp | wc -l` fork in the dispatch loop, and the final cache merge. A profile
built by summing that file reports a flattering number while wall clock grows.

**One leg reaches the network on every run.** `unattended kit gate` makes two HTTPS `ls-remote` calls
and carries no guard, so it runs even on a pure-records bar. Its verdict is a function of the remote
as well as of the tree.

**A SessionStart hook can inject load into a measured run.** `.claude/settings.json` runs
`check-wiring.sh --session` on every session start, and that script was measured at 1m22s under four
concurrent bars (`TOOL-aPromptedMandate-9`). An agent session opening mid-run contaminates it. This
is reported as an observed configuration fact, not acted on.

## 5. Recommendations for this repo

Ordered by measured value per unit of work. Each names the id it belongs to.

| # | Recommendation | Belongs to | Why it is where it is |
|---|---|---|---|
| G1 | Sweep `TMPDIR` of leaked scratch repos, and give every leg's `mktemp -d` an EXIT trap so a killed leg cleans up | new row | 786 leaked dirs; `du` of the tree exceeds 4 min. Cheapest fix, largest compounding win |
| G2 | Give the runner a per-leg deadline that kills and reports the leg rather than the run | `TOOL-aBoundedVerdict-10` | wall clock is unbounded today; one wedge cost this run 21+ min |
| G3 | Shard the two unattended selftests | `TOOL-aPacedTurnstile-8` | they alone are 78% of the wall on top of the other 84 |
| G4 | Evict timing-cache rows on the manifest, not on the run | new row | 3 orphans, 965s, 12% inflation, and the misleading comment at `run-gates.sh:287` |
| G5 | Emit a progress signal before the first leg returns | `TOOL-aPacedTurnstile-3` | 9.3 minutes of silence is what makes the bar feel broken rather than slow |
| G6 | Correct the stale figure in `AGENTS.md:492` | new row | it claims 335s serial to ~95s at width 8, measured at 47 legs; there are 86, and this run exceeded 48 min |

G1 and G2 are the two that change the experience. G3 is the only one that changes the floor, and it
is already specced as its own build that does not yet exist.

## 6. Recommendations for adopters

These are properties of any bounded-pool gate bar and carry no assumption about this repo's legs.

- **Compute the regime before optimising anything.** A bar has two independent lower bounds: the
  longest single leg, and total work over the pool width. Whichever is larger is the regime. On a
  floor-bound bar, adding workers and trimming small legs both buy exactly zero, and that is where
  most optimisation effort goes.
- **Never read a dispatch hint as a performance record.** If the file has no run id and no timestamp
  it cannot answer a trend question, and it will look like it can.
- **Evict on the declared population, not on the last run.** A carry-forward keyed on "did this run
  measure it" accumulates rows for things that no longer exist, forever.
- **Give every leg a deadline.** Without one, a single stall makes the wall clock unbounded, and
  afterwards a wedge is indistinguishable from expensive work.
- **Make every scratch directory self-cleaning under a trap.** A leg that dies without cleaning up
  leaves a cost that every later run pays, and on a platform with real-time antivirus that cost
  grows superlinearly with the temp directory.
- **Never pin a gate assertion to a wall clock.** Assert order and classification, which are
  properties of the runner. Send the seconds to a report.
- **Measure spawn cost beside the bar.** On a spawn-bound bar, "slower" usually means the platform
  got slower per process, not that the bar grew.
- **Report time-to-first-signal as its own number.** Longest-first dispatch optimises makespan and
  pessimises feedback; both matter, and only one of them is usually measured.

## 7. What this report does not establish

- Per-leg durations for this run. The run was killed before the cache write, deliberately.
- Whether the two unattended legs are slow or intermittently wedged. Both were observed; which one
  dominates is unresolved, and `TOOL-aBoundedVerdict-10` holds the wedge half.
- Any antivirus contribution. It is named as a lever in `TOOL-aTimedTurnstile-4` and is unquantified
  anywhere in this tree, including here.
- A clean absolute baseline. The machine was not quiet: at least two other worktrees ran bar work
  throughout, and the profiler was killed before it could write its own record of that condition. The
  relative shape holds; the minutes do not. A quiet-machine rerun is the obvious follow-up and is the
  reason the instrument now exists.
- Whether killing the bar kills its legs. It does not — stopping the wrapper left roughly 100 bash
  descendants running, including one dating to the run's own start. Not pursued here, and not
  cleaned up, because the same process population contains other sessions' live work and this unit
  will not kill what it cannot attribute.

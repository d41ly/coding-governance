# The lander is floor-bound — measurement, findings, recommendations

**Serves:** journal TOOL-aScannedThrottle-1

Node `a` · 2026-08-20 · base `4773902` · streams tooling · slug `aScannedThrottle`

> The owner reports the lander is extremely slow and does not use the machine, and names the canary
> gates as a congestion target. The first half is true and this report quantifies it. The second half
> is not: `run-gates canary` costs 466–587 s and deleting it entirely moves the bar's wall clock by
> **0.0 %**, because the bar's span is set by a leg that is not the canary.

## 1 · Method, and why it costs nothing to repeat

`aMeteredTurnstile` gave the runner a per-leg run record under `<git-dir>/gate-run/<id>/`. Each
`<i>.leg` row carries that leg's own start and end **in nanoseconds**, and the header carries the
resolved width and the dispatch order. A bar's entire schedule is therefore reconstructable after
the fact, with no instrumentation, no re-run and no perturbation. Every number in §2 and §3 comes
from records four real bars had already written before this session started.

Three tools were written to read them, all in the session scratchpad, none installed:

| tool | what it answers |
|---|---|
| `gantt.py` | span, leg-seconds, floor, throughput, utilization, packing, occupancy histogram |
| `dispatch.py` | where the floor leg sat in the dispatch order and when it actually started |
| `sim.py` / `sim2.py` | LPT list-schedule simulator: what each candidate fix would buy |

The simulator **refuses itself** when it cannot reproduce the run it is built from. That refusal is
what found the largest finding in this report — see §3.1.

## 2 · What four real bars measure

All `GATE_FULL=1`, profile row `capable`, width 8, node `a` (16 cores / 32693 MB).

| run (local) | span | leg-seconds | floor | utilization | packing | verdict |
|---|---|---|---|---|---|---|
| 14:44 | 970.0 s | 4644 | 812.1 s | 59.8 % | 0.84 | RED |
| 15:07 | 925.5 s | 5144 | 925.5 s | 69.5 % | **1.00** | GREEN |
| 15:38 | 1051.4 s | 5245 | 887.9 s | 62.4 % | 0.84 | RED |
| 16:05 | *in flight while this was written* | | | | | |

**Every run is FLOOR-bound**: the single longest leg exceeds leg-seconds ÷ width. That one fact
decides everything below. It means the bar's wall clock is set by one leg, and no scheduling
change, no extra worker and no faster sibling leg can move it.

Occupancy for the 15:38 run — wall seconds at each concurrent-leg count, width 8:

```
 1 busy    42.1s   4.0%  ##
 2 busy   274.7s  26.1%  ###############
 3 busy   156.1s  14.8%  ########
 4 busy    80.3s   7.6%  ####
 5 busy     2.6s   0.2%
 6 busy     8.1s   0.8%
 7 busy    96.8s   9.2%  #####
 8 busy   390.6s  37.2%  ######################
```

**52.6 % of the run has four or fewer of eight workers busy, and 26 % has exactly two.** That is the
owner's "does not use the machine", and it is not a pool defect — it is the two `unattended`
selftests running alone in a long tail after everything else has finished.

Top legs, 15:38 run:

| leg | seconds | share of leg-seconds |
|---|---|---|
| unattended driver selftest | 887.9 | 16.9 % |
| unattended gate selftest | 849.0 | 16.2 % |
| **run-gates canary** | **533.7** | **10.2 %** |
| run-gates evidence | 344.3 | 6.6 % |
| memory-hygiene self-test | 338.6 | 6.5 % |
| manifest-check self-test | 327.6 | 6.2 % |
| run-gates turnstile | 232.5 | 4.4 % |
| check-wiring self-test | 201.4 | 3.8 % |

## 3 · Findings

### 3.1 · The dispatch hint is per-worktree, was renamed without migration, and 24 of 26 worktrees have none

**This is the largest finding and the cheapest fix.**

The simulator reproduced the 15:07 run to **+0.0 %** and the 15:38 run to **−15.6 %**, and refused
the second rather than reporting a what-if against a model that did not fit. The gap is exactly the
floor leg's start offset.

`run-gates.sh:620-647` sorts legs longest-first using durations read from `$TIMINGS`, which is
`$LEDGER`, which is `<git-dir>/gate-ledger.tsv`. A leg the cache does not know scores `0.0`, and
Python's `sorted` is stable — so **an absent cache yields manifest order, silently**. There is no
signal on the run that the hint was unavailable.

Two consecutive runs in one worktree make a controlled pair. Nothing changed between them but the
existence of the ledger the first one wrote:

| | 14:44 (no ledger) | 15:07 (ledger present) |
|---|---|---|
| first 8 dispatched | manifest indices 0–7, costing 1.0–5.7 s each | the two 900 s legs, slots 1 and 2 |
| floor leg's dispatch rank | **55 of 87** | **1 of 87** |
| floor leg starts at | **+157.9 s** | **+0.0 s** |
| floor leg duration | 812.1 s | 925.5 s *(14 % slower)* |
| **span** | **970.0 s** | **925.5 s** |
| packing | 0.84 | **1.00** |
| utilization | 59.8 % | 69.5 % |

The second run's floor leg was **14 % slower** and its span was still **44.5 s shorter**. The
start delay is 157.9–163.5 s across the two badly-scheduled runs, **15.6–16.3 % of span**.

Now the reach. `$gd` is `git rev-parse --git-dir`, which for a linked worktree is
`.git/worktrees/<name>/`, so the ledger is **per-worktree** and never shared. Census of this node:

| state | worktrees |
|---|---|
| has `gate-ledger.tsv` (good dispatch) | **2** |
| has only the legacy `gate-timings.tsv`, which the runner no longer reads | **9** |
| has neither | **15** |

The cache was renamed `gate-timings.tsv` → `gate-ledger.tsv` and the old data was never migrated.
`.git/gate-timings.tsv` still sits there with 88 rows, last written 13:30, read by nobody. So
**every fresh worktree, and every worktree that has not completed a full bar since the rename, pays
the full ~160 s penalty** — and in this repo's workflow a fresh worktree is what every new unit
starts in.

Two fixes, both small, not exclusive:

1. **Read the ledger from the git COMMON dir**, not the per-worktree dir. Leg durations are a
   property of the repository, not of a checkout. The runner's own comment at `:388` already draws
   this line for the turnstile — *"evidence is per-worktree, contention is per-repository"* — and a
   dispatch hint is neither evidence nor contention; it is a shared, advisory, last-write-wins
   scheduling fact. Bars are serialised per repository by the turnstile, so concurrent writers are
   already excluded on the common path.
2. **Fall back to the legacy filename on read**, so the nine worktrees holding `gate-timings.tsv`
   recover their hint without running a bar first.

A third, independent of both: **say when the hint is missing.** A bar that dispatches in manifest
order because it found no cache currently looks identical to one that found a good cache. One line
on the profile line would have made this finding visible the day the rename landed, instead of
costing 16 % of every cold run silently. This is the repo's own "a probe that cannot move says so"
rule, applied to a scheduling input.

**Also, as a side effect: the orphan-row inflation on `gate-timings.tsv` is now moot for dispatch
but not for anyone reading it as a profile.** It carries three rows for legs that no longer exist
(`memory hygiene (20 checks)` 813.0 s, `marker contract (4 readers)` 131.3 s, `verifier fan-out
(≤5 verify agents per review)` 19.9 s) totalling **964.2 s**, which inflates any sum taken from it
by 23 %. That is `TOOL-aMeteredTurnstile-3`, still true, and now attached to a file nothing reads.

### 3.2 · The canary is not on the critical path, and the owner's target is the wrong one

Validated simulator (0.0 % error on the 15:07 run), width 8:

| change | span | delta |
|---|---|---|
| as measured | 925.5 s | — |
| canary work −25 % | 925.5 s | **+0.0 %** |
| canary work −50 % | 925.5 s | **+0.0 %** |
| canary work −90 % | 925.5 s | **+0.0 %** |
| **canary leg DELETED entirely** | **925.5 s** | **+0.0 %** |

The canary costs 466–587 s of real work and contributes **nothing** to the bar's wall clock,
because it runs inside the shadow of a 925 s leg. It is expensive; it is not congestion.

Attacking it only pays **after** the two `unattended` selftests are sharded:

| change | span | delta | bound |
|---|---|---|---|
| as measured | 925.5 s | — | FLOOR |
| shard both unattended selftests ×4 | 643.4 s | **−30.5 %** | THROUGHPUT |
| + canary work −50 % | 606.6 s | −34.5 % | THROUGHPUT |
| + every heavy leg −30 % | 547.5 s | −40.8 % | THROUGHPUT |
| + a further −20 % on every leg | 483.2 s | −47.8 % | THROUGHPUT |

Note the distinction the middle rows depend on: **sharding splits work, it does not remove it.**
Sharding the canary into 4 buys −0.0 % even after the floors are sharded, because the bar is then
throughput-bound at leg-seconds ÷ 8 and splitting changes neither term. Only making the canary
genuinely cheaper moves it.

### 3.3 · Width is a dead lever, and the table is right to cap it

| width | modelled span |
|---|---|
| 1 | 5144.0 s |
| 4 | 1286.2 s |
| 8 | 925.5 s |
| 12 / 16 / 24 / 88 | **925.5 s** |

Past 8 the model gains exactly nothing, because the bar is at its floor. And measured reality is
worse than the model: `TOOL-aMeteredTurnstile-6` records width 24 running **26 % slower** than
width 8 on this node, because the contended resource is process creation rather than CPU. Raising
`width=` in `gate-profiles.txt` is not a fix, and the table's declared 8 is correct.

### 3.4 · The lander's queue wait is real, is often the largest single component, and is recorded nowhere

Every span in §2 measures **first leg start → last leg end**. It excludes the turnstile.

`run-gates.sh:378-518` serialises **one bar per repository** across every worktree on the node — the
key is the git *common* dir, so all 26 worktrees here share one beacon. A lander arriving while a
peer holds it waits for the peer's whole bar. With a service time of 925–1051 s, a lander that
queues behind one peer experiences **~31–35 minutes**, and every span in this report reads it as
~16.

The serialisation is *correct* — `TOOL-aMeteredTurnstile-6` measured three concurrent bars at 39 %
CPU with both queues empty and width 24 running 26 % slower than width 8, so two concurrent bars
really are worse than two sequential ones on this node. The problem is not the queue. It is that
**the wait leaves no trace**:

- `run-gates.sh:518` prints `gate queue: waited Ns` to **stdout only**.
- `$gd/gate-queue-status` exists **only while waiting** and is deleted at `:505` the moment the bar
  starts.
- The run-record header has 19 keys and **none of them is the queue wait**.
- `gate-last-summary.txt` carries the profile line, the chunk roll-up and the verdict. Not the wait.

So the component of lander latency the owner actually feels is invisible to every measurement this
repo can take, including this report. Adding one `queued\t<n>` key to the run-record header at
`:708-737` would make it measurable; `profile_bar.py` already reasons about queue time and cannot
see it either.

Partial arrival census (the last five records per worktree — `GATE_RUN_KEEP=5` has swept the rest),
full bars, UTC: `11:44:16`, `12:07:52`, `12:38:54`, `13:05:47`. Inter-arrival 23.6 / 31.0 / 26.9 min
against a 15.4–17.5 min service time, so the turnstile runs near **60 % utilization** — high enough
that queueing is routine, not exceptional.

### 3.5 · The reds are real defects, not flakes — I checked, and my first reading was wrong

Two of the four recorded full bars are RED, and my first instinct was a flaky timing-sensitive leg
taxing every lander. **That is not what the records say.** Per-leg statuses across all four runs:

| run | head | failed legs |
|---|---|---|
| 14:44 | `b720fc79d` | `run-gates evidence`, `method carriers`, `playbook render wiring` |
| 15:07 | `a98a42f82` | none |
| 15:38 | `4773902fb` | `run-gates turnstile`, `run-gates gov canary` |
| 16:05 | `e6098aa43` | none |

**No leg failed in more than one of four runs.** The two RED bars sit at mid-build commits; the two
at settled heads are clean. The 15:38 pair is the missing-`chunk`-key defect of §3.10, fixed
upstream. `run-gates evidence` and `run-gates turnstile` each failed exactly once, at different
commits, for unrelated reasons.

So there is **no red-bar multiplier on lander cost**, and `TOOL-cFinalBerth-5`'s flip-flopping
`par*2 < ser` ratio did not reproduce in this sample. The bar was doing its job. Recorded because
"two of four bars are red" is a number that invites the wrong conclusion, and I drew it before
checking.

### 3.6 · Why the canary costs what it costs

Static inventory of `tools/run-gates/run-gates.test.sh` (1090 lines):

- **~23 nested invocations of the real `run-gates.sh`**, each in its own scratch repo: 4 via
  `run_scratch` (`:229`) and 19 via `runp` (`:583`, 17 call sites of which two sit in 2-iteration
  loops). Each nested run pays the full runner startup — python resolve, profile-table parse,
  turnstile ticket, porcelain walk, fingerprint, run-record header. The runner's own comment at
  `:600-606` measures 2136 ms to header-on-disk *in a two-file scratch repo*.
- **A rendezvous preamble that is a process storm.** `:186-215`: every fixture leg polls up to
  `RVWAIT_TICKS=30` times, and each tick runs `$(ls … | grep -c .)` plus `sleep 0.1` — a subshell
  fork plus three execs, so **up to ~4 process creations per tick per leg**. Four fixture legs × 30
  ticks = **up to 480 process creations per nested run**. The width-1 negative control never reaches
  its `peak >= 4` break condition, so it burns every tick.
- **Deliberate sleeps.** Fixtures sleep 2.0 / 1.5 / 1.5 / 1.5 s (`:213-214`), and the timeout arms
  use `sleeper.sh` (a 20 s foreground sleep plus a 20 s orphan, `:570`) and `stubborn.sh` (`trap ""
  TERM; sleep 25`, `:575`). One arm runs `sleeper` against a *loose* table, so it sleeps the full
  20 s by design.

The canary is expensive for a defensible reason — it is the only thing that tests the runner against
the real runner — but the cost is dominated by process creation, which is precisely this node's
scarce resource. See §4 R4 for the cheap half of the fix.

## 3.7 · The canary, traced: 72 % of it is five lines

Measured on a quiet box after the peer bar released the beacon at 16:23:37. `bash -x` with
`PS4='+${EPOCHREALTIME} …:${LINENO} '`, 1217 trace records, **99.9 % of wall attributed** (0.3 s
unattributed). The gap between record *i* and *i+1* is time spent inside record *i*'s command, which
is where a nested `run-gates.sh` and a `sleep` both land.

| wall held | line | what it is |
|---|---|---|
| **88.7 s** | `:458` | 4 reps × a **30-leg width-1** nested run — the reader-race arm |
| **57.5 s** | `:583` | `runp()` — **19** nested 2-leg runs, the profile-table arms |
| **55.7 s** | `:229` | `run_scratch()` — **4** nested 4-leg runs with the rendezvous preamble |
| **23.3 s** | `:743` | `sleeper` against the *loose* table — a deliberate 20 s sleep |
| **21.2 s** | `:395` | the width-clamp arms, timeout-bounded |
| 246.4 s | | **= 72 % of the 341.5 s traced run** |

Two numbers fall out of this that are worth more than the breakdown itself.

**Runner overhead is ~1.5 s fixed + ~0.74 s per leg.** `:458` runs 30 legs of literally `exit 0` at
width 1 in 22.2 s per rep; `:583` runs 2 such legs in 3.03 s. Solve the pair: fixed ≈ 1.5 s, per-leg
≈ 0.74 s. That per-leg figure is `runleg()`'s own machinery — two `date +%s%N`, the leg, `cat`, the
`redact` sed, two `chmod`, `input_key()`'s `git ls-files` + greps + `git hash-object`, and the atomic
`mv` — roughly 12–15 spawns at the 32–48 ms measured below.

**On the real bar that overhead is 1.3 % and not worth touching**: 88 legs × 0.74 s ≈ 65 s of 5144
leg-seconds. I had suspected `live()` at `:922` (`jobs -rp | wc -l`, a subshell fork plus an exec, in
a loop condition) was a significant cost. It is not, at bar scale. **Inside the canary it is half the
leg**: ~150 nested legs × 0.74 s + 23 startups × 1.5 s ≈ 145 s of the canary's 317 s.

So the canary is not slow because it is badly written. It is slow because it runs the real runner
~23 times, and the runner costs 1.5 s to start.

### 3.8 · The spawn tax has recovered, and `TOOL-aMeteredTurnstile-6` needs refining, not closing

Median of 15, quiet box, 16:23:57:

| op | 2026-08-11 baseline | `-6`'s degraded reading | **measured now** |
|---|---|---|---|
| `bash -c true` | 22.5 ms | 581 ms | **32.5 ms** |
| `git rev-parse` | 23.9 ms | 727 ms | **48.0 ms** |
| `python -c pass` | 103.7 ms | 1297 ms | **151.2 ms** |
| `mktemp -d` + `git init` | — | 2751 ms | **158.1 ms** |

Process creation is back within ~1.5× of the August-11 baseline, and `git init` is **17× faster**
than the degraded reading. `TOOL-aMeteredTurnstile-6` concludes *"serialized per-op latency, not
contention"* on the strength of CPU at 39 % with empty queues. That conclusion does not survive
this: the degraded readings were taken under four concurrent bars, and on a quiet box the same ops
are near baseline. The tax is **load-dependent after all**. Whatever the mechanism (Defender
scanning a burst of short-lived processes is the standing hypothesis), it manifests only under
concurrency — which is exactly what the turnstile now prevents.

That REFINES the row rather than closing it, and it demotes "chase the spawn tax" well down the
list: on a serialised, quiet box the tax the bar actually pays is much smaller than the backlog
believes.

### 3.9 · Measurement hygiene — two contamination events, both on the record

1. **A background job survived `TaskStop`.** The first measurement driver was stopped as a tracked
   task at 16:07, but its detached `bash` kept running and resumed at 16:32:09, starting a *second*
   canary at 16:32:16. The traced run spanned 16:29:22–16:35:04, so **its last ~172 s were
   contended**. The untraced baseline (317.4 s, 16:24:03–16:29:20) was clean; the traced run reads
   341.5 s, and the ~7 % gap is consistent with that overlap plus xtrace overhead. The line-level
   *proportions* are unaffected — contention dilates everything roughly uniformly.
2. **The first driver's quiet-box predicate matched its own wrapper shell.** It counted `bash`
   processes whose command line matched `run-gates|unattended`, and every shell this session used to
   *discuss* those names matched it — so it reported `peers=8` on an idle box and waited 1500 s for
   nothing. This is the repo's own `inputs-inside-the-subjects-reach` class. The replacement waits on
   the turnstile beacon directory, which the subject cannot forge.

**A dilation factor worth keeping:** the canary costs **317 s standalone** and **466–587 s inside
the bar at width 8**, i.e. it dilates **1.5–1.85×** under the pool's own load. That confirms
`TOOL-aTimedTurnstile-3`'s 1.66× figure at the current leg count, and it means every standalone leg
timing understates the bar by roughly half again.

### 3.10 · One red found, already fixed upstream

`run-gates gov canary` **failed** in 1.37 s at base `4773902`: `scratch-guard self-test` carries no
`chunk` key, and the gov canary requires one of six declared names. This is real at that base and
**already fixed** — `origin/main` has since advanced to `e6098aa`, which adds `"chunk":
"selftests"`. Not a new finding; recorded because a reader of this report will otherwise reproduce
the red and think it is one. (`origin/main` moved during this session: the peer's lander landed and
pushed while the measurements were running.)


## 4 · Recommendations, ranked by measured span reduction per unit of effort

A five-lens adversarial pass produced 55 findings; 28 survived a skeptic prompted to refute, and 8
of those touch the critical path. The ranking below is the survivors, ordered by what the validated
simulator says they buy. **Every entry states what it buys in seconds of span, or states zero.**

### R1 — Share the dispatch hint across worktrees, and pair it with time-to-first-signal

**Buys ~160 s (15.6–16.3 %) on any cold worktree, which today is 24 of 26.** `TOOL-aScannedThrottle-1`.

Three parts, and the third is not optional:

1. Read the ledger from the **git common dir** with a per-worktree fallback, so a fresh worktree
   inherits the repository's scheduling knowledge instead of dispatching in manifest order.
2. **Fall back to the legacy `gate-timings.tsv` filename on read**, recovering the nine worktrees
   that still hold one.
3. **Say when the hint is missing.** One clause on the profile line. This is the repo's own rule
   that a probe which cannot move must say so, applied to a scheduling input.

**The trap, and it is why this is not a pure win.** With a warm ledger the eight longest legs fill
all eight slots at t=0 and *nothing reports for 669.1 s* — measured. With a cold ledger the first
verdict lands at **5.1 s**. That is a **131× swing in time-to-first-signal decided solely by ledger
warmth**, and it confirms `TOOL-aMeteredTurnstile-5`. Fixing dispatch makes the bar 16 % faster and
makes it *feel* far worse: eleven minutes of silence in place of five seconds.

So R1 should ship with a reserved slot — dispatch longest-first into `width-1` workers and keep one
worker pulling shortest-first. Makespan is unchanged, because the floor leg still starts at t=0, and
the first verdict still lands in seconds. Without that, R1 trades a real 16 % for a perceived
regression, and the complaint that started this build is about *perceived* latency.

### R2 — Shard both `unattended` selftests. Both, into two.

**Buys 292 s (27.6 %) on run 130546, 282 s (30.5 %) on run 120751.** `TOOL-aPacedTurnstile-8`, already
open — raise it above everything else here.

The two legs are 33.1 % of all leg-seconds and the larger one *is* the floor. Three numbers decide
how to do it:

- Sharding the **driver alone buys 38.9 s (3.7 %)** — the gate selftest just becomes the new floor.
  Both must move together or the work is wasted.
- **Two shards each is sufficient.** Past that the bar is throughput-bound at ~766 s and further
  splitting buys exactly zero. Target the crossover, not a floor number.
- Each split adds ~2.75 s of leg-seconds, one fresh scratch repo per shard.

Seam guidance from the source: `check-unattended.test.sh` is the cleaner candidate, because its
`reset_tree` (`:118-124`) restores the ref namespace and its arms are genuinely independent.
`unattended.test.sh` is **one scratch repo by design** and its header says why, so price that before
splitting it — its 233 driver invocations through `run()` (`:171`) share the fixture.

### R3 — Record the turnstile queue wait

**Buys 0 s of span, and is the only way to see the largest component of the complaint.**
`TOOL-aScannedThrottle-2`.

A lander queueing behind one peer experiences ~31–35 min where every span in this report reads ~16.
One `queued` key in the run-record header at `run-gates.sh:708-737` fixes it. `profile_bar.py`
already reasons about queue time and cannot see it either.

### R4 — Measure Defender before excluding anything

**Buys UNQUANTIFIED, and the honest answer is probably less than you would hope.**
`TOOL-aScannedThrottle-3`.

Verified on this node: real-time protection, behaviour monitoring, on-access and script scanning all
ON; Defender is the only AV and there is no EDR sensor; **zero exclusions confirmed**, because
`Get-MpPreference` returns *"N/A: Must be an administrator to view exclusions"*. The closest
third-party measurement of *this exact workload shape* — parallel Bash calls driven by an agent on
Windows — got **64.78 s → 7.58 s, 8.5×**, by excluding two Git-for-Windows folders.

**The skeptic refuted the cost on this repo's own anchor, and it is right to.** On 2026-08-11 this
same node measured `bash -c true` at 22.5 ms *with Defender on and unexcluded*. Exclusions cannot
recover a regression that Defender was not causing then. §3.8 reaches the same place from the other
side: on a quiet box today the tax is already near baseline.

The step that produces a local number instead of a borrowed one:

```powershell
New-MpPerformanceRecording -RecordTo bar.etl
Get-MpPerformanceReport -Path bar.etl -TopPaths 20 -TopProcesses 20
```

Do not add exclusions before that names something.

### R5 — Establish when HVCI was enabled (a discriminator, not a fix)

**Buys 0 s directly; decides whether a whole branch is worth exploring.** `TOOL-aScannedThrottle-4`.

Verified: `Win32_DeviceGuard` reports `SecurityServicesRunning=2`,
`VirtualizationBasedSecurityStatus=2` and `CodeIntegrityPolicyEnforcementStatus=2` (Enforced) — HVCI
is **on and enforcing** on OS build 26200. Microsoft's own Q&A carries a third-party report of a
**3–7× CreateProcess slowdown** on exactly this shape, a parent repeatedly spawning short-lived
children and capturing their output, with Microsoft staff attributing it to *synchronous* antimalware
inspection of new processes under Device Guard and ETW counts to match. That thread is unresolved.

Strong mechanism, weak explanation, for one reason: **if HVCI was already on during the 2026-08-11
baseline it explains nothing about a regression.** Find the enablement date first. It is the owner's
setting either way — an agent should not be flipping Memory Integrity.

### R6 — The canary, and only after R2

**Buys 0 s today. After R2, halving it buys ~37 s (4 %).** `TOOL-aScannedThrottle-5`.

Stated plainly, because it is the opposite of the premise this build started from: **deleting the
canary outright changes the bar's wall clock by 0.0 %.** It is not on the critical path and cannot be
put on it by splitting — splitting divides work without removing it, and after R2 the bar is
throughput-bound, where only removed work counts.

If it is ever worth attacking, §3.7 says where: the 20 s deliberate sleep at `:743`, where the
loose-table control could use a shorter fixture and a proportionally shorter timeout;
`RVWAIT_TICKS=30` at `:198`, where the width-1 run can never reach its `peak >= 4` break and so
burns all 30 ticks across 4 legs; and the 4 reps at `:458`. Leave the last one — its comment records
a 1-in-40 race and explicitly forbids simplifying it.

### Dead ends — measured, so nobody re-explores them

| lever | why it is dead |
|---|---|
| raise `width` past 8 | 0 % modelled, because the bar is at its floor, and **−26 % measured**: width 24 ran *slower* than width 8. The table's declared 8 is correct. |
| Dev Drive / ReFS | No ReFS volume exists; **C: cannot be converted** and there is no unallocated space; one physical disk, so a VHDX shares the same array. Independent measurement of a real build toolchain spans **−62 % to +75 %**, i.e. not sign-determinate. Scratch creation is ~1.5 % of the floor leg. |
| per-leg runner overhead (`live()` at `:922`, `input_key()` at `:684`) | Real — 750 process creations per run, 140 of them git — but **1.3 % of bar leg-seconds**. I suspected `live()` mattered. At bar scale it does not. |
| the canary, before R2 | 0.0 %. See R6. |

### Already fixed upstream — do not re-report

Both reds at base `4773902` were fixed by `e6098aa` ("the landing bar's two reds — an integration
catch and a relative path"), which landed while this build was measuring:

- `scratch-guard self-test` carried no `chunk` key, reddening `run-gates gov canary`.
- `run-gates.turnstile.test.sh:275` compared **raw** `git rev-parse --git-common-dir` strings. From
  the primary tree that prints the literal `.git`, and a scratch repo prints `.git` too — so the arm
  was RED for **every bar run from the primary tree**, which is exactly where `push-main.sh` requires
  you to be. Confirmed by direct reproduction and by the run records: the primary-tree run at
  `4773902` failed this leg, the primary-tree run at `e6098aa` passed it. The fix resolves both sides
  through `cd … && pwd`.

The second deserves a note. Its failure message claimed nested legs would deadlock on the real
beacon, and that was **false** — `run-gates.sh:392` already resolves absolutely. A gate that reds the
landing bar while giving a wrong reason is worse than one that reds silently.

## 5 · Records to update

| id | action | why |
|---|---|---|
| `TOOL-aPacedTurnstile-8` | **KEEP OPEN, raise to top** | The one change that moves the span. Re-stamp to the crossover target of ~766 s rather than to a floor number. |
| `TOOL-aMeteredTurnstile-6` | **REFINE** | The tax is **load-dependent**, not standing: quiet-box readings sit within ~1.5× of the 2026-08-11 baseline and `git init` is 17× faster than the degraded figure. The row's "not contention" conclusion does not survive §3.8. |
| `TOOL-aMeteredTurnstile-3` | **REFINE** | The **live ledger is clean** — 0 orphans, 88 rows against 88 legs. The 964.2 s of orphan rows sits in the dead `gate-timings.tsv`, which nothing reads. Mechanism real, instance gone. |
| `TOOL-aMeteredTurnstile-2` | **KEEP OPEN** | Worse than recorded: **1053** scratch dirs against the row's 786, +34 %, with 291 created today. `run-gates.sh:520` never sets `TMPDIR`, and one export would redirect all 63 `mktemp -d` sites. |
| `TOOL-aMeteredTurnstile-4` | **KEEP OPEN** | `AGENTS.md` still states an 873 s wall and a 4018 s leg-sum. Measured mean across four runs is **1001.3 s**, 14.7 % low. |
| `TOOL-aMeteredTurnstile-5` | **KEEP OPEN, bind to R1** | Confirmed at **669.1 s versus 5.1 s** to first signal. It is the cost of fixing R1, not an independent item. |
| `TOOL-aTimedTurnstile-1` | **CLOSE** | False at HEAD. The pool landed, and the row's 79.9 s target sits 11× below the current floor. |
| `TOOL-cFinalBerth-5` | **KEEP OPEN, note** | Did not reproduce in this sample. The canary's between-run spread is 25.9 % across comparable bars. |

New rows to mint: `TOOL-aScannedThrottle-1` … `-5`, per §4.

## 6 · What this build did NOT establish

- **No cold-bar measurement.** Every run here had a warm filesystem cache. `TOOL-aTimedTurnstile-4`'s
  1.59× cold/warm factor is unverified at the current leg count.
- **Queue wait is unmeasured, not merely unrecorded.** §3.4 reasons about it from service time and
  arrival times; no run in this sample actually reported a non-zero `gate queue: waited`.
- **The four-run sample is one day on one node.** Spans 925–1058 s and utilization 59.8–69.5 % are
  consistent, but four runs cannot separate a trend from noise.
- **27 of the 55 lens findings were refuted and are not carried here.** Several were refuted for
  arithmetic that could not be reconciled with the measurement, which is the verify stage working;
  they are in the workflow journal, not in this report.

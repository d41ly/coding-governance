# Appendix — Gate runner: levers to reach the verdict faster

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-08, kept verbatim below its first heading. It ran no suite: every saving is an ESTIMATE from static spawn counts against the profiled bar in `2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, and the synthesis that ranks across all five is `2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`. Line citations are against `fa68a767` plus this unit's fixes.


The subject is the profiled bar on node a: `fa68a767`, `GATE_FULL=1 GATE_SELFTESTS=1`, width 8, run from a frozen clone, wall 13324 s. All line numbers refer to `tools/run-gates/run-gates.sh` unless another file is named. This was read-only research. No leg, suite or runner was executed.

**The instruments are committed beside this record, in `2026-10-08-build-TOOL-aMeteredSweep-1-runner-instruments.txt`, so the figures can be re-derived:**

- `occ.py` reads the pool occupancy and the completion-to-dispatch gaps from the run record.
- `sim.py` is a list-scheduling simulation over the measured durations.
- `reuse_est.py` and `reuse_sim.py` estimate guard-keyed reuse over recent `main` commits.

## What the run record says (re-derived from `gate-run/20261007T170502Z-120570/*.leg`)

| fact | value |
|---|---|
| pool phase (first dispatch to last pool completion) | 9214 s |
| serial retry phase after the drain (9 legs, one at a time) | **4050 s, 30 % of the wall** |
| time at concurrency 8 / 6-7 / 2-3 | 4585 s / 1398 s / **2798 s (the tail)** |
| killed attempts (pool seconds spent on the 9 legs whose ceiling fired) | **14217 leg-s, 26 % of the 54049 pool leg-s** |
| floor leg `run-gates canary` dispatched at | **+3445 s** (manifest order: the frozen clone had no ledger) |
| completion → next-dispatch gap | median 4.3 s, p90 8.4 s, sum 602 slot-s |
| startup: turnstile acquired → header written → first leg | 25 s + 4 s; teardown 6 s |
| memory pause | 3 holds, 872 s (bound, bound, fell) at 94-96 % used |

The simulation holds durations fixed at their contended width-8 values, so it isolates order and retry policy. Its manifest-order run gives 12885 s, against 13324 s observed; the difference is roughly the pause and the dispatch gaps. That agreement is what entitles the other simulated figures to be quoted.

**The profiler's verdict is misleading for this run.** `profile_bar.py:149-159` and `:519-521` report "BOUND: floor … widening and trimming buy ZERO". Its work term, 43864 s, takes the retried legs at their retry seconds. That drops the 14217 s of killed attempts, which the pool really paid for. The run was not floor-bound either: the floor leg started 3445 s late, and a 4050 s serial phase followed the pool. The profiler should report the floor leg's dispatch offset and the retry-phase seconds as two more terms of its regime.

## Ranked levers

The savings are NOT additive. A combined projection follows the table.

| # | lever | est. s saved on this bar | effort | risk | evidence |
|---|---|---:|---|---|---|
| 1 | Retry a deferred leg in the pool's drain tail, not serially after the drain | **~3300** (sim 10970 → 7673 with lever 2); the serial phase alone is 4050 | S-M | low-med | `run_leg_retry` 2974-3030 runs strictly one at a time after `wait` 3557; the tail sat at concurrency 2-3 for 2798 s |
| 2 | Longest-first dispatch with no ledger: the declared ceiling, or the tracked `ceiling-evidence.txt`, as the prior | **~1900** (sim 12885 → 10970; the ledger-order oracle gives 10789) | S, one expression at 1946 | very low | the header shows dispatch in manifest order; the canary started at +3445 s |
| 3 | Width from a measured per-host calibration (expect about 4 on node a), plus dynamic narrowing on spawn pressure | **2000-5000, conditional** on the saturation hypothesis; also likely removes the 872 s of pause holds and most ceiling fires (overlaps 1) | M | verdict: none; speed: medium, settled by calibration | effective concurrency 4.06; legs ran 2.4-6.9x faster alone; all 40 retained run records on this node are width 8, so nothing below 8 was ever measured |
| 4 | A host-wide slot pool (jobserver) shared by nested and foreign bars | unmeasured; large on a contended day | M-L | medium | `foreign-prefix.gov.test.sh:137` opens a nested pool at the printed width (8) inside the width-8 bar; the census saw 1-5 foreign trees for most legs; the turnstile is per repository (keyed on the common dir), so another repo's bar ran beside this one |
| 5 | Content-addressed reuse keyed on each leg's declared inputs, in a cache shared through the common dir | **0 as run** (fresh clone, no ledger, `GATE_REUSE` unset). With a green parent: 25014 leg-s skipped and the wall about 1000 s lower (still canary-bound). On a records-only commit (21 of the last 30 on `main`): the bar falls to the impure `unattended kit gate` floor, about 3937 s, saving ~9000 | M | medium (an owner policy call) | `reuse_est.py` and `reuse_sim.py`; the key includes `BASE` at 2154 |
| 6 | Cut the runner's own spawns: per leg about 45-65 fork/exec down to about 6, plus per-invocation startup | direct 75-150; indirect, inside the canary family (27 % of leg-s drives the runner about 100+ times), unmeasured, plausibly 500-2000 | M | low-med (output must stay byte-stable) | gap median 4.3 s; the canary log says a 3-leg fixture control "could not finish … inside 60s" |
| 7 | Run the self-test tier on another host or tier, not node a's bar | the tier is 46408 of 54049 leg-s; node a's bar falls to the push-bar class, measured 1700-1740 s | S (procedure) | low | gotcha `process-creation-is-the-suite-cost`: node d pays 19-39 ms a spawn against 78-251 ms here |
| 8 | Hang detection by progress, extending a ceiling rather than killing a leg that is still moving | ~3700 beyond lever 2 (sim D, a guess model); overlaps 1 | M | medium | the raw output is captured to a file (2411), so progress is observable; the wall watcher already polls every 30 s (2673) |
| 9 | Rewrite the runner in Python, or add a persistent worker | direct at most 150; the rest is reachable in bash | XL | high | see section 6 |

**Combined projection.** Levers 2 and 1 at fixed contended durations give 7673 s, against 13324 s observed (−5650). Adding lever 3, if the spawn path saturates near 4 workers, would put the bar at about 5000-5500 s. That last figure is a hypothesis until the calibration A/B has been run. Lever 7 changes the question entirely: node a's bar then sits in the ~1700 s push-bar class.

---

## 1. Width: what this hardware should run at, and the mechanism

**Today.** `gate-profiles.txt` maps 8 or more cores with at least 24000 MB to `width=8`. Its comment ("at 16 each leg dilates…") compares width 8 against 16 and 24, never against 4 or 6. `profile_from` read `detected, GATE_JOBS`, and every one of the 40 retained run records on this node is width 8. The only memory feedback is the mempause hold (454-530), which narrows dispatch above 90 % used.

**The evidence that 8 is past saturation here:**

- Effective concurrency was 54049 / 13324 = 4.06.
- Every ceiling-killed leg ran 2.4-6.9x faster alone (memory-hygiene 4801 → 1442 s, check-wiring 2322 → 601, pre-push 1786 → 402, run-log line 1201 → 175). The retries themselves had a foreign bar beside them.
- The repo's own record says width 24 ran 26 % slower than width 8, with CPU at 39 %. The contended resource is process creation behind Defender, not CPU.
- Nested pools multiply the width: the foreign-prefix leg runs every self-test in its own 8-wide pool inside the 8-wide bar.

**Answer: run at about 4 on node a, but derive it rather than retype it.** Cores and RAM thresholds cannot see the cost that binds here: spawn latency under an on-access scanner, which moves by 10x between nodes with identical core counts (19-39 ms on node d against 78-251 ms on node a).

**Mechanism, built from existing pieces:**

1. **A calibration verb and its cache.** `run-gates.sh --calibrate` times K concurrent spawn loops for K in {1, 2, 4, 6, 8}. Each loop is about 10 s of `git rev-parse` + `bash -c :` + `python -c pass`, the leg mix. It computes the aggregate rate T(K) and picks the smallest K with T(K) ≥ 0.9 × max T. That K is written tmp-then-rename to `<common-dir>/gate-host-calibration` beside `gate-spawn-floor`, which 2281-2340 already reads and writes in this style. The line carries `<width> <T1..T8> <iso> <boot-time>`. It is re-measured when absent, older than 7 days, or when the boot time differs, and costs about 60 s once.
   - The effective width becomes `min(row width, calibrated K)`. The profile row turns into a cap, and `GATE_JOBS` still overrides it.
   - The width cannot change a verdict, so the governing invariant (`gate-profiles.txt` header) holds.
   - The profile line prints `width 4 (calibrated <date>)`.
2. **Dynamic narrowing, the mempause generalised.** The census sampler already wakes every 60 s (`arm_census` 2752-2773). It would also time 3 spawns and write the ratio to `gate-spawn-floor` into a file. `check_dispatch_pause` would hold dispatch when that ratio exceeds a knob (`spawnpause=3`), reading the file with a builtin `read`, so the decision forks nothing, exactly as the mempause does. This is GNU make's `-l` load-average rule, keyed on the cost that matters here.
   - It adds a knob to `KNOWN_KNOBS` (356). The canary pins that set, so the canary must move with it.
3. **Memory.** Keep the mempause. With width at about 4, a peak of 94-96 % is unlikely unless a foreign bar is present, which is lever 4's job.

**Verification owed before landing.** A 3-arm A/B (W = 4, 6, 8) on a frozen clone with no foreign bar, each arm asserting it ran all its legs (the ab-arm-must-prove-it-ran gotcha). Report the bash or foreign count beside every figure.

## 2. The runner's own per-leg overhead

**Spawns paid per leg on the success path.** These are fork plus exec events. A `$(…)` around a function, or a pipeline, adds forks.

| site | line | events |
|---|---|---:|
| `s=$(date +%s%N)` | 2369 | 2 |
| `timeout` wrapper (the leg itself is inherent) | 2411 | 1 |
| `out=$(cat raw)` | 2407 | 2 |
| `e=$(date +%s%N)` | 2408 | 2 |
| `secs=$(printf …)` | 2409 | 1 |
| `lf="$(leg_log …)"`, with an inner `$(printf \| tr)` | 2424, 252-255 | ~5 |
| `{…} \| redact >lf`, then `chmod` | 2426-2427 | 3 + 2 |
| `{…} \| redact >RUNDIR/.out`, then `chmod` | 2440-2441 | 3 + 2 |
| `$(input_key)`: unguarded `printf \| git hash-object`; guarded adds `git ls-files \| sort` and a `printf \| grep` per guard path | 2452, 2137-2156 | 4 unguarded / ~17-21 guarded (66 of 126 legs are guarded) |
| `mv` of `.leg` | 2454 | 2 |
| `ts_hb`: `$(ts_now)` → `date`, then `mv` | 2461, 1060 | ~5 |
| `mv` of `.rc` | 2462 | 2 |
| reader `rc=$(cat .rc)` | 2522 | 2 |
| reader `live()` = `$(jobs -rp \| wc -l)`, 2-3 times per leg | 3509, 3519, 3531 | ~8-12 |
| **total** | | **~45-65 per leg** |

**Measured cost.** The completion-to-dispatch gap has a median of 4.3 s under this bar's load, and 1.0-2.8 s on push bars. On a throughput-bound bar that is about 602 / 8 = 75 s of wall. On a floor-bound one it is about 0.

**The multiplier is the real reason to cut it.** The run-gates canary, the floor leg at 5769 s, drives this runner over fixtures. `run-gates.test.sh` holds about 100 runner references, the evidence, turnstile and run-log suites another 64, and the gov canary, foreign-prefix leg and run-selftests self-test add more. Every nested bar pays the startup chain, which includes:

- python resolution, `nproc` and two `getconf` calls;
- the `timeout` probe and the python manifest parse;
- the process-monitor probe, `ps -W` plus python;
- the fingerprint script, `git status`, the turnstile `mkdir` and `date`;
- ten spawn-floor spawns, the census `ps -ef` plus `awk`, and the wall watcher.

It also pays the per-leg cost per fixture leg. The canary's own log records the size of that bill on this run: a 3-leg control fixture "could not finish … inside 60s", so three clamp arms and the spun-outcome arm went UNEXERCISED.

**Cuts.** All of these are bash 5.0+ builtins. The runner already requires 5.0 through `EPOCHSECONDS`, and node a has 5.3.9.

- `EPOCHREALTIME` for `s` and `e`, and `printf -v secs`: −5.
- `IFS= read -r -d '' out < raw` in place of `$(cat)`; `read -r rc < .rc` in the reader: −4.
- `leg_log` through `LC_ALL=C` with `${1//[!A-Za-z0-9._-]/_}`: −5. The file names must stay byte-identical; the `LC_ALL=C` is what keeps tr's byte semantics.
- Run `sed` only when `[[ $out == *://*@* ]]`, and write both copies with `printf`: −6 in the common case.
- A `umask 077` subshell in place of the two `chmod`: −4.
- **Precompute every `input_key` once, before dispatch.** Its inputs, `FPRINT_START`, `PORCELAIN_START` and `BASE`, are fixed at run start. One `git ls-files -s` plus one awk pass gives all 126 keys, held in an array that the forked workers inherit: −4 to −21 per leg.
- `ts_hb` through `$EPOCHSECONDS`: −3.
- `live()` as a builtin count of dispatched indices with no `.rc`: −8 to −12. This keeps the drain re-check at 3532-3556, whose race reasoning is unchanged.

The result is about 6 events per leg: `timeout` and the two `mv` atomic renames. Startup should then be counted once with a PATH shim that counts execs and trimmed the same way. For example, `measure_spawn_cost`'s ten spawns are already skipped when no bounded leg runs, and the process-monitor python probe only matters when the conf exists.

## 3. Scheduling

**Longest-first without a ledger.** The dispatch hint reads only `<git-dir>/gate-ledger.tsv` (336-340, 1940-1946). A fresh worktree or a frozen clone therefore dispatches in manifest order. Two priors already sit in the tree:

- **The declared `ceiling`.** It is already parsed into the rows, and README:381 derives it as about 3x the measured seconds. The sort key at 1946 becomes `-(durs.get(name) or ceiling/3.0)`. Simulated: 10970 s, against the ledger oracle's 10789 s and manifest order's 12885 s.
- **The tracked `ceiling-evidence.txt`.** It is generated, monotone and holds a per-leg maximum, so it is a better seed than the ceiling and needs no new file.

Either prior keeps the hint advisory, and the reporting walk (2572-2600) stays manifest order, so nothing a reader sees changes. Also consider resolving the ledger from the common dir (as `gate-spawn-floor` is) so that a new worktree inherits the hint.

**The self-tests as a tier.** They are already held by default (2082-2093). Mixed into one `GATE_SELFTESTS=1` bar, the self-tests are 86 % of the leg-seconds, and the canary family competes with the floor leg at the same width. Two options:

- (a) Keep node a's bar to the repository legs; that class measured 1700-1740 s. Run the held tier through `run-selftests.sh --pooled` on node d, whose spawns are 3-10x cheaper, or rely on the existing daily `held` job in `remote-ci.yml`.
- (b) On one host, run the self-test tier at the calibrated width as a second phase that starts the moment the repository legs drain. The verdict a push needs then arrives about 1700 s in, not at the end.

## 4. Retry policy

**Today.** A fired ceiling is deferred (2541-2553). After the pool drains, every deferred leg runs one at a time, alone (2974-3030). Here that cost the 14217 leg-s of killed attempts, and then a 4050 s serial phase on the wall while the pool sat at concurrency 0.

**Better, in order of value for effort:**

- **(a) Release a retry into the drain tail.** Queue a deferred leg's retry into the same dispatch loop once the running count falls to 1 or less (in practice, only the floor leg left), instead of after `wait`. The tail had about 5 idle slots for 2798 s, which is more than the 4033 s of retry work at ~2x packing. Simulated: 10970 → 7673 with lever 2.
  - The retry line already names its neighbour count (`measure_neighbours`, 2883).
  - The HOST judgement should then require that the retry ran alone, or report "not alone, HOST not measured". Today's rule only reads HOST after a verified-clear, alone retry, and that rule is kept.
- **(b) Retry concurrently after the drain at a narrow width (about 3).** This is the cheapest code change: 4033 → about 1442 s, saving ~2600 s, if their alone durations hold.
- **(c) Kill on a hang, not on a deadline.** Killing earlier at a fixed fraction only kills more slow-but-live legs. The better trigger is "no progress". At the ceiling, the wall watcher (2673, already a 30 s poll) checks whether the leg's `.raw` file grew or its group's CPU moved in the last N minutes.
  - If the leg is live, extend once, up to a hard cap of 2x the ceiling, so the hang bound is still bounded.
  - If it is dead, kill at once, which is earlier than the ceiling.
  - Contention-scaled ceilings (`ceiling × clamp(spawn_ratio, 1, 3)` at dispatch) are a weaker version: `timeout`'s deadline is fixed at launch, and contention arrives later.
- **(d) Fewer fires to begin with.** Lever 3's narrower width attacks the cause: ceilings were sized against the 8-wide pool, and the foreign bar pushed dilation past their ~3x margin.

## 5. Result reuse

**What exists.** `GATE_REUSE=1` (2219-2244) is opt-in and never set by `.githooks/pre-push`. A run that reused anything cannot stamp a full green (README 133-140). Its weaknesses:

- **One row per leg name in a per-git-dir ledger** (3584-3620). A new worktree or clone has nothing, and an A → B → A tree can never match its first green.
- **The key includes `BASE`** (2154). It changes whenever the merge-base or the origin tip moves, which is after every landing, even for a self-test that never reads the base. Reuse across commits therefore almost never fires.
- **The guard model.** The guard pass (2095-2104) skips a guarded leg on a scoped run, but `GATE_FULL` ignores every guard, and the profiled bar was full.

**Proposal.**

- **The cache.** `<common-dir>/gate-cache/<key>` holds `ok <secs> <run_id> <date>`, append-only with LRU trimming, and is shared by every worktree; a clone can be seeded by copying the directory.
- **The key** is `H(manifest row bytes, blob ids of the guard pathspecs from one ls-files pass, the porcelain slice, PYBIN and bash versions)`.
  - `BASE` enters only for a leg declaring that it reads it.
  - Impure legs are never cached.
  - An unguarded leg keys on the whole-tree fingerprint, as it does today.
- **The policy question for the owner.** Authoritative runs may reuse only keys that an authoritative full green wrote. They must re-execute any leg not executed in the last N landings or D days, so a guard that under-declares its reads is caught on a bounded schedule. This is the same trade the pre-push freshness rule already makes for guard-scoped pushes.

**What it would have saved here.**

- As run: 0, because the clone was fresh and had no ledger.
- With a green at the parent: 40 guarded legs and 25014 leg-s reusable. The wall drops about 1000 s beyond lever 2, and the canary still runs, because `tools/` moved.
- On a records-only commit (21 of the last 30 first-parent commits on `main`): 64 legs and about 46600 leg-s are reusable, and the bar becomes the impure `unattended kit gate` floor, about 3937 s contended.

## 6. A full rebuild of the runner

- **A Python orchestrator.** `subprocess.Popen` is a native CreateProcess with no cygwin fork, timers make soft ceilings and calibration trivial, and Job Objects (through ctypes) give a clean tree kill.
  - **Cost:** run-gates.sh is 3966 lines of gated semantics: verbs, the tail contract, record schemas, the wall, the turnstile, census, attribution, retry and HOST, mempause and docs mode. About 230 nested-runner references across its suites pin its bytes, and the kit deploys to adopters.
  - **Gain:** the direct overhead it removes is about 1 % of this bar. Every large win above is reachable in bash with a small diff.
  - **Risk:** high, with weeks of parity work.
  - **Not recommended.** Revisit only if lever 6's startup trim stalls and the canary family is still floor-bound.
- **A persistent worker or job server.** A warm bash does not help, because a leg's cost is the leg's own spawns. A **jobserver** does help, as lever 4: a token FIFO or a `mkdir`-slot directory under a host-wide path, exported as `GATE_JOBSERVER` so nested runners and `run-selftests --pooled` take tokens from the parent's budget instead of opening their own 8-wide pools.
  - Cost: medium.
  - Risk: deadlock if a nested runner holds a token while waiting for tokens. Mitigate as make does: each process owns one implicit token.

## What must NOT change

- **The verdict invariant** (`gate-profiles.txt` header): no knob turns a leg into a pass or a skip. Width, calibration, order, pauses and reuse may cost speed, never coverage.
- **Reporting order and bytes.** The reporting walk is manifest and chunk order whatever the dispatch order (2572-2600; the canary at `run-gates.test.sh:591` asserts that `GATE_JOBS=1` and `=4` report identically). The two-space tail contract (2465) and the verb set (`ok`, `FAIL`, `skip`, `reuse`, `held`, `retry`) also stay fixed.
- **The hang bounds.**
  - The per-leg ceiling with `-k 5s` (2411), captured through a file and never a pipe.
  - The whole-run wall, armed at the first dispatch (2652).
  - `TS_MAXWAIT` (938) and `MEMPAUSE_HOLD` (454).
  - Any extension in lever 8 has a hard cap below the wall.
- **Retry semantics.** One retry, only for a fired ceiling. An assertion failure is never retried. `retried` is never reusable. HOST is read only against a pre-bar floor with the attempts verified clear and the retry alone (2928-2972).
- **Record integrity.**
  - `.rc` is written last and atomically (2462), and the verdict file is written last; its absence is the crash signal.
  - The `.leg` row keeps 8 fields, and header keys are additive only.
  - A reused run never stamps `gate-full-green`.
- **Evidence hygiene.** Only `foreign 0` readings argue a ceiling. After a width change, re-derive the evidence but never lower it silently: the file is monotone by design.
- **Measurement discipline.** Wall clock on this AV-fronted host is good to about 2x. Every A/B above needs a frozen clone, no foreign bar, a positive per-arm artifact, and the bash or foreign count reported beside the seconds.

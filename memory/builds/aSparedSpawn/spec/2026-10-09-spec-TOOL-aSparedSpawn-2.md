# TOOL-aSparedSpawn-2 — the pool width comes from a measured spawn calibration, and dispatch pauses on spawn pressure

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Node `a` runs the bar at width 8 because `gate-profiles.txt` maps its cores and RAM to 8, and no run
below 8 has ever been recorded there. The profiled bar ran at an effective concurrency of about 4 and
its ceiling-killed legs ran 2.4 to 6.9 times faster alone, so 8 looks past saturation for the cost that
binds here, process creation. This unit measures widths 4, 6 and 8 first, then derives the width from
a per-host spawn calibration, and holds dispatch while spawn pressure is high, as the memory pause
already does for memory.

## 2. Scope (IN)

- **S1** — The width A/B, run BEFORE any runner edit and committed as instruments beside this unit's
  record under `memory/builds/aSparedSpawn/build/`: an instrument script and its rows. Six arms, widths
  4, 6 and 8 by `GATE_JOBS`, each quiet and under a declared synthetic spawn load, each from a frozen
  clone. Every row carries wall, leg-seconds, effective concurrency, ceiling fires, pause holds and the
  foreign and bash counts beside the seconds, and a positive artifact that the arm ran every leg of its
  subject. The subject is the owner's pick (F2). Observed by AC1.
- **S2** — A calibration verb, `--calibrate-width`, on the runner. It times K concurrent loops of the
  spawn `measure_spawn_cost` already times (the `GATE_SPAWN_CMD` seam's command, `true` by default) for
  K in 1, 2, 4, 6 and 8, computes each aggregate rate T(K), and selects the smallest K with
  T(K) >= THETA x max T. THETA is a source constant set from S1's rows. The verb prints the rates and
  the pick, and writes `<git-common-dir>/gate-host-calibration` tmp-then-rename, beside the
  `gate-spawn-floor` the runner already keeps there: `<width> TAB <rates> TAB <iso-utc> TAB <boot>`.
  Observed by AC2 and AC3.
- **S3** — An arm seam, `GATE_CALIBRATION_RATES`, read once and unset as `GATE_SPAWN_CMD` is: a list
  of T(K) values that stands in for the timed loops, so the selection is graded with no clock.
  Observed by AC2.
- **S4** — The bar reads the cache with `read` at start. It is valid when well formed, written under
  seven days ago, and written in this boot (boot time from `/proc/uptime` with a builtin read, where
  it exists). A valid cache sets the width by the rule F1 picks, below `GATE_JOBS` in precedence.
  Otherwise the row's width stands and the profile line says `uncalibrated` and which test failed.
  The header gains `width_from`, outside the four-key run envelope. Observed by AC3 and AC4.
- **S5** — The spawn-pressure pause, a fifth knob `spawnpause=<ratio>` in `KNOWN_KNOBS` and the
  table, 0 or absent meaning off. The census sampler (`arm_census`) also times three spawns on each
  tick and writes the reading to a file in the run's work dir. `check_dispatch_pause` holds the next
  dispatch while that reading exceeds `spawnpause` times the recorded floor, read with a builtin as
  the memory reading is. The memory pause's release rules apply unchanged: fell, drained, bound,
  unread, wall. With no floor recorded the knob is INERT and says so. A `spawn:` summary line follows
  the `memory:` line. Observed by AC5 and AC6.
- **S6** — An arm seam, `GATE_SPAWN_NOW`, naming a file read in place of the sampler's reading, as
  `GATE_MEMINFO` stands in for `/proc/meminfo`. Observed by AC5.
- **S7** — `PINNED_KNOBS` in the canary (`run-gates.test.sh:1385`) gains `spawnpause` in the same
  commit as `KNOWN_KNOBS`. Observed by AC7.
- **S8** — `gate-profiles.txt` documents the calibration, its cache, the precedence and the new knob in
  its KNOBS block, and every row declares `spawnpause` from S1's loaded rows; `tools/run-gates/README.md`
  gains the verb. NOT OBSERVED: prose and declared values, which no checker grades for truth.

## 3. Non-goals (OUT)

- No host-wide slot pool shared with nested or foreign bars (the runner report's lever 4). The
  foreign-prefix leg still opens its own pool inside the bar.
- No calibration at bar start. The verb is explicit; a bar only reads the cache, so the canary's
  nested bars, whose fixture repos have no cache, keep their row width and pay no calibration.
- No change to which leg runs, to any verdict, or to the per-leg ceilings. The governing invariant in
  the `gate-profiles.txt` header holds: a knob may cost speed, never coverage.
- No retry-policy change; that is the drain-tail retry's.
- No Windows Defender exclusion. It is the largest single factor and a security setting the owner owns.

### Edges

- **hands-off** `TOOL-aSparedSpawn-3` — the drain-tail retry and longest-first dispatch, whose value
  depends on the width this unit sets: longest-first alone packed the heaviest suites together in
  aMeteredSweep's second bar and manufactured ceiling fires.

## 4. Design

**What is measured today, re-verified at base 22efab65.** `measure_spawn_cost` (`run-gates.sh:2362`)
times ten spawns with `EPOCHREALTIME` and `write_spawn_floor` keeps the LOWEST reading in
`<git-common-dir>/gate-spawn-floor`. The floor is quiet-host cost; nothing reads load. The width is
`JOBS=${GATE_JOBS:-$PROF_WIDTH}` (`:771`), from the first row of `gate-profiles.txt` whose core and RAM
thresholds hold; node `a` selects `capable`, width 8.

**The evidence, as the research states it.** Effective concurrency 4.06 on the profiled bar at width
8 (54049 leg-s over a 13324 s wall). Every retained run record on node `a` is width 8. Spawn cost on
node `a` measured 21 ms quiet and 632 to 818 ms loaded (the round-two menu's table). The repo's own
record says width 24 ran 26 % slower than width 8 at 39 % CPU. None of it measured a width below 8,
which is why S1 runs before any edit and why the calibration's THETA is set from S1 rather than typed.

**Why a spawn rate selects a width.** The leg mix is spawn-bound. If K concurrent spawn loops stop
raising the aggregate rate past some K, more legs past that K share the same throughput and only
dilate each other, which is what fires ceilings. The pick is the knee, the smallest K within THETA
of the best rate. S1 checks that claim: the calibrated pick should equal the A/B's best-wall width or
sit one step from it, and AC1 records whether it did.

**Cache validity.** A reboot or a Defender update moves spawn cost by integer factors, so a pick from
another boot is stale; seven days bounds drift within one boot. A stale cache is not an error: the row
stands and the line says so, because a skip must announce itself.

**The pause** reuses the memory pause's machinery rather than copying it: one `check_dispatch_pause`
decision, two readings, the episode row gaining which reading held it. The sampler already wakes every
`CENSUS_EVERY` seconds, detached, so three spawns per tick cost the dispatch loop nothing; the loop
reads a file. The threshold is a ratio over the recorded floor, because absolute milliseconds differ
tenfold between nodes with identical core counts.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — the verb, the cache read, the precedence, the sampler reading, the pause.
- `tools/run-gates/gate-profiles.txt` — the KNOBS block and each row's `spawnpause`.
- `tools/run-gates/run-gates.test.sh` — `PINNED_KNOBS`, and the calibration and pause arms.
- `tools/run-gates/run-gates.evidence.test.sh` — the header `width_from` key arm.
- `tools/run-gates/README.md` — the verb and its cache.
- `tools/run-gates/kit.toml` — the kit version, moved once for the build.
- `memory/builds/aSparedSpawn/build/` — the A/B instrument and its rows (S1).

### Alternatives rejected

- **Retype the row to width 4.** It is a guess from one profile, it moves every node's bar, and the
  next hardware or scanner change makes it wrong silently. A measured pick moves with the host.
- **Calibrate at every bar start.** About a minute per bar on node `a` by the research's estimate, paid
  by each of the canary's nested bars too.
- **Narrow on CPU load average, as GNU make's `-l` does.** The profiled bar ran at 39 % CPU while
  saturated; CPU is not the contended resource here.
- **Contention-scaled ceilings at dispatch.** `timeout`'s deadline is fixed at launch and contention
  arrives later; the pause acts at the next dispatch, where the decision is still open.

## 5. Production-readiness checklist

- security: N/A — no new write path beyond a tmp-then-rename cache file in the common dir, the pattern `gate-spawn-floor` uses.
- perf / scale: the point of the unit; the verb costs about a minute once per boot, the sampler three spawns a tick.
- error / empty / loading states: an unreadable, stale or other-boot cache falls back to the row width and names why on the profile line.
- observability: the profile line names the width's source, the header gains `width_from`, and a `spawn:` line reports holds.
- risks: a THETA or `spawnpause` set wrong costs speed, never a verdict; whole-output readers in the suites must filter the new `spawn:` line.
- testing: clock-free arms through two seams, a canary pin move, and the A/B's per-arm artifacts.
- migration: none for data; a node with no cache behaves exactly as today plus the `uncalibrated` note.
- user docs: `gate-profiles.txt` KNOBS block and `tools/run-gates/README.md` (S8).

## 6. Acceptance criteria

- **AC1** — When the A/B instrument's rows are read, each of the six arms carries a wall, an
  effective concurrency, a ceiling-fire count, a foreign count and a positive artifact that every leg
  of its subject printed a `GATE` verb line, and a final row records the calibrated pick beside the
  best-wall width. Red when: an arm exited early and its row has no artifact, or a figure has no count.
  cost: six bars of the F2 subject; no run below width 8 exists on node `a`, so the cost is unmeasured.
  permission: the A/B runs bars, which a builder pass under a no-suites directive may not; the owner runs it or authorises it.
  figure: PINNED, each row dated and noded; THETA and every `spawnpause` are derived from these rows.
- **AC2** — When `--calibrate-width` runs with `GATE_CALIBRATION_RATES` naming rates that rise to K=4
  and stay within THETA after it, it prints a pick of 4; with rates still rising at 8, it prints 8.
  Red when: the selection takes the maximum rather than the knee, or reads the clock under the seam.
- **AC3** — When `--calibrate-width` completes in a fixture repo, `gate-host-calibration` holds one
  line of four tab-separated fields under that repo's common dir, and a following
  `--print-profile` reports the cached width and `calibrated`. Red when: the cache is not written, or
  the bar does not read it.
- **AC4** — When the cache is absent, carries another boot's time, or is older than seven days,
  `--print-profile` reports the row width and `uncalibrated` naming that cause; with `GATE_JOBS` set
  the override wins over a valid cache. Red when: a stale cache is used, or a fallback is silent.
- **AC5** — When a fixture bar runs with `spawnpause` set and `GATE_SPAWN_NOW` reading above it, the
  pause rows show a hold that ends `drained` or `bound`, and every leg still prints its verdict line.
  Red when: the pause never holds, or a held leg is skipped or never reported.
- **AC6** — When no spawn floor is recorded and a row declares `spawnpause`, the bar prints that the
  spawn pause is INERT and holds nothing. Red when: an absent floor reads as a ratio of zero or
  infinity and the pause holds or stays silent.
- **AC7** — When `KNOWN_KNOBS` carries `spawnpause` and `PINNED_KNOBS` in the canary does not, the
  canary's pin arm reds. Red when: the pin arm passes on a knob set it does not name.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates run-log line` ·
`run-gates gov canary` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push run-log line` ·
`push-main self-test` · `check-wiring self-test` · `settings-merge selftest` ·
`foreign-prefix parity (every self-test at three prefixes)` ·
`python resolver (behaviour + inline parity + idiom ban)` · `install-prefix self-test` ·
`dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` ·
`kit-placeholders self-test` · `harness arms (fail branches armed or pinned)` ·
`shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` ·
`testsuite counts (every bar self-test prints one)` · `line length` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.test.sh · covers AC2 AC3 AC4 · a selection taking the maximum, an unread cache, and a stale cache used · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/run-gates/run-gates.test.sh · covers AC5 AC6 · a pause that never consults the reading, and an absent floor read as a number · same floor
New arm: tools/run-gates/run-gates.test.sh · covers AC7 · `spawnpause` added to `KNOWN_KNOBS` alone · none

## 8. Open questions

- **F1 — Does the calibrated width replace the rows' `width` or override the width knob alone?**
  - (a) Override only: effective width is the lower of the row's width and the calibrated pick, below
    `GATE_JOBS` in precedence. Rows keep `width`, which becomes a cap, and an uncalibrated host
    behaves exactly as today. Smallest change; the row still means something on a node never calibrated.
  - (b) Replace: rows lose `width`, and a host with no cache uses a built-in default. One source of the
    number, but every node's first bar after landing changes width before anyone has calibrated it.
  - Recommendation: (a).
- **F2 — What does the A/B run, and under what load?**
  - (a) The default `GATE_FULL` bar. Cheapest, but the reuse report finds that bar floored by its
    impure `unattended kit gate` leg, so width may read flat for a reason unrelated to spawns.
  - (b) A `GATE_LEGS` subset manifest of the spawn-heaviest held self-test legs, the population the
    runner report saw dilate. It tests the saturation claim directly at a fraction of the tier's cost.
  - (c) The default bar with the whole held self-test tier: the population the claim is about, at
    hours per arm, six arms.
  - Load: a declared synthetic spawn loader (repeatable) or a neighbouring bar (realistic, not repeatable).
  - Recommendation: (b), with the synthetic loader, and the bash and foreign counts beside every figure.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "time process spawns to calibrate pool width"` ranked no
spawn-timing seam (`parse_time`, `resolve_rule_pool`, the process-monitor hooks); the seams this unit
extends are in the runner itself, which the probe's `run-gates` affordance seam covers:
`measure_spawn_cost` and `write_spawn_floor` for the timing and the common-dir file, and
`check_dispatch_pause` with `read_mem_used` for the pause, which gains a second reading instead of a
second copy.

Recall terms used: gate-profiles width GATE_JOBS spawn floor calibration mempause dispatch pause pool saturation node

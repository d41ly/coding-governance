# Brief — dRedressedBar: a gate profiler that runs every leg clean and profiles each one fully

**Serves:** research TOOL-dRedressedBar-18

## The prompt

> Add another feature to this build - a gate profiling tool (does none exist yet?) that will run ALL EXISTING (current and future) legs (including all self-tests) in either sequential or concurrent modes (to the max of 80% processor load/90% memory load), without any contaminating parameters, preserving all logs, no ceilings (to establish the truthful values), fully profiling each leg - cpu/memory load/process spawn time/processes spawned/each process detailed/anything else that's needed for a full profile.

> there is already a process monitor tool in this repo, how can it be used for stall detection?

## The brief

### Goal
The bar's profile in this build's research record
(`build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md`) had to be rebuilt from scratch
records the runner deletes on exit. It came from a run with a knob in its environment, could not see
inside any leg, and inferred spawn-boundedness from a coarse CPU average. Build a tool that measures
every gate leg truthfully, one leg at a time or concurrently, so the ceilings, the width profiles and
the "the cost is process creation" claim each stand on measurement.

### Items
1. **What exists, and what this extends (verified 2026-10-14).** Read these before choosing:
   - `tools/run-gates/profile_bar.py` wraps one bar run: its envelope (width, commit, host, wall,
     guards) and the regime (floor-bound or packing-bound). Its header: it "does not attribute a leg's
     cost to any cause inside it". No CPU, memory or spawn data.
   - `tools/run-gates/derive-ceilings.py` argues each ceiling from retained
     `<git-dir>/gate-run/<runid>/<i>.leg` rows, admitting only readings the census found free of
     foreign gate work. It measures nothing inside a leg.
   - `tools/process-monitor/census.py` `scan_processes()`: one bounded read of the process table, with
     rows `winpid`, `win_ppid` (defined for native processes too), `cpu_s`, `age_s`, `command`, Windows
     and MSYS joined. `tools/process-monitor/reap.py` `build_walk(rows, target)` walks one process's
     descendant tree. `tools/process-monitor/scope.py` `derive_scope` attributes by declared prefix.
     `tools/process-monitor/classify.py` grades a row on AGE against a ceiling, labelling it with a
     LIFETIME cpu/age rate.
   - `tools/run-gates/run-selftests.sh` runs the held self-tests serially or pooled, with budget verdicts.
   - The runner already measures spawn cost (`measure_spawn_cost`, `GATE_SPAWN_CMD`, the spawn floor)
     and censuses foreign gate work per leg.

   Nothing profiles inside a leg, and nothing runs every leg with no ceiling, no knob and every log
   kept. Extend these seams rather than writing a second process reader, a second leg-manifest parser or
   a second spawn timer.
2. **TOOL-dRedressedBar-18 — the gate profiler.** Its requirements, from the owner's words:
   - **Population:** every leg `tools/gate-legs.json` declares, DERIVED at run time so a leg added
     later is profiled with no edit to the tool. That includes every kit self-test (`subject = "kit"`
     and `chunk = "selftests"` legs). It also includes every guarded leg, with no guard applied. The
     `tools/unattended/` suites that are not legs stay out: a standing owner rule forbids running
     them, 2026-08-23.
   - **Modes:** `--serial`, and a concurrent mode that admits the next leg only while host CPU load
     stays at or under 80% and memory load at or under 90%, both measured live. Say how load is
     sampled and what one admission costs.
   - **No contaminating parameters:** each leg runs with every `GATE_*` knob, every inherited
     `GIT_*` repository pointer and every override the bar's push path scrubs removed (the
     `BAR_SCRUBBED_KNOBS` list at `.githooks/pre-push:1839` and its relatives). The tool prints the
     set it removed, derived and not typed. Find any other environment a leg's verdict depends on,
     and say how the tool holds it constant.
   - **No ceilings:** no per-leg timeout, no whole-run wall, no reaping, so every value is the true
     one. Every log and every scratch record is preserved under one run directory, and nothing is
     deleted on exit.
   - **A full profile per leg:** wall time; user and kernel CPU; peak and average memory; I/O counts
     and bytes; exit code and verdict; the number of processes spawned and the cost of spawning them;
     and per process its command line, parent, start, end, CPU and peak memory. Add anything else a
     full profile needs, and say why each field earns its place. Also record a host-load timeline,
     the foreign-load census, and the run's envelope as `profile_bar.py` records it.
   - **Stall detection that reports and never kills:** a leg is STALLED when, over a declared window,
     its process tree's summed CPU delta (successive `scan_processes` samples, walked with
     `build_walk` from the leg's root process) stays under a threshold AND its log stops growing.
     Process churn is context only. This build's hung canary kept a sampler spawning `sleep 60` while
     blocked on a FIFO, so churn alone would miss it. Report the stalled tree in detail and leave it
     running. `classify.py`'s age-ceiling verdicts are NOT the stall test: they need the ceiling this
     tool removes, and their lifetime rate hides a leg that worked and then hung.
   - Find the candidates for each measurement and the test each could lose (BUILD-METHOD M12),
     before choosing. Weigh at least these:
     - Windows Job Objects per leg, whose kernel accounting counts total processes, user and kernel
       time, peak memory and I/O exactly, short-lived processes included;
     - polling `census.py` for per-process detail;
     - a process start/stop event trace, which may need administrator rights.

     Name what each cannot see, on this node and on a POSIX node.
   - State the output format and where the record lands, so `derive-ceilings.py` and the profile
     tables can read it, and say whether `derive-ceilings.py` should admit its readings.
   - Name it through `.lexicon.conf` (`lexicon.py --suggest`), and declare its kit home, its
     descriptor rows and its own self-test leg, with the leg's argv reading the tool's own fixtures
     rather than running the real bar.
   - Order: after every other unit of this build, so the closing bar it is first used on runs over
     the fixed tree. Bump the version of whichever kit it lands in.

### Acceptance
- `--serial` over a two-leg fixture manifest, one leg spawning N processes, records N for that leg
  and per-process rows for each.
- The concurrent mode, given a fixture leg that holds CPU, admits no further leg while load is over
  80%.
- A fixture leg that blocks on a FIFO while a child spawns `sleep` reads STALLED. A fixture leg that
  works steadily for longer than the window does not.
- A leg run under the tool sees none of the removed knobs: a fixture leg prints its environment and
  the tool's record shows the set it removed.
- After the run, every log and record is present on disk.

### Gates
`run-gates canary` · `run-gates gov canary` · `shell hygiene (a fork spent on builtin work)` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `govkit selfcheck` · and the new tool's own self-test leg

### Non-goals
- No change to the merge bar's own behaviour, its ceilings or its legs. This tool measures, it does
  not gate.
- No running of the `tools/unattended/` self-test suites.

### Limitations
- Children run no bar and no whole suite. Verify with fixture manifests and hermetic probes; the
  first full profiled run is the main loop's, at the close.
- Under MSYS, `/tmp` and `C:/…/Temp` name one directory; compare through git.

### Reuse
`profile_bar.py`, `derive-ceilings.py`, `census.py` `scan_processes`, `reap.py` `build_walk`,
`scope.py` `derive_scope`, the runner's `measure_spawn_cost` and per-leg census, and the
`gate-legs.json` reader the runner and `run-selftests.sh` already share.

## Drawn from the session

> there is already a process monitor tool in this repo, how can it be used for stall detection?
— owner, 2026-10-14

## Owner confirmation

Asked: (the owner's own instruction)
Answer: Add another feature to this build - a gate profiling tool

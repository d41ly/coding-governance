# Appendix — The run-gates and push-side self-test legs: where the time goes, and ranked levers

**Serves:** research TOOL-aMeteredSweep-1

A read-only research pass by one of five agents on 2026-10-08, kept verbatim below its first heading. It ran no suite: every saving is an ESTIMATE from static spawn counts against the profiled bar in `2026-10-08-build-TOOL-aMeteredSweep-1-legs.tsv`, and the synthesis that ranks across all five is `2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`. Line citations are against `fa68a767` plus this unit's fixes.


This is read-only research. Nothing was run. Every figure below is either one of the measurements you
supplied, or a static count from the code converted at the recorded spawn cost. The recorded cost on
node a is 251 ms (one record) to 319 ms (`tools/lib/lib-selftest.sh:59`) per quiet spawn, and 751 ms
per git spawn (auto-memory). Treat every "est. s saved" as an order of magnitude, never as a promise.

## 0. Framing: what actually bounds the bar

- **The profile's own numbers.** Floor is 5769 s (the canary) and throughput is 5483 s (work / 8).
  They are within 5% of each other. **Sharding the canary by itself buys at most about 286 s of
  ideal**: the bound moves from the floor to throughput, and the next floor is memory-hygiene
  self-test at 4801 s, which is not one of these legs.
- **The observed wall was 13324 s, 2.3x the ideal.** About 4033 s of it is SERIAL RETRIES, which
  run after the pool drains. Three of these legs overran their ceilings in the pool and paid a
  serial retry on the critical tail: pre-push self-test (402 s), run-gates run-log line (175 s) and
  push-main self-test (242 s). That is 819 s of tail wall.
- **So the levers that cut total WORK move the bar the most.** They lower throughput, lower
  contention (which is what pushed those three legs over their ceilings), and shrink the canary as
  a side effect. These twelve legs are 16962 s of the 54049 s pool, which is 31% of it.
- **One cause dominates all of them: the nested bar.** The canary, evidence, turnstile, runlog and
  profile-bar suites drive about 270 nested `run-gates.sh` invocations between them. Each pays the
  runner's whole startup and teardown, plus a per-leg overhead of about 25 spawns. Cutting the
  runner's own spawns is the one change that speeds up all five suites at once. It also speeds up the
  real bar a little.

### The cost model, and how far to trust it

- **Static spawn census of `tools/run-gates/run-gates.sh`, per nested bar.** Roughly 80 spawns, about
  22 of them git, and 3-4 python launches:
  - `resolve_python` at :191;
  - the legs parse at :1909;
  - `PROF_CEILING_MAX` at :962, when a table is present;
  - `resolve_kit_dir` at :1010;
  - git `rev-parse` at :98, :214, :243, :1044 and :1484;
  - `fingerprint` twice, at :1881 and :3750;
  - porcelain at :1896;
  - the header's git at :2166-2189;
  - the stamp's git at :3827-3875;
  - the turnstile's `ls|sort|head` at :1285;
  - 19 execs after the last leg (measured by `run-gates run-log line` AC4: "baseline 19").
- **Per leg, inside `runleg`** (:2358-2463) **and `report_one`** (:2514), about 25 spawns:
  - `date +%s%N` twice, at :2369 and :2408;
  - `cat` at :2407;
  - `leg_log` `$(printf|tr)` at :2424 / :252;
  - `redact` sed twice, at :2426 and :2440;
  - `chmod` twice, at :2427 and :2441;
  - `input_key` at :2452, which is `git ls-files|sort|grep…|git hash-object`, and is computed a second
    time at :2242;
  - `mv` twice, plus `ts_hb`'s `$(date)` and `mv` at :1060;
  - `cat` again at :2522;
  - `live()` `jobs -rp | wc -l`, which is a fork plus `wc` on every dispatch check (:3509).
- **Checked against the canary's own reading.** About 150 nested bars times 80, plus about 700
  fixture-leg runs times 25, is about 29,500 spawns. At 0.25 s that predicts about 7400 s, against a
  measured 4080 s quiet. **The static model over-predicts by about 1.8x, so every canary figure below
  is multiplied by 0.55.** The cheap fix for this uncertainty is in §4, step 0.

## 1. Ranked levers

The figures are quiet seconds saved. Under contention multiply by 3-5x, comparing the pool column
with the serial-retry column.

| # | Leg(s) | Lever | Est. s saved (quiet) | Effort | Risk |
|---|---|---|---:|---|---|
| 1 | canary, evidence, turnstile, run-log line, profile-bar (+ real bar) | **Runner per-leg spawn cut**: `EPOCHREALTIME` for the `date` pair, `read`/`$(<)` for `cat`, a bash `${1//[^A-Za-z0-9._-]/_}` for `leg_log`'s `tr`, `redact` only when the output contains `://` with an `@`, `umask 077` for the `chmod`s, `input_key` computed ONCE per leg before dispatch, `ts_hb` on `$EPOCHSECONDS`, `live()` via `jobs -rp >file; mapfile`. 25 → about 8 spawns per leg | **~1270** (canary ~970, evidence ~125, turnstile ~80, run-log ~55, profile ~35); real bar about 175 s of leg work | M | M |
| 2 | same five | **Runner per-bar spawn cut**: one `git rev-parse --show-toplevel --show-prefix --git-dir --git-common-dir HEAD` replaces 6-7 calls; the manifest blob and HEAD computed once (header and stamp); the ceiling-max and kit-dir pythons merged into the legs-parse python, so one python per bar instead of 3-4; the turnstile's `ls\|sort\|head\|basename` replaced by a glob; `ts_now` on `$EPOCHSECONDS`. About 80 → 55 spawns | **~910** (canary ~520, evidence ~155, turnstile ~100, run-log ~105, profile ~25) | M | M |
| 3 | canary | **Shard it into 4 legs**, cut by MEASURED section cost (precedent: TOOL-aGraftedHelix-41's region shards). Per-shard floors summing to `FLOOR_ASSERTIONS=324`, and a shared prologue | Floor 5769 → about 1500 contended (largest shard). Bar ideal −286 s alone; with #1 and #2, the next floor (4801) binds | M-L | M |
| 4 | pre-push self-test | Run the decision-only arms through a direct hook invocation, as arm 9 and `pre-push.runlog.test.sh` `run_hook` already do. Keep about 10 real-push witnesses, plus one env/argv/stdin equivalence witness | ~120-200 quiet; and it stops the overrun that cost a **402 s serial retry** | M | M |
| 5 | canary | **Clamp arms** (:689-800): assert the clamped width through `--print-profile` (printed at :975, after the clamp at :719). Keep ONE real width-0 bar for termination. Grade `clamp_expired_verdict` with a stub runner that hangs or exits | ~120 quiet; **~480 contended**, which is what this bar burned on 3 expired arms and the spun-outcome SKIP; it also restores 4 arms that SKIPped | S-M | L |
| 6 | canary | Section-4 arms that read only the profile line (`profname`/`profline`, 28 sites, `runp` :1291) move to `runp --print-profile`, so they pay startup only. Keep real bars for every VERDICT assertion | ~150 | S-M | L |
| 7 | canary | 4g whole-run wall (:1895-1966): the unwalled control `sleep 120` → 20, and the `_cel - _wel >= 30` comparison (:1943) → "the control ran GREEN and its ledger row ≥ 15 s" | ~100, and one elapsed-time arm removed | S | L |
| 8 | all suites | Fixture git identity from the ENVIRONMENT: `GIT_AUTHOR_*`/`GIT_COMMITTER_*` plus `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false`, exported once per suite. This deletes the per-repo `git config` triples (about 300 dynamic git spawns across these suites) | ~75-225 | S | L-M |
| 9 | canary, run-selftests | Run the canary's 3g four reps concurrently on four fixture copies. Work is unchanged; the shard's wall falls | ~150-250 wall of that shard | S | L |
| 10 | canary | Rendezvous tick (:525-538): `n=$(ls … \| grep -c .)` → `set -- "$d"/*.up` (no spawn), and a 30-tick bound → a 3 s `EPOCHREALTIME` deadline. The width-1 run currently pays about 120 ticks × 3 spawns | ~65 | S | L |
| 11 | run-log line, pre-push run-log line | Parse a journal line once into an assoc array. `read_field` becomes builtins (86 + 103 call sites) and `measure_lines` becomes `mapfile` (37 + 44) | ~60 + ~75 | S | L |
| 12 | evidence | Event-driven move and kill arms (:513-528, :370-385): the leg waits on the mover's flag instead of `sleep 60`; kill -9 when the header appears instead of at `REC_KILL` 20-50 s | ~85, and one SKIP path and one flake removed | S | L |
| 13 | push-main self-test | Cases 24 and 25 (:652-653, :681-682) each clone the WHOLE repo, 3633 files checked out. Clone once and run 25 on its own branch in the same clone | ~20-40 quiet / ~100 contended, toward its **242 s retry** | S | L |
| 14 | evidence | `rec_repo` (×23) and `ru_repo` (×7) built once as a template, then `cp -a` per arm | ~40 | S | L |
| 15 | canary | 1e unbounded leg `sleep 45` → 8 (:332; the ceiling is 2 s, so any duration above about 6 s discriminates) | ~37 | S | L |
| 16 | turnstile | R16 (:845): kill the run when `queued at position` appears in its output instead of `timeout 45` | ~35 | S | L |
| 17 | run-selftests, all `resolve_python` callers | `run-selftests.sh --check`: merge its 3 python passes (:417, :529, :766) into one. Also: resolve python by USE (the first real python call is the probe), not by a separate `-c "import sys"` run | ~50 (run-selftests); about 1 python per script invocation elsewhere | M | M |
| 18 | canary | `build_hv_repo` ×11 (:2761) once, then `cp -a`; `build_age_fixture` (:2300; 13 commits × 4 fixtures) through one `git fast-import` | ~55 | S-M | L |
| 19 | evidence | derive-ceilings section (:998-1491; 27 python launches, ~98 `printf\|awk` asserts) in one python process | ~30 | M | L |
| 20 | pre-push bar self-test, profile-bar | Cache `git rev-parse --git-dir` per fixture (bar self-test :193); batch profile-bar's pure inline-python arms (16 launches) | ~10 + ~8 | S | L |
| — | branch-guard self-test, run-gates adopter e2e | **No lever is worth its risk**: 124 s and 143 s contended, small fixtures, no nested bar | 0 | — | — |

**Effort note for #3 and any new leg row.** A new leg trips the meta-gate set
(`memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`). Each shard needs:

- a `kit.toml` `[[gate_leg]]`;
- a `selftest-budgets.txt` row and `ceiling-evidence` rows;
- a codebase-map claim;
- a testsuite-counts line.

Runner edits (#1, #2) owe a lexicon verb for any new helper, a run-gates kit version bump, and the
`runlog` AC4 and pre-push AC7 exec comparisons. Those comparisons are relative, so they stay green.

## 2. Per leg

### run-gates canary — `bash {prefix}/run-gates/run-gates.test.sh` (ceiling 13200)

- **(a) What it guarantees.** The manifest is well-formed, the runner sources every leg from it, and
  every runner behaviour holds on fixture repos: pool equivalence, ceilings, wall, profiles,
  attribution, owned scratch, honest verdicts and the memory pause.
- **(b) Cost.** 5769 s in the pool, contended and FAILED (the memory-pause race, since fixed). 4080 s
  on a quiet re-run. The bar's floor.
- **(c) Where the time goes.** About 132 static nested-bar sites, about 150 dynamic. By section,
  counted by line range:

  | Section | Nested bars |
  |---|---|
  | 1 | 2 |
  | 3a-f | 11, plus up to 12 timed clamp runs |
  | 3g | 4 reps × a 30-leg width-1 bar (:825) |
  | 3h | 13 |
  | 3i | 6 |
  | 4 | 27 |
  | 4g / 5 / 6 / reap | 8 |
  | 7 attribution | 17, each over a 19-leg manifest plus runs at R |
  | 8 | 8 |
  | 9 | 20 |
  | 10 | 6 (`--print-profile`) |
  | 11 | 15 |

  - **Fixture repos.** About 22 `git init` sites, multiplied dynamically by the builders: 11 hv
    repos; 4 age fixtures of 13 commits each (:2318-2323); 4 attribution and replay fixtures; the
    owned fixture.
  - **About 41 `git config user.*` and 9 `core.autocrlf` sites.**
  - **Fixed waits:**
    - 1c's pipe-hold control, 30 s (:294);
    - 1e's unbounded 45 s leg (:332, :359);
    - the rendezvous width-1 run, 4 legs × the 30-tick wait, where each tick is fork + `ls` + `grep`
      + `sleep`;
    - 4h's sleeper control, 20 s (:1470);
    - 4g's unwalled control, 120 s (:1900);
    - 7's timed legs at 2, 3 and 1 s ceilings, retried serially, across 4 A1 bars;
    - 11's memory-pause sleeps.
  - **Clamp arms (:742).** Up to 5 runs + 3 controls + 2 verdict runs at a 60 s budget each. On this
    bar three expired and SKIPped, with the spun-outcome arm also SKIPped (gate log), which is about
    480 s for no coverage.
  - **Python.** 29 sites, mostly fixture writers.
- **(d) Levers, ranked:**
  - #1 and #2, the runner cuts: ~1490 s;
  - #3, the shards;
  - #5, the clamp arms;
  - #6, profile-line-only arms through `--print-profile`;
  - #7, the wall control;
  - #9, 3g concurrent;
  - #10, the rendezvous;
  - #18, fixtures;
  - #15, the 1e sleep;
  - **per-assertion `printf | grep` pipelines.** About 324 assertions × about 1.5 spawns ≈ 90 s.
    Converting them to `case` patterns is mechanical, but grep is line-anchored and `[[ =~ ]]` is
    not, so a `^…$` pattern must become `*$'\n'"…"*`. That is medium risk for about 50 s, so do it
    last, if at all.
  - **Nested bars that do not grade the turnstile or the profile** can run `GATE_TURNSTILE=0
    GATE_PROFILE=minimal`, as `run_hv_bar` already does. That saves about 10 spawns per bar (~70 s).
    But 3a asserts exactly one `gate queue: acquired` line, so this is per-arm work.
  - **Expected after #1, #2, #5-7 and #10:** ~4080 → ~2200 s quiet. Four shards then bring each to
    about 500-700 s.
- **(e) Full rebuild (the shard split).**
  - **The cut.** Shared prologue: resolvers, `KITDIR`, `PYBIN`, the `HAVE_TIMEOUT` probe and the
    rendezvous text. Sections 3h, 3i and 4 copy `$SCRATCH/…/run-gates.sh`, which is a byte copy of
    `$KITDIR/run-gates.sh`, so point them at `$KITDIR`. Four shards, cut by measured cost, for
    example:
    - S1 = 1 + 3a-3g;
    - S2 = 3h + 3i + 4;
    - S3 = 4g + 5 + 6 + reap + 7;
    - S4 = 8 + 9 + 10 + 11.
  - **Keeping the arm inventory.** The canary prints NOTHING per passing arm, so
    `tools/lib/extract-arms.sh` would report it UNEXTRACTABLE. **Step one of any rebuild** is
    therefore a per-arm `ok <label>` line, landed before the split, so the inventory can be diffed
    before and after. Per-shard floors must sum to 324, and a declaration check should assert that
    sum.
  - **Keeping every staged break.** Move each `fail` message byte-identical; check-arms wants the
    whole refusal text. Re-observe each recorded staged break against its shard. The ones named in
    the code include:
    - 1e's ceiling ignored;
    - 3c width-1 collapse;
    - 4h's `$(timeout)` capture;
    - 8's moved tree;
    - 9a's empty manifest;
    - 11's memory-pause arms;
    - 3a's line filter.
  - **The cost of not doing this first.** It goes up by every shard row the meta-gates demand.
- **(f) Measure before cutting, at near-zero cost.** Print `canary: section <id> <EPOCHSECONDS>` at
  each section header. That is a builtin, so no spawn. The next natural run then yields the real
  section table that the shard cut needs. aGraftedHelix-41 cut by measured region cost the same way.

### run-gates evidence — `bash {prefix}/run-gates/run-gates.evidence.test.sh` (ceiling 7040)

- **(a)** A red or green leg's own output, the run record (header, verdict, ledger) and the census
  survive on disk. derive-ceilings admits only windowed rows.
- **(b)** 2294 s in the pool (ok). About 1000 s quiet is the estimate.
- **(c) Where the time goes:**
  - about 45 nested bars: 21 `rec_run`, about 14 `ru_run`, 6 `run`, plus direct calls;
  - 23 `rec_repo` and 7 `ru_repo` builds (:304-340), each about 11 spawns (`mktemp`, `cp` ×2,
    `git init` + config ×2, `add`, `commit`, `update-ref`, `symbolic-ref`), plus `rec_legs` commits;
  - fixed waits:
    - the moved-tree arm's leg sleeps a full 60 s (:314, :511-523);
    - the hard-kill arm waits `REC_KILL` 20-50 s (:370-376);
    - the census arms' load legs run 5-6 s;
    - a `ps-slow` stub at 2 s (:772);
  - the derive-ceilings tail: 27 python launches and about 98 awk-per-assert checks.
- **(d) Levers:**
  - #1 and #2: ~280 s;
  - #12, event-driven move and kill: ~85 s;
  - #14, repo template: ~40 s;
  - #19, one-python derive-ceilings: ~30 s;
  - #8, env identity: ~15 s.
- **(e) Rebuild.** Not warranted. The arms are independent and already hermetic; the cost is the
  runner's.

### run-gates turnstile — `bash {prefix}/run-gates/run-gates.turnstile.test.sh` (ceiling 8210)

- **(a)** Two bars on one repo never overlap. A dead or stalled holder is reaped. A live holder is
  not reaped. FIFO order holds. The turnstile fails open and never changes the exit code.
- **(b)** 1978 s in the pool (ok).
- **(c) Where the time goes:**
  - about 29 nested bars and about 25 `mk_repo` builds (:170-198), each git init + config ×2 +
    commit;
  - the time is INHERENT wall clock: TTLs of 1-12 s, `TS_LONG` of 4-25 s, `TS_DWELL` 3 s, and the
    1 s-tick beacon polls (:404, :582, :590, :644);
  - R16 burns a fixed `timeout 45` (:845);
  - R6b's bounded run is 180 s (:390).
- **(d) Levers:**
  - #1 and #2: ~180 s;
  - #16, R16's event kill: ~35 s;
  - #8: ~15 s.
- **(e) Rebuild option: a clock seam.** The runner would read `ts_now` from a file under an env knob
  that only a test sets. TTL arms then advance time instantly instead of sleeping, which could remove
  most of the ~300-400 s of inherent waits.
  - **Cost.** A new runner knob must be classified by pre-push.test's `check_knob_classes`, needs a
    canary arm proving production ignores it, and needs a kit bump.
  - **Risk.** Medium. A time seam in a shipped runner is a reap lever if it is ever honoured outside
    a test, so it must be refused unless a test-only marker is present.
  - **Inventory.** Unchanged: the same arms over the seam. Every arm that grades the ticker against
    REAL time must keep a real-time variant.

### run-selftests self-test — `bash {prefix}/run-gates/run-selftests.test.sh` (ceiling 2040)

- **(a)** Every refusal of `run-selftests.sh` fires: declaration, sweep, calibrate, attribution, wall,
  GOV_NODE and the memory pause.
- **(b)** 1480 s in the pool (ok): 142 arms at width 1.
- **(c) Where the time goes:**
  - per arm, `lib-selftest.sh` `_st_run_one` (:142) does a `cp -a` of the snapshot (a git repo with
    hook samples), then `bash -c` the body, then the subject;
  - the subject is usually `run-selftests.sh`, which resolves python and runs 1-4 heredoc pythons;
    `--check` alone runs 3 (:417, :529, :766);
  - about 30 arms run pooled or calibrate sweeps over sleeping fixture suites: `suite-slow` 3 s,
    `suite-mid` 5 s, `cache` 4 s, `over` 3 s, and 3 s walls over the 30 s and 20 s suites.
- **(d) Levers:**
  - #17, merging `--check`'s pythons: ~50 s;
  - an empty `GIT_TEMPLATE_DIR` in `build_repo` (:195), so the snapshot carries no `hooks/*.sample`
    and each `cp -a` copies about 15 fewer files: ~20-30 s;
  - `SELFTEST_INNER_WIDTH=2` for this leg: about half the wall but the same work. Worth it only while
    the leg is on the critical path, which it is not.
- **(e) Rebuild.** Not warranted. Each arm needs its own mutated copy by design.

### run-gates run-log line — `bash {prefix}/run-gates/run-gates.runlog.test.sh` (ceiling 1200)

- **(a)** Every bar appends exactly one parseable journal line with the right verdict, rc and signal
  status, and the writer adds no external exec.
- **(b)** 1201 s in the pool (TIMEOUT); 175 s on the serial retry, which also FAILED. **The red is a
  real one, separate from cost:** AC8 EXITS finds the census watcher's `exit 0` sites
  (`run-gates.sh` `arm_census`, about :2763-2766) missing from the exit table.
- **(c) Where the time goes:**
  - 21 `run_bar` calls, plus 4 signal bars (AC3, each leg `exec sleep 30`, killed on a ready file),
    plus 3 `bash -x` traced bars (:529);
  - 86 `$(read_field)` and 37 `$(measure_lines)` sites, each a fork plus awk, or wc plus tr (:267-276);
  - `check_journal` python passes.
- **(d) Levers:**
  - #1 and #2: ~160 s;
  - #11, the builtin journal reader: ~60 s.
  - **Reuse its `measure_execs` (:502)** with the window opened at line 1 as the deterministic
    spawn census for #1 and #2. The instrument already exists.
- **(e) Rebuild.** None needed.

### profile-bar selftest — `bash {prefix}/run-gates/profile_bar.test.sh` (ceiling 1910)

- **(a)** The profiler names the right regime (floor or throughput), the ordering of the two bounds,
  and every refusal.
- **(b)** 568 s in the pool (ok).
- **(c) Where the time goes:**
  - 8 `profile_bar.py` runs, each driving one real nested bar of 2-4 sleeping legs (`sleep 6`, `2` ×4,
    `0.2`, `0.3`);
  - 16 inline python launches.
- **(d) Levers:**
  - #2: ~25 s;
  - #1: ~10 s;
  - #20: ~8 s.
  - The regime sleeps must stay: the 6 s against 0.2 s separation is what keeps the regime stable
    under spawn noise.
- **(e)** None.

### pre-push run-log line — `bash .githooks/pre-push.runlog.test.sh` (ceiling 600)

- **(a)** Every push writes a START/END pair or a once-line, with no credential, under the cap, and
  every exit is mapped.
- **(b)** 564 s in the pool (ok).
- **(c) Where the time goes:**
  - 12 real pushes, 20 direct `run_hook` calls and 3 traced runs;
  - one real runner copy (AC4);
  - 103 `$(read_field)` and 44 `$(measure_lines)` sites (:289-299).
- **(d) Levers:**
  - #11: ~75 s;
  - #8: ~5 s.
- **(e)** None.

### pre-push self-test — `bash .githooks/pre-push.test.sh` (ceiling 1780)

- **(a)** A real `git push` fires the hook, and the hook classifies every case: marker, default
  branch, renamed ref, multi-ref, stamps, inherited red, docs scoping and knob classes.
- **(b)** 1786 s in the pool (TIMEOUT at the ceiling); 402 s on the serial retry.
- **(c) Where the time goes:**
  - about 132 push and decide sites, roughly 100 real `git push` calls; each spawns push, send-pack,
    receive-pack and the connectivity check, plus the 1617-line hook (89 `$(…)`, 81 git sites, 24
    python mentions);
  - `decide()` (:242) adds a `git commit` per call;
  - 29 `git init` sites, 87 commits, and 24 `git config user.*` sites.
- **(d) Levers:**
  - #4, direct invocation for decision-only arms: ~120-200 s quiet, which takes the leg back under
    its ceiling under contention, and that saves the 402 s retry on the tail;
  - #8: ~20 s;
  - build the common work+remote pair once and `cp -a` it per family: ~15 s.
- **(e) Rebuild option: a two-tier harness.**
  - **Tier A.** About 10 real pushes witness that the hook FIRES, that a red blocks the remote from
    moving, and the multi-ref and renamed-ref cases.
  - **Tier B.** Every classification arm feeds the hook its argv and stdin directly.
  - **The bridge.** One witness arm captures the env, argv, cwd and stdin that git really hands the
    hook, and asserts the tier-B launcher supplies the same. That is what pins the equivalence.
  - **Risk.** Medium. The header's stated purpose is a real push, so get the owner's ruling first.
  - **Inventory.** Each arm keeps its `ok`/`bad` label, so `extract-arms.sh` diffs it directly.

### pre-push bar self-test — `python3 .githooks/pre_push_bar_selftest.py` (ceiling 600)

- **(a)** The hook refuses a bar it cannot vouch for, and a mutated copy with those arms disabled
  LANDS each hostile value.
- **(b)** 473 s in the pool (ok).
- **(c)** 2 fixtures, about 25 real pushes, each with a `git commit` and a `git rev-parse --git-dir`
  (:189-203).
- **(d)** #20: ~10 s. The pushes must stay real: the docstring records landings observed only through
  a moved remote.
- **(e)** None.

### push-main self-test — `bash {prefix}/push-main.test.sh` (ceiling 580)

- **(a)** The lander and the marker gate behave for attended and in-place landings, refusals, mints
  and missing kits.
- **(b)** 582 s in the pool (TIMEOUT); 242 s on the serial retry.
- **(c) Where the time goes:**
  - cases 24 and 25 each run `git clone --bare $SRC` plus a full `git clone` checkout of 3633 files
    (:652-653, :681-682), and then a `--prepare` over that full tree;
  - 7 inits, 40 commits and 2 small clones elsewhere.
- **(d) Levers:**
  - #13, one big clone: ~20-40 s quiet;
  - #8: ~10 s.
- **(e)** None.

### branch-guard self-test — `bash .githooks/pre-commit.test.sh` (ceiling 300)

- **(a)** The pre-commit guard refuses off-default commits, the map gate, and the hygiene leg's
  kit-root rungs.
- **(b)** 124 s in the pool (ok).
- **(c)** 2 repos and about 13 commits through the hook.
- **(d)** No lever is worth it beyond #8 (~5 s).

### run-gates adopter e2e — `bash {prefix}/run-gates/adopt-run-gates.test.sh` (ceiling 460)

- **(a)** The adopter's `--check` agrees with the runner, and the adopter derives its own prefix.
- **(b)** 143 s in the pool (ok).
- **(c)** 2 repos and 6 `adopt-run-gates.sh --check` runs, with no nested bar.
- **(d)** None worth it.

## 3. Wall-clock-timed arms: flake risk on a loaded host

Ordered by likelihood.

1. **`tools/run-gates/run-gates.turnstile.test.sh:534`.** The heartbeat refresher writes
   `$(date +%s)` every 0.25 s against `GATE_TURNSTILE_TTL=2`. That is a fork plus `date` plus
   `sleep` per tick, at 1-2 s each under load, so the period can pass the TTL. The runner then reaps
   the holder the arm needs ALIVE, and the arm reds. The fix is `printf '%s' "$EPOCHSECONDS"`, which
   spawns nothing.
2. **`run-gates.turnstile.test.sh:359-372` (R6), rooted in `run-gates.sh:1096-1106`.** It relies on
   the runner's ticker (`GATE_TURNSTILE_TICK=1`) refreshing faster than `TTL=6`. Each tick costs
   `sleep` + `$(cat nonce)` + `kill -0` + `$(date)` + `mv`, about 4 spawns, so under load the period
   can pass 6 s and a waiter reaps a LIVE holder. Fixed by #2's `ts_now` → `$EPOCHSECONDS` and
   `cat` → `read`.
3. **`tools/run-gates/run-gates.evidence.test.sh:513-519`.** The mover waits at most 20 × (`cat` +
   `sleep 1`) for the run's header, then moves the tree ANYWAY. If startup outlasts that window (this
   bar's clamp arms show startup above 60 s), the move lands before `FPRINT_START`, nothing is
   recorded, and the arm reds. Fixed by #12: move only once the header exists, and make the leg wait
   on the mover's flag.
4. **`tools/run-gates/run-gates.test.sh:725-800` (clamp arms).** A 60 s budget per run. They SKIP on a
   loaded host, which they did on this bar, four times. That is not a red, but it is lost coverage.
   Fixed by #5.
5. **`run-gates.evidence.test.sh:370-385`.** The `REC_KILL` timer can land during startup, giving an
   announced SKIP of the crash case. Fixed by #12.
6. **`run-gates.test.sh:1943`.** `_cel - _wel >= 30` is an elapsed comparison with a 112 s nominal
   gap. Low risk, but fixed by #7.
7. **`run-gates.test.sh:1474`.** `t_ctl - t_timed >= 10` (a 20 s sleeper against a 3 s bound plus its
   retry). Low-moderate risk.
8. **`run-gates.turnstile.test.sh:582`, `:590`, `:644`, `:404`.** Bounded beacon polls of 30, 15 and
   12 iterations; under extreme load startup can outlast them. Each announces itself with a `nope`
   or `skipped`. Low.
9. **`run-gates.test.sh:297`.** `_took > 20` over a 2 s bounded run, which has a large margin. Low.
10. **`run-gates.turnstile.test.sh:899`.** `t17 < 180`. Low.

The memory-pause arms, the 9b queue arms, the AC3 signal arms in both runlog suites and the
run-selftests AC9 stamps all order on files or rows, not on the clock. I found no risk there.

## 4. Suggested order

0. **Measure first.**
   - Add the canary's section stamps (§2, canary (f)).
   - Run `measure_execs` over one full fixture bar, window from line 1, to replace this report's
     static spawn estimates with a real count.
   - Both are spawn-free or single-run, and both decide the shard cut and validate #1 and #2.
1. **The cheap, low-risk items:** #5, #6, #7, #10, #12, #13, #15, #16, and the two flake fixes in §3
   (1 and 2).
2. **#1 and #2, the runner spawn cuts.** These are the work lever. Rerun the four suites that grade
   the runner's text: canary 1d, runlog AC4, pre-push AC7 and the knob classes.
3. **#4**, after an owner ruling on real-push versus direct-invocation.
4. **#3, the canary shards.** Only once the section table exists. Land the per-arm `ok` lines first.

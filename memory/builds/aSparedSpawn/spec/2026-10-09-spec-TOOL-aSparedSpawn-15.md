# TOOL-aSparedSpawn-15 — the remaining clock-bound arms on the flake list, ordered or calibrated

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-1 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Stop the self-test arms that read a wall clock from redding on a loaded host. aMeteredSweep fixed four
such arms and named the rest (`2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md`, "Arms whose
verdict reads a clock"); a spawn on node `a` costs 21 ms quiet and 632 to 818 ms loaded (PINNED,
measured 2026-10-09, the round-two menu's cost table), so a typed few-second margin is noise there.
This unit applies the pattern that held: order on a fact where one exists, and where a clock must
remain, measure the host first and derive the bound from that reading.

## 2. Scope (IN)

Each site was re-read on this tree at 22efab65; line numbers are that tree's. Three classes, and each
item names its class:

- **S1** — Speed assertion, `tools/hooks/agent-cap.test.sh:2165-2172`: the quadratic-budget arm
  asserts 8000 literals on one line finish in 10 s by `date +%s`. It times a CONTROL first in the same
  process, the same literals one per line, and asserts the one-line run takes at most four times the
  control plus 2 s, both read from `EPOCHREALTIME`. The absolute hook timeout is not this arm's
  question and is stated as such in its comment. Observed by AC1.
- **S2** — Spawns in a heartbeat, `tools/run-gates/run-gates.turnstile.test.sh:534`: the refresher
  writes `$(date +%s)` every 0.25 s against a 2 s TTL. It writes `$EPOCHSECONDS`, which forks
  nothing. Observed by AC2.
- **S3** — Spawns in the runner's ticker, the R6 arm at `run-gates.turnstile.test.sh:359-372`, rooted
  in `ts_tick_start` in `tools/run-gates/run-gates.sh`: each tick reads the nonce through `$(cat ...)`
  and the time through `$(ts_now)`, which is `date +%s`. The tick reads both with builtins, keeping
  `${EPOCHSECONDS:-$(date +%s)}` as its fallback the way the runner's owner record already does. The
  arm then measures the host before it runs: ten spawns timed as `measure_load_ratio` in
  `tools/run-gates/foreign-prefix.gov.test.sh` does, giving one tick's period, and its TTL becomes
  three periods and never under 6 s, with `TS_LONG` the TTL plus 8 s. Observed by AC3.
- **S4** — Clock as an ordering, `tools/run-gates/run-gates.evidence.test.sh:513-519`: the mover
  waits up to 20 polls of `cat` plus `sleep 1` for the run's header and then moves the tree ANYWAY.
  It moves only once the header exists; if the run ends first, it moves nothing and the arm reds
  naming "the mover never saw the header" rather than grading a tree that did not move. Observed by
  AC4.
- **S5** — Clock as an ordering, `tools/unattended/unattended.test.sh:7822-7836`: `run_bounded` must
  return in under 20 s against a 2 s bound, and the control must take 20 s or more. Each sleeper
  writes a marker file when it finishes on its own; the subject arms assert the marker is ABSENT when
  `run_bounded` returns, and the control asserts it is PRESENT when the command substitution returns.
  The subjects' sleepers lengthen to 60 s at no cost, since nothing waits for them, and are killed
  after the assertion; the control's stays at 30 s. Observed by AC5.
- **S6** — Hang guards on polls that exit on their fact. The pass path never reaches these bounds, so
  each becomes a hang bound of 120 s, and the red path pays it:
  - `read_stub_log`, `derive_winpid` and `read_task_gone` in `tools/unattended/resume-tick.test.sh`
    (10 s, 5 s and 5 s today); every caller on this tree expects the positive fact;
  - `read_pl_exec_token` and the two orphan polls after it in `tools/unattended/unattended.test.sh`
    (about 10 s, 30 s and 15 s today);
  - govkit's lock wait in `tools/govkit/selftest.py:6230`, `time.time() + 30`, whose loop already ends
    when the first `update` exits;
  - `skills/session-kickoff/manifest-check.test.sh:834`, `timeout 10` around a `--card --path` whose
    question is "returned rather than blocked".

  Observed by AC6, AC7, AC8.
- **S7** — Each changed arm's suite keeps its declared budget, and the kits owe their version bumps.
  NOT OBSERVED by a criterion of its own: the bumps are graded by the kit-epoch leg, and a budget
  breach reds the runner that reads `selftest-budgets.txt`.

## 3. Non-goals (OUT)

- `foreign-prefix parity`'s row budgets, already scaled by `measure_load_ratio` in aMeteredSweep.
- The evidence suite's `REC_KILL` timer at `run-gates.evidence.test.sh:370-385`, the canary's elapsed
  comparisons at `run-gates.test.sh` lines 297, 1474 and 1943, and the beacon polls in the turnstile
  suite. Each already announces a skip or carries a wide margin; they are the next flake list, not
  this one.
- The `sleep 1` orderings of second-resolution stamps in `unattended.test.sh`, which the research rated
  low risk.
- A clock seam in the runner, the research's rebuild option for the turnstile suite.

### Edges

none

## 4. Design

The three classes take three remedies, and none of them types a speed bound:

| Class | What the clock was doing | Remedy |
|---|---|---|
| Speed assertion | a typed ceiling on how fast something ran | a control timed in the same process, and a ratio |
| Ordering | a sleep or a window standing in for "A happened before B" | a marker file or the run's own header |
| Hang guard | a cap on a poll that exits on its fact | a bound the pass path never reaches |

S3 is the one site where a clock must remain: a TTL is a time by definition. It follows the canary's
AC6 pattern in `tools/run-gates/run-gates.test.sh` (a one-leg bar timed first, the bound derived from
it, a floor kept) with the cheaper reading `measure_load_ratio` takes, ten spawns over
`EPOCHREALTIME`, since the property at stake is a tick's spawn cost and not a whole bar's.

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/govkit/selftest.py`
- `skills/session-kickoff/manifest-check.test.sh`

### Alternatives rejected

- **Raise every typed bound.** It moves the red to a heavier day and keeps the arm's verdict a
  function of the host; the speed assertion in S1 also stops detecting the regression it exists for.
- **One shared load-measuring helper in `tools/lib/`.** Five kits would each carry it inline, and a
  kit file may not name a sibling kit; S3 is the only site that needs the reading.
- **A clock seam in the runner.** Large, and S3's spawn removal reaches the same property.

## 5. Production-readiness checklist

- security: N/A — test arms and one ticker body; no input, write path or authority moves.
- perf / scale: the ticker drops two forks a tick; S5 removes no wait the control did not already pay; S6 costs nothing on the pass path and up to 120 s per arm on the red path.
- error / empty / loading states: S4's mover reds when it never sees the header; S3 prints its measured period and TTL; every hang bound's failure line names the bound it hit.
- observability: S1 prints both timings and the ratio; S3 prints the measured tick period and the derived TTL, as the canary's AC6 line does.
- risks: S1's ratio can mask a slowdown that is linear in both runs, which is not the defect it guards; S3's builtin fallback must keep working where `EPOCHSECONDS` is absent.
- testing: each arm observed red on a staged break, then green alone and green under twelve concurrent fork loops.
- migration: none for data; the hooks, run-gates, unattended, govkit and kickoff-manifest kits each owe a version bump.
- user docs: N/A — no user-facing behaviour changes; each arm's comment states its class and remedy.

## 6. Acceptance criteria

- **AC1** — When the quadratic arm runs against a hook with the per-quote prefix copy restored, it
  reds on the ratio; against the shipped `agent-cap.js` it passes alone and under twelve fork loops.
  Red when: the restored copy passes, or the shipped hook reds under load.
  fixture: twelve background `true` loops, the load the unattended suite's exec-token comment measured.
- **AC2** — When the refresher at the turnstile arm's expired-wait case runs under twelve fork loops,
  the holder survives and the arm records `queued_from=expired`. Red when: the runner reaps the
  holder, which is the defect `$(date +%s)` per tick exposed.
- **AC3** — When `ts_tick_start`'s loop is run with `cat` re-inserted, the R6 arm's printed tick period
  rises; with the shipped body under twelve fork loops a live holder longer than the derived TTL is
  not reaped. Red when: R6 prints `stalled holder`, or prints no measured period.
- **AC4** — When the evidence suite's moved-tree arm runs with the header write delayed past the run's
  end, it reds naming the mover; in the normal order it records `tree_moved` as yes in the verdict. Red when: a
  delayed header lets the arm pass, or the normal order records nothing.
- **AC5** — When `run_bounded` is given a bound that waits for the grandchild, the grandchild arm
  reds on the marker being present; the control still finds its marker. Red when: the broken bound
  passes, or the control's marker is absent on this host.
- **AC6** — When `read_task_gone` reads a pid the tick never killed, it returns 0 after its bound and
  the AC4 and AC13 arms red; when the kill lands, it returns 1 at the first poll that sees it.
  Red when: the unkilled pid reads 1, or a landed kill waits out the bound.
- **AC7** — When govkit's contention case runs under twelve fork loops, the lock is observed held and
  `[-12] AC5` passes in its first attempt or a later one. Red when: three attempts expire without
  observing the lock. cost: a slice of govkit's selftest, prologue plus that function.
- **AC8** — When `read_session_id` is staged to read stdin although `--session` answered, the S4 arm
  of the kickoff suite reds with exit 124 at its 120 s bound; unstaged, it passes. Red when: the
  staged break passes.

## 7. Gates

`agent-cap self-test` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `hook destinations self-test` · `lexicon naming predicates` · `manifest-check self-test` · `recall floor arms` · `review-join self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `run-gates turnstile` · `run-gates evidence` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 · the per-quote prefix copy restored · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC2 AC3 · a forking refresher and a forking tick, under fork loops · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC4 · the header written after the run ends · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · a bound that waits for the grandchild · none
New arm: tools/unattended/resume-tick.test.sh · covers AC6 · a tick that never killed · none
New arm: tools/govkit/selftest.py · covers AC7 · the lock wait under fork loops · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC8 · `read_session_id` reading stdin · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "calibrate a wall-clock bound from a measured spawn"` ranks
`check_gate_wall` and `read_bound_key` in `tools/unattended/lib-unattended.sh`, neither of which
measures a host; no existing seam fits as a shared helper, and the evidence is that the one landed
measurement, `measure_load_ratio`, is a function inside `tools/run-gates/foreign-prefix.gov.test.sh`
that the reuse index does not surface. S3 reuses its method; the canary's AC6 and clamp calibrations
in `tools/run-gates/run-gates.test.sh` are the pattern for derived bounds.

Recall terms used: wall-clock flake loaded host calibrated bound spawn floor measure_load_ratio clamp
budget turnstile TTL heartbeat order on rows

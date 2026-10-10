# TOOL-aSparedSpawn-3 — a ceiling-killed leg retries in the pool's drain tail, and a bar with no ledger dispatches longest-first

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

On the profiled bar the serial retry phase cost 4050 s, 30 % of the wall, while the pool's tail sat at
concurrency 2 to 3 for 2798 s; and with no ledger the legs dispatched in manifest order, so the floor
leg started 3445 s in. This unit starts a deferred leg's retry inside that idle tail, and orders a
ledgerless bar by the per-leg maximum the tree already tracks. The research simulated the two together
at 12885 s down to 7673 s at fixed contended durations; the width the previous unit sets decides how
much of that holds.

## 2. Scope (IN)

- **S1** — `runleg`, on a first attempt whose own ceiling fired by `check_ceiling_fired`'s predicate,
  writes a `<i>.defer` marker in the work dir before its `.rc`. The worker holds the rc, the bound and
  the seconds the predicate reads, so the decision is the one `report_one` makes, taken at completion
  rather than when the manifest-order reader reaches the leg. Observed by AC1.
- **S2** — The dispatch pass, once every first attempt is dispatched, starts `runleg <i> .retry` as a
  pool job for a marked leg with no retry yet, whenever the running count is at most one. Markers are
  found with a glob, so the decision forks nothing. The job writes the pid file the wall reads, and the
  memory pause applies to it as to any dispatch. Observed by AC1 and AC3.
- **S3** — `report_one` keeps its deferral rule and its `GATE retry` line, wording per F2.
  `run_leg_retry`, after the drain, reads a tail attempt's result where one exists. A pass prints
  `GATE ok    <leg>  (retried after timeout)`, counts in `retried` and appends the `retry-passed`
  health event, all exactly as a serial pass does. A deferred leg with no tail attempt runs serially
  as today. Observed by AC2.
- **S4** — A tail attempt that does not pass is handled as F1 rules. Under the recommended (a), its
  files are set aside under a suffix of their own and the leg runs today's serial retry, alone, so every
  red retry verdict and every HOST reading still comes from an attempt that ran alone after the drain.
  Observed by AC4.
- **S5** — Dispatch priority in the legs-parse python (`run-gates.sh:2005`), per leg, in this order:
  the ledger's seconds; else the largest `ceiling-evidence.txt` reading for that leg, the file resolved
  beside the runner's own kit dir; else its declared `ceiling` divided by the median ceiling-to-evidence
  ratio over the legs carrying both, computed in the same pass; else 0. The hint stays advisory and the
  reporting walk stays manifest order. Observed by AC5 and AC6.
- **S6** — `tools/run-gates/README.md`'s retry section and dispatch-hint text describe the tail
  release and the priors. NOT OBSERVED: prose.

## 3. Non-goals (OUT)

- No change to which legs are deferred: only a fired ceiling, never an assertion failure, never a
  kill by anything else.
- No change to the HOST rule: a floor read before the bar, both attempts verified clear, the deciding
  attempt alone (`derive_host_note`).
- No hang detection by progress and no ceiling extension (the runner report's lever 8).
- No width change; the previous unit owns the width, and this unit releases at most one retry beside
  one running leg whatever the width.
- No ledger move to the common dir; a new worktree still has no ledger, which S5 makes harmless.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-2` — the calibrated width. Longest-first alone put the eight
  heaviest spawn-bound suites in the pool's opening together on aMeteredSweep's second bar and raised
  ceiling fires from 9 to 15; without a width set by measured spawn pressure, S5 manufactures the
  fires S2 then retries.

## 4. Design

**Today, re-verified at base 22efab65.** `report_one` (`run-gates.sh:2573`) defers a leg when
`check_ceiling_fired` (`:2920`) holds and prints `GATE retry`. Deferral happens when the manifest-order
walk REACHES the leg, which can be long after it finished. `run_leg_retry` (`:3033`) runs after the
pool's final `wait`, one leg at a time, each as a background job it waits on so the wall can reach it.
The dispatch hint is one sort in the legs-parse python, keyed on ledger seconds or 0 (`:2005`).

**Why the marker is written by the worker.** The tail exists only while the pool still runs, and the
reader may not reach a deferred leg until the floor leg ends. The worker knows at completion everything
the predicate reads, so it can leave the mark then; the reader's deferral and the marker apply one
predicate to one set of files, and an arm asserts they agree.

**Why at most one running.** The research's tail release used the same bound. A retry packed beside
several heavy legs recreates the contention that killed it, and under F1 (a) a non-passing tail
attempt costs a third run. One neighbour, typically the floor leg, is the cheapest contention that still
uses the idle slots.

**The priors, measured at writing time.** Over `tools/gate-legs.json` and `ceiling-evidence.txt` at
base 22efab65, every leg declares a `ceiling` and all but a handful carry an evidence row; the median
ceiling-to-evidence ratio was about 17. The research's `ceiling/3` would therefore rank a ceiling-only
leg several times too long against the evidenced ones, which is why S5 derives the divisor rather than
typing one. The ratio is PINNED to that base here; the python pass re-derives it on every bar.

**Byte stability.** Every line the bar prints keeps its position: deferrals in manifest order, retry
verdicts after the drain in `DEFERRED` order, then the `---- retry:` line. Only WHEN the retry ran
moves, plus the `GATE retry` wording if F2 picks (a).

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — the marker, the tail release, `run_leg_retry`, the sort key.
- `tools/run-gates/run-gates.test.sh` — the tail-release and fallback arms beside the retry arms.
- `tools/run-gates/run-gates.evidence.test.sh` — the record-row arms and the dispatch-order arms.
- `tools/run-gates/profile_bar.test.sh` — its `GATE retry` fixture lines, if F2 rewords.
- `tools/run-gates/README.md` — the retry section and the dispatch hint.
- `tools/run-gates/kit.toml` — the kit version, moved once for the build.

### Alternatives rejected

- **Retry concurrently after the drain at width 3** (the runner report's 4b). Cheaper code, but it still
  waits for the floor leg; the tail is where the idle slots are.
- **Kill on a hang instead of a deadline.** Larger, and it changes a verdict rule; it stays the
  report's lever 8.
- **`ceiling/3` as the ceiling-only prior.** The measured ratio says 3 is wrong for this tree by a
  factor of about five.
- **Release a retry the moment a slot frees.** It puts retries beside the heaviest legs, the setting
  that killed them.

## 5. Production-readiness checklist

- security: N/A — no new input, no new write path beyond a marker file in the run's own work dir.
- perf / scale: the research's estimate is about 3300 s from the tail and about 1900 s from the prior on the profiled bar, not additive with width.
- error / empty / loading states: an unreadable evidence file or ledger is a missing prior, never a failed run, as a corrupt ledger is today.
- observability: the retry row's start field shows the tail release; the header's `dispatch` key shows the order the priors produced.
- risks: a tail attempt's record is read by `derive-ceilings.py` and `profile_bar.py`, which glob every `.leg`; the set-aside suffix must stay a reading with its foreign count.
- testing: record-order arms with no clock bound, a byte-equality arm on the report, and order arms over fixture manifests.
- migration: none; a bar with a ledger orders exactly as today.
- user docs: `tools/run-gates/README.md` (S6).

## 6. Acceptance criteria

- **AC1** — When a fixture bar at `GATE_JOBS=2` runs a leg that outlives its ceiling once and passes on
  its next attempt beside a long sleeper leg, the retry's `.leg` row start field is earlier than the
  sleeper's end field, and a `.defer` marker named the leg. Red when: the retry starts after the drain.
- **AC2** — When that bar ends, its `GATE` and `----` lines for the leg are the deferral line, then
  `GATE ok    <leg>  (retried after timeout)`, then `---- retry: green  (1 retried, 0 failed)`, in the
  same positions a serial-retry bar prints them. Red when: the tail pass is reported elsewhere or twice.
- **AC3** — When the fixture's whole-run wall (`GATE_WALL`) fires while a tail retry runs, the breach
  names that leg and no retry line claims a verdict for it. Red when: the tail job outlives the wall.
- **AC4** — When a leg times out on its tail attempt and again on its serial retry, its `GATE FAIL`
  tail carries today's `again on its serial retry` wording and a HOST note from the serial attempt.
  Red when: a non-passing tail attempt issues the verdict, or the HOST note reads the tail attempt.
- **AC5** — When a fixture bar runs with no ledger and a kit-dir `ceiling-evidence.txt` naming three
  legs at different maxima, the header's `dispatch` key lists them largest first. Red when: the order is
  the manifest's.
- **AC6** — When a ledger row exists for one leg and evidence rows for all three, the ledger's seconds
  place that leg; a leg with neither is placed by its scaled `ceiling`. Red when: the evidence outranks
  the ledger, or a ceiling-only leg sorts as zero.
  cost: each arm drives the real runner over a fixture with sleeps of a few seconds; the tail arms need
  a second leg that outlasts a ceiling and a retry.

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
`spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 AC4 · a release after `wait`, a tail pass printed twice, a tail job with no pid file, and a tail timeout issuing FAIL · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC5 AC6 · the sort key reading only the ledger, then the evidence ahead of the ledger · its `FLOOR_ASSERTIONS` rises by the assertions added

## 8. Open questions

- **F1 — What does a tail retry that does not pass decide?**
  - (a) Nothing. Its files are set aside and the leg takes today's serial retry, alone, after the drain;
    only a pass is final from the tail. Every verdict rule is untouched, and a genuinely red leg runs
    three times.
  - (b) Everything. The tail attempt is the one retry; a timeout there reads FAIL with
    `not alone, HOST not measured` when it had a neighbour. Fewer runs, but a contended second timeout
    becomes a FAIL that today's alone retry would have passed.
  - Recommendation: (a).
- **F2 — Does the `GATE retry` line keep its bytes?** Its tail says `one serial retry after the pool
  drains`, which a tail release makes inexact.
  - (a) Reword it to name both, moving the README line, the canary's AC1 pattern and the
    `profile_bar.test.sh` fixture lines in the same commit.
  - (b) Keep the bytes; no reader moves, and the line stays true only of the fallback.
  - Recommendation: (a); every reader is in this kit and the split is on the head and the leg name.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "retry a timed-out leg after the pool drains"` ranked the
`run-gates` affordance seam and `run_leg_at` / `run_leg_reap` among name-token neighbours; the seams this
unit extends are the runner's own `check_ceiling_fired` (one predicate, now read at completion too),
`runleg` with its `.retry` suffix, and the legs-parse sort, plus `ceiling-evidence.txt`, which
`derive-ceilings.py` already generates and tracks.

Recall terms used: serial retry deferred ceiling fired HOST spawn floor drain dispatch order ledger longest-first

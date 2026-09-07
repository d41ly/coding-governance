# TOOL-aPooledSweep-1 — the sweep runs its suites in a bounded outer pool

**Status:** OPEN · rev-1 · 2026-09-07 · node a · Tier-2 · base 05fb897c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aPooledSweep-1-why-the-port-could-not-finish.md](../build/2026-09-07-build-TOOL-aPooledSweep-1-why-the-port-could-not-finish.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/run-selftests.sh` runs its declared population one suite at a time, so its wall
clock is the SUM of 59 suites. Run them through a bounded outer pool instead, so the wall clock
falls toward the longest suite, over the whole population and with no suite rewritten.

## 2. Scope (IN)

- **S1** — a `--sweep` mode that executes the resolved population through a bounded pool of
  concurrent suite processes, reporting one verdict line per suite. Observed by AC1.
- **S2** — REPORTING IS DECLARATION-ORDERED whatever the width and whatever order the pool frees a
  slot in, so the output is byte-stable against the serial mode's ordering. Observed by AC2.
- **S3** — THE COMPOSITE WIDTH INVARIANT IS PRESERVED: outer x inner never exceeds the profile row's
  declared width. `--sweep` re-divides it as `run-selftests.sh`'s own `OUTER=1` comment instructs,
  and prints the pair it chose before the first verdict. Observed by AC3.
- **S4** — the run's exit status is the SWEEP verdict alone: non-zero when any suite failed, zero
  when none did. Observed by AC1 and AC4.
- **S5** — the existing liveness refusal survives the new mode: a `--sweep` that resolved no suite
  REFUSES rather than printing a green line. Observed by AC4.
- **S6** — the default (no-flag) mode is UNCHANGED, byte-for-byte in its output shape, because it is
  what `run-unattended-gates.sh` and every Definition of Done already invoke. Observed by AC5.

## 3. Non-goals (OUT)

- Not porting, rewriting or touching any suite. The parent build's arm-inventory diff exists because
  a port can silently drop an arm; touching no suite makes that risk zero.
- Not making concurrency the default. The default mode grades budgets and must keep doing so.
- Not sharding a suite to shrink the pool's floor. `check-unattended.test.sh` already carries a
  `--shard` contract and dispatching its halves as independent pool members would lower the floor
  further; it is a follow-up, and it needs the shard-vs-whole-suite claim distinction that
  `run-unattended-gates.sh` records.
- Not deciding what a contended reading means. That is `TOOL-aPooledSweep-2`.
- Not proving the suites are safe to run together. That is `TOOL-aPooledSweep-3`.

### Edges

- **hands-off** `TOOL-aPooledSweep-2` — this unit produces the readings; that unit decides that a
  pooled one grades no budget. Without it this mode would issue cost verdicts from contended clocks.
- **hands-off** `TOOL-aPooledSweep-3` — this unit runs suites together; that unit observes whether
  doing so dirtied anything outside their own scratch.
- **consumes-from** external — `run-gates.sh --print-profile`, which already resolves the declared
  width and is the runner's existing width source.

## 4. Design

### The mode

A fourth `MODE` value beside `run`, `check`, `list` and `rank`. It resolves the population exactly as
`run` does — same `read_population`, same state handling, same `--kit` filter and same refusals — and
differs only in HOW the resolved rows are executed and WHAT is reported per row.

Sharing the resolution is the point: a second population reader would be a second answer to the
question `--check` asserts in both directions, which is the `two-answers-to-one-question` class the
bug-class checklist selects for these paths.

### The pool

The same shape `lib-selftest.sh` already runs its arms with, for the same reason and with the same
recorded trap: `wait -n` returns the exit STATUS of the job that finished, so `wait -n || wait` reads
a red suite as "this shell has no `wait -n`" and degenerates to a barrier per suite. The capability
is PROBED ONCE, outside the loop, exactly as the harness probes it.

Each suite runs as its own background process writing a verdict FILE, because a parent cannot read a
variable a background job set. The verdict file holds the suite's exit status and its elapsed
seconds; the rendering loop reads them by builtin in declaration order after the pool drains.

### The width

`OUTER` stops being the constant `1` and becomes the resolved width in `--sweep`, with
`SELFTEST_INNER_WIDTH` re-divided to `W / OUTER` by the arithmetic already in the file. At the
declared width that is outer `W`, inner 1: the population is 59 suites and one ported suite, so
outer parallelism is where the width buys anything. The product is what the invariant names, and it
is unchanged.

The runner PRINTS the pair it chose before the first verdict, as the serial mode already prints its
own. A width figure that is not printed is a width nobody can check against the invariant.

### Inventory

- `--sweep` — the flag. Named against the lexicon before it is written.
- `SWEEP_OUTER`, `SWEEP_ROOT`, `_rs_waitn` — the mode's locals. `_rs_` prefixed to match the file's
  existing private-name habit and to keep them out of the exported surface.
- No new file. The mode is ~50 lines inside the runner that already owns the population.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` · one build record.

### Alternatives rejected

**Porting more suites onto `lib-selftest.sh`**, which is what the parent build attempted. Rejected on
its own measurement: 12 of the 12 costliest surveyed are unportable under the harness's assertion
contract, and the two costliest — 32.2% of the population — were never surveyed at all because the
ranking that would have selected them was produced by the same act as the survey. The research record
beside this spec is the derivation.

**A `GATE_JOBS`-shaped environment knob instead of a flag.** Rejected: the mode changes what the run
MEANS, not merely how fast it goes, and an environment variable that silently withholds every cost
verdict is exactly the invisible-mode-switch this repo gates against elsewhere.

## 5. Production-readiness checklist

- security — N/A: no new execution path, no new input. The mode runs the same argv the serial mode
  runs, resolved by the same reader.
- perf / scale — the unit's whole subject, and it is bounded above by the longest suite rather than
  by the pool width.
- error / empty / loading states — a suite whose row could not be resolved keeps the serial mode's
  `FAIL` line and its state token. An empty population REFUSES (S5).
- observability — one verdict line per suite plus the chosen width pair, both on stdout.
- risks — the recorded one is the `wait -n` collapse, which turns the pool serial while still
  printing a width; AC3 observes the width and the elapsed sum makes the collapse visible. The second
  is cross-suite interference, which is `TOOL-aPooledSweep-3` and is why that unit exists.
- testing — `tools/run-gates/run-selftests.test.sh` gains arms for the new mode, including its
  failing case.
- migration — additive: a new flag, no change to any existing mode. Reverts by deleting the branch.
- user docs — none owed. The runner's `print_usage` is the surface and it gains a line.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh --sweep` runs over a fixture population whose
  suites include one that exits non-zero, it prints a verdict line for every suite and exits
  non-zero. Red when: a failing suite is reported `ok`, or the run exits 0 with a `FAIL` line
  printed.
- **AC2** — When the same fixture population is swept twice at two different widths, by running
  `bash tools/run-gates/run-selftests.sh --sweep` under two values of `GATE_JOBS`, the two stdouts
  are byte-identical apart from the width pair and the elapsed figures. Red when: the verdict lines
  reorder with the width.
  figure: DERIVED — the comparison runs the two widths at observation time.
- **AC3** — When `--sweep` starts, it prints the outer and inner widths it chose, and their product
  is at most the width `run-gates.sh --print-profile` reports. Red when: the product exceeds the
  declared width, or no pair is printed.
- **AC4** — When `--sweep` is given a `--kit` filter matching nothing, it REFUSES with the existing
  liveness message and exits non-zero, printing no green line. Red when: an empty sweep exits 0.
- **AC5** — When `bash tools/run-gates/run-selftests.sh --list` and the no-flag mode run before and
  after this change, their stdout shapes are unchanged. Red when: the default mode's output moves.
  figure: DERIVED — compared against the pre-change binary at the pinned base.

## 7. Gates

`run-selftests self-test` · `lexicon naming predicates` · `memory hygiene` · `testsuite counts (every bar self-test prints one)`

New arm: `tools/run-gates/run-selftests.test.sh` · a fixture population holding one suite that exits
non-zero and one that exits zero, swept · the suite's assertion floor moves by the number of arms
added.

## 8. Open questions

- **F1 — does `--sweep` re-divide to outer `W` / inner 1, or split the width between the two?**
  RESOLVED (agent, 2026-09-07, delegated): outer `W`, inner 1. The population is 59 suites and
  exactly one of them is on the inner harness, so inner width buys parallelism for 1/59th of the
  work while outer width buys it for all of it. The invariant is the product and it is satisfied
  either way; this split is the one that spends the width where the suites are.

## 9. Revision log

- rev-1 · 2026-09-07 · initial draft.

## 10. Reuse audit

The seam this unit extends is `tools/run-gates/run-selftests.sh` itself, which already resolves the
population, the `--kit` filter, the width and every refusal — this adds an execution mode to it and
reads nothing a second time. The pool shape is REUSED from `tools/lib/lib-selftest.sh`, whose
`run_arms` carries the probed `wait -n` capability, the verdict-file protocol and the
declaration-ordered rendering, all three of which this mode needs for the same reasons; the
`reuse_lookup.py` probe for "run a shell self-test suite's arms in parallel with isolated scratch
copies" returned `boundedParallel` and a `run` name-stem seam and named neither of these files, so
the seam was verified against source rather than taken from the probe.

Recall terms used: `python tools/memory-recall/query.py "why could the costly self-test suites not be
ported onto the parallel harness, and what would make them portable" --terms "selftest harness port
arm inventory extract negative assertion substring snapshot shard parallel budget majority share
spawn"`.

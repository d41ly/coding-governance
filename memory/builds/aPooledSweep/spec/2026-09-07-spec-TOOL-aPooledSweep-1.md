# TOOL-aPooledSweep-1 — the sweep runs its suites in a bounded outer pool

**Status:** CLOSED · rev-3 · 2026-09-07 · node a · Tier-2 · base 05fb897c · streams tooling · order 1 · ratified 2026-09-07

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md](../build/2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md) | journal | TOOL-aPooledSweep-2 TOOL-aPooledSweep-3 |
| [2026-09-07-build-TOOL-aPooledSweep-1-why-the-port-could-not-finish.md](../build/2026-09-07-build-TOOL-aPooledSweep-1-why-the-port-could-not-finish.md) | research | — |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPooledSweep-2 TOOL-aPooledSweep-3 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-aPooledSweep-2 TOOL-aPooledSweep-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/run-selftests.sh` runs its declared population one suite at a time, so its wall
clock is the SUM of 59 suites. Run them through a bounded outer pool instead, so the wall clock
falls toward the longest suite, over the whole population and with no suite rewritten.

## 2. Scope (IN)

- **S1** — a `--sweep` mode that executes the resolved population through a bounded pool of
  concurrent suite processes, reporting one verdict line per suite. Observed by AC1 and AC6.
- **S2** — REPORTING IS DECLARATION-ORDERED whatever the width and whatever order the pool frees a
  slot in, so the output is byte-stable against the serial mode's ordering. Observed by AC2.
- **S3** — THE COMPOSITE WIDTH INVARIANT IS PRESERVED: outer x inner never exceeds the profile row's
  declared width. `--sweep` re-divides it as `run-selftests.sh`'s own `OUTER=1` comment instructs,
  prints the pair it chose before the first verdict, and takes an explicit override from
  `SELFTEST_OUTER_WIDTH`, CLAMPED to the resolved width so the override cannot break the invariant.
  Observed by AC3 and AC10.
- **S4** — the run's exit status is the SWEEP verdict alone. Non-zero when any suite failed,
  observed by AC1; zero when none did, observed by AC7.
- **S5** — the existing liveness refusal survives the new mode: a `--sweep` that resolved no suite
  REFUSES rather than printing a green line. Observed by AC4.
- **S6** — the default (no-flag) mode is UNCHANGED, byte-for-byte in its output shape, because it is
  what `run-unattended-gates.sh` and every Definition of Done already invoke. Observed by AC5.
- **S7** — EVERY POOLED SUITE IS BOUNDED, and the whole run is too. A suite that overruns its bound
  is KILLED and rendered as a state distinguishable from both `ok` and `FAIL`; a run that overruns
  the wall kills what is outstanding and REDS naming those suites. Observed by AC8 and AC9.
- **S8** — THE BOUND CANNOT BE SILENTLY INERT. `timeout` is a probed capability, not an assumption,
  and a sweep that cannot resolve it REFUSES rather than running fifty-nine unbounded suites while
  S7 claims otherwise. Observed by AC11.
- **S9** — a pooled `FAIL` carries EVIDENCE, not just an exit code: the verdict file holds the
  suite's captured output and the renderer prints the same excerpt the serial mode does. Observed by
  AC1.

## 3. Non-goals (OUT)

- Not porting, rewriting or touching any suite. The parent build's arm-inventory diff exists because
  a port can silently drop an arm; touching no suite makes that risk zero.
- Not making concurrency the default. The default mode grades budgets and must keep doing so.
- Not sharding a suite to shrink the pool's floor. `check-unattended.test.sh` already carries a
  `--shard` contract and dispatching its halves as independent pool members would lower the floor
  further; it is a follow-up, and it needs the shard-vs-whole-suite claim distinction that
  `run-unattended-gates.sh` records.
- Not streaming verdicts as suites finish. S2's declaration-ordered rendering and a live stream are
  incompatible, and S7's bounds are what stop a hang from suppressing the report — a completion-order
  stream would trade a byte-stable output for partial progress the bounds already guarantee arrives.
- Not fixing `TOOL-aBoundedVerdict-10`. Its per-leg deadline half stays open and belongs to
  `run-gates.sh`; S7 bounds this mode's own exposure to it and does not close the row.
- Not deciding what a contended reading means. That is `TOOL-aPooledSweep-2`.
- Not proving the suites are safe to run together. That is `TOOL-aPooledSweep-3`.

### Edges

- **hands-off** `TOOL-aPooledSweep-2` — this unit produces the readings; that unit decides that a
  pooled one grades no budget. Without it this mode would issue cost verdicts from contended clocks.
- **hands-off** `TOOL-aPooledSweep-3` — this unit runs suites together; that unit observes whether
  doing so dirtied anything outside their own scratch.
- **consumes-from** external — `run-gates.sh --print-profile`, which already resolves the declared
  width AND the whole-run `wall`, and is the runner's existing width source.

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
variable a background job set. The verdict file holds the suite's exit status, its start stamp, its
end stamp AND its captured output; the rendering loop reads them by builtin in declaration order
after the pool drains. The output is there because the serial loop prints four grepped lines of it
on a failure, and a pooled `FAIL` that printed only an exit code would be a mode you cannot debug
without re-running the suite serially — which is the thing the mode exists to avoid.

**The start and end stamps are not decoration — they are the only evidence the pool ran as one.**
AC6 reads them, and without them the collapse this section describes is invisible from the output.

### The hang bound, and why BOTH halves are derived from this population

Backgrounding 59 suites with no bound is strictly worse than the serial loop it replaces: the
rendering is declaration-ordered and happens after the pool drains, so one non-returning suite
suppresses every verdict line rather than one. `TOOL-aBoundedVerdict-10` is OPEN and records
`unattended driver selftest` — a row in this population — hanging inside its first `--preflight`
with zero output at 240 s. The bound is therefore a requirement of this mode, not a refinement of it.

- **Per suite** — the row's declared budget multiplied by `sweep-ceiling-factor`, declared once in
  `tools/run-gates/selftest-budgets.txt`'s header with its reading. `timeout -k` enforces it, the
  same enforcement `lib-selftest.sh` uses per arm and for the same recorded reason: a captured pipe
  read to EOF applies the bound to the verdict rather than to the clock.
- **Per run** — the LARGEST per-suite bound in the resolved population, plus nothing. A pool cannot
  finish before its longest member's own bound expires, so any smaller wall kills the run for
  arriving on time. `SELFTEST_WALL` overrides it and is REFUSED below the largest per-suite bound,
  which is a refusal that can fire rather than a number that cannot be wrong.

**Rev-2 borrowed the run wall from `run-gates.sh --print-profile` and that was wrong twice over.**
The `capable` profile row declares `wall 10800`, while `selftest-budgets.txt` declares 13600 for
`unattended gate selftest` alone — so the borrowed wall sat BELOW this population's largest
per-suite bound, and the run would have been killed mid-sweep every single time, making AC9's staged
failing case the ordinary case. It also sat 19% above that suite's own 9067 s reading, which is not
headroom for a suite whose readings vary with load. And the probe it rides is the same
`--print-profile` call §4 concedes fails inside the test fixture, so the wall would have had no
value there at all. Deriving both halves from the budgets file removes the borrow, the fixture hole
and the arithmetic error together.

**This does not contradict the budgets header, and the distinction is worth stating because the
header states the opposite in capitals.** That header says a budget is a cost verdict and the hang
bound is the `ceiling` in `tools/gate-legs.json`. It is right, and this mode does not treat the
budget AS a hang bound — it DERIVES one from it by a declared factor, exactly as those manifest
ceilings are themselves derived at roughly 10x their recorded seconds. Reading the manifest ceilings
directly was rejected below.

### The bound that is not there

`timeout` is a probed capability. `tools/lib/lib-selftest.sh` probes for it with `command -v` and,
finding nothing, runs its arms UNBOUNDED — a reasonable default for a harness whose arms are
seconds long, and an unacceptable one for a mode whose entire S7 claim is that a hang cannot
suppress the report. So `--sweep` REFUSES when it cannot resolve `timeout`, and says which
capability is missing. `run-gates.sh` already announces its own ceilings as live or off on the
`--print-profile` line; this is the same announcement with a refusal behind it, because here the
missing capability removes the property the mode was built to add.

### The width

`OUTER` stops being the constant `1` and becomes the resolved width in `--sweep`, with
`SELFTEST_INNER_WIDTH` re-divided to `W / OUTER` by the arithmetic already in the file. At the
declared width that is outer `W`, inner 1. The product is what the invariant names, and it is
unchanged.

`SELFTEST_OUTER_WIDTH` overrides the outer half directly when set to a positive integer, CLAMPED to
the resolved width: the invariant is the product, and an override that could exceed it would be a
knob for breaking the rule this section exists to keep. It exists
because the width otherwise arrives through `run-gates.sh --print-profile`, and
`run-selftests.test.sh`'s `build_repo` copies exactly one file into its scratch repo — the runner —
so that probe fails there, its stderr is swallowed, and `W` falls back to the hard-coded 2 for every
arm. Without an override the fixture has ONE width and every width-varying criterion is constant.
The alternative — staging `run-gates.sh` and `gate-profiles.txt` into the fixture — was rejected
below.

The runner PRINTS the pair it chose before the first verdict, as the serial mode already prints its
own. A width figure that is not printed is a width nobody can check against the invariant.

### Inventory

- `--sweep` — the flag. Named against the lexicon before it is written.
- `SELFTEST_OUTER_WIDTH` — the outer-width override, named to match the existing
  `SELFTEST_INNER_WIDTH` export it composes with.
- `sweep-ceiling-factor` — the declared per-suite bound multiplier, a header key in
  `tools/run-gates/selftest-budgets.txt` beside `port-majority-share` and `port-minimum-factor`.
- `SELFTEST_WALL` — the whole-run bound override, refused below the largest per-suite bound.
- `TIMEOUT` — the verdict state for a killed suite, distinct from `ok` and `FAIL`.
- `SWEEP_ROOT`, `_rs_waitn` — the mode's locals. `_rs_` prefixed to match the file's existing
  private-name habit and to keep them out of the exported surface.
- No new file. The mode is inside the runner that already owns the population.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/run-gates/selftest-budgets.txt` (header key only) · one build record.

### Alternatives rejected

**Porting more suites onto `lib-selftest.sh`**, which is what the parent build attempted. Rejected on
its own measurement: 12 of the 12 costliest surveyed are unportable under the harness's assertion
contract, and the two costliest — 32.2% of the population — were never surveyed at all because the
ranking that would have selected them was produced by the same act as the survey. The research record
beside this spec is the derivation.

**A `GATE_JOBS`-shaped environment knob instead of a flag,** for the MODE. Rejected: the mode changes
what the run MEANS, not merely how fast it goes, and an environment variable that silently withholds
every cost verdict is exactly the invisible-mode-switch this repo gates against elsewhere. The
argument is about the mode and does not reach the WIDTH, which is why `SELFTEST_OUTER_WIDTH` is a
variable and `--sweep` is a flag.

**Reading each row's hang bound from `tools/gate-legs.json`'s `ceiling`.** Rejected on two counts. It
resolves for held legs and not for the six rows that are in no manifest — the `run-unattended-gates.sh`
suites the 2026-08-23 ruling removed from both — so those six would still run unbounded, which is the
half of the population containing the suite `TOOL-aBoundedVerdict-10` names. And a manifest ceiling
is sized against the BAR's contended conditions while this runner's budget is sized against its own,
so consuming both would give one suite two bounds from two conditions.

**Staging `run-gates.sh` and `gate-profiles.txt` into the test fixture** to make the real resolver
answer there. Rejected: it makes every width-varying arm depend on the host's detected cores and RAM,
so the arm's width is whatever the machine says, and a criterion whose expected value is
machine-dependent cannot be pinned.

## 5. Production-readiness checklist

- security — N/A: no new execution path, no new input. The mode runs the same argv the serial mode
  runs, resolved by the same reader.
- perf / scale — the unit's whole subject. Bounded above by the longest suite's own bound, which is
  what S7 makes true rather than assumed, and the run wall is that same figure rather than a
  borrowed one.
- error / empty / loading states — a suite whose row could not be resolved keeps the serial mode's
  `FAIL` line and its state token. A killed suite renders `TIMEOUT`. An empty population REFUSES,
  and so does a host with no `timeout` binary.
- observability — one verdict line per suite, the chosen width pair, the start and end stamps AC6
  and AC10 read, and a failing suite's captured excerpt, all on stdout.
- risks — the recorded one is the `wait -n` collapse, which turns the pool serial while still
  printing a width. AC6 is what observes it, and AC6 exists because rev-1's criteria did not: every
  one of them passed against a serial impostor, so the deliverable was commissioned and observed by
  nothing. The second risk is cross-suite interference, which is `TOOL-aPooledSweep-3`.
- testing — `tools/run-gates/run-selftests.test.sh` gains arms for the new mode, including its
  failing cases.
- migration — additive: a new flag, a new header key, no change to any existing mode.
- user docs — none owed. The runner's `print_usage` is the surface and it gains a line.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh --sweep` runs over a fixture population whose
  suites include one that exits non-zero, it prints a verdict line for every suite, prints an
  excerpt of the failing suite's own output beneath its row, and exits non-zero. Red when: a failing
  suite is reported `ok`; the run exits 0 with a `FAIL` line printed; or the `FAIL` row carries an
  exit code and no excerpt.
- **AC2** — When the same fixture population is swept twice under two values of
  `SELFTEST_OUTER_WIDTH`, the two stdouts carry their verdict lines in the same order with the same
  labels. Red when: the verdict lines reorder with the width.
  figure: DERIVED — the comparison runs the two widths at observation time.
- **AC3** — When `--sweep` starts, it prints the outer and inner widths it chose and their product
  is at most the resolved width; an in-range `SELFTEST_OUTER_WIDTH` is what the outer half reports,
  and one ABOVE the resolved width is clamped to it. Red when: the product exceeds the resolved
  width, no pair is printed, an in-range override is ignored, or an out-of-range one is honoured.
- **AC4** — When `--sweep` is given a `--kit` filter matching nothing, it REFUSES with the existing
  liveness message and exits non-zero, printing no green line. Red when: an empty sweep exits 0.
- **AC5** — When `bash tools/run-gates/run-selftests.sh --list` and the no-flag mode run before and
  after this change, their stdout shapes are unchanged. Red when: the default mode's output moves.
  figure: DERIVED — compared against the pre-change script at the pinned base.
- **AC6** — When a fixture population of suites that each sleep a known interval is swept at
  `SELFTEST_OUTER_WIDTH` above 1, the verdict files' start and end stamps show at least two suites
  whose intervals OVERLAP. Red when: no two intervals overlap, which is what the `wait -n` collapse
  in §4 produces while still printing a width pair.
  figure: DERIVED — the stamps are read from the run under observation, never pinned.
- **AC7** — When `--sweep` runs over a fixture population where every suite exits zero, it prints no
  `FAIL` line and exits 0. Red when: an all-green sweep exits non-zero.
- **AC8** — When a fixture suite runs longer than its derived per-suite bound, `--sweep` KILLS it and
  renders it `TIMEOUT`, distinguishable from both `ok` and `FAIL`, and the run exits non-zero. Red
  when: the suite runs to completion, or its row renders as an ordinary `FAIL`.
  fixture: a budgets row whose budget times `sweep-ceiling-factor` is below a deliberately slow
  fixture suite's runtime.
- **AC9** — When the whole-run wall is exceeded, `--sweep` kills what is outstanding and REDS NAMING
  those suites; and over the REAL population the derived wall is at least the largest derived
  per-suite bound. Red when: the run continues past the wall; it reds without naming what it killed;
  or the derived wall is below the largest per-suite bound, which is the arithmetic that made rev-2's
  borrowed 10800 s wall kill every sweep of a population declaring 13600 s.
  figure: DERIVED — both sides are computed from `tools/run-gates/selftest-budgets.txt` at
  observation time, never pinned here.
- **AC10** — When a sleeping fixture population is swept, the PEAK number of suites whose start-to-end
  intervals overlap at any instant, computed from the verdict files under `SWEEP_ROOT`, is at most
  the outer width `bash tools/run-gates/run-selftests.sh --sweep` printed. Red when: peak
  concurrency exceeds the printed outer width, which is the invariant being broken rather than
  merely mis-reported — AC3 reads the printed pair and this reads what the pool actually did.
  figure: DERIVED — computed from the verdict files of the run under observation.
- **AC11** — When `timeout` cannot be resolved, `--sweep` REFUSES before running any suite and names
  the missing capability. Red when: the sweep proceeds with the bound silently inert, which is the
  state `lib-selftest.sh`'s own probe falls back to and which S7 forbids here.
  fixture: the arm forces the failure through a `PATH` with no `timeout` on it.

## 7. Gates

`run-selftests self-test` · `lexicon naming predicates` · `memory hygiene` · `testsuite counts (every bar self-test prints one)`

New arm: `tools/run-gates/run-selftests.test.sh` · a sleeping fixture population swept at two outer
widths, staged red by forcing the no-`wait -n` path so the pool collapses · the suite's assertion
floor moves by the number of arms added.
New arm: `tools/run-gates/run-selftests.test.sh` · an all-passing fixture population swept, staged
red by forcing the exit expression to a constant · same floor move.
New arm: `tools/run-gates/run-selftests.test.sh` · a fixture suite slower than its derived bound, and
a population whose wall is exceeded · same floor move.
New arm: `tools/run-gates/run-selftests.test.sh` · a `PATH` carrying no `timeout`, and a population
whose declared wall is below its largest derived per-suite bound · same floor move.

## 8. Open questions

- **F1 — does `--sweep` re-divide to outer `W` / inner 1, or split the width between the two?**
  RESOLVED (agent, 2026-09-07, delegated): outer `W`, inner 1. THREE of the 59 suites source
  `tools/lib/lib-selftest.sh` at top level — `tools/check-line-length.test.sh`,
  `tools/lib/extract-arms.test.sh` and `tools/run-gates/run-selftests.test.sh`, derived over the
  tracked tree rather than counted from either figure rev-1 carried, both of which were wrong in
  opposite directions. So inner width buys parallelism for 3/59ths of the work and outer width for
  all of it. The invariant is the product and is satisfied either way; this split spends the width
  where the suites are, and the corrected figure does not change the answer.
- **F2 — where does a pooled suite's hang bound come from?** RESOLVED (agent, 2026-09-07,
  delegated): BOTH halves are derived from `tools/run-gates/selftest-budgets.txt` — per suite, the
  row's budget times the declared factor; per run, the largest of those. §4 states why the manifest
  `ceiling` was rejected and why rev-2's borrowed profile wall was arithmetically impossible against
  this population. The survivor is the only option that resolves for all 59 rows, works inside the
  test fixture, and cannot be smaller than the suite it has to outlive.
- **F3 — what happens on a host with no `timeout`?** RESOLVED (agent, 2026-09-07, delegated):
  REFUSE. `lib-selftest.sh` runs unbounded in that case and is right to, because its arms are
  seconds long; here the missing binary deletes S7 outright, and a mode whose stated property is
  silently absent is the class this repo gates against everywhere. The cost is that a host without
  coreutils cannot sweep, which is a refusal with a name rather than a green run with no bound.

## 9. Revision log

- rev-1 · 2026-09-07 · initial draft.
- rev-2 · 2026-09-07 · §2 S3, S4, S7 · §3 · §4 · §6 AC2, AC3, AC6, AC7, AC8, AC9 · §7 · §8 F1, F2 ·
  folded round-1 spec audit B1, B2, H1, H6, H7. B1: every rev-1 criterion passed against a serial
  `--sweep`, so AC6 now observes overlap directly. B2: no hang bound at all over a population holding
  an OPEN hang row, so S7 adds both bounds. H1: the fixture has no width resolver and the runner
  never read `GATE_JOBS`, so AC2 and AC3 were constant. H6: no criterion ran an all-green sweep.
  H7: the inner-harness suite count was wrong in both sub-specs.
- rev-3 · 2026-09-07 · §2 S3, S7, S8, S9 · §4 · §5 · §6 AC1, AC3, AC9, AC10, AC11 · §7 · §8 F2, F3 ·
  folded round-2 spec audit B2, H1, H3, H4, M1, M2. The loop exited NON-CONVERGENT at round 2 — 14
  defects against round 1's 9 — so every finding was disposed by FOLD rather than re-reviewed. B2:
  the borrowed profile wall of 10800 s sits below this population's largest per-suite bound of
  13600 s, so both halves are now derived from the budgets file. H1: that wall rode the
  `--print-profile` probe which fails inside the fixture. H3: `timeout` is probed and its absence
  ran the arms unbounded, so S8 refuses. H4: the width invariant was observed only on the PRINTED
  pair, so AC10 reads peak concurrency from the verdict files. M1: the verdict file carried no
  output, so a pooled FAIL had no evidence. M2: an override above the resolved width could not
  satisfy both clauses of AC3, so it is clamped.

## 10. Reuse audit

The seam this unit extends is `tools/run-gates/run-selftests.sh` itself, which already resolves the
population, the `--kit` filter, the width and every refusal — this adds an execution mode to it and
reads nothing a second time. The pool shape is REUSED from `tools/lib/lib-selftest.sh`, whose
`run_arms` carries the probed `wait -n` capability, the verdict-file protocol, the `timeout -k`
bound and the declaration-ordered rendering, all four of which this mode needs for the same reasons;
the `reuse_lookup.py` probe for "run a shell self-test suite's arms in parallel with isolated scratch
copies" returned `boundedParallel` and a `run` name-stem seam and named neither of these files, so
the seam was verified against source rather than taken from the probe.

Recall terms used: `python tools/memory-recall/query.py "why could the costly self-test suites not be
ported onto the parallel harness, and what would make them portable" --terms "selftest harness port
arm inventory extract negative assertion substring snapshot shard parallel budget majority share
spawn"`.

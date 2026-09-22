# TOOL-aTimedTurnstile-5 — run the merge bar's legs concurrently

**Status:** CLOSED · rev-4 · 2026-08-20 · node a · Tier-2 · base af6de231 · streams tooling · review aTimedTurnstile-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-11-review-TOOL-aTimedTurnstile-5-1.md](../reviews/2026-08-11-review-TOOL-aTimedTurnstile-5-1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates.sh` runs all 47 legs serially, so the bar's wall clock is the sum of its legs:
382.1s warm, 607.3s cold, 335.2s for the real runner with one guard-skip. Run the legs through a
bounded worker pool instead, which a measured prototype completes in 79.9s with every leg still
green. The template this repo ships already requires this of an adopter's gate runner.

## 2. Scope (IN)

- **S1** — replace the serial `while read … leg` loop in `tools/run-gates.sh` with a bounded worker
  pool. Each leg runs in its own subprocess exactly as today, with stdin denied and its combined
  output captured.
- **S2** — resolve the pool width from `GATE_JOBS`, defaulting to `min(8, nproc)`. A width of 1 is
  the same code path with one worker, not a separate serial branch.
- **S3** — dispatch longest-leg-first using per-leg durations cached at `<git-dir>/gate-timings.tsv`,
  written by every run. The cache is advisory: absent, stale or corrupt, dispatch falls back to
  manifest order and only the wall clock changes.
- **S4** — print results in MANIFEST order regardless of completion order, streaming each leg's line
  as soon as every leg before it has reported. The `GATE ok`, `GATE FAIL` and `GATE skip` lines,
  the indented failure output, the `----` rule and the verdict line keep their current text.
- **S5** — evaluate the `guard` diff-scoping decision for every leg up front, serially, before any
  dispatch. Skip accounting is unchanged.
- **S6** — extend `tools/run-gates.test.sh` with arms for the new behaviour, driven by a scratch
  repo carrying its own minimal manifest, never by the real 47-leg bar.

## 3. Non-goals (OUT)

- Widening `guard` coverage to the 29 self-test legs. That is `TOOL-aTimedTurnstile-2` and it needs
  an owner decision first, because guards honoured at the push boundary make the authoritative run
  diff-scoped while `AGENTS.md` calls that run the full bar.
- Making any individual leg faster. That is `TOOL-aTimedTurnstile-3`, and after this unit it is the
  only remaining lever, because the floor becomes the longest leg under load.
- Adding a new gate leg. S6 extends the existing sibling self-test instead, which keeps the leg
  count at 47 and avoids the four-gate cascade a new leg triggers.
- Any change to which legs exist, what they assert, or their exit-code contract.

## 4. Design

The runner keeps its shape: parse `tools/gate-legs.json`, decide run-or-skip per leg, execute, report
per leg, tally, exit. Only execution changes from a serial loop to a bounded pool, and only reporting
gains a reorder buffer.

### Data model

Per-leg state lives in one scratch directory created with `mktemp -d` and removed on `EXIT`. For leg
index `i` the worker writes `i.out` (combined output), then `i.sec` (wall seconds), then atomically
renames a temporary into `i.rc` (exit status). `i.rc` appearing LAST is the completion signal, so the
reader never observes a half-written result. A skipped leg gets its `i.rc` written as the literal
`skip` at decision time, before any dispatch.

The timing cache is a two-column file of leg name and wall seconds, rewritten whole at the end of
every run. It is keyed by leg NAME, so a renamed or new leg simply misses and sorts last.

Dispatch and reporting share ONE shell, so that shell owns every worker and can block on `wait -n`.
The first build separated them, with a dispatcher subshell and a reader that polled for result files
every 50ms. That is wrong on this platform for a measurable reason: `sleep` is a process, measured at
75ms for a 50ms sleep, so the poll tick cost more than the sleep it bought and spent roughly 317s of
a 617s serial run doing nothing else. Blocking on `wait -n` removes the tick entirely rather than
tuning it.

The width knob is bounded by LENGTH before any numeric test reads it, because `test -lt` and `$(( ))`
both ERROR on an int64 overflow rather than comparing. Independently, the outer loop force-dispatches
one leg whenever a pass started nothing and nothing is running, so forward progress does not depend on
the width being sane at all. The two are deliberate defence in depth: with either one present a
20-digit width still terminates green, and only removing BOTH reproduces the hang. That is why the arm
asserts the observable outcome — terminates, and reports every leg — rather than either mechanism.

Reporting a leg as `(no result)` is guarded by TWO further conditions, not just an empty job table:
dispatch must be exhausted, and a full `wait` must have reaped every worker, after which the result
file is checked once more. `jobs -rp` counts only RUNNING jobs, so a worker forked microseconds ago
is invisible, and the unguarded reading declared healthy legs dead. Measured against the unguarded
reader: 30 instant legs at width 1 reproduces it in 6 runs out of 8, while widths 2, 4 and 8
reproduce it in 0 out of 8.

### Inventory

| Concern | Today | After |
|---|---|---|
| execution | one leg at a time, in manifest order | up to `GATE_JOBS` legs at once |
| dispatch order | manifest | longest-first when the cache has entries |
| report order | manifest | manifest, unchanged |
| `GATE_JOBS` unset | n/a | `min(8, nproc)`, falling back to 4 when `nproc` is absent |
| failure summary | appended inside `leg()` | appended by the reader, in manifest order |

Width defaults to 8 rather than the core count because it was measured: 16 workers returned 80.5s
against 8 workers at 82.9s, while each leg dilates 1.66x under load. Wall clock is the longest leg
under load, so buying more workers past 8 only lengthens that leg.

### Rollout

One commit. `GATE_JOBS=1` reproduces the current wall clock and the current output exactly, which is
the rollback: no revert is needed to diagnose a suspected concurrency problem.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/run-gates.sh` | the pool, the reorder buffer, the width resolver, the timing cache |
| `tools/run-gates.test.sh` | S6 arms, and a widened header comment |
| `AGENTS.md` | the gate-suite paragraph names the runner's concurrency and the `GATE_JOBS` knob |

### Alternatives rejected

- **A separate serial code path for `GATE_JOBS=1`.** Two paths diverge, and the equivalence arm would
  then test the path nobody runs. One pool of width 1 keeps the arm honest.
- **A static `weight` field per leg in the manifest.** It goes stale silently and adds a maintenance
  burden to every leg edit. A cache the runner writes itself cannot drift from what the legs cost.
- **`xargs -P`.** It cannot express per-leg result files and manifest-ordered reporting without a
  helper script, and the repo has no seam for one.
- **Printing every line only after all legs finish.** Simpler, but it replaces a ticking bar with
  80 seconds of silence.
- **A dispatcher subshell with a polling reader.** Built first, then removed: it cannot block on
  `wait -n`, because the reader is not the workers' parent, so it must poll — and a poll tick is a
  process spawn here. It also made the reader's view of liveness indirect, which is what let it
  declare a pending leg dead.

## 5. Production-readiness checklist

- security — no new input is trusted. `GATE_JOBS` only sets a worker count and is clamped to at
  least 1; it cannot skip a leg or change a verdict.
- perf / scale — the point of the unit. Measured 335.2s to 79.9s on 47 legs at width 8.
- a11y — N/A, a shell gate runner has no user interface.
- i18n — N/A, the output is developer-facing English and already is.
- error / empty / loading states — an empty or unparseable manifest still exits 2 through the
  existing guard; a leg that writes no result file is reported rather than silently dropped.
- observability — per-leg wall seconds become available for the first time, in the timing cache.
- risks (concurrency, data-loss, rollback hazards) — the legs were audited for shared mutable state
  before this unit: every heavy self-test isolates itself with `mktemp -d` plus `git init`, no leg
  writes global git config, and no leg writes into the real tree. The prototype ran all 47 legs at
  widths 4, 8 and 16 with zero failures. Rollback is `GATE_JOBS=1`.
- testing + left-shift gates — S6, run from a scratch repo so the arms cost seconds.
- migration / rollback — none needed; the manifest format is unchanged.
- user docs — the `AGENTS.md` gate-suite paragraph.

## 6. Acceptance criteria

- **AC1** — When `tools/run-gates.sh` runs on this repo with the default width, every leg reports the
  same verdict it reports today and the runner exits 0.
- **AC2** — When the runner executes with `GATE_JOBS=1`, its stdout is byte-identical to the stdout of
  the pre-change runner on the same tree.
- **AC3** — When a leg fails, its `GATE FAIL` line and its indented output both appear, and the
  failing leg's name reaches `<git-dir>/gate-last-summary.txt`.
- **AC4** — When legs complete out of order, the printed lines are still in manifest order.
- **AC5** — When the timing cache is absent or corrupt, the run still completes green.
- **AC6** — When the bar runs at the default width on this repo, wall clock is under 150s, against a
  measured 335.2s serial baseline.
- **AC7** — When the runner is driven repeatedly at width 1 over a many-leg manifest, no healthy leg
  is ever reported `(no result)`, AND that manifest is asserted to have actually run. Asserted over
  repeated runs, because the failure is a race.
- **AC8** — When a leg carries a `guard` whose paths are unchanged, the run prints `GATE skip` at that
  leg's MANIFEST position and tallies it as skipped, at every width. When no base resolves, the same
  leg RUNS instead. Both directions, because only asserting the skip lets an always-skip regression
  pass.
- **AC9** — When a guard-skipped leg had a cached duration, that row survives the run's cache rewrite.
- **AC10** — When the width knob is given a negative, non-numeric, zero, or out-of-range value, the
  run TERMINATES under a timeout and still reports every leg.

## 7. Gates

`run-gates canary` is the leg this unit edits and must keep green. `memory hygiene (19 checks)`
covers this spec and the build record. `harness arms (fail branches armed or pinned)` and
`install-prefix (shipped surface)` both read `tools/run-gates.sh` and must stay green. The whole bar
runs at the DoD, since every leg's verdict is the thing being preserved.

## 8. Open questions

none — RESOLVED by observation at close (2026-08-20), which is the only way a question this old
should be answered. The fork was where the S6 arms live: extending the runner's sibling self-test,
or paying for a named leg. Both halves came true and neither cost what the question feared. The arms
live in the sibling self-test, which `TOOL-aPacedTurnstile-1` then moved into the kit as
`tools/run-gates/run-gates.test.sh`; and that file IS a named leg, `run-gates canary`, so the
visibility the owner might have preferred arrived without a separate row. The leg count did not stay
at 47 either — it is 86 — and the four gates the question priced now fire on every leg-adding commit
as ordinary cost rather than as a reason to avoid one.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft, written against measurements recorded in commit f638d8b.
- rev-3 · 2026-08-11 · folded Tier-2 review aTimedTurnstile-1 (16 raw, 11 confirmed, precision 0.69,
  verdict LAND IT, 0 blockers). All six confirmed defects fixed and armed. The highest, F1, was that
  the guard/skip path — the mechanism this unit restructured most — had ZERO arm coverage, so an
  always-skip regression stayed green by construction; AC8 now asserts both directions. F3 replaced
  an absolute 5000ms timing pin with a ratio, because this leg is graded against load it does not
  control. F2, F4, F5, F6 fixed per AC9/AC10. Fixing F2 initially REINTRODUCED the rev-2 race: the
  progress guard declared undispatched legs dead once the cache decoupled dispatch from manifest
  order, measured at 6 of 30 on the second run. Replaced by a forced dispatch. Gates A2/A3/B2 are
  deferred to their own unit as the review recommends.
- rev-4 · 2026-08-20 · CLOSED, on the same status audit. The bounded worker pool (S1), the
  `GATE_JOBS` resolution (S2), the longest-first dispatch from `<git-dir>/gate-timings.tsv` (S3),
  manifest-order reporting (S4) and the serial guard pre-pass (S5) are all in `run-gates.sh` and have
  been through two later units. S2's `min(8, nproc)` default is SUPERSEDED by
  `TOOL-aPacedTurnstile-2`, which moved the width into a declared table keyed on detected cores and
  RAM (`tools/run-gates/gate-profiles.txt`); node `a` selects the `capable` row at width 8, so this
  unit's behaviour did not move when the mechanism did. Leaving this record non-terminal made it the
  spec of record for four seams that three later units rewrite, which is two builds holding one seam
  open at once.

  The prototype figure in §1 is superseded and worth keeping visible rather than editing: this unit
  promised 79.9 s against a 47-leg serial bar. The bar is now 86 legs and, measured on a quiet node
  `a` at `43a6c13` by `tools/run-gates/profile_bar.py`, runs 1033.2 s against 4614.6 s of leg work.
  The pool did what this unit claimed — packing is 1.24x of the ideal — and the bar grew past it.
  What the same instrument reports is that the bar is now FLOOR-bound: one leg is 836.5 s, 81 % of
  the wall clock, so no width and no dispatch order can move it. That is the finding that re-scoped
  `aPacedTurnstile`, and it is recorded here because this is the unit whose mechanism it retires as a
  lever.
- rev-2 · 2026-08-11 · folded two defects found while building, both caught by arming the arms rather
  than by the build passing. The dispatcher-plus-polling-reader design was replaced by a single shell
  blocking on `wait -n` after the poll tick was measured at 317s of a 617s serial run; and the
  `(no result)` branch gained its dispatch-exhausted plus full-`wait` guard after the unguarded
  reading was measured declaring healthy legs dead 6 runs in 8. AC7 added for the second.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bounded worker pool that runs shell commands
concurrently and reports per item"` returns no shell concurrency seam. The repo's only bounded
fan-out helpers are `boundedParallel` and `boundedPipeline` in `tools/workflows/`, which are
JavaScript for the `Workflow` runtime and enforce an agent cap rather than a process pool. They do
not apply. The pool is therefore written here, and it is deliberately confined to `run-gates.sh`
rather than added to `tools/lib/`, because no second caller exists.

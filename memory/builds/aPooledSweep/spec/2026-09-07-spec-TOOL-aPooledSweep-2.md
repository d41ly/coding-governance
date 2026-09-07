# TOOL-aPooledSweep-2 — a contended reading grades no budget, and says so

**Status:** CLOSED · rev-3 · 2026-09-07 · node a · Tier-2 · base 05fb897c · streams tooling · order 2 · ratified 2026-09-07

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md](../build/2026-09-07-build-TOOL-aPooledSweep-1-acceptance-ledger-and-the-measured-ab.md) | journal | TOOL-aPooledSweep-1 TOOL-aPooledSweep-3 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-diff-review-round1.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-diff-review-round1.md) | diff-review | TOOL-aPooledSweep-1 TOOL-aPooledSweep-3 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-diff-review-round2.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-diff-review-round2.md) | diff-review | TOOL-aPooledSweep-1 TOOL-aPooledSweep-3 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPooledSweep-1 TOOL-aPooledSweep-3 |
| [2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md](../reviews/2026-09-07-review-TOOL-aPooledSweep-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-aPooledSweep-1 TOOL-aPooledSweep-3 |

<!-- /gen:spec-records -->

## 1. Goal

`run-selftests.sh` grades each suite against its declared budget, and that grading is the whole
reason its loop is serial. A pooled sweep charges every suite the others' contention, so its clock
cannot grade a budget. Make the runner say which kind of reading it took, and issue a cost verdict
only for the kind that can carry one.

## 2. Scope (IN)

- **S1** — every reading the runner takes is TAGGED with the condition it was taken under: `serial`,
  or `pooled@<outer>x<inner>`. Observed by AC1.
- **S2** — the budget comparison fires for a `serial` reading and is WITHHELD for a pooled one. A
  withheld row prints its elapsed seconds and the word `withheld`, never `ok` and never a breach.
  Observed by AC1 and AC2.
- **S3** — the summary line states HOW MANY cost verdicts were withheld and why, so a sweep is never
  mistakable for a budget-clean run. Observed by AC2.
- **S4** — a pooled run writes no reading into any artifact that a later ranking reads. Observed by
  AC3.
- **S5** — `--rank` GAINS an explicit refusal for a pooled condition, because it has none today. A
  budgets row whose reading names the pooled tag joins the UNBACKED list by name, and `--rank` then
  computes no share at all and exits non-zero — which is the refusal that already exists for an
  unrecognised condition, not a new one. Observed by AC5.
- **S6** — THE TAG THE RUNNER EMITS IS THE TAG THE REFUSAL MATCHES. One spelling, asserted as a round
  trip rather than hand-typed twice. Observed by AC6.

## 3. Non-goals (OUT)

- Not changing any declared budget. The numbers in `tools/run-gates/selftest-budgets.txt` and the
  conditions beside them are the parent build's and stay as they are.
- Not making a contended reading usable by scaling it. This repo has measured one leg varying 5.5x
  median and 47.1x worst under contention; a correction factor derived from one suite would be
  applied to fifty-eight it was never measured on.
- Not removing the serial mode. It is the only mode that can grade a budget, and it stays the
  default for exactly that reason.

### Edges

- **consumes-from** `TOOL-aPooledSweep-1` — the pooled mode and the width pair it chose, which is
  what the condition tag is composed from. Without it there is no pooled reading to withhold.
- **hands-off** external — a future unit that wants a pooled reading to grade something must first
  establish a contention model this repo does not have.

## 4. Design

### Why this is a separate unit and not a branch inside the pool

The pool is a scheduling change. This is a claim about what a NUMBER means. They fail
independently: a correct pool that grades budgets from its own contended clock reports breaches that
are the pool's doing, and a correct withholding rule attached to a broken pool withholds nothing
because nothing ran concurrently. One mechanism per spec, so that a closing diff review can tell
which half a finding lands on.

### The tag, and where it is composed

The runner already knows both facts at the moment it takes a reading: which mode it is in, and the
outer/inner pair `TOOL-aPooledSweep-1` resolved. The tag is composed once, before the first suite
starts, and carried as one variable — not re-derived per row, which would be the same fact spelled
twice in a file whose own header names that defect.

### Withheld is not passed, and not failed

Three states, printed distinguishably:

| state | when | exit contribution |
|---|---|---|
| `ok` | serial reading, inside budget | none |
| `OVER` | serial reading, over budget | non-zero |
| `withheld` | pooled reading | none |

`withheld` contributing nothing to the exit status is the correct reading of S4 in
`TOOL-aPooledSweep-1`: the sweep's exit status is the SWEEP verdict, and a budget nobody graded is
not evidence either way. What stops that being a silent pass is S3 — the summary states the count,
so a green sweep announces on every run how many budgets it did not grade.

This is the same shape the repo already uses for a held gate leg and for `lib-selftest.sh`'s
declared-nothing refusal: an announced skip, never an omitted row.

### The refusal that did not exist, and where it has to sit

Rev-1's S5 asserted that `--rank` would already refuse a pooled reading. It does not.
`run-selftests.sh:80` matches conditions with `measured (\d+)s (?:on )?(.+?)(?:,|$)`, whose second
group accepts ANY text up to a comma or end of line — so `measured 42s pooled@8x1 on node a, x1.5`
parses cleanly and ranks as a `direct` reading. The closed vocabulary is closed on the two reading
SHAPES, not on the condition text after the seconds, and eleven of the fifty-nine rows already use
that spelling, three of them already carrying a width clause. So the likely spelling is the one that
slips through.

**It is NOT a new `CONDS` entry, and rev-2 had that backwards.** A `CONDS` match is precisely what
RANKS a row: the loop at `run-selftests.sh:102` breaks on the first match and appends to `rows`,
and only the `for…else` fall-through reaches `unbacked`. Adding a pooled pattern to that list would
make a pooled reading rank rather than refuse — the exact inversion of the intent — and the lenient
`measured` entry sits above it and would match first anyway.

So the refusal is a REFUSE list consulted BEFORE the `CONDS` loop: a reading matching it goes
straight to `unbacked` without being offered to the rankers. `unbacked` is already a total refusal —
`run-selftests.sh:120-129` prints every offending row by name, states that no share was computed,
and raises `SystemExit(1)` — and that is the correct behaviour rather than a limitation to work
around: a denominator missing its largest members is not a majority of anything, which is what
`TOOL-aQuenchedHarness-6` S2 already decided for the same file. Rev-2's AC5 asked for the serial row
to "still rank" beside a refused one, which that path cannot do and should not.

### Inventory

- `SWEEP_CONDITION` — the composed tag.
- `withheld` — the row state token. A word rather than a symbol, so a reader grepping a captured
  sweep for a verdict finds it.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` · one build record.

### Alternatives rejected

**Grading the budget anyway and widening it for the pool.** Rejected: the widening factor is
unmeasured across the population, and a budget that is wide enough never to red under contention is
wide enough never to red at all — the criterion-that-cannot-fail the parent build already had to
delete once.

**Timing each suite against its own start rather than the sweep's.** Rejected: it does not address
contention, which is other suites competing for the same cores and the same on-access scanner during
this suite's own window. A per-suite clock under a pool is still a contended clock.

## 5. Production-readiness checklist

- security — N/A: no execution path changes; this decides what a printed number means.
- perf / scale — N/A: the tag is composed once per run.
- error / empty / loading states — a row whose suite could not be resolved has no reading at all and
  keeps the existing unresolved-row line; it is not a withheld verdict.
- observability — the per-row state token and the summary count are the record.
- risks — the failure that matters is a withheld verdict rendering as `ok`, which would make a sweep
  read as budget-clean. AC2 stages exactly that.
- testing — arms in `run-selftests.test.sh` for both modes over one fixture population.
- migration — additive. The serial mode's tokens are unchanged.
- user docs — `print_usage` gains a clause naming what `--sweep` does not grade.

## 6. Acceptance criteria

- **AC1** — When a fixture suite whose elapsed time exceeds its declared budget is run in the
  DEFAULT mode, its row reads `OVER` and the run exits non-zero; when the same suite is run under
  `--sweep`, its row reads `withheld` and contributes nothing to the exit status. Red when: the
  pooled row reads `ok` or `OVER`.
  fixture: a budgets row whose declared seconds are below a deliberately slow fixture suite's.
- **AC2** — When `--sweep` finishes, its summary names the NUMBER of cost verdicts withheld, and
  that number equals the count of `withheld` rows it printed. Red when: the summary is absent, or
  the number disagrees with the rows.
  figure: DERIVED — both sides are counted from the same run's output.
- **AC3** — When a pooled run finishes, `git status --porcelain -- tools/run-gates/selftest-budgets.txt`
  is empty and no file a `--rank` read consumes has changed. Red when: a pooled reading is written
  anywhere a ranking would later sort against a serial one.
- **AC4** — When `bash tools/run-gates/run-selftests.sh --help` is read, it states that `--sweep`
  issues no cost verdict. Red when: the flag is documented as a faster equivalent of the default.
- **AC5** — When a fixture budgets file carries one row whose reading names the pooled tag and one
  ordinary serial row, `bash tools/run-gates/run-selftests.sh --rank` NAMES the pooled row in its
  unbacked list, computes no share at all, and exits non-zero; and when the pooled row is removed,
  the same file ranks cleanly. Red when: the pooled row is ranked as a `direct` reading; or the
  refusal fires on the file that carries only serial rows, which would make it a blanket rather than
  a predicate.
- **AC6** — When `--sweep` emits its condition tag and that exact emitted string is written into a
  fixture budgets row, `--rank` refuses it. Red when: the emitter's spelling and the refusal's
  pattern differ, which a fixture that hand-types the tag on both sides cannot detect.
  figure: DERIVED — the tag is captured from a `--sweep` run rather than typed into the arm.

## 7. Gates

`run-selftests self-test` · `memory hygiene` · `lexicon naming predicates`

New arm: `tools/run-gates/run-selftests.test.sh` · a fixture suite deliberately slower than its
declared budget, run in both modes · the suite's assertion floor moves by the number of arms added.
New arm: `tools/run-gates/run-selftests.test.sh` · a fixture budgets file carrying one pooled-tagged
reading and one serial reading, ranked, plus the same file with the pooled row removed · same floor
move.
New arm: `tools/run-gates/run-selftests.test.sh` · the tag CAPTURED from a `--sweep` run and fed to
`--rank`, so the emitter and the reader are joined rather than hand-typed twice · same floor move.

## 8. Open questions

- **F1 — should a pooled sweep offer an opt-in to grade budgets anyway?** RESOLVED (agent,
  2026-09-07, delegated): no. An opt-in to grade a number that cannot carry a verdict is a flag whose
  only use is to produce a verdict the runner has just finished saying is unsound, and the survivor
  after M3's veto 1 is the option that does not contradict this unit's own S2.

## 9. Revision log

- rev-1 · 2026-09-07 · initial draft.
- rev-2 · 2026-09-07 · §2 S5 · §4 · §6 AC5 · §7 · folded round-1 spec audit H5. S5 asserted a
  `--rank` refusal that does not exist — its second condition pattern accepts any text after the
  seconds — so the net is now built and AC5 observes it, staged both ways so the refusal is not a
  blanket.
- rev-3 · 2026-09-07 · §2 S5, S6 · §4 · §6 AC5, AC6 · §7 · folded round-2 spec audit B1, H2, H6, L1.
  The loop exited NON-CONVERGENT at round 2, so every finding was disposed by FOLD. B1: `unbacked`
  is a blanket `SystemExit` before any ranking, so rev-2's AC5 asked for behaviour the path cannot
  have; the criterion now asserts the total refusal and stages the clean file beside it. H2: a
  `CONDS` match RANKS a row, so a pooled entry there would have done the opposite of the intent —
  the refusal moves ahead of that loop. H6: no criterion read the tag the runner emits, so AC6 makes
  it a round trip. L1: three of the eleven `measured Ns` rows carry a width clause, not one.

## 10. Reuse audit

No existing seam fits the withholding rule: `tools/run-gates/run-selftests.sh` has exactly one
verdict path today, `elapsed > budget`, with no state between pass and fail and no condition tag
anywhere in its runtime. The evidence is the file itself — its `OUTER=1` comment states the serial
loop exists BECAUSE two suites racing would charge each the other's contention, which is the
problem this unit answers rather than a seam that answers it. The announced-skip SHAPE is reused
from two places that already carry it, `run-gates.sh`'s held legs and `lib-selftest.sh`'s
declared-nothing refusal, and both were read at source rather than cited from prose.

Recall terms used: `python tools/memory-recall/query.py "why could the costly self-test suites not be
ported onto the parallel harness, and what would make them portable" --terms "selftest harness port
arm inventory extract negative assertion substring snapshot shard parallel budget majority share
spawn"`.

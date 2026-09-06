---
slug: aQuenchedHarness
node: a
opened: 2026-09-06
streams: tooling
roster: TOOL
parents: aBoundedCeiling
authorized-by: prompt
ids: TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 TOOL-aQuenchedHarness-9
---

# aQuenchedHarness — self-checks that cannot wedge a build, and that adopters never run

## The problem this build exists to solve

Self-check gate legs run for hours and can wedge, freezing unattended builds; two concurrent builds
stalled 9 h and 6 h. Measured at HEAD on node `a`: 49 of the 94 legs in `tools/gate-legs.json` are
self-tests holding 7969 s of a 13644 s leg-sum, and every ceiling is sized about 10x its recorded
seconds, so a wedged leg burns 1.2 to 4.5 hours before the runner kills it. The cost is not compute
— a bare spawn measures 319 ms here and `python -c pass` 773 ms, so a suite forking per arm pays
process creation and little else. Separately, 30 self-test `[[gate_leg]]` rows ship through kit
descriptors while `chunk`, half of the hold predicate, reaches no adopter manifest, so a repo that
copy-installs a kit runs that kit's self-tests on every bar.

## Expected improvements

- A default bar runs no self-test leg, in this repo and in every adopter.
- A wedged leg is bounded by a ceiling derived from its recorded seconds, and a wedged bar by a wall.
- The held population runs on demand inside a declared budget and REDs on breach.
- The rebuilt suites keep every staged break they had, at a fraction of the spawns.

## Detriments if this is not built

- Unattended builds keep stalling for hours on a bar with no owner turn to interrupt it.
- Adopters keep paying for suites that test kit source they never edit.
- Kit work stays unverifiable in practice: the only checks that grade it cost hours, so nobody runs
  them, and a held leg accumulates drift silently (`TOOL-aBoundedCeiling-10`).

## Build-level rules

- **Reuse before invention.** `tools/unattended/run-unattended-gates.sh` already IS this pattern for
  one kit, under an owner ruling of 2026-08-23 recorded in `AGENTS.md`. This build GENERALIZES that
  ruling and that script. It does not reverse the ruling and does not author a second mechanism.
- **The hold predicate is `subject == kit || chunk == selftests`**, in `tools/run-gates/run-gates.sh`.
  The adopter gap is that `chunk` travels to no descriptor and no emitted manifest —
  `TOOL-aScouredKit-27` states it and warns that half-building it is worse than the gap.
- **No derived count or duration is typed in prose.** Every figure comes from `tools/gate-legs.json`
  or `<git-dir>/gate-ledger.tsv` at read time. The one exception is a DECLARED budget, which is a
  decision and carries the reading it was set against, per this repo's settled habit.
- **A rebuilt suite keeps its arm inventory** — same staged breaks, same expected verdicts, compared
  before and after. A rebuild that drops an arm is a regression wearing a speed-up's clothes.
- **A ceiling measured standalone does not bound a leg under the pool** (`TOOL-dRetiredFork-40`).
  Derive from the ledger's loaded readings, never from a quiet stopwatch.
- **This build inherits its parent's unfinished half.** `aBoundedCeiling` ran on nearly this prompt
  and shipped the ceilings that are now the hang bound. Its open rows are inputs, not prior art.

- **Unit 8 was ADDED mid-build and takes order 1.** Probing unit 2's ceiling band found the
  actual cause of the stalls: the bar reaps its own live holder, so bars run concurrently.
  Cost work is worth less while the bar multiplies itself.

## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aQuenchedHarness-1` | OPEN | a bar's own wall, so a wedged run dies with a verdict instead of stalling a build |
| 2 | `TOOL-aQuenchedHarness-2` | OPEN | a leg ceiling carries the reading it was set against, in the tree |
| 3 | `TOOL-aQuenchedHarness-3` | OPEN | a self-test never reaches an adopter, as a leg or as a file at all |
| 4 | `TOOL-aQuenchedHarness-4` | OPEN | one on-demand runner for the whole held population, budget-graded |
| 5 | `TOOL-aQuenchedHarness-5` | OPEN | a spawn-cheap self-test harness the suites are rebuilt onto |
| 6 | `TOOL-aQuenchedHarness-6` | OPEN | the dominant suites rebuilt onto it, arms preserved and a floor cleared |
| 7 | `TOOL-aQuenchedHarness-7` | OPEN | the longest leg on the bar is a repo check the hold never reaches |
| 8 | `TOOL-aQuenchedHarness-8` | OPEN | the turnstile stops reaping a live holder, so two bars stop running as one |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 8 unit(s) · node a · opened 2026-09-06 · streams tooling
ids TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 TOOL-aQuenchedHarness-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aQuenchedHarness-8 — the turnstile stops reaping a live holder, so two bars stop running as one](spec/2026-09-06-spec-TOOL-aQuenchedHarness-8.md) | 1 | 2 | INPROGRESS | rev-2 | 2026-09-06 |
| [TOOL-aQuenchedHarness-1 — the bar's own wall, so a wedged run dies with a verdict](spec/2026-09-06-spec-TOOL-aQuenchedHarness-1.md) | 2 | 2 | INPROGRESS | rev-5 | 2026-09-06 |
| [TOOL-aQuenchedHarness-3 — a self-test never reaches an adopter, as a leg or as a file](spec/2026-09-06-spec-TOOL-aQuenchedHarness-3.md) | 3 | 2 | INPROGRESS | rev-5 | 2026-09-06 |
| [TOOL-aQuenchedHarness-2 — a leg ceiling carries the reading it was set against, in the tree](spec/2026-09-06-spec-TOOL-aQuenchedHarness-2.md) | 4 | 2 | INPROGRESS | rev-4 | 2026-09-06 |
| [TOOL-aQuenchedHarness-4 — one on-demand runner for every kit's self-tests, budget-graded](spec/2026-09-06-spec-TOOL-aQuenchedHarness-4.md) | 5 | 2 | INPROGRESS | rev-4 | 2026-09-06 |
| [TOOL-aQuenchedHarness-5 — a self-test harness whose unit of cost is not a process](spec/2026-09-06-spec-TOOL-aQuenchedHarness-5.md) | 6 | 2 | OPEN | rev-3 | 2026-09-06 |
| [TOOL-aQuenchedHarness-6 — the dominant suites rebuilt onto the harness, arm inventory preserved](spec/2026-09-06-spec-TOOL-aQuenchedHarness-6.md) | 7 | 2 | OPEN | rev-3 | 2026-09-06 |
| [TOOL-aQuenchedHarness-7 — the longest leg on the bar is a repo check the hold never reaches](spec/2026-09-06-spec-TOOL-aQuenchedHarness-7.md) | 8 | 2 | OPEN | rev-3 | 2026-09-06 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aQuenchedHarness-8` | no |
| 2 | `TOOL-aQuenchedHarness-1` | no |
| 3 | `TOOL-aQuenchedHarness-3` | no |
| 4 | `TOOL-aQuenchedHarness-2` | no |
| 5 | `TOOL-aQuenchedHarness-4` | no |
| 6 | `TOOL-aQuenchedHarness-5` | no |
| 7 | `TOOL-aQuenchedHarness-6` | no |
| 8 | `TOOL-aQuenchedHarness-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aBoundedCeiling](../aBoundedCeiling/README.md)
<!-- /gen:build-edges -->

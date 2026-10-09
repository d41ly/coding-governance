---
slug: aFrugalTurnstile
node: a
opened: 2026-10-09
streams: tooling+playbook+deployer
roster: TOOL+PLAY+DEPL
ids: DEPL-aFrugalTurnstile-1 PLAY-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10
authorized-by: prompt
status: OPEN
---

# aFrugalTurnstile — land a build without paying the full bar again and again

## The problem this build exists to solve

Landing one build across inCMS and NicoCares took more than six hours on 2026-10-09, nearly all of it
full bars re-run at gov's push boundary over trees the unattended close had already graded. The
staleness bound counts every commit, a wrapper bar can never stamp a usable green, a red costs a
whole bar again, three repos' bars starve one host together, and nothing lets a landing take the
scoped bar safely. The owner's prose is the mandate, recorded under
[prompts/](prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md); the design every unit builds from is
[the design record](build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md).

## Expected improvements

- A push whose tree already carries a full green runs no bar.
- After a red, the next bar re-runs what failed and what moved, and can still stamp.
- One bar per host; queued bars name their holder.
- An adopter that declares it lands on the scoped bar, and a post-merge full red blocks the next landing.

## Detriments if this is not built

- Every multi-commit landing keeps paying a full bar, often several.
- A wrapper bar like inCMS's never earns a green the boundary can use.
- Concurrent bars keep failing on load rather than on code.
- The unattended rule keeps demanding a full bar per landing, with no binding post-merge alternative.

## Build-level rules

- **Classification (M2)**: twelve units, MISSING at open, authored this run, one mechanism each,
  every spec citing the design record's decision it implements (`design D<n>`).
- Units writing `.githooks/pre-push` (1, 2, 4, 7) run in that order; so do the `run-gates.sh`
  writers (1, 5, 4, 6) and the `unattended.sh` writers (3, 9). The three text units are disjoint
  from all code and from each other.
- Each unit stages its failing case first and observes it RED in a scratch fixture, never a suite.
- One kit-version bump per touched kit, after the last unit.
- Item 5 of the sibling session owns `run-gates.sh`'s held-summary line; this build does not touch it.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aFrugalTurnstile-1` | staleness counts first-parent landings, and a runner stamp is trusted only for the runner's own manifest |
| 2 | `TOOL-aFrugalTurnstile-2` | pre-push records the green of the bar it ran, and a push whose tree carries one runs nothing |
| 3 | `TOOL-aFrugalTurnstile-3` | the unattended close records the green of the bar it ran |
| 4 | `TOOL-aFrugalTurnstile-4` | lineage reuse: after a red, the boundary's full bar re-runs only failed and moved legs, and may stamp |
| 5 | `TOOL-aFrugalTurnstile-5` | the gate turnstile is host-wide, names its holder, lets nested bars through, and `--hold` admits a foreign bar |
| 6 | `TOOL-aFrugalTurnstile-6` | `post-merge.sh` runs the full bar on a landed sha and publishes its verdict as a remote ref |
| 7 | `TOOL-aFrugalTurnstile-7` | pre-push binds a post-merge red, and `--decide` prints the boundary's decision |
| 8 | `TOOL-aFrugalTurnstile-8` | push-main starts the post-merge bar after a landing where it is declared |
| 9 | `TOOL-aFrugalTurnstile-9` | the unattended close runs the boundary's decision where a post-merge bar is declared |
| 10 | `TOOL-aFrugalTurnstile-10` | the unattended protocol's landing rule states the scoped-then-full path |
| 11 | `PLAY-aFrugalTurnstile-1` | the charter's §1 Landing states the scoped-then-full path |
| 12 | `DEPL-aFrugalTurnstile-1` | the runbook states what an adopter declares to use each part |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-09 · streams tooling+playbook+deployer
ids DEPL-aFrugalTurnstile-1 PLAY-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

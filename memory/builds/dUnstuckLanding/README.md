---
slug: dUnstuckLanding
node: d
opened: 2026-10-04
streams: tooling
roster: TOOL
ids: TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2 TOOL-dUnstuckLanding-3 TOOL-dUnstuckLanding-4 TOOL-dUnstuckLanding-5 TOOL-dUnstuckLanding-6 TOOL-dUnstuckLanding-7 TOOL-dUnstuckLanding-8 TOOL-dUnstuckLanding-9 TOOL-dUnstuckLanding-10 TOOL-dUnstuckLanding-11 TOOL-dUnstuckLanding-12 TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-21 TOOL-dUnstuckLanding-22 TOOL-dUnstuckLanding-23 TOOL-dUnstuckLanding-24
authorized-by: prompt
---

# dUnstuckLanding — unattended runs that close themselves, and a verb for the ones that do not

## The problem this build exists to solve

Unattended runs reach their close and stop there. The two causes the owner names are a red bar the
run did not cause, inherited from the default branch or from another build, which the run does not
resolve itself, and a closing decision the run hands back to an owner who is not there. The run then
writes `ABORTED`, the work lands later with the owner present, and the record says `ABORTED`
forever. A terminal that is false about what happened makes every later reader wrong. The owner's
prompt is recorded verbatim under `prompts/`.

## Expected improvements

- A census of closing-time failures across this repo, inCMS and NicoCares, each one cited.
- A design that lets a run close unattended through an inherited red and a closing decision.
- A separate, truthful record shape for a run that was interrupted and then landed attended.
- The kit mechanisms for asks 3 to 10, built and landed: `--handoff`, `--settle`, and inherited
  reds that land at any age, among them.

## Detriments if this is not built

- Runs keep ending `ABORTED` over work that landed, so the record contradicts git.
- Each inherited red keeps costing an owner turn the mandate was meant to remove.
- Deferred closing decisions keep leaving builds with no status anyone can act on.

## Build-level rules

- **The build also BUILDS asks 3 to 10** (owner, 2026-10-04, `TOOL-dUnstuckLanding-21`). The run
  had read "research and design" as design only. Ask 11 stays filed, for a deployer build. The
  rulings `-22` and `-23` ratify the reversals of D12-i4 and D8; `-24` runs the kit self-tests once,
  at the close.
- Units 13 to 20 close asks 3 to 10 in order. They are `Tier-2` shipped-kit edits, built one at a
  time, because nearly all of them write `tools/unattended/unattended.sh`.
- Classified at kickoff (M2): both units MISSING. Unit 1 is the census and unit 2 the design,
  sequenced 1 then 2, because the design is only as good as the evidence under it.
- The census reads the other two repositories and never writes to them.
- Units 1, 2 and 12 are `Tier-1`, because they write only records.
- Closing review round 1 converged: 0 blockers, 5 HIGH, 17 MEDIUM, 7 LOW. Its HIGHs became
  `TOOL-dUnstuckLanding-12`, and its other findings folded into rev-2 of specs 1 and 2. H1 is
  left-shifted as a new gotcha class, `liveness-negative-from-another-population`. The rest map onto
  existing classes: `observed-by-claim-no-arm-discharges` (H2, M12 to M15),
  `amendment-leaves-its-other-half-standing` (H3, H4, M11) and `two-answers-to-one-question` (M5, M7).

## Parked decisions

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dUnstuckLanding-1` | 1 | the closing-time failure census across gov, inCMS and NicoCares |
| 2 | `TOOL-dUnstuckLanding-2` | 1 | the design: unattended closes through inherited reds and closing decisions, plus attended-landing verbs |
| 3 | `TOOL-dUnstuckLanding-12` | 1 | design rev-2: the closing review's five HIGH findings closed (promoted) |
| 4 | `TOOL-dUnstuckLanding-13` | 2 | `--handoff`: HELD under `owner-landing` or `owner-decision`, with recipe, landing facts and a fail-83 guard (ask 3) |
| 5 | `TOOL-dUnstuckLanding-14` | 2 | the attended terminal: HELD-handoff derives LANDED; `--settle` writes it, and `work-landed-at` on ABORTED (ask 4) |
| 6 | `TOOL-dUnstuckLanding-15` | 2 | drift-audit signals `aborted_work_landed` and `discarded_work_landed` (ask 5) |
| 7 | `TOOL-dUnstuckLanding-16` | 2 | an INHERITED red lands at any age; the age bound becomes a BLOCKER escalation; kit default `land` (ask 6) |
| 8 | `TOOL-dUnstuckLanding-17` | 2 | history legs grade the run's own range; fleet counters a per-build budget, with `fleet_over_budget` (ask 7) |
| 9 | `TOOL-dUnstuckLanding-18` | 2 | the close-decision table and the carry-forward `build-complete` (ask 8) |
| 10 | `TOOL-dUnstuckLanding-19` | 2 | refresh before a verdict: `refreshed-at` on park, handoff, abort and primary close (ask 9) |
| 11 | `TOOL-dUnstuckLanding-20` | 2 | `LANDING_NODES`: a run on a non-landing node hands off by design (ask 10) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 11 unit(s) · node d · opened 2026-10-04 · streams tooling
ids TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2 TOOL-dUnstuckLanding-3 TOOL-dUnstuckLanding-4 TOOL-dUnstuckLanding-5 TOOL-dUnstuckLanding-6 TOOL-dUnstuckLanding-7 TOOL-dUnstuckLanding-8 TOOL-dUnstuckLanding-9 TOOL-dUnstuckLanding-10 TOOL-dUnstuckLanding-11 TOOL-dUnstuckLanding-12
ids TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-21 TOOL-dUnstuckLanding-22 TOOL-dUnstuckLanding-23 TOOL-dUnstuckLanding-24

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dUnstuckLanding-1 — the closing-time failure census across gov, inCMS and NicoCares](spec/2026-10-04-spec-TOOL-dUnstuckLanding-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-dUnstuckLanding-13 — `--handoff`: a run whose work is sound, but which an owner must land or decide, ends HELD instead of ABORTED](spec/2026-10-04-spec-TOOL-dUnstuckLanding-13.md) | 1 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-14 — the attended terminal: a handed record derives LANDED, `--settle` writes it, and a landed ABORTED record gains `work-landed-at`](spec/2026-10-04-spec-TOOL-dUnstuckLanding-14.md) | 2 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-2 — the design: unattended closes through inherited reds and closing decisions, plus attended-landing verbs](spec/2026-10-04-spec-TOOL-dUnstuckLanding-2.md) | 2 | 1 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-dUnstuckLanding-12 — design rev-2: the closing review's five HIGH findings closed](spec/2026-10-04-spec-TOOL-dUnstuckLanding-12.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-15 — drift-audit reports ABORTED run records whose work landed anyway](spec/2026-10-04-spec-TOOL-dUnstuckLanding-15.md) | 3 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-16 — an INHERITED red lands at any age, and the age escalates its ask](spec/2026-10-04-spec-TOOL-dUnstuckLanding-16.md) | 4 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-17 — the history legs grade the run's own range, and check 23 a per-build budget](spec/2026-10-04-spec-TOOL-dUnstuckLanding-17.md) | 5 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-18 — the close-decision table, and a build that lands with its rest carried forward](spec/2026-10-04-spec-TOOL-dUnstuckLanding-18.md) | 6 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-19 — refresh before a verdict: one helper, the `refreshed-at` fact](spec/2026-10-04-spec-TOOL-dUnstuckLanding-19.md) | 7 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
| [TOOL-dUnstuckLanding-20 — `LANDING_NODES`: landing capability declared, resolved from machine and user, and a planned hand-off](spec/2026-10-04-spec-TOOL-dUnstuckLanding-20.md) | 8 | 2 | INPROGRESS | rev-1 | 2026-10-04 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-12 TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-2
TOOL-dUnstuckLanding-20.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dUnstuckLanding-1`, `TOOL-dUnstuckLanding-13` | yes |
| 2 | `TOOL-dUnstuckLanding-14`, `TOOL-dUnstuckLanding-2` | yes |
| 3 | `TOOL-dUnstuckLanding-12`, `TOOL-dUnstuckLanding-15` | yes |
| 4 | `TOOL-dUnstuckLanding-16` | no |
| 5 | `TOOL-dUnstuckLanding-17` | no |
| 6 | `TOOL-dUnstuckLanding-18` | no |
| 7 | `TOOL-dUnstuckLanding-19` | no |
| 8 | `TOOL-dUnstuckLanding-20` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

---
slug: dClosedLoop
node: d
opened: 2026-10-14
streams: playbook+kickoff+tooling+deployer
roster: PLAY
ids: PLAY-dClosedLoop-1 PLAY-dClosedLoop-2 PLAY-dClosedLoop-3 PLAY-dClosedLoop-4 PLAY-dClosedLoop-5 PLAY-dClosedLoop-6 PLAY-dClosedLoop-7 PLAY-dClosedLoop-8 PLAY-dClosedLoop-9 PLAY-dClosedLoop-10 PLAY-dClosedLoop-11
spec-audit: 2026-10-14
authorized-by: prompt
---

# dClosedLoop — gov re-architected onto one lifecycle loop: Plan, Design, Build, Test, Deploy, Maintain, with Review at any stage

## The problem this build exists to solve

Gov governs agentic, multi-node development through 17 kits, 140 gate legs, nine role agents and
about 600 KB of protocol, organised by mechanism and by id family rather than by the lifecycle a
governed repository runs. Nothing states what each stage of that lifecycle takes in, produces and
proves, so handoffs between stages are implicit, some stages have no contract at all, and records
accrete faster than anything drains them: 24 non-terminal builds, 20 of them dormant, and 521 live
asks, 435 of them unlabelled. The owner's prompt is recorded verbatim under `prompts/`.

## Expected improvements

- One ratified architecture stating every stage's entry and exit contract, artifacts, roles, gates
  and Review trigger, once.
- A gap register naming every distance between today's product and that architecture.
- An ordered chain of builds, one per stage plus a convergence build, each owning its gaps.

## Detriments if this is not built

- Each new kit or rule lands wherever its author's mechanism fits, and the loop stays implicit.
- Stages with no contract, such as deploying and maintaining a governed product, stay ungoverned.
- Records and asks keep accreting, because no stage owns draining them.

## Build-level rules

- A design build: it writes no product code. Every change to `tools/`, `skills/`, the template or
  the runbook is a unit of a chain build.
- One spec, `PLAY-dClosedLoop-1`, carries the architecture and the chain plan. A spec writer writes
  it from the ratified decisions, and the declared spec audit runs before any chain build opens.
- Research runs as role agents, one question each; their returns are recorded under `build/`
  beside the spec they serve.
- Chain builds open with a README and a planned unit roster only; their own sessions write their
  specs (owner, 2026-10-14).
- Mapping the non-terminal builds onto the chain is a recommendation: no existing build or ask
  changes status here.
- The chain counts on no build outside it (owner, 2026-10-14): what the design needs, a chain build
  builds; a live build sharing a subject finishes on its own track and is reconciled at the merge,
  never waited on.

## Parked decisions

- **Closing reviews owed:** none through `6ba4eaaa1`. The pair the owner asked for on 2026-10-19, "run the
  review pair on the 11 commits, medium effort", covered the parked debt, and its 35 defects are folded
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`). That fold is unreviewed, and
  `review_debt.py` counts it until a closing review covers it.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `PLAY-dClosedLoop-1` | design: the architecture and the chain plan, one spec written from the ratified decisions, then the declared audit |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-10-14 · streams playbook+kickoff+tooling+deployer
ids PLAY-dClosedLoop-1 PLAY-dClosedLoop-2 PLAY-dClosedLoop-3 PLAY-dClosedLoop-4 PLAY-dClosedLoop-5 PLAY-dClosedLoop-6 PLAY-dClosedLoop-7 PLAY-dClosedLoop-8 PLAY-dClosedLoop-9 PLAY-dClosedLoop-10 PLAY-dClosedLoop-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [2026-10-20-spec-PLAY-dClosedLoop-1](spec/2026-10-20-spec-PLAY-dClosedLoop-1.md) | — | 2 | INPROGRESS | rev-1 | 2026-10-20 |
<!-- /gen:build-units -->

Records: 571 bound to this build, across 4 record folder(s).

Ids no record names: 2026-10-20-spec-PLAY-dClosedLoop-1.

Ids no `spec-audit` record has ever named: 2026-10-20-spec-PLAY-dClosedLoop-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

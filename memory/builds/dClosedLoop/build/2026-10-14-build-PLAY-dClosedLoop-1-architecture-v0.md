# Architecture proposal v0 — the closed loop: stage contracts, witnesses the actor cannot write, one contract for both modes

**Serves:** research PLAY-dClosedLoop-1

The main loop's first proposal, written from the gap register and the six research records before
the owner's design rounds. It is kept unedited so that later revisions can be read against it;
every owner answer that changes it is recorded in
`build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`, and the architecture that survives
is written into the spec `PLAY-dClosedLoop-1`.

## The model in one paragraph

Gov becomes one declared loop of six stages (Plan, Design, Build, Test, Deploy, Maintain) plus
Review. A build is the work item that moves through the stages, and its units move through Design,
Build and Test inside it. Every stage has a CONTRACT: the artifact it takes in, the roles and
harness that do the work, the artifact it hands out, the WITNESS that proves the hand-off (a check
the actor cannot write), its Review lens and trigger, its records and its concurrency claim. The
contracts are declared once, in a machine-readable loop definition, and the charter, kickoff,
`/build`, the bar's grouping and the docs index are rendered from it. Every shipped part declares
the stage it serves, and a coverage gate reds a part that serves none. Maintain closes the loop by
feeding Plan, and a Loop Review reads the loop's own metrics and proposes contract changes,
including retiring gates that never catch anything.

## Principles

- **P1. One loop, declared once.** The loop definition is the single source; nothing restates a
  stage contract (`[one-fact]`, `[derive]`). It grows from `tools/roles/workflows.toml`, which
  already orders the middle of the loop as stages 0 to 7. (gap-spine-01, gap-design-01)
- **P2. A hand-off is a witnessed artifact, never a status token.** A stage's exit is computed from
  committed history, a derived join or a remote verdict, never from a value the actor typed: no
  self-set INPROGRESS, no route the guarded agent wrote, no hand-writable verdict.
  (gap-spine-02, gap-design-04, gap-build-01)
- **P3. The binding verdict lives off the actor's node.** A remote verifier decides whether the
  default branch moves; local bars are early signal; verdicts are published per tree so every node
  reads one answer. (gap-test-01, gap-test-02, gap-test-05, gap-deploy-02)
- **P4. One contract, two authorizations.** Attended and unattended builds run the same stage
  contracts; the mode decides only who authorizes a transition, the owner's turn or a mandate. The
  unattended definition of done becomes the loop's exit checks for everyone. (gap-spine-03,
  gap-build-02)
- **P5. Concurrency by lease.** A build holds a lease from Plan's exit and a unit from Design's
  exit, on the remote, with the fleet tag, a heartbeat and an expiry, in both modes; a design index
  joins every live spec's files across builds and refuses an overlap no spec acknowledges.
  (gap-conc-01, gap-conc-02, gap-design-02)
- **P6. Maintain feeds Plan.** Maintain runs on a cadence; every detector carries a pin and an
  owning stage; every breach becomes an ask with a severity and an acceptance, which Plan must place
  or dispose. (gap-maint-01, gap-maint-02, gap-plan-02, gap-plan-05)
- **P7. Review at every stage, and of the loop.** Each stage declares its Review lenses and their
  trigger, deterministic checks first and agent lenses only where judgment is needed. The Loop
  Review is periodic and reads stage cycle time, review yield, each gate's catches against its
  cost, and records overhead. `[left-shift]` gains a twin: a gate, rule or bug class that catches
  nothing for a declared period is retired. (gap-review-01, gap-review-02, gap-maint-03)
- **P8. The product is the loop.** The loop definition and the stage kits are what ships; gov's
  repository is adopter zero with a thin overlay; adopters receive every stage's contract, including
  a product-test shape, a declared release, deploy and verify path, emitted CI and a currency watch.
  (gap-spine-04, gap-test-03, gap-deploy-01, gap-deploy-03, gap-deploy-04)
- **P9. Weight is budgeted.** The governing surface carries budgets (legs, guide bytes, registry
  rows), and the share of work spent on records is a measured loop metric with a ceiling.
  (gap-spine-05, gap-maint-03, gap-maint-04)

## Stage contracts, first draft

| Stage | Takes in | Work and roles | Hands out | Witness | Review |
|---|---|---|---|---|---|
| Plan | an owner prompt, an ask, a Loop Review proposal | a planner and triager role drafts; the owner ratifies | an opened build placed in the ordered plan, with dependencies and a lease | every live build and every open BLOCKER or HIGH ask placed or disposed; the lease exists | Plan Review: order, dependencies, duplicates, overlap with live builds |
| Design | a planned, leased build and its brief | reuse scout and researcher where needed; spec writer; spec reviewer, skeptic, synthesizer | a spec set at a named revision, forks resolved, overlaps acknowledged | derived design state READY (never FORKED); an audit record naming the revision where the risk tier owes one; the design index | spec audit lenses plus the deterministic cross-build index |
| Build | a unit with its design witness and lease | one builder per unit, each in its own worktree | commits in the unit's scope; owed arms observed; a closing review over the range | history legs in pre-push and CI: scope attribution, closing review recorded, pass order | the closing diff review |
| Test | a built range | the local bar as early signal; the remote verifier as the binding run: the full bar, the held self-tests, the adopter's product tests | a verdict published for the tree | the remote verdict, a required check | gate review: new gates seen red, arms armed, cost inside ceiling; flake triage |
| Deploy | a verified tree | the lander; for gov, kit mints and release notes; for an adopter, its declared release, deploy and verify steps run by emitted CI; govkit distribution | a landed SHA, per-SHA deploy and verify verdicts, release notes, adopter currency | verdict refs published by CI; the currency probe | landing review, release review, adopter-update review |
| Maintain | a cadence tick or an event | a maintenance recipe: detectors, cleanup and reap dry-runs, triage drafts, dormancy proposals | asks with severity and acceptance; signals inside pins or owned; a maintenance record | every detector pinned and owned | the Loop Review |

## How today's assets converge

| Today | Becomes |
|---|---|
| `tools/roles/workflows.toml` (stages 0–7) | the seed of the loop definition |
| the unattended `DOD_CORE` | the shared stage exit checks, for both modes |
| `tools/run-gates/` and `tools/gate-legs.json` | the Test stage's runner, legs grouped by stage, plus a shipped CI workflow |
| `tools/workflows/tier2-review.js` | the Review harness, with lens sets per stage |
| `tools/drift-audit/` | Maintain's detectors, each pinned and owned |
| `tools/govkit/` | Deploy's distribution, plus the currency watch and emitted CI |
| `tools/memory-tree/` | the record layer of every stage, plus the plan record |
| `tools/codebase-map/` | stage claims per part, and the design index |
| `skills/session-kickoff/` | the stage-aware entry: orientation, then the Plan to Design hand-off |
| the `recipe` mode of `tools/unattended/` | Maintain's cadence |
| `tools/branch-reconcile/`, `tools/process-monitor/`, `tools/runlog/` | Maintain's actuators and readers |

## A first cut of the chain

A directed chain with one root and one sink, ordered by dependency rather than loop position,
because later stages' witnesses depend on the Test stage's published verdicts:

1. **Spine**: the loop definition, stage claims on every part, the coverage gate, the rendered
   charter loop section, the witness rule, the product and overlay split.
2. **Test**: the remote verifier, published verdicts, held self-tests before landing, the
   seen-red recorder, flake records, the adopter product-test shape.
3. **Build**: exit by history in both modes, unit scope, one worktree per unit.
4. **Concurrency**: leases for builds and units, the design index, overlap refusal.
5. **Design**: the hand-off witness, the audit default by risk tier, reuse and alternatives checks.
6. **Plan**: the plan record, the planner and triager role, Plan Review, placement and dormancy.
7. **Deploy**: emitted CI, the adopter release contract, per-SHA verdicts, the currency watch,
   release notes.
8. **Maintain**: the cadence, bound detectors, the value and retirement ledger.
9. **Review**: lenses per stage and the Loop Review.
10. **Convergence**: the charter regrouped by stage, docs consolidated and derived, superseded
    legs, rules and builds retired, adopters migrated.

## Open questions for the owner

Scope of the product; the meaning of Deploy for an adopter's own product; where the binding verdict
lives; which transitions the owner keeps; the Review default and its cost appetite; hard or
advisory concurrency; what a maintenance run may do unattended; who orders the plan; whether the
surface is budgeted and pruned; what happens to the 24 live builds; the chain's order and shape.
Each is asked, and its answer recorded, in the design-rounds record.

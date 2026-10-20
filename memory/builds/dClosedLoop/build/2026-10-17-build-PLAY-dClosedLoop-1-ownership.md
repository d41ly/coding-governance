# PM-10's ownership table: every node a build must build, and its owner

**Serves:** research PLAY-dClosedLoop-1

PM-8 made a node's owning build a field on the node, and PM-10 asked for that field's values as a proposal
the owner approves in one pass. This record holds the rule, the proposal for all 351 nodes with each one's
evidence, the 47 rows that need the owner's eye, and what lands once it is approved.

## [words] The owner's words, 2026-10-17

- PM-10, verbatim: "I propose, you approve (Recommended)"
- The convergence order that makes this table its first step, verbatim:

  > Let's take convergence steps in order, then. No new scope until 2-4 are done but we're not 'finishing the build' until this design takes full shape. Execute on The PM-10 ownership table, The chain reordering, and The review declared at kickoff.

  The state record's `[convergence]` carries the order.

## [rule] What owning means, and the evidence

- **A node's owner is the build that implements the behaviour the node names or switches.** A caller or a
  reader is not its owner. dBoundRoles's driver runs `placement.check`, and dRankedPlan, which defines
  the check, owns it.
- **The population is PM-8's six kinds of node:**
  - the flow's 81 items;
  - the catalogue's 187 rows, `review.<stage>` among them as one row, which the preset check expands to
    six keys;
  - Runtime's 10 points;
  - the 25 tag namespaces;
  - the 7 systems;
  - 41 record kinds. They are tabulated here from layer-memory `[contract]`'s list and the chain rows
    that name a kind. Each layer's contract registers its own kinds, so the list is not closed, and its
    fold arms the map's record-kind namespace.
- **The evidence, strongest first:**
  - `decided`: an owner's answer (PM-9), or a step section's own statement, as flow-steps `[lifecycle]`
    names dWellOiledMachine (RT-3);
  - `stage`: the chain table gives the item's step to its stage's build;
  - `row`: a chain row cites the node by tag, bare or with a value, as `retrofit.cadence: hot-first`;
  - `row-wildcard`: a chain row cites the node's namespace by a wildcard, as `core.*`;
  - `system`: a system's design table lists the key, and the system's record names its owner;
  - `declared`: the systems record's Owners bullet registers the namespace with a build;
  - `layer`: the node is a layer's point, and the chain table gives the layer's stage to one build;
  - `namespace`: nothing names the key itself, and its namespace's work sits in one chain row, quoted in
    `[namespaces]`;
  - `judgment`: the evidence disagrees, or there is none, and the row says why.
- **A row is flagged** when it rests on judgment or its evidence disagrees with its proposal. Its "Look"
  cell says `yes`.

## [summary] The proposal in numbers

```text
$ python proposal.py out
nodes 351: items 81, keys 187, points 10, tag namespaces 25, systems 7, record kinds 41
by evidence: row 94, namespace 78, stage 68, judgment 43, declared 25, system 18, decided 13, layer 10, row-wildcard 2
by owner: dTotalRecall 52, dDeclaredLoop 42, dWellOiledMachine 40, dWitnessedBar 33, dShippedRelease 29, dOrderedCharter 25, dCalibratedLens 22, dRankedPlan 21, dBoundRoles 21, dIndexedDesign 20, dScopedBuild 18, dTendedCadence 14, dFairHearing 8, dMindYourWords 6
every node has exactly one owner, and every owner is a chain build: yes · flagged 47
chain builds that own no node: dConvergedCharter
```

- **Every node has exactly one proposed owner, and every owner is a chain build.**
- **dConvergedCharter owns no node.** Its work migrates and retires what the other builds make, and it
  owns 7 gaps.
- **Four rows cite a key whose namespace is otherwise another build's.** Each row implements the key's
  behaviour, so the row stands:
  - `review.opt-in` and `review.unclassed`, dFairHearing's;
  - `deps.landing`, dShippedRelease's;
  - `review.findings`, dScopedBuild's.

## [look] The rows that need the owner's eye

The 47 flagged rows, in one table:

| Node | Kind | Proposed owner | Why |
| --- | --- | --- | --- |
| `entry.intake` | item | dWellOiledMachine | PM-9: the intake hook stays dWellOiledMachine's, with `gap-rt-14`; dRankedPlan's row also describes the hook, which the re-cut reconciles |
| `review.trigger` | item | dCalibratedLens | dCalibratedLens's row: review by policy per stage, breakpoints placeable at any item boundary |
| `review.pin` | item | dFairHearing | dFairHearing's row cites it, where the stage rule would give it to dCalibratedLens; row dFairHearing |
| `review.lens` | item | dFairHearing | the panel's lenses run in the review harness; dCalibratedLens's row draws each stage's lenses from dFairHearing's catalogue |
| `review.refute` | item | dFairHearing | dFairHearing's row: skeptic batches sorted by cited address |
| `review.report` | item | dFairHearing | dFairHearing's row cites it, where the stage rule would give it to dCalibratedLens; row dFairHearing |
| `review.fold` | item | dCalibratedLens | it disposes the confirmed findings into the unbuilt specs, after `review.dispose`, which dCalibratedLens's row holds; the spec writer acts in it |
| `preset` | key | dDeclaredLoop | dDeclaredLoop's row builds the named presets and their completeness check; dFairHearing's row cites `preset` as the review harness's own argument, a homonym; row dFairHearing |
| `hooks.bypass` | key | dWitnessedBar | whether the bar's hooks may be bypassed; dWitnessedBar's row records bypasses and owns the hook-read verdict, and the enforcement surface is dWellOiledMachine's |
| `placement.check` | key | dRankedPlan | dRankedPlan's row defines placement and its check; dBoundRoles's driver only runs it; row dBoundRoles,dRankedPlan |
| `orient.budget` | key | dDeclaredLoop | dDeclaredLoop's row records orientation cost per stage, which the key's values switch |
| `decisions.major` | key | dTotalRecall | it says who declares a decision major for the log, dTotalRecall's; `build.ratify`, dScopedBuild's, rules on forks already classed |
| `notify.channel` | key | dWellOiledMachine | notification adapters are a Runtime point (layer-runtime `[extend]`) |
| `instructions.edit` | key | dOrderedCharter | the instruction manifest and its guarded write command are dOrderedCharter's; dTotalRecall and dMindYourWords route their changes through it; row dOrderedCharter,dTotalRecall,dMindYourWords |
| `verdict.remote.trust` | key | dWitnessedBar | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point |
| `verdict.remote.pin-scope` | key | dWitnessedBar | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point |
| `verdict.remote.pin` | key | dWitnessedBar | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point |
| `build.closes` | key | dShippedRelease | `deploy.released` reads it, and Deploy holds the close; dDeclaredLoop's row cites it only as the presets check's example; row dDeclaredLoop |
| `build.release-hold` | key | dShippedRelease | it says what waits at `deploy.released` (RH-1), a Deploy item; dWellOiledMachine's sweep only raises a wait past `build.release-ceiling` |
| `integrations.tracker` | key | dTotalRecall | it mirrors the ask register out; the register is dTotalRecall's, and the mirror is an integrations adapter at its point |
| `patch.ratify` | key | dPlacedRequest | `entry.claim`, dPlacedRequest's own item, reads it for every patch at entry, and its other readers, `deploy.mandate` and `maintain.patch`'s route, descend from dPlacedRequest (moved from dTendedCadence by the owner's FK-6-2, 2026-10-20) |
| `annotations.delivery` | key | dBoundRoles | it switches the work order's code-notes slot, which dBoundRoles renders; the annotations system is dTotalRecall's; system annotations (dTotalRecall) |
| `review.twin` | key | dFairHearing | dFairHearing's row runs the twin merge `review.twin` opts in (RS-1); the role-shapes system, dBoundRoles's, declares the `twin` shape kind; row dFairHearing; system role-shapes (dBoundRoles) |
| `memory.default-load` | key | dTotalRecall | dTotalRecall's row holds the default load of the charter and the card; dWellOiledMachine's session-start hook performs the load; system memory-structure (dTotalRecall),project-map (dTotalRecall) |
| `memory.item-budget` | key | dTotalRecall | the read budget per role item is dTotalRecall's; dCalibratedLens derives one of its values, `measured`; row dTotalRecall,dCalibratedLens; system memory-structure (dTotalRecall) |
| `memory.project-map` | key | dBoundRoles | it selects the roles whose work orders carry the map slot, which dBoundRoles declares; the project-map system is dTotalRecall's; row dBoundRoles; system project-map (dTotalRecall) |
| `memory.map-unfold` | key | dBoundRoles | the unfolds render in the work order's map slot, dBoundRoles's; the project-map system is dTotalRecall's; system project-map (dTotalRecall) |
| `memory.map-purpose` | key | dTotalRecall | the map and its purposeless-node population are dTotalRecall's; dOrderedCharter adds the namespace rows' purpose-source field the key reads; row dOrderedCharter,dTotalRecall; system project-map (dTotalRecall) |
| `retrofit.drain` | key | dScopedBuild | `build.unit-pass` drains the legacy a unit touches, in dScopedBuild's row; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) |
| `retrofit.drain-cap` | key | dScopedBuild | dScopedBuild's row drains in hunks under it; the retrofit system is dWitnessedBar's; row dScopedBuild; system retrofit (dWitnessedBar) |
| `retrofit.claim-on-touch` | key | dScopedBuild | dScopedBuild's row claims the baselined map keys a write set holds; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) |
| `retrofit.claim-cap` | key | dScopedBuild | dScopedBuild's row claims under it; the retrofit system is dWitnessedBar's; row dScopedBuild; system retrofit (dWitnessedBar) |
| `retrofit.reconstruct` | key | dTotalRecall | the `adopt` program is dTotalRecall's, and its row governs `adopt.reconstruct` by it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) |
| `retrofit.decisions` | key | dTotalRecall | `adopt.decisions` is dTotalRecall's, routed through it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) |
| `retrofit.practice-pending` | key | dTotalRecall | `adopt.practices` is dTotalRecall's, ruled through it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) |
| `retrofit.cadence` | key | dTendedCadence | dTendedCadence's row files each period's sweep under `retrofit.cadence: hot-first`; the retrofit system is dWitnessedBar's; row dTendedCadence; system retrofit (dWitnessedBar) |
| `retrofit.slot-bytes` | key | dBoundRoles | it caps the work order's legacy slot, which dBoundRoles renders; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) |
| intake | record kind | dWellOiledMachine | its writer is `entry.intake`'s hook (PM-9); dRankedPlan's row also describes that hook, which the re-cut reconciles |
| fork | record kind | dIndexedDesign | a flow record kind (layer-memory `[decisions]`); fork resolution by `design.forks` is dIndexedDesign's, though forks arise in every step |
| lease | record kind | dPlacedRequest | dDeclaredLoop's row built the one lease grammar until NP-24 moved it to dPlacedRequest (revised 2026-10-19, the night pass two, point 4); layer-memory lists the lease among Runtime's kinds |
| mailbox message | record kind | dKeptSession | dDeclaredLoop's row built the mailbox and its message kinds until NP-24 moved them to dKeptSession (revised 2026-10-19, the night pass two, point 4); layer-memory lists it among Runtime's kinds |
| run record | record kind | dWellOiledMachine | `RUN.md` belongs to the unattended run, which the supervisor executes; observability's `observability.run-record` reads it |
| review | record kind | dFairHearing | its writer is `review.report`, the harness's, under the proposal for the breakpoint's items |
| design record | record kind | dTotalRecall | a core memory kind with no writer item; the memory contract declares it |
| backlog row | record kind | dTotalRecall | the ask register's row store; the memory contract declares it |
| ruling | record kind | dTotalRecall | `adopt.practices` writes the ruling records, an item dTotalRecall owns |
| lexicon declaration | record kind | dMindYourWords | layer-memory lists the lexicon as an optional component's kind; dMindYourWords builds the declaration and its packs |

## [namespaces] The namespace rules

The 78 keys that nothing names take their namespace's owner:

| Namespace | Owner | Keys | The owner's row says |
| --- | --- | --- | --- |
| `budgets` | dCalibratedLens | 1 | caps re-derived from evidence and review cost |
| `card` | dDeclaredLoop | 1 | the build's orientation card at level 1 |
| `currency` | dShippedRelease | 2 | the fleet register and currency watch |
| `deploy` | dShippedRelease | 4 | the deploy engine |
| `deps` | dDeclaredLoop | 3 | dependency coordination by the parent's lease |
| `design` | dIndexedDesign | 2 | the derived-READY hand-off; the design index |
| `floor` | dDeclaredLoop | 1 | the guard, the TTY CLI and the default floor |
| `flow` | dDeclaredLoop | 1 | one transition table per level; a default failure route |
| `install` | dShippedRelease | 1 | the deploy engine; the fleet register |
| `kits` | dShippedRelease | 3 | the fleet register and currency watch; the kit factory |
| `landing` | dShippedRelease | 1 | landings ordered through the landing queue it builds |
| `leases` | dDeclaredLoop | 6 | one lease grammar for builds, units and cadence runs |
| `maintain` | dTendedCadence | 10 | the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |
| `observability` | dTendedCadence | 1 | Maintain and the Loop Review delivered as cadence steps of the observability expansion |
| `plan` | dRankedPlan | 4 | the planner and triager role and Plan workflow; rule-based triage |
| `policy` | dDeclaredLoop | 3 | the guard, the TTY CLI and the default floor; policy at govkit intake |
| `release` | dShippedRelease | 1 | promotion after landing through environments |
| `reuse` | dTotalRecall | 1 | reuse entries proposed with their build through the instruction command |
| `review` | dCalibratedLens | 13 | review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |
| `runtime` | dWellOiledMachine | 9 | the supervisor, act sessions and the one enforcement surface |
| `tests` | dWitnessedBar | 3 | the product-test contract with runner adapters |
| `transitions` | dDeclaredLoop | 1 | the transition record three ways |
| `verdict` | dWitnessedBar | 6 | the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |

## [items] Items

| Item | Step | Owner | Evidence | Why | Look |
|---|---|---|---|---|---|
| `entry.intake` | entry | dWellOiledMachine | decided | PM-9: the intake hook stays dWellOiledMachine's, with `gap-rt-14`; dRankedPlan's row also describes the hook, which the re-cut reconciles | yes |
| `entry.orient` | entry | dDeclaredLoop | decided | PM-9 |  |
| `entry.place` | entry | dDeclaredLoop | decided | PM-9 |  |
| `entry.place-check` | entry | dDeclaredLoop | decided | PM-9 |  |
| `entry.place-owner` | entry | dDeclaredLoop | decided | PM-9 |  |
| `entry.claim` | entry | dDeclaredLoop | decided | PM-9 |  |
| `plan.input` | plan | dRankedPlan | stage | — |  |
| `plan.dedupe` | plan | dRankedPlan | stage | — |  |
| `plan.triage-rule` | plan | dRankedPlan | stage | — |  |
| `plan.triage-judge` | plan | dRankedPlan | stage | — |  |
| `plan.record` | plan | dRankedPlan | stage | — |  |
| `plan.research` | plan | dRankedPlan | stage | — |  |
| `plan.place` | plan | dRankedPlan | stage | — |  |
| `plan.lease` | plan | dRankedPlan | stage | — |  |
| `plan.recommend` | plan | dRankedPlan | stage | — |  |
| `plan.reason` | plan | dRankedPlan | stage | — |  |
| `plan.exit` | plan | dRankedPlan | stage | — |  |
| `design.input` | design | dIndexedDesign | stage | — |  |
| `design.reentry` | design | dIndexedDesign | stage | row dIndexedDesign |  |
| `design.inventory` | design | dIndexedDesign | stage | — |  |
| `design.seams` | design | dIndexedDesign | stage | — |  |
| `design.decompose` | design | dIndexedDesign | stage | — |  |
| `design.research` | design | dIndexedDesign | stage | — |  |
| `design.overlaps` | design | dIndexedDesign | stage | — |  |
| `design.unit-spec` | design | dIndexedDesign | stage | — |  |
| `design.recommend` | design | dIndexedDesign | stage | — |  |
| `design.reason` | design | dIndexedDesign | stage | — |  |
| `design.ready` | design | dIndexedDesign | stage | — |  |
| `design.exit` | design | dIndexedDesign | stage | — |  |
| `build.base` | build | dScopedBuild | stage | — |  |
| `build.unit-lease` | build | dScopedBuild | stage | — |  |
| `build.unit-pass` | build | dScopedBuild | stage | row dScopedBuild |  |
| `build.acceptance` | build | dScopedBuild | stage | — |  |
| `build.scope` | build | dScopedBuild | stage | row dScopedBuild |  |
| `build.recommend` | build | dScopedBuild | stage | — |  |
| `build.ratify` | build | dScopedBuild | stage | — |  |
| `build.distill` | build | dScopedBuild | stage | — |  |
| `build.core` | build | dScopedBuild | stage | — |  |
| `build.exit` | build | dScopedBuild | stage | — |  |
| `test.merge` | test | dWitnessedBar | stage | — |  |
| `test.select` | test | dWitnessedBar | stage | — |  |
| `test.verdict` | test | dWitnessedBar | stage | — |  |
| `test.route` | test | dWitnessedBar | stage | — |  |
| `test.attribute` | test | dWitnessedBar | stage | — |  |
| `test.flakes` | test | dWitnessedBar | stage | — |  |
| `test.seen-red` | test | dWitnessedBar | stage | — |  |
| `test.recommend` | test | dWitnessedBar | stage | — |  |
| `test.reason` | test | dWitnessedBar | stage | — |  |
| `test.exit` | test | dWitnessedBar | stage | — |  |
| `deploy.current` | deploy | dShippedRelease | stage | — |  |
| `deploy.mandate` | deploy | dShippedRelease | stage | — |  |
| `deploy.parents` | deploy | dShippedRelease | stage | — |  |
| `deploy.land` | deploy | dShippedRelease | stage | — |  |
| `deploy.core` | deploy | dShippedRelease | stage | — |  |
| `deploy.record` | deploy | dShippedRelease | stage | — |  |
| `deploy.distill` | deploy | dShippedRelease | stage | — |  |
| `deploy.recommend` | deploy | dShippedRelease | stage | — |  |
| `deploy.notify` | deploy | dShippedRelease | stage | — |  |
| `deploy.released` | deploy | dShippedRelease | stage | — |  |
| `deploy.snapshot` | deploy | dShippedRelease | stage | — |  |
| `deploy.unlease` | deploy | dShippedRelease | stage | — |  |
| `deploy.close` | deploy | dShippedRelease | stage | — |  |
| `review.trigger` | breakpoint | dCalibratedLens | judgment | dCalibratedLens's row: review by policy per stage, breakpoints placeable at any item boundary | yes |
| `review.pin` | breakpoint | dFairHearing | row | dFairHearing's row cites it, where the stage rule would give it to dCalibratedLens; row dFairHearing | yes |
| `review.lens` | breakpoint | dFairHearing | judgment | the panel's lenses run in the review harness; dCalibratedLens's row draws each stage's lenses from dFairHearing's catalogue | yes |
| `review.refute` | breakpoint | dFairHearing | judgment | dFairHearing's row: skeptic batches sorted by cited address | yes |
| `review.report` | breakpoint | dFairHearing | row | dFairHearing's row cites it, where the stage rule would give it to dCalibratedLens; row dFairHearing | yes |
| `review.dispose` | breakpoint | dCalibratedLens | stage | row dCalibratedLens |  |
| `review.fold` | breakpoint | dCalibratedLens | judgment | it disposes the confirmed findings into the unbuilt specs, after `review.dispose`, which dCalibratedLens's row holds; the spec writer acts in it | yes |
| `review.cost` | breakpoint | dCalibratedLens | stage | row dCalibratedLens |  |
| `life.request` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `life.quiesce` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `life.notify` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `life.snapshot` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `life.unlease` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `life.close` | lifecycle | dWellOiledMachine | decided | flow-steps `[lifecycle]`: Runtime executes the owner's controls (dWellOiledMachine, RT-3) |  |
| `adopt.census` | adopt | dTotalRecall | row | row dTotalRecall |  |
| `test.seed` | adopt | dWitnessedBar | row | dWitnessedBar's row builds it; dShippedRelease's row cites it as what its install and update hooks call; row dWitnessedBar,dShippedRelease |  |
| `adopt.practices` | adopt | dTotalRecall | row | row dTotalRecall |  |
| `adopt.decisions` | adopt | dTotalRecall | row | row dTotalRecall |  |
| `adopt.reconstruct` | adopt | dTotalRecall | row | row dTotalRecall |  |

## [keys] Policy keys

| Node | Owner | Evidence | Why | Look |
|---|---|---|---|---|
| `preset` | dDeclaredLoop | judgment | dDeclaredLoop's row builds the named presets and their completeness check; dFairHearing's row cites `preset` as the review harness's own argument, a homonym; row dFairHearing | yes |
| `charter.override` | dOrderedCharter | row | row dOrderedCharter |  |
| `charter.practices` | dOrderedCharter | row | row dOrderedCharter |  |
| `core.bypass` | dOrderedCharter | row-wildcard | row-wildcard dOrderedCharter |  |
| `core.exceptions` | dOrderedCharter | row-wildcard | row-wildcard dOrderedCharter |  |
| `design.forks` | dIndexedDesign | row | row dIndexedDesign |  |
| `design.reentry` | dIndexedDesign | row | row dIndexedDesign |  |
| `autonomy` | dCalibratedLens | row | row dCalibratedLens |  |
| `policy.guard` | dDeclaredLoop | namespace | dDeclaredLoop's row: the guard, the TTY CLI and the default floor; policy at govkit intake |  |
| `policy.proof` | dDeclaredLoop | namespace | dDeclaredLoop's row: the guard, the TTY CLI and the default floor; policy at govkit intake |  |
| `floor` | dDeclaredLoop | namespace | dDeclaredLoop's row: the guard, the TTY CLI and the default floor |  |
| `hooks.bypass` | dWitnessedBar | judgment | whether the bar's hooks may be bypassed; dWitnessedBar's row records bypasses and owns the hook-read verdict, and the enforcement surface is dWellOiledMachine's | yes |
| `transitions.record` | dDeclaredLoop | namespace | dDeclaredLoop's row: the transition record three ways |  |
| `leases` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `leases.granularity` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `leases.renewal` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `leases.expiry-hours` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `leases.overlap` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `leases.offline` | dDeclaredLoop | namespace | dDeclaredLoop's row: one lease grammar for builds, units and cadence runs |  |
| `deps.coordination` | dDeclaredLoop | namespace | dDeclaredLoop's row: dependency coordination by the parent's lease |  |
| `deps.early-build` | dDeclaredLoop | namespace | dDeclaredLoop's row: dependency coordination by the parent's lease |  |
| `deps.messaging` | dDeclaredLoop | namespace | dDeclaredLoop's row: dependency coordination by the parent's lease |  |
| `landing.order` | dShippedRelease | namespace | dShippedRelease's row: landings ordered through the landing queue it builds |  |
| `card.follows` | dDeclaredLoop | namespace | dDeclaredLoop's row: the build's orientation card at level 1 |  |
| `placement` | dRankedPlan | row | row dRankedPlan |  |
| `placement.check` | dRankedPlan | judgment | dRankedPlan's row defines placement and its check; dBoundRoles's driver only runs it; row dBoundRoles,dRankedPlan | yes |
| `kickoff.runs` | dRankedPlan | row | row dRankedPlan |  |
| `card.store` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `card.snapshot` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `actions.free` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `resume.partial` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `resume.context` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `orient.budget` | dDeclaredLoop | judgment | dDeclaredLoop's row records orientation cost per stage, which the key's values switch | yes |
| `driver.reads` | dBoundRoles | row | row dBoundRoles |  |
| `prompts.author` | dBoundRoles | row | row dBoundRoles |  |
| `roles.retries` | dBoundRoles | row | row dBoundRoles |  |
| `roles.no-spawn` | dBoundRoles | row | row dBoundRoles |  |
| `roles.trust` | dBoundRoles | row | row dBoundRoles |  |
| `roles.answered-calls` | dBoundRoles | row | row dBoundRoles |  |
| `roles.verifier-context` | dBoundRoles | row | row dBoundRoles |  |
| `roles.on-contradiction` | dBoundRoles | row | row dBoundRoles |  |
| `reuse.delivery` | dTotalRecall | row | row dTotalRecall |  |
| `reuse.propose` | dTotalRecall | namespace | dTotalRecall's row: reuse entries proposed with their build through the instruction command |  |
| `annotations.grammar` | dTotalRecall | row | row dTotalRecall; system annotations (dTotalRecall) |  |
| `builds.agent-root` | dTotalRecall | row | row dTotalRecall |  |
| `asks.acceptance` | dTotalRecall | row | row dTotalRecall |  |
| `decisions.major` | dTotalRecall | judgment | it says who declares a decision major for the log, dTotalRecall's; `build.ratify`, dScopedBuild's, rules on forks already classed | yes |
| `builds.slug-words` | dTotalRecall | row | row dTotalRecall |  |
| `builds.slug-style` | dTotalRecall | row | row dTotalRecall |  |
| `builds.slug-date` | dTotalRecall | row | row dTotalRecall |  |
| `lexicon.pin` | dMindYourWords | row | row dMindYourWords |  |
| `lexicon.forced` | dMindYourWords | row | row dMindYourWords |  |
| `lexicon.at-commit` | dMindYourWords | row | row dMindYourWords |  |
| `lexicon.drift` | dMindYourWords | row | row dMindYourWords |  |
| `lexicon.packs` | dMindYourWords | row | row dMindYourWords |  |
| `review.opt-in` | dFairHearing | row | row dFairHearing |  |
| `runtime.spawn-backend` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.relaunch` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.act-ceiling` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.hold-ceiling` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.hook-failure` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.attended-judge` | dWellOiledMachine | row | row dWellOiledMachine |  |
| `runtime.attended-allowance` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.harnesses` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.journal` | dWellOiledMachine | row | row dWellOiledMachine |  |
| `runtime.secret-home` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `runtime.secret-scan` | dWellOiledMachine | namespace | dWellOiledMachine's row: the supervisor, act sessions and the one enforcement surface |  |
| `plan.ratification` | dRankedPlan | row | row dRankedPlan |  |
| `run.host` | dWellOiledMachine | row | row dWellOiledMachine |  |
| `notify.owner` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `notify.channel` | dWellOiledMachine | judgment | notification adapters are a Runtime point (layer-runtime `[extend]`) | yes |
| `run.on-owner-question` | dBoundRoles | row | row dBoundRoles |  |
| `deps.landing` | dShippedRelease | row | row dShippedRelease |  |
| `mailbox.reads` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `review.follow-up` | dCalibratedLens | row | row dCalibratedLens |  |
| `prompts.batch` | dBoundRoles | row | row dBoundRoles |  |
| `context.on-full` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `context.threshold` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `card.pointers` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `notices.record` | dBoundRoles | row | row dBoundRoles |  |
| `instructions.checks` | dOrderedCharter | row | row dOrderedCharter |  |
| `instructions.edit` | dOrderedCharter | judgment | the instruction manifest and its guarded write command are dOrderedCharter's; dTotalRecall and dMindYourWords route their changes through it; row dOrderedCharter,dTotalRecall,dMindYourWords | yes |
| `instructions.proof` | dOrderedCharter | row | row dOrderedCharter |  |
| `review.breakpoints` | dCalibratedLens | row | row dCalibratedLens |  |
| `deps.on-parent-withdrawn` | dDeclaredLoop | row | row dDeclaredLoop |  |
| `review.design.rounds` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.design.round-count` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.unverified` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.unclassed` | dFairHearing | row | row dFairHearing |  |
| `flow.route-backs` | dDeclaredLoop | namespace | dDeclaredLoop's row: one transition table per level; a default failure route |  |
| `policy.on-missing-expansion` | dDeclaredLoop | namespace | dDeclaredLoop's row: the guard, the TTY CLI and the default floor; policy at govkit intake |  |
| `tests.without-cadence` | dWitnessedBar | namespace | dWitnessedBar's row: the product-test contract with runner adapters |  |
| `verdict` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `verdict.blocks` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `verdict.held` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `verdict.flakes` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `tests.product` | dWitnessedBar | namespace | dWitnessedBar's row: the product-test contract with runner adapters |  |
| `tests.landing-levels` | dWitnessedBar | namespace | dWitnessedBar's row: the product-test contract with runner adapters |  |
| `verdict.tree` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `verdict.red-route` | dWitnessedBar | namespace | dWitnessedBar's row: the runner-written verdict; attribution deciding what blocks; held legs by policy; flake quarantine |  |
| `verdict.remote.trust` | dWitnessedBar | judgment | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point | yes |
| `verdict.remote.pin-scope` | dWitnessedBar | judgment | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point | yes |
| `verdict.remote.pin` | dWitnessedBar | judgment | the verdict engine reads it; a remote verdict arrives through an integrations adapter at Test's verdict-backend point | yes |
| `plan.authority` | dRankedPlan | namespace | dRankedPlan's row: the planner and triager role and Plan workflow; rule-based triage |  |
| `plan.unplaced` | dRankedPlan | namespace | dRankedPlan's row: the planner and triager role and Plan workflow; rule-based triage |  |
| `plan.triage` | dRankedPlan | namespace | dRankedPlan's row: the planner and triager role and Plan workflow; rule-based triage |  |
| `plan.kickoff` | dRankedPlan | namespace | dRankedPlan's row: the planner and triager role and Plan workflow; rule-based triage |  |
| `design.handoff` | dIndexedDesign | namespace | dIndexedDesign's row: the derived-READY hand-off; the design index |  |
| `design.overlap` | dIndexedDesign | namespace | dIndexedDesign's row: the derived-READY hand-off; the design index |  |
| `build.scope` | dScopedBuild | row | row dScopedBuild |  |
| `build.worktree` | dWellOiledMachine | row | row dWellOiledMachine |  |
| `deploy.runs` | dShippedRelease | namespace | dShippedRelease's row: the deploy engine |  |
| `deploy.promotion` | dShippedRelease | namespace | dShippedRelease's row: the deploy engine |  |
| `deploy.on-verify-fail` | dShippedRelease | namespace | dShippedRelease's row: the deploy engine |  |
| `deploy.currency` | dShippedRelease | namespace | dShippedRelease's row: the deploy engine |  |
| `currency.max-behind` | dShippedRelease | namespace | dShippedRelease's row: the fleet register and currency watch |  |
| `currency.on-behind` | dShippedRelease | namespace | dShippedRelease's row: the fleet register and currency watch |  |
| `install.from` | dShippedRelease | namespace | dShippedRelease's row: the deploy engine; the fleet register |  |
| `build.closes` | dShippedRelease | judgment | `deploy.released` reads it, and Deploy holds the close; dDeclaredLoop's row cites it only as the presets check's example; row dDeclaredLoop | yes |
| `build.release-hold` | dShippedRelease | judgment | it says what waits at `deploy.released` (RH-1), a Deploy item; dWellOiledMachine's sweep only raises a wait past `build.release-ceiling` | yes |
| `build.release-ceiling` | dShippedRelease | judgment | the release wait's declared deadline, whose arm dShippedRelease builds, dWellOiledMachine's sweep being generic over each wait's deadline (moved by the owner's FK-2-3, 2026-10-20) | yes |
| `kits.cadence` | dShippedRelease | namespace | dShippedRelease's row: the fleet register and currency watch; the kit factory |  |
| `kits.host` | dShippedRelease | namespace | dShippedRelease's row: the fleet register and currency watch; the kit factory |  |
| `kits.watch-cadence` | dShippedRelease | namespace | dShippedRelease's row: the fleet register and currency watch; the kit factory |  |
| `release.environments` | dShippedRelease | namespace | dShippedRelease's row: promotion after landing through environments |  |
| `integrations.tracker` | dTotalRecall | judgment | it mirrors the ask register out; the register is dTotalRecall's, and the mirror is an integrations adapter at its point | yes |
| `maintain.host` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.cadence` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.fixes` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.on-breach` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.events` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.reading-tree` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.node-readings` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.reading-admission` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.dead-after` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `maintain.record-when` | dTendedCadence | namespace | dTendedCadence's row: the Maintain run as its step checklist; the cadence; the safe-fix set; detectors with owners |  |
| `observability.run-record` | dTendedCadence | namespace | dTendedCadence's row: Maintain and the Loop Review delivered as cadence steps of the observability expansion |  |
| `patch.ratify` | dPlacedRequest | judgment | `entry.claim`, dPlacedRequest's own item, reads it for every patch at entry, and its other readers, `deploy.mandate` and `maintain.patch`'s route, descend from dPlacedRequest (moved from dTendedCadence by the owner's FK-6-2, 2026-10-20) | yes |
| `review.<stage>` | dCalibratedLens | row | row dCalibratedLens |  |
| `review.<stage>.effort` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.recommendation` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.build.when` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.findings` | dScopedBuild | row | row dScopedBuild |  |
| `review.blocks` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.left-shift` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.recommendation.source` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.loop.cadence` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.loop.retire` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.loop.window-days` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `review.loop.catch-source` | dCalibratedLens | namespace | dCalibratedLens's row: review by policy per stage and effort; the stage-exit recommendation; the weekly Loop Review |  |
| `budgets.*` | dGroundRules | judgment | dGroundRules's `budgets.enforce` clause makes the key each cap's one declaration, and dCalibratedLens's row re-derives the values (moved from dCalibratedLens by the owner's FK-1-3, 2026-10-20) | yes |
| `tags.slice` | dOrderedCharter | system | system tags (dOrderedCharter) |  |
| `tags.retired-cites` | dOrderedCharter | system | system tags (dOrderedCharter) |  |
| `tags.positional` | dOrderedCharter | system | system tags (dOrderedCharter) |  |
| `tags.bare-refs` | dOrderedCharter | system | system tags (dOrderedCharter) |  |
| `annotations.lookup` | dTotalRecall | system | system annotations (dTotalRecall) |  |
| `annotations.budget` | dTotalRecall | system | system annotations (dTotalRecall) |  |
| `annotations.resolve-scope` | dTotalRecall | system | system annotations (dTotalRecall) |  |
| `annotations.delivery` | dBoundRoles | judgment | it switches the work order's code-notes slot, which dBoundRoles renders; the annotations system is dTotalRecall's; system annotations (dTotalRecall) | yes |
| `instructions.slices` | dOrderedCharter | system | system instruction-writing (dOrderedCharter) |  |
| `instructions.legacy` | dOrderedCharter | system | system instruction-writing (dOrderedCharter) |  |
| `instructions.task-charter` | dOrderedCharter | system | system instruction-writing (dOrderedCharter) |  |
| `review.twin` | dFairHearing | judgment | dFairHearing's row runs the twin merge `review.twin` opts in (RS-1); the role-shapes system, dBoundRoles's, declares the `twin` shape kind; row dFairHearing; system role-shapes (dBoundRoles) | yes |
| `roles.shape-enforce` | dBoundRoles | system | system role-shapes (dBoundRoles) |  |
| `roles.orientation.house-index` | dBoundRoles | system | system role-shapes (dBoundRoles) |  |
| `memory.default-load` | dTotalRecall | judgment | dTotalRecall's row holds the default load of the charter and the card; dWellOiledMachine's session-start hook performs the load; system memory-structure (dTotalRecall),project-map (dTotalRecall) | yes |
| `memory.load-budget` | dTotalRecall | row | row dTotalRecall; system memory-structure (dTotalRecall) |  |
| `memory.item-budget` | dTotalRecall | judgment | the read budget per role item is dTotalRecall's; dCalibratedLens derives one of its values, `measured`; row dTotalRecall,dCalibratedLens; system memory-structure (dTotalRecall) | yes |
| `memory.over-budget` | dTotalRecall | system | system memory-structure (dTotalRecall) |  |
| `memory.project-map` | dBoundRoles | judgment | it selects the roles whose work orders carry the map slot, which dBoundRoles declares; the project-map system is dTotalRecall's; row dBoundRoles; system project-map (dTotalRecall) | yes |
| `memory.map-budget` | dTotalRecall | row | row dTotalRecall; system project-map (dTotalRecall) |  |
| `memory.map-overflow` | dTotalRecall | system | system project-map (dTotalRecall) |  |
| `memory.map-unfold` | dBoundRoles | judgment | the unfolds render in the work order's map slot, dBoundRoles's; the project-map system is dTotalRecall's; system project-map (dTotalRecall) | yes |
| `memory.map-purpose` | dTotalRecall | judgment | the map and its purposeless-node population are dTotalRecall's; dOrderedCharter adds the namespace rows' purpose-source field the key reads; row dOrderedCharter,dTotalRecall; system project-map (dTotalRecall) | yes |
| `memory.legacy-anchors` | dTotalRecall | system | system memory-structure (dTotalRecall) |  |
| `memory.superseded-slices` | dTotalRecall | system | system memory-structure (dTotalRecall) |  |
| `retrofit.drain` | dScopedBuild | judgment | `build.unit-pass` drains the legacy a unit touches, in dScopedBuild's row; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) | yes |
| `retrofit.drain-cap` | dScopedBuild | judgment | dScopedBuild's row drains in hunks under it; the retrofit system is dWitnessedBar's; row dScopedBuild; system retrofit (dWitnessedBar) | yes |
| `retrofit.claim-on-touch` | dScopedBuild | judgment | dScopedBuild's row claims the baselined map keys a write set holds; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) | yes |
| `retrofit.claim-cap` | dScopedBuild | judgment | dScopedBuild's row claims under it; the retrofit system is dWitnessedBar's; row dScopedBuild; system retrofit (dWitnessedBar) | yes |
| `retrofit.widen` | dWitnessedBar | system | system retrofit (dWitnessedBar) |  |
| `retrofit.unseeded` | dWitnessedBar | system | system retrofit (dWitnessedBar) |  |
| `retrofit.reconstruct` | dTotalRecall | judgment | the `adopt` program is dTotalRecall's, and its row governs `adopt.reconstruct` by it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) | yes |
| `retrofit.decisions` | dTotalRecall | judgment | `adopt.decisions` is dTotalRecall's, routed through it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) | yes |
| `retrofit.practice-pending` | dTotalRecall | judgment | `adopt.practices` is dTotalRecall's, ruled through it; the retrofit system is dWitnessedBar's; row dTotalRecall; system retrofit (dWitnessedBar) | yes |
| `retrofit.cadence` | dTendedCadence | judgment | dTendedCadence's row files each period's sweep under `retrofit.cadence: hot-first`; the retrofit system is dWitnessedBar's; row dTendedCadence; system retrofit (dWitnessedBar) | yes |
| `retrofit.slot-bytes` | dBoundRoles | judgment | it caps the work order's legacy slot, which dBoundRoles renders; the retrofit system is dWitnessedBar's; system retrofit (dWitnessedBar) | yes |

## [points] Points

| Node | Owner | Evidence | Why | Look |
|---|---|---|---|---|
| `actor-kinds` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `command-adapters` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `spawn-backends` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `role-harnesses` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `hook-packs` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `harness-adapters` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `host-adapters` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `notification-adapters` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `journal-readers` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |
| `cadence-items` | dWellOiledMachine | layer | layer-runtime `[extend]` declares it a Runtime point, and the chain table gives the Runtime stage to dWellOiledMachine |  |

## [tag-namespaces] Tag namespaces

| Node | Owner | Evidence | Why | Look |
|---|---|---|---|---|
| `reader` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `level` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `layer` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `step` | dDeclaredLoop | declared | the systems record's Owners bullet |  |
| `item` | dDeclaredLoop | declared | the systems record's Owners bullet |  |
| `role` | dBoundRoles | declared | the systems record's Owners bullet |  |
| `policy` | dDeclaredLoop | declared | the systems record's Owners bullet |  |
| `practice` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `principle` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `kind` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `record` | dTotalRecall | declared | the systems record's Owners bullet |  |
| `kit` | dOrderedCharter | row | dOrderedCharter's row: the namespaced tag system (reader, level, layer, ..., kit); the Owners bullet defaulted it |  |
| `section` | dTotalRecall | declared | the systems record's Owners bullet |  |
| `doc` | dOrderedCharter | declared | the systems record's Owners bullet |  |
| `unit` | dOrderedCharter | declared | the systems record's Owners bullet |  |
| `field` | dBoundRoles | declared | the systems record's Owners bullet |  |
| `leg` | dWitnessedBar | declared | the systems record's Owners bullet |  |
| `check` | dWitnessedBar | declared | the systems record's Owners bullet |  |
| `point` | dWellOiledMachine | declared | the systems record's Owners bullet |  |
| `hook` | dWellOiledMachine | declared | the systems record's Owners bullet |  |
| `command` | dDeclaredLoop | declared | the systems record's Owners bullet |  |
| `pack` | dWitnessedBar | declared | the systems record's Owners bullet |  |
| `feature` | dTotalRecall | declared | the systems record's Owners bullet |  |
| `class` | dTotalRecall | declared | the systems record's Owners bullet |  |
| `marker` | dTotalRecall | declared | the systems record's Owners bullet |  |

## [systems] Systems

| Node | Owner | Evidence | Why | Look |
|---|---|---|---|---|
| `tags` | dOrderedCharter | declared | its record's owners |  |
| `annotations` | dTotalRecall | declared | its record's owners |  |
| `instruction-writing` | dOrderedCharter | declared | its record's owners |  |
| `role-shapes` | dBoundRoles | declared | its record's owners |  |
| `memory-structure` | dTotalRecall | declared | its record's owners |  |
| `retrofit` | dWitnessedBar | declared | its record's owners |  |
| `project-map` | dTotalRecall | declared | its record's owners |  |

## [record-kinds] Record kinds

| Node | Owner | Evidence | Why | Look |
|---|---|---|---|---|
| intake | dWellOiledMachine | decided | its writer is `entry.intake`'s hook (PM-9); dRankedPlan's row also describes that hook, which the re-cut reconciles | yes |
| card | dDeclaredLoop | row | the build's orientation card at level 1, its stores and snapshot |  |
| plan | dRankedPlan | stage | its writer is `plan.record` |  |
| dupes | dRankedPlan | stage | its writer is `plan.dedupe` |  |
| seams | dIndexedDesign | stage | its writer is `design.seams` |  |
| feature design | dIndexedDesign | stage | its writer is `design.decompose` |  |
| spec | dIndexedDesign | stage | its writer is `design.unit-spec`; the spec redesigned as a structured, tagged contract |  |
| fork | dIndexedDesign | judgment | a flow record kind (layer-memory `[decisions]`); fork resolution by `design.forks` is dIndexedDesign's, though forks arise in every step | yes |
| acceptance | dScopedBuild | stage | its writer is `build.acceptance` |  |
| scope | dScopedBuild | stage | its writer is `build.scope` |  |
| verdict | dWitnessedBar | stage | its writer is `test.verdict` |  |
| attribution | dWitnessedBar | stage | its writer is `test.attribute` |  |
| flake | dWitnessedBar | stage | its writer is `test.flakes`; flake quarantine |  |
| landing | dShippedRelease | row | the landing record; its writer is `deploy.record` |  |
| transition | dDeclaredLoop | row | the transition record three ways; every step's exit item writes it |  |
| lease | dPlacedRequest | judgment | dPlacedRequest's row builds the one lease grammar since NP-24 (revised 2026-10-19, the night pass two, point 4); layer-memory lists the lease among Runtime's kinds | yes |
| mailbox message | dKeptSession | judgment | dKeptSession's row builds the mailbox and its message kinds since NP-24 (revised 2026-10-19, the night pass two, point 4); layer-memory lists it among Runtime's kinds | yes |
| return | dWellOiledMachine | row | the persisted-return store, keyed per spawn site |  |
| act | dWellOiledMachine | row | one act session per role act; act binding and the epoch check |  |
| session binding | dWellOiledMachine | row | sessions bound on every source |  |
| journal | dWellOiledMachine | row | the journal grammar moved into the core |  |
| run record | dWellOiledMachine | judgment | `RUN.md` belongs to the unattended run, which the supervisor executes; observability's `observability.run-record` reads it | yes |
| work order | dBoundRoles | row | the work order rendered per item |  |
| review | dFairHearing | judgment | its writer is `review.report`, the harness's, under the proposal for the breakpoint's items | yes |
| research return | dTotalRecall | row | the research view over the research-return kind and its dated backfill; `plan.research` and `design.research` write it |  |
| design record | dTotalRecall | judgment | a core memory kind with no writer item; the memory contract declares it | yes |
| ask | dTotalRecall | row | the ask kind's acceptance at filing |  |
| backlog row | dTotalRecall | judgment | the ask register's row store; the memory contract declares it | yes |
| decision | dTotalRecall | row | decisions split by kind, the major-decision log |  |
| gotcha | dTotalRecall | row | gotchas handed by write set |  |
| dossier | dTotalRecall | row | dossiers anchored to symbol keys |  |
| symbols | dTotalRecall | row | the caller map |  |
| callers | dTotalRecall | row | the caller map |  |
| annotation index | dTotalRecall | row | the generated annotation index and its resolve check |  |
| recall index | dTotalRecall | row | memory-recall narrowed to a record finder |  |
| baseline | dTotalRecall | row | retrofit's `baseline` and `census` record kinds |  |
| census | dTotalRecall | row | retrofit's `baseline` and `census` record kinds; `adopt.census` writes it |  |
| ruling | dTotalRecall | judgment | `adopt.practices` writes the ruling records, an item dTotalRecall owns | yes |
| shape-run | dTotalRecall | row | the shape-run kind |  |
| maintenance record | dTendedCadence | row | the maintenance record |  |
| lexicon declaration | dMindYourWords | judgment | layer-memory lists the lexicon as an optional component's kind; dMindYourWords builds the declaration and its packs | yes |

## [fold] What lands once the table is approved

- **The owner fields** (PM-8):
  - flow-steps' item tables gain an `Owner` column;
  - v2's catalogue gains an `Owner` column, and so does layer-runtime `[extend]`;
  - the systems record's Owners bullet names the seven namespaces dOrderedCharter registers;
  - layer-memory `[contract]` gains the record-kind table.
- **The generator reads those fields only.** It infers no owner from a stage, a literal or a default,
  and derives a step's owners from its items, so a step can have several. Its owner check covers the six
  kinds, is seen red on a planted orphan, and fills the header's `unowned`.
- **The atlas, the role matrix and the preset check** read the new columns.
- **The re-cut** reconciles the chain rows with the table. A row that describes work the table gives to
  another build is rewritten to call it. dRankedPlan's prompt-submit hook is the first case: the intake
  hook is dWellOiledMachine's under PM-9.

## [instrument] The proposal, as run

It ran from the worktree root on a clean tree at `248ef556d`, reading the map's node table and v2:

```python
"""PM-10's ownership table: a proposed owning build for every item, policy key, point, tag namespace, system and
record kind, each with its evidence. A node's owner is the build that implements the behaviour the node names
or switches; a caller or a reader of it is not its owner.

Usage: python proposal.py <out-dir>   (from the worktree root)

Evidence, strongest first:
- decided: an owner's answer (PM-9) or a step section's own statement (flow-steps [lifecycle], RT-3);
- stage: the chain table gives the item's step to its stage's build;
- row: a chain row cites the node by tag in backticks, alone or with a value (`retrofit.cadence: hot-first`);
- row-wildcard: a chain row cites the node's namespace by a wildcard (`core.*`, `builds.slug-*`);
- system: a system's design table lists the key, and the system's record names its owner;
- declared: the systems record's Owners bullet registers the tag namespace with a build;
- layer: the node is a point of a layer, and the chain table gives the layer's stage to one build;
- namespace: no evidence names the key itself; its namespace's work sits in one chain row, quoted;
- judgment: the evidence disagrees or is absent, and the proposal says why. Every judgment row is flagged.
A row whose evidence disagrees with its proposal is flagged as well.
"""
import importlib.util
import json
import pathlib
import re
import sys

B = "memory/builds/dClosedLoop/build/"
OUT = pathlib.Path(sys.argv[1])


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mp = load("projectmap", B + "2026-10-17-build-PLAY-dClosedLoop-1-map.py")
A, ns = mp.derive()
v2 = open(B + "2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
rows = dict(re.findall(r"^\| (d[A-Z][a-z]+[A-Z]\w+) \|(.*)$", v2, flags=re.M))
assert len(rows) == 15, len(rows)
STAGE = {c["stage"]: c["build"] for c in A["chain"]}


def cites(tag):
    """The chain rows that cite tag in backticks, bare or followed by a value."""
    pat = re.compile(r"`" + re.escape(tag) + r"(?=`|:|=|\s)")
    return [b for b, r in rows.items() if pat.search(r)]


def wildcard(tag):
    """The chain rows whose backticked wildcard (`ns.*`, `prefix-*`) covers tag."""
    hit = []
    for b, r in rows.items():
        for w in re.findall(r"`([a-z][a-z0-9.-]*)\*`", r):
            if tag.startswith(w) and tag != w:
                hit.append(b)
                break
    return hit


# Each system's keys: the backticked first cells of the tables in its design section.
sys_owner = {n["key"]: (dict(n["rels"]).get("owner") or [""])[0] for n in ns["system"]}
sys_keys = {}
sysrec = open(B + "2026-10-16-build-PLAY-dClosedLoop-1-systems.md", encoding="utf-8").read()
for m in re.finditer(r"^### \[design-([a-z-]+)\] [^\n]+\n(.*?)(?=^### |^## |\Z)", sysrec, flags=re.M | re.S):
    for k in re.findall(r"^\s*\| `([a-z]+\.[a-z0-9.<>-]+)` \|", m.group(2), flags=re.M):
        sys_keys.setdefault(k, []).append(m.group(1))
for name, rel in (("retrofit", "2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md"),
                  ("project-map", "2026-10-17-build-PLAY-dClosedLoop-1-project-map.md")):
    body = open(B + rel, encoding="utf-8").read()
    design = body.split("\n## [design]", 1)[1].split("\n## ", 1)[0] if "\n## [design]" in body else ""
    for k in re.findall(r"^\| `([a-z]+\.[a-z0-9.<>-]+)` \|", design, flags=re.M):
        sys_keys.setdefault(k, []).append(name)

# ------------------------------------------------------------------------------------------------ the judgments
ITEM_JUDGED = {
    "review.lens": ("dFairHearing", "the panel's lenses run in the review harness; dCalibratedLens's row draws "
                    "each stage's lenses from dFairHearing's catalogue"),
    "review.refute": ("dFairHearing", "dFairHearing's row: skeptic batches sorted by cited address"),
    "review.trigger": ("dCalibratedLens", "dCalibratedLens's row: review by policy per stage, breakpoints "
                       "placeable at any item boundary"),
    "review.fold": ("dCalibratedLens", "it disposes the confirmed findings into the unbuilt specs, after "
                    "`review.dispose`, which dCalibratedLens's row holds; the spec writer acts in it"),
}
KEY_JUDGED = {
    "preset": ("dDeclaredLoop", "dDeclaredLoop's row builds the named presets and their completeness check; "
               "dFairHearing's row cites `preset` as the review harness's own argument, a homonym"),
    "build.closes": ("dShippedRelease", "`deploy.released` reads it, and Deploy holds the close; dDeclaredLoop's "
                     "row cites it only as the presets check's example"),
    "build.release-hold": ("dShippedRelease", "it says what waits at `deploy.released` (RH-1), a Deploy item; "
                           "dWellOiledMachine's sweep only raises a wait past `build.release-ceiling`"),
    "placement.check": ("dRankedPlan", "dRankedPlan's row defines placement and its check; dBoundRoles's driver "
                        "only runs it"),
    "instructions.edit": ("dOrderedCharter", "the instruction manifest and its guarded write command are "
                          "dOrderedCharter's; dTotalRecall and dMindYourWords route their changes through it"),
    "memory.item-budget": ("dTotalRecall", "the read budget per role item is dTotalRecall's; dCalibratedLens "
                           "derives one of its values, `measured`"),
    "memory.map-purpose": ("dTotalRecall", "the map and its purposeless-node population are dTotalRecall's; "
                           "dOrderedCharter adds the namespace rows' purpose-source field the key reads"),
    "memory.project-map": ("dBoundRoles", "it selects the roles whose work orders carry the map slot, which "
                           "dBoundRoles declares; the project-map system is dTotalRecall's"),
    "memory.map-unfold": ("dBoundRoles", "the unfolds render in the work order's map slot, dBoundRoles's; the "
                          "project-map system is dTotalRecall's"),
    "memory.default-load": ("dTotalRecall", "dTotalRecall's row holds the default load of the charter and the "
                            "card; dWellOiledMachine's session-start hook performs the load"),
    "review.twin": ("dFairHearing", "dFairHearing's row runs the twin merge `review.twin` opts in (RS-1); the "
                    "role-shapes system, dBoundRoles's, declares the `twin` shape kind"),
    "retrofit.drain": ("dScopedBuild", "`build.unit-pass` drains the legacy a unit touches, in dScopedBuild's "
                       "row; the retrofit system is dWitnessedBar's"),
    "retrofit.drain-cap": ("dScopedBuild", "dScopedBuild's row drains in hunks under it; the retrofit system is "
                           "dWitnessedBar's"),
    "retrofit.claim-on-touch": ("dScopedBuild", "dScopedBuild's row claims the baselined map keys a write set "
                                "holds; the retrofit system is dWitnessedBar's"),
    "retrofit.claim-cap": ("dScopedBuild", "dScopedBuild's row claims under it; the retrofit system is "
                           "dWitnessedBar's"),
    "retrofit.reconstruct": ("dTotalRecall", "the `adopt` program is dTotalRecall's, and its row governs "
                             "`adopt.reconstruct` by it; the retrofit system is dWitnessedBar's"),
    "retrofit.decisions": ("dTotalRecall", "`adopt.decisions` is dTotalRecall's, routed through it; the "
                           "retrofit system is dWitnessedBar's"),
    "retrofit.practice-pending": ("dTotalRecall", "`adopt.practices` is dTotalRecall's, ruled through it; the "
                                  "retrofit system is dWitnessedBar's"),
    "retrofit.cadence": ("dTendedCadence", "dTendedCadence's row files each period's sweep under "
                         "`retrofit.cadence: hot-first`; the retrofit system is dWitnessedBar's"),
    "retrofit.slot-bytes": ("dBoundRoles", "it caps the work order's legacy slot, which dBoundRoles renders; the "
                            "retrofit system is dWitnessedBar's"),
    "annotations.delivery": ("dBoundRoles", "it switches the work order's code-notes slot, which dBoundRoles "
                             "renders; the annotations system is dTotalRecall's"),
    "hooks.bypass": ("dWitnessedBar", "whether the bar's hooks may be bypassed; dWitnessedBar's row records "
                     "bypasses and owns the hook-read verdict, and the enforcement surface is dWellOiledMachine's"),
    "orient.budget": ("dDeclaredLoop", "dDeclaredLoop's row records orientation cost per stage, which the key's "
                      "values switch"),
    "integrations.tracker": ("dTotalRecall", "it mirrors the ask register out; the register is dTotalRecall's, "
                             "and the mirror is an integrations adapter at its point"),
    "patch.ratify": ("dTendedCadence", "Maintain files patch intakes from detector readings in dTendedCadence's "
                     "row, and the key says who ratifies them (FL-M3)"),
    "decisions.major": ("dTotalRecall", "it says who declares a decision major for the log, dTotalRecall's; "
                        "`build.ratify`, dScopedBuild's, rules on forks already classed"),
    "notify.channel": ("dWellOiledMachine", "notification adapters are a Runtime point (layer-runtime "
                       "`[extend]`)"),
    "verdict.remote.trust": ("dWitnessedBar", "the verdict engine reads it; a remote verdict arrives through an "
                             "integrations adapter at Test's verdict-backend point"),
    "verdict.remote.pin-scope": ("dWitnessedBar", "the verdict engine reads it; a remote verdict arrives through "
                                 "an integrations adapter at Test's verdict-backend point"),
    "verdict.remote.pin": ("dWitnessedBar", "the verdict engine reads it; a remote verdict arrives through an "
                           "integrations adapter at Test's verdict-backend point"),
}
NAMESPACE = {
    "policy": ("dDeclaredLoop", "the guard, the TTY CLI and the default floor; policy at govkit intake"),
    "floor": ("dDeclaredLoop", "the guard, the TTY CLI and the default floor"),
    "transitions": ("dDeclaredLoop", "the transition record three ways"),
    "leases": ("dDeclaredLoop", "one lease grammar for builds, units and cadence runs"),
    "deps": ("dDeclaredLoop", "dependency coordination by the parent's lease"),
    "flow": ("dDeclaredLoop", "one transition table per level; a default failure route"),
    "card": ("dDeclaredLoop", "the build's orientation card at level 1"),
    "landing": ("dShippedRelease", "landings ordered through the landing queue it builds"),
    "deploy": ("dShippedRelease", "the deploy engine"),
    "currency": ("dShippedRelease", "the fleet register and currency watch"),
    "install": ("dShippedRelease", "the deploy engine; the fleet register"),
    "kits": ("dShippedRelease", "the fleet register and currency watch; the kit factory"),
    "release": ("dShippedRelease", "promotion after landing through environments"),
    "reuse": ("dTotalRecall", "reuse entries proposed with their build through the instruction command"),
    "runtime": ("dWellOiledMachine", "the supervisor, act sessions and the one enforcement surface"),
    "review": ("dCalibratedLens", "review by policy per stage and effort; the stage-exit recommendation; the "
               "weekly Loop Review"),
    "budgets": ("dCalibratedLens", "caps re-derived from evidence and review cost"),
    "tests": ("dWitnessedBar", "the product-test contract with runner adapters"),
    "verdict": ("dWitnessedBar", "the runner-written verdict; attribution deciding what blocks; held legs by "
                "policy; flake quarantine"),
    "plan": ("dRankedPlan", "the planner and triager role and Plan workflow; rule-based triage"),
    "design": ("dIndexedDesign", "the derived-READY hand-off; the design index"),
    "maintain": ("dTendedCadence", "the Maintain run as its step checklist; the cadence; the safe-fix set; "
                 "detectors with owners"),
    "observability": ("dTendedCadence", "Maintain and the Loop Review delivered as cadence steps of the "
                      "observability expansion"),
}
TAGNS_ROW = {"reader", "level", "layer", "practice", "principle", "kind", "kit"}
# Record kinds, tabulated from layer-memory [contract]'s list and the chain rows that name a kind. Each layer's
# contract registers its own kinds, so the list is not closed. A kind's owner is the build of its writer.
KINDS = [
    ("intake", "dWellOiledMachine", "decided", "its writer is `entry.intake`'s hook (PM-9); dRankedPlan's row "
     "also describes that hook, which the re-cut reconciles", True),
    ("card", "dDeclaredLoop", "row", "the build's orientation card at level 1, its stores and snapshot", False),
    ("plan", "dRankedPlan", "stage", "its writer is `plan.record`", False),
    ("dupes", "dRankedPlan", "stage", "its writer is `plan.dedupe`", False),
    ("seams", "dIndexedDesign", "stage", "its writer is `design.seams`", False),
    ("feature design", "dIndexedDesign", "stage", "its writer is `design.decompose`", False),
    ("spec", "dIndexedDesign", "stage", "its writer is `design.unit-spec`; the spec redesigned as a structured, "
     "tagged contract", False),
    ("fork", "dIndexedDesign", "judgment", "a flow record kind (layer-memory `[decisions]`); fork resolution by "
     "`design.forks` is dIndexedDesign's, though forks arise in every step", True),
    ("acceptance", "dScopedBuild", "stage", "its writer is `build.acceptance`", False),
    ("scope", "dScopedBuild", "stage", "its writer is `build.scope`", False),
    ("verdict", "dWitnessedBar", "stage", "its writer is `test.verdict`", False),
    ("attribution", "dWitnessedBar", "stage", "its writer is `test.attribute`", False),
    ("flake", "dWitnessedBar", "stage", "its writer is `test.flakes`; flake quarantine", False),
    ("landing", "dShippedRelease", "row", "the landing record; its writer is `deploy.record`", False),
    ("transition", "dDeclaredLoop", "row", "the transition record three ways; every step's exit item writes it",
     False),
    ("lease", "dDeclaredLoop", "judgment", "dDeclaredLoop's row builds the one lease grammar; layer-memory lists "
     "the lease among Runtime's kinds", True),
    ("mailbox message", "dDeclaredLoop", "judgment", "dDeclaredLoop's row builds the mailbox and its message "
     "kinds; layer-memory lists it among Runtime's kinds", True),
    ("return", "dWellOiledMachine", "row", "the persisted-return store, keyed per spawn site", False),
    ("act", "dWellOiledMachine", "row", "one act session per role act; act binding and the epoch check", False),
    ("session binding", "dWellOiledMachine", "row", "sessions bound on every source", False),
    ("journal", "dWellOiledMachine", "row", "the journal grammar moved into the core", False),
    ("run record", "dWellOiledMachine", "judgment", "`RUN.md` belongs to the unattended run, which the "
     "supervisor executes; observability's `observability.run-record` reads it", True),
    ("work order", "dBoundRoles", "row", "the work order rendered per item", False),
    ("review", "dFairHearing", "judgment", "its writer is `review.report`, the harness's, under the proposal "
     "for the breakpoint's items", True),
    ("research return", "dTotalRecall", "row", "the research view over the research-return kind and its dated "
     "backfill; `plan.research` and `design.research` write it", False),
    ("design record", "dTotalRecall", "judgment", "a core memory kind with no writer item; the memory contract "
     "declares it", True),
    ("ask", "dTotalRecall", "row", "the ask kind's acceptance at filing", False),
    ("backlog row", "dTotalRecall", "judgment", "the ask register's row store; the memory contract declares "
     "it", True),
    ("decision", "dTotalRecall", "row", "decisions split by kind, the major-decision log", False),
    ("gotcha", "dTotalRecall", "row", "gotchas handed by write set", False),
    ("dossier", "dTotalRecall", "row", "dossiers anchored to symbol keys", False),
    ("symbols", "dTotalRecall", "row", "the caller map", False),
    ("callers", "dTotalRecall", "row", "the caller map", False),
    ("annotation index", "dTotalRecall", "row", "the generated annotation index and its resolve check", False),
    ("recall index", "dTotalRecall", "row", "memory-recall narrowed to a record finder", False),
    ("baseline", "dTotalRecall", "row", "retrofit's `baseline` and `census` record kinds", False),
    ("census", "dTotalRecall", "row", "retrofit's `baseline` and `census` record kinds; `adopt.census` writes it",
     False),
    ("ruling", "dTotalRecall", "judgment", "`adopt.practices` writes the ruling records, an item dTotalRecall "
     "owns", True),
    ("shape-run", "dTotalRecall", "row", "the shape-run kind", False),
    ("maintenance record", "dTendedCadence", "row", "the maintenance record", False),
    ("lexicon declaration", "dMindYourWords", "judgment", "layer-memory lists the lexicon as an optional "
     "component's kind; dMindYourWords builds the declaration and its packs", True),
]


def key_owner(k):
    exact = cites(k)
    wild = [b for b in wildcard(k) if b not in exact]
    sysk = sys_keys.get(k, [])
    sown = sorted({sys_owner[s] for s in sysk})
    ev = []
    if exact:
        ev.append("row " + ",".join(exact))
    if wild:
        ev.append("row-wildcard " + ",".join(wild))
    if sysk:
        ev.append("system " + ",".join(f"{s} ({sys_owner[s]})" for s in sysk))
    if k in KEY_JUDGED:
        b, why = KEY_JUDGED[k]
        return b, "judgment", why, True, ev
    if len(exact) == 1:
        flag = bool(sown) and exact[0] not in sown
        return exact[0], "row", "", flag, ev
    if len(exact) > 1:
        sys.exit(f"{k}: cited by {exact} and no judgment")
    if sysk:
        if len(sown) > 1:
            sys.exit(f"{k}: in systems with owners {sown} and no judgment")
        return sown[0], "system", "", False, ev
    if len(wild) == 1:
        return wild[0], "row-wildcard", "", False, ev
    nsname = k.split(".")[0].rstrip("*")
    if nsname in NAMESPACE:
        b, quote = NAMESPACE[nsname]
        return b, "namespace", f"{b}'s row: {quote}", False, ev
    sys.exit(f"{k}: no evidence and no rule")


def item_owner(tag, step):
    exact = cites(tag)
    ev = ["row " + ",".join(exact)] if exact else []
    if tag in ITEM_JUDGED:
        b, why = ITEM_JUDGED[tag]
        return b, "judgment", why, True, ev
    if step == "entry":
        if tag == "entry.intake":
            return "dWellOiledMachine", "decided", "PM-9: the intake hook stays dWellOiledMachine's, with "\
                "`gap-rt-14`; dRankedPlan's row also describes the hook, which the re-cut reconciles", True, ev
        return "dDeclaredLoop", "decided", "PM-9", False, ev
    if step == "lifecycle":
        return "dWellOiledMachine", "decided", "flow-steps `[lifecycle]`: Runtime executes the owner's controls "\
            "(dWellOiledMachine, RT-3)", False, ev
    if step == "adopt":
        if len(exact) == 1:
            return exact[0], "row", "", False, ev
        if tag == "test.seed":
            return "dWitnessedBar", "row", "dWitnessedBar's row builds it; dShippedRelease's row cites it as "\
                "what its install and update hooks call", False, ev
        sys.exit(f"{tag}: adopt item with rows {exact}")
    stage = STAGE[{"plan": "Plan", "design": "Design", "build": "Build", "test": "Test", "deploy": "Deploy",
                   "breakpoint": "Review"}[step]]
    if exact and exact != [stage]:
        if len(exact) == 1:
            return exact[0], "row", f"{exact[0]}'s row cites it, where the stage rule would give it to {stage}", \
                True, ev
        sys.exit(f"{tag}: rows {exact} against stage {stage}")
    return stage, "stage", "", False, ev


def cell(s):
    return s.replace("|", "/")


def table(head, body):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in body]
    return "\n".join(out)


result = {"items": [], "keys": [], "points": [], "tagns": [], "systems": [], "kinds": []}
for n in ns["item"]:
    step = dict(n["rels"])["owner"][0]
    b, cls, why, flag, ev = item_owner(n["key"], step)
    result["items"].append(dict(node=n["key"], step=step, owner=b, cls=cls, why=why, flag=flag, ev=ev))
for n in ns["policy-key"]:
    b, cls, why, flag, ev = key_owner(n["key"])
    result["keys"].append(dict(node=n["key"], owner=b, cls=cls, why=why, flag=flag, ev=ev))
for n in ns["point"]:
    result["points"].append(dict(node=n["key"], owner=STAGE["Runtime"], cls="layer",
                                 why="layer-runtime `[extend]` declares it a Runtime point, and the chain table "
                                     "gives the Runtime stage to " + STAGE["Runtime"], flag=False, ev=[]))
for n in ns["tag-namespace"]:
    own = (dict(n["rels"]).get("owner") or [""])[0]
    if n["key"] in TAGNS_ROW:
        result["tagns"].append(dict(node=n["key"], owner="dOrderedCharter", cls="row",
                                    why="dOrderedCharter's row: the namespaced tag system (reader, level, layer, "
                                        "..., kit); the Owners bullet defaulted it", flag=False, ev=[]))
    else:
        result["tagns"].append(dict(node=n["key"], owner=own, cls="declared",
                                    why="the systems record's Owners bullet", flag=False, ev=[]))
for n in ns["system"]:
    result["systems"].append(dict(node=n["key"], owner=sys_owner[n["key"]], cls="declared",
                                  why="its record's owners", flag=False, ev=[]))
for name, b, cls, why, flag in KINDS:
    result["kinds"].append(dict(node=name, owner=b, cls=cls, why=why, flag=flag, ev=[]))

OUT.mkdir(parents=True, exist_ok=True)
json.dump(result, open(OUT / "ownership.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(NAMESPACE, open(OUT / "namespace-rules.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
parts = []
for sec, rows_ in (("items", result["items"]), ("keys", result["keys"]), ("points", result["points"]),
                   ("tagns", result["tagns"]), ("systems", result["systems"]), ("kinds", result["kinds"])):
    body = [[f"`{r['node']}`" if sec != "kinds" else r["node"], r["owner"], r["cls"],
             "; ".join(x for x in [r["why"]] + r["ev"] if x) or "—", "yes" if r["flag"] else ""] for r in rows_]
    if sec == "items":
        body = [[f"`{r['node']}`", r["step"], r["owner"], r["cls"],
                 "; ".join(x for x in [r["why"]] + r["ev"] if x) or "—", "yes" if r["flag"] else ""]
                for r in rows_]
        parts.append((sec, table(["Item", "Step", "Owner", "Evidence", "Why", "Look"], body)))
    else:
        parts.append((sec, table(["Node", "Owner", "Evidence", "Why", "Look"], body)))
for sec, t in parts:
    (OUT / f"table-{sec}.md").write_text(t + "\n", encoding="utf-8", newline="\n")

allrows = [r for v in result.values() for r in v]
by_cls, by_owner = {}, {}
for r in allrows:
    by_cls[r["cls"]] = by_cls.get(r["cls"], 0) + 1
    by_owner[r["owner"]] = by_owner.get(r["owner"], 0) + 1
assert all(r["owner"] for r in allrows), [r["node"] for r in allrows if not r["owner"]]
chain = {c["build"] for c in A["chain"]}
assert all(r["owner"] in chain for r in allrows), [r for r in allrows if r["owner"] not in chain]
flags = [(sec, r) for sec, v in result.items() for r in v if r["flag"]]
print(f"nodes {len(allrows)}: items {len(result['items'])}, keys {len(result['keys'])}, points "
      f"{len(result['points'])}, tag namespaces {len(result['tagns'])}, systems {len(result['systems'])}, record "
      f"kinds {len(result['kinds'])}")
print("by evidence: " + ", ".join(f"{k} {v}" for k, v in sorted(by_cls.items(), key=lambda x: -x[1])))
print("by owner: " + ", ".join(f"{k} {v}" for k, v in sorted(by_owner.items(), key=lambda x: -x[1])))
print(f"every node has exactly one owner, and every owner is a chain build: yes · flagged {len(flags)}")
unowned_builds = sorted(chain - set(by_owner))
print(f"chain builds that own no node: {', '.join(unowned_builds) or 'none'}")
```

## [answers] The owner's answer, 2026-10-17

The owner chose, verbatim: "Approve as proposed (Recommended)". All 351 owners land as proposed, the 47 flagged rows among them.
The answer is structural, so it adds no policy key.

## [folded] What landed

- **The owner fields:**
  - flow-steps' nine item tables gain an `Owner` column, 81 rows, and `[rules]` says so;
  - v2's catalogue gains an `Owner` column, 187 rows, under a revision note;
  - layer-runtime `[extend]` gains an `Owner` column, 10 rows;
  - the systems record's Owners bullet declares the seven namespaces dOrderedCharter registers;
  - layer-memory `[contract]` gains the record-kind table, 41 rows.
- **The generator reads the declared fields only** (`build/2026-10-17-build-PLAY-dClosedLoop-1-map.py`):
  - an item's owner from its `Owner` column, a key's from the catalogue's, a point's from `[extend]`'s, a
    record kind's from layer-memory's table, and a namespace's from the Owners bullet. The stage rule,
    the point literal and the namespace default are gone;
  - a step's and a policy namespace's owners are derived from their members, so the breakpoint reads
    `owner=dCalibratedLens,dFairHearing`;
  - the owner check covers the six kinds: exactly one owner each, a chain build, read from a declared
    field. A missing owner renders `owner=?` and the header counts it as `unowned`;
  - record kinds have an extractor at last, so no namespace is unarmed, and the map exits 0.
- **The atlas** carries each item's and each key's owner. **The preset check** reads the catalogue's five
  columns, and still reads 192 keys, 182 presettable and 182 preset rows.

```text
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check
map: 2066 nodes in 30 namespaces; 27770 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1372, derived 243, pending 451
rc 0
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check --plant <case>, for each case
orphan: FINDING owner: item.entry.intake names no owning build rc 1
two-owners: FINDING owner: policy-key.preset names 2 owning builds rc 1
inferred: FINDING no inference: point.actor-kinds's owner comes from no declared field rc 1
no-owner: FINDING owner: tag-namespace.reader names no owning build rc 1
drop-line: FINDING complete: layer has nodes on no line and in no count: ['instruction'] rc 1
bad-count: FINDING count: item.* counts 82, the table holds 81 rc 1
ghost-rel: FINDING resolves: chain.dOrderedCharter names owner=dGhostBuild, which resolves nowhere rc 1
census: FINDING census: tools/newkit/kit.toml is on disk with no kit node rc 1
```

- **The other instruments hold:** the role matrix reads 81 of 81 items with 0 findings, the gap join is
  clean, the table-shape check finds only its 2 known rows, and the atlas derives 137 records.

## [amended] Amended after approval

- **RC-8, 2026-10-18:** `placement` and `placement.check` are dDeclaredLoop's, not dRankedPlan's. The entry step's
  placing items are dDeclaredLoop's under PM-9, and they branch on the one key and are witnessed by the other, so the
  keys move with them; dBoundRoles's driver then runs a check its ancestor owns. v2's catalogue carries the change
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` `[order-review]`). The tables above keep the approved proposal as it was.
- **PM-12, 2026-10-18:** the owner's answers on the table's re-verification move 13 owners, take a
  recommendation for 5 more, add 52 nodes and give the `disposition` kind to dDeclaredLoop. The owner fields
  carry the changes (`build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md` `[pm-12]`, `[answers-2]`).
- **AF-1, 2026-10-18:** the design audit's H1 and H2 put the stage-exit recommendation and the owner gate where every
  step reaches them. The breakpoint mechanism is dDeclaredLoop's: 12 items, 11 keys, the `recommendation` kind and
  gap-flow-11 and gap-flow-12, which re-opens PM-12a for the 8 stage items
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md` `[af-1]`).
- **FM4, 2026-10-18:** `review.findings` follows `review.dispose`, which reads it, to dDeclaredLoop, so AF-1's cut
  leaves no key of the disposal on the far side (`build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md`
  `[review-fold]`).
- **The night pass, 2026-10-18** (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`): the new nodes and their owners, proposed for the owner's approval as PM-10's
  were (NP-23), each owner the build that implements the behaviour or registers the kind:
  - items `probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, `probe.run`, `probe.judge` and
    `probe.return`: dDeclaredLoop;
  - keys `attendance`, `probe.points`, `probe.raise`, `probe.observations` and `probe.experiment.authority`:
    dDeclaredLoop; `attendance.scope`: dWellOiledMachine; `memory.code-budget` and
    `memory.code-roles`: dBoundRoles; `memory.code-languages` and `memory.code-enrich`: dTotalRecall; `tags.bundle`
    and `tags.bundle-rows`: dOrderedCharter;
  - record kinds `probe`: dDeclaredLoop; `code`: dTotalRecall, replacing `symbols` and `callers`; `playbook`:
    dIndexedDesign; `playbook set`: dIndexedDesign, which registers its set check at Test's leg-pack point (the
    closing review's H2); `attendance override`: dWellOiledMachine (M13).
- **NP-23, 2026-10-18:** the owner approved the night pass's nodes and owners on review, asked as four groups
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[answers]`), with the keys NP-19 to NP-21 add:
  `maintain.security-review` and `maintain.tiers`: dTendedCadence; `install.guards`: dShippedRelease.
- **SP-1, 2026-10-18:** the owner chose S3, so dDeclaredLoop splits into itself, dPlacedRequest and dKeptSession
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-np24-pricing.md`). The nodes move with their clauses:
  - to dPlacedRequest: the entry items `entry.orient`, `entry.place`, `entry.place-check`, `entry.place-owner` and
    `entry.claim`, the probe program's seven items, the `lease`, `card` and `probe` kinds, and the keys
    `leases`, `leases.granularity`, `leases.renewal`, `leases.expiry-hours`, `leases.overlap`, `leases.offline`, `card.follows`, `card.store`, `card.snapshot`, `resume.partial`, `resume.context`, `placement`, `placement.check`, `probe.points`, `probe.raise`, `probe.observations`, `probe.experiment.authority`;
  - to dKeptSession: the `mailbox message` kind and the keys `preset`, `attendance`, `deps.coordination`, `deps.early-build`, `deps.messaging`, `notify.owner`, `mailbox.reads`, `context.on-full`, `context.threshold`, `card.pointers`, `actions.free`, `orient.budget`.
- **WK-4, 2026-10-18:** the owner chose C2, so dTotalRecall splits into itself and dLinkedLibrary, and dBoundRoles into itself
  and dFurnishedOrders (`build/2026-10-18-build-PLAY-dClosedLoop-1-wk3-pricing.md`). The nodes move with their units:
  - to dLinkedLibrary: the items `adopt.census`, `adopt.practices`, `adopt.decisions`, `adopt.reconstruct`, the kinds `research return`, `decision`, `gotcha`, `annotation index`, `recall index`, `baseline`, `census`, `ruling`, the
    annotations system, and the keys `annotations.budget`, `annotations.grammar`, `annotations.lookup`, `annotations.resolve-scope`, `decisions.major`, `memory.code-enrich`, `retrofit.decisions`, `retrofit.practice-pending`, `retrofit.reconstruct`, `reuse.delivery`, `reuse.propose`;
  - to dFurnishedOrders: the keys `annotations.delivery`, `instructions.slices`, `memory.code-budget`, `memory.code-roles`, `memory.map-unfold`, `memory.project-map`, `notices.record`, `prompts.batch`, `retrofit.slot-bytes`, `roles.answered-calls`, `roles.on-contradiction`, `roles.orientation.house-index`, `roles.trust`, `roles.verifier-context`.
- **The whole-design audit's fork answers, 2026-10-20**
  (`build/2026-10-20-build-PLAY-dClosedLoop-1-fold-brief-w7.md`): `patch.ratify` moves from dTendedCadence to
  dPlacedRequest, whose `entry.claim` reads it for every patch (FK-6-2); `build.release-ceiling` moves from
  dWellOiledMachine to dShippedRelease with the release arm of the event-wait sweep (FK-2-3); `budgets.*` moves
  from dCalibratedLens to dGroundRules, which makes it each cap's one declaration (FK-1-3); and the items
  `kits.install-attended` and `kits.update-attended` join dShippedRelease (FK-5-1). The rows above carry the
  moves.

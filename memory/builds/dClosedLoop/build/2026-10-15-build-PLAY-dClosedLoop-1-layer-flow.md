# Layer review: the flow layer

**Serves:** research PLAY-dClosedLoop-1

The second round of the owner's layer-by-layer review. It covers the flow layer, set against the
current design:
- the flow record;
- the flow-roles record;
- the roles record's `[map]`;
- v2's `[principles]`, `[contracts]` and `[layers]`.

The item-level audit runs through two researchers, dispatched 2026-10-15. Their returns are saved as
`build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-{a,b}.md`.

## [words] The owner's words, 2026-10-15

> Let's review the Flow layer next, thoughts so far:
> [2. DLG Flow, Development Lifecycle Layer]
>
> * 5 mandatory steps + a flexible review step that reviews work at a breakpoint.
> * This is the backbone of the product, that defines a process that everything gets built through.
> * Each step must be a detailed, deterministic (checklist?) process, mechanically enforced to the
>   fullest extent possible - how is a feature planned? how is it designed? how is it tested? how is
>   it tested? how is it deployed? how is it maintained?
> * Clearly defined and enforced which pieces of the instruction layer apply at each step.
> * Clearly defined roles that can participate at each step of the layer.
> * Clear transition flow between steps and interactions between them.

## [how] Each step at a glance, as designed today

| Step | The question it answers | Its items, by name | Its roles | Its exit witness | Where it routes |
|---|---|---|---|---|---|
| Plan | Is this worth building, and what exactly? | intake, duplicates, triage, disposition, plan record, practice reach, placement, lease, recommendation and review, ratification, transition | planner, researcher on request; review roles | the intake record (the request is the ratification) and the plan record's checks | Design, with the ratified plan record; a duplicate attaches to a live build; out of scope is refused |
| Design | How will it be built, and in what pieces? | input, seams, features and units, unit specs, overlaps, review, derived READY, transition | reuse scout, architect, spec writers in parallel; review roles | derived READY for every unit; frozen interfaces posted to dependents | Build; a fork the goal cannot survive becomes a plan revision under the request's mandate |
| Build | Is each unit built to its spec? | base, unit leases, unit builds, routes, scope report, closing review, core checks, transition | builders, one per unit; review roles (diff lens) | in-scope commits, the closing review recorded, the core checks | Test; `diverged` goes back to the spec writer or the architect |
| Test | Does the merged result hold? | prepared merge, selection, verdict, attribution, flakes, seen-red, review, transition | tester; review roles (gate lens) when owed | the runner-written verdict for the tree, which the pre-push hook reads | Deploy; each red to a builder fix pass, a new unit at Design, an ask, or a conflict resolution |
| Deploy | Is it landed and verified? | currency, mandate, landing, landing record, release notes, verifies, review, leases released, transition | deployer; review roles (landing lens) when owed | the lander's and the engine's records; `landed` sent to dependents | closed; a moved tip goes back to Test; a verify that fails after the build closed goes to Plan's triage |
| Maintain, the repository's | Is what landed still healthy? | period lease, detectors, cadence tests, safe fixes, filings, release, currency, record, lease released | tester, maintainer, deployer | the maintenance record | patch builds to Design; asks to Plan's triage; metrics to the Loop Review |

The flow has two review checklists:
- a stage review, of seven items, blocking its transition;
- the Loop Review, of five items, run on its cadence.

## [shape] The layer's shape against the owner's

- **Five mandatory steps are a build's lifecycle, and Maintain is the repository's step.**
  - The design has six steps, while the owner counts five mandatory ones and still asks how a feature
    is maintained. One reading reconciles both.
  - Every build passes Plan, Design, Build, Test and Deploy, from its entry point to its landing.
  - Maintain runs on a cadence and on events, over what has landed, and never inside one build. The
    design already runs it so (flow `[maintain]`: daily at session start, plus events).
  - Maintain closes the loop (P6): it opens patch builds at Design and files asks into Plan's triage.
  - It stays core, with core detectors:
    - the cadence test levels and held legs;
    - dormant builds;
    - the process census;
    - gate health.
  - The expansions plug in further detectors:
    - drift, from observability;
    - map freshness, from knowledge;
    - adopter currency, from distribution.
- **Review is a breakpoint, not a step.**
  - Today a stage review sits at one fixed item per step (`review.<stage>`); owner gates sit at
    `autonomy`'s points; the Loop Review runs on its cadence; and every review that runs blocks
    (`review.blocks`).
  - The owner's "breakpoint" names the abstraction that unifies them: a pause declared at an item
    boundary, disposed by a reviewer lens or by the owner, and blocking the next item until it is
    disposed.
  - "Flexible" then means a breakpoint can sit at any item boundary, by policy.
- **The backbone is designed:** nothing changes tracked content outside the flow (P20).
- **A checklist is the view; the step itself is a program (P24).**
  - Items declare their dependencies, so independent items run in parallel (spec writers per unit,
    builders on disjoint units) and dependent ones run in order.
  - Each item is a typed declaration:
    - its tag and actor;
    - its inputs, by layer;
    - its instruction scope;
    - its allowance;
    - its return template, with a closed outcome set;
    - its witness and its routes.
- **Enforcement follows three rules:**
  - Sequence and structure are mechanical. The engine runs ready items, a witness closes each one,
    and the transition table refuses any transition it does not declare.
  - Judgment is confined to role items, whose returns are schema-forced.
  - Quality is checked at breakpoints.
- **Instruction scope per step:** the instruction layer gives the mechanism (P13, P27). The flow's
  half is that every item declares its scope tags: the practices' reach for its step, the method
  views, the templates and the policy keys it reads. Its load set is then derived and checked.
- **Roles per step:** the actor map exists (roles `[map]`). A step's roster derives from its items'
  actors, and exclusivity is held at four points (roles `[guard]`).
- **Transitions:**
  - The pieces exist: entry points, contracts, backward routes, the records chain, and coordination
    between builds.
  - They are scattered across six records, and one declared table per level is the fix.

## [fit] The owner's requirements against the current design

| The owner's requirement | The current design | Status |
|---|---|---|
| Five mandatory steps, and review at a breakpoint | six steps with Maintain on a cadence; stage reviews at fixed items; owner gates by `autonomy`; the Loop Review | designed; the count and the breakpoint framing are to settle |
| The backbone everything is built through | P20; the entry-point table; patch builds at Design | designed |
| Each step a deterministic, enforced process | the items `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` declares, each witnessed; P2, P24; the item cycle (flow-roles `[cycle]`) | designed as programs since the step definitions: each item declares what it needs, and items are tagged |
| The instruction pieces per step, enforced | practice reach at Plan and Design items; P27's load sets | partly: items declare no instruction scope |
| The roles per step | the actor map; flow-roles `[steps]`; four exclusivity points | designed, though three items have the driver reasoning |
| Transitions and interactions | entry points; v2 `[contracts]`; backward routes; the records chain; dependencies, the mailbox, `landed` | partly: scattered, with no single declared table and no terminal state but landing |

## [uncovered] What the layer does not yet cover

Three new gaps are proposed:
1. **gap-flow-10, HIGH, dWellOiledMachine since RT-3.** A build can end only by landing.
   - There is no withdrawn, superseded or merged terminal state.
   - The owner's pause, resume and abort exist only for unattended runs (`--hold`, `--resume`,
     `--abort`), not as a build's lifecycle, and supersede does not exist.
   - A dependent held until its parent lands (`deps.landing`) waits forever on a parent that never
     will.
2. **gap-flow-11, MED, dCalibratedLens.** Reviews and owner gates are two mechanisms, fixed to set
   points.
   - Each step's review sits at one item (`review.<stage>`).
   - Owner gates sit at `autonomy`'s three points.
   - Neither can be placed at another item boundary.
3. **gap-flow-12, MED, dCalibratedLens.** The driver reasons in four items.
   - The review recommendation at Plan, Design, Test and Deploy is scored by a command and reasoned by
     the driver.
   - That breaks P25 and `driver.reads`, and FL-R3's "scored signals and reasoning" never named a role
     to do the reasoning.

Two more gaps were registered from the audit, at `[settled]`:
- **gap-flow-13, HIGH, dDeclaredLoop.** Item declarations are incomplete. Items carry more than one
  actor, many state no witness or no failure route, and the records disagree. Deploy had no item for
  settled behaviours: the parent-landing hold, the core re-check and the `landed` notice.
- **gap-flow-14, HIGH, dDeclaredLoop.** Witnesses typed by the acting agent decide routes or mandates:
  the tester's class routes a red, the builder's own "checks run" stands for acceptance, the driver's
  typed disposition places a request, and Maintain's agent-typed intake becomes a patch build's
  mandate.

Already registered, and not proposed again:
- no stage model (gap-spine-01);
- no feature level (gap-flow-01);
- a build's step when its units sit in different steps (gap-flow-07);
- landing order (gap-flow-08);
- merge conflicts (gap-flow-09);
- coordination between builds (gap-flow-06);
- different contracts for attended and unattended runs (gap-spine-03);
- instructions joined to no step or item (gap-found-09);
- the core depending on expansions (gap-found-17).

## [recommendations] What would make the layer coherent and extendable

**F-A. A build's lifecycle is five mandatory steps, and Maintain is the repository's step.**
- A build enters at Plan or at Design, by the entry-point table, and passes every later step up to
  landing.
- Maintain runs over the repository, on its cadence and its events, with core detectors and an
  extension point for more.

**F-B. Review is a breakpoint.**
- One mechanism carries reviews and owner gates. A breakpoint has:
  - a position: an item boundary or a step's exit;
  - a disposer: a reviewer lens, with its skeptic and synthesizer, or the owner;
  - a blocking rule, by `review.blocks`.
- `review.<stage>` and `autonomy` become breakpoint declarations, and their current points become the
  defaults.
- The owner may add a breakpoint at any item boundary by policy (`review.breakpoints`).
- An owner breakpoint parks a build by definition, so it exists only where the owner places one. FR-4's
  rule that no build parks still governs forks.
- The Loop Review is the breakpoint on the loop itself, run on its cadence.

**F-C. Each step is a program, and its checklist is the view.**
- Every item declares:
  - its tag and actor;
  - its inputs, by layer;
  - its instruction scope tags;
  - its allowance;
  - its return template, with a closed outcome set;
  - its witness and its routes;
  - what it depends on, and its fan-out.
- The engine runs ready items in dependency order, in parallel within the fan-out bound.
- P24's "resolved before the next item starts" becomes "resolved before any item that depends on it
  starts".

**F-D. One transition table for each level: build, feature and unit.**
- Each is a state machine whose states are derived from witnesses (P22). Each row holds the state
  it leaves, the event or outcome, the state it enters, the witness, and where the transition is
  recorded.
- The engine refuses any transition the table lacks, which generalises "refuses any transition back to
  Plan".
- Entry points, backward routes, breakpoints and terminal states are all rows of these tables.

**F-E. Terminal states and lifecycle events.**
- A build ends landed, withdrawn or superseded. When superseded, its replacement inherits its kept work
  through the re-design inventory already settled for planning misses.
- The owner can pause, resume, withdraw or supersede a build. The controls extend unattended's
  `--hold`, `--resume` and `--abort`, supersede is new, and Runtime executes them (RT-3; flow-steps
  `[lifecycle]`).
- A withdrawal:
  - releases the build's leases;
  - commits the card's terminal snapshot;
  - sends `withdrawn` to its dependents, who act as `deps.on-parent-withdrawn` says.

**F-F. Each step declares its extension points (P28).**

| Step | Extension point | Fed by |
|---|---|---|
| Design | seams, from the map | knowledge |
| Build | bug classes | knowledge |
| Test | verdict leg packs | leg packs |
| Deploy | release channels and adopter currency | distribution, integrations |
| Maintain | detectors | observability, knowledge, distribution, runtime housekeeping |
| Every step | notifications | integrations |

**F-G. The driver routes and roles reason.**
- The review recommendation's reasoning becomes a reviewer item: one question, under the step's lens.
- Where no reviewer runs, the recommendation is signals-only. `review.recommendation.source` already
  allows that.

**F-H. Items are named by tags,** as settled in the instruction layer's round. The audit proposes the
names.

## [audit] The item audit, returned 2026-10-15

Two researchers declared every item of the 70 and checked each against the layer's requirements.
Their returns are saved verbatim:
- `build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-a.md` covers Plan, Design and Build:
  31 items and 22 findings, by its own count;
- `build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-b.md` covers Test, Deploy, Maintain
  and both reviews: 39 findings, by its own count.

Each return gives, per item: a proposed tag, the actor, the witness, its inputs by layer, its instruction
scope, its routes, its fan-out and dependencies, and its flags. Each also lists every step's extension
points.

The findings fall into these classes:
- **The driver judges.** It places a request at Plan (a F1). It reasons out the review recommendation at
  Plan, Design, Test and Deploy (a F2, b F-X1).
- **Witnesses are typed by the acting agent and decide what happens next:**
  - the tester's class routes a red (b F-T3);
  - the builder's own "checks run" stands for acceptance (a F5);
  - the bug-class trailer (a F6);
  - the deployer's notes and dispositions (b F-D7, F-D8);
  - Maintain's intake becoming a mandate (b F-M2);
  - class identity for left-shift (b F-R2).
- **Items have more than one actor:** a F4, b F-T1, F-D1, F-M7, F-R1.
- **Witnesses are not stated:** a F10, b F-T10, F-D12, F-M10, F-R10.
- **Failure routes are missing:** a F11, b F-T5, F-T7, F-M8, F-R3, F-R9. There is also the bar's labels
  MIXED, CONTENDED and DEAD PROBE, which have no route (b F-T4).
- **Core items need expansions:** the reuse probes, the bug classes, the lexicon (a F6 to F8); flakes
  (b F-T8); Maintain's detectors (b F-M3); kit versions and currency (b F-D9, F-M4).
- **Records disagree:**
  - two disposition sets (a F12);
  - checklist text against later settlements (a F15, b F-M1);
  - actor rows (b F-D3, F-R6);
  - `plan.authority`'s owner clause under `request` (a F14).
- **Settled behaviours have no item:** the parent-landing hold, the core re-check, the `landed` notice and
  the terminal snapshot (b F-D5).
- **Order:** the landing review "blocks" but runs after the push (b F-D4).

The researcher for Test, Deploy and Maintain also raised a sorting question. The core's test, "request to
landing", cannot classify what runs after landing: the release record, Maintain and the Loop Review. The
owner's answer on Maintain settles it by the same test, so all three sit outside the core.

## [forks] Asked, 2026-10-15

**F2-1. "How should the flow's steps be counted?"** Offered:
- Five per build + repo Maintain (Recommended);
- Six per build;
- Maintain as an expansion.

Answer: Maintain as an expansion.

**F2-2. "How should review stop the flow?"** Offered:
- Breakpoints anywhere (Recommended);
- Fixed review points.

Answer: Breakpoints anywhere (Recommended).

**F2-3. "How may a build end besides landing?"** Offered:
- Withdraw or supersede (Recommended);
- Landing only.

Answer: Withdraw or supersede (Recommended).

**F2-4. "What shape should a step's process take?"** Offered:
- Program with dependencies (Recommended);
- Strict ordered checklist.

Answer: Program with dependencies (Recommended).

## [settled] What changed, 2026-10-15

**The core flow is five steps,** Plan to Deploy, carrying a build from its request to its landing.
- Maintain and the Loop Review are cadence steps delivered with the observability expansion. The owner
  chose this, over the recommendation that Maintain be a core repository step.
- By the same sorting test, promotion through environments after landing is an integrations extension
  point. Deploy's core ends at the landing, its record, the leases released, the `landed` notice and the
  terminal snapshot.
- P6 is amended. Without Maintain, the loop closes through requests alone.

**Review is a breakpoint** (P7 amended).
- One mechanism carries reviews and owner gates.
- `review.<stage>` and `autonomy` are its default declarations. `review.breakpoints` adds breakpoints at
  any item boundary, defaulting to none beyond those.
- An owner breakpoint parks a build by definition, and exists only where the owner places one.

**A build ends landed, withdrawn or superseded** (P20 amended).
- A build that ends in planning, by triage or by a re-placement after `plan.dedupe`, ends deferred,
  retired, refused, merged or answered. flow-steps' `[transitions]` holds the whole terminal set
  (revised 2026-10-16).
- The owner pauses, resumes, withdraws or supersedes a build through the owner's controls, which
  Runtime executes (flow-steps `[lifecycle]`).
- A withdrawn parent's dependents act as `deps.on-parent-withdrawn` says: `replan` by default, with
  `adopt-parent-work` and `withdraw-too` allowed.

**Steps are programs with dependencies** (P24 amended). An item's witness is resolved before any item
that depends on it starts.

**Consistency fixes the audit found.** Each follows from settled design, so no fork was put:
- **The recommendation's reasoning** comes from the step's producing role: the planner, architect or
  tester, answering one question after the score (flow-steps `[rules]`). Build and core Deploy have no
  single producing role, so theirs is signals only. Its score stays computed. This reads FL-R3's "the
  agent" through P25 (a F2, b F-X1).
- **The placement disposition** is the orientation scout's return. The driver records it and runs
  `placement.check` (a F1; OR-1's "agent places" is the scout).
- **Ratification under `request`:** the request meets `plan.authority`'s owner clause, and a plan revision
  proceeds under the request's mandate (a F14; FR-1, FR-12).
- **The landing review** blocks the build's close, not the push. Its findings enter by the entry-point
  table's post-close row, which now covers a landing-review finding and a post-landing core red, each
  entering as a patch build, beside a verify that fails after the build closed (b F-D4).
- **The bar's labels** MIXED, CONTENDED and DEAD PROBE route by `verdict.blocks`: to an ask when they do
  not block, and otherwise to the tester, a re-run, a probe repair or an owner exception (flow-steps
  `test.route`; b F-T4).
- **Research records:** a build's own are memory, the trail; the library across builds is knowledge
  (a F9).
- **Flake records** are a flow record kind that observability reads: the nondeterministic legs
  `test.route`'s re-run finds, made a record. Under `verdict.flakes: quarantine`, a flaky leg past the
  threshold is held (b F-T8; revised 2026-10-16).
- **Dispositions:** one closed set, continue, amend, new, patch, ask or none. Defer maps to ask, and a
  duplicate maps to continue (a F12).
- **Item tags** live in the `item` namespace, their full spelling `item.<step>.<name>`, apart from
  `policy.` keys (a F21; layers round one, R-B).

**The register gains five gaps:**
- `gap-flow-13` and `gap-flow-14`, owned by dDeclaredLoop;
- `gap-flow-10`, owned by dDeclaredLoop then, and by dWellOiledMachine since RT-3;
- `gap-flow-11` and `gap-flow-12`, owned by dCalibratedLens.

**Units:**
- dDeclaredLoop, dCalibratedLens, dBoundRoles, dTendedCadence and dShippedRelease gain the units that
  carry the settlement, and dWellOiledMachine, since RT-3, the owner's controls.
- The audit's tables are the input to dDeclaredLoop's item declarations.

## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded

Two Tier-2 rounds reviewed this record together with
`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`. That record's `[revised]` places all 61
defects, those fixed here among them:
- `[fit]` points at the items flow-steps declares;
- `[uncovered]` gives `gap-flow-10` to dWellOiledMachine and corrects its controls, counts four
  reasoning items, and states `gap-flow-13` and `gap-flow-14`;
- F-E's controls extend unattended's verbs;
- `[settled]` names the producing roles that reason, the post-close row's patch builds, the bar's
  labels routed by `verdict.blocks`, flake records, the items' full spelling, and dWellOiledMachine's
  share.

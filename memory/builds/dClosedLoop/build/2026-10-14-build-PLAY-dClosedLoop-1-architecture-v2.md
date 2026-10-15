# Architecture v2 — the converged design: one loop, every behaviour a policy, local-first, facts not prose

**Serves:** research PLAY-dClosedLoop-1

The design after the owner's rounds 1 to 5 (`build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md`)
and the build-by-build walk-through (`build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md`). It
supersedes v1 as the spec writer's input; v0 and v1 stay unedited beside it. Fork ids cite their
record: `R2.4` is round 2's fourth question, `walk T1` the walk-through's first Test fork.

Revised: 2026-10-14, at the owner's direction ("Add named policy presets", recorded in the design
rounds): the `[presets]` section is added and the Spine's roster gains the presets unit. The chain
is still unapproved, pending the owner's revisit of the high-level architecture and flow.

Revised: 2026-10-14, after the foundations revisit's step 1
(`build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md`): principles P13 and P14 are added;
`[front-door]` is rewritten around the ranked charter; `charter.override` and `charter.practices`
join the catalogue, the first of them the presets; the chain gains a new root, dOrderedCharter,
which takes the front door and the tag grammar from the Spine.

Revised: 2026-10-14, after step 1's continuation: P15 is added; the charter gains its drive section
and the 32 KiB bound; dOrderedCharter renders the drive section from kit descriptors and dDeclaredLoop
builds the `next` verb and the `next —` line check.

Revised: 2026-10-14, after the core consistency step (foundations `[core]`): P16 is added;
`core.bypass` and `core.exceptions` join the catalogue and the presets; dOrderedCharter owns the
principle registry, the meta-check, the kinds register and the exception register; each extension
kind's factory and gate lands with its owning build; dScopedBuild's exit refuses while a core red the
build's own commits introduced stands. `core.bypass`'s default rests on an interpretation of the
owner's K1 answer that awaits confirmation.

Revised: 2026-10-14, after the flow walk's Plan stage (`build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md`):
builds run unattended by default past Plan, so `autonomy`'s default and the `standard` preset's
value move to `plan-only`; the owner's plan ratification is the mandate. A critical planning issue is a
recorded plan revision followed by a re-design that preserves completed work.

Revised: 2026-10-14, after the flow walk's Design stage: P17 and P18 are added; the preset `autonomous`
is renamed `guarded`; `design.forks` and `design.reentry` join the catalogue and the presets; the charter's
order ranks the core, then the decision principles, then the practices; four owner-raised `gap-flow-*`
gaps are owned by dOrderedCharter, dRankedPlan and dIndexedDesign.

Revised: 2026-10-14, after the flow walk's Build stage: P19 is added; `review.findings` joins the catalogue
and the presets; dScopedBuild freezes built specs and disposes every closing-review finding as new
units, owning `gap-flow-05`.

Revised: 2026-10-14, after the flow walk's Test stage: `verdict.tree`, `verdict.red-route` and
`tests.landing-levels` join the catalogue and the presets; Test verifies the prepared merge, so one
bar serves Test and the landing.

Revised: 2026-10-14, after the flow walk's Deploy stage: `build.closes` and `release.cadence` join
the catalogue and the presets; a build closes at landing by default, and Deploy's release is recorded
per SHA across landings; gov's kits reach adopters as tagged releases cut on a cadence.

Revised: 2026-10-14, after the flow walk's Maintain stage: `maintain.events` and `patch.ratify`
join the catalogue and the presets; nothing changes tracked content outside the flow, so Maintain's
safe fixes and small product changes enter at Design as patch builds; the entry points are settled.

Revised: 2026-10-14, after the flow walk's Review stage: P20 is added; `review.blocks`,
`review.left-shift` and `review.recommendation.source` join the catalogue and the presets; the flow
walk is complete, and the chain is re-cut around it after the owner's next steps.

Revised: 2026-10-14, after the flow-interactions round (`build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md`):
P21 is added; `deps.coordination`, `deps.early-build`, `deps.messaging`, `landing.order` and `card.follows`
join the catalogue and the presets; four owner-raised gaps are owned by dLeasedFleet, dDeclaredLoop,
dWitnessedBar and dShippedRelease.

Revised: 2026-10-14, at the owner's directive that no build outside the chain is counted on
(`build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`): dLeasedFleet leaves the chain, and its
leases, the mailbox and dependency coordination become dDeclaredLoop's coordination feature, with
gap-conc-01, gap-conc-02 and gap-flow-06; P5 is restated; no chain build waits for a live build's
close, and Maintain's run no longer rides recipe mode; the chain has ten builds.

Revised: 2026-10-14, after the orientation round (`build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md`):
P22 to P24 are added; the build's orientation card joins the charter at the ladder's rank 1;
`placement`, `placement.check`, `kickoff.runs`, `card.store`, `actions.free`, `resume.partial`,
`resume.context` and `orient.budget` join the catalogue and the presets; `gap-orient-01` to
`gap-orient-10` are owned by dDeclaredLoop, dRankedPlan, dOrderedCharter, dScopedBuild and dTendedCadence.

Revised: 2026-10-14, adopting the researched way to preserve the card (orientation OR-5, dispatch 15): the
remote ref is the card's truth, delivered at rank 1 through an imported per-worktree file and re-rendered
by every session-start hook in the session's own tree; the clone's copy is a cache keyed by object id;
`card.snapshot` joins the catalogue and the presets; `gap-orient-11` to `gap-orient-13` are owned by
dDeclaredLoop and dOrderedCharter.

Revised: 2026-10-14, after the owner confirmed both orientation interpretations: the charter wins any
conflict with the build's card at rank 1, and a session runs the full kickoff only when it has no saved
READY card for the build and slice it is placed into.

Revised: 2026-10-14, after the roles round (`build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md`): P25 and
P26 are added; `driver.reads`, `prompts.author`, `roles.retries` and `roles.no-spawn` join the catalogue
and the presets; the chain gains `dBoundRoles`, the roles layer's own build, child of dDeclaredLoop, which
owns `gap-roles-01` to `gap-roles-08` and takes `gap-orient-07` from dOrderedCharter and `gap-orient-09`
from dScopedBuild with their units.

Revised: 2026-10-15, after the flow revisit with roles (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`):
the owner's request is the ratification, so the gate `autonomy` keeps at Plan is met as `plan.ratification`
says; P18 gains the rule that no build parks on an unresolved fork; `plan.ratification`, `run.host`,
`notify.owner`, `run.on-owner-question`, `deps.landing`, `mailbox.reads`, `review.follow-up` and
`prompts.batch` join the catalogue and the presets; the session model's holes are all settled, and the
units that carry them join six chain rows.

Revised: 2026-10-15, after the compaction experiment (`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`):
`context.on-full` (default compact-with-card, fresh-at-boundary allowed), `context.threshold`,
`card.pointers` (default every-item: the card's pointers updated as the build progresses, the owner's
addition) and `notices.record` (default none, all three values allowed) join the catalogue and the
presets; gap-orient-14 joins dDeclaredLoop and gap-roles-09 joins dBoundRoles; the compaction checks
join `[owed]`.

Revised: 2026-10-15, K1 confirmed: the reading of `core.bypass` went to the owner as a fork, and the
owner chose "the violator pays". `with-hooks-report` stands as read in foundations `[core]`, and P16
is unchanged. dShippedRelease's lander gains a core re-check on the landed tree before it releases a
build, so a core red that first appears in the landing merge still stops that build from closing.

Revised: 2026-10-15, after layers round one (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`): the owner framed the product as layers; the
`[layers]` section is added (capabilities, five core layers with Runtime among them, four expansions);
P11 and P13 are amended to the owner's two instruction principles and the tag system, P27 and P28 are
added; the ladder is renumbered with the charter at level 0 and the card at level 1; Skills are level-4
thin entries; `instructions.checks` and `instructions.edit` join the catalogue, the first in every
preset, the second kept from presets; `gap-found-09` to `gap-found-17` join dOrderedCharter,
dConvergedCharter and dCalibratedLens.

Revised: 2026-10-15, after layers round two (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md`):
- A build's lifecycle is five core steps, Plan to Deploy, each a program of items with declared
  dependencies.
- Maintain and the Loop Review are cadence steps delivered with the observability expansion.
- Promotion after landing is an integrations extension.
- Review is a breakpoint, placeable at any item boundary.
- A build ends landed, withdrawn or superseded.
- P6, P7, P20 and P24 are amended.
- `review.breakpoints` and `deps.on-parent-withdrawn` join the catalogue and the presets.
- `gap-flow-10` to `gap-flow-14` join the register. The item audit's findings are owned as item
  declarations by dDeclaredLoop.

Revised: 2026-10-15, after the step definitions (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`): four keys join the catalogue and the presets:
- `review.design.rounds`, one round by default;
- `review.design.round-count`;
- `review.unverified`, an ask by default;
- `tests.without-cadence`, running at landing by default.

Revised: 2026-10-15, after the roles layer's review (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`):
- P29 is added: a role acts on what its work order hands it, and verifies only what its job is to
  verify.
- `roles.trust`, `roles.answered-calls`, `roles.verifier-context` and `roles.on-contradiction` join
  the catalogue and the presets.
- dBoundRoles' roster is sorted into core and expansion roles. Its units gain the trust mechanism,
  the derived role-by-step matrix and role metrics.
- `gap-roles-10` to `gap-roles-17` join dBoundRoles.

Revised: 2026-10-15, opening round four:
- `gap-roles-18` joins dBoundRoles: role items declare no execution shape.
- `[owed]` gains the roles layer's mechanical shape, which the owner set for a later revisit.

Revised: 2026-10-15, after the memory layer's review (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`):
- P30 is added: memory is declared once and written through one door.
- The chain gains dTotalRecall, the memory layer's own build and a child of dDeclaredLoop. It owns
  the memory contract and Knowledge's stores.
- Eight keys join the catalogue and the presets: `reuse.delivery`, `annotations.grammar`, `builds.agent-root`, `asks.acceptance`, `builds.slug-words`, `builds.slug-style`, `builds.slug-date` and `lexicon.pin`.
- `gap-mem-01` to `gap-mem-11` join dTotalRecall. `gap-tool-01` to `gap-tool-06` join dWitnessedBar,
  dShippedRelease, dDeclaredLoop and dConvergedCharter.

Revised: 2026-10-15, after the lexicon kit's review (`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`):
- The chain gains dMindYourWords, the lexicon's own build and a child of dTotalRecall. It takes the
  lexicon pin and `gap-mem-10` from dTotalRecall.
- `lexicon.forced`, `lexicon.at-commit`, `lexicon.drift` and `lexicon.packs` join the catalogue and
  the presets.
- `gap-lex-01` to `gap-lex-07` join dMindYourWords.

Revised: 2026-10-15, after the runtime layer's review (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`) and its two Tier-2 rounds:
- The chain gains dWellOiledMachine, Runtime's own build and a child of dBoundRoles and dTotalRecall
  (RT-3).
  - From dDeclaredLoop it takes the `next` verb and its micro-format, the owner's pause, resume,
    withdraw and supersede, the executor's launch, the resume card fix and the compact hook, with
    `gap-found-06`, `gap-flow-10`, `gap-tool-03`, `gap-orient-12` and `gap-orient-14`.
  - From dScopedBuild it takes the worktree mechanism and the commit queue, with `gap-conc-03`.
  - From dShippedRelease it takes lander hardening, with `gap-deploy-07`.
  - dDeclaredLoop keeps the position function, which gains a closed answer set.
- dScopedBuild and dTendedCadence gain dWellOiledMachine as a parent.
- `context.on-full` now defaults to `fresh-at-boundary` in every preset (RT-1).
- Six `runtime.*` keys join the catalogue and the presets. The owner sent RT-2 back to be re-verified,
  and it adds no seventh key. Dispatch 36 found that no CLI floor is needed, so `runtime.below-floor` is
  retired. Every version fails closed through ask rules on gated tools that only the dispatcher answers.
- `gap-rt-01` to `gap-rt-10` join dWellOiledMachine. Two proposed gaps restated `gap-maint-01` and
  `gap-maint-07`, so those rows took the runtime review's corrected facts instead.

Revised: 2026-10-15, after the review system's research
(`build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md`) and the owner's R-1 to R-3:
- The chain gains dFairHearing, the review harness's own build. It is a child of dClosedLoop, so it
  lands early. It carries:
  - the design-audit preset;
  - opt-in lenses;
  - skeptic batches by address;
  - a grade per id;
  - twins shown to the synthesizer;
  - fix verdicts by class, and gates with a home.
- dCalibratedLens gains dFairHearing as a parent, and draws its per-stage lenses from that build's
  catalogue.
- `review.opt-in` joins the catalogue and the presets.
- `gap-review-04` to `gap-review-09` join dFairHearing.

Revised: 2026-10-16, after two Tier-2 rounds on each of layers 1 to 4
(`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`) and the owner's LR-1 to LR-6,
folded layer by layer, each layer record's `[revised]` naming where every defect went:
- **The instruction layer:**
  - `instructions.proof` joins the catalogue, and presets never touch it;
  - dOrderedCharter's row:
    - instruction units replace governing documents;
    - the layer kind gains its factory and conformance gate;
    - tag names get a core shape check, with the lexicon's vocabulary at an extension point;
    - budgets extend `template-size-limits.txt`;
    - the card reaches another harness through Runtime's harness adapter, not an override file;
  - dConvergedCharter's row moves the retired guides' rationale to `help/`;
  - `[layers]`:
    - core writes decisions and research, and Knowledge consults them;
    - Runtime's row follows the runtime layer;
    - an expansion fills a core render only through an optional slot;
  - `[owed]` gains dOrderedCharter's policy consumers;
  - the renumbered ladder supersedes "rank 1" in the notes above: the charter holds level 0 and the
    card level 1;
  - `gap-rt-11` to `gap-rt-13` join dWellOiledMachine.

## [layers] The product's layers

A layer is a capability named by a tag. A kit implements layers, and its descriptor declares the layer
and the extension point that each of its parts serves (P28). One test sorts them: the core alone
carries one build from request to landing, and an expansion is never needed for that (layers round
one, `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`).

| Layer | Kind | What it is |
|---|---|---|
| `instruction` | core | everything an agent is told, levelled 0 to 7 and tagged by scope |
| `flow` | core | a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as breakpoints, with the verdict engine and the lander |
| `roles` | core | the bound workers, and the driver |
| `memory` | core | the build trail: records, transitions, witnesses, the card's truth |
| `runtime` | core | what executes the cycle: the supervisor and its checklist engine, act sessions and the spawn harness, the `next` verb and the owner's controls, the hooks, isolation, process supervision |
| `knowledge` | expansion | what agents consult to decide: the map, bug classes, the lexicon, and the recall of decisions and past research, whose records the core writes |
| `observability` | expansion | signals about the loop and the runtime, and the cadence steps that act on them: Maintain and the Loop Review |
| `integrations` | expansion | adapters to outside services: remote CI, notifications, cloud hosts, trackers, and deploy engines that promote a landed tree through environments |
| `distribution` | expansion | the product's delivery: govkit, the adopt scripts, overlays, the install of the render targets Runtime's harness adapters define, currency |

The core is a cycle on a base:
- instruction directs the flow;
- the flow names items;
- roles perform them;
- their returns become memory;
- memory renders the card and feeds `next`;
- runtime executes the cycle and enforces what the instruction layer states.

Every layer fills one contract, whether core or expansion:
- its tag and definition;
- its instruction units;
- its engine kits;
- its record kinds;
- the extension points it declares, and those it uses;
- its policies and its gates.

A work-order field, or any part of a core render, that an expansion fills is an optional slot, rendered
empty on a core-only install. The kit-to-layer map is in the layer record. The layers are reviewed one
by one with the owner, each in its own layer record.

## [principles] What every chain build implements

- **P1 One loop, declared once.** A new loop kit owns WHAT each stage takes in, hands out and proves,
  and the policy schema; the roles kit owns WHO does the work, its workflows naming loop stages by
  id (walk S1b). Every shipped part declares its stage; a coverage gate reds an unclaimed part.
- **P2 Witnessed hand-offs.** A stage exit is computed from committed history, a hook-written record
  or a verifier's verdict, never from state the acting agent typed.
- **P3 Local-first verdict.** The local hook is the default and first-built verdict path, because
  remote CI is not available (R4.4); a peer-node verifier ships as a switchable backend (R5.2);
  remote CI is a designed slot.
- **P4 One contract, two authorizations.** Attended and unattended work run the same stage
  contracts; the autonomy level decides which transitions need the owner (R1.4).
- **P5 Concurrency by lease, inside the flow.** Builds, units and cadence runs hold remote leases, and
  builds reach each other through a durable mailbox; both are the flow's own mechanics, built with the
  loop and never by a separate build, and overlap warns by default (R2.2; coordination record).
- **P6 Maintain closes the loop, as an expansion.** The core flow carries a build from request to
  landing in five steps. Maintain, delivered with the observability expansion, runs over what landed,
  on its cadence and its events. It turns declared safe fixes into patch builds and files everything
  else into Plan's triage. Without it, the loop closes through requests alone (R2.3; layers round
  two).
- **P7 Review at breakpoints.** Review is not a step. A breakpoint declared at any item boundary
  pauses the flow until a reviewer lens or the owner disposes it, and every review that runs blocks.
  Agent review is opt-in except the closing review. Every transition carries a recommendation: its
  score is computed, and its reasoning is returned by the step's producing role. The Loop Review,
  with observability, prunes (R2.1, R3.2; layers round two).
- **P8 Every adopter is an adopter, gov included.** The charter is the shared foundation; each
  repository's own rules render from its own overlay as a separate project block (walk CV1).
- **P9 Measured weight.** A value ledger prices gates, rules and bug classes; caps are re-derived
  from evidence of when they blocked work and when they stopped bloat (walk R4).
- **P10 Flexible and configurable.** Every behaviour is an owner-switchable policy whose default is
  the owner's answer and whose allowed values are the options offered (R2.4, walk C3, walk T3);
  structural choices are decisions, not policies. One policy file, one reader, one guard.
- **P11 Everything loaded gives direction.** Every loaded unit is one of six statement types: a
  directive, a constraint, a definition, a pointer, a policy value or a derived fact. Prose that bears
  no load does not exist, and headings are directives. Render provenance never loads, and neither
  does a typed fact that can go stale. Sections, checklist items and layers are named by tags that
  survive reordering, never by numbers or `§` references (walk CV2; layers round one).
- **P12 Specs are structured contracts.** A spec gives a builder precise, deterministic, structured
  instructions: definitions, design, boundaries, interfaces and acceptance as fields a check reads
  (walk D3).
- **P17 Features carry the design between units.** A build decomposes into features and each feature
  into units; a feature's design declares its units' interfaces structurally, so a change is classified
  mechanically and re-design happens at the unit or the feature as the change requires (flow FL-D2,
  FL-D4, FL-D5).
- **P18 Decision principles outrank practices in unattended forks.** Agents resolve forks by the most
  feature-rich option, then the most expandable, with a full record; the charter's practices govern
  and are adjustable, and yield to these in a fork; only options the core admits are options (flow
  FL-D3, FL-D6). No build parks on an unresolved fork: the role that meets it resolves it by these
  principles and records it, a fork the goal cannot survive included, whose plan revision proceeds
  under the request's mandate (flow-roles FR-4, FR-12).
- **P19 Built work is never rewritten in place.** A built unit's spec is frozen; every later change,
  a review finding's fix included, arrives as a new unit with its own spec, so the trail is complete
  (flow FL-B3).
- **P20 The flow is the layer above the build.** A build passes five steps, Plan, Design, Build, Test
  and Deploy, from its fixed entry point: complex features enter at Plan, in-goal amendments and patch
  builds at Design. Each step is a deterministic, mechanically enforced program of items, and the
  build carries each step's records. A build ends landed, withdrawn or superseded. Nothing changes
  tracked content outside the flow. Builds run unattended past Plan by default, with the executor
  running the steps (flow record, walked 2026-10-14; layers round two).
- **P21 Builds coordinate before they wait.** A build's step is its least-advanced unit's; a dependent
  build messages the sessions of the builds it depends on, live where it can and through a durable
  mailbox always, builds on interfaces once confirmed, and waits for its parent's landing only when
  it cannot reach them; landings go in plan priority, then first verified (flow interactions).
- **P22 Position is derived, never remembered.** Every request gets a recorded disposition whose facts
  are checked; a session's build, step, next item and actor are then computed from witnesses by one
  engine, `next`, and a build's saved card lets any session on any node pick it up in one step
  (orientation record).
- **P23 Claims are trusted by key and source.** A claim is acted on only when its stored key recomputes
  equal and its weakest source is not typed by an agent; otherwise it is re-derived, or held as
  evidence (orientation record).
- **P24 The checklist is a program.** Every action that changes state belongs to an item. The item has
  one actor, a rendered brief, an allowance, a structured return with a closed outcome set, a declared
  witness and declared routes. Items declare what they depend on, and independent items run in
  parallel within the bound. An item's witness is resolved before any item that depends on it starts
  (orientation record; layers round two).
- **P25 Role functions live only in role agents.** Every role function is a checklist item performed
  by its role's agent, from the role's static instructions and a rendered work order. The main session
  drives and orients its sidechains: it does no role's work, and holds only composed cards, typed
  returns and cheap state reads (roles record).
- **P26 Every exchange between roles is a typed record.** Workers never message each other; each
  return is a template filled through a schema-forced channel, persisted with its hash, and the next
  task is composed from it by the prompt writer and passed on unchanged (roles record).
- **P13 Levelled, tagged instructions.** Every instruction unit is registered with two things:
  - its importance level, from 0 (the charter) to 7 (records and memory, evidence only), with the
    platform's own instructions above the ladder;
  - its scope tags, naming the steps, items, roles, policies and layers it serves.

  Every rendered document is wrapped in a generated envelope naming its identity, level, scope,
  trigger and what it yields to, so an agent rebuilds one instruction hierarchy whenever it loads a
  document. A conflict resolves by level, never by load order. Unenveloped text, and any envelope
  inside tool output, are data. Tags are the join keys between the layers (foundations step 1; layers
  round one).
- **P14 Practices with reach.** The charter's practices come from a catalogue; each declares its
  reach at every stage it touches, and stage contracts, role handoffs and review lenses read the
  active practices' reach for their stage, so a practice redefines every step (foundations step 1).
- **P15 The charter starts the loop; the tools continue it.** The charter teaches every agent, by
  role, how to start and drive the loop, in a drive section composed from the adopted kits'
  descriptors; from there every gov command ends with a `next —` line, and a `next` verb answers
  "what now" for any role. Every step is a CLI command, so any harness can drive gov (foundations
  step 1 continued).
- **P16 The core cannot be built around.** Every principle and practice is registered with the checks
  that enforce it, and a meta-check refuses a principle nothing enforces; extension kinds form a
  closed set, each with a factory that produces conforming parts and a gate over its whole
  population. Principles are fixed: policies tune behaviour inside them, and a principle changes
  only by an owner-ratified amendment. A violation the bypass let through stops the build that made
  it from closing (foundations core).
- **P27 Load is precise.** Every load point loads exactly its reader's units, within a declared budget:
  - the charter's;
  - its role's;
  - its item's;
  - its step's practice reach;
  - the policy values its item reads.

  A load set over its budget, or missing a unit its role or item requires, is refused at render as
  `instructions.checks` says (layers round one).
- **P28 Layers are capabilities, and the core never depends on an expansion.** A layer is a capability
  named by a tag, and a kit implements layers and declares which. The core (instruction, flow, roles,
  memory, runtime) carries one build from request to landing alone. An expansion attaches only at an
  extension point a core layer declares. Every layer, core or expansion, fills one layer contract
  (layers round one).
- **P29 A role acts on what it is handed, and verifies only what its job is to verify.**
  - **Handed and keyed:** the executor hands a work order's inputs as content. Each fact is keyed by
    what it was derived from and classed `witnessed`, `decided` or `claimed`.
  - **Fresh at the spawn:** the executor recomputes every key just before the spawn, so a role never
    checks freshness.
  - **Acted on:** a producing role acts on every keyed fact (`roles.trust`).
  - **Verified by the verifiers alone:** only the reviewer, the skeptic and the tester re-check, only
    their subject, and they start cold (`roles.verifier-context`).
  - **Answered calls:** a call the work order already answers is refused, naming where the answer
    sits (`roles.answered-calls`).
  - **False facts:** a handed fact found false is repaired, recorded in the return and filed against
    its producer's record (`roles.on-contradiction`).
  - **Recall:** recall is re-verified once, by the orientation scout at entry.

  (Layers round three.)
- **P30 Memory is declared once and written through one door.**
  - **Declared:** every record kind is declared once in the memory contract: its tag, layer, home,
    id rule, schema, writer, readers, lifecycle and check. Its template and checks are generated
    from that declaration.
  - **Written:** one `record` command mints ids, renders templates and refuses invalid values at
    the write boundary.
  - **Derived:** status, indexes, inverses and every view are generated. Relations are typed and
    checked both ways.
  - **Never instructing:** a standing directive found in memory becomes an instruction only by
    promotion through the instruction write path. A reuse entry is such a unit, rendered into
    work orders when a build's needs match (`reuse.delivery`).

  (Layers round four.)

## [front-door] The charter as the loop's first step

The charter is what every agent loads first (walk S1). Its whole content sits in the level-0
envelope, `[AGENTS.md · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them …]` … `[/AGENTS.md]`, and it reads in this order:
what gov is and how it works and is used; the precedence and override rule (level decides, never
load order; the charter wins a live conflict unless the owner explicitly overrides it, and the
override is recorded); the instruction map (the levels below it, what loads when, and how to rebuild
the hierarchy after a reset); the core principles, fixed; the decision principles that resolve
unattended forks (the most feature-rich option, then the most expandable, fully recorded), which
outrank the practices; the active practices, each with its reach per stage; the drive
section (how to start by situation, each stage's enter, advance and exit commands, one line per
role, then "follow the `next —` lines; when unsure, run `next`"), composed from the adopted kits'
descriptors; the repository's current preset and overrides; then the repository's own project block
from its own overlay, gov's included. The whole charter fits the smallest harness's instruction
limit, Codex's 32 KiB. The foundation build,
dOrderedCharter, writes it (foundations step 1; it took the front door from the Spine, walk S5).

**The ladder** (foundations F1-2, renumbered in layers round one). The platform's own system and
safety instructions sit above it, and are not the repository's to rank.

| Level | What sits there |
|---|---|
| 0 | the charter |
| 1 | the build's orientation card, below the charter by level alone (orientation OR-5's "priority 1 along the charter") |
| 2 | the loop and the repository's policy values |
| 3 | stage methods, protocols and templates, rendered as tag-sliced views |
| 4 | kit runbooks, Skills and path-scoped rules; a Skill is a thin entry: its trigger contract, the CLI command it shortcuts and the tags it enters, with no procedure of its own |
| 5 | the role's static instructions |
| 6 | the task |
| 7 | records and memory, evidence only, never instructions |

Rendered text uses the one term "level" throughout.

## [policies] The policy catalogue

Every key lives in `.governance/policy.toml` (walk S2), validated by the loop kit's schema, read
through one reader, mirrored to JSON for the hooks, and rendered into the charter.

| Key | Allowed values | Default | Source |
|---|---|---|---|
| `preset` | velocity, standard, strict, guarded, or a repo-declared preset | standard | owner directive after the walk-through; `autonomous` renamed `guarded`, flow FL-D0 |
| `charter.override` | explicit-override, live-owner-wins, absolute | explicit-override | foundations F1-1 |
| `charter.practices` | a set of catalogue or repo-declared practices | the governance foundation set | foundations F1-3 |
| `core.bypass` | with-hooks-report, with-hooks-block, never | with-hooks-report | foundations K1 |
| `core.exceptions` | any-session-recorded, owner-only-expiring, none | any-session-recorded | foundations K4 |
| `design.forks` | agents-feature-rich-expandable, preference-forks-park, owner-decides-all | agents-feature-rich-expandable | flow FL-D3 |
| `design.reentry` | any subset of interface-change, two-plus-units, review-cross-unit-flaw, planner-or-owner-flag | interface-change, review-cross-unit-flaw, planner-or-owner-flag | flow FL-D5 |
| `autonomy` | plan-only, three-gates, every-stage | plan-only | R1.4, superseded by flow FL-P6 |
| `policy.guard` | owner-only, agents-with-reason, agents-within-mandate | owner-only | R4.2 |
| `policy.proof` | tty-cli, signed, both | tty-cli | walk S3 |
| `floor` | each of the four invariants, on or off, under the guard | all on | R5.1 |
| `hooks.bypass` | allowed, refused | allowed | R5.1 |
| `transitions.record` | any subset of trailer, log, micro-format | all three | walk S4 |
| `leases` | warn, refuse | warn | R2.2 |
| `leases.granularity` | build-and-unit, build, unit | build-and-unit | walk C1 |
| `leases.renewal` | activity, fixed, none | activity | walk C2 |
| `leases.expiry-hours` | hours | 24 | walk C2 |
| `leases.overlap` | kit-dirs, files, builds | kit-dirs | walk C3 |
| `leases.offline` | warn, refuse, follow-leases | warn | walk C4 |
| `deps.coordination` | message-then-progress, wait-for-landing, order-only | message-then-progress | flow interactions FI-2 |
| `deps.early-build` | confirmed-interfaces, design-only, anything-coordinated | confirmed-interfaces | flow interactions FI-5 |
| `deps.messaging` | live-and-mailbox, live-only, mailbox-only | live-and-mailbox | flow interactions FI-6 |
| `landing.order` | plan-priority-then-first-verified, first-verified, owner-orders | plan-priority-then-first-verified | flow interactions FI-7 |
| `card.follows` | re-render-at-transition, card-per-step, fixed-at-start | re-render-at-transition | flow interactions FI-8 |
| `placement` | agent-places, declared-checked, owner-places | agent-places | orientation OR-1 |
| `placement.check` | refuse, record | refuse | orientation OR-6 |
| `kickoff.runs` | no-ready-card, opening-a-build, every-session, plan-absorbs | no-ready-card | orientation OR-2 |
| `card.store` | any subset of remote-ref, build-folder, local-clone | all three | orientation OR-5 |
| `card.snapshot` | terminal-only, every-transition | terminal-only | orientation OR-5, the adopted research |
| `actions.free` | read-only-probes, item-reads-only, recorded-anything | read-only-probes | orientation OR-3 |
| `resume.partial` | continue-item, restart-item, ask-owner | continue-item | orientation OR-4 |
| `resume.context` | fresh-when-idle, always-resume, always-fresh | fresh-when-idle | orientation OR-7 |
| `orient.budget` | record-only, warn-at-evidence-ceiling, owner-ceiling | record-only | orientation OR-8 |
| `driver.reads` | none-scout-only, state-reads-only, read-only-probes | state-reads-only | roles RL-5 |
| `prompts.author` | prompt-writer, requesting-worker-rendered | prompt-writer | roles RL-4 |
| `roles.retries` | a retry count | 3 | roles RL-7 |
| `roles.no-spawn` | executor-role-session, recorded-stand-in, refuse | executor-role-session | roles RL-8 |
| `roles.trust` | keyed, witnessed-only | keyed | roles layer F3-1 |
| `roles.answered-calls` | refuse, warn, record | refuse | roles layer F3-2 |
| `roles.verifier-context` | cold, warm | cold | roles layer F3-3 |
| `roles.on-contradiction` | repair-and-record, return, ask | repair-and-record | roles layer F3-4: the owner's answer over the recommended `return` |
| `reuse.delivery` | rendered, on-demand | rendered | memory layer F4-1: reuse entries rendered into work orders when a build's needs match |
| `annotations.grammar` | voluntary, required, pushed-at-read | voluntary | memory layer F4-2 |
| `builds.agent-root` | work-order, readme | work-order | memory layer F4-5 |
| `asks.acceptance` | refuse, grade | refuse | memory layer F4-6 |
| `builds.slug-words` | a word range | 1-3 | memory layer, the owner's words |
| `builds.slug-style` | humorous, descriptive | humorous | memory layer, the owner's words: humorous ids are a foundation |
| `builds.slug-date` | none, shown, in-slug | none | memory layer F4-7 |
| `lexicon.pin` | shrink-only, absorb, no-gate | shrink-only | memory layer F4-8 |
| `lexicon.forced` | verified, by-name, by-annotation | verified | lexicon review L-1: forced names recognised by what forces them |
| `lexicon.at-commit` | refuse, warn, off | refuse | lexicon review L-2 |
| `lexicon.drift` | refuse-new, report, off | refuse-new | lexicon review L-3 |
| `lexicon.packs` | detected-and-declared, detected, declared, all | detected-and-declared | lexicon review L-5: the owner's answer, custom packs included |
| `review.opt-in` | none, or a set of named lenses, each replacing a named default lens of its preset | none | review system R-1: the owner's answer, "Both" |
| `runtime.spawn-backend` | in-session, headless, or a registered spawn backend | in-session | runtime `[spawn]`; the spike decides the default for single-agent acts |
| `runtime.relaunch` | fresh, resume | fresh | runtime `[supervise]` |
| `runtime.act-ceiling` | hours | 1.5 | runtime `[supervise]` |
| `runtime.hold-ceiling` | hours | 6 | runtime `[supervise]` |
| `runtime.hook-failure` | closed, open | closed | runtime `[enforce]` |
| `runtime.harnesses` | a set of named harness adapters | claude-code | runtime `[harness]` |
| `plan.ratification` | request, hook-keyword, terminal-command, signed-commit | request | flow-roles FR-1 |
| `run.host` | requesting-node, os-scheduler, cloud-routine | requesting-node | flow-roles FR-2 |
| `notify.owner` | turn-micro-formats, park-and-landing, every-transition, park-only | turn-micro-formats | flow-roles FR-3 |
| `run.on-owner-question` | best-effort-recorded, park-item, park-build, stop-run | best-effort-recorded | flow-roles FR-4, FR-12 |
| `deps.landing` | hold-until-parent-lands, test-decides | hold-until-parent-lands | flow-roles FR-7 |
| `mailbox.reads` | every-item, transitions-only, every-item-amendments-at-transitions | every-item | flow-roles FR-8 |
| `review.follow-up` | after-high, while-finding, never | after-high | flow-roles FR-9 |
| `prompts.batch` | per-batch, per-task | per-batch | flow-roles FR-10 |
| `context.on-full` | compact-with-card, fresh-at-boundary | fresh-at-boundary | compaction CX-1; runtime RT-1 |
| `context.threshold` | a share of the window | 60% | compaction CX-1; read only under `fresh-at-boundary` |
| `card.pointers` | every-item, at-transitions | every-item | compaction CX-1, the owner's addition |
| `notices.record` | none, security-and-failures, all | none | compaction CX-2 |
| `instructions.checks` | refuse, warn, record | refuse | layers round one, the owner's "enforced wherever possible" |
| `instructions.edit` | owner-command-agents-propose, flow-only, command-for-all | owner-command-agents-propose | layers round one, the owner's write path |
| `instructions.proof` | tty-cli, signed, both | tty-cli | the instruction layer's fold: the instruction command's owner proof, as `policy.proof` |
| `review.breakpoints` | a set of named item boundaries | none | layers round two: breakpoints beyond those `review.<stage>` and `autonomy` declare |
| `deps.on-parent-withdrawn` | replan, adopt-parent-work, withdraw-too | replan | layers round two |
| `review.design.rounds` | one, until-no-blocker, until-no-high, until-clean, fixed-count | one | flow steps: the owner's "1 spec review by default" |
| `review.design.round-count` | a round count | 2 | flow steps; read only under `fixed-count` |
| `review.unverified` | ask, block, record | ask | flow steps |
| `tests.without-cadence` | run-at-landing, report-unrun, wait-for-expansion | run-at-landing | flow steps: the slower levels when observability's Maintain is not installed |
| `verdict` | local-hook, peer-node, remote-ci | local-hook | R1.3, R4.4, R5.2 |
| `verdict.blocks` | own-mixed-contended, every-red, own-only | own-only | walk T1 |
| `verdict.held` | peer-or-cadence, push-selected, on-demand | on-demand | walk T2 |
| `verdict.flakes` | quarantine, record, retry-only; a threshold | quarantine | walk T3 |
| `tests.product` | declared, declared-with-runners, none | declared-with-runners | walk T4 |
| `tests.landing-levels` | any subset of unit, integration, e2e, performance | unit, integration | flow FL-T3 |
| `verdict.tree` | prepared-merge, build-tip | prepared-merge | flow FL-T1 |
| `verdict.red-route` | fix-pass-or-design, always-new-unit | fix-pass-or-design | flow FL-T2 |
| `plan.authority` | planner-drafts-owner-ratifies, planner-within-themes, owner-orders | planner-drafts-owner-ratifies | R2.4 |
| `plan.unplaced` | warn, refuse-new, review-only | warn | walk P2 |
| `plan.triage` | owner-batches, rules, archive-legacy | rules | walk P3 |
| `plan.kickoff` | offer-next, binding, advisory | offer-next | walk P4 |
| `design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready | walk D1 |
| `design.overlap` | warn, refuse, index-only | warn | walk D2 |
| `build.scope` | warn-and-ask, refuse, report | warn-and-ask | walk B1 |
| `build.worktree` | per-unit, parallel-only, shared | shared | walk B2 |
| `deploy.runs` | landing-node, adopter-ci, operator | landing-node | walk DP1 |
| `deploy.promotion` | owner-approves-prod, auto-on-green, owner-approves-each | auto-on-green | walk DP2 |
| `deploy.on-verify-fail` | rollback-and-ask, halt-and-alert, roll-forward | roll-forward | walk DP3 |
| `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch | walk DP4 |
| `build.closes` | at-landing, after-release-verifies, at-landing-maintain-owns | at-landing | flow FL-DP1 |
| `release.cadence` | every-landing, daily, weekly, owner-cut | weekly | flow FL-DP2; the period is the main loop's choice |
| `maintain.host` | session-start, os-scheduler, cloud-routine | session-start | walk M1 |
| `maintain.cadence` | daily, weekly, every-session | daily | walk M2 |
| `maintain.fixes` | a set of named safe fixes | reap, prune landed, regenerate stale, defer dormant, records-only fixes, close finished run records | R2.3 |
| `maintain.on-breach` | file-ask, red-leg, report | file-ask | walk M3 |
| `maintain.events` | any subset of default-branch-red, release-verify-failed, session-start-breach | all three | flow FL-M2 |
| `patch.ratify` | auto, owner | auto | flow FL-M3 |
| `review.<stage>` | off, opt-in, owed, owed-above-tier | opt-in; Build owed | R2.1 |
| `review.<stage>.effort` | the role efforts | the role's declared effort | R2.1 |
| `review.recommendation` | advice, binding, binding-above-tier | advice | R4.3 |
| `review.build.when` | per-build, per-unit, per-landing | per-build | walk B3 |
| `review.findings` | blocker-high-own, all-own, blocker-own | blocker-high-own | flow FL-B3 |
| `review.blocks` | every-review, owed-only, none | every-review | flow FL-R1 |
| `review.left-shift` | second-occurrence, every-class, owner-selects | second-occurrence | flow FL-R2 |
| `review.recommendation.source` | scored-signals-and-reasoning, agent-judgment, signals-only | scored-signals-and-reasoning | flow FL-R3 |
| `review.loop.cadence` | weekly, monthly, every-n-landings | weekly | walk R1 |
| `review.loop.retire` | propose-ratify, demote-then-propose, report | propose-ratify | walk R2 |
| `review.loop.window-days` | days | 60 | walk R3 |
| `budgets.*` | each cap's value and its mode, hard or soft | re-derived from evidence | walk R4 |

## [presets] Named policy presets

The catalogue's keys are too many to set one by one, and switching them one at a time is how a single policy file
would rebuild the sprawl gap-spine-06 measured. A preset is a named, complete assignment of the
policy keys; a repository names one preset and overrides individual keys on top of it.

**Rules.**
- `preset` is itself a policy key; its default is `standard`. Choosing or switching a preset is a
  policy change: guarded and recorded like any other.
- The effective policy is the preset's assignment with the repository's overrides applied. The
  charter renders the preset's name and only the keys that differ from it, so a reader sees the
  posture and its exceptions, not the whole catalogue.
- Every shipped preset assigns every presettable key, and only values that key allows; a check
  refuses a preset with a key missing or a value outside the schema, and a new key cannot land
  without a value in every shipped preset.
- Presets never touch the floor, `policy.guard`, `policy.proof`, `charter.practices`,
  `instructions.edit` or `instructions.proof`: loosening
  the guard or switching an invariant off stays an explicit owner choice, never a side effect of
  picking a posture, and a methodology is a choice about the product, not a posture.
- A repository may declare its own named presets in its policy file, each extending a shipped one,
  under the same completeness check.

**The four shipped presets.**
- `velocity`: least friction, for a solo owner or an early repository. Everything warns or records,
  nothing refuses but the floor, the closing review is opt-in too, and records are kept to the
  commit trailer.
- `standard`: the default. Exactly the owner's answers in rounds 1 to 5 and the walk-through:
  guarded governance (owner-only guard, the closing review owed, flakes quarantined), the owner gating
  only the plan with builds unattended past it (flow FL-P6),
  with speed-leaning delivery (bypass allowed, auto-promotion, roll-forward).
- `strict`: maximum assurance. Overlaps and stray scope refuse, every red blocks, reviews are owed at
  Design and Build and above-tier at Test and Deploy, recommendations bind, production waits for the
  owner, failed verifies roll back.
- `guarded` (named `autonomous` until flow FL-D0): the same unattended flow as `standard`, under
  `plan-only` autonomy, with the guardrails that stand in for the owner's eyes switched on, for when
  gates are reliable: leases refuse, kickoff opens only
  planned work, recommendations bind above the tier, worktrees are per unit, production waits for
  the owner, failed verifies roll back.

`strict` and `guarded` refuse hook bypass. Until dWitnessedBar's reliability bar is met, choosing
either one will stall on the same gate problems that made the owner allow bypass (R5.1). `strict`
and `guarded` also declare the peer-node verifier, which needs a second fleet node; a solo
repository on either overrides `verdict` to `local-hook`.

| Key | velocity | standard (default) | strict | guarded |
|---|---|---|---|---|
| `autonomy` | plan-only | plan-only | every-stage | plan-only |
| `charter.override` | live-owner-wins | explicit-override | absolute | explicit-override |
| `core.bypass` | with-hooks-report | with-hooks-report | never | never |
| `core.exceptions` | any-session-recorded | any-session-recorded | owner-only-expiring | owner-only-expiring |
| `hooks.bypass` | allowed | allowed | refused | refused |
| `transitions.record` | trailer | trailer, log, micro-format | trailer, log, micro-format | trailer, log, micro-format |
| `leases` | warn | warn | refuse | refuse |
| `leases.granularity` | build | build-and-unit | build-and-unit | build-and-unit |
| `leases.renewal` | activity | activity | activity | activity |
| `leases.expiry-hours` | 24 | 24 | 24 | 12 |
| `leases.overlap` | kit-dirs | kit-dirs | files | kit-dirs |
| `leases.offline` | warn | warn | refuse | follow-leases |
| `deps.coordination` | message-then-progress | message-then-progress | wait-for-landing | message-then-progress |
| `deps.early-build` | anything-coordinated | confirmed-interfaces | design-only | confirmed-interfaces |
| `deps.messaging` | live-and-mailbox | live-and-mailbox | live-and-mailbox | live-and-mailbox |
| `landing.order` | first-verified | plan-priority-then-first-verified | owner-orders | plan-priority-then-first-verified |
| `card.follows` | re-render-at-transition | re-render-at-transition | re-render-at-transition | re-render-at-transition |
| `placement` | agent-places | agent-places | owner-places | declared-checked |
| `placement.check` | record | refuse | refuse | refuse |
| `kickoff.runs` | no-ready-card | no-ready-card | every-session | no-ready-card |
| `card.store` | remote-ref, build-folder, local-clone | remote-ref, build-folder, local-clone | remote-ref, build-folder, local-clone | remote-ref, build-folder, local-clone |
| `card.snapshot` | terminal-only | terminal-only | every-transition | terminal-only |
| `actions.free` | recorded-anything | read-only-probes | item-reads-only | read-only-probes |
| `resume.partial` | continue-item | continue-item | ask-owner | restart-item |
| `resume.context` | always-resume | fresh-when-idle | always-fresh | fresh-when-idle |
| `orient.budget` | record-only | record-only | warn-at-evidence-ceiling | warn-at-evidence-ceiling |
| `driver.reads` | read-only-probes | state-reads-only | none-scout-only | state-reads-only |
| `prompts.author` | requesting-worker-rendered | prompt-writer | prompt-writer | prompt-writer |
| `roles.retries` | 5 | 3 | 1 | 3 |
| `roles.no-spawn` | recorded-stand-in | executor-role-session | refuse | executor-role-session |
| `roles.trust` | keyed | keyed | witnessed-only | keyed |
| `roles.answered-calls` | warn | refuse | refuse | refuse |
| `roles.verifier-context` | warm | cold | cold | cold |
| `roles.on-contradiction` | repair-and-record | repair-and-record | return | return |
| `reuse.delivery` | rendered | rendered | rendered | rendered |
| `annotations.grammar` | voluntary | voluntary | voluntary | voluntary |
| `builds.agent-root` | work-order | work-order | work-order | work-order |
| `asks.acceptance` | grade | refuse | refuse | refuse |
| `builds.slug-words` | 1-3 | 1-3 | 1-3 | 1-3 |
| `builds.slug-style` | humorous | humorous | humorous | humorous |
| `builds.slug-date` | none | none | none | none |
| `lexicon.pin` | absorb | shrink-only | shrink-only | shrink-only |
| `lexicon.forced` | verified | verified | verified | verified |
| `lexicon.at-commit` | warn | refuse | refuse | refuse |
| `lexicon.drift` | report | refuse-new | refuse-new | refuse-new |
| `lexicon.packs` | detected-and-declared | detected-and-declared | detected-and-declared | detected-and-declared |
| `review.opt-in` | none | none | none | none |
| `runtime.spawn-backend` | in-session | in-session | in-session | in-session |
| `runtime.relaunch` | fresh | fresh | fresh | fresh |
| `runtime.act-ceiling` | 1.5 | 1.5 | 1.5 | 1.5 |
| `runtime.hold-ceiling` | 6 | 6 | 6 | 6 |
| `runtime.hook-failure` | closed | closed | closed | closed |
| `runtime.harnesses` | claude-code | claude-code | claude-code | claude-code |
| `plan.ratification` | request | request | terminal-command | hook-keyword |
| `run.host` | requesting-node | requesting-node | os-scheduler | os-scheduler |
| `notify.owner` | turn-micro-formats | turn-micro-formats | every-transition | park-and-landing |
| `run.on-owner-question` | best-effort-recorded | best-effort-recorded | park-item | best-effort-recorded |
| `deps.landing` | test-decides | hold-until-parent-lands | hold-until-parent-lands | hold-until-parent-lands |
| `mailbox.reads` | every-item | every-item | every-item | every-item |
| `review.follow-up` | never | after-high | while-finding | after-high |
| `prompts.batch` | per-batch | per-batch | per-task | per-batch |
| `context.on-full` | fresh-at-boundary | fresh-at-boundary | fresh-at-boundary | fresh-at-boundary |
| `context.threshold` | 60% | 60% | 60% | 60% |
| `card.pointers` | at-transitions | every-item | every-item | every-item |
| `notices.record` | none | none | all | security-and-failures |
| `instructions.checks` | warn | refuse | refuse | refuse |
| `review.breakpoints` | none | none | none | none |
| `deps.on-parent-withdrawn` | replan | replan | replan | replan |
| `review.design.rounds` | one | one | until-no-high | until-no-blocker |
| `review.design.round-count` | 2 | 2 | 2 | 2 |
| `review.unverified` | record | ask | block | ask |
| `tests.without-cadence` | report-unrun | run-at-landing | run-at-landing | run-at-landing |
| `verdict` | local-hook | local-hook | peer-node | peer-node |
| `verdict.blocks` | own-only | own-only | every-red | own-mixed-contended |
| `verdict.held` | on-demand | on-demand | peer-or-cadence | peer-or-cadence |
| `verdict.flakes` | record | quarantine | record | quarantine |
| `tests.product` | declared | declared-with-runners | declared-with-runners | declared-with-runners |
| `tests.landing-levels` | unit | unit, integration | every declared level | unit, integration |
| `verdict.tree` | prepared-merge | prepared-merge | prepared-merge | prepared-merge |
| `verdict.red-route` | fix-pass-or-design | fix-pass-or-design | always-new-unit | fix-pass-or-design |
| `plan.authority` | planner-within-themes | planner-drafts-owner-ratifies | owner-orders | planner-within-themes |
| `plan.unplaced` | review-only | warn | refuse-new | warn |
| `plan.triage` | rules | rules | owner-batches | rules |
| `plan.kickoff` | advisory | offer-next | binding | binding |
| `design.handoff` | derived-ready | derived-ready | ready-plus-audit | derived-ready |
| `design.overlap` | index-only | warn | refuse | warn |
| `design.forks` | agents-feature-rich-expandable | agents-feature-rich-expandable | owner-decides-all | agents-feature-rich-expandable |
| `design.reentry` | planner-or-owner-flag | interface-change, review-cross-unit-flaw, planner-or-owner-flag | all four triggers | interface-change, review-cross-unit-flaw, planner-or-owner-flag |
| `build.scope` | report | warn-and-ask | refuse | warn-and-ask |
| `build.worktree` | shared | shared | per-unit | per-unit |
| `deploy.runs` | landing-node | landing-node | landing-node | landing-node |
| `deploy.promotion` | auto-on-green | auto-on-green | owner-approves-each | owner-approves-prod |
| `deploy.on-verify-fail` | roll-forward | roll-forward | rollback-and-ask | rollback-and-ask |
| `deploy.currency` | pull-and-watch | pull-and-watch | push-branches | pull-and-watch |
| `build.closes` | at-landing | at-landing | after-release-verifies | after-release-verifies |
| `release.cadence` | every-landing | weekly | owner-cut | weekly |
| `maintain.host` | session-start | session-start | os-scheduler | os-scheduler |
| `maintain.cadence` | weekly | daily | daily | daily |
| `maintain.fixes` | the full safe set | the full safe set | reap and regenerate only; the rest filed as asks | the full safe set |
| `maintain.on-breach` | report | file-ask | red-leg | file-ask |
| `maintain.events` | default-branch-red | all three | all three | all three |
| `patch.ratify` | auto | auto | owner | auto |
| `review.plan` | opt-in | opt-in | opt-in | opt-in |
| `review.design` | opt-in | opt-in | owed | owed-above-tier |
| `review.build` | opt-in | owed | owed | owed |
| `review.test` | opt-in | opt-in | owed-above-tier | opt-in |
| `review.deploy` | opt-in | opt-in | owed-above-tier | opt-in |
| `review.maintain` | opt-in | opt-in | opt-in | opt-in |
| `review.<stage>.effort` | the role's effort | the role's effort | the role's effort | the role's effort |
| `review.recommendation` | advice | advice | binding | binding-above-tier |
| `review.build.when` | per-build | per-build | per-unit | per-build |
| `review.findings` | blocker-own | blocker-high-own | all-own | blocker-high-own |
| `review.blocks` | owed-only | every-review | every-review | every-review |
| `review.left-shift` | second-occurrence | second-occurrence | every-class | second-occurrence |
| `review.recommendation.source` | scored-signals-and-reasoning | scored-signals-and-reasoning | scored-signals-and-reasoning | scored-signals-and-reasoning |
| `review.loop.cadence` | monthly | weekly | weekly | weekly |
| `review.loop.retire` | propose-ratify | propose-ratify | propose-ratify | propose-ratify |
| `review.loop.window-days` | 60 | 60 | 90 | 60 |
| `budgets.*` | every cap soft | each cap's evidence-derived mode | every cap hard | each cap's evidence-derived mode |

## [floor] The default floor

On by default, each switchable only under the policy guard (R5.1): a binding verdict runs before
the default branch moves; every policy change and stage transition is recorded; the guard protects
its own switch; no stage witness reads actor-typed state. Refusing hook bypass is a policy,
`hooks.bypass`, allowed by default until gate reliability is fixed; each bypass is recorded.

## [witnesses] Local-first witnesses

Harness refusals of agent writes to the policy file, hooks and verdict refs; a policy CLI that
needs an interactive terminal; a verdict the pre-push hook writes per tree hash; build exits
re-derived from committed history at the push; a peer node that re-runs the bar on the pushed tree
where `verdict = peer-node`.

## [contracts] Stage contracts

| Stage | Takes in | Hands out | Witness | Owner gate under `three-gates` (the default `plan-only` keeps only Plan's) | Review default |
|---|---|---|---|---|---|
| Plan | a prompt, an ask, a Maintain finding, a Loop Review proposal | a build placed in the plan by priority and `parents:`, leased | the placement predicate (warn); the ratification change | plan ratification | opt-in |
| Design | a planned, leased build and its brief | a structured spec set at a revision, forks resolved, overlaps acknowledged | derived READY; the design index (warn) | the design go | opt-in |
| Build | a unit in derived READY with its lease | in-scope commits and one closing review per build | history checks at the push: scope (warn and ask), review recorded | none | owed |
| Test | a built range | a hook-written verdict per tree; gate health, flake and seen-red records | the verdict from the declared backend; OWN reds block | none | opt-in |
| Deploy | a verified tree | a landing record; kit release notes; per-SHA deploy and verify records; adopter currency | lander and engine records; the currency probe | landing authorization | opt-in |
| Maintain | the daily cadence at session start | safe fixes applied; asks filed by stage; a maintenance record | detectors pinned and owned; fixes inside the declared set | none | the weekly Loop Review |

This table predates layers round two, which changed four things:
- Maintain is an expansion step;
- owner gates are breakpoints (P7);
- Plan's witness is the hook-written intake (FR-1);
- each item's witness is declared by the loop (dDeclaredLoop).

## [chain] The chain: fifteen builds, final rosters

| Build | Stage | Parents | Planned units | Gaps owned |
|---|---|---|---|---|
| dOrderedCharter | Foundation | dClosedLoop | the practice catalogue with each practice's reach per stage, and `charter.practices`; the charter re-founded in its level-0 envelope (front door, precedence and override rule with `charter.override` and its record, instruction map, active practices with reach, hand-off to the loop, the repository's project block from its own overlay); the instruction registry and the ladder; envelopes rendered for every registered document and the gate over them; the instruction map re-injected on compact and resume; ranked envelopes in every subagent handoff; the section-tag grammar and its resolver; the drive section composed from a drive table in each adopted kit's descriptor, checked both ways, each subagent's role line repeated in its handoff, the charter held inside 32 KiB; the core: the principle registry, the meta-check, the kinds register with each kind's owning build, the conformance-gate contract, the exception register and the `core.*` policies, and the factories and gates for instruction units, practices, Skills and layers; the build's card delivered at level 1 through an ignored per-worktree card file the charter's entry file imports, re-rendered by every session-start hook in the session's own tree, subagents' slices through the brief and the subagent-start hook, another harness's through its Runtime harness adapter, never an override file, which for Codex would replace the charter, after the primary-to-worktree compaction fixture passes; the instruction-unit registry (per unit: tag, level, statement type, scope tags, trigger, budget class, source, owning kit), documents rendered from units; the namespaced tag system (reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit), joined both ways over non-empty populations, its names shape-checked in the core and the lexicon's vocabulary added at an extension point; load sets derived per reader and item, budgeted per load point and per harness, extending `template-size-limits.txt`, refused at render when over budget or missing a required unit (`instructions.checks`), injected load points measured; the statement grammar and its check, render provenance in a sidecar lock; the ladder renumbered, the platform above it and the charter at level 0; memory instructing nothing, a standing directive promoted into a unit; the instruction manifest and its guarded write command (`instructions.edit`, `instructions.proof`), its checks also a leg over the tree, instruction packs extending `charter.practices` into the preset catalogue; the layer register, the layer contract, the layer kind's factory and conformance gate, and the check that the core never depends on an expansion | gap-found-01, gap-found-02, gap-found-03, gap-found-04, gap-found-05, gap-found-07, gap-found-08, gap-flow-02, gap-orient-13, gap-found-09, gap-found-10, gap-found-11, gap-found-14, gap-found-15, gap-found-17 |
| dFairHearing | Review harness | dClosedLoop | the owed replays first: the design-audit preset run blind at blob 767187aa in a worktree at 6cfd21619, the verify stage with batches by address, the synthesis with twins shown, and aRoutedQuill #23's fix re-judged by class; the design-audit preset for design and architecture records, chosen by the subject's kind (coherence; grounding flagging untested assumptions; reuse held to precedent; failure-envelope extended to trust boundaries; alternatives-and-cost in place of blast-radius); opt-in lenses (security, precedent, assumptions, alternatives, cost, portability, adopter migration, topology), each replacing a named default lens of its preset under the five-per-array limit, chosen by `review.opt-in`; skeptic batches sorted by cited address; duplicates counted as merged confirmations, with the orphan check on both kinds; items carrying a grade per id, ranked by the highest; refuted claims and same-address twins handed to the synthesizer to flag; fix verdicts judged by class, and every proposed gate naming an existing leg, suite or bug class from a manifest the harness hands over; portability, topology and adopter migration as universal bug classes, with lens notes passed by the driver; the review records brought back in line with the code (REVIEW-PROTOCOL.md's lens list, lens count and skeptic default, agent-cap's lens comment, and the synthesizer role's input line) | gap-review-04 to gap-review-09 |
| dDeclaredLoop | Spine | dOrderedCharter | the loop kit and definition keyed by the stage tags, the roles kit's stage table moved and its seven readers re-pointed in the same unit, never waiting for a live build's close; `.governance/policy.toml`, schema, one reader, JSON mirror; the named presets and their completeness check; the guard, the TTY CLI and the default floor; the transition record three ways; stage claims and the coverage gate; the witness-class rule; policy at govkit intake; the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows; the coordination feature: one lease grammar for builds, units and cadence runs with run claims migrated onto it, acquired, renewed, released and taken over through CLI verbs the step checklists call, overlap warned or refused, fleet identity and uniqueness against the remote, offline behaviour; the mailbox per build, its closed set of message kinds checked on write, read and disposed at every transition, shown on the card and kept in the build's transition log; live delivery where the harness has it; dependency coordination by the parent's lease, interfaces confirmed at Design's exit, change and landing notices; the position engine: deriving each unit's step, the build's step, the next item and its interrupts from witnesses, items idempotent by witness and keyed by round or pass and input SHAs, answering from a closed set (act, blocked, terminal, stuck, invalid-input, stale-remote), the read set and each claim's key and verdict printed; the build's orientation card at level 1, below the charter, kept as a ref per build on the remote (the truth), cached in the clone by build and object id and snapshotted into the build folder per `card.snapshot`, the stores selected by `card.store`, looked up and re-keyed in the session's own tree on resume, a fresh session recommended by `resume.context`, partial work handled by `resume.partial`; claims keyed and trusted by key and source; each step's items declared with actor, inputs, allowance, return schema and witness; `actions.free` at the tool call; orientation cost recorded per stage; backward transitions recorded like forward ones; the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind; progress reported by `notify.owner`; a fresh session in the build's worktree recommended until the card-import fixture passes; the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compacted or fresh session reorients from them; what a session does as its window fills, by `context.on-full` and `context.threshold`; a compaction's summary read as a lead, never a source; every checklist item named by a semantic tag, its number only display order; each step a program of items with declared dependencies, every item declared with its tag, actor, inputs by layer, instruction scope, allowance, return template and closed outcome set, computed witness and routes (the item audit's tables as input); one transition table per level (build, feature, unit), the engine refusing any transition it lacks; a default failure route (the refusal recorded, `next` naming the first unwitnessed item); terminal states landed, withdrawn and superseded, and `deps.on-parent-withdrawn`; one closed disposition set; witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, red attribution joined to the verdict) | gap-spine-01, gap-spine-02, gap-spine-06, gap-design-01, gap-flow-07, gap-conc-01, gap-conc-02, gap-flow-06, gap-orient-02, gap-orient-03, gap-orient-04, gap-orient-05, gap-orient-06, gap-orient-08, gap-orient-11, gap-flow-13, gap-flow-14 |
| dBoundRoles | Roles | dDeclaredLoop | the roster sorted by layer: twelve core roles (orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, tester, one reviewer with a lens per step, skeptic, synthesizer), and the deployer and maintainer as expansion roles registered through the integrations and observability layer contracts, with the reviewer's maintenance-run and loop lenses; each role's static instructions as structured fields, every limit paired with its enforcer, a ceiling of tools, write classes and gate legs, and a typed return template; the work order rendered per item (the item, its inputs as record fields at their SHAs, its allowance, its return template, its witness), hashed into the spawn marker and bound to the agent's calls by its agent id; the prompt writer composing every role's task from the driver's details; the orientation scout composing the card in a sidechain at session start; returns through a schema-forced channel, residual failures retried by `roles.retries`; the role index and agent files beyond every worker's reach, a tree with no index refused, `role-sha` compared at spawn; shell writes held to the allowance; the role-gate arm's field escape explained and closed; the `none` and `review` write classes enforced; `driver.reads`, `prompts.author` and `roles.no-spawn`; every fork resolved by the role that meets it and recorded, never parking a build (`run.on-owner-question`); prompt-writer calls batched by `prompts.batch`; a return's harness notices persisted with it, by `notices.record`; work-order fields an expansion fills (bug classes, the map's dossiers) declared as optional slots; the orientation scout's return carrying the placement disposition and its reason, the driver recording it and running `placement.check`; the trust mechanism (P29): inputs handed as content, each fact keyed and classed by the executor and re-cut fresh at the spawn; each role's trust profile and context temperature declared and rendered (`roles.trust`, `roles.verifier-context`); the answered-call hook (`roles.answered-calls`); repairs recorded in returns and filed as asks against the producer's record (`roles.on-contradiction`); the role files' re-verification orders and protocol pointers replaced by rendered slices; the role-by-step matrix derived from the item declarations and joined both ways; role metrics per role and item into the value ledger, accepted against `role_orientation.py`'s baseline | gap-roles-01, gap-roles-02, gap-roles-03, gap-roles-04, gap-roles-05, gap-roles-06, gap-roles-07, gap-roles-08, gap-orient-07, gap-orient-09, gap-roles-09, gap-roles-10, gap-roles-11, gap-roles-12, gap-roles-13, gap-roles-14, gap-roles-15, gap-roles-16, gap-roles-17, gap-roles-18 |
| dTotalRecall | Memory | dDeclaredLoop | the memory contract: the record-kind registry (per kind: tag, layer, home, id rule, schema, writer, readers, lifecycle, check), templates and checks generated from it, and `HYGIENE.md`'s prose rendered as its view; the one `record` write command, which mints ids, renders templates and refuses invalid values; the build README's declared front-matter schema, with unknown keys refused, `node`, `roster` and `streams` derived, a generated routing region by purpose, and the work order as each agent's root (`builds.agent-root`); the slug and id grammar exported once and read by every slug and id reader (`builds.slug-words`, `builds.slug-style`, `builds.slug-date`), proven by flipping the grammar in a scratch clone; typed relations (`depends-on`, `patches`, `amends`, `supersedes`, `implements`), inverted, checked both ways and rendered as the relation graph; the ask kind's acceptance at filing (`asks.acceptance`); decisions split by kind: reuse entries as level-3 instruction units beside their dossiers and in `FOUNDATION`, promoted through the instruction write path, the major-decision log with its holds-now view, today's 200 rows routed by two raters at kappa 0.8 or better, and the `[records]` rule reworded; the reuse scout's house index (symbols, callers, dossiers, reuse entries), delivered through the card's `reuse` slot (`reuse.delivery`); `reuse_lookup.py` retired with its readers rewritten, and memory-recall narrowed to a record finder; the caller map: every Python definition, import-aware calls, shell and JavaScript edges under the ambiguity test, cross-language invocation edges, freshness-checked, with dossiers anchored to symbol keys; the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries, the generated annotation index and its resolve check (`annotations.grammar`), the shipped-evidence signal re-checked first; gotchas handed by write set; the generated views: README routing, the relation graph, the decisions' holds-now view and the reuse view | gap-mem-01, gap-mem-02, gap-mem-03, gap-mem-04, gap-mem-05, gap-mem-06, gap-mem-07, gap-mem-08, gap-mem-09, gap-mem-11 |
| dMindYourWords | Lexicon | dTotalRecall | the definition classes (conforming, forced, out of scope, not a name, debt), with only debt counted against the shrink-only pin (`lexicon.pin`); forced names recognised by what forces them (`lexicon.forced`): packs keyed by base member, base prefix and host namespace, applied only where the site resolves statically through its imports to that base, against committed pack data; gov's own contract-forced names declared beside the reader that keys on them, with a stale arm; override markers verified against the packs; a reasoned site suppression as the owner's counted fallback; `--suggest` made forced-aware; the packs, generated per host kit (`inspect` per Python minor, wheel AST, pluggy hookspecs, `.d.ts`), shell hosts curated, each with its kit, version range and generator command: the first wave (the data model, the commonly subclassed stdlib bases, unittest, pytest, argparse, `ast`, `http.server`, `logging`, `json`, `cmd`, the shell hosts), and the second wave (Django, Flask, Starlette, FastAPI, React) after an adopter-side census; packs detected from the import census and manifests and declared by the owner, custom packs included (`lexicon.packs`); enforcement: the work order's vocabulary slice and forced-aware answers, staged definitions checked at commit (`lexicon.at-commit`), and the branch's offenders compared with its base's by name at the bar, with move-aware keys proven by replaying the merges since 2026-08-16; drift beyond verbs (`lexicon.drift`): one verb per family per object, and a noun canon seeded from the corpus and frozen; the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and the `init` row re-justified; one extraction, with the lexicon classifying the map's definitions and the dependency inverted; the kit's defects fixed: repeated block headers refused, IIFE values and properties ungraded, the dead modes, and the Skill, conf and README reconciled; records kept out by the path selector | gap-mem-10, gap-lex-01, gap-lex-02, gap-lex-03, gap-lex-04, gap-lex-05, gap-lex-06, gap-lex-07 |
| dWellOiledMachine | Runtime | dBoundRoles, dTotalRecall | the platform spike first: a role-typed Workflow agent run inside a headless act session, with the headless backend measured beside it; the `next` verb over the loop kit's position function, the `next —` micro-format, and the check that every declared command ends with one or declares itself terminal, laggards on a shrink-only list owned by their stage's build, with the readers of `--plan` and `--status` re-pointed; the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto unattended's verbs; the supervisor: `resume-tick.sh` grown, started and restarted by the node tick, the executor launched where `run.host` says, its liveness its build lease's beat, one act session per role act, relaunch capped by `RESUME_ATTEMPTS`, limit holds, fencing epochs, command adapters that are idempotent or reconcile, and shared records written by the supervisor alone; act binding at the Workflow, Agent and shell call, with in-script spawns declared and reconciled; the persisted-return store and the shared deferral block; agent slots reserved under agent-cap's cap; the one enforcement surface: the kits' fragments as packs, one dispatcher entry per event, ask rules on gated tools that only the dispatcher's PermissionRequest entry answers, `onFailure` wherever the CLI carries it, the owner-pack table, witnesses with named readers, signal traps on every git hook, the trusted hooks copy, and lander hardening, the lander a versioned command adapter with its dependency on the bar's kit declared; workspaces by `build.worktree`, the commit queue, integration before release and the sweep; sessions bound on every source, a resume that delivers no card diagnosed and closed, the compact hook re-injecting the build's current card, never the kickoff's, the PreCompact flush and the keep-list; the scheduler's host adapters and per-period cadence witnesses; harness adapters with capability tables; the node registry's runtime facts; the journal grammar moved into the core | gap-rt-01 to gap-rt-13, gap-found-06, gap-flow-10, gap-tool-03, gap-orient-12, gap-orient-14, gap-conc-03, gap-deploy-07 |
| dWitnessedBar | Test | dDeclaredLoop | gate health measured and the reliability bar; bypasses recorded; attribution deciding what blocks; the hook-written verdict; held legs by policy; the peer-node verifier; seen-red records; flake quarantine; the product-test contract with runner adapters; derived pre-commit list and multi-node cost evidence; the gate-leg factory and its conformance gate, every leg declaring the principles it enforces | gap-test-01, gap-test-02, gap-test-03, gap-test-04, gap-test-05, gap-test-06, gap-test-07, gap-test-08, gap-test-09, gap-flow-09, gap-tool-01 |
| dRankedPlan | Plan | dDeclaredLoop | priority beside `parents:` and the generated plan view; the planner and triager role and Plan workflow; the placement predicate; rule-based triage; dormancy disposal; the live-build mapping carried out; Plan Review; kickoff offering the next item and attended briefs gated; placement: a disposition for every request, made by `placement` and recorded with its reason in the intake record, its facts checked by `placement.check`, an unattended prompt placed the same way; the full kickoff only where `kickoff.runs` says; the prompt-submit hook writing each owner prompt verbatim to the session's intake log, and the request as the ratification by `plan.ratification` | gap-plan-01, gap-plan-02, gap-plan-03, gap-plan-04, gap-plan-05, gap-plan-06, gap-plan-07, gap-flow-03, gap-flow-04, gap-orient-01 |
| dIndexedDesign | Design | dDeclaredLoop | the derived-READY hand-off; the design index; design review by policy; reuse and alternatives backed by recorded probes; the research harness; agreement and tier checks; the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract; the feature level (build, features, units) with each feature's interfaces declared structurally, two-level re-entry by `design.reentry`, additive-versus-breaking interface classification (proposed), fork resolution by `design.forks` | gap-flow-01, gap-design-02, gap-design-03, gap-design-04, gap-design-05, gap-design-06, gap-design-07, gap-design-09 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar, dWellOiledMachine | one exit contract with a history-derived base, refusing a build's exit while a core red its own commits introduced stands; built specs frozen, every closing-review finding disposed as new units by `review.findings`; scope at the push; the closing review recorded; a write gate reading derived state; the checklist witnessed; the core checks run by the executor at Build's exit | gap-spine-03, gap-build-01, gap-build-02, gap-build-03, gap-build-04, gap-flow-05 |
| dShippedRelease | Deploy | dWitnessedBar | the landing record; kit release notes; the deploy engine; the incms adapter; the fleet register and currency watch; optional emitted CI; a derived runbook; the kit factory and its conformance gate; a dependent's landing held until its parent lands (`deps.landing`); landings through the existing turnstile queue; the lander running the core checks on the landed tree before it releases the build, so a core red the landing merge introduced stops that build from closing (foundations K1); the landing review blocking the build's close rather than the push; promotion after landing through environments as an integrations extension point | gap-deploy-01, gap-deploy-02, gap-deploy-03, gap-deploy-04, gap-deploy-05, gap-deploy-06, gap-deploy-08, gap-flow-08, gap-tool-02, gap-tool-04 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan, dWellOiledMachine | the Maintain run as its step checklist on the flow's executor, never a recipe-mode playbook; the cadence, on Runtime's hosts; the safe-fix set; detectors with owners; map freshness; the maintenance record; a detector for the memory's dead pointers, owned by Maintain; Maintain and the Loop Review delivered as cadence steps of the observability expansion, detectors registered by layer, patch intakes rendered from keyed detector readings, event runs keyed by event | gap-maint-01, gap-maint-02, gap-maint-05, gap-maint-06, gap-maint-07, gap-maint-08, gap-orient-10 |
| dCalibratedLens | Review | dTendedCadence, dFairHearing | review by policy per stage and effort; the stage-exit recommendation; lenses for Plan, Test, Deploy and Maintain, drawn from dFairHearing's catalogue; the shared value ledger; the weekly Loop Review; caps re-derived from evidence and review cost; follow-up closing-review rounds by `review.follow-up`; instruction effectiveness measured from returns and findings that cite unit tags, the Loop Review pruning units that bear no load and tightening those broken often; breakpoints placeable at any item boundary (`review.breakpoints`), reviews and owner gates one mechanism with `review.<stage>` and `autonomy` its default declarations; the recommendation's score computed and its reasoning returned by the step's producing role | gap-review-01, gap-review-02, gap-review-03, gap-maint-03, gap-design-08, gap-found-16, gap-flow-11, gap-flow-12 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens | protocol text derived to facts only, each document in its envelope; every remaining positional reference migrated to tags; records merged by evidence; superseded parts retired through ratified proposals; adopters migrated onto the ranked charter and the loop; the record-kind factory and its conformance gate; protocols and templates rendered as tag-sliced views from the loop's checklists, the roles, the record schemas and the policies, the hand-written guides retired and their rationale moved to `help/`; Skills converged to level-4 thin entries, each described "Use when …; runs …" | gap-spine-04, gap-spine-05, gap-maint-04, gap-found-12, gap-found-13, gap-tool-05, gap-tool-06 |

The live-build mapping is v1's table with one change: no chain build waits for a live build to close
or relies on what it delivers, so "after it closes" no longer holds. The active builds finish on
their own track (R3.3); the chain build covering each one's area builds what the design needs, and a
concurrent change is reconciled in Test's prepared merge (FI-3). The Plan build carries the mapping
out with the owner's ratification and confirms dPolishedVitrine's track, which went dormant on
2026-10-14.

## [open] Interpretations to confirm at chain approval

- Positional section references other than `§` (numbered method steps such as `M5`, numbered spec
  sections, numbered hygiene checks) carry the defect walk CV2 names, so the tag grammar would
  replace them too, inventoried by Convergence.
- Coordination (`build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`, `[interpretations]`): a
  parent is reachable while its build lease is live, with no separate timeout; Design's exit posts each
  frozen feature's declared interfaces to the dependents' mailboxes; a transition is refused while a
  message addressed to the build is neither answered nor acknowledged; the lease carries the build's
  verified tree for the landing order; each transition keeps the messages it disposed in the build's
  transition log, and Maintain prunes a closed build's mailbox ref once its folder holds them all.


- The session model (`build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md`, `[holes]`): fourteen
  places where the settled design is silent or does not hold together when one build is walked
  through every step, H1 to H14, and two more found with roles, H15 and H16: all settled in the
  flow revisit (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`, `[closed]`).

## [owed] Owed to the chain re-cut

- **Settled by the runtime layer** (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`):
  - the flow's executor and its checklist engine: dWellOiledMachine owns them (RT-3);
  - the executor's harness: Runtime's `[spawn]`, with act sessions and a persisted-return store. The
    turnstile landing queue stays Deploy's;
  - the compaction checks (CX-3): disposed in Runtime's `[sessions]`, with `context.on-full` settled
    by RT-1.
- The roles layer's lower-level design (layers round three):
  - how the answered-call hook matches a Read's range against the handed ranges at the blob SHA, and
    which Bash readers it parses;
  - how the executor cuts and keys excerpts;
  - how a repair's ask carries the repaired fact onward until the producer's record is fixed.
- **The expansion roles' home.** At the re-cut, the deployer's and the maintainer's definitions move to
  the builds that deliver integrations and observability. dBoundRoles keeps their registration
  through the layer contract.
- **The roles layer's mechanical shape**, for the revisit the owner set when round four opened. Each
  role item's execution shape is declared: its agent set, effort, checklist, orientation template
  and merge. aScoutedSeam's benchmark is the evidence (layer-roles `[owner-notes]`):
  - one checklist scout matched a two-scout workflow with a judge, on a third of the agents;
  - a scout that reads a generated house index first raised recall from 13 to 16 of 24;
  - two independent medium Tier-2 rounds on the runtime design each found about three quarters of
    their union of 59 defects (`build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md`).
- **dTotalRecall's place in the re-cut.** Two chain builds consume what dTotalRecall builds:
  - dIndexedDesign's "reuse and alternatives backed by recorded probes" uses its house index and
    reuse entries;
  - dTendedCadence's "map freshness" runs on its caller map.

  The re-cut therefore orders dTotalRecall ahead of both.
- **The tooling order** (memory layer `[tools]`). Dispatch 26 picks "Flow first". Its objection to
  starting with the instruction layer assumed that step tags come from the loop kit, but the step
  definitions already declare them. The re-cut weighs both orders.
- **dMindYourWords' second-wave packs need an adopter census.** Django, Flask, Starlette, FastAPI and
  React each ship only after a census in an adopter shows their names actually offend. That census
  is adopter-repository work, so it waits for the owner's ask at that build.
- **The `next` verb now lands with Runtime** (RT-3). Every stage build whose commands must end with a
  `next —` line depends on dWellOiledMachine, which lands after dBoundRoles and dTotalRecall. The
  re-cut either orders dWellOiledMachine ahead of those builds or lands its `next` unit first.
- **Kit confs beside the policy file.** Every key is said to live in `.governance/policy.toml`, yet
  Runtime reads `FANOUT_CAP`, `PROCMON_REAP_MODE`, `RESUME_ATTEMPTS` and `RESUME_TURNS` from kit
  confs. Whether those confs fold into the policy file is undecided.
- **dOrderedCharter's policy consumers** (the instruction layer's fold). The load-set refusal and the
  guarded write command read `instructions.checks`, `instructions.edit` and `instructions.proof`, and
  the charter renders the repository's preset. Yet the policy file, its schema, its one reader and the
  guard land with dDeclaredLoop, dOrderedCharter's child. The re-cut moves the policy file, schema and
  reader into dOrderedCharter, or orders those units after dDeclaredLoop.

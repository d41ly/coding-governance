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
- **The flow layer** (flow-steps' `[revised]`):
  - `flow.route-backs` joins the catalogue and every preset: a route back, a review round included,
    becomes an owner item past it;
  - `policy.on-missing-expansion` joins the catalogue after LR-4, `refuse` by default, and presets
    never touch it;
  - dShippedRelease builds a landing queue (`gap-flow-08`), since the turnstile is a bar semaphore;
  - `[owed]` and `[open]` follow: the landing queue stays Deploy's, and the close program prunes a
    closed build's mailbox;
  - `gap-flow-15` joins dDeclaredLoop, and `gap-rt-14` joins dWellOiledMachine.
- **The roles layer** (layer-roles' `[revised]`):
  - P29 is amended after LR-2: a claimed fact guides and never decides, keys are fresh at act launch,
    and an answered call is one whose handed answer still holds;
  - dBoundRoles' row binds a work order by task-sha, and measures answered calls from the hook's
    records;
  - the matrix is derived from each Actor cell's opening, and its three arms are seen red.
- **The fold's closing review** (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`):
  - dDeclaredLoop's failure route returns the frontier, dBoundRoles' forks are held as
    `run.on-owner-question` says, and Test's verdict is runner-written in the contracts and
    dWitnessedBar's row;
  - the close program keeps every mailbox message before pruning the ref;
  - `gap-flow-15` gains the join between items' routes and the transition table;
  - after LR-7, dTotalRecall's acceptance forms cover every core ask kind.
- **The follow-up round** (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold-followup.md`):
  - P20 and dDeclaredLoop's row cite the transition table's terminal set;
  - `gap-deploy-09`, `gap-mem-13` and `gap-mem-14` are new, and `gap-test-04` and `gap-deploy-02`
    carry the tool-level detail the round found.
- **The memory layer** (layer-memory's `[revised]`):
  - `record` is idempotent, content-addressed and minted under the build's lease, and each layer
    registers its own record kinds;
  - a reuse entry's one door is the instruction command, proposed with the build after LR-6;
  - an acceptance is mechanical for core filers and an `accept` line for the rest, after LR-5,
    extending V14;
  - dTotalRecall's row follows: the house index in M1c's shape, the benchmark re-run, and the task
    card's `**Reuse:**` field;
  - `[owed]` gains the order of dTotalRecall and its gaps' owners, and `gap-mem-12` joins
    dTotalRecall.

Revised: 2026-10-16, after KN-1 (`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`): the owner chose "One layer, two
sides". Knowledge folds into the memory layer:
- `[layers]` has five core layers and three expansions: observability, integrations and distribution;
- memory is the trail, what happened in a build, and the library, what generalizes beyond one: major
  decisions, reuse entries, bug classes and research;
- the codebase-map, memory-recall and lexicon kits are memory's optional components, and P28 governs
  them as it governs expansions;
- reuse entries are core, so a reuse directive renders on a core-only install;
- `policy.on-missing-expansion` covers an absent optional component too;
- the next round designs the library side, in place of a Knowledge layer.

Revised: 2026-10-16, after the library round's forks LB-1 to LB-4
(`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`):
- `review.unclassed`, `reuse.propose` and `decisions.major` join the catalogue and every preset;
- the library fills at declared flow points: `review.report`'s left-shift dispositions,
  `build.unit-pass`'s reuse lines and `deploy.distill`'s decision-log rows, beside a derived research
  view;
- `gap-review-10` joins dFairHearing and `gap-mem-15` joins dTotalRecall.

Revised: 2026-10-16, after the library round's review (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`):
- `build.distill` writes the major decisions' rows before Test, from forks whose class is declared, and
  `deploy.distill` confirms them at the landed SHA;
- an optional slot renders filled, searched with nothing found, or not installed, never empty;
- dBoundRoles renders bug classes as a core field, dOrderedCharter's dependency check covers optional
  components, and dTotalRecall moves recall's two core-read functions into memory-tree.
- Revised 2026-10-17, the debt round: dOrderedCharter moves them, all eight names check 27 imports,
  before its dependency check lands (layer-library `[consult]`).

Revised: 2026-10-16, after the expansion round's forks EX-1 to EX-3 and DI-1
(`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`):
- the three expansions are defined from what each layer's two research runs agree on, and P28
  adds that expansions meet only through the core;
- seventeen keys join the catalogue and sixteen join every preset; `release.environments` joins
  the keys presets never touch, and the keys that select an extension take registered names;
- the core's records declare the eight points the expansions attach at: Runtime's cadence items,
  reading and fix classes, adapter grants and install targets; Test's verdict backends; Deploy's
  release and version slots; and memory homes for records that belong to no build;
- `deploy.release` and `life.release` are renamed `deploy.unlease` and `life.unlease`;
- twenty gaps join the register and their chain builds' cells.

Revised: 2026-10-16, after the expansion round's two Tier-2 reviews and the owner's RH-1 and PIN-1
(`build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`):
- `build.release-hold` (close-only by default) and `verdict.remote.pin-scope` (workflow by default)
  join the catalogue and every preset, and `verdict.remote.pin` joins the keys presets never touch;
- `kits.host` and `kits.watch-cadence` join for distribution's programs; `release.cadence` is renamed
  `kits.cadence`, `maintain.detector-admission` `maintain.reading-admission`, and the key
  `maintain.record` `maintain.record-when`; `integrations.secret-home` and `integrations.secret-scan`
  become Runtime's `runtime.secret-home` and `runtime.secret-scan`;
- `policy.on-missing-expansion` governs a value on a key the core reads, and a key an absent
  expansion owns is unread, so no preset is refused for it; a pair rule holds `runtime.journal` at
  `all` or at least `review.loop.window-days`;
- dOrderedCharter's layer check gains EX-1's arm, dMindYourWords takes the lexicon's two drift signals
  as its leg pack, dShippedRelease sandboxes `kits.offer`, and dWellOiledMachine enforces grants and
  runs the secret scan; `gap-deploy-13` and `gap-lex-08` join their cells.

Revised: 2026-10-16, after the fold's closing review
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`):
- the journal pair rule binds only while observability is installed;
- dDeclaredLoop's preset check owes the core-only preset load, and dShippedRelease's `kits.offer` runs
  nothing from the adopter's tree.

Revised: 2026-10-16, after the follow-up round (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md`):
- `build.release-ceiling` joins the catalogue and every preset: how long the release hold waits before an
  owner item;
- dDeclaredLoop's core-only preset load is seen red both ways, and dWellOiledMachine owes event waits
  and their ceiling sweep.

Revised: 2026-10-16, the stale sweep: `[owed]` gains gap-orient-08, which orientation's rule moves with the executor,
and RT-3 placed the executor in dWellOiledMachine.

Revised: 2026-10-17, after the debt round's folds (`build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared.md`,
its `[fold-*]` sections, and the lexicon and review-system records' `[debt-fold]`):
- dMindYourWords' parents become dWellOiledMachine and dWitnessedBar, whose extension points it fills,
  and its row takes LX-1 to LX-3 and the tag-name vocabulary check;
- dFairHearing becomes a parent of dDeclaredLoop, and its row takes RV-1's preset, the opt-in swap, the
  disposition grammar and the template sources it edits;
- dOrderedCharter moves check 27's eight recall-kit names into memory-tree, from dTotalRecall;
- dDeclaredLoop's lease grammar carries an epoch, and its answer set gains `awaiting`;
- dWellOiledMachine decides act binding and the epoch check in the PermissionRequest entry, keys returns
  per spawn site, writes `onFailure` on every entry, and wakes an owner request on an unleased build as
  an event.

Revised: 2026-10-17, after the systems and retrofit rounds and the owner's AN-1, AN-2, IW-1, IW-2,
RS-1, RS-2, MS-1 to MS-3 and RF-1 to RF-6 (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`,
`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`):
- thirty-one keys join the catalogue and every preset: four `tags.*`, `annotations.lookup` and three
  more `annotations.*`, three `instructions.*`, `review.twin`, two `roles.*`, six `memory.*` and eleven
  `retrofit.*`. Each default is the owner's answer or the round's design; the non-default presets were
  assigned by analogy with their neighbours, velocity taking the lighter value and strict the heavier.
  `review.twin` and `memory.over-budget` keep the owner's answer in every preset, since RS-1 makes
  twins the owner's opt-in and MS-3 chose report over refusing under strict;
- IW-2 amends the front door: the charter keeps one line per practice, and each practice's reach
  per step renders as step-scoped units in work orders;
- the chain rows gain the units each round's owners name, retrofit a system across the layers whose
  ledger dWitnessedBar builds (RF-1, RF-5);
- twenty-six gaps join the register and their chain builds' cells.

Revised: 2026-10-17, after the systems and retrofit audit
(`reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`), folded item by item in
`build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md` `[fold-systems-retrofit]`:
- dTotalRecall and dBoundRoles follow dWitnessedBar, whose ledger they read, and dShippedRelease
  follows dTotalRecall, whose census `adopt` runs (M2);
- the chain rows gain the parts the audit found unowned: the six tag namespaces and `marker`, the
  progress cell, origin's check and rendering, `adopt.reconstruct`, the CI-job import and the keyed
  pins (M3, M10, M16, M32, M33);
- the ledger's populations stay where their checks keep them, each with a direction, and gov's 27
  registries convert in place (H1, H4, M24);
- the strict preset's `instructions.task-charter` is `when-not-static`, and
  `retrofit.practice-pending`'s second value is `propose-retire`, RF-4's second option (M29, M30);
- P27 exempts memory slices, which MS-3 answers (M1).

Revised: 2026-10-17, after the owner's RT-4 and MS-2, asked a third time
(`build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md` `[answers]`):
- `runtime.attended-judge` joins the catalogue, `classifier-or-person` by default, with
  `runtime.attended-allowance` beside it. Only act sessions load the permission baseline, as an extra
  settings source at launch;
- `memory.item-budget` defaults to `measured`: 96 for every role until 30 sliced work orders per role
  are measured, then each role's own p90;
- both keep the owner's answer in every preset, as `review.twin` and `memory.over-budget` do.

Revised: 2026-10-17, after the owner's PM-1 to PM-3
(`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md` `[answers]`):
- a seventh system, the level-0 project map, is derived in core memory from the one index (PM-2);
- the roles that change structure receive it, and unit workers keep their slice (PM-1). That amends
  layer-memory `[views]`;
- its keys, `memory.project-map` among them, join the catalogue at its design's fold, after the
  research PM-3 opened.

Revised: 2026-10-17, after the project map's design and the owner's PM-4 to PM-7
(`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md` `[design]` and `[answers-design]`):
- five `memory.map*` keys and `memory.project-map` join the catalogue and every preset, the owner's
  answers kept in each, and `memory.default-load` gains `card-and-map`, its default for attended
  sessions (PM-7);
- nine chain rows gain the map's units. dTotalRecall builds it, and each namespace's owning build adds
  its purpose field and reviews its existing nodes (PM-5);
- `gap-mem-26`, `gap-mem-27` and `gap-orient-15` join the register and their chain builds' cells.

Revised: 2026-10-17, after the project map's findings and the owner's PM-8 to PM-11
(`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md` `[fixes]` and `[answers-fixes]`):
- a node's owning build is a field on the node, declared once: an item's in the loop definition, a
  policy key's in the catalogue, and a point's or a record kind's in its registry. The owners of a
  step, a system and a namespace are derived from their members. A chain row's prose describes a
  build's work, and is never read as its ownership (PM-8);
- the map's owner check covers every node a build must build, each owned by exactly one build, and
  the renderer infers no relation;
- the entry step's items are dDeclaredLoop's, and `entry.intake`'s hook stays dWellOiledMachine's
  (PM-9);
- a map line opens with a node's native id where one exists (PM-11);
- the owner fields land as columns in flow-steps and the catalogue once the owner approves the
  proposed table (PM-10).

Revised: 2026-10-17, after the owner approved PM-10's
ownership table (`build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md` `[answers]`):
- every node a build must build declares its owning build: the catalogue's rows in its `Owner` column, the
  items in flow-steps', the points in layer-runtime `[extend]`'s, the tag namespaces in the systems
  record's Owners bullet, and the record kinds in layer-memory `[contract]`'s table;
- 351 nodes, each owned by exactly one chain build. dConvergedCharter owns none of them, and owns its 7
  gaps;
- the re-cut reconciles the chain rows with them.

Revised: 2026-10-18, after the re-cut
(`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md`):
- dIndexedDesign follows dTotalRecall; `gap-orient-08` is dWellOiledMachine's and `gap-design-01`
  dTotalRecall's (RC-2); the deployer's and the maintainer's definitions are dShippedRelease's and
  dTendedCadence's, their registration dBoundRoles's;
- kit conf keys fold into the policy file at convergence (RC-3); the instruction layer stays first
  (RC-4); `[open]` is confirmed (RC-5); `instructions.edit` stands (RC-6); the roles layer's lower-level
  design goes to dBoundRoles's unit specs (RC-7);
- the rows name the entry step's program in dDeclaredLoop's and the intake hook in dWellOiledMachine's
  (PM-9);
- where the policy file, its schema and its reader land waits on the owner's Tier-2 review of the build
  order (RC-1).

Revised: 2026-10-18, after the Tier-2 review of the build order (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-chain-order.md`) and the
owner's RC-1, RC-8 and RC-9 (`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` `[order-review]`):
- a sixteenth build, dGroundRules, lands ahead of both roots with the policy file, its schema, its reader
  and a minimal guard, and owns `gap-spine-06` (RC-1);
- `placement` and `placement.check` are dDeclaredLoop's, with `gap-orient-01` (RC-8);
- dRankedPlan's ratification falls back to an owner breakpoint until dWellOiledMachine lands the intake
  hook, which then drains the fallback (RC-9);
- dShippedRelease follows dBoundRoles; the review's other fixes are folded row by row, each marked with
  its item.

Revised: 2026-10-18, after the owner's PM-12 on the ownership table's re-verification
(`build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md` `[pm-12]`, `[answers-2]`):
- every stage's reason and recommend items are dCalibratedLens's, one mechanism with one owner;
  `instructions.slices` and `instructions.task-charter` are dBoundRoles's, `review.build.when` dScopedBuild's,
  `roles.shape-enforce` and `memory.default-load` dWellOiledMachine's, and `integrations.tracker`
  dShippedRelease's;
- the `acceptance` and `disposition` kinds are dDeclaredLoop's, and the run record is observability's,
  so dTendedCadence's;
- the expansions' 26 items and 26 more record kinds join the table, 403 nodes in all;
- the rows that claimed a moved behaviour are narrowed, and the receiving rows name it.

Revised: 2026-10-18, after the declared whole-design audit (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`) and the owner's AF-1 to AF-3
(`build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md`):
- the breakpoint mechanism, its owner gate and the stage-exit recommendation are dDeclaredLoop's, so every step
  reaches them from an ancestor; dCalibratedLens keeps the lenses, the ledger and the Loop Review (AF-1);
- an invalid policy input reads the last valid landed revision, or refuses, as `policy.on-invalid` says (AF-2);
  strict holds a repository to the test levels it declares (AF-3);
- dShippedRelease follows dWellOiledMachine, whose points its programs register at (C1);
- the audit's other items are folded row by row, each marked with its item.

Revised: 2026-10-18, after the audit fold's closing review (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-audit-fold-closing.md`) and the owner's FL1
(`build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md` `[review-fold]`):
- the design audit's marks carry a DA- prefix, apart from the chain-order review's H, M and L (FM6);
- `review.findings` follows `review.dispose` to dDeclaredLoop (FM4), and dTendedCadence follows dIndexedDesign,
  whose Design entry its patch builds take (FH3);
- `follow-leases` works on under held leases until they expire, and refuses new leases, claims and mints (FL1);
- the review's other items are folded row by row, each marked with its item.

Revised: 2026-10-18, the night pass (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`), the owner's eight points worked in while the owner was away:
- unattended is the core flow's default state, and attendance an override that adds only the owner's interactions:
  P4, P20 and P25 amended, `attendance` and `attendance.scope` added, the unattended kit dissolved into the chain, and
  playbook mode seated through the `repeat` disposition and the playbook record kind (point 1);
- testing happens wherever the work needs it: P31, the probe program and its keys, the tester agent, the experiment
  shape and the visual witness (point 2);
- every role sees the code its item touches: P32, the core `code` record replacing the optional symbols and callers,
  and a `code` slot per item (point 3);
- one relational syntax across memory: P33, the closed edge set, the span rule and `gov tag bundle` (point 4);
- the compaction replay carries the whole default load and ends with `next`'s line (point 5);
- five practices from Anthropic's AI-native SDLC playbook (point 6);
- twenty-eight gaps registered, each owned, and the forks the owner's words leave open parked as NP-1 to NP-24, the
  defaults they set shown as recommendations until answered.

Revised: 2026-10-18, after the night pass's closing review (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-night-pass-closing.md`), CLEAN WITH FIXES, 26 items, 3 high:
- `repeat` gains its transition row and its Design entry (H1), and the order's gate now checks both (H1);
- each new dependency on a later build gets a stand-in, a class row or a move: the playbook set check moves to
  dIndexedDesign, the probe's re-run joins dDeclaredLoop's computed witnesses, and the probe program declares its
  stand-ins (H2, M1, M2);
- the owner's session hosts the driver under its owner binding, each role act it hosts act-bound, one statement
  everywhere (M6); attendance writes its own record kind, the attendance override (M13);
- the map's fates arms fail hard on an absent record and are counted, and the order's gate is one committed script
  (H3, M7, M8, M14, M15);
- the other items are folded row by row in the night-pass record's `[review-fold]`.

Revised: 2026-10-17, after the folds' closing review (`reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`):
- dTotalRecall's row gains the shared extraction primitive, the research-return backfill and the
  `adopt` program, whose keys had no reader on any row;
- dRankedPlan gains dTotalRecall as a parent, since its read sets are dTotalRecall's keys;
- dOrderedCharter's pre-check move covers every core module's recall imports, not check 27's alone;
- dFairHearing's opt-in arguments come from `review.pin`, and its replay counts known defects;
- dShippedRelease's offered updates leave seeding and adoption to the adopter's own run.

## [layers] The product's layers

A layer is a capability named by a tag. A kit implements layers, and its descriptor declares the layer
and the extension point that each of its parts serves (P28). One test sorts them: the core alone
carries one build from request to landing, and an expansion is never needed for that (layers round
one, `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`).

| Layer | Kind | What it is |
|---|---|---|
| `instruction` | core | everything an agent is told, levelled 0 to 7 and tagged by scope |
| `flow` | core | a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as breakpoints and testing as probes at any boundary, with the verdict engine and the lander |
| `roles` | core | the bound workers, and the driver |
| `memory` | core | the trail, what happened in a build: records, transitions, witnesses, the card's truth; and the library, what generalizes beyond one: major decisions, reuse entries, bug classes, research. Its optional components, the map's owner views and dossiers, recall and the lexicon, are what agents consult to decide; the map's code depth is core since the night pass (point 3) (KN-1) |
| `runtime` | core | what executes the cycle: the supervisor and its checklist engine, act sessions and the spawn harness, the `next` verb and the owner's controls, the hooks, isolation, process supervision |
| `observability` | expansion | signals about the loop and the runtime, read and filed but never deciding a position, and the cadence programs that act on them: Maintain and the Loop Review |
| `integrations` | expansion | adapters to outside services, each registered at the core point it serves under one header: remote CI as a verdict backend, notifications, cloud hosts, and deploy engines that promote a landed tree through environments |
| `distribution` | expansion | the product's delivery across a repository boundary: govkit's install by copy at a release tag and its receipt, gov's tagged kit releases, overlays, the install of the targets Runtime's harness adapters declare, currency and the fleet register |

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

A work-order field, or any part of a core render, that an expansion or an optional component fills is an
optional slot. It renders filled, searched with nothing found, or not installed with the core's fallback
named, never empty (layer-library `[consult]`). The kit-to-layer map is in the layer record. The layers are reviewed one
by one with the owner, each in its own layer record.

## [principles] What every chain build implements

- **P1 One loop, declared once.** A new loop kit owns WHAT each stage takes in, hands out and proves,
  and extends the policy schema dGroundRules owns (RC-1, DA-M2); the roles kit owns WHO does the work, its workflows naming loop stages by
  id (walk S1b). Every shipped part declares its stage; a coverage gate reds an unclaimed part.
- **P2 Witnessed hand-offs.** A stage exit is computed from committed history, a hook-written record
  or a verifier's verdict, never from state the acting agent typed.
- **P3 Local-first verdict.** The local hook is the default and first-built verdict path, because
  remote CI is not available (R4.4); a peer-node verifier ships as a switchable backend (R5.2);
  remote CI is a designed slot.
- **P4 One flow, attended or not.** Unattended is the default state: the request is the mandate, and the
  driver carries a build from entry to its terminal state with no owner turn but those `autonomy` places.
  Attendance, set by `attendance` or by an attend request, adds only the owner's interactions: the announcement of
  each act's step and role, the owner's confirmations at breakpoints, and owner questions asked live. It never
  changes an item, its actor, the driver, a role's use or its enforcement (R1.4; the owner's point 1, night pass).
- **P5 Concurrency by lease, inside the flow.** Builds, units and cadence runs hold remote leases, and
  builds reach each other through a durable mailbox; both are the flow's own mechanics, built with the
  loop and never by a separate build, and overlap warns by default (R2.2; coordination record).
- **P6 Maintain closes the loop, as an expansion.** The core flow carries a build from request to
  landing in five steps. Maintain, delivered with the observability expansion, runs over what landed,
  on its cadence and its events. It turns declared safe fixes into patch builds and files everything
  else into Plan's triage. Without it, the loop closes through requests alone (R2.3; layers round
  two).
- **P7 Review at breakpoints.** Review is not a step. A breakpoint declared at any item boundary
  pauses the flow until a reviewer lens or the owner disposes it, and a review that runs blocks as
  `review.blocks` says, every review by default (DA-M4).
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
  FL-D3, FL-D6). By default no build parks on an unresolved fork: the role that meets it resolves it by these
  principles and records it, a fork the goal cannot survive included, whose plan revision proceeds
  under the request's mandate (flow-roles FR-4, FR-12); `run.on-owner-question` and `design.forks` let
  the owner choose to park instead (DA-M4).
- **P19 Built work is never rewritten in place.** A built unit's spec is frozen; every later change,
  a review finding's fix included, arrives as a new unit with its own spec, so the trail is complete
  (flow FL-B3).
- **P20 The flow is the layer above the build.** A build passes five steps, Plan, Design, Build, Test
  and Deploy, from its fixed entry point: complex features enter at Plan, in-goal amendments, patch
  builds and playbook runs (`repeat`) at Design. Each step is a deterministic, mechanically enforced program of items, and the
  build carries each step's records. A build ends in a terminal state flow-steps' `[transitions]`
  declares. Nothing changes
  tracked content outside the flow. Builds run unattended by default, from the request that is their
  mandate, with the executor running the steps (flow record, walked 2026-10-14; layers round two; night pass,
  point 1).
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
  by its role's agent, from the role's static instructions and a rendered work order. The driver
  drives and orients its sidechains: the supervisor in every mode, or the owner's session while it hosts the
  driver (night pass, point 1). It does no role's work, and holds only composed cards, typed
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
  `instructions.checks` says (layers round one). Memory slices are exempt: over `memory.item-budget`,
  they are answered by `memory.over-budget` (MS-3), never refused or routed back (revised 2026-10-17,
  the systems and retrofit audit's M1).
- **P28 Layers are capabilities, and the core never depends on an expansion.** A layer is a capability
  named by a tag, and a kit implements layers and declares which. The core (instruction, flow, roles,
  memory, runtime) carries one build from request to landing alone. An expansion attaches only at an
  extension point a core layer declares. Every layer, core or expansion, fills one layer contract
  (layers round one). A core layer's optional component, such as memory's map, recall and lexicon
  kits, attaches the same way, and the core never depends on it either (KN-1). Expansions meet only
  through the core: each registers only at points a core layer declares, and one uses another's output
  only as records it reads through memory, falling back to the core when the other is absent (EX-1).
- **P29 A role acts on what it is handed, and verifies only what its job is to verify.**
  - **Handed and keyed:** the executor hands a work order's inputs as content. Each fact is keyed by
    what it was derived from and classed `witnessed`, `decided` or `claimed`.
  - **Fresh at act launch:** the supervisor recomputes every key when it cuts the work order at act
    launch, and a claimed fact whose source moved is handed as stale evidence, so a role never checks
    freshness.
  - **Acted on:** a producing role works from every keyed fact (`roles.trust`). Nothing that changes
    state rests on a `claimed` fact without P23's re-derivation: a verdict, a position, a landing or
    a gate. P23 governs decisions, and P29 governs inputs (the owner's LR-2).
  - **Verified by the verifiers alone:** only the reviewer, the skeptic and the tester re-check, only
    their subject, and they start cold (`roles.verifier-context`).
  - **Answered calls:** a call the work order already answers, while the handed answer still holds,
    is refused, naming where the answer sits (`roles.answered-calls`).
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
- **P31 Testing happens wherever the work needs it.** A probe, a verification, a reproduction or an experiment, is
  placed at any item boundary by the driver, the owner or a policy, or raised by any role as the outcome of its
  item. It pins its subject by SHA, commits its losing outcome before it runs, and returns a typed record to the item
  that asked (P26). Its verdict is computed by a re-run or a scorer, and an agent's judgment is held as claimed (P2).
  Test stays the landing verdict, the one test that gates a landing (the owner's point 2, night pass).
- **P32 Every role sees the code its item touches.** The core derives a code record from the tree: files,
  definitions with their ranges, imports, resolved calls, tests and kit membership, cached by tree hash. Each item
  declares a seed, and its work order carries the seed's code neighbourhood as ranges, never bodies: its
  definitions, their callers, callees and tests, and their kit's siblings. Purposes are derived first and enriched
  by an agent, each keyed to its definition's body hash, so a stale one is found, never trusted. `git grep` is the
  floor where no extractor runs (the owner's point 3, night pass).
- **P33 One relational syntax.** Every part of memory and code is a node named by a tag, and parts relate by typed
  edges from one closed set, each declared once at the site that owns its fact, its inverse derived. A span is
  derived where a definition's extent is known, and marked only where it is not. Pulling a tag returns its bundle:
  every member, region and instruction joined to it, as a manifest of ranges under a row budget (the owner's
  point 4, night pass).

## [front-door] The charter as the loop's first step

The charter is what every agent loads first (walk S1). Its whole content sits in the level-0
envelope, `[AGENTS.md · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them …]` … `[/AGENTS.md]`, and it reads in this order:
what gov is and how it works and is used; the precedence and override rule (level decides, never
load order; the charter wins a live conflict unless the owner explicitly overrides it, and the
override is recorded); the instruction map (the levels below it, what loads when, and how to rebuild
the hierarchy after a reset); the core principles, fixed; the decision principles that resolve
unattended forks (the most feature-rich option, then the most expandable, fully recorded), which
outrank the practices; the active practices, one line each, each practice's reach per step rendered as step-scoped units handed in work orders (IW-2); the drive
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

Every key lives in `.governance/policy.toml` (walk S2), validated by dGroundRules's schema (DA-M2), read
through one reader, mirrored to JSON for the hooks, and rendered into the charter. A kit's conf keys, such
as the four Runtime reads (`FANOUT_CAP`, `PROCMON_REAP_MODE`, `RESUME_ATTEMPTS` and `RESUME_TURNS`), stay
in their kit confs, on the shrink-only list dGroundRules declares, until dConvergedCharter folds every one the
retrofit does not convert into the policy file, with `.githooks/gate-env.sh`'s owner-policy keys, as dGroundRules's derived list marks them (DA-M5), and
`tools/roles/house/policy.toml`'s `[effort]` and `[gates]`, their readers re-pointed in the fold's own unit (DA-H5). The retrofit keeps its date cutoffs registered as
cutoffs and turns its scalar pins into keyed ledger populations (revised 2026-10-18, RC-3, H6 and M7). The file,
its schema and its reader are dGroundRules's (RC-1). An absent file reads defaults, and a malformed one or an
out-of-set value reads as `policy.on-invalid` says, that key itself read from the last valid landed revision (AF-2,
FM2).

| Key | Allowed values | Default | Source | Owner |
|---|---|---|---|---|
| `preset` | velocity, standard, strict, guarded, or a repo-declared preset | standard | owner directive after the walk-through; `autonomous` renamed `guarded`, flow FL-D0 | dDeclaredLoop |
| `charter.override` | explicit-override, live-owner-wins, absolute | explicit-override | foundations F1-1 | dOrderedCharter |
| `charter.practices` | a set of catalogue or repo-declared practices | the governance foundation set | foundations F1-3 | dOrderedCharter |
| `core.bypass` | with-hooks-report, with-hooks-block, never | with-hooks-report | foundations K1 | dOrderedCharter |
| `core.exceptions` | any-session-recorded, owner-only-expiring, none | any-session-recorded | foundations K4 | dOrderedCharter |
| `design.forks` | agents-feature-rich-expandable, preference-forks-park, owner-decides-all | agents-feature-rich-expandable | flow FL-D3 | dIndexedDesign |
| `design.reentry` | any subset of interface-change, two-plus-units, review-cross-unit-flaw, planner-or-owner-flag | interface-change, review-cross-unit-flaw, planner-or-owner-flag | flow FL-D5 | dIndexedDesign |
| `autonomy` | plan-only, three-gates, every-stage | plan-only | R1.4, superseded by flow FL-P6 | dDeclaredLoop |
| `attendance` | unattended, announce, confirm-steps, confirm-acts | unattended | the owner's point 1, night pass: unattended is the default state; which attended value a bare attend request selects, night pass, pending NP-2; the default shown is the recommendation until the owner answers | dDeclaredLoop |
| `attendance.scope` | session, build, repository | build | how long an attend or unattend request holds, night pass, pending NP-3; the default shown is the recommendation until the owner answers | dWellOiledMachine |
| `policy.guard` | owner-only, agents-with-reason, agents-within-mandate | owner-only | R4.2 | dDeclaredLoop |
| `policy.proof` | tty-cli, signed, both | tty-cli | walk S3 | dDeclaredLoop |
| `policy.on-invalid` | last-valid, refuse | last-valid | the design audit's AF-2: a malformed file, an out-of-set value or a stale mirror never reads defaults; the key is read from the last valid landed revision whenever the current file is invalid, and an out-of-set value of it counts as malformed (FM2) | dGroundRules |
| `floor` | each of the four invariants, on or off, under the guard | all on | R5.1 | dDeclaredLoop |
| `hooks.bypass` | allowed, refused | allowed | R5.1 | dWitnessedBar |
| `transitions.record` | any subset of trailer, log, micro-format | all three | walk S4 | dDeclaredLoop |
| `leases` | warn, refuse | warn | R2.2 | dDeclaredLoop |
| `leases.granularity` | build-and-unit, build, unit | build-and-unit | walk C1 | dDeclaredLoop |
| `leases.renewal` | activity, fixed, none | activity | walk C2 | dDeclaredLoop |
| `leases.expiry-hours` | hours | 24 | walk C2 | dDeclaredLoop |
| `leases.overlap` | kit-dirs, files, builds | kit-dirs | walk C3 | dDeclaredLoop |
| `leases.offline` | warn, refuse, follow-leases | warn | walk C4; with the remote unreachable, `warn` records an acquisition and queues a claim or an ask-id mint keyed by content, each pushed by compare-and-swap on reconnection and yielding on conflict; `refuse` refuses both; `follow-leases` works on under the leases already held until each one's recorded expiry, and refuses new leases, claims and mints (the owner's FL1); no value mints a local id | dDeclaredLoop |
| `deps.coordination` | message-then-progress, wait-for-landing, order-only | message-then-progress | flow interactions FI-2 | dDeclaredLoop |
| `deps.early-build` | confirmed-interfaces, design-only, anything-coordinated | confirmed-interfaces | flow interactions FI-5 | dDeclaredLoop |
| `deps.messaging` | live-and-mailbox, live-only, mailbox-only | live-and-mailbox | flow interactions FI-6 | dDeclaredLoop |
| `landing.order` | plan-priority-then-first-verified, first-verified, owner-orders | plan-priority-then-first-verified | flow interactions FI-7 | dShippedRelease |
| `card.follows` | re-render-at-transition, card-per-step, fixed-at-start | re-render-at-transition | flow interactions FI-8 | dDeclaredLoop |
| `placement` | agent-places, declared-checked, owner-places | agent-places | orientation OR-1 | dDeclaredLoop |
| `placement.check` | refuse, record | refuse | orientation OR-6 | dDeclaredLoop |
| `kickoff.runs` | no-ready-card, opening-a-build, every-session, plan-absorbs | no-ready-card | orientation OR-2 | dRankedPlan |
| `card.store` | any subset of remote-ref, build-folder, local-clone | all three | orientation OR-5 | dDeclaredLoop |
| `card.snapshot` | terminal-only, every-transition | terminal-only | orientation OR-5, the adopted research | dDeclaredLoop |
| `actions.free` | read-only-probes, item-reads-only, recorded-anything | read-only-probes | orientation OR-3 | dDeclaredLoop |
| `resume.partial` | continue-item, restart-item, ask-owner | continue-item | orientation OR-4 | dDeclaredLoop |
| `resume.context` | fresh-when-idle, always-resume, always-fresh | fresh-when-idle | orientation OR-7 | dDeclaredLoop |
| `orient.budget` | record-only, warn-at-evidence-ceiling, owner-ceiling | record-only | orientation OR-8 | dDeclaredLoop |
| `driver.reads` | none-scout-only, state-reads-only, read-only-probes | state-reads-only | roles RL-5 | dBoundRoles |
| `prompts.author` | prompt-writer, requesting-worker-rendered | prompt-writer | roles RL-4 | dBoundRoles |
| `roles.retries` | a retry count | 3 | roles RL-7 | dBoundRoles |
| `roles.no-spawn` | executor-role-session, recorded-stand-in, refuse | executor-role-session | roles RL-8 | dBoundRoles |
| `roles.trust` | keyed, witnessed-only | keyed | roles layer F3-1 | dBoundRoles |
| `roles.answered-calls` | refuse, warn, record | refuse | roles layer F3-2 | dBoundRoles |
| `roles.verifier-context` | cold, warm | cold | roles layer F3-3 | dBoundRoles |
| `roles.on-contradiction` | repair-and-record, return, ask | repair-and-record | roles layer F3-4: the owner's answer over the recommended `return` | dBoundRoles |
| `reuse.delivery` | rendered, on-demand | rendered | memory layer F4-1: reuse entries rendered into work orders when a build's needs match | dTotalRecall |
| `reuse.propose` | new-seam, every-unit, owner-asks | new-seam | the library round's LB-2: which units close with a reuse line | dTotalRecall |
| `annotations.grammar` | voluntary, required, pushed-at-read | voluntary | memory layer F4-2; the systems round's AN-2: `pushed-at-read` fires on shell reads as well as Read; under `voluntary`, retrofit's drain checks a note's shape only where a unit writes one | dTotalRecall |
| `builds.agent-root` | work-order, readme | work-order | memory layer F4-5 | dTotalRecall |
| `asks.acceptance` | refuse, grade | refuse | memory layer F4-6 | dTotalRecall |
| `decisions.major` | author-rubric, author-owner-ratifies, owner-only | author-rubric | the library round's LB-3: who declares a decision major, for the log | dTotalRecall |
| `builds.slug-words` | a word range | 1-3 | memory layer, the owner's words | dTotalRecall |
| `builds.slug-style` | humorous, descriptive | humorous | memory layer, the owner's words: humorous ids are a foundation | dTotalRecall |
| `builds.slug-date` | none, shown, in-slug | none | memory layer F4-7 | dTotalRecall |
| `lexicon.pin` | shrink-only, absorb, no-gate | shrink-only | memory layer F4-8 | dMindYourWords |
| `lexicon.forced` | verified, by-name, by-annotation | verified | lexicon review L-1: forced names recognised by what forces them | dMindYourWords |
| `lexicon.at-commit` | refuse, warn, off | refuse | lexicon review L-2 | dMindYourWords |
| `lexicon.drift` | refuse-new, report, off | refuse-new | lexicon review L-3 | dMindYourWords |
| `lexicon.packs` | detected-and-declared, detected, declared, all | detected-and-declared | lexicon review L-5: the owner's answer, custom packs included | dMindYourWords |
| `review.opt-in` | none, or a set of named lenses, each replacing a named default lens of its preset | none | review system R-1: the owner's answer, "Both" | dFairHearing |
| `runtime.spawn-backend` | in-session, headless, or a registered spawn backend | in-session | runtime `[spawn]`; the spike decides the default for single-agent acts | dWellOiledMachine |
| `runtime.relaunch` | fresh, resume | fresh | runtime `[supervise]` | dWellOiledMachine |
| `runtime.act-ceiling` | hours | 1.5 | runtime `[supervise]` | dWellOiledMachine |
| `runtime.hold-ceiling` | hours | 6 | runtime `[supervise]` | dWellOiledMachine |
| `runtime.hook-failure` | closed, open | closed | runtime `[enforce]` | dWellOiledMachine |
| `runtime.attended-judge` | classifier-or-person, allowance, person | classifier-or-person | runtime `[act]`; the owner's RT-4: "Classifier or you (Recommended)" | dWellOiledMachine |
| `runtime.attended-allowance` | a set of named tools and command patterns, read under `allowance` | none | runtime `[act]`, RT-4 | dWellOiledMachine |
| `runtime.harnesses` | a set of named harness adapters | claude-code | runtime `[harness]` | dWellOiledMachine |
| `runtime.journal` | days, or all | 60 | the expansion round: the journal's retention, bounded by `[presets]`' pair rule while observability is installed | dWellOiledMachine |
| `runtime.secret-home` | os-keychain, env-injected | os-keychain | the expansion round, as `integrations.secret-home`; Runtime's since its review, as the grant's home: a CI-hosted adapter reads the CI store | dWellOiledMachine |
| `runtime.secret-scan` | value-gate, value-gate+shape-report | value-gate+shape-report | the expansion round, as `integrations.secret-scan`; Runtime's since its review: a shape scan alone reds on fixtures | dWellOiledMachine |
| `plan.ratification` | request, hook-keyword, terminal-command, signed-commit | request | flow-roles FR-1 | dRankedPlan |
| `run.host` | requesting-node, os-scheduler, cloud-routine, or another registered host | requesting-node | flow-roles FR-2 | dWellOiledMachine |
| `notify.owner` | turn-micro-formats, park-and-landing, every-transition, park-only | turn-micro-formats | flow-roles FR-3 | dDeclaredLoop |
| `notify.channel` | terminal, or another registered channel | terminal | the expansion round: integrations' notification adapters | dWellOiledMachine |
| `run.on-owner-question` | best-effort-recorded, park-item, park-build, stop-run | best-effort-recorded | flow-roles FR-4, FR-12 | dBoundRoles |
| `deps.landing` | hold-until-parent-lands, test-decides | hold-until-parent-lands | flow-roles FR-7 | dShippedRelease |
| `mailbox.reads` | every-item, transitions-only, every-item-amendments-at-transitions | every-item | flow-roles FR-8 | dDeclaredLoop |
| `review.follow-up` | after-high, while-finding, never | after-high | flow-roles FR-9 | dDeclaredLoop |
| `prompts.batch` | per-batch, per-task | per-batch | flow-roles FR-10 | dBoundRoles |
| `context.on-full` | compact-with-card, fresh-at-boundary | fresh-at-boundary | compaction CX-1; runtime RT-1 | dDeclaredLoop |
| `context.threshold` | a share of the window | 60% | compaction CX-1; read only under `fresh-at-boundary` | dDeclaredLoop |
| `card.pointers` | every-item, at-transitions | every-item | compaction CX-1, the owner's addition | dDeclaredLoop |
| `notices.record` | none, security-and-failures, all | none | compaction CX-2 | dBoundRoles |
| `instructions.checks` | refuse, warn, record | refuse | layers round one, the owner's "enforced wherever possible" | dOrderedCharter |
| `instructions.edit` | owner-command-agents-propose, flow-only, command-for-all | owner-command-agents-propose | layers round one, the owner's write path | dOrderedCharter |
| `instructions.proof` | tty-cli, signed, both | tty-cli | the instruction layer's fold: the instruction command's owner proof, as `policy.proof` | dOrderedCharter |
| `review.breakpoints` | a set of named item boundaries | none | layers round two: breakpoints beyond those `review.<stage>` and `autonomy` declare | dDeclaredLoop |
| `probe.points` | a set of named item boundaries | none | the owner's point 2, night pass: probes placed beyond those `probe.observations` owes and the roles raise | dDeclaredLoop |
| `probe.raise` | roles-and-owner, owner-only, off | roles-and-owner | the owner's point 2: "roles need to be able to work a problem out by testing" | dDeclaredLoop |
| `probe.observations` | verify-before-place, verify-at-plan, on-request | verify-before-place | an owner's observation in a request, night pass, pending NP-7; the default shown is the recommendation until the owner answers | dDeclaredLoop |
| `probe.experiment.authority` | owner-opts-in, within-cap, free | owner-opts-in | aScoutedSeam's one re-run spent 195 agents, night pass, pending NP-6; the default shown is the recommendation until the owner answers | dDeclaredLoop |
| `deps.on-parent-withdrawn` | replan, adopt-parent-work, withdraw-too | replan | layers round two | dDeclaredLoop |
| `review.design.rounds` | one, until-no-blocker, until-no-high, until-clean, fixed-count | one | flow steps: the owner's "1 spec review by default" | dDeclaredLoop |
| `review.design.round-count` | a round count held below unattended's `RUNAWAY_CEILING` | 2 | flow steps; read only under `fixed-count` | dDeclaredLoop |
| `review.unverified` | ask, block, record | ask | flow steps | dDeclaredLoop |
| `review.unclassed` | refuse, reason, owner-rules | refuse | the library round's LB-1: a confirmed finding that fits no class | dFairHearing |
| `flow.route-backs` | a route-back count | 3 | the flow layer's fold: a route back past the count becomes an owner item | dDeclaredLoop |
| `policy.on-missing-expansion` | refuse, fallback-reported | refuse | the owner's LR-4: a value, on a key the core reads, that selects an absent expansion or optional component (KN-1); a key an absent expansion owns is unread | dDeclaredLoop |
| `tests.without-cadence` | run-at-landing, report-unrun, wait-for-expansion | run-at-landing | flow steps: the slower levels when observability's Maintain is not installed | dWitnessedBar |
| `verdict` | local-hook, peer-node, remote-ci, or another registered backend | local-hook | R1.3, R4.4, R5.2 | dWitnessedBar |
| `verdict.blocks` | own-mixed-contended, every-red, own-only | own-only | walk T1 | dWitnessedBar |
| `verdict.held` | peer-or-cadence, push-selected, on-demand | on-demand | walk T2 | dWitnessedBar |
| `verdict.flakes` | quarantine, record, retry-only; a threshold | quarantine | walk T3 | dWitnessedBar |
| `tests.product` | declared, declared-with-runners, none | declared-with-runners | walk T4 | dWitnessedBar |
| `tests.landing-levels` | any subset of unit, integration, e2e, performance, or every-declared | unit, integration | flow FL-T3 | dWitnessedBar |
| `verdict.tree` | prepared-merge, build-tip | prepared-merge | flow FL-T1 | dWitnessedBar |
| `verdict.red-route` | fix-pass-or-design, always-new-unit | fix-pass-or-design | flow FL-T2 | dWitnessedBar |
| `verdict.remote.trust` | pinned-workflow, owner-reviews-workflow-change, app-only | pinned-workflow | the expansion round: a remote verdict's workflow sits in the tree it judges | dWitnessedBar |
| `verdict.remote.pin-scope` | workflow, dispatch-closure | workflow | the owner's PIN-1: the files the remote verdict's pin covers | dWitnessedBar |
| `verdict.remote.pin` | the pinned files' blob ids | none, until the owner pins | the expansion round's review: written only by the owner's guarded command | dWitnessedBar |
| `plan.authority` | planner-drafts-owner-ratifies, planner-within-themes, owner-orders | planner-drafts-owner-ratifies | R2.4 | dRankedPlan |
| `plan.unplaced` | warn, refuse-new, review-only | warn | walk P2 | dRankedPlan |
| `plan.triage` | owner-batches, rules, archive-legacy | rules | walk P3 | dRankedPlan |
| `plan.kickoff` | offer-next, binding, advisory | offer-next | walk P4 | dRankedPlan |
| `design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready | walk D1 | dIndexedDesign |
| `design.overlap` | warn, refuse, index-only | warn | walk D2 | dIndexedDesign |
| `build.scope` | warn-and-ask, refuse, report | warn-and-ask | walk B1; it also grades retrofit's touch join | dScopedBuild |
| `build.worktree` | per-unit, parallel-only, shared | shared | walk B2 | dWellOiledMachine |
| `deploy.runs` | landing-node, adopter-ci, operator | landing-node | walk DP1 | dShippedRelease |
| `deploy.promotion` | owner-approves-prod, auto-on-green, owner-approves-each | auto-on-green | walk DP2 | dShippedRelease |
| `deploy.on-verify-fail` | rollback-and-ask, halt-and-alert, roll-forward | roll-forward | walk DP3 | dShippedRelease |
| `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch | walk DP4 | dShippedRelease |
| `currency.max-behind` | 0, 1, 2, 4 | 2 | the expansion round: releases behind before an owner item | dShippedRelease |
| `currency.on-behind` | note, owner-item, red | owner-item | the expansion round: a red would block an adopter's landings on gov's cadence | dShippedRelease |
| `install.from` | release-tag, any-commit | release-tag | the expansion round: the receipt names one release | dShippedRelease |
| `build.closes` | at-landing, after-release-verifies, at-landing-maintain-owns | at-landing | flow FL-DP1 | dShippedRelease |
| `build.release-hold` | close-only, whole-close | close-only | the owner's RH-1: what waits for the release under `after-release-verifies` | dShippedRelease |
| `build.release-ceiling` | hours | 72 | the expansion fold's follow-up round: how long `deploy.released` waits for an exit record before an owner item | dWellOiledMachine |
| `kits.cadence` | every-landing, daily, weekly, owner-cut | weekly | flow FL-DP2, as `release.cadence`, renamed by the expansion round's review so `release.*` stays integrations'; the period is the main loop's choice | dShippedRelease |
| `kits.host` | session-start, os-scheduler, cloud-routine, or another registered host | session-start | the expansion round's review: distribution's cadence programs run on a host key of their own | dShippedRelease |
| `kits.watch-cadence` | daily, weekly, every-session | daily | the expansion round's review: the period of the currency probe, the fleet reading, and the cut under `kits.cadence: owner-cut` | dShippedRelease |
| `release.environments` | an ordered list of registered environments | none | the expansion round: integrations' release program runs for listed environments only | dShippedRelease |
| `integrations.tracker` | none, mirror-out | none | the expansion round: the ask backlog is the tracker | dShippedRelease |
| `maintain.host` | session-start, os-scheduler, cloud-routine, or another registered host | session-start | walk M1 | dTendedCadence |
| `maintain.cadence` | daily, weekly, every-session | daily | walk M2 | dTendedCadence |
| `maintain.fixes` | a set of named safe fixes | reap, prune landed, regenerate stale, defer dormant, records-only fixes, close finished run records | R2.3 | dTendedCadence |
| `maintain.on-breach` | file-ask, red-leg, report | file-ask | walk M3 | dTendedCadence |
| `maintain.events` | any subset of default-branch-red, release-verify-failed, session-start-breach | all three | flow FL-M2 | dTendedCadence |
| `maintain.reading-tree` | clean-base, worktree | clean-base | the expansion round: 14 of 108 repeated readings varied with the tree | dTendedCadence |
| `maintain.node-readings` | every-node, lease-holder | every-node | the expansion round: a node-scoped reading sees only its node | dTendedCadence |
| `maintain.reading-admission` | refuse-unowned, report-unowned | refuse-unowned | the expansion round: 0 of 27 drift signals carry an owner | dTendedCadence |
| `maintain.dead-after` | 5, 10, 20 | 10 | the expansion round: drift-report's existing limit | dTendedCadence |
| `maintain.record-when` | every-period, on-finding | every-period | the expansion round's EX-3: both values built; renamed by its review, so the item `maintain.record` keeps its name | dTendedCadence |
| `observability.run-record` | per-run, on-anomaly, none | per-run | the expansion round | dTendedCadence |
| `patch.ratify` | auto, owner | auto | flow FL-M3 | dTendedCadence |
| `review.<stage>` | off, opt-in, owed, owed-above-tier | opt-in; Build owed | R2.1 | dDeclaredLoop |
| `review.<stage>.effort` | the role efforts | the role's declared effort | R2.1 | dCalibratedLens |
| `review.recommendation` | advice, binding, binding-above-tier | advice | R4.3 | dDeclaredLoop |
| `review.build.when` | per-build, per-unit, per-landing | per-build | walk B3 | dScopedBuild |
| `review.findings` | blocker-high-own, all-own, blocker-own | blocker-high-own | flow FL-B3 | dDeclaredLoop |
| `review.blocks` | every-review, owed-only, none | every-review | flow FL-R1 | dDeclaredLoop |
| `review.left-shift` | second-occurrence, every-class, owner-selects | second-occurrence | flow FL-R2 | dDeclaredLoop |
| `review.recommendation.source` | scored-signals-and-reasoning, agent-judgment, signals-only | scored-signals-and-reasoning | flow FL-R3 | dDeclaredLoop |
| `review.loop.cadence` | weekly, monthly, every-n-landings | weekly | walk R1 | dCalibratedLens |
| `review.loop.retire` | propose-ratify, demote-then-propose, report | propose-ratify | walk R2 | dCalibratedLens |
| `review.loop.window-days` | days | 60 | walk R3 | dCalibratedLens |
| `review.loop.catch-source` | verdict-records, node-journal | verdict-records | the expansion round: another node cannot see a node's journal | dCalibratedLens |
| `budgets.*` | each cap's value and its mode, hard or soft | re-derived from evidence | walk R4 | dCalibratedLens |
| `tags.slice` | leaf, subtree | leaf | the systems round | dOrderedCharter |
| `tags.retired-cites` | refuse-new, warn, allow | refuse-new | the systems round | dOrderedCharter |
| `tags.positional` | shrink-only, refuse, report | shrink-only | the systems round | dOrderedCharter |
| `tags.bare-refs` | charter-only, unique, never | charter-only | the systems round; read by the `resolves` check and the resolver | dOrderedCharter |
| `tags.bundle` | manifest, inline, both | manifest | what `gov tag bundle` returns, night pass, pending NP-14; the default shown is the recommendation until the owner answers | dOrderedCharter |
| `tags.bundle-rows` | 20, 40, 80 | 40 | night pass, point 4: the `roles` feature's bundle runs about 44 rows unfolded and 39 with its kit folded | dOrderedCharter |
| `annotations.lookup` | query-and-map, query, map-index | query-and-map | the systems round's AN-1: the owner's "both" | dTotalRecall |
| `annotations.budget` | refuse, warn, record, each over the blocks a commit touches | refuse | the systems round | dTotalRecall |
| `annotations.resolve-scope` | notes, every-comment-ref | every-comment-ref | the systems round | dTotalRecall |
| `annotations.delivery` | work-order, on-demand, off | work-order | the systems round | dBoundRoles |
| `instructions.slices` | handed, pointer | handed | the systems round | dBoundRoles |
| `instructions.legacy` | shrink-only, refuse | shrink-only | the systems round; IW-1 arms the render gate at dOrderedCharter | dOrderedCharter |
| `instructions.task-charter` | when-not-static, always | when-not-static | the systems round; the single-carry check refuses `always` on a backend that loads the static block, where it carries the charter twice | dBoundRoles |
| `review.twin` | never, design-records, design-and-landing, always | never | the systems round's RS-1: twin runs only on the owner's opt-in | dFairHearing |
| `roles.shape-enforce` | refuse, record | refuse | the systems round | dWellOiledMachine |
| `roles.orientation.house-index` | handed, pointer, off | handed | the systems round | dBoundRoles |
| `memory.default-load` | card, card-and-live, card-and-map | card-and-map | the systems round; the owner's PM-7, "Card and map (Recommended)": the owner's session opens with the card and the map, and an act session loads its work order | dWellOiledMachine |
| `memory.code-budget` | 4k, 8k, 16k | 8k | the `code` slot's budget, ranges and never bodies, night pass, pending NP-8; the default shown is the recommendation until the owner answers | dBoundRoles |
| `memory.code-roles` | working-roles, every-role, structural-roles | working-roles | the working roles are the spec writer, builder, tester, researcher, architect and reviewer, and the prompt writer through its actor, night pass, pending NP-9; the default shown is the recommendation until the owner answers | dBoundRoles |
| `memory.code-languages` | python-shell-js, file-level-only, ctags | python-shell-js | other languages at file level, `git grep` the floor, night pass, pending NP-10; the default shown is the recommendation until the owner answers | dTotalRecall |
| `memory.code-enrich` | symbol-hash-slots, in-code-notes, derived-only | symbol-hash-slots | purposes keyed to a definition's body hash, night pass, pending NP-11; the default shown is the recommendation until the owner answers | dTotalRecall |
| `memory.load-budget` | 4k, 8k, 16k | 8k | the systems round; MS-1 holds the auto-memory's remainder to it | dTotalRecall |
| `memory.item-budget` | measured, 96 or 128 for every role, or KB per role (each role's cap the owner's to adjust) | measured | the systems round's MS-2, asked a third time: "Measure, then set"; 96 for every role until 30 sliced work orders per role are measured, then each role's own p90, which the Loop Review derives; a KB is 1,000 bytes | dTotalRecall |
| `memory.over-budget` | refuse, report, off | report | the systems round's MS-3: the owner's "Report only"; memory slices over the cap are exempt from `instructions.checks`' refusal and roles' route-back (P27) | dTotalRecall |
| `memory.project-map` | structural-roles, every-role, owner-only | structural-roles | the project map's PM-1, "Structural roles (Recommended)" | dBoundRoles |
| `memory.map-budget` | 16k, 24k, 32k | 32k | the project map's PM-4, "32k" | dTotalRecall |
| `memory.map-overflow` | degrade, refuse | degrade | the project map's design: over its budget the map degrades in a fixed order and never drops a node | dTotalRecall |
| `memory.map-unfold` | item-declared, none, all | item-declared | the project map's PM-6, "Item-declared (Recommended)" | dBoundRoles |
| `memory.map-purpose` | review, ledger, derive, refuse | review | the project map's PM-5, in the owner's words: "Required for new nodes, review all the existing nodes and either derive from available information or consult with the owner" | dTotalRecall |
| `memory.legacy-anchors` | derived, none | derived | the systems round | dTotalRecall |
| `memory.superseded-slices` | refuse, mark | refuse | the systems round | dTotalRecall |
| `retrofit.drain` | hunk, file, off | hunk | the retrofit round's RF-2; `file` owes every baselined site in each touched file, under the cap | dScopedBuild |
| `retrofit.drain-cap` | 5, 20, 50 sites per unit | 20 | the retrofit round | dScopedBuild |
| `retrofit.claim-on-touch` | claim, carry, off | claim | the retrofit round | dScopedBuild |
| `retrofit.claim-cap` | 1, 3, 5 keys per unit | 3 | the retrofit round | dScopedBuild |
| `retrofit.widen` | record-reason, refuse | record-reason | the retrofit round | dWitnessedBar |
| `retrofit.unseeded` | unarmed, refuse | unarmed | the retrofit round; `refuse` refuses the adoption at `adopt` and the registration at `test.seed` while a registered check lacks a seed | dWitnessedBar |
| `retrofit.reconstruct` | on-touch, at-adoption, on-ask | on-touch | the retrofit round; `at-adoption` and `on-ask` run `adopt.reconstruct`, the value being the owner's ask | dTotalRecall |
| `retrofit.decisions` | author-rubric, docs-owner-ratifies, docs-and-trailers | author-rubric | the retrofit round's RF-3: the owner switches it per repository | dTotalRecall |
| `retrofit.practice-pending` | alongside, propose-retire | alongside | the retrofit round's RF-4: `propose-retire` is its second option, read at `adopt.practices` | dTotalRecall |
| `retrofit.cadence` | off, hot-first | hot-first | the retrofit round's RF-6: read only where observability is installed, and off where it is absent | dTendedCadence |
| `retrofit.slot-bytes` | 512, 1024, 2048 | 1024 | the retrofit round | dBoundRoles |

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
- A pair rule binds two keys, and the same check applies it to each preset and to a repository's
  overrides on top of one. While observability is installed, `runtime.journal` is `all`, or at least
  `review.loop.window-days`; without it, the window is unread and binds nothing.
- Presets never touch the floor, `preset` itself, `policy.guard`, `policy.proof`, `policy.on-invalid`,
  `charter.practices`,
  `instructions.edit`, `instructions.proof`, `policy.on-missing-expansion`, `release.environments`,
  `verdict.remote.pin`, `attendance` or `attendance.scope`:
  loosening the guard or switching an invariant off stays an explicit owner choice, never a side
  effect of picking a posture; a methodology is a choice about the product, not a posture; a
  repository's environments and its pinned workflow are facts about it; and whether the owner attends is
  the owner's own choice (night pass, point 1).
- A repository may declare its own named presets in its policy file, each extending a shipped one,
  under the same completeness check.

**The four shipped presets.**
- `velocity`: least friction, for a solo owner or an early repository. Everything the posture
  governs warns or records; the floor, fail-closed hooks, the secret value gate and shrink-only
  ratchets still refuse, and a landing still blocks on an own red, an owed review and a blocker finding
  (DA-L3, FL2). The closing review is opt-in too, and records are kept to the commit
  trailer.
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
repository on either overrides `verdict` to `local-hook`. Both close a build only after its release
verifies, which needs integrations with an environment listed (LR-4); without it,
`policy.on-missing-expansion` decides.

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
| `reuse.propose` | owner-asks | new-seam | every-unit | new-seam |
| `annotations.grammar` | voluntary | voluntary | voluntary | voluntary |
| `builds.agent-root` | work-order | work-order | work-order | work-order |
| `asks.acceptance` | grade | refuse | refuse | refuse |
| `decisions.major` | author-rubric | author-rubric | author-owner-ratifies | author-rubric |
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
| `runtime.attended-judge` | classifier-or-person | classifier-or-person | classifier-or-person | classifier-or-person |
| `runtime.attended-allowance` | none | none | none | none |
| `runtime.harnesses` | claude-code | claude-code | claude-code | claude-code |
| `runtime.journal` | 60 | 60 | 90 | 60 |
| `runtime.secret-home` | os-keychain | os-keychain | os-keychain | os-keychain |
| `runtime.secret-scan` | value-gate | value-gate+shape-report | value-gate+shape-report | value-gate+shape-report |
| `plan.ratification` | request | request | terminal-command | hook-keyword |
| `run.host` | requesting-node | requesting-node | os-scheduler | os-scheduler |
| `notify.owner` | turn-micro-formats | turn-micro-formats | every-transition | park-and-landing |
| `notify.channel` | terminal | terminal | terminal | terminal |
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
| `probe.points` | none | none | none | none |
| `probe.raise` | roles-and-owner | roles-and-owner | roles-and-owner | roles-and-owner |
| `probe.observations` | on-request | verify-before-place | verify-before-place | verify-before-place |
| `probe.experiment.authority` | within-cap | owner-opts-in | owner-opts-in | owner-opts-in |
| `deps.on-parent-withdrawn` | replan | replan | replan | replan |
| `review.design.rounds` | one | one | until-no-high | until-no-blocker |
| `review.design.round-count` | 2 | 2 | 2 | 2 |
| `review.unverified` | record | ask | block | ask |
| `review.unclassed` | reason | refuse | refuse | refuse |
| `flow.route-backs` | 5 | 3 | 2 | 3 |
| `tests.without-cadence` | report-unrun | run-at-landing | run-at-landing | run-at-landing |
| `verdict` | local-hook | local-hook | peer-node | peer-node |
| `verdict.blocks` | own-only | own-only | every-red | own-mixed-contended |
| `verdict.held` | on-demand | on-demand | peer-or-cadence | peer-or-cadence |
| `verdict.flakes` | record | quarantine | record | quarantine |
| `tests.product` | declared | declared-with-runners | declared-with-runners | declared-with-runners |
| `tests.landing-levels` | unit | unit, integration | every-declared | unit, integration |
| `verdict.tree` | prepared-merge | prepared-merge | prepared-merge | prepared-merge |
| `verdict.red-route` | fix-pass-or-design | fix-pass-or-design | always-new-unit | fix-pass-or-design |
| `verdict.remote.trust` | pinned-workflow | pinned-workflow | owner-reviews-workflow-change | pinned-workflow |
| `verdict.remote.pin-scope` | workflow | workflow | dispatch-closure | workflow |
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
| `currency.max-behind` | 4 | 2 | 1 | 2 |
| `currency.on-behind` | note | owner-item | red | owner-item |
| `install.from` | any-commit | release-tag | release-tag | release-tag |
| `build.closes` | at-landing | at-landing | after-release-verifies | after-release-verifies |
| `build.release-hold` | close-only | close-only | whole-close | close-only |
| `build.release-ceiling` | 24 | 72 | 168 | 72 |
| `kits.cadence` | every-landing | weekly | owner-cut | weekly |
| `kits.host` | session-start | session-start | os-scheduler | os-scheduler |
| `kits.watch-cadence` | weekly | daily | daily | daily |
| `integrations.tracker` | none | none | none | none |
| `maintain.host` | session-start | session-start | os-scheduler | os-scheduler |
| `maintain.cadence` | weekly | daily | daily | daily |
| `maintain.fixes` | the full safe set | the full safe set | reap, regenerate stale | the full safe set |
| `maintain.on-breach` | report | file-ask | red-leg | file-ask |
| `maintain.events` | default-branch-red | all three | all three | all three |
| `maintain.reading-tree` | worktree | clean-base | clean-base | clean-base |
| `maintain.node-readings` | lease-holder | every-node | every-node | every-node |
| `maintain.reading-admission` | report-unowned | refuse-unowned | refuse-unowned | refuse-unowned |
| `maintain.dead-after` | 20 | 10 | 5 | 10 |
| `maintain.record-when` | on-finding | every-period | every-period | every-period |
| `observability.run-record` | none | per-run | per-run | per-run |
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
| `review.loop.catch-source` | node-journal | verdict-records | verdict-records | verdict-records |
| `budgets.*` | every cap soft | each cap's evidence-derived mode | every cap hard | each cap's evidence-derived mode |
| `tags.slice` | leaf | leaf | leaf | leaf |
| `tags.retired-cites` | warn | refuse-new | refuse-new | refuse-new |
| `tags.positional` | report | shrink-only | refuse | shrink-only |
| `tags.bare-refs` | unique | charter-only | never | charter-only |
| `tags.bundle` | manifest | manifest | manifest | manifest |
| `tags.bundle-rows` | 40 | 40 | 40 | 40 |
| `annotations.lookup` | query-and-map | query-and-map | query-and-map | query-and-map |
| `annotations.budget` | warn | refuse | refuse | refuse |
| `annotations.resolve-scope` | notes | every-comment-ref | every-comment-ref | every-comment-ref |
| `annotations.delivery` | work-order | work-order | work-order | work-order |
| `instructions.slices` | handed | handed | handed | handed |
| `instructions.legacy` | shrink-only | shrink-only | refuse | shrink-only |
| `instructions.task-charter` | when-not-static | when-not-static | when-not-static | when-not-static |
| `review.twin` | never | never | never | never |
| `roles.shape-enforce` | record | refuse | refuse | refuse |
| `roles.orientation.house-index` | handed | handed | handed | handed |
| `memory.default-load` | card-and-map | card-and-map | card-and-map | card-and-map |
| `memory.code-budget` | 8k | 8k | 16k | 8k |
| `memory.code-roles` | working-roles | working-roles | every-role | working-roles |
| `memory.code-languages` | python-shell-js | python-shell-js | python-shell-js | python-shell-js |
| `memory.code-enrich` | derived-only | symbol-hash-slots | symbol-hash-slots | symbol-hash-slots |
| `memory.load-budget` | 8k | 8k | 8k | 8k |
| `memory.item-budget` | measured | measured | measured | measured |
| `memory.over-budget` | report | report | report | report |
| `memory.project-map` | structural-roles | structural-roles | structural-roles | structural-roles |
| `memory.map-budget` | 32k | 32k | 32k | 32k |
| `memory.map-overflow` | degrade | degrade | refuse | degrade |
| `memory.map-unfold` | item-declared | item-declared | item-declared | item-declared |
| `memory.map-purpose` | review | review | review | review |
| `memory.legacy-anchors` | derived | derived | derived | derived |
| `memory.superseded-slices` | mark | refuse | refuse | refuse |
| `retrofit.drain` | hunk | hunk | hunk | hunk |
| `retrofit.drain-cap` | 20 | 20 | 20 | 20 |
| `retrofit.claim-on-touch` | carry | claim | claim | claim |
| `retrofit.claim-cap` | 3 | 3 | 3 | 3 |
| `retrofit.widen` | record-reason | record-reason | refuse | record-reason |
| `retrofit.unseeded` | unarmed | unarmed | refuse | unarmed |
| `retrofit.reconstruct` | on-touch | on-touch | on-touch | on-touch |
| `retrofit.decisions` | author-rubric | author-rubric | docs-owner-ratifies | author-rubric |
| `retrofit.practice-pending` | alongside | alongside | alongside | alongside |
| `retrofit.cadence` | off | hot-first | hot-first | hot-first |
| `retrofit.slot-bytes` | 1024 | 1024 | 1024 | 1024 |

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
| Test | a built range | a runner-written verdict per tree, read by the pre-push hook; gate health, flake and seen-red records | the verdict from the declared backend; OWN reds block | none | opt-in |
| Deploy | a verified tree | a landing record; kit release notes; per-SHA deploy and verify records; adopter currency | lander and engine records; the currency probe | landing authorization | opt-in |
| Maintain | the daily cadence at session start | safe fixes applied; asks filed by stage; a maintenance record | detectors pinned and owned; fixes inside the declared set | none | the weekly Loop Review |

This table predates layers round two, which changed four things:
- Maintain is an expansion step;
- owner gates are breakpoints (P7);
- Plan's witness is the hook-written intake (FR-1);
- each item's witness is declared by the loop (dDeclaredLoop).

## [chain] The chain: its builds and their final rosters

| Build | Stage | Parents | Planned units | Gaps owned |
|---|---|---|---|---|
| dGroundRules | Policy | dClosedLoop | `.governance/policy.toml`, its schema, its one reader and its JSON mirror, moved from dDeclaredLoop so that both roots read policy from a build ahead of them (RC-1); the reader extending `read_policy_key`'s contract, read at the landed revision, never from the working tree, parsed and never sourced (M7); each key resolved in one order: an override in the file, then the named preset's value once dDeclaredLoop adds presets to this reader, then the catalogue default with the reason recorded, which is all an absent file or one naming no preset reads (H4, DA-M10); a malformed file or an out-of-set value read as `policy.on-invalid` says, by default the last valid landed revision with the reason recorded and, with none, the push and landing gates refusing and naming the line, `policy.on-invalid` itself read from the last valid landed revision whenever the current file is invalid and an out-of-set value of it counting as malformed, each failure class (absent, malformed, missing key, out-of-set value, and a valid revision setting `refuse` followed by a malformed one, which must refuse) planted with its stated outcome, and a planted repository whose last valid revision sets each guard-bearing key explicitly at strict's [presets] value reading those values from a later malformed revision, never the catalogue defaults (AF-2, DA-H6, FM2, FM9); the JSON mirror regenerated at each landing and pinned to the landed revision, every consumer reading the mirror from the landed revision's blob, or checking its hash against the TOML at that revision and else reading through the TOML reader, a parity leg red on a hand-edited mirror, an arm red when a hook enforces a hand-edited working-tree mirror's loosened value, and a stale or absent mirror read as `policy.on-invalid` says (AF-2, DA-M11, FM1); the minimal guard, enforcing the defaults of `policy.guard` and `policy.proof`, owner-only and the TTY proof, without reading either key, and refusing agent writes to the policy file, its JSON mirror and the instruction manifest until dDeclaredLoop's guard lands (M11, FM1); the legacy homes on a shrink-only list derived by query from the files they guard, never typed, red on a planted row and green on today's files: every kit conf key the retrofit does not convert, `REVIEW_ROUNDS` among them until dDeclaredLoop's retirement removes its last reader (DA-M8, FM7), every key `.githooks/gate-env.sh` assigns, documents in its header or has a reader parse from it, each marked an owner policy dConvergedCharter folds (`INHERITED_RED`, `INHERITED_RED_MAX_AGE`, `GATE_DOC_PATHS`, `GATE_WSL_PARITY_RUNS`, and `GATE_POST_MERGE`, declared and unassigned as gap-deploy-02 records) or a mechanic that stays (`GOV_KITROOT`, `GATE_WSL_MIRROR_DEFAULT`, the gate commands, the Python and the self-test switch), and `tools/roles/house/policy.toml`'s `[effort]` and `[gates]` (M4, M7, DA-M5); an arm red when a key whose Owner build has landed has no reader, its population the catalogue's Owner column joined to the builds landed on the default branch, derived from history, a reader being a call site that consumes the key's value and never this reader's own default path, seen red on a key planted with a landed Owner and no consumer and green on the same key with an unlanded Owner (H4, DA-M1) | gap-spine-06 |
| dOrderedCharter | Foundation | dGroundRules | the practice catalogue and `charter.practices`; the charter re-founded in its level-0 envelope (front door, precedence and override rule with `charter.override` and its record, instruction map, active practices, one line each, hand-off to the loop, the repository's project block from its own overlay); envelopes rendered for every registered document and the gate over them; the instruction map re-injected on compact and resume; ranked envelopes in every subagent handoff; the drive section composed from a drive table in each adopted kit's descriptor, checked both ways, each subagent's role line repeated in its handoff, the charter held inside 32 KiB, measured at its first unit against `template-size-limits.txt`'s AGENTS.md and charter-template rows, the raise owed under that file's conditions (DA-L6); the core: the principle registry, the meta-check, the kinds register with each kind's owning build, the conformance-gate contract, the exception register and the `core.*` policies, and the factories and gates for instruction units, practices, Skills and layers; the build's card delivered at level 1 through an ignored per-worktree card file the charter's entry file imports, re-rendered by every session-start hook in the session's own tree, subagents' slices through the brief and the subagent-start hook, another harness's through its Runtime harness adapter, never an override file, which for Codex would replace the charter, after the primary-to-worktree compaction fixture passes; the instruction-unit registry (per unit: tag, level, statement type, scope tags, trigger, budget class, source, owning kit), documents rendered from units; the namespaced tag system (reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit), of which it registers reader, level, layer, practice, principle, kind and kit, each later namespace's join armed by the build that registers it, step, item and policy by dDeclaredLoop, role by dBoundRoles and record by dTotalRecall (M5), its own joined both ways over non-empty populations, its names shape-checked in the core and the lexicon's vocabulary added at an extension point; load sets derived per reader and item, budgeted per load point and per harness, extending `template-size-limits.txt`, refused at render when over budget or missing a required unit (`instructions.checks`), injected load points measured; the statement grammar and its check, render provenance in a sidecar lock; the ladder renumbered, the platform above it and the charter at level 0; memory instructing nothing, a standing directive promoted into a unit; the instruction manifest and its guarded write command (`instructions.edit`, `instructions.proof`), each `instructions.edit` value given its arm, witness and planted red, `flow-only` refused at load as selecting an absent component until dDeclaredLoop lands (L3), and every write refused until dDeclaredLoop's guard lands (M11), its checks also a leg over the tree, instruction packs extending `charter.practices` into the preset catalogue; the layer register, the layer contract, the layer kind's factory and conformance gate, and the check that the core never depends on an expansion or an optional component, landing after every name a core memory-tree module imports from the recall kit moves into memory-tree, memory-recall importing them: check 27's eight, the id grammar's `grammar_for`, `anchor_at` and `repo_root`, which `backlog.py`, `corpus_ids.py`, `merge-rows.py` and `transition_audit.py` import, `recall_conf.resolve` and its `Conf.digest`, which `transition_audit.py` calls, and `extract.grammar_for`, which `gen_build_index.py` imports, its population every edge from a core kit to a non-core kit, derived over the tree by kind (imports found by AST at any depth, `__import__` and `importlib` loads, path probes and resolutions of a kit's directory, file copies of its modules, shell references, and `requires_if` rows in kit.toml), each kind seen red on a planted edge of its shape (M8, DA-H3, DA-M7), dTotalRecall extending the moved parser with the slug grammar, its population drawn from the kit-to-layer map's optional rows and seen red on a core item that reads the map unconditionally, and its arm that fails when one expansion uses a point another declares (EX-1), seen red on a planted pair; the edges that check finds today each made a declared optional slot with a named fallback, or moved into the core, in its own unit: `gen_build_index.py`'s `drift_report` import, `push-main.sh`'s lexicon call, `unattended.sh`'s drift-audit and runlog calls, `check-verdict-epoch.sh`'s read of `extract.py`, `gotchas.py`'s check-18 probe, `corpus_ids.py`'s `GRAMMAR_DIR`, `migrate_backlog.py`'s kit copy and `backlog.py`'s `resolve_kit_dir` call, gotchas' check 18 still resolving ids on a scratch clone without memory-recall (DA-H3, DA-M7); the moved grammar's by-path consumers re-pointed in the move's own unit, from an inventory of every reader of `extract.py` and `recall_conf.py` by path: `check-verdict-epoch.sh`'s scan set and its DELEGATES, `migrate_backlog.py`'s `seed_recall_kit` and `merge-rows.test.sh`'s fixture copies, the scan-set change proven by a staged break in the moved module that reds `check-verdict-epoch.sh` (DA-H4); the tag grammar, its namespace registry and the derived tag index, one JSON file per tree at `<git-common-dir>/gov/index/<tree>.json` written atomically, its rows for uncommitted edits marked `dirty`, with one resolver (`gov tag show`, `where`, `refs` and `check`) and the `doc` and `unit` namespaces, the `tags` leg pack, `compute_coverage` moved to `tools/lib` as the join factory, with `map_lib.resolve_compare_base`, `derive_baseline_additions` and the pure `drop_touched_exemptions` beside it, so no core build imports codebase-map (H5), its consumers rewritten in the move's unit while `map_lib` re-exports the moved names for one release: `test_codebase_map.template.py` and its copy `test_codebase_map.py`, `selftest.py`, `gen_map.py` and `map_diff.py`, the template re-copied into adopters through govkit's update, and the codebase-map leg run after the move and seen red on the move without the re-export (DA-M9, FM10), and positional references aliased to tags, the live ones kept as a keyed list until dWitnessedBar's migration registers it; the instruction unit's schema and grammar, the one renderer with the charter and work-order templates and the write command, absorbing playbook parity, playbook render wiring, roles render wiring and agent-instructions wiring, each instruction file held to one renderer of record and each unit's status derived from its change record, the render gate armed with a shrink-only legacy list (IW-1), and the one-fact check over units; each practice's reach per step rendered as step-scoped units handed in work orders, the charter keeping one line per practice (IW-2); the namespace row's `purpose-source` and `owner` fields and the chain registry's purpose field, their existing entries reviewed by dTotalRecall's PM-5 unit, which reads `memory.map-purpose` (H1); a build run unattended by default from its request, said in the drive section, and the charter's `[land]` rule read through the request's mandate (night pass, point 1); the edge-type registry and the `edge` grammar: one closed set of typed edges, each declared once at the site that owns its fact and its inverse derived, and the instruction selectors open to a namespace a later build registers (night pass, point 4); `gov tag bundle`, returning a tag's members, regions and instructions as a manifest of ranges under `tags.bundle-rows`, folded past it, with its type-registered and target-resolves checks each seen red (night pass, point 4); file:line citations joined to the positional population `tags.positional` holds, new text citing `path#symbol` or a blob-pinned line, as NP-17 settles (night pass, point 4); each role's load set budgeting the `code` slot (night pass, point 3) | gap-found-01, gap-found-02, gap-found-03, gap-found-04, gap-found-05, gap-found-07, gap-found-08, gap-flow-02, gap-orient-13, gap-found-09, gap-found-10, gap-found-11, gap-found-14, gap-found-15, gap-found-17, gap-found-18, gap-found-19, gap-found-20, gap-found-21, gap-found-22, gap-found-23, gap-found-24, gap-found-25, gap-found-26 |
| dFairHearing | Review harness | dGroundRules | the owed replays first: the design-audit preset run blind at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository, scored by `review_replay.py` against a known-set file of all 59 known defects, each with its address, grade and escape flag, counting each matched defect once, at 45 of 59 known defects, 4 of 6 escapes and 7 of 8 highs in each run, a miss keeping the unit-spec preset for design records, the verify stage with batches by address, the synthesis with twins shown, and aRoutedQuill #23's fix re-judged by class; the design-audit preset of the spec-audit kind for design and architecture records, chosen by a `preset` argument that Design's breakpoint passes when every pinned spec revision is one (RV-1) (coherence, grounding flagging untested assumptions, reuse held to precedent, failure-envelope extended to trust boundaries, and alternatives-and-cost in place of blast-radius); opt-in lenses (security, alternatives, cost, portability, adopter migration, topology), each swapped for a named default lens of its preset in the five-element literal, passed as per-run `optIn` and `preset` arguments that `review.pin` maps from `review.opt-in` and the pinned revisions' record kind, checked once at the argument boundary, and each shipping on its losing test; skeptic batches sorted by cited address; duplicates counted as merged confirmations, with the orphan check on both kinds; items carrying a grade per id, ranked by the highest; refuted claims and same-address twins handed to the synthesizer to flag; fix verdicts judged by class, and every confirmed finding given one disposition from `review.report`'s grammar (`class:`, `new:`, `gate:`, or `none` under `review.unclassed`), against the leg manifest and the class slugs the harness hands over; portability, topology and adopter migration as bug-class checklist entries anchored to their paths, never universal, and lens notes passed by the callers, derived per preset after a swap; the review records brought back in line with the code at their sources (`tools/workflows/REVIEW-PROTOCOL.template.md`'s lens list, lens count and skeptic default, agent-cap's lens comment, `tools/workflows/tier2-review.template.js`, and `tools/roles/agents/gov-synthesizer.agent.md`'s input line), each live copy re-rendered; the panel's internals, and the twin merge a review step runs when the owner's `review.twin` opts it in (RS-1); the scorer factory: one deterministic scorer that re-derives every figure from committed raw outputs, pairs the cases every variant answered and refuses a partial population, extracted from `review_replay.py` with aScoutedSeam's grader as its second instance (night pass, point 2) | gap-review-04 to gap-review-10, gap-review-12, gap-review-13, gap-test-18 |
| dDeclaredLoop | Spine | dOrderedCharter, dFairHearing | the loop kit and definition keyed by the stage tags, the roles kit's stage table moved and its seven readers re-pointed in the same unit, never waiting for a live build's close; the named presets and their completeness check, with its pair rules, and each shipped preset loaded with only the core installed, refused only for a value on a core key that selects an absent expansion, seen red both ways: on a planted Absent clause that refuses by key, and on a loader stubbed to accept every value, since `strict` and `guarded` must be refused for `build.closes` on a core-only install; the preset step added to dGroundRules's reader, so a key the file does not override reads the named preset's value, seen red when a strict-named file with no override reads `hooks.bypass` as anything but `refused` (DA-M10); the charter's preset section, the preset's name and the keys that differ from it, rendered through dOrderedCharter's renderer and seen red on a planted override (DA-M3); the guard, the TTY CLI and the default floor; the transition record three ways; stage claims and the coverage gate; the witness-class rule; policy at govkit intake; the factories and conformance gates for commands, policy keys, presets, stages, hooks, roles and workflows; the coordination feature: one lease grammar for builds, units and cadence runs, each lease carrying an epoch bumped at every take-over, with run claims migrated onto it, acquired, renewed, released and taken over through CLI verbs the step checklists call, overlap warned or refused, fleet identity and uniqueness against the remote, offline behaviour, for leases and for every compare-and-swap mint alike, as `leases.offline`'s catalogue row defines each value, an unreachable remote never minting a local id (DA-M13, FL1); the mailbox per build, its closed set of message kinds checked on write, read and disposed at every transition, shown on the card and kept in the build's transition log; live delivery where the harness has it; dependency coordination by the parent's lease, interfaces confirmed at Design's exit, change and landing notices; the position engine: deriving each unit's step, the build's step, the next item and its interrupts from witnesses, items idempotent by witness and keyed by round or pass and input SHAs, answering from a closed set (act, awaiting, blocked, terminal, stuck, invalid-input, stale-remote), the read set and each claim's key and verdict printed; the build's orientation card at level 1, below the charter, kept as a ref per build on the remote (the truth), cached in the clone by build and object id and snapshotted into the build folder per `card.snapshot`, the stores selected by `card.store`, looked up and re-keyed in the session's own tree on resume, a fresh session recommended by `resume.context`, partial work handled by `resume.partial`; claims keyed and trusted by key and source; the entry step's items: the card's orientation, the three placing items and the claim (PM-9); the placement predicate and its check, moved from dRankedPlan (RC-8): a disposition for every request, made by `placement` and recorded with its reason, its facts checked by `placement.check`, an unattended prompt placed the same way, the disposition carried in the claim commit `entry.claim` writes until dWellOiledMachine's intake kind lands (RC-9); each step's items declared with actor, inputs, allowance, return schema and witness; `actions.free` at the tool call; orientation cost recorded per stage; backward transitions recorded like forward ones; the mailbox read at every item boundary by `mailbox.reads`, with the `intake` message kind; progress reported by `notify.owner`; a fresh session in the build's worktree recommended until the card-import fixture passes; the card's pointers updated as the build progresses, by `card.pointers`: the latest records by tag, the open forks and the item in flight, so a compacted or fresh session reorients from them; what a session does as its window fills, by `context.on-full` and `context.threshold`; a compaction's summary read as a lead, never a source; every checklist item named by a semantic tag, its number only display order; each step a program of items with declared dependencies, every item declared with its tag, actor, inputs by layer, instruction scope, allowance, return template and closed outcome set, computed witness and routes (the item audit's tables as input); one transition table per level (build, feature, unit), the engine refusing any transition it lacks; a default failure route (the refusal recorded, `next` returning the frontier: the unwitnessed items whose needs are witnessed); the terminal states flow-steps' `[transitions]` declares, and `deps.on-parent-withdrawn`; one closed disposition set; witnesses computed rather than typed by the acting agent (acceptance re-run by the executor, a probe's commands re-run at its pinned SHA, red attribution joined to the verdict); the `step`, `item`, `policy` and `command` tag namespaces, with their extractors; the items' declarations of the `map` slot and their unfolds; the policy namespaces' purposes, reviewed; breakpoints placeable at any item boundary (`review.breakpoints`), reviews and owner gates one mechanism with `review.<stage>` and `autonomy` its default declarations, a review breakpoint running dFairHearing's harness and an owner gate held until the owner's disposition record, which `run.on-owner-question` resolves only once dBoundRoles lands it and never for a ratification (AF-1, DA-H1); the breakpoint program's own items, `review.trigger`, `review.dispose`, `review.fold` and `review.cost`, with `review.blocks`, `review.unverified`, `review.left-shift` and `review.findings`, which `review.dispose` reads (AF-1, FM4); follow-up closing-review rounds by `review.follow-up`, and the design audit's rounds by `review.design.rounds` and `review.design.round-count`, `REVIEW_ROUNDS` retired in the same unit, its readers derived by key value over code, confs and kit.toml key lists and each re-pointed, and a planted round count at the runaway ceiling refused (AF-1, DA-M8, FM7, FM10); the stage-exit recommendation: every step's recommend and reason items, the score computed and the reasoning returned by the step's producing role, as `review.recommendation` and `review.recommendation.source` say (AF-1, DA-H2); the attendance rule: `attendance` places owner breakpoints and has owner questions asked live, and never selects an item's actor, the driver or a binding, its arm seen red on a planted value that swaps an actor, the `step —` announcement joining when dWellOiledMachine lands it (night pass, point 1); the `repeat` disposition in the placement set and its `none` row in the transition table, routing a request onto a `playbook`, filed as an ask until dIndexedDesign lands that record kind (night pass, point 1); the probe program (`probe.trigger`, `probe.pin`, `probe.design`, `probe.experiment`, `probe.run`, `probe.judge`, `probe.return`) and the `probe` record kind, a probe placed at any item boundary by `probe.points` or the owner and raised by any role's `probe` outcome under `probe.raise`, its record handed to the asking item, an entry-time probe keyed by content as triage is, and a stand-in for each later part it rests on, as flow-steps' `[probe]` declares (night pass, point 2); each item's declared code seed: its write set, its scope paths or its question's paths (night pass, point 3) | gap-spine-01, gap-spine-02, gap-flow-07, gap-conc-01, gap-conc-02, gap-flow-06, gap-orient-01, gap-orient-02, gap-orient-03, gap-orient-04, gap-orient-05, gap-orient-06, gap-orient-11, gap-flow-13, gap-flow-14, gap-flow-15, gap-spine-07, gap-flow-11, gap-flow-12, gap-flow-16, gap-flow-18 |
| dBoundRoles | Roles | dDeclaredLoop, dWitnessedBar | the roster sorted by layer: twelve core roles (orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, tester, one reviewer with a lens per step, skeptic, synthesizer), and the deployer and maintainer as expansion roles registered through the integrations and observability layer contracts, their definitions built by dShippedRelease and dTendedCadence, with the reviewer's maintenance-run and loop lenses; each role's static instructions as structured fields, every limit paired with its enforcer, a ceiling of tools, write classes and gate legs, and a typed return template; the work order rendered per item (the item, its inputs as record fields at their SHAs, its allowance, its return template, its witness), hashed into the spawn marker and bound to its act by task-sha and the session's binding record; the prompt writer composing every role's task from the driver's details; the orientation scout composing the card in a sidechain at session start; returns through a schema-forced channel, residual failures retried by `roles.retries`; the role index and agent files beyond every worker's reach, a tree with no index refused, `role-sha` compared at spawn; shell writes held to the allowance; the role-gate arm's field escape explained and closed; the `none` and `review` write classes enforced; `driver.reads`, `prompts.author` and `roles.no-spawn`; every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says (LR-3); prompt-writer calls batched by `prompts.batch`; a return's harness notices persisted with it, by `notices.record`; work-order fields an optional component or an expansion fills (the map's dossiers) declared as optional slots in their three states, and bug classes rendered as a core field by the unit's write set; the orientation scout's return carrying the placement disposition and its reason, the driver recording it and running `placement.check`; the trust mechanism (P29): inputs handed as content, each fact keyed and classed by the executor and re-cut fresh at act launch; each role's trust profile and context temperature declared and rendered (`roles.trust`, `roles.verifier-context`); the answered-call hook (`roles.answered-calls`); repairs recorded in returns and filed as asks against the producer's record (`roles.on-contradiction`); the role files' re-verification orders and protocol pointers replaced by rendered slices; the role-by-step matrix derived from the item declarations and joined both ways; role metrics per role and item into the value ledger, answered calls from the hook's records and the other classes from runlog's extractor, accepted against `role_orientation.py`'s baseline; the `role` and `field` tag namespaces; the role static block carried once per spawn; the shapes, extending each `tools/roles/workflows.toml` entry with its kind (`single`, `per-unit`, `panel`, `twin`, and `experiment`, whose cases, variants, bounded fan, scorer or blind judge and re-runs keyed by variant and effort come from aScoutedSeam's benchmark, night pass point 2), fan, checklist, orientation template, merge, twin rule and an agent cap bounded by agent-cap's `FANOUT_CAP`, with effort kept in `tools/roles/house/policy.toml` by workflow and stage until dConvergedCharter folds it (M7), the orientation scout at medium and the builder at high (RS-2), and the registry's readers rewritten in the same unit; the work order's memory slices, code-notes slot and legacy slot, each under its own budget and its own answer (systems `[cross]`), the legacy slot in its four states; the work order's `map` slot for the roles `memory.project-map` names, with the unfolds each item declares (PM-6), rendering "not installed" until dTotalRecall's renderer lands; the orientation scout composing the card's map cell; the answered-call hook's range matching, the excerpt keys and a repair's carry, designed in its own unit specs (RC-7); the tester agent, absent today, with its allowance (scratch, and the browser where the harness has it), and the `probe` outcome on every role's return template (night pass, point 2); owner questions asked live while the build is attended, best effort recorded once the wait passes (night pass, point 1); the `code` slot rendered per item from its declared seed: the seed's definitions with their ranges, their callers, callees and tests and their kit's siblings, as ranges under `memory.code-budget`, for the roles `memory.code-roles` names, with the map's delivery extended to the researcher and the prompt writer, rendering "not installed" until dTotalRecall's `code` record lands (night pass, point 3); the work order selecting instruction units by `feature.*` once dTotalRecall arms that selector, and the code-notes slot filled from the tag's bundle (night pass, point 4) | gap-roles-01, gap-roles-02, gap-roles-03, gap-roles-04, gap-roles-05, gap-roles-06, gap-roles-07, gap-roles-08, gap-orient-07, gap-orient-09, gap-roles-09, gap-roles-10, gap-roles-11, gap-roles-12, gap-roles-13, gap-roles-14, gap-roles-15, gap-roles-16, gap-roles-17, gap-roles-18, gap-roles-19, gap-roles-20, gap-orient-15, gap-roles-21, gap-roles-22 |
| dTotalRecall | Memory | dDeclaredLoop, dWitnessedBar | the memory contract: the record-kind registry (per kind: tag, layer, home, id rule, schema, writer, readers, lifecycle, check), templates and checks generated from it, and `HYGIENE.md`'s prose rendered as its view; the one `record` write command, which mints ids under the build's claim or lease, is idempotent and content-addressed, renders templates and refuses invalid values; for every filer outside a build, ids minted under an ask family's counter ref advanced by a `--force-with-lease` push, the claimant key on every claim commit and slug claim refs never pruned, seen red by a two-clone concurrent mint against today's local-only `check_slug_claimed`, and an unreachable remote handled as `leases.offline` says (gap-mem-13, DA-M12, DA-M13, FL1); the build README's declared front-matter schema, with unknown keys refused, `node`, `roster` and `streams` derived, a generated routing region by purpose, and the work order as each agent's root (`builds.agent-root`); the slug and id grammar exported once and read by every slug and id reader (`builds.slug-words`, `builds.slug-style`, `builds.slug-date`), proven by flipping the grammar in a scratch clone; typed relations (`depends-on`, `patches`, `amends`, `supersedes`, `implements`), inverted, checked both ways and rendered as the relation graph; the ask kind's acceptance at filing (`asks.acceptance`), extending backlog.py's V14; decisions split by kind: reuse entries as level-3 instruction units beside their dossiers and under `memory/map/conventions/`, proposed with their build through the instruction command and rendered once the owner accepts them, the major-decision log with its holds-now view, today's 200 rows routed by two raters at kappa 0.8 or better, and the `[records]` rule reworded; the reuse scout's house index in M1c's shape (a digest of symbols, callers, dossiers and reuse entries, with the sketch and census steps), delivered through the task card's `**Reuse:**` field (`reuse.delivery`) and accepted by re-running aScoutedSeam's benchmark; `reuse_lookup.py` retired with its readers rewritten, and memory-recall narrowed to a record finder; the core `code` record (night pass, point 3), replacing the optional symbols and callers: files, definitions with their ranges and body hashes, imports, every Python definition with import-aware calls, shell and JavaScript edges under the ambiguity test, cross-language invocation and registry edges, tests and kit membership, derived per blob through the shared extraction primitive in the languages `memory.code-languages` names and cached by tree hash, freshness-checked, with dossiers anchored to symbol keys; the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries, the generated annotation index and its resolve check (`annotations.grammar`), the shipped-evidence signal re-checked first; gotchas handed by write set; the generated views: README routing, the relation graph, the decisions' holds-now view and the reuse view; the research view, over the research-return kind; the `section`, `record`, `feature` and `class` extractors, `record find`, its last line naming the total past 40 rows, and `record show` over the one index, section tags declared per record kind with legacy anchors derived, the read budget per role item (`memory.item-budget`, MS-2, reported when exceeded, MS-3), the default load's memory share, the card and the auto-memory's remainder, held to `memory.load-budget` and reported at session start, the loading itself dWellOiledMachine's (PM-12), and the auto-memory's standing directives promoted through `instructions.edit` (MS-1); the `annotations` leg, the marker query with the map's index rows where the map is installed (AN-1), and the read hook on shell reads too (AN-2); retrofit's `baseline` and `census` record kinds, the `origin` field, and the `adopt` program the core's own command runs where distribution is absent: `adopt.census`, `adopt.practices` (the owner's one ruling per practice, through `retrofit.practice-pending`) and `adopt.decisions` (two raters by the author's rubric, through `retrofit.decisions`), with `adopt.reconstruct`, which `retrofit.reconstruct` governs, and a declined decision kept `rejected`; the origin check, re-derived from history, `origin` among the fields every slice renders, and the reuse digest's ranking; the progress cell; the annotation resolve check's legacy and the untouched long blocks registered as ledger populations; the `marker` namespace over the existing `gov:` words; derived anchors suffixed for a repeated heading; the shape-run kind; the acceptance re-measure counted over every read channel; the shared extraction primitive in `tools/lib` (LX-2), reading the working tree, the index or a revision, with the shell and JavaScript tokenizers moved into it, which the map and the lexicon each call; and the dated backfill of `kind: research-return` over the existing returns, 72 at `1b759b620`; the level-0 project map (PM-1, PM-2): its renderer and `gov map`, derived from the one index and cached beside it, at most `memory.map-budget` and degraded in a fixed order over it, never dropping a node; the three-way completeness check and the `map` leg pack; the atlas re-rendered from the same node table; the record-kind registry's purpose field, today's kinds, and the namespaces and chain builds whose fields dOrderedCharter adds, reviewed as `memory.map-purpose` says (PM-5, H1); the replay with the map and without at its first unit, so a losing map is never built, and a loss routed: the slot's "not installed" made terminal, dWellOiledMachine's map load and read count skipped, and dCalibratedLens's not-in-view computed from the slice manifest alone (M12); `gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the engine of `where` and the floor for a language with no extractor, the map's level 0 holding one counted `code` line (night pass, point 3); the enrichment workflow: purposes derived first from docstrings and headers, an agent's pass for the rest as `memory.code-enrich` says, each keyed to its definition's body hash and stale when the hash moves, joined both ways with a pending population (night pass, point 3); the replay's losing test extended to code: a unit's files read and its lookups counted, with the `code` slot and without it (night pass, point 3); extractors emitting typed edges from annotations, front matter, dossiers and decision rows, `decides` written on decision rows, and the span rule: a definition's extent where one derives, `gov:end <tag>` only where none does (night pass, point 4); the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it (night pass, point 4); the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles (night pass, point 4); the `feature` namespace armed as an instruction selector when it registers, as NP-13 settles (night pass, point 4) | gap-mem-01, gap-mem-02, gap-mem-03, gap-mem-04, gap-mem-05, gap-mem-06, gap-mem-07, gap-mem-08, gap-mem-09, gap-mem-11, gap-mem-12, gap-mem-13, gap-mem-14, gap-mem-15, gap-mem-16, gap-mem-17, gap-mem-18, gap-mem-19, gap-mem-20, gap-mem-21, gap-mem-22, gap-mem-23, gap-mem-24, gap-mem-25, gap-mem-26, gap-mem-27, gap-design-01, gap-mem-28, gap-mem-29, gap-mem-30, gap-mem-31, gap-mem-32, gap-mem-33 |
| dMindYourWords | Lexicon | dWellOiledMachine, dWitnessedBar | the definition classes (conforming, forced, out of scope, not a name, debt), with only debt counted against the shrink-only pin (`lexicon.pin`), held as a keyed ledger population of offender names once dWitnessedBar's factory lands, never as a count; forced names recognised by what forces them (`lexicon.forced`): packs keyed by base member, base prefix and host namespace, applied only where the site resolves statically through its imports to that base, against committed pack data; gov's own contract-forced names declared in a table the instruction write path owns, the code carrying at most a pointer a check resolves (LX-3), with a stale arm; override markers verified against the packs; a reasoned site suppression as the owner's counted fallback; `--suggest` made forced-aware; the packs, generated per host kit (`inspect` per Python minor, wheel AST, pluggy hookspecs, `.d.ts`), shell hosts curated, each with its kit, version range and generator command: the first wave (the data model, the commonly subclassed stdlib bases, unittest, pytest, argparse, `ast`, `http.server`, `logging`, `json`, `cmd`, the shell hosts), and the second wave (Django, Flask, Starlette, FastAPI, React) after an adopter-side census; packs detected from the import census and manifests and declared by the owner, custom packs included (`lexicon.packs`); enforcement: the work order's vocabulary slice and forced-aware answers, staged definitions checked at commit (`lexicon.at-commit`), and the branch's offenders compared with its base's by name at the bar, with move-aware keys proven by replaying the merges since 2026-08-16; drift beyond verbs (`lexicon.drift`): one verb per declared family per object, the families declared by the packs the stack census selects for the kits it discovers and by the owner through `instructions.edit` (LX-1), and a noun canon seeded from the corpus and frozen; the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and the `init` row re-justified; one extraction primitive in `tools/lib`, which dTotalRecall builds and the map and the lexicon each call over the working tree, the index or a revision, so neither kit requires the other (LX-2); the tag-name vocabulary check, registered at the instruction layer's name-check point that dOrderedCharter builds; the kit's defects fixed: repeated block headers refused, IIFE values and properties ungraded, the dead modes, and the Skill, conf and README reconciled; records kept out by the path selector; the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point; the overloaded terms settled: attended as a session kind and as a mode, playbook as the charter renderer and as playbook mode, and baseline as retrofit's debt and as a measured reference (night pass, points 1 and 2) | gap-mem-10, gap-lex-01, gap-lex-02, gap-lex-03, gap-lex-04, gap-lex-05, gap-lex-06, gap-lex-07, gap-lex-08, gap-lex-09 |
| dWellOiledMachine | Runtime | dBoundRoles, dTotalRecall | the platform spike first: a role-typed Workflow agent run inside a headless act session, with the headless backend measured beside it; the `next` verb over the loop kit's position function, the `next —` micro-format, and the check that every declared command ends with one or declares itself terminal, laggards, the commands of builds already closed, re-pointed by its own unit before it closes, so the list it seeds drains to empty (M3), with the readers of `--plan` and `--status` re-pointed; the owner's pause, resume, withdraw and supersede through the guarded command, mapped onto unattended's verbs, and attend and unattend, each writing an `attendance override` record scoped by `attendance.scope` (night pass, point 1); the prompt-submit hook writing each owner prompt verbatim to the session's intake log, its secrets redacted and its size capped (`entry.intake`, PM-9); Plan's ratification and the placement dispositions re-pointed to the intake record, RC-9's fallback drained per harness, only where an adapter's capability table declares the prompt-submit event and kept in force for any other, seen on a planted Codex-shaped adapter that still reaches Plan's exit (DA-M14), and builds witnessed under the fallback kept readable, the re-pointed readers accepting a fallback witness at any time from an adapter whose capability table lacks the prompt-submit event and from any other only before its own drain landing, seen on a build that crosses the drain and refused for a capable adapter's fallback witness written after its drain (DA-M15, FM3); the supervisor: `resume-tick.sh` grown, started and restarted by the node tick, the executor launched where `run.host` says, its liveness its build lease's beat, one act session per role act, relaunch capped by `RESUME_ATTEMPTS`, limit holds, fencing epochs, command adapters that are idempotent or reconcile, and shared records written by the supervisor alone; act binding and the epoch check at the Workflow, Agent and shell call, decided in the dispatcher's PermissionRequest entry, with in-script spawns declared and reconciled; the persisted-return store, keyed per spawn site, and the shared deferral block; agent slots reserved under agent-cap's cap; the one enforcement surface: the kits' fragments as packs, one dispatcher entry per event, ask rules on gated tools that only the dispatcher's PermissionRequest entry answers, loaded into each act session as an extra settings source at launch and into an attended session only as `runtime.attended-judge` says (RT-4), `onFailure` written on every entry with its effect recorded per binary, the owner-pack table, witnesses with named readers, signal traps on every git hook, the trusted hooks copy, and lander hardening, the lander a versioned command adapter with its dependency on the bar's kit declared; workspaces by `build.worktree`, the commit queue, integration before release and the sweep; sessions bound on every source, a resume that delivers no card diagnosed and closed, the compact hook re-injecting the build's current card, never the kickoff's, the PreCompact flush and the keep-list, the keep-list naming the classes a summary drops (handles, a decision's condition, rejected options, open forks), and each compaction journaled with its session, build, item in flight and trigger (night pass, point 5); the scheduler's host adapters and per-period cadence witnesses; harness adapters with capability tables; the node registry's runtime facts; the journal grammar moved into the core, and its retention by `runtime.journal`; the grant enforced on every adapter row, and the secret value scan at every boundary that publishes; event waits woken by their record, keyed by the record's id and the build, an owner request on an unleased build woken the same way, and the sweep that raises a wait past `build.release-ceiling` once, under the release hold's one key; act binding against the resolved shape's digest, and the journal reconciled against it, writing each non-review act's shape-run row; the `hook` and `point` tag namespaces; the hook-message and harness-prompt templates; hook and point purposes, reviewed; the session-start hook loading the set `memory.default-load` names, the card and the map by default in the owner's session, at startup, at resume and at a compaction, ending with `next`'s line computed at that moment (PM-7, PM-12, night pass point 5); the journal's count of map reads outside a slice; the supervisor the only driver in every mode, the owner's session its client, which hosts the driver only before this build lands or if its platform spike fails, under its owner binding, each role act it hosts act-bound with that act's epoch (night pass, point 1); the `step —` announcement before each act while attended, and once when attendance begins, rendered from `next` and the item's declaration, never typed by a model (night pass, point 1); intake for a prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer (night pass, point 1); the unattended kit dissolved into the loop kit and the runtime's own kit: its hooks repacked, its supervisor seam taken, `/unattended` a client of `run` until dConvergedCharter retires it (night pass, point 1); a measured `browser` row in each harness adapter's capability table, and the `visual.capture` command adapter: the pinned tree served, the cache busted, the declared viewports taken, screenshots kept by hash after the secret scan, console and DOM results returned (night pass, point 2); act binding and shape-run rows for an experiment's acts (night pass, point 2); a hook pack's refusal text, naming its rule and its remedy, declared in the pack's contract and checked at registration (night pass, point 6) | gap-rt-01 to gap-rt-21, gap-found-06, gap-flow-10, gap-tool-03, gap-orient-08, gap-orient-12, gap-orient-14, gap-conc-03, gap-deploy-07, gap-rt-22, gap-rt-23, gap-rt-24, gap-orient-16, gap-orient-17, gap-orient-18 |
| dWitnessedBar | Test | dDeclaredLoop | gate health measured and the reliability bar; bypasses recorded; attribution deciding what blocks; the runner-written verdict the pre-push hook reads; held legs by policy; the peer-node verifier; seen-red records; flake quarantine; the product-test contract with runner adapters; derived pre-commit list and multi-node cost evidence; the gate-leg factory and its conformance gate, every leg declaring the principles it enforces; the `leg`, `check` and `pack` tag namespaces, each leg given a `tag` field beside its free-text name, which stays the join key; retrofit's baseline ledger factory in `tools/lib`, one file per population, each registration declaring its direction (shrink-only debt, append-only history, declared set or ceiling) and its home, keyed never by line and carried across a rename, its both-ways arm `compute_coverage`, its base `resolve_compare_base`'s, moved to `tools/lib` by dOrderedCharter (H5), its TSV rows merged by a row-keyed driver, reaching copy-installed adopters as every `tools/lib` primitive does; the `ratchet` leg pack, with its `populated`, `seed laundering`, rename and merge rows; `test.seed` at every check's registration, seeding only an absent population and recording a failed or dead-probe seed unarmed; gov's own 27 registries converted in place onto the ledger (RF-5), 17 shrink-only debt, 2 append-only histories, 7 declared sets and 1 ceiling, with the readers the conversion owes; the seven record and row pins as keyed populations, and the date cutoffs registered as cutoffs; the positional references and IW-1's legacy list registered from dOrderedCharter's keyed lists; the leg's purpose field in `gate-legs.json`, today's 140 legs reviewed: each purpose derived from what the leg carries, or put to the owner (PM-5); the legacy-homes list dGroundRules declares, converted into a ledger population keyed by conf and key when its factory lands (M4); a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wrong-spec judgment to Design as a new unit, its arm seen red on a planted fix pass that writes the red leg's test file, and a fix pass after a failed acceptance leaving the acceptance commands' own files alone (night pass, point 6); the `tests=` and `enforces=` edge fields on legs (night pass, point 4) | gap-test-01, gap-test-02, gap-test-03, gap-test-04, gap-test-05, gap-test-06, gap-test-07, gap-test-08, gap-test-09, gap-test-10, gap-test-11, gap-test-12, gap-test-13, gap-flow-09, gap-tool-01, gap-test-14, gap-test-15, gap-test-16, gap-test-17, gap-test-19 |
| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall | priority beside `parents:` and the generated plan view; the planner and triager role and Plan workflow; rule-based triage; dormancy disposal; the live-build mapping carried out; Plan Review; kickoff offering the next item and attended briefs gated; the full kickoff only where `kickoff.runs` says; the session's intake log, which `entry.intake`'s prompt-submit hook writes (dWellOiledMachine's, PM-9), read as the request's ratification by `plan.ratification`; until that hook and the intake kind land, `plan.exit` under `plan.ratification: request` falls back to dDeclaredLoop's owner gate, held for the owner's disposition, its witness recorded as "intake not installed" (RC-9, AF-1, DA-H1); each role item's memory read set sized at Plan, as `id#tag` keys; `plan.record` declaring the probes owed before Design (night pass, point 2); the plan record's intent fields: the affected systems derived from the `code` record and checked, and the open questions as fork tags (night pass, point 6) | gap-plan-01, gap-plan-02, gap-plan-03, gap-plan-04, gap-plan-05, gap-plan-06, gap-plan-07, gap-flow-03, gap-flow-04, gap-plan-08 |
| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall | the derived-READY hand-off; the design index; design review by policy, its opt-in, effort and audit guard, the stage-exit recommendation being dDeclaredLoop's (AF-1); reuse and alternatives backed by recorded probes; the research harness, built on the `experiment` shape once dBoundRoles registers it, and run as today until then (night pass, point 2); agreement and tier checks; the spec measured, recommendations emitted, and the spec redesigned as a structured, tagged contract; the feature level (build, features, units) with each feature's interfaces declared structurally, two-level re-entry by `design.reentry`, additive-versus-breaking interface classification (proposed), fork resolution by `design.forks`; spec sections named by tag across tiers; the playbook record kind: dScriptedRepeat's canon, its declaration block, pieces and sets identified by hash, amendment by proposal, and `check-playbook` as Design's pack (night pass, point 1); the playbook set record and its set check, registered at Test's leg-pack point (night pass, point 1); the structured spec declaring `implements=` and `decides=` edges, and `design.seams` reading a tag's bundle (night pass, point 4) | gap-flow-01, gap-design-02, gap-design-03, gap-design-04, gap-design-05, gap-design-06, gap-design-07, gap-design-09, gap-design-10, gap-flow-17 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar, dWellOiledMachine | one exit contract with a history-derived base, refusing a build's exit while a core red its own commits introduced stands; built specs frozen, every closing-review finding disposed as new units by `review.findings`; scope at the push; the closing review recorded; a write gate reading derived state; the checklist witnessed; the core checks run by the executor at Build's exit; `build.unit-pass` and `build.scope` draining the legacy a unit touches, in hunks under `retrofit.drain-cap`, and claiming the baselined map keys its write set holds (dossiers) under `retrofit.claim-cap`; the touch join as `build.scope`'s one check, graded by its value, over the union of `git diff-tree -U0 --no-merges -M` across the unit's own commits, calling the pure `drop_touched_exemptions` in `tools/lib`, the map's own writer behind a point, and the claim arm "not installed" where the map is absent, seen on a planted core-only tree (H5); a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report (night pass, point 2); a playbook's pieces built as units with piece records joined by hash, and a proposal to amend the playbook filed as an ask (night pass, point 1) | gap-spine-03, gap-build-01, gap-build-02, gap-build-03, gap-build-04, gap-flow-05, gap-build-05 |
| dShippedRelease | Deploy | dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine | the landing record; kit release notes; the deploy engine; the incms adapter; the fleet register and currency watch; optional emitted CI; a derived runbook; the kit factory and its conformance gate; a dependent's landing held until its parent lands (`deps.landing`); landings ordered through the landing queue it builds (`gap-flow-08`); the lander running the core checks on the landed tree before it releases the build, so a core red the landing merge introduced stops that build from closing (foundations K1); the landing review blocking the build's close rather than the push; promotion after landing through environments as an integrations extension point; an unattended `kits.offer` in a govkit mode that runs nothing from the adopter's tree, its checks left to the adopter's lander, pushing through the adopter's own scoped grant; the install and update hooks that call `adopt` and `test.seed`, attended; the integrations import of an adopter's CI jobs as legs, test jobs only, each through an adapter row with its grant and secret reference, a job that deploys, publishes or pushes refused, and a registration check red on a planted deploy job; an update `kits.offer` offers runs neither in the adopter's tree, and its outbox order names the adopter's own run of both; the kit factory's purpose field and a `kit.toml` for govkit and lib, today's kits reviewed, lib's marked not installable and each `*/kit.toml` consumer naming how it treats one: `regen.py`, `check-kit-placeholders.py`, `run-gates.sh`, `check-hook-destinations.sh`, `render_playbook.py` and govkit's descriptor checks, each consumer's leg run on a tree with both descriptors and one seen red on a planted lib descriptor (DA-M16, FM10); the ask tracker's one-way mirror, the adapter `integrations.tracker: mirror-out` selects (PM-12); the deployer's definition, release notes for distribution and verify judgment for integrations, registered through dBoundRoles's layer contract | gap-deploy-01, gap-deploy-02, gap-deploy-03, gap-deploy-04, gap-deploy-05, gap-deploy-06, gap-deploy-08, gap-deploy-09, gap-deploy-10, gap-deploy-11, gap-deploy-12, gap-deploy-13, gap-flow-08, gap-tool-02, gap-tool-04, gap-tool-07 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign | the Maintain run as its step checklist on the flow's executor, never a recipe-mode playbook; the cadence, on Runtime's hosts; the safe-fix set; detectors with owners; map freshness; the maintenance record; a detector for the memory's dead pointers, owned by Maintain; Maintain and the Loop Review delivered as cadence steps of the observability expansion, detectors registered by layer, patch intakes rendered from keyed detector readings, event runs keyed by event; `maintain.retrofit-heat`, filing each period's sweep as a patch build under `retrofit.cadence: hot-first`'s standing ask and sweep asks only under `off`, and the progress cell's share of reads; the maintainer's definition, Maintain's filings, registered through dBoundRoles's layer contract; a cyclic playbook's cadence item, filing `repeat` intakes (night pass, point 1); a detector for bundle members whose code changed while their head line did not (night pass, point 4) | gap-maint-01, gap-maint-02, gap-maint-05, gap-maint-06, gap-maint-07, gap-maint-08, gap-maint-09, gap-maint-10, gap-maint-11, gap-orient-10 |
| dCalibratedLens | Review | dTendedCadence, dFairHearing | each stage review's lenses and effort: lenses for Plan, Test, Deploy and Maintain, drawn from dFairHearing's catalogue, run at `review.<stage>.effort` through dDeclaredLoop's breakpoints (AF-1); the shared value ledger; the weekly Loop Review; caps re-derived from evidence and review cost; instruction effectiveness measured from returns and findings that cite unit tags, the Loop Review pruning units that bear no load and tightening those broken often; each role's `memory.item-budget` derived from its p90 over 30 sliced work orders under `measured`, through the guarded policy command, the owner's own setting for a role winning (MS-2); the value ledger's shape rows, priced from the shape-run rows `review.cost` writes for review acts and the journal reconcile writes for every other; the not-in-view cause added to `review.dispose`'s record, computed from the author's slice manifest, the map and the `code` slot (night pass, point 3), and the Loop Review's reading of its share, proposing the map's retirement if it does not fall by 15 points over 38 confirmed findings; probe cost priced in the value ledger, and compactions counted per item kind as a sizing signal (night pass, points 2 and 5); instruction evals: a replay suite of recorded items with known outcomes, re-run as a held leg when an instruction unit changes, a confirmed finding whose cause is an instruction adding a case (night pass, point 6); the Loop Review's delivery metrics: lead time, landing frequency, change failure rate, time to restore, first-pass verdict rate, route-backs per build and scope drift (night pass, point 6) | gap-review-01, gap-review-02, gap-review-03, gap-maint-03, gap-design-08, gap-found-16, gap-review-11, gap-review-14, gap-review-15 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens | protocol text derived to facts only, each document in its envelope; every remaining positional reference migrated to tags; records merged by evidence; superseded parts retired through ratified proposals; adopters migrated onto the ranked charter and the loop; the record-kind factory and its conformance gate; protocols and templates rendered as tag-sliced views from the loop's checklists, the roles, the record schemas and the policies, the hand-written guides retired and their rationale moved into their units' `help` fields, never into `help/`'s feature pages; the remaining renderers absorbed, each retired with its last document: kit/dogfood doc parity, review-protocol parity, each kit's skill wiring `--check` and govkit's placeholder render; Skills converged to level-4 thin entries, each described "Use when …, runs …"; the protocol slices and Skill entries rendered from units; every kit conf key the retrofit does not convert folded into the policy file, with the legacy homes dGroundRules lists (RC-3, M7), and a reader inventory derived by key value over the tree, red on any reader of a folded key that still reads its old home: `transition_audit.read_modes`, which reads both homes keyed by commit, govkit's conf-key gap checks, kit.toml's `*_keys`, the kit-placeholders leg and the agent-cap parser (H6), and, each re-pointed to dGroundRules's reader at the landed revision in the fold's own unit, the four copies of `read_policy_key` in `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh` and `tools/unattended/unattended.sh` with their callers, `tools/run-gates/held_halves.py`, and `roles_lib.load_policy` with `check_roles.py`, `handoff.py` and `render_agents.py`, proven in a scratch clone where `INHERITED_RED=park` is folded, `.githooks/pre-push --decide` reading `land` before the re-point and `park` after it (DA-H5, DA-M6); the unattended kit, its four guides and `/unattended` retired once dWellOiledMachine's driver carries every run, the kit's README and the product rule's "four-verb driver" corrected with them (night pass, point 1); feature-specific guide prose migrated into feature-scoped units (night pass, point 4); every part in the fates table at its fate, the table's join run as convergence's exit check (night pass, point 8) | gap-spine-04, gap-spine-05, gap-maint-04, gap-found-12, gap-found-13, gap-tool-05, gap-tool-06, gap-tool-08, gap-tool-09 |

The live-build mapping is v1's table with one change: no chain build waits for a live build to close
or relies on what it delivers, so "after it closes" no longer holds. The active builds finish on
their own track (R3.3); the chain build covering each one's area builds what the design needs, and a
concurrent change is reconciled in Test's prepared merge (FI-3). The Plan build carries the mapping
out with the owner's ratification and confirms dPolishedVitrine's track, which went dormant on
2026-10-14.

## [open] Interpretations to confirm at chain approval

Confirmed by the owner, 2026-10-17 (RC-5, the re-cut's `[applied]`).

- Positional section references other than `§` (numbered method steps such as `M5`, numbered spec
  sections, numbered hygiene checks) carry the defect walk CV2 names, so the tag grammar would
  replace them too, inventoried by Convergence.
- Coordination (`build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`, `[interpretations]`): a
  parent is reachable while its build lease is live, with no separate timeout; Design's exit posts each
  frozen feature's declared interfaces to the dependents' mailboxes; a transition is refused while a
  message addressed to the build is neither answered nor acknowledged; the lease carries the build's
  verified tree for the landing order; each transition keeps the messages it disposed in the build's
  transition log, and the close program copies every message on a closed build's mailbox ref into its
  folder, disposed or not, then prunes the ref (flow-steps `[rules]`).


- The session model (`build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md`, `[holes]`): fourteen
  places where the settled design is silent or does not hold together when one build is walked
  through every step, H1 to H14, and two more found with roles, H15 and H16: all settled in the
  flow revisit (`build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`, `[closed]`).

## [owed] Owed to the chain re-cut

Revised 2026-10-18: the re-cut (`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` `[owed-state]`) records each item's state.

- **Settled by the runtime layer** (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`):
  - the flow's executor and its checklist engine: dWellOiledMachine owns them (RT-3);
  - the executor's harness: Runtime's `[spawn]`, with act sessions and a persisted-return store. The
    landing queue stays Deploy's;
  - the compaction checks (CX-3): disposed in Runtime's `[sessions]`, with `context.on-full` settled
    by RT-1.
- The roles layer's lower-level design (layers round three): State, 2026-10-18: goes to dBoundRoles's unit specs (RC-7).
  - how the answered-call hook matches a Read's range against the handed ranges at the blob SHA, and
    which Bash readers it parses;
  - how the executor cuts and keys excerpts;
  - how a repair's ask carries the repaired fact onward until the producer's record is fixed.
- **The expansion roles' home.** State, 2026-10-18: applied: dShippedRelease and dTendedCadence define them, and dShippedRelease now follows dBoundRoles, which registers them (M9). At the re-cut, the deployer's and the maintainer's definitions move to
  the builds that deliver integrations and observability. dBoundRoles keeps their registration
  through the layer contract.
- **The roles layer's mechanical shape**, for the revisit the owner set when round four opened. Revised
  2026-10-17: the systems round designs it (`build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`
  `[design-role-shapes]`), and dBoundRoles builds the shapes registry. Each
  role item's execution shape is declared: its agent set, effort, checklist, orientation template
  and merge. aScoutedSeam's benchmark is the evidence (layer-roles `[owner-notes]`):
  - one checklist scout matched a two-scout workflow with a judge, on a third of the agents;
  - a scout that reads a generated house index first raised recall from 13 to 16 of 24;
  - two independent medium Tier-2 rounds on the runtime design each found about three quarters of
    their union of 59 defects (`build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md`).
- **dTotalRecall's place in the re-cut.** State, 2026-10-18: applied: dIndexedDesign follows dTotalRecall. Two chain builds consume what dTotalRecall builds:
  - dIndexedDesign's "reuse and alternatives backed by recorded probes" uses its house index and
    reuse entries;
  - dTendedCadence's "map freshness" runs on its caller map.

  The re-cut therefore orders dTotalRecall ahead of both.
- **dTotalRecall and its gaps' owners** State, 2026-10-18: answered: `gap-plan-06`'s owner follows dTotalRecall, and `gap-design-01` moved to it (RC-2). (the memory layer's fold). `gap-design-01` (dDeclaredLoop,
  dTotalRecall's parent) and `gap-plan-06` (dRankedPlan, its sibling) have their fixes designed
  into dTotalRecall's units. The re-cut orders dTotalRecall ahead of each owner, or moves the gaps
  to dTotalRecall.
- **The tooling order.** State, 2026-10-18: answered: the instruction layer first (RC-4). Was: dispatch 26
  picked "Flow first" (memory layer `[tools]`), assuming step tags come from the loop kit, though the step
  definitions already declare them (DA-L4).
- **dMindYourWords' second-wave packs need an adopter census.** Django, Flask, Starlette, FastAPI and
  React each ship only after a census in an adopter shows their names actually offend. That census
  is adopter-repository work, so it waits for the owner's ask at that build.
- **The `next` verb lands with Runtime.** State, 2026-10-18: answered: dWellOiledMachine lands the check,
  and its laggard list, the commands of builds already closed, drains to empty (M3). Was: every stage
  build whose commands end with a `next —` line seemed to wait on dWellOiledMachine (RT-3, DA-L4).
- **Kit confs beside the policy file.** State, 2026-10-18: answered: dConvergedCharter folds them into
  the policy file, the retrofit's conversions excepted, and re-points their readers (RC-3, H6, DA-H5). Was:
  Runtime read `FANOUT_CAP`, `PROCMON_REAP_MODE`, `RESUME_ATTEMPTS` and `RESUME_TURNS` from kit confs (DA-L4).
- **dOrderedCharter's policy consumers.** State, 2026-10-18: answered: dGroundRules holds the file,
  schema and reader ahead of both roots (RC-1), and dDeclaredLoop renders the charter's preset section
  (DA-M3). Was: the load-set refusal, the guarded write command and the charter's preset render read
  policy that dDeclaredLoop, dOrderedCharter's child, would have landed (the instruction layer's fold, DA-L4).
- **gap-orient-08 follows the executor.** State, 2026-10-18: applied: dWellOiledMachine's. Orientation's rule moves it with the executor when the
  re-cut places the executor outside dDeclaredLoop (`build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md`
  `[gaps]`), and RT-3 placed it in dWellOiledMachine. The re-cut moves gap-orient-08 there.
- **The night pass's owed checks** (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`):
  - the compact and resume hooks' output cap, measured with a 32 KiB map, so the default load comes back whole
    (point 5);
  - the platform spike decides where the driver runs: if a role-typed Workflow agent cannot run inside a headless
    act session, the owner's session keeps hosting the driver under its owner binding, each role act it hosts
    act-bound with that act's epoch (point 1, NP-1);
  - the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside
    spans sit in a derivable definition (point 4);
  - the code record's cold derivation re-timed at dTotalRecall's first unit: over 30 s or over 1 MB loses (point 3);
  - the level-0 map's headroom, 31,203 of 32,768 B at `15cec9200` with the kits' layer and fate keys, budgeted for
    the `code` line before it lands (point 3).

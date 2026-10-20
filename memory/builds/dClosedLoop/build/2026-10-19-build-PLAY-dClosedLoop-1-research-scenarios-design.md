# Research: scenarios in the converged design

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 127's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-8-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

## Scenarios in the converged design (dClosedLoop, at `e1a54ac67`): what exists, what's missing, and one method

I wrote nothing in the repository. Every probe was a read against the live tree, so no temp copy was needed.

**Record keys.** All live in `memory/builds/dClosedLoop/build/`, with the `2026-10-1x-build-PLAY-dClosedLoop-1-` prefix dropped:

| Key | Record |
|---|---|
| v2 | architecture-v2 |
| FA | flow-roles-adoption |
| FS | flow-steps |
| NP | night-pass |
| SYS | systems |
| RS | review-system |
| LR | layer-roles |
| LRT | layer-runtime |
| LE | layer-expansions |
| LM | layer-memory |
| MP | memory-plan |
| FD | foundations |
| LF | layer-flow |
| LI | layer-instruction |

**Probes, quoted as measured:**
- `grep -l -i scenario *.md`: the word appears only in owner quotes (NP [words], RS [words]), the session log, and prior-art or adoption test-case tables. No record defines a scenario.
- Transition rows in FS [transitions]: 4 from `none`, 24 in all, and 8 terminal states.
- Item rows in FS (all programs): 88.
- `grep -l -E '^kind:|^mode:' memory/builds/*/README.md` returns nothing. Of 173 builds, none records a kind.
- `grep -c 'FA-[1-7]'` per record: FS 0, RS 0, LR 0, LF 0, SYS 3.
- `grep -i experiment` over SYS: 0 hits.

---

### 1. Decided

**A scenario declared: parts that exist today**
- **The entry-point table.** This is the only per-build variant the design has.
  - The variants are: features enter at Plan; in-goal amendments, patch builds and playbook runs (`repeat`) enter at Design (v2 [principles] P20).
  - There are four entry rows from `none`: new, triage select, patch and repeat (FS [transitions]).
  - `design.input` branches on seven input kinds (FS [design]).
  - A variant chooses only the entry step and the Design branch. It carries no roles, lenses, legs or policy.
- **Playbooks and `repeat`.**
  - A playbook is a design record kind. Following one is the `repeat` disposition, which enters Design and supplies the feature design. Its pieces are built as units, and its set check sits at Test's leg-pack point (NP [p1-unattended] 6; v2 [chain] dIndexedDesign).
  - The canon describes a content recipe: `step_selector`, `outputs`, `grain`, `piece_checks`, `set_checks`, `legs` (`memory/guides/PLAYBOOK-TEMPLATE.md:1-8`, declaration block).
  - dScriptedRepeat "refuses ordinary code builds" (`memory/builds/dScriptedRepeat/README.md`, owner's ask).
- **Presets.**
  - A preset is a named, complete assignment of policy keys. A repository may declare its own, extending a shipped one. `preset` is one repository-wide key (v2 [presets]).
  - Presets never touch `charter.practices`, because "a methodology is a choice about the product, not a posture" (v2 [presets]).
  - "Structural choices are decisions, not policies" (v2 [principles] P10).
- **Repository stages.** A stage is spliced between two adjacent gov stages by pinned transition rows. Gov's five stages stay whole and in order. "Every build that passes its two neighbours passes it, unless a route of its own skips it" (FA [folded], FA-3; P20).
- **Repository rows of every kind.** Items, roles, workflows, lenses and legs live in the overlay in their kinds' schemas. They may amend (field patch), supersede or exclude gov rows. Reordering happens only through `needs` (FA [design] 3-8). Every check, the position engine and every render read the composition (P8; FA [design] 11).
- **Routes.** Every outcome routes, and routes are declared where a policy value decides them. An item whose actor a policy chooses is one item per value. Route-backs are bounded by `flow.route-backs` (FS [rules]).
- **`review.breakpoints` and `probe.points`.** Both are repository-wide sets of item boundaries (v2 [policies]). A per-build breakpoint or probe exists only by the owner's request (FS [breakpoint] trigger; FS [probe]).
- **Shapes registry.**
  - Each workflow entry carries a kind, fan, checklist, orientation template, merge, twin rule and agent cap. A per-call intensity is a "named variant row" (SYS [design-role-shapes]).
  - There are five kinds: single, per-unit, panel, twin, and experiment (NP [p2-testing] 6).
- **Lens catalogue.** A lens is a catalogue row whose brief is a unit, chosen by `review.opt-in` into five fixed slots (FA [design] 3).
- **Leg packs.** `leg.repo.*` rows come in through the leg factory at Test's leg-pack point (FA [design] 3).

**Selection**
- **Who places a request.** The orientation scout at `entry.place`, under `placement: agent-places` (the default). It returns one disposition from a closed set: continue, amend, new, patch, repeat, ask or none. The witness is `placement.check` over the return's facts. Alternatives are `declared-checked` and `owner-places` (FS [entry]; v2 [policies] `placement`).
- **Triage.** `plan.triage-rule` selects asks, filings and proposals, with the planner's `plan.triage-judge` behind it (FS [plan]).
- **The plan record.** Its fields are problem, goal, cut-line, acceptance, priority, parents and practice reach. It has no kind field (FS [plan] `plan.record`).
- **How a wrong pick is caught.**
  - A failed `placement.check` routes back to `entry.place`.
  - `plan.dedupe` triggers a re-placement.
  - `design.reentry` classifies an amendment.
  - A plan revision leads to `design.inventory`.
  - A route-back past the bound becomes an owner item (FS [entry], [plan], [design], [rules]).
- **Scope of policy.** Every policy value is repository-wide. The only build-scoped value in the catalogue is `attendance.scope: build` (v2 [policies]).

**Pipelines**
- **Across builds.**
  - Typed relations `depends-on` (alias `parents:`), `patches`, `amends`, `supersedes` and `implements`, with `depends-on` acyclic (LM [relations]).
  - P21, plus the `deps.coordination`, `deps.early-build`, `deps.messaging`, `deps.landing` and `deps.on-parent-withdrawn` keys (v2 [policies]).
  - Design's exit posts interfaces to dependents (v2 [open]).
  - A superseded build's kept work passes through its replacement's `design.inventory` (FS [lifecycle]).
  - Findings become patch-build intakes (FS [breakpoint] `review.dispose`). Maintain's fixes become patch builds (P6).
  - A cyclic playbook is a cadence item that files `repeat` intakes (NP [p1-unattended] 6).
- **Within a build.**
  - The needs graph runs in parallel within the fan-out bound (P24; FS [rules]).
  - There is one transition table per level. The feature and unit tables are owed (FS [transitions]; `gap-flow-15`).
  - The position engine answers from a closed set (v2 [chain] dDeclaredLoop).
  - The composition is pinned per step (FA [design] 15).

**Adaptation on the fly**
- **Allowed inside a build:**
  - a probe raised by a role (P31; FS [probe]);
  - research routed back to the asking item;
  - owner items;
  - bounded route-backs;
  - amendment re-entry, and plan revision followed by `design.inventory` (FS [design]);
  - forks resolved under the mandate (P18).
- **Structural change** goes only through the overlay.
  - The write path is `instructions.edit: owner-command-agents-propose` with owner proof `instructions.proof: tty-cli` (v2 [policies]).
  - Every build then moves at its next step boundary, its witnesses carried by the change records' successors (FA-7).
- **Refused:**
  - removing, reordering or replacing a gov stage (FA [folded]);
  - any change to a fixed row or field (FA [design] 9);
  - an agent writing the overlay under the default policy.
- **Recorded.** The transition record into each step carries the composition's revision (FA [design] 15). So the flow each step ran under can be derived. Playbooks change by "amendment by proposal" (v2 [chain] dIndexedDesign).

**A pre-shipped set (decided so far)**
- The entry kinds: feature, amendment, patch and playbook run (P20).
- The four shipped presets (v2 [presets]).
- The cadence programs: Maintain, the Loop Review and the kit release. These are programs, not builds (LE [design-observability]; FS [expansions]).

**Workflow shapes**
- `single` covers one agent. `per-unit` covers parallel agents, with disjoint write sets run in parallel (FS [build] `build.unit-pass`). `panel` mixes roles over several stages: finders, at most five skeptic batches, and one synthesizer. `twin` runs two parallel copies of one shape. `experiment` runs variants in a bounded fan (SYS [design-role-shapes]; FS [probe]).
- Multi-step workflows with mixed roles are the workflow's `stages` map from stage to role (`tools/roles/workflows.toml:37`).
- **Caps.**
  - Each workflow's agent cap is bounded by `FANOUT_CAP` (SYS).
  - `FANOUT_CAP` can only lower the cap, to an integer from 1 to 5, set per repository in `.agent-cap.conf` (`tools/hooks/agent-cap.js:61-72`, `:492` `MAX_VERIFIERS = 5`; LRT [supervise]).
  - The cap is enforced in four places: the supervisor's slot reservation queues an act; the attended PreToolUse entry refuses (LRT [supervise]); act binding refuses a call whose roles, efforts or fan differ from the shape digest, and a verifier whose role wrote what it verifies (SYS [design-role-shapes] Binding); and `roles.shape-enforce` (v2 [policies]).
- The kinds, `FANOUT_CAP`'s bound and the five lens slots are fixed (FA [design] 9).

**Lenses**
- Adding one takes a `lens.repo.<name>` row in the overlay with its brief as a unit, chosen by `review.opt-in`, swapping out a named default lens (FA [design] 3; v2 [policies] `review.opt-in`).
- Gov's own lenses get tagged in the `lens` namespace, owned by dCalibratedLens (FA [chain]).
- agent-cap counts slots, never names. That is owed as a test at dFairHearing (FA [owed]).
- Today the lens sets are literals in code: `tools/workflows/tier2-review.js:705`, `:741`, `:773`, with `KINDS` at `:183` and `ROLE_KEYS` at `:229`.

---

### 2. Undecided (and why I say nothing decides it)

1. **A scenario as a unit.** No record names, schemas or registers a flow variant (the grep above). FD [core] C3's closed kind set has no such kind. The FA kinds are item, role, workflow, lens and leg.
2. **Picking per build, or several per build.** Every input is repository-wide: one `preset` key; one composition at the landed revision (P8; FA [design] 11); breakpoints and probe points as repository sets. Nothing records a build's kind: the plan record has no field for it (FS [plan]), and 0 of 173 READMEs carry one.
3. **Selecting by the kind of work** (design work, a mobile app, a high-precision data system). The disposition set is closed and names entry kinds, not domains (FS [entry]). A repository stage runs for every build unless "a route of its own skips it" (FA [folded]), and no fact exists for such a route to read.
4. **A design-only build.**
   - The transition table has no row from designing to a terminal state other than through Build, Test and Deploy (FS [transitions]), and P20 makes every build pass gov's five stages.
   - Whether a design-only build is record-units-through-five-stages (as this build's own landing implies) or a shorter path is decided nowhere.
5. **Promoting a build's adapted flow.**
   - `promoted-from` covers only an instruction unit made from a memory node (MP [edges]).
   - The Loop Review proposes only retiring or merging rows, and re-deriving caps (LE [design-observability] `loop.propose`).
   - Playbook amendment covers content canons only.
   - Nothing turns a build's composition delta into a reusable row set.
6. **An agent changing the flow mid-build while unattended.** `instructions.edit` lets agents propose, but where a proposal goes was never walked: "`instructions.edit`'s alternatives are still not walked" (LI, line 686). P18 says no build parks, so the build would go on under the unchanged composition.
7. **A build-local composition.** FA-7 moves every build to the repository's new composition. No record gives one build its own patch set.
8. **Different compositions per feature or unit inside one build.** The feature and unit transition tables are owed (`gap-flow-15`; FS [transitions]).
9. **Caps per scenario or per build.** Caps exist only per workflow entry and per repository (SYS; LRT [supervise]). What `probe.experiment.authority: free` lets past agent-cap's fixed 5 is ambiguous. NP [answers] keeps `free` "since P10 makes every offered option one", while `agent-cap.js:61` says the 5 is "never raisable".
10. **Removing a lens.**
    - Undecided: whether `instructions.exclude` may drop a gov default lens, or only a swap may. The five slots are fixed (FA [design] 9), and excluding a default would empty a slot.
    - Undecided: whether a repository lens owes RS [lenses]' "each lens ships on its test" (a swapped-in lens must beat the dropped one on a blind replay).
11. **One agent for a whole build.** No record allows it. One actor per item (FS [rules]), the verifier separation (SYS Binding), and the fixed cycle roles (FA [design] 9) all refuse it. No record discusses relaxing them.

---

### 3. Contradictions between records

1. **How a lens is added.**
   - FS [breakpoint] Extension points (lines 488-490) and RS [lenses] (lines 161-163) both say an expansion's lens enters "by an edit to the harness's literal catalogue". RS adds that "the hook denies … a registry of lens sets".
   - FA [design] 3 and FA [chain] dFairHearing say a lens is catalogue data.
   - FA [folded] updated v2, SYS, MP, the gap register and the fates record, but not FS or RS (FA-mention count: FS 0, RS 0).
2. **The number of shape kinds.** SYS [design-role-shapes] says "Four role harnesses" and never mentions `experiment` (0 hits). NP [p2-testing] 6 registers `experiment` as the fifth kind.
3. **The closed kind set.** FD [core] C3 lists no `item` or `lens` kind, yet v2 [chain] dDeclaredLoop adds "the `item` kind in the kinds register" and FA [chain] adds "the `lens` kind". C3 was never amended.
4. **Fixed transitions.** FA [design] 9 fixes "each level's transitions between stages". FA [folded] lets a splice change them ("fixed except where a splice sits"). Item 9 was not re-marked. (Item 3 was re-marked.)
5. **The terminal set.** LF [settled] (line 305) and v2's revision note (line 127) say a build ends "landed, withdrawn or superseded". FS [transitions] lists eight terminal states, and P20 cites FS.
6. **Repository roles in the matrix (an ambiguity).** LR [matrix]'s arm "no core item names an expansion role" doesn't classify a repository role. FA-4 lets one act in a gov item, and FA [chain] dBoundRoles says the arms "read the composition". LR has 0 FA mentions.
7. **Record against code.** Today `workflows.toml` has none of the shape fields (kind, fan, cap): its schema comment lists only name, stage, driver, harness, roles, stages, enforced-by and trigger (`tools/roles/workflows.toml:1-11`). `WORKFLOW_NAMES` is closed at ten (`tools/roles/check_roles.py:90-91`). This is a gap the design owns, not a stale record.
8. **A seam today's code has and the design dissolved.**
   - Today's unattended run has `AUTH_MODES="slug prompt recipe"` (`tools/unattended/unattended.sh:1051`) and directives scoped to a mode (`playbook-followed:M7:recipe`, `:1042`).
   - NP [p1-unattended] 1 says "No slug, playbook or ask mode starts a run".
   - So the one existing per-run variant switch is retired, with nothing put in its place.

---

### 4. Candidates for one cohesive method

| # | Mechanism | Smallest losing test | Result against the records |
|---|---|---|---|
| A | **Presets as scenarios.** A named preset per build carries the variant's policy. | Can it declare an item, a role or a stage, or be picked per build? | **Loses.** P10: "structural choices are decisions, not policies". Presets assign keys only (v2 [presets]). Structure lives in the overlay (FA-1). `preset` is repository-wide, and only `attendance.scope` takes `build`. Kept as the policy slot of D. |
| B | **Playbooks as scenarios.** Extend the playbook kind and `repeat`. | Can a playbook choose roles, stages or order for a code build? | **Loses.** The canon is a content-piece recipe (PLAYBOOK-TEMPLATE declaration block). `repeat` enters at Design and only "supplies the feature design" (FS [entry]; NP [p1-unattended] 6). dScriptedRepeat refuses ordinary code builds. Kept as one shipped scenario of D. |
| C | **The FA composition alone.** Variation comes from repository stages and items whose own routes skip. | Two builds in one repository, one mobile and one data-system, run different roles and items at once, each with a witness naming its variant. | **Loses.** There is one composition per repository, and every build moves to it (FA [design] 11, 15; FA-7). A skip route needs a fact about the build, and none exists (no plan-record kind; 0 of 173). Selection would be scattered per-item outcomes with no named variant. Passes on structure. |
| D | **A `scenario` kind over the composition.** `scenario.<owner>.<name>` rows in gov's packs and the overlay. Each row has: `extends` another scenario; an entry disposition; the repository stages and items it activates; field patches and exclusions scoped to it (FA's grammar); roles, workflow entries and lens opt-ins; leg packs; a preset plus overrides; an admission predicate. `entry.place` picks it, `placement.check` witnesses it, and it is pinned in the claim and in each step's transition record beside the composition revision (FA-7's pin). Switches happen only at step boundaries. Cross-build pipelines use `depends-on`. | (T1) Does a principle forbid two compositions in one repository at once? (T2) Can it reorder gov's stages? (T3) Can it end a design-only build after Design? (T4) Can an unattended agent adapt it mid-build? | **(T1) Passes.** FA-7 already runs builds pinned to different composition revisions at once, so the position engine is multi-composition by design. P8's singular "the composition" needs a one-line amendment. **(T2) Refused**, as for every candidate (P20; FA [folded]). This is a principle limit, so it doesn't separate the candidates. **(T3) Undecided:** it passes only as record units through all five stages unless P20 changes. **(T4) Loses under the default** `instructions.edit`. Agents only propose. |
| E | **Conditional rows.** Each overlay row carries `applies-when: <predicate over build facts>`. | Can an owner pick a named variant from a shipped set, or compose two in order? | **Loses.** There is no unit to name, pick, ship, pin or promote. Overlapping predicates only show up at composition. It also needs the build-fact field that C lacks. |
| F | **Chains of builds only.** A "scenario" is a template that files child builds with `depends-on`. | Can it change roles or lenses inside one build? | **Loses as a whole method.** Every build still runs the one composition (FA-7). It survives as the cross-build pipeline half of D. |
| G | **Shape variants only.** The registry's named variant rows. | Can a variant change items or stages? | **Loses.** A shape belongs to a role item (SYS [design-role-shapes]). It survives as D's execution slot, inside agent-cap's fixed 5. |

**"Is there only one mechanism?" (question 8).** No. The design today has six separate seams:
- entry kinds;
- playbooks;
- presets;
- the FA composition with its repository stages;
- per-boundary policy sets;
- shape and lens registries.

They overlap without a common selector. Entry kinds pick the start, presets pick the posture, the overlay picks structure, and each is chosen at a different place: placement, the policy file, and the overlay at landing. Only D puts them behind one named, pinned, witnessed selector.

---

### 5. Pick

**I pick D**, the `scenario` kind, built by extending existing seams rather than adding a structural mechanism:
- the row grammar, pins and patches from dOrderedCharter (FA [chain]);
- presets from dKeptSession, as a scenario's policy slot;
- placement and `placement.check` from dPlacedRequest, as the selector and its witness;
- FA-7's per-step composition pin from dDeclaredLoop, as the record of what ran and the switch point for in-build pipelines;
- the playbook kind as the `repeat` scenario's Design input;
- the shapes registry's variant rows, as the execution slot.

The pre-shipped set follows the records' own build kinds: `feature` (Plan entry), `amendment`, `patch` and `playbook-run` (Design entry), plus `design-only`, pending item 2 below. Cadence programs stay programs.

**What the pick leaves undecided, for the owner:**
1. Whether to amend P8 to "a composition per build's scenario", and FD C3 to register `scenario` (P16 makes a kind change an owner-ratified amendment).
2. The design-only scenario: record units through all five stages, or a P20 change adding a designing-to-terminal row.
3. Whether a scenario may carry per-build policy values. The only precedent is `attendance.scope: build`, and P10 says "one policy file, one reader".
4. Who may adapt a build's scenario mid-build while unattended. This means walking `instructions.edit`'s alternatives (LI) and deciding where a proposal goes, given P18's rule that no build parks.
5. A promotion route from a build's pinned scenario delta to a reusable `scenario.repo.*` row: a new `promoted-from` source, or a Loop Review proposal kind. Neither exists (MP [edges]; LE `loop.propose`).
6. Several scenarios inside one build in parallel, per feature or unit. This waits on the owed feature and unit transition tables (`gap-flow-15`).
7. How a wrong pick is caught after placement: whether `design.reentry` or a plan revision may re-pick at a step boundary, and how witnesses carry across.
8. Caps per scenario under agent-cap's fixed 5, including what `probe.experiment.authority: free` means.
9. Lens removal (exclude versus swap), and whether repository lenses owe the shipping test.

**Tests the build must run** (described here, not built):
- composition checks over every shipped scenario, seen red on a planted scenario that reorders a gov stage;
- two builds pinned to different scenarios, positioned concurrently;
- a planted wrong `placement.check` predicate, refused;
- a scenario switch at a step boundary that carries its witnesses.

**Files read:**
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`: v2, FA, FS, NP, SYS, RS, LR, LRT, LE, LM, MP, FD, LF, LI, and the dispatch-124 return `2026-10-19-build-PLAY-dClosedLoop-1-research-flow-design.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dScriptedRepeat\README.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\guides\PLAYBOOK-TEMPLATE.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\hooks\agent-cap.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\workflows.toml`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\check_roles.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\tier2-review.js`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\unattended\unattended.sh`

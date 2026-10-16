# Layer review: the instruction layer

**Serves:** research PLAY-dClosedLoop-1

The owner's layer-by-layer review of the design, starting with the instruction layer. This record
holds:
- the owner's words;
- what the layer loads today, measured;
- the owner's layer set against the current design;
- what it does not yet cover;
- the dos and don'ts the charter shows;
- the recommendations;
- the forks put to the owner;
- the fold of two Tier-2 rounds, in `[revised]`.

## [words] The owner's words, 2026-10-15

> Let's revisit the design at its highest level layer by layer and ensure the design accounts for
> everything and every piece is planned out. Advise me where necessary to ensure it pieces together
> into a coherent, extendable practice. Provide recommendations.
> Currently, I'm thinking of this product in layers on top of one another, and this is already
> reflected in how its re-architecture is shaping up. There are 4 **mandatory** product layers: 1.
> Instruction - 2. DLG - 3. Roles - 4. Memory (the 'build' part of the memory, since builds are what
> this product drives), without them, this product is shapeless. There are also additional
> 'expansion' layers that add functionality to the core layers but, technically, are not required
> for it to run: 4.1 Memory (the other part of the memory - all the bookkeeping that exists in the
> repo today that enhances the build trail, backlog functionality, codebase map, gotchas ) - Let's
> start by reviewing the first one.
>
> [1. Instruction layer]
>
> * Charter.
> * Policies, principles.
> * Protocols, templates, guides - instructions that shape the product processes.
> * Importance levels, clearly stated. Ranked, from 0 to 7.
> * A tag system must be adopted and enforced at this layer, so any instruction can be seamlessly
>   mapped to a process or a role it belongs to.
> * Should skills be considered part of this layer (technically, they are also instruction and also
>   must follow the same instruction conventions and policies; currently we have session-kickoff,
>   deploy-governance, build, drift-audit, lexicon, memory-recall, runlog, unattended, cleanup)?
> * Important: this layer must enforce not just WHAT is instructed but also HOW. Instruction shaping
>   is mandatory in agentic development - two primary principles here are 1. everything that's
>   loaded must provide clear direction and constraints, ambiguous prose must not exist; 2. HOW MUCH
>   is loaded into context is just as important as WHAT is loaded - neither too much or too little
>   is good, every level below must be oriented with instructions precise to their process and role.
>
> This layer's load bearing part is entirely 'text' and therefore text is where optimization has to
> happen. DOs and donts using the current AGENTS.md as an example:
>
> * 'coding-governance — agent charter' - title provides no direction or instructions, it's not
>   useful in any way to the agent that loads it, despite being the very first non-system string to
>   be read. An agent would already know this is Coding Governance, and since this file's already
>   loaded automatically, naming it 'agent charter' is meaningless. 'Non-negotiable project
>   instructions. Importance level: 0 (Highest). They must always be enforced unless explicitly
>   overridden by the owner'.
> * 'Rendered from the coding-governance charter template, whose version is the marker below.' -
>   does the agent need to know that right at the start? This note may be important for orientation
>   or intructions re-rendering but definitely not on each session/agent load.
> * '1. Governing practices' ..etc - sections are numbered, not tagged. Section numbers, letters,
>   special characters should be retired in favor of tags, that will eliminate any chance of
>   ordering issues.
> * 'Agent roles — hand the work to its role'; 'Protocols — read the one whose trigger holds' - seem
>   to be great titles, giving clear instruction.
> * There are tags used in the file now, however, all they're used for is instruction rendering -
>   they're not otherwise mapped to anything else in the repo. Instructions must interact with lower
>   layers by step/role/process tags/pointers - clearly state which tags a step/role/process is
>   supposed to orient itself in.
>
> Instructions and templates should be mechanically rendered and enforced wherever possible,
> instruction rendering should happen from am extensive preset catalogue and owner interactions can
> happen through a session or a scripting tool that allows instruction addition/editing/deletion to
> its respective manifest.
>
> Does this layer's shape make sense? How does it fit into the current design? What is not yet
> covered at this layer?

## [layers] The layer model

The owner's model has four mandatory layers, without which the product is shapeless:
1. instruction;
2. the DLG flow;
3. roles;
4. memory, meaning the build trail.

Expansion layers add function to a core layer and are not needed to run it. The first named is memory
bookkeeping: the backlog, the codebase map, gotchas, and the trail's enhancements.

**It sharpens the current design.**
- v2 sets three layers and leaves memory implicit, carried by P22 (position derived from witnesses)
  and P26 (every exchange a typed record).
- Naming the build trail as the fourth mandatory layer names the substrate that `next`, the card and
  every work order already read.
- The four layers form a cycle, not only a stack. Instructions direct the flow, the flow names items,
  roles perform them, and their returns become memory.
- Memory feeds back twice: `next` derives position from it, and the card and every work order are
  rendered from it.

**The owner's addition, sent mid-turn, verbatim:**

> There were additional 'expansion' layers that were omitted from the other prompt: 5. Instrument
> layer (tools that are supposed to expand other layers, such as memory-recall, playbook, lexicon,
> memory-tree, etc.) - 6. Monitoring layer (logging, monitoring and health tools, such as runlog,
> process-monitor) - 7. Deployment layer (run-gates and its children, govkit, gate-lint, drift-audit).
> - 8. ??? any other layers that make sense in this design? Do these ones make sense, or should I be
> thinking about this differently?

**Layers are capabilities, and kits implement them.**
- Layers 1 to 4 name capabilities, which is what the practice does. Layers 5 to 7 group tools, which
  is how it is done.
- Mixing the two axes files core engines as optional:
  - playbook renders the charter, so it is the instruction layer's engine;
  - memory-tree keeps the build trail, so it is the memory layer's engine;
  - run-gates gives the verdict the floor requires before the default branch moves, so it is the Test
    step's engine.
- The recommended framing:
  - a layer is a capability named by a tag;
  - a kit is an implementation, and its descriptor declares the layer and the extension point each of
    its parts serves.
- Under that framing:
  - **"Instrument" dissolves**, because every kit instruments some layer.
  - **"Deployment" splits**:
    - the verdict engine and the lander are the flow's Test and Deploy engines, and are core;
    - govkit is Distribution;
    - drift-audit is Observability.
  - **"Monitoring" stands**, as Observability.

**One test sorts core from expansion.** Can a fresh adopter carry one build from request to landing
without it?
- If not, it is **core**:
  - instruction;
  - flow, including its verdict engine and its lander;
  - roles;
  - memory, meaning the trail;
  - runtime.
- If so, it is an **expansion**:
  - knowledge, folded into memory as its library side by KN-1 (2026-10-16);
  - observability;
  - integrations;
  - distribution, once gov is installed.

**Runtime is the missing core layer.** It is what executes the cycle:
- the supervisor and its checklist engine;
- act sessions and the spawn harness;
- the hooks that enforce at the tool boundary;
- the `next` verb and the owner's controls (RT-3);
- isolation;
- process supervision.

Three reasons:
- P24 makes the checklist a program, and a program needs a runner.
- The items v2's `[owed]` held without a home were runtime: the executor and its harness.
  dWellOiledMachine now owns them. The landing queue and the lander's core re-check stay Deploy's
  (dShippedRelease), and only the lander's hardening moved to Runtime.
- The instruction layer's MUST and NEVER become real only where Runtime enforces them.

In one line: Instruction says, Runtime enforces, Flow witnesses, Memory proves.

**The proposed expansions:**
- **Knowledge**, consulted to decide better:
  - the codebase map and its house index; the reuse lookup retires (memory layer F4-3);
  - consulting decisions, through memory-recall;
  - bug classes, the gotchas;
  - the lexicon;
  - consulting past research.

  It absorbs most of the owner's memory bookkeeping. The research records and the major decisions
  themselves are core: core items write them, and Knowledge holds the consulting (the memory layer's
  refinement).

  Revised 2026-10-16 (KN-1, `build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`): Knowledge folded into the memory layer
  as its library side, and its kits became memory's optional components.
- **Observability**, signals about the loop and the runtime, read by Maintain and the Loop Review:
  - run logs, through runlog, whose journal grammar is core (Runtime);
  - process health, from process-monitor's reports;
  - drift, through drift-audit;
  - gate health and flakes;
  - cost and token telemetry;
  - instruction effectiveness (R-J).
- **Integrations**, adapters to outside services:
  - remote CI, P3's designed slot;
  - notifications beyond the turn;
  - cloud hosts, through `run.host`;
  - trackers.
- **Distribution**, the product's delivery: govkit, the adopt scripts, overlays, the install of each
  harness's render targets, which Runtime's harness adapters define (R-K), and version currency.

**The rules that keep it extendable:**
- **Dependencies point one way.** Core never depends on an expansion. An expansion attaches only at an
  extension point a core layer declares, so a core-only adopter runs. Today's design breaks this three
  times:
  - the builder's work order carries bug classes, from Knowledge;
  - the reuse scout's work order carries the map's dossiers, from Knowledge;
  - each role's static block carries the universal gotcha classes, from Knowledge (memory layer).

  Each such field, and each part of a core render that carries an expansion's content, becomes an
  optional slot that its expansion fills. A core-only install renders it empty.

  Revised 2026-10-16 (KN-1): bug classes are core, on memory's library side, so the first and the third
  are no longer breaks. The map is an optional component of memory, so the second stays an optional
  slot.
- **Every layer fills one contract**, core or expansion. The contract holds:
  - its tag and its definition;
  - its instruction units;
  - its engine kits;
  - its record kinds;
  - the extension points it declares, and those it uses;
  - its policies and its gates.

  A new expansion is a filled contract, which makes "extendable" a mechanism rather than a hope.
  "Layer" joins foundations C3's closed set of extension kinds, so it has a factory (C4) and a
  conformance gate (C5), both built by dOrderedCharter.
- **Layers are named by tags, not numbers**, the rule the owner set for sections. Numbers are display
  order only.
- **The picture is a cycle on a base, with plug-ins**, not a stack:
  - the core cycle runs from Instruction to Flow to Roles to Memory, and back;
  - it runs on Runtime;
  - expansions plug in at declared points;
  - Distribution installs it all. The diagram is
    `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-model.svg`.

**Kits mapped to layers:**

| Kit or tool | Layer | Core or expansion |
|---|---|---|
| playbook | Instruction: renders the charter | core engine |
| agent-instructions | Instruction: each harness's instruction files, which Runtime's harness adapters define | core |
| roles | Roles: definitions and handoffs | core engine |
| workflows | Roles and Runtime: the review and unit harnesses | core; Runtime runs them inside act sessions |
| memory-tree | Memory: build folders, records, the index, hygiene | core engine; its backlog, rotation and gotchas settle at the memory review |
| the loop kit, to be built | Flow: stage tags, checklists, the position function | core engine |
| run-gates | Flow: the Test verdict | core engine; its legs come as packs |
| gate-lint, pytest-parallel-guardrails | Flow: verdict leg packs | expansion |
| `push-main.sh`, the lander | Flow: Deploy (dShippedRelease); the lander's hardening is Runtime's | core |
| the turnstile | Flow: Test, the host-wide bar semaphore | core |
| session-kickoff | Flow: Entry, through the orientation scout | core |
| unattended | Runtime: the supervisor, `resume-tick.sh` grown, and the `next` verb (RT-3); the `/unattended` Skill is a client of `run <build>` | core |
| hooks | Runtime: enforcement at the tool boundary | core |
| process-monitor | Runtime: reaping; its reports feed Observability | core |
| branch-reconcile and the cleanup Skill | Runtime: isolation housekeeping | expansion |
| codebase-map, lexicon, memory-recall | Memory: the library side's optional components (KN-1); `reuse_lookup.py` retires | expansion |
| runlog, drift-audit | Observability; runlog's journal grammar is core (Runtime) | expansion |
| govkit and the adopt scripts | Distribution | expansion |
| lib | shared primitives inside kits | no layer |

## [current] What the layer loads today, measured 2026-10-15 (`wc -c`)

| Load point | When | What, in bytes |
|---|---|---|
| Session start, main session | every session | `CLAUDE.md` 12, importing `AGENTS.md` 16,732; the auto-memory index `MEMORY.md` 13,187, injected by the harness under its instruction framing; the hook's card, beside the SessionStart output of check-wiring and procmon; the harness's lists of agent and Skill descriptions: nine agents, seven project Skills, and the user-level Skills beside them, session-kickoff among those through a symlink. deploy-governance is installed as no Skill |
| Role spawn | each subagent | its agent definition (nine files, 45,213 together) and the handoff's task part; no `CLAUDE.md` (`omitClaudeMd: true`); SubagentStart `additionalContext` from scratch-guard |
| Act session (Runtime) | each role act | `CLAUDE.md` importing the whole `AGENTS.md`, driver-scoped units included; the act's static block; the work order cut at act launch |
| Hook output | at hook events | Stop-hook block reasons (format-guard, stop-guard) and PreToolUse deny reasons, composed in code |
| Trigger reads | when a charter pointer's trigger holds | guides, `HYGIENE.md`, `TEMPLATE-SPEC.md` and one path rule, each read whole: 409,376 as counted, which includes three guides no charter pointer names (ANNOTATION-STYLE, PLAYBOOK-TEMPLATE, SESSION-KICKOFF); the three unattended sub-guides are reached through UNATTENDED-PROTOCOL, and the four unattended guides alone are 216,448 |
| Skill invocation | on `/<skill>` | nine `SKILL.md` files of 3,611 to 18,310 each; session-kickoff's 258,177 bytes of engine files are mostly executed code (`manifest-check.sh` and its test), not loaded text |

The counts are `wc -c` on a working copy under `core.autocrlf=true`. `CLAUDE.md`,
`.claude/rules/product.md` and the deploy-governance `SKILL.md` check out CRLF, so their counts include
CR bytes.

The charter's state:
- it has 46 tagged rule lines and three numbered sections;
- it renders from a 13,695-byte template;
- its tags key the renderer and the roles kit's join: each role's `rules:` key names the rule tags it
  loads, `roles_lib.py` selects them, and `check_roles.py` checks the join.

Six load points already carry declared byte budgets: `tools/template-size-limits.txt`, gated by
`check-template-size.sh` with a high-water ratchet, where the owner decides who may raise a row:

| Load point | Budget, bytes |
|---|---|
| `coding-governance-agents.template.md` | 49,152 |
| `AGENTS.md` | 20,480 |
| `skills/session-kickoff/SKILL.md` | 18,432 |
| `memory/guides/BUILD-METHOD.md` | 30,720 |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 66,860 |
| `.claude/skills/unattended/SKILL.md` | 10,240 |

Foundations `[step-1]` measured about 25 load-bearing documents, about 551 KB, arriving by six routes.

## [fit] The owner's layer against the current design

| The owner's element | The current design | Status |
|---|---|---|
| Charter | dOrderedCharter re-founds it: the top envelope, the front door, the drive section rendered from kit descriptors, the 32 KiB cap (foundations `[step-1]`) | designed |
| Policies, principles | one policy file, with the catalogue and presets in v2 `[policies]` and `[presets]`; the principles in v2 `[principles]`, with a registry and a meta-check (P10, P16) | designed |
| Protocols, templates, guides | registered at level 3 and enveloped (foundations R2); facts, not prose (P11); specs structured (P12) | partly: still hand-written whole documents, none rendered from the structured sources, each read whole |
| Importance levels 0 to 7 | the ladder as R-G renumbers it: the platform above it, 0 the charter, 1 the card, 2 to 7 below | designed; before L3 it ran one off from the owner's model, with the charter and the card at 1 |
| A tag system mapping instructions to processes and roles | the section-tag grammar and its resolver (dOrderedCharter); stage tags (dDeclaredLoop); practice tags; the roles kit's `rules:` join of each role to charter rule tags | partly: only roles join to rule tags; nothing joins an instruction to a step, item or policy; checklist items are numbered |
| Skills | level 4; "a Skill is a Claude Code shortcut over the same command" (foundations R5); a kind with a factory (P16) | partly: the shape is decided, but today's Skills carry their own procedures |
| HOW: no ambiguous prose | P11, facts only; tags, never `§` | partly enforced: `check-microformats.sh` closes the micro-formats' grammar, `check-playbook-parity.sh`'s S4 arm refuses a section cited by number, `format-guard.js` holds the final message; no grammar governs the rest |
| HOW MUCH: precise loads | the charter's 32 KiB cap; six load points budgeted and gated (`template-size-limits.txt`); one line per role (foundations R6); `orient.budget` record-only; gap-orient-07 | partly: no load set is computed per role and item, and no injected load point is measured |
| Mechanical rendering and enforcement | envelopes generated from the registry, and a gate over them | partly: documents, not units |
| A preset catalogue | the practice catalogue with `charter.practices`; policy presets | partly: practices only |
| An owner write path | the policy CLI needing an interactive terminal; a `new` verb per kind | missing for instructions |

## [uncovered] What the layer does not yet cover

Proposed gaps, each with its proposed owner build. The register holds them as `gap-found-09` to
`gap-found-16`, in this order.

1. **Instructions map to almost nothing below them.** HIGH, dOrderedCharter.
   - Tags name sections, and the roles kit joins each role to charter rule tags (`rules:`), but
     nothing else joins.
   - Checklist items are numbered.
   - No registry joins an instruction to the step, item or policy it serves, so no loader can select
     an agent's instructions by its item.
2. **Load is mostly unbudgeted and unmeasured.** HIGH, dOrderedCharter.
   - Six load points carry declared, gated byte budgets (`[current]`); the rest carry none.
   - No load set is computed per reader, so none is measured against a budget.
   - Session start loads about 30 KB of repository and user text before the card.
   - A trigger read pulls whole documents, up to 216 KB for the unattended four.
   - The injected load points, the auto-memory index, the harness's lists and hook output, are
     measured nowhere.
3. **Loaded text is unshaped.** MED, dOrderedCharter. Nothing checks that a loaded line gives
   direction. Today's charter shows the result:
   - headings name provenance or a label ("3. Generated", "agent charter");
   - it points at text it never loads ("the marker below");
   - render provenance loads every session;
   - a placeholder reads as a stale fact: "Worktrees: none yet" means that no worktree bootstrap
     script exists, and reads as "no worktrees" beside 13 of them;
   - a model name loads in the trailer.
4. **Protocols and templates are hand-written monoliths.** HIGH, dConvergedCharter.
   - 409 KB of guides and templates restate the flow's steps in prose, so one rule lives in a guide,
     a Skill and a checklist at once.
   - Nothing renders a protocol view from the loop's, the roles' and the policies' structured
     definitions.
5. **Skills are parallel procedures.** MED, dConvergedCharter.
   - build, unattended and session-kickoff carry their own procedures, rather than shortcutting a CLI
     command into the flow.
   - Every installed Skill's description loads each session without a trigger contract.
6. **Memory instructs outside the ladder.** HIGH, dOrderedCharter; the memory layer review may move it.
   - The auto-memory index loads every session under the harness's instruction framing, and its
     feedback entries carry directives.
   - Gov never renders it: the harness writes and injects it from outside the repository, per user,
     node and worktree.
   - Nothing promotes a standing directive into the instruction layer, or holds memory at evidence.
7. **No write path for instructions.** MED, dOrderedCharter.
   - The owner can change an instruction only by editing a source or the template by hand.
   - There is no manifest, no validating command and no recorded change.
   - There is no instruction preset beyond the practice catalogue.
8. **No instruction's effect is measured.** LOW, dCalibratedLens. Nothing records which units an agent
   loaded or broke, so text that bears no load is never found, though P11 says to remove it.

## [charter-today] The charter's dos and don'ts

**The owner's, recorded:**
- the title is not a directive;
- render provenance loads every session;
- sections are numbered;
- "Agent roles — hand the work to its role" and "Protocols — read the one whose trigger holds" are
  the model headings;
- the tags map to nothing but the renderer and the roles kit's join.

**Added from the same file:**
- **Don't point at text that isn't loaded.** "Whose version is the marker below" names a marker the
  agent never sees.
- **Don't let a typed line read as a stale fact.**
  - "Worktrees: none yet" is the `WORKTREE_SCRIPT` placeholder: it says that no bootstrap script
    exists, and reads as "no worktrees" beside 13 of them.
  - The trailer's model name meets a harness reminder naming another model every session.
  - Derive the fact at render time, or point to where it is derived. The playbook renderer's `PROBES`
    table and the registry's `probe =` rows already derive facts at render, so they are the seam.
- **Don't load what the reader never acts on.**
  - The node registry loads every session. The card names the session's node, but derives that cell
    from this very table, through the kickoff manifest's `registry:` key. The registry leaves the
    loaded charter only in the unit that re-points that key at its new home.
  - The driver reads `[migrations]`, `[bytes]` and `[spec]` though it does no role work. Their reach
    belongs in the work orders of the roles they bind.
- **Don't name sections by provenance** ("This repository", "Generated"). Name them by what the reader
  does.
- **Keep one thing in one source.** The roles kit already renders the charter's role list and the
  harness's agent list from the same role files, with the agent description carrying the trigger. Keep
  it so.
- **Do lead with the level and the override rule.** For example:
  `[AGENTS.md · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]`.
- **Do keep trigger pointers**, the shape the protocols section already has.
- **Do keep the micro-formats with the driver**, which reports. "Level" says what wins, and scope says
  who loads it, so they stay at the top level and are scoped to the driver alone.

## [recommendations] What makes the layer coherent and extendable

**R-A. The unit is the atom, and documents are renderings.**
- The registry gains unit rows. Each row carries:
  - a tag;
  - a level;
  - a statement type;
  - scope tags;
  - a trigger;
  - a budget class;
  - `required-by`: the roles and items that require it, which R-C's "too little" refusal reads;
  - its source, whether written text or rendered from a structured definition;
  - its owning kit, or the repository for an adopter's own unit.
- The charter, a protocol view, a role's static instructions and a work order are each assembled from
  units by their tags. Each is wrapped in the envelopes foundations R2 already designs.
- An envelope names its document's level. A unit of another level inside it keeps its own level,
  marked where it renders, and a conflict resolves by the unit's level. The charter's policy block is
  level 2 inside the level-0 charter.
- The kind "governing document" becomes "instruction unit", made by the same `new` factory. v2's
  dOrderedCharter row and foundations C3 carry the new name.

**R-B. One tag system, namespaced, registered and joined both ways.**
- A tag's full spelling is `<namespace>.<name>`, as the roles layer spells `role.<name>`. Where a
  context fixes the namespace, such as a checklist or the policy file, the short name stands. Full
  spellings are unique, so the item `item.build.scope` and the policy key `policy.build.scope` never
  collide.
- The namespaces are `reader`, `level`, `layer`, `step`, `item`, `role`, `policy`, `practice`,
  `principle`, `kind`, `record` and `kit`.
- Level says what wins; scope tags say who loads it. Two kinds of namespace:
  - **selectors** decide who loads a unit: `reader` (with `reader.every`, for every reader), `role`,
    `item`, `step`, `practice` and `policy`;
  - **descriptors** classify a unit and never select it: `level`, `layer`, `principle`, `kind`,
    `record` and `kit`.

  A unit that names no role binds the driver alone (roles `[tags]`), so a top-level unit for every
  reader carries `reader.every`.
- The joins, checked both ways:
  - every unit carries at least one selector;
  - every step, and every item whose actor reads instructions, a role or the owner, has at least one
    unit. Command and hook items are exempt, since no model reads their units;
  - every role has at least one unit;
  - every tag used is registered.
- Each join runs over a population it asserts is non-empty, and the build that creates the population
  arms it: dOrderedCharter the unit join, dDeclaredLoop the step and item join, dBoundRoles the role
  join. Until then the join reports "unarmed", never green.
- The join extends a seam. The roles kit already joins each role to charter rule tags through its
  `rules:` key, `roles_lib.py` selects each role's units by tag, and `check_roles.py` checks the join.
  R-B widens it to steps, items and the other selectors.
- The name check is core: a shape check on the namespace and the name. The lexicon, an expansion,
  adds its vocabulary check at an extension point where it is installed (P28).
- Checklist items keep the flow's settled tags, such as `plan.input` or `build.unit-pass`; numbers are
  display order only. The unattended driver's handle registries are the seams the item and directive
  tags extend: `DOD_CORE`, item handles with their witness class, and `DIRECTIVES_CORE`, directive
  handles with their method section and scope.
- dOrderedCharter builds the mechanism, and each chain build registers its own tags, as with the
  principle registry.
- Retiring a section number re-points its readers in the same unit. The charter's readers are
  `roles_lib.py`'s `SECTION_ONE_RE`, which finds the rules under `## 1. ` and refuses with R0 without
  it, and the review harness prompts that grade by section number. The hygiene gate's `§n`, `Sn` and
  `ACn` scope tokens and the other positional references are Convergence's inventory (v2 `[open]`).
  Frozen records keep their numbers (P19).

**R-C. Load sets are derived, budgeted and measured.**
- A load set contains:
  - the units scoped to every reader;
  - the units scoped to the reader's role, the driver's scope included;
  - the units scoped to its item;
  - the active practices' reach for the step;
  - the policy values the item reads;
  - the task and the handed facts, under the work order's packet budget (roles layer).
- Each load point declares a budget, in bytes of the committed blob, never of a working copy.
  - A budget is per load point, one render each. A budget summed over the files a session reads is
    what `TOOL-dSpentCeiling-1` retired, and it stays retired.
  - The budgets extend `tools/template-size-limits.txt` and `check-template-size.sh`, with their
    high-water ratchet and the owner's rule for who may raise a row. A new load point joins that
    table.
  - The role block is the exception: its carrier is `check_roles.py`'s `BODY_CEILINGS` (roles
    `[tags]`), which the render reads for a role file. Each load point has one carrier.
- Load points come in two classes:
  - **Rendered**, which gov writes: the charter, role files, Skills and work orders. The render refuses
    a set over budget, which is too much. It refuses a set missing a unit that a role or item names in
    `required-by`, which is too little.
  - **Injected**, which the harness or a hook places: the auto-memory index, the harness's agent and
    Skill lists, and hook output. Gov cannot refuse these, so they are measured at session start and a
    breach is reported. Hook text is composed from registered units (`gap-rt-13`).
- A refusal leaves the spawn undone, and the caller files an ask naming the overage. Under
  `instructions.checks=warn`, the set loads whole and the reader sees the breach; under `record`, the
  breach is recorded. Neither skips the check (LR-1).
- Field loads are measured from the roles' runs.
- The act session is a load point. Its set is a role's set: driver-scoped units never reach it
  (`gap-rt-12`).

**R-D. A closed statement grammar.** Every loaded unit is one of six types:
1. a directive: MUST, NEVER or ALWAYS, with its scope and its condition;
2. a constraint, with its value;
3. a definition;
4. a pointer: a trigger leading to a tag or a command the reader can load;
5. a policy value, rendered from the policy file;
6. a fact, derived, with its source.

Around the grammar:
- Headings are directives (P11).
- Render provenance lives in a sidecar lock, never in loaded text.
- The grammar governs units. Handed content is data: facts, findings, diffs and quotes travel in the
  work order's fenced blocks labelled as data, and are never read as directives (dBoundRoles' render).
- A reuse entry (memory layer) is a directive: MUST, with its trigger as its condition.
- A check enforces the grammar. It extends the instruction gates that exist: `check-microformats.sh`,
  whose closed grammar covers the charter's micro-formats, `format-guard.js`, `check-line-length.sh`,
  `check-placeholders.sh`, and `check-playbook-parity.sh`, whose S4 arm already refuses a charter
  section cited by number.
- Its red cases are the shapes found in today's charter, each seen red on the charter as it stands:
  - a provenance paragraph, which is none of the six types;
  - a numbered heading, which is no directive;
  - a pointer to text never loaded ("the marker below");
  - a fact with no source ("Worktrees: none yet").
- Reuse aHonedRuleset's prose census and `memory/guides/ANNOTATION-STYLE.md`.

**R-E. Protocols and templates are rendered views.**
- The sources are the loop's checklists, the roles' definitions, the record schemas and the policy
  catalogue.
- The guides and templates become views sliced by tag, so an agent reads its slice and never a whole
  guide.
- Explanation for humans lives outside every load set, under `help/`. dConvergedCharter moves the
  retired guides' rationale there.

**R-F. Skills belong to the layer, at level 4, as thin entries.**
- A Skill is its trigger contract, the CLI command it shortcuts, and the tags of what it enters. It
  has no procedure of its own (P1).
- **Core entries**, each entering the flow:
  - session-kickoff: Entry, through the orientation scout;
  - build: the Build step, attended;
  - unattended: a client of `run <build>`, which Runtime's supervisor executes.
- **Expansion entries**, each in its own layer:
  - memory-recall and lexicon: memory's optional components (KN-1), lexicon naming at Design and Build;
  - runlog and drift-audit: Observability;
  - cleanup: Runtime's isolation housekeeping.
- deploy-governance retires (the memory layer's tooling map). Adoption runs through govkit, in
  Distribution.
- Each Skill declares its layer. Its description is budgeted and phrased "Use when …; runs …".

**R-G. Renumber the ladder to the owner's model.** The platform sits above the ladder, unranked by the
repository. The levels:

| Level | What sits there |
|---|---|
| 0 | the charter |
| 1 | the build's card, so the charter outranks it by level alone and the special rule retires; this matches OR-5's "priority 1 along the charter" |
| 2 | the loop and the policy values |
| 3 | methods, protocols and templates, as rendered views, and reuse entries |
| 4 | runbooks, Skills and path rules |
| 5 | the role's static instructions, an act session's static block among them |
| 6 | the task, an act among them |
| 7 | records and memory, evidence only |

Rendered text uses one term throughout: "level". The renumbering re-points the old values' carriers:
foundations R2's envelope, precedence rule and gate, and `[fit]`'s level 3, each under a dated
`Revised:` line. v2's dated revision notes keep "rank 1", since they record what held then; v2's
revision note of 2026-10-16 supersedes them.

**R-H. Memory instructs nothing.**
- A standing directive found in memory is promoted into the instruction layer as a unit, through the
  write path. The memory keeps a pointer.
- The auto-memory index is an injected load point. The harness writes and injects it from outside the
  repository, per user, node and worktree, so gov never renders it. Gov measures it at session start
  against its budget, and reports a breach or a directive found in it (`gap-found-14`).
- The promotion route is settled with the memory layer.

**R-I. An instruction manifest and a guarded write path.**
- There is one manifest per kit, and the adopter's own manifest, its overlay. A manifest may be split
  into parts, such as one beside each feature for its reuse entries (memory layer).
- Manifests merge deterministically with the adopter's overlay.
- One command adds, edits, removes, lists, renders and checks units. It extends the seams that already
  serve this text: `render_playbook.py` with `adopt-playbook.sh --check`, the placeholder registry, and
  the roles kit's house overlay.
- The command proves its caller is the owner by `instructions.proof`, as `policy.proof` does for
  policy writes: `tty-cli` by default, with `signed` and `both` allowed, and presets never touch it.
  An agent's shell call cannot pass the proof, so an agent only proposes a change, through the flow
  (P20).
- Validation does not live in the command alone. The same checks run as a gate leg over the tree and
  at every render, so an edit at a structured source, a merge, an overlay edit or a kit install is
  validated where the command never runs. The checks are:
  - the schema;
  - the tags;
  - the grammar;
  - the budgets;
  - conflicts at the same level;
  - references: a removal or a rename strands no pointer unit, no `required-by` join, and no step,
    item or role left with no unit.
- A tag is active or retired. A retired tag stays registered with a forward pointer, since frozen
  records cite it, and its name is never reused.
- Across nodes, manifests are row stores, reconciled additively at merge. Rendered views are
  re-rendered after a merge, never merged. The change record is append-only. The command writes a
  manifest row and its change record in one commit, and the re-render is the regen leg's.
- The instruction files are the ones the manifest registry lists: each manifest and part, each
  structured source (loop checklists, role definitions, record schemas, the policy catalogue) and each
  rendered target. That list is the predicate Runtime's one-door check reads.
- The command records every change and re-renders every affected load set.
- The owner uses it directly; top-level principles still need an owner-ratified amendment (K2).
- A rendered unit changes at its structured source.
- Instruction packs extend `charter.practices` into a preset catalogue: methodologies, governance
  sets and language packs.

**R-J. Instruction effectiveness feeds the Loop Review.**
- Effectiveness rests on what is witnessed, never on what an agent says it followed (P23):
  - **loaded:** the render records which units each spawn received;
  - **broken:** a confirmed finding or a red that names a unit's tag.
- "Followed" is not measured, since only the acting agent could type it, and no return schema gains a
  self-report field.
- The Loop Review prunes units that load but that no check enforces and no confirmed breach has cited
  over its window. It tightens the ones broken often (P9, extended to instructions).
- runlog's `prose.py` already measures final messages against the micro-format units, the seam the
  breach measure extends.

**R-K. Load points per harness come from Runtime's harness adapters.** The instruction layer defines
each load set. Each registered harness adapter (Runtime `[harness]`, `runtime.harnesses`) says which of
its harness's files carry it. The agent-instructions kit already wires each harness's instruction
file, Gemini, Copilot, Cursor and Windsurf included, and measures Codex's 32 KiB limit (`CODEX_MAX`).
It is the seam the adapters' render targets extend.

| Harness | Load points |
|---|---|
| Claude Code | `CLAUDE.md`, agents, Skills, hooks, rules |
| Codex | `AGENTS.md` alone. Codex reads one file per directory, so an override file would replace the charter rather than add to it. The 32 KiB limit covers the whole chain of files it reads. Codex has no SessionStart, so the card reaches it only through the adapter's launch input (`gap-rt-11`) |
| The rest | the file the agent-instructions kit wires for each |

## [forks] Asked, 2026-10-15

**L1. "How should the layer model be framed?"**
- Offered:
  - Capabilities, Runtime core (Recommended);
  - Capabilities, four core;
  - Tool-based layers.
- Answer: Capabilities, Runtime core (Recommended).

**L2. "Which expansion layers should the design carry?"** Multi-select, with each expansion plugging in at
a declared extension point and the core never depending on one.
- Offered: Knowledge, Observability, Integrations, Distribution.
- Answer: all four.

**L3. "How should the importance levels be numbered?"**
- Offered:
  - Charter 0, card 1 (Recommended);
  - Keep today's ladder.
- Answer: Charter 0, card 1 (Recommended).

**L4. "Are Skills part of the instruction layer, and what may they contain?"**
- Offered:
  - Level 4, thin entries (Recommended);
  - Level 4, own procedures;
  - Outside the layer.
- Answer: Level 4, thin entries (Recommended).

## [settled] What changed, 2026-10-15

**v2 `[layers]` is added.** It holds:
- the capability framing;
- the test that sorts core from expansion;
- five core layers: instruction, flow, roles, memory, runtime;
- four expansions: knowledge, observability, integrations, distribution;
- the cycle on a base;
- the layer contract;
- optional slots for expansion-filled work-order fields.

Revised 2026-10-16 (KN-1): three expansions remain. Knowledge folded into the memory layer as its library
side, and its kits became memory's optional components, which fill optional slots the same way.

**Principles.**
- P11 now carries the owner's first instruction principle: everything loaded gives direction, through
  six statement types.
- P13 now carries the levels and the scope tags as the join keys.
- P27, load is precise, is the owner's second instruction principle.
- P28 says layers are capabilities and the core never depends on an expansion.
- All four are owner-ratified in this round: the owner's own principles, and the layer framing they
  chose. Each will need its enforcing check in the principle registry (P16):
  - P27's is the load-set render check. Its refusal softens by `instructions.checks`, which
    foundations C6 allows since LR-1: `warn` and `record` still run the check and show every breach,
    and no switch skips it;
  - P28's is the one-way dependency check and the layer contract's conformance gate, the gate of the
    layer kind (foundations C3).

**The ladder** is renumbered:
- the platform sits above it;
- the charter is level 0, and the card level 1;
- Skills are level-4 thin entries;
- rendered text uses the one term "level".

**Two policies** are set from the owner's own words in this round. Their alternatives are offered, but
not yet walked:
- `instructions.checks`:
  - the values are `refuse`, `warn` and `record`;
  - the default is `refuse`, from "enforced wherever possible";
  - `velocity` sets `warn`.
- `instructions.edit`:
  - the values are `owner-command-agents-propose`, `flow-only` and `command-for-all`;
  - the default is `owner-command-agents-propose`, from "a session or a scripting tool that allows
    instruction addition/editing/deletion to its respective manifest";
  - presets never touch it, because who may edit instructions is a guard-like choice.

A third key, `instructions.proof`, joined at the fold (R-I). Its default is `tty-cli`, with `signed`
and `both` allowed, and presets never touch it.

**The register** gains `gap-found-09` to `gap-found-17`:
- dOrderedCharter owns 09, 10, 11, 14, 15 and 17;
- dConvergedCharter owns 12 and 13;
- dCalibratedLens owns 16.

`gap-found-09` to `gap-found-16` are `[uncovered]`'s gaps 1 to 8, in order. `gap-found-17`, the
missing layer model, comes from `[layers]`.

**The chain rows gain the units that carry them:**
- dDeclaredLoop names every checklist item by a semantic tag;
- dBoundRoles declares expansion-filled work-order fields as optional slots.

**v2 `[owed]`:** Runtime's build was owed to the re-cut. The runtime layer settled it as
dWellOiledMachine (RT-3), now in v2's chain.

## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded

Two Tier-2 rounds reviewed this record at blob `3cfd547a`. The comparison record places their findings
on 54 defects (`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`,
`[map-instruction]`), and its map's `disposition` cells point here. Each defect's fix sits in place,
in the sections named:
- **amend:** this record, or a sibling record, now states the fix;
- **gap:** the owning chain build carries it in the register;
- **owed:** v2's `[owed]` carries it to the chain re-cut;
- **fork:** the owner answered it, in the comparison record's `[answers]`;
- **none:** every finding on it was refuted.

| Defect | Disposition | Where the fix sits |
|---|---|---|
| `tag-spelling` | amend | R-B: a tag's full spelling is `<namespace>.<name>` |
| `example-item-names` | amend | R-B: the flow's settled `plan.input` and `build.unit-pass` |
| `kit-layer-map-stale` | amend | `[layers]`: the Runtime list, the Knowledge list and the kit table |
| `runtime-deferral-stale` | amend | `[layers]`' three reasons; `[settled]`'s v2 `[owed]` line |
| `stale-figures` | amend | `[fit]` points at v2's catalogue and principles instead of counting them; R-E says "a whole guide" |
| `skills-layer-split` | amend | R-F: each expansion entry in its own layer, deploy-governance retired, unattended a client of `run <build>` |
| `harness-injected-loads` | amend | R-C's injected class; R-H; `gap-found-14` gains the measure |
| `act-session-load-point` | amend, gap | `[current]`'s act-session row; R-C; R-G's levels 5 and 6; `gap-rt-12` |
| `codex-override` | amend, gap | R-K's Codex row; v2's dOrderedCharter row; `gap-rt-11` |
| `harness-load-point-owner` | amend | R-K: Runtime's harness adapters say which files carry each load set; `[layers]`' Distribution and the kit table follow |
| `agent-instructions-seam` | amend | R-K names the agent-instructions kit and `CODEX_MAX` |
| `join-population` | amend | R-B: each join asserts a non-empty population, armed by the build that creates it |
| `charter-before-policy` | owed | v2 `[owed]`: the re-cut moves the policy file, its schema and reader into dOrderedCharter, or orders the consuming units after dDeclaredLoop |
| `write-path-bypass` | amend | R-I: validation as a gate leg and at render, reconciliation across nodes, one commit per change |
| `knowledge-in-core-render` | amend | `[layers]`: the one-way rule covers every core render |
| `effectiveness-citations` | amend | R-J: loaded and broken are witnessed, and followed is not measured |
| `effectiveness-seam` | none | refuted; R-J names `prose.py` anyway |
| `heading-grammar` | amend | R-D: headings are directives (P11) |
| `gap-count-mismatch` | amend | `[uncovered]` and `[settled]` map gaps 1 to 8 onto `gap-found-09` to `gap-found-16`, and 17 onto `[layers]` |
| `skill-description-count` | amend | `[current]`'s session-start row; `[uncovered]` 5 |
| `hook-injected-loads` | amend, gap | `[current]`'s hook rows; R-C; `gap-rt-13` |
| `lexicon-dependency` | amend | R-B: a core shape check, the lexicon's vocabulary at an extension point; v2's dOrderedCharter row |
| `trigger-read-bytes` | amend | `[current]`'s trigger-read and Skill rows |
| `crlf-byte-counts` | amend | `[current]`'s note; R-C budgets the committed blob |
| `existing-budgets` | amend | `[current]`'s budget table; `[fit]`; `[uncovered]` 2; R-C extends `template-size-limits.txt`; `gap-found-10` corrected |
| `retired-summed-budget` | amend | R-C: a budget per load point; the summed budget stays retired |
| `tag-registry-seams` | amend | R-B names `DOD_CORE` and `DIRECTIVES_CORE` |
| `roles-tag-join` | amend | `[current]`, `[fit]`, `[uncovered]` 1, `[charter-today]` and R-B; `gap-found-09` corrected |
| `section-number-readers` | amend | R-B: retiring a number re-points its readers in the same unit |
| `one-source-roles-list` | amend | `[charter-today]`: keep the one source the roles kit already has |
| `grammar-check-seams` | amend | `[fit]`; R-D extends the instruction gates that exist |
| `ladder-renumber-carriers` | amend | R-G; foundations R2 under a dated `Revised:` line; `[fit]`'s level 3; v2's revision note of 2026-10-16 |
| `card-rank-or5` | none | refuted |
| `provenance-marker-readers` | none | refuted |
| `microformats-fence` | none | refuted |
| `governing-document-rename` | amend | foundations C3 and v2's dOrderedCharter row say "instruction unit" |
| `gap-found-17-stale` | amend | `gap-found-17` drops its runtime clause, which dWellOiledMachine closed |
| `owner-proof` | amend | R-I: `instructions.proof`; v2's catalogue and the presets' exclusions |
| `load-set-contents` | amend | R-A's `required-by`; R-C: the task and handed facts, the budget's unit, the refusal's route, the softened modes |
| `grammar-red-case` | amend | R-D: the red cases are today's charter defects |
| `grammar-template-type` | none | refuted |
| `reuse-entries-units` | amend | R-D: a MUST with its trigger; R-G: level 3; R-I: manifest parts beside each feature |
| `command-items-units` | amend | R-B: command and hook items are exempt from the item join |
| `scope-selection` | amend | R-B: selectors and descriptors, and `reader.every` |
| `principle-check-switchable` | fork, amend | LR-1; `[settled]`; foundations C6 |
| `layer-conformance-gate` | amend | `[layers]`; foundations C3 gains "layer"; v2's dOrderedCharter row |
| `policy-level` | amend | R-A: a unit keeps its own level inside another's envelope |
| `help-move-owner` | amend | R-E; v2's dConvergedCharter row |
| `node-registry-card` | amend | `[charter-today]`: the registry leaves only with the `registry:` key re-pointed |
| `worktrees-placeholder` | amend | `[uncovered]` 3 and `[charter-today]`: a placeholder, and the `PROBES` seam |
| `instruction-paths` | amend | R-I: the manifest registry lists the instruction files |
| `tag-lifecycle` | amend | R-I: reference checks, and the retired state |
| `handed-content-grammar` | amend | R-D: handed content is data, fenced |
| `instruction-command-seams` | none | refuted; R-I names the seams anyway |

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
- the forks put to the owner.

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
  - knowledge;
  - observability;
  - integrations;
  - distribution, once gov is installed.

**Runtime is the missing core layer.** It is what executes the cycle:
- the executor and its checklist engine;
- the always-spawn harness;
- the hooks that enforce at the tool boundary;
- the `next` CLI;
- isolation;
- process supervision.

Three reasons:
- P24 makes the checklist a program, and a program needs a runner.
- Every item still homeless in v2's `[owed]` is runtime: the executor, its harness, the turnstile and
  the lander.
- The instruction layer's MUST and NEVER become real only where Runtime enforces them.

In one line: Instruction says, Runtime enforces, Flow witnesses, Memory proves.

**The proposed expansions:**
- **Knowledge**, consulted to decide better:
  - the codebase map and the reuse lookup;
  - decisions, through memory-recall;
  - bug classes, the gotchas;
  - the lexicon;
  - research records.

  It absorbs most of the owner's memory bookkeeping.
- **Observability**, signals about the loop and the runtime, read by Maintain and the Loop Review:
  - run logs, through runlog;
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
- **Distribution**, the product's delivery: govkit, the adopt scripts, overlays, the render targets per
  harness, and version currency.

**The rules that keep it extendable:**
- **Dependencies point one way.** Core never depends on an expansion. An expansion attaches only at an
  extension point a core layer declares, so a core-only adopter runs. Today's design breaks this twice:
  - the builder's work order carries bug classes, from Knowledge;
  - the reuse scout's work order carries the map's dossiers, from Knowledge.

  Each such field becomes an optional slot that its expansion fills.
- **Every layer fills one contract**, core or expansion. The contract holds:
  - its tag and its definition;
  - its instruction units;
  - its engine kits;
  - its record kinds;
  - the extension points it declares, and those it uses;
  - its policies and its gates.

  A new expansion is a filled contract, which makes "extendable" a mechanism rather than a hope.
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
| agent-instructions | Instruction: the render targets per harness | core |
| roles | Roles: definitions and handoffs | core engine |
| workflows | Roles and Runtime: the review and unit harnesses | core; the always-spawn harness grows here |
| memory-tree | Memory: build folders, records, the index, hygiene | core engine; its backlog, rotation and gotchas settle at the memory review |
| the loop kit, to be built | Flow: stage tags, checklists, `next` | core engine |
| run-gates | Flow: the Test verdict | core engine; its legs come as packs |
| gate-lint, pytest-parallel-guardrails | Flow: verdict leg packs | expansion |
| `push-main.sh`, the turnstile, the lander | Flow: Deploy, executed by Runtime | core |
| session-kickoff | Flow: Entry, through the orientation scout | core |
| unattended | Runtime: the executor | core |
| hooks | Runtime: enforcement at the tool boundary | core |
| process-monitor | Runtime: supervision; its reports feed Observability | core |
| branch-reconcile and the cleanup Skill | Runtime: isolation housekeeping | expansion |
| codebase-map, lexicon, memory-recall | Knowledge | expansion |
| runlog, drift-audit | Observability | expansion |
| govkit and the adopt scripts | Distribution | expansion |
| lib | shared primitives inside kits | no layer |

## [current] What the layer loads today, measured 2026-10-15 (`wc -c`)

| Load point | When | What, in bytes |
|---|---|---|
| Session start, main session | every session | `CLAUDE.md` 12, importing `AGENTS.md` 16,732; the auto-memory index `MEMORY.md` 13,187, injected by the harness under its instruction framing; the hook's card; the harness's lists of nine Skill and nine agent descriptions |
| Role spawn | each subagent | its agent definition (nine files, 45,213 together) and the handoff's task part; no `CLAUDE.md` (`omitClaudeMd: true`) |
| Trigger reads | when a charter pointer's trigger holds | ten guides, `HYGIENE.md`, `TEMPLATE-SPEC.md` and one path rule, 409,376 together, each read whole; the four unattended guides alone are 216,448 |
| Skill invocation | on `/<skill>` | nine `SKILL.md` files of 3,611 to 18,310 each; session-kickoff also carries 258,177 of engine files |

The charter's state:
- it has 46 tagged rule lines and three numbered sections;
- it renders from a 13,695-byte template;
- its tags key the renderer and nothing else.

Foundations `[step-1]` measured about 25 load-bearing documents, about 551 KB, arriving by six routes.

## [fit] The owner's layer against the current design

| The owner's element | The current design | Status |
|---|---|---|
| Charter | dOrderedCharter re-founds it: the top envelope, the front door, the drive section rendered from kit descriptors, the 32 KiB cap (foundations `[step-1]`) | designed |
| Policies, principles | one policy file, 94 keys, 4 presets; P1 to P26 fixed, with a registry and a meta-check (P10, P16) | designed |
| Protocols, templates, guides | registered at rank 3 and enveloped (foundations R2); facts, not prose (P11); specs structured (P12) | partly: still hand-written whole documents, none rendered from the structured sources, each read whole |
| Importance levels 0 to 7 | ladder: 0 the platform, 1 the charter with the card beside it, 2 to 7 below | designed, numbered one off from the owner's model |
| A tag system mapping instructions to processes and roles | the section-tag grammar and its resolver (dOrderedCharter); stage tags (dDeclaredLoop); practice tags | partly: tags name sections; nothing joins an instruction to a step, item, role or policy; checklist items are numbered |
| Skills | rank 4; "a Skill is a Claude Code shortcut over the same command" (foundations R5); a kind with a factory (P16) | partly: the shape is decided, but today's Skills carry their own procedures |
| HOW: no ambiguous prose | P11, facts only; tags, never `§` | stated, unenforced: no statement grammar, no check |
| HOW MUCH: precise loads | the charter's 32 KiB cap; one line per role (foundations R6); `orient.budget` record-only; gap-orient-07 | partly: one load point is capped; none is measured; no load set is computed per role and item |
| Mechanical rendering and enforcement | envelopes generated from the registry, and a gate over them | partly: documents, not units |
| A preset catalogue | the practice catalogue with `charter.practices`; policy presets | partly: practices only |
| An owner write path | the policy CLI needing an interactive terminal; a `new` verb per kind | missing for instructions |

## [uncovered] What the layer does not yet cover

Proposed gaps, each with its proposed owner build:

1. **Instructions map to nothing below them.** HIGH, dOrderedCharter.
   - Tags name sections only: the charter's 46 rule tags key the renderer and nothing else.
   - Checklist items are numbered.
   - No registry joins an instruction to the step, item, role or policy it serves, so no loader can
     select an agent's instructions by its role and item.
2. **Load is unmeasured and unbudgeted.** HIGH, dOrderedCharter.
   - No load point declares a budget or is measured; the 32 KiB cap binds the charter alone.
   - Session start loads about 30 KB of repository and user text before the card.
   - A trigger read pulls whole documents, up to 216 KB for the unattended four.
   - No harness's load points are inventoried.
3. **Loaded text is unshaped.** MED, dOrderedCharter. Nothing checks that a loaded line gives
   direction. Today's charter shows the result:
   - headings name provenance or a label ("3. Generated", "agent charter");
   - it points at text it never loads ("the marker below");
   - render provenance loads every session;
   - stale typed facts load at the top level: "Worktrees: none yet" beside 13 worktrees, and a model
     name in the trailer.
4. **Protocols and templates are hand-written monoliths.** HIGH, dConvergedCharter.
   - 409 KB of guides and templates restate the flow's steps in prose, so one rule lives in a guide,
     a Skill and a checklist at once.
   - Nothing renders a protocol view from the loop's, the roles' and the policies' structured
     definitions.
5. **Skills are parallel procedures.** MED, dConvergedCharter.
   - build, unattended and session-kickoff carry their own procedures, rather than shortcutting a CLI
     command into the flow.
   - Every Skill's description loads each session without a trigger contract.
6. **Memory instructs outside the ladder.** HIGH, dOrderedCharter; the memory layer review may move it.
   - The auto-memory index loads every session under the harness's instruction framing, and its
     feedback entries carry directives.
   - Nothing promotes a standing directive into the instruction layer, or holds memory at evidence.
7. **No write path for instructions.** MED, dOrderedCharter.
   - The owner can change an instruction only by editing a source or the template by hand.
   - There is no manifest, no validating command and no recorded change.
   - There is no instruction preset beyond the practice catalogue.
8. **No instruction's effect is measured.** LOW, dCalibratedLens. Nothing records which units an agent
   loaded, followed or broke, so text that bears no load is never found, though P11 says to remove it.

## [charter-today] The charter's dos and don'ts

**The owner's, recorded:**
- the title is not a directive;
- render provenance loads every session;
- sections are numbered;
- "Agent roles — hand the work to its role" and "Protocols — read the one whose trigger holds" are
  the model headings;
- the tags map to nothing.

**Added from the same file:**
- **Don't point at text that isn't loaded.** "Whose version is the marker below" names a marker the
  agent never sees.
- **Don't type facts that go stale.**
  - "Worktrees: none yet" stands beside 13 worktrees.
  - The trailer's model name meets a harness reminder naming another model every session.
  - Derive the fact at render time, or point to where it is derived.
- **Don't load what the reader never acts on.**
  - The node registry loads every session, though the card already names the session's node.
  - The driver reads `[migrations]`, `[bytes]` and `[spec]` though it does no role work. Their reach
    belongs in the work orders of the roles they bind.
- **Don't name sections by provenance** ("This repository", "Generated"). Name them by what the reader
  does.
- **Don't state one thing twice.** The roles are described in the charter and again in the harness's
  agent list. One source should render both, with the agent description carrying the trigger.
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
  - its source, whether written text or rendered from a structured definition;
  - its owning kit.
- The charter, a protocol view, a role's static instructions and a work order are each assembled from
  units by their tags. Each is wrapped in the envelopes foundations R2 already designs.
- The kind "governing document" becomes "instruction unit", made by the same `new` factory.

**R-B. One tag system, namespaced, registered and joined both ways.**
- The namespaces are `level`, `layer`, `step`, `item`, `role`, `policy`, `practice`, `principle`,
  `kind`, `record` and `kit`.
- Level says what wins; scope tags say who loads it.
- The joins, checked both ways:
  - every unit carries at least one scope tag;
  - every step, item and role has at least one unit;
  - every tag used is registered;
  - the lexicon checks tag names.
- Checklist items get semantic tags, such as `plan.intake` or `build.unit-commit`; numbers are display
  order only.
- dOrderedCharter builds the mechanism, and each chain build registers its own tags, as with the
  principle registry.

**R-C. Load sets are derived, budgeted and measured.**
- A load set contains:
  - the top level's units;
  - the units scoped to the reader's role, the driver's scope included;
  - the units scoped to its item;
  - the active practices' reach for the step;
  - the policy values the item reads.
- Each load point declares a budget.
- The render refuses a set over budget, which is too much.
- It refuses a set missing a unit its role or item requires, which is too little.
- Field loads are measured from the roles' runs.

**R-D. A closed statement grammar.** Every loaded unit is one of six types:
1. a directive: MUST, NEVER or ALWAYS, with its scope and its condition;
2. a constraint, with its value;
3. a definition;
4. a pointer: a trigger leading to a tag or a command;
5. a policy value, rendered from the policy file;
6. a fact, derived, with its source.

Around the grammar:
- Headings are directives or scope statements.
- Render provenance lives in a sidecar lock, never in loaded text.
- A check enforces the grammar and is seen red on planted prose.
- Reuse aHonedRuleset's prose census and `memory/guides/ANNOTATION-STYLE.md`.

**R-E. Protocols and templates are rendered views.**
- The sources are the loop's checklists, the roles' definitions, the record schemas and the policy
  catalogue.
- The guides and templates become views sliced by tag, so an agent reads its slice and never a 67 KB
  whole.
- Explanation for humans lives outside every load set, under `help/`.

**R-F. Skills belong to the layer, at level 4, as thin entries.**
- A Skill is its trigger contract, the CLI command it shortcuts, and the tags of what it enters. It
  has no procedure of its own (P1).
- **Core entries**, each entering the flow:
  - session-kickoff: Entry, through the orientation scout;
  - build: the Build step, attended;
  - unattended: the executor;
  - deploy-governance: adoption.
- **Expansion entries**:
  - memory-recall, runlog, drift-audit and cleanup: memory bookkeeping and Maintain;
  - lexicon: naming, at Design and Build.
- Each Skill declares its layer. Its description is budgeted and phrased "Use when …; runs …".

**R-G. Renumber the ladder to the owner's model.** The platform sits above the ladder, unranked by the
repository. The levels:

| Level | What sits there |
|---|---|
| 0 | the charter |
| 1 | the build's card, so the charter outranks it by level alone and the special rule retires; this matches OR-5's "priority 1 along the charter" |
| 2 | the loop and the policy values |
| 3 | methods, protocols and templates, as rendered views |
| 4 | runbooks, Skills and path rules |
| 5 | the role's static instructions |
| 6 | the task |
| 7 | records and memory, evidence only |

Rendered text uses one term throughout: "level".

**R-H. Memory instructs nothing.**
- A standing directive found in memory is promoted into the instruction layer as a unit, through the
  write path. The memory keeps a pointer.
- The memory index is a load point with a budget.
- The mechanism is settled with the memory layer.

**R-I. An instruction manifest and a guarded write path.**
- There is one manifest per kit. Manifests merge deterministically with the adopter's overlay, under
  a lock.
- One command adds, edits, removes, lists, renders and checks units. At the write boundary it
  validates:
  - the schema;
  - the tags;
  - the grammar;
  - the budgets;
  - conflicts at the same level.
- The command records every change and re-renders every affected load set.
- The owner uses it directly; top-level principles still need an owner-ratified amendment (K2).
- An agent only proposes a change, through the flow (P20).
- A rendered unit changes at its structured source.
- Instruction packs extend `charter.practices` into a preset catalogue: methodologies, governance
  sets and language packs.

**R-J. Instruction effectiveness feeds the Loop Review.**
- Returns and findings cite the unit tags they followed or broke.
- The Loop Review prunes units that bear no load, and tightens the ones broken often (P9, extended to
  instructions).

**R-K. Load points per harness.** The manifest renders one target per harness, each with its load
points and budgets. This extends foundations R5 and R6 and gap-orient-13.

| Harness | Load points rendered |
|---|---|
| Claude Code | `CLAUDE.md`, agents, Skills, hooks, rules |
| Codex | `AGENTS.md` within 32 KiB, plus the card's override file |
| The rest | `AGENTS.md` |

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

**Principles.**
- P11 now carries the owner's first instruction principle: everything loaded gives direction, through
  six statement types.
- P13 now carries the levels and the scope tags as the join keys.
- P27, load is precise, is the owner's second instruction principle.
- P28 says layers are capabilities and the core never depends on an expansion.
- All four are owner-ratified in this round: the owner's own principles, and the layer framing they
  chose. Each will need its enforcing check in the principle registry (P16):
  - P27's is the load-set render check;
  - P28's is the one-way dependency check and the layer contract's conformance gate.

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

**The register** gains `gap-found-09` to `gap-found-17`:
- dOrderedCharter owns 09, 10, 11, 14, 15 and 17;
- dConvergedCharter owns 12 and 13;
- dCalibratedLens owns 16.

**The chain rows gain the units that carry them:**
- dDeclaredLoop names every checklist item by a semantic tag;
- dBoundRoles declares expansion-filled work-order fields as optional slots.

**v2 `[owed]`:** Runtime gets its own chain build at the re-cut, once its layer review settles what that
build holds.

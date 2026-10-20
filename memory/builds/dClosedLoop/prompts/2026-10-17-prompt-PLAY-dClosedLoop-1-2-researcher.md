**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-2-researcher.md role-sha=51b61c49e522 task-sha=0310c1380d2d -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.
The owner reviews the design layer by layer. All eight layers, the five core and the three expansions,
are designed, reviewed and folded. Six systems that cut across every layer were then researched,
designed, audited and folded: tags, code annotations, instruction writing, role workflow shapes, memory
structure, and retrofitting gov's practices into an existing repository. The owner now asks, in these
words:

> Now that even this plan has grown to a substantial size, how do you stay oriented in the entirety of
> it at high level (to make sure no piece of it is lost at a glance)? As in, when a session is opened,
> as a question is asked, do you have an overview of the ENTIRE design, then dig deeper into specific
> parts of it? Previously, codebase map tool was supposed to do exactly that - allow an agent to load
> the entire project at a high level, so no piece of it is left out. After, an agent would dig deeper
> into the parts it needs and still be able to find all relations at any point. Is this even needed?
> Feels like an essential piece to memory layer.

The owner then settled PM-1 and PM-2, handed below, and asked for this system to be researched twice,
then designed. Yours is **the level-0 project map**. Design it to fit the architecture handed below,
across all eight layers and the six systems. Measure what today's product does, say what the current
design already settles and what it lacks, and say what makes your pick efficient, in numbers a check
could hold it to.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **The layers** (architecture v2 `[layers]`). A layer is a capability named by a tag, and a kit
  implements layers and declares which. The core alone carries one build from request to landing,
  and an expansion is never needed for that.

  | Layer | Kind | What it is |
  |---|---|---|
  | `instruction` | core | everything an agent is told, levelled 0 to 7 and tagged by scope |
  | `flow` | core | a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as breakpoints, with the verdict engine and the lander |
  | `roles` | core | the bound workers, and the driver |
  | `memory` | core | the trail, what happened in a build: records, transitions, witnesses, the card's truth; and the library, what generalizes beyond one: major decisions, reuse entries, bug classes, research. Its optional components, the map, recall and the lexicon, are what agents consult to decide |
  | `runtime` | core | what executes the cycle: the supervisor and its checklist engine, act sessions and the spawn harness, the `next` verb and the owner's controls, the hooks, isolation, process supervision |
  | `observability` | expansion | signals about the loop and the runtime, and the cadence steps that act on them: Maintain and the Loop Review |
  | `integrations` | expansion | adapters to outside services: remote CI, notifications, cloud hosts, trackers, and deploy engines that promote a landed tree through environments |
  | `distribution` | expansion | the product's delivery: govkit, the adopt scripts, overlays, the install of the render targets Runtime's harness adapters define, currency |

- **P28.** The core never depends on an expansion. An expansion attaches only at an extension point a
  core layer declares. Every layer, core or expansion, fills one layer contract:
  - its tag and definition;
  - its instruction units;
  - its engine kits;
  - its record kinds;
  - the extension points it declares, and those it uses;
  - its policies and its gates.
- **The optional slot.** A work-order field, or any part of a core render, that an expansion fills is
  an optional slot. It renders filled, searched with nothing found, or not installed with the core's
  fallback named, never empty. `policy.on-missing-expansion` (`refuse` or `fallback-reported`, default
  `refuse`) governs a preset value whose expansion is absent.
- **Items, witnesses, policies and records.**
  - Every action that changes state belongs to an item, tagged `<step>.<name>`. An item has one actor
    (a command, a role, a hook, the owner or the executor), what it needs, what it does, its witness
    and its routes (P24).
  - A witness is computed from committed history, a hook-written record or a verifier's verdict, never
    from state an agent typed (P2).
  - Every behaviour is a policy key. Its default is the owner's answer, and its allowed values are the
    options offered (P10). Structural choices are decisions, not keys.
  - Every record kind is declared once in the memory contract (tag, layer, home, id rule, schema,
    writer, readers, lifecycle, check), and written through one door, the `record` command (P30).
- **Runtime's extension points** (layer-runtime `[extend]`). Runtime declares nine and uses none.
  Integrations fill the host and notification adapters. Observability and memory's optional
  components register packs and read the journal. A key that selects an extension takes registered
  names, validated against the registry.

  | Extension point | What registers there | Examples |
  |---|---|---|
  | actor kinds | a kind of actor an item can name | role, command, hook, executor, owner |
  | command adapters | a command, with its witness contract and its idempotence or reconcile probe | the bar, the lander, `record`, the instruction command |
  | spawn backends | a way to start a role agent | in-session Workflow, headless per agent, another harness's spawner |
  | role harnesses | a Workflow script, with its declared spawn sites and fan | the role cycle, the Tier-2 review |
  | hook packs | a fragment, with its owner, class, failure mode, budget and key | the spawn guard, act binding, the lexicon's commit check |
  | harness adapters | how a harness loads instructions, spawns, hooks and compacts, with its capability table | Claude Code, Codex |
  | host adapters | where the supervisor and its sessions run | the node tick, a cloud host |
  | notification adapters | how an owner request reaches the owner | the terminal, a push notification |
  | journal readers | what reads the journal | runlog, observability's store |

- **The chain.** Every gap in the register is owned by exactly one chain build, and the expansions'
  work lands in those builds.
- **P11.** Everything loaded gives direction. Every loaded unit is one of six statement types: a
  directive, a constraint, a definition, a pointer, a policy value or a derived fact. Prose that bears
  no load does not exist, and headings are directives. Render provenance never loads, and neither does
  a typed fact that can go stale. Sections, checklist items and layers are named by tags that survive
  reordering, never by numbers or `§` references.
- **P12.** Specs are structured contracts: definitions, design, boundaries, interfaces and acceptance as
  fields a check reads.
- **The charter's rules** bind this design too: derive over author, one fact in one place, gate the
  class, a gate never seen red is not a gate, and spend tokens on new judgment.
- **Where the records are.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`: `architecture-v2` (v2) and the layer records
  `layer-instruction`, `layer-flow`, `flow-steps`, `flow-roles`, `layer-roles`, `layer-memory`,
  `layer-library`, `layer-runtime` and `layer-expansions`. A record cites its sections as `[tag]`.
  Records written before 2026-10-16 that say Knowledge mean memory's library side.

**Your part: the level-0 project map, seeing the whole project at once.** Every agent today starts from
the charter and one build's card, and reaches everything else by query or grep. A query finds only what
its asker names. In the systems and retrofit audit, 37 of 52 items needed a piece their author did not
have in view (`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md` `[sort]`). The system is a
derived map of every part of the project, one line per node, that the roles which change structure hold
whole, then dig from by tag, and from which they find every relation.

Settled, which the design must serve:
- **PM-1, the owner's answer: "Structural roles (Recommended)".** The orientation scout composes the
  card from the map. Planners, architects, spec writers, and the coherence and reuse review lenses get it
  in their work orders. Builders, testers and other unit workers keep their slice, plus `refs` for
  relations. "Every agent" and "the owner only" stay allowed values. This amends layer-memory `[views]`,
  which said agents never read a view.
- **PM-2, the owner's answer: "Core memory (Recommended)".** The core derives the map from the one index
  over every registered namespace, so it exists without any optional kit. The codebase map adds code
  depth, its symbols, callers and dossiers, where it is installed.
- **The one index and its verbs** (the systems record `[cross]`, `[design-tags]` and
  `[design-memory-structure]`): one derived JSON index per tree, `gov tag show`, `where` and `refs`,
  `record find` and `record show`. Drill-down and relations are designed already; the map is what an
  agent holds before it knows what to ask.
- **Load and budgets:** P27, each load point loads exactly its reader's units; the card is at most 8 KB
  (`memory.load-budget`); memory slices are priced by `memory.item-budget` (`measured`, MS-2).
- **The size probe** in the project-map record `[probe]`: all of gov at one line per node is 176 nodes
  in 10.4 KB, from today's sources, without record kinds, decisions or this build's records.

**Read:** the project-map record, all of it; layer-memory `[words]`, `[views]`, `[map]`, `[reuse]` and
`[relations]`; the systems record `[cross]`, `[design-tags]` and `[design-memory-structure]`; the
orientation record (`build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md`) `[design]`; layer-roles
on the work order and `[matrix]`; and v2 `[principles]` P27 and `[chain]`. Outside the build, read
`tools/codebase-map/` (what renders `memory/map/generated/MAP.md` and `CARDS.md`),
`tools/memory-tree/gen_build_index.py` (what renders `memory/LIVE.md` and each README's regions), and
the atlas generator `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`,
which already derives a whole-design view for the owner.

**Measure in the tree and in the transcripts:**
- every class of node the map must hold for nothing to be lost: layers, principles, chain and live and
  closed builds, features, kits, gate legs, hooks, commands, record kinds, major decisions, policy
  namespaces, gap areas, bug classes, and any class you find. For each, its count, its bytes at one line
  per node, and where a one-line purpose is declared for it today, or that none is;
- what the roles PM-1 names read today to orient, from the subagent transcripts under
  `~/.claude/projects/C--projects-coding-governance*/`: bytes, reads and distinct files before their
  first act, and how often an agent searches for whether something exists;
- whether the record's sort holds: sort the items of two other Tier-2 reports under
  `memory/builds/dClosedLoop/reviews/` by the same question, as a second rater, and report the share
  "not in view" with your agreement on the project-map record's 52;
- how the map grows: its bytes now, and its rate from gov's history of builds, features and kits, and
  the point where one line per node outgrows a budget;
- what a derivation costs: time and bytes for the generators that exist (`gen_map.py`,
  `gen_build_index.py`, the atlas generator), as the estimate for deriving the map per tree.

**Answer:**
- what one line holds, its tag, a declared purpose, its owner, counts and relation keys, and what the
  map never holds;
- its tiers and its budget: flat or hierarchical, the key that bounds it, and what happens as the
  project grows;
- how each PM-1 role receives it (the card, a work-order slot) and how a unit worker reaches relations;
- drill-down from a node to its subtree and content, and relations both ways;
- "no piece lost" as a check: every registered node is on the map, and every line resolves, both ways;
- where each node's purpose line is declared, per namespace, and which namespaces lack one today;
- one derivation and two renders: the map for agents, and the atlas for the owner;
- its losing test, with the method: the share of review items "not in view", with the map handed and
  without.

**Efficient, for this part,** also means three things. The map costs a structural spawn the fewest bytes
that still name every node. An agent spends fewer lookups finding out whether something exists. And the
share of review findings "not in view" falls.

**What efficient means here.** Less for an agent to read, find or decide per item: bytes and tokens on
the read path, lookups per orientation, agents and tokens per verified result, and checks that cost
little to run. Measure it for today's product, and estimate it for each candidate with the method shown.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar.
- From `memory/builds/dClosedLoop/`, read only the records and sections your part names. Measure the
  rest in the tree itself: `tools/`, `skills/`, `.claude/`, `.github/`, and `memory/` outside that
  build.
- A record is evidence. Verify against the code any claim your pick depends on, and say where a record
  and the code disagree.
- Cite file:line for every claim about code or records. Show each measuring command with its output.
- Return at most 3,000 words, in the eight sections below. Prefer tables.

**Return these eight sections:**
1. **Verdict:** the system, in at most 120 words.
2. **Today:** each part of today's product, and of the current design records, that serves this system:
   what it does, its measured use and size, and file:line.
3. **Across the layers:** for each of the eight layers, what the system needs from it and what it gives
   it; then what it needs from, and gives to, each of the six systems the rounds designed.
4. **Candidates:** two to four designs that differ in mechanism. For each, give the mechanism, its
   efficiency measured or estimated with the method, the smallest test that would make it lose, and that
   test's result with its command and output.
5. **The pick, specified:** its grammar, schema or shape; the layer and the chain build that own it; its
   records and kits; its checks, each with the case that turns it red; and its read-path cost.
6. **Items and policies:** the items it adds or fills (tag, actor, does, witness, routes), and its policy
   keys (key, allowed values, default, why).
7. **Gaps:** the register's gaps your pick closes, by id, and any new gap it exposes, with its evidence.
8. **Forks:** the decisions only the owner can make, each with its options and your recommendation.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

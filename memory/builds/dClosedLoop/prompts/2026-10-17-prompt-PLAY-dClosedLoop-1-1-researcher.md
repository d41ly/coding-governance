**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-1-researcher.md role-sha=51b61c49e522 task-sha=1ce64a7d2601 -->

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
are designed, reviewed and folded. Five systems that cut across every layer were then researched and
designed: tags, code annotations, instruction writing, role workflow shapes and memory structure. The
owner is settling their forks. The owner now opens a sixth system, in these words:

> Continue with your current work queue but budget research+design for another system: retrofitting the
> gov practices. What layer (extension?) does it go to? When gov is adopted into a fresh repo, maintaining
> its methods (to be designed) like tagging, code annotations, decision log and its major decisions, etc.,
> is not an issue - they all happen along as code is planned, designed, and built. However, Gov may be
> adopted into a product/repo that has an extensive codebase already and has been following different
> practices. How would gov retrofit its practices into an existing repo as it goves over its code to
> ensure efficient practices?

Yours is **retrofitting gov's practices into an existing repository**. Design it to fit the architecture
handed below, across all eight layers and the five systems. Measure what today's product does, say what
the current design already settles and what it lacks, and say what makes your pick efficient, in numbers
a check could hold it to.

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

**Your part: retrofitting gov's practices into an existing repository.** In a fresh repository gov's
records grow as the code is planned, designed and built: tags, code annotations, the codebase map and
reuse entries, the decision log and its major decisions, bug classes, specs and instruction units. In a
repository with an extensive codebase and practices of its own, none of that history exists, and gov's
gates, orientation and read path meet code that no record describes. The system is how gov brings such a
repository under its practices as it goes over the code.

Settled, which the design must serve:
- **The five systems** (the systems record `[design]` and `[answers]`): one tag grammar with a derived
  index; `gov:note` and `gov:feature` annotations, found by the marker query and by the codebase map's
  index (AN-1), with a read hook that fires on shell reads too (AN-2); instruction units rendered from
  templates, with a render gate armed at dOrderedCharter over a shrink-only list of today's hand-written
  documents (IW-1); role shapes declared as data; and keyed memory sections, with derived anchors for
  legacy headings.
- **P28 and the optional slot** (handed above). The core alone carries a build from request to landing.
  So whatever the core needs to carry a build in an existing repository cannot live in an expansion.
- **Seams that already tolerate legacy.** These include the codebase map's `memory/map/baseline.toml`,
  which holds the keys no dossier claims yet and shrinks unless a recorded decision says otherwise. They
  also include IW-1's shrink-only list and `memory.legacy-anchors`. Find the others.
- **Distribution** (`layer-expansions` `[design-distribution]`) delivers gov into a repository: govkit,
  the adopt scripts, overlays and currency. **Observability** (`[design-observability]`) holds the
  cadence steps, Maintain and the Loop Review.

**Read:** the systems record, `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`, its `[design]` and
`[answers]`; `layer-expansions` `[core-points]`, `[design-observability]`, `[design-distribution]` and
`[revised]`; `layer-memory` `[decisions]`, `[reuse]`, `[map]` and `[annotations]`; `layer-library`
`[design]` and `[consult]`; and `flow-steps` `[build]` and `[expansions]`. Outside the build, read
`memory/builds/aDeployScout/spec/governance-deployer-research.md` and `WIRE-INTO-PROJECT.md` on adoption
today: their retrofit installs gov's kits into a repository, and does not bring its code under gov's
practices. Open no other repository, since the build does no adopter-repo work: gov's own tree and
history are the evidence.

**Measure in the tree:**
- gov's own history as a retrofit case. Each kit that arrived over an existing tree baselined the debt
  it found. Start with `memory/map/baseline.toml`: its keys when it landed and now, from git history,
  how fast it shrank, and what shrank it. Then take the lexicon's marginal offenses, which drift-audit
  reports, and the documents IW-1 lists;
- how far touching reaches: the share of the tree's code files changed in the last 30, 90 and 365 days,
  and the share unchanged since it landed. From transcripts, the share of agents' reads that land on
  recently changed code;
- what an existing repository already holds that gov could derive from rather than author: commit
  messages, comments and docstrings, documents shaped like decision records, tests, CODEOWNERS and lint
  configuration. Measure what gov's own tree yields from each, and say which of them a check could
  trust;
- what each of gov's gates and checks does on code no record describes: which red, which pass by
  finding nothing, and which already read a baseline.

**Answer:**
- the placement the owner asks for: a layer, an expansion's capability, or a system across the layers
  like the five. Say which parts the core must hold under P28 and which an expansion may add, with the
  evidence for each placement you weigh;
- the modes by which retrofit reaches the code: at adoption, as each unit touches code, on a cadence,
  and at the owner's ask. Say what each covers, what it costs, and which practices it serves;
- for each practice (tags, code annotations, the codebase map and reuse entries, the decision log and
  its major decisions, bug classes, specs, instruction units and records): what can be derived from the
  existing code and history, what needs an agent's judgment, and what needs the owner. Say how a
  reconstructed record is marked apart from one written as the work happened;
- how the repository's own practices are treated: imported, translated, kept alongside or retired, and
  who decides;
- the baseline and the ratchet: what is recorded at adoption, what a gate refuses on new code while
  tolerating baselined legacy, what shrinks, and how progress is measured and reported;
- how retrofit stays out of the owner's way: its share of each unit's cost, with a bound a check holds,
  and what it never does, without the owner's ask, to code no unit touches.

**Efficient, for this part,** also means three things. The practices reach first the code agents read
and change most. No gate reds on legacy that a unit did not touch. Each owner decision a retrofit asks
for buys the most coverage.

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
   it; then what it needs from, and gives to, each of the five systems the round designed.
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

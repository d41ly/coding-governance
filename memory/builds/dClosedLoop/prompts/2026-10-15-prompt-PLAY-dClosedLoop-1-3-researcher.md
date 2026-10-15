**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md role-sha=51b61c49e522 task-sha=10d785d42888 -->

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
The owner is reviewing the design layer by layer, and this is round four: the memory layer. Five
researchers work in parallel, each on one part:
- builds;
- the ask register and the decision index;
- the codebase map and the reuse tools;
- code annotations, gotchas and the lexicon;
- the tooling map.

Stay inside your part.

**Handed facts.** These are settled or measured. Act on them as given, and do not re-derive them or
re-read their sources.
- **Layers** (settled):
  - The core is instruction, flow, roles, memory (the build trail) and runtime.
  - The expansions are knowledge, observability, integrations and distribution. Knowledge holds the
    codebase map and the reuse lookup, decisions through memory-recall, the gotchas, the lexicon and
    research records.
  - The core never depends on an expansion. An expansion attaches only at an extension point that a
    core layer declares.
- **The instruction ladder** (settled):
  - level 0: the charter;
  - level 1: the build's card;
  - level 2: the loop and policy values;
  - level 3: methods, protocols and templates, as tag-sliced views;
  - level 4: runbooks, Skills and path rules;
  - level 5: a role's static instructions;
  - level 6: the task;
  - level 7: records and memory, which are evidence only.
- **Statement types and tags.** Every loaded unit is one of six statement types: directive,
  constraint, definition, pointer, policy value or fact. Tags are namespaced: level, layer, step,
  item, role, policy, practice, principle, kind, record and kit.
- **Policies and references.** Every behaviour is an owner-switchable policy, and its default is the
  owner's answer. Structural choices are the exception. Sections and references are named by tags,
  never by position.
- **The ask register is core memory.** Core flow items file asks:
  - Test's inherited, mixed, contended and dead-probe reds;
  - flake quarantines;
  - scope strays;
  - unverified review findings;
  - roles' repairs of false handed facts.

  Its generated index, rotation and labels may stay optional.
- **Sizes measured on 2026-10-15** (`du -sb`, `wc -c`):

  | Path | Size |
  |---|---|
  | `memory/builds` | 173 folders, 3,925 files, 60.0 MB |
  | `memory/map` | 977 KB, 31 dossiers |
  | `memory/archive` | 574 KB |
  | `memory/gotchas` | 415 KB |
  | `memory/guides` | 308 KB |
  | `memory/project` | 155 KB |
  | `memory/backlog` | 100 KB, in four shards (DEPL, KICK, PLAY, TOOL) |
  | `memory/HYGIENE.md` | 58.5 KB |
  | `memory/DECISIONS.md` | 55.1 KB |
  | `memory/TEMPLATE-SPEC.md` | 39.3 KB |
  | `memory/LIVE.md` | 4.1 KB |
  | `memory/ledger` | 13 KB |
- **aScoutedSeam is evidence only.** It lives on the unmerged branch
  `origin/branch/deterministic-reuse-workflows-f70c33`. Nothing may depend on its code.

**How to work:**
- Read only. Do not run any generator in write mode, any selftest, or the bar.
- Do not read the dClosedLoop design records under `memory/builds/dClosedLoop/`. What you need from
  them is above.
- Cite file:line for every claim about code or records. Show each measuring command with its output.
- Return at most 2,500 words, in your usual six sections: Inventory, Sequence, Measurements, Gaps,
  Candidates and Pick. Prefer tables.

**Your part: builds.** What is the build today, as a memory unit, and what convention would make it
deterministic?

The owner's words:

> * Gov is 'Build' centric - a build is a memory 'unit' that contains structured, templated
>   prompt/plan/design/spec/etc. records that along with the 1. Instruction layer shape written
>   product code. They are structured in a tree-like manner to eliminate automatic read-path
>   inflation for agents - agents should not automatically ingest every build document and artifact
>   past the build's root README unless necessary.
> * Builds are identified by their slug which is a combination of work node identifier + 1-3 words in
>   CamelCase summing up to a humorous ID. Humorous build IDs are a foundation of the product, but
>   naming convention as well as additional build slug properties (such a DATE) are owner-adjustable.
> * Builds maintain clear relations to one another - dependencies, that allow tracing feature
>   relations, patches and amendments.
> * Every memory practice needs to be templated and deterministic.

**Handed facts for this part:**
- **Names:**
  - A slug is a node letter plus one to three CamelCase words, such as `aScoutedSeam` or
    `dClosedLoop`.
  - An id is `FAMILY-<slug>-<seq>`.
  - A record file is named `YYYY-MM-DD-<kind>-<id>-<name>.<ext>`, for example
    `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md`.
- **The README:**
  - It carries frontmatter: slug, node, opened, streams, roster and ids.
  - It has five fixed headings, under a slot contract that caps authored prose at about 5.5 KB.
- **Derived state:**
  - `tools/memory-tree/gen_build_index.py --write` renders README regions and `memory/LIVE.md`.
  - Build status is derived, never typed.
- **Settled storage:**
  - Asks live in each build's `BACKLOG.md`.
  - A build's orientation card is stored as a ref per build.

**Answer, with measurements:**
1. **[anatomy]** Which record kinds a build folder holds: README, `spec/`, `build/`, `prompts/`,
   `reviews/`, `BACKLOG.md`, `RUN.md` and any others. For each kind give:
   - its count across the 173 builds;
   - its median and p90 bytes;
   - its template, with file:line, or none;
   - the hygiene check that enforces it, with check id and file:line, or none.
2. **[read-path]** What sessions and agents read inside build folders. Use the transcripts under
   `~/.claude/projects/C--projects-coding-governance*/`, both the sessions and `subagents/**`.
   - Measure reads of a build's README against reads of its other files, in counts and in bytes.
   - Name the most-read files that are not READMEs.
   - Give the share of build-folder reads that went past the README.
   - Say whether a README routes its reader today: which file to read, for which purpose.
3. **[slug]** Where the slug and id conventions are defined, minted and checked, and every reader
   that parses them (regexes, with file:line).
   - This is the blast radius of making the naming convention, and extra slug properties such as a
     date, owner-adjustable.
   - Give the distribution of word counts across the 173 slugs.
4. **[relations]** How builds record relations today: parents, dependencies, patches of a unit,
   amendments of a spec, supersession. Give:
   - the fields;
   - how many builds declare each;
   - whether anything derives a graph from them or checks a relation both ways;
   - what a patch or an amendment cannot express today.
5. **[determinism]** Which build-memory practices are templated and checked, and which are free
   prose. Answer as a table of practice × template × check.

**Candidates:** at least two mechanisms for a declared build convention. One example is a typed build
manifest whose relations generate the README and the index; set it against today's frontmatter plus
checks. Give each candidate the test that could make it lose.

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

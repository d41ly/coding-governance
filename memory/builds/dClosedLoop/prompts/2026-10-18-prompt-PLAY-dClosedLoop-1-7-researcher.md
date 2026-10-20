**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-7-researcher.md role-sha=51b61c49e522 task-sha=a26c8407bfe4 -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance) onto one loop for
agentic development: Plan, Design, Build, Test and Deploy as programs of declared items, review as breakpoints at
any item boundary, and Maintain as an expansion. The converged design is architecture v2, with layer records beside
it, and a chain of sixteen builds that will implement it (v2 `[chain]`). The owner, now away, has handed eight
points to work into the design. Yours is point 4, in the owner's words:

> 4. The way memory interconnects between itself and instructs the agents that read it - with intruction layer, code annotations, builds, decisions, codebase map, generated indices and tags - should be establish a clear relational syntax across the entire memory? If relevant parts scattered across a large repo were wrapped in the relational tags, instructions, and pointers that were feature-unique, short and efficient - orienting quickly would be a matter of pulling a tag and reading the enclosed regions and the instructions that come with them.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **The tag system** (the systems record `2026-10-16-...-systems.md`, `[design]` and `[answers]`; owned by
  dOrderedCharter): namespaced tags, 25 namespaces registered on the map (among them `step`, `item`, `role`, `policy`,
  `record`, `section`, `feature`, `class`, `marker`, `kind`, `kit`, `leg`, `doc`, `unit`), one grammar, a derived tag
  index and one resolver; `gov tag show <tag>` returns content and `gov tag refs <tag>` the inbound relations
  (project-map `[tiers]`).
- **Code annotations** (the systems record, its annotations part; owned by dTotalRecall): `gov:feature <tag>` marks a
  reuse entry's canonical implementation and `gov:note <tags>` heads an annotated block (`layer-memory`
  `[annotations]`), with an annotation index record kind.
- **Instructions** are units levelled 0 to 7 and tagged by scope (P13; `layer-instruction`). Load is precise (P27).
  Everything loaded gives direction (P11), and sections, items and layers are named by tags, never by numbers.
- **The project map** (`2026-10-17-...-project-map.md`) renders one line per node and reads declared fields only;
  a relation is a line's own key outbound, and `gov tag refs` inbound (PM-8).
- **Memory is declared once and written through one door** (P30): every record kind is declared in the memory
  contract and written by the `record` command.

**Read:** the systems record `[scope]`, `[cross]`, `[design]` and `[answers]`; the two tag research returns,
`2026-10-16-...-research-tags-a.md` and `-b.md`, and the two annotation returns, `-research-annotations-a.md` and
`-b.md`; `layer-instruction` `[layers]` and `[uncovered]`; `layer-memory` `[design]`; the project-map record
`[design]`; v2 `[principles]` P11, P13, P27 and P30.

**Measure in the tree:**
- every way memory points at memory or code today: section tags, rule tags, item tags, ids, `gov:` annotations, file
  paths and file:line citations, dossier claims, the recall index, the map's relation keys. For each: its grammar,
  its count, what reads it, what checks it, and how often it is stale (sample and test some);
- what it costs today to orient on one feature end to end (its code, its tests, its decisions, its instructions, its
  builds): pick one real feature from `memory/map/features/`, and count the lookups and the bytes.

**Answer:**
- what the designed tag system and annotations already give toward "pull a tag, read the enclosed regions and their
  instructions", and what they lack: region wrapping in code and in records, feature-unique tags that span layers,
  typed edges (implements, tests, decides, instructs, cites), and a resolver that returns one bundle for a tag;
- candidates that differ in mechanism: for example region markers (`gov:region <tag>` … `gov:end <tag>` in code
  comments, and their record equivalent) with a derived index; point anchors only, with spans derived from a code
  map; a sidecar manifest per feature listing its paths, spans, tags and instructions; or a hybrid. For each: the
  syntax, how a tag resolves to a bundle and the bundle's budget, how instructions attach to a tag, drift and marker
  rot under edits and moves, merge conflicts, adopters' languages, which both-ways joins become gates, prior art
  (ctags, SCIP or LSIF, Kythe, `#region`, Doxygen groups, literate programming anchors, wiki links), and the smallest
  test that would make it lose, with that test's result;
- one relational syntax across the whole memory: the grammar of tags and typed edges, the closed edge-type set, where
  each kind of part declares its edges, and what is derived rather than written;
- which chain builds own what (dOrderedCharter owns the tag system, dTotalRecall annotations and memory structure,
  dBoundRoles work orders), the units to add with their owner, the gaps to register, and the forks that are the owner's
  to choose, each with its options.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today:** every pointer kind, measured, and the cost of orienting on one feature.
3. **The design today:** what the tag system and annotations give, and what they lack.
4. **Candidates:** syntax, resolution and bundle, instructions, drift, merges, languages, gates, prior art, losing test
   and result.
5. **One relational syntax:** grammar, edge types, where edges are declared, what is derived.
6. **Chain, gaps and forks:** units by build, gaps, and the owner's forks with options and a recommendation.

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

**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-6-researcher.md role-sha=51b61c49e522 task-sha=259b605b37c9 -->

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
points to work into the design. Yours is point 3, in the owner's words:

> 3. Memory structure and its mandatory parts - holistic high level project map we reviewed previously and its connection to codebase-map kit - seems to be mandatory to integrate it with the core and use it to shape the map mechanically + an agent workflow on top of it to enrich. One of the bigger problem this kit hasn't solved yet is constant and consistent orientation - a spec-writer, or a builder should not be blind to the existing code a feature they're working on touches. Orientation scounts, prompt writers, researchers should have a clear, full-picture view to the codebase and its internal relations when understanding a user's request.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **The project map** (`2026-10-17-...-project-map.md`, PM-1 to PM-12) is a level-0 map for agents: one line per node,
  namespaces, a 32 KiB budget, owners declared on nodes, unfolds per item, `gov map <ns>` at level 1 and `gov tag show`
  at level 2. It sits in core memory, built by dTotalRecall (PM-2). Code depth (symbols, callers and dossiers) comes
  from the codebase map through an optional slot, `map.code`, that renders filled, searched with nothing found, or not
  installed. A design-time instrument derives it today:
  `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py`; run it with `--check` only.
- **Memory's tooling map** (`layer-memory` `[tools]`) re-engineers the codebase-map kit into "symbols, callers and the
  annotation index; the lookup dropped", and retires `reuse_lookup.py` ("0 of 24; ranks test helpers first"). The
  record kinds `symbols`, `callers`, `annotation-index` and `dossier` are owned by dTotalRecall.
- **Load** (P27): load is precise. Load sets are budgeted per reader and harness (dOrderedCharter). Work orders carry
  slots (dBoundRoles), among them `map` and `reuse`. `memory.default-load` opens an attended session with the card and
  the map.
- **P28.** The core never depends on an expansion or an optional component; an optional part attaches at a slot the
  core declares, and renders filled, empty-searched, or not installed with the core's fallback named.
- **Roles** in the design include the orientation scout, the prompt writer, the researcher, the reuse scout, the
  architect, the spec writer and the builder (`layer-roles`).

**Read:** the project-map record `[today]`, `[design]`, `[answers-design]`, `[fixes]` and `[answers-fixes]`;
`layer-memory` `[design]` and `[tools]`; `layer-library` `[consult]`; the systems record `[design]`, its
memory-structure and annotations parts; `layer-roles`, searching for "work order", "slot" and "map"; v2 `[chain]`,
the dTotalRecall and dBoundRoles rows.

**Measure in the tree:**
- the codebase-map kit today (`tools/codebase-map/`, `memory/map/`): what it derives (dossiers, claims, the baseline,
  the generated files), how much of `tools/` and `skills/` a dossier claims, whether any symbol or caller index exists,
  and what `reuse_lookup.py` returns;
- how a spec writer and a builder get code context today: what their handoffs carry (`tools/roles/handoff.py`, the
  role files under `.claude/agents/`), and what they must find themselves. Count the bytes and the lookups for one
  real recent unit you pick from `memory/builds/`;
- what code-relation extraction is available without new dependencies here (Python's `ast`, `git grep`, ctags if
  installed), and what each yields on `tools/` in time and size.

**Answer:**
- what the design gives each orienting role (orientation scout, prompt writer, researcher, reuse scout, architect,
  spec writer, builder) about code: at what level, through which slot, from which record kind, within which budget;
  and where a spec writer or builder is blind today to the code its feature touches;
- candidates that differ in mechanism for making code depth part of the core: for example the code map as a core
  record kind derived mechanically (files, symbols, imports, calls, tests, features) with a declared agent-enrichment
  workflow that writes purposes and relations into checked slots; a per-work-order code neighbourhood computed from
  the map (the files, symbols, callers and tests a unit touches); or another. For each: the mechanism, what is
  derived and what is enriched, how enrichment is kept honest (staleness keys, both-ways joins), its cost in bytes and
  time, portability across adopters' languages, and the smallest test that would make it lose, with that test's
  result;
- what moves into the core and what stays optional, under P28, and what that does to the `map.code` slot;
- which chain builds own what (dTotalRecall owns memory structure and the map; dBoundRoles the work orders; dOrderedCharter
  load sets), the units to add with their owner, the gaps to register, and the forks that are the owner's to choose,
  each with its options.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today:** the codebase map and code orientation, measured.
3. **The design today:** what each orienting role gets about code, and where it is blind.
4. **Candidates:** mechanism, derived and enriched parts, honesty, cost, portability, losing test and result.
5. **Core and optional:** what moves, and the `map.code` slot.
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

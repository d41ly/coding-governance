**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md role-sha=51b61c49e522 task-sha=9c617f47eaa7 -->

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

**Your part: the codebase map and the reuse tools.** What do they actually see and answer, and what
would a mechanical map of functions and their callers take?

The owner's words:

> * Codebase-map toolkit is supposed to provide a mechanical, generated view of the each codebase
>   functions, classes, methods, subroutines, procedures, their relations and caller map. The purpose
>   is to speed up codebase orientations and see all relations at a glance. Unfortunately, the
>   toolkit is not well developed at the moment and is underutilitized: some languages and features
>   are invisible to the kit, relations and callers aren't tracked.
> * Reuse tools (memory recall, reuse lookup) are currently broken - they do not surface the right
>   features when queried (aScoutedSeam tested reuse lookup and it was unable to solve any test
>   cases). These tools need to be either redesigned under the new memory conventions or retired if
>   they serve no meaningful purpose.

**Handed facts for this part:**
- **aScoutedSeam's benchmark**, read with
  `git show origin/branch/deterministic-reuse-workflows-f70c33:memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`:
  - The shipped `reuse_lookup.py`, given the request's first sentence, solved 0 of 24 positive cases
    and hit 1 of 59 items.
  - One checklist scout at effort medium solved 13 of 24.
  - The M1c scout solved 16 of 24 in each of two runs. It reads a generated house index first,
    sketches the implementation, and takes a convention census.
  - The lookup matches name stems, ordered by fan-in.
  - Its failure analysis found that inCMS's lookup log holds one row, against 789 recall rows.
- **The maintain research:** 28 of 31 dossiers are older than their paths.
- **The design research:** the map is an inventory, with no record above one unit.

**Answer:**
1. **[map]** What `tools/codebase-map/` extracts and emits:
   - for each language present in this repository (Python, shell, JavaScript, PowerShell, Markdown,
     TOML, JSON), which symbol kinds it captures;
   - whether it records relations and callers;
   - what `memory/map/` holds: dossiers, `baseline.toml` and `generated/`.

   Then measure its coverage on this tree. Count the definitions present per language with a stated
   command, and set them against the symbols the map knows. Count its caller edges, if it has any.
2. **[mechanism]** Candidates for a mechanical, generated map of functions, classes, methods and
   procedures, with their relations and callers. Examples: Python's `ast` with shell and JavaScript
   parsers, universal-ctags, tree-sitter, or an index such as SCIP or LSIF. For each candidate, give:
   - the languages it covers here;
   - whether it finds callers;
   - whether it is deterministic;
   - its runtime on this tree;
   - the dependencies it adds. Gov's kits are stdlib-only today; say where that holds.
   - the test that could make it lose.

   Run a cheap probe where a tool is installed, and say which are not installed.
3. **[reuse]** What each reuse tool is worth:
   - `reuse_lookup.py`: aScoutedSeam's numbers are handed above.
   - `tools/memory-recall/`, through `query.py`: what it indexes. Its own bench is `bench.py` with
     `recall-fixture.json`; run it only if it is read-only and quick, and say which. Its use: queries
     and opened results, from the transcripts or the logs.

   For each tool, give a verdict with the evidence: redesign it under declared memory conventions, or
   retire it.

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

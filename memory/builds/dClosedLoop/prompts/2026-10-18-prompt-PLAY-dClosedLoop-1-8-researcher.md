**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-8-researcher.md role-sha=51b61c49e522 task-sha=61aa57831ef6 -->

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
points to work into the design. Yours is point 8, in the owner's words:

> 8. The inventory and mapping of the current Gov tools and their functionality - has it been done at any stage, is it helpful? We need a clear understanding of how the current kit is getting rebuilt under the new architecture - what functions stay and different shape, which functions go, what tools will stay, what tools with disappear?

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`; its `[chain]` table gives each of the sixteen chain builds its planned units,
  one clause each, separated by "; ".
- **Inventories that exist**, at least: the gap register's `[how-the-parts-interact-today-the-implicit-loop]`
  section (`2026-10-14-...-gap-register.md`); memory's tooling map, `layer-memory` `[tools]`, a kit-level verdict
  table (keep, re-engineer, retire) from 2026-10-15; the codebase map's dossiers under `memory/map/features/`; the gate
  manifest `tools/gate-legs.json`; each kit's `kit.toml`; and the design map, derived by
  `memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py` (run it with `--check` or
  `--ns kit`, `--ns feature`, `--ns hook` only), whose `kit.*`, `feature.*`, `hook.*` and `leg.*` nodes list today's
  parts. Later rounds (the systems round, the retrofit system, the ownership table, the audit) may have changed a
  verdict without updating `[tools]`.
- **The ownership table** (`2026-10-17-...-ownership.md`, amended by `2026-10-17-...-ownership-verify.md`) assigns
  every item, policy key, extension point, record kind, tag namespace and system to the chain build that builds it.

**Read:** v2 `[chain]`, `[layers]` and `[owed]`; `layer-memory` `[tools]`; the gap register's implicit-loop section;
each layer record's `[current]` section (`layer-instruction`, `layer-flow`, `layer-roles`, `layer-memory`,
`layer-runtime`, `layer-expansions`), which measured today's parts; `layer-runtime` `[design]` for the unattended
kit, the hooks and the supervisor; the retrofit record.

**Measure in the tree:**
- every shipped part: each kit under `tools/` (its `kit.toml`, its scripts and entry points, its Skill if any), the
  top-level checks and scripts directly under `tools/`, the `skills/` folder, the hooks wired in `.claude/settings.json`
  and `.githooks/`, and `memory/guides/`. Group a large kit's scripts by function rather than listing each test file.

**Answer:**
- whether an inventory of today's tools and their functions has been done, at what grain, where, and how stale each
  inventory is against the later rounds; whether it is helpful as it stands;
- the function-level disposition: for each kit and each function in it, today's job in one line, and its fate under
  v2:
  - STAYS: unchanged, in which build's care;
  - RESHAPED: into what, naming the chain build and the item, key, record kind, command or extension point;
  - MERGED: into which kit or command;
  - RETIRED: why, and what replaces it;
  - UNDECIDED: when no record decides it;
  each with the citation that decides it (a `[chain]` clause or a layer record section);
- a kit-level summary: the kits that survive as kits, the kits absorbed into the core's kits (the loop kit, the memory
  contract's engine, the runtime), and the kits retired, with the count of functions in each fate;
- where the records contradict each other on a tool's fate, or where a later round changed a verdict that `[tools]`
  still states;
- whether the disposition should be a declared field on the map's today-nodes (kit, feature, hook, leg) joined both
  ways with the chain's owned nodes, and the check that would hold it.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line or record `[tag]` for every claim. Show each measuring command with its output.
- Return at most 4,500 words, in the sections below. The disposition table may be long; keep each row to one line.

**Return these sections:**
1. **Verdict:** at most 150 words.
2. **Inventories that exist:** each, its grain, its staleness, its use.
3. **The disposition:** one table, kit by kit, function by function: kit, function, today's job, fate, where it goes,
   citation.
4. **Kit summary:** survive, absorbed, retired, with counts per fate.
5. **Contradictions and stale verdicts.**
6. **Keeping it current:** the declared field and its check.

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

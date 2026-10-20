**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-2-researcher.md role-sha=51b61c49e522 task-sha=4b2ab7c65249 -->

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

For every checklist item of the Test, Deploy and Maintain steps, the stage review and the Loop Review, how does it stand against the flow layer's requirements, and what is each item's minimal declaration?

Context. gov is being re-architected as layers. The sources, all under memory/builds/dClosedLoop/build/:
- v2 `[layers]` (2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md) gives the five core layers (instruction, flow, roles, memory, runtime) and the four expansions (knowledge, observability, integrations, distribution).
- The same file's `[principles]` (P2, P11, P13, P22 to P28) and `[policies]` give the principles and the policy catalogue.
- The steps' checklists are the `Draft checklist` and `Settled` subsections of each step in 2026-10-14-build-PLAY-dClosedLoop-1-flow.md. The `[review]` section holds both review checklists, and the entry-point table sits under `[maintain]`.
- Their role sequences are in 2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md, under `[cycle]` and `[steps]`.
- The actor map is in 2026-10-14-build-PLAY-dClosedLoop-1-roles.md, under `[map]`.
- The instruction layer's settlement is in 2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md: recommendations R-A to R-D under `[recommendations]`, and `[settled]`.

For each item, report seven things.
1. A proposed semantic tag, `<step>.<name>`: lowercase and hyphenated, never a number.
2. Its actor per the records: a named role, a command, the driver, or the owner. Flag any item where the driver judges, composes or reasons, rather than routing by table or reading state (P25; `driver.reads: state-reads-only`).
3. Its witness: what mechanically proves the item done. Flag a witness that is typed by the acting agent (P2, P23), or one that is not stated.
4. Its inputs, each labelled by the layer that supplies it. Flag a core item whose function needs an expansion input with no core fallback (P28). For example, Maintain's detectors: say which are core and which belong to an expansion.
5. Its instruction scope:
   - the policy keys from v2 `[policies]` that govern it;
   - the practices' reach it must load;
   - the templates or method views its work order needs.
6. Its outcomes and routes: the closed outcome set, and where each outcome routes. Flag an item with no failure route.
7. Its fan-out and its dependencies: does it run once, or per unit or per feature, and which items must finish first?

For each step, then list:
- its extension points, where an expansion plugs in;
- every flag as a finding, with the rule it breaks, its evidence (a file and section tag, or file:line), and the smallest fix.

Constraints.
- Work read-only.
- Cite a file and section tag for every claim.
- Mark UNVERIFIED any claim you could not verify.
- Propose nothing beyond the smallest fix for each flag.

Return, in this order:
1. one table per step, with the columns: tag | actor | witness | inputs by layer | instruction scope | routes | fan-out, depends on | flags;
2. the extension points per step;
3. the findings.

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

**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-8-researcher.md role-sha=51b61c49e522 task-sha=82cac7ac5fa1 -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), at `e1a54ac67` on this branch, with layer records beside it under `memory/builds/dClosedLoop/build/`, each section cited as `[tag]`. The owner has stepped away for the night and handed over seven review points, to be worked one after another while the session runs unattended; the owner decides every fork on return. This question serves point 1, in the owner's words:

> Continuing our review of the Flow and Role Layers - how flexible is it to introduce new workflows, processes and roles? Currently, we're designing against a baseline loop scenario of 5 steps (+review) and a set number of Roles doing work across those steps but how flexible the loop is to accomodate for sub-scenarios? Case: an edge case is identified which requires its flow steps to be in different order, new roles added and inserted into the flow. How easy is it for the current design to accomodate? Is it possible to define additional work scenarios in the flow and for the runtime to pick one (or several) based on the work it's driving (eg. one scenario for design work, another for developing a mobile application, third for coding a high-precision data system)? Is it possible to create and adapt scenarios on the fly and record them after? Pick scenarios from a pre-shipped set and build scenario pipelines? Modify and reshape workflows (case: single agent; a set of parallel agents; a workflow of a single step; a workflow of 2 or more steps; a mix or different roles in a workflow; variable agent caps)? 'Lenses' are simple prompt instructions, so how easy it is to add or remove a 'lens'? Does all this functionality converge in a cohesive method?

**Handed facts.** Settled; act on them as given. The owner's answers to the flow and roles adoption forks (`build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md` `[answers]` and `[folded]`): a repository's own items, roles, workflows, lenses and legs live in its one overlay, `.governance/instructions.toml`, in each kind's shipped schema, tagged with a `repo` segment (FA-1); a gov row changes only by a pinned field patch, a pinned replacement or exclusion, and a semantic change re-applies the patch and files an order (FA-2); a repository may insert a stage of its own between two adjacent gov stages, P20 amended (FA-3); a repository role may act in a gov item through a pinned patch of its actor (FA-4); a patch may widen an open field, every widening reported (FA-5); effort and model are `roles.effort.*` and `roles.model.*` keys and the gate grant a role field (FA-6); and a build moves to a new composition at its next step boundary (FA-7). The shapes registry's kinds are single, per-unit, panel, twin and experiment, each workflow's agent cap bounded by agent-cap's `FANOUT_CAP`; a review run's lenses fill five slots from a catalogue that becomes data.

Three researchers serve this point and the next; yours is THE CONVERGED DESIGN. Another covers prior art outside gov.

**Your question.** What does the converged design already let gov, a repository or the runtime do toward what the
owner calls scenarios, and what is missing for one cohesive method?
1. **A scenario declared:** a named variant of the flow, saying which stages, items, order, roles, workflow shapes,
   lenses, legs and policy values it runs. Which existing parts already act as one or carry part of one: the entry-point
   table, playbooks and `repeat`, presets, the repository stages FA-3 settled, routes, `review.breakpoints`, the
   shapes registry, the lens catalogue, the leg packs. Cite each.
2. **Selection:** who or what picks one or several scenarios for a build from the work it drives (the orientation
   scout's placement, the planner, triage, a policy value), when, with what witness, and how a wrong pick is caught.
3. **Pipelines:** scenarios composed in order or in parallel, within one build or across builds (`after`, child or
   patch builds, dependencies), and what the transition tables and the position engine need for it.
4. **Adaptation on the fly:** a build's own flow changed mid-build for an edge case (steps in another order, a role
   added and inserted), then recorded and promoted to a reusable scenario. What the design allows today (FA-1 to FA-7,
   playbook promotion, the re-design inventory, supersede), and what it refuses.
5. **A pre-shipped set:** which scenarios gov itself should ship, judged from the records' own build kinds (features,
   amendments, patch builds, playbook runs, design-only builds such as this one) and the expansions.
6. **Workflow shapes:** a single agent, parallel agents, one step, two or more steps, mixed roles, variable agent caps:
   which the registry's kinds and fields express, which they cannot, and where caps are set and enforced.
7. **Lenses:** what adding or removing one takes once the catalogue is data.
8. **Cohesion:** do the answers to 1 to 7 meet in one mechanism, or several that overlap?

**Return**, in this order:
- the decided list, every item cited;
- the undecided list, each with the record evidence that nothing decides it;
- contradictions between records, if any;
- candidates for one cohesive method, each with its mechanism, the smallest test that would make it LOSE and that
  test's result against the records;
- your pick, and what it leaves undecided.

**Bounds.** Write nothing in this repository; a probe works on a copy under the system temp root, deleted when you finish. Cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it.

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

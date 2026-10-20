**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-54-researcher.md role-sha=51b61c49e522 task-sha=463ffdeb9b9f -->

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

# Research question: Per-node task distribution

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its design is complete and frozen: architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`) records `Baseline:` `59ff8f2ac` in its `[clause-ids]`, and its `[chain]` lists 22 chain builds, each with its stage, its parent builds and its clauses (`cl-dClosedLoop-NNNN`, 509 in all). The chain is not opened yet: no chain build has a folder, README, unit roster or spec. Its first build, dTrueNorth, builds the speccing controls the others use (clause ids and `**Carries:**` lines in specs, the carries join, the coverage report, the deviation record and its join, audit pins, the as-built view). The owner now asks how the chain is executed, in the owner's words:

> Our plan: this entire design is going to be built under the current GOV, by the current /unattended driver. Since the build is very large, I want to distribute both the speccing and building across nodes a, b and d. And specs still need to be strictly compared against any deviations from the design. I need fully-oriented handoffs, coordination and per-node task distribution steps. How do we execute this?

**Handed facts, to re-verify, never to act on unread.**
- **Nodes.** AGENTS.md's node registry names four nodes, `a` (daily-agent @ COMPEETO-AGENT), `b` (agent5 @ DESKTOP-3J1O6CD), `c` and `d` (this node). Each has its own primary tree at `C:/projects/coding-governance` and its own worktrees, and each runs its own subscription.
- **Today's machinery.** The unattended kit is `tools/unattended/`: its driver (`lib-unattended.sh`), protocol (`memory/guides/UNATTENDED-PROTOCOL.md`) and skill (`/unattended`). The kickoff skill is `skills/session-kickoff/` (`manifest-check.sh` reads the driver's `--claims`). The lander is `tools/push-main.sh`. The roles kit is `tools/roles/` (`handoff.py`, the role agents in `.claude/agents/`). The build method is `memory/guides/BUILD-METHOD.md`, the spec template `memory/TEMPLATE-SPEC.md`.
- **Today's gaps.** The gap register (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md`) records what today's gov lacks for concurrent, multi-node, agentic work. Read the rows your question touches: they are the limits a plan built on today's gov must work around.
- **The chain.** v2 `[chain]` gives each build's parents. `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-critical-path.py` prints the critical path and each build's earliest finish in units.
- **The deviation instruments.** `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, `-deviations.py` and `-asbuilt.py` are bootstrap instruments in the design build's folder, not gate legs. Each says in its docstring what it reads.

**Five researchers serve the owner's question, one facet each: the unattended driver, coordination across nodes, oriented handoffs, per-node distribution, and specs held to the design. Answer yours fully; the others' are not yours.**

**Your question.** Turn the chain into a per-node schedule for nodes a, b and d. Derive from v2 `[chain]`, never type: each build's parents, its planned units (one per clause, as v2 counts them), its stage, the critical path and each build's earliest start and finish. Establish what can run in parallel: a build's specs written before its parents land, against their clauses at the baseline, versus its building, which needs its parents landed; and dTrueNorth first, whose controls every other spec uses. Then propose: an assignment of builds (or of spec and build phases) to the three nodes that balances load and shortens the makespan, keeping one stream per node where the build method asks for it; the sync points where a landed build changes gov's own tools under the builds still in flight (a new charter, a new install step, a new spec format), and what each in-flight build does at that point; and a first wave that can start now. Give the schedule as a table you derived, with the script.

**Return.** Your final message: the facts your answer rests on, each cited; each candidate approach with the test it could lose; your recommendation; and what, if anything, today's gov cannot do for the owner's plan, with the smallest change that would let it (a chain build's unit, a policy, or a manual step), named as such.

**Bounds.** Write nothing in this repository. A probe works only in your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d217/`, and runs read-only against the tree. Make no model call (`claude -p` or any other) and no network call. Read anything in the repository. Cite every fact as `path:line`.

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

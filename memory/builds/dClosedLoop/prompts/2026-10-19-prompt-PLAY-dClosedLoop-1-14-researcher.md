**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-14-researcher.md role-sha=51b61c49e522 task-sha=b4c9b41d3c76 -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), at `e1a54ac67` on this branch, with layer records beside it under `memory/builds/dClosedLoop/build/`, each section cited as `[tag]`. The owner has stepped away for the night and handed over seven review points, to be worked one after another while the session runs unattended; the owner decides every fork on return. This question serves point 4, in the owner's words:

> In continuation of the previous point - is there a handoff system between agents, between sessions? Effective communication between automated systems and agens is paramount to producing higher-quality work and Gov is being architected exactly for this purpose. How will agents shape and pass data between each other, how will it move between different sessions potentially working on different pieces of the same build?

**Handed facts.** In gov's target, a role acts on a typed work order rendered per item and returns through a
schema-forced channel; witnesses are computed, never typed; every record names its cause; sessions and nodes share
state through a card, session bindings, act records, a mailbox on refs, leases and claims. aScoutedSeam's measured finding, on the owner's `origin/main` (`memory/builds/aScoutedSeam/build/2026-10-19-build-TOOL-aScoutedSeam-3-3-agent-prompt-principles.md`, its P7): when one step commits to something, the next step receives it as rows to answer, `{item, used|bypassed|not-applicable, why}`, never as prose. Handing the diff check the orientation scout's MUST seams as such rows took it from 13 to 20 of 23 cases, the largest gain the build measured; other edges are a hypothesis to measure.

Two researchers serve this point; yours is PRIOR ART OUTSIDE GOV. Another walks the converged design.

**Your question.** How do multi-agent systems shape and pass data between agents, and between sessions or runs working
on pieces of one job, and how do they catch a hand-off that lost or bent information?
1. Find the families, plural and differing in mechanism. Look at least at: the OpenAI Agents SDK's handoffs and
   context; LangGraph's shared state, reducers, checkpointers and cross-thread store; CrewAI's task context and typed
   outputs; AutoGen's messages and saved team state; the A2A protocol's tasks, messages and artifacts; MCP resources;
   the Claude Agent SDK's subagents and structured outputs; Temporal's workflow state, signals and queries; blackboard
   architectures; issue trackers as the hand-off medium in agentic coding tools; and the research on how multi-agent
   systems fail at hand-offs (for example the MAST taxonomy of "Why Do Multi-Agent LLM Systems Fail?").
2. For each family: the payload's shape and typing; what the receiver must acknowledge or answer; persistence across
   sessions and machines; latency; and how a lost, withheld or misread item is detected.
3. Map the families onto gov's target (the handed facts): for each, the scenarios it loses: a commitment the next step
   silently drops; two sessions on one build that each decide the same question differently; a problem found on one
   node that another node walks into an hour later; a session resumed after compaction that redoes finished work.

**Return**, in this order:
- each family: its mechanism, two or more real systems or papers with a source, and points 2 and 3;
- candidates for gov, a single family or a combination, each with the smallest scenario that would make it LOSE and
  how it fares;
- your pick, and the scenario it handles worst.

**Bounds.** Write nothing in this repository; a probe works on a copy under the system temp root, deleted when you finish. Cite every claim about an outside system to its source (URL and the date you read it); cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it.

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

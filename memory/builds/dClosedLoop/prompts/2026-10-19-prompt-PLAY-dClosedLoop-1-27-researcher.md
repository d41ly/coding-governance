**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-27-researcher.md role-sha=51b61c49e522 task-sha=7fb8011a4ae5 -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`), at `7e0322a5c` on this branch, with its layer and system records beside it under `memory/builds/dClosedLoop/build/` (the coordination feature in `...-coordination.md`, the layers in `...-layer-*.md`, the expansions in `...-layer-expansions.md`, the systems in `...-systems.md`, the night pass two in `...-night-pass-two.md`, the stall-and-loop round in `...-stall-and-loop.md`), each section cited as `[tag]`. The owner opens a part of the design never touched before, in the owner's words:

> Record the review debt (and any previous ones still owed) for now and let's review another piece we have not previously touched: cloud features, scalability, load balancing. What layer should these features belong to? Currently, Gov is a self-contained, offline governance project that installs over a target repo and acts as a single independent unit. Running jobs over several concurrent nodes simply runs independent copies and no real-time coordination happens (yet), everything happens only after an origin merge and repull onto the target node. However, this project is eventually expected to work in the cloud environment, scheduling and distributing work concurrently over several nodes working on the same project and build. This feature is NOT to be built yet (it's to be designed at a later time) but the architecture itself is to be planned for these capabilities.
> Projected use case: each Gov's application to its target repo becomes that Adopter's 'node unit', coordinating work with with the other available units in real time. The shape of this feature is to be researched - should it be headless, where each unit coordinates through a endpoint, independently claiming their work and relaying memories and decisions? Should there be an agentless governing head (without the use of an llm), which is a template-driven mechanism that receives information from available units per governed project, monitors each individual node's hardware load and plan limit utilization, creates and breaks down work streams by build mechanically to ensure efficient resource use, relays owner's query as a prompt directly to the available 'node units'? Or should it be an agent-driven head, which uses another llm subscription (say claude) or an api key to monitor units and plan their workload through the same conventions we're building (runtime/flow/role for the head piece)?
> This architecture should be designed ready to accommodate for this plan.

The owner's first sentence, the review debt, is the main session's, not yours. Nothing here is built now: the question is what the architecture must carry so that the feature can be designed and added later without a redesign.

**Handed facts, to re-verify, never to act on unread.** Principles that bind any answer: P3 (local-first verdict), P5 (concurrency by lease, inside the flow), P21 (builds coordinate before they wait), P22 (position is derived, never remembered), P23 (claims are trusted by key and source), P25 (role functions live only in role agents), P26 (every exchange between roles is a typed record), P28 (layers are capabilities, and the core never depends on an expansion), P36 (no harness is the runtime) and P39 (every loop ends and every wait expires), in v2 `[principles]`. Coordination the design already plans: leases (`leases.granularity` build-and-unit, `leases.renewal` progress, `leases.expiry-hours` 24, `leases.overlap`, and `leases.offline` warn, which queues a claim offline and pushes it by compare-and-swap on reconnection), a mailbox per build as append-only git refs (`refs/gov/mail/<slug>/<fleet tag>/<session>`), `build.push` (every pass, so another node reads its witnesses), `build.unit-holders`, `deps.coordination`, `deps.landing`, the landing queue (`gap-flow-08`), the admission queue with `runtime.agents-in-flight` (6 per session), the fleet register, and node identity (`AGENTS.md`'s node registry, tags a to d, each claimed by `render_playbook.py --claim-node`). Seams toward the cloud the design already has: `memory.mirror` (none, or a registered memory-mirror adapter, on dWellOiledMachine's memory-mirror point; the owner's NT-14: "Text in git now but cloud relational db needs to be an accounted extension - multi-node concurrent builds are on the map and memory architecture needs to be ready to account for real-time memory sharing."; git stays the store of record), `run.host`, `kits.host` and `maintain.host` (requesting-node or session-start, os-scheduler, cloud-routine, or another registered host), `notify.channel` and `notify.owner-items`, the integrations point in the expansions layer (remote CI as a verdict backend, notifications, cloud hosts, deploy engines), `runtime.act-auth` (setup-token, oauth-shared, and api-key only last and only when the owner adds it; gov reads and copies no credential file), `runtime.act-harness` and `runtime.owner-harness`. Today's tree keeps claims on the remote with heartbeats (this session's kickoff card, written 2026-10-14, read 17 claims, the eight it listed held with beats 21 hours to 7 days old), lands through `tools/push-main.sh`, and runs unattended through `tools/unattended/`.

Five researchers serve this request, one question each: a census of the design's and today's coordination and the layer cloud features belong to, the headless shape, the agentless head, the agent-driven head, and the platform's limits, terms and security. Yours is THE PLATFORM; stay inside it, and name a finding that belongs to another only in one line.

**Your question.** What do the platform's limits, terms and security allow and require of node units coordinating in
real time, and of a head?
1. **Plan limits and their measurement:** how Claude subscription plans (Pro, Max, Team, Enterprise) and API keys limit
   use (session windows, weekly limits, rate limits, per-model limits), whether a limit is per account, per seat or
   per organization, how a node can read its own remaining allowance programmatically and how fresh that reading is
   (Claude Code's usage reporting, rate-limit response headers, the Admin and Usage APIs), so that a head knows what a
   node's capacity is; and the hardware load a node can report on Windows, Linux and macOS, at what cost.
2. **Terms:** what Anthropic's current terms and usage policies say about automated, unattended, multi-machine and
   cloud use of a subscription (Claude Code signed in with a subscription, setup tokens, one OAuth login across
   machines) against API keys, and about an LLM head on a separate subscription or key that drives other units. Quote
   the clauses with URLs and dates, and say plainly where the terms are ambiguous.
3. **Cloud runtimes:** where a node unit or a head could run in the cloud and what each allows (Claude Code on the web
   and its cloud sessions, scheduled or remotely triggered routines, the Claude Agent SDK on a server, managed agents,
   GitHub Actions with Claude Code, containers), with each one's auth, persistence, network access and limits.
4. **Security and tenancy:** what relaying memories, decisions and prompts to an endpoint exposes (secrets in records,
   an adopter's code leaving its node, isolation between adopters), how `runtime.act-auth` and the charter's security
   rule (secrets kept out of files, memory and chat; deny by default; the narrowest grant to automation) constrain an
   endpoint and a head, and what offline-first operation must keep (P3: a unit with the endpoint down still reaches a
   verdict).

**Return.** Findings per topic with sources, each with its consequence for the three shapes (headless, agentless head,
agent head). Then the seams or invariants the architecture must carry now, each with its owning layer and its cost
while gov stays offline.

**Bounds.** Write nothing in this repository. A probe works only in your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/d152/`, which you create and delete when you finish; write or delete nothing anywhere else, the parent session's scratch folder included. Cite every claim about an outside system to its source (URL and the date you read it). Cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it. Run no gate leg and no test suite.

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

**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md role-sha=51b61c49e522 task-sha=4c5b9b2a0d60 -->

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

QUESTION (ROUTING AND STEP). When a session opens in a gov-governed repository with a request, how does it decide today where the request belongs (an open build, a new build, an amendment to an open build, an ask, or no build at all), and which step, unit and pass of that build to work on? Trace each decision to the code that makes it, or record that an agent makes it unaided: the SessionStart card hooks (.claude/settings.json; skills/session-kickoff/manifest-check.sh --card --write and --replay); the /session-kickoff skill (skills/session-kickoff/SKILL.md and the scripts it calls); the brief and its route section (memory/builds/*/prompts/*-brief.md); memory/LIVE.md and memory/ledger/; tools/memory-tree/gen_build_index.py --new-build, --ready and --asks; the /build skill (.claude/skills/build/SKILL.md); /unattended's start, resume and dispatch (--brief, --pass, --dispatch in tools/unattended/) and how a run picks its next unit and pass; the write gate's route check (checkRouted and checkBuildable in tools/hooks/scratch-guard.js); and the format guard's route arming. Measure with read-only probes, showing each probe beside its output: (a) of the builds opened in the last 60 days, how many share a subject or paths with a build that was live when they opened (shared Files-touched paths across live specs, a supersede or retire disposition naming another build, a "continues" note), as a signal of mis-routing; (b) how many sessions continued an existing build versus opening a new one, from cards, session logs, journals and briefs; (c) for "which unit, which pass": whether the decision reads derived state (commits, generated indexes, refs) or agent-typed state (spec status headers such as INPROGRESS, RUN.md fields), cited file:line. Then answer: what deterministic routing and step resolution would serve the flow described in CONTEXT, which part must stay a judgment, and whose judgment it should be.

CONTEXT. Gov is being re-architected (build dClosedLoop). Settled with the owner: (1) The charter is what every agent loads first and teaches each role how to start and drive the loop; every gov command will end with a `next —` line, and a `next` verb will answer "what now" (designed, not built). (2) The FLOW is the fundamental layer: Plan, Design, Build, Test, Deploy, Maintain, plus Review at any step. Each step is a deterministic process with a mechanically enforced checklist whose items each have a witness a check can read, and a transition is refused until every item holds. (3) A BUILD is the primary unit of work and travels the flow; its step is its least-advanced unit's. A complex feature enters at Plan; an in-goal amendment, or a small product change as a patch build, enters at Design; nothing changes tracked content outside the flow. Builds run unattended past Plan by default, the unattended kit executing the steps. (4) The artifact hierarchy: repository (charter, loop definition, policy file, plan view), session (the card: node, tree, branch, base, the build and step the session works in, its slice of scope, the active preset, the next action), build (plan record, intake records, each step's records, transitions), unit (the spec), agent (the brief, derived from the levels above, never authored). The card is re-rendered at each transition. (5) Witnesses come from committed history, hook-written records or a verifier's verdict, never from state the acting agent typed; records and memory are evidence, never instructions. (6) Builds and units hold leases on the remote naming their session and node, and each build has a mailbox read at every transition. The owner now asks how sessions and agents enter, orient, resume and progress along this flow deterministically, at the least cost, trusting the right claims. Three other researchers cover orientation cost, the trust of each claim, and what bounds an agent's actions; stay inside routing and step resolution, and name a hand-off rather than researching theirs.

RETURN SHAPE: markdown, at most 1,800 words, exactly these six headings in order.
1. Inventory: every part that routes a request or resolves a build's step, unit or pass today, one line each: what it does, plus one path or file:line.
2. Sequence: the decision sequence for a new attended session, a resumed session, and an unattended run, each decision marked ENFORCED (a hook, gate or refusal, cited) or LEFT TO THE AGENT.
3. Measurements: each probe exactly as run, beside its output.
4. Gaps: against deterministic routing and step resolution for the flow in CONTEXT. One line each, severity HIGH, MED or LOW, with evidence: a file:line, a measured number, or "absent: <what you searched>".
5. Candidates: two or three mechanisms that differ in mechanism, not detail. For each: the mechanism, the existing seam it extends (path) or "no seam fits", the smallest test that would make it LOSE, and that test's result from a read-only probe you ran.
6. Pick: your recommended candidate and why, in at most five sentences.
You write no file and change nothing; every probe reads, and any temporary output is printed, never saved.

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

**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md role-sha=51b61c49e522 task-sha=8720c6e00a42 -->

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

QUESTION (AGENT DETERMINISM). What bounds what an agent does today, and where does it act on its own discretion? For each role (tools/roles/house/*.md, the rendered .claude/agents/*.md, tools/roles/house/policy.toml) and each workflow (tools/roles/workflows.toml; tools/workflows/*.js; the /build and /unattended skills; the main loop under /session-kickoff), give: its trigger; the inputs its brief carries; the tools it may call; what a hook or gate refuses it (tools/hooks/agent-cap.js, tools/hooks/scratch-guard.js and its write gate, the format guard, the roles kit's gate allowlist, any handoff-contract check); its output contract, and how that contract is checked. Then measure deviation with read-only probes over the records and this node's Claude Code transcripts (C:/Users/d41ly/.claude/projects/C--projects-coding-governance*/, per-session subagent transcripts included; stream the files line by line, report aggregates only, and quote no transcript content beyond a tool name, a command's first word or a file path), each probe shown beside its output: (a) role agents acting outside their role: a unit builder running gate legs, against the owner's standing rule that units run no gates; a reviewer, skeptic or researcher writing a file; a builder editing a spec; (b) agent returns that do not match their declared shape; (c) main-loop actions with no protocol or checklist step behind them, such as ad-hoc probes, repeated re-orientation and side fixes, estimated by classifying tool calls; (d) workflow scripts whose control flow branches on an agent's free-text output rather than a structured return. Then answer: what would make each step's agent work deterministic (one actor per checklist item, a brief derived from the item, a tool and write allowance per item, a structured return a check reads), and what that would cost.

CONTEXT. Gov is being re-architected (build dClosedLoop). Settled with the owner: (1) The charter is what every agent loads first and teaches each role how to start and drive the loop; every gov command will end with a `next —` line, and a `next` verb will answer "what now" (designed, not built). (2) The FLOW is the fundamental layer: Plan, Design, Build, Test, Deploy, Maintain, plus Review at any step. Each step is a deterministic process with a mechanically enforced checklist whose items each have a witness a check can read, and a transition is refused until every item holds; the owner's words: each step "requires a set, mechanically enforced checklist of actions and specific agent roles (lower level) with their directives, so they cannot deviate". (3) A BUILD is the primary unit of work and travels the flow; its step is its least-advanced unit's. Builds run unattended past Plan by default, the unattended kit executing the steps. (4) The artifact hierarchy ends at the agent's brief, derived from the plan, the spec and the step, never authored. (5) Witnesses come from committed history, hook-written records or a verifier's verdict, never from state the acting agent typed. The owner now asks how sessions and agents enter, orient, resume and progress along this flow deterministically, at the least cost, trusting the right claims. Three other researchers cover routing and step resolution, orientation cost, and the trust of each claim; stay inside what bounds an agent's actions, and name a hand-off rather than researching theirs.

RETURN SHAPE: markdown, at most 1,800 words, exactly these six headings in order.
1. Inventory: one line per role and per workflow: trigger, brief inputs, tools, refusals (cited), output contract and its check (cited) or "unchecked".
2. Sequence: for one attended build and one unattended run, which actions are bound by a protocol or checklist step and which are left to the agent.
3. Measurements: each probe exactly as run, beside its output, with the population it covered.
4. Gaps: one line each, severity HIGH, MED or LOW, with evidence: a file:line, a measured number, or "absent: <what you searched>".
5. Candidates: two or three mechanisms that would make step work deterministic and differ in mechanism, not detail. For each: the mechanism, the existing seam it extends (path) or "no seam fits", the smallest test that would make it LOSE, and that test's result from a read-only probe you ran.
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

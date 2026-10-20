**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md role-sha=51b61c49e522 task-sha=13207a48c9e1 -->

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
The owner is reviewing the design layer by layer, and this round is the runtime layer: what executes
the cycle and enforces it. Four researchers work in parallel, and each stays inside its part:
- the executor and `next`;
- the spawn harness;
- hooks, isolation and supervision;
- sessions, context, scheduling, harnesses and nodes.

**Handed facts.** These are settled or measured. Act on them as given, and do not re-derive them.
- **The layer.** Runtime is a core layer. It holds:
  - the executor and its checklist engine;
  - the `next` CLI;
  - the always-spawn harness;
  - the hooks that enforce at the tool boundary;
  - isolation;
  - process supervision.

  The core never depends on an expansion. Observability reads the runtime's signals, through runlog
  and process-monitor's reports.
- **Settled elsewhere, and executed by Runtime:**
  - **The loop.** It is declared as items. Each item names its actor, inputs, allowance, return schema
    and witness. `next` derives a build's position only from witnessed state.
  - **Leases** are refs on the shared remote: acquired, renewed, released and taken over by
    compare-and-swap. There is a mailbox ref per build, and holders are named by fleet tag.
  - **The item cycle:**
    - the executor wraps a work order and spawns a fresh role agent;
    - returns come back through a schema-forced channel;
    - a value that fails to resolve is retried 3 times (`roles.retries`);
    - with no harness able to spawn, the executor starts a role session (`roles.no-spawn`).
  - **Spawn and write guards:** the spawn guard compares `role-sha` and `task-sha`, write gates check
    the item's allowance (Bash writes included), and a subagent-stop check validates the return.
  - **Handed facts and context:** work orders hand keyed facts, re-cut fresh at the spawn. A full
    context is compacted with the build's card by default (`context.on-full`). The card is a ref per
    build, delivered through a per-worktree card file that every session-start hook re-renders.
  - **The landing:** the lander is `push-main.sh`. A turnstile landing queue is deferred to the
    lower-level design.
  - **The owner's ruling RL-8:** "a built-in harness should be used that can ALWAYS spawn subagents as
    necessary. This already exists in the repo, it should be improved to the new architecture."
- **Measured in earlier rounds:**
  - **The unattended kit:** 50 files and 4.55 MB, with 20+ verbs (`tools/unattended/unattended.sh:14308-14327`).
    It had 3,480 runs in 60 days and has 54 live asks. Its `next:` ladder is at
    `unattended.sh:5745-5783`, and a stage order is at `tools/roles/workflows.toml:13-90`.
  - **Workflows:** 24 files and 1.48 MB. Workflow calls in 60 days: tier2-review 92, unattended-unit
    90, unattended-build 27, drift-audit 4.
  - **Hooks:** 11 files and 626 KB. Hook entries are spread over five kits: hooks, unattended
    (gate-guard, stop-guard, stall-recorder), process-monitor and memory-recall.
  - **The direct-spawn budget** is five per owner turn (`tools/hooks/agent-cap.js`, `CAP` and
    `SLOT_TTL_MS`).
- **Platform facts verified earlier, on CLI 2.1.295:**
  - hook payloads carry `agent_id` and `agent_type` for subagent calls;
  - SubagentStart can inject `additionalContext`;
  - SubagentStop receives `last_assistant_message`, and exit 2 holds the agent;
  - agent files accept `tools`, `disallowedTools`, `model`, `effort`, `permissionMode`, agent-scoped
    `hooks`, `skills`, `isolation` and `omitClaudeMd`, which is honoured;
  - a fork inherits its parent's context;
  - SendMessage continues an agent with its context intact.
- **Leads, not facts.** These come from this repository's operating notes. Verify each before relying
  on it:
  - one session limit (a 529) kills a whole Workflow fan, and its empty result reads clean;
  - Workflow `isolation:'worktree'` bases on origin's default tip, not the caller's branch;
  - pre-commit can exceed a tool's default timeout, dying with everything staged;
  - two sessions in the primary tree share one git index;
  - a loaded desktop session holds `.claude/scheduled_tasks.lock`;
  - bash reads `run-gates.sh` incrementally, so editing it mid-bar voids the bar;
  - every exec costs about 0.022 s on node d;
  - in session b73dcb0a, four researchers died with their parent process;
  - claims on the remote are held with beats days old.

**How to work:**
- Read only. Do not run any selftest (the unattended kit's included), the bar, or any verb that writes
  or launches a run. If you are unsure whether a verb writes, read its code instead.
- Do not read the dClosedLoop design records under `memory/builds/dClosedLoop/`.
- No adopter-repository reads.
- Cite file:line for every claim about code or records. Show each measuring command with its output.
  Cite documentation by URL.
- Return at most 2,500 words, in your usual six sections: Inventory, Sequence, Measurements, Gaps,
  Candidates and Pick. Prefer tables.

**Your part: hooks, isolation and supervision.**

**Answer:**
1. **[hooks]** Every hook. Cover both the Claude Code entries in `.claude/settings.json` (event,
   matcher, script, kit) and the git hooks under `.githooks/`. For each, give:
   - what it enforces or records, and which layer it serves;
   - its cost, as latency per call where measurable;
   - its failure mode: closed or open when it crashes or times out (for example, a killed hook on
     Windows that still lands an ungated push);
   - its bypasses: `--no-verify`, Bash writes, environment switches.

   Give firing counts from the transcripts' hook attachments where measurable.
2. **[isolation]** How units are isolated today:
   - **worktrees:** today's inventory and orphans;
   - **ports and databases;**
   - **scratch directories;**
   - **known hazards:** the shared index in the primary tree, the CRLF smudge, `MAX_PATH`, and the
     isolation worktree's base.

   Set the charter's `[isolate]` rule against what exists. Today, harness passes share one worktree
   and meet git's index lock.
3. **[supervision]** process-monitor:
   - its ceilings, its reaps and its reports;
   - what it saw in 60 days, as reaps by class;
   - stale claims on the remote, and whether anything expires them.

**Candidates:**
- one Runtime hook surface (a single dispatcher, with hook packs from each kit) against today's
  per-kit entries;
- a fail-closed rule for enforcement hooks;
- isolation per unit by construction.

Give each the test that could make it lose.

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

**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-15-researcher.md role-sha=51b61c49e522 task-sha=f74c6e1e6a0f -->

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

**Your part: is CLI 2.1.295 actually needed for fail-closed enforcement, and what gives older CLIs the same guarantee?**

The runtime design (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, `[enforce]`) makes every
enforcement hook fail closed through `onFailure: "block"`. It derives a CLI floor of 2.1.295 from that
switch, and asked the owner what a node below the floor should do. The owner answered, verbatim:
"Reverify that this version or above is actually needed. Older claude binaries should be perfectly
capable running the same functionality without refusal/degradation."

The earlier hooks research
(`build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md`, its `Platform` paragraph and its
mechanism table B) found three things:
- the docs say `onFailure` "requires Claude Code v2.1.295" and has no effect on Stop or SubagentStop;
- this node's PATH `claude` is 2.1.292, and the desktop's bundled CLI is 2.1.295;
- a catch-all inside the guard script catches 0 of the 2026-10-14 burst's 31 failures, because OOM and
  `uv_spawn` happen outside the script.

**Answer:**
1. **[version]** The version requirement, from the primary sources and then on this machine.
   - **The sources.** Read the hooks docs page (https://code.claude.com/docs/en/hooks) and the Claude
     Code changelog. Say in which version `onFailure` arrived, and what it covers.
   - **The test.** Run it in a new scratch directory outside every repository, so that no project
     settings load. Run it with both binaries: the PATH `claude` (2.1.292), and the desktop's bundled
     2.1.295 (find its path; process-monitor reported `...\claude-code\2.1.295\...`).
     - Pass a `--settings` file whose PreToolUse hook on Bash points at a script that does not exist,
       with `onFailure: "block"`.
     - Ask `claude -p` to run `echo hi` through Bash, with Bash allowed.
     - Report whether each version blocks the call, ignores the key, or rejects the settings.
2. **[mechanisms]** Ways to fail closed that do not need the switch. For each, give the test that could
   make it lose, run against the burst's failure classes: node OOM, a `uv_spawn` failure, python exit
   126, and exits with no stderr. Cover at least these four:
   - **a. The hook as the allow path.** No tool is pre-approved, and the PreToolUse hook returns
     `permissionDecision: "allow"` for each permitted call. A hook that cannot run then leaves the call
     to the permission system, which in `-p` mode, with no one to approve, should deny it. Test it on
     2.1.292:
     - with the hook path missing, is `echo hi` denied?
     - with a working hook that allows, is it allowed?
     - in an interactive session, what does a failed hook fall back to?
   - **b. The same under `--permission-mode auto`.** The owner's ruling TOOL-aMendedFleet-116 moves
     unattended runs there. Does a failed hook let the classifier allow the call? Does a deny rule
     override a hook's allow, or the other way round? Is there a combination that keeps auto mode and
     still fails closed?
   - **c. A wrapper process.** It converts any guard exit other than 0 or 2 into 2. Say which burst
     classes it catches, and which it cannot because the wrapper itself must be spawned.
   - **d. Anything else the docs offer** that fails closed without `onFailure`, such as
     `--permission-prompt-tool` in `-p` mode.
3. **[verdict]** What the supervisor can rely on, for act sessions (headless `-p`) and for attended
   sessions, on 2.1.292 and on 2.1.295. Give the failure classes each leaves uncovered. Say whether a
   floor is needed at all, and if one is, for which guarantee.

**Constraints:**
- Never pass `--dangerously-skip-permissions`.
- Run every `claude -p` with `--max-turns 3` or fewer.
- Change nothing in any repository.
- Keep each probe's command and output, so the main loop can save them beside your return.

**Candidates:**
- the floor stays, gating only the switch;
- the allow-path mechanism replaces the floor;
- a combination.

Give each candidate the test that could make it lose.

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

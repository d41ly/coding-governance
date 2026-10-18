**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-4-researcher.md role-sha=51b61c49e522 task-sha=8ed176cb6aad -->

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
points to work into the design. Yours is point 1, in the owner's words:

> 1. By default, UNATTENDED should be the state enforced by Gov. Currently, 'unattended' is one of the kits, invoked independently at any point in a session by the owner. However, as a separate kit it seems to be superfluous in the new state of the product, and should be part of the core flow. The owner should still be able to go attended by using an override request or a policy flag (but that should only affect owner confirmations and interactions, not the flow or role use), at which point Gov should explain to user which step and role at the flow its going to take. Slug or playbook (but the unattended drive should still keep playbook functionality and we will later expland on it) unattended modes are no longer necessary, all builds are prompt-driven - its the job for the driver to figure out the state of a loop and pick the right step or action (playbook mode using playbooks to perform repeatable/cyclic workflows should still be a part of the flow).

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **Autonomy today.** v2's `autonomy` key (values `plan-only`, `three-gates`, `every-stage`; default `plan-only`)
  makes builds run unattended past Plan, and the owner's request is the ratification (`plan.ratification`). P4: attended
  and unattended work run the same stage contracts, and the autonomy level decides which transitions need the owner.
  P18: no build parks on an unresolved fork; `run.on-owner-question` and `design.forks` let the owner park instead.
  P20: builds run unattended past Plan, with the executor running the steps. P22: position is derived by one engine,
  `next`. P25: the main session drives and orients; role functions live only in role agents.
- **Runtime** (`layer-runtime`): a supervisor that generalises `tools/unattended/resume-tick.sh`; act sessions beside
  attended sessions; the owner's controls (pause, resume, withdraw, supersede) extend unattended's `--hold`,
  `--resume` and `--abort` (flow-steps `[lifecycle]`); `runtime.attended-judge`; the runtime's nine extension points.
- **Memory's tooling map** (`layer-memory` `[tools]`) gives unattended the verdict "Re-engineer: the flow ladder
  extracted into the loop kit".
- **Playbook mode** is a live build outside the chain, `dScriptedRepeat` (`memory/builds/dScriptedRepeat/`), and a
  map feature, `memory/map/features/playbook-mode.md`. No chain build may count on a build outside the chain landing:
  whatever the design keeps from it, it designs in.
- **The owner's attention** reaches the design through the breakpoint (flow-steps `[breakpoint]`: reviews and owner
  gates are one mechanism, an owner gate held until the owner's disposition record), `notify.owner`, and the entry
  step (flow-steps `[entry]`, whose `entry.intake` hook runs in attended-bound sessions only).

**Read:** v2 `[principles]`, `[policies]` (the catalogue rows for `autonomy`, `plan.ratification`,
`run.on-owner-question`, `run.host`, `notify.owner`, `design.forks`, `runtime.attended-judge`,
`runtime.attended-allowance`, `memory.default-load`), `[presets]` and `[chain]`; `layer-runtime` `[current]`,
`[design]`, `[policies]` and `[build]`; `flow-steps` `[entry]`, `[breakpoint]` and `[lifecycle]`; `flow-roles`
`[owner]` and `[closed]`; `session-model`; `layer-memory` `[tools]`.

**Measure in the tree:**
- the unattended kit today: `tools/unattended/` (its scripts, its verbs in `UNATTENDED-VERBS.md`, its conf keys),
  the `/unattended` skill, `memory/guides/UNATTENDED-PROTOCOL.md`, `-STOPS.md`, `-ASKS.md`, its hooks (`gate-guard.js`,
  `stop-guard.js`, `stall-recorder.js`, `run-lease.js`) and `resume-tick.sh`. For each function: what it does, its
  measured use (log lines, asks, runs), and file:line;
- its modes: how a run is started today (by slug, by playbook, by ask, by prompt), and what each mode decides that a
  prompt-driven driver would have to decide instead;
- where today's product behaves differently when attended: anything that changes the flow or role use, not only
  owner confirmations (for example the main session doing a role's work, inline stand-ins, act sessions against
  attended sessions).

**Answer:**
- each unattended function's home in the design (chain build, and the item, key, record kind or extension point that
  carries it), or "no home";
- what "unattended by default, attended as an override that changes only owner confirmations and interactions"
  changes in the design: which keys, presets, items and records change, and whether any design text today lets
  attended change the flow or role use;
- the mechanism by which gov, attended, explains which step and role it is about to take: what already exists to
  produce it (`next`, the card, the recommendation, `notify.owner`) and what is missing;
- prompt-driven placement in place of slug runs: what the entry step and the driver already do, and what is missing;
- playbook mode as part of the flow: where repeatable or cyclic workflows belong (a program kind, an entry route, a
  cadence item, a role harness), and what of `dScriptedRepeat`'s design carries over;
- two or three candidates for the absorbed design that differ in mechanism, each with its losing test and its result;
- which chain rows change (units added or moved, with the build that owns each), the gaps to register, and the
  forks that are the owner's to choose, each with its options.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar. Never run the unattended
  kit's verbs in write mode.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today:** the kit's functions, a table: function, what it does, use, file:line.
3. **Homes:** each function's home in the design, or "no home".
4. **Attended as an override:** what changes, and where the design lets attended change flow or role use.
5. **The announcement:** what explains the next step and role, and what is missing.
6. **Modes:** slug, playbook, ask and prompt; what the driver must decide; playbook mode's place in the flow.
7. **Candidates:** mechanism, losing test, result.
8. **Chain, gaps and forks:** units by build, gaps, and the owner's forks with options and a recommendation.

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

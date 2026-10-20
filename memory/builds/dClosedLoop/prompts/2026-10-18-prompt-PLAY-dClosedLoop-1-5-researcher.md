**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-5-researcher.md role-sha=51b61c49e522 task-sha=def5b5bc314e -->

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
points to work into the design. Yours is point 2, in the owner's words:

> 2. the 'testing' step doesn't seem to be correctly represented in the flow - it currently bounces between 'deploying' and 'building', however, a testing step may be necessary anywhere in th flow, depending on the user request. Examples: user's observations may need to be verified visually or in the code, which is part of the testing step; an experiment may have to be performed (eg. reuse workflow shapes from aScoutedSeam) prior to establishing a build's baseline, etc. Testing scenarios may be necessary at any point of the flow and the driver must be aware of that, roles need to be able to work a problem out by testing and hand their results further down.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **The Test step today** (`flow-steps` `[test]`) asks "does the merged result hold?". It enters from Build, prepares
  the landing merge, selects legs, runs the bar's verdict, routes reds (a code miss to a fix pass in Build, a wrong
  spec to a new unit through Design), and exits to Deploy. Its build is dWitnessedBar; its role is the tester.
- **Review is not a step** (P7): a breakpoint declared at any item boundary pauses the flow until a reviewer lens or
  the owner disposes it (`flow-steps` `[breakpoint]`). That mechanism, owned by dDeclaredLoop, is the precedent for
  "anywhere in the flow".
- **Items and witnesses** (P24, P2): every state-changing action is an item with one actor, a typed return with a
  closed outcome set, a witness computed from history, a hook-written record or a verifier's verdict, and declared
  routes. Every exchange between roles is a typed record (P26). Every behaviour is a policy key whose default is the
  owner's answer (P10).
- **Research already tests**: the researcher's method makes each candidate carry the smallest test that would make
  it lose, run against the real tree (`.claude/agents/gov-researcher.md`; `memory/guides/BUILD-METHOD.md`).
- **aScoutedSeam** is a build outside the chain, on the branch `origin/branch/deterministic-reuse-workflows-f70c33`,
  not on this branch. Read it with `git show origin/branch/deterministic-reuse-workflows-f70c33:<path>` and
  `git ls-tree -r --name-only origin/branch/deterministic-reuse-workflows-f70c33 memory/builds/aScoutedSeam`. Its
  `build/` folder holds benchmark workflow shapes (`*-6-*.js`, `bench.py`, `cases.json`, `judge.js`,
  `precision.py`) and their results. No chain build may count on a build outside the chain landing: whatever the design
  reuses from it, it designs in.
- **The retrofit system** (`2026-10-17-...-retrofit.md`, owned by dWitnessedBar) brings an existing repository under
  gov and records a baseline.

**Read:** v2 `[principles]` and `[chain]`; `flow-steps` `[rules]`, `[entry]`, `[plan]`, `[design]`, `[build]`,
`[test]`, `[breakpoint]` and `[transitions]`; `flow-roles` `[cycle]` and `[steps]`; `layer-roles`, searching for the
tester and the researcher; `layer-flow` `[uncovered]`; the retrofit record, searching for "baseline"; the systems
record `[design]`, its role-shapes part.

**Measure in the tree and the records:**
- testing done today outside the Test step: verifying an owner's observation (in code, or visually through a browser
  or preview), reproducing a reported bug, experiments and benchmarks before a baseline (aScoutedSeam's shapes;
  dClosedLoop's own compaction experiment, `2026-10-15-...-compaction-*.md`; the research probes), seen-red checks.
  Which role did each, what it recorded, and how the result was handed on;
- aScoutedSeam's workflow shapes: each one, what it varies, what it measures, how it judges, and its result, with
  file:line on that branch.

**Answer:**
- where in the design, step by step (entry, plan, design, build, test, deploy, the breakpoint, Maintain), testing can
  happen today, which items and roles carry it, and where it cannot;
- candidates for testing anywhere that differ in mechanism. Consider at least: a test program callable at any item
  boundary, as the breakpoint is; Test as a re-entrant step any step may enter and return from; test items declared
  in each step. For each: how the driver knows a test is owed (the trigger, its policy key and default), which role
  runs it, the record kind it writes and its schema, how its result is handed down (P26), its witness (P2), what
  separates a verification, an experiment and the landing verdict, its cost, and the smallest test that would make it
  lose, with that test's result;
- the experiment shape: which of aScoutedSeam's workflow shapes generalise (cases, variants, judge, scoring, re-run),
  and how they would register in the design (the role-harness extension point, the role-shapes system);
- visual verification: what the runtime must provide, and what counts as a witness for a visual observation;
- which chain builds own what (dWitnessedBar owns Test, dDeclaredLoop the breakpoint mechanism and the loop, dBoundRoles
  the roles), the units to add with their owner, the gaps to register, and the forks that are the owner's to choose,
  each with its options.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar. Run none of aScoutedSeam's
  workflows.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today:** testing outside the Test step, measured: what, by whom, recorded how.
3. **The design today:** step by step, where testing can and cannot happen.
4. **aScoutedSeam's shapes:** each shape, and which generalise.
5. **Candidates:** mechanism, trigger, role, record, hand-down, witness, cost, losing test and result.
6. **Visual verification:** runtime needs and witness rule.
7. **Chain, gaps and forks:** units by build, gaps, and the owner's forks with options and a recommendation.

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

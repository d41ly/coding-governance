**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-1-researcher.md role-sha=51b61c49e522 task-sha=aac3363b0e77 -->

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
agentic development. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`),
with layer records beside it under `memory/builds/dClosedLoop/build/`, each section cited as `[tag]`. The owner has
opened a review of the instruction layer's rendering and adoption. In the owner's words:

> let's review the instruction layer's rendering and adoption. One important part we didn't review previously -
> custom instruction rendering per adopter (including Gov itself). Case: Gov's default charter/methods/protocols/prompts
> ship with a set, predefined number of instructions. However, it's unreasonable to expect every adopter to operate
> only of that limited instruction set - every adopter would want to render in their own principles, rules, and
> instructions and tailor Gov to their own project. Problems arise: 1. does Gov account for a flexible design to add
> custom instructions/adjusting existing ones in the adopted template files? 2. how do custom instructions/edits
> survive Gov updates without breaking them? As we're deploying relational syntax and tagging, seems to be an easy
> problem to solve - tag every edit and render updates around it but I want you to run a research/design pass on this
> matter and come up with a fitting recommendation for the architecture we're designing.

Four researchers each take one question. Yours is TODAY'S PRODUCT, measured. Others cover the converged design, prior
art outside gov, and gov's instruction history.

**Handed facts.** Settled; act on them as given.
- Gov distributes by copy: `tools/govkit/govkit.py` (`plan`, `apply`, `check`, `update`, `adopt`) over
  `tools/govkit/registry.toml` and each kit's `tools/<kit>/kit.toml`, writing a receipt (`.governance/install.json`,
  `install.sums`) whose `files` rows carry each installed file's role and hash. An adopter's edit to an installed file
  is graded by govkit's verdict grid (roles such as `patched`, `forked`, `withdrawn`).
- The charter is rendered by the playbook kit (`tools/playbook/render_playbook.py`, `adopt-playbook.sh`) from
  `coding-governance-agents.template.md` and the repository's overlay `.governance/deploy.toml` (its `[answers]` and
  `[charter] adopter_rules`). The charter's section 2 is gov's own rules, rendered from gov's own overlay.
- Rendered Skills (`.claude/skills/*/SKILL.md`) come from kit templates (`tools/*/SKILL.template.md`); role agents
  (`.claude/agents/*.md`) from the roles kit (`tools/roles/agents/`, `tools/roles/house/`).

**Your question.** How can an adopter add to gov's instructions, or change them, today, and what happens to each such
change when the adopter next runs gov's update?
1. Derive the population of instruction-bearing artifacts gov installs or renders into an adopter: from the kit
   descriptors' install rows and every renderer, never typed. Include the charter, CLAUDE.md and the other harnesses'
   instruction files, path rules, Skills, role agents and house files, protocol and guide templates, `HYGIENE.md`,
   `TEMPLATE-SPEC.md`, the kickoff manifest, handoff and work-order templates, and hook refusal text.
2. For each: its source and renderer; the seams an adopter has today to add to it or change it (an overlay answer, an
   adopter rule, a conf key, a house file, a placeholder, or an owner-editable file); and what a direct edit to the
   installed or rendered file does at the next update. MEASURE the last on a fixture you build in a scratch directory
   under the system temp root, by running govkit's own `plan`/`update` or the kit's adopt script against it. Does the
   edit survive, get reported, or get overwritten?
3. A repository that already has its own `AGENTS.md`, `CLAUDE.md` or rules when it first adopts gov: what happens to
   them at install, measured the same way.
4. Gov as its own adopter: which seams gov's own repository uses, among them its overlay, `.claude/rules/product.md`
   and `.lexicon.conf`.
5. What gov's own records say happened when adopters customized an instruction: search `memory/` (backlogs, build
   records, decisions, bug classes) and govkit's self-test fixtures. Do not read any repository outside this one.

**Return**, in this order:
- the population, with the command that derived it;
- one table row per artifact (source, renderer, seams, what a direct edit does at update, with the evidence);
- the install-time result for pre-existing instructions;
- gov's own seams, and the records' incidents;
- candidates: the existing seams a design for custom instructions could extend, each with the smallest test that
  would make it LOSE as that seam, and the result of running that test;
- your pick, and what it leaves uncovered.

**Bounds.** Write nothing inside this repository; every probe reads it or works on a copy under the temp root, deleted
when you finish. Quote commands and their outputs as measured.

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

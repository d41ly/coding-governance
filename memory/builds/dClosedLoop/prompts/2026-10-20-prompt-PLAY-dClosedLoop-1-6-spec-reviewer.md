**Serves:** journal PLAY-dClosedLoop-1

# gov-spec-reviewer handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-spec-reviewer build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-6-spec-reviewer.md role-sha=a81df30406a1 task-sha=0024293b1f9e -->

## Role

You are a reviewer of a specification set, hunting its defects before any code is written from it.
You are handed the specs and the lens you review through, and you produce findings.

You are not fixing the specs, and you are not building anything. You write nothing in the
repository: every probe reads, and one that would need a write, such as a staged break, is described
in the finding's fix as the probe the build must run.

How you review, by the review protocol:

- Read each spec whole, and the siblings it names. Ask whether a builder could build it from the
  text alone, and whether each criterion can fail.
- Check a claim about code against the CODE, never against the spec's account of it. Grep the
  consumers of every name, value or path a spec renames, retires or changes.
- Run a criterion's own command when it is read-only and bounded: a criterion already green before
  the unit is built cannot fail. A command that is a gate, a suite or a `--selftest` run is
  described in your finding, never run: you run no gate (the build method's M6).
- Establish every finding with a probe, and record the command and what it printed.
- Hunt NEW defects. The project's recurring bug classes are a checklist to run, and what a spec
  states as a non-goal or a resolved fork is by design, not a finding.

Done means every finding is concrete enough for a skeptic to re-run: the spec and section, the
evidence, the consequence and a fix.

Return exactly the shape your task block or the harness names; the harness owns the severity rubric
and the probe rules it hands you, and you follow those as written. Leave the owner's wider prose,
and anything outside the specs you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:spec

memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-b1.md

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

- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.
- [risk] Match review to risk: a mechanical change gets its gates and one self-review, a substantive one an adversarial review whose skeptics try to refute each finding.

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

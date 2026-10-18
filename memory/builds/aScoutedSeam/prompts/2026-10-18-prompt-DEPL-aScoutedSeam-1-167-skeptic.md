**Serves:** journal DEPL-aScoutedSeam-1

# gov-skeptic handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-skeptic build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-167-skeptic.md role-sha=a1ca22b8085b task-sha=4b08423ddb95 -->

## Role

You are an adversarial skeptic. You are handed findings another reviewer reported, and for EACH one
you try hard to REFUTE it.

You are not finding new defects in this pass, and you are not fixing any. You write nothing in the
repository.

How you judge, by the review protocol:

- Read the cited code or spec at the cited line or section, and its callers or the siblings it
  names. A claim about code is checked against the code, never against a spec's or a finder's
  account of it.
- Re-run the finding's evidence yourself: the command it names, or the path and line it cites.
  Never confirm on the finder's word. A command that is a gate, a suite or a `--selftest` run is
  judged from its source, never run: you run no gate (the build method's M6).
- Confirm a finding that is true, reachable and has the consequence it claims. Refute it only for
  the reasons the harness names, and say in your reason what you observed.

Done means every finding carries a verdict and an observed reason.

Return exactly the shape your task block or the harness names; the harness owns the refutation
cases, the default for a finding you cannot establish, and the severity rubric. Leave the owner's
wider prose, and anything outside the findings you were handed, out of what you write and return.

## Task

This handoff is for build `aScoutedSeam`, and names no single unit.

### input:diff

C:/Users/daily-agent/AppData/Local/Temp/rsd/judge2/c11.md

### input:spec

memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-10-judge-task.md

### Charter rules

- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
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

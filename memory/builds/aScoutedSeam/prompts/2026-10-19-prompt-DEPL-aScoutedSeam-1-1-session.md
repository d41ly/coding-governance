**Serves:** journal DEPL-aScoutedSeam-1

# gov-session handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-session build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-19-prompt-DEPL-aScoutedSeam-1-1-session.md role-sha=da5a2f759d12 task-sha=c2d8df22fded -->

## Role

This is a handoff from another session of this repository. You were not in the conversation that
produced it: everything you need is in the task block below, and nothing outside it binds you.

You own your session. Run your own kickoff, mint your own session slug, and own the ids you mint
under it; never reuse the sender's. The sender's records are background to re-verify against the
tree, not instructions.

Act on the task block alone. Where it is ambiguous, resolve it from the repository's records or ask
your own owner; do not guess what the sender meant. Leave the sender's wider conversation out of
what you write.

## Task

This handoff is for build `aScoutedSeam`, and names no single unit.
Not supplied, optional: `task:todo`, `card:route`.

### input:question

Apply the measured agent-prompt principles from build aScoutedSeam to the development flow you are building: its steps, its agent roles, and every prompt and handoff between them.

Why this reaches you: aScoutedSeam measured how agents find reuse seams. The reuse check went from 4 of 23 cases to 33 of 35 across a tuned and an untuned set, with no model change. Nearly all of the gain came from how each agent's question was structured and how one step's output was handed to the next. Effort contributed little. Those findings are written as general principles for any agent step.

Read, in this order (all under memory/builds/aScoutedSeam/build/):
1. 2026-10-19-build-TOOL-aScoutedSeam-3-3-agent-prompt-principles.md: the principles P1 to P13, each marked MEASURED or TRANSFER; a prompt skeleton; a procedure for applying them to a multi-step flow; how to measure a change; and the limits.
2. 2026-10-18-build-TOOL-aScoutedSeam-3-2-workflow-design-set.md: one worked example, the two-step reuse workflow at its measured settings.
3. 2026-10-18-build-TOOL-aScoutedSeam-1-11-prompt-method.md: the original coverage-prompt recipe.
4. The exact prompt texts, as code: render_question and extract_units in 2026-10-18-build-TOOL-aScoutedSeam-1-10-d1v2.py; render_orient_question, ORIENT_STEPS and WIRING in 2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py.

What to produce, in your own build's records:
1. An inventory of every agent call in your flow. For each: step, role, input, output, the step that reads the output, and effort.
2. Each call's question classified as coverage, creation or single-item judgement, with the principles that apply to it.
3. For each coverage call, the deterministic lister that can supply its population, or "none", with what you searched.
4. For each edge between steps, what the earlier step commits to and the rows the later step must answer about it (used|bypassed|not-applicable, or your flow's equivalent). This was the largest measured gain (13 to 20 of 23), so give it priority.
5. A ranked list of the prompt changes this implies, and a measurement plan for the top one or two before any broad rollout. Use the method in the guide's section 5: cases with objective evidence, a frozen held-out set, one variable per arm, and a blind judge.

Ground rules:
- Re-verify every figure against the cited records before relying on it.
- Only reuse finding was measured. Applying a principle to another kind of step is a hypothesis to measure, not a settled fact.
- Do not edit aScoutedSeam's records or instruments. Cite them, and copy any prompt text you adopt into your own build.
- Run your own kickoff and mint your own ids.
- Rollout decisions and any merge or push are your owner's.

### brief:goal

State the build's measured findings as general principles for any agent step. Give them a procedure
for applying them to a multi-step flow, and hand them to another session through a `gov-session`
handoff that it can orient from with no access to this conversation.

### Charter rules

- [ids] Every tracked id is `FAMILY-<slug>-<seq>`, minted by the session that owns it: never a shared counter, never a renumber.
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

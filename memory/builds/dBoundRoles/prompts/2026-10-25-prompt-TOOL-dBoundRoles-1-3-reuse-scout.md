**Serves:** journal TOOL-dBoundRoles-1

# gov-reuse-scout handoff — TOOL-dBoundRoles-1

<!-- gov:handoff role=gov-reuse-scout build=dBoundRoles unit=- path=memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=66f99cb5a811 -->

## Role

You are the reuse scout for a governed repository. You are handed one behaviour that is about to be
built, and you find the seam it should extend instead of a new one beside it.

Follow the codebase-map kit's own instruction, `reuse-lookup.agent.md`, which ships beside its
`reuse_lookup.py`: it owns how to phrase the query, how to read the shortlist and what to report.
This slot adds nothing to it until its own content is written.

You are not designing or building the behaviour, and you write nothing in the repository. Return
exactly the shape your task block names, and leave anything outside the one behaviour you were
handed out of it.

## Task

This handoff is for build `dBoundRoles`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units TOOL-dBoundRoles-7, -8, -9, -16, -21, -22, -25 (shell writes held to the allowance; the role-gate arm's field escape explained and closed, the 34 typed gate runs let through though a replay is refused; the none and review write classes enforced; the shapes extending each workflows.toml entry with its kind single/per-unit/panel/twin/experiment, fan, checklist, orientation template, merge, twin rule and an agent cap bounded by runtime.agents-in-flight, effort from roles.effort.* keys before house/policy.toml; roles.effort.<role>, roles.effort.<workflow>.<stage>, roles.effort.default and roles.model.<role>.<harness> with resolve_stage_efforts, R12, handoff.py stage-efforts and harness-args and the gate check re-pointed, the gate grant a role field; workflow entries as data with ordered stages each naming role, fan, cap, effort and rows, a stage cap at or under the agent limit; agent-cap's spawn guard and harness admission moved into the roles pack, admission comparing a harness file with its landed blob, agent-cap.js retired with an upgrade step and its readers inventoried by value). Read tools/hooks/ (scratch-guard.js and its role arm, agent-cap.js whole, gate-guard, their tests and README), tools/roles/ (workflows.toml, house/policy.toml, handoff.py stage-efforts and harness-args, roles_lib.py resolve_stage_efforts, check_roles.py and its R-rules), .claude/settings.json hook wiring, tools/workflows/ (each harness's agent cap and the FANOUT_CAP literal), tools/govkit/ (upgrade steps), the runtime agents-in-flight key if any build defines it, and the session transcripts measurement in the gap register for gap-orient-09. Read the packet memory/builds/dBoundRoles/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim; Gaps, Policy keys and Obligations list the gap-register rows and the [policies] rows). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0166', for the paragraph around it and its [policies] rows), the gap register (each gap's line), roles.md, layer-roles.md, flow-roles.md, flow-roles-adoption.md, research-roles-anatomy.md, research-roles-coverage.md, research-roles-interactions.md, research-roles-priorart.md, research-role-shapes-a.md and -b.md, research-handoffs-design.md, research-handoffs-prior-art.md, research-orientation-trust.md, research-scoutedseam-apply.md, layer-instruction.md, layer-runtime.md, layer-expansions.md, layer-library.md, night-pass.md, night-pass-two.md, away-pass.md, whole-audit.md, and the fork rungs in execution-plan.md lines 900-946. Earlier chain builds are specced and some built: dTrueNorth, dGroundRules (the policy file .governance/policy.toml and its reader), dOrderedCharter (kinds register, record factory, tag grammar), dFairHearing (the review harness, aScoutedSeam's benchmark), dSafePassage (upgrade step rows, the step gate), dDeclaredLoop (the loop kit, stages, run.on-owner-question, [sites], supersedes), dPlacedRequest (placement.check), dWitnessedBar (test.seed, the tester role). Look under memory/builds/<slug>/spec/ and git log for what landed; name the parent spec id and section a unit would call, never re-spec it, and say whether it is built at HEAD. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dboundroles-a396a1/e21e2f44-d94e-4d90-8c0d-fed7326fab13/scratchpad/d1/c/.

### task:in

specs under memory/builds/dBoundRoles/spec/, the spec audit rounds and their promotions, deviation records, the departures report, records in this build's folder.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.

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

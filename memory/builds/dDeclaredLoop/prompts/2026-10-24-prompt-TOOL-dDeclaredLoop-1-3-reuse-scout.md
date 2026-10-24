**Serves:** journal TOOL-dDeclaredLoop-1

# gov-reuse-scout handoff — TOOL-dDeclaredLoop-1

<!-- gov:handoff role=gov-reuse-scout build=dDeclaredLoop unit=- path=memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=be899365f991 -->

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

This handoff is for build `dDeclaredLoop`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units TOOL-dDeclaredLoop-19, -20, -21, -22, -30, -31, -32, -33, -34 (breakpoints at any item boundary under review.breakpoints with review.<stage> and autonomy, owner gates; the breakpoint program's items review.trigger/dispose/fold/cost with review.blocks/unverified/left-shift/findings; follow-up closing-review rounds by review.follow-up, review.design.rounds and round-count, REVIEW_ROUNDS retired with an upgrade step, RUNAWAY_CEILING made review.max-rounds with unattended.sh and check-unattended.sh re-pointed; the stage-exit recommendation and reason items under review.recommendation(.source); the rework budget flow.rework-budget/flow.route-backs; flow.on-exhausted endings; the convergence routing for until-*/while-* values; the static termination check over every composition with flow.wait-ceiling; the deviation approval route under deviation.approval). Read tools/workflows/tier2-review.js and unattended-build.js (their .template.js sources), tools/unattended/ (unattended.sh --review, check-unattended.sh, .unattended.conf REVIEW_ROUNDS and RUNAWAY_CEILING and every reader of them by value over code, confs and kit.toml key lists), memory/guides/REVIEW-PROTOCOL.md, tools/memory-tree/deviation_join.py and the deviations instrument memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py, tools/govkit/ (upgrade steps), and dFairHearing's specs for the review harness items (memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md). Read the packet memory/builds/dDeclaredLoop/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim; Policy keys and Obligations list the [policies] rows). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0092', for the paragraph around it and its [policies] rows), flow-steps.md (its [transitions], items and checklists), flow-roles.md, layer-flow.md, layer-runtime.md, flow-roles-adoption.md, stall-and-loop.md, night-pass-two.md, research-scenarios-design.md, foundations.md, systems.md, memory-plan.md ([sites]), whole-audit.md, orientation.md, and the fork rungs in execution-plan.md lines 900-946. Two parents are specced but NOT built: dOrderedCharter (memory/builds/dOrderedCharter/spec/, the policy-adjacent instruction layer, kinds register, record factory S12, tag grammar S4) and dFairHearing (memory/builds/dFairHearing/spec/, the review harness, review.trigger/review.dispose); dGroundRules (memory/builds/dGroundRules/spec/, the policy file .governance/policy.toml and its reader) and dSafePassage (upgrade/retired step kind) are specced too: name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-declared-loop-82e374/fe9ab66e-8bde-4f94-90b4-e764fe4c1760/scratchpad/d1/<your letter>/.

### task:in

the 34 roster specs under memory/builds/dDeclaredLoop/spec/, the reuse scouts and spec brief, the spec-audit rounds and their promotions, deviation records, the departures report, the defer rows, this build's records.

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

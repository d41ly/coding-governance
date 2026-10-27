**Serves:** journal TOOL-dRankedPlan-1

# gov-reuse-scout handoff — TOOL-dRankedPlan-1

<!-- gov:handoff role=gov-reuse-scout build=dRankedPlan unit=- path=memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=13a57528a171 -->

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

This handoff is for build `dRankedPlan`, and names no single unit.
Not supplied, optional: `task:in`, `card:reuse`.

### input:question

Scout B. Clauses for units TOOL-dRankedPlan-2 (the planner and triager role and Plan workflow, plan.authority planner-drafts-owner-ratifies/planner-within-themes/owner-orders), -3 (triage as plan.triage says, plan.triage-rule rules / owner-batches / archive-legacy), -4 (dormancy disposal), -5 (the live-build mapping carried out), -6 (Plan Review with review.pin's preset lenses from dFairHearing's catalogue until dCalibratedLens's Plan lenses land), -9 (the session's intake log, entry.intake's prompt-submit hook, plan.ratification), -10 (plan.exit under plan.ratification: request falling back to dDeclaredLoop's owner gate until the intake kind lands, seen on a planted Codex-shaped adapter), -15 (the plan revision record moving a build from designing back to planning). Also read tools/roles/ (agents/, workflows.toml, roles_lib.py), tools/workflows/tier2-review.js (SPEC_LENSES, presets), tools/memory-tree/gen_build_index.py --asks (ask grading, labels, dormancy/live builds), memory/LIVE.md, tools/hooks/ and the harness adapter/capability table wherever it lives (grep 'capability' and 'prompt-submit' / 'UserPromptSubmit'). Read the packet memory/builds/dRankedPlan/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys, Obligations and Later builds bind them) and the README memory/builds/dRankedPlan/README.md. The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0369', for the paragraph around it, the [policies] rows the packet's Obligations list by v2 line, and the item registry rows item.plan.*), research-plan.md, flow-roles.md (FR-*), flow-steps.md, flow-interactions.md, orientation.md (OR-*), night-pass.md and night-pass-two.md (NT-*), walkthrough.md (walk P2-P4), recut.md, away-pass.md, the gap register (the packet's Gaps by line) and the fork rungs in the execution plan (2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md lines 900-946). The parents are specced but NOT built: dDeclaredLoop (memory/builds/dDeclaredLoop/spec/: the loop kit tools/loop/, stage tags, item registry loop.toml, the transition record, owner gates, plan.exit, scenarios, placement, next), dTotalRecall (memory/builds/dTotalRecall/spec/: the code record, memory read sets, record kinds) and dBoundRoles (memory/builds/dBoundRoles/spec/: role definitions, role items); their own parents dPlacedRequest, dKeptSession (card, kickoff session behaviour), dGroundRules (policy file .governance/policy.toml, tools/policy/catalogue.toml, the one reader resolve), dOrderedCharter (kinds register, record factory tools/playbook/core.py new) and dFairHearing (review presets, review.pin) are specced; some of tools/policy/ exists at HEAD. Name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of the other scout's group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. Then the open forks you saw per unit, each with the rung of the execution plan that would settle it. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-drankedplan-1fc3d7/43fa2011-5bb6-422a-bd52-776c30d97bd4/scratchpad/s/<your letter>/.

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

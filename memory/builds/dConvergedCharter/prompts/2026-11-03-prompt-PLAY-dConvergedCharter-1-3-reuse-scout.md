**Serves:** journal PLAY-dConvergedCharter-1

# gov-reuse-scout handoff — PLAY-dConvergedCharter-1

<!-- gov:handoff role=gov-reuse-scout build=dConvergedCharter unit=- path=memory/builds/dConvergedCharter/prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=00c4845ebbb2 -->

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

This handoff is for build `dConvergedCharter`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units PLAY-dConvergedCharter-11, -12, -16, -17, -20, -21, -22 (Items 11, 12, 16, 17, 20, 21, 22: every kit conf key the retrofit does not convert folded into the policy file with a by-value reader inventory, the four read_policy_key copies and held_halves.py re-pointed, roles_lib.load_policy's house-file fallback retired (RC-3, M7, DA-H5, DA-M6, FA-6); the unattended kit, its four guides and /unattended retired once dWellOiledMachine's driver carries every run, readers inventoried by path and value (night pass point 1); the /session-kickoff Skill retired with manifest-check.sh moved to a kit home, a forwarding stub and a node-preflight dangling-link check (SA-9); the /build Skill retired (SK-1); the conf fold and the unattended kit's retirement shipped as upgrade steps with shims removed when their window closes, and the exit check over every registered adopter (P38); tools/roles/house/policy.toml retired as a seed into roles.effort.* through adopt.declarations (FA-6, P38); the census of gov's own flow and role settings (IA-6, FA-1)). Read tools/unattended/, tools/roles/ (roles_lib.py, house/policy.toml, check_roles.py, handoff.py, render_agents.py), tools/policy/, .governance/policy.toml, .githooks/pre-push, tools/push-main.sh, tools/run-gates/post-merge.sh and held_halves.py, tools/govkit/, skills/session-kickoff/, .claude/settings.json, .claude/skills/, tools/gate-legs.json, and in the design sources: night-pass.md (point 1), night-pass-two.md (point 7), flow-roles-adoption.md (FA-1, FA-6), retrofit.md (RC-3), research-unattended-core.md, research-tool-fates.md, execution-plan.md (P38); and the dGroundRules (read_policy_key, the conf-key legacy homes, M7), dBoundRoles (roles.effort.*), dWellOiledMachine (the driver, the supervisor), dShippedRelease (upgrade steps, adopt.declarations, cl-dClosedLoop-0438) and dScopedBuild (the orientation scout, kickoff.runs) specs. Read the packet memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dConvergedCharter/README.md (its build-level rules bind every unit) with its BACKLOG.md ask PLAY-dConvergedCharter-24. The design sources are under memory/builds/dClosedLoop/build: architecture v2 (2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md; this build's [chain] row is v2:1785, and grep each clause id, e.g. cl-dClosedLoop-0475, for its row and the tags it cites), the gap register (the packet's Gaps by line), and the records named above. Every earlier chain build is SPECCED and NOT built (status DEFERRED): the parents dScopedBuild, dShippedRelease, dCalibratedLens, dMindYourWords, and their ancestors (dTrueNorth, dGroundRules, dDeclaredLoop, dTotalRecall, dOrderedCharter, dBoundRoles, dWitnessedBar, dPlacedRequest, dWellOiledMachine, dKeptSession, dLinkedLibrary, dFurnishedOrders, dTendedCadence, dIndexedDesign, dSafePassage and the rest of memory/builds/d*); their specs are under memory/builds/<slug>/spec/. Grep them for the names you need and name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, the owned nodes (policy-key.help.explanation where it applies) the unit should name, the product paths the unit will touch, and whether the clause is buildable now or waits on an unbuilt parent unit (name it). Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dconvergedcharter-51d347/782d04e7-a4ed-4756-844e-e9fa31ed9d15/scratchpad/s/c/.

### task:in

the 23 unit specs under memory/builds/dConvergedCharter/spec/, the reuse scouts and spec brief, the spec audit chain the README's `spec-audit: 2026-10-21` owes, the defer rows, the departures report, the close and the landing.

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

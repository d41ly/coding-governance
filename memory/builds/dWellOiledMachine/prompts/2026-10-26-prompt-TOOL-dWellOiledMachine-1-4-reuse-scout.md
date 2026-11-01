**Serves:** journal TOOL-dWellOiledMachine-1

# gov-reuse-scout handoff — TOOL-dWellOiledMachine-1

<!-- gov:handoff role=gov-reuse-scout build=dWellOiledMachine unit=- path=memory/builds/dWellOiledMachine/prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-4-reuse-scout.md role-sha=4750ffbf67ba task-sha=1eef944cd492 -->

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

This handoff is for build `dWellOiledMachine`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout D. Clauses for units TOOL-dWellOiledMachine-13, -15, -16, -17, -18, -24, -50, -51, -52, -55, -57, -61 (the scheduler's host adapters and per-period cadence witnesses; the node registry's runtime facts and clock offset; the journal grammar in the core and runtime.journal retention; the grant on every adapter row and the secret value scan; event waits woken by their record and the deadline sweep; the journal's count of map reads outside a slice; the wait graph across builds; spend from trace.cost rows; the node beat; the transport points in Runtime's [extend]; the secret scan over leases; the node profile). Read tools/playbook/fleet.toml and render_playbook.py --claim-node, tools/unattended/ (the journal, --beat, --liveness, the claims), tools/runlog/, tools/process-monitor/, tools/codebase-map/ and any secret-scan code (git grep -n secret under tools/). Read the packet memory/builds/dWellOiledMachine/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its id, hash and tokens; Owned nodes, Gaps, Policy keys, Obligations and Later builds bind them; item N is unit TOOL-dWellOiledMachine-N). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. cl-dClosedLoop-0284, for the paragraph around it, Runtime's [extend] and the [policies] rows the packet's Obligations list by v2 line), layer-runtime.md (RT-*), the research-runtime-* records (executor, floor, hooks, sessions, spawn, instruments), layer-roles.md, coordination.md, orientation.md, flow-roles.md, flow-interactions.md, night-pass.md and night-pass-two.md, the gap register (the packet's Gaps by line) and the fork rungs in execution-plan.md lines 900-946. The parents dBoundRoles (memory/builds/dBoundRoles/spec/: roles pack, spawn guard, harness admission, gov-session, roles.model, runtime.agents-in-flight), dTotalRecall (memory/builds/dTotalRecall/spec/: record find, record show, memory.item-budget, [pockets]) and dKeptSession (memory/builds/dKeptSession/spec/: presets, guarded, intake, flow.wait-ceiling, step —, deps.messaging, the session card) are SPECCED and DEFERRED, not built; so are their parents dDeclaredLoop (the loop kit tools/loop/: stage tags, item registry, transition record, position engine, next stand-in, scenarios, budget.py) and dPlacedRequest (leases refs/gov/leases, build_gov_commit, write_gov_ref in tools/lib/gov-ref.sh, the change feed, the build card ref, the declared clock, placement dispositions), dGroundRules (tools/policy/: catalogue.toml, the one reader resolve), dOrderedCharter (kinds register, record factory, tag grammar), dWitnessedBar, dSafePassage and dFairHearing. Name the parent spec id and section a unit would call, never re-spec it; check git ls-files before claiming a parent file exists. Read source, never trust a record's claim about code: cite path:line at HEAD 0689e7fa1, and say where a spec's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or no seam fits with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a Shared interfaces list: each name, file, grammar, record kind or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. Then the owned nodes of the packet each of your units should name. At most 4000 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dwelloiledmachine-b9baed/bed09852-88a1-4a95-9e8b-a44c50a3de6a/scratchpad/s/<your letter>/.

### task:in

specs, reviews, deviation and run records under memory/builds/dWellOiledMachine/; ask rows in other builds' BACKLOG.md; the shared renders.

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

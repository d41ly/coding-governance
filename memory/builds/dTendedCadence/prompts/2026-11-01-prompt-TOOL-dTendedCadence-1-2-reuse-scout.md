**Serves:** journal TOOL-dTendedCadence-1

# gov-reuse-scout handoff — TOOL-dTendedCadence-1

<!-- gov:handoff role=gov-reuse-scout build=dTendedCadence unit=- path=memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=c8f2fa311fa9 -->

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

This handoff is for build `dTendedCadence`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units TOOL-dTendedCadence-4, -14, -15, -16 (Items 4, 14, 15, 16: detectors with owners under maintain.reading-admission refuse-unowned and report-unowned; readings tiered by deviation from their pins under maintain.tiers bands, band edges declared at registration, the log, diagnose (probe.trigger) and act bands; maintain.on-breach's three values file-ask, red-leg and report at maintain.file, the red-leg reading the newest maintenance record offline at Test's leg-pack point as distribution's currency leg reads its own record, report through the notification adapter; node-scoped readings for an act past runtime.act-ceiling, an unrecorded run, a pushed commit missing a required key from the commit-key leg's registration on, and a standing directive in auto-memory not promoted, filed as asks and never a bar or push leg, with maintain.node-readings). Read tools/drift-audit/ (drift_report.py, its signal registry, liveness, the DEAD PROBE path, limits), tools/run-gates/ (gate-legs.json, any leg-pack point), tools/memory-tree/ (ask filing, BACKLOG rows, gen_build_index.py --asks), tools/policy/, and the parent specs for the reading registry, pins, probe.trigger, Plan's triage, the notification adapter, the currency leg, the commit-key leg and runtime.act-ceiling (grep the dWitnessedBar, dRankedPlan, dWellOiledMachine, dShippedRelease and dPlacedRequest specs). Read the packet memory/builds/dTendedCadence/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dTendedCadence/README.md with its BACKLOG.md asks TOOL-dTendedCadence-19 and -20. The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. cl-dClosedLoop-0442, for its row; read the [policies] rows v2:1319-1333 and v2:1389 and the [owed] lines v2:1970 and v2:1990), research-maintain.md, layer-expansions.md, flow-steps.md, layer-flow.md, night-pass.md and night-pass-instruments.md, walk.md, ownership.md, recut.md, and the gap register (the packet's Gaps by line). Parents are SPECCED and NOT built (status DEFERRED): dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders, and their own ancestors (dBoundRoles, dPlacedRequest, dDeclaredLoop, dOrderedCharter, dTotalRecall, dFairHearing and the rest); their specs are under memory/builds/<slug>/spec/. Grep them for the names you need and name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or "no seam fits" with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, the owned nodes (item.maintain.*, policy-key.*, record-kind.*) the unit should name, and the product paths the unit will touch. Then a "Shared interfaces" list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dtendedcadence-e82dac/d0ebabbc-fb8a-4ad6-a3f0-13d769046272/scratchpad/s/b/.

### task:in

the 18 roster specs under memory/builds/dTendedCadence/spec/, the spec audit (spec-audit: 2026-10-21) and its promotions, deviation records, the departures report, deferral of every unit, the close.

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

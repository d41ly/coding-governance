**Serves:** journal TOOL-dLinkedLibrary-1

# gov-reuse-scout handoff — TOOL-dLinkedLibrary-1

<!-- gov:handoff role=gov-reuse-scout build=dLinkedLibrary unit=- path=memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-1-reuse-scout.md role-sha=4750ffbf67ba task-sha=d8436c676d1c -->

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

This handoff is for build `dLinkedLibrary`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout A. Clauses for units TOOL-dLinkedLibrary-1, -2, -3, -5, -6, -13, -22, -24, -25 (Items 1, 2, 3, 5, 6, 13, 22, 24, 25: decisions split by kind with reuse entries as level-3 instruction units under memory/map/conventions/ and the major-decision log; the reuse scout's house index delivered through the card's **Reuse:** field and accepted by re-running aScoutedSeam's benchmark; reuse_lookup.py and its agent retired with every reader rewritten by name and by value (hygiene check 12's §10 arm, unattended's MAP_CLI, the reuse-probed DoD item, M5, a [[retired]] row, memory-recall narrowed); the holds-now and reuse views; the research view and the dated kind: research-return backfill over 72 returns at 1b759b620; decides on every decision row with Decided: trailers read as rows and every bug class naming cause, language and platform; each bug class's gate status derived; the records that contradict the code corrected at their sources). Read memory/DECISIONS.md, memory/gotchas/ (and tools/memory-tree/gotchas.py), memory/map/ (README, features/, baseline.toml), tools/codebase-map/ (reuse_lookup.py, reuse-lookup.agent.md, map_lib.py), tools/memory-recall/, tools/memory-tree/ (check-memory-hygiene.sh checks 12 and 19, gen_build_index.py, backlog.py, tree_lib.py), tools/unattended/ (MAP_CLI, reuse-probed), memory/guides/BUILD-METHOD.md M5, memory/TEMPLATE-SPEC.md, tools/roles/ (the gov-reuse-scout role), and memory/HYGIENE.md (record kinds). Read the packet memory/builds/dLinkedLibrary/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0238', for the paragraph around it, and the [policies] rows the packet's Obligations list by v2 line), the memory-layer, library-round, systems-round, retrofit-round and night-pass records (grep LB-, AN-, RF-, NP-, NT-, FK-, IA-, SA-, P37, P38 and M1c), the ownership record, and the gap register (the packet's Gaps by line). The parent dTotalRecall is specced but NOT built (memory/builds/dTotalRecall/spec/: record find, the record door, the relation graph, README routing, the map's level 0, tools/lib primitives), and so are dDeclaredLoop (the loop kit tools/loop/, the Decided: trailer reader), dOrderedCharter (kinds register, record factory 'core.py new', charter renderer), dFairHearing (scorer factory, aScoutedSeam benchmark held-out cases), dBoundRoles (the experiment kind) and dWitnessedBar; dGroundRules is built and landed (tools/policy/: .governance/policy.toml, catalogue.toml, resolve/readPolicy). Name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dlinkedlibrary-4f9fd9/656f8198-ecf1-4716-a7c6-3c9ec44fadde/scratchpad/s/<your letter>/.

### task:in

25 specs under memory/builds/dLinkedLibrary/spec/, the spec audit the README declares (spec-audit: 2026-10-21) and its promotions, the departures report, the packet re-render, the defer rows.

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

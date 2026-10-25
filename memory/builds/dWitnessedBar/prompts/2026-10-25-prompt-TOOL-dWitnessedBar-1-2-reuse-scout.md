**Serves:** journal TOOL-dWitnessedBar-1

# gov-reuse-scout handoff — TOOL-dWitnessedBar-1

<!-- gov:handoff role=gov-reuse-scout build=dWitnessedBar unit=- path=memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=b936b50e3488 -->

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

This handoff is for build `dWitnessedBar`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units TOOL-dWitnessedBar-9, -10, -11, -12, -19, -22, -24, -28 (the product-test contract with runner adapters under tests.product, tests.landing-levels and tests.without-cadence; the derived pre-commit list and multi-node cost evidence; the gate-leg factory and its conformance gate, every leg declaring the principles it enforces; the leg, check and pack tag namespaces with a tag field beside the free-text name; the purpose field in gate-legs.json reviewed over today's legs; the tests= and enforces= edge fields on legs; the portability leg pack: the line-ending class leg, encoding arms moved in from gate-lint's encoding_posture.py, sh_hygiene.py's legs, the path, temp-file, quoting and bare-shell-name arms, the interpreter-floor arm and the shell-role ledger; a repository's legs from its overlay's leg rows through the leg factory, with pinned patches, instructions.exclude, the canary key set and the shrink-only legacy list). Read tools/gate-legs.json and its readers, tools/run-gates/ (how legs load, the canary, held legs, guards, ceilings), every kit.toml [[gate_leg]] row and the govkit emitter (tools/govkit/: the manifest, subject pins, selfcheck 7h), .githooks/pre-commit (its hand-named list), tools/gate-lint/ (encoding_posture.py, sh_hygiene.py), .gitattributes, tools/lib/ (resolve-python.sh and the interpreter floor), the overlay and adopter manifest files, and any leg-cost evidence (budgets, ceilings, profile_bar). Read the packet memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim; Gaps, Policy keys and Obligations list the gap-register rows and the [policies] rows). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0339', for the paragraph around it and its [policies] rows), the gap register (each gap's line), research-test.md, research-retrofit-a.md, research-retrofit-b.md, retrofit.md, flow-steps.md (its items and checklists, the test.* items), flow-roles.md, flow-roles-adoption.md, layer-flow.md, layer-runtime.md, research-runtime-floor.md, research-python-floor.md, research-testing-anywhere.md, research-observability-trace.md, research-integrations-a.md and -b.md, night-pass.md, night-pass-two.md, away-pass.md, whole-audit.md, systems.md, and the fork rungs in execution-plan.md lines 900-946. Earlier chain builds are specced and some built: dTrueNorth, dGroundRules (the policy file .governance/policy.toml and its reader, the legacy-homes list), dOrderedCharter (kinds register, record factory, tag grammar, compute_coverage and resolve_compare_base moved to tools/lib, H5), dFairHearing (the review harness), dSafePassage (upgrade step rows, the resolver floor), dDeclaredLoop (the loop kit, stages, transitions, flow.wait-ceiling; specced, NOT built). Look under memory/builds/<slug>/spec/ and git log for what landed; name the parent spec id and section a unit would call, never re-spec it, and say whether it is built at HEAD. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dwitnessedbar-d0e46e/871858cc-6dd1-48fc-bfcd-88d1d87e87dc/scratchpad/d1/b/.

### task:in

specs under memory/builds/dWitnessedBar/spec/, review records, departure records, RUN.md, the packet re-render over the moved as-built view, ask rows in other builds' BACKLOG.md, shared renders.

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

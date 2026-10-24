**Serves:** journal TOOL-dWitnessedBar-1

# gov-reuse-scout handoff — TOOL-dWitnessedBar-1

<!-- gov:handoff role=gov-reuse-scout build=dWitnessedBar unit=- path=memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=6f5939cfba8a -->

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

Scout C. Clauses for units TOOL-dWitnessedBar-13, -14, -15, -16, -17, -18, -20, -26, -27 (retrofit's baseline ledger factory in tools/lib, with each population's direction and home and the row-keyed merge driver merge-rows.py and merge-rows.sh; the ratchet leg pack with its populated, seed-laundering, rename and merge rows under retrofit.widen; test.seed at every check's registration under retrofit.unseeded; gov's own 27 registries converted in place onto the ledger (RF-5: 17 shrink-only debt, 2 append-only, 7 declared sets, 1 ceiling) with their readers; the seven record and row pins as keyed populations and the date cutoffs registered as cutoffs; the positional references, IW-1's legacy list and the unpinned facts from dOrderedCharter's keyed lists, and dSafePassage's landed step rows as an append-only population; the legacy-homes list dGroundRules declares converted to a ledger population keyed by conf and key; one bash resolver in tools/lib with its JavaScript twin, replacing every resolve_bash, resolve_launcher, resolve_bash_shell, every loop over bash.exe and bash, and the stop guard's spawnSync('bash', ...); a wrong-shell refusal at every entry point for WSL's bash over a Windows gitdir). Read tools/lib/ (every file), tools/memory-tree/merge-rows.py, merge-rows.sh and merge-rows.test.sh, compute_coverage and resolve_compare_base wherever they live at HEAD, every registry, baseline, waiver and pin file under memory/project/ and the map's baseline.toml, the drift kit, the lexicon's VERB_OFFENDER_PIN, check-memory-hygiene.sh's pins and cutoffs (SPEC_CARRIES_CUTOFF, ROUTED_COMMIT_CUTOFF), tools/govkit/govkit.py's resolve_bash and resolve_shell_argv, profile_bar.resolve_bash, corpus_ids.py, tools/unattended/stop-guard.js, and a git grep over tracked Python and JavaScript for every bash launch site. Use research-retrofit-a.md:26-27 and research-retrofit-b.md for the 27-registry census. Read the packet memory/builds/dWitnessedBar/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim; Gaps, Policy keys and Obligations list the gap-register rows and the [policies] rows). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0339', for the paragraph around it and its [policies] rows), the gap register (each gap's line), research-test.md, research-retrofit-a.md, research-retrofit-b.md, retrofit.md, flow-steps.md (its items and checklists, the test.* items), flow-roles.md, flow-roles-adoption.md, layer-flow.md, layer-runtime.md, research-runtime-floor.md, research-python-floor.md, research-testing-anywhere.md, research-observability-trace.md, research-integrations-a.md and -b.md, night-pass.md, night-pass-two.md, away-pass.md, whole-audit.md, systems.md, and the fork rungs in execution-plan.md lines 900-946. Earlier chain builds are specced and some built: dTrueNorth, dGroundRules (the policy file .governance/policy.toml and its reader, the legacy-homes list), dOrderedCharter (kinds register, record factory, tag grammar, compute_coverage and resolve_compare_base moved to tools/lib, H5), dFairHearing (the review harness), dSafePassage (upgrade step rows, the resolver floor), dDeclaredLoop (the loop kit, stages, transitions, flow.wait-ceiling; specced, NOT built). Look under memory/builds/<slug>/spec/ and git log for what landed; name the parent spec id and section a unit would call, never re-spec it, and say whether it is built at HEAD. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dwitnessedbar-d0e46e/871858cc-6dd1-48fc-bfcd-88d1d87e87dc/scratchpad/d1/c/.

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

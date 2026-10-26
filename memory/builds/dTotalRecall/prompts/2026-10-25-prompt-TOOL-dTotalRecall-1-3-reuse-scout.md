**Serves:** journal TOOL-dTotalRecall-1

# gov-reuse-scout handoff — TOOL-dTotalRecall-1

<!-- gov:handoff role=gov-reuse-scout build=dTotalRecall unit=- path=memory/builds/dTotalRecall/prompts/2026-10-25-prompt-TOOL-dTotalRecall-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=026c88892e5f -->

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

This handoff is for build `dTotalRecall`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units TOOL-dTotalRecall-5, -6, -11, -14, -15, -17, -26 (the slug and id grammar exported once under builds.slug-words/-style/-date with BUILD_SLUG_RE derived; typed relations depends-on, patches, amends, supersedes, implements with the cycle check and pending remote targets; the shape-run kind; the level-0 project map and `gov map` under memory.map-budget and memory.map-overflow; the three-way completeness check and the `map` leg pack; the replay with the map and without, scored through dFairHearing's scorer factory; the atlas under help/atlas/ under help.atlas). Read every slug and id reader the repo has (grep BUILD_SLUG_RE, slug regexes, id regexes across tools/), tools/memory-tree/ (gen_build_index.py and its parents:/edges region, design_lib.py), tools/unattended/ (slug minting and claims), tools/codebase-map/ (gen_map.py, MAP.md, CARDS.md, the map dossiers under memory/map/), memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py and 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py (the design instruments), help/, the regeneration kit and its stages, tools/workflows/tier2-review.js and dFairHearing's scorer factory, tools/gate-legs.json and the leg packs. Read the packet memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim; Owned nodes, Gaps, Policy keys and Obligations list the gap-register rows and the [policies] rows). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0212', for the paragraph around it and its [policies] rows), the gap register (each gap's line), layer-memory.md, memory-plan.md, systems.md, project-map.md, research-project-map-a.md and -b.md, research-memory-structure-a.md and -b.md, research-memory-pockets.md, research-memory-tooling.md, research-memory-map-reuse.md, research-memory-builds.md, research-memory-asks-decisions.md, compaction-recall.md, lexicon.md, atlas-instruments.md, research-final-atlas.md, night-pass.md, night-pass-two.md, away-pass.md, whole-audit.md, retrofit.md, and the fork rungs in the execution plan (grep 'rung'). Earlier chain builds are specced and some built: dTrueNorth (design_lib.py, the binding lines), dGroundRules (the policy file .governance/policy.toml and its reader), dOrderedCharter (kinds register, record factory, tag grammar, compute_coverage and resolve_compare_base moved to tools/lib), dFairHearing (the review harness, the scorer factory), dSafePassage (upgrade step rows, the resolver floor), dDeclaredLoop, dPlacedRequest and dWitnessedBar (specced, NOT built: the loop kit, the probe kind and request records, tools/lib extraction and test.seed). Look under memory/builds/<slug>/spec/ and git log for what landed; name the parent spec id and section a unit would call, never re-spec it, and say whether it is built at HEAD. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dtotalrecall-4bf827/23826028-3fee-42de-ac69-b4090f699257/scratchpad/d1/c/.

### task:in

specs under `memory/builds/dTotalRecall/spec/`, its review and build records, deviation records, ask rows, the shared renders a landing re-renders.

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

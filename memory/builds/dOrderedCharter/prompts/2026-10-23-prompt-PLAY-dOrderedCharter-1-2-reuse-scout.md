**Serves:** journal PLAY-dOrderedCharter-1

# gov-reuse-scout handoff — PLAY-dOrderedCharter-1

<!-- gov:handoff role=gov-reuse-scout build=dOrderedCharter unit=- path=memory/builds/dOrderedCharter/prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=66c53018963b -->

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

This handoff is for build `dOrderedCharter`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units PLAY-dOrderedCharter-7, -10, -16, -17, -18, -19, -22, -24, -25, -26, -28 (the core and principle registry, the namespaced tag system, the layer register and the core-depends-on-no-expansion check, the edges made optional slots, the moved grammar's by-path consumers, the tag grammar and the SQLite tag index, namespace purpose/owner fields, the edge-type registry and edge grammar, gov tag bundle, file:line citations, the shared edge grammar at memory-plan sites). Read tools/memory-tree/ (gen_build_index.py, backlog.py, corpus_ids.py, merge-rows.py, transition_audit.py, gotchas.py, migrate_backlog.py), tools/memory-recall/ (extract.py, recall_conf.py), tools/codebase-map/ (map_lib.py compute_coverage, resolve_compare_base, derive_baseline_additions, drop_touched_exemptions, gen_map.py, map_diff.py, selftest.py), tools/lib/, tools/lexicon/, every kit.toml (requires_if), tools/push-main.sh lexicon call, tools/unattended/unattended.sh drift-audit and runlog calls, tools/unattended/check-verdict-epoch.sh. Also find whether a 'gov' CLI entry point exists today and where a 'gov tag' subcommand would live. Read the packet memory/builds/dOrderedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0031', for the paragraph around it and its [policies] rows), layer-instruction.md, foundations.md, systems.md, layer-library.md, layer-expansions.md, adopter-instructions.md, research-tags-a/b.md, research-instruction-writing-a/b.md, memory-plan.md, night-pass.md, night-pass-two.md, whole-audit.md, execution-plan.md (fork rungs). Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any that a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-10a315/74d36c28-2550-4cf3-9384-4e645df92da1/scratchpad/d1/<your letter>/.

### task:in

the 37 roster specs under memory/builds/dOrderedCharter/spec/, the spec audit rounds and their promotions, deviation records, the departures report, the defer rows, this build's records.

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

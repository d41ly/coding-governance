**Serves:** journal TOOL-dScopedBuild-1

# gov-reuse-scout handoff — TOOL-dScopedBuild-1

<!-- gov:handoff role=gov-reuse-scout build=dScopedBuild unit=- path=memory/builds/dScopedBuild/prompts/2026-11-01-prompt-TOOL-dScopedBuild-2-1-reuse-scout.md role-sha=4750ffbf67ba task-sha=f6939b1f7169 -->

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

This handoff is for build `dScopedBuild`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units TOOL-dScopedBuild-2, -4, -13 (Items 2, 4, 13: built specs frozen, a revision of a spec whose unit has landed refused at the commit with or without a deviation record, red on a planted in-place edit of a landed unit's spec and green on a status-only edit, and every closing-review finding disposed as new units by review.findings (gap-flow-05); the closing review recorded, run as review.build.when says, per-build, per-unit or per-landing, so attended builds carry one as unattended ones do (gap-build-02); the closing review handed, beside its range, each unit's acceptance criteria and the MUST seams its spec carried as rows each finder answers, recorded, gating once a measurement passes (gap-flow-22)). Read tools/workflows/tier2-review.js (its diff-review args, priorFindings, the verifier packet), memory/guides/REVIEW-PROTOCOL.md, the memory-tree hygiene checks on spec revisions and review records (memory/HYGIENE.md checks 5 and 21, check-spec-tokens), the pre-commit hook under .githooks/, the attended /build Skill and the disposal stage of tools/workflows/unattended-build.js, and the parents' specs naming review.findings or other review.* policy keys (grep memory/builds/*/spec for review.findings). Read the packet memory/builds/dScopedBuild/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dScopedBuild/README.md with its BACKLOG.md ask TOOL-dScopedBuild-16. The design sources are under memory/builds/dClosedLoop/build (files named 2026-10-*-build-PLAY-dClosedLoop-1-<name>.md): architecture v2 (grep the clause id for its row and the [policies] rows the packet's Obligations cite by v2 line), the gap register (the packet's Gaps by line), research-build.md, flow.md, flow-steps.md, walk.md and the walk-return-b*.md records (walks B1, B3), retrofit.md with research-retrofit-a/b.md, night-pass.md, night-pass-two.md with its answers, research-scoutedseam-apply.md, final-questions.md (FQ-3), and as-built.md; grep them for the clause's key terms. Parents are SPECCED and NOT built (status DEFERRED): dIndexedDesign, dWitnessedBar, dWellOiledMachine, dFurnishedOrders; dTrueNorth (deviation joins, design_lib.py) is landed. Their specs are under memory/builds/<slug>/spec/. Grep them for the names you need and name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or "no seam fits" with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, the owned nodes (item.build.*, policy-key.*, record-kind.*) the unit should name, and the product paths the unit will touch. Then a "Shared interfaces" list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dscoped-build-bb2a9b/837796a8-5865-4267-b799-0e5da2f1c61e/scratchpad/s/<your letter>/.

### task:in

15 specs under memory/builds/dScopedBuild/spec/, the spec audit the README declares, its promotions, defer rows, departure records and the departures report.

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

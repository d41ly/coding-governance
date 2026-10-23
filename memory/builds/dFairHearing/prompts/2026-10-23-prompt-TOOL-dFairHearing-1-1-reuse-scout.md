**Serves:** journal TOOL-dFairHearing-1

# gov-reuse-scout handoff — TOOL-dFairHearing-1

<!-- gov:handoff role=gov-reuse-scout build=dFairHearing unit=- path=memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-1-reuse-scout.md role-sha=4750ffbf67ba task-sha=afb67dd94cef -->

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

This handoff is for build `dFairHearing`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

For each of dFairHearing's 18 clauses (the packet's Items, memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md), name the existing seam in the review kit the unit should extend (path:line, function or literal), what already exists of the behaviour, and the interface names two or more clauses would share (the preset argument, the lens catalogue's file and shape, the report's disposition grammar, the round-state field, the scorer factory's module). Read tools/workflows/tier2-review.template.js, REVIEW-PROTOCOL.template.md, review_replay.py, check-review-join.sh, check-verifier-fanout.sh, tools/hooks/agent-cap.js review rules, tools/roles/agents/gov-synthesizer.agent.md, tools/memory-tree/gotchas.py, and the design record memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md plus the night-pass-two record where it decides a clause. Return a table, one row per clause, then a Shared interfaces list with one proposed spelling each and the source that already spells it, at most 2500 words.

### task:in

18 specs under memory/builds/dFairHearing/spec/, the spec audit the README's spec-audit: 2026-10-21 opts into, promotions it disposes, deviation records under memory/builds/dFairHearing/build/, the departures report, the close by carry-forward.

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

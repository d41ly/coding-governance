**Serves:** journal TOOL-dCalibratedLens-1

# gov-reuse-scout handoff — TOOL-dCalibratedLens-1

<!-- gov:handoff role=gov-reuse-scout build=dCalibratedLens unit=- path=memory/builds/dCalibratedLens/prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-1-reuse-scout.md role-sha=4750ffbf67ba task-sha=ab342dc32047 -->

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

This handoff is for build `dCalibratedLens`, and names no single unit.
Not supplied, optional: `task:in`, `card:reuse`.

### input:question

For each of dCalibratedLens's 17 clauses (the packet's Items, memory/builds/dCalibratedLens/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md), name the existing seam the unit should extend (path:line, function, literal or record), what already exists of the behaviour at HEAD, and which parent spec (dFairHearing and dTendedCadence are SPECCED BUT UNBUILT; their specs are under memory/builds/<slug>/spec/) or landed build already owns a primitive the clause reads (dDeclaredLoop's breakpoints and review.dispose, dFairHearing's lens catalogue tools/workflows/lenses.toml and scorer factory replay_scorer.py, dSafePassage's step gate, dGroundRules' budgets.enforce and guarded policy command, the trace and journal rows, the observability expansion's cadence steps, review.cost's shape-run rows). Then propose the interface names two or more clauses share: the value ledger's file, row shape and writer; the Loop Review's module, record kind loop-review, its item.loop.* steps (gather, price, propose, file, record, lease) and how its lease keys the period; the lens kind and tag namespace; the policy-key route for review.loop.* and flow.promote; the replay suite's home. Read the design sources under memory/builds/dClosedLoop/build/ where they decide a clause: v2 2026-10-14-...-architecture-v2.md (grep each clause id and owned node), the review system record, the layer-flow, layer-runtime, layer-expansions, the night-pass and night-pass-two records, and the gap register lines the packet's Gaps cite. Return a table, one row per clause, then a Shared interfaces list with one proposed spelling each and the source that already spells it, then any clause whose primitive no landed build or parent spec provides, at most 3000 words. Verify every line number you cite against source.

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

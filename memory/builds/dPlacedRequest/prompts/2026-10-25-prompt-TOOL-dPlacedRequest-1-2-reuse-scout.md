**Serves:** journal TOOL-dPlacedRequest-1

# gov-reuse-scout handoff — TOOL-dPlacedRequest-1

<!-- gov:handoff role=gov-reuse-scout build=dPlacedRequest unit=- path=memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=ebfa4775b6e0 -->

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

This handoff is for build `dPlacedRequest`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units TOOL-dPlacedRequest-2, -3, -4, -5, -9, -10, -14, -19, -21 (the build's orientation card at level 1 kept as a ref per build on the remote, cached and snapshotted, card.follows/store/snapshot, resume.context/partial; the entry step's items entry.orient, entry.place, entry.place-check, entry.place-owner, entry.claim; the placement predicate and placement.check, a disposition for every request; the breakpoint disposition fired through review.trigger; the kickoff manifest's facts as level-2 instruction units the card reads ([pockets]); a build's scenarios chosen at entry.place; the pre-claim budget keyed to the request's content key; a request not yet a build written as a project-level record any node may claim by lease; entry.claim writing a patch or repeat build's derived plan record, patch.ratify). Read skills/session-kickoff/ (SKILL.md, manifest-check.sh --card/--append, the orientation card writer), tools/hooks/ (the card SessionStart entries, scratch-guard.js), tools/unattended/ (--preflight, the prompt path, asks), tools/memory-tree/ (gen_build_index.py, the scaffold for build folders, asks/BACKLOG), memory/guides/SESSION-KICKOFF.md, tools/roles/ (orientation scout role, handoff.py), and dDeclaredLoop's specs on scenarios, review.trigger and the item registry. Read the packet memory/builds/dPlacedRequest/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys, Obligations and Later builds bind them). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0120', for the paragraph around it and its [policies] rows), coordination.md, orientation.md and its research-orientation-* records, flow-steps.md (its entry and probe items, [rules], [probe]), flow-roles.md, layer-runtime.md, layer-memory.md, memory-plan.md ([pockets], [sites]), night-pass.md, night-pass-two.md (NT-*), research-scenarios-design.md, research-exec-coordination.md, whole-audit.md (C2-F*, A1-F5), and the fork rungs in execution-plan.md lines 900-946. The parent dDeclaredLoop is specced but NOT built (memory/builds/dDeclaredLoop/spec/, 100 units: the loop kit tools/loop/, the transition record, stage claims, the review program's review.trigger, flow.rework-budget, flow.wait-ceiling, scenarios). Its own parents dGroundRules (the policy file .governance/policy.toml and its reader), dOrderedCharter (kinds register, record factory, tag grammar), dFairHearing (review harness) and dSafePassage are specced, not built: name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function or literal) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dplacedrequest-f41432/a4a72c24-4423-4b1e-9176-5acec5cc094f/scratchpad/s/<your letter>/.

### task:in

the 21 unit specs under memory/builds/dPlacedRequest/spec/, the spec audit the README declares, the audit's promotions, the defer rows, the departures report, RUN.md and the shared renders.

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

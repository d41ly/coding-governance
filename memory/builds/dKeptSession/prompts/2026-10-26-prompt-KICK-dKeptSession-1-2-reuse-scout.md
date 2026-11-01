**Serves:** journal KICK-dKeptSession-1

# gov-reuse-scout handoff — KICK-dKeptSession-1

<!-- gov:handoff role=gov-reuse-scout build=dKeptSession unit=- path=memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=1bafa460193c -->

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

This handoff is for build `dKeptSession`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units KICK-dKeptSession-5, -6, -10, -21, -22, -23, -24, -25, -27, -28 (the mailbox per build, one append-only ref per writing session refs/gov/mail/<slug>/<fleet tag>/<session>, closed message kinds, written only through the coordination verbs, transitions refused while a message is unanswered until flow.wait-ceiling; live delivery where the harness has it; mailbox.reads at every item boundary with the intake kind; mailbox.notice and mailbox.fetch-seconds with a bounded fetch and a tool-call hook; deterministic message ids and the duplicate check across per-session refs; every mail write appended to the change feed; a waiting message's deadline by the declared clock leases use; mailbox.answer by the owning role, the asker's declared default as stand-in until next lands, leases.renewal: progress; session sequence numbers and content keys on confirmed/changed; recipients naming a node by fleet tag or the whole project). Read dPlacedRequest's specs for refs/gov/*, build_gov_commit, write_gov_ref, the change feed, leases and their declared clock; tools/unattended/unattended.sh's run claims (grep 'refs/gov', 'update-ref', RUN_CLAIMS); tools/lib/; tools/hooks/ (the PreToolUse hooks, for the tool-call notice); tools/playbook/fleet.toml (fleet tags); and dDeclaredLoop's transition record and item boundary specs. Read the packet memory/builds/dKeptSession/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys, Obligations and Later builds bind them). The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0143', for the paragraph around it and the [policies] rows the packet's Obligations list by v2 line), coordination.md, orientation.md and its research-orientation-* records, compaction and runtime records (grep CX-1, RT-1), flow-roles.md (FR-*), flow-interactions (FI-*), night-pass.md, night-pass-two.md (NT-*), the whole-audit (C2-F*, A2-F*, CS4-F1), the gap register (the packet's Gaps by line) and the fork rungs in execution-plan.md lines 900-946. The parents are specced but NOT built: dDeclaredLoop (memory/builds/dDeclaredLoop/spec/: the loop kit tools/loop/, stage tags, item registry, transition record, scenarios, flow.wait-ceiling, flow.rework-budget, next) and dPlacedRequest (memory/builds/dPlacedRequest/spec/: leases refs/gov/leases, build_gov_commit, write_gov_ref, the change feed gov-feed.log, the build card ref refs/gov/builds/<slug>/card, resume.context, placement dispositions). Their own parents dGroundRules (the policy file .governance/policy.toml, tools/policy/catalogue.toml, the one reader read_policy_key/resolve with its preset no-op branch), dOrderedCharter (kinds register, record factory, tag grammar, charter renderer), dFairHearing and dSafePassage are specced, not built: name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dkeptsession-dd0ede/7b83d341-b894-474a-9793-b9a2975dc79b/scratchpad/s/<your letter>/.

### task:in

specs, reviews, deviation records and run records under memory/builds/dKeptSession/; ask rows in other builds' BACKLOG.md; the shared renders.

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

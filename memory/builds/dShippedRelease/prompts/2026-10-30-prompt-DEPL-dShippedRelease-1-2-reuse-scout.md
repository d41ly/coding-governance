**Serves:** journal DEPL-dShippedRelease-1

# gov-reuse-scout handoff — DEPL-dShippedRelease-1

<!-- gov:handoff role=gov-reuse-scout build=dShippedRelease unit=- path=memory/builds/dShippedRelease/prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=f832d40219d8 -->

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

This handoff is for build `dShippedRelease`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units DEPL-dShippedRelease-11, -12, -27, -30 (Items 11, 12, 27, 30): deps.landing; the landing queue with landing.order and the landing-turn ref taken by compare-and-swap; carries on the landing record over <current default>..HEAD --no-merges, the landing native-id class, a publication recorded per (SHA, artifact environment), commits.squash's three values, Codex install targets with their trust step; a patch build raised by a landing, keyed by (default-branch-red, landed SHA), the shared rework budget across a chain, the draw on a closed root re-acquiring the terminal lease, the keep-waiting answers counted. Read tools/push-main.sh, .githooks/pre-push, tools/run-gates/ (the turnstile), tools/unattended/ claims (refs/gov/runs), tools/lib/, tools/govkit/ (install targets), the dWellOiledMachine specs for leases, epochs, tombstones, the rework budget, intake and the entry-point table, the dDeclaredLoop specs for owner items, and any spec defining leases.queued-claim-days or cl-0134. Read the packet memory/builds/dShippedRelease/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dShippedRelease/README.md with its BACKLOG.md ask DEPL-dShippedRelease-32. Design sources are under memory/builds/dClosedLoop/build (B/): architecture v2 B/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md (grep each clause id and each named item), the gap register B/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md at the lines the packet's Gaps section names, B/2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md, B/2026-10-16-build-PLAY-dClosedLoop-1-research-distribution-a.md and -b.md, B/2026-10-16-build-PLAY-dClosedLoop-1-research-integrations-a.md and -b.md, B/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md, B/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md and B/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md, plus whichever record a clause cites (P<n>, FK-, FA-, FM, DA-M, AP-, NP-, PM-, WK-, K1). The parent builds dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary and dFurnishedOrders, and dSafePassage, dOrderedCharter, dDeclaredLoop and dFairHearing, are SPECCED AND DEFERRED, none built: their specs are under memory/builds/<slug>/spec/ and their surfaces do not exist at HEAD, so cite each by spec id and section and say it is not built. Return, in this order: (1) one row per unit: the seam to extend with verified path:line at HEAD, what already exists, the design lines that decide it, the owned nodes it should carry (each node of the packet's Owned nodes list your group touches, with its proposed owner unit), the policy keys it should own and whether each already has a tools/policy/catalogue.toml row, and the product paths it would touch; (2) where records and source disagree, numbered: every claim in the clause or its design record that source shows wrong or stale, with the evidence; (3) the interfaces your units share with each other and with other groups, spelled as proposed names; (4) the order constraints between your units and on parents, and which parent surfaces each unit needs; (5) the forks you can see, and which you could not settle from source. Verify every line number by reading it. Write nothing in the repository; temp files go under the scratch path your harness names.

### task:in

the packet re-render when only derived inputs moved, reuse scouts, one spec brief, 31 specs, the spec audit and its promotions, deviation and departure records, ask rows, RUN.md.

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

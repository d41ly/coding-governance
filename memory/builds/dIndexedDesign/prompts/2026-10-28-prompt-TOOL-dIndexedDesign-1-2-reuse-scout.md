**Serves:** journal TOOL-dIndexedDesign-1

# gov-reuse-scout handoff — TOOL-dIndexedDesign-1

<!-- gov:handoff role=gov-reuse-scout build=dIndexedDesign unit=- path=memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-2-reuse-scout.md role-sha=4750ffbf67ba task-sha=dbf743fc7875 -->

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

This handoff is for build `dIndexedDesign`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout B. Clauses for units TOOL-dIndexedDesign-4, -5, -13, -14 (Items 4, 5, 13, 14: reuse and alternatives backed by recorded probes (gap-design-05, -06: the reuse audit's outcome is prose, rejected candidates unchecked); the research harness built on dBoundRoles' experiment shape (gap-design-07); the reuse scout's return under aScoutedSeam's M1c contract — needs and a concrete sketch before the search, anchors resolved, a convention census, at most twelve seams and five MUSTs, a MUST defined as an existing implementation new code would duplicate, the unmet needs, MUST and SHOULD seams handed on as rows (gap-design-11, NT-10); the return also naming at most five bug classes by intent from the catalogue's one-line index, armed only once a replay over closed code scores above the anchor ranking's top five with precision at least 20%, retired unarmed otherwise (NT-26)). Read .claude/agents/gov-reuse-scout.md and tools/roles/ (the role's source, its rendered prompt and handoff.py), tools/codebase-map/ (reuse_lookup.py, reuse-lookup.agent.md), tools/memory-recall/, tools/memory-tree/gotchas.py and memory/gotchas/ (the catalogue and any one-line index), tools/memory-tree/check-memory-hygiene.sh check 12 (the §10 arm) and its SPEC10_EVIDENCE_CUTOFF, memory/TEMPLATE-SPEC.md §10, memory/guides/BUILD-METHOD.md M5 and M12, memory/builds/aScoutedSeam/ (M1c and its benchmark), dBoundRoles' experiment-kind spec, and dLinkedLibrary's house-index, research-view and scout specs (grep their spec/ folders). Read the packet memory/builds/dIndexedDesign/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dIndexedDesign/README.md with its BACKLOG.md asks TOOL-dIndexedDesign-18 and -19. The design sources are under memory/builds/dClosedLoop/build: architecture v2 (grep the clause id, e.g. 'cl-dClosedLoop-0383', for the paragraph around it; grep 'item.design.' and 'record-kind.' for the owned nodes' rows, and read the [policies] rows the packet's Obligations list by v2 line), the night-pass instruments and night pass two records, the walk and walk returns, the ownership record, the flow-steps and research-flow-items records, and the gap register (the packet's Gaps by line). Parents are specced and NOT built: dDeclaredLoop (the loop kit tools/loop/, stage exits, AF-1, policy-key readers), dTotalRecall (record kinds, the stream-plan kind, record find), dKeptSession, dBoundRoles (the experiment kind, role agents), dLinkedLibrary (the reuse scout's house index, decision rows, the research view) — their specs are under memory/builds/<slug>/spec/; name the parent spec id and section a unit would call, never re-spec it. dTrueNorth and dGroundRules are BUILT and landed: tools/memory-tree/design_lib.py (binding lines), tools/check-spec-tokens.py (the carries join), tools/policy/ (.governance/policy.toml, catalogue.toml, resolve/readPolicy). Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or 'no seam fits' with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, the owned nodes (item.design.*, policy-key.design.*, record-kind.*) the unit should name, and the product paths the unit will touch. Then a 'Shared interfaces' list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dindexeddesign-516d37/75965d52-bd39-4234-bbfb-fb440f651df7/scratchpad/s/<your letter>/.

### task:in

16 roster specs (TOOL-dIndexedDesign-1..16) under memory/builds/dIndexedDesign/spec/, the spec audit the README declares (spec-audit: 2026-10-21) with M4 promotions, the departures report, the packet re-render, and asks filed in this build's BACKLOG.md.

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

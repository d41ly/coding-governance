**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-22-reuse-scout.md role-sha=4750ffbf67ba task-sha=47b063de97ed -->

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

This handoff is for build `aScoutedSeam`, and names no single unit.
Not supplied, optional: `task:in`, `card:reuse`.

### input:question

You are the REUSE REVIEWER for a diff about to land. This task block OVERRIDES your role's pointer to reuse-lookup.agent.md. Your job is a COVERAGE job: account for EVERY unit the diff adds, one verdict per unit, so that no duplicate goes unexamined because another was found first.

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c19/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c19.diff (a unified diff with a --stat header; commit subject: "TOOL-aRuledFrontispiece-1: the build README's generated surface"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. PLAN_OPEN  [py-constant · tools/memory-tree/gen_build_index.py]
U2. PLAN_CLOSE  [py-constant · tools/memory-tree/gen_build_index.py]
U3. GEN_REGIONS  [py-constant · tools/memory-tree/gen_build_index.py]
U4. ORDER_RE  [py-constant · tools/memory-tree/gen_build_index.py]
U5. -347,6 +374,12: # Every tracked record, for the document-inventory region. The filenam  [hunk · tools/memory-tree/gen_build_index.py]
U6. render_order  [def · tools/memory-tree/gen_build_index.py]
U7. render_edges  [def · tools/memory-tree/gen_build_index.py]
U8. render_docs  [def · tools/memory-tree/gen_build_index.py]
U9. REGION_RENDERERS  [py-constant · tools/memory-tree/gen_build_index.py]
U10. apply_region  [def · tools/memory-tree/gen_build_index.py]
U11. -507,16 +620,19: opens = [i for i, l in enumerate(lines) if _is(l, mark_open)]  [hunk · tools/memory-tree/gen_build_index.py]
U12. _marker_index  [def · tools/memory-tree/gen_build_index.py]
U13. slot_violations  [def · tools/memory-tree/gen_build_index.py]
U14. insert_region  [def · tools/memory-tree/gen_build_index.py]
U15. plan  [def · tools/memory-tree/gen_build_index.py]
U16. do_check_format  [def · tools/memory-tree/gen_build_index.py]
U17. -694,7 +926,10: # The message now NAMES the pair. With four registered regions, "expec  [hunk · tools/memory-tree/gen_build_index.py]
U18. -882,6 +1117,77: # ---- TOOL-aRuledFrontispiece-1: the slot contract, region creation,   [hunk · tools/memory-tree/gen_build_index.py]

FOR EACH LISTED UNIT, in order, return one row:
- unit: its U-number and name;
- nearest: the closest EXISTING implementation in the tree of the same need, as path::symbol, found by searching the CONCEPT with synonyms across all file types, or `none` with what you searched;
- verdict: `duplicate` (the existing one already covers the need and is reachable from the new code), `should-extend` (the existing one covers most of it and should have been extended), `new` (genuinely new capability) or `not-a-unit` (a lister artefact);
- why: one line.
Then ADD rows for duplicated units the lister cannot see: a repeated literal value, a hardcoded design value beside an existing token, a copied function body under a new name, a JSON tree node re-built beside an existing one. Mark each added row `added: true`.

Do not stop at the first duplicate. A review that leaves a listed unit without a row is incomplete.

RETURN CONTRACT. End your reply with ONE ```json block holding an object with keys: rows (every row above), seams, verdict. seams: one entry per `duplicate` or `should-extend` row, each with repo, path (repo-relative, the EXISTING seam), symbol, binding (MUST for duplicate, SHOULD for should-extend), new_code (what the diff added), how (how the diff should use the seam instead), evidence (file:line). verdict: `duplicates-found` or `clean`.

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

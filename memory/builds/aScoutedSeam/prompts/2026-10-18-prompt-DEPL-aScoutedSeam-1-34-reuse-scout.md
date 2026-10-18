**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-34-reuse-scout.md role-sha=4750ffbf67ba task-sha=56c44b1d45a9 -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c09/tree
HOST CORE TREE (incms, the platform this package installs into): C:/Users/daily-agent/AppData/Local/Temp/rsb/c09/incms

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c09.diff (a unified diff with a --stat header; commit subject: "feat(package): PKG-dLimnedTriage-1 — the medical intake gets a stage, a topbar and a card"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. bg  [json-key · package/nicocares-v3/blocks/descriptors.json]
U2. logo  [json-key · package/nicocares-v3/blocks/descriptors.json]
U3. nc-mi-stage  [json-key · package/nicocares-v3/blocks/descriptors.json]
U4. nc-mi-bg  [json-key · package/nicocares-v3/blocks/descriptors.json]
U5. nc-mi-topbar  [json-key · package/nicocares-v3/blocks/descriptors.json]
U6. nc-mi-content  [json-key · package/nicocares-v3/blocks/descriptors.json]
U7. nc-mi nc-mi-col  [json-key · package/nicocares-v3/blocks/descriptors.json]
U8. nc-mi-card  [json-key · package/nicocares-v3/blocks/descriptors.json]
U9. nc-mi-head  [json-key · package/nicocares-v3/blocks/descriptors.json]
U10. Text  [json-key · package/nicocares-v3/blocks/descriptors.json]
U11. Heading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U12. nc-mi-panel  [json-key · package/nicocares-v3/blocks/descriptors.json]
U13. nc-mi-complete  [json-key · package/nicocares-v3/blocks/descriptors.json]
U14. firstName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U15. lastName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U16. street  [json-key · package/nicocares-v3/blocks/descriptors.json]
U17. apt  [json-key · package/nicocares-v3/blocks/descriptors.json]
U18. city  [json-key · package/nicocares-v3/blocks/descriptors.json]
U19. state  [json-key · package/nicocares-v3/blocks/descriptors.json]
U20. zipCode  [json-key · package/nicocares-v3/blocks/descriptors.json]
U21. gender  [json-key · package/nicocares-v3/blocks/descriptors.json]
U22. currentMedication  [json-key · package/nicocares-v3/blocks/descriptors.json]
U23. medicationName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U24. weightChange  [json-key · package/nicocares-v3/blocks/descriptors.json]
U25. weightGoal  [json-key · package/nicocares-v3/blocks/descriptors.json]
U26. waterIntake  [json-key · package/nicocares-v3/blocks/descriptors.json]
U27. appetiteSuppression  [json-key · package/nicocares-v3/blocks/descriptors.json]
U28. sideEffects  [json-key · package/nicocares-v3/blocks/descriptors.json]
U29. majorSideEffects  [json-key · package/nicocares-v3/blocks/descriptors.json]
U30. allergy  [json-key · package/nicocares-v3/blocks/descriptors.json]
U31. allergyMedications  [json-key · package/nicocares-v3/blocks/descriptors.json]
U32. medicationsOrSupplements  [json-key · package/nicocares-v3/blocks/descriptors.json]
U33. medicationsOrSupplementsDetails  [json-key · package/nicocares-v3/blocks/descriptors.json]
U34. priorConditions  [json-key · package/nicocares-v3/blocks/descriptors.json]
U35. priorConditionsDetails  [json-key · package/nicocares-v3/blocks/descriptors.json]
U36. knowAbout  [json-key · package/nicocares-v3/blocks/descriptors.json]
U37. nc-mi-form  [json-key · package/nicocares-v3/blocks/descriptors.json]
U38. nc-mi-done  [json-key · package/nicocares-v3/blocks/descriptors.json]
U39. nc-mi-id  [json-key · package/nicocares-v3/blocks/descriptors.json]
U40. nc-mi-id-resume  [json-key · package/nicocares-v3/blocks/descriptors.json]
U41. nc-mi-idform  [json-key · package/nicocares-v3/blocks/descriptors.json]
U42. photo  [json-key · package/nicocares-v3/blocks/descriptors.json]
U43. nc-mi-disclosure  [json-key · package/nicocares-v3/blocks/descriptors.json]

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

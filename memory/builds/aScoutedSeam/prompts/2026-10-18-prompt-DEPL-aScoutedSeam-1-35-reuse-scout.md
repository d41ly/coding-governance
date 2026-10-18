**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-35-reuse-scout.md role-sha=4750ffbf67ba task-sha=00b465c1ddc6 -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c08/tree
HOST CORE TREE (incms, the platform this package installs into): C:/Users/daily-agent/AppData/Local/Temp/rsb/c08/incms

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c08.diff (a unified diff with a --stat header; commit subject: "feat(package): the post-payment medical intake, end to end"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. medical-intake  [json-key · package/nicocares-v3/account-layouts/layouts.json]
U2. -24605,19 +24605,19: "label": "1 month \u2014 try it and see"  [hunk · package/nicocares-v3/blocks/descriptors.json]
U3. medical-intake  [json-key · package/nicocares-v3/blocks/descriptors.json]
U4. eyebrow  [json-key · package/nicocares-v3/blocks/descriptors.json]
U5. heading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U6. lede  [json-key · package/nicocares-v3/blocks/descriptors.json]
U7. disclosure  [json-key · package/nicocares-v3/blocks/descriptors.json]
U8. doneHeading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U9. doneLine  [json-key · package/nicocares-v3/blocks/descriptors.json]
U10. completeHeading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U11. completeLine  [json-key · package/nicocares-v3/blocks/descriptors.json]
U12. accountLabel  [json-key · package/nicocares-v3/blocks/descriptors.json]
U13. accountHref  [json-key · package/nicocares-v3/blocks/descriptors.json]
U14. idHeading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U15. idLede  [json-key · package/nicocares-v3/blocks/descriptors.json]
U16. idDoneLine  [json-key · package/nicocares-v3/blocks/descriptors.json]
U17. idHeldLine  [json-key · package/nicocares-v3/blocks/descriptors.json]
U18. nc-mi  [json-key · package/nicocares-v3/blocks/descriptors.json]
U19. nc-mi-head  [json-key · package/nicocares-v3/blocks/descriptors.json]
U20. Text  [json-key · package/nicocares-v3/blocks/descriptors.json]
U21. Heading  [json-key · package/nicocares-v3/blocks/descriptors.json]
U22. nc-mi-panel  [json-key · package/nicocares-v3/blocks/descriptors.json]
U23. nc-mi-complete  [json-key · package/nicocares-v3/blocks/descriptors.json]
U24. firstName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U25. lastName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U26. street  [json-key · package/nicocares-v3/blocks/descriptors.json]
U27. apt  [json-key · package/nicocares-v3/blocks/descriptors.json]
U28. city  [json-key · package/nicocares-v3/blocks/descriptors.json]
U29. state  [json-key · package/nicocares-v3/blocks/descriptors.json]
U30. zipCode  [json-key · package/nicocares-v3/blocks/descriptors.json]
U31. gender  [json-key · package/nicocares-v3/blocks/descriptors.json]
U32. currentMedication  [json-key · package/nicocares-v3/blocks/descriptors.json]
U33. medicationName  [json-key · package/nicocares-v3/blocks/descriptors.json]
U34. weightChange  [json-key · package/nicocares-v3/blocks/descriptors.json]
U35. weightGoal  [json-key · package/nicocares-v3/blocks/descriptors.json]
U36. waterIntake  [json-key · package/nicocares-v3/blocks/descriptors.json]
U37. appetiteSuppression  [json-key · package/nicocares-v3/blocks/descriptors.json]
U38. sideEffects  [json-key · package/nicocares-v3/blocks/descriptors.json]
U39. majorSideEffects  [json-key · package/nicocares-v3/blocks/descriptors.json]
U40. allergy  [json-key · package/nicocares-v3/blocks/descriptors.json]
U41. allergyMedications  [json-key · package/nicocares-v3/blocks/descriptors.json]
U42. medicationsOrSupplements  [json-key · package/nicocares-v3/blocks/descriptors.json]
U43. medicationsOrSupplementsDetails  [json-key · package/nicocares-v3/blocks/descriptors.json]
U44. priorConditions  [json-key · package/nicocares-v3/blocks/descriptors.json]
U45. priorConditionsDetails  [json-key · package/nicocares-v3/blocks/descriptors.json]
U46. knowAbout  [json-key · package/nicocares-v3/blocks/descriptors.json]
U47. nc-mi-form  [json-key · package/nicocares-v3/blocks/descriptors.json]
U48. nc-mi-done  [json-key · package/nicocares-v3/blocks/descriptors.json]
U49. nc-mi-id  [json-key · package/nicocares-v3/blocks/descriptors.json]
U50. nc-mi-idform  [json-key · package/nicocares-v3/blocks/descriptors.json]
U51. photo  [json-key · package/nicocares-v3/blocks/descriptors.json]
U52. medical-intake  [json-key · package/nicocares-v3/content/pages/27-medical-intake.json]
U53. sign-in-panel  [json-key · package/nicocares-v3/content/pages/27-medical-intake.json]
U54. -7,7 +7,28: {  [hunk · package/nicocares-v3/dashboard/widgets.json]
U55. -18,9 +39,18: {  [hunk · package/nicocares-v3/dashboard/widgets.json]
U56. -31,7 +61,10: {  [hunk · package/nicocares-v3/dashboard/widgets.json]
U57. -40,10 +73,16: "body": "Your record shows the email on your account, your intake stat  [hunk · package/nicocares-v3/dashboard/widgets.json]
U58. -54,7 +93,10: {  [hunk · package/nicocares-v3/dashboard/widgets.json]
U59. -193,6 +193,22: {  [hunk · package/nicocares-v3/plugin.json]
U60. EXPECTED_ACCOUNT_LAYOUT_ROUTES  [py-constant · scripts/check_package_refs.py]
... and 5 more units the lister found past its cap of 60; cover them as you read the diff.

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

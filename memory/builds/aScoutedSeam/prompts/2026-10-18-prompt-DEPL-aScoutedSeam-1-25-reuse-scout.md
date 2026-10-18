**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-25-reuse-scout.md role-sha=4750ffbf67ba task-sha=93c3c18e986f -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c01/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c01.diff (a unified diff with a --stat header; commit subject: "feat(blocks,theme): O-1 per-section/-block decor pattern/texture layer (Tier-2)"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. hasOwnDecor  [const · packages/blocks/src/registry.tsx]
U2. -21,7 +22,12: return (  [hunk · packages/blocks/src/renderWrappers.tsx]
U3. Comp  [const · packages/blocks/src/renderWrappers.tsx]
U4. withBackground  [def · packages/blocks/src/renderWrappers.tsx]
U5. -321,6 +321,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U6. -412,6 +457,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U7. -699,6 +753,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U8. -814,6 +913,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U9. -1389,6 +1497,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U10. -1496,6 +1649,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U11. -1552,6 +1714,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U12. -1664,6 +1871,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U13. -3984,6 +4200,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U14. -4157,6 +4418,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U15. -4648,6 +4918,51: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U16. -4762,6 +5077,15: "decor": {  [hunk · packages/blocks/src/schema/blocks.capabilities.json]
U17. -1,5 +1,12: import {  [hunk · packages/blocks/src/sections/CTA.tsx]
U18. Copy  [def · packages/blocks/src/sections/CTA.tsx]
U19. BandBody  [def · packages/blocks/src/sections/CTA.tsx]
U20. copyClass  [const · packages/blocks/src/sections/CTA.tsx]
U21. tileFg  [const · packages/blocks/src/sections/CTA.tsx]
U22. Split  [def · packages/blocks/src/sections/CTA.tsx]
U23. label  [field · packages/blocks/src/sections/CTA.tsx]
U24. href  [field · packages/blocks/src/sections/CTA.tsx]
U25. -197,11 +283,19: if (  [hunk · packages/blocks/src/sections/CTA.tsx]
U26. -209,8 +303,18: band: {  [hunk · packages/blocks/src/sections/CTA.tsx]
U27. heading  [field · packages/blocks/src/sections/CTA.tsx]
U28. -240,8 +350,10: bodyHtml:  [hunk · packages/blocks/src/sections/CTA.tsx]
U29. Table  [def · packages/blocks/src/sections/Comparison.tsx]
U30. -50,7 +62,15: <th  [hunk · packages/blocks/src/sections/Comparison.tsx]
U31. -61,11 +81,21: <th  [hunk · packages/blocks/src/sections/Comparison.tsx]
U32. Cards  [def · packages/blocks/src/sections/Comparison.tsx]
U33. -132,7 +199,10: values: {  [hunk · packages/blocks/src/sections/Comparison.tsx]
U34. Answer  [def · packages/blocks/src/sections/FAQ.tsx]
U35. -44,7 +58,14: blobs={[  [hunk · packages/blocks/src/sections/FAQ.tsx]
U36. -58,12 +79,30: <span className="font-semibold text-[var(--block-fg)]">  [hunk · packages/blocks/src/sections/FAQ.tsx]
U37. -81,9 +120,18: <div  [hunk · packages/blocks/src/sections/FAQ.tsx]
U38. -99,8 +147,14: <h3 className="font-display font-semibold text-[var(--block-fg)]">  [hunk · packages/blocks/src/sections/FAQ.tsx]
U39. -111,15 +165,32: {  [hunk · packages/blocks/src/sections/FAQ.tsx]
U40. needs  [const · packages/blocks/src/sections/FAQ.tsx]
U41. NumberedCards  [def · packages/blocks/src/sections/ProcessSteps.tsx]
U42. -50,8 +69,12: <h3 className="mt-5 font-display text-lg font-semibold text-[var(--blo  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U43. -66,21 +89,44: {  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U44. -94,15 +140,25: <div  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U45. -115,7 +171,12: <SectionHeading  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U46. -128,8 +189,12: <h3 className="font-display font-semibold text-[var(--block-fg)]">  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U47. -144,12 +209,26: <div  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U48. -170,14 +249,27: {  [hunk · packages/blocks/src/sections/ProcessSteps.tsx]
U49. -15,7 +15,12: import {  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U50. ReviewCards  [def · packages/blocks/src/sections/SocialProof.tsx]
U51. -94,20 +118,34: <span className="text-2xl font-semibold text-[var(--block-fg)]">  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U52. StatBandDesign  [def · packages/blocks/src/sections/SocialProof.tsx]
U53. JourneyCardsDesign  [def · packages/blocks/src/sections/SocialProof.tsx]
U54. -158,14 +231,18: <p className="font-semibold text-[var(--block-fg)]">  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U55. -183,9 +260,18: blobs={[  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U56. -196,7 +282,10: <div  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U57. -224,11 +313,21: blobs={[  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U58. -239,9 +338,17: {author ? (  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U59. -295,9 +403,27: {  [hunk · packages/blocks/src/sections/SocialProof.tsx]
U60. -44,16 +44,33: blobs={[  [hunk · packages/blocks/src/sections/ValueProps.tsx]
... and 48 more units the lister found past its cap of 60; cover them as you read the diff.

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

**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-27-reuse-scout.md role-sha=4750ffbf67ba task-sha=da4599fa8c56 -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c05/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c05.diff (a unified diff with a --stat header; commit subject: "feat(email): U5 P1 — the email block family, the table renderer and the theme palette"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. -167,11 +167,17: // email/EmailBlockView.tsx: the ONE canvas host for email block outpu  [hunk · packages/blocks/eslint.config.js]
U2. _BLOCKS_ABI_SEMVER  [const · packages/blocks/src/blocksAbi.ts]
U3. -87,8 +87,13: *  declare `>=1.1.0`, which is exactly what the shipped demo now does.  [hunk · packages/blocks/src/blocksAbi.ts]
U4. -73,6 +74,12: /** The EMAIL family (ARCH-dCandidPostmark-5 / S16) — a sibling array,  [hunk · packages/blocks/src/capabilities.ts]
U5. -113,6 +120,11: // `src` (ARCH-dCandidPostmark-5): the email family's `EmailImage.src`  [hunk · packages/blocks/src/capabilities.ts]
U6. -267,6 +279,14: // S16 — the EMAIL family as a SIBLING array, mirroring the choice alr  [hunk · packages/blocks/src/capabilities.ts]
U7. EmailBlockView  [def · packages/blocks/src/email/EmailBlockView.tsx]
U8. palette  [const · packages/blocks/src/email/EmailBlockView.tsx]
U9. label  [field · packages/blocks/src/email/blocks/EmailButton.tsx]
U10. href  [field · packages/blocks/src/email/blocks/EmailButton.tsx]
U11. col1  [field · packages/blocks/src/email/blocks/EmailColumns.tsx]
U12. col2  [field · packages/blocks/src/email/blocks/EmailColumns.tsx]
U13. col3  [field · packages/blocks/src/email/blocks/EmailColumns.tsx]
U14. p  [const · packages/blocks/src/email/blocks/EmailColumns.tsx]
U15. count  [const · packages/blocks/src/email/blocks/EmailColumns.tsx]
U16. width  [const · packages/blocks/src/email/blocks/EmailColumns.tsx]
U17. -0,0 +1,18: import type { BlockDef } from "../../types";  [hunk · packages/blocks/src/email/blocks/EmailDivider.tsx]
U18. text  [field · packages/blocks/src/email/blocks/EmailHeading.tsx]
U19. src  [field · packages/blocks/src/email/blocks/EmailImage.tsx]
U20. alt  [field · packages/blocks/src/email/blocks/EmailImage.tsx]
U21. width  [field · packages/blocks/src/email/blocks/EmailImage.tsx]
U22. href  [field · packages/blocks/src/email/blocks/EmailImage.tsx]
U23. -0,0 +1,26: import type { BlockDef } from "../../types";  [hunk · packages/blocks/src/email/blocks/EmailRawHtml.tsx]
U24. -0,0 +1,18: import type { BlockDef } from "../../types";  [hunk · packages/blocks/src/email/blocks/EmailSpacer.tsx]
U25. -0,0 +1,20: import { richTextField } from "../../fields/RichTextField";  [hunk · packages/blocks/src/email/blocks/EmailText.tsx]
U26. -0,0 +1,20: import type { BlockDef } from "../../types";  [hunk · packages/blocks/src/email/blocks/EmailUnsubscribe.tsx]
U27. EMAIL_COLUMN_SLOTS  [const · packages/blocks/src/email/columns.ts]
U28. columnCount  [def · packages/blocks/src/email/columns.ts]
U29. n  [const · packages/blocks/src/email/columns.ts]
U30. columnCellWidth  [def · packages/blocks/src/email/columns.ts]
U31. columnCellStyle  [const · packages/blocks/src/email/columns.ts]
U32. -0,0 +1,26: /**  [hunk · packages/blocks/src/email/index.ts]
U33. -0,0 +1,29: /**  [hunk · packages/blocks/src/email/manifest.email.ts]
U34. EmailPaletteContext  [const · packages/blocks/src/email/paletteContext.tsx]
U35. EmailPaletteProvider  [def · packages/blocks/src/email/paletteContext.tsx]
U36. useEmailPalette  [def · packages/blocks/src/email/paletteContext.tsx]
U37. palette  [const · packages/blocks/src/email/paletteContext.tsx]
U38. ADMIN_ONLY_EMAIL_BLOCKS  [const · packages/blocks/src/email/registry.tsx]
U39. EMAIL_LINK_ROLES  [const · packages/blocks/src/email/render.ts]
U40. EMAIL_CONTENT_WIDTH  [const · packages/blocks/src/email/render.ts]
U41. LINK_REL  [const · packages/blocks/src/email/render.ts]
U42. FONT_STACK  [const · packages/blocks/src/email/render.ts]
U43. asString  [const · packages/blocks/src/email/render.ts]
U44. escapeText  [def · packages/blocks/src/email/render.ts]
U45. escapeAttr  [def · packages/blocks/src/email/render.ts]
U46. coerceNumber  [def · packages/blocks/src/email/render.ts]
U47. n  [const · packages/blocks/src/email/render.ts]
U48. attr  [def · packages/blocks/src/email/render.ts]
U49. openTable  [def · packages/blocks/src/email/render.ts]
U50. blockProps  [def · packages/blocks/src/email/render.ts]
U51. props  [const · packages/blocks/src/email/render.ts]
U52. renderChildren  [def · packages/blocks/src/email/render.ts]
U53. renderHeading  [def · packages/blocks/src/email/render.ts]
U54. level  [const · packages/blocks/src/email/render.ts]
U55. tag  [const · packages/blocks/src/email/render.ts]
U56. size  [const · packages/blocks/src/email/render.ts]
U57. style  [const · packages/blocks/src/email/render.ts]
U58. renderTextBlock  [def · packages/blocks/src/email/render.ts]
U59. renderImage  [def · packages/blocks/src/email/render.ts]
U60. src  [const · packages/blocks/src/email/render.ts]
... and 65 more units the lister found past its cap of 60; cover them as you read the diff.

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

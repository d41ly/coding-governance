**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-13-reuse-scout.md role-sha=4750ffbf67ba task-sha=51069fb02d2f -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c28/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c28.diff (a unified diff with a --stat header; commit subject: "feat(workflows): W1+W2 — the review protocol becomes a gate, not a note"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. KIT_AGENT_CAP_VERSION  [const · .claude/hooks/agent-cap.js]
U2. CAP  [const · .claude/hooks/agent-cap.js]
U3. FIXED_MARK  [const · .claude/hooks/agent-cap.js]
U4. MAX_VERIFIERS  [const · .claude/hooks/agent-cap.js]
U5. MAX_LENSES  [const · .claude/hooks/agent-cap.js]
U6. boundedK  [def · .claude/hooks/agent-cap.js]
U7. t  [const · .claude/hooks/agent-cap.js]
U8. fanoutFindings  [def · .claude/hooks/agent-cap.js]
U9. lines  [const · .claude/hooks/agent-cap.js]
U10. code  [const · .claude/hooks/agent-cap.js]
U11. consts  [const · .claude/hooks/agent-cap.js]
U12. m  [const · .claude/hooks/agent-cap.js]
U13. ok  [const · .claude/hooks/agent-cap.js]
U14. scan  [const · .claude/hooks/agent-cap.js]
U15. l  [const · .claude/hooks/agent-cap.js]
U16. asg  [const · .claude/hooks/agent-cap.js]
U17. name  [const · .claude/hooks/agent-cap.js]
U18. c  [const · .claude/hooks/agent-cap.js]
U19. s  [const · .claude/hooks/agent-cap.js]
U20. refs  [const · .claude/hooks/agent-cap.js]
U21. buf  [const · .claude/hooks/agent-cap.js]
U22. j  [const · .claude/hooks/agent-cap.js]
U23. depth  [const · .claude/hooks/agent-cap.js]
U24. closed  [const · .claude/hooks/agent-cap.js]
U25. inner  [const · .claude/hooks/agent-cap.js]
U26. d  [const · .claude/hooks/agent-cap.js]
U27. n  [const · .claude/hooks/agent-cap.js]
U28. bad  [const · .claude/hooks/agent-cap.js]
U29. openersOf  [const · .claude/hooks/agent-cap.js]
U30. out  [const · .claude/hooks/agent-cap.js]
U31. pending  [const · .claude/hooks/agent-cap.js]
U32. ch  [const · .claude/hooks/agent-cap.js]
U33. win  [const · .claude/hooks/agent-cap.js]
U34. hit  [const · .claude/hooks/agent-cap.js]
U35. before  [const · .claude/hooks/agent-cap.js]
U36. braces  [const · .claude/hooks/agent-cap.js]
U37. script  [const · .claude/hooks/agent-cap.js]
U38. spath  [const · .claude/hooks/agent-cap.js]
U39. fan  [const · .claude/hooks/agent-cap.js]
U40. READ_PATH_CEILING  [constant · .memory-tree.conf]
U41. verifier fan-out (≤5 verify agents per review)  [json-key · tools/gate-legs.json]
U42. verifier fan-out self-test  [json-key · tools/gate-legs.json]
U43. review-protocol parity (kit vs dogfood)  [json-key · tools/gate-legs.json]
U44. KIT_AGENT_CAP_VERSION  [const · tools/hooks/agent-cap.js]
U45. CAP  [const · tools/hooks/agent-cap.js]
U46. FIXED_MARK  [const · tools/hooks/agent-cap.js]
U47. MAX_VERIFIERS  [const · tools/hooks/agent-cap.js]
U48. MAX_LENSES  [const · tools/hooks/agent-cap.js]
U49. boundedK  [def · tools/hooks/agent-cap.js]
U50. t  [const · tools/hooks/agent-cap.js]
U51. fanoutFindings  [def · tools/hooks/agent-cap.js]
U52. lines  [const · tools/hooks/agent-cap.js]
U53. code  [const · tools/hooks/agent-cap.js]
U54. consts  [const · tools/hooks/agent-cap.js]
U55. m  [const · tools/hooks/agent-cap.js]
U56. ok  [const · tools/hooks/agent-cap.js]
U57. scan  [const · tools/hooks/agent-cap.js]
U58. l  [const · tools/hooks/agent-cap.js]
U59. asg  [const · tools/hooks/agent-cap.js]
U60. name  [const · tools/hooks/agent-cap.js]
... and 34 more units the lister found past its cap of 60; cover them as you read the diff.

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

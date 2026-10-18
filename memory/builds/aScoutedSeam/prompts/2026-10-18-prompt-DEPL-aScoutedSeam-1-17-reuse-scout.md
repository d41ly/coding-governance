**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-17-reuse-scout.md role-sha=4750ffbf67ba task-sha=3809ede3f46d -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c18/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c18.diff (a unified diff with a --stat header; commit subject: "TOOL-dClosedLexicon-1: land tools/lexicon/ UNARMED, + the placeholder catalogue gate"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. ROOT  [constant · tools/check-placeholders.sh]
U2. TEMPLATE  [constant · tools/check-placeholders.sh]
U3. COMPANION  [constant · tools/check-placeholders.sh]
U4. CATALOGUE  [constant · tools/check-placeholders.sh]
U5. placeholders_in  [shell-fn · tools/check-placeholders.sh]
U6. tally_for  [shell-fn · tools/check-placeholders.sh]
U7. -0,0 +1,41: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/check-placeholders.kit.toml]
U8. -69,6 +69,15: [[entry]]  [hunk · tools/govkit/registry.toml]
U9. ROOT  [constant · tools/lexicon/adopt-lexicon.sh]
U10. KIT_DIR  [constant · tools/lexicon/adopt-lexicon.sh]
U11. CONF  [constant · tools/lexicon/adopt-lexicon.sh]
U12. resolve_python  [shell-fn · tools/lexicon/adopt-lexicon.sh]
U13. MODE  [constant · tools/lexicon/adopt-lexicon.sh]
U14. -0,0 +1,74: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/lexicon/kit.toml]
U15. -0,0 +1,7: # lexicon layer waivers — deliberate exceptions to predicate P3.  [hunk · tools/lexicon/lexicon-layer-waivers.txt]
U16. -0,0 +1,7: # lexicon suffix waivers — deliberate exceptions to predicate P2.  [hunk · tools/lexicon/lexicon-suffix-waivers.txt]
U17. -0,0 +1,7: # lexicon verb waivers — deliberate exceptions to predicate P1.  [hunk · tools/lexicon/lexicon-verb-waivers.txt]
U18. KIT_LEXICON_VERSION  [py-constant · tools/lexicon/lexicon.py]
U19. CONF_NAME  [py-constant · tools/lexicon/lexicon.py]
U20. WAIVER_FILES  [py-constant · tools/lexicon/lexicon.py]
U21. PIN_KEYS  [py-constant · tools/lexicon/lexicon.py]
U22. PATTERN_SETS  [py-constant · tools/lexicon/lexicon.py]
U23. Offender  [def · tools/lexicon/lexicon.py]
U24. __init__  [def · tools/lexicon/lexicon.py]
U25. __str__  [def · tools/lexicon/lexicon.py]
U26. tracked_files  [def · tools/lexicon/lexicon.py]
U27. ext_of  [def · tools/lexicon/lexicon.py]
U28. _python_defs  [def · tools/lexicon/lexicon.py]
U29. _probe_defs  [def · tools/lexicon/lexicon.py]
U30. hits  [def · tools/lexicon/lexicon.py]
U31. extract  [def · tools/lexicon/lexicon.py]
U32. load_waivers  [def · tools/lexicon/lexicon.py]
U33. _glob_match  [def · tools/lexicon/lexicon.py]
U34. run  [def · tools/lexicon/lexicon.py]
U35. main  [def · tools/lexicon/lexicon.py]
U36. BLOCK_KEYS  [py-constant · tools/lexicon/lexicon_conf.py]
U37. ConfError  [def · tools/lexicon/lexicon_conf.py]
U38. load_conf  [def · tools/lexicon/lexicon_conf.py]
U39. _parse_block  [def · tools/lexicon/lexicon_conf.py]
U40. langs  [def · tools/lexicon/lexicon_conf.py]
U41. _main  [def · tools/lexicon/lexicon_conf.py]
U42. SEED_VERBS  [py-constant · tools/lexicon/scaffold_lexicon.py]
U43. KNOWN  [py-constant · tools/lexicon/scaffold_lexicon.py]
U44. HEADER  [py-constant · tools/lexicon/scaffold_lexicon.py]
U45. main  [def · tools/lexicon/scaffold_lexicon.py]
U46. KIT  [py-constant · tools/lexicon/selftest.py]
U47. FAILURES  [py-constant · tools/lexicon/selftest.py]
U48. PASSES  [py-constant · tools/lexicon/selftest.py]
U49. BASE_CONF  [py-constant · tools/lexicon/selftest.py]
U50. BANNED_SUFFIXES  [constant · tools/lexicon/selftest.py]
U51. LANGS  [constant · tools/lexicon/selftest.py]
U52. VERB_OFFENDER_PIN  [constant · tools/lexicon/selftest.py]
U53. SUFFIX_OFFENDER_PIN  [constant · tools/lexicon/selftest.py]
U54. LAYER_OFFENDER_PIN  [constant · tools/lexicon/selftest.py]
U55. VERBS  [py-constant · tools/lexicon/selftest.py]
U56. LAYERS  [py-constant · tools/lexicon/selftest.py]
U57. check  [def · tools/lexicon/selftest.py]
U58. run_case  [def · tools/lexicon/selftest.py]
U59. SENTINELS  [py-constant · tools/lexicon/selftest.py]
U60. subtokens  [def · tools/lexicon/subtokens.py]
... and 1 more units the lister found past its cap of 60; cover them as you read the diff.

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

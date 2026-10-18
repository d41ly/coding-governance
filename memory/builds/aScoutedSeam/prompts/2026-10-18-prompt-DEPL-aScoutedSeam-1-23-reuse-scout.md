**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-23-reuse-scout.md role-sha=4750ffbf67ba task-sha=14c8412a505f -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c27/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c27.diff (a unified diff with a --stat header; commit subject: "feat(govkit): rollout 1 — the registry, a descriptor per entry, and the selfcheck that ratchets them"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. -114,3 +114,11: # govkit — the deployer's registry and its per-entry descriptors. Pinn  [hunk · .gitattributes]
U2. -0,0 +1,29: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/agent-instructions/kit.toml]
U3. -0,0 +1,59: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/codebase-map/kit.toml]
U4. -0,0 +1,70: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/drift-audit/kit.toml]
U5. verifier fan-out (\u22645 verify agents per review)  [json-key · tools/gate-legs.json]
U6. govkit selfcheck  [json-key · tools/gate-legs.json]
U7. -0,0 +1,25: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/gate-lint/kit.toml]
U8. -0,0 +1,33: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/check-install-prefix.kit.toml]
U9. -0,0 +1,30: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/check-kit-versions.kit.toml]
U10. -0,0 +1,24: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/check-wiring.kit.toml]
U11. -0,0 +1,47: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/kickoff-manifest.kit.toml]
U12. -0,0 +1,34: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/playbook.kit.toml]
U13. -0,0 +1,45: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/push-main.kit.toml]
U14. -0,0 +1,27: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/govkit/entries/settings-merge.kit.toml]
U15. KIT_GOVKIT_VERSION  [py-constant · tools/govkit/govkit.py]
U16. Refusal  [def · tools/govkit/govkit.py]
U17. repo_root  [def · tools/govkit/govkit.py]
U18. git  [def · tools/govkit/govkit.py]
U19. tracked  [def · tools/govkit/govkit.py]
U20. load_toml  [def · tools/govkit/govkit.py]
U21. surface_paths  [def · tools/govkit/govkit.py]
U22. rule_sources  [def · tools/govkit/govkit.py]
U23. rule_destinations  [def · tools/govkit/govkit.py]
U24. entry_members  [def · tools/govkit/govkit.py]
U25. Report  [def · tools/govkit/govkit.py]
U26. __init__  [def · tools/govkit/govkit.py]
U27. fail  [def · tools/govkit/govkit.py]
U28. note  [def · tools/govkit/govkit.py]
U29. emit  [def · tools/govkit/govkit.py]
U30. selfcheck  [def · tools/govkit/govkit.py]
U31. USAGE  [py-constant · tools/govkit/govkit.py]
U32. main  [def · tools/govkit/govkit.py]
U33. -0,0 +1,162: # registry.toml — the deployable population, as a DECLARATION.  [hunk · tools/govkit/registry.toml]
U34. -0,0 +1,28: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/hooks/kit.toml]
U35. -0,0 +1,44: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/memory-recall/kit.toml]
U36. -0,0 +1,75: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/memory-tree/kit.toml]
U37. -0,0 +1,36: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/pytest-parallel-guardrails/kit.toml]
U38. -0,0 +1,77: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/unattended/kit.toml]
U39. -0,0 +1,33: # kit.toml — this entry, declared as data. Read by tools/govkit/. Cont  [hunk · tools/workflows/kit.toml]

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

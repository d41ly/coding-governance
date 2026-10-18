**Serves:** journal DEPL-aScoutedSeam-1

# gov-reuse-scout handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-reuse-scout build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-18-prompt-DEPL-aScoutedSeam-1-20-reuse-scout.md role-sha=4750ffbf67ba task-sha=fafc06b0a035 -->

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

TREE (the parent revision, before the diff landed): C:/Users/daily-agent/AppData/Local/Temp/rsd/c17/tree

THE DIFF: C:/Users/daily-agent/AppData/Local/Temp/rsd/c17.diff (a unified diff with a --stat header; commit subject: "build(TOOL-aReapedSpinner-1): the census — one bounded read, keyed on the id every process has"). Read the --stat first, then the hunks that add code or styles.

RULES: read-only. Search only inside the tree(s) above. Never read anything under C:/projects or any other checkout, and never consult git history: the tree is the state before the diff.

THE UNITS THIS DIFF ADDS, enumerated by a deterministic lister (product files only):
U1. process-monitor census selftest  [json-key · tools/gate-legs.json]
U2. process-monitor adopter selftest  [json-key · tools/gate-legs.json]
U3. print_note  [shell-fn · tools/process-monitor/adopt-process-monitor.sh]
U4. add_problem  [shell-fn · tools/process-monitor/adopt-process-monitor.sh]
U5. build_normalized  [shell-fn · tools/process-monitor/adopt-process-monitor.sh]
U6. -108,28 +108,28: "") add_problem "PROCMON_REAP_MODE is unset — it has no default here,   [hunk · tools/process-monitor/adopt-process-monitor.sh]
U7. MSYS_SYNTHETIC_BIT  [py-constant · tools/process-monitor/census.py]
U8. BACKEND_TIMEOUT_S  [py-constant · tools/process-monitor/census.py]
U9. CensusRefused  [def · tools/process-monitor/census.py]
U10. run_bounded  [def · tools/process-monitor/census.py]
U11. parse_cim  [def · tools/process-monitor/census.py]
U12. parse_ps_w  [def · tools/process-monitor/census.py]
U13. build_windows_rows  [def · tools/process-monitor/census.py]
U14. parse_posix  [def · tools/process-monitor/census.py]
U15. parse_cpu_clock  [def · tools/process-monitor/census.py]
U16. resolve_backend  [def · tools/process-monitor/census.py]
U17. scan_processes  [def · tools/process-monitor/census.py]
U18. measure_rows  [def · tools/process-monitor/census.py]
U19. FIELDS  [py-constant · tools/process-monitor/census.py]
U20. render_rows  [def · tools/process-monitor/census.py]
U21. main  [def · tools/process-monitor/census.py]
U22. -27,16 +27,31: [[files]]  [hunk · tools/process-monitor/kit.toml]
U23. HERE  [py-constant · tools/process-monitor/selftest.py]
U24. PASS  [py-constant · tools/process-monitor/selftest.py]
U25. FAIL  [py-constant · tools/process-monitor/selftest.py]
U26. check  [def · tools/process-monitor/selftest.py]
U27. check_true  [def · tools/process-monitor/selftest.py]
U28. build_cim_fixture  [def · tools/process-monitor/selftest.py]
U29. build_ps_w_fixture  [def · tools/process-monitor/selftest.py]
U30. test_row_contract_is_complete  [def · tools/process-monitor/selftest.py]
U31. test_both_kinds_are_present_and_distinguished  [def · tools/process-monitor/selftest.py]
U32. test_native_is_the_majority_on_this_node  [def · tools/process-monitor/selftest.py]
U33. test_continuation_rows_are_rejected_and_counted  [def · tools/process-monitor/selftest.py]
U34. test_partial_rows_survive_and_are_counted_apart  [def · tools/process-monitor/selftest.py]
U35. test_unjoined_row_keeps_native_kind  [def · tools/process-monitor/selftest.py]
U36. test_posix_fixture_collapses_both_namespaces  [def · tools/process-monitor/selftest.py]
U37. test_cpu_clock_parses_every_shape  [def · tools/process-monitor/selftest.py]
U38. test_non_utf8_backend_output_survives  [def · tools/process-monitor/selftest.py]
U39. test_summary_counts_are_derived  [def · tools/process-monitor/selftest.py]
U40. test_no_backend_refuses  [def · tools/process-monitor/selftest.py]
U41. test_empty_read_refuses_rather_than_reporting_zero  [def · tools/process-monitor/selftest.py]
U42. test_hung_backend_is_bounded  [def · tools/process-monitor/selftest.py]
U43. test_live_read_sees_itself  [def · tools/process-monitor/selftest.py]
U44. test_every_live_row_answers_its_own_liveness_probe  [def · tools/process-monitor/selftest.py]
U45. main  [def · tools/process-monitor/selftest.py]

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

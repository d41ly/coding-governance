**Serves:** research TOOL-dTotalRecall-40

# TOOL-dTotalRecall-40 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-40-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, read at `8fbc5a337`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-40`, hygiene check 12 and the pinned-facts check are clean for the spec.
- Moved by the landed code: the alias reader is `tree_lib.py#resolve_kind` (unit 18); unit 4 rev-4 already reads the `logs` row through it, so S1 checks every comparison in `render_routes` as unit 4 lands it and proves a `journal` and a `log` record both route under `logs`; AC1's fixture uses a family id `read_bindings` binds; AC2 is an `ast.get_source_segment` probe of `render_routes`; the census (S2) is an arm of `check_record_kinds` beside `check_pockets`, with `ALIAS_COMPARE_KEPT` keyed by path under the tool root and a new AC4 with plant `alias-compare-kept`; the predicate over the real tree finds only the govkit shim's `install.on-shim-call` mode `journal` (DERIVED, the writer's run), none a record-kind comparison.
- Forks RESOLVED (agent, delegated): F3 S1 kept as the check over unit 4's renderer; F4 `ALIAS_COMPARE_KEPT` admits a homonym reason beside the fixture reason, opening with the two govkit files (renaming the shim mode is a policy value adopters set, veto 2). Parked: none.
- Follow-up: TOOL-dTotalRecall-53 S34 turns this keep list into `# census: kept` markers, which would break two `shims.py` lines inside `JS_TEMPLATE`.

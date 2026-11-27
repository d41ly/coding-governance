**Serves:** research TOOL-dTotalRecall-1

# TOOL-dTotalRecall-1 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-1-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-1-reground-spec-writer.md), saved verbatim in substance.

- Re-grounded at rev-6, base `8b8b1374`; `check-spec-tokens.py --spec`, hygiene check 12 (with 25) and `unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-1` exit 0; 48652 B against the 49152 B ceiling (DERIVED, `wc -c`).
- Spec-token hits at the pass's start: 1 (DERIVED by the writer's run), `policy fixtures <- tools/memory-tree/kit.toml`, cleared by F6; four more raised by the edit were fixed.
- Moved by the landed code: every cited parent is CLOSED, so F1's two re-point asks are moot; the typed field table lives in `build_records.py#KINDS`, so `schema.source` became `{prefix}/memory-tree/build_records.py:KINDS.<kind>.required`; kit paths in the registry spell `{prefix}` (the install-prefix ban); the run-record writer is `runlog.py record --write`; 16 typed kinds (DERIVED, `TYPED_RECORD_KINDS`) each get a row, `deviation`'s writer `hand`; every `fields` row carries a `home`; review rows declare `Serves` only; the step-gate class row needs `read_kind_schema_members` and `write_kind_schema_plant`, AC3 runs `--plant record-kind-schema`; the gap-key resolver is `record_kinds:--print-gap-keys`, exit 3 with no register tracked; the legacy ledger gains a `--seed-legacy` verb, a home under `memory/project/` and a `PROJECT_REGISTRY_EXTRA` entry.
- Forks RESOLVED (agent, delegated): F5 the `design-record` home is `memory/builds/*/build/*-architecture-v*.md`; F6 `record-kinds-legacy` registers in `tools/govkit/registry.toml` (in `kit.toml` it would ship to every adopter, M3 veto 2); F7 a typed kind with no record prints `<kind>: unarmed — no record yet` and passes.
- Parked: none.
- Follow-ups: F6 contradicts TOOL-dTotalRecall-19 and -52 (ledger tables in `tools/memory-tree/kit.toml`) and TOOL-dTotalRecall-43's AC19; their re-grounds follow F6. The records region grows two rows at the index regen; the spec's size is re-checked after it.

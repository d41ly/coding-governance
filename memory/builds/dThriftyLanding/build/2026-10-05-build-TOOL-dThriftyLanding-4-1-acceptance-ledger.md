# Acceptance ledger — TOOL-dThriftyLanding-4

**Serves:** journal TOOL-dThriftyLanding-4

Built on `ff628c54`. The suite arms are D1 (beside M6), D2, D3 (beside the scratch-gov guard-class
arms) and the M5 key-set update in the govkit selftest. A probe importing the module ran the D1 and D2
cases and the policy key against the new module (8 ok) and the base module (5 red). AC4 was observed
on this tree: a `doc_reads` planted on `memory hygiene` in the manifest alone made the new selfcheck
name the disagreement, and the base selfcheck said nothing. The D3 suite arm is owed to the close.

**Evidences:** TOOL-dThriftyLanding-4
- AC1 — `derive_doc_reads` — returned `["memory/builds/"]` for `{memory_root}/builds/` and `[]` for a declared empty list; the writer calls it at `DOC_READS_FLOOR_RUN_GATES`; absent from the base module
- AC2 — `doc_reads omitted` — the helper returned no list with `matches no tracked path` for one untracked element and named `map_root` for an unresolved token
- AC3 — `1.24` — refused at the doc-reads floor while the same target passed the subject floor; `1.25` accepted
- AC4 — `disagree about which doc paths` — printed by the new selfcheck for `memory hygiene` with `doc_reads` in the manifest and none in `tools/memory-tree/kit.toml`; the base selfcheck printed nothing
- AC5 — `GATE_DOC_PATHS` — in `POLICY_KEYS`; the base module's tuple lacked it

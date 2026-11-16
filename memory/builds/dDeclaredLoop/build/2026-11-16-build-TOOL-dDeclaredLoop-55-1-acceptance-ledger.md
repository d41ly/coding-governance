# TOOL-dDeclaredLoop-55 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-55

No merge bar and no self-test suite ran in this pass, and it wrote no product file, as rev-4 §8 F3 (a)
resolves. The criteria were observed on node `d` (win32), at rev-4 of the spec, over the working tree at
`f74eacaf5`, the tree `TOOL-dDeclaredLoop-33` (`aeef7e3c8`) left at order 34: the two `python -c` probes
section 6 spells, standing in for the no-guard arm `TOOL-dDeclaredLoop-67` S31 adds to the
`run-gates gov canary` leg at order 38. The AC1 probe's liveness was observed on an in-memory copy of the manifest whose
`loop termination` row was given a `guard`, which printed `1 [True]`, and with the name changed to one no
row carries, which printed `0 []`, so the probe can read red on both of its red cases.

Owed to the close: every leg section 7 names. Owed RED-first: none, the spec mints no arm; the lasting
no-guard arm is `TOOL-dDeclaredLoop-67` S31's.

**Evidences:** TOOL-dDeclaredLoop-55
- AC1 — `1 [False]` — `json.load` over `tools/gate-legs.json`, keeping the rows named `loop termination`, printed `1 [False]`: one row, its argv `{prefix}/loop/termination.py check --selftest`, carrying no `guard` key.
- AC2 — `[] 1` — `tomllib` over `tools/loop/kit.toml` and `tools/govkit/registry.toml` printed `[] 1`: the descriptor's `gate_leg` tables are `loop definition` and `loop transition tables` alone, and one `[[exempt_leg]]` row names `loop termination`.

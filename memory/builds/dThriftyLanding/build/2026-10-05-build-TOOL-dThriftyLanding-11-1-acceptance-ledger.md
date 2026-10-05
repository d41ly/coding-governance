# Acceptance ledger — TOOL-dThriftyLanding-11

**Serves:** journal TOOL-dThriftyLanding-11

Built on `079a947c`. The M5 block now grades `build_policy_re()` rather than a hand copy. Executed
standalone it passed 19 checks against the engine; with the f765eb8e pattern injected as the builder,
the three multi-path arms and gov's real line failed and every other check held.

**Evidences:** TOOL-dThriftyLanding-11
- AC1 — `GATE_DOC_PATHS='a/ b/'` — caught, with the double-quoted, exported-and-commented and gov's own multi-path lines, by the builder; all four missed by the f765eb8e pattern; `GATE_DOC_PATHS="a b" bash x` stays an invocation

# Acceptance ledger — TOOL-dThriftyLanding-3

**Serves:** journal TOOL-dThriftyLanding-3

Built on `501e0a9a`. The arms are the `DOCS` block at the foot of the hook suite, each over a scratch
clone whose gate-env file at R declares the class under test, with a stub bar that records the docs
base it received. A slice holding the suite's prologue and that block ran against the new hook (8
ok), against the unit-2 hook swapped in (AC1, AC4, AC6, AC7, AC8 red), and against three mutations:
no per-commit read (AC3 red), no non-doc refusal (AC2, AC3, AC8 red), the class read from the pushed
tip (AC5 red).

**Evidences:** TOOL-dThriftyLanding-3
- AC1 — `docs-only: 1 path(s) in GATE_DOC_PATHS at` — printed on the scoped line, and the bar received `docs=` R
- AC2 — `src/x.sh` — a push changing it beside a doc printed no `docs-only` and the bar received an empty docs base; red under the mutation that drops the non-doc refusal
- AC3 — `docs-only` — absent when a code file was added and removed inside the range; red under the mutation that reads the net diff only
- AC4 — `scoped gate` — a doc-only merge whose second parent the record does not cover; the unit-2 hook forced `FULL gate`
- AC5 — `docs-only` — absent when only the pushed tree declares the class; red under the mutation that reads the class at the pushed tip
- AC6 — `not a plain repo path` — printed for `notes/*`, and the push is not doc-only
- AC7 — `doc-only, but` — the FULL line past the lag bound, with the `commits behind` reason
- AC8 — `GATE_DOCS_BASE` — named among the knobs not honoured, and the stub bar received an empty docs base

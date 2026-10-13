# Acceptance ledger — TOOL-dSweptBranches-10

**Serves:** journal TOOL-dSweptBranches-10

Built on `0308aa5c`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-10
- AC1 — `branch_reconcile.py` — a probe whose name only prefixes a longer test, one whose name appears only in prose, and one whose name is declared under another body each read `UNMERGED-LIVE`; the landed probe, whose case and body exist in a default test file, still reads covered. Before the fix all three read covered. Red again with the body check replaced by a name hit. A staged break of the first version's declaration-form ERE stayed green, because the declaring line is one of the probe's own lines; the ERE was dropped and spec rev-2 records it

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

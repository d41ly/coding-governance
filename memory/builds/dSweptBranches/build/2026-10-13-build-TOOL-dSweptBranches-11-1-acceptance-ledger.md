# Acceptance ledger — TOOL-dSweptBranches-11

**Serves:** journal TOOL-dSweptBranches-11

Built on `6aa20124`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-11
- AC1 — `branch_reconcile.py` — a branch that rewrites `| TOOL-aSlug-1 | fix x | open |` in place to a resolved row reads `UNMERGED-LIVE`, while the archived row still reads `SUPERSEDED` by `rotated 1` and the citing spec stays `UNMERGED-LIVE`. Before the fix the edit read `SUPERSEDED`. Red again with the lookup keyed on the row's id instead of its whole text

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

# Acceptance ledger — TOOL-dSweptBranches-13

**Serves:** journal TOOL-dSweptBranches-13

Built on `237f4960`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-13
- AC1 — `--force-with-lease` — after a second clone pushed new work to `landed-b` behind this clone's fetch, `--write --remote` left `landed-b` on the remote, printed it `failed` by name, still deleted `landed-a`, and exited 1. Before the fix the push deleted `landed-b` with its new commit and exited 0. Red again with the leases removed
- AC2 — `branch_reconcile.py --write` — a local branch moved through the remover seam between grading and its deletion is kept and printed `moved since it was graded`. Before the fix it was deleted. Red again with the re-check removed

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

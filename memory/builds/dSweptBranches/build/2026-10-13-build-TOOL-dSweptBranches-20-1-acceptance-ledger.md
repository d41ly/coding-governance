# Acceptance ledger — TOOL-dSweptBranches-20

**Serves:** journal TOOL-dSweptBranches-20

Built on `13cc354f`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-20
- AC1 — `git grep -n -E` — every hit of `diff-filter=[A-Z]*A|--name-status|diff-tree` over `tools/`, `.githooks/` and `skills/`, tests and Markdown excluded, is a row of `2026-10-13-build-TOOL-dSweptBranches-20-1-range-reader-audit.md`, decided by shape and base
- AC2 — `range-probe.sh` — over a gov feature branch at `6e8f8b1d` merging `2b852f5f` (seven `memory/` files gained, asserted first), the staged set, a frozen-base log, `log -m`, `diff-tree -m` and `log --first-parent` read all seven; a default-tip log, a three-dot diff, a plain `diff-tree` and `--ancestry-path` read none; gov's `check-memory-hygiene.sh --staged` over the merge in progress exits 0. Two staged-set sites are filed as `TOOL-dSweptBranches-22`
- AC3 — `gotchas.py --for-paths` — over `tools/runlog/model.py` its checklist names `a-merge-of-the-default-branch-read-as-additions`

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

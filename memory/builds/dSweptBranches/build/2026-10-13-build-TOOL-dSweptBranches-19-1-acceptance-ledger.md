# Acceptance ledger — TOOL-dSweptBranches-19

**Serves:** journal TOOL-dSweptBranches-19

Built on `5c20cc2b`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-19
- AC1 — `adopt-branch-reconcile.sh --check` — exits 0 naming `.claude/skills/cleanup/SKILL.md`, a fresh render whose front matter reads `name: cleanup`; the old render was moved with `git mv`, not copied
- AC2 — `git grep -n -F` — over the tree outside this build's closed records and run record, `/branch-reconcile`, `skills/branch-reconcile` and `branch-reconcile skill` appear only in spec 19 itself, which describes the rename, and in closed spec 5, kept as history
- AC3 — `govkit.py selfcheck` — 0 problems with `cleanup skill wiring` declared in the descriptor, the leg manifest and the subject pins; `gen_map.py --check` exits 0 over the dossier claiming it; `check-kit-versions.sh` clean

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

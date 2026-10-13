# Acceptance ledger — TOOL-dSweptBranches-23

**Serves:** journal TOOL-dSweptBranches-23

Built on `67cb3c10`, inline, promoted at the follow-up's closing review. The arm was written first and
observed red against the unfixed adopter; then the fix's content test was staged out on a copy,
observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-23
- AC1 — `test_scaffold_withdraws_the_old_render` — red against the unfixed adopter (the old render, planted beside a fresh cleanup render in a fixture repository under the prefix `kits/br`, survived `--scaffold`); green with the fix, the file and its directory gone
- AC2 — `test_scaffold_keeps_an_unrecognised_old_file` — with the content test staged out of `check_old_render`, `--scaffold` exited 0 and deleted the adopter's own file; restored, it exits 1 naming the path and the file is unchanged
- AC3 — `test_check_reds_while_the_old_render_stays` — red against the unfixed adopter (`--check` exited 0 beside the old render); green with the fix, exit 1 naming the old path, and exit 0 once it is withdrawn
- AC4 — `grep -n "branch-reconcile skill wiring" WIRE-INTO-PROJECT.md` — finds section 3g's step 4. The whole kit self-test then passed 96 of 96 at its raised floor of 96, and gov's own `--check` exits 0

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.

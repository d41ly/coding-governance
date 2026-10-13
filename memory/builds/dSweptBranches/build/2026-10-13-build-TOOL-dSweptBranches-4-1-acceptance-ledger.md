# Acceptance ledger — TOOL-dSweptBranches-4

**Serves:** journal TOOL-dSweptBranches-4

Built on `f3ac796f`, inline, before unit 3. The arms call `remove_worktree` in-process under the
fixture's git environment, with the module's `run_worktree_remove`, `run_rm` and `RM_NAME` seams
replaced where a failure must be staged. This node creates symlinks, so the skeleton carries a
dangling link to an MSYS-style `/c/...` target; a link scanned with `os.stat` reports the reparse
attribute `0x400`. Each break was staged on a copy of `branch_reconcile.py`, observed red, and the
bytes restored.

**Evidences:** TOOL-dSweptBranches-4
- AC1 — `remove_worktree` — with git's removal failing "Result too large", `rm -rf` removed the directory and `git worktree list` no longer names it; red with the fallback removed
- AC2 — `remove_worktree` — the empty skeleton of directories and a dangling link was removed and no spawned argv named `readlink`; red with the skeleton step removed, and with the walk following links, which raised WinError 123 on the MSYS target itself
- AC3 — `remove_worktree` — a skeleton holding one regular file reads `kept · it still holds a regular file` and stays on disk; red with the zero-file assertion removed
- AC4 — `remove_worktree` — `Device or resource busy` from `rm` returns `busy`; red with busy classed as a failure. The write-mode exit half is unit 3's, by spec rev-2
- AC5 — `RM_NAME` — with no `rm` on `PATH` the row fails, names the missing command and leaves the directory; red with a fallback to another deleter

## Owed at the close

The `branch-reconcile selftest` leg and the spec's §7 legs run in the close's bar.

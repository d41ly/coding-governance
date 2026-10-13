# Acceptance ledger — TOOL-dSweptBranches-21

**Serves:** journal TOOL-dSweptBranches-21

Built on `23618142`, inline. The stubbed arm was written first and observed red against HEAD's
reaper; the live arm was measured by a scratch driver that ran it repeatedly and tallied each red's
member and signal outcome.

**Evidences:** TOOL-dSweptBranches-21
- AC1 — `test_live_tree_dies_completely` — with a five-second delay staged into the tree's body, the arm stays green under the poll (the tree was whole after 5.4 s), and the old fixed three-second wait reds it on the same delay; the bytes were restored
- AC2 — `test_msys_signal_is_backstopped_by_winpid` — red against HEAD's `reap.py` (`kill: 104: Permission denied` reported, no taskkill issued), green with the backstop: a single-pid taskkill on winpids 1, 2 and 4, no signal error
- AC3 — `test_live_tree_dies_completely` — on an unchanged HEAD the arm redded 2 of 5, 2 of 6 and 2 of 10 live runs, every red the native python grandchild (`Permission denied`, or accepted and still alive after the settle); `kill -f -9` redded 2 of 10 and a refusal-only taskkill 1 of 8; with the backstop, 12 of 12 green, each settled on the first census read. The whole suite then passed 72 of 72

## Owed at the close

The `process-monitor census selftest` leg runs in the close's bar.

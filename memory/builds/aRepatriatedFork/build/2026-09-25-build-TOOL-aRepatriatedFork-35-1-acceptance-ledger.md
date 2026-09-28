# TOOL-aRepatriatedFork-35 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-35

Written by the unit pass on node a. The staged breaks were made in the worktree, observed, and
restored byte-for-byte before the commit. The long suites ran as SLICES: a prologue plus the block
the rename touched, in a temp script removed afterwards. The lander and scratch-guard suites are
short and ran whole.

**Evidences:** TOOL-aRepatriatedFork-35
- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0 and prints `adopter names: 3 from 3 adopters.toml row(s) over 267 shipped file(s) · 0 site(s)`. At base the same arm printed `131 site(s), 131 carried`
- AC2 — `tools/push-main.sh` — with `# staged probe: ported from inCMS.` appended, `selfcheck` exits 1 printing `'tools/push-main.sh' names the adopter `inCMS` 1 time(s) — a shipped file reaches every adopter, and one's brand gate reds on another's name. Cite the record id and `adopter ic` instead`
- AC3 — `tools/govkit/adopters.toml` — with `[adopter.carried]` and one row appended, `selfcheck` exits 1 printing `adopters.toml row ['inCMS'] declares `carried`, which the ban no longer reads`
- AC4 — `.githooks/pre-push.test.sh` — the prologue plus the TOOL-aRepatriatedFork-8 block, sliced, exits 0 with 11 `ok` lines, among them `AC2 a remote named mirror reaches the bar, which refuses as gate-red`; `bash tools/push-main.test.sh` exits 0, `all cases ok`; `bash tools/hooks/scratch-guard.test.sh` exits 0, `167 passed, 0 failed`; the lexicon selftest's TypeScript block, sliced, exits 0 at `43 arm(s)` with 115 of 115 records in exact agreement
- AC5 — `tools/govkit/fixtures/make_adopter_receipt.py` — `python3 tools/codebase-map/test_codebase_map.py` exits 0 after `gen_map.py --write`, having printed `STALE symbols.json` before it; `bash tools/check-dead-paths.sh` and the encoding-posture scan exit 0
- AC6 — `bash tools/check-kit-versions.sh` — exits 0 with agent-cap 1.22, check-wiring 1.10, codebase-map 1.10, drift-audit 1.14, lexicon 1.8, memory-recall 1.13, memory-tree 2.98, pytest-parallel-guardrails 1.2, review-harness 1.13, run-gates 1.11 and unattended 1.39; before the fix-up it named seven stale carriers

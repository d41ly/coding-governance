# TOOL-aRepatriatedFork-31 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-31

Written by the unit pass on node a. Every observation is a direct check; no suite ran. The staged
breaks were made in the worktree, observed, and restored byte-for-byte before the commit.

**Evidences:** TOOL-aRepatriatedFork-31
- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0 and prints `adopter names: 3 from 3 adopters.toml row(s) over 267 shipped file(s) · 131 site(s), 131 carried`. Before the scrub, the same arm exited 1 naming each of the 17 files carrying NicoCares, the first `'.githooks/pre-push' names the adopter NicoCares 4 time(s) against 0 carried`
- AC2 — `python3 tools/memory-tree/row_grammar.py --selftest` — exits 0 with the relabelled arm
- AC3 — `tools/hooks/README.md` — with `Staged probe: ported from NicoCares.` appended and staged, `selfcheck` exits 1 printing `'tools/hooks/README.md' names the adopter NicoCares 1 time(s) against 0 carried`
- AC4 — `tools/push-main.sh` — with the inCMS on its line 3 rewritten to `an adopter`, `selfcheck` exits 1 printing `adopters.toml carries 6 inCMS site(s) in 'tools/push-main.sh' and 5 remain`
- AC5 — `bash tools/check-kit-versions.sh` — exits 0 with memory-tree 2.96, unattended 1.38, review-harness 1.12 and check-wiring 1.9; `python tools/govkit/govkit.py epoch` over a probe commit had named those four FAILED before the bump

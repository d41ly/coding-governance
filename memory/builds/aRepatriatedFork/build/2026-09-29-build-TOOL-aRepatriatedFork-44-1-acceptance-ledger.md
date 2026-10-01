# TOOL-aRepatriatedFork-44 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-44

Written by the unit pass on node a, on a tree carrying none of `TOOL-aRepatriatedFork-23`'s work:
that unit's staged bytes were parked as a binary patch and re-applied after this commit. The staged
break was made in the worktree, observed, and restored byte-for-byte. The govkit selftest ran as a
SLICE: its prologue plus the S13 block that reads the fixture, in a temp script removed afterwards.

**Evidences:** TOOL-aRepatriatedFork-44
- AC1 — `tools/govkit/fixtures/` — `git grep -n 'incms-2cff5855' -- ':!memory/'` exits 1 with no output, and `git diff --cached -M --stat` records the fixture as a pure rename, 0 lines changed
- AC2 — `tools/govkit/selftest.py` — the prologue plus lines 6702 to 6764, sliced, exits 0 with 9 `ok` lines, among them `[-9] S13 LIVENESS the committed inCMS fixture carries the 52-row population` and `[-9] AC1 over the REAL inCMS population: 21 verbatim, 6 eol, 5 relocate, 20 no rung`
- AC3 — `bash tools/check-dead-paths.sh` — exits 0, `24 derived needle(s), 14 declared waiver(s), no undeclared carrier`; with the waiver file restored to its base bytes it exits 1 naming the fixture's lines 128, 129, 597 and 600 under the new path
- AC4 — `python tools/govkit/govkit.py selfcheck` — exits 0 printing `adopter names: 3 from 3 adopters.toml row(s) over 267 shipped file(s) · 0 site(s)`; `govkit.py epoch --base f8fdd873` reports no FAILED entry and `bash tools/check-kit-versions.sh` exits 0, because no descriptor ships a renamed or edited file

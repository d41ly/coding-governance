# TOOL-aRepatriatedFork-36 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-36

Written by the unit pass on node a. The long suites ran as SLICES in temp files inside the kit dir,
removed afterwards: the govkit selftest's `[aRF-36]` arms and its `DEPL-dCarriedReceipt-10` block,
and the check-wiring suite's prologue with its AC8, AC13 and receipt blocks. Every old-bytes run
swapped in `HEAD`'s file and restored it, byte-compared.

**Evidences:** TOOL-aRepatriatedFork-36
- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0. With `extract.py`'s header put back to `FORKED from` it exits 1 printing `'tools/memory-recall/extract.py' declares `FORKED from` in its head but entry 'memory-recall' claims it with role 'engine'`
- AC2 — `tools/govkit/selftest.py` — the `[aRF-36]` slice prints `ok   [aRF-36] apply lands memory-recall's CLI, extractor and hook on a fresh target` and `ok   [aRF-36] ...and reports no entry INCOMPLETE`; over `HEAD`'s `kit.toml` both print FAIL
- AC3 — `tools/check-wiring.test.sh` — the AC8 slice exits 0 at `11 passed, 0 failed`; over `HEAD`'s `check-wiring.sh` and `settings-merge.py` it prints `FAIL AC8 an adopter-owned receipt row moves the resolved hook to the target's copy` and `FAIL AC8 recall hook kept elsewhere and declared owned -> ok, exit 0`, while the control and the parity arm pass. The AC13, AC8 and receipt blocks together exit 0 at `24 passed, 0 failed`
- AC4 — `python tools/settings-merge.py --selftest` — prints `settings-merge selftest: PASS`; with the owned join removed from `resolve_hook_path` it raises `AssertionError: k/h.js` at arm 13b
- AC5 — `tools/govkit/selftest.py` — the synthetic slice exits 0 with 35 `ok` and 0 failures. Before the fixture repair its LIVENESS arm printed `FAIL [-10] LIVENESS a complete `forked` rule is selfcheck-GREEN — govkit: no such descriptor: …/fork-ok/tools/govkit/adopters.toml`
- AC6 — `bash tools/check-kit-versions.sh` — exits 0 with memory-recall 1.14, check-wiring 1.11 and settings-merge 1.8; `bash tools/check-hook-destinations.sh` exits 0; the memory-recall selftest exits with 71 `ok`

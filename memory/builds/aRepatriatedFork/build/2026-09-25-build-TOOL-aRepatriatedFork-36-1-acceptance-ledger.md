# TOOL-aRepatriatedFork-36 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-36

Written by the unit pass on node a, and rewritten by the rev-3 fold of the closing diff review of
units 31 to 38 (2026-09-26), whose criteria it now answers; rev-2's lines are superseded. The long
suites ran as SLICES in temp files inside the kit dir, removed afterwards: the govkit selftest's
`[aRF-36]` arms and its `DEPL-dCarriedReceipt-6` block, and the check-wiring suite's prologue with
its AC8 block. Every old-bytes run swapped in the rev-2 file (`176e1060`) and restored it,
byte-compared. The whole check-wiring suite ran once on the built tree: `136 passed, 0 failed`.

**Evidences:** TOOL-aRepatriatedFork-36
- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0. With `opt_in = "With-Hook"` staged into the recall descriptor it prints `entry 'memory-recall' declares opt_in 'With-Hook', which is not a key a target can set in its [kit.memory-recall] table`; arm 3d's `FORKED from` refusal is unchanged from rev-2
- AC2 — `[aRF-36]` — the slice prints 7 `ok`: CLI and extractor land, no INCOMPLETE, no `recall-opened.js` without the opt-in, the skip names `with_hook`, a declaring target gets the hook, the reserved key is refused, and `plan` agrees. Over rev-2's `govkit.py` and descriptor four of them print FAIL, the hook having landed through the `**` rule
- AC3 — `tools/check-wiring.test.sh` — the AC8 slice exits 0 at `25 passed, 0 failed`; over rev-2's `check-wiring.sh` and `settings-merge.py` it prints `11 passed, 14 failed`, among them `FAIL AC8 both copies present, the undeclared one wired -> UNWIRED, exit 1` and all eight crafted-row refusals
- AC4 — `python tools/settings-merge.py --selftest` — prints `settings-merge selftest: PASS`; with rev-2's `resolve_owned_hook` swapped in, arm 13c raises `AssertionError: backslashes: resolved to '..\\..\\other\\h.js' instead of refusing`
- AC5 — `tools/govkit/selftest.py` — the `DEPL-dCarriedReceipt-6` slice exits 0; with its builder's `adopters.toml` line removed it prints `FAIL [-6] S4 LIVENESS a descriptor declaring an unshippable leg engine REDS selfcheck — govkit: no such descriptor: …/a6-unshipped/tools/govkit/adopters.toml` and two more
- AC6 — `bash tools/check-kit-versions.sh` — exits 0 with settings-merge 1.9, check-wiring 1.12 and memory-recall 1.16; `bash tools/check-hook-destinations.sh` exits 0; the memory-recall selftest passes 76/76

# Acceptance ledger — TOOL-dFairHearing-38

**Serves:** journal TOOL-dFairHearing-38

Built against spec rev-3, observed at the pass's parent `ff578b9df`, whose `tools/memory-tree/gotchas.py`
this unit's commit carries unchanged, by scratch probes under the pass's scratch directory and a
fixture repository under `%TEMP%/fgc`. The replay verdict record
`2026-11-04-build-TOOL-dFairHearing-30-replay-verdict.md` states `selected` at :374, the decision unit
37's ledger graded under its AC4, so both criteria apply. No suite, gate or bar ran in the pass: spec §7
declares no new arm, and its three legs are owed to the close.

S1's supersession entry is unit 37's ledger, AC4, which already records the `selected` half superseded
here and grades no exit of `gotchas.py`.

**Evidences:** TOOL-dFairHearing-38
- AC1 — `%TEMP%/fgc` — the fixture held two class records, `inside-selection` anchored and gated on the one path the range `HEAD~1..HEAD` touches, and `outside-ungated` anchored on a path it never touches, whose body says no machine gate. `gotchas.py --for-diff HEAD~1..HEAD --all-ungated` and the same call without the flag both exited 0, and `cmp` found the outputs byte-identical: one class selected, `inside-selection`. A staged copy, whose `--for-diff` branch opens with `if "--all-ungated" in argv[3:]:` and prints every class `check_ungated` admits over `git ls-files`, also exited 0 both ways, and its flagged output differs by one leading line, `ungated: outside-ungated`. Its unflagged output is byte-identical to the tracked file's. The fixture was removed after the probe
- AC2 — `branch.py` — §4's script over `tools/memory-tree/gotchas.py` printed `branch 1461-1465 lines 5` and `all-ungated 0`, and exited 0. The span moved from rev-2's 1366-1370 as later units added lines above it. Over the staged copy of AC1 it printed `branch 1461-1471 lines 11` and `all-ungated 1`, and exited 1

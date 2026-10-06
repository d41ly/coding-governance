# TOOL-aMendedFleet-16 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-16

**Evidences:** TOOL-aMendedFleet-16
- AC1 — `python tools/memory-tree/gotchas.py --selftest` — printed PASS with five new arms: the three-tier fixture lists universal, path, directory, basename in that order, all in full, through both `--for-diff` and `--for-paths`; the 2-plus-11 fixture prints the two path classes in full and the eleven directory classes as one line each, through both verbs; the third header line reads 2, 11 and 0. Staged breaks, each observed RED first: with the sort removed four arms failed on catalogue order, and with the first tier made compactable the same four failed
- AC2 — `e4abc55bf~1..e4abc55bf` — against a `git clone --local` under `%TEMP%` checked out at 6f72841a1, the pass's parent, the sorted slug lists from the `- [ ] ` lines matched (53 and 53) and `cmp` on the first two lines reported them equal; the same held for the merge range 2cbb2f09c^1..2cbb2f09c, 56 and 56
- AC3 — `python tools/memory-tree/gotchas.py --for-diff e4abc55bf~1..e4abc55bf` — all 53 items matched the first-line pattern, the tags never returned to an earlier tier, and the third header line's counts, 31, 5 and 11, summed to the 47 the second line selects
- AC4 — `gotchas.py --report` — reported 6 universal; the run over 6a88fbf7b~1..6a88fbf7b printed all six tagged universal, each followed by its description and its record path
- AC5 — `grep -n "specificity" tools/memory-tree/README.md` — hit line 40, the `gotchas.py` row, which names the path, directory and basename tiers and the budget of 12

## What the close owes

The tier counts reproduced the spec's pinned table on all five ranges only under the
leading-directory reading of S1, which rev-3 records. The `gotchas selftest`, `memory hygiene` and
`codebase-map coverage + freshness` legs were not run in this pass; the bar owes them at the close.

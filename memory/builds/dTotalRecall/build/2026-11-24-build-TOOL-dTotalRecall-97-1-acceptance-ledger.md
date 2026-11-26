# TOOL-dTotalRecall-97 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-97
**Caused-by:** TOOL-dTotalRecall-97

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-2 over base
`4e8296e94284541d8c5517af65ea94c5bc859abe` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's three fences, verbatim, each extracted from the spec into a file under the scratch directory and
sourced from the repository root.

§4's fixture, read by `c5_input` for each label (DERIVED 2026-11-24, those runs):

| Label | Printed, its lines joined by a comma (DERIVED 2026-11-24) |
|---|---|
| `y` | `y rc=1`, `y MANIFEST check 5 FAILED — watched files changed since last-audit`, `y unplaced 0` |
| `p69` | `p69 rc=0`, `p69 unplaced 0` |
| `p69^` | `p69^ rc=1`, `p69^ unplaced 0` |
| `v`, `k`, `w`, `x` | one line each: `v unplaced 1`, `k unplaced 1`, `w unplaced 1`, `x unplaced 1` |
| `u` | `u rc=0`, `u unplaced 1` |
| `none` | `none unplaced 0` |

An absent file, an empty path and a file that is not UTF-8 each exited 1 and printed no `unplaced` line
(DERIVED 2026-11-24, those runs).

The one path §4's listing named is
`memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-80-1-acceptance-ledger.md`. The block is §4's
answer over it, `p69` then `p69^` (DERIVED 2026-11-24, that run at the base):

```text
p69 rc=0
p69 unplaced 0
p69^ rc=0
p69^ unplaced 0
```

The zeros are no unmovable count. Over a scratch copy of that ledger whose `p69` status line was made a bullet holding
two reads, `c5_input` printed `p69 unplaced 1` alone; over a copy whose line was an indented, backticked bullet of
status 1 it placed that line and printed `p69 unplaced 0` (DERIVED 2026-11-24, those runs). Unit 80's ledger therefore
keeps the form its S1 states: every line naming a read of either label is placed.

**Evidences:** TOOL-dTotalRecall-97
- AC1 — `c5_input "$SCRATCH/ledger97.md" <label>` — printed, for each of the labels AC1 names, the lines §4 pins and the table above holds, among them both `y` lines with `y unplaced 0`, `v unplaced 1`, `u unplaced 1`, `w unplaced 1` and `p69 unplaced 0` (DERIVED 2026-11-24, those runs).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-97" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone once it was written. Unit 80's acceptance ledger is `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-80-1-acceptance-ledger.md`; the block above is the verbatim output of `c5_input` for `p69` and for `p69^` over it, each ending in its `unplaced` line, and a run made over that path after this ledger was written printed the same lines (DERIVED 2026-11-24, these commands).

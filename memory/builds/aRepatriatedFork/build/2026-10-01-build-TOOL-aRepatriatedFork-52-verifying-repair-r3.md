**Serves:** journal TOOL-aRepatriatedFork-52 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-28

# aRepatriatedFork: VERIFYING repair pass R3, the redesigned leg's first whole runs

*Node `a`, 2026-10-01. The main loop ran `tools/run-gates/foreign-prefix.gov.test.sh` whole, alone,
after `TOOL-aRepatriatedFork-52` closed at `f21e441b`. Five runs: four redded, the fifth at `19ef4230`
printed PASS in 2494 s. Each fix folds into the unit whose commit wrote the line, spec-first. No merge,
no push, no hook bypassed, and the full bar did not run.*

## Per run

| Run | Head | Seconds | Verdict | Cause | Fix | Owner |
|---|---|---|---|---|---|---|
| 1 | `f21e441b` | 193 | red at `scripts/` | `govkit selftest`: the clone was a detached HEAD, so no ref carried the vintage the suite pins | the clone checks out a named branch (rev-4) | TOOL-aRepatriatedFork-52 |
| 1 | `f21e441b` | 193 | red at `scripts/` | `corpus-ids selftest`, red at `tools/` too: the self-test swapped `GRAMMAR_DIR` but S4's refusal reads `GRAMMAR_WHERE` | the helper swaps both (rev-7) | TOOL-aRepatriatedFork-46 |
| 1, 2 | `f21e441b`, `6a5e4642` | 193, 192 | red at `scripts/` | `backlog migration selftest` overran its 80 s budget, alone as well as pooled (79 to 105 s on node a) | budget 300, its manifest ceiling | TOOL-aRepatriatedFork-52 |
| 3 | `23404939` | 708 | green at two prefixes on 46 of 81 rows | the row loop read its list on stdin, so every row after `run-gates canary` never ran | the list rides fd 3, rows read `/dev/null` | TOOL-aRepatriatedFork-52 |
| 3 | `23404939` | 708 | red at the root | codebase-map and corpus-ids fixtures built their prefixed shape at the derived prefix, empty at a root install | a stand-in prefix when the derived one is empty (rev-8 each) | TOOL-aRepatriatedFork-28, TOOL-aRepatriatedFork-46 |
| 4 | `87c9acff` | 638 | red at `vendor/gov/` | two whole rows timed out in the 8-wide pool at budgets measured one suite at a time | whole rows run serially after the pool (rev-5) | TOOL-aRepatriatedFork-52 |
| 3, 4 | | | red at the root | `govkit selftest`: 58 selfcheck problems about gov's own registry at an empty tool root | declared gov layout, not graded at the root (rev-6) | TOOL-aRepatriatedFork-52 |
| 5 | `19ef4230` | 2494 | PASS | | | |

## For the owner

`govkit selftest` is not graded at the repo root. Its first arm checks gov's own registry, and govkit
ships to no adopter, so a root install of gov is not a layout gov has. Supporting it is the run's
parked question about gov's own tool-root move, and the 58 problems are its inventory: `./`
destinations against claims spelled bare, guard pathspecs that fall into no class, and the
`{prefix}/*` surface glob, which covers every top-level file once the prefix is empty.

The leg's evidence row was written from a clone holding no `gate-run` readings. A `--write` here would
have admitted every killed and contended reading this worktree keeps, and redded a dozen unrelated
ceilings.

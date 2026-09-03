## Verdict: CLEAN WITH FIXES

**Serves:** diff-review TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-6 TOOL-aCollapsedScan-7

Two rounds, node `a`, 2026-08-26. Round 1 from the pinned BASE `3c37a1fb` to `b679190c`; round 2
from `b679190c` to the fold at `378818dd`, so it read the FIX rather than re-reading the diff.

| Round | Raised | Confirmed | Refuted | Blockers | Verdict |
|---|---|---|---|---|---|
| 1 | 28 | 20 | 8 | 2 | CONVERGING |
| 2 | 12 | 9 | 3 | 0 | CONVERGED |

Precision 0.71 and 0.75 — well above the ~0.5 the charter names as the tighten-priming threshold, and
a long way from the spec audit's 0.33 earlier in this build. The difference was the brief: both
closing rounds were handed the nine bug classes `gotchas.py` selected for the diff and an explicit
by-design list, and round 2 was additionally handed round 1's confirmed set as already-fixed.

## The three findings that changed code rather than prose

**The walk-up had no repository boundary (round 1, medium, and the most serious thing found).**
`recall_conf.repo_root()`'s new walk returned the nearest conf-holding ancestor with no `.git` test,
so it walked out of the checkout entirely. `tools/codebase-map/map_lib.py`'s `resolve_root` already
pays two lines to stop there, and its docstring records why: worktrees are commonly kept INSIDE the
primary tree — this repo puts them under `.claude/worktrees/` — so an unbounded walk from a
worktree's kit dir reaches the PRIMARY tree's conf and resolves into a different repository. A lens
REPRODUCED it: conf at `outer/`, a separate git repo at `outer/inner/` holding the kit, and the
patched function answered `outer` where the pre-fix code correctly refused. The justification the
spec offered for skipping the boundary was circular — it established that the returned root has a
conf, not that it is this checkout's root — and the fix now quotes it as such.

The same two lines closed a second finding: a conf-bearing tree that is not a git repo at all now
falls through to the git probe and gets the kit's `ConfError` at exit 2, where the unbounded version
had turned it into a `CalledProcessError` traceback at exit 1.

**The new selftest arm leaked, and the suite's own sweep check said otherwise (round 1, medium ×4).**
It was the only arm in the file with no `try/finally`, dropping a scratch repo AND a registered
worktree per run. Because `_SWEPT` is appended only inside `cleanup()`, the closing residue arm could
not see either, and printed `ok  every scratch repo this run created was removed`. The guard shared
its population with the thing it guarded. Sweep count went 32 → 34.

**Both blockers were generated-artifact and record drift, not logic.** `memory/map/generated/symbols.json`
still claimed the `repo_root` the unit deleted and missed the arm it added — regenerating an artifact
is part of the unit that changes it, not a later chore. And a backlog row backticked `path:65` with
the line number inside the backticks, which hygiene check 15 rule 1 reads verbatim as a path.

## The finding that audited a citation rather than code

Round 2, medium. The `-7` and `-8` rows both credited `tools/govkit/govkit.py` with stopping at the
repository boundary. Verified at source: it walks `here.parents` for `tools/govkit/registry.toml`
with no `.git` test and no break — the same unbounded shape round 1 had just refused in this kit.
Only `map_lib.resolve_root` carries the boundary. So the precedent cited for the fix was a function
with the defect the fix removes. Rows corrected; `TOOL-aCollapsedScan-12` files govkit's own walk.

## The half-done fix

Round 2, medium. Round 1 flagged a stale authored count in `merge-rows.test.sh`'s header
(`Measured: 12 of the 34 run cases`). The fold deleted it and left its complement standing one
sentence later — `The other 22 are held by...` — orphaned, and wrong by two at the live 40. Half a
de-counting edit, in the file whose header argues against authored counts. It also left the
`so that...` clause dangling off the wrong antecedent.

## What was deliberately not raised

`NEVER_WORSE_FLOOR` stayed at 12 against a live 16. Unlike its two siblings, which are pure greps of
the file and therefore identical on every node, that bound counts the controls `git merge-file` exits
0 on, which is a property of the git in hand. Raising it off one node's reading could red another.
The note beside it now says that, and names the 4-case window as the price — an explanation rather
than a silent ratchet, which is the reviewer's own second option.

Three residuals are filed rather than fixed: `TOOL-aCollapsedScan-8` (`drift_report.py` carries the
identical pre-fix resolver), `-11` (a `kit.toml` guard cannot name a sibling kit, so the descriptor
and the manifest now disagree in content), and `-12` (govkit's unbounded walk).

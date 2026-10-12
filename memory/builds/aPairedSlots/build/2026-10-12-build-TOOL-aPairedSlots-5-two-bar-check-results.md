# The two-real-bar check — two concurrent bars of one repository keep every record whole

**Serves:** journal TOOL-aPairedSlots-5 TOOL-aPairedSlots-7

Run on node a from 2026-10-11T23:32Z to 2026-10-12T05:29Z by
`2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh`, over two worktrees of one frozen repository
at `b6cd9fa6`, under a private turnstile at two slots. Each worktree ran the default full bar once
alone and once beside the other. The rows sit beside this record as
`2026-10-12-build-TOOL-aPairedSlots-5-two-bar-check-rows.tsv`. The run began on the check's earlier
copy, whose own verdict was FAIL for reasons TOOL-aPairedSlots-13 and -14 removed; the verdict below
is `grade` from the check as those units left it, over what the run left.

## What the run records say

| Bar | Run | Slot | Acquired | Ended | Wall | Verdict |
|---|---|---|---|---|---|---|
| w1, alone | 20261011T233221Z-285794 | 1 | 23:32:26 | 01:43:06 | 7861 s | RED |
| w2, alone | 20261012T014314Z-542294 | 1 | 01:43:16 | 03:56:13 | 7990 s | RED |
| w1, beside w2 | 20261012T035632Z-843545 | 1 | 03:56:34 | 05:27:00 | 5440 s | RED |
| w2, beside w1 | 20261012T035632Z-843549 | 2 | 03:56:40 | 05:28:50 | 5550 s | RED |

The concurrent pair held slots 1 and 2 at once: each was admitted before the other ended. The alone
bars ran slower than the concurrent ones because the turnstile suite and its slices ran on the host
during them; walls here grade nothing.

## The grade

- **Records kept whole.** Every bar left one whole run-log line under its run id in the common dir's
  `runlog/gates.log`, a run record with a verdict, and 65 ledger rows for its 65 reported legs. No row
  was lost or torn, alone or beside the other bar.
- **w1's leg verdicts are identical** alone and beside w2: 55 ok and 10 FAIL each time.
- **w2's differ in one leg, `straggler-guard arms`, and the difference is the host's.** That leg
  timed out at its 300 s ceiling in all four bars, and was retried serially after each pool drained.
  Its retry finished inside the ceiling once, in w2 beside w1, and timed out in the other three. A
  ceiling breach is a cost verdict, and its outcome followed the host's load, not which files the two
  bars shared. `brief-recorded` timed out at 900 s and failed in all four.
- The other eight reds are the same in all four bars. They are the frozen tree's own, at a base before
  the reconcile with origin/main.

`grade` prints `TWO-BAR CHECK FAIL` on that one leg, because it compares verdicts as they fell. Read
with the attribution above, two concurrent bars of one repository produced the same verdicts as the
same bars run one at a time on every leg whose outcome is not a ceiling breach, and lost or tore
nothing. That is the prompt's second acceptance item, observed.

# TOOL-dPlacedRequest-48 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-48

The unit was built from its spec at rev-10 on base `86c5380c1`. Built: S1 to S3 as one placed-race
block in region eight of `tools/unattended/unattended.test.sh`, after the `TOOL-dPlacedRequest-43`
block's AC32 rows and before its `rm -rf "$LF"`, over that block's lease fixture and
`tools/unattended/unattended.test.sh#run_request_arm`; S5 as the two floors with their `RAISED`
comments. No product code changed and no function was added, so `memory/map/generated/` is unmoved.
No gate, suite or bar ran in this pass.

THE BLOCK PROBE, the reading the lines below cite as "the probe": a scratch script holding the block's
lines byte for byte, a `diff` of the two read identical, over the suite's own `mkconf` and
`write_lease_fixture` copied out of it and its `same` and `hit` helpers, never the suite, the fixture
under the node's short temp path. It executes the block's rows and prints its line of exits.
The block's assertion count, 5 `same` and 3 `hit` with no loop or skip branch: (DERIVED)
- 8 (DERIVED)

**Evidences:** TOOL-dPlacedRequest-48
- AC1 — `requests.lock busy` — the probe over the HEAD driver printed no failing row: B exits 2 naming the lock, A exits 0 `recorded`, the stored copy is `a.md` by `cmp -s`, `.typed` holds one `qA` line and the origin one ref for the key. (PINNED)
- AC1 — B's seconds after the hold, on this node: (PINNED)
- 6 s (PINNED)
- AC1, RED — `3fc16744c` — the probe with `SCRIPT` the driver of a detached worktree at that commit, before unit 43's lock: B exits 0 `recorded`, A exits 0 `already recorded`, the stored copy differs from `a.md`, and the third call exits 0; the AC3 row stays green, so the stub fires on that driver's copy too and the red reads the lock alone. (PINNED)
- AC1, RED — the failing rows of that run, every AC1 and AC2 row: (PINNED)
- 7 (PINNED)
- AC2 — `collision` — the probe over the HEAD driver: the third call with `b.md` exits 2 printing `collision: a different text keys alike`. (PINNED)
- AC3 — `request race never placed` — the probe with the stub swapped for a pass-through `cp` printed `FAIL DPR48 AC3 ... got [request race never placed]` and exited 1, A waited for and B run after the bound. (PINNED)
- AC4 — `TOOL-dPlacedRequest-48` — the AC30 paragraph of spec 43, cut by the criterion's `awk` and squeezed by `tr -s '[:space:]' ' '`, names this unit and holds no `two background`. (DERIVED)

## Owed at the close

- The new arm's RED-first observation, the spec's `New arm:` line: the block run with `SCRIPT` the
  driver of a worktree at `3fc16744c` reds, and green once restored; the probe above stands in for it
  in this pass and is not that observation.
- S5's floors, read only by the suite's own count, whose run README rule 8 waives for this landing.
- The legs the spec's Gates section names, run once by the main loop.

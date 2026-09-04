# Acceptance ledger — DEPL-dSealedTally-1

**Serves:** journal DEPL-dSealedTally-1

Tier-2 · node d · 2026-09-04

## The headline: this unit found a regression I had shipped three commits earlier

`derive_unclaimed_candidates` holds its own copy of the `_decided` loop, and the landing block holds
another. `DEPL-dSealedTally-2` narrowed the landing's copy and left the classifier's untouched — so
once the rename map was filled eagerly, the classifier treated every declared destination of every
kit as already-decided and answered ZERO.

The read-only preview IS that classifier. So from commit `a6e67049` onward, `govkit update` reported
`unclaimed sources: 0 would land` on a run that landed one. **A preview disagreeing with the write
is the exact failure the preview was built to prevent**, and the comment above it claims "ONE
IMPLEMENTATION, TWO CALLS" — which was already untrue when I read it, and my change made the
untruth consequential.

Reproduced on a four-file scratch repository: preview `0 would land`, write lands 1. After
narrowing the classifier the same way: preview `1 would land`.

The two copies are still two, recorded in the code rather than hidden. Routing the landing through
the classifier is a larger change than this unit; `AC9` is what makes the next divergence red.

## Built in five steps, each verified before the next

The unit restructures ~180 lines, so it went in as A→E with a full suite run between each: the
return shape and its consumer, the write-path call and the widened `touched_kits`, the block split,
the snapshot entry and restore branch, then the arms. Every step held at 1087 arms before the next
began.

**Reading the existing code first removed the largest piece of work.** The restore loop already
handles an absent pre-state with `git rm --cached` then `unlink`, which is exactly a landed file's
rollback — so the file half needed no new branch at all. `origin` exists only for the half that
genuinely differs: a row this run MINTED must be removed, not restored, and its `ROLLBACK_FIELDS`
restore skipped.

## The criteria

**Evidences:** DEPL-dSealedTally-1

- AC1 — MET, OBSERVED — `python tools/govkit/selftest.py` runs the `[-ST1]` fixture, a kit whose
  only change is a landed source and whose check rejects that very file: after the rollback the file
  is gone from the worktree, the target is back to exactly the file set it had, and the run reached
  its own rollback report rather than a traceback.
- AC2 — MET BY EXISTING ARMS in `tools/govkit/selftest.py`, not by a new one, and that is stated
  rather than implied. The passing-check case is what the `[-RS1]` arms already assert: a
  landing on a run that does not roll back survives and is tracked. This unit built no second
  fixture for it, so the property is covered on a different fixture than AC1's.
- AC3 — MET, OBSERVED — the `[-ST1]` arms assert the path is gone from `git ls-files`, which is the
  half a bare `unlink` misses.
- AC4 — MET, OBSERVED — the post-rollback receipt in `tools/govkit/selftest.py` names no landed
  path, so the minted row went with the file.
- AC5 — NOT MET — the `demand_contained_dest` monkeypatch was not built. The guard IS reached,
  since the restore loop calls it for every path before touching one, but nothing here observes the
  call, so the claim rests on reading. Recorded rather than faked; see the residue.
- AC6 — MET, OBSERVED BY TWO STAGED BREAKS over `tools/govkit/govkit.py`, and they discriminate.
  Removing the landing's `snap_rows` append reds SIX `[-ST1]` arms — file survives, stays indexed, row kept, summary
  reports it. Removing the `origin == "landed"` branch reds THREE — the file is still removed, but
  the order says `restored` and the summary reports the undone landing. Different mutations,
  different arm sets, and zero non-`[-ST1]` collateral in either.
- AC7 — MET, OBSERVED — the closing `unclaimed sources:` summary names no rolled-back
  destination, which is what proves the S2 split: a tally moved above the verify pass would
  still list it.
- AC8 — MET, OBSERVED — the rollback order contains `removed   tools/landkit/arrival.txt` and does
  NOT contain `restored  tools/landkit/arrival.txt`.
- AC9 — MET, OBSERVED — `[-ST1]` arms assert the read-only preview names the source the write lands,
  BY PATH and not merely by count, and that the read-only run wrote nothing. These are the arms the
  regression above made necessary.
- AC10 — MET — `python tools/govkit/selftest.py` exits 0 at **1100 arms**, thirteen more than the
  1087 observed at the head of `order 2`, against a spec floor of eight.

## Two of my own arms were wrong, and both mattered

The first LIVENESS arm asserted the word `"rolled back"` appeared in stdout. That matches the
summary line `rolled back 0`, so it passed green over a run that rolled back NOTHING — the
fixture-passes-by-finding-nothing class, in the arm written to prevent it. It now asserts
`rolled back 1`, a count.

The second asserted the write run's stdout NAMES the landed path, which directly contradicted AC7
requiring the summary not to name it. Both were right about their own concern: the tally prints
after the rollback removed the entry, which is exactly why the split leaves the tally below the
pass. The rollback order is the correct witness and proves three things at once — the landing
happened, it was undone, and it printed under the right verb.

## Residue

AC5 is unobserved: nothing checks that `demand_contained_dest` is called for a landed path. The arm
needs a monkeypatch recording the guard's `where` argument, which the suite has no seam for today.
Third unit in this build with a gap of this shape, after `DEPL-dSealedTally-2`'s AC5 and
`DEPL-dSealedTally-4`'s mid-write catch — the pattern is that a guard reached only on a failure path
is hard to observe without a seam for forcing that path.

# Acceptance ledger — DEPL-dSealedTally-4

**Serves:** journal DEPL-dSealedTally-4

Tier-2 · node d · 2026-09-04

## The headline: the fix made the mirror image of the bug it was fixing

`index_read` batched 400 paths into `git ls-files` with `check=False` and never read the exit code,
so a failed chunk produced empty stdout and every path in it parsed as absent-from-index. Absent is
the answer that lets a writing verb decide a path is free to write, in a repository gov does not
own. That is the dead-probe shape and it is what this unit closes.

The first cut added the exit-code check and redded the `[-11]` escape arm. **`git ls-files` exits
128 for a path outside the repository** — measured directly, `fatal: … is outside repository` — and
that is an ANSWER, not a probe failure: such a path is definitionally absent from that index. The
rename-destination probe for a `prefix` that climbs out of the tree therefore raised where it used
to return empty, the verb exited on a `Refusal`, and the run never reached its own containment
refusal. The arm asserts `returncode == 1`; it got the `Refusal` code instead.

So the unit's own subject, one level up: a non-zero exit is not automatically a failure, and
treating it as one manufactures a different wrong answer from the same signal. S4 adds the filter,
in `index_read` so all eight callers inherit it, using the same `resolve()`/`relative_to` idiom the
rename-destination containment check already uses.

## How it was found, which took three wrong theories first

The arm was green at the previous run and red after, with `index_read` as the only `govkit.py`
change between them. Three hypotheses about the call graph all died on inspection — none of the
other `index_read` callers is inside `resolve_entry`, so none could have changed `renamed_to`.

What settled it was reverting the change and re-running (green, so the cause was mine), then a
four-line scratch repository confirming the mechanism in seconds. The message counts I had been
reading were actively misleading: passing arms print nothing, so a message absent from the log meant
nothing at all, and the failure detail is only the last 1500 characters of stdout — the refusal I
was looking for had been truncated out of it.

## The criteria

**Evidences:** DEPL-dSealedTally-4

- AC1 — MET, OBSERVED — `python tools/govkit/selftest.py` drives `index_read` against a directory
  that is not a repository and asserts it RAISES rather than reporting every path absent.
- AC2 — MET, OBSERVED — the same `[-ST4]` arms assert the refusal names the exit code and the
  chunk's first path, and states what the caller would OTHERWISE have concluded.
- AC3 — MET — `python tools/govkit/selftest.py` returns all-green at 1087 arms, so an ordinary read
  over a healthy fixture behaves as it did at base `0f19429a`; the eight in-place callers are the
  evidence.
- AC4 — MET, OBSERVED — an `[-ST4]` arm passes an EMPTY path list and asserts empty maps with no
  git invocation. The `if not chunk` guard is not what handles that: the chunking loop does not
  execute at all, which is what L1 corrected in rev-2.
- AC5 — MET, OBSERVED BY STAGED BREAK — removing the returncode check from `tools/govkit/govkit.py`
  and re-running reds EXACTLY the three arms that grade the raise, while AC4's empty-list arm and all three AC6 filter arms stay
  green. That split proves the break is in the check rather than in the filter.
- AC6 — MET, OBSERVED — `[-ST4]` arms assert an out-of-tree path does not raise, is absent from both
  return values, AND that the in-tree path beside it is really found. The third is the liveness
  half: without it a filter that dropped everything would pass.
- AC7 — MET, OBSERVED BY STAGED BREAK — the `python tools/govkit/selftest.py` run without the
  filter is recorded, and it redded the `[-11]` escape arm. That is not a hypothetical mutation; it is how the constraint was found.

## Residue

The mid-write caller at the rename-destination probe catches `Refusal` and fails the row rather than
aborting a part-written target. **Nothing observes that catch.** Building the fixture needs an
in-tree path that makes `git ls-files` fail during the write walk, and the levers available here —
a non-repository target, an out-of-tree path — are both excluded by the time the walk runs: the
first cannot reach the walk, the second is now filtered. Recorded rather than claimed; the same
shape of gap as `DEPL-dSealedTally-2`'s AC5.

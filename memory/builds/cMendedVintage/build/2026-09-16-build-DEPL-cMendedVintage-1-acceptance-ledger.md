# cMendedVintage — the acceptance ledger for DEPL-cMendedVintage-1

**Serves:** journal DEPL-cMendedVintage-1

*Node `c`, 2026-09-16. BACK-FILLED, not written by the pass that built the unit: it is taken from
that unit's own commits — `5605591736cb` and the rev-3 follow-up `03ba97f196a8` — whose messages
record what the pass measured, and from the arms and engine those commits left in the tree. Where a
commit names a run and its result, that is cited AS the commit's record. Where nothing in the tree
evidences a criterion, this file says so rather than inventing a run. No merge bar, no `*.test.sh`
and no `govkit selftest` ran in the build pass, by its own mandate, and none ran to write this.*

## The one thing worth reading twice

**The RED was observed first, on a fixture that had to be built for it.** Commit `5605591736cb` and
the fixture's own header record the same measurement: against the engine with this unit not landed,
`update --write` printed `ROLLED BACK`, reverted `tools/stale/conf.txt` to its pre-run blob, wrote
`update-rollback-stale.md`, and printed no decline line at all. That is the wedge the unit closes — a
rolled-back run takes the `if r.problems` arm and withholds the `gov_commit` re-stamp, so the next
run classifies identically and decides identically, which is how two adopters reached five rollbacks
and three kits that could not advance at any number of retries.

**A new fixture was necessary rather than preferred.** `_rr_stale` is empty in every rollback arm
that already existed, because none of their kits ships a `rendered` row, so re-running them would
have graded nothing at all — the `fixture-passes-by-finding-nothing` class the build brief named in
advance.

**Evidences:** DEPL-cMendedVintage-1

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` — driven by a standalone
  fixture over a scratch gov tree whose kit ships a `rendered` row, declares no `[[regenerate]]`,
  and whose `[check]` reds once the render goes a vintage stale. Commit `5605591736cb` records the
  run both ways: against the unfixed engine ROLLED BACK with the bytes reverted, a rollback order
  written and no decline printed; against the fixed one every acceptance arm green. The arms
  labelled `[-1] AC1`, committed to `tools/govkit/selftest.py`, are that run made permanent and
  assert each half separately — the kit printed `DECLINED RED` with both states and both exit codes,
  the index NOT matching the pre-write snapshot, gov's new bytes standing on disk, the receipt row
  keeping this run's `commit`, `update-declined-red-stale.md` written with no `update-rollback-stale.md`
  beside it, and the run still exiting non-zero with `gov_commit` unchanged. Those arms have not
  been executed; see the closing section.
- AC2 — `update-declined-red-stale.md` — the order's first paragraph is the decline string this run
  recorded for that kit, ahead of any merge advice, and the file never says `restored`, because
  nothing was. The writer in `tools/govkit/govkit.py` composes it in that order and names the
  declined step as the thing to fix. The committed arm asserts both halves and guards the second
  against its own vacuity: a missing order file would make a bare not-present test green, which is
  the shape this unit exists to refuse. Same fixture run as AC1.
- AC3 — `_rerender_on` — the gate is gone from the decline print, which now walks every recorded
  decline unconditionally; the two lines above it that count runs and declines stay gated, because
  those are the re-render step's own report and a flag-off run ran nothing. The fixture run printed
  a decline line naming the kit, and `5605591736cb` records that the same fixture against the
  unfixed engine printed none. ONE THING HAS MOVED SINCE: `DEPL-cMendedVintage-7` flipped the flag's
  default on, so the committed arm now pins `GOVKIT_RERENDER=0` to keep asking the flag-off question
  that the build pass answered by stripping the variable from a child environment whose default was
  already off.
- AC4 — `declined red 0` — the verify tally gained the count and prints it including its zero. On
  the fixture's `update --write` the run printed the count at 1 beside `rolled back 0`. The zero
  itself is graded where the four sibling counts are already graded: the new count was added to the
  existing every-tally-prints arm over the `-14` fixture rather than to an arm of its own, so it is
  held to the same rule as its siblings instead of being a new count that nothing holds to it.
- AC5 — `tools/govkit/selftest.py` — the flag-off arm's decline half is inverted in the same commit:
  it keeps its assertion that no regenerate ran and replaces `"DECLINED" not in _pvoff.stdout` with
  a positive assertion that the decline naming that kit IS printed. rev-2 records that the clause
  sat two lines below where rev-1 read it and that the kit it names is `review-harness`; the arm's
  subject is unchanged. OBSERVED IN THE SOURCE, NOT IN A RUN. What the criterion asks — what the arm
  asserts — is readable and was read. What is NOT observed is that the arm passes, which is the risk
  it was written against: S4 makes the decline string appear, and an arm left asserting its absence
  would land this unit on a broken suite. Nothing has run the suite, so that half is owed.

## What this ledger does NOT claim

That the merge bar is green. No leg of it ran in the build pass and none ran here. The gates section
7 names are all owed: `govkit selftest`, `govkit selfcheck`, `govkit refusal join` and
`govkit acceptance matrix`. The first of them owns every arm cited above.

That any committed arm passes. Each arm above stands in for an observation the standalone fixture
made at the shell; none of them has been executed by the suite that will grade them.

A post-unit correction belongs on this unit's record even though it moved no criterion. Commit
`9597176f1865` renamed the fixture helper this unit added: it led with a token the declared verbs
table does not hold, and the offender pin is a two-sided equality, so one new offender redded the
lexicon legs at 984 against a pin of 983. That commit records the measurement rather than inferring
it — a detached worktree at the pre-build commit `4cf0944d` exits 0 at 983, this tree exited 1 at
984, and the single rename returns it to 0 — and records that an earlier attempt to reproduce the
baseline with `git archive` into a fresh `git init` was a DEAD PROBE whose every population read
`0 of 0`, so its non-zero exit meant nothing.

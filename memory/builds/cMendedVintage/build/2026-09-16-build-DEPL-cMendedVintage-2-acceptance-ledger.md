# cMendedVintage — the acceptance ledger for DEPL-cMendedVintage-2

**Serves:** journal DEPL-cMendedVintage-2

*Node `c`, 2026-09-16. BACK-FILLED, not written by the pass that built the unit: it is taken from
that unit's own commits — `9eb0fbe0628d` and the records follow-up `96cab2de9e6d` — whose messages
record what the pass measured, and from the arms and engine those commits left in the tree. Where a
commit names a run and its result, that is cited AS the commit's record. Two of this unit's six
criteria are answered by nothing that ran, and both say so in their own words below rather than
borrowing an observation from a neighbour.*

## The one thing worth reading twice

**The fixture falsified three of this spec's own claims, and the spec moved before the code did.**
rev-3 records all three. A DIRECTORY at the worktree path does NOT make `checkout-index -f` refuse —
git removes a directory in its way and restores the file cleanly, measured on the real engine before
anything was written — so the fixture rev-2 named would have graded an ordinary rollback and passed
for the wrong reason. `checkout-index -f` unlinks before it writes, so on the failing path the
worktree file is ABSENT rather than holding this run's bytes, which is why AC2's disk clause and the
order's line are stated as a disagreement between index and worktree and not as a promise about
which bytes are there. And AC3's filter turned out to be unobservable on any population this tree
can reach.

**The failure had to be manufactured inside the run's own window.** Each of the three plumbing
branches needs the TARGET's git to refuse a call, which nothing outside the run can arrange. The
kit's own `[check]` runs after the write and before the rollback, so it configures a `required`
filter whose smudge command fails and binds the victim path to it; `git checkout-index` then cannot
write that one path. The committed block opens with an arm asserting the branch was really reached,
because without that arm every arm below it grades an ordinary rollback and the whole block is an
assertion about nothing.

**Evidences:** DEPL-cMendedVintage-2

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` — commit `9eb0fbe0628d`
  records this probe as staged red first and then green against the fix. On the fixed engine the
  `r.fail` message names the path and the call that refused it, and the rollback order carries
  `NOT restored tools/demo/victim.txt` under its own verb and under no other — before this unit a
  failed path appeared in none of `restored`, `removed` or `left alone`, which reads as a file the
  rollback never touched. The arms labelled `[-2] AC1` are committed to `tools/govkit/selftest.py`
  and replay exactly that; they have not been executed, and the closing section says why.
- AC2 — `sha256` — after the run the receipt row for the failed path carries this run's `sha256`,
  its `commit` stayed forward with it, and the pre-run row carried neither, so the row describes
  what the run did rather than a state nothing returned to. The worktree does not hold the pre-run
  bytes either. Commit `9eb0fbe0628d` records the RED this was staged against: the row reverted to
  the pre-run `sha256` while the file never came back. The disk half is asserted as a negative
  deliberately, per rev-3 — a refused `checkout-index -f` leaves no file at all, so the positive
  rev-2 asked for is unobservable on the only fixture that reaches this branch.
- AC3 — amended rev-3, and retired rather than observed. The section 9 rev-3 line (d) is the
  record. No reachable snapshot entry mixes a written path with an untouched one: the only two-path
  entry is a `renamed` one whose two spellings enter together or neither does, and a `withdrawn`
  entry carries exactly one path. So no fixture can stage the population, dropping
  `p in written_paths` changes no receipt anywhere in this tree today, and rev-2's claim that it
  would break every successful rollback is false. NOTHING OBSERVES THIS CRITERION AND NOTHING CAN
  from here — the filter ships as a class guard with its reason at the code site, which is what a
  criterion no run can fail is worth. The follow-up `96cab2de9e6d` removed the halves the retirement
  left standing: S2 still routed to AC3 as an observer, and section 4 still said an unfiltered
  predicate would keep every row forward.
- AC4 — `NOT restored` — the order's lead sentence no longer covers the whole document. It is
  narrowed to the restored block with an and-only-those clause, and the sentence after it says that
  any path under the new block is one the rollback could not return at all. The line for the
  `checkout-index` failure carries the half-restored fact — the index was already reverted to the
  pre-run blob, so the index and the worktree now disagree at that path — and it does not say whose
  bytes are on disk, because after a refused checkout nothing in this tool knows. Observed on the
  same probe run AC1 cites, by the arms labelled `[-2] AC4`.
- AC5 — `restored  tools/demo/conf.txt` — HALF OBSERVED, and the halves are worth separating. What
  was observed is the clean path inside the failing run itself: the same rollback that could not
  return the victim path still put this one back and reverted its receipt row to the pre-run
  `sha256`, so the gate fires on the failed entry and on nothing else. What was NOT observed is the
  criterion as it is written — the two arms it names, the `-14` rollback fixture and the landing
  fixture, were never executed, because no suite ran in the build pass and none ran here. Until
  `govkit selftest` runs, nothing has confirmed those arms are still green.
- AC6 — amended rev-3, and nothing in the tree evidences it. The section 9 rev-3 line (c) is the
  record: rev-2 called this case cheap to stage and it is not, so the criterion's own fixture clause
  now reads NONE. Reaching the line needs a receipt row whose path escapes the target AND a verdict
  touching enough to enter the snapshot rows, which the receipt-integrity preamble is built to
  refuse before the rollback is ever reached. The containment sentence therefore ships class-guarded
  — the block is assembled per path from the predicate that decided that path's fate, never from
  `unrestored` as one list — on exactly the footing the refusal it reports on already declares for
  itself. The branch count is held by `govkit refusal join` on the owed bar; this sentence is held
  by nothing, and that is the claim, not a gap to be smoothed over.

## What this ledger does NOT claim

That the merge bar is green. No leg of it ran in the build pass and none ran here. The gates section
7 names are all owed: `govkit selftest`, `govkit selfcheck`, `govkit refusal join` and
`govkit acceptance matrix`.

That the other three restore-failure branches are covered. The fixture reaches `git checkout-index`
and nothing else. The `git rm --cached` and `git update-index` failures each got their list append
in this unit and neither has an arm, for the same reason their own header already gave; the
containment refusal is AC6's, and has none either.

That any adopter was touched or measured. Nothing outside this repo's scratch fixtures was run.

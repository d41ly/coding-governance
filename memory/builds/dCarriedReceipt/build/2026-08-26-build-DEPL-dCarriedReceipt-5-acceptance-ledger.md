# Acceptance ledger — DEPL-dCarriedReceipt-5, the `[[decline]]` contract

**Serves:** journal DEPL-dCarriedReceipt-5

Built on node `a` under session slug `aResumedRelay`, immediately behind the coverage unit it reads.

**Evidences:** DEPL-dCarriedReceipt-5
- AC1 — `git show <pre-coverage>:tools/govkit/govkit.py | grep -c decline` — RED observed on the
  engine as it stood before this build's coverage unit: exactly one hit, in an unrelated comment
  about what `apply` prints when it declines a RULE. No reader of a `[[decline]]` block existed, so
  an owner decision written into `deploy.toml` was parsed and ignored. It cannot be re-observed now
  without removing the reader; two arms hold the GREEN instead — the engine reads the block, and
  the evidence set is a closed module constant rather than a check spelled per call site.
- AC2 — `tools/govkit/selftest.py` — an empty `why` reds naming the kit and the dest, in the words
  the exemption hygiene already uses one level up, and the row excuses nothing: its gap is still
  counted. Both halves asserted, because a red that still hid the row would be the worse failure.
- AC3 — `tools/govkit/selftest.py` — a decline whose `dest` the target now tracks reds as stale and
  the message says the file arrived, asserted on that phrase rather than on the exit code.
- AC4 — `tools/govkit/selftest.py` — a decline naming a destination no claimed kit ships reds as
  stale with `gov has withdrawn it`. This is the arm that makes the list self-cleaning; without it
  a decline outlives the thing it declined and quietly widens the surface it narrowed.
- AC5 — `tools/govkit/selftest.py` — `taken_as` whose index blob equals gov's blob reports
  `declined` and drops out of the gap count; one byte changed reports `diverged` and **the exit
  code does not move**. The second half is the load-bearing one: redding a local edit would red the
  honest adopter who relocated a file and then edited it, whose only route back to green is
  deleting the decline — the exclusion list eating the evidence that made it trustworthy.
- AC6 — `tools/govkit/selftest.py` — a `taken_as` differing from gov's blob ONLY in line endings
  still reports `declined`, and the arm asserts `diverged` is absent so it cannot pass by reporting
  both. This is the arm that fails against a plain `_sha` comparison and is why `_sha_nocr` exists
  as its own function rather than as a flag on the existing one.
- AC7 — `tools/govkit/selftest.py` — `consumed_into` naming a tracked path passes; naming an
  untracked one reds. Deliberately weak by design: gov cannot know what "folded into" means
  byte-wise, and a predicate that pretended to would pass on everything.
- AC8 — `tools/govkit/selftest.py` — a discharge exiting 0 reports `discharged`, exiting 1 reports
  `undischarged`, and an unresolved `{token}` refuses by name rather than running. Three arms, one
  per outcome, through the same runner a `[[hole]]` probe already uses — no second execution path.
- AC9 — `tools/govkit/selftest.py` — two evidence fields red on the one-field rule, naming both.
  The fixture makes each field individually VALID, so an implementation that graded them first and
  complained second would pass every other arm and fail only this one.
- AC10 — amended rev-5 — the frozen-fixture gap, declared and residual counts are struck; the
  arithmetic replaces them and is gated in three arms: declining rows moves them out of the gap
  count one for one, the write-row total does not move, and the declined count rises to match.
  **The live reading**, against the index-only inCMS mirror described in `-4`'s ledger: declaring
  the eight rows inCMS's own `kits.json` records as vendored under its workflow paths moved the
  reading from **gap 76 of 136** to **gap 68 of 136, 8 declined**, exit 0, total unchanged. Every
  one of the eight reported `diverged` rather than `declined` — inCMS's copies carry local edits,
  and three are marked `diverged` in its own kits.json — so the reclassification is not a
  hypothetical: it is what the first real decline set does, and it kept every row visible with its
  reason instead of redding a run over an adopter's sanctioned edits. Nothing was written into
  `C:/projects/incms`; the declines were written into the scratch mirror.

Five arms beyond the criteria, one per refusal branch that serves none: a row with no `kit` or no
`dest`, a `kit` outside the run's selection, a `taken_as` the target does not track, a `discharge`
with no command, and a discharge probe that cannot LAUNCH. Those five would otherwise ship
unasserted, which is what the refusal join exists to prevent. Two more hold S7's second call site by
OBSERVATION rather than by reading the source: the same stale fixture reds in `check` and in
`plan --coverage`, so neither verb can excuse what the other refuses.

`BRANCH_PIN` moved 197 → 208, both values named in that file's own header. Eleven new branches
rather than the seven §7 estimated — re-derived at landing, which is what §7 asked for.

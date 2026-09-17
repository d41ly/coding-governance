# Build brief — DEPL-cMendedVintage-18

**Serves:** journal DEPL-cMendedVintage-18

Read the spec whole first. This repairs an assumption `DEPL-cMendedVintage-2` made earlier in this
same build, and the failure it leaves behind is data loss in a target's receipt.

*Standing note: eighteen briefs in this build carried a figure or mechanism measurement disproved,
and every one of the last eleven units amended its own spec mid-build after measuring. The last one
found an acceptance criterion that graded a branch belonging to a different unit and would have
stayed green with its own case deleted. Treat this as evidence, not authority.*

## The defect, and why it is the worst-shaped one left

One gate covers two effects. `DEPL-cMendedVintage-2` gated the `withdrawn_rows.remove` together with
the `ROLLBACK_FIELDS` revert on the assumption that no snapshot entry is also a withdrawn row.
`_touching` admits `withdrawn` whenever `--write-withdrawals` is passed, so on those runs the
assumption is false.

`withdrawn_rows` is the DELETE list. Skipping the removal deletes the row from the receipt for a path
the rollback could NOT return — so the file stays on disk and nothing in the receipt claims it. That
is the same shape `DEPL-cMendedVintage-15` fixed for the `.gitattributes` block: gov's bytes in a
repository gov no longer admits to owning.

## S2 will feel backwards, and it is correct

A withdrawn-and-unrestored row keeps THIS run's field values, not its pre-run ones. The invariant is
that the row describes the bytes on disk, and the bytes did not go back. Reverting the fields would
make the receipt describe a state that does not exist.

## S4 is the half worth the most, so do not shrink it

The invariant is one level up and over EVERY arm that exercises a rollback, not over your fixture: no
path may end a run both absent from the receipt's `files[]` and present in the worktree. Gate the
CLASS. Fixing one path and asserting over that one path certifies coverage you do not have, which is
the same could-not-fail shape one level up.

Run it over the existing arms before you rely on it and report what it finds — if it reds an arm
nobody was thinking about, that is a finding, not an obstacle.

## Every line number in the spec is stale, badly

It names `tools/govkit/govkit.py:7666`, `:6692` and `:7818`. Eight units have edited that file since
this spec was written, several of them in the rollback and snapshot code specifically —
`DEPL-cMendedVintage-13`, `-21` and `-14` all landed there within the last few hours. Locate every
site by symbol and by the text the spec quotes. A line-keyed read that lands one block over, in code
that decides what gets deleted, is not a bug you will notice.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`selftest.py` or `matrix.py` — that class has landed twice in this build, both in test-side helpers,
and three specs have since proposed non-conforming names that `--suggest` corrected. Spell no
`tools/<kit>/…` path in shipped prose or comments.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo — each needs a scratch fixture target under the run's scratch root. Write the
acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-18-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape, spelled out, because my earlier briefs got it wrong and two units redded.**
`memory/HYGIENE.md` gives the canonical form as `- AC1 — ``<token>`` — what was observed`: the
backticked witness sits on the bullet's FIRST line, immediately after the label. Check 23 reads form
from that first line only, so a bullet whose witness sits on a continuation line below it is graded
`bad` however tidy it looks. The token must also share content with the criterion's own backticked
token, case-folded, either way round. Check 23 is HELD under `--staged`, so the commit hook will not
tell you.

Re-declare with `--dispatch` if your write set grows; it refuses a declaration naming `RUN.md`. Bound
every command at 900s or more.

# Pre-code review, round 5 — part 1 of 2, the engine and safety units, DEPL-dCarriedReceipt-1..8

**Serves:** spec-audit DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8

**Reviewed:** all 15 specs plus the build README, against the round-4 fold at `8e98a381`.
**Base:** `8e98a381`. Source read at `9ddcc5c9`; `tools/govkit/govkit.py` is byte-identical between
the two, so every line citation holds at either sha.
**Harness:** five primed finder lenses over the fold diff (fold fidelity, fold collateral, citation
integrity, residual contradiction, acceptance observability), then batched default-refute skeptics,
then one synthesis. Eleven agents, all returned. Seventeen confirmed entries arrived; deduplicated
they are the 11 defects across both parts, and 21 were refuted.
**Scope:** this round audits the FOLD, not the design. Every finding is either a round-4 edit that
landed wrong, or collateral the fold created while landing a correct one.
**Why two parts:** the Serves id list renders into one build-README row and 15 ids blow its entry
cap. That is DEPL-dCarriedReceipt-16; rounds 1 and 4 split on the same boundary.

This record carries the findings against units 1-8. Units 9-15 are part 2,
`2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md`, which carries the convergence answer, the
blocker and the fork ruling. Two of part 2's findings land edits inside THIS half: B1 rewrites
`-7` S1 and adds a fourth arm to `-7` S9, and H2 corrects `-7` §4's `sha256` dictionary entry.

## Verdict: BLOCKED

One blocker, B1, down from three. It lands edits in `-7` and in `-13`, and it is carried in
part 2 with the convergence answer.

## Low

**L1 — `-4`'s rev-4 entry records a two-line `--kits` split the file does not have, and argues a future fold back into the break.**
*Unit: `-4` §9 rev-4 (:185-189) against §6 AC2 (:140-142). Provenance: round-4 part 1 L6.*

The rev-4 entry reads: "It is re-indented two spaces. The value is 193 columns on one line, so it is split at a comma across two indented lines; the wider of the two is 104 columns, which no two-line split of that value gets under, and de-indenting is what this finding refuses."

Measured: AC2's command spans lines 140-142; line 141 ends at `--kits` and line 142 carries the entire `check-install-prefix,…,review-harness` value on ONE indented line, 195 columns wide. `cat -A` confirms the two-space indent and no comma break anywhere. The split was made and then reverted inside the same commit, correctly — the fold's own message records why: "splitting AC2's `--kits` value put a newline inside an inline code span, so the 'FULL command' stopped being one shell argument."

So the revision log records as done the one edit the same commit undid, and asserts a measurement ("the wider of the two is 104 columns") about text that does not exist. This is not a historical round label — rev-4 is the current revision describing itself. No line-length gate covers `memory/` prose, so nothing else catches a re-break.

**Edit:** replace rev-4's second and third sentences with *"It is re-indented two spaces and deliberately left on ONE line. A split at a comma was tried and withdrawn: the value sits inside the multi-line inline code span that IS the FULL command, and a newline mid-value breaks it. The line is 195 columns and stays that way — the over-width line is the narrower defect, and de-indenting is what this finding refuses."*

---

## What remains unverified

Stated plainly, because a green convergence answer over unmeasurable ground would be worth nothing.

- **`-9` AC2's `13` pairs and `26` needles cannot be closed in this tree.** They must be measured over inCMS at `2cff5855`, a population this repo does not contain. Round 5 could not verify or falsify them either, and neither could round 4's fold. The spec's flag is the honest state; it stays a DoR item for whoever has that checkout.
- **`-6` AC6's and `-4` AC3's inCMS readings depend on a descriptor this build does not write.** `ABL-dPinnedVintage-1` lands `.governance/deploy.toml` in `d41ly/incms`, outside this build's carry, and both criteria's `[kit.*]` layout overrides are only checkable there.
- **F5 is an agent inference the owner has not ratified.** `-13` F5 says so itself — "Recorded as the round-4 reviewer's inference from those three instruments rather than as a measured fact, and flagged there as a decision the owner should ratify." H2 above makes the definition consistent; it does not make it ratified, and one of F5's three instruments is removed by `-8` before `adopt` ever runs.
- **B1's remedy is an owner fork and this record does not pick.** Direction A costs S9 its field-presence purity; direction B adds two fields to a row class whose bytes gov does not own. Both close the refusal; they say different things about what a merged row means.
- **No arm has ever been run.** All 15 specs are SPECCED, every line citation is a source read at `9ddcc5c9`, and no gate, selftest or `refusal_join.py` arm in this build has been observed either green or red. In particular B1's refusal has been derived from source and from the two kit descriptors, not reproduced by running `update` against a target carrying a merged row — that reproduction is the cheapest way to confirm this record's blocker and is worth doing before folding it.
- **The AC13/AC14 fixture family exists only as a §4 estimate.** `-13` §4 is headed "Files touched (estimate)" and declares one family carrying verbatim, `eol`, `relocate`, unattributable, declared-forked, one `[[lf_pin]]`, one merged rule and one ambiguous gov directory. Whether one family can carry all of that without arms interfering is unmeasured, and three round-5 findings turn on which fixture a criterion runs over.
- **One observation outside the confirmed set, flagged as such.** `-13` §9's rev-4 entry labels itself "round-5 fold" while rev-5 labels itself "round-4 fold"; rev-4 was written by commit `2f9d7a4f`, the third-round fold, so the label is wrong and inverted against its neighbour. It is pre-fold text this round's subject never touched, no skeptic verified it, and it is recorded here only so round 6 does not spend a lens rediscovering it.

# TOOL-dFairHearing-1 deviation 11 — the known-set file holds the 6 escapes beside the 59 reviewed defects

**Serves:** deviation TOOL-dFairHearing-1

- **Departs from:** `cl-dClosedLoop-0068@b4e6c04e`
- **Hand-off:** design-to-spec
- **Before:** the owed replays first: the design-audit preset run blind at blob 767187aa, from a bundle of the history to 6cfd21619 cloned outside the repository, scored by `review_replay.py` against a known-set file of all 59 known defects, each with its address, grade and escape flag, counting each matched defect once, at 45 of 59 known defects, 4 of 6 escapes and 7 of 8 highs in each run
- **After:** the same replays, scored by `review_replay.py` against a known-set file of 65 rows, the 59 defects the two baseline rounds confirmed with `escaped` `no` and the 6 escapes with `escaped` `yes`, each with its address and grade, counting each matched defect once, at 45 of the 59 reviewed rows, 4 of the 6 escaped rows and 7 of the 8 high rows in each run
- **Cause:** design defect
- **Reason:** No escape is among the 59. The 59 are the comparison record's confirmed defects, every one found by run A or run B, and an escape is by the records' own definition a defect found after both rounds, so an escape flag on those 59 rows could never be set and "4 of 6 escapes" could never be scored. Holding the 6 as rows of their own is the one reading under which all three of the clause's counts are measurable, and it leaves the 45-of-59 count exactly as the clause states it.
- **Evidence:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md:80-81` (59 confirmed defects) and its `[map]` (:162-224), which places no escape; its `[neither]` (:226-245), the four defects found while folding; `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md:102-109`, which counts those four and the floor probe's two as the six escapes; TOOL-dFairHearing-1 §8 F1, S1 and AC1
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dFairHearing's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0068@b4e6c04e
- **Caused-by:** PLAY-dClosedLoop-1

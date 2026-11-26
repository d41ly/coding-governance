# TOOL-aPrunedIndex-20 deviation 1 — AC5 accepted on its readings with the gauge band unmet

**Serves:** deviation TOOL-aPrunedIndex-20

- **Departs from:** `TOOL-aPrunedIndex-20@rev-2` [AC5]
- **Hand-off:** code-to-record
- **Before:** AC5 is green only on a timing set whose load gauges lie within 1.5x of each other. Three out-of-band sets are red, and a red set writes neither the budget row nor the evidence row.
- **After:** AC5 stands accepted on its three recorded sets, every one outside the 1.5x gauge band. The spec retakes an out-of-band set rather than grading it, so no set was graded, and the owner's ruling accepts the readings as they stand. The ungraded sets also cross one of AC5's other bounds: set 2's ratio is 82.6/108.6 = 0.76, over the 0.75 bound. Sets 1 and 3 have ratios of 0.57 and 0.58. Every reading exited 0 with `PASS — the tag plants, 14 rows` under the 300 s ceiling. No budget or evidence row is written. Every after-reading, the most 104.7 s, sits under the 159 s budget row. One before-reading, 181.4 s on the tree without this unit, is over it. The owner saw these figures in the building session's table (AC5: 102 to 181 s before, 66 to 105 s after, ratio 0.57 to 0.76).
- **Cause:** owner ruling
- **Reason:** other sessions loaded the node throughout, and the gauge swung 3 to 10 times within every set, so no set could meet the band. The owner accepted the readings rather than waiting for a quiet node.
- **Evidence:** the AC5 line of `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md`, and the owner's words in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`.
- **Risk:** loosening
- **Approver:** owner, in the building session on 2026-11-26, quoted in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`
- **Follow-through:** ask TOOL-aPrunedIndex-18
- **Caused-by:** 2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver

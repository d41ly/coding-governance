# TOOL-aPrunedIndex-17 deviation 1 — AC8 accepted on its readings with the gauge band unmet

**Serves:** deviation TOOL-aPrunedIndex-17

- **Departs from:** `TOOL-aPrunedIndex-17@rev-4` [AC8]
- **Hand-off:** code-to-record
- **Before:** AC8 is green only on a timing set whose load gauges lie within 1.5x of each other. Three out-of-band sets are red, and a red set writes neither the budget row nor the evidence row.
- **After:** AC8 stands accepted on its three recorded sets, every one outside the 1.5x gauge band. The spec retakes an out-of-band set rather than grading it, so no set was graded, and the owner's ruling accepts the readings as they stand. The ungraded sets also cross AC8's other bounds. Set 3's ratio is 132.0/139.5 = 0.95, over the 0.90 bound, and its worst after-reading of 132.0 s is over the 106 s cap. Sets 1 and 2 have ratios of 0.80 and 0.82 and worst after-readings of 90.0 s and 80.7 s. Every reading exited 0 with `PASS — the tag plants, 14 rows` under the 300 s ceiling. No budget or evidence row is written: unit 17's worst after-reading of 132.0 s sits under the 159 s budget row. The owner saw these figures in the building session's table (AC8: 79 to 140 s before, 68 to 132 s after, ratio 0.80 to 0.95). (PINNED, 2026-11-26)
- **Cause:** owner ruling
- **Reason:** other sessions loaded the node throughout, and the gauge swung 3 to 10 times within every set, so no set could meet the band. The owner accepted the readings rather than waiting for a quiet node.
- **Evidence:** the AC8 line of `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md`, and the owner's words in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`.
- **Risk:** loosening
- **Approver:** owner, in the building session on 2026-11-26, quoted in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`
- **Follow-through:** ask TOOL-aPrunedIndex-18
- **Caused-by:** 2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver

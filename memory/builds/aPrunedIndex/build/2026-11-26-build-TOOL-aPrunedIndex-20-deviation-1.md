# TOOL-aPrunedIndex-20 deviation 1 — AC5 accepted on its readings with the gauge band unmet

**Serves:** deviation TOOL-aPrunedIndex-20

- **Departs from:** `TOOL-aPrunedIndex-20@rev-2` [AC5]
- **Hand-off:** code-to-record
- **Before:** AC5 is green only on a timing set whose load gauges lie within 1.5x of each other. Three out-of-band sets are red, and a red set writes neither the budget row nor the evidence row.
- **After:** AC5 stands accepted on its three recorded sets. Every reading exited 0 with `PASS — the tag plants, 14 rows` under the 300 s ceiling, and the after/before ratios were 0.57 to 0.76 against its 0.75 bound. The gauge band was not met. Neither row is written: the 159 s budget row already covers the worst reading of 104.7 s on the full tree.
- **Cause:** owner ruling
- **Reason:** other sessions loaded the node throughout, and the gauge swung 3 to 10 times within every set, so no set could meet the band. The owner accepted the readings rather than waiting for a quiet node.
- **Evidence:** the AC5 line of `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md`, and the owner's words in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`.
- **Risk:** loosening
- **Approver:** owner, in the building session on 2026-11-26, quoted in `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md`
- **Follow-through:** ask TOOL-aPrunedIndex-18
- **Caused-by:** 2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver

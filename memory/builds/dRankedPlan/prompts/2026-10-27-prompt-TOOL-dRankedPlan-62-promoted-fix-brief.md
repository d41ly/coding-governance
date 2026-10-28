**Serves:** research TOOL-dRankedPlan-62

# Promoted-fix brief — dRankedPlan, the one check-spec-tokens hit on the round-5 promotions

The round-5 spec audit's disposal (run `wf_00dd7d9e-308`) authored `TOOL-dRankedPlan-53` to `-62`. The main loop ran
`tools/check-spec-tokens.py`: one hit. Fix exactly it, in place, changing no status header, `**Carries:**` line, §3
edge or §8 mark. Commit nothing, and return what you changed.

1. check-spec-tokens `[path]` · `2026-10-27-spec-TOOL-dRankedPlan-62.md` cites `tools/loop/ratify.py` where the checker
   grades paths (§6), and it is not tracked at HEAD. Cite it by basename in §6 (`ratify.py`, the loop kit's), keeping
   the full path in §2, §4 and Files touched.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file.

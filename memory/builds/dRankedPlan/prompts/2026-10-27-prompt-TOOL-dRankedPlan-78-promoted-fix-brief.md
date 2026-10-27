**Serves:** research TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-81

# Promoted-fix brief — dRankedPlan, the check-spec-tokens hits on the round-8 promotions

The round-8 spec audit's disposal (run `wf_e43c04d4-261`), the last audit round by the owner's ruling, authored
`TOOL-dRankedPlan-78` to `-81`. The main loop ran `tools/check-spec-tokens.py`: the hits below; hygiene read clean.
Fix exactly these, in place, changing no status header, `**Carries:**` line, §3 edge or §8 mark. Commit nothing, and
return each hit with what you changed.

1. check-spec-tokens `[bar]` · `2026-10-27-spec-TOOL-dRankedPlan-78.md`, `-79.md` and `-81.md` each name `selftest.py`
   as an acceptance observation in §6. A suite is not one: observe the unit's own code on a staged break or a fixture
   in §6 (a probe of the function the criterion grades, run on a planted input), and name the suite on a `New arm:`
   line in §7 if it is not there already.
2. check-spec-tokens `[path]` · the same three specs cite `tools/loop/ratify.py` where the checker grades paths (§6),
   and it is not tracked at HEAD. Cite it by basename in §6 (the loop kit's `ratify.py`), keeping the full path in §2,
   §4 and Files touched.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file.

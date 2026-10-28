**Serves:** research TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77

# Promoted-fix brief — dRankedPlan, the checks' hits on the round-7 promotions

The round-7 spec audit's disposal (run `wf_8ecbf04c-3c4`) authored `TOOL-dRankedPlan-68` to `-77`. The main loop ran
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25` and `tools/check-spec-tokens.py`: the hits below.
Fix exactly these, in place, changing no status header, `**Carries:**` line, §3 edge or §8 mark. Commit nothing, and
return each hit with what you changed.

1. Hygiene check 25 · `2026-10-27-spec-TOOL-dRankedPlan-70.md` and `-77.md` · a §2 item retires a named thing (or reads
   as one: check 25 reads any retirement word — "drops", "dropped", "retired", "replaces", "replaced", "removes",
   "removed", "deleted" — beside a backticked token) and carries no `**Readers:**` clause. Where the item truly retires
   the thing, add a `**Readers:**` clause answering `by name:` with every reader that spells the name and `by value:`
   with every reader of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the tree. Where it
   does not retire anything, reword the item so no retirement word sits beside a backticked token.
2. check-spec-tokens `[path]` · `2026-10-27-spec-TOOL-dRankedPlan-70.md` and `-74.md` cite `tools/loop/ratify.py` where
   the checker grades paths (§6), and it is not tracked at HEAD. Cite it by basename in §6 (the loop kit's
   `ratify.py`), keeping the full path in §2, §4 and Files touched.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file.

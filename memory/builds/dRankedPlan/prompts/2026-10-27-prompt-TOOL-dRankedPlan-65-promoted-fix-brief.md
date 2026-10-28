**Serves:** research TOOL-dRankedPlan-65

# Promoted-fix brief — dRankedPlan, the one hygiene hit on the round-6 promotions

The round-6 spec audit's disposal (run `wf_e14f7014-e3e`) authored `TOOL-dRankedPlan-63` to `-67`. The main loop ran
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25` and `tools/check-spec-tokens.py`: one hit, below;
check-spec-tokens read 0. Fix exactly it, in place, changing no status header, `**Carries:**` line, §3 edge or §8 mark.
Commit nothing, and return what you changed.

1. Hygiene check 25 · `2026-10-27-spec-TOOL-dRankedPlan-65.md` · a §2 item retires a named thing (or reads as one:
   check 25 reads any retirement word — "drops", "dropped", "retired", "replaces", "replaced", "removes", "removed",
   "deleted" — beside a backticked token) and carries no `**Readers:**` clause. Where the item truly retires the
   thing, add a `**Readers:**` clause answering `by name:` with every reader that spells the name and `by value:`
   with every reader of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the tree. Where
   it does not retire anything, reword the item so no retirement word sits beside a backticked token.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file.

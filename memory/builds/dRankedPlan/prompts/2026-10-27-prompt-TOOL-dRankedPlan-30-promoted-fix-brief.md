**Serves:** research TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37

# Promoted-fix brief — dRankedPlan, the checks' hits on the round-2 promotions

The round-2 spec audit's disposal (run `wf_d7d7d790-af4`) authored `TOOL-dRankedPlan-30` to `-37` and folded their
hands-off edges. The main loop then ran `bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25` and
`tools/check-spec-tokens.py`: the hits below, every one on a promoted spec. Fix exactly these, in place, keeping every
`**Carries:**` line, §3 edge and §8 mark as it stands unless a hit says otherwise. The promoted specs are uncommitted:
change no status header. Commit nothing, and return each hit with what you changed. The spec brief,
`memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md`, still binds every rule.

## The hits

1. Hygiene check 25 · `2026-10-27-spec-TOOL-dRankedPlan-32.md`, `-33.md` and `-37.md` · a §2 item retires a named
   thing (or reads as one: check 25 reads any retirement word — "drops", "retired", "replaces", "removes" — beside a
   backticked token) and carries no `**Readers:**` clause. Where the item truly retires the thing, add a
   `**Readers:**` clause answering `by name:` with every reader that spells the name and `by value:` with every reader
   of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the tree (a reader that does not
   exist yet because a parent has not built it is named with the spec that builds it). Where it does not retire
   anything, reword the item so no retirement word sits beside a backticked token.
2. check-spec-tokens `[handoff]` · `2026-10-27-spec-TOOL-dRankedPlan-32.md` hands the token `ratify.py "$slug"` to
   `TOOL-dRankedPlan-37`, whose spec never names it. Either unit 37 truly reads that invocation — then name it there,
   in backticks, where it reads it — or it does not, and unit 32's bullet is corrected. Say which.
3. check-spec-tokens `[path]` · `2026-10-27-spec-TOOL-dRankedPlan-37.md` cites `{prefix}/loop/ratify.py`,
   `{prefix}/memory-tree/plan_fields.py` and `{prefix}/memory-tree/plan_record.py` where the checker grades paths
   (§6), and none is tracked at HEAD. Cite each by basename in §6 (`ratify.py`), keeping the full repository path in
   §2, §4 and Files touched.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file. The main loop re-runs `check-spec-tokens.py` after you return.

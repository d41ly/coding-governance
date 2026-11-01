**Serves:** research TOOL-dRankedPlan-38 TOOL-dRankedPlan-41 TOOL-dRankedPlan-45

# Promoted-fix brief — dRankedPlan, the checks' hits on the round-3 promotions

The round-3 spec audit's disposal (run `wf_9005b2b5-c5a`) authored `TOOL-dRankedPlan-38` to `-45` and folded their
hands-off edges. The main loop then ran `bash tools/memory-tree/check-memory-hygiene.sh --only 2,5,12,21,25` and
`tools/check-spec-tokens.py`: the hits below, every one on a promoted spec. Fix exactly these, in place, keeping every
`**Carries:**` line, §3 edge and §8 mark as it stands unless a hit says otherwise. The promoted specs are uncommitted:
change no status header. Commit nothing, and return each hit with what you changed. The spec brief,
`memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md`, still binds every rule.

## The hits

1. Hygiene check 25 · `2026-10-27-spec-TOOL-dRankedPlan-41.md` and `-45.md` · a §2 item retires a named thing (or reads
   as one: check 25 reads any retirement word — "drops", "dropped", "retired", "replaces", "removes" — beside a
   backticked token) and carries no `**Readers:**` clause. Where the item truly retires the thing, add a `**Readers:**`
   clause answering `by name:` with every reader that spells the name and `by value:` with every reader of its value,
   or `NO VALUE READERS` and a reason, each found by `git grep` over the tree. Where it does not retire anything,
   reword the item so no retirement word sits beside a backticked token.
2. check-spec-tokens `[bar]` · `2026-10-27-spec-TOOL-dRankedPlan-45.md` names `.githooks/pre_push_bar_selftest.py` as an
   acceptance observation. A suite is not one: observe the unit's own code on a staged break or a fixture in §6, and
   name the suite on a `New arm:` line in §7.
3. check-spec-tokens `[guards]` · `2026-10-27-spec-TOOL-dRankedPlan-45.md` §4 Files touched names `tools/gate-legs.json`,
   which trips the guard of the leg `run-gates canary`, absent from the §7 leg line. If the unit truly edits that file,
   add `run-gates canary`, spelled as `tools/gate-legs.json` names it, to the §7 leg line; if it does not, name the file
   it does edit.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file. The main loop re-runs `check-spec-tokens.py` after you return.

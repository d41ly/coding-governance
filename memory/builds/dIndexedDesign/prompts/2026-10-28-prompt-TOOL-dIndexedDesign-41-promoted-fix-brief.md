**Serves:** research TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-46

# Fix brief — dIndexedDesign, the round-2 promotions' check findings before their commit

The round-2 spec audit of `unattended-build.js` run `wf_979ec72c-b6f` (record
`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md`) promoted its
findings into eight new specs, `TOOL-dIndexedDesign-39` to `-46`. The main loop ran the memory hygiene gate and
`tools/check-spec-tokens.py` over the staged set, and the findings below are the whole remainder. Fix each in the file
it names, and nothing else; your handoff names the one unit you may write, so fix only that unit's findings. The
promoted specs are uncommitted rev-1 drafts: edit them in place, with no rev bump and no §9 line. Do not commit and do
not run the build-index generator.

Read `memory/builds/dIndexedDesign/prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md` "Every spec" and
"What the last spec runs had to fix" first; each finding below breaks one of its rules.

## TOOL-dIndexedDesign-41

1. §4 Files touched names `memory/builds/dIndexedDesign/build/`, which trips the guards of the legs `recall floor` and
   `recall floor arms`, absent from the §7 leg line. Either add both legs, spelled exactly so, to the §7 leg line, or,
   where the build folder is a record the unit writes rather than a product path, name the record file it writes
   instead of the folder so no guard is tripped. Say which you chose.

## TOOL-dIndexedDesign-46

2. §6 cites `tools/loop/loop.toml` (line 303) and `tools/workflows/replay_scorer.py` (AC14, line 317) by full path; neither
   exists at HEAD, so `check-spec-tokens.py` reds each as untracked. In §6 cite a file a parent or this build will
   create by its basename (`loop.toml`, `replay_scorer.py`) and keep its full path in §2, §4 and Files touched.
3. Hygiene check 25: scope items S7 and S12 retire a named thing and carry no `**Readers:**` clause. Write one per
   item: `**Readers:**`, then `by name:` and every reader that spells the name, then `by value:` and every reader of
   its value or `NO VALUE READERS` with the reason, each reader found by `git grep` over the tree and cited by path
   in backticks. Where the retired thing does not exist at HEAD, check 25's `READER NOT IN TREE` form is the answer.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against a private copy of the git
index in your scratch path, and return each finding fixed, by number, with the file and the change.

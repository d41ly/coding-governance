**Serves:** research TOOL-dTotalRecall-67

# Round-5 fix brief — dTotalRecall, the checks the round-5 promotions owe before their commit

The round-5 spec audit's disposal (`unattended-build.js` run `wf_8896c5e9-a1f`) wrote the promoted specs
TOOL-dTotalRecall-67 to -70 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Clear every finding below, changing nothing else in any spec's design, so that
`python tools/check-spec-tokens.py` prints no dTotalRecall hit and `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file.

- Units 67 to 70 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and Files
touched. A backticked `<rev>:<path>` (even `<rev>:./name`) is read as a path: cite the revision and the basename apart,
e.g. "`git show 462d20f3` of `tree_lib.py`, run from `tools/memory-tree/`". The hits:
- unit 68: `memory/project/census-kept-paths.txt`
- unit 70: `tools/memory-tree/record_causes.py`, `tools/memory-tree/record_kinds.py`,
  `memory/project/census-kept-paths.txt`, `462d20f3:./tree_lib.py`, `commit>:./legacy-records.txt`

## F2 · a Readers clause with an empty by-value half

Hygiene check 25 reds unit 70's S8: its `**Readers:**` clause's `by value:` half names no backticked reader and carries
no `NO VALUE READERS` with a reason. Name each reader of the retired value in backticks, found by `git grep`, or write
`NO VALUE READERS` followed by the reason nothing reads the value.

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.

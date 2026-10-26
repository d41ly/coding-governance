**Serves:** research TOOL-dTotalRecall-61

# Round-4 fix brief — dTotalRecall, the checks the round-4 promotions owe before their commit

The round-4 spec audit's disposal (`unattended-build.js` run `wf_57861322-efe`) wrote the promoted specs
TOOL-dTotalRecall-61 to -66 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Hygiene checks 2, 5, 12, 21 and 25 already read clean; clear the three
`python tools/check-spec-tokens.py` hits below, changing nothing else in any spec's design.

- Units 61 to 66 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place afterwards. Do not commit and do not run the build-index generator.

## F1 · `<rev>:<path>` spellings read as untracked paths

A backticked `<rev>:<path>` in an acceptance criterion reads to the token arm as a path that does not exist at HEAD.
Cite the revision and the basename apart (for example "`git show <commit>` of `id_grammar.py`, run from
`tools/memory-tree/`"), keeping the full path in §2, §4 and Files touched. The hits:
- unit 64: `commit>:tools/memory-tree/id_grammar.py`
- unit 66: `commit>:memory/project/legacy-records.txt`, `462d20f3:tools/memory-tree/tree_lib.py`

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.

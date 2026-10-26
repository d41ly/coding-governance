**Serves:** research TOOL-dTotalRecall-44

# Round-2 fix brief — dTotalRecall, the checks the round-2 promotions and folds owe before their commit

The round-2 spec audit's disposal (`unattended-build.js` run `wf_1b007877-14f`) wrote the promoted specs
TOOL-dTotalRecall-44 to -53 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Clear every finding below, changing nothing else in any spec's design, so that
`python tools/check-spec-tokens.py` prints no dTotalRecall hit and `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file.

- Units 44 to 53 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. A spec the disposal
  folded is uncommitted at its new rev: edit it in place at that rev, extending that rev's §9 line.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and Files
touched; describe a fixture's example path in prose rather than as a backticked path literal. The hits:
- unit 52: `memory/project/legacy-records.txt`
- unit 53: `tools/playbook/edge_grammar.py`, `memory/builds/dTotalRecall/spec/x.md` (a fixture example),
  `tools/runlog/memory_measure.py`

## F2 · a criterion with no witness

Hygiene check 12 reds unit 53's AC9: an acceptance bullet naming no backticked witness (`SPEC_WITNESS_CUTOFF`). Give
AC9 the backticked command, file or fixture that observes it, as every other criterion does.

## F3 · unit 43 is over the size ceiling again

The round-2 folds grew TOOL-dTotalRecall-43 to 50582 bytes, generated `gen:spec-records` region included, against
the 49152 ceiling. Trim its non-criterion text to at or under 48900 bytes as the file stands, region included. Keep
every criterion, scope item and finding id; do not split it and do not touch the generated region.

## Return

The list of files you edited, one line each on what changed, the size of unit 43, and the last line of the hygiene
gate run.

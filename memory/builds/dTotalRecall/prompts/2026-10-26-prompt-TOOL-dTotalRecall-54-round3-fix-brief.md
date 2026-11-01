**Serves:** research TOOL-dTotalRecall-54

# Round-3 fix brief — dTotalRecall, the checks the round-3 promotions and folds owe before their commit

The round-3 spec audit's disposal (`unattended-build.js` run `wf_7c2ca481-5e6`) wrote the promoted specs
TOOL-dTotalRecall-54 to -60 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Clear every finding below, changing nothing else in any spec's design, so that
`python tools/check-spec-tokens.py` prints no dTotalRecall hit and `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file.

- Units 54 to 60 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. A spec the disposal
  folded is uncommitted at its new rev: edit it in place at that rev, extending that rev's §9 line.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

In §6 cite a file this build or a parent will CREATE by its basename and keep its full path in §2, §4 and Files
touched; describe a fixture's example path in prose rather than as a backticked path literal; a `<rev>:<path>`
spelling is a path too, so cite the revision and the basename apart. The hits:
- unit 55: `tools/memory-tree/record_causes.py`
- unit 56: `tools/memory-tree/record_kinds.py`
- unit 57: `tools/memory-tree/record_causes.py`, `tools/x.py` (a fixture example)
- unit 58: `tools/memory-tree/record_causes.py`
- unit 59: `tools/lib/legacy_ledger.py`
- unit 60: `tools/memory-tree/id_grammar.py`, `tools/memory-tree/record_causes.py`, `462d20f3:tools/memory-tree/tree_lib.py`

## F2 · guarded legs missing from §7

Units 54, 55, 59 and 60 name `tools/codebase-map/gen_map.py` in §4 Files touched, which trips the guards of
`codebase-map kit selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e`. Add the three legs to each
one's §7 leg line.

## F3 · a retirement with no Readers clause

Hygiene check 25 reds unit 60's S1: a §2 item that retires a named thing carries no `**Readers:**` clause. Write it
as `memory/TEMPLATE-SPEC.md` states: `**Readers:**`, then `by name:` and every reader that spells the name, then
`by value:` and the readers of its value, or `NO VALUE READERS` and a reason, each found by `git grep` over the tree.

## F4 · unit 43 is over the size ceiling again

The round-3 folds grew TOOL-dTotalRecall-43 to 49494 bytes, generated `gen:spec-records` region included, against the
49152 ceiling. Trim its non-criterion text to at or under 48600 bytes as the file stands, region included, leaving
headroom for the next round's fold. Keep every criterion, scope item and finding id; do not split it and do not touch
the generated region.

## Return

The list of files you edited, one line each on what changed, the size of unit 43, and the last line of the hygiene
gate run.

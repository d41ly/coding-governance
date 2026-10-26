**Serves:** research TOOL-dTotalRecall-77

# Round-7 fix brief — dTotalRecall, the checks the round-7 promotions owe before their commit

The round-7 spec audit's disposal (`unattended-build.js` run `wf_aaa83294-f3d`) wrote the promoted specs
TOOL-dTotalRecall-77 to -88 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Clear every finding below, changing nothing else in any spec's design, so that
`python tools/check-spec-tokens.py` prints no dTotalRecall hit and `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file.

- Units 77 to 88 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · paths in acceptance criteria that do not exist at HEAD

In §6 cite a file this build or a parent will CREATE by its basename, with the folder it runs from in prose, and keep
the full path in §2, §4 and Files touched. The hits, all in unit 88: `tools/lib/legacy_ledger.py`,
`tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py`.

## F2 · retirements with no Readers clause

Hygiene check 25 reds a §2 item that retires a named thing and carries no `**Readers:**` clause: unit 77 S2, unit 78
S3, unit 87 S1, unit 88 S26 and S29. Write each as `memory/TEMPLATE-SPEC.md` states: `**Readers:**`, then `by name:`
and every reader that spells the name, then `by value:` and the readers of its value, or `NO VALUE READERS` and a
reason, each found by `git grep` over the tree.

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.

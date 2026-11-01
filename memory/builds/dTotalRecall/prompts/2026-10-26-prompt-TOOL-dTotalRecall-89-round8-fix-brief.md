**Serves:** research TOOL-dTotalRecall-89

# Round-8 fix brief — dTotalRecall, the checks the round-8 promotions owe before their commit

The round-8 spec audit's disposal (`unattended-build.js` run `wf_afe0e383-0d8`) wrote the promoted specs
TOOL-dTotalRecall-89 to -92 under `memory/builds/dTotalRecall/spec/` and folded each hands-off edge into the spec it
names. Nothing of it is committed yet. Every finding is in unit 92. Clear them, changing nothing else in its design,
so that `python tools/check-spec-tokens.py` prints no dTotalRecall hit and `bash tools/memory-tree/check-memory-hygiene.sh
--only 2,5,12,21,25` prints no FAILED line naming a dTotalRecall file.

- Units 89 to 92 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump.
- Your role admits the hygiene gate and the lexicon only. The files are staged in this worktree, so run the hygiene
  gate in place. Do not commit and do not run the build-index generator.

## F1 · a path inside a backticked one-liner

A criterion's backticked Python one-liner spells `open('memory/builds/dTotalRecall/README.md', …)`, which the token
arm reads as an untracked path fragment. Pass the README as the one-liner's argument (`sys.argv[1]`) and name it in
prose, as earlier rounds did.

## F2 · a criterion with no witness

Hygiene check 12 reds AC9: an acceptance bullet naming no backticked witness (`SPEC_WITNESS_CUTOFF`). Give AC9 the
backticked command, file or fixture that observes it.

## F3 · Readers clauses

Hygiene check 25 reds S9 (a retirement with no `**Readers:**` clause) and S11 (a `**Readers:**` clause with no
`by value:` half after its `by name:`). Write each as `memory/TEMPLATE-SPEC.md` states: `**Readers:**`, then
`by name:` and every reader that spells the name, then `by value:` and the readers of its value, or `NO VALUE READERS`
and a reason, each found by `git grep` over the tree.

## Return

The list of files you edited, one line each on what changed, and the last line of the hygiene gate run.

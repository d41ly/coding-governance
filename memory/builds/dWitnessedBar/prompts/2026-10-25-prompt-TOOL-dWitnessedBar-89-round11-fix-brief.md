**Serves:** research TOOL-dWitnessedBar-89

# Round-11 fix brief — unit 89's check-25 hit, before the round-12 audit

The round-11 spec audit's disposal wrote TOOL-dWitnessedBar-89, the batch of its 13 minors. Clear the finding below,
changing nothing else, so that `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no
dWitnessedBar finding and the main loop's `python tools/check-spec-tokens.py` stays at no dWitnessedBar hit.

- Unit 89 is uncommitted at rev-1 and unaudited: edit it in place with no rev bump. Touch no other spec, no `order`
  verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role
  admits the hygiene gate and the lexicon only. Keep its H1 at 255 bytes or less, line included.

## 1. Check 25 — TOOL-dWitnessedBar-89 S10

S10 is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing, reword it so
it no longer reads as a retirement, keeping its meaning, and say which you chose.

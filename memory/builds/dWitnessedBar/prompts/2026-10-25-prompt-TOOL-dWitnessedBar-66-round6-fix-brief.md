**Serves:** research TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67

# Round-6 fix brief — units 66 and 67's check-25 hits, before the round-7 audit

The round-6 spec audit's disposal wrote TOOL-dWitnessedBar-66 and -67. Clear the findings below, changing nothing
else, so that `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding;
`python tools/check-spec-tokens.py` already reads 0 dWitnessedBar hits and must stay so.

- Both units are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec and
  no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role admits the
  hygiene gate and the lexicon only.
- The orders stand as the tree has them (64 at 36, 65 at 37, 66 at 38, 67 at 39): change no `order` verb.
- Report the byte count of TOOL-dWitnessedBar-51 (you do not edit it).

## Check 25 — TOOL-dWitnessedBar-66 S4 · TOOL-dWitnessedBar-67 S2, S3

Each is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing, reword it so
it no longer reads as a retirement, keeping its meaning, and say which you chose.

**Serves:** research TOOL-dSafePassage-59

# Brief — dSafePassage: one round-7 promoted spec the memory hygiene hook refuses

## The prompt

> HYGIENE check 25 FAILED on the staged commit of the round-7 spec audit's promotions.

— the memory hygiene gate, run `--staged` by the main loop before committing the disposal stage's output

## The brief

### Goal

Make the spec the round-7 disposal stage wrote pass hygiene check 25, changing no design.

### Items

The gate's findings, verbatim, each fixed in its spec as the message says:

1. `2026-10-23-spec-TOOL-dSafePassage-59.md` S7: check 25, a §2 item that retires a named thing carries no `**Readers:**`
   clause. Write `**Readers:**` with `by name:` and the readers that spell the name, then `by value:` and the
   readers of its value, or `NO VALUE READERS` and a reason. A name only an unbuilt unit makes takes
   `READER NOT IN TREE` and the reason on that half. If an item retires nothing, reword it so it does not read as a
   retirement.
2. The same spec's S10: check 25, `by name:` lists `tools/govkit/upgrade_steps.py`, which no tracked reader spells,
   since the unit that makes it is unbuilt. Write `READER NOT IN TREE` and the reason on that half.

Check 25's grammar is in `memory/HYGIENE.md` (check 25). `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md`
S2, S23 and S30 hold accepted shapes from the same build.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with your edits staged into
it through `GIT_INDEX_FILE`, does not name this spec. Delete the copy after.

### Gates

Only the memory hygiene gate, as above.

### Non-goals

No design change, no other spec, no rev bump: the spec is rev-1, uncommitted, and unaudited and carried unaudited under the owner's audit cap.
No commit, no stage into the real index, and no write outside that one file.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

The accepted `**Readers:**` shapes in TOOL-dSafePassage-26.

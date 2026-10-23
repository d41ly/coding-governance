**Serves:** research TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-42

# Brief — dSafePassage: three round-3 promoted specs the memory hygiene hook refuses

## The prompt

> HYGIENE check 25 FAILED on the staged commit of the round-3 spec audit's promotions.

— the memory hygiene gate, run `--staged` by the main loop before committing the disposal stage's output

## The brief

### Goal

Make the three specs the round-3 disposal stage wrote pass hygiene check 25, changing no design.

### Items

The gate's findings, verbatim, each fixed in its spec as the message says:

1. `2026-10-23-spec-TOOL-dSafePassage-38.md` S2, `2026-10-23-spec-TOOL-dSafePassage-39.md` S1 and
   `2026-10-23-spec-TOOL-dSafePassage-42.md` S4: check 25, §2 items that retire a named thing carry no `**Readers:**`
   clause. Write `**Readers:**` with `by name:` and the readers that spell the name, then `by value:` and the
   readers of its value, or `NO VALUE READERS` and a reason. A name only an unbuilt unit makes takes
   `READER NOT IN TREE` and the reason on that half. If an item retires nothing, reword it so it does not read as a
   retirement.

Check 25's grammar is in `memory/HYGIENE.md` (check 25). `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md`
S2, S23 and S30 hold accepted shapes from the same build.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with your edits staged into
it through `GIT_INDEX_FILE`, names none of these three specs. Delete the copy after.

### Gates

Only the memory hygiene gate, as above.

### Non-goals

No design change, no other spec, no rev bump: the three specs are rev-1, uncommitted, and unaudited until round 4.
No commit, no stage into the real index, and no write outside the three files.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

The accepted `**Readers:**` shapes in TOOL-dSafePassage-26.

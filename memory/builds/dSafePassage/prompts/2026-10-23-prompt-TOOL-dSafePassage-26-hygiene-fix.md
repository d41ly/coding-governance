**Serves:** research TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26

# Brief — dSafePassage: three promoted specs the memory hygiene hook refuses

## The prompt

> HYGIENE check 12 FAILED and HYGIENE check 25 FAILED on the commit of the round-1 spec audit's promotions.

— the pre-commit hook, on the main loop's commit of the disposal stage's output

## The brief

### Goal

Make the three specs the round-1 disposal stage wrote pass hygiene checks 12 and 25, changing no design.

### Items

The hook's findings, verbatim, each fixed in its spec as the message says:

1. `2026-10-23-spec-TOOL-dSafePassage-26.md`: check 12, scope items naming neither an acceptance criterion nor
   NOT OBSERVED (`SCOPE_JOIN_CUTOFF`): S47. Name the criterion that observes S47, or mark it NOT OBSERVED with
   the reason, in the grammar `memory/TEMPLATE-SPEC.md` gives the scope join.
2. `2026-10-23-spec-TOOL-dSafePassage-24.md` S1, `2026-10-23-spec-TOOL-dSafePassage-25.md` S1, and
   `2026-10-23-spec-TOOL-dSafePassage-26.md` S21, S23, S28 and S30: check 25, §2 items that retire a named thing
   carry no `**Readers:**` clause. Write `**Readers:**` with `by name:` and the readers that spell the name, then
   `by value:` and the readers of its value, or `NO VALUE READERS` and a reason. If an item retires nothing, reword
   it so it does not read as a retirement.
3. `2026-10-23-spec-TOOL-dSafePassage-26.md` S2: check 25, `by name:` lists `cmd_frozen`,
   `tools/govkit/upgrade_steps.py` and `derive_push_base`, which no tracked reader spells, since the units that make
   them are unbuilt. On that half, name a reader that spells each, or write `READER NOT IN TREE` and the reason.

Check 25's grammar is in `memory/HYGIENE.md` (check 25) and `memory/TEMPLATE-SPEC.md`. Grep
`memory/builds/dTrueNorth/spec/` for `READER NOT IN TREE` and `NO VALUE READERS` to see the accepted shape.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --staged` names none of these three specs after the main loop
stages them. You may run that one gate: the spec-writer role allows the memory hygiene gate. Stage nothing
yourself. Run it only on a copy of the index if your role forbids staging, or skip it and say so.

### Gates

Only the memory hygiene gate, as above.

### Non-goals

No design change, no other spec, no rev bump: the three specs are rev-1, uncommitted, and unaudited until round 2.
No commit, no stage, no write outside the three files.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

The accepted `**Readers:**` shapes in dTrueNorth's specs.

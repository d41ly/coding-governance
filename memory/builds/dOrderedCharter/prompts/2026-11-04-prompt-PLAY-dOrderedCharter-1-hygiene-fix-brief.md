**Serves:** research PLAY-dOrderedCharter-1

# Brief: the spec-shape refusals on the second drift fold's commit

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. The memory-hygiene pre-commit hook refused the second drift fold's commit on two spec-shape
checks.

## The brief

### Goal

Make specs 1, 4, 6 and 55 pass both refusals below, so the fold commits.

### Items

1. **The template-conformance check.** Spec 4's rev-4 history entry names no section, scope id or acceptance id.
   Make it name what rev-4 changed: the S ids, the AC ids, or "section 7".
2. **The Readers check.** Every section-2 item that retires a named thing carries a `**Readers:**` clause. The clause
   has a `by name:` half listing the readers that spell the name, then a `by value:` half listing the readers of its
   value, or `NO VALUE READERS` and a reason. Fix these items:
   - spec 1 S7, which has no clause;
   - spec 6 S6, which has no clause;
   - spec 55 S17, which has no clause;
   - spec 55 S1 and S7, whose clauses lack the `by value:` half.
   - spec 1 S6: its `by name:` lists `tools/playbook/render_playbook.py@c7269a97`. That is a pin, not a name a reader
     spells. Name the reader by its tracked path, or write `READER NOT IN TREE` and a reason on that half.
   - Find each reader by `git grep` at HEAD. Spec 19's section-2 clauses are the accepted shape.
3. Edit the specs in the tree. No unit is building now.
4. New text names a section in words. It never uses the section-sign form, the method-rule form or the hygiene
   check-number form, and it adds no `path:line` citation.
5. Do not bump the rev again. Each spec gains one history line naming this brief, dated 2026-11-04, that names the
   S ids it touched.

For the run:

- Writes stay in specs 1, 4, 6 and 55.
- Do not commit and run no check.
- Return each clause as it now reads.

### Acceptance

- Every item above is fixed, and the return lists each one.

### Gates

The memory-hygiene pre-commit hook, run by the main loop's commit.

### Non-goals

- No other edit.

### Limitations

The items above, "For the run".

### Reuse

Spec 19's section-2 `**Readers:**` clauses.

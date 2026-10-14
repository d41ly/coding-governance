# Revision — dRedressedBar: TOOL-dRedressedBar-13 rev-2, the Readers clause check 25 requires

**Serves:** research TOOL-dRedressedBar-13

## The brief

### Goal
The pre-commit gate refused the commit holding this spec with HYGIENE check 25:
`memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md (§2 items that retire a
named thing carry no **Readers:** clause …): S6`. Revise the spec to rev-2. S6 gains a
`**Readers:**` clause that answers `by name:`, with every reader that spells the retired name found
by grep over the tracked tree, and `by value:`, with the readers of its value or `NO VALUE READERS`
and a reason. The grammar is `memory/HYGIENE.md` check 25 and `memory/TEMPLATE-SPEC.md`. Add a §9
revision line naming the change. Nothing else moves.

### Items
1. Revise `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-13.md` to rev-2 as the
   goal states. If a reader the grep finds is not already in the unit's scope or files touched, say
   so in the clause and add it to §4's files touched, because a reader left behind is the defect the
   check exists for.

### Acceptance
Staged with the other round-2 files, `bash tools/memory-tree/check-memory-hygiene.sh --staged` prints
no check 25 line for this spec.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any other spec, including the `-12` and `-14` specs.

### Limitations
- Children run no bar and no whole suite.

### Reuse
The Readers clauses in this build's other specs (unit 10, unit 11) as the worked form.

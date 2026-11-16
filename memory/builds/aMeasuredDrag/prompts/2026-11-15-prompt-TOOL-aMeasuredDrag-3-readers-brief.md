# Brief — aMeasuredDrag: the Readers clauses the spec commit owes

**Serves:** research TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4

## The prompt

> Build quick wins

The spec stage's one commit of the eleven specs was refused by the pre-commit hook's hygiene check 25, quoted here: "§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason: S4", for `TOOL-aMeasuredDrag-3` and `TOOL-aMeasuredDrag-4`.

## The brief

### Goal
The S4 scope items of the specs of `TOOL-aMeasuredDrag-3` and `TOOL-aMeasuredDrag-4` each carry the `**Readers:**` clause hygiene check 25 requires, so the spec set commits.

### Items
1. In `memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-3.md`, S4 (the usage text losing "and never --staged"): add `**Readers:** by name: <each tracked file that spells the retired text> by value: <its value readers, or NO VALUE READERS and a reason>`, found with `git grep` over the tree. The shape is in `memory/TEMPLATE-SPEC.md`, near line 448.
2. In `memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-4.md`, S4 (the registry row's `why` losing "among them the tag checks"): the same clause, by the same probe.
3. These specs are uncommitted and still rev-1, so edit them in place with no rev bump. Change nothing else.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --only 25` prints no line naming either spec. Run it with the two specs staged, as they are.

### Gates
Hygiene check 25 alone. No other gate, suite or bar.

### Non-goals
- Any other section of either spec, and every other spec.
- Do not commit.

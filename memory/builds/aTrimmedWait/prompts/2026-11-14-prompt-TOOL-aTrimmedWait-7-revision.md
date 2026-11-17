# Revision — TOOL-aTrimmedWait-7: S5 reads as a retirement to hygiene check 25

**Serves:** research TOOL-aTrimmedWait-7

## The prompt

The spec commit stage of run `wf_c8bf779c-f78` returned the pre-commit hook's refusal, quoted:

> HYGIENE check <N> FAILED (N = 25): "memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S5" — `doc.hygiene#the-check-catalog-all-in-tools-memory-tree-check-memory-hygiene-sh-this-file-is-the-prose-home`

## The brief

### Goal
The pre-commit hook refused the spec commit on hygiene check 25: "§2 items that retire a named thing
carry no **Readers:** clause ... S5". S5 says the descriptions name "how to drop it" (the cache
record); check 25 reads a retirement word beside a name. Nothing is retired: the unit adds a cache.
Reword S5 so it names no retirement (for example "how to clear it"), or, if the item genuinely
retires a named thing, give it the `**Readers:**` clause check 25 asks for. Change nothing else, and
leave the spec uncommitted: the main loop commits the set.

### Items
1. TOOL-aTrimmedWait-7 §2 S5 passes check 25 with its meaning unchanged.

### Acceptance
- `bash tools/memory-tree/check-memory-hygiene.sh --only 25` reports no finding for this spec.
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md` exits 0.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
Copied from the build's brief: no verdict change, and no narrowing of the full hygiene run, the bar,
or `--dispatch`'s own refusals.

### Limitations
Copied from the build's brief: every speed-up is keyed on what it read; measurements on node a, one
at a time; long suites on a frozen clone.

### Reuse
Copied from the build's brief: R6 reuses `load_session_calls` in `tools/roles/handoff.py`.

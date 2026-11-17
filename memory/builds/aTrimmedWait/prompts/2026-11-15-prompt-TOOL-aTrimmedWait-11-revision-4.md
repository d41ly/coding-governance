# Revision — TOOL-aTrimmedWait-11: the pass legs' pinned-facts reds in the spec

**Serves:** research TOOL-aTrimmedWait-11

## The prompt

The main loop's pass-legs run over `aa1695886..e99df8a27` read one leg red, `writing practice
(records and units)`, on four `pinned-facts` rows in this unit's spec, quoted:

> pinned-facts: red · memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md · unpinned fact `10 s`: pin it on its line (an id, a path:line, PINNED or DERIVED)

and the same for `26 lines`, `75 s` and `808 s`. The `26 lines` row reads the phrase "its check 26
lines" in §4 "Evidence" as a figure. Every other leg read green.

## The brief

### Goal
Revise TOOL-aTrimmedWait-11 so the `pinned-facts` rows read green over its spec.

### Items
1. Every measured figure the leg names carries `<!-- PINNED 2026-11-15 -->` or a DERIVED source on
   the same line as the figure, the figure and its pin never split by a line break.
2. The "its check 26 lines" phrase in §4 "Evidence" is reworded so no number sits before a unit word,
   with its meaning kept.

Change nothing else. Bump the revision, keep the header INPROGRESS, and leave the spec uncommitted:
the main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 25 --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-11` prints its clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to any figure's value, to what is compared, or to any criterion.

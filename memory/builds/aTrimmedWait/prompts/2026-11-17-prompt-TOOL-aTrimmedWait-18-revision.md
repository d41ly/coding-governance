# Revision — TOOL-aTrimmedWait-18: the pass legs' positional and pinned-facts reds in the spec

**Serves:** research TOOL-aTrimmedWait-18

## The prompt

The main loop's pass-legs run over `0159e06eb..9ddbabd41` read two legs red, both on this unit's
spec and nothing else. `positional (the citation check alone)`, quoted:

> tags: positional · unlisted · memory/builds/aTrimmedWait/spec/2026-11-17-spec-TOOL-aTrimmedWait-18.md · HYGIENE check <N> · cite `doc.hygiene#the-check-catalog-all-in-tools-memory-tree-check-memory-hygiene-sh-this-file-is-the-prose-home`, the alias row's tag

N is the build index's check, number 9, elided here as the leg would read this record the same way.
It reads the hook line §4 quotes in its fenced block. And `writing practice (records and units)`,
quoted:

> pinned-facts: red · memory/builds/aTrimmedWait/spec/2026-11-17-spec-TOOL-aTrimmedWait-18.md · unpinned fact `29 lines`: pin it on its line (an id, a path:line, PINNED or DERIVED)

It reads the "Keep git's `FLOOR_ASSERTIONS=3377`" entry under §4 "Alternatives rejected". Every other
leg read green.

## The brief

### Goal
Revise TOOL-aTrimmedWait-18 so the `positional` and `pinned-facts` rows read green over its spec.

### Items
1. The fenced hook excerpt in §4 no longer spells the hygiene check's number beside `HYGIENE check`:
   quote that line as `HYGIENE check <N> FAILED` with N stated beside the fence, or cite the check
   through the alias the leg names, keeping what the excerpt shows.
2. The figure in the "Keep git's `FLOOR_ASSERTIONS=3377`" entry carries a DERIVED source on the same
   line as the figure, or is reworded so no number sits before a unit word, with its meaning kept.

Change nothing else. Bump the revision and keep the header CLOSED: the unit is built, and this
revision changes the spec's prose only. Leave the spec uncommitted: the main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-17-spec-TOOL-aTrimmedWait-18.md` exits 0.
- `python tools/playbook/writing_practice.py check pinned-facts` prints no row for the spec.
- `python tools/playbook/positional.py check` prints no `unlisted` row for the spec.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it.

### Non-goals
No change to any figure's value, to any resolution, to what is compared, or to any criterion.

# Revision — specs 2 and 3: the pass legs red on writing practice

**Serves:** research TOOL-aTrimmedWait-3

## The prompt

The main loop's pass-legs run after unit 1's pass commit 78cc7c112 reported, among its reds, the
writing-practice leg's pinned-facts arm (each line names a spec and a fact) and the positional leg:

> pinned-facts: red · <spec> · unpinned fact `<fact>`: pin it on its line (an id, a path:line, PINNED or DERIVED)

> tags: positional · unlisted · <spec> · HYGIENE check <N> · cite `doc.hygiene#the-check-catalog-all-in-tools-memory-tree-check-memory-hygiene-sh-this-file-is-the-prose-home`, the alias row's tag

## The brief

### Goal
Clear the writing-practice and positional reds in the specs of TOOL-aTrimmedWait-2 and 3, with no
change of meaning. Pin each listed fact on its own line: a figure measured once gets
`<!-- PINNED 2026-11-14 -->` at the line's end, one derived from a source names that source (an id
or a path:line) or `DERIVED`. The facts, per spec: spec 2: `15 s`, `19 s`, `30 specs`, `376 s`, `60 s`; spec 3: `47 s` (DERIVED from the pass-legs log of 78cc7c112). Spec 3 also carries two positional reds, on its `HYGIENE check <N>` spellings (N = 12 and N = 9): cite the anchor the prompt quotes on each of those lines. Bump each edited spec's rev and add
its §9 line naming this record. Change nothing else; do not commit; do not run the build-index generator.

### Items
1. No pinned-facts line from the writing-practice leg names these specs.
2. No positional unlisted line names them.

### Acceptance
- `python tools/check-spec-tokens.py --spec <each edited spec>` exits 0.
- Every listed fact's line carries a pin, by `grep -n` over each edited spec.

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
The pin spelling at `memory/builds/aNimbleMend/README.md` line 26: `<!-- PINNED 2026-11-12 -->`.

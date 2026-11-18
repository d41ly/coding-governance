# Ruling — TOOL-aTrimmedWait-4: the owner resolves §8 F1

**Serves:** research TOOL-aTrimmedWait-4

## The prompt

The main loop asked the owner, through AskUserQuestion on 2026-11-14:

> Which mechanism should unit 4 build: the moved-only write, a reach-scoped render, or a per-file parse cache?

The owner answered: "Moved-only write (Recommended)".

## The brief

### Goal
Mark TOOL-aTrimmedWait-4's §8 F1 resolved in place, in the shape `memory/TEMPLATE-SPEC.md` §8 states:
`RESOLVED (owner, 2026-11-14): <pick>`, the pick being the owner's answer above. Bump the rev
and add the §9 line the template requires for an edit to a committed spec, naming this record. Change
nothing else. Do not commit and do not run the build-index generator: the main loop commits the set.

### Items
1. TOOL-aTrimmedWait-4 §8 F1 carries the owner's RESOLVED mark, so `bash tools/unattended/unattended.sh --plan aTrimmedWait --paths` no longer grades the unit FORKED.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-4.md` exits 0.
- `bash tools/unattended/unattended.sh --plan aTrimmedWait --paths` prints this unit READY.

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
Copied from the build's brief: see the build brief's Reuse section.

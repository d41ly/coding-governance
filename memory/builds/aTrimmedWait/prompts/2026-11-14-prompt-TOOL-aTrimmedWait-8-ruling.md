# Ruling — TOOL-aTrimmedWait-8 and TOOL-aTrimmedWait-9: the owner resolves the repair specs' forks

**Serves:** research TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9

## The prompt

The main loop asked the owner three questions on 2026-11-14, each fork on its own, through AskUserQuestion:

> Unit 9 M2: where should the comment cut go? — Answer: "Shared cut (Recommended)"

> Unit 8 F1: which cutoff-key set should the scoped-fixture gate check? — Answer: "Derived set (Recommended)"

> Unit 8 F2: should unit 8 also update help/commit-render.md, beyond the brief's three-file limit? — Answer: "Update the page (Recommended)"

## The brief

### Goal
Each answer is marked in its spec's §8 as `RESOLVED (owner, 2026-11-14): <pick>`. Unit 9's ruling
accepts one G3 verdict moving toward refusal: a suite whose only admitting word sits in a shell
comment is refused where it was admitted. Unit 8 adds `help/commit-render.md` to its files.

### Items
1. TOOL-aTrimmedWait-9 §8 F1 resolved to the shared cut in `scanCommandHeads`.
2. TOOL-aTrimmedWait-8 §8 F1 resolved to the derived cutoff set, F2 to updating the page.

### Acceptance
- `bash tools/unattended/unattended.sh --plan aTrimmedWait --paths` grades both units READY.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it.

### Non-goals
Copied from the build's brief: no narrowing of the full hygiene run, the bar, or `--dispatch`'s own
refusals.

### Limitations
Copied from the build's brief: measurements on node a, one at a time.

### Reuse
The ruling records of units 2, 4, 5 and 7 beside this one.

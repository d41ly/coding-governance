# Revision — TOOL-aTrimmedWait-11: the fixture arm's reads under `set -u`

**Serves:** research TOOL-aTrimmedWait-11

## The prompt

The builder of run `wf_0b836e97-5c0` returned DIVERGENCE before any edit. The suite runs under
`set -u`, so a read of an unset element of `_hs_c26` ends the suite with `unbound variable`. An empty
or short render therefore stops the whole suite at the fixture arm instead of reading as §4's last
paragraph and §5's "error / empty / loading states" row say, and the fourth assertion's non-empty
test can never read false. The builder's probe on bash 5.3.9 (Cygwin) printed `a[0]: unbound
variable` and exited 1. It also found §4 "Files touched" naming only the suite, while the pass writes
the codebase map, the acceptance ledger and the index files check 9 asks for. The owner ruled on
2026-11-15 for unset-safe reads.

## The brief

### Goal
Revise TOOL-aTrimmedWait-11 so its fixture arm reads as §4 and §5 claim under the suite's `set -u`.

### Items
1. Every read of an `_hs_c26` element in §4 "The fixture arm", the assertion table's Compares column
   included, uses the unset-safe default form, `"${_hs_c26[N]-}"`, so an empty or short render reds
   the assertions §4 names and the suite runs on.
2. §4's last paragraph and §5's "error / empty / loading states" row say so, naming `set -u` as the
   reason for the form.
3. §4 "Files touched" adds `memory/map/generated` for the codebase map re-render the new function
   owes, the unit's acceptance ledger, and the generated index files check 9 asks for.

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
No change to what is compared, the function, the floor or the arms' count.

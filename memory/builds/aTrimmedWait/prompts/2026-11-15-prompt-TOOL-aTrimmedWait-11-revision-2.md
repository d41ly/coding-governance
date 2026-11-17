# Revision — TOOL-aTrimmedWait-11: rev-2's spec commit refused, and the carriage-return strip

**Serves:** research TOOL-aTrimmedWait-11

## The prompt

The main loop's commit of rev-2 was refused by the pre-commit hook's memory hygiene, quoted:

> memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md (§2 items that retire a named thing carry no **Readers:** clause; ...): S1

S1 says the function "drops every check 26 `cache recomputed` line", and the check reads that verb as
retiring a named thing. Nothing is retired: the lines are set aside inside one comparison, and check 26
still prints them.

The rev-2 spec writer also reported that §4's line `_hs_c26=("${_hs_c26[@]%$'\r'}")` does not strip
the trailing carriage return under this node's bash 5.3 (Cygwin). The main loop observed on
2026-11-15 that holding the pattern in a variable does: `cr=$'\r'; B=("${A[@]%"$cr"}")` left no
carriage return in `B`.

## The brief

### Goal
Revise TOOL-aTrimmedWait-11 so its spec commits, with the fixture arm's strip correct on this node.

### Items
1. S1, and any other §2 item worded the same way, says the `cache recomputed` lines are set aside in
   the comparison, not dropped or removed, so no §2 item reads as retiring a named thing.
2. §4 "The fixture arm" strips the carriage return with the pattern held in a suite variable, and
   the sentence after it says why: the array expansion's `%$'\r'` leaves it on this node's bash.
   §4 "Inventory" names the variable.

Change nothing else. Bump the revision, keep the header SPECCED, and leave the spec uncommitted: the
main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 25 --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-11` prints its clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to what is compared, the function, the floor or the files touched.

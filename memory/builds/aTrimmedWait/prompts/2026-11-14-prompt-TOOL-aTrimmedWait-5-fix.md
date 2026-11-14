# Fix — TOOL-aTrimmedWait-5: an empty batch over one brief skips the fallback

**Serves:** research TOOL-aTrimmedWait-5

## The prompt

The unit's own builder reported, on its pass commit 69ed1688d, quoted:

> the bug-class checklist selected `line-count-reads-empty-capture-as-one`, and it applies here. `mapfile` over an empty here-string reads as one line. So with exactly one present brief, a batch that exits 0 and prints nothing passes the count check instead of falling back as S2 requires. ... The fix is one line: replace `mapfile -t _bnows <<<"$_bout"` with `[ -z "$_bout" ] || mapfile -t _bnows <<<"$_bout"`.

## The brief

### Goal
Make S2's fallback hold for an empty batch capture: an empty `_bout` yields zero lines, so the count
check against one present path fails and every row is graded by the per-path call. Change nothing
else in `verb_status`; the pass legs over 69ed1688d were green, so no other red is owed. Set the
header CLOSED again as the last commit.

### Items
1. In `tools/unattended/unattended.sh#verb_status`, the batch result splits to zero lines when the
   capture is empty.
2. The pass's arm in `tools/unattended/unattended.test.sh` gains the one-brief empty-output case:
   under a shim where `--stdin-paths` exits 0 with no output, the status line is unchanged and the
   per-path call runs once.
3. The acceptance ledger gains one row for this fix.

### Acceptance
- The scratchpad probe `r5.sh` prints the lines it printed at 69ed1688d.
- On a one-brief copy of the fixture under that empty-output shim, the driver makes one per-path
  `hash-object` call, where at 69ed1688d it made none.

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
The empty-capture guards the gotcha class `line-count-reads-empty-capture-as-one` already names.

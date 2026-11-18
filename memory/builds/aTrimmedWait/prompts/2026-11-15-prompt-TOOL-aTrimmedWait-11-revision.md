# Revision — TOOL-aTrimmedWait-11: F1 resolved, the `cache recomputed` lines set aside too

**Serves:** research TOOL-aTrimmedWait-11

## The prompt

The spec writer returned rev-1 of TOOL-aTrimmedWait-11 with F1 open: check 26's cache is shared by
every worktree, and an entry another worktree wrote under other declarations makes the unscoped run
print `cache recomputed <count> (foreign inputs)` while the scoped run, reading the rewritten entry,
prints none, so the partition arm still reds in that tree. The owner ruled on 2026-11-15 for (B): set
those lines aside on both sides too.

## The brief

### Goal
Revise TOOL-aTrimmedWait-11 so F1 is resolved for (B).

### Items
1. The partition arm's comparison also sets aside check 26's `cache recomputed` lines on both sides;
   every other line, and every other field of check 26's liveness line, is still compared byte for
   byte.
2. The fixture arm gains the fourth assertion F1 names, so `FLOOR_ASSERTIONS` reaches 749.
3. §3's F1 non-goal, §4 "What it does not check", §5's residual risk and §8 move to the resolved
   state; F1 is recorded as resolved by the owner on 2026-11-15.

Change nothing else. Bump the revision, keep the header SPECCED, and leave the spec uncommitted: the
main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-11` prints its clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to the count mask, the function's name or the files touched.

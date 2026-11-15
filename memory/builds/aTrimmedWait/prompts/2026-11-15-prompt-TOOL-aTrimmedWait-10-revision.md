# Revision — TOOL-aTrimmedWait-10: the kept fixture spelling of the retired conf key

**Serves:** research TOOL-aTrimmedWait-10

## The prompt

The builder of run `wf_f258d1a5-13f` returned DIVERGENCE before any edit: S3 and AC5 require
`git grep -n STAGED_RENDER -- ':!memory/'` to print nothing, while AC2, the §4 "AC2 off" fixture row,
the §7 `New arm:` line and "The unit-3 arms keep their names" require `test_staged_write` in
`tools/memory-tree/gen_build_index.py` to plant a conf line spelling it. The owner ruled on
2026-11-15 to keep the arm: a stale conf line is proved to move nothing.

## The brief

### Goal
Revise TOOL-aTrimmedWait-10 so its criteria hold together, with the arm kept.

### Items
1. S3 names the selftest fixture lines of `test_staged_write` in `tools/memory-tree/gen_build_index.py`
   as the one kept spelling of the retired conf key, and why: the arm plants a stale conf line to
   prove it no longer turns the render on.
2. AC5's grep admits only those fixture lines, by an exclusion or an expected count the spec states,
   and stays red on any other spelling.
3. The AC2 arm is renamed to name the key, so "The unit-3 arms keep their names" drops that arm.
4. §5's generator-run count is corrected: the runs stay at the count the builder derived from
   `run_write_staged(` calls, since the no-kit arm runs in-process.
5. "Files touched" adds `memory/guides/SESSION-KICKOFF.md` for the `last-audit` re-stamp the manifest
   owes when the commit stages `tools/memory-tree/check-memory-hygiene.sh` or `.memory-tree.conf`.
6. The builder's note joins §4 "Rollout": once `check_staged_write` reads the key, `--write-staged`
   declines in this repository until the owner's line reaches `origin/main`, so a check 9 refusal in
   the pass is cleared with `--write` and staging by hand.

Change nothing else. Bump the revision, set the header back to SPECCED, and leave the spec
uncommitted: the main loop commits it.

### Acceptance
- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-10.md` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-10` prints its clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to the key, its default, the fork sites or the owner's S8.

### Limitations
Copied from the build's brief: measurements on node a, one at a time; long suites on a frozen clone.

### Reuse
The builder's divergence report, quoted above.

# Promotion — TOOL-aTrimmedWait-11: the partition arm reads a warm cache

**Serves:** research TOOL-aTrimmedWait-11

## The prompt

The main loop ran `bash tools/memory-tree/check-memory-hygiene.test.sh` on a fresh frozen clone of
`ff4242f8b` to observe unit 10's arms green. It exited 1, and one of its red rows is no conf-example
row:

> FAIL the scoped runs do not partition the unscoped run's lines:

The diff under it is one line of check 26, the unscoped side reading `cache hits 0` and the scoped
side `cache hits 4`. Check 26 keeps a per-merge cache, so the unscoped run, which goes first, reads
it cold and writes it, and the scoped run of check 26 reads it warm. The arm compares the two line
sets byte for byte, so it reds on every fresh checkout and stays green in a tree whose cache is warm.

The arm came in with `TOOL-aSparedSpawn-7` and the field with `TOOL-dDerivedDocket-9`, both ancestors
of this build's base `846d51d39`; this build moves neither. The owner ruled on 2026-11-15 to repair it
in this build anyway.

## The brief

### Goal
Author the spec for TOOL-aTrimmedWait-11, a repair unit after which the partition arm of
`tools/memory-tree/check-memory-hygiene.test.sh` reads the same verdict on a cold clone and on a warm
tree, with no other verdict moved.

### Items
1. The partition arm compares check 26's line with its cache-hit count set aside on both sides, so a
   run order that warms the cache moves nothing; every other field of that line, and every other
   line, is still compared byte for byte.
2. Per [left-shift], an arm proves the comparison holds across a cold and a warm cache: the two line
   sets differing only in the cache-hit count compare equal, and two differing in any other field of
   that line still compare unequal. It is RED at `ff4242f8b`, which the main loop observes at the close.
3. Acceptance criteria a pass can observe with a fixture or a probe; each new suite arm on a `New arm:`
   line in section 7.

### Acceptance
- `python tools/check-spec-tokens.py --spec <the new spec>` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-11` prints its
  clean line.

### Gates
Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### Non-goals
No change to `tools/memory-tree/transition_audit.py` or to check 26's output, no change to the
engine `tools/memory-tree/check-memory-hygiene.sh`, and no other arm of the suite.

### Limitations
Copied from the build's brief: measurements on node a, one at a time; long suites on a frozen clone.

### Reuse
The partition arm's existing liveness-line exclusion, `grep -v '^HYGIENE --only '`, for shape.

# Promotion — aPiecewiseGrade: the closing review round 2's item 1, as TOOL-aPiecewiseGrade-7

**Serves:** research TOOL-aPiecewiseGrade-7

## The prompt

> Promote, build now (Recommended)

The owner's answer, 2026-11-16, to "Build them now or file them?", put through the session's question tool after the closing review `2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2` returned CLEAN WITH FIXES with one medium and one low item, each a missing arm.

## The brief

### Goal
The round-2 review's item 1 (id 1, medium): the foreign-runtime clause of `check_dir_lock_stale` in `tools/unattended/unattended.sh`, which keeps a recorded pid from another runtime counted as live, has no suite arm that reds when the clause is deleted, because every plant in the TOOL-aPiecewiseGrade-6 block is written through `write_dir_lock_pid`, which stamps the local runtime. TOOL-aPiecewiseGrade-7 adds the arm.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-7.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 6, at the tier `memory/guides/SESSION-KICKOFF.md`'s tier rule assigns to a suite-only change that moves no product behaviour. Read item 1 of `memory/builds/aPiecewiseGrade/reviews/2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2.md` whole; its Fix is the design to verify against HEAD, not to copy.
2. One plant in the driver suite's TOOL-aPiecewiseGrade-6 block whose pid record carries another runtime and a dead pid, written directly rather than through `write_dir_lock_pid`, expected held; the arm reds with the runtime clause deleted and greens once restored. The suite's assertion floor moves by the count the arm adds.
3. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, each criterion's id with one line, any fork with its recommendation, and the checker's final line.

### Acceptance
- A lock whose recorded owner is a dead pid from another runtime reads as held, and the arm saying so reds when the runtime clause is deleted.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any change to `tools/unattended/unattended.sh` or any other product file: the arm only.
- `tools/check-spec-tokens.py` and its suite, which TOOL-aPiecewiseGrade-8 writes.
- Any edit to a CLOSED spec.
- Building anything.

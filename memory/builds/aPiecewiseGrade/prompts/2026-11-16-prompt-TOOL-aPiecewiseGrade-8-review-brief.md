# Promotion — aPiecewiseGrade: the closing review round 2's item 2, as TOOL-aPiecewiseGrade-8

**Serves:** research TOOL-aPiecewiseGrade-8

## The prompt

> Promote, build now (Recommended)

The owner's answer, 2026-11-16, to "Build them now or file them?", put through the session's question tool after the closing review `2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2` returned CLEAN WITH FIXES with one medium and one low item, each a missing arm.

## The brief

### Goal
The round-2 review's item 2 (id 2, low): TOOL-aPiecewiseGrade-5's two key-set guards in `tools/check-spec-tokens.py`, the cache miss when a cached entry's `counts` carry another key set and the `KeyError` when a spec's counts differ from `SPEC_COUNTERS`, were observed only by a scratch probe removed after the pass, so deleting either leaves the spec-tokens suite green. TOOL-aPiecewiseGrade-8 adds the permanent arms, using the review's class-level fix.

### Items
1. Write `memory/builds/aPiecewiseGrade/spec/2026-11-16-spec-TOOL-aPiecewiseGrade-8.md`, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, order 6, at the tier `memory/guides/SESSION-KICKOFF.md`'s tier rule assigns to a suite-only change that moves no product behaviour. Read item 2 of `memory/builds/aPiecewiseGrade/reviews/2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2.md` whole; its class-level Fix is the design to verify against HEAD, not to copy.
2. One arm in the spec-tokens suite that edits a cached entry's `counts` key set and observes a miss with unchanged output; one arm that makes a spec's counts carry another key set and observes the loud failure with no summary line. Each reds with its guard deleted and greens once restored. The suite's assertion floor moves by the count the arms add.
3. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit. Return its path and status line, each criterion's id with one line, any fork with its recommendation, and the checker's final line.

### Acceptance
- Deleting either guard reds an arm of the spec-tokens suite, and restoring it greens that arm.

### Gates
`check-spec-tokens.py --spec` over the spec.

### Non-goals
- Any change to `tools/check-spec-tokens.py` or any other product file: the arms only.
- `tools/unattended/` and its suite, which TOOL-aPiecewiseGrade-7 writes.
- Any edit to a CLOSED spec.
- Building anything.

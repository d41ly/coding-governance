# Brief — dRenderedAnchor: the closing review's round-4 findings on unit 4, and the build's close

**Serves:** research TOOL-dRenderedAnchor-5

## The prompt

> Promote the LOWs as unit 5, no more reviews, finish the build.

## The brief

### Goal
Close the two low items of the closing diff review's round 4, which read unit 4, as one Tier-1 batch unit that changes comments and records only, and is the build's last unit: no review round follows it.

### Items
1. L1 — the arm 17 comment in `tools/roles/adopt-roles.test.sh` (around lines 674-676) states that, with no receipt row, the two values of `here` part on two layouts: a harness held at `<kit>/<home>/` (only the kit directory reaches it, probed first) or only in the directory above the tool root (only the tool root reaches it), and that the arm builds the second. Unit 4's spec stays as it is, CLOSED; the round-4 record holds the correction.
2. L2 — `help/roles.md` and the `tools/roles/adopt-roles.sh` header are reflowed so "a `workflow`-driver harness of the workflow table" sits whole on one line, and arm 15's comment in `tools/roles/adopt-roles.test.sh` likewise, so the gotcha entry in `memory/gotchas/two-answers-to-one-question.md` is true as written; or, where a reflow is not possible, that entry is reworded to quote the phrase without its article.

### Acceptance
`grep -c` for the full phrase, article included, over the carriers the gotcha entry names equals the carrier count. The arm 17 comment names both layouts. No line that runs changes: `bash -n` on both shell files, and `adopt-roles.test.sh` still reads `PASS (62 assertions)` at the close.

### Gates
The unit's spec derives them; at least roles adopter self-test · memory hygiene; then the full bar once, at the close.

### Non-goals
Any change to code that runs. Units 1 to 4's specs, all CLOSED. Another review round: the owner ruled on 2026-10-19 that none follows this unit.

### Limitations
Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
The round-4 record names each fix and the skeptic's verdict: `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-4-closing-diff-round4.md`.

## Drawn from the session

> Promote the LOWs as unit 5, no more reviews, finish the build.
— owner, after review round 4

## Owner confirmation

Asked: Review round 4 left only 2 LOW items … M4 says promote them as unit 5 and review again. Proceed?
Answer: Promote the LOWs as unit 5, no more reviews, finish the build.

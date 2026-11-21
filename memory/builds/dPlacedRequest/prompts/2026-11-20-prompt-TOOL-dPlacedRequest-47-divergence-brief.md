**Serves:** research TOOL-dPlacedRequest-47

# Brief — dPlacedRequest: TOOL-dPlacedRequest-47's divergence, resolved

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-47's builder returned a DIVERGENCE (run `wf_8db740e6-995`) and committed nothing. The unguarded
threshold compare §1, §4 and §10 cite is gone: `tools/unattended/unattended.sh#read_claims`'s walk `step` tests the
threshold only for a commit present in `seen`, and the walk loads only ISO-shaped sightings, so S1 and S2 already hold
on the tree. AC2 and AC3 read `unknown -` on HEAD and on both red copies the builder planted (the one §6 names, and
one also dropping the ISO-shape filter), so they cannot go red. AC1 reads red on HEAD only because `add_feed_sightings`
re-sights every cached tip at the read's clock, which §3 puts out of scope as the feed's own behaviour. The one input
that separates HEAD from the red copy: a tip sighted 60 s ago (PINNED), a `renews: no` middle commit with no feed
line, and an opener sighted 25 h ago (PINNED); HEAD reads on past the middle commit and reads `stale`, the red copy
stops at it and reads `unknown`. Revise the spec to the main loop's ruling.

### Items

1. F-scope: add to §8, resolved: "What does this unit build, when the guard and the unsighted-to-unknown mapping are already in the tree?" (a) rescope it to the regression arm that pins the guard, red on the mixed input above; (b) retire the unit as WONTDO. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; no arm pins the guard today and the TOOL-dPlacedRequest-35 test block hands this case to this unit, so the arm is the unit's remaining value, and retiring it would leave that case unowned. widens: none · relaxes: none`.
2. Rewrite §1 Goal, §2 Scope and §4 Design/Evidence to the arm: the guard and the mapping are cited as landed by `path#symbol`, the unit adds the arm only, and the builder's measured readings stand as the evidence. Drop the claim that the tree compares an unsighted commit today.
3. Rewrite §6: AC1 becomes the mixed input above (HEAD `stale`, red copy `unknown`); AC2 and AC3 stay as observations the arm also makes (each reads `unknown -`) but are no longer claimed to go red; the old AC1 (emptied or deleted feed) is dropped as `TOOL-dPlacedRequest-17` AC6's, with §3 naming it. Amend §7's `New arm:` line to cover the new AC1 as its red and AC2/AC3 as its green observations, keeping the README rule 8 waiver clause.
4. Cite code as `path#symbol`; the builder's measured ages are each pinned on their own line.

### Acceptance

Spec 47 at its next rev carries the resolved fork, §1, §2, §4, §6 and §7 rewritten to the arm, and one §9 line naming
this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-47` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-47, and no fork left open. Pin every figure you write with DERIVED or PINNED on its own line,
never let a section sign or a section number stand before a unit word, and never quote a check's hit literally in
prose.

# Brief — aNimbleMend: unit 14, the lane opens only on a red of this branch's present state

**Serves:** research TOOL-aNimbleMend-14

## The prompt

> Build an opt-in mechanism (opted in by default in any repo) that allows two things: 1. bar findings and red fixes to be made inline, without a spec, with the work record maintained AFTER the fact. 2. passes run ONLY fast legs.

The owner's prompt is recorded whole in `memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md`. This unit is promoted from the closing diff review, whose record is `memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`; read that record whole, since it holds each finding's place, consequence and fix.

## The brief

### Goal
The closing review's one HIGH item: the red-fix lane reads every carried-forward `fail` row of the gate ledger as an open red, so with the key at its default the lane is open in the primary checkout on landing for a write that answers no current red. This unit bounds an open red by the row's own head, as the review record's corrected fix states, so the lane opens only on a red of this branch's present state.

### Items
1. H1 — The red-fix lane opens on any stale `fail` row of the gate ledger (findings 1, 7, 22; each high): build the Fix the review record states under that heading, with the arm or probe it names, and its left-shift gate or bug-class entry.
2. Write the spec at `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-14.md`, Tier-2, status SPECCED, order 14, in the shape of `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md`. Units 1 to 13 are CLOSED and frozen, so declare edges as `external` only and state each correction in this spec itself.
3. Every spec line stating a figure with a unit carries the word PINNED or a commit sha on the same line. The acceptance section cites no path the unit has not built yet. A criterion that needs a gate leg, a suite or a pass-leg run is the main loop's, and the spec says so in that criterion with a `permission:` line.

### Acceptance
- Each finding's fix is observed by the probe or arm the review record names for it.
- The hook run against the primary checkout's own ledger prints the refusal, and the open-red reader over that git directory returns an empty list.
- Each new or changed gate behaviour has an arm seen red.

### Gates
The full bar once, at the close, with `GATE_FULL=1`, without the self-tests and without the unattended kit gate leg.

### Non-goals
- Any finding of the review record this brief's items do not list.
- Any kit version, which the lander's mint moves.
- Any edit to a CLOSED spec.

### Limitations
- Build the head bound, never the newest-run bound the review record rejects.
- A held leg redded at HEAD by a full bar still opens the lane.

### Reuse
The seams each finding's `Where` line names in the review record, extended in place.

## Drawn from the session

> Verdict CLEAN WITH FIXES, round 1. 23 confirmed findings in 18 items: 0 blocker, 1 high item (3 raw: ids 1, 7, 22), 13 medium items (16 raw), 4 low.
— agent, the closing diff review's synthesis, 2026-11-12, over `1265772cc..c428a23c3` (PINNED, 2026-11-12)

## Owner confirmation

not asked — the run is unattended, and the unit is promoted under the mandate by the closing review's exit

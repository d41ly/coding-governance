# Revision — dLandedOwners: TOOL-dLandedOwners-1 rev-2, fork F1 resolved by the owner

**Serves:** research TOOL-dLandedOwners-1

## The prompt

> Build, file an ask (Recommended)

The owner's answer of 2026-11-19 to the main loop's question on fork F1 of
`memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-1.md`, picking option (a).

## The brief

### Goal
Fold the owner's pick of option (a) on fork F1 into the spec as rev-2, so unit 1 builds as specced and the main
loop files one ask at the close naming dDeclaredLoop's pending cycle row in `tools/loop/termination-pending.txt`.

### Items
1. Mark F1 resolved with the closed fork mark the spec format states, naming the owner and the date:
   `RESOLVED (owner, 2026-11-19): (a), build as specced; the main loop files an ask at the close naming the row.`
   Keep the options' text as the record of what was weighed.
2. Correct every sentence that cites F1 as open or as holding the disposition (section 3's non-goal, section 4's
   "The loop's termination read", section 5's risks), so each states the resolution: the held `loop termination`
   leg reads the row stale on the daily job until a later build bounds the cycle or re-owns the row, and the ask
   records that.
3. Bump the rev and add one revision-log line naming this record and the owner's resolution; no other design
   change.

### Acceptance
`bash tools/unattended/unattended.sh --plan dLandedOwners --paths` grades TOOL-dLandedOwners-1 READY, not FORKED;
`--check-specs dLandedOwners TOOL-dLandedOwners-1` prints no refusal; `check-memory-hygiene.sh --only 12 --spec <path>`
and `check-spec-tokens.py --spec <path>` are clean; every figure typed before a unit word carries a pin on its line or
sits in a code span on that line.

### Gates
The spec-format, spec-token and naming-lexicon checks the role allows; no other gate.

### Non-goals
No change to the predicate's design; no product code; no ask row, which the main loop files; no commit and no index
render, which the main loop does.

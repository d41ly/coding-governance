# TOOL-dUnstalledConvoy-32 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-32

The arms are case 3h3 of `tools/run-gates/run-gates.test.sh`, shared with
`TOOL-dUnstalledConvoy-31` — one fixture, five legs, two chunks, because the two units read the
same run.

## The arms, and the break each one was observed against

| arm | red-first verdict |
|---|---|
| AC1 an all-held chunk closes SKIPPED with its counts | RED — `---- chunk held: green  (0 ran, 0 failed, 0 skipped, 0 reused)` |
| AC2 a mixed chunk closes green and carries its own held tally | RED — the tally was absent from the line entirely |

Both discriminating, neither a control.

## The defect was reachability, not the rule

`chunk_close` already carried the rule and already asserted it in a comment: a chunk whose every leg
skipped reports SKIPPED rather than green, because calling that green would be the loudest possible
green-by-absence, one altitude above a single leg. What it lacked was any path from the newer skip
kind to the code that applies it. A rule that is correct and unreachable is worse than an absent one,
because the comment asserts it and everybody reading believes it.

## The one deliberate break

The chunk count line gained a fifth field, so the existing end-anchored arm
(`^---- chunk one: green  \(2 ran, 0 failed, 0 skipped, 0 reused\)$`) stopped matching. It was
UPDATED rather than loosened: an arm that stops anchoring stops proving the shape, and the anchor is
why a field silently appearing or vanishing is visible at all.

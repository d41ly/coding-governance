---
name: one-value-field-records-a-mixed-outcome
description: a per-subject field holding ONE value has to record an outcome that was mixed — take the value that DEMANDS something, never the one that demands nothing
kind: class
universal: true
---

# A one-value field meets a mixed outcome, and the wrong choice is the silent one

## Symptom

A record carries one value per SUBJECT — a disposition, a status, a verdict. The thing it describes
turned out mixed: some of the subject's items went one way and the rest the other. Both values are
true of part of it and neither is true of all of it, and the field cannot hold both.

Whichever value gets written, the record then reads as though the outcome was uniform. Nothing in
the record says it was not.

## Why it matters which one

The two values are almost never symmetric. One of them **demands** something downstream — a gate
looks for a consequence, a reader owes a follow-up — and the other demands nothing.

Writing the demanding value on a mixed outcome OVER-ASKS: a gate asks for evidence covering items
that did not need it, which is visible, arguable and easy to answer. Writing the non-demanding value
UNDER-ASKS, and the part of the outcome that needed a consequence disappears silently. A check that
never fires is indistinguishable from a check that passed.

So: **record the value that demands something.** A mixed exit therefore records the promote value
and never the fold one, and the field becomes a LOWER BOUND rather than a claim of uniformity, which
is the honest reading of a lossy field.

## Where it bit

`memory/builds/dMispairedQuote/RUN.md`, subject `TOOL-dMispairedQuote-1`, retrofitted 2026-09-01 by
`TOOL-dFoldedVerdict-3`. Its review loop exited `NON-CONVERGENT` at four standing blockers: three
were PROMOTED to a new unit and one was FOLDED into the spec. `--review --disposition` holds one
value per subject.

`promote` demands a new unit id the build's generated region must gain, and check 2 of the unattended
kit reds when it is missing. `fold` demands nothing at all. Recording `fold` would have retired the
whole exit's obligation on the strength of one blocker out of four, and the three promotions would
have gone unobserved by a gate written to observe exactly that. `promote` was recorded.

## The fix

Write the demanding value, and put the full accounting where it already lives — the spec revision
log, the review record, the commit that disposed of the items. Do NOT invent a per-item field to
carry the split: a second grammar nothing reads is worse than a lossy field everyone understands.

Say in the record's own provenance that the value is a lower bound and where the rest of the story
is. A lossy field that ADMITS it is lossy is fine; one that reads as complete is not.

## Arming it

**Not gated, and the gap is stated rather than implied away.** No check can see that an outcome was
mixed — the mixedness lives in prose the field summarises, and the record is append-only, so a value
already written cannot be compared against a second source that does not exist.

What IS gated is the absence: a graded record whose exited subject records no disposition at all is a
refusal in check 2 of the unattended kit, and a value outside the closed set is its own refusal
beside it. Neither can tell a correct one-value answer from an incorrect one. This rule is a
documented manual check, and the honest form of shipping it is to say which.

---
name: a-spec-run-close-owes-the-closing-review-override
description: a spec run writes no code, so its close always meets closing-review-recorded unmet, and a first close passed without that override is a close attempt spent learning it
kind: class
universal: false
---

# A spec run's close has no closing diff review to record

## Symptom

A chain build's spec run reaches `unattended.sh --close` with every unit deferred and its audit
chain recorded, and the close blocks on `closing-review-recorded`: no `diff-review` record names the
run's units, because a spec-only diff is reviewed by its spec audit, never by a closing diff review
over code that does not exist yet.

## Where it bit

dKeptSession's first close blocked on it beside two reds of its own, and its later closes passed
`--override closing-review-recorded` with the reason the owner's ruling gave: the six-round audit
chain is the review of the spec-only diff, and the build run's closing diff review over the code stays
owed. dPlacedRequest's spec run met the same item and recorded the same disposition in
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-owner-review-until-no-high.md`
(PLAY-dClosedLoop-37 asks for the close section to state it).

## The fix

On a spec run's first `--close`, pass `--override closing-review-recorded --reason` naming the audit
records that stand in for the closing review and the build run that still owes one, beside
`--override specs-audited` for any promotion the ruled chain end left unaudited. Check the run kind
first: a build run that writes code owes the real closing review, and this override there is the
skipped-review defect, not this class.

No machine gate states the spec run's close ahead of `--close`, whose refusal is the first reader,
until PLAY-dClosedLoop-37 writes the recipe into the close section.

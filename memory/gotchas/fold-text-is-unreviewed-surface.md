---
name: fold-text-is-unreviewed-surface
description: a review round's fixes are folded into fresh prose nobody has reviewed, and that prose is where the next round's findings are
kind: class
universal: false
---

# The fold is unreviewed surface

## Symptom

A review round finds defects. The fixes are FOLDED into the spec or the code, the round is recorded
as answered, and the fold text ships. That text is freshly written, it is the only text in the
document nobody has reviewed, and it is where the next round's findings live.

The tell is a by-kind split. Classify each finding of round N+1 as one the fold CREATED, one where
the fold misread its own finding, or one round N simply missed. If the first two dominate, the loop
is no longer measuring the design — it is measuring the last fold.

## Where it bit

Measured on `dFramedEntrypoint`, whose round-2 spec audit is at
`memory/builds/dFramedEntrypoint/reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md`.
That record states the split in its own words: of 62 surviving findings, 25 were created by the fold
and 17 were the fold misreading its own finding, against 20 that round 1 had missed. So the fold
produced more findings than the review it was answering had failed to catch.

Measured again on `dTieredTribunal`, over three rounds, and the second measurement is the one worth
keeping because it kills the obvious remedy. Round 1 was folded by four parallel agents and round 2
confirmed 20 fold-created findings of 29. Round 2 was then folded BY HAND, on the reasoning that
fewer authors would mean fewer manufactured defects. Round 3 confirmed 20 fold-created findings of
32 — the same absolute count. **Author count is not what drives this.** The failure mode moved
instead: findings where the fold answered its own finding only in part rose from 6 of 29 to 11 of 32.

The recurring shapes, from those rounds, are worth knowing by name. A fold invents a line citation
it did not re-derive. A fold answers one of a finding's two halves and records the whole finding as
answered. A fold deletes three stale numbers, asserts none remain, and leaves a fourth standing. A
fold narrates a revision history that never happened, to justify an edit. And a fold widens one
carrier of a rule while leaving its two siblings governing the old shape.

A merge resolution is fold text too. On `dLoggedFlight` the resolution of a conflict in the unattended
Skill kept one side's sentence and the other side's mechanism, and dropped a guard neither side meant
to drop. No round read it until the closing diff review named the reconcile in its scope (R2-L3).

A fold can also go unreviewed by position. On `dClosedLoop`, 2026-10-16, the layers round's follow-up
fold, `1bc4883fe`, was the base of the next review's range, the library round's `1bc4883fe..aa9639d98`.
A range excludes its base, so that review read none of the fold, and no record named the debt. The
probe that found it found two more unreviewed folds and three designs no review had read
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-state.md` `[unreviewed]`).

It bit again in dClosedLoop's answers fold, 2026-10-18, reviewed twice (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-answers-reviews-compared.md`).
Seven of its seventeen defects were the fold's own text saying more than its source: a credential rule the owner's words
did not set, a trigger wider than the answer, a reason that failed on the floor step's down, a research edit count read
as a declaration count, a correction drawn from a census of one language, an evidence sentence that measured another
gap, and a separator lost inside an edited sentence. Run A alone found the one that was high.

It bit again in the flow and roles adoption's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`).
FA-6's fold narrowed the owner's chosen option, putting `roles.model.<role>` on the keys presets never touch, and
dropped the house file's required `[effort] default` with no destination. Both sat in fold prose the owner's answer
did not cover.

## The fix

**No machine gate**, and this is a documented check rather than an unwritten one. Nothing static can
tell a fold-created sentence from any other sentence, so the remedy is that the class is NAMED and
reaches the checklist of the rounds that need it. That is what
`python tools/memory-tree/gotchas.py --for-diff` is for, and it is why the anchors below matter more
than the prose does.

**The anchors, and why these three.** A spec fold writes under a build's `/spec/` directory, so that
token is the one that reaches a fold round's own write surface — it selects every tracked path under
a spec directory and nothing else. `memory/guides/BUILD-METHOD.md` reaches a diff that edits the fold
rule itself. `tools/workflows/tier2-review.js` reaches the harness that primes a fold round. The
spelling deliberately NOT used is a build-directory token, which selects roughly two thirds of this
tree and would put this class on almost every checklist; noise on a checklist is how reviewers learn
to skip the checklist.

Four practices, each earned by one of the shapes above:

- **Verify a did-not-land claim by reading the BODY at HEAD, never a revision log.** A revision log
  records what somebody believed they changed. `git diff` records what changed.
- **Fold a DELETION rather than appending a negation** beside the text it contradicts. Two sentences
  that disagree are worse than one wrong sentence, because a reader cannot tell which is live.
- **Re-derive every number and every citation the fold writes**, at the moment of writing it. A fold
  correcting a stale figure with a second stale figure is the commonest single instance.
- **When a finding names several carriers, edit all of them or record the refusal.** Answering one
  and logging the finding as folded is what turns a fold-created defect into an invisible one. Grep
  them for the old value's pronoun forms too (`it`, `the flag`), not only its spelling, and a fold
  that widens a claim from one value to two re-reads the code path for the SECOND value, not only
  the ruling behind the first (`dAlignedCarrier`'s closing review, round 2, L3 and M2).

**A fold's review is a fact of the history, so check it there.** Each report's Reviewed line is a
blob set or a range, and a range excludes its base. A fold commit at a range's base, or outside every
range, is unreviewed however many rounds ran around it. `coverage.py`, in the state record's
`[instrument]`, reads every report's line and names each such commit, with two reviewed commits as
its controls.

The round that follows a fold should be primed AT the fold rather than at the document: pass it the
previous round's confirmed set, tell it the diff under review is the fold, and require the by-kind
split in its record. `memory/guides/BUILD-METHOD.md` M8 already states the round-N-above-1 rule for a
diff review; a spec audit needs the same instruction and gets it from the driver rather than from a
rule. The harness that primes a diff review, `tools/workflows/tier2-review.js`, carries exactly one
sentence of fold priming today.

## What this does NOT say

It does not say a fold is optional, and it does not say a converged loop should keep running. The
build method's exit condition is a strictly falling confirmed-BLOCKER count, and that count can
discharge while fold-created findings are still the majority of everything else — which is exactly
what `dTieredTribunal` measured. Whether to run another round once the blocker rule has discharged
is the owner's call and not the loop's, and this record exists so that call is made with the split
in front of the person making it.

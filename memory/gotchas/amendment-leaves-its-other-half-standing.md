---
name: amendment-leaves-its-other-half-standing
description: a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts
kind: class
universal: false
---

# The amendment leaves its other half standing

## Symptom

A criterion, rule or claim is edited to correct it. The edit is disclosed, argued and correct. And
something that was written to sit BESIDE the old wording is not edited with it: a trailing clause of
the same sentence, a scope item that gates the criterion, a revision-log line that does the old
arithmetic, an authorization carve-out sized to the old edit. The two halves then disagree, and
because each reads fine on its own the disagreement is invisible to whoever made the change.

It is worse than an ordinary stale copy in one specific way. A stale copy drifts by neglect, over
time, and nobody claims to have just checked it. This one is produced by the act of checking — the
author has the file open, has just reasoned carefully about the exact sentence, and ships the
contradiction in the same keystroke as the correction. The care spent on the half being amended is
what makes the other half feel already handled.

## Where it bit

Build dTieredTribunal, run 2, the post-acceptance spec audit. Nine distinct defects, and four were
this class, all of them introduced by the amendments made twenty minutes earlier in the same session:

- The BLOCKER. A criterion demanded ZERO matches under a directory; it was already false at two, so
  its opening was rewritten to bless the survivors as historical citations. The SAME SENTENCE ended
  "and every surviving hit outside builds and archive is the backlog row" — a clause that was true by
  construction only while the opening demanded zero. After the amendment, four hits existed and three
  were under that directory, so the two halves returned opposite verdicts on one list.
- A scope item still demanded a provenance marker per edited SITE after the matching criterion had
  been moved to per-MECHANISM, so the spec asked for two different things one paragraph apart.
- An amendment accepted a seven-line edit to a file whose scope carve-out authorized two, widening
  the authorization by citing a criterion that happened to need it. Authorization by side effect.
- A revision-log entry kept doing arithmetic against a row count that the amendment had made
  irrelevant, and the count was wrong anyway.

None of the four was a lowered bar. Every one was a correct amendment with an uncorrected neighbour.

## The fix

**Amend the RULE, not the sentence.** Before writing the new wording, find everything whose truth
depended on the old wording, and treat that set as part of the edit rather than as follow-up. In a
spec that set is small and enumerable: the rest of the criterion's own sentence, the scope item that
gates it, any carve-out sized to the edit it authorizes, and the revision-log entries that reason
about it.

Two mechanical arms are worth more than the discipline, because they cannot forget:

- A fork or criterion whose RESOLVED text promises a follow-up must name a live backlog row. A
  promise with no row is a promise nobody can find.
- A file named in a spec's scope must appear in its inventory table. A scope item with no row is an
  authorization with no accounting.

Neither catches the blocker above. What catches that one is reading the whole sentence after editing
its first half — and the reason to write this down is that the author had, and did not.

There is **no machine gate** for this class today, and the two arms above are filed as
`TOOL-dTieredTribunal-24` rather than built here. Saying so plainly matters more than usual for this
particular record: a class whose whole subject is a half-finished edit would be a poor place to leave
"a gate exists" and "a gate was never written" indistinguishable from outside.

## The anchors

The taken set is `memory/builds/` — where specs, their criteria and their revision logs live, which
is the only surface on which this class has been observed. It is deliberately NOT `memory/`, which
would select on every note and index in the tree, and not the two spec paths that produced it, which
would make the record a citation of one build rather than a class. The record that found it is
memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-post-acceptance-round1.md,
written without backticks so it stays evidence rather than becoming a fifth anchor.

## What this does NOT say

It does not say amendments are suspect. Three of this build's amendments were correct and complete,
and the criterion they replaced was genuinely mis-specified in every case; refusing to amend would
have left a spec that graded position instead of property. The claim is narrower: the moment of
amending is a moment of unusually high confidence, and that confidence is local to the clause under
the cursor.

It also does not say a reviewer will catch it. The reviewer that found these four was reading the
specs as specs, at pinned blobs, hours after the edits, with no memory of having made them — which is
exactly the distance the author does not have.

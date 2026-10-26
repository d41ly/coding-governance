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

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Twice: the memory
plan's `[migration]` opened "Nothing is rewritten by hand" above a bullet that routes decision rows by hand, and
dOrderedCharter held `map_lib`'s re-export for one release after the deprecation window became a policy of two.

It bit again in the last three folds' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-folds-reviews-compared.md`). Four more: the memory
plan's deploy-overlay row kept `deploy.toml`'s level-0 units after IA-1 moved them out; dOrderedCharter's own upgrade
steps kept their old list after the fold gave the row three adopter-visible moves; the fates row kept the bug-class
selector on dLinkedLibrary after SA-7 moved it; and P8's "only through edges" and P38's "changes" outlived the exclusion
list and the gate's narrower predicate.

It bit again in the night pass two's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-reviews-compared.md`).
Folds landed in v2 and stopped there. The over-budget refusal survived in layer-instruction, layer-roles and the
adopter record; `FANOUT_CAP` in the systems and adoption records; agent-cap as the slot counter in the review-system
and adoption records; and the replaced fates of `agent-cap.js` and `gotchas.py`. dGroundRules also never carried the
two agent-cap rules point 7's table gave it.

It bit again in the flow and roles adoption's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-adoption-reviews-compared.md`).
FA-6's fold gave dBoundRoles the `roles.effort.*` keys and left the same row, and the systems record, keeping effort
in the house file until dConvergedCharter. The record's `[chain]` kept its lines from before FA-3, and
`instructions.stale` was read for rows with only `order` defined.

It bit again in the owner's answers' closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two-answers-reviews-compared.md`).
The answers' fold added an admission queue to dWellOiledMachine and left the same row's ledger fallback refusing the
Workflow call the queue now holds, at the limit of five that NT-28 replaced. The night record's analysis kept the
tool-call notice and the doorbell-only database that the answers replaced.

It bit again in the parked debt's closing review, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-parked-debt-reviews-compared.md`).
The cloud fold put the fenced push and the tombstone on dPlacedRequest and stopped there: layer-runtime still
called the re-read before the push safe, flow-steps' unlease items still deleted the lease, and the cloud
record's own `[chain]` kept a plant from before the owner's fleet. The stall fold left the route-back rule's
owner item standing twice in flow-steps, and two layer-runtime fixtures asserting the outcomes it replaced.

It bit again in dTrueNorth's closing diff review, 2026-10-22
(memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md, findings 10,
15 and 24). TOOL-dTrueNorth-16 S21 moved check 29's staged trigger into its verb, and its body comment, the
HYGIENE item and the kit README took the new rule; the hygiene engine's header kept TOOL-dTrueNorth-3 S5's
"held unless the commit stages a path under a build's spec/ folder or the conf", and never named check 30,
whose own staged trigger landed beside it. TOOL-dTrueNorth-26 S12 to S14 rewrote the header to point at the
two block comments, so the rule is stated once and the header carries no second copy to strand.

It bit again in dGroundRules' spec run, 2026-10-23
(memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-62.md, from the closing diff review's H4).
TOOL-dGroundRules-21 S12 changed what `read_default_value` returns for one case, a derived default, from a value
to a refusal; TOOL-dGroundRules-9's consumes-from edge on the reader still expected an unset `budgets.<cap>` to
read as no file value, source `default`. Both units were built, and every cap read `refuse` until
TOOL-dGroundRules-62 typed the refusal and the caps module answered that type alone as unset.

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

**Checklist line: a change to a durability default re-reads every resume promise.** Build aMendedFleet
moved the review harness's judge type to a default under which no judge writes its result file, and
left standing every note, relaunch line and protocol step that promised a re-run reuses those files.
The default is the amended half; the promises are the other half, spread across the harness, the
build harness, the driver and two rendered guides. The harness template,
`tools/workflows/tier2-review.template.js`, is anchored so the next edit to it selects this class.

**Checklist line: a fold that moves an owner or grows a check re-reads the record's summaries of it.** Build
dClosedLoop's night pass folded its closing review: the playbook set check moved to dIndexedDesign, and the map's
fates check grew from six arms to twelve findings. The fold brought the record's fold and instrument sections in
line, and left the per-point sections, written before it, saying "Test runs the set check (dWitnessedBar)" and "Six
arms hold every kit to a row". Those sections were what the owner would read first. Grep the record for the old
owner and the old count before calling a fold done.

**Checklist line: a later unit that changes a shared function's return for a case greps every
consumes-from edge naming that function**, and restates each consumer's expectation in its own spec:
kept, or changed with the consumer's code in the same unit. The earlier unit's edge is the other half,
and it reads fine until both are built.

There is **no machine gate** for this class today, and the two arms above are filed as
`TOOL-dTieredTribunal-24` rather than built here. Saying so plainly matters more than usual for this
particular record: a class whose whole subject is a half-finished edit would be a poor place to leave
"a gate exists" and "a gate was never written" indistinguishable from outside.

## The anchors

The taken set is `memory/builds/` — where specs, their criteria and their revision logs live — and
the review harness template named above, the one code surface where this class has been observed. It is deliberately NOT `memory/`, which
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

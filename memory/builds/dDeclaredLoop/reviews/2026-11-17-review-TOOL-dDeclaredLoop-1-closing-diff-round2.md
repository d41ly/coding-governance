**Serves:** diff-review TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112

# Tier-2 diff review — dDeclaredLoop (the Spine build of the dClosedLoop chain), round 2

Provenance: gov-diff-reviewer finders over five lenses, gov-skeptic batches, synthesis by gov-synthesizer, at head 99a1b7a06 on branch/unattended-declared-loop-d56bf0.

Range reviewed: bada76713db927cbdaf039bf0c2ff4019f838ca0...99a1b7a06b07d7605851be2f659a0ee02d6d3af4 (ROUND 2).

## Verdict: CLEAN WITH FIXES

No blocker and no high survived the skeptics.
Two items stand, both LOW.
By raw confirmed finding the tally is also 2: 0 blocker, 0 high, 0 medium, 2 low.
Both items are records defects in the round-1 record and change no behaviour.
This round does not re-grade round 1's two highs and five minors.
Those are promoted to units at the closing review's exit and are not fixed in this fold.
This round reads the fold since round 1's tip: the round-1 review record and the run-state row that records the round.
No product code changed in the fold.

Review shape: intensity full, raw 2, confirmed 2, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 2/2 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 0 judged sound, 0 judged UNSOUND, 2 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document supplied as `specs`, beside the range's commit messages.
- Checklist: 23 items, acquired by the harness from --for-diff bada76713db927cbdaf039bf0c2ff4019f838ca0..99a1b7a06b07d7605851be2f659a0ee02d6d3af4, each assigned to exactly one lens: security 5, correctness 5, seams 5, verification 4, intent 4.
- By design: the caller's byDesign.
- Refuted findings shown: 0. Same-address pairs shown: 0. Twins flagged: none.
- Every integrity count that must be zero is zero, so the run is complete.

## Items

### 1. LOW — the round-1 record says its items are fixed before the merge bar, but the run's rule promotes them (finding 1)

- Where: memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md@ec07f524:14.
- What is wrong: the line reads 'Every item is owed a fix, or a close deviation for the records items, before the close's merge bar and RED-first observations run'.
- The record never mentions promotion.
- The governing rule is the owner's 2026-10-04 rule, quoted in verb_review at tools/unattended/unattended.sh@c098d58a:13601-13604.
- That rule promotes every finding the closing diff review confirms: one unit for each BLOCKER and HIGH, with the MEDIUMs and LOWs batched.
- The run applies that rule: the RUN.md row added in this fold records 'round-highs 2 · round-minors 5', and the round's framing promotes at the exit.
- The record therefore gives two answers to what happens to the same items.
- Consequence: no reader parses the line, so behaviour is unaffected.
- Following the record, whoever runs the close next may fold the two HIGH items into this build before the merge bar, instead of promoting them.
- Those two items are the guard.py merge grading and the resolve_memory_root move.
- Grade: LOW, the binding grade, because the defect sits only in a record.
- Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): put the subject's exit rule in the synthesizer's task.
- For a closing review that rule is promote, per verb_review's 2026-10-04 rule; for a spec audit it is read_spec_exit_rule.
- The synthesizer then states the disposition from that rule, instead of writing a fixed 'owed a fix' sentence into every closing-review record.
- The finder's proposal cures only the cited instance: reword line 14 so it states the promote disposition.
- The finder's example wording: 'Every item is promoted at the closing review's exit: one unit for each HIGH, and the MEDIUMs and LOWs batched; the two records items are corrected through a close deviation.'
- Left-shift gate: add a fixture closing-review synthesis to the tier2-review self-test.
- The fixture fails when the record's disposition sentence differs from the subject's exit rule, for example when it says 'owed a fix' and the rule is promote.
- Disposition: class:two-answers-to-one-question.

### 2. LOW — one code site in round-1 item 2 has no blob pin (finding 2)

- Where: memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md@ec07f524:65.
- What is wrong: item 2 cites its fourth sibling site as a bare `tools/loop/upstream.py@43147593:297 (write_upstream_record)`.
- Every other site in the same Where list (lines 61-64) is pinned as file@blob:line.
- Probe: `git rev-parse bada76713:tools/loop/upstream.py` returns 43147593.
- Line 297 at that blob is the `memory_root = (read_design_conf(root).get("MEMORY_ROOT") ...` line, so the cite is correct today.
- Consequence: the unit promoted from item 2 inherits an unpinned address for the site the skeptic added.
- Once upstream.py is edited, line 297 drifts with nothing to anchor it, and a reader cannot tell which reviewed text was meant.
- Only the record is affected.
- Grade: LOW, the binding grade, because the defect sits only in a record.
- Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix): pin every file:line cite in the round-1 record to its blob at bada76713 (file@blob:line), not only line 65.
- That covers the cites on lines 66, 72 and 103 and the per-finding table rows at lines 129-135.
- Make the change in the promoted unit's spec or in the next generated rewrite of the record.
- The record must not be edited by hand, because it is persisted as written.
- The finder's proposal cures only the cited instance: write line 65's cite as `tools/loop/upstream.py@43147593:297 (write_upstream_record)`, matching the item's other sites.
- Left-shift gate: add a memory hygiene check over review records under memory/builds/*/reviews/.
- The check refuses a path:line code cite with no @blob pin in an item's Where list or in the per-finding table.
- A tier2-review self-test fixture should show the check firing on one unpinned cite.
- Disposition: class:fold-text-is-unreviewed-surface.

review-shape kind=diff-review round=2 intensity=full at=synth raw=2 confirmed=2 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=0 low=2 agents=8 out-tokens=27140 trigger=owed shape=- efforts=- role-sha=-
review-round round=2 limit=- prior=2 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | seams | memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md:14 | low | low | confirmed | Line 14 of the new round-1 record (added in this fold) reads 'Every item is owed a fix, or a close deviation for the records items, before the close's merge bar and RED-first observations run'. Nowhere in the record is promotion mentioned. verb_review at tools/unattended/unattended.sh quotes the owner's 2026-10-04 rule that every finding the closing diff review confirms is PROMOTED: one unit per BLOCKER and HIGH, with the MEDIUMs and LOWs batched. The RUN.md row this fold adds records 'round-highs 2 · round-minors 5', and the task framing also says promote at the exit. So the record contradicts the rule the run applies. No reader parses the sentence. Its only effect is that it can mislead whoever runs the close next, so this is low. | instance | amendment-leaves-its-other-half-standing | class:two-answers-to-one-question |
| 2 | intent | memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md:65 | low | low | confirmed | Line 65 of the round-1 record, which this fold adds, reads `tools/loop/upstream.py@43147593:297 (write_upstream_record)` with no blob pin. The four other sites in item 2's Where list (lines 61-64) are written as file@blob:line. `git rev-parse bada76713:tools/loop/upstream.py` returns 43147593cf4d…. Line 297 at that blob is the `memory_root = (read_design_conf(root).get("MEMORY_ROOT") ...` line, so the cite is correct today but has nothing to anchor it once the file changes. The fold introduced it, so it is in scope. It affects only the record and changes no behaviour. | instance | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |

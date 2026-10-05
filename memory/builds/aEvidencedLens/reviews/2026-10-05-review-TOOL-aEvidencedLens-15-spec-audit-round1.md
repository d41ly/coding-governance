**Serves:** spec-audit TOOL-aEvidencedLens-15

# aEvidencedLens — spec audit of TOOL-aEvidencedLens-15, round 1

*Node `a`, 2026-10-05. This is a Tier-2 adversarial pass over the spec for the last open unit of the
build. Five finder lenses ran, then a skeptic stage prompted to refute each finding, then one
synthesis. Findings are graded by consequence under the run's severity rubric.*

**Round: 1.** Range reviewed: the subject below, pinned at the blob it was read at, plus the tree it cites.

- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md@47d741cd66a04214a52584a9a043ec6ce591d036`

## Verdict: CLEAN WITH FIXES

No blocker and no high finding survived. Two medium findings and four low findings are confirmed.
All six are defects in the spec's acceptance text or its declared records, and none of them changes
what the observation does. Each one should be fixed in the spec before unit 15 is dispatched.

## Review shape

Intensity full, raw 6, confirmed 6, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 0 | 0 | 0 | 0 | 0 | - |
| reuse | yes | 0 | 0 | 0 | 0 | 0 | - |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

The adjudicated tally by item is 0 blocker, 0 high, 2 medium and 3 low, which makes 5 items. By raw
confirmed finding it is 0 blocker, 0 high, 2 medium (ids 4 and 5) and 4 low (ids 1, 2, 3 and 6).
Findings 2 and 6 describe the same defect from two lenses, so they are merged into one low item.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 3/3 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate
  refutations demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 5 judged sound, 1 judged UNSOUND, 0 with no fix proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 15 spec documents were supplied as `specs`, as sibling context.
- Checklist: 11 items, each assigned to exactly one of 5 lenses (coherence 3, grounding 2, reuse 2,
  blast-radius 2, failure-envelope 2).
- Move check: no checked subject moved.

Every counter above that could mark the run incomplete is zero, so this run is complete. The zero
yield from the grounding and reuse lenses is therefore a returned result, not a gap. It is still
only evidence that those two lenses found nothing on the generic brief.

## Findings

### MEDIUM — id 4: the only staged break never touches the masked line

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`, section 6
AC3 and section 2 S4.

AC3 stages its only break in step 1 of the probe. The class mask never touches that line. In
`tools/workflows/tier2-review.js` the `inputPrint` value is used at two places only: the key at
:702 and step 3's directory template at :720. So the mask writes `<KEY>` on step 3 alone, and no
liveness arm tests the mask's boundary there.

A mask broader than S1 would pass every criterion. One example is a mask that normalises the whole
step-3 directory spelling, which is the regex alternative section 4 itself rejects. AC1 would still
count 1 token, AC2 would still red under `--mask-key`, and AC3 would still red on the step-1 edit. A
real change to step 3's template would then read green, such as `<the first 12 hex of the head sha>`
becoming `<the first 16 hex ...>`. The observation would certify the very line it exists to cover.
The path needs the build to depart from S1's exact mask, and the effect is limited to a one-shot
ledger observation, so the grade is medium.

**Fix (judged SOUND by the skeptic):** Add a second staged break to AC3 and S4 on step 3's own line,
next to the masked value. For example, change `<the first 12 hex of the head sha>` to `<the first
16 hex of the head sha>` in a scratch copy of the HEAD render. Require the class-masked comparison
to red naming `resume:probe`, with the token count still 1. Record the outcomes of both breaks in
the AC4 ledger.

**Left-shift:** add a §10 checklist entry for the failure-envelope lens: "every staged break in a
masked comparison must sit on a line the mask writes, as well as on one it does not". A gate could
later grep a spec's staged-break criteria for a line reference that matches the mask's write site.

### MEDIUM — id 5: the HEAD bytes observed are not tied to the HEAD blob recorded

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`, section 6
AC1 and AC4.

Only the BASE side is read from the object database. AC1 passes the working-copy file
`tools/workflows/tier2-review.js` as the HEAD render, while AC4 records the HEAD blob from `git
rev-parse`. No criterion checks that the bytes observed are the blob recorded.

If the working copy differs from HEAD when the driver runs, the ledger names a blob the observation
never read. That can happen through a concurrent session, a stale re-render or an uncommitted fold
edit. Unit 13's ledger had to assert by hand that the working copy was clean against HEAD, and this
spec does not carry that over. The path is narrow and the effect stays inside one ledger record, so
the grade is medium.

**Fix (judged SOUND by the skeptic):** In AC1, take the HEAD side from the object database too, as
`git show HEAD:tools/workflows/tier2-review.js` saved to the scratchpad, mirroring the BASE fixture
line. Alternatively, require the driver run to be preceded by `git hash-object
tools/workflows/tier2-review.js`, with that value equal to the AC4 HEAD blob, and red when they
differ.

**Left-shift:** add a §10 checklist entry: "an observation that records a blob id must read its
bytes from that blob, or assert hash-object equality before it runs". This applies to both sides of
any BASE/HEAD comparison.

### LOW — id 1: the Edges block omits units 1 and 12

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`, section 3
Edges.

The Edges block declares only `consumes-from TOOL-aEvidencedLens-13`. S2 and AC1 rest on
`TOOL-aEvidencedLens-12` having landed. AC2's red-when ("the print did not move") rests on the
REVIEW_SHAPE move from `TOOL-aEvidencedLens-1`. Unit 13 makes the same reliance and declares both
edges. TEMPLATE-SPEC's Edges rule exists for this case, because nothing greps for an undeclared
dependence. The edge readers, `check-memory-hygiene.sh` and `tools/unattended/lib-unattended.sh`,
therefore do not see it. Units 1 and 12 are CLOSED, so nothing reads differently today, and the
effect is an incomplete record.

**Fix (REJECTED by the skeptic; the skeptic's corrected fix follows):** Add the two consumes-from
bullets to unit 15's section 3 Edges. In the same commit, add the reciprocal bullets to the closed
siblings:

- Add `- **hands-off** `TOOL-aEvidencedLens-15` — the harness as this build ships it, which unit 15
  observes from BASE` to unit 12's Edges.
- Add `- **hands-off** `TOOL-aEvidencedLens-15` — the REVIEW_SHAPE move that changes inputPrint,
  which unit 15's key-only liveness rests on` to unit 1's Edges.

Give each touched spec a revision-log line. Then run `check-memory-hygiene.sh` without `--staged`,
because the joins are held under `--staged`, and confirm check 12 stays green. The finder's
one-sided proposal is not safe to apply: check 12's reciprocity join is bidirectional, and it would
red memory hygiene.

**Left-shift:** extend check 12 with a reliance probe. A Tier-2 spec whose criteria name another
unit id in an "after X lands" or similar dependency phrase, without a matching consumes-from edge,
would red. Until that exists, add it to the coherence lens's checklist.

### LOW — ids 2 and 6 (merged): "both prints" and "the HEAD run" undercount the class

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`, section 2
S5, section 5 observability, and section 6 AC2 and AC4.

S5, the section 5 observability line and AC4 require the ledger to carry "both prints". AC2 names
"the HEAD run's print". The design runs two renders over two arg sets, so there are four stub runs
and four distinct `inputPrint` values. The script derives `inputPrint` at
`tools/workflows/tier2-review.js:696` from args that differ between round 1 and round 2. Unit 13's
ledger recorded four distinct values for the same arg sets.

A ledger that records only one BASE/HEAD pair satisfies AC4 as written. A driver that stops at the
first red under `--mask-key` satisfies AC2. Half of the evidence could go unrecorded while every
criterion reads green. AC1's per-run token counts still show that the mask reached every probe, so
the effect is an incomplete record only.

**Fix (judged SOUND by the skeptic, for both findings):** In S5, section 5 and AC4, say "the four
prints, BASE and HEAD for each arg set". In AC2, say that the red names `resume:probe` and prints,
per arg set, the HEAD run's print left standing.

**Left-shift:** add a §10 checklist entry: "a criterion over a multi-run observation counts per
class member (per arg set, per render), never with an instance count such as 'both' or 'the'".

### LOW — id 3: the dispatch write set omits the two generated indexes the pass rewrites

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md`, section 4
Files touched (estimate).

Unit 15 is the build's last non-terminal unit, at order 9 with every other unit CLOSED. The pass
that flips its status header to CLOSED therefore also flips the derived build status from SPECCED to
CLOSED. `gen_build_index.py` then removes the build's row from `memory/LIVE.md` and rewrites its row
in `memory/ledger/2026-10.md` in the same commit. Section 4 declares only the acceptance ledger, the
README and the spec's own region. The pass will write two files its `--dispatch` never declared.
Check 23 counts only passes that overlapped a sibling, and unit 15 runs alone, so the effect is a
wrong record of what the pass wrote rather than a red bar.

**Fix (judged SOUND by the skeptic):** In section 4, add `memory/LIVE.md` and
`memory/ledger/2026-10.md` to the dispatch write set. Say why: this is the last open unit, so
closing it re-renders the build status. Declaring them is safe here. The rule against declaring
generated indexes exists because a row that no later pass writes stays open, and this pass does
write them.

**Left-shift:** have `--dispatch` derive the generated-index writes itself. When the dispatched unit
is the only non-CLOSED unit in its build, it should add those two paths to the declared set, or warn
that the declaration omits them.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 3 Edges | low | low | confirmed | Re-read blob 47d741cd: section 3 Edges (lines 61-65) declares only consumes-from TOOL-aEvidencedLens-13. Yet S2 (line 32) and AC1 (line 133-134) rest on 'after TOOL-aEvidencedLens-12 lands', and AC2's red-when (line 144-145) rests on the print moving, which is unit 1's REVIEW_SHAPE move. Unit 13's spec (lines 82-87) declares consumes-from 6, 12 and 1 for the same reliance. TEMPLATE-SPEC section 3 Edges says a criterion resting on something the unit does not build is why an edge is DECLARED. The dependence is only transitive through unit 13 today. Units 1 and 12 are CLOSED, so the effect is an incomplete record: low. On the fix, check-memory-hygiene.sh:2262-2264 shows check 12's reciprocity join is bidirectional. A consumes-from bullet with no matching hands-off back prints 'that unit declares no matching hands-off back' and fails 12. grep shows unit 12 hands off only 13 (line 71), and unit 1 hands off 2, 11 and 13 (lines 71-75), never 15. The population row (U) carries no status filter, so CLOSED Tier-2 specs past SPEC_EDGES_CUTOFF 2026-09-08 are joined. The fix as written reds memory hygiene. Order is fine: 15 is at order 9, 12 at 7 and 1 at 1. | unsound |
| 2 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 2 S5, section 5 observability, section 6 AC2 and AC4 | low | low | confirmed | Re-read blob 47d741cd. S5 (line 43), the section 5 observability line and AC4 (line 154) all say 'both prints'. AC2 (line 142) says 'the HEAD run's print value'. The design loop (lines 87-91) runs two renders over two arg sets, so four keys and four prints exist. grep of unit 13's acceptance ledger (lines 29-30) shows four distinct values for the same arg sets: round 1 aada6477 at BASE against 6380ce0a at HEAD, and round 2 30f26c60 against 62ba7747. A ledger that names two of the four prints satisfies AC4 as written. AC2 does not say which of the two HEAD prints to name. Only this unit's ledger evidence is affected, and AC1-AC3's outcomes do not change, so the severity is low. | sound |
| 3 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 4 Files touched (estimate) | low | low | confirmed | Re-probed. In memory/LIVE.md:12 and memory/ledger/2026-10.md:9 the build's status is SPECCED. The gen:build-units table in the README shows units 1-14 CLOSED and only 15 SPECCED. gen_build_index.py derive_status returns the first PRECEDENCE token (INPROGRESS, BLOCKED, OPEN, SPECCED, DEFERRED) any unit holds, otherwise CLOSED. So unit 15's own header flip to CLOSED makes the build CLOSED, which removes the LIVE.md row and rewrites the ledger row. git show 90a137600 confirms that a unit pass flips its own header from SPECCED to CLOSED. Spec section 4 declares only the acceptance ledger, the README and the spec's own region. The impact is a wrong record of what the pass wrote, not a red bar: .unattended.conf says check 23 counts only passes that overlapped a sibling, and unit 15 is alone at order 9. | sound |
| 4 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 6 AC3 (and section 2 S4) | medium | medium | confirmed | Re-read the spec. AC3 (:146-149) stages its only break in the probe's step 1, and S4 names no line. In tools/workflows/tier2-review.js, inputPrint is interpolated only at :702 (the key) and :720 (step 3's directory template), so the mask writes <KEY> only on step 3. A mask broader than S1, such as the step-3 regex normalisation that section 4 itself rejects, would still give a token count of 1 (AC1), still red under --mask-key (AC2), and still red on a step-1 edit (AC3). No criterion would catch it, so a real move on step 3 would read green. S1 defines the mask exactly, so this happens only if the build deviates from S1. That is a narrow path with a contained effect: a one-shot ledger observation, not a shipped check. | sound |
| 5 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 6 AC1 and AC4 | medium | medium | confirmed | Spec at HEAD equals pinned blob 47d741cd. AC1 (lines 133-140) passes the working-copy path tools/workflows/tier2-review.js as the HEAD render, and its fixture line pins only base.js to the object database. AC4 (150-154) records the HEAD blob via git rev-parse. No criterion ties the observed bytes to that blob. grep on unit 13's ledger shows line 17 'the working copy clean against it' as a hand assertion, and spec 15 carries no equivalent. The path is narrow (a dirty worktree during one observation), and the effect is contained to one ledger record, so medium. | sound |
| 6 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-15.md:section 6 AC2 and AC4, section 2 S5 | low | low | confirmed | S2 and AC1 run two diff-kind arg sets, yet AC2 (line 142) says 'the HEAD run's print value' and S5 (43) and AC4 (154) say 'both prints'. tools/workflows/tier2-review.js:696 derives inputPrint from context, priorFindings, round and other args, so the two arg sets (r1, and r2 with priorFindings) carry distinct prints. That makes two HEAD runs and four prints, and the text admits a record of one pair. AC1's per-run token counts still evidence the mask, so the effect is an incomplete record only. | sound |

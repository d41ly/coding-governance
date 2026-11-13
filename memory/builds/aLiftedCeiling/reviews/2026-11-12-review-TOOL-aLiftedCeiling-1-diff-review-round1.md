**Serves:** diff-review TOOL-aLiftedCeiling-1

# aLiftedCeiling: Tier-2 diff review of TOOL-aLiftedCeiling-1, round 1

*2026-11-12, on `branch/unattended-aliftedceiling`. This is an adversarial pass over the unit built on the owner's "Yes, raise it". Three finder lenses ran (`gov-diff-reviewer`), then two skeptic batches prompted to refute each finding (`gov-skeptic`), then one synthesis (`gov-synthesizer`). The diff raises the `instruction edits (manifest checks)` leg's ceiling in `tools/gate-legs.json` from 180 s to 420 s. It adds one `--observed` evidence row (110 s) to the generated `tools/run-gates/ceiling-evidence.txt` and re-stamps the kickoff manifest. Each pin below names the file's blob at the reviewed sha.*

Reviewed range: aa8f0800087a4d4cde9854bdbfb18a4932857726...cbfadf0720abd71a59bdad6a8f1587b1c3c80d72. ROUND: 1.

## Verdict: CLEAN WITH FIXES

One low item stands, and it has a fix the skeptic judged sound. The new evidence row's source text records no host load, and it names a different clone sha from the one the spec names.

No confirmed finding faults the ceiling itself. 420 s clears the row's bound of 110 + max(120, 110) = 230 s. It also clears the runner's 171.7 s reading the spec names, whose bound is 343.4 s.

This was a light review, not a full one. The security and intent lenses did not run.

## Review shape

Intensity light, raw 2, confirmed 1, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.50.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |

Adjudicated tally by item: 0 BLOCKER, 0 HIGH, 0 MEDIUM, 1 LOW, 1 item in all.

Adjudicated tally by raw confirmed finding: 0 blocker, 0 high, 0 medium, 1 low, 1 in all.

## Run integrity

- Lenses: 3/3 returned, 0 DIED.
- Skeptic batches: 2/2 returned, 0 DIED.
- Verdicts: 0 contradictory demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 1 judged sound, 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more, and none is here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intensity: light. The security and intent lenses were NOT run, so their classes were swept only through the checklist shares.
- Intent: 1 spec document supplied as `specs`, beside the range's commit messages.
- Checklist: 32 items, acquired by the harness from `--for-diff aa8f0800087a4d4cde9854bdbfb18a4932857726..HEAD`, split correctness 11, seams 11, verification 10.
- By design: the caller's byDesign.
- Shown: 1 refuted finding and 1 same-address pair.
- Dispositions: unclassed refuse; 32 class slugs handed; 171 leg names read from `tools/gate-legs.json`.

No lens or skeptic batch died and nothing was demoted, so the finding set is complete for a light review. It is not a full review.

## Items

### L1 (LOW): the new `--observed` row records no host load and names the wrong clone sha (id 1)

- **Where:** `tools/run-gates/ceiling-evidence.txt@628251fa:67`, the `instruction edits (manifest checks)` row.
- **What is wrong:** The row's source text reads `gov_tag.py check raced against instructions_edit.py check on a fresh index in a scratch clone of 33a1a8676, instructions_edit waiting on the tag-index write lock, 110s wall, TOOL-aLiftedCeiling-1 AC2`. Spec lines 129-131 require the `--how` text to say what else was running on the host, and to name a scratch clone of `123123146`. The row has no host-load clause, and it names `33a1a8676` instead.
- **Consequence:** The file header (lines 24-26) says an `--observed` reading is admitted uncensused, and its `--how` text is the only record of the load it was taken under. With no load recorded, a later `--reset` or ceiling review cannot tell an idle-host 110 s from a contended one. The sha mismatch also leaves the record disagreeing with the spec. No ceiling or gate result changes, so the effect is limited to the record.
- **Grade:** low, the binding grade.
- **Fix (judged SOUND by the skeptic):** In a scratch clone, re-run `derive-ceilings.py --write --observed 'instruction edits (manifest checks)=110' --how '<how>'`. The `<how>` text names the host load during the race, for example `no other gate run on the host`. It also names either the clone sha the spec names, or `33a1a8676` together with a spec amendment that records it. Then copy the generated file in.
- **Left-shift gate:** Make `derive-ceilings.py --observed` refuse a `--how` text that carries no load clause, and pin that refusal with an arm in the run-gates self-test. Until that lands, add the class `observed-how-text-omits-host-load` to the bug-class checklist.
- **Refuted finding at the same address, not a twin:** Refuted id 2 cites the same line. It argues that the 110 s row lets `--check` pass any ceiling from 230 s up, so the check cannot fail on the reason 420 was chosen. That is a claim about how strong the check is, not about what the row records. Fixing id 1 would leave id 2's claim unchanged, so the two are different defects and this report sets no twin flag. Id 2 stays refuted and is not counted.

review-shape kind=diff-review round=1 intensity=light at=synth raw=2 confirmed=1 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=0 low=1 agents=6 out-tokens=17694
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/run-gates/ceiling-evidence.txt:67 | low | low | confirmed | The finding holds. Line 67 of tools/run-gates/ceiling-evidence.txt has a source text that names the race, the 110 s wall and AC2. It says nothing about what else was running on the host. It also names a clone of 33a1a8676, while the spec's lines just after its step block ask for '123123146' and for 'what else was running on the host'. The file header (lines 24-26) says the --how text of an --observed reading is the only record of the load it was taken under, so leaving the load out loses information that nothing else keeps. This only affects the record. 420 clears 110+max(120,110)=230, and it also clears the runner's 171.7 s, so no ceiling or gate result changes. Low. | sound | - | new:observed-how-text-omits-host-load |
| 2 | verification | tools/run-gates/ceiling-evidence.txt:67 | low | - | refuted | The arithmetic holds. The margin file declares a 120 s floor and a 1.0 fraction, and tools/run-gates/derive-ceilings.py@9f57a263:663 and :683 require ceiling >= row + max(120, 1.0*row), so the 110.0 s row lets anything from 230 s up pass. That is still not a defect this diff introduced. At base the leg had no row and was UNBACKED, so nothing graded it; the diff adds a bound where there was none. The check certifies only what it says it does: that the ceiling clears the evidenced maximum by the margin. Spec section 6 (lines 187-189) says outright that the check 'does not see a contended bar's wall', and that covers the 352 s bar case. The finding's claim that the spec puts the check's floor at 344 s misreads section 4. Line 82-84 calls 344 s the floor only once 'the next plain --write on node a carries [the 171.7 s reading] into the evidence file', and line 133 says the same. The finder concedes this is a gap the spec accepted, with no wrong result today. Nothing on any path ships a wrong verdict; this is the deliberate limit of an evidence-margin check. | unsound | - | - |

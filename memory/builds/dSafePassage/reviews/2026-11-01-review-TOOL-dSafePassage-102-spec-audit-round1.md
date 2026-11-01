**Serves:** spec-audit TOOL-dSafePassage-102@rev-1

# Tier-2 review: TOOL-dSafePassage-102 spec audit, round 1

Provenance: a round-1 spec audit of TOOL-dSafePassage-102. That unit closes ask TOOL-dSafePassage-85 as the owner ruled it in chat on 2026-11-01 ("Raise the ceilings"). Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, the synthesis gov-synthesizer.

Reviewed: memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md@184fdf4d5b4f2e04e477d3eb66a3b76053d4a63c

ROUND: 1

## Verdict: CLEAN WITH FIXES

The review found no blocker and no high. There are 3 items: 2 medium and 1 low. Counted by raw confirmed finding, that is 4 medium and 1 low, because one medium item merges ids 1, 3 and 6. The spec can be built once the fixes below are in it.

## Review shape

Intensity full, raw 7, confirmed 5, refuted 2, unverified 0 (0 uncertain), precision 0.71.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |

Adjudicated tally:
- By item: 0 blocker, 0 high, 2 medium, 1 low.
- By raw confirmed finding: 0 blocker, 0 high, 4 medium, 1 low.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- Verdict handling: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 3 judged sound, 2 judged UNSOUND, 0 with no fix proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: no spec was supplied as intent. The caller's statement served as `context`.
- Checklist: 12 items, each assigned to exactly one of the 5 lenses (coherence 3, grounding 3, reuse 2, blast-radius 2, failure-envelope 2).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Every counter above is zero, so this run is complete.

## Items

### 1. [MEDIUM] AC3 does not check reason fields or comment lines in fork-ceilings.txt (ids 1, 3, 6)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md`, section 6 AC3 (its Red-when "... or a sixth row changes"), against section 2 S1 and S3 and section 6 AC1 and AC2.

**What is wrong:** S1 promises that each of the five rows keeps its reason text and gains one clause. S3 promises that no other row changes and no comment line changes. Section 2 says AC1 to AC3 observe those promises, but none of them checks these parts:
- AC3's first pipeline (`grep -E '^[-+][a-z]' | cut -c2- | cut -f1,2,4-6 | sort | uniq -u`) cuts away field 7, the reason. A sixth row whose only change is its reason gives identical `-` and `+` lines, and `uniq -u` drops both.
- The `[a-z]` lead skips every `#` line, the SHRINK-ONLY header (lines 12-14) included.
- AC3's second pipeline only counts added lines that carry the TOOL-dSafePassage-85 and -11 tokens.
- AC1 reads only fields 1, 3 and 4.
- fork-count.sh skips `#` lines (line 123) and reads the reason as an ignored remainder (line 147).

The skeptics reproduced this on scratch copies. One copy appended " EDITED" to unattended-status's reason. Another set it to "clobbered" and wiped every other reason down to the two ids. AC1 and AC3 stayed green both times.

**Consequence:** A build could do any of the following, and the ledger would still certify S1 and S3 as observed:
- delete the raised/lowered history from the reasons of the five rows of this shrink-only record;
- rewrite the reason of a sixth row;
- rewrite the SHRINK-ONLY header, which is the rule that governs the very ceilings this unit raises.

The counter never grades these fields, so the damage stays in the record's provenance. The evidence file is already covered, because AC6's word-diff catches these moves there.

**Fix:** The skeptic judged the finders' fixes for ids 1 and 6 UNSOUND, so this is the skeptics' corrected fix. The skeptic judged id 3's row-count fix sound, and it is included here.
- Drop the word-diff variant and use field-level checks.
- Join the old and new rows by id, the old file being `git show 4f7ba0a30:memory/project/fork-ceilings.txt`. For each of the five S1 rows, assert that the new field 7 equals the old field 7 followed by `; ` and the raise clause. Assert that every other non-comment row is byte-identical.
- Assert that `git diff 4f7ba0a30 -- memory/project/fork-ceilings.txt | grep -cE '^[-+]#'` prints 0.
- Assert that `git diff -U0 4f7ba0a30 -- memory/project/fork-ceilings.txt | grep -cE '^\+[a-z]'` prints 5, and that the same count for `^-[a-z]` prints 5.
- Assert that `git diff -U0 4f7ba0a30 -- memory/project/fork-ceilings.txt | grep -E '^[-+][a-z]' | cut -c2- | cut -f1 | sort -u` prints exactly the five S1 ids.
- Reword AC3's Red-when so that it names a sixth row's reason edit and a comment edit.
- Run staged breaks on a scratch copy, one that wipes a reason, one that edits unattended-status's reason, and one that edits a comment, and see each go red.

**Left-shift gate:** add a bug-class checklist entry: "an acceptance criterion that `cut`s fields out of a diff must name the fields it drops, and must cover every promise about those fields with another check". Where a spec-lint can do it, flag any AC Red-when clause that has no staged break which reds it.

### 2. [MEDIUM] The spec misstates run-gates-2leg's history and sets its ceiling from a single reading (id 2)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md`, section 4 "What it does not cover" (first bullet), "Alternatives rejected" (headroom bullet), and S1 row run-gates-2leg.

**What is wrong:** The spec says the run-gates-2leg row records a polled reading that varied before TOOL-aSparedSpawn-4. The row's own reason (fork-ceilings.txt line 18 at 4f7ba0a30) says more: the ceiling was "lowered to the measured 53 plus two, the margin that polled reading still needs". The spec leaves that out. Its "Alternatives rejected" bullet calls any value above the count "a number nobody measured", which ignores the file's own measured-plus-two precedent for this row. The record also shows the variance in practice: the last raise set the ceiling to a single reading of 57, and the bar now reads 58.

**Consequence:** Built as written, run-gates-2leg gets a ceiling of 58 from one reading. The record says this count can move by up to 2 between runs, so the spawn budget leg can flake red on the next bar or on CI with no code change. The spec's account of the row would also mislead the next person who raises it. The effect is limited to one leg.

**Fix:** The skeptic judged this fix SOUND. Correct the claim to what line 18 says. Then do one of two things:
- set run-gates-2leg to the measured count plus 2 (60, which is inside the margin of 3 and so not stale), following the file's precedent;
- or have the build re-measure each row three times with `--only` before editing, and record "measured N three times" as the file's other raised clauses do.

**Left-shift gate:** add a bug-class checklist entry: "a spec that cites a record's history quotes the record's own words for it, and a ceiling raise follows the row's recorded margin or explains why it departs from it".

### 3. [LOW] Files touched leaves out the status flip and the regenerated renders (id 5)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md`, section 4 "Files touched (estimate)".

**What is wrong:** The list names only fork-ceilings.txt, ceiling-evidence.txt and the ledger. Closing ask TOOL-dSafePassage-85 also requires these changes:
- the spec's own Status line goes from DEFERRED to CLOSED;
- `memory/builds/dSafePassage/README.md` (its roster row) and `memory/backlog/TOOL.md` (ask 85's row, line 497) must be regenerated, because both are rendered by gen_build_index.py.

The sibling build commit for TOOL-dSafePassage-101 (6d6fe589b) touched these same kinds of files.

**Consequence:** A builder who follows the list will not regenerate the renders. The memory hygiene leg then goes red on render drift, through check-memory-hygiene.sh line 1483. Nothing wrong ships, but the build costs one red bar and a second pass.

**Fix:** The skeptic judged this fix SOUND. Add these to "Files touched":
- the spec's Status flip from DEFERRED to CLOSED;
- `memory/builds/dSafePassage/README.md` and `memory/backlog/TOOL.md`, regenerated with `python tools/memory-tree/gen_build_index.py --write` (ask 85's row leaves TOOL.md once 102 is CLOSED);
- if the run loop owns it, RUN.md's `asks-at-landing` token `TOOL-dSafePassage-85=OPEN`.

**Left-shift gate:** add a bug-class checklist entry, or a spec-lint where it fits: "a spec whose header says it closes an ask lists, in Files touched, its own Status flip and the gen_build_index.py renders".

## Refuted

Ids 4 (reuse) and 7 (failure-envelope) were refuted. Their reasons are in the appendix.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=7 confirmed=5 refuted=2 unverified=0 blocker=0 high=0 medium=4 low=1 agents=10 out-tokens=78578

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 2 S1 and S3, against section 6 AC1, AC2 and AC3 | medium | medium | confirmed | I re-read spec AC3 at blob 184fdf4. Its first pipeline is `grep -E '^[-+][a-z]' \| cut -c2- \| cut -f1,2,4-6 \| sort \| uniq -u`. Header line 4 of fork-ceilings.txt at 4f7ba0a30 says the reason is field 7 and the ceiling is field 3. Neither is compared, so a sixth row whose reason is rewritten shows the same fields 1,2,4-6 on both sides, and uniq -u drops it. The `[a-z]` lead drops every `#` comment line, the SHRINK-ONLY header (lines 12-14) included. The second pipeline only counts tokens on added lines. fork-count.sh line 123 skips `#` lines, and line 147 reads the reason as the ignored remainder `_`. So neither AC1 nor AC2 sees a reason or a comment. S3's 'no comment line changes' is therefore unchecked for this file, and AC3's Red-when 'a sixth row changes' is false for a reason edit. The effect is contained: the counter never grades those fields. But the ledger would certify S1's 'keeps its text' and S3 without checking them. | unsound | - |
| 2 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 4 "What it does not cover" (first bullet) and "Alternatives rejected" (headroom bullet); S1 row run-gates-2leg | medium | medium | confirmed | At 4f7ba0a30, line 18 field 7 reads 'which is what made the polled reading vary before (TOOL-aSparedSpawn-10 S9); lowered to the measured 53 plus two, the margin that polled reading still needs ... raised 55 -> 57 ... measured 57'. Spec section 4 line 174 reports only that the reading 'varied before TOOL-aSparedSpawn-4'. It leaves out the record's statement that the reading still needs a +2 margin. The 'Alternatives rejected' bullet calls any value above the count 'a number nobody measured', which ignores the file's own measured-plus-two precedent for this row. The record also bears the variance out: the last raise set the ceiling equal to a single 57 reading, and the bar now reads 58. The spec does say that a reading one higher reds again. But its account of the row's history is incomplete, and setting the ceiling to one reading invites a repeat red. That effect is contained to one leg, so medium. | sound | - |
| 3 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 6 AC3 (Red when: '... or a sixth row changes'); section 2 S3 | medium | medium | confirmed | Reproduced the finding in scratch verify-b. fa.txt is `git show 4f7ba0a30:memory/project/fork-ceilings.txt`. fb.txt raises the five ceilings by 1, appends a clause naming TOOL-dSafePassage-85 and -11 to their reasons, and appends ' EDITED' to unattended-status's reason. On these files, AC3's first pipeline (`cut -f1,2,4-6 \| sort \| uniq -u \| wc -l`) printed 0. Its count pipeline printed 5. The first pipeline cuts field 7 away, so the sixth row's - and + lines become identical and uniq -u drops both. AC1 reads only fields 1, 3 and 4. So AC3's red-when 'or a sixth row changes' and S3's 'Observed by AC3' claim coverage the commands do not have. The effect stays inside a free-text field the counter never grades (fork-count.sh reads it as the row's remainder), so the defect is contained. | sound | - |
| 4 | reuse | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 4 "The five rows" (the clause form and "The build re-measures before it edits"), section 10 | medium | - | refuted | The premise is partly false on re-probe, and the risk is already stated in the spec. In `git show 4f7ba0a30:memory/project/fork-ceilings.txt`, row 18's most recent raise reads 'raised 55 -> 57 ... measured 57 on node a under bash 5.3', a single measurement with no 'three times'. So the file has no uniform rule of three measurements per raise. The spec's form claim is about how the clause is worded ('raised X -> Y by ..., measured Y ... on node a under bash 5.3'), and its clause has that shape. The spec also gets a second reading: the bar's reading plus the build's `--only` re-measure, which halts the build when the counts differ. The consequence the finding predicts, a ceiling with no headroom that reds again if a later reading is one higher, is stated in the spec's own section 4 'What it does not cover' (first bullet, which cites row 18's varying polled reading) and again in section 5 'risks'. The spec declares that consequence out of scope, so the cited section already says it. | sound | - |
| 5 | blast-radius | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 4 "Files touched (estimate)" | low | low | confirmed | At blob 184fdf4d, spec lines 193-197 list only fork-ceilings.txt, ceiling-evidence.txt and the ledger. The header (line 3) has Status DEFERRED and 'closes TOOL-dSafePassage-85'. At 4f7ba0a30, memory/backlog/TOOL.md:497 carries ask 85's row and memory/builds/dSafePassage/README.md:167 lists 85, and both are gen_build_index renders. check-memory-hygiene.sh:1483 runs gen_build_index.py as a drift check. `git show --stat 6d6fe589b` shows that the sibling 101 build commit touched TOOL.md, BACKLOG.md, README.md, RUN.md and its own spec. The sibling spec 101's Files touched also names README.md as a re-render, so 102 is less complete than its sibling. The list is labelled an estimate and the hygiene leg would catch the render drift, so the cost is one red bar and a second pass, with nothing wrong shipped. That is low. | sound | - |
| 6 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 6 AC3 (and S1, S3) | medium | medium | confirmed | AC3 (spec lines 255-265) cuts fields 1,2,4-6 in its first pipeline, so the reason (field 7) is never compared. Its second pipeline only counts added lines that contain the two ids. I re-ran the simulation under scratch verify-skeptic: old = `git show 4f7ba0a30:memory/project/fork-ceilings.txt`; new = the five ceilings raised, unattended-status's reason set to 'clobbered', and every other reason replaced with the two ids. AC1 printed exactly the seven expected lines, AC3a printed nothing, and AC3b counted every row it was given. So wiped histories and an edited sixth row both pass. AC3's own Red-when says 'or a sixth row changes', which it does not detect when only the reason moves, so the criterion certifies part of S1/S3 it does not check. The damage is limited to a text record's provenance, so medium. | unsound | - |
| 7 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-102.md:section 4 'The five rows', 'The build re-measures before it edits' | medium | - | refuted | Both halves fail on re-probe. (a) Count variance and zero headroom: the spec already names this risk. Spec blob 184fdf4 §4 'What it does not cover' (lines 173-175) says: 'Whether a raised ceiling holds on a later run. The run-gates-2leg row's own history records a polled reading that varied ... A ceiling set equal to its count has no headroom ... so a reading one higher reds again.' §5's risks line (220) repeats it. Setting each ceiling to its measured count is the owner's ruling, which is BY DESIGN, and 'Alternatives rejected' (line 207) explains why there is no headroom. The 'three times' convention the finding cites is also not uniform. fork-ceilings.txt row 18's last raise reads 'raised 55 -> 57 ... measured 57 on node a', a single sample. (b) A skipped or NOT MEASURED re-measure read as agreement: fork-count.sh lines 181-185 show that an --only selection whose one declared row is skipped prints REFUSING and returns 2, so no count appears to agree with. NOT MEASURED prints only under a bash other than 5.3, and the spec scopes that out (line 176-177; AC2 fixture is bash 5.3). Whatever the re-measure shows, AC2 requires '7 passed · 0 red · 0 skipped' and exit 0 at the build commit, so no number can land unverified. | unsound | - |

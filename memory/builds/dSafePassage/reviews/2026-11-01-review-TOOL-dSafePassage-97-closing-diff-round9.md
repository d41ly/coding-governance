**Serves:** diff-review TOOL-dSafePassage-96 TOOL-dSafePassage-97

# Closing diff review, round 9: dSafePassage, the round-8 fix unit TOOL-dSafePassage-97

2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 5 skeptic batches, then this synthesis). This round reviews the unit promoted from round 8 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md`). It does not review round 8's subject again.

**Reviewed range:** `cc668aa426d8b5ebd88275427d1ba327ca1bf16f...e3038fea654c3e89ab569b5d45038db2b48e1b3c`. **ROUND 9.**

## Verdict: CLEAN WITH FIXES

There are no blockers, no highs and no mediums. One item is LOW: 1 item, 1 raw confirmed finding (id 4). The defect is a wording overclaim in spec 97's S3, which AC3 does not observe. It has no effect on behaviour. 96's ledger is unchanged in the range.

Subjects reviewed:

- 97 writes no product code and nothing under `tools/`.
- Spec 97 carries a corrections table to 96's CLOSED text. It has one row per round-8 item, quotes 96's lines at `ab71837da` with the corrected reading, and pastes the `--legs-for` output for the leg count.
- 97's build output is its acceptance ledger.
- The records filed and re-rendered in the range: the round-8 review, 96's spec audit, 97's prompts, README.md, RUN.md, LIVE.md and the packet.

Review shape: intensity full, raw 5, confirmed 1, refuted 4, unverified 0 (0 uncertain), precision 0.20. Adjudicated tally: by item, 0 blocker, 0 high, 0 medium, 1 low. By raw confirmed finding, 0 blocker, 0 high, 0 medium, 1 low.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 0 | 2 | 0 | 0 | 0.00 |
| seams | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | - |

**Run integrity:** lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Fixes on confirmed findings: 0 judged sound, 1 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED. Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict. No lens notes were supplied, so every lens ran on the kit's generic brief. The run is complete.

Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Intent: no spec was supplied. `context` was the caller's statement, read beside the range's commit messages.

Checklist: none was swept, because it is absent. A zero count is not evidence that the project's recurring bug classes are absent.

By design: the caller's byDesign.

## LOW

### 1. S3 claims more than AC3 observes (id 4)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:33` (S3) and `:162` (AC3).

**What is wrong:** S3 says the build pass writes its acceptance ledger and nothing else, and that AC3 observes this. AC3 cannot fail on that claim. It reads only two things: 96's spec with the generated records block stripped, compared against the blob at `ab71837da`, and `git diff --numstat ab71837da -- tools`. Neither reads 96's acceptance ledger or any other path under `memory/`. A hand edit to 96's ledger, which §3 line 42 names as a non-goal, would still print `True` and nothing.

**Consequence:** the check certifies a wider claim than it reads. S3 as worded is already false. The build commit `e3038fea6` also writes 97's own spec (the Status flip and a records row), README.md and RUN.md, and 97's ledger itself says "beside the spec's status flip". AC3 passed anyway. The effect stays in the record. `git diff --quiet ab71837da e3038fea6 -- <96 ledger>` exits 0, and that ledger was last touched at `cc668aa42`, so nothing got through.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** narrow S3 to what AC3 reads: 96's authored text is unchanged from `ab71837da`, and no file under `tools/` moves. If the write-set probe is wanted too, run it against the build commit's own parent. `git diff --name-only e3038fea6^ e3038fea6` lists only 97's ledger, 97's spec, and the generated README.md and RUN.md. Keep `git diff --quiet ab71837da -- memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-96-ledger.md` exiting 0, and show it red with `744d2551`, where it exits 1 (measured). 97 is a records-only unit, so the narrowed reading goes in the next unit's corrections table, as 97 did for 96.

**Left-shift gate:** add a bug-class checklist entry: "a scope line that claims a write set (`writes X and nothing else`) is observed by a criterion that lists the build commit's own write set against its parent, never by a diff scoped to one directory". A `check-spec-tokens` warning could flag an S-line containing "nothing else" whose observing AC runs no `--name-only` diff.

## Refuted

Id 1 (correctness, spec 97 line 72) claimed AC4 reads green on the base tree. It does not. At `744d2551`, the second `check_floor_bash` run on the same mkdtemp raises `FileExistsError`, and two lines FAIL. So item 1's "a loud red, not a false green" holds for AC4 too.

Id 2 (correctness, spec 97 line 76) claimed a contradiction in the covers lists. `TEMPLATE-SPEC.md:282-284` lets a preservation criterion that re-observes the arm be a cover. 96's Measured rows at lines 115 and 116 both show the `finally` cut turning the arm red. Nothing stated is false.

Id 3 (seams, spec 97 line 140) claimed the risk line is false. It is true. The round-8 review, now listed in 96's records block, carries all five corrected readings. The one-way link matches the established pattern from 94 and 95, which byDesign covers.

Id 5 (verification, spec 97 line 161) claimed AC2 misses a dropped fragment. AC2 promises only the red it states: a row that cites a line not holding its quoted text. The figure 16 is DERIVED, which the template allows. Cutting a whole row is AC1's red. The finding asks for a stronger contract than the spec claims.

review-shape kind=diff-review round=9 intensity=full at=synth raw=5 confirmed=1 refuted=4 unverified=0 blocker=0 high=0 medium=0 low=1 agents=11 out-tokens=63123

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:72 | low | low | refuted | I checked the code, and AC4 does not read green on the base tree. AC4 runs AC1's command, which calls check_floor_bash(t) twice on the same mkdtemp. At 744d2551, build_staged_copy (selftest.py:3640-3649) calls shutil.copytree(HERE, dst) without dirs_exist_ok, and check_floor_bash has no rmtree of tmp / "dsp94-narrowed" before its build_staged_copy call (4494-4501), because S3 is missing there. So with the finally cut, the second run raises FileExistsError. That prints FAIL for '[dSP-95] the staged copy of upgrade_steps.py loads'. steps94 is then left as an empty ModuleType, so read_fallback_argv(steps94) returns AttributeError and the second '[dSP-94] ... reads the spawn's OSError' check also FAILs. Those two FAILs break AC4's pass condition, 'ok for every other line'. 96's own Measured row for 744d2551 with no break records the same second-run FAILs. The finder's evidence, the '744d2551 \| the finally cut \| both [dSP-95]' row, names the restore lines that the break turns red. It does not show the whole two-run output reading ok. AC4's 'preservation check' wording at 96's lines 198-199 is also limited to the two [dSP-95] lines. So a pre-cc668aa42 AC4 run reads red, and item 1's sentence at 97:72, 'a loud red, not a false green', holds for AC4 as well as for AC2 and AC3. | unsound | - |
| 2 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:76 | low | - | refuted | I found no contradiction. memory/TEMPLATE-SPEC.md:282-284 defines `covers` as the criteria of this spec that the arm re-observes. It does not require the criterion to stage the unit's new conjuncts red. A preservation criterion that re-observes the arm is a valid cover. At ab71837da, 96's Measured rows at lines 115 and 116 both show the `finally` cut turning both `[dSP-95]` checks red, at 744d2551 and over S1 to S3. So both of 97's statements at spec-97 line 76 are true: 'staged red by the `finally` cut (AC4)', and 'Both covers lists stand'. AC4's own text at 96 lines 195-199 gives its red condition as 'S1 or S2 drops the memo read' and calls it a preservation check. So it observes the arm, and it does so through the memo read that S1 and S2 must keep. That is compatible with 'covers', not two readings of one rule. The round-8 fix (review line 106) made the add-the-break edit primary and the drop branch conditional, and 97 applied the primary edit. Citing line 116 without line 115 leaves the justification incomplete, but it states nothing false. No checker reads it either: the covers join reads only the ids. Graded low and with no defect shown, it is refuted. | unsound | - |
| 3 | seams | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:140 | low | - | refuted | The risk line at spec 97:140-141 says what is true. 97 uses 'this round's review' for the round-8 review: commit 2ec06177f filed memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md in the same commit as spec 97, and §3 line 40 and AC3 line 166 describe that same re-render. At e3038fea6, 96's gen:spec-records block (spec 96 line 15) lists that round-8 review. At cc668aa42 the block had no such row, so this range added it. The risk line never says the route leads to 97. It says a reader of 96 is pointed to the review that names the defects, and that holds. The round-8 review carries all five items, each with its corrected wording as a skeptic-judged SOUND fix (for example lines 58 and 82). So a reader who starts at 96 does reach the corrected readings. That route never reaches 97's table, as the finder says, but the risk line makes no claim that it does. The finder also notes that 95 and 94 have the same one-way link, which shows this is the established pattern for corrections carried in a later unit (also covered by BY DESIGN: 'its corrections live in 97's section 4 table, as 95 did for 94'). The claimed false statement does not hold. | sound | - |
| 4 | verification | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:162 | low | low | confirmed | Confirmed against the spec. S3 at line 33 of 97's spec says the build pass writes its acceptance ledger and nothing else, and says AC3 observes it. AC3 (around line 162) does only two things: it compares 96's spec with the records block stripped against the blob at ab71837da, and it runs `git diff --numstat ab71837da -- tools`. Neither reads 96's ledger or anything else under memory/, so the line-42 non-goal (no edit of 96's ledger) and the 'nothing else' claim are never checked. `git show --stat e3038fea6` shows the build commit also writes 97's spec (3 lines), README.md and RUN.md, and 97's ledger itself says 'beside the spec's status flip'. So S3 as worded is already false and AC3 passed it anyway. The defect is new in this diff: 97's spec is new. The effect is contained. `git diff --quiet ab71837da e3038fea6 -- <96 ledger>` exits 0, and that ledger was last touched at cc668aa42, so nothing slipped through. That leaves a wording overclaim in a records-only spec with no effect on behaviour, so the grade is low. | unsound | - |
| 5 | verification | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-97.md:161 | low | - | refuted | I re-ran the probe. With item 1's `; line 196: 'kind of scratch repository'` removed from the spec text, the AC2 command prints `15 []`, so the mechanics are as the finder says. But AC2 does what it says it does. Its Red-when clause at spec-97 lines 158-160 promises one red only: 'a row cites a line that does not hold its quoted text'. Its figure note marks 16 as DERIVED, which TEMPLATE-SPEC.md:107-111 and :542 explicitly allow as a figure the observer re-derives. No criterion claims to detect a dropped fragment. Cutting a whole row is already AC1's red: lines 150-151 measure that cutting item 3 prints `[1, 2, 4, 5]`. So the finder's second probe, which gave `(13, [])`, is caught by AC1. What is left is a request for a stronger completeness contract than the spec states, not a check that certifies something it does not check. The table is correct as written: AC2 re-ran green, and the ledger's line 18 records `16 []`. This is a low with no consequence. Under the harness default for a medium or low the finder cannot establish as a defect, it is refuted. | sound | - |

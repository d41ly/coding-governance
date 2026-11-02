**Serves:** diff-review TOOL-dSafePassage-96

# Closing diff review, round 8: dSafePassage, the round-7 fix unit TOOL-dSafePassage-96

2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 5 skeptic batches, then this synthesis). This round reviews the unit promoted from round 7 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-closing-diff-round7.md`). It does not review round 7's subject again. 96's round-1 spec audit (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-96-spec-audit-round1.md`, 5 low items, all spec wording) ran beside the build, so its items are carried into this review and graded against the built code and records.

**Reviewed range:** `744d2551799b37a538cfe1868bd52ed39e3fdc4a...cc668aa426d8b5ebd88275427d1ba327ca1bf16f`. **ROUND 8.**

## Verdict: CLEAN WITH FIXES

There are no blockers, no highs and no mediums. Five items are LOW. They are the five carried spec-audit items, and all five still hold. None of them changes what any check does. The code edits are correct, and the probes confirmed them on the built tree. The defects are in the wording of spec 96 and in one comment in `selftest.py`. They share one cause. The build commit flipped spec 96 to CLOSED without folding in the audit. The spec blob at `cc668aa42` (`bb36ec4a`) differs from the audited blob `22ae0f75` only in its Status line and one records row. Spec 96 is CLOSED, so the fixes belong in an erratum or in the promoted unit, not in a silent edit to the spec.

Subjects reviewed:

- 96 makes three edits inside `check_floor_bash` in `tools/govkit/selftest.py` (5 lines added, 2 removed).
- The raise-path `[dSP-95]` check also requires `isinstance(cut94, OSError)`.
- The return-path `[dSP-95]` check also requires `argv94 == ["bash", "x"]`.
- `shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)` runs before `build_staged_copy`.
- The new spec 96, its ledger, its prompts, and the records re-rendered in the range.

Review shape: intensity full, raw 18, confirmed 16, refuted 2, unverified 0 (0 uncertain), precision 0.89. Adjudicated tally by item: 5 items, 0 blocker, 0 high, 0 medium, 5 low. By raw confirmed finding: 16 findings, 0 blocker, 0 high, 0 medium, 16 low (ids 2-10 and 12-18).

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |
| seams | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| verification | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |
| intent | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

### Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 15 judged sound, 1 judged UNSOUND (id 8, whose corrected fix is written in item 4), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intent: no spec was supplied to the fan. `context` was the caller's statement, read beside the range's commit messages.
- Checklist: none was swept, because none exists. A zero count is not evidence that the project's recurring bug classes are absent.
- By design: the caller's byDesign list.

Every lens and every skeptic batch returned, so the run's integrity counts are all zero.

**Shared left-shift gate:** all five items survived because nothing stops a spec flipping to CLOSED while its spec audit's confirmed items are unfolded. Gate the flip: refuse a Status change to CLOSED when the spec has a spec-audit record, the spec blob differs from the audited blob only in Status and records, and that audit has no fold or waiver row. Each item below also names a gate for its own class.

## LOW

### 1. AC2 to AC4 build their scratch from `git archive HEAD tools`, not from the built tree (ids 2, 14)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:177-178` (AC2). AC3 and AC4 inherit the wording through "the same kind of scratch repository". The ledger repeats it for the owed AC2 to AC4. This is carried audit item 1.

**What is wrong:** section 4 (lines 60-62) says the measurements ran on `git archive 744d2551 tools` with the fenced text applied. AC2 says `git archive HEAD tools`. The spec never says which tree the criteria read.

**Consequence:** wording only. Before `cc668aa42` was committed, HEAD under `tools/` matched `744d2551`. A check run then would have archived the unbuilt `selftest.py`, shown the base result, and read as a failed build. That failure is loud, not a false green. Now that `cc668aa42` is HEAD, the wording happens to name the built tree. The probe of AC3's break in a git-archive scratch of `cc668aa42` printed the expected FAILs (`cut94 ['bash', 'x']`).

**Fix (skeptic judged it SOUND):** reword AC2 to name the built tree: "a scratch repository made from the built tools directory (`git archive HEAD tools` once the build is committed, or `744d2551`'s archive with the working-tree `tools/govkit/selftest.py` copied over it)". AC3 and AC4 inherit it. Because spec 96 is CLOSED, put this in an erratum or the promoted unit.

**Left-shift gate:** a bug-class checklist entry: "an acceptance criterion that archives a tree names the commit or state it reads, never a bare HEAD the build has not yet moved". A `check-spec-tokens` warning could flag `git archive HEAD` inside a spec section headed for acceptance.

### 2. Section 7 records five legs where `--legs-for` names 17 (ids 3, 7, 12, 15)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:217-219`. This is carried audit item 2.

**What is wrong:** section 7 says "the five legs whose guard covers the selftest file" and calls the rest "95's, unchanged". `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` names 17 legs. Four are guarded by `tools/govkit/` (recall floor arms, govkit selftest, govkit refusal join, govkit acceptance matrix). Policy fixtures is guarded by the file itself. Twelve trip through the broad `tools/` guard, among them python resolver, push-main self-test, and lexicon naming predicates. The account also contradicts itself: lexicon naming predicates is on 96's own leg line (line 212) and is a broad-guard leg. Spec 95 recorded the 17/5/12 split. 96 dropped it.

**Consequence:** only the gate record is affected, because all 17 legs run on the bar. A closing reviewer who takes section 7 at its word would not expect the twelve broad-guard legs to move, and could dismiss a red in one of them as unrelated.

**Fix (skeptic judged it SOUND):** restore spec 95's wording in the record that carries 96's gate account. `--legs-for` names 17 legs. Five have a specific guard and are listed. Twelve, lexicon naming predicates among them, trip through the broad `tools/` guard and are expected unchanged.

**Left-shift gate:** have `check-spec-tokens` compare a spec's section 7 leg count against `--legs-for` over the files the spec's slices touch, and fail when the stated count differs from the query's count.

### 3. The S3 comment claims a rerun safety the suite does not have (ids 6, 10, 16)

**Where:** `tools/govkit/selftest.py:4494`, the comment `# TOOL-dSafePassage-96: a reused tmp stages afresh`, added in this range. The spec title (line 1), section 4 S3 (lines 85-99) and the build commit subject make the same claim. This is carried audit item 3.

**What is wrong:** only a direct `check_floor_bash(tmp)` call is rerun-safe. AC1's twice-run of two direct calls on one tmp printed `[]` both times. `check_floor_bash` has one caller, `check_step_isolation` (defined at `:3684`, calling at `:4427`). That caller runs `quiet_target.mkdir(parents=True)` with no `exist_ok` at `:4404`, before the call, and makes its other `build_staged_copy` calls the same way. So the suite raises `FileExistsError` on a reused tmp before `check_floor_bash` is reached. The caller's byDesign note names this limit, but no record in the repo states it. The finding is about that missing wording, not a missing twice-run arm.

**Consequence:** no change in behaviour, because the bar uses a fresh `TemporaryDirectory`. The comment and the spec claim more than the suite provides, and the next change could rely on a suite-level rerun safety that nothing provides and no gate checks.

**Fix (skeptic judged it SOUND):** narrow the comment to `# TOOL-dSafePassage-96: a direct check_floor_bash call on a reused tmp stages afresh`. Add the audit's sentence to the record that carries 96's wording now that the spec is CLOSED (the promoted unit, or an erratum): S3 covers only a direct `check_floor_bash(tmp)` call, `check_step_isolation` and its other `build_staged_copy` calls stay single-use per tmp, and the bar's fresh `TemporaryDirectory` is what keeps them safe.

**Left-shift gate:** a bug-class checklist entry: "a comment or spec line that claims rerun or reuse safety names its scope (the function, or the suite) and the caller that bounds it".

### 4. The Measured row names its break "S4's replacement of 95", and spec 96 has no S4 (ids 4, 8, 13, 17)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:113`, the Measured row. This is carried audit item 4.

**What is wrong:** the row reads "S4's replacement of 95 given back `except OSError:`". Spec 96 defines only S1 and S2 (heading at line 64) and S3 (heading at line 85). The S4 meant is spec 95's "### S4: the copy staged by build_staged_copy" (spec-95:170). The same break has two other names: "the narrowed copy's replacement text" in AC3 (line 187), and "the `except OSError:` replacement" on the arm line at line 214.

**Consequence:** cosmetic. A reader has to work out that this is TOOL-dSafePassage-95's S4 before matching the row to AC3. The probe confirmed AC3's row on the built tree. With that break staged on `cc668aa42`, the second `[dSP-94]` check and the raise-path `[dSP-95]` check printed FAIL, the latter naming `cut94 ['bash', 'x']`. The return-path `[dSP-95]` check printed ok.

**Fix (the skeptics judged it SOUND for ids 4, 13 and 17 and REJECTED it for id 8; this is the corrected fix):** use one spelling for the break at all three sites (lines 113, 187 and 214). Write either "TOOL-dSafePassage-95 S4" in full or "the narrowed copy's replacement (the `src94.replace(anchor94, ...)` line) given back `except OSError:`". Id 8's skeptic rejected a bare `selftest.py:4497` cite. The spec's measurements ran on base `744d2551`, where that line is `:4496`. In the built tree it is `:4497`, because the S3 `rmtree` line was inserted above it. So any line cite must name its tree, `:4496` at `744d2551` or `:4497` at `cc668aa42`. Naming the `src94.replace` line instead avoids the drift.

**Left-shift gate:** have `check-spec-tokens` fail when a spec cites an S-id (`S<n>`) that the spec does not define as a heading, unless the cite carries a unit id (`TOOL-dSafePassage-95 S4`).

### 5. Both New arm lines list AC4 but do not name AC4's break (ids 5, 9, 18)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:214-215`. This is carried audit item 5.

**What is wrong:** line 214 says "covers AC2 AC3 AC4" and is staged red by the `except OSError:` replacement and the `steps._BASH = None` cut. Line 215 says "covers AC2 AC4" and is staged red by the `steps._BASH = None` cut only. AC4 (lines 195-200) stages a different break: the `finally` and its restore line cut from `read_fallback_argv`. The Measured row at line 116 ("S1 to S3 | the finally cut") shows that break turning both `[dSP-95]` checks red. So the arms do cover AC4, but neither arm line names the break.

**Consequence:** the arm declaration and the acceptance criteria disagree. The ledger still owes AC2 to AC4 at the close as the RED-first observations of these arm lines, and a closer checking which break turns each arm red for AC4 finds none listed. Check behaviour is unaffected. `check-spec-tokens`' covers join (`tools/check-spec-tokens.py:1339-1360`) reads only the ids in the covers field and treats the staging column as prose. The checks at `selftest.py:4516-4521` are unaffected.

**Fix (skeptic judged it SOUND):** add "and by the `finally` cut (AC4)" to the staging column of both New arm lines. If AC4 is only a preservation check, drop AC4 from their covers lists and call it that.

**Left-shift gate:** extend the covers join in `tools/check-spec-tokens.py` so that each AC id in an arm line's covers field must match a break the AC names, and that break must appear in the arm line's staging column. Where a parse is too loose for a gate, add a checklist entry: "every AC an arm covers names the break that turns the arm red".

## Refuted

Id 1 (correctness, `tools/govkit/selftest.py:4494`) raised the same rerun-scope limit as item 3. The skeptic refuted it as a defect claim. The caller's byDesign names the limit as known and tracked: S3's rerun safety covers a direct `check_floor_bash` call, and a twice-run through the selftest is out of scope. The comment is also literally true for the line it annotates. The wording gap that remains is item 3, confirmed through ids 6, 10 and 16.

Id 11 (verification, spec line 214) duplicates id 9: the same carried audit item 5, the same lines and the same fix. The defect is real and is item 5. This copy adds no separate defect.

review-shape kind=diff-review round=8 intensity=full at=synth raw=18 confirmed=16 refuted=2 unverified=0 blocker=0 high=0 medium=0 low=16 agents=11 out-tokens=55468

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/govkit/selftest.py:4494 | low | - | refuted | The facts are right. check_floor_bash has one caller, check_step_isolation (selftest.py:4427), and that caller runs quiet_target.mkdir(parents=True) at :4404 with no exist_ok, then about twenty build_staged_copy calls, so the whole suite is single-use per tmp. But this round's BY DESIGN names exactly this limit as known and tracked: 'S3's rerun safety covers a direct check_floor_bash call', and a twice-run of check_floor_bash through the selftest is out of scope. The comment at :4494 is also literally true for the line it annotates: it removes tmp/dsp94-narrowed, so that one staging step works on a reused tmp. Spec section 3 already lists the twice-run as a non-goal, and section 4 says the bar's one call uses a fresh TemporaryDirectory. The by-design limit covers the finding, so I refute it. | sound | - |
| 2 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:178 | low | low | confirmed | I checked this myself. `git rev-parse cc668aa42:<spec>` gives bb36ec4a. `git diff 22ae0f75 bb36ec4a` shows only two changes: the Status line (DEFERRED to CLOSED) and one records row. So audit item 1 was never folded in. AC2 at line 178 still says 'git archive HEAD tools', while section 4 at line 60 says the measurements used 'git archive 744d2551 tools' with the fenced text applied. The ledger at line 19 repeats the HEAD wording for the owed AC2 to AC4. Before cc668aa42 was committed, HEAD under tools matched 744d2551, so a check run then would have shown the base result. The failure would be loud, not a false green. Now that the build is committed, the wording happens to name the built tree, so the damage is small. It is a wording defect in a record this range added. | sound | - |
| 3 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:217 | low | low | confirmed | Line 217 of the spec still reads 'the five legs whose guard covers the selftest file'. I ran `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` and it named 17 legs: four guarded by tools/govkit/, policy fixtures guarded by the file itself, and twelve marked broad through tools/, lexicon naming predicates among them. Section 7 leaves out the twelve, but its own leg line includes lexicon. The spec at bb36ec4a is unchanged from the audited blob apart from Status and records. This only affects how the gates are recorded, because all legs run on the bar. | sound | - |
| 4 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:113 | low | low | confirmed | Line 113 at bb36ec4a still says "S4's replacement of 95 given back `except OSError:`". Section 2 of spec 96 defines only S1 to S3 (lines 29-38), so the S4 meant is TOOL-dSafePassage-95's. AC3 calls the same break 'the narrowed copy's replacement text', and section 7 calls it 'the `except OSError:` replacement'. This is cosmetic. The proposed fix cites selftest.py:4497. In the built code that is the src94.replace(anchor94, ...) line: 4494 is the rmtree, 4495 the try, 4496 spec94. So the cite is correct. | sound | - |
| 5 | correctness | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:214 | low | low | confirmed | The spec file is new in this range, so the defect is in scope. At cc668aa42, spec-96 line 214 says 'covers AC2 AC3 AC4' and its staging column names only the `except OSError:` replacement and the `steps._BASH = None` cut. Line 215 says 'covers AC2 AC4' and names only the `steps._BASH = None` cut. AC4 (lines 195-200) stages a different break, the `finally` cut, and the Measured row at line 116 shows that break turning both arms red. The audit's item 5 was not folded in, so it still holds. It affects only the declaration: check-spec-tokens' covers join (tools/check-spec-tokens.py:1339-1360) reads only the ids in the covers field and treats the staging column as prose. Behaviour is unaffected. | sound | - |
| 6 | seams | tools/govkit/selftest.py:4494 | low | low | confirmed | selftest.py:4494 carries the comment 'a reused tmp stages afresh'. check_floor_bash has one caller, check_step_isolation (selftest.py:3684, which makes the call at :4427). Before that call, check_step_isolation runs `quiet_target.mkdir(parents=True)` at :4404 with no exist_ok, so a reused tmp raises before check_floor_bash is reached. Spec-96 S3 (lines 35-38 and 85-99) and its title still say only that the bar is unaffected and never state the direct-call limit. The audit's item 3 was not folded in before the CLOSED flip. The harness's BY DESIGN note names the limit, but no record in the repo states it, and that gap is what this finding is about. It is wording only: the bar uses a fresh TemporaryDirectory. | sound | - |
| 7 | seams | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:217 | low | low | confirmed | I re-ran `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py`. It printed 17 legs: four guarded by tools/govkit/, policy fixtures guarded by the file itself, and twelve marked 'broad' through tools/, lexicon naming predicates among them. Spec-96 section 7 (lines 217-219) speaks only of 'the five legs whose guard covers the selftest file' and calls the rest '95's, unchanged'. Yet lexicon naming predicates is on 96's own leg line (line 212) and is one of the broad-guard legs. The account is incomplete and contradicts itself. Only the gate record is affected, because all 17 legs run on the bar. | sound | - |
| 8 | seams | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:113 | low | low | confirmed | Spec-96 line 113's Measured row names its break 'S4's replacement of 95 given back except OSError:'. Spec-96 defines only S1 to S3 (section 2, lines 29-38). The same break is called 'the narrowed copy's replacement text' in AC3 (line 187) and 'the except OSError: replacement' at line 214. The S4 meant is TOOL-dSafePassage-95's. The finding is cosmetic and true. | unsound | - |
| 9 | seams | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:214 | low | low | confirmed | At HEAD (cc668aa42), spec 96 line 214 reads `covers AC2 AC3 AC4 ... staged red by the except OSError: replacement and by the steps._BASH = None cut`, and line 215 reads `covers AC2 AC4 ... staged red by the steps._BASH = None cut`. AC4 (section 6) stages a different break: the finally and its restore line cut from read_fallback_argv. The Measured row 'S1 to S3 \| the finally cut' shows that break turns both [dSP-95] checks red, but neither arm line names it. Spec 96 is new in this range, so the defect is in scope, and the carried audit item 5 was not folded in: the build edited only selftest.py. The ledger still owes AC2 to AC4 as the RED-first observations of these arm lines. Low: it is a declaration mismatch with no effect on any check. | sound | - |
| 10 | verification | tools/govkit/selftest.py:4494 | low | low | confirmed | selftest.py:4494, added in this range, carries the comment `# TOOL-dSafePassage-96: a reused tmp stages afresh`. The function's only call is at :4427, from check_step_isolation, and :4404 runs `quiet_target.mkdir(parents=True)` with no exist_ok. So when the suite runs on a reused tmp it raises before check_floor_bash is ever reached. The claim holds only for a direct check_floor_bash(tmp) call, which is what AC1 runs. Spec 96 section 4 S3 says only that the bar is unaffected because it uses a fresh TemporaryDirectory, and never limits the claim to a direct call. Audit item 3 was not folded in. The BY DESIGN note about a selftest twice-run excludes a gate, not this scope wording. Low: comment and spec wording only. | sound | - |
| 11 | verification | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:214 | low | - | refuted | This is a duplicate of id 9: the same carried audit item 5, the same spec lines 214-215, the same missing finally-cut break for AC4, and the same fix. The defect itself is real, and id 9 confirms it. This copy adds no separate defect. | sound | - |
| 12 | verification | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:217 | low | low | confirmed | I ran `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py`, a query mode and not a gate. It printed 17 legs: recall floor arms, govkit selftest, govkit refusal join and govkit acceptance matrix, guarded by tools/govkit/; policy fixtures, guarded by the file itself; and twelve marked `<- tools/ ... broad`, lexicon naming predicates among them. Spec 96 line 217 says 'The leg line names the five legs whose guard covers the selftest file', but the broad tools/ guard covers that file too, and the spec never names those twelve. This paragraph is new in this range. Audit item 2 was not folded in. Low: it affects only the gate record, and every leg still runs on the bar. | sound | - |
| 13 | verification | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:113 | low | low | confirmed | Line 113 of spec 96 at cc668aa42 reads "S4's replacement of 95 given back `except OSError:`". Spec 96 has only S1 and S2 (line 64) and S3 (line 85). The S4 it means is in spec 95 ("### S4: the copy staged by build_staged_copy", spec-95:170). AC3 (line 187) calls the same break "the narrowed copy's replacement text" and section 7 (line 214) calls it "the `except OSError:` replacement". Spec 96 first appears in this range, and the build commit changed only its Status line and records table, so audit item 4 was never folded in. The effect is cosmetic. | sound | - |
| 14 | intent | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:177 | low | low | confirmed | AC2 (line 177-178) still builds its scratch with `git archive HEAD tools`, and AC3 and AC4 inherit it through "the same kind of scratch repository". Section 4 (lines 60-62) says the measurements ran on `git archive 744d2551 tools` with the fenced text applied. `git diff d07da781e cc668aa42` on the spec shows only the Status and records-table edits, so audit item 1 was not folded in. HEAD now holds the built selftest.py, so this is wording only. | sound | - |
| 15 | intent | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:216 | low | low | confirmed | Section 7 (line 217, the finder cited 216) says "the five legs whose guard covers the selftest file". I ran `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` and it printed 17 legs: four guarded by tools/govkit/, policy fixtures guarded by the file itself, and twelve marked `<- tools/ ... broad`, among them lexicon naming predicates, which is on the leg line. Section 7 is unchanged from audited blob 22ae0f75 (the build diff on the spec does not touch it). Only the gate record is affected. | sound | - |
| 16 | intent | tools/govkit/selftest.py:4494 | low | low | confirmed | selftest.py:4494 (added in cc668aa42) has the comment "TOOL-dSafePassage-96: a reused tmp stages afresh", and the spec title on line 1 says the same. Grep finds one caller of check_floor_bash, at :4427 inside check_step_isolation. That function runs `quiet_target.mkdir(parents=True)` with no exist_ok at :4404, so a reused tmp raises before the call is reached. Only a direct check_floor_bash call is rerun-safe. Spec section 4 S3 (lines 98-99) says only that the bar is unaffected and never states this limit. The BY DESIGN note about S3 covering a direct call is not written in the spec or the comment. The finding asks for wording, not a twice-run arm. Behaviour does not change. | sound | - |
| 17 | intent | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:112 | low | low | confirmed | The spec file is new in this range: git show 744d2551 reports it is not in that tree. The Measured table row (line 113, one line below the cited 112) reads "S4's replacement of 95 given back `except OSError:`". The only S-items the spec defines are the headings at line 64 (S1 and S2) and line 85 (S3), and grep finds no other S4 in the file. AC3 at line 187 calls the same break "the narrowed copy's replacement text", and the arm line at 214 calls it "the `except OSError:` replacement". So one break has three names and one of them points nowhere in this spec. It is cosmetic: no check changes. | sound | - |
| 18 | intent | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:213 | low | low | confirmed | In the spec, which is new in this range, the two New arm lines sit at 214 and 215, not 213. Line 214 says covers AC2 AC3 AC4 and is staged red by the `except OSError:` replacement and the `steps._BASH = None` cut. Line 215 says covers AC2 AC4 and is staged red by the `steps._BASH = None` cut only. AC4 (around line 195) stages a different break: the `finally` and its restore line cut from read_fallback_argv. Neither arm line names that break. The Measured row for the `finally` cut on S1 to S3 shows both [dSP-95] checks reading FAIL, so the arms do cover AC4; only the declaration leaves the break out. The selftest.py checks at 4516-4521 are unaffected, so the effect is on wording only. | sound | - |

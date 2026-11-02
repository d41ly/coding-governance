**Serves:** spec-audit TOOL-dSafePassage-96@rev-1

# Tier-2 review: round-1 spec audit of TOOL-dSafePassage-96

This audit was promoted from the round-7 closing diff review (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-closing-diff-round7.md`). Spec 96 makes three edits inside `check_floor_bash` in `tools/govkit/selftest.py`:

- The raise-path [dSP-95] check also requires `isinstance(cut94, OSError)`.
- The return-path [dSP-95] check also requires `argv94 == ["bash", "x"]`.
- One `shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)` line before `build_staged_copy` makes a reused tmp safe.

Reviewed: memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md@22ae0f75ccc1b55bcd53e208d57b659fdcac7ff2
ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers, no highs and no mediums. Five items are LOW, covering six raw confirmed findings, because findings 3 and 6 describe one defect. All six are wording or declaration defects in the spec, and none changes what the build does. The build can go ahead once the five wording fixes are folded into the spec.

Review shape: intensity full, raw 6, confirmed 6, refuted 0, unverified 0 (0 uncertain), precision 1.00. Adjudicated tally by item: 0 blocker, 0 high, 0 medium, 5 low. By raw confirmed finding: 0 blocker, 0 high, 0 medium, 6 low.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 0 | 0 | 0 | 0 | 0 | - |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 3/3 returned, 0 died.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Discards: 0 spurious verdicts were discarded and 0 duplicates were found.
- Fixes on confirmed findings: 6 judged sound, 0 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches were gov-skeptic, and synthesis was gov-synthesizer.
- Intent: no spec was supplied as intent. The `context` was the caller's statement.
- By design: the caller's byDesign.
- Move check: no checked subject moved.
- Checklist: none was swept, because there is none. The zero count is not evidence that the project's recurring bug classes are absent.

Every count is zero, so the run is complete.

## Items

### 1. LOW: AC2 to AC4 build their scratch from `git archive HEAD`, which is the unbuilt tree until the build commits (ids 3, 6)

- **Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md`, section 6 AC2 (line 176). AC3 and AC4 inherit it through "the same kind of scratch repository".
- **What is wrong:** AC2 builds its scratch repository with `git archive HEAD tools`. Section 4 (lines 57-60) says the measurements ran on `git archive 744d2551 tools` with the fenced text applied to the working tree. The spec never says the archive must be taken after the build commit. Under `tools`, HEAD (d07da781e, the spec commit) is byte-identical to 744d2551: `git diff --stat 744d2551 HEAD -- tools` prints nothing. HEAD's `selftest.py:4516-4518` still holds the memo-only [dSP-95] checks.
- **Consequence:** A builder who checks AC2 to AC4 before committing is following verify-before-done, but archives the unbuilt `selftest.py`. Under the `steps._BASH = None` cut, AC2 shows both [dSP-95] lines `ok`, which is the base result. AC3 shows the raise-path [dSP-95] line `ok`. That reads as a build failure on a correct build, or the builder ends up running the criteria only after committing. The failure is loud, not a false green, and the measured rows let a careful builder tell which tree ran.
- **Fix (judged SOUND by the skeptic):** Name the build's working tree as the source of the scratch, not HEAD. For example: "a scratch repository made from the build's working-tree tools directory (`git archive HEAD tools` once the build is committed, or 744d2551's archive with the working-tree `tools/govkit/selftest.py` copied over it)". AC3 and AC4 inherit the same wording.
- **Left-shift gate:** add a spec-tokens check that flags `git archive HEAD` inside an acceptance criterion unless the criterion names the post-commit tree. Failing that, add a checklist entry: "an AC's scratch names the built tree, not HEAD".

### 2. LOW: section 7 records five covering legs, but the guard query names 17 (id 4)

- **Where:** section 7, the paragraph under the New arm lines (lines 215-217).
- **What is wrong:** The paragraph speaks of "the five legs whose guard covers the selftest file". `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` names 17 legs:
  - four guarded by `tools/govkit/`;
  - policy fixtures, guarded by the file itself;
  - twelve that trip through the broad `tools/` guard.

  Section 7 neither names the twelve nor says they run. One of them, `lexicon naming predicates`, is on the leg line anyway, where section 7 counts it among "95's". The account contradicts itself. Spec 95's section 7 (lines 355-359) stated the 17/5/12 split correctly, and spec 96 dropped it.
- **Consequence:** The effect is limited to how the gates are recorded. All 17 legs still run on the bar. A builder or closing reviewer who takes section 7 at its word would not expect the other legs to trip, so a red in one would read as unrelated. Those legs are run-gates canary, foreign-prefix parity, push-main self-test, check-wiring self-test, settings-merge selftest, install-prefix self-test, dead-path carriers self-test, spec-tokens self-test, kit-placeholders self-test, run-gates evidence and python resolver.
- **Fix (judged SOUND by the skeptic):** Restore 95's wording. For example: "`python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` names 17 legs. The leg line names the five whose guard is specific (the four guarded by tools/govkit/, and policy fixtures, guarded by the file itself) plus the unguarded legs 95 named. The other twelve, among them lexicon naming predicates, trip through the broad tools/ guard and are expected unchanged."
- **Left-shift gate:** have check-spec-tokens compare any leg count stated in a spec's section 7 with the `--legs-for` output for the files the spec touches, and fail when they differ.

### 3. LOW: S3's rerun safety holds only for a direct `check_floor_bash` call, and the spec does not say so (id 5)

- **Where:** section 2 S3, and section 4 "S3: the staging directory removed first". The spec title and the S3 code comment are affected too.
- **What is wrong:** S3 makes one staging call in `check_floor_bash` safe on a reused tmp. `check_floor_bash` has exactly one caller, `check_step_isolation` (`selftest.py:4427`). On a reused tmp, that caller raises `FileExistsError` long before it reaches `check_floor_bash`:
  - first at `quiet_target.mkdir(parents=True)` (`:4403-4404`), which has no `exist_ok`;
  - then at its roughly twenty other `build_staged_copy` calls.

  The title and the code comment say "a reused tmp stages afresh". Section 4 says only that the bar is unaffected because it uses a fresh TemporaryDirectory. Nothing states that the safety holds only for a direct call such as AC1's.
- **Consequence:** The effect is on wording only, and behaviour does not change, because the bar uses a fresh TemporaryDirectory. But the next change could rely on a rerun safety the suite does not have. This finding does not ask for a twice-run selftest gate, so the BY DESIGN exclusion does not cover it.
- **Fix (judged SOUND by the skeptic):** Add one sentence to section 4 S3, or a non-goal to section 3, saying three things:
  - S3 makes only a direct `check_floor_bash(tmp)` call rerun-safe.
  - `check_step_isolation` and its other `build_staged_copy` calls stay single-use per tmp.
  - The bar's fresh TemporaryDirectory is what keeps them safe.

  Word the code comment to match, for example "a direct rerun on one tmp stages afresh".
- **Left-shift gate:** add a checklist entry: "a rerun-safety or idempotence claim names the entry point it holds for, and every caller of the guarded function is checked against it".

### 4. LOW: one staged break is spelled three ways, one of them a dangling "S4" (id 1)

- **Where:** section 4 Measured, rows 5-6 (line 111, "S4's replacement of 95 given back except OSError:").
- **What is wrong:** Spec 96 defines only S1 to S3 (section 2, lines 27-36). The S4 meant is TOOL-dSafePassage-95's S4, defined at `spec-TOOL-dSafePassage-95.md:47`. The same break is spelled three ways:
  - "S4's replacement of 95" in section 4 (line 111);
  - "the narrowed copy's replacement text" in AC3 (line 185);
  - "the except OSError: replacement" in section 7 (line 212).
- **Consequence:** The defect is cosmetic, and behaviour does not change. A builder who reads "S4" in 96 finds no such item and has to work out that it is 95's S4 before matching the row to AC3.
- **Fix (judged SOUND by the skeptic):** Rename the row's break "the narrowed copy's replacement (selftest.py:4496) given back except OSError:" to match AC3's wording, or write "TOOL-dSafePassage-95 S4" out in full.
- **Left-shift gate:** have check-spec-tokens fail on a bare `S<n>` reference that has no matching S-item in the same spec's section 2.

### 5. LOW: both New arm lines claim AC4 but do not name AC4's break (id 2)

- **Where:** section 7 Gates, both New arm lines (lines 212-213).
- **What is wrong:** The arm lines say:
  - line 212: `covers AC2 AC3 AC4`, with a staging column that names only the `except OSError:` replacement and the `steps._BASH = None` cut;
  - line 213: `covers AC2 AC4`, with a staging column that names only the `steps._BASH = None` cut.

  AC4 (line 193) stages a different break, the cut of the `finally` from `read_fallback_argv`. The Measured row at line 114 shows that this break turns both [dSP-95] checks red. So the arms do cover AC4, but neither line lists the break that does it.
- **Consequence:** The arm declaration and the acceptance do not match. A reader who checks which staged break turns each arm red for AC4 finds none listed. The check's behaviour is unaffected, and AC4 itself names its break.
- **Fix (judged SOUND by the skeptic):** Add "and by the `finally` cut (AC4)" to the staging column of both New arm lines. Alternatively, drop AC4 from their covers lists if AC4 is meant only as a preservation check.
- **Left-shift gate:** have check-spec-tokens check that every AC an arm line covers names a break which appears in that arm line's staging column.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=6 confirmed=6 refuted=0 unverified=0 blocker=0 high=0 medium=0 low=6 agents=9 out-tokens=48011

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 4 Measured, rows 5-6 ("S4's replacement of 95 given back except OSError:") | low | low | confirmed | I read the pinned blob 22ae0f75. Line 111 says `S4's replacement of 95 given back except OSError:`. The only S4 in 96 is that one line. Section 2 defines S1-S3 only (lines 27-36). The S4 meant is TOOL-dSafePassage-95's, defined at spec-TOOL-dSafePassage-95.md:47. AC3 (line 185) names the same break 'the narrowed copy's replacement text', and section 7 line 212 calls it 'the except OSError: replacement'. So one break has three spellings. This is cosmetic. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 7 Gates, both New arm lines | low | low | confirmed | Line 212 says `covers AC2 AC3 AC4` and its staging column names only the except OSError: replacement and the steps._BASH = None cut. Line 213 says `covers AC2 AC4` and its staging column names only the steps._BASH = None cut. AC4 (line 193) uses a different break: the finally cut from read_fallback_argv. The Measured row at line 114 shows that break turns both [dSP-95] checks red. So both arms do cover AC4, but neither New arm line lists the break that does it. The mismatch is only in the declaration; AC4 names its own break, so behaviour is unaffected. | sound | - |
| 3 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 6 AC2 (inherited by AC3 and AC4, 'the same kind of scratch repository') | low | low | confirmed | I read the spec blob 22ae0f75. Lines 57-60 say the measurements ran on `git archive 744d2551 tools` with the fenced text applied to the working tree. AC2 (line 176) builds its scratch with `git archive HEAD tools`, and AC3 and AC4 inherit that through 'the same kind of scratch repository'. Nothing in the spec says the archive must be taken after the build commit. `git diff --stat 744d2551 HEAD -- tools` printed nothing, so HEAD today is the base under tools, and a run before the commit would test the unbuilt tree. Nothing ships wrong, because the measured rows tell the two trees apart and a careful builder would notice, so this is low. | sound | - |
| 4 | blast-radius | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 7, the paragraph under the New arm lines | low | low | confirmed | `python tools/check-spec-tokens.py --legs-for tools/govkit/selftest.py` printed 17 legs. Four are guarded by tools/govkit/, policy fixtures is guarded by the file itself, and twelve are marked `<- tools/ ... broad`, lexicon naming predicates among them. Spec-96 section 7 (lines 215-217) talks about 'the five legs whose guard covers the selftest file' and says nothing about the twelve broad-guard legs that also trip. 95's section 7 (lines 355-359 at HEAD) gave the 17/5/12 split, and 96 dropped it. The legs still run on the bar, so the only effect is on how the gates are recorded: low. | sound | - |
| 5 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 2 S3 and section 4 'S3: the staging directory removed first' | low | low | confirmed | Confirmed by reading the code. check_floor_bash has exactly one caller, check_step_isolation (selftest.py:4427). That caller runs `quiet_target = tmp / "dsp69-target"; quiet_target.mkdir(parents=True)` at :4403-4404 with no exist_ok, so a reused tmp fails there before it ever reaches check_floor_bash. The spec's title says 'a reused tmp stages afresh', and the S3 code comment uses the same words. Section 4 S3 says only that 'The bar is unaffected either way' because of the fresh TemporaryDirectory (:5523). Nowhere does it say that rerun safety holds only for a direct check_floor_bash call. The BY DESIGN item excludes a twice-run selftest gate, which this finding does not ask for, and no non-goal covers the scope statement. The effect is wording only and does not change behaviour, so low. | sound | - |
| 6 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-96.md:section 6 AC2 (and AC3 and AC4 by 'the same kind of scratch repository') | low | low | confirmed | Confirmed. Section 6 AC2 builds its scratch repository with `git archive HEAD tools`, and AC3 and AC4 reuse that repository through 'the same kind of scratch repository'. HEAD is d07da781e, the spec commit. `git diff 744d2551 HEAD --stat -- tools` printed nothing, and selftest.py:4516-4518 at HEAD still holds the memo-only [dSP-95] checks. So until the build is committed, HEAD is the unbuilt tree. Section 4 meanwhile describes its own measurements as `git archive 744d2551 tools` with the fenced text applied. If a builder verifies before committing, the criteria show the base result. That failure is loud, not a false green, so the effect is contained: low. | sound | - |

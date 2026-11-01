**Serves:** spec-audit TOOL-dSafePassage-95@rev-1

# Review: round-1 spec audit of TOOL-dSafePassage-95

2026-11-01 · Tier-2 · on `branch/unattended-dsafepassage-567339` · adversarial fan through `tier2-review.js` (5 finder lenses, then 5 skeptic batches, then this synthesis). This audit was promoted from the round-6 closing diff review (memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-94-closing-diff-round6.md). TOOL-dSafePassage-95 edits only check_floor_bash in tools/govkit/selftest.py. It spells the stand-in path through joinpath so the [dSP-71] AC4 hand-picked-copies guard no longer reads a hit there, which was round 6's item 1, a red govkit selftest leg at the tip. The third [dSP-94] check observes the mtime pin and the bytecode precondition. A new [dSP-95] check observes the _BASH restore. steps94 is staged through build_staged_copy behind a guard. The anchor replace is counted once. A corrections table carries 94's spec-text items.

Reviewed: memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md@cbb36ab3894ca8826a17fe85463ef201cadbe79d

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. The one HIGH item is a false-red acceptance criterion (AC3). It must be fixed in the spec before the build is graded against AC3. The other items are spec-text corrections or a small added test arm.

Review shape: intensity full, raw 9, confirmed 8, refuted 1, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| reuse | yes | 0 | 0 | 0 | 0 | 0 | - |
| blast-radius | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 1 high, 1 medium, 4 low (6 items).
Adjudicated tally by raw confirmed finding: 0 blocker, 1 high, 3 medium, 4 low (8 findings).

Run integrity: lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates. Fixes on confirmed findings: 7 judged sound, 1 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (id 8, high to medium). Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict. Lens notes: none supplied, so every lens ran on the kit's generic brief.
Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Intent: no spec was supplied as intent. `context` was the caller's statement.
By design: the caller's byDesign.
Move check: no checked subject moved.
Checklist: NONE swept, because none is present. A zero count is not evidence that the project's recurring bug classes are absent.

## HIGH

### H1. AC3's 94-spec diff is red on a correct build (id 1)

- **Where:** memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md, §6 AC3 (third command), and the §3 non-goal "Any edit to ... TOOL-dSafePassage-94.md".
- **What is wrong:** AC3 requires `git diff --numstat 0e5967090 -- tools memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md` to print exactly one line, for selftest.py. 95's own spec commit 6a9aa008b already added a row (the round-6 closing review) to the generated `<!-- gen:spec-records -->` block in 94's spec. So the command prints `1 0 ...-94.md` today, before any build, and it will print two lines on any correct build. The non-goal "no edit to 94's spec" is already false at the spec's own commit, and the records generator will keep writing that file.
- **Consequence:** AC3 cannot pass. A builder who follows it either reports a false red or reverts a generated records row in a CLOSED spec, which breaks memory hygiene and the spec-records render.
- **Fix (skeptic judged SOUND):** Pin the diff base to HEAD at build start (6a9aa008b or later) instead of 0e5967090. Alternatively, compare 94's spec with its `<!-- gen:spec-records -->` block stripped, e.g. `git show <base>:<94 spec>` against the tip. Restate the non-goal as "no hand edit of 94's authored text; the generated records block is re-rendered as usual".
- **Left-shift gate:** add a spec-lint check that runs every `git diff --numstat <base>` AC at the spec's own commit and flags any that is already non-empty for a path the AC says must not change. Where no gate fits, add a checklist entry: "a no-edit AC on a memory record excludes its gen: blocks".

## MEDIUM

### M1. The same AC3 false red, reported by three more lenses (ids 3, 5, 8)

- **Where:** the same spec, §6 AC3 (third clause), with §2 S6 and §3 non-goal 4 ("94 is not edited").
- **What is wrong:** This is the defect in H1. The grounding, blast-radius and failure-envelope lenses each found it on their own, and the skeptics graded each of their findings medium (id 8 was re-graded from high, because the builder sees the red and nothing is falsely certified). The grading rules keep findings with different binding grades in separate items. So these three ids sit here and H1 carries id 1. This is one defect, and H1's high grade governs it. Two details are added here. S6 (line 49) states that 94 is not edited, which is already untrue for the generated block (id 3). Every later record filed against 94, including 95's own reviews, moves that block again, so the criterion can never hold as written (ids 5, 8).
- **Consequence:** the same as H1: a false-red AC, and the risk that a builder reverts the generated records row.
- **Fix (skeptic judged SOUND on all three):** Diff from the build's starting commit, e.g. `git diff --numstat 6a9aa008b -- tools <94 spec>`. Alternatively, keep 0e5967090 for `tools` only and check 94's spec separately with its gen:spec-records block excluded. In S6 and §3, state that the generated records block of 94's spec is re-rendered by the index generator, does not count as an edit, and is exempt from the "not edited" rule. The build should then confirm that the numstat prints exactly one `tools/govkit/selftest.py` line.
- **Left-shift gate:** the gate in H1.

## LOW

### L1. AC4 contradicts its memo-guard-cut Measured row (id 2)

- **Where:** the same spec, §6 AC4 against the §4 "Measured" row "that break with S4's memo guard also cut".
- **What is wrong:** AC4 says that for every Measured break, AC1's command prints `FAIL` for the lines its row names and `ok` for every other line. For the memo-guard-cut row, an `AttributeError` traceback ends the run after the `[dSP-95] ... loads` FAIL, because selftest.py:4474 reads `held = steps._BASH` outside the try. The remaining lines and the final FAILURES line never print.
- **Consequence:** AC4 cannot pass as worded for that row. The row's own text states the expected outcome, so the effect is contained.
- **Fix (skeptic judged SOUND):** Reword AC4 to "prints FAIL for the lines that row names and ok for every other line it prints, and for the memo-guard-cut row the run ends in an AttributeError traceback after the [dSP-95] loads FAIL". Alternatively, drop that row from AC4's set, since it shows why the guard is needed and is not a break the shipped arms must catch.
- **Left-shift gate:** add a checklist entry: "an AC that quantifies over every Measured row is checked against each row's stated outcome, including rows that end in a traceback".

### L2. §7 undercounts the guard join for selftest.py (id 6)

- **Where:** the same spec, §7, the paragraph after the New arm rows (line 305).
- **What is wrong:** §7 says the guard join for `tools/govkit/selftest.py` is the four `{prefix}/govkit/` legs plus `policy fixtures`. A prefix join against tools/gate-legs.json matches 17 legs. Twelve of them match on `{prefix}/`: python resolver, push-main, check-wiring, settings-merge, run-gates canary, run-gates evidence, foreign-prefix parity, install-prefix, dead-path carriers, lexicon naming predicates, spec-tokens and kit-placeholders.
- **Consequence:** the prose undercounts for a reviewer checking that the touched file's guarded legs ran. Every guarded leg runs anyway, so behaviour is unaffected.
- **Fix (skeptic judged SOUND):** State the full join. Alternatively, say the paragraph lists only the legs whose guard names `{prefix}/govkit/` or the file itself, and that the `{prefix}/`-guarded legs also run and are expected unchanged.
- **Left-shift gate:** add a small helper or spec-lint step that prints the guard join for a path from tools/gate-legs.json, so specs paste the computed join instead of typing their own list (the charter forbids leg lists typed elsewhere).

### L3. Item 7's correction misses 94's Alternatives-rejected bullet (id 7)

- **Where:** the same spec, §4 "Corrections to 94's text", item 7 row (line 183).
- **What is wrong:** Item 7 corrects 94's `selftest.py:7734-7736` citation at §4 lines 160-161 and §10 line 345. It misses a third carrier of the same citation: 94's Alternatives-rejected bullet "A shared factory for the staged copy, used by S2 and `selftest.py:7734-7736`" (line 257 at 0e5967090, line 258 at HEAD). The table's line numbers are pinned to 0e5967090 by its lead-in (line 176), so the off-by-one at HEAD is deliberate and is not a defect.
- **Consequence:** the correction record leaves one uncorrected claim in 94. This affects the record's prose only.
- **Fix (skeptic judged SOUND):** Add the Alternatives-rejected bullet (line 257 at 0e5967090) to item 7's "94 says, at" cell. Optionally, also cite each row by section and quoted text.
- **Left-shift gate:** add a checklist entry: "a correction row for a wrong citation greps every carrier of that citation in the corrected record".

### L4. The [dSP-95] restore check never observes the raise path (id 9)

- **Where:** the same spec, §2 S3 (line 39) and §4 "S3 and S5" (line 134).
- **What is wrong:** The [dSP-95] check observes the memo restore only on `us`, whose resolve_shell_argv catches the Refusal and returns. The raise path, which is the case the `finally` exists for, runs only on steps94. There, `_BASH` is None before the read, so a restore cannot be told apart from no restore. The Measured row at line 198 stages only the whole-finally cut.
- **Consequence:** suppose the restore is moved out of `finally` into the try's return path. Every check stays green while the memo is left None on the exception path. The effect is limited to a test arm.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Set the sentinel inside S4's load try, right after `spec94.loader.exec_module(steps94)`: `steps94._BASH = sentinel94`. A copy that does not load then still has no _BASH. After the read, add `steps94._BASH == sentinel94` to the [dSP-95] restore check, or give it its own check. Add a §4 Measured row that stages "restore only on the return path" (the restore moved out of finally into the try body after the call) and shows that check going red.
- **Left-shift gate:** add a checklist entry: "a check that observes a `finally` restore stages a value that differs from the default on the path that raises".

## Refuted

- id 4 (grounding, low): the line numbers in the corrections table are off by one at HEAD. Refuted, because the table's lead-in pins every row to 0e5967090, where the numbers hold. No action is needed.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=9 confirmed=8 refuted=1 unverified=0 blocker=0 high=1 medium=3 low=4 agents=11 out-tokens=75809

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 6 AC3 (third command), and section 3 non-goal 'Any edit to ... TOOL-dSafePassage-94.md' | high | high | confirmed | Re-ran it. `git diff --numstat 0e5967090 -- tools <94 spec>` prints `1	0	...TOOL-dSafePassage-94.md` on today's tree. The diff is one added row, the round-6 closing-diff-round6 review, inside 94's `<!-- gen:spec-records -->` block, written by 95's own spec commit. AC3 (spec lines 277-280) requires one line, for the selftest file, and calls an edit to 94's spec red. So on a correct build the command prints two lines. The non-goal at line 62 ('Any edit to ...-94.md') is already false at the spec's own commit, through the generated block. A builder reading AC3 literally either reports it red or reverts a generated record row in a CLOSED spec. The BY DESIGN block does not cover this. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 6 AC4 against section 4 'Measured', row 'that break with S4's memo guard also cut' | low | low | confirmed | Spec line 200 (Measured row 'that break with S4's memo guard also cut') says an AttributeError traceback ends the run after the `[dSP-95] ... loads` FAIL. AC4 (lines 282-284) says that for every Measured break, AC1's command prints FAIL for the named lines and `ok` for every other line. For this row the remaining lines never print, so AC4 as worded contradicts its own row. In the tree, selftest.py:4474 has `held = steps._BASH` outside the try, and the spec's S5 guard (lines 163-167) is the thing that row cuts, so the traceback is real. The effect is contained because the row's text states what is expected. | sound | - |
| 3 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 6 AC3 (third clause), with section 2 S6 and section 3 non-goal 4 | medium | medium | confirmed | I re-ran the diff at HEAD with a clean tree. `git diff --numstat 0e5967090 -- tools <94 spec>` already prints `1 0 memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md`, and `git diff 0e5967090 HEAD -- <94 spec>` shows one added row, the round-6 closing-diff review, inside `<!-- gen:spec-records -->`. 95's AC3 (spec line 277) says the command prints one line, for the selftest file, and its red-when reading names 'the build edits 94's spec'. A correct build that touches only selftest.py will therefore print two lines and turn AC3 red. S6 (line 49) and non-goal 4 say 94 is not edited, but its generated block already was edited. The effect is contained: a false-red criterion that could mislead the builder. | sound | - |
| 4 | grounding | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 4 'Corrections to 94's text' (the '94 says, at' column) | low | - | refuted | Refuted under case (2), the cited section already says it. The table's lead-in, at line 176 of 95's spec, reads '94 is CLOSED and frozen. Each row is the reading that holds at `0e5967090`.' That sentence pins every line number in the table to 0e5967090, where the finder agrees they are correct. The one-line shift at HEAD comes from the generated records row, as I saw in `git diff 0e5967090 HEAD`, and the section already anchors its citations to a revision that excludes it. | unsound | - |
| 5 | blast-radius | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 6 AC3 (third command), with section 3 non-goal 'Any edit to ...-94.md' | medium | medium | confirmed | I re-ran `git diff --numstat 0e5967090 -- tools <94 spec>` at HEAD. It printed `1	0	memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md` before anything is built, and tools/ shows no change. AC3 (spec line 277) requires exactly one line, for the selftest file, and its Red-when lists 'the build edits 94's spec'. A correct build therefore prints two lines and reads red. The extra line comes from the spec commit 6a9aa008b's re-render of the generated records region, which the section 3 non-goal (line 62) does not separate from a hand edit. No BY DESIGN entry covers it. The effect is contained to a false-red acceptance criterion, plus the risk that a builder reverts the generated region. | sound | - |
| 6 | blast-radius | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 7 (the paragraph after the New arm rows) | low | low | confirmed | Section 7 line 305 says 'The four {prefix}/govkit/ legs and policy fixtures are the guard join's for selftest.py'. I ran a python -B prefix join of tools/govkit/selftest.py against the guards in tools/gate-legs.json. It printed 17 legs. 12 matched on '{prefix}/': python resolver, push-main, check-wiring, settings-merge, run-gates canary, run-gates evidence, foreign-prefix parity, install-prefix, dead-path carriers, lexicon naming predicates, spec-tokens and kit-placeholders. 4 matched on '{prefix}/govkit/' and policy fixtures matched on the file itself. So the stated join undercounts. The consequence is limited to the prose: every guarded leg runs regardless of what section 7 says, and the section's Gates line already names lexicon naming predicates. | sound | - |
| 7 | blast-radius | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 4 'Corrections to 94's text', item 7 row | low | low | confirmed | Re-probed. `grep -n 7734` on 94's spec at HEAD prints 162, 258 and 346. At 0e5967090 it prints 161, 257 and 345. Line 257/258 is the Alternatives-rejected bullet 'A shared factory for the staged copy, used by S2 and `selftest.py:7734-7736`'. 95's item-7 row (spec line 183) cites only '§4, lines 160-161, and §10, line 345', so that third carrier is missing from the record. The off-by-one half is weaker than the finding says. The table heading (spec line 176) already says 'Each row is the reading that holds at `0e5967090`', so the line numbers are deliberately pinned to that revision, and `sed -n 38p` at HEAD shows the HEAD shift the finding describes. The real defect is the missed bullet. The only effect is in a record's prose, with no behaviour change, so it grades low. | sound | - |
| 8 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 6 AC3 (third clause), with section 3 Non-goals 'Any edit to ... spec-TOOL-dSafePassage-94.md' | high | medium | confirmed | Re-probed. `git diff --numstat 0e5967090 -- tools <94 spec>` already prints `1 0 memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md` before anything is built. `git diff` shows one added row inside `<!-- gen:spec-records -->`, the round6 closing-diff-review row. AC3 (spec lines 276-281) requires that command to print one line, for selftest.py, and says it goes red when 'the build edits 94's spec'. §3 line 62 forbids any edit to 94's spec and does not exempt the generator. Once built, AC3 prints two lines and reads red without any authored edit, which could push a builder to revert a generated row. The builder sees the failure, though, and it does not falsely certify anything, so the effect is contained: medium, not high. | sound | - |
| 9 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md:section 2 S3 and section 4 'S3 and S5' | low | low | confirmed | The claim holds. I read tools/govkit/selftest.py:4470-4481. read_fallback_argv saves steps._BASH, sets it to None, returns from inside try, returns e from except, and restores the saved value in finally. In upgrade_steps.py:425-441, resolve_shell_argv catches only Refusal. So `us` returns normally, while steps94 (check_runs narrowed to catch ValueError) lets the spawn's OSError escape, and the raise path is taken only on steps94. steps94 is a fresh module (selftest.py:4485-4489, and S4's module_from_spec), so its _BASH is None before the read. Restored or not, it reads None afterwards, so the raise path's restore cannot be observed. Spec section 2 S3 (line 39) and the S3/S5 code block (line 134) check only `us._BASH == bash87`. The section 4 Measured row at line 198 stages only the whole-finally cut. A refactor that restores only on the return path would leave every check green. Nothing in the spec covers this: it is not a non-goal and not in the BY DESIGN block. The effect stays inside a test arm and no shipped behaviour changes, so the grade is low. | unsound | - |

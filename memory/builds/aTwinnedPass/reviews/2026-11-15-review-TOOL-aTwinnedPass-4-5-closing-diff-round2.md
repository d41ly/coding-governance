**Serves:** diff-review TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5

# Closing diff review, round 2: aTwinnedPass units 4 and 5, the fold of round 1

Tier-2 · 2026-11-15 · on `branch/dazzling-jackson-b895c0` · adversarial fan through `tier2-review.js`: 5 finder lenses (`gov-diff-reviewer`), 5 skeptic batches (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The diff spans 22 files, +2538/−73, merged as `850143b3b`, `563eff37a` and `39a71c080` on top of round 1's tip `c40c39fb6`. Unit 4 holds the pass identity to the runtime's spelling (BRANCH_SHAPE, a confined TREE_SHAPE, `check_pass_branch`, `check_pass_holder`, `remove_pass_tree`, and `--from` at 7 to 64 hex digits). Unit 5 corrects and adds arms in the three suites. Intent came from the three spec documents supplied and the range's commit messages. Every line ref below is pinned to the blob at the reviewed sha `39a71c08`. (PINNED 2026-11-15)

**Reviewed range:** `c40c39fb6430626c5845d53c5a14f829ad057870...39a71c080570cc41b18898467931aed9acdeedb0`. **ROUND 2.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. Five items are MEDIUM. One is a deny rule that the spec and a comment state but the code does not implement (M1). One is a spec rationale claiming that a safeguard ties the returned branch and worktree together when nothing does (M2). Three are suite arms that cannot go red on a regression they are meant to catch (M3 to M5). The three LOW items are text that misstates coverage or classification, plus one missing branch-gone assertion.

## Review shape

Intensity **full** · raw **10** · confirmed **8** · refuted **2** · merged **0** · unverified **0** (0 uncertain) · precision **0.80**.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

No two confirmed findings describe the same defect, so the 8 confirmed findings form **8 items**.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 3 LOW** (8 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 3 LOW** (8 findings).

Every id keeps its bracketed binding grade, and I re-grade none. Id 3 is the one the skeptic re-graded, from the finder's low to medium, and that medium is binding.

Twin flag: refuted id 2 is the same defect as confirmed id 5. Both say the returned branch and worktree are each shape-checked alone, so a mismatched pair passes. Id 2 was refuted as pre-existing and a stated non-goal. Id 5 survived because spec 4's rationale falsely claims that `check_pass_holder` covers the gap. The flag changes no grade, item or count. Refuted id 1 (no binding of a branch to its pass) is a different defect from any confirmed finding, so it gets no flag.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts were demoted to unverified, and **0** orphaned duplicate refutations were demoted.
- **0** duplicate refutations were counted as merged confirmations.
- **0** spurious verdicts were discarded, and **0** duplicates were removed.
- Fixes on confirmed findings: **7** judged sound, **1** judged UNSOUND (id 9), **0** judged INSTANCE-ONLY, **0** none proposed, **0** NOT JUDGED.
- Severity on confirmed findings: **0** UNGRADED by the skeptic, **1** RE-GRADED by the skeptic (id 3).
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Checklist: **42** items, acquired from `--for-diff c40c39fb6430626c5845d53c5a14f829ad057870..HEAD`, each assigned to one of the five lenses (security 9, correctness 9, seams 8, verification 8, intent 8).
- By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.
- Shown to this synthesis: 2 refuted findings and 1 same-address pair.
- Dispositions: unclassed refuse; 42 class slugs and 175 leg names handed.

Every count above is zero where it should be, so this run is complete.

## MEDIUM

### M1 — an unreadable worktree list admits the holder, but the spec and the comment say it denies (id 3)

- **Where:** `tools/unattended/pass-tree.sh@8e75d203:131`, the comment, and the guard at `:136` in `check_pass_holder`. It calls `derive_holder_where` (`tools/unattended/unattended.sh@dba68e98:9306`). The spec claim is at `memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-4.md@8416b5c8:191`.
- **What:** The comment says "An unreadable list leaves the primary empty, which fails the comparison". Spec 4 says "an unreadable worktree list denies". But `derive_holder_where` reads `git worktree list --porcelain 2>/dev/null`. When that read fails and the branch exists, it prints the remedy sentence "no worktree on this node has it checked out...". That text is not a directory, so `[ -d "$where" ] || return 0` admits the branch with `PT_WHERE` empty before the primary is ever read. The empty-primary comparison can refuse only if the first list read works and the second one fails.
- **Consequence:** A deny-by-default rule stated in the spec is not implemented. The effect is contained: `--merge` proceeds, `remove_pass_tree` skips the worktree removal, and `branch -D` still meets git's own held-branch refusal. The false text will mislead the next edit that relies on it. The binding grade is MEDIUM, re-graded up from the finder's low because a spec-stated deny path is missing, which is more than a comment fault.
- **Fix (judged SOUND by the skeptic):** Either make the guard deny or correct the text.
  - To deny: in `check_pass_holder`, read the porcelain list once, refuse when that read fails, and derive both the holder and the primary from that one capture.
  - To correct the text: state that an unreadable list reads as "no holder" and leaves the worktree to `branch -D`'s own refusal, and drop the claim from the comment and from spec 4 line 191.
  - Probe: wrap `GIT` so that `worktree list` exits 128, run `--remove` on a held confined branch, and observe exit 0 or 1 from `remove_pass_tree` rather than the holder refusal.
- **Left-shift gate:** Add an arm to the `unattended kit gate` leg's `pass-tree.test.sh` that fails `git worktree list` through a `GIT` wrapper and asserts whichever behaviour the text states. Every deny-on-unreadable claim then has a red-first arm.

### M2 — the returned branch and worktree are checked each alone, and spec 4 claims `check_pass_holder` ties them together (id 5; refuted twin id 2)

- **Where:** `tools/workflows/unattended-unit.js@08be490b:449` (the checks at lines 446-449). The rationale is at `memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-4.md@8416b5c8:327-328`.
- **What:** `ownBranch` and `ownTree` are each graded against their own regex. A node probe of the shipped regexes printed `true true` for branch `worktree-agent-x1` with tree `C:/p/.claude/worktrees/agent-x2`. The tree reaches only `nextAction` (line 485), as the directory where the pass legs run. `pass-tree.sh` takes only `--branch` (line 311), and `check_pass_holder` (line 132) derives the holder path from the branch. It never sees the returned worktree. Spec 4's line "`check_pass_holder` holds them together at the destructive end" is therefore false.
- **Consequence:** With a mismatched pair, `nextAction` runs `PL --base <passBase>` in x2's worktree, so x2's HEAD is graded. Then `pass-tree.sh --merge --branch worktree-agent-x1` passes the holder check and merges x1's commit, a commit no pass leg ever ran over. The green that was printed belonged to another pass. The behavioural gap already existed at base with looser shapes. What this diff adds is the false rationale, which tells the next change that a safeguard exists when it does not. This diff also gives both values a common `<id>`, so the cross-check is now cheap. Only a faulty or hostile builder can return a mismatched pair, and `nextAction` still names the returned sha, so the effect is contained.
- **Fix (judged SOUND by the skeptic):**
  - In `unattended-unit.js`, return `''` for both values, or at least for the worktree, unless the `<id>` after `worktree-agent-` in `ownBranch` equals the `<id>` after `agent-` at the end of `ownTree`.
  - Add a TP4 arm that feeds branch x1 with worktree agent-x2 and expects `"worktree":""` and the "returned unusable" `nextAction`.
  - Correct spec 4's rationale lines, or the next unit's text, so they no longer claim that `pass-tree.sh` ties the two together.
- **Left-shift gate:** Add an arm to the `unattended-build self-test` leg that feeds every pair of agent-returned values sharing an identity (here the branch and the worktree) a mismatched pair and asserts refusal. Pair it with a `spec tokens (the pass's own spec)` style check that a named safeguard function actually receives the value the spec says it guards.

### M3 — no arm tests the primary-tree anchor of the holder check (id 7)

- **Where:** `tools/unattended/pass-tree.test.sh@96d03d18:316` (the TP4 block, lines 316-353), against the exact comparison at `tools/unattended/pass-tree.sh@8e75d203:138-139`.
- **What:** `check_pass_holder` builds `want="$primary/.claude/worktrees/${PT_BRANCH#worktree-}"` and compares the holder to it exactly. TP4's refused holders are q1 at `$T/elsewhere/agent-q1`, which has no `.claude/worktrees` segment, and q3 at `$R/.claude/worktrees/agent-zz`, which has the wrong id. Both also fail a suffix test such as `case $where in */.claude/worktrees/${PT_BRANCH#worktree-})`. Every admitted holder (the p* branches and q4) sits under `$R`, so the suffix test admits it too. No arm puts a correct-id holder under a tree other than the primary.
- **Consequence:** Losing the primary anchor would let `--remove` and `--merge` run `git worktree remove --force` on a worktree of this repository that sits under some other tree's `.claude/worktrees/agent-<id>`, for example under a linked run worktree's own `.claude/worktrees`, untracked files included. Every T1-T7 and TP4 arm would stay green. Spec 4 §7's staged breaks never test this half. Today's code is correct, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** Add a TP4 arm.
  - Run `git -C "$R" worktree add -q -b worktree-agent-q5 "$T/elsewhere/.claude/worktrees/agent-q5" "$C"` and write a `keep.txt` there.
  - Run `--remove tRun --branch worktree-agent-q5`. Check that it exits 1, that its stderr carries "where the runtime cuts that pass's worktree", and that both the directory and `keep.txt` remain.
  - Observe the arm red under the suffix-match break above, then green, and record the break in the arm's comment.
- **Left-shift gate:** For every confinement rule with more than one half (here the primary anchor and the `agent-<id>` tail), the `unattended kit gate` leg's suite should hold one refused fixture per half that passes every other half. Record each half's staged break in spec §7.

### M4 — the AC3 and AC5 `--remove` arms stay green under the staged break spec 4 names for them (id 8)

- **Where:** `tools/unattended/pass-tree.test.sh@96d03d18:324` (the q1 `--remove` arms at lines 321-326 and the q3 arms at 345-346). The staged break is at `memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-4.md@8416b5c8:414`.
- **What:** Spec 4 §7 names the break "`check_pass_holder` returning 0 always, which force-removes q1". The built `remove_pass_tree` (pass-tree.sh lines 179-189) runs `worktree remove --force` only when `PT_WHERE` is non-empty. A bare `return 0` leaves `PT_WHERE` empty, so the call falls through to `git branch -D`. Git refuses to delete a branch that a worktree holds, and its error names the holder path. A probe printed `error: cannot delete branch 'worktree-agent-q1' used by worktree at '.../elsewhere/agent-q1'` and exited 1. `cmd_remove_tree` then prints one REFUSING line ("could not be taken away whole") and exits 1.
- **Consequence:** Under the named break, all six AC3 `--remove` arms and both q3 arms stay green: rc 1, one REFUSING line, the error text carrying `elsewhere/agent-q1`, and the directory, `keep.txt` and branch all remaining. Only the `--merge` q1 text arm goes red. The red-first observation owed at close for AC3 cannot happen as written, and the `--remove` arms cannot tell the holder refusal from the `branch -D` fallback. A break that does set `PT_WHERE` and force-removes would still be caught, so the effect is contained.
- **Fix (judged SOUND by the skeptic):**
  - Add `check_has ... "$err" "where the runtime cuts that pass's worktree"` to the `--remove` q1 arm and to the q3 arm, as the `--merge` q1 arm already does.
  - Restate spec 4's staged break as "`check_pass_holder` admits any holder (`PT_WHERE=$where` with the comparison dropped)", which does force-remove q1.
  - Close probe: stage `check_pass_holder() { PT_WHERE=""; return 0; }`, run the suite, and confirm the new text arms go red.
- **Left-shift gate:** Each staged break named in a spec §7 should be run mechanically at close, with the suite required to go red. The `harness arms (fail branches armed or pinned)` leg is the natural home. A refusal arm should assert the refusing function's own text, not only an exit code that a fallback also produces.

### M5 — T6 claims to arm every exit-2 path of `main`, and arms five of twelve (id 9)

- **Where:** `tools/unattended/pass-tree.test.sh@96d03d18:359` (the T6 header) and its "Not checked" line at `:364`. The acceptance criterion is at `memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-5.md@87041699:527`.
- **What:** `main` in `tools/unattended/pass-tree.sh` (lines 305-332) has twelve `exit 2` sites. T6 makes five `check_usage_refused` calls: the missing `--from`, a second `--branch`, `--remove` carrying `--pass`, slug `../x`, and the unit of another build. Seven sites have no arm: a missing value after a flag (306), a second verb (309), an unknown argument (315), `--merge` without `--pass` (319), `--merge` without `--branch` (320), `--remove` without `--branch` (323), and no verb (324). The T6 header says "every exit-2 path of main". The "Not checked" line names only paths a later edit adds. Spec 5's AC4 says it is red when "an exit-2 path of `main` has no arm asserting exit 2".
- **Consequence:** The comment and the acceptance criterion certify coverage that does not exist. Deleting any of the seven unarmed usage exits keeps T6 green. The effect is confined to the test's coverage claim, so the grade is MEDIUM.
- **Fix:** The finder's proposed fix was judged UNSOUND, so this is the skeptic's corrected fix. Choose one of the following.
  - Reword the T6 header, its "Not checked" line and spec 5's AC4 Red-when to name the five armed paths and list the seven unarmed ones. Spec 5 is CLOSED and frozen by `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`, so this has to go through a new spec revision.
  - Or add `check_usage_refused` calls for all seven, and in the same revision change AC4's expected count from 5 to 12.
- **Left-shift gate:** Add a count check to the `harness arms (fail branches armed or pinned)` leg. It counts `exit 2` sites in `main` and `check_usage_refused` calls in T6 and fails when a header claims "every" path and the counts differ.

## LOW

### L1 — the T7 header lists the NOTE's stream as not checked, when the T7 arm does check it (id 4)

- **Where:** `tools/unattended/pass-tree.test.sh@96d03d18:30`.
- **What:** The header's not-checked list includes "which stream the T7 NOTE goes to". But T7 captures stdout into `out` and stderr into `$T/err` (line 389), and the NOTE arm at line 393 reads only `$err`. If the `>&2` at `tools/unattended/pass-tree.sh@8e75d203:266` were dropped, that arm would go red, and so would the ls-tree arms that read `$out` as a sha.
- **Consequence:** The header understates what is covered. A later editor could add a duplicate stream arm, or treat the stream as unguarded and miss a real gap somewhere else. Behaviour is unaffected.
- **Fix (judged SOUND by the skeptic):** Remove "and which stream the T7 NOTE goes to" from the not-checked list, or state that the T7 NOTE arm reads stderr alone, so dropping the `>&2` at `tools/unattended/pass-tree.sh@8e75d203:266` fails it.
- **Left-shift gate:** Add a line to this project's bug-class checklist: when a fold adds a "Not checked" line, check each entry against the arms beneath it in both directions.

### L2 — the build README's classification lists reasons for three units while classifying five (id 6)

- **Where:** `memory/builds/aTwinnedPass/README.md@a115c137:34`.
- **What:** The Classification bullet gained "and two promoted from the closing review's round 1". The reasons that follow still name only the three original kinds of change: a changed kit contract, a new kit tool, and a changed `--dispatch` behaviour. Nothing describes unit 4 (a narrowed shape and holder check) or unit 5 (corrected suite arms).
- **Consequence:** The build's own M2 classification of units 4 and 5 says nothing true about them. Behaviour is unaffected.
- **Fix (judged SOUND by the skeptic):** Extend the clause to classify units 4 and 5, for example "a narrowed handoff shape and holder check in the kit tool, and corrected suite arms". Or split the bullet into one line for the three units at open and one for the two promoted units.
- **Left-shift gate:** Extend the `build README slot contract` leg so the Classification slot names a reason for each unit it counts.

### L3 — the AC6 q4 arm never checks that the branch is gone (id 10)

- **Where:** `tools/unattended/pass-tree.test.sh@96d03d18:351`. The criterion is at `memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-4.md@8416b5c8:392`.
- **What:** AC6 says that after `--remove` of `worktree-agent-q4` "the directory and branch are gone". The q4 arms check only rc 0 and that the directory is gone. No assertion reads `refs/heads/worktree-agent-q4`.
- **Consequence:** A regression in which `remove_pass_tree` removes the worktree but skips `branch -D` on the confined-holder path would leave AC6's branch half unobserved. T5 arms check branch deletion on other branches, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** After line 351, add `git rev-parse --verify -q refs/heads/worktree-agent-q4 >/dev/null; check_same "TP4 branch worktree-agent-q4 is gone (AC6)" "$?" 1`.
- **Left-shift gate:** Add a line to this project's bug-class checklist: each clause of an AC's observable outcome ("X and Y are gone") gets its own assertion. A `spec tokens`-style trace from AC clauses to arm labels could enforce this later.

review-shape kind=diff-review round=2 intensity=full at=synth raw=10 confirmed=8 refuted=2 merged=0 unverified=0 blocker=0 high=0 medium=5 low=3 agents=11 out-tokens=86419
review-round round=2 limit=- prior=3 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/pass-tree.sh@8e75d203:138 | high | - | refuted | Pre-existing, and this diff narrowed it rather than introducing it. At base, remove_pass_tree (`git show c40c39fb6:tools/unattended/pass-tree.sh` line 152) ran `git worktree remove --force` on whatever holder derive_holder_where named. Base BRANCH_SHAPE (tools/workflows/unattended-unit.js@c40c39fb6:443) admitted any branch name. So at base, a builder naming a sibling pass's worktree-agent-<id>, another build's pass or another session's agent tree already reached the same force-remove. --merge of a same-run sibling was equally possible at base. The header at base also already said, in section 5, "That `--branch` is the branch the harness returned for `--pass`: the main loop's word is taken". The text is unchanged at the tip (pass-tree.sh line 50). The diff built round 1's corrected fix for H2 (review round1, lines 78-82): confine the branch to ^worktree-agent-[A-Za-z0-9]+$ and the holder to <primary>/.claude/worktrees/agent-<id>, keep --force, add no dirty refusal. check_pass_holder (lines 132-143) does that, and the spec's AC arms cover it. Binding a branch to its pass was never part of that fix or of spec 4's scope. The new header sentence 'neither ever removes a tree it did not cut' is literally true, since the runtime cut every tree the check admits. This is the base defect's residue, not a new defect the fold introduced. | unsound | destructive-step-before-its-precondition | - |
| 2 | security | tools/workflows/unattended-unit.js@08be490b:449 | medium | - | refuted | Pre-existing and by the unit's design. At base (`git show c40c39fb6:tools/workflows/unattended-unit.js` lines 442-445), ownTree and ownBranch were also each checked alone against their own regex, and the base shapes were looser. So a mismatched branch and worktree already reached nextAction and the merge at base. The diff only tightened each shape. Spec TOOL-aTwinnedPass-4 also lists the cross-check under §3 Non-goals ('A cross-check in the harness that the worktree's <id> equals the branch's') and under 'What the design does not check'. That rules it out of scope for this fold rather than a defect the diff introduced or made reachable. | instance | - | - |
| 3 | correctness | tools/unattended/pass-tree.sh@8e75d203:131 | low | medium | confirmed | At 39a71c080, check_pass_holder in pass-tree.sh calls derive_holder_where (tools/unattended/unattended.sh@dba68e98:9306), which reads `git worktree list --porcelain 2>/dev/null`. If that read fails, wp is empty and the branch still exists, so the function prints the remedy sentence 'no worktree on this node has it checked out...'. That text is not a directory, so `[ -d "$where" ] \|\| return 0` admits the branch with PT_WHERE empty before primary is ever read. The empty-primary comparison can only refuse if the first list read works and the second fails. Both the comment added in this diff (tools/unattended/pass-tree.sh@8e75d203:131, 'An unreadable list leaves the primary empty, which fails the comparison') and spec 4 line 191 ('an unreadable worktree list denies') claim a deny rule the code does not have. The diff introduced this. The effect is contained, because branch -D still gets git's own held-branch check. But a spec-stated deny path is not implemented, so this is more than a comment fault. | sound | guard-above-a-fold-makes-its-fallback-dead | class:guard-above-a-fold-makes-its-fallback-dead |
| 4 | correctness | tools/unattended/pass-tree.test.sh@96d03d18:30 | low | low | confirmed | The header line was added in this diff at tools/unattended/pass-tree.test.sh@96d03d18:30. It lists 'which stream the T7 NOTE goes to' as not checked. But the T7 arm captures stdout into out and stderr into $T/err, and its check_has on the 'no effective generated output covers them: fx-stray.txt' needle reads only $err. pass-tree.sh emits the NOTE with >&2. Dropping that redirect would move the NOTE into out, so that arm would go red, and the ls-tree arms that read $out as a sha would go red too. The header therefore understates what is covered. It is comment-only, with no effect on behaviour. | sound | observed-by-claim-no-arm-discharges | new:not-checked-line-names-an-armed-condition |
| 5 | seams | tools/workflows/unattended-unit.js@08be490b:449 | medium | medium | confirmed | The independent checks at tools/workflows/unattended-unit.js@08be490b:446-449 are real. ownBranch and ownTree are each graded alone, and a node probe of the shipped regexes printed `true true` for branch worktree-agent-x1 with tree C:/p/.claude/worktrees/agent-x2. The tree reaches only nextAction (line 485), as the directory where the pass legs run. pass-tree.sh reads only --branch (line 311), and check_pass_holder (line 132) derives the holder path from the branch. It never sees the returned worktree. So spec 4's line saying `check_pass_holder holds them together at the destructive end` is false. The behavioural gap already existed at base c40c39fb6, where both shapes were looser and also graded alone. What this diff adds is the false rationale in spec 4, a new document that tells the next change a safeguard exists when it does not. This diff also gives both values a common <id>, so pairing them is now a cheap check that the spec's rationale argues away. The effect is contained: only a faulty or hostile builder can return a mismatched pair, and nextAction still names the returned sha. That makes it medium. | sound | - | new:paired-handoff-values-checked-each-alone |
| 6 | seams | memory/builds/aTwinnedPass/README.md:34 | low | low | confirmed | The diff changed README.md line 34 only to append `and two promoted from the closing review's round 1`. The reasons that follow still list three kinds of change: a changed kit contract, a new kit tool, and a changed --dispatch behaviour. None of them describes unit 4, a narrowed shape and holder check, or unit 5, corrected suite arms. The build record is wrong about this but behaviour is unaffected, so it is low. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 7 | verification | tools/unattended/pass-tree.test.sh@96d03d18:316 | medium | medium | confirmed | tools/unattended/pass-tree.sh@8e75d203:137-139 builds want="$primary/.claude/worktrees/${PT_BRANCH#worktree-}" and compares it exactly. The TP4 holders in pass-tree.test.sh are q1 at $T/elsewhere/agent-q1, which has no .claude/worktrees segment, and q3 at $R/.claude/worktrees/agent-zz, which has the wrong id. Both fail a suffix test `*/.claude/worktrees/agent-<id>` just as they fail the exact test. Every admitted holder (p*, q4) sits under $R, so the suffix test admits it too. No arm puts a holder at a correct-id path under a tree other than the primary, so losing the primary anchor leaves every arm green. check_pass_holder is new in this diff, so the gap is in scope. It is a missing guard on a forced-removal rule, and today's code is correct, so the effect is contained. | sound | - | class:containment-tested-one-way |
| 8 | intent | tools/unattended/pass-tree.test.sh@96d03d18:324 | medium | medium | confirmed | Spec 4 §7 names the staged break 'check_pass_holder returning 0 always, which force-removes q1'. The built remove_pass_tree (tools/unattended/pass-tree.sh@8e75d203:179-189) runs `worktree remove --force` only when PT_WHERE is non-empty. A bare return 0 leaves PT_WHERE empty, so the call goes on to `branch -D`. Git refuses that for a branch a worktree holds, and its error names the holder path. cmd_remove_tree:297 then prints a single REFUSING line ('could not be taken away whole') and exits 1. So the --remove q1 arms (rc 1, one REFUSING line, err has elsewhere/agent-q1, directory, keep.txt and branch remain) and both q3 arms (rc 1, directory remains) all stay green. Only the --merge q1 text arm goes red. The spec's stated red-first observation ('force-removes q1') does not happen as written, and the --remove arms cannot tell the holder refusal from the branch -D fallback. Contained: a break that does set PT_WHERE and force-removes would still be caught. | sound | staged-break-substitutes-a-synthetic-value | class:staged-break-substitutes-a-synthetic-value |
| 9 | intent | tools/unattended/pass-tree.test.sh@96d03d18:359 | medium | medium | confirmed | I checked main in tools/unattended/pass-tree.sh (lines 305-332). It has twelve `exit 2` sites. T6 (pass-tree.test.sh, after line 359) makes exactly five check_usage_refused calls: the missing --from, a second --branch, --remove carrying --pass, slug ../x, and the unit of another build. Seven sites have no T6 arm: the missing value at line 306, the second verb at 309, the unknown argument at 315, --merge without --pass at 319, --merge without --branch at 320, --remove without --branch at 323, and no verb at 324. Two texts claim more than that. The T6 header says 'every exit-2 path of main', and its 'Not checked' line names only paths a later edit adds. Spec 5's AC4 Red-when says 'an exit-2 path of main has no arm asserting exit 2'. Both certify coverage that does not exist. This diff introduced T6 and the AC, so the finding is in scope. The effect is contained to the test's coverage claim, so I grade it medium. | unsound | - | class:observed-by-claim-no-arm-discharges |
| 10 | intent | tools/unattended/pass-tree.test.sh@96d03d18:351 | low | low | confirmed | Spec 4's AC6 says that after --remove of worktree-agent-q4 'the directory and branch are gone'. The q4 arms in pass-tree.test.sh check only rc 0 and that the directory is gone (`[ -d ... ]` expecting 1). No assertion reads refs/heads/worktree-agent-q4. A regression that skips `branch -D` on the confined-holder path would leave this arm green. Other T5 arms check branch deletion on other branches, so the effect is contained. The fix is sound: like the neighbouring q1 arm, it uses `git rev-parse --verify -q refs/heads/<branch>` from the repo's working directory. That command exits 1 for an absent ref, so it cures the gap and introduces nothing new. | sound | - | class:observed-by-claim-no-arm-discharges |

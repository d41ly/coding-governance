**Serves:** diff-review TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3

# Closing diff review, round 1: aTwinnedPass units 1 to 3, parallel passes in worktrees of their own

Tier-2 · 2026-11-15 · on `branch/dazzling-jackson-b895c0` · adversarial fan through `tier2-review.js`: 5 finder lenses (`gov-diff-reviewer`), 5 skeptic batches (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The diff spans 40 files, +4769/−27. It covers the worktree-isolated pass in `tools/workflows/unattended-unit.js` (unit 1), the new `tools/unattended/pass-tree.sh` merge-back and removal tool (unit 2), and condition 1's generated-output skip in `tools/unattended/unattended.sh` (unit 3). Intent came from the three unit specs and the range's commit messages. Every line ref below is pinned at the reviewed sha `c40c39fb`. (PINNED 2026-11-15)

**Reviewed range:** `aebbb4a725d58dd69b12f1f319e82f5b5d8a8e8e...c40c39fb6430626c5845d53c5a14f829ad057870`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker. Three items are HIGH, and the build should not close until they are fixed. Two are security holes on a narrow path, where a builder's free-text return reaches the main loop or a destructive git command without the shape check the security model requires: H1 is the worktree path and H2 is the branch handed to `--remove`. The third is a suite arm that certifies an absence it never tests. The six MEDIUM items are one sha-shape mismatch between the harness and `pass-tree.sh`, plus five coverage gaps where the code is correct today but no arm would go red if it regressed. The two LOW items are a misleading admission arm and a stream condition no arm can see.

## Review shape

Intensity **full** · raw **15** · confirmed **14** · refuted **0** · merged **1** · unverified **0** (0 uncertain) · precision **1.00**.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 1 | 0 | 1 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

The merged count is id 4, a duplicate of id 5 that the pipeline counted as a merged confirmation. It is not a confirmed id and is not adjudicated here.

My own merges collapse the 14 confirmed findings into **11 items**. Ids 3, 6 and 13 are the one vacuous `'OWN WORKTREE'` needle, seen by three lenses. Ids 5 and 14 are the one `--from` versus passBase shape mismatch.

Adjudicated, by item: **0 BLOCKER · 3 HIGH · 6 MEDIUM · 2 LOW** (11 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 3 HIGH · 8 MEDIUM · 3 LOW** (14 findings).

Every id keeps its bracketed binding grade, and I re-grade none. A merged item takes the highest grade among its ids.

No refuted findings and no same-address pairs were shown, so no twin is flagged.

## Run integrity

- Lenses **5/5** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts were demoted to unverified, and **0** orphaned duplicate refutations were demoted.
- **1** duplicate refutation was counted as a merged confirmation (id 4 into id 5).
- **0** spurious verdicts were discarded, and **0** duplicates were removed.
- Fixes on confirmed findings: **11** judged sound, **3** judged UNSOUND (ids 2, 7 and 12), **0** judged INSTANCE-ONLY, **0** none proposed, **0** NOT JUDGED.
- Severity on confirmed findings: **0** UNGRADED by the skeptic, **3** RE-GRADED by the skeptic (ids 3, 5 and 6).
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- Checklist: **66** items, acquired from `--for-diff aebbb4a7..HEAD`, each assigned to one of the five lenses (security 14, correctness 13, seams 13, verification 13, intent 13).
- By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.
- Shown to this synthesis: 0 refuted findings and 0 same-address pairs.

Every count above is zero where it should be, so this run is complete.

## HIGH

### H1 — TREE_SHAPE passes shell metacharacters and `..` into the main loop's instruction (id 1)

- **Where:** `tools/workflows/unattended-unit.js@c40c39fb:442`, spliced into `nextAction` around lines 480-482.
- **What:** `TREE_SHAPE = /^(\/|[A-Za-z]:[\\/])[^\r\n`]*$/` refuses only CR, LF and backtick. It is the only check between the builder's free-text `worktree` and the main loop's instruction to run the pass legs "with its working directory at `<worktree>`". Spec TOOL-aTwinnedPass-1 names it as the answer to agent-output-interpolated-into-an-instruction.
- **Consequence:** A return such as `/w/a"; touch /tmp/pwn; "`, `/w/$(id)` or `C:/../../Windows` reaches the instruction intact; the finder's probe printed `true` for all three. If the main loop turns that into `cd "<path>" && ...`, the payload runs with the main loop's grants, which the builder lacks. If it does not, the legs run in a tree that is not the pass's. Reaching this needs a misbehaving or injected builder, so the path is narrow, and the grade is HIGH.
- **Fix (judged SOUND by the skeptic):** Hold `worktree` to the layout the runtime actually cuts.
  - Require a final segment `.claude[\\/]worktrees[\\/]agent-[A-Za-z0-9]+$`.
  - Allow only a character class with no shell metacharacters, such as `^(\/|[A-Za-z]:[\\/])[A-Za-z0-9._ \\/:-]*$`.
  - Refuse any `..` segment, as `tools/workflows/unattended-build.template.js@cc868b60:311` already does for `scratch` and `repo`.
  - Tighten BRANCH_SHAPE to `^worktree-agent-[A-Za-z0-9]+$` in the same change.
  - Probe it with returns whose `worktree` is `/w/$(id)` and `/x/../y`, and assert that `worktree` comes back `''` and that `nextAction` names neither value.
- **Left-shift gate:** Add a class-wide arm to the `unattended-build self-test` leg. It feeds every agent-returned value that reaches `nextAction` a fixed set of hostile strings (`$(…)`, `"`, `;`, `..`, backtick, newline) and asserts that each one is refused.

### H2 — `--remove` force-removes any worktree holding a builder-named branch (id 2)

- **Where:** `tools/unattended/pass-tree.sh@c40c39fb:152`, inside `remove_pass_tree` (lines 150-158), reached from `cmd_remove_tree` (around lines 255-268) and `check_pass_branch` (lines 98-114).
- **What:** `--remove` checks only these things about `--branch`:
  - it is a legal ref name;
  - it does not start with `-`;
  - it is not the run's own branch;
  - none of its commits is unique to it.

  It then runs `git worktree remove --force` on whatever worktree holds that branch, followed by `git branch -D`. Nothing confines either step to a harness-cut `worktree-agent-*` branch or to a holder under `.claude/worktrees/agent-*`. The value is the builder's returned `branch`, and BRANCH_SHAPE (`tools/workflows/unattended-unit.js@1094ea03:443`) admits any branch name.
- **Consequence:** Suppose a builder returns `committed:false` and names another live worktree's fully pushed branch, such as another session's worktree or the operator's own. That worktree is force-removed, uncommitted and untracked files included, and its branch is dropped. This is data loss outside the run, reached through agent free text, on a narrow path, so the grade is HIGH.
- **Fix:** The finder's proposed fix was judged UNSOUND, so this is the skeptic's corrected fix.
  - In `check_pass_branch`, refuse any branch not matching `^worktree-agent-[A-Za-z0-9]+$`.
  - In `remove_pass_tree`, refuse unless the holder path from `derive_holder_where` sits under `<primary tree>/.claude/worktrees/agent-`.
  - Keep `--force` for a confined pass holder, and add no dirty-tree refusal.
  - Tighten BRANCH_SHAPE in `unattended-unit.js` to the same pattern.
- **Left-shift gate:** Add an arm to the `unattended kit gate` leg's `pass-tree.test.sh`. It creates a second worktree on a pushed branch outside `.claude/worktrees/agent-*`, runs `--remove` naming that branch, and asserts exit 1 with the worktree still present.

### H3 — the T3 absence arm searches for a needle the harness never emits (ids 3, 6, 13)

- **Where:** `tools/workflows/unattended-build.test.sh@c40c39fb:1417`, plus spec TOOL-aTwinnedPass-1 line 340, which carries the same needle.
- **What:** `hasnt_ "TP1 T3 $m has no worktree paragraph" "${!m}" 'OWN WORKTREE'` checks for a string that appears nowhere in `unattended-unit.js`. The paragraph at `tools/workflows/unattended-unit.js@1094ea03:339` reads `THIS PASS BUILDS IN A WORKTREE OF ITS OWN`, and the log line at `:419` reads `own worktree from` in lower case. `hasnt_` at line 278 is a case-sensitive glob, so the arm can never fail.
- **Consequence:** Spec 1 S8/AC2 requires that a call without passBase keeps exactly the base prompt. If the reset-to-passBase paragraph leaked into every default prompt, both T3 arms (childU and childA) would stay green. T2's `same` comparison would still catch the leak for childA, but for childU, the unattended default, nothing would. Both arms count toward the raised FLOOR_ASSERTIONS.
- **Grades:**
  - id 13 keeps its binding HIGH, because it is a check certifying what it does not check, with only partial cover elsewhere;
  - ids 3 and 6 keep their binding MEDIUM, as the skeptic re-graded them, weighing the sibling arms that still cover part of it.

  The item takes HIGH.
- **Fix (judged SOUND by the skeptic, for all three ids):**
  - Change the needle to the paragraph's own opening, `THIS PASS BUILDS IN A WORKTREE OF ITS OWN`, which T1 already uses as its positive control, or to `git reset --hard`.
  - Make the same change to spec 1's T3 text at line 340.
  - Observe the arm go red once by emitting the paragraph without passBase in a scratch copy.
- **Left-shift gate:** Add a rule to the `harness arms (fail branches armed or pinned)` leg. It refuses a `hasnt_`/`miss` needle that is a literal absent from every file the suite's subject emits, so an absence arm must name text its subject can produce.

## MEDIUM

### M1 — `--from` accepts 7 to 40 hex digits, while passBase accepts 7 to 64 (ids 5, 14)

- **Where:** `tools/unattended/pass-tree.sh@c40c39fb:179` against `tools/workflows/unattended-unit.js@c40c39fb:178` (COMMIT_SHAPE). The refusal text is at `tools/unattended/pass-tree.sh@def02e16:181`, and the header at `tools/unattended/pass-tree.sh@def02e16:23` orders the main loop to pass "the same sha" to both.
- **What:** One handoff has two shapes. The harness accepts a 64-digit passBase, and `pass-tree.sh` refuses the same value as `--from`. Spec 2 (lines 51 and 223) carries the same 40-digit limit.
- **Consequence:** In a SHA-256 repository the full `git rev-parse HEAD` value is 64 digits. The builder resets to it and commits, and then every `--merge --from <that sha>` is refused, so no parallel pass merges back until someone shortens the sha by hand. The refusal is clean and nothing is lost. The kit is project-agnostic, so such repositories are in scope.
- **Grades:** id 14 keeps MEDIUM, and id 5 keeps LOW, as the skeptic re-graded it for a contained, clean refusal. The item takes MEDIUM.
- **Fix (judged SOUND by the skeptic, for both ids):**
  - Widen `tools/unattended/pass-tree.sh@def02e16:179` to `^[0-9a-f]{7,64}$`; `git rev-parse --verify` already decides whether the value names a commit.
  - Update the refusal text and spec 2's S4 lines 51 and 223 to match.
  - Add a `pass-tree.test.sh` arm that passes C's full `git rev-parse` output as `--from`, and one in a `git init --object-format=sha256` fixture that must succeed.
- **Left-shift gate:** Add a parity arm to the `unattended kit gate` leg. It reads the sha shape from both ends of the passBase-to-`--from` handoff and fails when they differ.

### M2 — no arm tells the own-side generated-output skip from the old loop (id 7)

- **Where:** `tools/unattended/unattended.sh@c40c39fb:14906` (`for p in $_c1_own`), and the new arms at `tools/unattended/unattended.test.sh@c188e38f:9530-9555`.
- **What:** B2 and B6 exercise only the sibling-side skip. The one case where `$_c1_own` and `"$@"` differ is this call declaring a covered path under a sibling's directory claim, and no arm builds it. Spec AC7 is a one-time source awk, not a suite arm.
- **Consequence:** Reverting line 14906 to `for p in "$@"` keeps every arm green. That regression would wrongly refuse an honest pass declaring an index under a sibling's directory. The code is correct today.
- **Fix:** The finder's proposed fix was judged UNSOUND, so this is the skeptic's corrected fix.
  1. After B6, where ARCH-tRun-3 is admitted with `--writes work`, dispatch ARCH-tRun-4 with `--writes work/idx` in the same group.
  2. Assert `dispatch declared`, and miss `two passes claiming one file are not disjoint`.
  3. Confirm it goes red with line 14906 reverted to `"$@"`.
  4. Raise FLOOR_ASSERTIONS and FLOOR_SHARD_4 by the arm's count.
- **Left-shift gate:** Extend the `unattended kit gate` leg so that every condition with a skip carries a two-sided arm, one with the skipped path on this call's side and one with it on the sibling's side.

### M3 — no arm feeds TREE_SHAPE or BRANCH_SHAPE the characters they exist to block (id 8)

- **Where:** `tools/workflows/unattended-unit.js@c40c39fb:442` (TREE_SHAPE and BRANCH_SHAPE at 442-443), with the only fixture at `tools/workflows/unattended-build.test.sh@c40c39fb:1426`.
- **What:** T5 feeds only `a b` and `rel/w`. Those values fail on the space and on the missing absolute prefix, so the backtick, CR and LF exclusions are never exercised.
- **Consequence:** Loosening the CR, LF and backtick exclusion, or admitting a backtick into BRANCH_SHAPE, keeps T5 green. A worktree value that closes the code span with a backtick and appends an order of its own could then reach the main loop's instruction channel. The code is correct today.
- **Fix (judged SOUND by the skeptic):**
  - Add T5 fixtures that start with a valid absolute prefix but carry a backtick or a newline, such as `/w/a` followed by a backtick and `b`, and `/w/a\nb`.
  - Add a branch fixture carrying a backtick.
  - Assert `"worktree":""` and `"branch":""`, and assert that `nextAction` does not carry the raw value.
  - Observe each arm red against a TREE_SHAPE without the excluded class.

  Pair this with H1's tightening, since the new shape changes which characters the fixtures must name.
- **Left-shift gate:** Use the same hostile-string arm proposed under H1, in the `unattended-build self-test` leg.

### M4 — three `check_pass_tree_run` refusals have no arm (id 9)

- **Where:** `tools/unattended/pass-tree.sh@c40c39fb:85`, inside `check_pass_tree_run` (lines 76-94).
- **What:** Spec S2 says AC3 observes these refusals, but no arm reaches any of them:
  - a missing run-state file;
  - a LANDED or ABORTED run;
  - a run-state file naming no run branch (rc 2).

  `pass-tree.test.sh` writes RUN.md once, as `phase: BUILDING` with a run-branch, and T3 reaches only the other-branch refusal.
- **Consequence:** A regression could drop the LANDED/ABORTED case, or invert rc 2, and let `--merge` commit into a finished run's branch with the suite green.
- **Fix (judged SOUND by the skeptic):**
  1. In T3, rewrite RUN.md's phase to LANDED, then drop the run-branch line, then move the file away, restoring or committing after each.
  2. For each case, assert exit 1, one REFUSING line, and an unchanged HEAD and status, as `check_merge_refused` already does.
  3. Restore the file.
- **Left-shift gate:** Add a rule to the `harness arms (fail branches armed or pinned)` leg. Every `print_pass_tree_refusal` call site in `pass-tree.sh` must be matched by an arm that greps its text.

### M5 — no arm reaches any exit-2 path of `pass-tree.sh` (id 10)

- **Where:** `tools/unattended/pass-tree.sh@c40c39fb:270`. That is the usage refusals at lines 270-289, the slug-shape refusal at 292, and the unit-of-this-build refusal at 296-298.
- **What:** Every `run_tool` call in `pass-tree.test.sh` passes well-formed arguments and asserts rc 0 or 1.
- **Consequence:** Breaking the `[ "$mid" != "$slug" ]` test would let `--merge tRun --pass TOOL-other-3` write another build's unit id into the merge subject. That break, or one in the required-flag checks, would leave the suite green.
- **Fix (judged SOUND by the skeptic):** Add a usage arm covering each of these, and assert rc 2 and an unchanged HEAD for each:
  - a missing `--from`;
  - a duplicate `--branch`;
  - `--remove` carrying `--pass`;
  - a slug of `../x`;
  - `--pass TOOL-other-2` under slug `tRun`.
- **Left-shift gate:** Extend the `harness arms (fail branches armed or pinned)` leg so that every documented exit code of a kit tool is asserted by at least one arm.

### M6 — the stage-new-outputs loop after regeneration never runs in the suite (id 11)

- **Where:** `tools/unattended/pass-tree.sh@c40c39fb:224` (loop at 224-232, with `check_generated_output` at 230).
- **What:** The fixture's `render.sh` only rewrites the tracked `fx-out.txt` and `README.md`, so `ls-files --others` is always empty in T1. T4's untracked file is undone before line 224.
- **Consequence:** Dropping `check_generated_output` from line 230, or skipping the loop, goes unnoticed. A regen that creates a new generated file would then ship a merge commit without it, or with stray files staged.
- **Fix (judged SOUND by the skeptic):**
  - Have a fixture pass add a file under a second `[[generated]]` path that the render creates fresh, and assert that the merge commit's tree carries it.
  - Separately, have the render leave a non-generated scratch file, and assert that the NOTE names it and that the file is not in the commit.
- **Left-shift gate:** Extend the `unattended kit gate` leg so that `pass-tree.test.sh` includes a render that creates an untracked file, both generated and not, ensuring both arms of the loop run.

## LOW

### L1 — the AC6 `--check-commit` arm cannot fail for any `Pass: none` message (id 12)

- **Where:** `tools/unattended/pass-tree.test.sh@c40c39fb:175`.
- **What:** `check_commit_message` (`tools/unattended/unattended.sh@dba68e98:14309-14311`) returns 0 whenever the trailer reads `none`. The merge message always carries `Pass: none`, which the arm at line 164 already asserts. This arm repeats that check while being counted as AC6 evidence that the merge is admitted.
- **Consequence:** The arm misleads, with no effect on behaviour.
- **Fix:** The finder's alternative was judged UNSOUND, so this is the skeptic's corrected fix.
  - Drop the arm.
  - If a live-hook control is wanted, use a subject naming TOOL-tRun-4 or TOOL-tRun-7, which are dispatched with no pass commit yet during T1, with no Pass trailer. Assert exit 1 before reading the merge message's 0.
- **Left-shift gate:** Under the `harness arms (fail branches armed or pinned)` leg, require an admission arm to be paired with a negative control on the same fixture.

### L2 — no arm can tell which stream condition 1's note is printed on (id 15)

- **Where:** `tools/unattended/unattended.test.sh@c40c39fb:9541` (B1, and B2 at 9546). The `run()` helper at line 687 merges `2>&1`, and the note is at `tools/unattended/unattended.sh@dba68e98:14781`.
- **What:** Spec 3 AC2 says the note goes to stderr, never stdout, and lists "printed on stdout" as a red condition. Only the pass's one-off probe observed this.
- **Consequence:** Dropping the note's `>&2` would put it on the driver's stdout, which callers parse, and every arm would stay green. Behaviour is correct today.
- **Fix (judged SOUND by the skeptic):**
  1. In B1, capture stdout alone (`out=$(run_main_at_head run_driver --dispatch ... 2>/dev/null)`).
  2. Miss `so condition 1 leaves them out of the sibling comparison` on that stdout.
  3. Observe the arm red with `>&2` dropped.
  4. Raise FLOOR_ASSERTIONS and FLOOR_SHARD_4 by one each.
- **Left-shift gate:** Extend the `unattended kit gate` leg so that a spec acceptance criterion naming a stream is observed by an arm that captures that stream alone.

review-shape kind=diff-review round=1 intensity=full at=synth raw=15 confirmed=14 refuted=0 merged=1 unverified=0 blocker=0 high=3 medium=8 low=3 agents=11 out-tokens=80191
review-round round=1 limit=- prior=- count=3 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/unattended-unit.js@1094ea03:442 | high | high | confirmed | tools/workflows/unattended-unit.js@1094ea03:442 is `TREE_SHAPE = /^(\/\|[A-Za-z]:[\\/])[^\r\n`]*$/`. It refuses only CR, LF and backtick, so `$(...)`, `"`, `;` and `..` segments pass. ownTree (line 445) is then spliced into nextAction as 'with its working directory at `<ownTree>`' (lines 480-482). Spec TOOL-aTwinnedPass-1 line 616 names BRANCH_SHAPE and TREE_SHAPE as the answer to agent-output-interpolated-into-an-instruction. The sibling template already refuses `..` for `scratch` and `repo` at tools/workflows/unattended-build.template.js@cc868b60:311. The check stops the value breaking out of the code span, but not shell expansion or traversal once the main loop runs a cd into that path. The path needs a misbehaving or injected builder, so it is narrow, but the consequence is a security hole, which grades it high. | sound | - | class:agent-output-interpolated-into-an-instruction |
| 2 | security | tools/unattended/pass-tree.sh@def02e16:152 | high | high | confirmed | check_pass_branch (tools/unattended/pass-tree.sh@def02e16:98-114) checks three things only: check-ref-format, that the name does not start with '-', and that it is not the run's own branch. cmd_remove_tree (around lines 255-268) adds just the check that no commit is unique to the branch. remove_pass_tree (150-158) then runs `git worktree remove --force` on whatever worktree derive_holder_where finds holding that branch, followed by `branch -D`. Nothing confines either one to a worktree-agent-* branch or to a .claude/worktrees/agent-* holder. The --branch value is the builder's returned branch, and BRANCH_SHAPE (tools/workflows/unattended-unit.js@1094ea03:443) admits any branch name. So another worktree on a fully pushed branch would be force-removed with its uncommitted files. That is data loss on a narrow path, which grades it high. | unsound | - | class:destructive-step-before-its-precondition |
| 3 | correctness | tools/workflows/unattended-build.test.sh@064bace0:1417:1417 | high | medium | confirmed | tools/workflows/unattended-build.test.sh@064bace0:1417 asserts that 'OWN WORKTREE' is absent. A grep finds that string nowhere in unattended-unit.js; the paragraph at tools/workflows/unattended-unit.js@1094ea03:339 reads 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN'. So the arm passes whatever childU or childA contain, and it certifies an absence it never tests. The sibling arms in the same loop, no 'isolation:' and no '"branch"', still check something, so the effect is contained to this arm: medium. | sound | - | class:fixture-passes-by-finding-nothing |
| 4 | correctness | tools/unattended/pass-tree.sh@def02e16:179:179 | low | - | refuted | duplicate of id=5. It is the same mismatch between tools/unattended/pass-tree.sh@def02e16:179 ({7,40}) and tools/workflows/unattended-unit.js@1094ea03:178 COMMIT_SHAPE ({7,64}) on the same passBase-to---from handoff. | sound | - | - |
| 5 | seams | tools/unattended/pass-tree.sh@def02e16:179 | medium | low | confirmed | Confirmed by reading both files. tools/unattended/pass-tree.sh@def02e16:179 tests `$4 =~ ^[0-9a-f]{7,40}$`, and its refusal text says '7 to 40'. tools/workflows/unattended-unit.js@1094ea03:178 has COMMIT_SHAPE = /^[0-9a-f]{7,64}$/, and line 182 uses it to accept passBase. COMMIT_SHAPE existed at the base, but using it for passBase is new in this diff, and pass-tree.sh is new, so the diff introduced the mismatch. In a SHA-1 repo a 41-64 digit value already fails the builder's git reset, so the only reachable case is a SHA-256 repo where the main loop passes the full rev-parse output. There the merge is refused with a clear message and nothing is written. Nothing comes out wrong and no data is lost, so the effect is contained. Spec-2 lines 51 and 223 carry the same 40-digit limit and would need the same edit. | sound | - | class:two-guards-one-question-two-answers |
| 6 | verification | tools/workflows/unattended-build.test.sh@064bace0:1417 | high | medium | confirmed | Line 1417 checks `hasnt_ ... 'OWN WORKTREE'`. The paragraph at tools/workflows/unattended-unit.js@1094ea03:339 reads 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN', and the log line at :419 reads 'own worktree from'. Neither contains the case-sensitive substring 'OWN WORKTREE', and hasnt_ at line 278 is a case-sensitive glob, so this arm can never fail. For childA, the T2 'same' comparison would still catch the paragraph leaking into the default prompt. For childU, the unattended default, nothing would. One vacuous arm in a suite, with the attended side still covered by another check, is a contained effect, so I grade it medium. Checking for 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN', the string T1 already uses as its positive control, fixes it. | sound | liveness-negative-from-another-population | class:fixture-passes-by-finding-nothing |
| 7 | verification | tools/unattended/unattended.sh@dba68e98:14906 | medium | medium | confirmed | I read tools/unattended/unattended.sh@dba68e98:14903-14917 and the block of new arms at tools/unattended/unattended.test.sh@c188e38f:9530-9555. B2 has the own path work/idx facing a sibling's work/idx, which the inner check_generated_output skip catches whichever list the outer loop reads, and lane/two overlaps nothing. B6's own path is `work`, which is not generated, so it is compared either way. No arm has this call declaring a covered path under a sibling's directory claim. That is the one case where `for p in "$@"` and `for p in $_c1_own` differ: overlaps(work/idx, work) is true, so "$@" refuses and _c1_own admits. Reverting line 14906 leaves the suite green. The effect is limited to a missing test: the code is correct today. | unsound | - | class:containment-tested-one-way |
| 8 | verification | tools/workflows/unattended-unit.js@1094ea03:442 | medium | medium | confirmed | TREE_SHAPE /^(\/\|[A-Za-z]:[\\/])[^\r\n`]*$/ and BRANCH_SHAPE sit at tools/workflows/unattended-unit.js@1094ea03:442-443. ownTree is spliced into nextAction inside backticks at line ~481. The only T5 fixture (tools/workflows/unattended-build.test.sh@064bace0:1426) gives branch 'a b' and worktree 'rel/w'. 'rel/w' fails on its missing absolute prefix and 'a b' fails on its space, so loosening the [^\r\n`] exclusion, or admitting a backtick in BRANCH_SHAPE, keeps T5 green. No arm exercises the injection characters these shapes exist to block. The code is correct today, so the gap is contained to the test. | sound | agent-output-interpolated-into-an-instruction | class:agent-output-interpolated-into-an-instruction |
| 9 | verification | tools/unattended/pass-tree.sh@def02e16:85 | medium | medium | confirmed | check_pass_tree_run (tools/unattended/pass-tree.sh@def02e16:76-94) has four refusals: a missing file, LANDED/ABORTED, rc 2 (no run branch), and the other-branch case. pass-tree.test.sh writes RUN.md only once, as 'phase: BUILDING' with run-branch (line 131), and never removes or rewrites it. Of the four, T3 reaches only the other-branch refusal (line 205); a grep for LANDED, ABORTED, 'no run-state file' or 'names no run branch' in the suite finds nothing. Spec S2 says these refusals are observed by AC3, yet none of them is. A regression in any of the three would stay green. The effect is limited to a missing test. | sound | - | class:observed-by-claim-no-arm-discharges |
| 10 | verification | tools/unattended/pass-tree.sh@def02e16:270 | medium | medium | confirmed | main() in pass-tree.sh has exit-2 paths for usage refusals (lines 270-289), check_slug_shape (292) and the unit-of-build check (296-298). Every run_tool call in pass-tree.test.sh (147, 155, 180, 198, 231, 240, 245, 249, 254) passes well-formed arguments and asserts rc 0 or 1. No arm asserts rc 2, so breaking the `$mid != $slug` test or the required-flag checks would leave the suite green. The gap is in test coverage only and the tool's behaviour is unaffected, so medium. | sound | - | class:rule-stated-with-no-check-that-fails |
| 11 | verification | tools/unattended/pass-tree.sh@def02e16:224 | medium | medium | confirmed | The fixture's render.sh writes only fx-out.txt and README.md. Both are tracked from the base commit, so after regen `ls-files --others --exclude-standard` returns nothing in T1. The loop at 228-232 and its check_generated_output branch never run. The only arm that creates an untracked file is T4, where fx-partial.txt is written and the regen fails, and that path undoes the merge before line 224. If line 230 dropped check_generated_output, no arm would go red. Contained to coverage, so medium. | sound | - | new:fixture-never-drives-the-branch-under-test |
| 12 | verification | tools/unattended/pass-tree.test.sh@e00f17f5:175 | low | low | confirmed | check_commit_message (tools/unattended/unattended.sh@dba68e98:14309) returns 0 whenever the parsed Pass trailer contains `none`, and the merge message pass-tree.sh writes always carries `Pass: none`. Line 164 already asserts that trailer. The arm at 174-175 therefore cannot fail for this message, yet it is labelled as AC6 evidence. It is a misleading test with no effect on behaviour, so low. The fix's first option, dropping the arm, is sound. Its alternative negative control, a subject naming TOOL-tRun-2 with no trailer, would not exit 1 at that point. check_pass_open (14227) finds P2 as pass 2's pass commit, and P2 wrote its declared p2.txt, so the pass reads closed. P2 is not HEAD either, so no `o` row exists for TOOL-tRun-2 and the hook returns 0. A unit that is dispatched and has no pass commit yet in T1 is needed instead. | unsound | liveness-negative-from-another-population | class:criterion-asserts-what-its-own-command-cannot-show |
| 13 | intent | tools/workflows/unattended-build.test.sh@064bace0:1417 | high | high | confirmed | The claim holds. tools/workflows/unattended-build.test.sh@064bace0:1417 checks the needle 'OWN WORKTREE', and that string appears nowhere in unattended-unit.js. The paragraph it should catch is emitted at line 339 and reads 'THIS PASS BUILDS IN A WORKTREE OF ITS OWN'; the log line at line 419 says 'own worktree from' in lowercase. The only other place 'OWN WORKTREE' appears is spec 1 line 340. So the T3 arm passes whether or not the paragraph is in the default prompts, which means a check certifies something it never tests. I graded it high, not blocker, because other arms still give partial cover: T1 is a positive control, and T2 compares the default attended prompt with the passBase prompt after the paragraph is removed. | sound | observed-by-claim-no-arm-discharges | class:fixture-passes-by-finding-nothing |
| 14 | intent | tools/unattended/pass-tree.sh@def02e16:179 | medium | medium | confirmed | The claim holds. tools/unattended/pass-tree.sh@def02e16:179 refuses any --from that does not match ^[0-9a-f]{7,40}$, and its refusal text at line 181 says the same. The harness's COMMIT_SHAPE at tools/workflows/unattended-unit.js@1094ea03:178 accepts 7 to 64 hex digits, and the header at tools/unattended/pass-tree.sh@def02e16:23 tells the main loop to pass 'the same sha' to both. In a SHA-256 repository a full 64-digit passBase is accepted by the harness and then refused by --merge. The effect is contained: the main loop can still pass an abbreviation of 40 digits or fewer by hand, and nothing is lost. | sound | - | class:two-guards-one-question-two-answers |
| 15 | intent | tools/unattended/unattended.test.sh@c188e38f:9541 | low | low | confirmed | The claim holds. run() at tools/unattended/unattended.test.sh@c188e38f:687 merges stderr into stdout with 2>&1, so arms B1 and B2 cannot tell which stream the note is on. The note at tools/unattended/unattended.sh@dba68e98:14781 does go to stderr today through >&2, but no suite arm would turn red if that >&2 were dropped. Behaviour is correct now; this is a coverage gap only. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |

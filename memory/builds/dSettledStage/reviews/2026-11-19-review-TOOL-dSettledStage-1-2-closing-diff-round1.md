**Serves:** diff-review TOOL-dSettledStage-1 TOOL-dSettledStage-2

# Closing diff review, round 1: dSettledStage's cumulative diff landing on main, units 1 and 2

Node `d` · 2026-11-19 · Tier-2 · on `branch/elated-morse-1a3bcc` · adversarial fan through `tier2-review.js`: 5 finder lenses (`gov-diff-reviewer`), then 5 skeptic batches (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The range adds the lander's `write_staged_change` helper and its callers in `tools/push-main.sh` with arms 42 and 43 in `tools/push-main.test.sh` (TOOL-dSettledStage-1). It also adds `sh_hygiene.py --stage-commits` and its leg `shell hygiene (a stage committed with no staged-diff test)` (TOOL-dSettledStage-2), plus the build's specs and records.

**Reviewed range:** `12764ec2133f0f40a250dbec3d5503b8d746c7fe...41e57fca5d8c8659457c7353d2dd00151830e698`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker.
One defect is HIGH: `write_staged_change` ignores a failed `git add -A` and answers "nothing staged", so the lander silently skips its mint, gov-first and regen commits and its merge fold (ids 1, 3, 5).
Three lenses reported that defect, and it needs one fix.
The other MEDIUM defects are all in the new `--stage-commits` scan.
It reads a quoted `$( … )`'s `)` as the end of a verb's arguments (id 4).
It leaves out a commit spelled behind a global git option other than `-c`/`-C`, and does not state that boundary (id 8).
It follows stagers only one hop (id 9).
The LOW defects are arm 43's missing liveness markers (ids 2, 6) and the spec's unkept promise to add the new leg to §7's Gates line (id 10).

## Review shape

- Intensity full. Raw 10, confirmed 9, refuted 1, merged 0, unverified 0 (0 uncertain). Precision 0.90.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 1 HIGH, 3 MEDIUM, 2 LOW, which is 6 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 1 HIGH (id 5), 5 MEDIUM (ids 1, 3, 4, 8, 9), 3 LOW (ids 2, 6, 10), which is 9 findings.
- Every confirmed finding keeps its binding grade.
- Item 1 holds one HIGH and two MEDIUM findings on one defect, so it ranks HIGH.
- Intent input: neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages.
- Checklist: 50 items, acquired by the harness from `--for-diff 12764ec2133f0f40a250dbec3d5503b8d746c7fe..HEAD`, each assigned to exactly one of 5 lenses (security 10, correctness 10, seams 10, verification 10, intent 10).
- By design: none supplied, with no caller byDesign and a block of 0.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 5 judged sound (ids 2, 4, 6, 9, 10), 0 judged UNSOUND, 4 judged INSTANCE-ONLY (ids 1, 3, 5, 8), 0 with no fix proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so this report gives the skeptic's class-level fix for each.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 1 (id 7). Same-address pairs shown: 0.
- Id 7 is not a twin of any confirmed finding: it concerns arm 42's unguarded `$_py_arms` call, a different defect from arm 43's missing liveness markers.
- Dispositions: unclassed refuse; 50 class slugs handed; 199 leg names read from `tools/gate-legs.json`.
- Every counter above is zero where it must be zero, so this run is complete within the generic brief and the commit messages.
- Coverage is limited to what those inputs let the lenses hunt.

## Items

### 1. HIGH: `write_staged_change` reads a failed `git add -A` as "nothing staged" (ids 5 HIGH, 1 MEDIUM, 3 MEDIUM)

- **Where:** `tools/push-main.sh@f8e4540d:987`, the helper body at lines 985-990, its three attended callers at lines 1361, 1385 and 1408, and `write_merge_fold` at line 1081.
- **What is wrong:** the helper runs `git add -A` and never reads its exit status, then answers 1 when `git diff --cached --quiet` passes.
- When staging fails (a held `.git/index.lock`, an unreadable file, an I/O error), the index still equals HEAD, so the helper answers 1, its answer for a clean tree.
- The script runs under `set -u` alone, and the helper is called inside `if` conditions, so nothing stops on the failed add.
- **Consequence:** the mint, gov-first and regen callers skip their commit without a word and go on to the bar and `git push` at line 1427, with the minted versions, receipts or regenerated outputs left uncommitted.
- `write_merge_fold`'s `write_staged_change || return 0` reports "the tree was HEAD's", so `--prepare` reports a merge prepared without its fold.
- At the base 12764ec2, the commit that followed a failed add failed too, and the lander aborted with its own "Aborted (no push)" line, so this diff introduced the regression.
- The only backstop is `.githooks/pre-push`'s dirty-tree refusal, which runs later and names the wrong cause.
- Without that hook, the push lands without the outputs the lander owes.
- Three probes reproduced it: in a scratch repo with a planted `.git/index.lock`, the helper printed git's fatal lock error and returned rc=1, and `git status --porcelain` still showed the change.
- **Grades:** id 5 is HIGH, because the push goes ahead with no dirty-tree check between the regen block and line 1427. Ids 1 and 3 are MEDIUM, because they weigh the downstream pre-push refusal as containment. All three keep their binding grades.
- **Fix (all three judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** give `write_staged_change` a third answer for a failed stage, `git add -A || return 2`, and make every caller refuse on 2.
- Each attended site becomes `write_staged_change; rc=$?; [ $rc -eq 2 ] && { echo "...could not stage... Aborted (no push)"; exit 1; }; [ $rc -eq 0 ] && <commit>`, each with its own stage's line.
- `write_merge_fold` becomes `write_staged_change; case $? in 1) return 0;; 2) return 1;; esac`, so a failed stage refuses instead of folding.
- Do not rely on the caller's later `git commit` or `commit-tree` to fail.
- Add a `push-main.test.sh` arm that holds `.git/index.lock` after a real change and asserts both refusals: the landing aborts with no push, and `write_merge_fold` returns 1.
- The finders proposed `git add -A || return 0`, so the caller's own commit refuses loudly. That cures the cited instance alone and leaves the class standing.
- **Left-shift gate:** extend `sh_hygiene.py --stage-commits` (leg `shell hygiene (a stage committed with no staged-diff test)`) to red a `git add` whose exit status a stager function never reads. The index.lock arm above then pins the lander's own instance in `push-main self-test`.

### 2. MEDIUM: `read_stage_events` ends a verb's arguments at a quoted substitution's `)` (id 4 MEDIUM)

- **Where:** `tools/gate-lint/sh_hygiene.py@19e87517:1326`, `read_stage_events`, new in this diff.
- **What is wrong:** it searches `[;&|)]` for the end of the arguments on `build_blanked(code, keep_substitutions=True)`, which leaves a quoted `$( … )` as code.
- The `)` that closes the substitution is therefore read as the end of the arguments, and every flag after it is lost.
- This contradicts the docstring, which says the arguments run to the next unquoted `)`.
- **Consequence:** `git add -A` followed by `git commit -q -m "$(date)" --allow-empty` reads unchecked=1, empty-ok=0, while the same flags in the other order read empty-ok=1.
- `git add -A` followed by `git diff "$(echo x)" --cached --quiet || git commit -m x` reads unchecked=1, admitted=0, because `--cached` was dropped.
- The leg reds correctly guarded code and forces a registry row whose stated reason is false.
- It never misses a real unchecked commit, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** find the end of the arguments on a blank that skips a balanced `$( … )` as a unit.
- For example, walk `blank[verb_end:]` with `read_substitution` so that a `$(` jumps past its matching `)`, or search `build_blanked(code)` without `keep_substitutions` for the terminator.
- Add the two probe inputs above as `stage_cases` rows, expecting (0,0,0,1) and (0,1,0,0).
- **Left-shift gate:** the `shell-hygiene selftest` leg carries those rows, plus one quoted-substitution row ahead of a load-bearing flag for every scan that reads a `keep_substitutions` blank.

### 3. MEDIUM: `STAGE_EVENT` leaves out a git verb behind any global option other than `-c`/`-C`, and states no boundary for it (id 8 MEDIUM)

- **Where:** `tools/gate-lint/sh_hygiene.py@19e87517:1273`, `STAGE_EVENT`.
- **What is wrong:** the regex accepts only `-c <word>` and `-C <word>` between `git` and the verb.
- `git --git-dir=.git commit`, `git --no-pager commit` and `git --work-tree=x commit` are never counted.
- That miss is not a `STAGE_BOUNDARY` row, and neither `run_stage_scan`'s docstring nor the README's `--stage-commits` section names it, though spec S3 promises one docstring entry per boundary row.
- **Consequence:** `git --git-dir=.git add -A` then `git --git-dir=.git commit -q -m x` scans as all zeros, and so does `git add -A` then `git --no-pager commit -q -m x`.
- A future site spelled this way passes the leg green with no stated boundary, which defeats spec 2 §1's goal that the next such site reds.
- The product tree has no such spelling today, so the miss is latent.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** do both halves.
- Widen the prefix to every global-option spelling git accepts before the verb: `-c <w>`, `-C <w>`, `-p`, `-P`, `--<opt>`, `--<opt>=<w>`, and the separate-argument forms `--git-dir <w>`, `--work-tree <w>`, `--namespace <w>` and `--exec-path <w>`.
- Add fixture rows for `git --git-dir=x commit`, `git --no-pager commit` and `git -p commit`.
- Add a `STAGE_BOUNDARY` row for any prefix the regex still leaves unread, and name it in the `run_stage_scan` docstring and the README `--stage-commits` section.
- Raise `FLOOR_ASSERTIONS` by the number of new arms.
- Re-measure `memory/project/stage-commit-sites.txt` after widening, because the existing `git --git-dir=... commit-tree` test sites become events.
- The finder proposed either widening to `--<opt>[=<word>]` or adding a boundary row. The widening alone cures only the cited spellings and still misses `-p`/`-P` and the space-separated forms.
- **Left-shift gate:** the `shell-hygiene selftest` boundary arm asserts one fixture per git global-option form, each either counted or matched to a `STAGE_BOUNDARY` row.

### 4. MEDIUM: `read_stage_helpers` follows stagers one hop, so a same-file wrapper hides an unchecked commit (id 9 MEDIUM)

- **Where:** `tools/gate-lint/sh_hygiene.py@19e87517:1334`, `read_stage_helpers` (lines 1334-1352).
- **What is wrong:** a function counts as a stager only when its own body holds an `add` event, and a call to another stager is never counted.
- A commit after a call to a wrapper of an unchecked stager reads `unpaired`, which is never gated, instead of `unchecked`.
- The documented "a stage in another scope" boundary is a different shape: there the commit's scope never calls the stager.
- **Consequence:** `s1() { git add -A; }`, `s2() { s1; }`, `s2`, `git commit -q -m x` scans as unchecked [] and unpaired [(4, 'git commit -q -m x')], so the leg stays green.
- Unpaired sites are still printed, and the miss needs a two-level helper shape, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** close the helper set transitively by iterating `read_stage_helpers` until it stops changing.
- Treat a call to a stager as a stage, and a call to a checked stager as a stage then a test.
- Add a selftest fixture for the two-hop wrapper, expecting 1 unchecked.
- If one hop is intended instead, add a `STAGE_BOUNDARY` row ("a stager called through another same-file function", class unpaired) and name it in the docstring and the README.
- **Left-shift gate:** the two-hop fixture in the `shell-hygiene selftest` leg.

### 5. LOW: arm 43's line-ending half never checks that its fixture produced the shape it tests (ids 2 LOW, 6 LOW)

- **Where:** `tools/push-main.test.sh@a4ace06a:1709`, arm 43 (lines 1693-1720), want list at line 1717.
- **What is wrong:** the arm asserts only `eol-rc=0`, `eol-head=same`, `real-rc=0` and `real-moved=1`.
- It never echoes that status reports `f.txt` dirty, or that the stage comes out empty, before `write_merge_fold` runs.
- Arm 42 guards the same shape with `eol-dirty=1` and `eol-empty=1` (lines 1237-1246).
- **Consequence:** if the CRLF checkout does not happen, status is clean and both the base fold and the new helper return 0 with HEAD unchanged.
- That happens when `GIT_CONFIG_VALUE_0=true` does not take (for example on a git older than 2.31 that ignores `GIT_CONFIG_COUNT`), or when a git version, platform or config reads the rewritten file as clean.
- The half then passes on both the base and the built lander, and its "red at the base lander 12764ec2" claim goes unobserved.
- A probe shows it is red at the base today, so this is a test-adequacy gap with no runtime effect.
- **Fix (both judged SOUND by the skeptic):** before calling `write_merge_fold`, add arm 42's liveness echoes.
- After the LF rewrite, add `[ -n "$(git status --porcelain -- f.txt)" ] && echo eol-dirty=1`.
- Add a stage-empty check, for example `git add -A; git diff --cached --quiet && echo eol-empty=1; git reset -q`, and re-dirty the file afterwards.
- Add `eol-dirty=1` and `eol-empty=1` to the `w43` want list, so the half reds when the shape is absent.
- **Left-shift gate:** the `harness arms (fail branches armed or pinned)` leg could require a shape-liveness marker in the want list of every arm whose comment claims "red at the base". Where that does not fit, it becomes a bug-class checklist entry under `fixture-passes-by-finding-nothing`.

### 6. LOW: spec 2 §7 promises a revision that adds the new leg to its Gates line, and the spec closed without it (id 10 LOW)

- **Where:** `memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md@2a72eb4c:400`, with the Gates line at :394.
- **What is wrong:** §7 says `shell hygiene (a stage committed with no staged-diff test)` joins the Gates line "in a revision once its manifest row exists".
- Commit 6dee50847 adds that row (`tools/gate-legs.json@833ffdfb:245`), and the spec reads `CLOSED · rev-2`.
- The Gates line still leaves the leg out, and the revision log has no rev-3.
- **Consequence:** a reader driving the close from §7 skips the leg whose red and green the acceptance ledger owes.
- The bar reads `gate-legs.json`, so the gap is in a document only.
- **Fix (judged SOUND by the skeptic):** add the leg's name to §7's Gates line with a rev-3 revision-log entry, or reword §7 so it no longer promises a revision.
- **Left-shift gate:** `spec tokens (the pass's own spec)` could red a CLOSED spec whose §7 Gates line leaves out a leg its unit's commits added to `tools/gate-legs.json`.

review-shape kind=diff-review round=1 intensity=full at=synth raw=10 confirmed=9 refuted=1 merged=0 unverified=0 blocker=0 high=1 medium=5 low=3 agents=11 out-tokens=69125 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=1 state=CONVERGING
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/push-main.sh@f8e4540d:987 | medium | medium | confirmed | Observed at tools/push-main.sh@f8e4540d:985-990: write_staged_change runs `git add -A` with its status unchecked, then `git diff --cached --quiet && return 1`. The script uses only `set -u` (line 68), and the helper is called inside `if` conditions anyway, so nothing stops on a failed add. If the add fails, the index still equals HEAD and the helper answers 1. At the base (12764ec2:1345/1370/1394) a dirty status went straight to `git add -A; git commit`, and that commit then failed loudly with its 'Aborted (no push)' line. The mint, gov-first and regen callers (1361/1385/1408) now skip their commit silently. write_merge_fold (1081) maps 1 to `return 0`, so the fold is skipped too. The diff introduced this regression. It is reachable only when staging fails (index.lock held, I/O error), which is a narrow path, and the pre-push dirty-tree check still blocks it downstream. So the effect is contained: medium. | instance | - | new:failed-stage-reads-as-nothing-staged |
| 2 | security | tools/push-main.test.sh@a4ace06a:1709 | low | low | confirmed | Observed at tools/push-main.test.sh@a4ace06a:1693-1720: arm 43 sets GIT_CONFIG_VALUE_0=true, which relies on line 197 exporting GIT_CONFIG_COUNT/KEY_0=core.autocrlf. It re-checks out f.txt and rewrites it as LF, but never asserts that f.txt then shows as dirty. The required list at 1717 is only eol-rc=0, eol-head=same, real-rc=0, real-moved=1. The base write_merge_fold (12764ec2:1063) starts with `[ -n "$(git status --porcelain ...)" ] \|\| return 0`. So if the CRLF checkout does not happen (for example a git older than 2.31 that ignores GIT_CONFIG_COUNT), status is clean and the base also yields eol-rc=0 and eol-head=same. The arm's 'red at the base' claim then goes unobserved. Arm 42 does carry the eol-dirty=1 and eol-empty=1 liveness markers (1237-1246). This is a test-adequacy gap with no runtime effect: low. | sound | fixture-passes-by-finding-nothing | class:fixture-passes-by-finding-nothing |
| 3 | correctness | tools/push-main.sh@f8e4540d:987 | medium | medium | confirmed | At tools/push-main.sh@f8e4540d:985-990, write_staged_change runs `git add -A` and does not check its exit status, then returns 1 when `git diff --cached --quiet` passes. I ran the function body in a scratch repo with a modified tracked file and .git/index.lock present. git printed its fatal lock error, the function returned rc=1, and status still showed ` M f`. All three attended callers (lines 1361, 1385, 1408) then skip their commit without a word. The base (12764ec21 lines 1344-1351, 1369-1376, 1393-1400) ran `git commit` after the add, which failed on the same lock and refused with its own line, so this change introduced the regression. In write_merge_fold, the lock case returns 0 ('the tree was HEAD's') where the base's write-tree/commit-tree would have failed and refused. The effect is contained: the landing goes on with an uncommitted tree, and pre-push's dirty-tree refusal is a later backstop. | instance | - | new:failed-stage-reads-as-nothing-staged |
| 4 | correctness | tools/gate-lint/sh_hygiene.py@19e87517:1326 | medium | medium | confirmed | read_stage_events is new in this diff (the base sh_hygiene.py has no read_stage_events). It searches `[;&\|)]` on build_blanked(code, keep_substitutions=True), which leaves a quoted `$( … )` as code, so that substitution's `)` ends the arguments. I imported the module and re-ran the probes. `git add -A\ngit commit -q -m "$(date)" --allow-empty` gave unchecked=1, empty-ok=0. The same flags in the other order gave empty-ok=1. `git add -A\ngit diff "$(echo x)" --cached --quiet \|\| git commit -m x` gave unchecked=1, admitted=0. This contradicts the docstring's 'next unquoted ... )'. The effect is a false red that forces a registry row with a false reason. The gate never misses a real unchecked commit, so the effect is contained. | sound | - | new:quoted-substitution-paren-read-as-a-terminator |
| 5 | seams | tools/push-main.sh@f8e4540d:987 | high | high | confirmed | At tools/push-main.sh@f8e4540d:985-990, write_staged_change runs a bare `git add -A` and then `git diff --cached --quiet && return 1`. If the add fails, the index still equals HEAD, so the helper returns 1, the same answer it gives for a clean tree. Its three attended callers (lines 1361, 1385, 1408) then skip their commit without a message and reach `git push` at line 1427. Nothing between the regen block and the push checks for a dirty tree. At the base 12764ec2, those sites ran `git add -A` and then `if ! git commit ...; then ... Aborted (no push)`, so a lock failure in add was followed by a failing commit and a loud abort. The diff introduced this regression. It needs a staging failure such as a stale index.lock, which is a narrow path, so it is high. | instance | - | new:failed-stage-reads-as-nothing-staged |
| 6 | verification | tools/push-main.test.sh@a4ace06a:1709 | low | low | confirmed | Arm 43 (tools/push-main.test.sh, around lines 1693-1720) asserts only eol-rc=0, eol-head=same, real-rc=0 and real-moved=1. Nothing echoes that status reported f.txt dirty, or that the stage came out empty, before the fold runs. Arm 42 does both at lines 1237-1238 and lists eol-dirty=1 and eol-empty=1 in its want list at line 1246. If status ever reads the re-written file as clean, the line-ending half of arm 43 passes vacuously on both the base and the built lander. The effect is limited to test coverage, so it is low. | sound | - | class:fixture-passes-by-finding-nothing |
| 7 | verification | tools/push-main.test.sh@a4ace06a:1236 | low | - | refuted | Arm 42 is new in this diff, and it does call "$_py_arms" at tools/push-main.test.sh@a4ace06a:1236 without a guard. The claimed consequence, a false red where the suite would otherwise print a skip, does not hold. (1) The arm guarded in the 'same way' is arm 33 (line 1264), and with no launcher it prints `bad "33 no python launcher runs..."`, a red, not a skip. (2) Arms 28-32 sit in the same `if [ -n "$_rg_k" ]` block (line 1130) and have no python guard either. With no launcher, the lander's run_regen prints 'generated outputs were NOT regenerated — no usable python launcher' (tools/push-main.sh@f8e4540d:922), so arm 28's stale index is never restored and it reds too. (3) Arm 42 needs rc=0, landed=1 and 'gating + pushing', and the lander's bar cannot run without python, so the arm reds on that host whether or not it is guarded. Arm 42 behaves exactly like its block siblings on such a host. The only true part is that the line-1108 comment does not list 42 among the arms using the shared interpreter, which is a comment omission with no effect on behaviour. | unsound | - | - |
| 8 | intent | tools/gate-lint/sh_hygiene.py@19e87517:1273 | medium | medium | confirmed | The widening option as written (`--<opt>[=<word>]`) still misses `-p`/`-P` and the space-separated `--git-dir <path>` forms, so it leaves members of the same class unread and unstated. Only the boundary-row option states the whole class. The fix offers the two as alternatives, so taking the widening option alone cures only the cited spellings. | instance | - | new:gate-misses-a-spelling-its-boundary-never-names |
| 9 | intent | tools/gate-lint/sh_hygiene.py@19e87517:1334 | medium | medium | confirmed | read_stage_helpers (tools/gate-lint/sh_hygiene.py@19e87517:1334-1352) marks a function as a stager only when read_stage_events finds an `add` event in its own body. A call to another stager is never counted, so stagers are followed exactly one hop. I re-ran the probe: scan_stage_file on 's1() { git add -A; }\ns2() { s1; }\ns2\ngit commit -q -m x' returned unchecked [] and unpaired [(4, 'git commit -q -m x')]. STAGE_BOUNDARY (:1290-1302), run_stage_scan's docstring and the README's --stage-commits section (:232) list only 'a stage in another scope', described as 'a function the commit's scope does not call', plus a sourced library and -a. None of them covers a same-file wrapper that the commit's scope does call. The --stage-commits mode is new in this range (6dee50847), so the diff introduced the miss. Medium, not higher: unpaired sites are still printed, and the miss needs a two-level helper shape. | sound | - | new:helper-closure-stops-at-one-hop |
| 10 | intent | memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-2.md:400 | low | low | confirmed | The spec's §7 Gates line still leaves out `shell hygiene (a stage committed with no staged-diff test)`, and the paragraph under it says that leg 'joins this line in a revision once its manifest row exists'. tools/gate-legs.json@833ffdfb:245 now holds that row. Yet the spec header reads 'CLOSED · rev-2', and the revision log stops at rev-2 with no entry adding the leg. The spec promises a revision it never made. The effect is on a document only: the bar itself reads gate-legs.json, so this is low. | sound | - | class:amendment-leaves-its-other-half-standing |

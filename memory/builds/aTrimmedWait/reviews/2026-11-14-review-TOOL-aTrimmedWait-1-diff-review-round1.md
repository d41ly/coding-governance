**Serves:** diff-review TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7

# aTrimmedWait — Tier-2 diff review of TOOL-aTrimmedWait-1..7, round 1

*2026-11-14. Seven units of build aTrimmedWait (`memory/builds/aTrimmedWait/README.md`, brief `memory/builds/aTrimmedWait/prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md`) that cut the time builds spend waiting on checks, renders and polls: `--check-specs` spec-file refusals (unit 1), hygiene check 12 scoped to one `--spec` or `--build` (unit 2), the pre-commit hook's staged render under `STAGED_RENDER` (unit 3), `--write` skipping unmoved artifacts (unit 4), one batched `git hash-object --stdin-paths` call (unit 5), scratch-guard's polling-wait refusal and G3's `-o` cluster reading (unit 6), and the per-transcript session-call cache in `handoff.py agents` (unit 7). The build rule: no refusal, red or green moves, except unit 6's polling rows. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 7 spec documents supplied as `specs`, beside the range's commit messages. By design: 1 invariant from the checklist's by-design block. The known item, unit 3's realpath comparison where spec §4 says abspath, was weighed and not re-raised by any finding.*

**Range reviewed: `846d51d39de6bd14174032a338234604273afd8d...72dc239162a8e283e8e0620164f2bec26453e29f`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER or HIGH. Seven MEDIUM items and two LOW items stand.

No item moves a verdict outside the intended polling class. Every behavioural item fails safe: the commit is refused or the agent is refused, and nothing wrong is committed.

Two behavioural defects sit in `--write-staged` (M1, L1): a staged decline can leave the worktree or the index changed, which breaks spec 3's "writing nothing" contract. One sits in the new polling class (M2): a short `sleep` carrying a shell comment is refused.

The other six items are verification gaps: a code path the build added can regress while every gate stays green.

No reviewer ran a gate. Every statement about a leg's colour is judged from source or from a read-only probe.

## Review shape

Intensity full, raw 12, confirmed 10, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.83.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| seams | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| verification | yes | 6 | 6 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 9 items (0 blocker, 0 high, 7 medium, 2 low).
Adjudicated tally by raw confirmed finding: 10 (0 blocker, 0 high, 8 medium, 2 low).
One synthesis merge accounts for the difference: findings 4 and 12 are one defect (M1).
Every finding keeps its binding grade; no grade was changed in synthesis.
No twin flag is raised. Refuted finding 5 shares an address with findings 1 and 8, but it describes a different defect (the hook's index versus the real index under `git commit -a`). Refuted finding 3 matches no confirmed finding.

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 4/4 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 7 judged sound, 1 judged UNSOUND (finding 10), 2 judged INSTANCE-ONLY (findings 1 and 11, curing the cited instance and leaving its class standing), 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Checklist: 87 items, acquired by the harness from `--for-diff 846d51d39de6bd14174032a338234604273afd8d..HEAD`, each assigned to exactly one of 5 lenses: security 18, correctness 18, seams 17, verification 17, intent 17.
- Refuted findings shown to synthesis: 2. Same-address pairs shown: 2.
- Dispositions: unclassed refuse; 87 class slugs handed; 175 leg names read from `tools/gate-legs.json`.
- Every count above is zero where it must be, so this run is complete.

## MEDIUM

### M1 — `--write-staged` writes and stages the render before it raises the view refusal (findings 4 and 12, medium)

**Where:** `tools/memory-tree/gen_build_index.py@fb93e554:3365` (the late `raise refused`) and `tools/memory-tree/gen_build_index.py@fb93e554:3346` (the `git add` into the hook's index); write path at lines 3332-3351.

**What is wrong:** In staged mode, a Problem from `render_asbuilt_view` (lines 3302-3303) is only held in `refused`. `cmd_write` still writes the moved artifacts, removes orphans and runs `git add -A` into `GIT_INDEX_FILE`, and only then raises. A `git add` failure at 3349 likewise raises after the files are written. The data-loss-guard decline (3314-3322) is the only one that restores and returns before writing.

**Consequence:** The hook (`.githooks/pre-commit:242`) reads exit 1 as a declined render and refuses the commit. Under a plain `git commit` the hook's index is the real `.git/index`, so the rendered README and ledger paths stay staged, and the user's next commit carries paths they never staged. This breaks spec 3's rule that every decline exits 1 and writes nothing (§S2, error-states line 255, AC prose 294-295), and the hook comment's "refuses as before". It is reachable in this repo: `.memory-tree.conf` arms `DESIGN_VIEW`, `DESIGN_RECORD`, `DESIGN_BASELINE` and `STAGED_RENDER=1`, and the same Problem fails check 9, so the hook reaches `--write-staged`. Contained: the commit is refused and the paths are visible.

**Fix (judged SOUND by the skeptic, both findings):** Check `refused` before anything is written. Right after the view render: `if staged and refused: print('build-index: render NOT staged — ' + str(refused)); return 1`, as the guarded decline does. Make the `git add` failure restore what was written, or probe that `git add` works before writing.

**Left-shift gate:** Add a `test_staged_write` arm in the `build-index selftest` leg whose fixture arms `DESIGN_VIEW` with an unreadable `DESIGN_RECORD` (or `DESIGN_BASELINE`) and stages a spec status change. It runs `--write-staged` and asserts rc 1, an unchanged `git status --porcelain` and an unchanged `git diff --cached --name-only`.

### M2 — P3 reads a shell comment as a sleep duration and refuses a sub-floor pause (finding 2, medium)

**Where:** `tools/hooks/scratch-guard.js@3220edce:1647` (`checkPollWait`); `deriveSleepSeconds` near line 1619.

**What is wrong:** `checkPollWait` reads every word after `sleep` as a duration, comment words included. `deriveSleepSeconds` returns null on `#`, and null is treated as "a duration that does not read", which is refused.

**Consequence:** The skeptic re-ran the probe: `checkPollWait("sleep 3 # brief pause")` returned row `P3 sleep at or over 5 s` with argv `["sleep","3","#","brief","pause"]`; `sleep 3` returned null. A role agent's 3-second pause is refused as soon as it carries a comment, and the deny text attached to the refusal says a pause under 5 s outside a loop is admitted. This is a false hit inside the build's one intended new refusal class. Contained: the agent can drop the comment and retry.

**Fix (judged SOUND by the skeptic):** Cut `rest` at the first word that starts with `#` before deriving the seconds. Better, strip comments once in `buildCommandView` or `scanCommandHeads`, so every gate row sees the same argv.

**Left-shift gate:** Add `scratch-guard self-test` rows: `sleep 3 # x` admitted with empty stderr, `sleep 9 # x` refused naming P3.

### M3 — The AC6 arm reads the hygiene producer, but its leg's guard does not name that file (finding 6, medium)

**Where:** `.githooks/pre-commit.test.sh@6afa5a00:294` (the arm, lines 286-296); the guard of leg `branch-guard self-test` at `tools/gate-legs.json@c487c5fe:619`.

**What is wrong:** The arm greps `echo "HYGIENE check $1 FAILED` out of `tools/memory-tree/check-memory-hygiene.sh` so that a message edit there reds it. The leg that runs the suite is guarded only by `.githooks/` and `{prefix}/lib/`, and `run-gates.sh`'s `changed()` (near line 538) skips a guarded leg when none of its guard paths moved.

**Consequence:** A commit that edits only the `fail()` wording skips the very arm written to catch it, or reuses its stale green. The hook's `grep -q '^HYGIENE check 9 FAILED'` then silently stops matching, and every check-9 refusal reverts to a manual re-render while the bar reads green. Bounded: the pre-push hook forces a full run when no recorded full green covers the tip within its commit window, so the signal comes late rather than never.

**Fix (judged SOUND by the skeptic):** Add `{prefix}/memory-tree/check-memory-hygiene.sh` to the `branch-guard self-test` guard. `gen_build_index.py` need not be added: the suite uses a stand-in for it.

**Left-shift gate:** A meta-check that every file a suite reads from outside its own guard is named in its leg's guard (the class `held-suite-guard-misses-a-sibling-kit`). Probe for this instance: edit only the `fail()` literal and run the bar in changed mode; the leg must run and go red.

### M4 — No arm exercises the `.lock` or relative-path arms of the staged index rule (finding 7, medium)

**Where:** `tools/memory-tree/gen_build_index.py@fb93e554:1011` (`allowed` built from `own` and `own + ".lock"` in `check_staged_write`); `test_staged_write` at line 4710.

**What is wrong:** `test_staged_write` sets `GIT_INDEX_FILE` only as unset, a foreign copy, and the absolute `<t>/.git/index` (line 4779). A read-only probe showed git hands the hook `<abs>/.git/index.lock` under `git commit -a`, and a relative `.git/index` under a plain commit. The hook suite uses a stand-in generator (line 314), so the real `check_staged_write` never runs under `git commit -a`.

**Consequence:** Dropping `own + ".lock"`, or comparing the lock path in another form, passes every gate. Every `git commit -a` would then decline the render and fall back to the old check-9 refusal, though spec 3's own table lists that row as "in the commit". A lost speed-up and a false decline, not a wrong result.

**Fix (judged SOUND by the skeptic):** Add a `test_staged_write` arm with `GIT_INDEX_FILE=<t>/.git/index.lock` (a copy of the index under that name) expecting rc 0, and one with the relative `.git/index`. Or add a pre-commit suite arm that runs the real generator under `git commit -a`.

**Left-shift gate:** The two arms above in the `build-index selftest` leg, one per row of spec 3's index table.

### M5 — The guarded decline's view restore and the orphan staging have no test (finding 8, medium)

**Where:** `tools/memory-tree/gen_build_index.py@fb93e554:3314` (the `staged and guarded` branch, 3314-3322); `to_stage += moved + list(orphans)` at 3327.

**What is wrong:** The guarded branch restores `view_prev`, or removes the view when it was new, then returns 1. No `test_staged_write` arm (4710-4790) plants a guarded view; its declines are blank, illegal, foreign-index, no-bytes-moved and unstaged-input. The guard arms near 7334-7356 use plain `--write`/`--check`. No arm reaches the orphan staging with an orphan.

**Consequence:** A broken restore (wrong bytes, or a skipped `os.remove` for a new view) passes every gate. A guarded decline would then leave a rewritten view unstaged, breaking S2's "writing nothing" contract, and the hook would refuse over a dirty tree the author did not make. Contained to the author's worktree.

**Fix (judged SOUND by the skeptic):** Add a `test_staged_write` arm in which `plan()` reports a guarded view and the armed view's bytes move; assert rc 1, the "data-loss guard holds" line and an unchanged `git status --porcelain`. Add one arm with an orphaned ledger shard asserting the removal is staged.

**Left-shift gate:** One `test_staged_write` arm per decline spec 3 §S2 lists, each asserting an unchanged `git status --porcelain`, so a new decline without an arm is visible against the list.

### M6 — The scoped hygiene fixture sets no `SPEC_EDGES_CUTOFF`, so the scoped edge reading never runs (finding 9, medium)

**Where:** `tools/memory-tree/check-memory-hygiene.test.sh@2b3fa466:1303` (the scoped12 fixture conf); the guarded paths at `check-memory-hygiene.sh:2136` (`{ STAGED || SCOPED; } && -n SPEC_EDGES_CUTOFF`, which tags siblings `J`) and `:3030` (`stg="$((STAGED | SCOPED))"` in the edge awk).

**What is wrong:** The fixture conf sets `SPEC_FORMAT_CUTOFF` and `BASE_RESOLVE_CUTOFF` but not `SPEC_EDGES_CUTOFF`, and no fixture spec declares an edge. The other conf that sets the cutoff (line 4601) is not used for a scoped run.

**Consequence:** This repo's conf sets `SPEC_EDGES_CUTOFF="2026-09-08"`, so every real `--only 12 --spec` run takes this untested path. Removing `|| SCOPED` (a missing mirror edge passes) or `| SCOPED` (siblings' own payload findings leak into a `--spec` run) passes every gate, against spec 2 S2's promise.

**Fix (judged SOUND by the skeptic):** Set `SPEC_EDGES_CUTOFF` in the scoped fixture conf. Plant a pair in which tOne-1 declares `**hands-off** tOne-2` and tOne-2 declares no mirror, plus a sibling holding an empty-payload edge bullet. Assert `--spec tOne-1` reports the missing mirror, matching the unscoped line, and does not report the sibling's own payload finding.

**Left-shift gate:** A `memory-hygiene self-test` assertion that the scoped fixture conf sets every cutoff key this repo's `.memory-tree.conf` sets, so a pin-gated path cannot sit unarmed in the fixture.

### M7 — Arm 23's append and torn arms cannot tell a resumed read from a cold re-parse (finding 10, medium)

**Where:** `tools/roles/adopt-roles.test.sh@0deeb156:1055` and the torn arm after it; resume code at `tools/roles/handoff.py:905-940`.

**What is wrong:** Both arms assert only that the output equals the cold lines (`check_cold23`), and the torn arm adds a `cmp` on the transcript. A full re-read from byte 0 prints the same lines and, with `rec` None, writes a record with offset equal to the file size and the full prefix. The only arm that proves the record is read (the poison arm at :1051) runs on an unchanged file.

**Consequence:** Unit 7's speed-up, parsing only the appended bytes, can vanish behind a green suite: a regression that treats any record whose offset is below the file size as a miss passes every arm. Spec 7's AC4 red-when ("by_id is not rebuilt") can only go red if a resume actually happens. Lost speed, not a wrong verdict.

**Fix (the finder's proposal was judged UNSOUND by the skeptic; this is the skeptic's corrected fix):** After the first-line run (and after the torn first run), change the seeded record so its output differs from the cold output, for example strip the `gov:handoff` marker from `calls[0].input.prompt` in the record JSON. Then append the remaining bytes, run again, and assert the output shows the poison (the A9L1 line is gone or changed). That holds only if the record seeded the resumed read and the appended `res`/notification lines attached through the rebuilt `by_id`.

**Left-shift gate:** The poisoned-record arm above in the `roles adopter self-test` leg, for each of the append and torn cases.

## LOW

### L1 — `--write-staged` rewrites the as-built view before `plan()` can raise (finding 1, low)

**Where:** `tools/memory-tree/gen_build_index.py@fb93e554:3312` (the view `write_text`), before `plan()` at 3313.

**What is wrong:** In staged mode the as-built view (`DESIGN_VIEW`, armed in this repo) is overwritten before `plan()` runs, and only the `guarded` decline puts `view_prev` back. When `plan()` raises a Problem (line 2790, a `parents:` entry naming a non-build folder; also 2870 and 2954), the view stays rewritten and unstaged.

**Consequence:** Under the opt-in `STAGED_RENDER=1`, a refused commit leaves a render input changed in the worktree, against `conf.example`'s "writing nothing" (lines 482-485). On the next attempt, with `LIVE_LANDED_UNCLOSED=1` making the pathspec the whole tree, `check_staged_write` declines over the view's unstaged change, so the real cause is replaced by an "unstaged change" message about a file the user never edited. Contained: git recovers the view, nothing is committed, and check 9 raises the plan Problem anyway.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Wrap everything from the staged view write up to the `git add` in `try/finally`, keyed on "staged and not yet staged", so `view_prev` is restored on any exception (not only Problem) and on every decline return, including the guarded branch. The finder's proposal, a `try` around `plan()` that restores `view_prev` on Problem, cures the cited instance alone. This `finally` also restores the view on the M1 path; M1 still needs its early return to keep the artifacts unwritten.

**Left-shift gate:** A `test_staged_write` arm that arms `DESIGN_VIEW`, plants a README whose `parents:` names a non-build folder, runs `--write-staged` and asserts `git status --porcelain` is unchanged. Add `destructive-step-before-its-precondition` arms for every raise inside the staged window.

### L2 — The P3 rows test only far from the 5 s floor and no unit suffix (finding 11, low)

**Where:** `tools/hooks/scratch-guard.test.sh@1eaa4530:1469` (rows 1469-1476: `sleep 240`, `sleep "$W"`, `sleep 30`, `sleep 1`); `checkPollWait` at `scratch-guard.js:1648` (`s >= POLL_SLEEP_FLOOR_S`), `deriveSleepSeconds` at `:1620`.

**What is wrong:** No row tests `sleep 5` (exactly the floor), a sub-floor decimal, a unit suffix (`m`, `h`, `d`) or `infinity`, all of which `deriveSleepSeconds` parses.

**Consequence:** Changing `>=` to `>`, or breaking the suffix multipliers, passes every arm, and `sleep 5` or `sleep 1m`, which spec 6's P3 row refuses, would be admitted. Limited to the new polling class.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Add role rows that deny `sleep 5`, `sleep 1m`, `sleep 1h`, `sleep 1d` and `sleep infinity`, each naming P3, and rows that admit `sleep 4.9` and `sleep 4s` with empty stderr. Raise `FLOOR_ASSERTIONS` by the number of rows added. The finder's proposal (`sleep 5`, `sleep 1m`, `sleep 4.9` only) cures the cited instance alone.

**Left-shift gate:** The rows above in `scratch-guard self-test`; as a checklist entry, every numeric threshold a guard compares gets a row at the threshold and one on each side of it.

review-shape kind=diff-review round=1 intensity=full at=synth raw=12 confirmed=10 refuted=2 merged=0 unverified=0 blocker=0 high=0 medium=8 low=2 agents=10 out-tokens=111388
review-round round=1 limit=- prior=- count=0 state=CONVERGED
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/gen_build_index.py:3312 | low | low | confirmed | cmd_write (gen_build_index.py:3307-3313) runs write_text on the view before plan(). Only the `guarded` branch puts view_prev back. plan() raises Problem at 2790 (a parents: entry that names a non-build folder) and at 2870 and 2954, and that raise leaves the rewritten view unstaged. This repo's .memory-tree.conf arms DESIGN_VIEW and STAGED_RENDER=1. The conf.example (lines 482-485) says the mode declines 'writing nothing'. With LIVE_LANDED_UNCLOSED=1 the pathspec is the whole tree, so on the next run check_staged_write declines over the view's unstaged change. Both functions are new in this diff (absent at base). The effect is contained: git can recover the view, nothing is committed, and check 9 raises the plan Problem anyway. | instance | destructive-step-before-its-precondition | class:destructive-step-before-its-precondition |
| 2 | correctness | tools/hooks/scratch-guard.js:1647 | medium | medium | confirmed | I re-ran the probe. checkPollWait('sleep 3 # brief pause') returned row 'P3 sleep at or over 5 s' with argv [sleep,3,#,brief,pause]. 'sleep 3' returned null. deriveSleepSeconds (scratch-guard.js ~1619) returns null on the word '#', and checkPollWait treats null as a refusal. So the guard refuses a 3 s pause that its own deny text says is admitted. This is a false refusal inside the new polling class. Its effect is contained, because the agent can drop the comment and retry. | sound | - | new:shell-comment-word-read-as-an-argument |
| 3 | correctness | tools/memory-tree/gen_build_index.py:1017 | medium | - | refuted | The scenario rests on the render reading DESIGN_RECORD from the worktree, and it does not. The conf's key doc (.memory-tree.conf:1050-1051) says the record is 'read only at DESIGN_BASELINE ... never from the working tree', so an unstaged edit to the record cannot move the rendered view. cmd_check_asbuilt adds DESIGN_RECORD to its staged trigger set, but that is a set of verdict triggers, not a list of worktree inputs to the render. The view itself is staged by --write-staged whenever its bytes move, so the commit carries what the render wrote. The claimed outcome, a view rendered from a record the commit lacks, therefore cannot happen as described. | unsound | two-readers-of-one-config-one-re-derived | - |
| 4 | seams | tools/memory-tree/gen_build_index.py:3365 | medium | medium | confirmed | I read cmd_write in tools/memory-tree/gen_build_index.py (around lines 3284-3368). With staged=True, a Problem from render_asbuilt_view is only held in `refused`. The code still writes the moved artifacts, removes orphans and runs `git add -A` into the hook's index. Only then does it `raise refused`, and main() turns that into exit 1 (around 9206-9211). A git add failure also raises a Problem after the files are written. The data-loss-guard branch is the only decline that restores and returns before writing. The hook at .githooks/pre-commit:242 reads the non-zero exit as a declined render, sets rc=1 and refuses the commit, but the paths are already written and staged. The commit's index is the real index, or its .lock under commit -a, which becomes the index, so the staged paths survive the refused commit. Spec 3's error-state line 255 and its AC prose (lines 294-295) say a decline leaves `git status --porcelain` unchanged. This path breaks that. cmd_check holds the same Problem and raises it, so check 9 fails and the hook reaches --write-staged. The effect is contained: the commit is refused and the user sees the paths. | sound | invariant-held-on-one-admission-path | class:invariant-held-on-one-admission-path |
| 5 | seams | tools/memory-tree/gen_build_index.py:3313 | medium | - | refuted | The mechanics are right. run() drops GIT_INDEX_FILE (around line 265), plan() lists inputs with `git ls-files` against the real index, and check_staged_write diffs against the hook's index. But spec 3's 'What it does not check' section (lines 181-184) records this exact limitation as accepted: under `git commit -a` the hygiene leg reads the repository's index, not the hook's, and 'The mode accepts that index'. The disagreement the finding describes is also not introduced by this diff. Before it, a user who rm'd a tracked memory file, ran --write by hand and then ran `commit -a` got the same render over the same real-index tracked set, and the same pre-existing check 9 passed it. The next commit refused it the same way. --write-staged reproduces what the manual remedy already produced, and the regrade's index blindness is pre-existing and documented. That makes this a by-design limitation of the pre-existing check, not a defect this change introduced. | instance | invariant-held-on-one-admission-path | - |
| 6 | verification | .githooks/pre-commit.test.sh:294 | medium | medium | confirmed | This diff adds the AC6 arm at .githooks/pre-commit.test.sh:286-296. It greps `echo "HYGIENE check $1 FAILED` out of the hygiene producer, tools/memory-tree/check-memory-hygiene.sh, and uses that literal to drive the render arms. The leg that runs this suite, 'branch-guard self-test' in tools/gate-legs.json (around lines 619-631), is still guarded only by `.githooks/` and `{prefix}/lib/`, and the diff does not touch gate-legs.json. run-gates.sh's changed() (around line 538) skips a guarded leg when none of its guard paths moved. So a commit that edits only the fail() wording skips the very arm written to catch it, while the hook's `grep -q '^HYGIENE check 9 FAILED'` silently stops matching. The effect is bounded: the pre-push hook forces a full run when no recorded full green covers the tip within a set number of commits. It costs an early signal, not a permanent miss, so medium. | sound | held-suite-guard-misses-a-sibling-kit | class:held-suite-guard-misses-a-sibling-kit |
| 7 | verification | tools/memory-tree/gen_build_index.py:1011 | medium | medium | confirmed | gen_build_index.py:1011 builds `allowed` from own and own + ".lock". test_staged_write (line 4710) sets GIT_INDEX_FILE three ways only: unset, a foreign copy (`other-index`), and the absolute `<t>/.git/index` (line 4779). No arm uses the .lock name or a relative path. In .githooks/pre-commit.test.sh the generator at line 314 is a stand-in heredoc, so the real check_staged_write never runs under `git commit -a`. Nothing else in tools/ calls --write-staged with an index path. If someone dropped the .lock entry, every gate would still pass, and every `git commit -a` would fall back to the old check-9 refusal. That is a lost speed-up and a false decline, not a wrong result, so the effect is contained. | sound | - | class:rule-stated-with-no-check-that-fails |
| 8 | verification | tools/memory-tree/gen_build_index.py:3314 | medium | medium | confirmed | The `staged and guarded` branch at gen_build_index.py:3314-3322 restores view_prev, or removes the view when it was new, then returns 1. No arm in test_staged_write (4710-4790) plants a guarded view; its declines are blank, illegal, foreign-index, no-bytes-moved and unstaged-input. The existing guard arms near 7334-7356 use plain --write/--check, not --write-staged. `to_stage += moved + list(orphans)` at 3327 is likewise never reached with an orphan in this suite. A broken restore would leave an unstaged rewritten view and still pass every gate. The effect stays in the author's worktree. | sound | - | class:rule-stated-with-no-check-that-fails |
| 9 | verification | tools/memory-tree/check-memory-hygiene.test.sh:1303 | medium | medium | confirmed | The scoped12 fixture conf at check-memory-hygiene.test.sh:1303 sets SPEC_FORMAT_CUTOFF and BASE_RESOLVE_CUTOFF but no SPEC_EDGES_CUTOFF. So the guard at check-memory-hygiene.sh:2136 (`{ STAGED \|\| SCOPED; } && -n SPEC_EDGES_CUTOFF`) is false in every scoped arm, no sibling is tagged J, and the edge awk at 3030 with stg=$((STAGED\|SCOPED)) never sees a scoped run. The --spec and --build calls appear only in the 1295-1343 block, and the other conf that sets the cutoff (4601) is not used for a scoped run. The repository's own conf sets SPEC_EDGES_CUTOFF="2026-09-08" (line 383), so real scoped runs take this untested path. Removing `\|\| SCOPED` or `\| SCOPED` would pass every gate. SCOPED is new in this diff. | sound | - | class:fixture-lacks-a-gate-the-consumer-has |
| 10 | verification | tools/roles/adopt-roles.test.sh:1055 | medium | medium | confirmed | I read tools/roles/adopt-roles.test.sh:1054-1060 and the resume code in tools/roles/handoff.py:905-940. The append arm and the torn arm each call check_cold23 only, and the torn arm also runs cmp on the transcript. A run that re-parses from byte 0 prints the same two lines, and because rec is None it also writes a record with offset equal to the file size and the full prefix. So a regression that drops the resume step passes both arms, even though the arm-23 header comment says each one is 'resumed from the record's offset'. The only arm that proves the record is read (the poison arm at :1051) runs on an unchanged file. Nothing in the suite outside handoff.py calls read_session_record, and the AC4/AC5 r6probe probes are not part of the suite. The cost of such a regression is lost speed, not a wrong verdict, so medium. | unsound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 11 | verification | tools/hooks/scratch-guard.test.sh:1469 | low | low | confirmed | The P3 rows at scratch-guard.test.sh:1469-1476 use sleep 240, sleep "$W", sleep 30 and sleep 1. checkPollWait (scratch-guard.js:1648) refuses when s >= POLL_SLEEP_FLOOR_S, and deriveSleepSeconds (:1620) handles the s/m/h/d suffixes and infinity. None of these rows tests the floor value itself or any suffix, so changing >= to > or breaking the multipliers leaves the suite green. The effect stays inside the new polling refusal class and changes no other verdict, so low. | instance | - | new:threshold-tested-only-far-from-its-floor |
| 12 | intent | tools/memory-tree/gen_build_index.py:3346 | medium | medium | confirmed | In gen_build_index.py:3299-3366, cmd_write(staged=True) catches the Problem from render_asbuilt_view into `refused`. It then still writes the moved artifacts and runs `git add -A` into GIT_INDEX_FILE, and only re-raises at :3365, so the process exits 1. check_staged_write accepts the repository's own index, which is the index git hands the hook under a plain `git commit`. The hook at .githooks/pre-commit:242 then sets rc=1 and refuses the commit, but the paths stay staged in the real index. This repo's .memory-tree.conf sets DESIGN_VIEW and STAGED_RENDER=1, so the path is reachable. That contradicts the hook comment ('a declined render, any other failure ... refuses as before') and spec 3's 'Every decline ... exits 1'/'writes nothing'. The code is new in this diff: the base has no --write-staged. test_staged_write has no arm for a view refusal. | sound | - | class:invariant-held-on-one-admission-path |

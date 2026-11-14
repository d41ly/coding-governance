**Serves:** diff-review TOOL-aLightenedLoop-1 TOOL-aLightenedLoop-2 TOOL-aLightenedLoop-3 TOOL-aLightenedLoop-4 TOOL-aLightenedLoop-5

# Implementation diff review, round 1: build aLightenedLoop, units 1 to 5

2026-11-14 · Tier-2 · on `branch/alightenedloop-eb7b8b` · adversarial fan through `tier2-review.js`: 5 finder lenses (gov-diff-reviewer), then 4 skeptic batches (gov-skeptic), then this synthesis (gov-synthesizer). The build's one binding rule is PARITY: every touched check keeps its exit code, refusal text and rendered bytes as at BASE, and only time may move.

**Reviewed range:** `846d51d39de6bd14174032a338234604273afd8d...ef77564196690c235c2786cf6831c2ba7e0bdf0a`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or HIGH, and no confirmed finding shows a touched check returning a verdict, refusal or byte that differs from BASE today. M1 still has to be fixed before unit 2 can land. `print_wake` calls `read_recorded_phase` outside check 39's allow-list, so the unattended kit leg is red on this tree. M3 is the one cache defect. The spec-token cache key is derived after the stability bracket closes, so an edit made during the replay can be recorded under a verdict computed over the earlier tree. Every other item is a suite arm that cannot fail, or one avoidable re-read on a hot path.

## Review shape

Intensity full, raw 11, confirmed 10, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 1 | 0 | 1 | 0 | 0 | 1.00 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 0 HIGH, 7 MEDIUM, 1 LOW, which is 8 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 0 HIGH, 9 MEDIUM (ids 1, 2, 3, 5, 6, 7, 8, 10, 11), 1 LOW (id 9), which is 10 findings.
- One merge was made at write time. Ids 2, 5 and 10 describe one defect, the L5-AC4 checkout move, and form M2. Id 4, a seams duplicate of id 5, was counted by the harness as a merged confirmation. It is not a confirmed id and is not counted again here.
- I re-grade nothing. Every id keeps its bracketed binding grade. Ids 1 and 5 were re-graded from high to medium by their skeptics.
- Security found nothing. Its zero is real evidence because every lens returned, but it is bounded by the stated model: local tooling with no network surface.
- Intent input: 6 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 77 items, acquired from `--for-diff` over the range, each assigned to exactly one of 5 lenses: security 16, correctness 16, seams 15, verification 15, intent 15. By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 1 duplicate refutation counted as a merged confirmation (id 4 into id 5), 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 4 judged sound (ids 1, 3, 9, 11), 4 judged UNSOUND (ids 2, 5, 6, 10), 2 judged INSTANCE-ONLY, curing the cited instance and leaving its class standing (ids 7, 8), 0 none proposed, 0 NOT JUDGED. Where a fix was judged unsound, only the skeptic's corrected fix appears below. Where it was judged instance-only, the skeptic's class-level fix is the fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (ids 1 and 5, high to medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags.
- Every count above that should be zero is zero, so the run is complete.

## The hunt list, answered

1. **A cache or skip that can return what a fresh run would not.** One is confirmed: M3, where the spec-token key is derived outside the stability bracket. No finding was confirmed against the render stamp's trust after an unstaged edit, check 9's quiet-record skip, check 29's early exit, or the stop-guard's liveness key inputs and staleness window. Their test coverage is thin, though (M2, M4, M5).
2. **A shared-condition extraction that changed an existing verb's output.** None confirmed. `--resume`, `--audit`, `--liveness` and `--status` drew no finding. The one extraction-adjacent defect is M1: the new verb's reader is missing from a per-function allow-list.
3. **A suite arm that cannot fail.** M2 (the checkout move cannot isolate `head`), M4 (the near-expiry arm sits past the margin), M5 (the stamp guard's three conditions have no arm), M6 (three of `--wake`'s FULL reasons have no arm) and L1 (one not-recorded branch has no arm).

## MEDIUM

### M1 — `print_wake` reads the recorded phase outside check 39's allow-list, so the unattended kit leg reds (id 1)

`tools/unattended/unattended.sh@72489115:8794`, against `tools/unattended/check-unattended.sh@c43efbd9:6227`.

The new `print_wake()` (it starts at `:8787`) calls `read_recorded_phase "$rel" >/dev/null; ph=$_fact`. Check 39 allows that reader only inside the functions named by `PHASE_RECORDED_FNS`: refuse_if_terminal, archive_name_of, verb_landed, print_liveness, run_settle, check_commit_message and main. The diff does not add `print_wake` to that list. The skeptic ran check 39's own awk over the driver and got exactly one offender, `8794 print_wake`, which becomes `fail 39`. The unattended kit leg on the merge bar is red on this tree. The bar refuses the merge, so nothing wrong ships, but unit 2 reads as done while it cannot land.

- Fix judged SOUND by the skeptic: add `print_wake` to `PHASE_RECORDED_FNS` in `tools/unattended/check-unattended.sh`. Put the reason on a comment line above it, as the other entries have: `--wake` is offline, so it reads the RECORDED phase, and it answers FULL on LANDING and HELD, the two phases where the derived phase can differ. Then run the unattended kit leg and confirm check 39 is clean.
- Left-shift: the existing `unattended kit gate` leg already catches this. The miss is that the unit closed without that leg green. A unit that touches `tools/unattended/` should not record CLOSED until `bash tools/run-gates/run-gates.sh` passes on its tree. That is the bar run before close, not a new gate.

### M2 — L5-AC4's checkout move cannot go red when `head` is dropped from the liveness key (ids 2, 5, 10)

`tools/unattended/stop-guard.test.sh@fe85cba0:637`.

`deriveLivenessKey` in `tools/unattended/stop-guard.js` hashes `<gitDir>/HEAD` as the `head` part and `git show-ref --head` as the `refs` part. The AC4 loop's checkout move is `run_fxgit checkout -q -b other`. That creates `refs/heads/other`, so `refs` moves too, and the second stop still spawns with `head` removed from the key. No other move changes HEAD alone: commit changes refs, and the session move does not touch HEAD. The arm header's claim, "RED when deriveLivenessKey drops the part that move reaches", is false for this move. Spec 5 AC4, which asks for "a checkout of another branch at the same sha", is not met either. The consequence is a missing guard, not a wrong verdict today. `head` is the only part that moves when a worktree switches to an existing branch at the same commit, and the driver's ELSEWHERE verdict is keyed on that symbolic ref. A later edit that drops `head` would serve a cached LIVE or HELD and block with `run-open` where a fresh read says ELSEWHERE and allows, while this suite stays green.

- id 2, fix REJECTED by the skeptic. Corrected fix: create the branch inside the preceding `commit` move, which already changes refs: `commit) run_fxgit commit -q --allow-empty -m move; run_fxgit branch other ;;`. The checkout move then becomes `checkout) run_fxgit checkout -q other ;;`. At that point `other` and HEAD point at the same commit, so `show-ref --head` prints identical lines and only the HEAD file moves. Observe the arm red against a copy of `stop-guard.js` without the `head` part.
- id 5, fix REJECTED by the skeptic. Corrected fix: create `other` with `run_fxgit branch other` before the baseline stops. Then put the checkout move before the commit move in the loop (`for MOVE in checkout record commit ...`) and make it `run_fxgit checkout -q other`, so `other` and HEAD still share a sha when the switch happens.
- id 10, fix REJECTED by the skeptic. Corrected fix: make the checkout move `run_fxgit checkout -q --detach`. That rewrites `.git/HEAD` to a raw sha and leaves `git show-ref --head` byte-identical, so only `head` moves.
- Synthesis note: all three corrections isolate `head`. The id 2 and id 5 forms keep spec AC4's wording, "another branch at the same sha", and the `--detach` form does not. Prefer id 2's form, since it leaves the loop order alone. Whichever form lands, it must be observed red against the `head`-less copy.
- Left-shift: a staged-break discipline for key-derivation suites. For every part in `deriveLivenessKey`'s parts list, the suite runs a staged copy with that part deleted and asserts its arm reds. The part list is read from the source, so a new part without an isolating move reds the suite. Add it as an arm family in `stop-guard.test.sh`.

### M3 — `run_spec_token_check` derives the cache key after its stability bracket closes (id 3)

`tools/unattended/unattended.sh@72489115:14601`.

`run_spec_token_check` reads the tree state before the checker runs (`:14581`) and again after it (`:14596`), and compares the two. Only then does `derive_spec_token_key` run `check-spec-tokens.py --input-key`. That call replays every recorded read, listing and git call against the live tree. A write that lands after the second `read_tree_state` but during the replay therefore goes into the recorded key, while the admitted verdict was computed over the earlier tree. On the next `--dispatch`, the cache-hit path (`:14573-14578`) derives the same key from the edited tree and prints `spec-token check skipped`. That admits a dispatch a fresh checker run would refuse under check 49. The race is reachable when a sibling unit's builder writes in the same worktree, for example a spec edit, during a replay that re-runs git calls and the packet door and can take seconds. The bar's whole-tree spec-tokens leg is the remaining backstop, which keeps this MEDIUM.

- Fix judged SOUND by the skeptic: derive the key inside the bracket. Call `derive_spec_token_key` before the second `read_tree_state`, then require `_stnow == _stat` before writing `_strec`. Alternatively, read the tree state again after the derive and record only if it still equals `_stat`. Probe the build should run: a stub `SPEC_TOKENS_CLI` that loads the real checker module, plus a replayed `run` line whose command edits a tracked spec on its first replay. With the fix, the key must not be recorded.
- Left-shift: a bug-class checklist entry for every verdict cache in the kit: the key and the verdict must both be derived inside one stability bracket, and an arm mutates the input during key derivation and asserts that nothing is recorded. The stop-guard's liveness cache and the render stamp are the other two caches in this build, and they should be swept against the same entry.

### M4 — The liveness cache's near-expiry arm sits past the margin it should test (id 6)

`tools/unattended/stop-guard.test.sh@fe85cba0:661`.

`readLiveness` in `stop-guard.js` stores `deadline = t0 - lastMove + staleBound`, and a hit requires `now + wait + 1 <= entry.deadline`. The near-expiry arm uses `set_live_clock 10 5`, which stores `deadline = t0-5`, already in the past. Even `now <= deadline` misses, so the arm stays green with the `wait + 1` margin removed. The header promises that a stored LIVE expires before a fresh read could say STALE. Spec 5 AC5 states that a hit needs `deadline - now` to exceed the bound plus one second. A regression that serves a LIVE inside the last bound-plus-one seconds, where the fresh driver may already print STALE (which the stop-guard allows), passes the suite. The effect is a contained test gap.

- Fix REJECTED by the skeptic. Corrected fix: add the near-margin case with `STOP_GUARD_LIVENESS_BOUND_MS=3000` (wait=3) and `set_live_clock 0 3`, so the deadline is t0+3. The current code needs `now+4 <= t0+3`, which never holds, so the second stop always spawns: assert the count is 2. With the margin removed, the condition becomes `now <= t0+3`, the second stop is served from cache, the count reads 1 and the arm goes red.
- Left-shift: a bug-class checklist entry: an inequality with a margin gets two arms, one at margin plus one, which must hit, and one inside the margin, which must miss. Each is observed red against a copy with the margin removed.

### M5 — The render stamp's guard has no arm for a red write (id 7)

`tools/memory-tree/gen_build_index.py@634b8026:4729`.

`test_render_stamp` (`:4729-4762`) covers AC1, AC3 and the "one more working-tree byte" half of spec 1 AC4. It has no arm for the other half: a `--write` whose check would be red must leave no stamp. Red here means an unmanaged file, a guarded view or a verdict rc other than 0, and spec 1 AC4 names the unmanaged ledger-file case explicitly. `cmd_write`'s guard (around `:3342`) is `if stamp and rc == 0 and not unmanaged and not guarded`. It can be weakened to `if stamp` with the selftest still green. `--check --staged` (around `:9096`) would then answer from the stamp and certify a tree that a full `--check` refuses. The only coverage today is the one-off acceptance probe at the close. The push-boundary full render backstops it, which keeps this MEDIUM.

- Fix judged INSTANCE-ONLY by the skeptic. Class-level fix: give each of the stamp guard's three conditions its own arm: (a) an unmanaged non-shard file under `memory/ledger/`, (b) a fixture row whose verdict makes `print_verdicts` return nonzero, and (c) a guarded view. Each arm runs `--write`, `git add -u` and `--check --staged`, then asserts that no "answered by the stamp" line appears and that no stamp file exists. Observe each arm red with only its own condition removed. The finder's proposal, a single unmanaged-ledger-file arm, cures the cited instance alone.
- Left-shift: the `build-index selftest` leg is where these arms land. The class rule is one arm per conjunct of any guard that lets a cache certify, so that no conjunct can be deleted without a red.

### M6 — Three of `--wake`'s FULL reasons have no arm (id 8)

`tools/unattended/unattended.test.sh@dfb3aa3f:9819`, against `tools/unattended/unattended.sh@72489115:8818` and `:8826`.

`print_wake` (`tools/unattended/unattended.sh@72489115:8787-8840`) has a `clock probe` branch (TC_DEAD), a `task probe` branch (TA_DEAD), and a phase case covering empty, HELD, LANDING and terminal phases. The wake suite's `check_wake_full` calls (`tools/unattended/unattended.test.sh@dfb3aa3f:9800-9819`) cover only phase HELD, abandoned, asks moved, worktree, holder, lease, claims unread, claim, tree idle and task stalled. "clock probe" appears in the suite only in unrelated `--audit` and lease arms. If either probe branch is deleted, a dead probe falls through to HEALTHY and every wake arm stays green. The tick would then end without running `--resume`/`--audit`, which would have refused with check 51. That is the reassuring wrong verdict spec 2's table (lines 151-162) routes to check 51. A terminal phase dropped from the case would read HEALTHY the same way.

- Fix judged INSTANCE-ONLY by the skeptic. Class-level fix: add one `check_wake_full` arm for every `<reason>` row in spec 2's table and one for every alternative in `print_wake`'s phase case. That covers phase absent (an empty phase line), phase LANDING, one terminal phase, clock probe and task probe. Observe each arm red with only its own branch or case alternative deleted. The finder's proposal, arms for clock probe, task probe, phase LANDING and one terminal phase, cures the cited instance alone.
- Left-shift: the `harness arms (fail branches armed or pinned)` leg is the natural home. Extend it to treat each `FULL <reason>` emitted by `print_wake` as a fail branch that needs an arm naming its reason, so a new reason without an arm reds the bar.

### M7 — Check 29's staged INPROGRESS path reads every chain spec twice (id 11)

`tools/check-spec-tokens.py@d073ec44:1344`.

When `building=True` and at least one chain spec is INPROGRESS, `derive_carries_coverage` calls `read_carries_texts` at `:1344`. It then falls through to `read_carries_specs` at `:1352`, which calls `read_carries_texts` again at `:1149`. Every chain spec's text is re-read and its header re-parsed. `cmd_check_coverage` passes `building=staged`, so every commit made during a chain build pays one extra status pass over every chain spec. Spec 1 measured that pass at 1.3 s over 1,543 specs (PINNED). This is the INPROGRESS case AC8 exercises, and the build's whole purpose is that time may only fall. Verdicts and bytes are unaffected, which keeps this MEDIUM.

- Fix judged SOUND by the skeptic: on the INPROGRESS path, reuse the texts already read. Have `read_carries_specs` take an optional pre-read `(texts, statuses, skipped)`, or split out its history half, and call that from the building branch instead of calling `read_carries_specs` again. Its existing callers keep the current signature.
- Left-shift: the spec-tokens selftest gets an arm that counts `read_carries_texts` calls on the staged INPROGRESS path, with a counting shim, and asserts exactly one. A time-only build should pin read counts on each path it claims to shorten, because wall-clock figures are too noisy for a gate.

## LOW

### L1 — The "input record cannot be replayed" not-recorded branch has no arm (id 9)

`tools/unattended/unattended.sh@72489115:14602`.

`run_spec_token_check` (`:14595-14608`) has three branches that decline to record a key. The suite (`tools/unattended/unattended.test.sh@dfb3aa3f:7878-7893`) hits "the tree or HEAD moved" and "the checker wrote no input record". It never hits "the input record cannot be replayed", and a grep of the suite for that string returns nothing. The `--input-key` popen arm in `check-spec-tokens.test.sh` tests the checker, not this driver branch. Collapsing the branch, for example recording an empty key or skipping the announcement, would go unnoticed. An empty or failed key is never recorded or matched, so the effect is limited to a lost or misleading announcement line.

- Fix judged SOUND by the skeptic: add a stub checker that writes `{"kind":"popen","argv":["x"]}` to `$SPEC_TOKENS_INPUTS` and exits 0. Assert that the call prints `spec-token cache not recorded: the input record cannot be replayed` and that a repeat call does not print `spec-token check skipped`.
- Left-shift: the same `harness arms (fail branches armed or pinned)` extension as M6. Every distinct "not recorded" announcement string in the driver should be named by at least one arm.

review-shape kind=diff-review round=1 intensity=full at=synth raw=11 confirmed=10 refuted=0 merged=1 unverified=0 blocker=0 high=0 medium=9 low=1 agents=10 out-tokens=148328
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/unattended/unattended.sh@72489115:8794 | high | medium | confirmed | print_wake() starts at column 0 on tools/unattended/unattended.sh@72489115:8787, and line 8794 is `read_recorded_phase "$rel" >/dev/null; ph=$_fact`. PHASE_RECORDED_FNS at tools/unattended/check-unattended.sh@c43efbd9:6227 is untouched by the diff and does not name print_wake. I ran check 39's own function-tracking and allow-list awk over the driver. It printed exactly one offender, `8794 print_wake`, so check 39 fails 39 and the unattended kit leg reds. Graded medium: the bar refuses the merge, so nothing wrong ships, but unit 2 cannot land as it stands. | sound | hand-named-gate-list-green-while-the-bar-reds | gate:unattended kit gate |
| 2 | correctness | tools/unattended/stop-guard.test.sh@fe85cba0:637 | medium | medium | confirmed | deriveLivenessKey (tools/unattended/stop-guard.js@15689703:143-155) hashes the HEAD file as `head` and `git show-ref --head` as `refs`. The arm's checkout move is `git checkout -q -b other` (tools/unattended/stop-guard.test.sh@fe85cba0:637). That creates refs/heads/other, which changes the show-ref output, so the key still moves and the spawn count still rises even with `head` removed. No other move changes HEAD alone, so dropping `head` would leave the suite green. Graded medium: this is a coverage gap in a test, and it changes no behaviour. | unsound | liveness-negative-from-another-population | class:comment-claims-a-check-the-case-does-not-run |
| 3 | seams | tools/unattended/unattended.sh@72489115:14601 | medium | medium | confirmed | In run_spec_token_check (tools/unattended/unattended.sh@72489115:14596-14606), _stnow is read and compared with _stat first. Only afterwards does derive_spec_token_key run `check-spec-tokens.py --input-key`, which re-reads the recorded inputs from the live tree. An edit that lands after the _stnow read but during the replay therefore goes into the recorded key, while the admitted verdict was computed over the earlier tree. On the next --dispatch, the cache-hit path at 14573-14578 derives the same key from the edited tree and skips the checker. The read_tree_state bracket does not cover the key derivation, so the race is real. Graded medium: the window is the length of the replay, and the bar's whole-tree leg still grades the specs. | sound | - | class:witness-graded-against-a-fact-written-after-it |
| 4 | seams | tools/unattended/stop-guard.test.sh@fe85cba0:637 | low | - | refuted | duplicate of id=5. It is the same claim against the same line: in stop-guard.test.sh line 637, `checkout -q -b other` creates refs/heads/other, so the `refs` part of the key (`git show-ref --head`) moves along with `head`. | unsound | - | - |
| 5 | verification | tools/unattended/stop-guard.test.sh@fe85cba0:637 | high | medium | confirmed | The finding holds. stop-guard.js deriveLivenessKey hashes 'head' (the bytes of .git/HEAD) and 'refs' (`git show-ref --head` stdout) as separate parts. The AC4 loop's checkout move (test.sh line 637) is `run_fxgit checkout -q -b other`, which adds a refs/heads/other line to show-ref's output. The counter therefore rises even when the 'head' part is dropped, so no arm guards that part. That contradicts spec AC4, which asks for 'a checkout of another branch at the same sha' and is red when any one part is dropped. The header claim 'RED when deriveLivenessKey drops the part that move reaches' is false for this move. I graded it medium rather than high: nothing ships a wrong verdict today, only coverage of a future regression is missing. The proposed fix is unsound. In the loop the commit move (`commit --allow-empty`) runs just before checkout and advances main past the seed commit. A branch `other` created before the baseline stops still points at the seed, so `checkout -q other` changes HEAD's sha. show-ref --head's `HEAD` line then changes, `refs` moves again, and the arm stays green with 'head' dropped. | unsound | comment-claims-a-check-the-case-does-not-run | class:comment-claims-a-check-the-case-does-not-run |
| 6 | verification | tools/unattended/stop-guard.test.sh@fe85cba0:661 | medium | medium | confirmed | The finding holds. In stop-guard.js readLiveness, the stored deadline is t0 - lastMove + staleBound, and a hit requires `now + wait + 1 <= entry.deadline`. The near-expiry arm (`set_live_clock 10 5`) stores deadline = t0-5, which has already passed, so even `now <= deadline` misses. The arm stays green with the `wait + 1` margin removed. Spec AC5 only requires red when the deadline is ignored, which this arm does catch. But AC5's stated behaviour (spawn unless deadline-now exceeds the bound plus one second) is never exercised at the margin. The effect is a contained test gap: medium. The proposed fix is unsound. With bound 1000 ms, wait=1 and deadline=t0+2, a second stop in the same second gives now+1+1 = t0+2 <= t0+2. That is a HIT, so on correct code the count stays 1 and the asserted 2 fails. The finding's own arithmetic ('needs now+2 <= t0+2 to hit, so it must spawn') reverses the inequality. | unsound | - | new:boundary-arm-sits-past-its-margin |
| 7 | verification | tools/memory-tree/gen_build_index.py@634b8026:4729 | medium | medium | confirmed | In gen_build_index.py, test_render_stamp (4729-4762) has arms for AC1, for AC3 and for AC4's 'one more working-tree byte' half (the last arm, around line 4761). It has no arm where --write warns of an unmanaged file, prints a verdict or hits a guarded view. Spec 1's AC4 (line 326-330) names the unmanaged ledger-file case explicitly. cmd_write's guard at line 3342 is `if stamp and rc == 0 and not unmanaged and not guarded`. If it were weakened to `if stamp`, the stamp would still be written, and `--check --staged` (around line 9096) would then answer from it with nothing going red. The effect is contained because the push-boundary full render backstops it. | instance | - | class:rule-stated-with-no-check-that-fails |
| 8 | verification | tools/unattended/unattended.test.sh@dfb3aa3f:9819 | medium | medium | confirmed | print_wake (unattended.sh 8787-8840) has a 'clock probe' branch (TC_DEAD), a 'task probe' branch (TA_DEAD) and a phase case for empty, HELD, LANDING and terminal phases. The wake suite's check_wake_full calls (unattended.test.sh 9800-9819) cover only phase HELD, abandoned, asks moved, worktree, holder, lease, claims unread, claim, tree idle and task stalled. A grep of the suite finds 'clock probe' only in unrelated --audit and lease arms (11957, 12853). Deleting either probe branch would let a dead probe read HEALTHY with every wake arm still green. That is the reassuring wrong verdict the spec's table (spec 2 lines 151-162) routes to check 51. | instance | - | class:rule-stated-with-no-check-that-fails |
| 9 | verification | tools/unattended/unattended.sh@72489115:14602 | low | low | confirmed | run_spec_token_check (unattended.sh 14595-14608) has three not-recorded branches. The suite (unattended.test.sh 7878-7893) hits 'the tree or HEAD moved' and 'the checker wrote no input record' but never 'the input record cannot be replayed'. A grep of the suite for that string returns nothing. The effect is limited to the announcement line, because an empty or failed key is never recorded or matched. | sound | - | new:refusal-branch-with-no-arm |
| 10 | intent | tools/unattended/stop-guard.test.sh@fe85cba0:637 | medium | medium | confirmed | At tools/unattended/stop-guard.test.sh@fe85cba0:637 the checkout move is `run_fxgit checkout -q -b other`. That creates refs/heads/other, so the `refs` part (tools/unattended/stop-guard.js@15689703:143-155, `git show-ref --head` output) also moves, and the stop misses the cache even with `head` (tools/unattended/stop-guard.js@15689703:154, <gitDir>/HEAD bytes) dropped from the key. No other move in the loop changes .git/HEAD without also changing show-ref output: commit changes refs, and the session move does not touch HEAD. Spec 5 AC4 (line 286) says the arm goes red when any one part is dropped, so the `head` break would stay green. The test cannot catch the regression it claims to guard. The effect stays inside the suite. | unsound | criterion-asserts-what-its-own-command-cannot-show | class:comment-claims-a-check-the-case-does-not-run |
| 11 | intent | tools/check-spec-tokens.py@d073ec44:1344 | medium | medium | confirmed | In derive_carries_coverage, building=True calls read_carries_texts at tools/check-spec-tokens.py@d073ec44:1344. When any status is INPROGRESS it falls through to read_carries_specs at :1352, which calls read_carries_texts again at :1149. So every chain spec's text is re-read and its header re-parsed through the scan and parse. Verdicts and bytes do not change. On the INPROGRESS staged path, which is common during a build, the work is strictly more than the single read_carries_specs at base. That works against the unit's time-only goal. The effect is contained to time. | sound | - | new:hot-path-reads-its-input-twice |

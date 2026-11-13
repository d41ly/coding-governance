**Serves:** diff-review TOOL-aQueuedIndex-1

# aQueuedIndex: Tier-2 diff review of TOOL-aQueuedIndex-1, round 1

*2026-11-12, on `branch/unattended-aqueuedindex`. This is an adversarial pass over the unit built on the owner's prompt "fix the tag index contention so bars don't flake". Five finder lenses ran (`gov-diff-reviewer`), then three skeptic batches prompted to refute each finding (`gov-skeptic`), then one synthesis (`gov-synthesizer`). The diff makes `load_index` connect in autocommit and opens the tree-build, overlay and `--gc` write blocks with `BEGIN IMMEDIATE`. It makes `build_index` re-read `tree_built` under the lock and raises `BUSY_TIMEOUT` from 60 to 600. It also adds the `queued-writers` fixture plant and a help line. Each pin below names the file's blob at the reviewed sha.*

Reviewed range: 97e0841d7d0bdb38df314a1f8d01616a4d431dad...1c64f6f09deb0b316e32bf773ef8a5b21fd06fce. ROUND: 1.

## Verdict: BLOCKED

One blocker item stands. The `queued-writers` plant cannot go red when S3's re-read under the lock is deleted. So the arm that the spec names as AC2's only observer certifies a mechanism it never checks. Three findings, ids 1, 4 and 6, describe this one defect.

One medium item and one low item follow. The medium is that no arm can fail when the overlay or `--gc` block loses its `BEGIN IMMEDIATE`. The low is that the plant prints `both writers green` on a run it then fails.

The locking change itself is not faulted by any confirmed finding. What fails is the evidence for it.

## Review shape

Intensity full, raw 6, confirmed 5, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.83.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 1 BLOCKER, 0 HIGH, 1 MEDIUM, 1 LOW, 3 items in all.

Adjudicated tally by raw confirmed finding: 2 blocker, 1 high, 1 medium, 1 low, 5 in all.

The two tallies differ because item B1 holds three findings: two graded blocker and one graded high.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 3/3 returned, 0 DIED.
- Verdicts: 0 contradictory demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 4 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED. An INSTANCE-ONLY fix cures the cited instance and leaves its class standing. An unjudged fix would be the finder's proposal and nothing more, and none is here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intent: 1 spec document was supplied as `specs`, beside the range's commit messages.
- Checklist: 29 items, acquired by the harness from `--for-diff 97e0841d7d0bdb38df314a1f8d01616a4d431dad..HEAD`. Each went to exactly one lens: security 6, correctness 6, seams 6, verification 6, intent 5.
- By design: the caller's byDesign.
- Shown for twin detection: 1 refuted finding and 0 same-address pairs.
- Dispositions: unclassed is `refuse`, 29 class slugs were handed and 171 leg names were read from `tools/gate-legs.json`.

Every count above is zero where it could mark a gap, so this run is complete.

## BLOCKER

### B1. The `queued-writers` plant passes with S3's re-read deleted, so AC2 cannot go red (ids 1, 4, 6)

**Where:** `tools/playbook/gov_tag.py@0fd35bfa:826`, the plant's verdict `return 0 if print_equal(...) and a > 0 and b == 0 else 1`. The mechanism it claims to observe is the re-read at `tools/playbook/tag_index.py@46bfe37d:669-670`. The spec's text is at `memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@d7815fbf:296-298`. The adopt row is `tools/playbook/adopt-playbook.sh@320df434:344` (`writer two parsed 0; both writers green`).

**What is wrong:** The plant grades writer two only on `b == 0`, where `b` is `state["parsed"]`. Delete the re-read and writer two's `BEGIN IMMEDIATE` (`tag_index.py@46bfe37d:668`) waits for writer one to commit. Writer two then rebuilds tree H and calls `_write_parsed`. That function reads `held` from `blob_parsed` inside the same transaction (`tag_index.py@46bfe37d:586`). Every blob of H is already recorded at its current version: the pause blob was parsed by writer one, and the base blobs by the earlier rebuild. So every blob is counted under `skipped`, `todo` is empty, and the function returns before `stats["parsed"] += len(todo)` (`tag_index.py@46bfe37d:609`). The value of `b` stays 0. The overlay adds nothing, because the scratch worktree is clean after `write_commit`. The dumps still match, because writer two only rewrites the same `tree_path` and `tree_built` rows.

**Evidence:** Finding 1's probe loaded `tag_index.py` in memory, replaced the two re-read lines with a print marker, and ran `gov_tag.py --fixture --plant queued-writers` through `runpy`. The marker printed 4 times, so writer two did rebuild under the lock. The plant still printed `writer one parsed 1 blob(s), writer two parsed 0; both writers green` and `incremental rows equal a cold build's`, and it exited 0.

**Consequence:** AC2's "Red when" (the waiter "builds the tree again, printing a non-zero count for writer two") can never happen. Spec §7 names this arm as AC2's cover, and AC2 is the only observer of S3. The adopt row passes either way. The RED-first observation still owed for AC2 cannot be produced, and the selftest leg stays green if someone later deletes the re-read.

**Grades:** Ids 1 and 6 take blocker, their binding grade: a gate leg certifies a mechanism it does not check. Id 4 keeps its binding high. Its skeptic graded the consequence of S3 going missing, which is only a redundant write and not a wrong result. The other two graded the vacuous gate. Both readings are recorded. The item takes the highest, BLOCKER.

**Fix:** For ids 1 and 6 a skeptic judged the fix SOUND. For id 4 the skeptic judged the fix INSTANCE-ONLY and supplied a class-level fix, which is part of the fix below.

1. Grade writer two on a signal that only the early return leaves untouched. Use either option:
   - Require `b == 0 and not state["runs"] and not state["skipped"]`. The re-read returns before `_write_parsed`, so both counters stay empty. A rebuild without the re-read counts every blob as skipped.
   - Read `tree_built.built_at` for H after writer one finishes and again after writer two, and require it unchanged. Without the re-read, writer two's `INSERT OR REPLACE` restamps it.
2. Print the writer-two counts in the plant's line. Print `both writers green` only when the checks pass; item L1 is the same line.
3. Rewrite AC2's "Red when" in the spec to name the chosen observable instead of a non-zero parsed count.
4. Show the arm red on a scratch copy with `tag_index.py` lines 669-670 deleted. Run `python tools/playbook/gov_tag.py --fixture --plant queued-writers` and confirm it exits 1 (today it exits 0). Only then record AC2 as observed red.

Finder 4 also proposed a fix, which cures the cited instance alone. It compared writer two's `tree_built` timestamp, or used `con.set_trace_callback` on writer two's connection to require that no `DELETE FROM tree_path` runs after its `BEGIN IMMEDIATE`. The skeptic's class-level fix above takes in its timestamp option, and it adds rewriting AC2's text and making the staged break a probe the build must run.

**Left-shift:** This is an instance of `criterion-asserts-what-its-own-command-cannot-show`: a state that holds when the scope item is skipped. Add a staged-break case to the `tags positional selftest` leg. Like finding 1's probe, it loads `tag_index.py` with the re-read removed, runs the plant through `runpy`, and requires exit 1. With that case in the selftest, the arm's ability to go red is checked on every bar.

## MEDIUM

### M1. Nothing fails if the overlay or `--gc` write block loses its `BEGIN IMMEDIATE` (id 5)

**Where:** `tools/playbook/tag_index.py@46bfe37d:745` (`build_overlay`) and `tools/playbook/tag_index.py@46bfe37d:784` (`remove_dead_versions`), under `isolation_level=None` at `tools/playbook/tag_index.py@46bfe37d:519`. The spec claim is S2's "Observed by AC1 and AC3" at `memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@d7815fbf:31`.

**What is wrong:** In autocommit, `with con:` opens no transaction. Delete one of these `BEGIN IMMEDIATE` lines and its block becomes a run of separately committed statements. No arm sees that. The plant's overlay runs over a clean worktree with zero entries. `--gc` runs only single-threaded in the plant (around `gov_tag.py@0fd35bfa:907`). AC3's scratch clone is also clean and never runs `--gc`. The skeptic narrowed the finder's claim for line 668: deleting it does turn the plant red, because the plant's 0.5 s held-lock poll then hits its 30 s deadline.

**Consequence:** If line 745 or 784 is deleted, a crash partway through leaves partial `dirty_path` or `--gc` rows committed. A reader can also land between statements. S2's "Observed by AC1 and AC3" is false for two of its three blocks. This diff created the gap: at BASE, implicit transactions made each block atomic without an explicit `BEGIN`. The effect is contained, so the grade is medium, the binding grade.

**Fix (judged SOUND by the skeptic):** Add one arm that fails when a write block is not atomic, in either form:
- A plant whose extractor raises partway through `_write_parsed` after some rows are inserted. It then asserts that `tree_path`, `blob_row` and `tree_built` hold no rows for that tree, and that `dirty_path` is unchanged for the overlay.
- A static check that every `with con:` in `tag_index.py` has `con.execute("BEGIN IMMEDIATE")` as its first statement.

Observe the arm red on a scratch copy with line 745 deleted.

**Left-shift:** This is an instance of `observed-by-claim-no-arm-discharges`. The static form of the fix belongs in the `tags positional selftest` leg, so that it covers every write block, including any added later.

## LOW

### L1. The plant prints `both writers green` before it checks anything (id 3)

**Where:** `tools/playbook/gov_tag.py@0fd35bfa:825`.

**What is wrong:** The `say` line `writer one parsed {a} blob(s), writer two parsed {b}; both writers green` runs with no condition. The next line returns 1 if `print_equal` fails, if `a` is 0 or if `b` is not 0.

**Consequence:** A red run logs `both writers green`. The exit code and the adopt row still go red, so the verdict is correct. Only someone reading a failing run's log is misled. The grade is low, the binding grade.

**Fix (judged SOUND by the skeptic):** Print the counts without the verdict phrase. Print `both writers green` only when `a > 0 and b == 0` and `print_equal` holds. Alternatively, move the `say` after the checks. This is step 2 of B1's fix, so one edit closes both items.

**Left-shift:** This is a new class, `success-line-printed-before-its-checks`. Add it as an entry in the project's bug-class checklist. No existing leg reads a plant's log text against its exit code.

## Refuted findings and twins

Id 2 was refuted by a skeptic. It is not counted, graded or reinstated here, and the appendix holds the skeptic's reason. It is not a twin of any confirmed finding: it concerns the spec's `**Status:** CLOSED` field, not the plant or the write blocks. No same-address pairs were shown.

review-shape kind=diff-review round=1 intensity=full at=synth raw=6 confirmed=5 refuted=1 merged=0 unverified=0 blocker=2 high=1 medium=1 low=1 agents=9 out-tokens=52242
review-round round=1 limit=- prior=- count=3 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/playbook/gov_tag.py@0fd35bfa:826 | blocker | blocker | confirmed | I read the code and the claim holds. In tools/playbook/gov_tag.py the queued-writers plant grades writer two only on `b == 0`, where b is `state["parsed"]`. In tag_index.py `_write_parsed` adds a blob to `stats["parsed"]` only when the blob is in `todo`. A blob that already has a `blob_parsed` row at the current version is counted under `stats["skipped"]` instead, and the function returns early when `todo` is empty. If the re-read at the head of build_index's BEGIN IMMEDIATE block were removed, writer two would rebuild tree H after writer one committed. Every blob would then land in `skipped`, and `parsed` would still be 0. build_overlay adds nothing here because the scratch worktree is clean after write_commit, so `b == 0` comes out the same with or without the re-read. The spec's AC2 'Red when' (a non-zero writer-two count) therefore cannot happen, and the say() line prints 'both writers green' before the return value is computed. The arm certifies the S3 re-read without testing it, and its owed RED-first observation for AC2 cannot go red. The plant is new in this diff, so the defect is in scope. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 2 | seams | memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md:3 | high | - | refuted | The order this finding objects to is the order the build method prescribes. The ledger itself says: 'Where a line says "owed", the main loop observes it after every unit is terminal.' `doc.build-method#m8-closing-the-build` also says: 'Observe the owed arms before the bar. For each New arm: line of the build's specs, the main loop observes the arm RED on its staged break and GREEN once restored, and records both in that unit's acceptance ledger under a Pass: none commit.' That is a post-close, pre-bar step. So a unit goes CLOSED with its RED-first runs, AC3's hand races and its Gates legs listed as 'owed to the close'. Those are then paid by the main loop before the bar and landing, and the branch is still under this round-1 review and has not landed. The status field is not certifying anything the protocol says should already be observed at this point, so this is by design and not a defect introduced by the diff. | unsound | one-value-field-records-a-mixed-outcome | - |
| 3 | seams | tools/playbook/gov_tag.py@0fd35bfa:825 | low | low | confirmed | At 1c64f6f09 in tools/playbook/gov_tag.py, the queued-writers plant prints `writer one parsed {a} blob(s), writer two parsed {b}; both writers green` with no condition. The next line returns 1 if print_equal fails, a is 0 or b is not 0. So a red run still logs 'both writers green'. The exit code is still correct, so only the log misleads. That makes it low. | sound | - | new:success-line-printed-before-its-checks |
| 4 | verification | tools/playbook/gov_tag.py@0fd35bfa:826 | high | high | confirmed | I traced build_index and _write_parsed at 1c64f6f09. If the re-read after BEGIN IMMEDIATE is removed, writer two waits for writer one's commit and then runs _write_parsed. That function reads `held` from blob_parsed inside the lock and finds the pause blob already parsed at the current version. The base blobs were parsed by the earlier rebuild. So `todo` is empty, the function returns before `stats["parsed"] += len(todo)`, and b stays 0. The rest only rewrites the same rows: tree_path is deleted and re-inserted with the same entries, _write_path_rows skips existing parsed rows, and tree_built is replaced. The dumps still match. The spec's AC2 says it is red when the waiter skips the re-read and prints a non-zero count for writer two. That red case cannot happen, so the plant and its adopt row certify S3 without testing it. S3 missing only costs a redundant write, not a wrong result, so this is high rather than blocker. | instance | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 5 | verification | tools/playbook/tag_index.py@46bfe37d:745 | medium | medium | confirmed | Partly true, and the true part stands. At 1c64f6f0, load_index connects with isolation_level=None (tools/playbook/tag_index.py@46bfe37d:519). The three write blocks open with BEGIN IMMEDIATE at 668 (build_index), 745 (build_overlay) and 784 (remove_dead_versions). Under autocommit, `with con:` opens no transaction, so deleting one of those lines makes its block a run of separately committed statements. The finder overstates one thing. Deleting line 668 does turn the queued-writers plant red. The plant's poll (gov_tag.py ~800-818) needs the lock held for 0.5 s, and in autocommit writer one holds it only for single statements, never across its 3 s parse, so the poll hits its 30 s deadline and prints 'writer one never took the write lock'. For lines 745 and 784 the claim holds. The plant's overlay runs over a clean worktree with no entries. --gc runs only single-threaded, in the plant around tools/playbook/gov_tag.py@0fd35bfa:907. No other arm tests whether either block is atomic. AC3's scratch clone is also clean and never runs --gc. So spec S2's 'Observed by AC1 and AC3' is false for two of its three blocks. This diff created the gap: at BASE, implicit transactions made each block atomic without the explicit BEGIN. The effect is contained: partial dirty_path or --gc rows after a crash, or a reader landing between statements. Medium. | sound | - | class:observed-by-claim-no-arm-discharges |
| 6 | intent | tools/playbook/gov_tag.py@0fd35bfa:826 | blocker | blocker | confirmed | I traced this at 1c64f6f0. Writer two's second load_view creates fresh stats (tools/playbook/tag_index.py@46bfe37d:807) and calls build_index. Suppose the re-read at 669-670 is deleted. Writer two's BEGIN IMMEDIATE waits for writer one to commit, then it rewrites tree_path and runs _write_parsed. That function reads `held` from blob_parsed inside the same transaction (line 586). Writer one has already recorded every blob of H at the current versions, including pause.tags, and its remove_unheld_rows sweep keeps H, so every blob counts under `skipped`, `todo` is empty, and `parsed` stays 0. The overlay adds nothing because the worktree is clean. The plant's verdict, `a > 0 and b == 0` plus print_equal, therefore still exits 0 and prints 'writer two parsed 0'. AC2's 'Red when' condition, 'a non-zero count for writer two', cannot happen, yet spec §7 names this arm as covering AC2, the only observer of S3. That is a gate leg certifying a mechanism it does not check, which the rubric grades blocker. Each fix option works. (a) Writer two's `skipped` is non-zero without the re-read and all zero with it, since the early return skips _write_parsed and the overlay is empty. (b) tree_built.built_at is restamped by INSERT OR REPLACE only when there is no re-read. Either option, with AC2's text corrected, cures the class. | sound | staged-break-substitutes-a-synthetic-value | class:criterion-asserts-what-its-own-command-cannot-show |

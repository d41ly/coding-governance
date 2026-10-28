**Serves:** journal TOOL-dSafePassage-2

# TOOL-dSafePassage-2 — acceptance ledger

The unit as built. In `tools/govkit/upgrade_steps.py`: `derive_pending_steps` (S1), `run_step_walk`
with its five moves and its post-spawn re-read (S2, S3), the attended order `write_attended_order`
(S5), the reclaim's `read_lock_holder`, `check_holder_dead` and `write_reclaimed_lock` (S7), the
staging journal's `write_staging_line` and `read_staging_journal` (S8) and the step writes' staging
(S11), and `fixture walk|lock|update [--plant <case>]` with every plant of §4 "Inventory" (S9). Three
helpers the inventory does not name: `resolve_landed_ref`, lifted out of `cmd_list` so the walk and
`list` read one default branch; `derive_step_context`, lifted out of `run_step_isolated` so the
attended order names the argv the spawn would have resolved; and `remove_shared_file`, the unlink a
racing reader on Windows refuses (below). In `tools/govkit/govkit.py`: the lock record's `host`,
`describe_write_lock` naming it, `take_write_lock` reclaiming through `write_reclaimed_lock` with the
remedy naming the reclaim (S6, S7); `RECLAIM_GUARD_SUFFIX`, `STAGING_JOURNAL_REL` and
`ATTENDED_ORDER_PREFIX`; `release_write_lock` unlinking the journal with the lock; a journal line
before every index write in `_cmd_update` and `land_through_index`; `dirty_claimed_paths` and
`demand_claimed_paths_clean` taking the reclaimed journal, and `demand_writable_target` taking the
lock before the dirty test, since the reclaim is what reads the journal (S8); the walk after the HOLD
REGION END marker with its summary line, and the read-only preview's `would walk` lines (S4); and the
stamp reading `schema` off the receipt, so it never writes over the schema a step re-read in (S3).
`help/upgrade-steps.md` gains "What `update` does with steps" (S10). `tools/govkit/selftest.py`
gains `check_step_walk`, the `New arm:` line's arm, and its `[-12] AC5` remedy needle moves from
`rm ` to the reclaim. `refusal_join.py`'s `BRANCH_PIN` moves 310 -> 314 by the measured delta.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture <family> [--plant <case>]` on node d (Windows,
Python 3.14); its repositories sit under `%TEMP%`. The arm's body, `check_step_walk`, was run outside
the suite by a scratch probe that loads `selftest.py` by path and counts its `check` calls: 22 ok, 0
failed. Each red was staged in a scratch copy of `tools/govkit` and `tools/process-monitor`, one
edit per case, the fixture run from the copy.

A BUG THE FIXTURE FOUND, fixed in the pass: under `lock-race` on Windows the winner's `finally`
unlinked the guard while the loser was reading it, and the unlink raised `PermissionError`, so the
winner held the lock and exited 1 with a traceback. `remove_shared_file` retries the unlink for two
seconds, and the guard's and the lock's `O_EXCL` creates read `PermissionError`, a file pending
deletion, as `busy`. Three runs of `lock-race` after the fix: each `[0, 1]` or `[1, 0]`, the loser
`busy`.

A FOLLOW-UP COMMIT acted on the M6 checklist. `containment-tested-one-way`: the walk staged the
paths a step's before-image lists without asking whether they sit inside the target, and the image
is the step's own output, so each path now goes through `check_contained` first. A probe of
`run_step_walk` over a step whose image lists `../x.txt` printed `'../x.txt' is not a path inside the
target, so no step may write it`; the same probe printed the walk's two other refusals, a receipt
that `does not read back after the spawn` and a `git add` that `refused the step's writes`, and
`check_step_walk` gains the escaping case beside them. `two-answers-to-one-question`: the journal's
suffix was spelled twice, in `STAGING_JOURNAL_REL` and in `release_write_lock`; both read
`STAGING_JOURNAL_SUFFIX` now. The arm's body was not re-run after the follow-up: the role hook
refuses a run that loads `selftest.py`, so its three in-process cases are owed at the close.

Owed at the close: the `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `encoding posture` and `spec tokens` legs, and the RED-first observation of
`check_step_walk`.

**Evidences:** TOOL-dSafePassage-2
- AC1 — `fixture walk`, rc 0: `step fx/s1 · applied` to `step fx/s4 · applied` in that order, the receipt's `steps` listing them so, and `walk: fx/s3 introduced at M`; `--plant not-pending`, rc 0: `s1`, `s3`, `s4` applied and `walk: canaries of s2 and s5: none`. Red staged: `derive_pending_steps` sorting the reader's rows by id, reversed, printed `walk: FAILED · the step lines are not ['fx/s1', 'fx/s3', 'fx/s4'] in that order`; dropping the `applied` filter printed `walk: FAILED · a step outside the pending set spawned`.
- AC2 — `--plant witness-holds`, rc 0: `step fx/s2 · skipped (witness holds)`; `walk: fx/s2 up canary absent · row applied`. Red staged: move 1's skip disabled printed `walk: FAILED · s2's up ran over a holding witness`.
- AC3 — `--plant fail-k`, rc 1: `step fx/s3 · failed · exit 1: fx: s3 up fails by its plant`, `s1` and `s2` `applied`, the canaries `s4.up` and every `.down` absent. Red staged: move 4 recording without stopping printed `walk: FAILED · s3's failure does not name exit 1 and its stderr line`.
- AC4 — `--plant kill-step`, rc 0: `walk: after the kill · last applied ['fx/s2'] · fx/s3 failed · interrupted: started <utc>, no exit recorded`; the re-run applied `s3` and `s4`; `walk: the re-run's target and receipt equal an uninterrupted walk's`; `fx/s3 up spawned 2 time(s) · resume not spawned`. `--plant resume`, rc 0: `step fx/s3 · applied · by its resume`, `fx/s3 up spawned 1 time(s) · resume spawned`. Red staged: move 3's persist removed printed `walk: FAILED · the kill left no interrupted failure for s3: the pre-spawn row was not persisted`; `resume` ignored printed `walk: FAILED · the re-run spawned s3's up, not its declared resume`.
- AC5 — `--plant attended`, rc 1: `step fx/s2 · failed · attended: the step needs the target's code`, the order `update-attended-step-fx-s2-387edb03.md` naming `fx/s2` and its `fx.py up` argv, `up canary absent`; after `s2`'s up run by hand, the re-run printed `step fx/s2 · skipped (witness holds)`, `step fx/s3 · applied`, `step fx/s4 · applied`, rc 0. Red staged: the attended test disabled printed `walk: FAILED · s2 is not failed attended`.
- AC6 — `fixture update`, rc 0: `step fx/s1` and `step fx/s2` at output lines 10 and 11, after the write loop's `tools/demo/one.txt` line (6) and before `govkit update — re-render` (13); `govkit update — steps: 2 pending · 2 applied · 0 skipped · stopped at none`; `gov_commit` at B; `git diff --cached --name-only` naming `s1.txt`, `s2.txt` and both before-images. `--plant read-only`, rc 0: `would walk fx/s1`, `would walk fx/s2`, `step canaries none`. `--plant scoped`, rc 0: `steps: not walked — a --kits run walks no step, ... · 2 pending`, no canary. `--plant update-fail`, rc 1: `gov_commit A · steps {'fx/s1': 'applied', 'fx/s2': 'failed'} · tools/demo/one.txt b'v2\n'`, no `.down` canary. Red staged: the stop's `r.fail` turned into a print printed `update: FAILED · a stopped walk let the stamp move`; the `--kits` test dropped printed `update: FAILED · a step spawned on a read-only or scoped run`.
- AC7 — `fixture lock --plant lock-dead`, rc 0: `govkit update — reclaimed ...: its holder, pid <n> on host <h> ..., no process on this host has pid <n> any more`, the lock naming the taker's pid and `host`; `lock-reused`, rc 0: `pid <n> now names a process started after the lock was taken, a reused pid`; `lock-live`, `lock-foreign-host` and `lock-unreadable`, rc 1 each: `another govkit write holds` with the holder described and `reclaimed by the next run` in the remedy, the planted lock unchanged. Red staged: the live row read dead printed `lock: FAILED · a refusing take changed the lock` under `lock-live`; the reclaim disabled printed `lock: FAILED · the dead holder pid <n> was not reclaimed, naming it` under `lock-dead`.
- AC8 — `--plant lock-race`, rc 0: `lock: racers exit [0, 1]`, the lock naming the winner, the loser `busy, the lock changed while this run judged it: another run took it`. `--plant guard-dead`, rc 0: `busy, cleared the guard .update.lock.reclaim, whose holder, pid <n>, is no longer running`; `lock: first take exits 1 · guard cleared · lock unchanged`; the second take reclaimed. Red staged: clearing a dead `.reclaim` guard and reclaiming in one call printed `lock: FAILED · the first take did not clear the dead guard and refuse busy`.
- AC9 — `fixture update --plant kill-walk`, rc 0: `update: after the kill · journal ['tools/demo/one.txt'] · staged ['tools/demo/one.txt']`, the `.update.lock.staged` paths equal to the staged set; the re-run printed `govkit update — reclaimed ...`, walked `s1` and `s2`, and `update: the re-run's bytes equal an uninterrupted run's`. `--plant kill-walk-edit`, rc 2: `1 path(s) this target's receipt claims are DIRTY: tools/demo/one.txt`. A probe of `dirty_claimed_paths` over a scratch repo: with no journal `['a.txt', 'b.txt', 'c.txt (deleted from the index, still in HEAD)']`; with `.update.lock.staged`'s mapping (a's oid, another oid for b, a deletion for c) `['b.txt']`. Red staged: `land_through_index`'s journal line removed printed `update: FAILED · the staging journal's paths do not equal the staged set`; carve-out 3 accepting any blob printed `update: FAILED · the re-run did not refuse the operator's different blob at a journaled path as dirty`.
- AC10 — `git grep -n -e "would walk" -e "update-attended-step" -e ".update.lock.staged" -- "help/upgrade-steps.md"` names all three inside "What `update` does with steps".

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_walk`, cut to `walk fail-k` and `update update-fail`. Break: `run_step_walk` no longer stops after a failed up. RED: `FAIL [dSP-33] fixture walk fail-k exits 1 and names step fx/s3 · failed · exit 1: fx: s3 up fails by its plant, …` with the fixture line `walk: FAILED · s3's failure does not name exit 1 and its stderr line`. `update-fail` stayed ok. GREEN restored: both arms ok. Inconclusive at HEAD: this unit's three in-process arms `[dSP-2] S2 the walk refuses a spoiled|unstaged|escaping step, naming it` fail on both sides. The refusal they get is `git -C …/gk-walk-ref-… rev-parse --absolute-git-dir exits 128: fatal: not a git repository`, because their scratch target is not a repository. That `rev-parse` call dates from `015fa02e3` (TOOL-dSafePassage-30); I did not run those arms at an earlier commit.

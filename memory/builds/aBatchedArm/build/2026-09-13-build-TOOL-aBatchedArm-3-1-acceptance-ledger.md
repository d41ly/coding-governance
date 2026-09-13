# TOOL-aBatchedArm-3 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-3

Written as the readings were taken, not after. Every long run went on a frozen `git clone --local`
under `C:/Users/daily-agent/AppData/Local/Temp/u3/` with stdout and stderr redirected to a file and
`date +%s` stamped beside it. The runner helper is `u3/runsuite.sh`: it runs the suite under `bash -x`
with `PS4='+$EPOCHREALTIME L$LINENO: '` and `BASH_XTRACEFD=9` to a separate trace file, so the
floor-graded `$n` can be read from a RED run (at BASE the suite prints it only on `PASS` or on a floor
breach, and the suite is RED at BASE) and so wall time can be attributed to the LINE it was spent on.
The trace shares no fd with anything an arm captures and the child checker never inherits `-x`; the
ledger says which runs were traced.

## Host state

The box was NOT idle when this unit started, 2026-09-13 19:25 local: `ps -ef` showed another
session's five `check-unattended.test.sh --shard 2/2` runs (started 18:36 under
`$TEMP/ar2/`), one unsharded `tip/check-unattended.test.sh`, a `run-gates.sh` bar (19:23) and a
`run-gates.test.sh`. Every UNTIMED run below was taken beside them; every TIMED reading names the
`ps` answer beside it, and a reading taken beside another bar is written as NO READING. Measured
while they ran: one checker invocation inside the suite cost 75 to 115 s (trace gaps at the
`run` line), against the ~2 s `TOOL-aTracedSpawn-2` bounds it at on an idle box and the ~30 s the
existing budget row's 9067 s reading implies — the process-spawn path is shared, so the box's
throughput, not its core count, is what every run below divided.

## Runs

- `s2base` — the unsharded run at BASE `0422ea2e` on clone `u3/base` (suite blob
  `29b8175b`), traced, started 19:36 local after a first start at 19:27 was killed to add the line
  stamps to the trace. Yields AC12's baseline `FAIL` set, AC6's pre-split floor-graded count, and
  the per-line seconds the cut was balanced from.
- `s3c1` — the unsharded run at commit one `94a6b677` on clone `u3/c1` (suite blob `cd3533cc`),
  traced, started 19:36. Yields AC12's post-delete `FAIL` set.

## The hoist population, derived

`awk` over the commit-one file for `^[A-Za-z_][A-Za-z0-9_]*\(\) *\{` between the first `in_shard`
line and the floor line: 27 definitions (`dispconf mkdisp drop_readme break_fm break_slug noop_break
_bm_sections wreset drive wline kick_engine _bm31 _mkskill pedit frozen add_mode add_bad_mode
add_recipe_seam add_recipe_mode gut_parser seed_ros add_u7 rrow drow drows gdrows land_as`). The
spec's rev-4 figure of 28 counted the `fail() { :; }` string inside a `for _hijack in` loop, which is
not a definition. All 27 are hoisted; the transformation is `xform.py` (scratch, reproducible from
the commit-one blob) and the arm lines it leaves are byte-identical to commit one's except the one
`same` S6 adds.

**Evidences:** TOOL-aBatchedArm-3
- AC5 — the ported join, exercised first as bare awk over crafted rows (every direction: complete
  1..8 clean; index 5 deleted names `no row for index 5`; index 3 twice; index 9 of 8; two arities
  8 and 2; a malformed `x/y`; a whole-called row alone clean), then as arms of
  `bash tools/run-gates/run-selftests.test.sh`: `a deleted shard row reds the join NAMING the
  missing index, rather than seven green rows` (rc 1, `no row for index 5`) and `a suite that
  declares SHARD_ARITY and is called WHOLE is not graded by the join` (rc 0, `declaration clean`),
  with the existing ratio arm now staging the COMPLETE set of eight so it stays green under the
  join. `PASS (55 arms, width 1)`, floor moved 53 to 55. RED observed: with `shard_faults=""`
  staged after the awk, the suite reported exactly `FAIL (1 of 55 arms)` — the deleted-row arm
  got rc 0 and `declaration clean — 9 row(s)`; unstaged, 55 of 55 again. The real-tree half of
  this criterion (`--check` green with the eight rows and the driver row) is read at commit three.
- AC12 — the head sets, with the SHIPPED function bodies: a fixture built the way the prologue
  builds it (bare origin with a HEAD symref, `main` pushed, `unit` branched, `ANCHOR0` and
  `PRISTINE` set), the two leaks planted exactly as the arms plant them (`git push -q -f origin
  "$ahead:refs/heads/ahead"`; `git branch -f trunk main` then `git push -q origin trunk`), then
  `reset_tree` taken by `sed -n '/^reset_tree() {/,/^}/p'` from the commit-one blob and `eval`'d.
  Planted: origin `[ahead main trunk]`, local `[main trunk unit]`. After commit one's `reset_tree`:
  origin `[refs/heads/main]`, local `[refs/heads/main refs/heads/unit]` — the fresh set in both
  stores. The failing case, same fixture, BASE's body `eval`'d the same way: after its
  `reset_tree` the origin still carries `[ahead main trunk]` and the clone `[main trunk unit]` —
  all three leaks survive, which is what the delete exists to stop. The `FAIL`-set half of this
  criterion is `s2base` against `s3c1` and is written below them when both end.

## The second pass — under the 2026-09-13 owner ruling

The first pass was stopped for running suites per step; its edits are the checkpoint `cbf8ebce`
and nothing in it had been graded. `s2base` and `s3c1` above ended with no reading written, so
every figure they were to yield is re-taken in Phase B below. This pass runs NO suite before
Phase B, and Phase B is one verification pass.

**Phase A, the static half.** Dispatch re-declared at `77f3946f` with `memory/guides/SESSION-KICKOFF.md`
added, which the checkpoint touched and the first row did not name. Kept from the checkpoint:
the cut, the 27 hoists, `topo_capture` at boundaries 2..8, `replay_landed_main` at 4, the `MUT`
counter with `MUT_EXPECTED=13` (re-counted: 13 non-comment `reset_tree` calls from the
declaration to the control, the control's own `reset_tree` included), eight placeholder floors,
the join and its two arms, both notes. Added: the eight budget rows at the old row's `13600`
as PLACEHOLDERS naming themselves so, the carried count `14 -> 21` raised by hand with its
reason, and a `CHECK_UNATTENDED_PLANT` hook in the prologue, because AC8's negative needs the
derived leaked set PLANTED before a shard's opening capture and the fixture is built inside the
process where nothing outside can reach it. Inert unless set.

**The three carriers, scanned at the eight-region cut (S5):**
- functions — `awk` for `^name() {` between the first `in_shard` line and the floor line: 0
  definitions remain inside any region; the 27 are in the prologue.
- variables — two readings of one scan (`varscan.py`, scratch): a variable read in a region that
  never assigns it while another region does: 0; order-aware, a variable read in a region before
  that region's own first assignment while another region assigns it: 0. 27 variables are
  prologue-assigned and read in regions, which is the direction a cut cannot break.
- refs — traced by reading every `push`/`branch -f`/`checkout main`/`merge` line. Region 3's
  lifecycle control (the text `land the run`, pushed) leaves `unit` an ancestor of `main` in BOTH
  stores and its closing `reset_tree` moves neither `main`; region 4's tWaive tail (the text
  `git reset -q --hard "$ANCHOR0"; git push -q -f origin main`) restores both. Every other ref move
  in regions 1..8 is an `anchor_break`/`anchor_restore` pair or an in-arm restore. Predicted:
  boundary 4 owes the replay, boundaries 2, 3, 5, 6, 7, 8 match a fresh start. Derived leaked set
  per boundary: `{ahead}` at 4..8 (pushed at the text `"$ahead:refs/heads/ahead"` in region 3),
  EMPTY at 2 and 3 (`trunk` is created in region 8 and leaks past no boundary). Phase B run 2's
  captures are the observation; this is the prediction they are checked against.

Gates run in Phase A, seconds each, none a suite: `run-selftests.sh --check` — `declaration clean
— 68 row(s)`; `--kit tools/unattended/check-unattended.test.sh --list` — exactly the eight rows,
`declared total 108800s`; `check-install-prefix.sh` — RED first (`ROSE tools/run-gates/selftest-budgets.txt 14 -> 21`,
the brief's predicted red), then clean after the hand raise; `check-line-length.sh` OK;
`check-arms.py --check` rc 0; `run-gates.gov.test.sh` `PASS (16 assertions)`; `bash -n` on the suite.

## What this ledger does not evidence

Pending Phase B.

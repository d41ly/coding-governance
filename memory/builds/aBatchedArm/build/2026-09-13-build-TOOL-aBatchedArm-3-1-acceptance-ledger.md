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

## Phase B — the one verification pass

**Harness.** Four frozen `git clone --local` trees under `C:/Users/daily-agent/AppData/Local/Temp/u3b/`:
`base` at `0422ea2e`, `head`, `brk` and `pool` at the Phase A commit `43a0a2d6`. `one.sh` runs the
suite once, direct, no trace, stdout+stderr to a file with `date +%s` stamps either side; the
environment is the caller's. **The BASE clone carries ONE staged line**: HEAD's
`echo "  ($n assertions executed in $MODE against a floor of $FLOOR)"` inserted before the floor
grade — the suite is RED at BASE and prints its floor-graded count only on `PASS` or a floor breach,
so without it AC6's pre-split count is readable nowhere; an `echo` moves no verdict, and the first
pass's alternative, an exported `BASH_XTRACEFD`, leaked into every child `sh` as stderr the arms
capture, which is why its traced runs cannot supply a FAIL set. **Run 2 is direct, not through
`run-selftests.sh --serial`**: that loop captures each suite into `out=$(...)` and prints four FAIL
lines of it, so the counts, FAIL sets and captures the brief expected from it do not exist in its
output; the direct loop runs the same argv with the same clock, one after another, and keeps every
byte. The runner's own `--serial` pass over the eight rows is taken as well, for the budget readings
in the runner's spelling. **Box state before every timed run** is a `ps` count printed first.

**Declared before run 2 — the balance tolerance:** `max(shard) <= 1.35 × (sum / 8)` on the serial
walls. The pooled wall the goal grades is the longest shard, so anything looser than about a third
over the ideal is a re-cut that buys back more than its one permitted repeat costs; anything tighter
asks a cut confined to `reset_tree`-led edges for a balance it may not have.

**Host state at Phase B start.** `ps -ef` at 22:52 showed another session's
`run-gates.turnstile.test.sh` (started 22:44, `claude-da35-cwd`, not this session's) with its bars;
not mine to kill, so Phase B waited for it. That session (`unattended-asurfaced-lexicon-7cf573`)
went on to `run-gates.test.sh`, `run-gates.evidence.test.sh`, a full `GATE_SELFTESTS=1 GATE_JOBS=4`
bar at 23:22, another at 00:29, and a `.githooks/pre-push` bar on the primary tree at 02:07; a third
tree (`backlog-items-build-c4c36b`) ran `check-memory-hygiene.test.sh` at 23:41. The first clear
window was 00:03, and run 1a started in it.

**What this node costs per checker invocation, measured in this pass.** With the box at 5 % CPU
and no other session's process running (04:03), one `run` — the suite's `bash check-unattended.sh`
over the fixture — took 47 to 60 s wall (`ps` stamps on the child, 04:03:18 → 04:04:05 and on).
The suite makes 293 of them, so an unsharded run on node `a` is ~4 to 5 hours whatever the load;
the 9067 s budget reading was not a contended figure, it was this node. The `~2 s` per invocation
`TOOL-aTracedSpawn-2` bounds is not what this box does, and the HEAD unsharded run's own
`topo-at` stamps agree: `t=2933 n=81` at boundary 2, `t=6747 n=139` at 3, `t=8397 n=177` at 4 —
36 to 43 s per assertion, with two to four suites of mine and at most one other session's bar
present. Concurrency between suites moved that figure little, which is the throughput-bound
regime `TOOL-aPacedTurnstile-8` measured and the one AC4 grades.

**Run 1a — the unsharded run at BASE** (`b1-unsharded`): started 00:03:45 with `ps before: 0`,
ended 05:50:43, wall 20817 s, rc 1, **554 assertions executed in unsharded against a floor of
392** (the staged echo), 21 `FAIL` lines, 0 fork-noise lines, the C21 pair and `rc=` after the
count line, so the run reached its end. The 21 lines are the suite's pre-existing red: the
dispatched-verb surface arm, the DoD-floor pair (`11 against 12`), the killed-remote-observation
arm, and the seventeen `fixture no-op` / `missing` lines of the protocol-count and declared-parser
blocks (`TOOL-aQuenchedHarness-9`, `TOOL-aHoistedPass-38`, not this unit's). This set is AC12's
baseline and 554 is AC6's pre-split count.
**Run 2u — the unsharded run at HEAD** (`b2-unsharded`, `CHECK_UNATTENDED_TOPO=1`): started
01:14 beside run 1a, untimed, ended 07:03:54, wall 20977 s, rc 1, **555 assertions executed in
unsharded against a floor of 392**, 21 `FAIL` lines, 0 fork-noise lines, seven `topo boundary=`
lines. The 21 lines are BYTE-IDENTICAL to run 1a's (sorted set comparison, `analyze.py`): the
delete, the cut, the hoist, the replay and the counter moved no unsharded verdict. 555 against
554 is the ONE assertion S6 adds — the `same` over `MUT`/`MUT_EXPECTED` — and nothing else, so
AC6's "equals the pre-split count" holds as 554 + 1 and the rev-8 line says so. The seven
captures, verbatim: boundaries 2, 3, 5, 6, 7, 8 read `origin=[refs/heads/main ]
local=[refs/heads/main refs/heads/unit ] unit<main=no unit<origin-main=no`; boundary 4 reads the
same name sets with `unit<main=yes unit<origin-main=yes` — exactly the prediction, and the one
boundary that owes the replay. `topo-at` stamps: `t=2933 n=81` · `t=6747 n=139` · `t=8397 n=177`
· `t=11804 n=254` · `t=13734 n=318` · `t=15663 n=393` · `t=18598 n=506`. **AC4 arm one, attempt 1** (`attempt1/b1-s1of2`, `b1-s2of2`): the
pair started 02:03:36 with no other session's process on the box and this pass's two unsharded runs
named as the only load; the primary tree's `pre-push` bar arrived at 02:07:27, four minutes in. At
03:05, with region 1 of shard 1 not yet through, both were stopped (rc 143, wall 3665 s, no
trailer) — **NO READING**, and the pair is re-taken in a clean window. **Run 2 — the eight shards,
direct, serial, TOPO=1** (`b2-s1..8`): started 04:05:46 beside this pass's two unsharded runs and no
other session's process, ended 08:27:03. Every shard carries its trailer. Per shard — wall · count
· FAIL lines · condition:

| shard | wall s | count | FAIL | beside |
|---|---|---|---|---|
| 1 | 3176 | 81 | 3 | both unsharded runs |
| 2 | 2182 | 58 | 1 | both unsharded runs |
| 3 | 2320 | 38 | 0 | both unsharded runs |
| 4 | 3028 | 77 | 0 | both unsharded runs (1a ended 05:50 inside it) |
| 5 | 1127 | 64 | 6 | the HEAD unsharded run, then the BASE pair from 07:04 |
| 6 | 1059 | 75 | 0 | the BASE pair |
| 7 | 1877 | 113 | 11 | the BASE pair, and `session-orientation-tooling-2faa`'s `run-gates.test.sh` from 07:51 |
| 8 | 893 | 49 | 0 | the same |

- **AC1** — `81+58+38+77+64+75+113+49 = 555`, and run 2u's floor-graded count
  is 555. EQUAL, `PROLOGUE_ARMS` 0. The partition is also visible in run 2u's own `topo-at`
  stamps: `n=81, 139, 177, 254, 318, 393, 506` are exactly the running sums.
- **AC6** — the union of the eight `FAIL` sets is 21 lines and is IDENTICAL, as a sorted set, to
  run 2u's 21; per region the split is 3 · 1 · 0 · 0 · 6 · 0 · 11 · 0 in both. Count: 555 against
  the pre-split 554, the S6 assertion (above).
- **AC8, the positive half** — every shard's opening capture is byte-identical to run 2u's line at
  that boundary: 2, 3, 5, 6, 7, 8 fresh, 4 `unit<main=yes unit<origin-main=yes` after
  `replay_landed_main`. Seven MATCH, none differ. (Shard 1 has no boundary.)
- **Balance, as declared** — sum 15662 s, mean 1958 s, max 3176 s (shard 1), `max/mean = 1.62`,
  OUTSIDE 1.35. The walls are CONFOUNDED by the load shift inside the pass: shards 1–4 ran at 39,
  38, 61 and 39 s per assertion beside two unsharded runs, shards 5–8 at 17.6, 14.1, 16.6 and
  18.2 s beside two shard runs. Normalising 1–4 to the lighter rate (`~17 s/assertion`: 1380 ·
  990 · ~650 · 1310) the max moves to shard 7 (1877 s against a mean of ~1160) and the ratio is
  still ~1.6 — region 7 carries 113 of 555 assertions, one fifth of the suite. The verdict is
  OUTSIDE on both readings, so the re-cut and the one permitted repeat are owed. The per-block
  profile that decides the new cut is `prof-s7` below; the walls above are recorded as the FIRST
  candidate beside the chosen one.

**AC4 arm one, attempt 2 — the two-shard reading at BASE** (`b1-s1of2`, `b1-s2of2`): two
concurrent direct invocations on the BASE clone, started 07:04:39 with `ps before: 7` — that count
is this pass's own serial shard (5/8 at the time) and its children, no other session's process;
`session-orientation-tooling-2faa`'s `run-gates.test.sh` ran beside it 07:51 to ~08:20, and the
`prof-s7` profile below from 08:30. **shard 1/2: 4193 s, rc 1, trailer present, 4 FAIL lines** ·
**shard 2/2: 6656 s, rc 1, trailer present, 17 FAIL lines** — both READINGS by the trailer rule,
4 + 17 = 21 the pre-existing set, 0 fork-noise lines. The two-shard longest is **6656 s**.

**The per-block profile of region 7** (`prof-s7`, a scratch clone at the Phase A commit with an
`echo "nmark L<line> n=$n t=$SECONDS"` before each of region 7's 47 `reset_tree`-led lines, run as
`--shard 7/8`, 08:30 to 08:55, wall 1546 s, 113 assertions, 47 marks): the first half (L2560 to
L2705, 63 assertions) costs 498 s and the second half (the check-28 round-2 `mutate` arms) 1048 s,
at 36 to 107 s per two-assertion block. At the `# ---- 28c.` header (first `reset_tree` L2770 of
that copy) the counters read `n=93 t=1119`, so the tail past it is 20 assertions and 427 s.

**The re-cut, one boundary.** Region 8 now begins at that header: region 7 keeps 93 assertions,
region 8 takes 69. Every other boundary is where it was, so six of the seven captures already
observed stand; boundary 8's is re-observed by the repeat's unsharded run. The prediction from the
normalised walls (shards 1–4 divided by the 2.3 load ratio measured across the pass: 1380 · 950 ·
1010 · 1320, then 1127 · 1059 · ~1119 · ~1320): max ≈ 1380 against a mean ≈ 1160, `~1.19`,
inside 1.35. Region 7 carries no `push`, `branch -f`, `checkout main` or `anchor_*` line, so the
topology at the new edge is boundary 7's; the variable scan re-run on the re-cut file reports 0
crossings on both readings, and `check-arms.py --check` is green.

## What this ledger does not evidence

Pending Phase B's repeat.

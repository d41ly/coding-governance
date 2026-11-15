# aTrimmedWait — the new arms observed red and green by the main loop

**Serves:** journal TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10

Observed by the main loop on node a, 2026-11-14 and 2026-11-15, on a frozen clone of `057f26ba4`,
one suite at a time with nothing running beside it. Every `New arm:` line of the nine specs.

## What ran

- RED at base: each suite at `057f26ba4` with its production file checked out at the build's base
  `846d51d39`, the "RED at base" several specs name. Suites: scratch-guard, roles adopter, branch
  guard, unattended-build, memory hygiene, and the unattended driver suite's shards 3 and 4, where
  units 1 and 5 put their arms.
- RED on staged breaks, for arms green at base or whose suite lives in the file it tests:
  `gen_build_index.py --selftest` under four breaks (G1 the staged mode falls through to a plain
  write; G2 every artifact counts as moved; G34 the early view decline, the `finally` restore, the
  `.lock` admission and the orphan staging each removed; G6 the staged-write check skipped);
  scratch-guard under S9a (the comment cut removed) and S9b (cut at any `#`); the roles adopter under
  R7 (the record's prefix and parser no longer compared).
- GREEN: every one of those suites on the clean clone at `057f26ba4`.

## What it read

| Unit | Arm | RED | GREEN |
|---|---|---|---|
| 1 | driver suite, `--check-specs` (AC1 AC2) | shard 3 at base: `check-specs: a clean untracked build exits 0` and 9 more FAIL lines | no `check-specs` FAIL line |
| 1 | unattended-build suite, TW1 (AC5) | at base: 6 `TW1 AC5` FAIL lines | `PASS (1460 assertions)` |
| 2 | hygiene suite, scoped check 12 (AC1-AC3) | at base: 9 `scoped` FAIL lines, among them `--build tOne exited 2` | no `scoped` FAIL line |
| 3 | `test_staged_write` (AC1-AC4) | G1: every `TOOL-aTrimmedWait-3 AC1` to `AC4` arm FAIL | `PASS — gen_build_index: all arms held` |
| 3 | branch-guard suite (AC5 AC6) | at base: `AC5 a check 9 refusal runs --write-staged` and `AC6 a declined render` FAIL | `43 passed, 0 failed` |
| 4 | `test_write_moved` (AC1-AC3) | G2: all three `TOOL-aTrimmedWait-4` arms FAIL | as unit 3 |
| 5 | driver suite, TW5 (AC2 AC3) | shard 4 at base: the four `TW5` FAIL lines, the empty-batch one included | no `TW5` FAIL line |
| 6 | scratch-guard rows R1-R7 (AC1-AC3) | at base: all seven `W-AC2` rows FAIL | all new rows `ok` |
| 7 | arm 23 (AC1 AC2 AC4 AC5) | at base: five rows of arm 23 FAIL | `PASS (88 assertions)` |
| 7 | arm 23 (AC3 AC6) | R7: the transcript-edit and foreign-key rows FAIL | as above |
| 8 | `test_staged_write` (AC1-AC3) | G34: AC1, AC2 and both AC3 rows FAIL | as unit 3 |
| 8 | `test_staged_write` (AC4-AC7) | G34: AC4, AC5, AC7 FAIL; G6: the foreign-index row carrying AC6 FAIL | as unit 3 |
| 8 | hygiene suite, tThree and derived keys (AC8 AC9) | at base: `--spec tThree-1` and `no *_CUTOFF key derived` FAIL | no FAIL line for either |
| 9 | scratch-guard C1-C6 (AC1 AC2) | at base: C2, C4, C5, C6; S9a: C1, C3, C6; S9b: C5 | all new rows `ok` |
| 9 | scratch-guard F1-F7 (AC4) | at base: F1 to F5 FAIL | all new rows `ok` |
| 9 | arm 23 rewrite (AC7) | at base: the append and torn rows FAIL | as unit 7 |

## What was not observed

- Unit 7's unwritable-folder row was read green under every break: no coherent break of the record
  code makes a cold read fail there, so it is an arm that guards a fallback and has no red case here.
- The driver suite whole and the `unattended kit gate` leg: shards 3 and 4 only; the bar runs all.
- The breaks named one per arm were folded into the combined breaks above, not run one at a time.

## Inherited, not this build's

- scratch-guard: the seven `S-AC2` to `S-AC8` rows fail in every run, the base runs included; spec 6
  names the suite as red on the held job under TOOL-aCarriedStop-7.
- memory hygiene: seven rows say the shipped conf example declares no `OSTYPE` or `RECALL_*` key the
  memory-tree modules read; those readers predate the base (the id grammar moved in at `2d03321ab`),
  and this build adds only `STAGED_RENDER` to the example.
- Driver shard 3: `TOOL-aFrugalTurnstile-12 AC3` (the scrub list against `GATE_REGEN_CHECK`) and the
  redefined `write_bar_green` row, the same at base. Shard 4: the five check-118 rows reading the
  clone's default-branch side, the same at base.
- Shard 4 GREEN alone read two `missing: pid-alive: yes` rows in the `--liveness` arms, which compare
  a lease stamp to a background sleep's start time; the build touches no pid, lease or liveness
  code, so this is timing in the clone, and the bar re-reads it.

## TOOL-aTrimmedWait-3's AC9 and AC10, observed by the main loop

Two clones, the hook pointed at each clone's own `.githooks`, one staged status flip of
`memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-6.md` in each:

- Unit clone at `057f26ba4`: `git commit -m probe` exited 0 in 313.5 s and the commit carries the
  build README. <!-- PINNED 2026-11-15 -->
- Base clone at `846d51d39`: the same commit exited 1 on the check 9 refusal in 162.7 s; its remedy,
  `--write`, `git add` and the second commit, took 187.8 s more. <!-- PINNED 2026-11-15 -->
- AC10: the unit clone with `STAGED_RENDER` blank exited 1; its hygiene lines equal the base clone's
  line for line, and the one added line is the hook's decline.

## TOOL-aTrimmedWait-10's arms, observed by the main loop

Frozen clones of `ff4242f8b`, one suite at a time, 2026-11-15:

- RED under G10, `check_staged_write` reading the switch from the conf key again:
  `gen_build_index.py --selftest` exited 1, and its three unit-10 arms failed, the two AC3 arms among
  them. The unit-3 staged arms failed beside them, since no conf key turns the render on any more.
- RED with `check-memory-hygiene.sh` checked out at `49cdded06`: the unscoped `--only 2` arm failed on
  the unbound variable. The run was stopped once that arm had failed, as every later arm of that
  engine fails the same way and each scoped run walks the whole tree.
- GREEN: `gen_build_index.py --selftest` exited 0, all three unit-10 arms ok. The hygiene suite
  exited 1 on eight rows, none of them unit 10's: the seven conf-example rows listed under
  "Inherited" above, and the partition arm below.

## Found at the close: the partition arm reads a warm cache

The hygiene suite's partition arm compares the unscoped run's lines with the union of the scoped
runs' lines, and check 26's line carries `cache hits N`. On a cold clone the unscoped run goes first
and reads 0, then the scoped run of check 26 reads the cache that run wrote and prints 4, so the arm
reds on every fresh checkout and stays green in a tree whose check 26 cache is already warm.

It is inherited: the arm came in with `TOOL-aSparedSpawn-7` and the field with
`TOOL-dDerivedDocket-9`, both ancestors of the base `846d51d39`, and this build moves neither the arm
nor `tools/memory-tree/transition_audit.py`. The owner ruled on 2026-11-15 to repair it here anyway,
as `TOOL-aTrimmedWait-11`.

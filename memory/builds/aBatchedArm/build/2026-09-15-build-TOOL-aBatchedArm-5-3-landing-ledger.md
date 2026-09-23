**Serves:** journal TOOL-aBatchedArm-5 TOOL-aBatchedArm-1 TOOL-aBatchedArm-2 TOOL-aBatchedArm-3

# aBatchedArm — landing ledger: the build's one gate pass, the pooled DoD pass, and the flip

The owner's rulings of 2026-09-13 and 2026-09-14 moved every suite run to ONE pass after all five
units were built. This record is that pass, in the order `RUN.md` pinned: the gate pass, the eight
direct shard runs and the paste (step 0), the calibrate and its evidence (steps 1–2), the pooled
parity pass (step 3), the staged breaks the unit ledgers owed, and the flip (step 4). Every figure
below is read from a run's own output; the outputs sit under `<git-dir>/gate-logs/` (the bar and the
pooled pass) and in this record (the direct runs). The rows in the `Evidences` blocks at the end
answer the acceptance criteria the four unit ledgers left AMENDED; those ledgers are not rewritten,
this record supersedes their amended rows by date.

## The final gate pass — `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at 72f54937

2662 s wall on node a, 107 legs, 4 red, run detached from a PowerShell `Start-Process` after the
harness's own background job died at 72 minutes (the second attempt; the first, at 0d983990, also
found the shell-hygiene leg red, fixed in 72f54937 by reading the evidence file once into a
variable). The four reds, each analysed rather than re-run into green:

- `memory-hygiene self-test` — killed by its 900 s ceiling under the 8-wide bar; run alone
  afterwards on the same tree: PASS (394 assertions), 2765 s. A ceiling breach under contention,
  not a red suite.
- `install-prefix self-test` — exit 1 under the bar (a `comm`-sort flake in one arm); green alone.
- `govkit selftest` — 31 FAILED, `update classifies an out-of-date engine row as stale …`; it fails
  on a frozen clone of origin/main's tip too, and the cause is the environment
  (`GOVKIT_NO_REMOTE_PROBE`), not this build. Reported to the owner in the landing report.
- `unattended kit gate` — read at the time as check 23 (its two report rows name TOOL-dRetiredFork-15
  and -17 dispatches); the FAILED lines were check 24's, two LATE rescope rows this run owed for
  units 2 and 3, found and recorded at the landing (63612e99, below). The kit gate is green there.

Every leg the unit ledgers owed to this pass is green in it: `run-selftests self-test` (PASS 112
arms, width 1 — unit 5's fixture ACs), `unattended arms-groups selftest` (PASS 35 — unit 2's AC6),
`check-arms selftest`, `every held leg is budgeted, every budget row resolves`. Neither
`tools/run-gates/run-selftests.sh` nor `run-selftests.test.sh` moved after 72f54937 (the merge of
4cf0944d touched neither), so those logs stand for the landing tree.

## Step 0 — the eight direct shard runs, the paste, the floors

Eight concurrent direct invocations of `check-unattended.test.sh --shard k/8` on a frozen
`git clone --local` at 72f54937, `ps before: 0`: 3420 · 3406 · 3175 · 3734 · 2891 · 3152 · 3256 ·
3762 s (the box was carrying the memory-hygiene self-test and the tail of the bar). Every shard
printed its trailer. The fourteen `check_emitted "?"` sentinels each printed their
`FAIL check_emitted: expected set not yet observed — owed at the final pass · call at line N` line
with the `    observed:` lines beneath; `paste_sets.py` resolved every observed line to the longest
checker signature it contains (interpolation-stripped, `check-arms.py`'s rule), 14 calls → 14 sets,
no unresolved line, pasted at 7549981a with the run named beside each call. The seven affected
shards re-run on a clone at 7549981a (1304 · 1290 · 1126 · 1597 · — · 1126 · 1186 · 1635 s; shard 5
carries no set): zero `FAIL check_emitted:` lines, and the union of the eight shards' `FAIL` lines
sorted is byte-identical to the 21-line oracle (`fails-base.txt`, the unsharded FAIL set unit 3
established). The union is the same 21 at 72f54937 with the sentinel lines removed. Executed
counts 83 · 59 · 40 · 78 · 64 · 78 · 95 · 80 (sum 577 = unit 3's 555 + the fourteen calls + main's
eight merged arms); floors re-read ~3 % under at 9069512b; shard 8's budget row re-measured
(D13) to `measured 1635s … x1.5` = 2460.

## The reboot, and the second merge

The first calibrate (launched at 9069512b, 01:36) died 53 minutes in to a Windows Update restart
at 02:29–02:32 (KB5129195): 15 of 16 verdict files written, the driver suite mid-run, the runner's
EXIT trap never reached, the evidence file byte-unchanged, and the wrapper's rc file reading `0`.
Before relaunching, `git fetch` showed origin/main at 4cf0944d — the aProbedUnit build, unattended
kit 1.21 → 1.22, 78 files, landed after this build's first reconcile at 286b62d1. The flip is
observed on the tree that lands, so the relaunched calibrate was killed at 5 minutes and origin/main
merged again (519eab89): two conflicts, `check-unattended.test.sh` (main re-bodied `mkdisp` with
`DISPDATE`; the hoisted copy took the delta, the old site kept our comment; the eight-shard floors
kept whole with main's +10 assertions noted) and the manifest header (main's newer `last-audit`
datetime at the shared base, our `watch:` superset, our `last-body-change`); every other shared
file auto-merged additively; `memory/LIVE.md` re-rendered; the post-merge re-stamp at 4cf0944d
(a117faeb, delta none). Step 0 re-run at a117faeb, 8-wide on the now-idle box: 677 · 807 · 569 ·
889 · 517 · 570 · 603 · 922 s, executed 83 · 69 · 40 · 78 · 64 · 78 · 95 · 80 (main's ten all in
region 2), FAIL union still the 21-line oracle, no `check_emitted` red; `FLOOR_SHARD_2` 57 → 67 and
`FLOOR_ASSERTIONS` 559 → 569 at fd6dc1fd.

## Steps 1–2 — the calibrate at fd6dc1fd, and its evidence

`bash tools/run-gates/run-selftests.sh --kit tools/unattended --pooled --calibrate`, detached,
`ps before: 0`, 2099 s wall under the 21380 s serial-sum wall, `tree fingerprint MATCHED before and
after`, `calibrated 16 row(s), 7 red, graded none`, sixteen `pooled@8x1` rows on node `a` written
and committed at 177c1725 with `--check` green (`16 pooled evidence row(s) well-formed, trailer arm
graded 14 row(s) under pooled-kit tools/unattended (2 declared no-trailer)`):

```
READ  unattended adopter e2e                            50s  rc 1, 10 FAIL, 85 executed
READ  unattended arms-groups selftest                    4s  rc 0, 0 FAIL, 35 executed
READ  unattended brief-recorded selftest               113s  rc 0, 0 FAIL, - executed  (declared trailer-less)
READ  unattended cross-component                       151s  rc 0, 0 FAIL, 21 executed
READ  unattended driver selftest                      2063s  rc 1, 54 FAIL, 1076 executed
READ  unattended gate selftest shard 1/8               792s  rc 1, 3 FAIL, 83 executed
READ  unattended gate selftest shard 2/8               991s  rc 1, 1 FAIL, 69 executed
READ  unattended gate selftest shard 3/8               636s  rc 0, 0 FAIL, 40 executed
READ  unattended gate selftest shard 4/8              1092s  rc 0, 0 FAIL, 78 executed
READ  unattended gate selftest shard 5/8               576s  rc 1, 6 FAIL, 64 executed
READ  unattended gate selftest shard 6/8               647s  rc 0, 0 FAIL, 78 executed
READ  unattended gate selftest shard 7/8               698s  rc 1, 9 FAIL, 95 executed
READ  unattended gate selftest shard 8/8               936s  rc 1, 2 FAIL, 80 executed
READ  unattended gate-guard selftest                    97s  rc 0, 0 FAIL, 165 executed
READ  unattended pass-order selftest                   148s  rc 0, 0 FAIL, - executed  (declared trailer-less)
READ  unattended playbook selftest                     322s  rc 0, 0 FAIL, 123 executed
```

The seven red rows are the suites' own state, now their parity baselines. The eight shard rows
carry the 21-line oracle split 3 · 1 · 0 · 0 · 6 · 0 · 9 · 2. `unattended adopter e2e` reads rc 1
with 10 FAIL (`--check agrees with what --render just wrote`, `gate-guard hook is UNWIRED`, …) and is
byte-identical on a frozen clone of origin/main's tip 4cf0944d (65 s, rc 1, the same 10). The
driver suite reads rc 1 with 54 FAIL over 1076 executed; on the same clone of 4cf0944d it reads
rc 1 with the same 54 FAIL lines, byte-identical once the two trees' paths are
normalised (2117 s, `bash tools/unattended/unattended.test.sh` on the clone of 4cf0944d). Neither red is this build's: this build added one trailer line to each of those
two files and nothing else.

## Step 3 — `bash tools/unattended/run-unattended-gates.sh --pooled` at 177c1725

Detached at 177c1725 with `ps before: 0` (the origin/main driver-suite probe below was launched
beside it, one extra process on sixteen cores), 2146 s wall, rc 0. The runner's own lines:

```
run-selftests: SWEEP of 16 suite(s), width 8 (outer 8, inner 1), node a
run-selftests: condition: pooled@8x1
run-selftests: per-suite bound = max(budget, calibrated reading) + headroom max(120s, 1.0 x that); run wall 7720s; NO cost verdict is issued
ok    unattended adopter e2e                            64s  cost withheld  ok (rc 1, 10 FAIL, 85 executed matched)
ok    unattended arms-groups selftest                    5s  cost withheld  ok (rc 0, 0 FAIL, 35 executed matched)
ok    unattended brief-recorded selftest               131s  cost withheld  ok (rc 0, 0 FAIL, - executed matched)
ok    unattended cross-component                       177s  cost withheld  ok (rc 0, 0 FAIL, 21 executed matched)
ok    unattended driver selftest                      2125s  cost withheld  ok (rc 1, 54 FAIL, 1076 executed matched)
ok    unattended gate selftest shard 1/8               855s  cost withheld  ok (rc 1, 3 FAIL, 83 executed matched)
ok    unattended gate selftest shard 2/8              1043s  cost withheld  ok (rc 1, 1 FAIL, 69 executed matched)
ok    unattended gate selftest shard 3/8               692s  cost withheld  ok (rc 0, 0 FAIL, 40 executed matched)
ok    unattended gate selftest shard 4/8              1151s  cost withheld  ok (rc 0, 0 FAIL, 78 executed matched)
ok    unattended gate selftest shard 5/8               619s  cost withheld  ok (rc 1, 6 FAIL, 64 executed matched)
ok    unattended gate selftest shard 6/8               692s  cost withheld  ok (rc 0, 0 FAIL, 78 executed matched)
ok    unattended gate selftest shard 7/8               737s  cost withheld  ok (rc 1, 9 FAIL, 95 executed matched)
ok    unattended gate selftest shard 8/8               929s  cost withheld  ok (rc 1, 2 FAIL, 80 executed matched)
ok    unattended gate-guard selftest                    90s  cost withheld  ok (rc 0, 0 FAIL, 165 executed matched)
ok    unattended pass-order selftest                   148s  cost withheld  ok (rc 0, 0 FAIL, - executed matched)
ok    unattended playbook selftest                     314s  cost withheld  ok (rc 0, 0 FAIL, 123 executed matched)
run-selftests: peak concurrency 8 of outer 8
run-selftests: tree fingerprint MATCHED before and after — no suite wrote outside its scratch
sweep GREEN — 16 suite(s) ran concurrently, every one to its own end and matching its baseline; killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 0; NO cost verdict was issued for any of them
unattended gates GREEN — 16 ran on demand; no self-test here runs on the merge bar · pooled, 16 cost verdicts withheld
```

Every row completed, printed its trailer (or is one of the two declared no-trailer rows) and MATCHED
its (rc, ^FAIL, executed) baseline; the summary is `killed 0 · walled 0 · unrun 0 · unstarted 0 ·
mismatched 0`, the fingerprint MATCHED, and the kit runner's own verdict is `unattended gates GREEN`.
The per-row log of each suite is under `<git-dir>/gate-logs/selftests/`. This is S4's parity GREEN,
S5's step (3), and the observation that licenses the flip.

## The staged breaks the unit ledgers owed, each on its own frozen clone at 177c1725

Each break is a text-located mutation of `check-unattended.test.sh` in its own `git clone --local`
at 177c1725 (`stage.py`, one letter per break), the mutated shard run directly, output kept beside
this record's other runs. Every one observed RED, then the clone discarded — nothing here is unstaged
in the tree because nothing here was ever staged in it.

- **A — unit 1's AC2, a stale `check_emitted` set.** The last signature dropped from the one
  multi-signature set in region 3 (`… the shipped verb carrier and this repo's installed copy have
  drifted …`); `--shard 3/8`, 659 s, rc 1, one FAIL naming BOTH sides:
  `FAIL check_emitted: expected [one half of the protocol pair is missing, …] · missing: ·
  unexplained: [UNATTENDED check 10 FAILED — the shipped verb carrier and this repo's installed copy
  have drifted, …]`, 40 executed against the floor of 38.
- **B — unit 3's AC2, the mis-cut region.** Two stagings, because the first found a dependency that
  is not one. B moved the whole tWaive block (121 lines, from its `reset_tree` to check 18) into
  region 3: `--shard 3/8` ran GREEN, rc 0, 53 executed — a fresh fixture's `main` has not diverged
  from `unit`, so the block's merge fast-forwards there exactly as it does after region 4's replay;
  the block depends on `main` NOT being ahead, which every shard start satisfies. B2 is the mis-cut
  proper: a shard-5 window spliced INSIDE the block, between its green control (which sets `WP`) and
  its arms 1–3 (whose `wreset` is `git reset -q --hard "$WP"`); `--shard 5/8` RED at 3 s, rc 1:
  `check-unattended.test.sh: line 434: WP: unbound variable` — the arms moved into a shard that does
  not carry the state they depend on cannot run at all, and the suite's `set -u` says which state.
- **C — unit 3's AC9, the separated control.** The `same` over `$MUT` against `$MUT_EXPECTED` moved
  to directly after the block's own `MUT=0; MUT_EXPECTED=13` line, before any of the nine cycles;
  `--shard 4/8`, 1048 s, rc 1, one FAIL: `the tree is still clean after nine mutations: every cycle of
  its block ran in this process: expected [13], got [0]`; 78 executed against the floor of 75. The
  unseparated control is GREEN in every run above (the 21-line oracle carries no such line).
- **D — unit 3's AC10, the un-hoisted helper.** `dispconf()` moved from the hoist into region 1;
  `--shard 2/8` (its callers), 946 s, rc 1: fifteen `dispconf: command not found` lines and 10 FAILs
  (the disposition arms that called it), 69 executed against the floor of 67.
- **E — unit 3's AC11, the stranded block.** The 7-arm block of region 3 wrapped in `if false`;
  `--shard 3/8`, 532 s, rc 1: `FAIL executed 33 assertions in shard 3/8 against a floor of 38 — arms
  are UNREACHABLE rather than absent; look for a block stranded past an exit or a return`. The floors
  are within their headroom at every reading above (80/83 · 67/69 · 38/40 · 75/78 · 62/64 · 75/78 ·
  92/95 · 77/80, unsharded 569 against the 587 sum).
- **F — unit 3's AC8, the named negative.** For every boundary 2..8, shard k started twice on one
  clone with `CHECK_UNATTENDED_TOPO=1`, once bare and once with `CHECK_UNATTENDED_PLANT="ahead trunk"`
  (the derived leaked set at this base), each run cut off once its opening capture had printed. Bare,
  every boundary reads `origin=[refs/heads/main ] local=[refs/heads/main refs/heads/unit ]` with
  `unit<main=no unit<origin-main=no` at 2, 3, 5, 6, 7, 8 and `unit<main=yes unit<origin-main=yes` at 4
  (after `run_landed_replay`); planted, every boundary reads `origin=[refs/heads/ahead refs/heads/main
  refs/heads/trunk ] local=[refs/heads/ahead refs/heads/main refs/heads/trunk refs/heads/unit ]`.
  Seven DIFFERENT pairs, so the capture is live at every boundary and a leak of either name would
  show. The derived leaked set is EMPTY at every boundary in the unsharded run since `reset_tree`
  deletes both names (unit 3's S5 fix), so no boundary owes an "arm it breaks": the skip line for
  each of 2, 3, 4, 5, 6, 7 and 8 is this sentence, naming all seven.
- **The eight-row pooled reading, unit 3's AC4 arm two.** `run-selftests.sh --pooled --kit
  tools/unattended/check-unattended.test.sh` on a frozen clone at 177c1725, `ps before: 0`:
  `SWEEP of 8 suite(s), width 8 (outer 8, inner 1), node a`, so N = 8 and O = 8; sweep GREEN with
  every row matched; walls 877 · 1043 · 741 · 1149 · 674 · 748 · 788 · 1184 s — max 1184 s (19.7
  min), mean 900 s; the two-shard longest at BASE was 6656 s (unit 3's ledger), ratio 0.178, under
  the 0.5 that would have sent F2 to its fallback; the eight-shard longest is under 20 minutes, the
  GOAL. Caveat stated rather than hidden: the kit's `--checks` half (two runs, ~7 min each, started
  by this session) overlapped part of this run, so the box was not wholly idle; the idle direct
  reading of the same eight shards is 922 s (step 0 at a117faeb).

## Step 4 — the flip, at 3e7e7aae

The carrier predicate before, at 4fccc0ee — eight lines, the spec's eight with the post-merge line
numbers:

```
.githooks/gate-env.sh:27:#     bash tools/unattended/run-unattended-gates.sh --selftests --serial   # --pooled after calibration (TOOL-aBatchedArm-5)
AGENTS.md:518:`bash tools/unattended/run-unattended-gates.sh --serial`. The compensating check is written into that kit's
memory/guides/SESSION-KICKOFF.md:173:  `--selftests --serial` only when they ask. The cost is process creation, not logic:
tools/unattended/README.md:90:run-unattended-gates.sh --serial # the kit's self-tests, ON DEMAND ONLY; the mode is declared,
tools/unattended/kit.toml:139:#     bash tools/unattended/run-unattended-gates.sh --serial        # the self-tests, each graded; --pooled after calibration
tools/unattended/kit.toml:140:#     bash tools/unattended/run-unattended-gates.sh --all --serial  # and the legs beside them; --pooled after calibration
tools/unattended/run-unattended-gates.sh:27:# `tools/unattended/` is a GREEN verdict from `run-unattended-gates.sh --selftests --serial` (--pooled after calibration) pasted
tools/unattended/run-unattended-gates.sh:246:#   bash tools/unattended/run-unattended-gates.sh --selftests --serial
```

The phrase predicate before — six lines: `.githooks/gate-env.sh:26`, `tools/run-gates/run-selftests.sh:15`,
`tools/unattended/kit.toml:137`, `:144`, `tools/unattended/run-unattended-gates.sh:27`, `:192`.

The flip commit is exactly the two sets. Set one, the four DoD carriers spelling `--pooled` with the
dark marker gone: `.githooks/gate-env.sh:27` → `bash tools/unattended/run-unattended-gates.sh
--selftests --pooled`; `kit.toml:139` → `run-unattended-gates.sh --pooled # the self-tests through
the bounded pool, parity graded`; `kit.toml:140` → `run-unattended-gates.sh --checks # and the legs
beside them, which take no mode`; `run-unattended-gates.sh:27` → `a GREEN parity verdict from
run-unattended-gates.sh --selftests --pooled`. Set two, the five phrase lines re-worded to the pooled
criterion: `gate-env.sh:26` (`GREEN parity verdict … the pooled evidence bound`), `kit.toml:137`
(`not done until this prints parity GREEN`), `kit.toml:144-146` (the landed-dark paragraph now names
parity against the calibrated evidence and calls the serial mode the on-demand cost reading),
`run-unattended-gates.sh:27` and `:192-193` (`--serial … the on-demand cost reading`, `--pooled …
parity against the calibrated evidence — the recorded DoD path`); `run-selftests.sh:15` byte-unchanged,
naming no mode. Plus the one added README line beside the on-demand serial line
(`run-unattended-gates.sh --pooled # the DoD for work touching this kit: parity against the calibrated
evidence`), one added gate-command line in the kickoff manifest, and `last-audit` re-stamped at
4fccc0ee.

After, in the working tree and again at the commit: the carrier predicate yields the four POINTERS
only — `AGENTS.md:518`, `memory/guides/SESSION-KICKOFF.md:174` (moved one line by the added
gate-command line, bytes identical), `tools/unattended/README.md:90`,
`tools/unattended/run-unattended-gates.sh:246` — each byte-identical to 4fccc0ee (`git diff 4fccc0ee
-- AGENTS.md` empty; the manifest diff is the `last-audit` line and the added line; the README diff
is the added line; the runner's `:246` is outside its diff), and no line spelling `--serial` as a
criterion. The phrase predicate yields three lines — `run-selftests.sh:15`, `kit.toml:137`,
`run-unattended-gates.sh:193` — and ZERO naming `--serial` or `landed dark`. `bash -n` on both
scripts, `manifest-check.sh` rc 0, install-prefix clean (no literal rose), line-length OK, govkit
selfcheck clean, kit versions paired, `run-selftests.sh --check` clean; the kit's own `--checks`
half was RED on check 24 (two LATE rescope rows, units 2 and 3 — present since the gate pass at
72f54937 and misread there; recorded through `--rescope --act add` at 63612e99, after which the kit
gate is green).

## Reported to the owner, not fixed here

- The `govkit selftest` and check-23 reds above are main's and the merge's; the lander's bar meets
  the second.
- The 20-minute target is host-bound: a checker invocation costs 47–60 s on node `a`, so the
  unsharded suite is ~5.8 h there; the eight-shard pooled reading is the number the flip stands on.
- `--rank` refuses two of main's budget rows whose reason columns carry no ranked condition;
  pre-existing.
- The two suites red-by-design in the pooled population (adopter e2e, the driver suite) are red on
  origin/main's own tip; their parity baselines carry those counts until someone fixes them and
  re-calibrates.

## Evidences

The rows below answer the criteria the unit ledgers left AMENDED; each names the run above that
observed it. Where a ledger's row is still the amended one, this record is the later answer.

**Evidences:** TOOL-aBatchedArm-1
- AC1 — `emitted` — the fourteen `check_emitted` calls with their pasted sets pass in every run at
  7549981a and after: no `FAIL check_emitted:` line in the seven re-run shards, the eight shards at
  a117faeb, the calibrate or the pooled pass, and the executed counts rose by exactly the fourteen
  calls over unit 3's 555 (577 at 7549981a). The helper's own red is stage A.
- AC2 — `emitted` — stage A: the set with one signature dropped reds `--shard 3/8` naming the
  expected set and the unexplained observed line, both sides in one `FAIL check_emitted:` line.
- AC3 — `check-unattended.test.sh` — the `FAIL` set of the eight shards' union is byte-identical to
  the 21-line oracle at 72f54937 (sentinels removed), 7549981a and a117faeb; `n` moved only by the
  fourteen `check_emitted` calls (555 → 577) and then by main's ten merged arms (→ 587), both stated.
- AC5 — `FLOOR_ASSERTIONS` — re-declared 569 against the 587 reading, and the eight per-shard floors
  80 · 67 · 38 · 75 · 62 · 75 · 92 · 77 against 83 · 69 · 40 · 78 · 64 · 78 · 95 · 80, each carrying
  its reading in the comment beside it (fd6dc1fd); no floor is the unconverted suite's.
- AC6 — `TOOL-aBatchedArm-3` — the converted suite on a frozen clone on an idle box with the
  eight-shard arity: longest shard 922 s (shard 8) at a117faeb, timed with `date +%s`, written into
  `tools/run-gates/selftest-budgets.txt` beside each shard row at 4fccc0ee as the idle eight-wide
  reading; under 20 minutes. The pooled reading of the same eight rows is 1184 s longest.
- AC8 — `emitted` — before the final pass every call carried `"?"` and the helper refused it by name
  (the fourteen sentinel lines in the runs at 72f54937); after, every call carries a set pasted from
  that observed run with the run named beside it, `grep -c 'check_emitted "?"'` is 0, and the linter's
  header reads `sentinels 0`.

**Evidences:** TOOL-aBatchedArm-2
- AC6 — `bash tools/run-gates/run-gates.sh` — with the kit self-tests enabled at 72f54937 the leg
  `unattended arms-groups selftest` appears in the manifest-derived list and reports `GATE ok`
  (PASS 35); it also ran in the calibrate and the pooled pass as row 2, `rc 0, 0 FAIL, 35 executed
  matched`. The linter over the tracked suite at the landing still reads `rule A 0 · rule B 4 · rule
  C 1`, its starting figures, with `sentinels 0`.

**Evidences:** TOOL-aBatchedArm-3
- AC2 — `check-unattended.test.sh --shard <i>/8` — stage B2: the mis-cut shard 5 REDS, rc 1, `WP:
  unbound variable` at `wreset`; stage B, the whole block moved to region 3, ran green and is
  recorded as the dependency that is not one.
- AC4 — `SWEEP of N suite(s), width W (outer O, inner I)` — arm two: the eight-row pooled run at
  177c1725 shows N = 8, O = 8, walls 877 · 1043 · 741 · 1149 · 674 · 748 · 788 · 1184 s, max 1184 s,
  mean 900 s, the two-shard longest 6656 s at BASE, ratio 0.178; every row trailed and matched.
  The GOAL holds at 19.7 minutes pooled and 15.4 minutes direct; F2 stays at eight.
- AC8 — `git ls-remote --heads "$ORIGIN"` — the negative half: stage F's seven planted/unplanted
  pairs differ at every boundary 2..8, the derived leaked set is empty at each, and the skip line
  names all seven; the positive half stands in unit 3's ledger.
- AC9 — `same` — stage C: the separated control reds `expected [13], got [0]`; the correct run is
  green on it in every run above.
- AC10 — `check-unattended.test.sh --shard <i>/8` — stage D: `dispconf: command not found`, fifteen
  times, shard 2 rc 1 with 10 FAILs.
- AC11 — `FLOOR_SHARD_i` — stage E: the stranded 7-arm block reds shard 3's floor (`executed 33 …
  against a floor of 38 — arms are UNREACHABLE`); every floor sits within its headroom of its
  reading, both figures beside it (fd6dc1fd).

**Evidences:** TOOL-aBatchedArm-5
- AC1 — `selftest-pooled-evidence.txt` — the fixture arms in `run-selftests self-test` at 72f54937,
  `GATE ok`, PASS 112 arms (`bounded at 120s: budget won`, `bounded at 400s: reading won`, the run
  wall, the wall refusal, the margin refusal all `ok`); on the real tree every pooled row printed its
  derived bound (`bounded at 180s: budget won (budget 60s; reading 50s …) + headroom`).
- AC2 — `run-selftests.sh --pooled` — the fixture refusal arms in the same leg (`NO pooled reading
  under pooled@2x1 on node t`, the foreign tag, the missing registry row), all `ok`; the real
  tree's refusal was not run at this pass — before the calibrate the `--check` line read `0 pooled
  evidence row(s) well-formed`, the announced-unarmed state, and after it `--pooled` bounded all
  sixteen rows from their readings.
- AC3 — `run-selftests.sh --pooled --calibrate` — the fixture half in the same leg; the real-row
  half: the calibrate at fd6dc1fd over the sixteen rows `--list` resolves (sixteen at this base, not
  the spec's fourteen: the merge of 4cf0944d added none, unit 2 added one, main's gate-guard row is
  one), serial-sum wall 21380 s, 2099 s wall, no row walled, no row untrailed, sixteen readings
  written.
- AC4 — `run-selftests.sh --rank` — the fixture arm in the same leg; on the real tree `--rank` after
  the calibrate still exits without reading a pooled token (`grep -c pooled@ selftest-budgets.txt`
  is 0) and refuses the same two of main's rows it refused before.
- AC5 — `--pooled` — the landing half: step 3's `unattended gates GREEN` with `killed 0 · walled 0 ·
  unrun 0 · unstarted 0 · mismatched 0` and `fingerprint MATCHED`, then the flip commit with both
  predicate lists before and after and the phrase re-run's zero `--serial`/`landed dark` lines.
- AC6 — `--serial` — `run-selftests self-test` at 72f54937 runs every pre-existing `--serial` arm
  green; `git diff 1c736fd9 -- tools/run-gates/run-selftests.sh` carries no hunk in the serial loop.
- AC7 — `selftest-budgets.txt` — the fixture arm `a sweep-ceiling-factor header staged back in is
  IGNORED` is `ok` in the same leg; the real file carries no `sweep-ceiling-factor` line.
- AC8 — `run-selftests.sh --serial --calibrate` — the three refusal arms `ok` in the same leg.
- AC9 — `run-selftests.sh --check` — the six evidence-shape arms `ok` in the same leg; the real tree
  reads `16 pooled evidence row(s) well-formed` after the calibrate.
- AC10 — `run-selftests.sh --pooled --calibrate --reset <row>` — the five reset arms `ok` in the same
  leg.
- AC11 — `run-selftests.sh --pooled` — the parity arms `ok` in the same leg (`ok (rc 1, 3 FAIL, 81
  executed matched)`, the MISMATCH trio, the five-word GREEN summary, one RED arm per class); on the
  real tree the seven red-by-design rows render `ok … matched` in step 3 and the summary's five
  counts are all 0.

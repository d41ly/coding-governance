# TOOL-aBatchedArm-1 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-1

One pass under two owner rulings — 2026-09-13 (build agents run no self-test per step) and
2026-09-14 (no gate until every unit of the build is built). This unit ran NO suite, NO shard, NO
bar, NO fixture and NO `run-unattended-gates.sh` in any mode. What it ran, because each executes
no suite and costs seconds: a classifier over the TEXT of `check-unattended.test.sh` (rules below,
counts below), `bash -n` over the edited file, `python tools/memory-tree/check-arms.py --check`,
`bash tools/check-install-prefix.sh`, the AC4/AC7 scan and its planted red on a scratch copy, a
probe of the new helper ALONE over literal strings (no fixture, no checker), `grep -c` counts,
`git diff` against the base, and the record gates the pre-commit hook runs. Every criterion that
needs the suite is AMENDED below, naming the command the build's final gate pass observes it by.

## What the pass built, and what it did not

- **S1, built.** `emitted <signatures> <output>` is the fourth helper in the assertion block beside
  `hit`, `miss` and `same` — same counter, same failure idiom. Its contract is its own header in the
  file. It has NO call site.
- **S2, converted ZERO groups**, and the reason is a measurement, not a choice. The classifier below
  finds no group whose expected set can be written without an observed run, and the 2026-09-14
  ruling forbids the run. The question is PARKED to the owner in the run-state file with four
  options and the refusal reason (`decision · item TOOL-aBatchedArm-1 S2`).
- **S3, trivially held**: with zero groups, every arm S3 names sits alone — observed by the scan
  under AC4 and AC7 below.
- **S4 and S5, owed at the final pass** as the build brief and the rev-5 line say: the floors and
  the budget rows are unit 3's readings, and a conversion that added zero `emitted` calls moved no
  count.

## The classification (F1's measured distribution), at 46b12b93

A scratch script (`classify.py`, reproducible from the rules here) walked every block between one
boundary line and the next inside each `if in_shard k` region — a boundary is a non-comment line
leading with `reset_tree`, `anchor_break`, `anchor_restore`, `seed_ros`, `wreset`, the guarded
`replay_landed_main`, or carrying `; reset_tree` — and tagged each block BATCHABLE only when ALL of
these held, else SOLO with the reasons named:

- exactly one invocation, and it is the line `out=$(run)`;
- no `miss`, no `same`, no `rc=$?`, no bare counter line, no shell control flow;
- every assertion is `hit "$out" "<literal>"` with no `$` or backtick in the literal;
- at least one literal CONTAINS exactly one fail-branch signature (the `check-arms.py` normaliser:
  the longest literal run between interpolations, trailing `:" ` trimmed); a literal containing no
  signature is a fragment riding on the block's resolved branch; one containing two is ambiguous;
- no resolved branch is one of the three check-1 `exit` branches (checker lines 113, 197, 384 at
  46b12b93), and none is under a check with a STANDING skip line on the pristine fixture — 23 (no
  concurrent dispatch), 24 (`tRun`'s empty baseline roster), 31 (no rendered Skill, no carrier) —
  because the skip-line detector would red on every tree;
- not RED at 46b12b93: no literal among the 21 `FAIL missing:` lines and no `mutate` script among
  the `fixture no-op` lines of unit 3's run 2u (`u3b/b2-unsharded.out`, 21 lines);
- no `GOV_UNATTENDED_REPORT`, no `PATH=`/`TMPDIR=` stub, no `git remote`/`push`/`branch -f`/
  `update-ref`/`symbolic-ref`/`checkout`/`merge`, no `--git-dir="$ORIGIN"` write.

A GROUP is contiguous BATCHABLE blocks inside one region whose touched-file sets are pairwise
disjoint (a `git commit` counts as touching the ref `unit`), carrying no hit literal twice, at most
five blocks. Two readings of one rule, because the build brief's "every existing `hit` line stays
byte-identical" and the spec's "assertions against `$out` verbatim" disagree on the shape
`hit "$(run)" "…"`, which is the shape 174 of the hit-only blocks have:

| reading | blocks | BATCHABLE | SOLO | groups | sizes | blocks grouped | invocations saved |
|---|---|---|---|---|---|---|---|
| hit LINES byte-identical (the brief) | 332 | 10 | 322 | 0 | — | 0 | 0 of 285 |
| hit LITERALS verbatim, `"$(run)"` → `"$out"` allowed (the spec) | 332 | 112 | 220 | 19 | 14 × 2, 5 × 3 | 43 | 24 of 285 |

SOLO reasons under the brief's reading (a block may carry several): inline `hit "$(run)"` 174 ·
`miss` 88 · no invocation at all (restore-only blocks) 73 · `same` 21 · two or more invocations 23
· report channel 15 · ref move 16 · control flow 13 · `rc=$?` 6 · bare counter 6 · env stub 7 ·
RED at base 6 · check-1 exit 1 · variable-bearing literal 2. Under the spec's reading the inline
count falls to 40 (blocks whose ONLY blemish was the token), and 16 more blocks are SOLO because
no literal resolves to a signature and 9 because their check carries a standing skip line.

**The 10 BATCHABLE blocks under the brief's reading, by first line at 46b12b93, none adjacent to
another:** 527 · 835 · 843 · 894 · 914 · 1143 · 1213 · 1229 · 2073 · 2660.

**The 19 candidate groups under the spec's reading, by line range at 46b12b93** (the owner's
menu, if the token is allowed): region 1 880–886, 887–898 · region 2 1208–1217 · region 3
1223–1238, 1289–1301 · region 4 1592–1625, 1634–1645, 1646–1655, 1809–1858 · region 6 2486–2492,
2498–2512, 2513–2524 · region 7 2697–2706, 2736–2750, 2759–2765 · region 8 2776–2784, 2785–2799,
2800–2806, 2817–2824.

## The finding: an expected set derived from the arms is INCOMPLETE for this file

`emitted` grades SET EQUALITY — every expected signature present and every `FAILED` line explained
— which is the spec's own answer to "why the set and not a count". The brief derives the expected
set from the arms. Three of the 19 candidates are proven, from the checker's source, to fire
branches their arms never name, so their derived set is wrong before any group-mate is added:

- 885–886, `PHASES_CORE=" "`: the arm asserts `the effective phase vocabulary is empty`; the checker
  then runs its TERMINAL-phase loop (`a TERMINAL phase is not in the effective vocabulary`, once per
  terminal phase) and check 4 grades `tRun`'s `RUNNING` against the empty set.
- 887–893, `DOD_CORE=" "`: the arm asserts `the effective Definition-of-Done set is empty`; check
  16's table join (`dcore` empty, `ed2` = every protocol item) fires `the protocol's
  Definition-of-Done table names an item the driver does not carry`.
- 1233–1238, `rm VERBS.template.md`: the arm asserts check 10's `one half of the verb-carrier pair
  is missing`; check 26's `[ -f "$VERBSHIP" ] || fail 26 "the verb carrier is absent…"` fires too,
  which the suite's own comment at the check-26 arm already records.

Under the spec's rollout rule a tranche whose `emitted` reds is REVERTED, not repaired from the
observation, and the complete emission of the other 16 candidates is unknowable without the run.
So no group was written. This is the fact the parked decision carries.

## The helper, probed alone

`bash -n` clean. The function body was extracted by `sed -n '/^emitted() {/,/^}/p'` into a scratch
file and sourced into a bare shell with `n=0 st=0`; seven literal cases, no fixture and no checker:

```
[1 exact set, unrelated skip -> green] st=0 n=1 out_lines=2 0 report lines left
[2 extra FAILED line -> red] st=1 n=1        (unexplained: names the check-11 line)
[3 missing signature -> red] st=1 n=1        (missing: names the check-11 signature)
[4 skip naming an explained check -> red] st=1 n=1   (dark: names the skip line)
[5 empty set -> red] st=1 n=1                (no signature given)
[6 nothing emitted -> red] st=1 n=1          (missing: both)
[7 padding tolerated, skip stripped from out -> green] st=0 n=1 out_lines=2 0 report lines left
```

Each red prints the expected set, the missing and unexplained members and the skip lines seen;
each call moves `n` by exactly one. This is the helper's own check and NOT AC1 or AC2, which speak
of a batch's TREE firing checks and need the suite.

## Static evidence over the converted file

- `git diff --stat 46b12b93 -- tools/unattended/check-unattended.test.sh`: 1 file, 53 insertions,
  0 deletions — every existing line byte-identical, `hit` lines included.
- `grep -c '\$(run)'`: 285 at 46b12b93, 285 after. Lines leading with `hit` 249 → 249, `miss` 101
  → 101, `same` 28 → 28, `mutate` 51 → 51, `emitted` calls 0 → 0.
- `python tools/memory-tree/check-arms.py --check`: rc 0 — the armed-branch pin did not move, and
  the helper's lines carry no signature.
- `bash tools/check-install-prefix.sh`: clean, carried-prefix clean, this file at 3 and not rising.
- The counted block (`MUT_EXPECTED=13`), the floors and the seams are untouched: the diff is one
  insertion after `same()` in the prologue.

**Evidences:** TOOL-aBatchedArm-1
- AC1 — amended rev-5 — NOT OBSERVED under the 2026-09-14 ruling, and not observable on this tree
  as landed, because no group exists; owed at the build's final gate pass by staging ONE group in a
  scratch clone: the two region-2 appends — the bypass-flag line the check-11 arm appends to
  `memory/builds/tRun/RUN.md` (the arm at the text `parked: considered`) and `printf '\ndrifted
  line\n' >> memory/guides/UNATTENDED-PROTOCOL.md` (check 10) — under one `reset_tree`, `out=$(GOV_UNATTENDED_REPORT=1 run)`,
  `emitted "the shipped protocol and this repo's installed copy have drifted, so the kit ships
  something other than what it runs on | a run-state file names the declared bypass flag, and
  bypassing the lander discards the whole bar the mandate leaned on" "$out"`, then the three
  existing `hit` lines against `$out`; run `bash tools/unattended/check-unattended.test.sh --shard 2/8`
  and read the floor-graded count one above 58 with no new `FAIL` line. Red when the count does
  not move or a `FAIL emitted:` line appears — the latter is ALSO the first observation of whether
  those two breaks emit only their own branches, which nothing on this tree has observed.
- AC2 — amended rev-5 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass on the same staged group as AC1 with a third break added and the `emitted` argument left
  alone: `sed -i '/^base: /d' memory/builds/tRun/RUN.md` (check 9, `a run-state file records no
  BASE`); `bash tools/unattended/check-unattended.test.sh --shard 2/8` must print one `FAIL emitted:`
  line naming `expected […]` with both signatures and `unexplained: [UNATTENDED check 9 FAILED …]`.
  Red when the run passes or the line names only one side. Unstaged after.
- AC3 — amended rev-5 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/unattended/check-unattended.test.sh > <log> 2>&1` on a frozen clone at the
  final-pass commit: `grep '^FAIL' <log> | sort` must be byte-identical to the 21 lines of unit 3's
  run 2u at 46b12b93 (`u3b/b2-unsharded.out`: the dispatched-verb line, the DoD-floor pair with
  `11 against 12`, the killed-remote line and seventeen `fixture no-op`/`missing` lines of the
  protocol-count and declared-parser blocks), and `grep 'assertions executed' <log>` must read
  **555** — the floor-graded `n` at 46b12b93 plus the number of `emitted` calls this unit added,
  which is **ZERO**. Red when a `FAIL` line appears, disappears or changes, or `n` is not 555.
- AC4 — `reset_tree` — OBSERVED now by the static scan (`ac47.py`, rules in its header) over the landed file:
  `blocks 340; groups (blocks carrying an emitted call) 0`; located and found alone — check-1
  exit arms 1 + 1 + 2 blocks, exit-code-only 5, empty-output 11, anchor 9, PATH/TMPDIR 2, remote-
  rewriting 5, every `miss` 88, every `same` 21, equality arms with `_f1_clean` 3 — `0 inside a
  group` for each; verdict GREEN. LIVENESS: the same scan over a scratch copy with one `emitted "x"
  "$out"` planted into the region-2 `witness: deadbeef…` block (a `hit` + `miss` block) reports
  `groups 1`, `every miss: 1 inside a group`, verdict RED — the scratch copy only, the tree untouched.
- AC5 — amended rev-5 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/unattended/check-unattended.test.sh` unsharded and `--shard <i>/8` for each
  `i`, reading `assertions executed in <mode> against a floor of <F>` against `FLOOR_ASSERTIONS=538`
  and `FLOOR_SHARD_1..8` (78 56 36 74 62 72 90 66). The floors are NOT carried across from an
  unconverted suite: this unit converted zero groups and added zero executed assertions, so the
  converted suite IS the suite those floors were read from; unit 3's ledger owes shard 8's direct
  reading at the same pass. Red when any count is under its floor.
- AC6 — amended rev-5 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.sh --pooled --calibrate --kit tools/unattended` on an
  idle box, the longest of the eight shard walls read from the runner's own row output and from
  `date +%s` either side, written into `tools/run-gates/selftest-budgets.txt` with the reading it
  was taken from. Red when the longest shard exceeds 1200 s. This unit contributes nothing to the
  figure: the pair's wall is unit 3's split alone until a group lands.
- AC7 — OBSERVED now by the same scan as AC4: `groups containing a miss or a same: 0 []`, verdict
  GREEN; the planted scratch copy reports `1 [(980, 987)]`, verdict RED.

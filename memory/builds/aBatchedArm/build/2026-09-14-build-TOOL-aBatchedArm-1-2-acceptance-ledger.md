# TOOL-aBatchedArm-1 — acceptance ledger, pass 2

**Serves:** journal TOOL-aBatchedArm-1

The second pass, under the owner's 2026-09-14 ruling that REOPENED the spec at rev-6 (the `$out`
token allowed, the nineteen groups converted, each set written from the observed run at the build's
final gate pass) and still under the two rulings the first pass ran under — 2026-09-13, no self-test
per step; 2026-09-14, no gate until every unit is built. So this pass ran NO suite, NO shard, NO
bar, NO fixture and NO `run-unattended-gates.sh`. What it ran, because each executes no suite and
costs seconds: a READ of the checker's source for every candidate group, `bash -n`, a binary-mode
conversion script with its own invariants, `python tools/memory-tree/check-arms.py --check`,
`bash tools/check-install-prefix.sh`, `bash tools/check-line-length.sh`, the AC4/AC7 scan and its
three planted reds on scratch copies, a probe of the helper ALONE over literal strings, `grep -c`
counts, `git diff` against the base, and the record gates the pre-commit hook runs. The first pass's
ledger (`…-1-1-acceptance-ledger.md`) still holds the classification, the counts it derived and the
helper's seven-case probe; this one carries the delta.

## What the pass built

- **S1, extended.** `emitted "?" …` is refused BY NAME: one `FAIL emitted: expected set not yet
  observed — owed at the final pass · call at line <L>` per call, `st=1`, the counter moved by one,
  and the run's `UNATTENDED check N FAILED` lines printed beneath it, indented as `    observed: …`
  so `grep '^FAIL'` does not count them — `out` is captured and never printed, so without this the
  final pass would have nothing to paste a group's set from, and the caller's line is what joins a
  refusal to its group. The report-channel strip now happens ONCE at the top of the helper, so
  every path leaves `out` stripped (the sentinel branch had spelled it a second time).
- **S2, converted FOURTEEN of the nineteen.** The rule, read from the checker rather than chosen: a
  group is converted only where the checker's own control flow keeps every block's branch reachable
  with its group-mates applied. Five groups are not converted and four are cut from three blocks
  to two; each carries its proof below. Every survivor's branches were read to sit in independent
  arms of the checker. Shape per group: one `reset_tree`, the mutations in sequence with each
  block's own comment ahead of its mutation, one `out=$(GOV_UNATTENDED_REPORT=1 run)` (S1's channel
  and the helper's header; the pass-2 brief's `out=$(run)` was shorthand), one `emitted "?" "$out"`,
  then the `hit "$out" "<literal>"` lines with every literal byte-identical. Blank lines between
  grouped blocks are dropped; nothing else in the file moves.
- **S3, held** — observed by the scan under AC4 and AC7 below, over fourteen real groups this time.
- **S4 and S5, owed at the final pass**, as rev-5 says: the counts rose and none fell, so every
  floor stays valid until that pass re-declares them from its own readings.

## The nineteen groups — rev-5's range at 46b12b93 → this pass's range at 025c76c0

| # | region | at 46b12b93 | at 025c76c0 | disposition |
|---|---|---|---|---|
| 1 | 1 | 880–886 | 941–948 | converted, 2 blocks |
| 2 | 1 | 887–898 | 949–959 | converted, 2 blocks |
| 3 | 2 | 1208–1217 | 1270–1278 | converted, 2 blocks |
| 4 | 3 | 1223–1238 | 1285–1294 + solo 1295–1296 | cut to 2: `rm VERBS.template.md` stays solo |
| 5 | 3 | 1289–1301 | 1351–1359 | converted, 2 blocks |
| 6 | 4 | 1592–1625 | inside 1637–1720 | NOT converted: the counted block |
| 7 | 4 | 1634–1645 | inside 1637–1720 | NOT converted: the counted block |
| 8 | 4 | 1646–1655 | inside 1637–1720 | NOT converted: the counted block |
| 9 | 4 | 1809–1858 | 1872–1889 + solo 1905–1912 | cut to 2: the NOT-A-UNIT arm stays solo |
| 10 | 6 | 2486–2492 | 2549–2556 | converted, 2 blocks |
| 11 | 6 | 2498–2512 | 2562–2571 | converted, 2 blocks |
| 12 | 6 | 2513–2524 | 2577–2582 + solo 2586–2587 | cut to 2: `VERBS_SLUG=""` stays solo |
| 13 | 7 | 2697–2706 | 2762–2772 | converted, 2 blocks |
| 14 | 7 | 2736–2750 | 2802–2814 | converted, 2 blocks |
| 15 | 7 | 2759–2765 | 2826–2831, untouched | NOT converted: the fence indent empties 28b's key loop |
| 16 | 8 | 2776–2784 | 2843–2849 | converted, 2 blocks |
| 17 | 8 | 2785–2799 | solo 2853–2854 + 2858–2866 | cut to 2: the bare `git cat-file` arm stays solo |
| 18 | 8 | 2800–2806 | 2869–2875 | converted, 2 blocks |
| 19 | 8 | 2817–2824 | 2887–2893, untouched | NOT converted: `rm check-playbook.sh` empties `dl_b` |

Derived, not targeted: 14 converted, 28 blocks, 14 invocations saved; every group carries exactly
two blocks, and two of them (3 and 4) carry three `hit` lines because one block asserted twice.

## The proofs — where a group-mate's break makes the other arm's branch unreachable

Each is a reading of `tools/unattended/check-unattended.sh` at 025c76c0, cited by the text that
anchors it; converting these would have changed an arm's verdict, which the spec's rollout rule
reverts, so they are refused by reading instead of by the run the ruling forbids.

- **6, 7, 8 — the counted block.** `MUT=0; MUT_EXPECTED=13` opens it and
  `same "the tree is still clean after nine mutations: every cycle …" "$MUT" "$MUT_EXPECTED"`
  closes it; `reset_tree` increments `MUT`, so folding any two of its cycles onto one tree lowers
  the count and reds the control. rev-5's own fact (2) says the block stays exactly as it is; the
  rev-5 enumeration listed three ranges inside it anyway, which is a defect in that ledger and is
  the reason nineteen was never reachable.
- **4 — `rm VERBS.template.md` beside a drifted `UNATTENDED-VERBS.md`.** Check 10's `_c10_cmp`
  returns 2 when either half is missing, BEFORE the drift compare, and the caller is
  `if [ "$_c10rc" -eq 2 ] … elif [ "$_c10rc" -ne 0 ]`: only "one half of the verb-carrier pair is
  missing" fires, and the drift arm's two `hit` lines (the drift message and `drifted line`) would
  fail. The protocol-pair half and the verb-pair drift are independent `_c10_cmp` calls, so those
  two convert.
- **9 — the NOT-A-UNIT arm beside the broken units regions.** Check 30 counts a build only when its
  `--plan` frame closes at rc 0 (`if [ "$_pv_s" = "$_pv_cur" ] && [ "$_pv_rc" = 0 ]`), and the
  suite's own comment on the liveness arm says "with every build's units pair broken, every --plan
  refuses". The README break that arms branch 1 refuses `tPlanOk`, so the `_pv_bad` verdict the
  third block asserts cannot follow. Check 18 (the Skill template's `--preflight` anchor) reads
  `$tmpl` and `KICKOFF_ENGINE` only, so it converts beside branch 1.
- **12 — `VERBS_SLUG=""` beside the carrier and Skill joins.** Check 26 is
  `if [ "$nverbs" -lt 10 ]; then fail 26 "cannot read the driver's verb declarations…" else …`, and
  the absent-carrier refusal and the per-verb Skill join both live in that `else`. The other two
  convert: with the carrier absent, `[ -f "$VERBSHIP" ] || fail 26` fires and the loop still reaches
  the Skill join for `--propose`.
- **15 — the fence indent beside the ad-hoc read.** 28b's key loop is fed by the `awk` over the
  template's toml fence that prints every `^[a-z_]+[[:space:]]*=` key; the indented fence yields no
  key, `kb_keys` stays 0, the liveness branch fires, and the ad-hoc-pipeline branch — inside that
  loop, per key — has no key to fire on. Two blocks, one dependency, so the group is refused whole.
- **17 — the bare `git cat-file -p "$1"` beside "graded nothing".** 28c's raw arm counts every
  bare `git <verb> <rev>` as `sha_raw_graded`, and `[ "$sha_raw_graded" -gt 0 ] || fail 28 "every
  bare git invocation … graded nothing"` needs that count at zero; the arm that adds a bare
  dereference keeps it above zero. The `GITSHOW() { GIT show` and `GIT() {` → `GITWRAP() {` pair
  converts: the rename leaves no `git <verb> <rev>` behind (its body is `git -c … "$@"`), so the
  graded count stays zero and `_wrapdef` reads zero.
- **19 — `rm check-playbook.sh` beside `piece_checks = [oops]`.** The template parse lives in the
  `else` of `if [ -z "$dl_a" ] || [ -z "$dl_b" ]; then fail 28 "the declared-list parser is missing
  …" elif … else`; the missing leg empties `dl_b`, so the "declared null" branch is never reached.
  Refused whole.

Read and found independent, in the checker's own arms: 1 (`[ -n "$CORE_FLOOR" ]` and
`[ -n "${PHASES//…}" ]` are separate tests; with the floor undeclared `pfloor` is empty, so the
"shrunk below its floor" branch the solo arm also fires stays silent — an EXTRA the observed set
will record, not a `hit` that fails); 2 (check 3's `[ -n "${DOD//…}" ]` and check 4's population
guard read different inputs; `git commit -am` also commits the driver edit, which the checker reads
from the working tree either way); 3 and 5 (checks 9, 10 and 11 read different files); 10 (the
`DIRECTIVES_EXTRA` scope loop sits under `tblpairs`, the pass-kind loop under `ppk`); 11 (two
`case`s inside one per-verb loop); 13 (`KIT_SH` loses the playbook leg, 28a still walks the driver);
14 (`rc_refusers` and the `KEY_EXEMPT` row are read by different rules); 16 (the wrapper-definition
loop and the raw-dereference loop are separate passes over `KIT_SH`); 18 (`_pbatch` sources one
parser body per call, so a gutted `declared_scalar` cannot reach the `declared_list` template rows).

## The helper, probed alone (pass 2)

`bash -n` clean. The function body was extracted by `sed -n '/^emitted() {/,/^}/p'` into a scratch
file and sourced into a bare shell with `n=0 st=0`; five literal cases, no fixture and no checker,
over a sample carrying one `UNATTENDED check 11 FAILED` line, one skip line and one plain line:

```
FAIL emitted: expected set not yet observed — owed at the final pass · call at line 5
    observed: UNATTENDED check 11 FAILED — a run-state file names the declared bypass flag
[1 sentinel] st=1 n=1 out_lines=2 report_left=0
[2 padded sentinel is NOT the sentinel] st=1 n=1        (graded as a signature: missing + unexplained)
[3 exact set still green] st=0 n=1
[4 empty set -> red, out still stripped] st=1 n=1 out_lines=2 report_left=0
[5 wrong set -> red, out still stripped] st=1 n=1 out_lines=2 report_left=0
```

`grep -c '^FAIL'` over that output reads 4 — the indented `observed:` line is not counted. This is
the helper's own check and NOT AC1 or AC2, which speak of a batch's TREE and need the suite.

## Static evidence over the converted file

- `git diff --stat 97abf7e1 HEAD -- tools/unattended/check-unattended.test.sh`: 1 file, 74
  insertions, 60 deletions; the hunks are the helper and the fourteen group stanzas and nothing else.
- `grep -c '\$(run)'`: **285 at 97abf7e1, 257 after** (two per group folded). The report-channel
  spelling `GOV_UNATTENDED_REPORT=1 run)`: 11 → 25 (+14, one per group). Invocations in the two
  spellings together: 296 → 282, **14 saved**.
- Lines leading with `hit` 248 → 248 · `miss` 101 → 101 · `same` 27 → 27 · `emitted` 0 → 14, all
  fourteen spelling `emitted "?" "$out"` · lines 3386 → 3400. `mutate` CALLS are unchanged; seven
  now lead their line because the `reset_tree; ` ahead of them was the fold.
- The conversion script's own invariant, asserted on every region: the ordered list of `hit`
  literals (the bytes after the capture token) is identical before and after.
- `python tools/memory-tree/check-arms.py --check`: rc 0 after every region — the armed-branch pin
  did not move, since a `hit` line carries the same literal wherever it sits.
- `bash tools/check-install-prefix.sh`: clean, carried-prefix clean, this file at 3 and not rising.
- `bash tools/check-line-length.sh`: rc 0.
- The counted block (`MUT_EXPECTED=13` at 1637 through the `same` at 1720), the floors and the
  seams are untouched.
- **The AC4/AC7 scan** (`ac47.py`, rules in its header: blocks between boundary lines inside each
  `if in_shard k` region, a group is a block carrying an `emitted` call) over the landed file:

```
blocks 310; groups (blocks carrying an emitted call) 14
group hit-count distribution {2: 12, 3: 2}; groups per region {1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 3, 7: 2, 8: 3}
AC7 groups containing a miss or a same: 0 []
AC4 check-1 exit arms      located   4 blocks · 0 inside a group
AC4 exit-code-only         located   5 blocks · 0 inside a group
AC4 empty-output           located  10 blocks · 0 inside a group
AC4 anchor                 located  18 blocks · 0 inside a group
AC4 PATH/TMPDIR stub       located   2 blocks · 0 inside a group
AC4 remote-rewriting       located  14 blocks · 0 inside a group
AC4 every miss             located  88 blocks · 0 inside a group
AC4 every same             located  20 blocks · 0 inside a group
AC4 equality _f1_clean     located   4 blocks · 0 inside a group
AC4 counted block 1637-1720: emitted calls inside 0
verdict GREEN
```

  The scan also grades each group's SHAPE: exactly one `emitted`, its argument the sentinel,
  exactly one invocation and it is the report-channel run, at least two `hit` lines, every one
  against `"$out"`. LIVENESS, three planted reds on scratch copies: an `emitted "x"` planted into
  the region-2 `witness: deadbeef…` block (a `hit` + `miss` block) reports `AC7 … 1`, `every miss:
  1 inside a group`, verdict RED; one group's sentinel replaced by `"typed"` reports `emitted is not
  the sentinel`, RED; an `emitted` planted into the counted block reports `counted block carries
  emitted`, RED. The tree was untouched by all three.

**Evidences:** TOOL-aBatchedArm-1
- AC1 — amended rev-6 — NOT OBSERVED under the 2026-09-14 ruling; the group the rev-5 line staged
  by hand now EXISTS at 1270–1278 (check 11's bypass line with check 10's drifted protocol), so it
  is owed at the build's final gate pass by that pass's own golden-writing step under AC8: paste
  that group's set from the `observed:` lines under its refusal, re-run
  `bash tools/unattended/check-unattended.test.sh --shard 2/8`, and read the floor-graded count one
  above unit 3's 58 with no `FAIL emitted:` line and the three `hit` lines silent. Red when the
  count does not move or a `FAIL` line names that group's `emitted`.
- AC2 — amended rev-6 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass on a scratch copy of that same group with a third break added and the pasted `emitted`
  argument left alone: `sed -i '/^base: /d' memory/builds/tRun/RUN.md` (check 9, `a run-state file
  records no BASE`); `bash tools/unattended/check-unattended.test.sh --shard 2/8` must print one
  `FAIL emitted:` line naming `expected […]` with both signatures and `unexplained: [UNATTENDED
  check 9 FAILED …]`. Red when the run passes or the line names only one side. Unstaged after.
- AC3 — amended rev-6 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/unattended/check-unattended.test.sh > <log> 2>&1` on a frozen clone, in TWO
  readings. Before the sets are written: `grep '^FAIL' <log> | sort` must be the 21 lines of unit
  3's run 2u at 46b12b93 (`u3b/b2-unsharded.out`) PLUS fourteen lines `FAIL emitted: expected set
  not yet observed — owed at the final pass · call at line <L>`, one per group at its own `L`, and
  nothing else; after: the 21 exactly. Both readings: `grep 'assertions executed' <log>` reads
  **569** — the floor-graded `n` of 555 at 46b12b93 plus the number of `emitted` calls this unit
  added, which is **14** (rev-7). Per shard the rise is 2 · 1 · 2 · 1 · 0 · 3 · 2 · 3. Red when a
  `FAIL` line appears, disappears or changes beyond that set, or `n` is not 569.
- AC4 — `reset_tree` — OBSERVED now by the static scan (`ac47.py`, output above) over the landed
  file: fourteen groups, and every S3 class located with `0 inside a group` — the check-1 exit
  arms, exit-code-only, empty-output, anchor, PATH/TMPDIR stub, remote-rewriting, every `miss`,
  every `same`, the `_f1_clean` equality arms, and the counted block; verdict GREEN. LIVENESS by the
  three planted reds above.
- AC5 — amended rev-6 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/unattended/check-unattended.test.sh` unsharded and `--shard <i>/8` for each
  `i`, reading `assertions executed in <mode> against a floor of <F>`. `FLOOR_ASSERTIONS=538` and
  `FLOOR_SHARD_1..8` (78 56 36 74 62 72 90 66) are still VALID floors — every count rose by its
  region's group count and none fell — but they are unit 3's readings, so S4's re-declaration with
  the reading beside each number is that pass's, from its own counts. Red when any count is under
  its floor, or a floor is re-declared without its reading.
- AC6 — amended rev-6 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.sh --pooled --calibrate --kit tools/unattended` on an
  idle box WITH `TOOL-aBatchedArm-3`'s arity, the longest of the eight shard walls read from the
  runner's row output and from `date +%s` either side, written into
  `tools/run-gates/selftest-budgets.txt` with the reading it was taken from. Red when the longest
  shard exceeds 1200 s. This unit now removes 14 invocations from the pair's wall; the figure is
  DERIVED there.
- AC7 — `miss` — OBSERVED now by the same scan as AC4: `groups containing a miss or a same: 0 []`,
  verdict GREEN; the planted scratch copy reports `1`, verdict RED.
- AC8 — `emitted "?" "$out"` — first half OBSERVED now: `grep -c '^emitted "?" "\$out"$'` reads 14
  and `grep -c '^emitted '` reads 14, so every call carries the sentinel; the helper REFUSES it by
  name, probed alone above (case 1). Second half owed at the build's final gate pass, the
  golden-writing step: run each `bash tools/unattended/check-unattended.test.sh --shard k/8 > <log>`
  once; for each `FAIL emitted: … · call at line <L>` take the `    observed:` lines beneath it,
  derive each line's signature as `check-arms.py` derives it (the longest literal run before the
  first interpolated value, trailing `:" ` trimmed — the helper matches by substring), and paste
  them `|`-joined as the `emitted` argument at line `L` with the run named beside it (`# set
  observed: shard k/8 at <sha>, <date>`); re-run that shard until it prints no `FAIL emitted:`
  line; then the unsharded AC3 reading. Red when a `"?"` survives, a set was typed from the arms
  rather than pasted from an `observed:` line, or the helper passes a sentinel.

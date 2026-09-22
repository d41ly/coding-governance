# TOOL-aWokenSentinel-23 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-23

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite. The pass verified with the direct checks the spec's section 7 names for it: the checker
run whole over a scratch kit seeded by the kit gate suite's own PREAMBLE (lines 1 to 278 of
`tools/unattended/check-unattended.test.sh`, sourced under `bash -c` with `$0` set to the suite so
`HERE` derives to the kit, `TMPDIR` pointed at `%TEMP%/lc23`, the arm sourced after it from the
session scratchpad's `lc23-arm.sh`), three times — the break, the near-miss and the restored copy —
with the kit gate's own suite copied into the scratch kit beside the driver suite copy, so the
population read is the one the close reads; the predicate run as a probe over every tracked `.sh`
with hits AND near-misses printed before wiring (`lc-probe.sh` in the scratchpad); the greps of
AC2, AC3 and AC5 over the tip and the base; and the `gotchas.py` reads of AC4. Those stand in for
the `unattended kit gate`, `harness arms (fail branches armed or pinned)`, `memory hygiene`,
`spec tokens` and `install-prefix` legs, which run once at the close. One spec fold was owed and
taken as rev-3: the Files-touched estimate gains the dossier claim and the generated map, because
a gotcha record is a `gotcha-classes` inventory key. The check landed as 33, one above the
high-water of 32 derived by `grep -oE 'fail [0-9]+'` at the pass.

**Evidences:** TOOL-aWokenSentinel-23
- AC1 — the copied checker over the driver suite copy with `  _x=$(printf '%s\n' "$_o" | wc -l)` spliced in after `check_status_one_line() {` (the copy's line 88, spliced from a fragment-assembled file by sed `r`) printed one FAILED line, `UNATTENDED check 33 FAILED — a shell file in this kit counts a captured variable's lines by adding a newline first — printf '%s\n', echo or a here-string into wc -l — which reads an EMPTY capture as one line, so an assertion on the count passes on a command that wrote nothing; count with printf '%s' "$x" | grep -c '' instead, which reads empty as 0. hits: unattended.test.sh:88:  _x=$(printf …`, and exited 1; the files named in the hits were `unattended.test.sh:88` and no other, with `check-unattended.test.sh` present in the scratch kit and excluded by name; the same scratch kit with the restored copy printed zero FAILED lines and exited 0; with `  _x=$(printf '%s' "$_o" | wc -l)` spliced in instead (the near-miss) it printed zero FAILED lines and exited 0. Each checker run took 14 s on node `a` inside this fixture; the 199 s the spec priced is the ledger's contended bar-leg figure. OBSERVED
- AC2 — `grep -c 'does NOT check' tools/unattended/check-unattended.sh` printed `2` at the tip and `1` at the base (`git show HEAD:tools/unattended/check-unattended.sh`, HEAD being 077788ec before this commit); the new header names `printf '%s' "$x" | wc -l` with NO newline as correct and not a hit, the intermediate-command count (`grep -o … | wc -l`) as not read, and the checker's own exclusion by name. OBSERVED
- AC3 — `python tools/memory-tree/check-arms.py --report` at the tip printed `check 33 branch 1  line 3605  ARMED` under `tools/unattended/check-unattended.sh -> tools/unattended/check-unattended.test.sh`; `grep -c 'reads an EMPTY capture as one line' tools/unattended/check-unattended.test.sh` printed `1` at the tip and the suite at the base carried no such line (the check did not exist). The `harness arms` leg's whole-population verdict is `observed at --close`. OBSERVED
- AC4 — `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.test.sh` printed `- [ ] line-count-reads-empty-capture-as-one` with the record's path beneath it (the same selection `--for-diff` makes over a range whose `--name-only` lists the driver suite; this pass's own commit range is the reading the M6 checklist takes after the commit); `--for-paths tools/gate-lint/sh_hygiene.py` selected it too; `--report` printed `unanchored : 0` and `class 4 anchor(s) line-count-reads-empty-capture-as-one`, the four being the driver suite, the checker, the kit gate's suite and the repo-wide scanner; `python tools/memory-tree/gotchas.py --check` exited 0 at the tip after `--write` regenerated `memory/gotchas/INDEX.md` to 73 records. The `memory hygiene` leg's reading is `observed at --close`. OBSERVED
- AC5 — the predicate as the check spells it, `^[^#]*`-anchored, run by `grep -cE` over `tools/unattended/check-unattended.test.sh` at the tip printed `0` (the probe's `AC5 shape` row); `grep -c 'check-unattended.test.sh) continue' tools/unattended/check-unattended.sh` printed `1`. The same predicate over every tracked `.sh` printed no hit; the nine near-misses printed beside it are the driver's eight `printf '%s' … | wc -l` lines (1286, 4592, 4694, 4752, 4828, 4931, 4996, 5129) and the driver suite's `grep -o … | wc -l` at 1540. OBSERVED
- checkers — `bash -n` exited 0 on both the checker and its suite, neither carries a CR byte, and `python tools/codebase-map/gen_map.py --check` exited 0 after `--write` re-rendered `MAP.md` and `inventories.json` with the class claimed under the unattended dossier's `gotcha-classes`. `FLOOR_ASSERTIONS` rose 416 to 422 and `FLOOR_SHARD_2` 325 to 331, the six assertions the three arms execute (two `mutate`, two `hit`, two `miss`), which the whole suite observes at the close and this pass did not; the two `mutate` calls ran inside the AC1 fixture and reported `n=2 st=0`. OBSERVED

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, install-prefix leg, map leg or `*.test.sh` suite ran
inside this pass; every one is `--close`'s and each row above says so. The `echo` and here-string
spellings were seen to fail only in the pre-wiring probe's synthetic lines (five spellings HIT,
four controls not), never staged into a suite copy: those two staged readings are
`TOOL-aWokenSentinel-28`'s by the spec's hands-off edge. The checker's header names the repo-wide
scanner as the gate-lint kit's `sh_hygiene.py` rather than by path, because the checker's row in
`tools/install-prefix-carried.txt` is shrink-only at 3 and a fourth kit literal would red the
install-prefix leg; the gotcha record, which is not a shipped file, anchors the scanner by path. No
identifier under `tools/` was minted; `_lc_*` are shell locals of the checker and the suite. The
`unattended gate selftest` budget row (13600 s against a measured 9067 s) absorbs the three added
checker runs without a re-measure. The build README's authored roster row for this unit moved
`PLANNED` to `CLOSED` beside the spec header. The dossier claim put `memory/map/features/unattended.md`
43 B over its 20480 B `DOSSIER_CAP_BYTES` (it sat 1 B under), and hygiene check 6 refused the first
commit; the Gaps bullet that still said `CORE_FLOOR` is `10:8` and two DoD items (the conf reads
`12:12`) was refreshed to point at the conf instead of counting, which is the re-derivation that
section asks for on touch and leaves the file 12 B under the cap. The NEXT claim on this dossier
cannot fit: the gate's remedy is a split into two dossiers, which no unit of this build is scoped
to do, and the curation-debt row was not taken because a row silences checks 6, 7 and 8 on the
whole file to buy 43 bytes. The bug-class checklist over the pass commit (`gotchas.py --for-diff
HEAD~1..HEAD`, 30 classes) selected `two-answers-to-one-question` against the one count the diff
typed in prose: the checker header, the arm comment and the gotcha record each said the driver's
correct idiom sits "at eight lines", a figure the near-miss grep owns; the count is removed from
all three in the follow-up commit, and the eight line numbers stay only in AC5's row above as the
measurement taken at the pass.

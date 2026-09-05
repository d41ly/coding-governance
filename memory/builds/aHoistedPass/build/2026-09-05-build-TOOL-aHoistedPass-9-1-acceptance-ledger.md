**Serves:** journal TOOL-aHoistedPass-9

# Acceptance ledger — TOOL-aHoistedPass-9

Tier-2 · node a · 2026-09-05 · spec rev-6 · pass base `c0a6d5ae`

Check 31 lands in `tools/unattended/check-unattended.sh`. When the route the `passes-harnessed`
directive names does not resolve in the tree being graded, the leg now says which case it could not
reach instead of exiting green with nothing printed. Six branches: five announced skips on the kit's
REPORT channel, each naming its own subject, and one `fail 31` for a named route script that is
absent while the directory holding it is present.

**What is graded by nothing, and is not argued away.** `tools/unattended/check-unattended.test.sh`
is on no gate leg — the 2026-08-23 owner ruling took this kit's `*.test.sh` legs off the bar — so
every arm below is an observation THIS PASS made by hand, and nothing standing re-checks it. That
suite's own state is reported below rather than summarised, because it is RED for reasons that
predate this unit and a reader owes the attribution.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-9

- **AC1** — MET — `grep -oE 'fail [0-9]+' … | sort -un` on the landed file prints
  `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 25 26 27 28 29 30 31`, and
  `git grep -c 'fail 23'` on that file returns 0, so 23 is still claimed only by `report` and
  `printf` labels.
- **AC2** — MET — the failing case for `fail 31` was observed RED before the check landed, twice. The
  block's own bytes, extracted from the landed file by its own markers and run against the real tree
  with `tools/workflows/unattended-unit.js` moved aside and its directory left in place, printed
  `UNATTENDED check 31 FAILED — … : tools/workflows/unattended-unit.js` and set `status=1`; the file
  was restored and `git status` confirmed it. The suite's F1 arm stages the same break inside the
  real checker. **That observation was taken on the SHIPPED carrier, which names TWO route scripts,
  and the verdict named only the deleted one** — the per-path property, witnessed on the real value
  rather than on a one-path fixture.
- **AC3** — MET — with the section naming the route and its directory absent, `bash tools/unattended/check-unattended.sh` prints
  no `check 31` line and `GOV_UNATTENDED_REPORT=1` prints
  `check 31 skipped for <path> — the directory that would hold it is absent`. Observed at both the
  kit's own prefix and a foreign one.
- **AC4** — MET — `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh` on the intact
  tree exits 0 and `grep -c 'check 31'` over its whole output returns **0**. The three outcomes are
  byte-distinguishable: nothing, an `unattended-report:` line, a stdout `FAILED` line with
  `status=1`.
- **AC5** — MET — with `memory/guides/BUILD-METHOD.md` removed, the REPORT run prints
  `check 31 skipped for <root>/guides/BUILD-METHOD.md — this tree carries no build-method carrier …`
  and no `fail 31` appears.
- **AC6** — MET — with the section present and naming no backticked route, `GOV_UNATTENDED_REPORT=1` prints
  `check 31 skipped for <carrier> — M6 names no backticked route script …`. The section token in that
  line came out of the registry, not out of the check.
- **AC7** — MET, in both directions, on `vendor/harness/workflows/unattended-unit.js`. With the section rewritten to
  `vendor/harness/workflows/unattended-unit.js` and that directory absent, the verdict is the skip;
  with `mkdir -p vendor/harness/workflows` and no file, it is `fail 31` naming that same foreign
  path. The check spells no install prefix — the directory under test is `dirname` of the path the
  section itself names.
- **AC8** — MET — `python tools/memory-tree/check-arms.py --check` exits 0, and `--report` shows
  `tools/unattended/check-unattended.sh check 31 branch 1 … ARMED`, with the gate at
  **176 branches (floor 101) / 168 armed (floor 100)**. No row was added to
  `memory/project/unarmed-branches.txt` and `ARMS_FLOORS` in `.memory-tree.conf` is untouched — the
  floor comparison is one-sided upward, so an added armed branch cannot breach it.
- **AC9** — MET as restated at rev-5, and the struck half is the finding. `--skip 28` reaches
  check 31 and is silent on it. `--only 28` does NOT reach it and never did: measured before any
  edit of mine, that run exits **1** printing
  `tools/unattended/check-unattended.sh: line 2932: MEMORY_ROOT: unbound variable`. Check 30 reads a
  variable assigned inside the `only28` guard, so the leg dies twenty lines before check 31 exists.
  Filed as `TOOL-aHoistedPass-37`, parked through the driver, and NOT repaired here: the one-token
  fix trades a crash for a silent skip of check 30's whole corpus walk, which is the class this build
  exists to remove.
- **AC10** — NOT MET, and `tools/unattended/check-unattended.test.sh` is the reason rather than an excuse. The suite does
  not report PASS in either shard, and it did not before this unit either. Shard 1/2 ran to
  COMPLETION — `rc=1`, 12 failures, the closing C21 arms and the shard notice both printed, and no
  assertion-floor failure, so it met its floor of 83. Shard 2/2 was re-run after the AC15 repair and
  stood at 12 failures with the run still in flight when this ledger was written; its pre-repair
  sibling was stopped at 13. **`grep -c 'check 31'` over every shard output is 0**, and the arms
  positioned after this unit's block did fire on their own unrelated causes, so the seven arms added
  here executed and none of them failed. What the criterion asked for — PASS with a raised assertion
  count — is not available from a suite that is red for four pre-existing reasons, and claiming it
  would be reporting a green nobody saw.
- **AC11** — MET — `bash tools/check-kit-versions.sh` exits 0. No literal version appears in this
  line, and that is the point: `DEPL-aHoistedPass-1` rev-5 parked the `unattended` bump to the owner,
  so order 2 moved nothing and every carrier still agrees at whatever it agreed at before. The
  checker grades agreement, not movement, and this unit moved neither.
- **AC12** — MET, after one RED from `bash tools/check-install-prefix.sh` that was mine and is the reason the arms look the way they do.
  `bash tools/check-install-prefix.sh` first refused: `ROSE tools/unattended/check-unattended.test.sh
  3 -> 9`, because six arms spelled `tools/workflows/…` literally. That gate is a BAN, not a ratchet.
  The arms now derive the route from the suite's own `KIT_REL`, the gate exits 0, and both rows in
  `tools/install-prefix-carried.txt` still read 3.
- **AC13** — MET as restated at rev-5. `bash tools/unattended/check-unattended.sh` exits 0 and its default-channel stdout is
  **byte-identical** before and after: 42 lines, 18276 bytes, `diff` silent. Both runs were taken on
  the same git state, uncommitted, so the comparison isolates check 31 rather than measuring this
  pass's own commit through check 23. "No output" was struck because check 7's EXCLUDED notices and
  check 23's dispatch-join notices print on the default channel by design and this corpus emits both.
- **AC14** — MET — with the driver's `DIRECTIVES_CORE` emptied, the REPORT run prints
  `— the directive registry names no passes-harnessed handle this leg can read`, the default run
  prints no `check 31` line, and no `fail 31` appears. This is the branch `--only 28` would have
  reached if check 30 let it.
- **AC15** — MET, the rev-5 AMEND in `tools/unattended/check-unattended.test.sh`. Its derived build-method carrier now emits each
  section's handles as well as its heading, both counted from the registry: **10 sections, 17
  distinct handles, against a registry of 17**. Before the repair the carrier named 0 of 17, so
  check 16's body term fired seventeen times and check 17's green control failed on a message about
  directives rather than about waivers.

## The suite

`bash tools/unattended/check-unattended.test.sh` was hand-run in both shards, which is the
compensating check the 2026-08-23 ruling relies on. **It is RED, and no failure names check 31** —
`grep -c 'check 31'` over every shard output returns 0. Shard 1/2: `rc=1`, 12 failures, ran to
completion and met its assertion floor. Shard 2/2, re-run after the AC15 repair: 12 failures and
still running when this was written, against 13 in the pre-repair run that was stopped to free the
machine. The check-17 waiver control that headed the pre-repair list is GONE from the repaired run,
which is AC15 witnessed in situ rather than argued.

Unlike its sibling `tools/unattended/unattended.test.sh` (`TOOL-aHoistedPass-36`), this suite does
RUN — it aborts nowhere and both regions reach their closing arms. It simply reports failures nobody
has read since its legs left the bar.

The failures are pre-existing and attributed by measurement, not by assumption:

- **`DISPOSITION_CUTOFF` is blank in the fixture conf**, so check 2 prints a notice on the DEFAULT
  channel and every arm asserting total emptiness fails — including the suite's opening control,
  `a conforming tree prints nothing`. Introduced by `TOOL-dFoldedVerdict-2` at `7bd33a4d`, present in
  `.unattended.conf` at this run's BASE `e828f778`. The shipped `.unattended.conf.example` declares
  the key BLANK, so this may be the product telling the truth rather than the fixture being wrong,
  and deciding that is `dFoldedVerdict`'s question and not this unit's.
- **`--disposition` and `--unit` are absent from the verb surfaces an agent reads.** From
  `TOOL-dFoldedVerdict-1` at `86005cdf` and `TOOL-dBriefedPass-2` at `b9fb4fb0`.
- **The protocol's stated count of core Definition-of-Done items has moved** — two `fixture no-op`
  reports on the `Ten kit-owned core items.` sed, plus an `11 against 12` count arm.
- **The derived build-method carrier fell behind check 16's body term** — this build's own
  regression, from `TOOL-aHoistedPass-2` at `8c759e50`. This is the one this pass repaired, because
  it is this build's, it is in this unit's declared write set, and the fixture's own comment names
  that failure class as the reason it is derived at all.

The rest are filed rather than fixed. Fixing another build's fixture debt inside a unit about check
31 is scope creep, and the `DISPOSITION_CUTOFF` one is not obviously a fixture bug at all.

## The bar, and one red on it that is not this unit's

`bash tools/memory-tree/check-memory-hygiene.sh` exits **1**, on check 23: an acceptance-ledger AC
line must carry a backticked token on its OWN first line, or name `amended rev-N`, or be a checkbox —
the classifier in `tools/memory-tree/check-memory-hygiene.sh` at line 1430 reads that one line and nothing
below it. Seventeen entries were named. **Nine were mine and are fixed**: AC2, AC3, AC5, AC6, AC7,
AC10, AC12, AC13 and AC15 carried their evidence on a continuation line, and each now names it up
front. No claim changed.

**The other eight are `TOOL-aHoistedPass-6`'s**, and this leg was already RED before this pass began.
Measured at the pass base `c0a6d5ae`: AC2b, AC7, AC10, AC15, AC17, AC21, AC22 and AC23 of that
ledger were already in the bad form, and `git diff c0a6d5ae..HEAD` shows this pass never touched that
file. They are filed as `TOOL-aHoistedPass-39` rather than repaired here. Repairing them is NOT
mechanical: each line's evidence sits in its continuation prose, so choosing the token means reading
that unit's evidence and deciding what it was, which is rewriting another unit's conformance claim
from the outside. The remedy is one line each and belongs to whoever closes that unit or the build.

The other two hygiene lines are REPORTED rather than gated: a check 16 read-path finding about
`memory/map/baseline.toml`, and a check 15 citation in `memory/backlog/TOOL.md`
for `TOOL-aHoistedPass-33`, which is not this pass's row.

## What this unit did not do

- It did not repair check 30's `--only 28` crash. `TOOL-aHoistedPass-37`.
- It did not move the `unattended` kit version. `DEPL-aHoistedPass-1` parked that to the owner.
- It does not grade whether the route script WORKS, only that a path the section names in backticks
  resolves. A present-but-broken script passes, and the block's own header says so.
- It filed a backlog row in `memory/backlog/TOOL.md`, which `--dispatch` refuses to accept in a write
  set because that path is a declared shared mutable record. Same residual `TOOL-aHoistedPass-4` and
  `-6` recorded in this run: a unit whose scope files a backlog row has a write no dispatch row names.

# TOOL-dFinishedRecord-1 — acceptance ledger

**Serves:** journal TOOL-dFinishedRecord-1

The main loop observed the owed arms at the close, in a throwaway clone at `9feeafc6b`. The
`New arm:` line owes arms A to C. Each run was the suite's region 8 alone (`--shard 8/8`). The
instrument is reproduced below under Instruments.

The arms ran four times:

- Green at the pass commit: 234 assertions, 0 FAIL lines.
- With the parent leg in place: 3 FAIL lines.
- With the staged break `rs_dl=0`: every check 24 roster arm red, arm B included.
- With the `rs_unavail=1` guard deleted: 1 FAIL line.

The leg itself ran once over the build's tip, for AC5.

The spec's third red form for AC3 was not staged: return 2 treated as excluded. Arm C's two other
red forms were observed.

**Evidences:** TOOL-dFinishedRecord-1
- AC1 — `check 24 FAILED` — at the pass commit, arm A passed. On the parent leg it
  failed twice: "missing: check 24 EXCLUDED memory/builds/tRos/RUN.md — derived LANDED: its
  landing commit 41ee9aaf…", then "unexpected: check 24 FAILED".
- AC2 — `rs_dl=0` — under that staged break, region 8 printed "missing: so the scope moved with
  nothing on the record saying so: ARCH-tRos-7 in memory/builds/tRos/RUN.md". It then printed
  "unexpected: check 24 EXCLUDED", once for arm B and once for arm C. Every other check 24 roster
  `hit` went red with them. With the break restored, the region passed.
- AC3 — `check 24 exclusion UNAVAILABLE` — the line printed once at the pass commit. The parent
  leg failed "prints once: expected [1], got [0]". With the `rs_unavail` guard deleted, the region's
  one FAIL line was "expected [1], got [2]".
- AC4 — `git diff 51912ffc -- tools/unattended/check-unattended.test.sh` — the diff removes two
  lines, `FLOOR_ASSERTIONS=1133` and `FLOOR_SHARD_8=208`. Both sit outside the check 24 roster
  block. Region 8 passed at the pass commit with 0 FAIL lines, so every existing `hit`, `miss` and
  `same` of the block stayed green.
- AC5 — `bash tools/unattended/check-unattended.sh` — over the build's tip `9feeafc6`, the leg
  printed "check 24 EXCLUDED memory/builds/dConvergedCharter/RUN.md — derived LANDED: its landing
  commit 923954b6…". It printed 0 `check 24 FAILED` lines. The landing attempt's bar over
  `51912ffce` carried the parent leg's `check 24 FAILED` for PLAY-dConvergedCharter-41. The
  prepared merge's leg runs inside the lander's bar.
- AC6 — `grep -c '^check_derived_landed()'` — prints 1 at the pass commit. The call-site grep
  prints 1. The diff from `51912ffc` adds no line naming `read_landing_commit` or
  `check_adv_reaches`, which prints 0.
- AC7 — `sed -n 1,45p tools/unattended/check-unattended.sh` — at the pass commit the header
  carries both `check 24 EXCLUDED` and `check 24 exclusion UNAVAILABLE`.
- AC8 — `FLOOR_ASSERTIONS` — prints 1140 and 1140 is 1133 plus 7. `FLOOR_SHARD_8` prints 215 and
  215 is 208 plus 7. `grep -c 'TOOL-dFinishedRecord-1'` over the suite prints 2.
- AC9 — `bash -n tools/unattended/check-unattended.sh` — exits 0 at the pass commit. The bare-CR
  count is 4 at `51912ffc` and 4 at `9feeafc6b`.
- AC10 — `KIT_UNATTENDED_VERSION` — prints `1.113` at line 62 of the pass commit.

## Instruments

The arm-observation script, run from the session scratchpad:

```bash
#!/usr/bin/env bash
SRC=C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347
SP="<session scratchpad>"
C=C:/Users/d41ly/AppData/Local/Temp/dfr
rm -rf "$C"; git clone -q --no-hardlinks "$SRC" "$C" && git -C "$C" checkout -q 9feeafc6b6ca8dfef0c3560829930ccc2d476942 || exit 9
cd "$C"
L=tools/unattended/check-unattended.sh
runit() { local tag=$1; bash tools/unattended/check-unattended.test.sh --shard 8/8 > "$SP/arm-$tag.log" 2>&1; echo "$tag rc=$? $(grep -ciE '^FAIL|FAIL:' "$SP/arm-$tag.log") fail-lines"; }
runit green
git show HEAD~1:$L > $L; runit parent; git checkout -q -- $L
sed -i 's/rs_dl=\$?/rs_dl=0/' $L; git diff --stat; runit break-dl; git checkout -q -- $L
sed -i '/^ *rs_unavail=1/d' $L; git diff --stat; runit break-unavail; git checkout -q -- $L
echo done
```

AC5 was `bash tools/unattended/check-unattended.sh` at the worktree's tip `9feeafc6b`, its output
redirected to the scratchpad.

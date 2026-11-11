# TOOL-dFinishedRecord-2 — acceptance ledger

**Serves:** journal TOOL-dFinishedRecord-2

The main loop observed arm D at the close, in a throwaway clone at `2d4ee43dc`. Each run was the
suite's region 8 alone (`--shard 8/8`):

- Under the staged break, the region printed 2 FAIL lines.
- With the break restored, it passed 236 assertions with 0 FAIL lines.

The script then ran the unsharded suite, which the owner's standing instruction forbids. The run
executed 1457 assertions against the floor of 1142 and exited 1 on three FAIL lines. They were the
verb-surface arm, a promotion-count arm and check 30's population pattern. All three read files
this build does not touch, and none is in check 24. Whether they also fail at `3acab47a8` was not
observed.

AC2 to AC8 were observed at `2d4ee43dc` in the worktree, with the spec's `S`, `B`, `O` and `A` set.

**Evidences:** TOOL-dFinishedRecord-2
- AC1 — `check 24 FAILED` — under the staged break `case "$ph" in LANDING) ...`, region 8's two
  FAIL lines were the following:
  - "missing: check 24 EXCLUDED memory/builds/tRos/RUN.md — derived LANDED: its landing commit
    693e2703…"
  - "unexpected: check 24 FAILED"

  Arms A to C stayed green. With the break restored, the region passed.
- AC2 — `reset_tree` — the heading grep printed `# A:`, `# B `, `# C:`, `# D:` and `rese` in that
  order. The block's `hit|miss|same` count is 9. The HELD fixture string count is 1. The arm-D
  comment count is 1. `bash -n` exits 0.
- AC3 — `RAISED 1140 -> 1142 by exactly the arms, TOOL-dFinishedRecord-2` — the floor grep printed
  `FLOOR_ASSERTIONS=1142` and `FLOOR_SHARD_8=217`. The raise comment count is 1.
- AC4 — `after its recorded-phase skip` — prints 0 over the build README. The reworded row-1 grep
  prints 1.
- AC5 — `python tools/memory-tree/gotchas.py --for-paths tools/unattended/check-unattended.sh` —
  the class grep prints 2.
- AC6 — `TOOL-dFinishedRecord-1` — inside Where it bit it counts 1 in
  `observed-by-claim-no-arm-discharges` and 2 in `amendment-leaves-its-other-half-standing`. The
  two-surfaces sentence counts 1. The one-surface sentence counts 0.
- AC7 — `ANCHOR_RE` — the anchor count prints 7 for the first class and 13 for the second. Each
  INDEX row grep prints 1. `git diff --numstat a18457df -- memory/gotchas/INDEX.md` prints 2 added
  and 2 deleted.
- AC8 — `tools/unattended/lib-unattended.sh` — `git diff --stat a18457df 2d4ee43dc` over the leg,
  the library and the driver prints nothing.

## Instruments

The arm-observation script, run from the session scratchpad:

```bash
#!/usr/bin/env bash
SRC=C:/projects/coding-governance/.claude/worktrees/unattended-dconvergedcharter-51d347
SP="<session scratchpad>"
C=C:/Users/d41ly/AppData/Local/Temp/dfr2
rm -rf "$C"; git clone -q --no-hardlinks "$SRC" "$C" && git -C "$C" checkout -q 2d4ee43dc || exit 9
cd "$C"; L=tools/unattended/check-unattended.sh
python - "$L" <<'PY'
import sys
p=sys.argv[1]; b=open(p,'rb').read()
old=b'check_derived_landed "$f"; rs_dl=$?'
assert b.count(old)==1
b=b.replace(old,b'case "$ph" in LANDING) check_derived_landed "$f"; rs_dl=$? ;; *) rs_dl=1 ;; esac')
open(p,'wb').write(b)
PY
git diff --stat
bash tools/unattended/check-unattended.test.sh --shard 8/8 > "$SP/arm-d-break.log" 2>&1; echo "d-break rc=$?"; grep -E '^FAIL' "$SP/arm-d-break.log" | cut -c1-160
git checkout -q -- $L
bash tools/unattended/check-unattended.test.sh --shard 8/8 > "$SP/arm-d-green.log" 2>&1; echo "d-green rc=$?"; grep -cE '^FAIL' "$SP/arm-d-green.log"
bash tools/unattended/check-unattended.test.sh > "$SP/arm-d-full.log" 2>&1; echo "full rc=$?"; grep -cE '^FAIL' "$SP/arm-d-full.log"; tail -3 "$SP/arm-d-full.log"
```

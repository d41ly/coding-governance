# TOOL-dTotalRecall-77 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-77
**Caused-by:** TOOL-dTotalRecall-77

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-4 over
base `0573fa2c551f945b6c35a5df83936786d353f4c4` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The probe is §4's two bash fences, one file under the scratch directory, read equal to the spec's fences extracted by
`diff`, and run by its path with the repository root as its one argument (DERIVED 2026-11-24, that run).

The probe's lines, its exit 0 (DERIVED 2026-11-24, that run). The failed `cd` of `absent` and the refused empty path of
`empty` each wrote one line to stderr, which is the shell's and not a line of `read_checker`.

```text
fail lines 1
stall rc=1
stall MANIFEST check 9 FAILED — stalled
two rc=1
two MANIFEST check 5 FAILED — stale
two MANIFEST check 9 FAILED — stalled
crash rc=2
green rc=0
absent rc=1
empty rc=1
old pipe 0
```

The checker's file is unchanged between `aec378661`, which §4 pins, and the base: `git diff --stat` over it printed
nothing (DERIVED 2026-11-24, that command).

Unit 76's sweep, its last unit line and its staged read, copied from the block in
`2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md`, where the sweep's ASCII output holds `?` for the
checker's dash. The line before `live` is the same clone's checkout read unstaged, and no failure line stands beneath it:

```text
87 073d03dd7df748eccc25079328c2199fa132c972 rc=0
live rc=1
live MANIFEST check 9 FAILED ? last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite: 0000000000000000000000000000000000000000
```

**Evidences:** TOOL-dTotalRecall-77
- AC1 — `fail lines 1` — the probe printed `fail lines 1`, `stall rc=1`, `stall MANIFEST check 9 FAILED — stalled`, `two rc=1`, `two MANIFEST check 5 FAILED — stale`, `two MANIFEST check 9 FAILED — stalled`, `crash rc=2`, `green rc=0`, `absent rc=1`, `empty rc=1` and `old pipe 0`, and no other line on stdout. The `git grep` for `live (rc=|MANIFEST check 9 FAILED)` over unit 76's ledger printed two lines: `live rc=1` and `live MANIFEST check 9 FAILED ? last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite: 0000000000000000000000000000000000000000` (DERIVED 2026-11-24, these runs).
- AC2 — `git grep -n "Evidences:\*\* TOOL-dTotalRecall-77" -- memory/builds/dTotalRecall/build` — run with `--untracked` before the commit, printed this ledger's block line alone. The sweep's last unit line before `live` is `87 073d03dd7df748eccc25079328c2199fa132c972 rc=0`, with no failure line beneath it and so no check-9 failure: the staging alone put one in `live` (DERIVED 2026-11-24, this command and unit 76's block read here).

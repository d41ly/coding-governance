# TOOL-dQuietDisk-19 — acceptance ledger

**Serves:** journal TOOL-dQuietDisk-19

This pass ran no merge bar, no self-test suite, no gate leg, no `--selftest` and no instrument. Every reading is the main loop's, committed in `291aa99e4` (B0) and `b57a5eeb7` (A). The pass derived the Comparison section with a Python script in the session scratch directory and read the nicocares record as a committed blob only. Each block below ran on node d on 2026-11-22 under python 3.15.2 and git 2.54.0.windows.1, from the worktree root, with `$P` written from the spec's own section 5 block. Every line marked OWED belongs to the main loop at the close.

**Evidences:** TOOL-dQuietDisk-19
- AC1 — `The instrument` — at the pass, after the `### The instrument` heading line was added above the B0 fence, the AC1 block printed `spec True record True identical True`.
- AC2 — `python "$P" "$REC"` — at the pass, the probe printed only `probe done`: no `missing ` or `bad ` line, so the eleven B0, A-off and A-on rows hold integer cells, and M1's A-off row reads `not taken` with its reason.
- AC3 — `B0 is the build base` — at the pass, the AC3 block printed `B0 is the build base` and `A is one ancestor of HEAD`, and no `late` line.
- AC4 — `cell-mismatch` — at the pass, the probe printed no `cell-mismatch`, `missing-comparison`, `missing-reading-for` or `bad-comparison-row` line over the sixteen rows. A scratch copy with one `saved` cell moved by 1 printed `cell-mismatch M3 git processes`.
- AC5 — `rc-differs-unnamed` — at the pass, the probe printed no `rc-differs-unnamed` line: each subject's A-on rc equals its before rc (M1 1, M2 0 and 0, M3 1), so Limits carries no `rc differs:` line.
- AC6 — `bound-uncited` — at the pass, the probe printed no `bound-uncited` line. A scratch copy whose M1 peak quote read "never rise" printed `bound-uncited M1 peak temp TOOL-dQuietDisk-10`.
- AC7 — `source resolves` — at the pass, the AC7 block printed `source resolves` for the section's `source:` line, and `cmp` found the copied rows identical to `git show 7b9396cae:memory/builds/dSeededKiln/build/measurements.txt` in `C:/projects/nicocares/main`.
- AC8 — `bash "$I" "$R" "$W" "$A" A-on-again M2 2 '^pass-order: graded' -- bash tools/unattended/check-pass-order.sh` — the main loop's re-take, committed in `b57a5eeb7`: the pass read the A-on-again M2 rows' git-process cells, 8811 and 24, equal to the A-on M2 rows' 8811 and 24.
- AC9 — `name True serves True sections True` — at the pass, the AC9 block printed that line over the record's eight sections.
- AC10 — `awaiting:` — at the pass, the AC10 block printed `awaiting: TOOL-dQuietDisk-18 AC8, the main loop's at VERIFYING`. OWED: the main loop's VERIFYING records commit replaces it with the counts line.
- Gates — `memory hygiene` — OWED: `memory hygiene`, `recall floor`, `recall floor arms`, `pass-order history` and `brief-recorded`, at the close. No arm is added or moved.

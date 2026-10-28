**Serves:** journal TOOL-dSafePassage-78

# TOOL-dSafePassage-78 — acceptance ledger

The unit as built, at spec rev-2. Product writes: `tools/govkit/govkit.py` (S2, the walk branch's
`or schema < 3` and its third reason), `tools/govkit/selftest.py` (S1 the walk-refusal block over a
scratch repository, S3 the AC9 loop's `--kits`, S5 `extract_plan_writes`, S6 the shim check) and
`help/upgrade-steps.md` (S4).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree's working copy, by `git grep`, the unit's fixture CLI, or §4's probes
written to the run's scratchpad, with fixture targets under `%TEMP%/p78` (removed after).

Where the build met what the spec does not say: §4's probes ran from the worktree root rather than a
`git clone --shared`, so the schema probe read the working copy's `govkit.py`; the source probe's clone
is `--shared` of the worktree's HEAD. AC2's red side was observed from a `git clone --shared` of HEAD
(S2 not yet in it). S1 was also probed by a scratch replica of the block calling `run_step_walk`
directly, not by loading the suite file.

Owed at the close: every `New arm:` line's RED-first observation — the three `[dSP-2] S2` rows of
`check_step_walk` (AC1), the `[dSP-3 AC2]` and `[dSP-3 AC9]` rows of `check_receipt_schema` (AC2, AC3),
the `[dSP-8] AC3` files row of `check_source_mode` (AC5), the ten `[dSafePassage-6] AC6 ... missing`
rows of the shim block (AC6) — and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-78
- AC1 — the spec's `git grep` — printed three lines, `selftest.py:4588`, `:4590`, `:4601`, each inside `check_step_walk` (`:4434` to the next `def`). A scratch replica of the block over `run_step_walk` printed `PASS` for `spoiled`, `unstaged` (`fx/x: \`git add\` refused the step's writes`) and `escaping` (`'../x.txt' is not a path inside the target`) with the `git init` target, and `FAIL` for all three without it (`rev-parse --absolute-git-dir exits 128`).
- AC2 — `python <scratch>/schema_probe.py 2` — printed `0 3 True []`, `govkit update — steps: not walked — the receipt is at schema 2, and its first step starts from 3: this run lifts it to 3, and the next \`update --write\` walks them · 3 pending`, and `0 4 [('govkit/receipt-schema-4', 'applied')]`. From a clone of HEAD without S2 it printed `1 2 True []`, `stopped at govkit/receipt-schema-4`, `1 2 []`.
- AC3 — `python <scratch>/schema_probe.py 3 --kits check-wiring` — printed `0 3 True []`; the spec's `git grep` printed `selftest.py:4922`, the AC9 loop's line.
- AC4 — the spec's `git grep` — printed one line, `help/upgrade-steps.md:233`, inside the `--kits` bullet.
- AC5 — `python <scratch>/source_probe.py` — printed `True False`; the spec's `git grep` printed one line, `selftest.py:5209`.
- AC6 — `shims.py --fixture --plant window --window 2 --releases 1 --expect allowed` — exit 1, one `MISS`, last line `0 of 1 observation(s) matched`; with `--expect held` — exit 0, no `MISS`, `1 of 1 observation(s) matched`; the spec's `git grep -c` printed `2`.

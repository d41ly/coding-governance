# TOOL-dGroundRules-44 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-44

No merge bar, no gate leg and no self-test suite ran in this pass. The read criteria ran in this
worktree from the repository root. The staged criteria ran on a `git clone` of the branch under
`%TEMP%/gr44`, each staging applied by a scratch script and the clone reset before the next. The
arm was run alone: a scratch driver lifted the lines from `OVERLAP_PAIRS=` to the arm's closing `fi`
out of a copy of the suite and evaluated them against the clone, with `PFX` at `tools/`. With
`NOT_A_TRAP` staged, the HEAD copy of the arm printed `arm ok` and the built copy printed
`arm FAIL ... [row policy/a.py policy/ab.py disjoint: not a string-prefix trap]`; with `RAW_BOTH`
staged the built copy printed `arm FAIL ... [row policy policy-x.py disjoint: check_writes_intersect
True] [row policy policy-x.py disjoint: overlaps exit 0]`; unstaged, both copies printed `arm ok`.
Owed at the close: the `spec-tokens self-test` over the built tree and the `New arm:` line's red-first
observation (AC2, AC3).

**Evidences:** TOOL-dGroundRules-44
- AC1 — `TRAP_PROBE` from the root — printed one line, `policy policy-x.py True False`, read from the last line of the quoted `OVERLAP_PAIRS` string.
- AC2 — `TRAP_PY` and `TRAP_SH` from the root — printed `False` and `1`; with `RAW_BOTH` staged in `SCRATCH` they printed `True` and `0`.
- AC3 — `NOT_A_TRAP` staged in `SCRATCH`, then `TRAP_PROBE` — printed one line, `policy/a.py policy/ab.py False False`, which matches `NOT_A_TRAP_WANT`; the arm run alone over that copy failed naming `not a string-prefix trap`, and passed over the HEAD copy of the arm.

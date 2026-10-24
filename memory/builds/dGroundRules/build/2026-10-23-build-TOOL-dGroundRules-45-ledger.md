# TOOL-dGroundRules-45 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-45

No merge bar, no gate leg and no self-test suite ran in this pass. The read criteria ran in this
worktree from the repository root, `PAIRS_TABLE` from a scratch file holding its §6 text verbatim.
The staged criterion ran on a `git clone` of the branch under `%TEMP%/gr45` carrying the built suite.
The arm was run alone: a scratch driver lifted the lines from `UNATTENDED_DIR=` to the arm's closing
`fi` out of the suite and evaluated them with `PFX` at `tools/`. Unstaged it printed `arm ok` with 2
rows; with `ROW_ADDED` it printed `arm ok` with 3 rows; with the trap row's expected answer staged to
`intersect` it printed `arm FAIL ... [row policy policy-x.py intersect: check_writes_intersect False]
[row policy policy-x.py intersect: overlaps exit 1]`, one disagreement per rule; with the disjoint
row respelled `policy/a.py policy/ab.py disjoint` it printed `arm FAIL ... not a string-prefix trap`.
`TOOL-dGroundRules-44`'s `TRAP_PROBE` printed `policy policy-x.py True False` from the call line, and
`TOOL-dGroundRules-40`'s `ARM_ROWS` and `ARM_NOTE` printed `1` and `0`. Owed at the close: the
`spec-tokens self-test` over the built tree and the `New arm:` line's red-first observation (AC2).

**Evidences:** TOOL-dGroundRules-45
- AC1 — `ROW_COUNT` on the built tree — printed `2`.
- AC2 — `PAIRS_TABLE` on the built tree — printed exactly the two lines of `PAIRS_WANT`: `tools/policy/ tools/policy/x.py intersect True 0` and `tools/policy tools/policy-x.py disjoint False 1`.
- AC3 — `ROW_ADDED` in the `%TEMP%/gr45` copy, then `PAIRS_TABLE` there — printed three lines, the third `tools/docs tools/docs-x.md disjoint False 1`.

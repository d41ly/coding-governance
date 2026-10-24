# TOOL-dGroundRules-40 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-40

No merge bar, no gate leg and no self-test suite ran in this pass. AC1, AC2, AC4 and AC5 ran from
this worktree's root. AC3 ran from a fixture git repository under `%TEMP%/d40fx` holding copies of
the unattended, memory-tree and lib kits, with `check_writes_intersect` and `covers` both staged by a
script to a raw `startswith` in either direction. The same fixture ran the arm itself, extracted from
the suite: green on clean copies, red naming the disjoint row once per rule under both stagings, red
naming only the staged rule under either one alone, and red with `rows 0` on an emptied table. Owed
at the close: the `spec-tokens self-test` leg over the built tree and the new arm's red-first
observation (AC3).

**Evidences:** TOOL-dGroundRules-40
- AC1 — `PAIRS_PY` — printed `True` then `False`.
- AC2 — `PAIRS_SH` — printed `0` then `1`.
- AC3 — `RAW_BOTH`, then `PAIRS_PY` and `PAIRS_SH` in the fixture — printed `True`, `True`, `0`, `0`; the extracted arm printed `arm FAIL` naming `[row policy policy-x.py disjoint: check_writes_intersect True] [row policy policy-x.py disjoint: overlaps exit 0]`.
- AC4 — `ARM_ROWS` — printed `1`.
- AC5 — `ARM_NOTE` — printed `0`.

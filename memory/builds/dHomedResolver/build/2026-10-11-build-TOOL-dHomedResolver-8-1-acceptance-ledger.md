# Acceptance ledger — TOOL-dHomedResolver-8

**Serves:** journal TOOL-dHomedResolver-8

Built on `5c8d7625`. All three legs were observed red first, at `b726385f` itself in a detached
worktree, with the same failure lines the close's bar printed: the parity arm's four `does not
declare` lines, arm 26's mint subject naming no unit, and `36db2dbf` naming no unit. On this code the
three run green through the bar runner with a selected legs file.

**Evidences:** TOOL-dHomedResolver-8
- AC1 — `check-memory-hygiene.sh` — the suite passes at 569 assertions and prints no `does not declare` line for the three routed keys or GATE_PUSH_BASE; four such lines at b726385f
- AC2 — `26 the attended mint commit names the` — the push-main suite's arm 26 passes; red at b726385f
- AC3 — `routed_commits.py` — with GATE_PUSH_BASE unset it lists no FAILED commit, 13 waived; 36db2dbf was its one offender at b726385f

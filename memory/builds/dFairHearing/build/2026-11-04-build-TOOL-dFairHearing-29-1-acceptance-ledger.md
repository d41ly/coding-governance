# Acceptance ledger — TOOL-dFairHearing-29

**Serves:** journal TOOL-dFairHearing-29

Built against spec rev-3 in pass commit `fb6c5b8d3`, whose parent is `59afeaaa9`. The main loop drafted this ledger at the close from the builder return. `members.py` is the spec's script, written under the pass's scratch directory. Units 16, 23 and 26 had finished the move, so no suite changed. No suite, gate or bar ran in the pass: the spec's gate legs and the `New arm:` line's RED and GREEN are owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-29
- AC1 — `python members.py 3708a705` — it printed five `member` lines, at :874, :959, :985, :988 and :1063, each label holding an escaped quote and equal to the spec's table byte for byte, and exited 0. This line is `precondition` evidence: it reads only `3708a705`, so it is green before any build
- AC2 — `python members.py 3708a705` — with `tools/hooks/agent-cap.test.sh` and `tools/workflows/spec-audit-optin.test.sh` as its two paths, it printed no `home`, `gone` or `not a member` line and exited 0. A grep found the :874 and :1063 arms in the pack's suite at lines 331 and 520, so the pass is no match on nothing
- AC3 — `not a member :873` — three staged breaks each exited 1. The pack's suite with line 331 cut printed the `home` line for `rule0: kind [\"spec-audit\"] (an array) on the undeclared README → deny`, the hook's suite with the :1063 arm appended printed a `gone` line naming that label, and `LINES` holding 873 printed `not a member :873`

## Supersessions

Each one is named by the hands-off bullet to `TOOL-dFairHearing-36` in this unit's spec.

- `TOOL-dFairHearing-29` S2 and AC2 — the move sentence and AC2 are answered by `TOOL-dFairHearing-36` S1, the move being unit 28's alone
- `TOOL-dFairHearing-29` AC1 — recorded as `precondition` evidence by `TOOL-dFairHearing-36` S7

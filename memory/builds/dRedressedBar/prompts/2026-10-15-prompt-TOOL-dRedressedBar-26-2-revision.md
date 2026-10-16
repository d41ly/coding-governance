# Revision — dRedressedBar: TOOL-dRedressedBar-26's spec-writer pass, spec 24 corrected in place

**Serves:** research TOOL-dRedressedBar-26 TOOL-dRedressedBar-24

## The brief

### Goal
Unit 25 is CLOSED at `8e1fe8782`; `<w25>` did not touch spec 24. Run spec 26's `<w26>` pass now, before its build pass: apply every row of spec 26 §4's correction table to spec 24, and add the `hands-off TOOL-dRedressedBar-26` mirror bullet spec 26's §3 `consumes-from` edge needs. Spec 24 takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-26` and every report id the table assigns it (22, 6, 7, 10, 21, 8, 19), and stays CLOSED.

### Items
1. **TOOL-dRedressedBar-24** — the table's rows and the mirror bullet, exactly as spec 26 §4 states them. Read spec 26 S24, that §4 section and the AC that reads `<w26>` first; that AC reads this commit, so the diff must satisfy it. Unit 25 edited `tools/run-gates/measure_legs.py` and `tools/gate-legs.json` but not `tools/gate-lint/sh_hygiene.py` or the runner scripts, so spec 26's cites into those should still hold; confirm each, cite the tip's line where one moved, and report any row already true or whose target is gone.

### Acceptance
`git diff` over spec 24 shows one header rev change, one new revision line and the table's edits, and nothing else; it still reads CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 26 READY, and a full `memory hygiene` run reports no check 12 reciprocity line for unit 26.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 24. No status change.

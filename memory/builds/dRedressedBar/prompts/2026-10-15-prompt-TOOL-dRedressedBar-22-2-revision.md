# Revision — dRedressedBar: TOOL-dRedressedBar-22's spec-writer pass, specs 18 and 19 corrected in place

**Serves:** research TOOL-dRedressedBar-22 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19

## The brief

### Goal
Unit 21 is CLOSED at `64e887ae6`. Run spec 22's `<w22>` pass now, before its build pass: apply every row of spec 22 §4's correction table to its target, spec 18 or spec 19, and add the `hands-off TOOL-dRedressedBar-22` mirror bullets §3's `consumes-from` edges need. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-22` and every report id the table assigns it, and stays CLOSED.

### Items
1. **TOOL-dRedressedBar-18 and -19** — the table's rows, exactly as spec 22 §4 states them. Read spec 22's S-item for the record, that §4 section and the AC that reads `<w22>` first; that AC reads this commit, so the diff must satisfy it. Unit 21 (`dc732dba3`) and `<w21>` (`e41b65e47`) moved `tools/run-gates/measure_legs.py`'s lines and bumped both specs since spec 22 was written: apply each row to the text as it stands, cite the tip's lines, keep `<w21>`'s corrections true alongside yours, and report any row already true or whose target is gone.

### Acceptance
`git diff` over specs 18 and 19 shows, in each, one header rev change, one new revision line and the table's edits, and nothing else; both still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 22 READY, and a full `memory hygiene` run reports no check 12 reciprocity line for unit 22.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 18 and 19. No status change.

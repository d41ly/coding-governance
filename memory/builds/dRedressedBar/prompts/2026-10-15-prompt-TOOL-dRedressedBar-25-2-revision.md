# Revision — dRedressedBar: TOOL-dRedressedBar-25's spec-writer pass, specs 18, 21 and 22 corrected in place

**Serves:** research TOOL-dRedressedBar-25 TOOL-dRedressedBar-18 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22

## The brief

### Goal
Specs 25 and 26 are committed at `b5472169f` and both grade READY. Run spec 25's `<w25>` pass now, before its build pass: apply every row of spec 25 §4's correction table to its target, spec 18, 21 or 22, and add the three `hands-off TOOL-dRedressedBar-25` mirror bullets that section words exactly. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-25` and every report id the table assigns it, and stays CLOSED.

### Items
1. **TOOL-dRedressedBar-18, -21 and -22** — the table's rows and mirror bullets, exactly as spec 25 §4 states them. Read spec 25's S-item for the record, that §4 section and the AC that reads `<w25>` first; that AC reads this commit, so the diff must satisfy it. Where a cited line has moved, apply the row to the text as it stands, cite the tip's line, keep every earlier correction true alongside yours, and report any row already true or whose target is gone.

### Acceptance
`git diff` over specs 18, 21 and 22 shows, in each, one header rev change, one new revision line and the table's edits, and nothing else; all three still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 25 READY, and a full `memory hygiene` run reports no check 12 reciprocity line for unit 25.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 18, 21 and 22. No status change.

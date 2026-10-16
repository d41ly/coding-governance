# Revision — dRedressedBar: TOOL-dRedressedBar-23's spec-writer pass, specs 12 and 14 to 17 corrected in place

**Serves:** research TOOL-dRedressedBar-23 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17

## The brief

### Goal
Units 21 and 22 are CLOSED (unit 22 at `c84518fff`). Run spec 23's `<w23>` pass now, before its build pass: apply every row of spec 23 §4 "What this unit corrects" to its target, spec 12, 14, 15, 16 or 17, and add the `hands-off TOOL-dRedressedBar-23` mirror bullet each of spec 23's §3 `consumes-from` edges needs. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-23` and every report id the table assigns it, and stays CLOSED.

### Items
1. **TOOL-dRedressedBar-12, -14, -15, -16 and -17** — the table's rows, exactly as spec 23 §4 states them. Read spec 23's S-item for the record, that §4 section and the AC that reads `<w23>` first; that AC reads this commit, so the diff must satisfy it. `<w19>` bumped these specs since spec 23 was written and units 21 and 22 touched no govkit file, so its `tools/govkit/` line cites should still hold at the tip; confirm each, cite the tip's line where one moved, keep every earlier correction true alongside yours, and report any row already true or whose target is gone.

### Acceptance
`git diff` over specs 12 and 14 to 17 shows, in each, one header rev change, one new revision line and the table's edits, and nothing else; all five still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 23 READY, and a full `memory hygiene` run reports no check 12 reciprocity line for unit 23.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 12 and 14 to 17. No status change.

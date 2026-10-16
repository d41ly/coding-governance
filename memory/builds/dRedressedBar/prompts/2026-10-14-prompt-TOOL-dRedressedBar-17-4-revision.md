# Revision — dRedressedBar: TOOL-dRedressedBar-17's spec-writer pass, specs 9, 12, 13, 14 and 15 corrected in place

**Serves:** research TOOL-dRedressedBar-17 TOOL-dRedressedBar-9 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15

## The brief

### Goal
Units 9 to 16 are CLOSED (unit 15 at `7da62c241`). Run spec 17's S25 first half now, as the pass §4 names `<w17>`: apply every row of spec 17 §4's correction table to its target spec, 9, 12, 13, 14 or 15. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-17` and every report id the table assigns that spec. Each is a records fix with its status unchanged: all five stay CLOSED.

### Items
1. **TOOL-dRedressedBar-9, -12, -13, -14 and -15** — the table's rows, exactly as spec 17 §4 states them. Read spec 17 S25, §4's correction-pass paragraph and table, and AC25 first; AC25 reads this commit, so the diff must satisfy it.
2. **What moved since spec 17 was written.** Several passes landed after it: `<w13>`, `<w14>` and `<w16>` bumped specs 9 to 12; unit 15's spec took rev-4 (S10 and AC11, the CONFIGURE comment); and units 13 to 16 edited `tools/govkit/govkit.py`, `tools/govkit/matrix.py` and `tools/govkit/selftest.py`. Where a row's cited lines, criterion numbers or sentences have moved, apply the row's intent to the text as it stands at the tip, cite the tip's lines, and say so in that spec's revision line. Keep every earlier correction true alongside yours. If a row's target sentence no longer exists or a row is already true at the tip, say so in the revision line and change nothing for it; report each such row.

### Acceptance
`git diff` over specs 9, 12, 13, 14 and 15 shows, in each, one header rev change and one new revision line, plus the table's in-place edits, and nothing else. All five headers still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 17 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 9, 12, 13, 14 and 15. No status change.

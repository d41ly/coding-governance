# Revision — dRedressedBar: TOOL-dRedressedBar-21's spec-writer pass, specs 18 and 19 corrected in place

**Serves:** research TOOL-dRedressedBar-21 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19

## The brief

### Goal
Spec 21 (rev-2) is committed at `9bf1eb443` and READY. Run its `<w21>` pass now, before its build pass: apply every row of spec 21 §4 "What this unit corrects in each spec" to its target, spec 18 or spec 19, and add the two mirror bullets that section words exactly. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-21` and H1, and stays CLOSED.

### Items
1. **TOOL-dRedressedBar-18 and -19** — the table's rows and mirror bullets, exactly as spec 21 §4 states them. Read spec 21 S7, that §4 section and AC8 first; AC8 reads this commit, so the diff must satisfy it. Where a cited line has moved since spec 21 was written (`<w19>` and units 18 and 19 edited both specs), apply the row to the text as it stands and cite the tip's line in the revision line.

### Acceptance
`git diff` over specs 18 and 19 shows, in each, one header rev change, one new revision line and the table's edits, and nothing else; both still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 21 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 18 and 19. No status change.

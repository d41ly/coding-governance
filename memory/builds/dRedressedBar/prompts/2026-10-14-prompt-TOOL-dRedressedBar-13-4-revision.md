# Revision — dRedressedBar: TOOL-dRedressedBar-13's spec-writer pass, specs 9, 10 and 11 corrected in place

**Serves:** research TOOL-dRedressedBar-13 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11

## The brief

### Goal
Units 10, 11 and 12 are CLOSED (unit 12 at `fda78c56e`). Run spec 13's S25 first half now, as the pass §4 names `<w13>`: apply every row of spec 13 §4's correction table to its target spec, 9, 10 or 11. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-13` and every report id the table assigns that spec. Each is a records fix with its status unchanged: all three stay CLOSED.

### Items
1. **TOOL-dRedressedBar-9, -10 and -11** — the table's rows, exactly as spec 13 §4 states them. Read spec 13 S25, §4's correction-pass paragraph and table, and AC21 first; AC21 reads this commit, so the diff must satisfy it. Where a row's cited line numbers have moved since the spec was written (units 10, 11 and 12 edited `tools/govkit/govkit.py`), cite the tip's lines and say so in the revision line.
2. **A finding to place, not to fold on your own:** unit 10's builder found that spec 10 §5 observability says a refused stop prints `no declared outcome accepts that`, which is true for `update`, while `apply` still prints that no outcome evaluator exists yet. If a row of spec 13's table already covers spec 10 §5 observability, fold the corrected fact into that row's edit. If none does, add nothing and report it, so the main loop can decide.

### Acceptance
`git diff` over specs 9, 10 and 11 shows, in each, one header rev change and one new revision line, plus the table's in-place edits, and nothing else. All three headers still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 13 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 9, 10 and 11. No status change.

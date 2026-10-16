# Revision — dRedressedBar: TOOL-dRedressedBar-19's spec-writer pass, specs 12 and 14 to 18 corrected in place

**Serves:** research TOOL-dRedressedBar-19 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18

## The brief

### Goal
Units 12 to 18 are CLOSED (unit 18 at `997fc294f`). Run spec 19's S44 first half now, as the pass §4 names `<w19>`: apply every row of spec 19 §4's correction table to its target spec, 12, 14, 15, 16, 17 or 18. Each target takes ONE rev bump and one §9 revision line naming `TOOL-dRedressedBar-19` and every report id the table assigns that spec. Each is a records fix with its status unchanged: all six stay CLOSED.

### Items
1. **TOOL-dRedressedBar-12 and -14 to -18** — the table's rows, exactly as spec 19 §4 states them. Read spec 19 S44, §4's correction-pass paragraph and table, and AC44 first; AC44 reads this commit, so the diff must satisfy it.
2. **What moved since spec 19's table was written.** `<w17>` bumped specs 12 to 15 again; unit 17 built its batch; spec 18 took rev-4 (owner F3 (b), the alias resolution, the path conversion moved in from unit 19) and unit 18 built against it in `6783992aa` and `997fc294f`. Where a row's cited lines, criterion numbers or sentences have moved, apply the row's intent to the text as it stands at the tip, cite the tip's lines, and say so in that spec's revision line. Keep every earlier correction true alongside yours. If a row is already true at the tip or its target no longer exists, say so in the revision line and change nothing for it; report each such row.
3. **Spec 19's own build scope, checked against what unit 18 built.** Spec 19 is unbuilt. For each of its S-items and criteria that reads `tools/run-gates/measure_legs.py`, its fixtures, its declarations or the process-monitor census, check it against the tip. Where unit 18 already built it, or built it differently from what spec 19 assumes (spec 19 was audited against spec 18 rev-3), revise spec 19 so its build pass does exactly the remaining work, each change named in a rev-bumped §9 line. Unit 18's builder named two reds spec 19 owns: the new leg's row in `tools/govkit/subject-pins.tsv` (S22) and its `WHOLE_RUN` row (S25); confirm both still hold. Report every spec-19 item you moved.

### Acceptance
`git diff` over specs 12 and 14 to 18 shows, in each, one header rev change and one new revision line, plus the table's in-place edits, and nothing else. All six headers still read CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 19 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 12, 14 to 18 and 19. No status change.

# Revision — dRedressedBar: TOOL-dRedressedBar-14's spec-writer pass, spec 11 corrected in place

**Serves:** research TOOL-dRedressedBar-14 TOOL-dRedressedBar-11

## The brief

### Goal
Unit 11 is CLOSED, and `<w12>` (62f965ccf) and `<w13>` (cdc2912f7) have each bumped spec 11, which now reads rev-5. Run spec 14's S5 now, as the pass §4 "The spec-11 correction's pass" names `<w14>`. Correct spec 11's §4 "Which receipt bytes" paragraph in place, as a records fix with its status unchanged (CLOSED stays CLOSED). Bump its rev by one, and add a §9 revision line naming `TOOL-dRedressedBar-14`. The paragraph states that in `apply` the term reads the receipt this run wrote ahead of CONFIGURE; that receipt holds this run's rows and the carried ones, and it is still the bytes the adopter read. `update` is unchanged.

### Items
1. **TOOL-dRedressedBar-11** — the in-place correction above, exactly as spec 14 S5 states it. Read spec 14 S5, §4 "The spec-11 correction's pass" and AC6 first; AC6 reads this commit, so the diff must satisfy it. Keep what `<w12>` and `<w13>` wrote into the same paragraph true alongside it: reword their sentences only where unit 14's ordering makes them false, and name each such reword in the revision line.

### Acceptance
`git diff` over spec 11 shows only the rev bump, the §4 "Which receipt bytes" edit and the §9 line. The status header still reads CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 14 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 11. No status change.

# Revision — dRedressedBar: TOOL-dRedressedBar-16's spec-writer pass, spec 12 corrected in place

**Serves:** research TOOL-dRedressedBar-16 TOOL-dRedressedBar-12

## The brief

### Goal
Unit 12 is CLOSED at `fda78c56e`. Run spec 16's S4 now, as the pass §4 "The spec-12 correction's pass" names `<w16>`. Correct `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-12.md` in place as a records fix with its status unchanged (CLOSED stays CLOSED). Bump its rev by one, and add a §9 revision line naming report id 7 and TOOL-dRedressedBar-16's AC1 and AC2. Its §3 second non-goal states that the `emitted` carry was taken by `TOOL-dRedressedBar-16`, because the same-argv rule does not reach an argv gov has changed. Its §4 Alternatives row C5 states that its rejection rested on that false premise and that unit 16 takes C5. Spec 12's S2 and criteria are not rewritten.

### Items
1. **TOOL-dRedressedBar-12** — the in-place correction above, exactly as spec 16 S4 states it. Read spec 16 S4, §4 "The spec-12 correction's pass" and AC4 first; AC4 reads this commit, so the diff must satisfy it, including that §3's joined cut no longer carries `so it wedges nothing`.

### Acceptance
`git diff` over spec 12 shows only the rev bump, the §3 non-goal, the C5 row and the §9 line. The status header still reads CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 16 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 12. No status change.

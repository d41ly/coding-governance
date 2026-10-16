# Revision — dRedressedBar: TOOL-dRedressedBar-12's spec-writer pass, spec 11 corrected in place

**Serves:** research TOOL-dRedressedBar-12 TOOL-dRedressedBar-11

## The brief

### Goal
Unit 11 is CLOSED at `b65688cde`. Run spec 12's S4 now, as the pass §4 "The spec-11 correction's pass" names `<w12>`. Correct `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-11.md` in place as a records fix with its status unchanged (CLOSED stays CLOSED). Bump its rev by one, and add a §9 revision line naming report id 23 and TOOL-dRedressedBar-12's AC2. In its §4 "Which receipt bytes", state that a refused apply still writes its receipt and that a later run reads that receipt, which unit 12 keeps whole. In the first "What an adopter sees change" row, the "After" cell says the refusal holds on every re-run. Spec 11's AC3 text does not move.

### Items
1. **TOOL-dRedressedBar-11** — the in-place correction above, exactly as spec 12 S4 states it. Read spec 12 S4, §4 "The spec-11 correction's pass" and AC5 first; AC5 reads this commit, so the diff must satisfy it.

### Acceptance
`git diff` over spec 11 shows only the rev bump, the §4 "Which receipt bytes" sentence, the first "After" cell and the §9 line. The status header still reads CLOSED. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` still grades unit 12 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 11. No status change.

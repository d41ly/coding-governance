# Revision — dRedressedBar: TOOL-dRedressedBar-21's Readers clauses, and spec 13's title under the index line cap

**Serves:** research TOOL-dRedressedBar-21 TOOL-dRedressedBar-13

## The brief

### Goal
The pre-commit hygiene gate refused the commit of specs 21, 22 and 23 on two checks. Check 25: spec 21's S2, S3 and S4 each retire a named thing and carry no `**Readers:**` clause. Check 7: `memory/builds/dRedressedBar/README.md:159` is 457 characters against a 350 cap. That line is the generated build-units row for TOOL-dRedressedBar-13, whose text is spec 13's H1. The cap binds now because adding units 21 to 23 moved the build from CLOSED back to SPECCED; the row did not change.

### Items
1. **TOOL-dRedressedBar-21** — give S2, S3 and S4 each a `**Readers:**` clause in the form check 25 names: `by name:` with the readers that spell the retired name, then `by value:` with the readers of its value, or `NO VALUE READERS` and a reason. Find the readers with grep over the tree; do not guess. No other change; no rev bump is owed for an uncommitted rev-1.
2. **TOOL-dRedressedBar-13** — shorten its H1 so the generated row (`| [<H1>](../spec/2026-10-14-spec-TOOL-dRedressedBar-13.md) | 9 | 2 | CLOSED | rev-N | <date> |`) is at most 350 characters, keeping the id and saying what the unit did. It is a CLOSED spec: a records fix with a rev bump and a §9 line naming this record, status unchanged. Check every other spec in the build the same way and report any row over 350.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --staged` over the staged specs 13 and 21 to 23 and the re-rendered README prints no check 7 or check 25 line.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 13 and 21. No status change. No index regeneration; the main loop runs it.

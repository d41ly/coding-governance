# Fix brief — dFoldedAudit: foreign ids read as claimed

**Serves:** research TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-8

## The brief

### Goal
Stop hygiene check 13 reading another build's ids as claimed by this one. Commit nothing; the main loop commits.

### Items
1. TOOL-dFoldedAudit-8 lines 88, 174 and 208 are headings opening with `TOOL-dDeclaredLoop-32`, `TOOL-dDeclaredLoop-20` and `TOOL-dFairHearing-17`. Reword each so the id does not lead the line, for example `### The revision of `TOOL-dDeclaredLoop-32``, and keep any cross-reference that points at those headings working.
2. TOOL-dFoldedAudit-1 line 158 opens with `TOOL-dDeclaredLoop-20's unbuilt S9`. Reword so the id does not lead the line.

### Acceptance
Each spec carries a rev bump and a §9 line. `check-memory-hygiene.sh --only 13` prints no line naming dFoldedAudit once the main loop has staged it.

### Gates
`tools/check-spec-tokens.py` and check 13, run by the main loop after this pass.

### Non-goals
No other text, no code, no write outside these two specs.

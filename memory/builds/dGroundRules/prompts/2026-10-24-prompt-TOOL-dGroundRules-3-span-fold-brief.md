**Serves:** research TOOL-dGroundRules-3

# Fold brief — criterion code spans rejoined onto one line

## The prompt

> Hygiene check 23 failed on TOOL-dGroundRules-3/AC3: its criterion wraps the code span `policy.py get budgets.enforce --explain` across two lines, and check 23 tokenizes each criterion line on its own (`tools/memory-tree/check-memory-hygiene.sh`, the `altoks(line)` calls in the acceptance-ledger reader), so the wrapped span pairs the wrong backticks and the criterion's tokens become prose fragments no ledger answer can share.

## The brief

### Goal
In each spec named below, rejoin every inline code span that §6 Acceptance criteria wraps across a line break, so each span opens and closes on one line, with no change of meaning. Author only: no product code, no commit, no gate.

### Items
1. The specs, each under `memory/builds/dGroundRules/spec/`, and the §6 lines found with an odd backtick count outside a fence: `TOOL-dGroundRules-2` (AC8), `-3` (AC3, and the AC6 list literal), `-4` (AC4, the `get budgets.enforce` span near AC8, AC9), `-6` (the `admitted on the terminal proof` span), `-10` (AC12, AC14), `-20` (AC1), `-23` (AC3), `-25` (the `not graded` span near line 443), `-32` (AC11), `-34` (AC8), `-52` (the `%TEMP%` span near line 277). Re-scan each spec's §6 yourself; fix any other wrapped span you find there, and leave fenced blocks alone.
2. Reflow by moving the line break before the span's opening backtick or after its closing one; never split a span, change a token's bytes, or reword a criterion.
3. Each spec's status header rev rises by one, with a §9 line: a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change. The status cell stays as it is (CLOSED stays CLOSED, DEFERRED stays DEFERRED).

### Acceptance
`python tools/check-spec-tokens.py` exits 0; in each named spec, every §6 line outside a fence carries an even number of backticks; a word diff of each spec shows only whitespace moved inside §6, plus the header and the §9 line.

### Gates
No gate runs in this pass; the main loop runs check 23 after the commit.

### Non-goals
Any other spec section; any other spec; product code; a fix to check 23 itself.

### Limitations
Two units, 2 and 3, are CLOSED: their specs change only in line breaks, so their design is untouched.

### Reuse
The odd-backtick scan: an awk pass over each spec's `## 6.` section counting backticks per line.

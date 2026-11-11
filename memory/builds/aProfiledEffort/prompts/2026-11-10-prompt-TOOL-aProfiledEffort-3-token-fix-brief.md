# Brief — aProfiledEffort: unit 3's AC3 spells two paths the token check cannot resolve

**Serves:** research TOOL-aProfiledEffort-3

## The brief

### Goal
`python tools/check-spec-tokens.py` reports two unwaived hits on `memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-3.md`: AC3 of its §6 carries one backticked `diff <(…) <(…)` command, and the checker reads `memory/guides/UNATTENDED-VERBS.md)` and `tools/unattended/VERBS.template.md)`, each with the closing parenthesis, as paths git does not track. The line is respelled so each path stands alone in its own backticks and the criterion observes the same thing.

### Items
1. AC3's second clause reads: and a `diff` of `memory/guides/UNATTENDED-VERBS.md` against `tools/unattended/VERBS.template.md`, each read through `tr -d '\r'`, prints nothing.
2. The spec takes a rev bump to rev-2 and a §9 line naming this record and the two hits.

### Acceptance
1. `python tools/check-spec-tokens.py` prints `0 unwaived hit(s)` and exits 0.
2. AC3 still opens with its backticked token before its first wrap, and no other criterion moved.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any other line of the spec, any sibling spec, any code. A change to what AC3 observes.

### Limitations
Records only. No gate, suite or bar runs in the pass beyond the token check. The main loop commits.

### Reuse
The fix is the same respelling `TOOL-dFairHearing-1`'s token-fix brief ordered: a path inside a compound backticked command is split out into backticks of its own.

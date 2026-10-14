# Revision — dRedressedBar: TOOL-dRedressedBar-17, AC24's red half re-read over the built `<p15>`

**Serves:** research TOOL-dRedressedBar-17

## The brief

### Goal
The `<w17>` writer found that spec 17's AC24 red half cannot reproduce over the built `<p15>`. Unit 15's selfcheck already triggers on the `via` key's presence (`tools/govkit/govkit.py:3296` at `7da62c241`) and checks the value is a string that names a registry entry before using it. So over `<p15>`, both `via = ""` and `via = ["other"]` print one `govkit: entry 'demo' declares [adopt] via` line ending `names no registry entry`, with no traceback. AC24's "Red when" expects no line for `via = ""` and a `Traceback` with `unhashable` for `via = ["other"]`, and the `New arm:` line covering AC11 and AC24 states the same. Both are false against the built code. The other red half, `resolve_adopter_argv` falling back to the entry's own argv instead of raising `KeyError` for `via = ""`, should still hold; confirm it by reading `resolve_adopter_argv` at the tip.

### Items
1. **TOOL-dRedressedBar-17** — bump the rev. Restate S24 against `<p15>`: the selfcheck half is a reason refinement (a value that is not a non-empty string now reads `is not a non-empty string`, not `names no registry entry`), and the `scan_entry_argv`/`resolve_adopter_argv` half is the behaviour change. Rewrite AC24's "Red when" to what `<p15>` actually prints for each value: the `names no registry entry` reason in place of `is not a non-empty string`, and the fallback in place of `KeyError`. Rewrite the `New arm:` line covering AC11 and AC24 the same way. Keep AC24's green half. Check the §1 table row for id 24 and §4's sentence at the "S24 turns a silent fallback into a" paragraph against the built code and correct whatever is false. Name the finding in the §9 line.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 17 READY. AC24's "Red when" and its `New arm:` line name only outputs `<p15>` produces, each confirmed by reading the code at the tip.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 17. No status change.

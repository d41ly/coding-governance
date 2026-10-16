# Revision — dRedressedBar: TOOL-dRedressedBar-5, the builder's divergence on AC3's count

**Serves:** research TOOL-dRedressedBar-5

## The brief

### Goal
DIVERGENCE: §6 AC3 (its second half) contradicts §2 S5 and §4 "The suites", so a build that does exactly what S5 and §4 say would fail AC3. AC3 says that across the pass, `grep -o '\$(printf ' tools/workflows/unattended-build.test.sh | wc -l` falls by exactly five (288 to 283). But all eight `var-pipe` candidates §4 pins (`:1902`, `:1904`, `:1909`, `:2698`, `:2711`, `:2757`, `:2768`, `:2771`) are written as `$(printf '%s' "$X" | sed 's#"slug":"tB",#…#')`. Each one carries a `$(printf ` occurrence, and the forms-table row `w=${v/'A'/'B'}` removes it. I counted these with grep over those lines: 8 occurrences, and 6 more on the six `printf-subst` candidate lines. So the fall would be 5 + 8 = 13, from 288 to 275. Picking different sites does not help: only two `var-pipe` sites in the file sit outside a `$(printf ` (`:1582` and `:1999`), so dropping `var-pipe` by eight always takes at least six `$(printf ` occurrences with it. To be consistent, AC3 would have to say one of two things. Either the `grep -o '\$(printf '` count falls by exactly thirteen (five `printf-subst` sites plus the eight `sed` sites, 288 to 275). Or the count is limited to `$(printf ` substitutions with no `|` inside them, which falls by exactly five. Its "Red when" and figure lines would change to match. The first half of AC3 holds as written (exactly five `-` lines spell a pipe-free `$(printf `, and their `+` lines spell `printf -v _wfj`). Nothing else I read diverged: the start-of-unit `git diff ebce889c` over the five files moves no site, and the AC1 and AC2 baselines match the pinned figures.

### Items
1. **TOOL-dRedressedBar-5** — bump the rev and make AC3 consistent with S5 and §4. Pick whichever of the two forms the goal names discriminates better: one that fails if a `printf-subst` site is left unconverted, and fails if a `var-pipe` conversion leaves its `$(printf `. Change its "Red when" and figure lines to match. Nothing else in the spec moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-5 READY, and AC3's arithmetic matches the eight `var-pipe` and five `printf-subst` sites §4 pins.

### Gates
`shell hygiene (a fork spent on builtin work)` · `memory hygiene`

### Non-goals
- No code.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix.
- No merge to local main and no push without the owner's ask.

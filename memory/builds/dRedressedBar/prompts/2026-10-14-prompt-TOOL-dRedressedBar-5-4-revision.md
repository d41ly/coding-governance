# Revision — dRedressedBar: TOOL-dRedressedBar-5, the builder's second divergence (CR in a substitution, the one-line loop)

**Serves:** research TOOL-dRedressedBar-5

## The brief

### Goal
DIVERGENCE: two statements in spec rev-3 are wrong about the code. Building either site as the spec describes it would turn a §7 gate red at the close. Fixing either one means choosing a placement the spec does not give.

(1) §4 "The suites", `tools/roles/adopt-roles.test.sh` `:160` and `:245` (ebce889c numbering), and the forms-table `tr -d '\r'` row. Both sites sit inside the `"$( … )"` argument of `check_arm`. On the bash the bar runs (Git Bash 5.3.9, MSYS), a `$'\r'` written inside a command substitution loses its CR, so `${out//$'\r'/}` there strips nothing. Probe: `out=$'a\r'; [ "${out//$'\r'/}" = a ]` passes at top level, but `echo "$([ "${out//$'\r'/}" = a ] && echo ok || echo FAIL)"` prints FAIL. The same happens with `[[ ]]` and with a bare `$( )`. A CR held in a variable set at top level works, and `$'\n'` inside `$( )` also works. `handoff.py` stdout carries CR on Windows (52 CR bytes in one `roster` run), so arms 6 and 9 would fail wrongly. The assertion probe, run against the HEAD spellings, flipped both arms' passing specimens from 1 to 0.

What the spec would have to say: where the strip goes. Either at top level on the capture lines, as `out=$(…); rc=$?; out=${out//$'\r'/}` at ebce `:158` and `:243` (`out` is not read again in either arm before arm 7 reassigns it), or through a CR variable set at top level, which needs a new §4 Inventory row such as `_cr`. The row's `exact only when` cell would have to exclude a command substitution under MSYS bash, and AC4 would need a specimen run inside `$( )`.

(2) §4, the paragraph under the forms table ("It is not a `while read` loop, so the loop leg does not grade it") and §7's note that the loop leg "grades the `mapfile` form". Both are false for the row written on one line at `:183`. `scan_file` (`tools/gate-lint/sh_hygiene.py:314-322`) treats a line as a loop when `done` appears anywhere on it. It then grades a `<<<` whose tail names a variable last assigned from a command substitution as `loop-var-sub`, a gated class. `out` is assigned at `:182` by `out=$(cd "$FX" && …)`, and the file has no row in `memory/project/substitution-fed-loops.txt`, so `shell hygiene (a loop fed by a command substitution)` would go red. Probe: `scan_file` on the one-line spelling returns `{'loop-var-sub': [(2, '<<<')]}`. With `mapfile -t _l8 <<< "$out"` moved to the end of the `:182` capture line and the `for` loop left on `:183`, it returns nothing.

What the spec would have to say: that placement, or another, with the paragraph and §7 corrected.

### Items
1. **TOOL-dRedressedBar-5** — bump the rev, and correct both findings with the placements the builder measured, or better ones with their own probe:
   - (1) the CR strip at top level on the capture lines, or a top-level CR variable with its Inventory row, its `exact only when` cell excluding a command substitution under MSYS bash, and an AC4 specimen run inside `$( )`;
   - (2) the `mapfile` moved onto the capture line, with §4's paragraph and §7's note corrected to what `scan_file` actually grades.
   Nothing else in the spec moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-5 READY. No sentence in the spec says a `$'\r'` inside a command substitution strips a CR, or that a one-line `… done` row escapes the loop leg.

### Gates
`shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `roles adopter self-test` · `memory hygiene`

### Non-goals
- No code.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix.
- No merge to local main and no push without the owner's ask.

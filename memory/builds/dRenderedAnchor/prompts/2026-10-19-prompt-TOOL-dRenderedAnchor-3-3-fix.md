# Fix — dRenderedAnchor: the closing bar's one own red, the suites' unregistered forks

**Serves:** research TOOL-dRenderedAnchor-3

## The brief

### Goal
The closing bar at `b4b79004d` (`GATE_FULL=1 GATE_SELFTESTS=1`) read 6/142 legs red. Five were attributed by re-running each leg standalone, four as INHERITED at the base `a60b0c7dc` and pre-push as contended, green alone at the tip. The one OWN red is `shell hygiene (a fork spent on builtin work)`, green at the base: `tools/lib/resolve-python.test.sh: the registry declares 8 site(s) at var-pipe and the scan measures 11`, and `tools/roles/adopt-roles.test.sh: 8 var-pipe site(s) and no registry row declares them`. Every one of those sites is an assertion line this build added (sections 2e and 2f, arms 14 to 17). Convert each to the no-fork form so the leg reads green with `memory/project/spawn-idiom-sites.txt` unchanged.

### Items
1. In `tools/lib/resolve-python.test.sh`, the three `var-pipe` sites this build added (the row-count `grep -c .` and the two `tr '\n' ' '` message expansions in section 2e, and the `| tr -d '\r'` capture in section 2f, whichever three the lint counts) take the no-fork form: a parameter expansion, `[[ =~ ]]`, or a `while read` count, so the scan reads 8 again.
2. In `tools/roles/adopt-roles.test.sh`, the eight `var-pipe` sites in arms 14 to 17 take the no-fork form, so the file needs no registry row.
3. No assertion changes meaning: each converted line asserts what it asserted, and each arm still reads RED on the staged break its `New arm:` line names.

### Acceptance
`python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` exits 0 at the fix commit, with `memory/project/spawn-idiom-sites.txt` byte-identical to `a60b0c7dc`. The main loop then re-observes `adopt-roles.test.sh` `PASS (62 assertions)`, `resolve-python.test.sh` green, and arms 14 to 17 and sections 2e and 2f RED on their staged breaks.

### Gates
shell hygiene (a fork spent on builtin work) · roles adopter self-test · python resolver (behaviour + inline parity + idiom ban); then the full bar once more.

### Non-goals
Any product-code change; any registry row added or raised; the four inherited reds and the contended pre-push red.

### Limitations
A unit pass runs no gate leg; verify with a scratch copy of the lint's spawn-idiom classifier over the two files, or a probe of the lines. Merge and push wait for the owner's explicit ask.

### Reuse
`tools/gate-lint/sh_hygiene.py`'s message names the no-fork forms: `${p##*/}`, `${p%/*}`, `printf -v`, a parameter expansion or `[[ =~ ]]`.

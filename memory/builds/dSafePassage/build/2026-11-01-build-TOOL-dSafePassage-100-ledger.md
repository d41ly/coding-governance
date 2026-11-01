**Serves:** journal TOOL-dSafePassage-100

# TOOL-dSafePassage-100 — acceptance ledger

The unit as built, at spec rev-2. Product write: `tools/push-main.test.sh` only. S1: `measure37`
calls `"$_py_arms" -c '` with no default. S2: the derived-count block's guard reads
`if [ -n "$_mt_rc" ] && [ -n "$_py_arms" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then`, and the
TOOL-dSafePassage-46 S2 comment above it gains one TOOL-dSafePassage-100 sentence, which spells no
parameter default. S3: the `else` skip names the launcher and ends `is NOT covered`. The lines the
spec cites at `f519c1934` were where it says at this pass's parent `3909ba68e`; the added comment
line moves the guard to 1424 and the skip to 1446.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every probe ran on node a
(Windows 11) from this worktree's root, in Git Bash. AC4's fixture is a scratch bash under the run's
scratchpad that evals, cut from the suite file it is given: the resolver block, the `_mt_rc` scan,
the `PREPARE_REFUSALS` array, `ok` and `bad` as the suite spells them, then arm 37's lines from
`measure37()` to the `fi` closing the derived-count block, with `HERE` at the tools directory and a
scratch `tmp`.

Owed at the close: the RED-first observation of §7's `New arm:` line, and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-100
- AC1 — `git grep -nF -e ':-python3}' -- '*.sh'` printed nothing and exited 1; `bare_scan`, cut from `tools/lib/resolve-python.test.sh` and run over the lander suite, printed nothing. Red: `bare_scan` over the suite at `3909ba68e` printed `1409:  "${_py_arms:-python3}" -c '`.
- AC2 — `git grep -nF -e 'if [ -n "$_mt_rc" ] && [ -n "$_py_arms" ]' -- '*.sh'` printed exactly one line, `tools/push-main.test.sh:1424`, the derived-count block's guard.
- AC3 — `git grep -nF -e 'or python launcher beside this lander, so the derived-count arm is NOT covered' -- '*.sh'` printed exactly one line, `tools/push-main.test.sh:1446`, the skip echo in that guard's `else` branch.
- AC4 — the scratch fixture with `_py_arms=""` printed only `skip — 37 no memory-tree kit (check-arms.py) or python launcher beside this lander, so the derived-count arm is NOT covered`; with `_py_arms` set by `resolve_python` it printed `ok   — 37 cmd_prepare refuses 6 way(s) after the gov-first walk, and PREPARE_REFUSALS carries a row for each` and `ok   — 37 a commented and a quoted return 1, and run_gov_first named above the call, leave the count at 6`; 6 equals the row count of `PREPARE_REFUSALS`. Red: on a scratch copy whose guard lacks `[ -n "$_py_arms" ]`, the empty run printed two `FAIL — 37` lines, `cmd_prepare refuses 0 way(s)` and `0, not 0`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by the main loop at `2c459254d`, arm 37 cut from the suite by the pass's AC4 fixture (the resolver block, the `_mt_rc` scan, `PREPARE_REFUSALS`, `ok`/`bad` and arm 37). RED, a copy whose line-1424 guard drops `[ -n "$_py_arms" ]`, with `_py_arms` empty: `FAIL — 37 cmd_prepare refuses 0 way(s) after the gov-first walk (0 means the anchor matched nothing), PREPARE_REFUSALS carries 6 row(s)` and `FAIL — 37 the derived count moved on a lander copy ...: 0, not 0`. GREEN, the suite as committed: with `_py_arms` empty, only `skip — 37 no memory-tree kit (check-arms.py) or python launcher beside this lander, so the derived-count arm is NOT covered`; with the resolved launcher, `ok   — 37 cmd_prepare refuses 6 way(s) after the gov-first walk, and PREPARE_REFUSALS carries a row for each` and `ok   — 37 a commented and a quoted return 1, and run_gov_first named above the call, leave the count at 6`.

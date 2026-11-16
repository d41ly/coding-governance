# Brief — aMeasuredDrag: the close bar's shell-hygiene red in unit 12's arms

**Serves:** research TOOL-aMeasuredDrag-12

## The prompt

> Build quick wins

The close's merge bar at `f3a0c830` redded the leg `shell hygiene (a fork spent on builtin work)`.
The scan counts four sites more than its registry declares, and this unit's arms added all four.
Unit 12 is reopened at INPROGRESS for this fix, which rides the inline red-fix lane.

## The brief

### Goal
Rewrite the four fork idioms that unit 12's arms added in their no-fork forms, so the spawn-idiom
scan is back at or under its registry, with no arm's verdict moved.

### Items
1. `.githooks/pre-commit.test.sh`, `var-pipe` (registry 6, scan 7). The site is arm S11's `n_runs=`
   line, which pipes `"$out"` into `grep -c 'TEMPLATE-SIZE RAN'`. Count matching lines instead with
   a `while IFS= read -r` loop over a here-string, testing each line with a `[[ == *…* ]]` match.
2. `tools/run-gates/run-gates.test.sh`, `printf-subst` (registry 2, scan 3). The site is the
   `exec $(printf '%q' "$_mexe")` line that writes arm 1m's stub `$_md/py`. Use
   `printf -v _mq '%q' "$_mexe"` on its own line first, then `exec $_mq …` inside the stub.
3. `tools/run-gates/run-gates.test.sh`, `path-subst` (registry 12, scan 13). The site is the
   `d=$(cd "$(dirname "$0")" && pwd)` text the arm writes to `$_md/leg.sh`. Use `${0%/*}` in place
   of `$(dirname "$0")`. The leg runs as `bash <dir>/leg.sh`, so `$0` always holds a slash.
4. `tools/run-gates/run-gates.test.sh`, `cat-file` (registry 25, scan 27). The sites are arm 1m's
   `_mmemo=` and `_mlaunch=` lines. Use `if [ -f F ]; then v=$(<F); else v=<fallback>; fi`, with
   the fallbacks unchanged: `"NO LEG RAN"` for the memo and `""` for the launcher.

### Acceptance
- Each rewritten expression gives the old one's value. Check this with a `bash -c` probe over
  scratch values:
  - the count, for 0, 1 and 2 matching lines;
  - a missing file, which must give the fallback;
  - a present file, which must give its bytes.
- The leg's own command,
  `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`,
  exits 0 and prints no "the scan measures" finding. It is a lint, not a suite.

### Gates
The leg `shell hygiene (a fork spent on builtin work)`, re-run by the main loop's close bar.

### Non-goals
Any other line of either file, the site registry, any spec or record. The main loop writes the
red-fix record and closes the unit again.

### Limitations
- One commit, touching exactly the two files.
- The subject names `TOOL-aMeasuredDrag-12` and says `red-fix`.
- Trailers: `Red-fix: shell hygiene (a fork spent on builtin work)`, `Pass: none`, and the charter's
  `Co-Authored-By` line.
- Author the edits with the edit tools, never a heredoc.

### Reuse
None needed: each item's no-fork form is the one the leg's own message names.

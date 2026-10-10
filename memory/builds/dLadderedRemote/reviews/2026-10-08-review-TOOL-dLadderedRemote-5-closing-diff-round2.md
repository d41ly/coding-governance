**Serves:** diff-review TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-5

# Tier-2 closing diff review — dLadderedRemote, ROUND 2

One reviewer agent, run directly on 2026-10-08 on node `d`. It was READ-ONLY and primed with the
round-1 brief, the round-1 record and unit 5's spec. It read only the fold, from round 1's recorded
tip. Every finding carried a reproduction from a scratch repo, and the main loop re-read each one
against the code before promoting it.

**Reviewed range:** `75a55242c...be3ac3844`. The later commit `185da1d44` renames test helpers and a
fixture remote and was not in scope; round 3 reads it. **ROUND: 2.**

## Verdict: CLEAN WITH FIXES

All nineteen round-1 items are CLOSED. No BLOCKER or HIGH. Seven new items, which is strictly fewer
than round 1's nineteen. One is MEDIUM, a regression in the widened ban that unit 5 introduced; the
other six are LOW. All seven are promoted into one batch unit, `TOOL-dLadderedRemote-6`.

## Findings

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| N1 | MEDIUM | `tools/check-remote-literals.sh` default shape | A `${...}` default whose parameter does not start with a letter escapes, so `${1:-origin}`, `"${2:-origin}"` and `${opts[remote]:-origin}` pass. All three were caught at round 1's tip. | unit 6 |
| N2 | LOW | the assignment shape | The unquoted form reds a Python or JS VARIABLE named like the remote, such as `self.origin = origin`; `tools/runlog/extract.py` holds such variables. | unit 6 |
| N3 | LOW | the remedy and last-argument shapes | Flags between the verb and the name (`git fetch --quiet origin`) and list-form argv (`["git", "fetch", "origin"]`) escape, and the header does not say so. | unit 6 |
| N4 | LOW | the ban's self-test | `remote.<name>.`, `pull`, `${x-name}` and `${x=name}` have no arm of their own. | unit 6 |
| N5 | LOW | `tools/codebase-map/selftest.py` | A failing assert leaves `GOV_DEFAULT_BRANCH` set for every later test in the process. | unit 6 |
| N6 | LOW | `WIRE-INTO-PROJECT.md` | It says every kit reads `GOV_DEFAULT_BRANCH` first, but three readers take the observed branch only. It also says the ladder is "below" when it is above. | unit 6 |
| N7 | LOW | `.githooks/pre-commit` | The ladder refusal prints on every commit in the primary tree, including when `GOV_DEFAULT_BRANCH` already decides. The guard's own `symbolic-ref --short HEAD` is item 7's class one line away. | unit 6 |

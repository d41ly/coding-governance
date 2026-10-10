**Serves:** diff-review TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6

# Tier-2 closing diff review — dLadderedRemote, ROUND 3

One reviewer agent, run directly on 2026-10-08, node `d`. It was READ-ONLY and primed with the
round-1 brief, the round-2 record and unit 6's spec. Its probes ran on copies of the HEAD files in a
scratch directory while a full bar ran in the repository untouched.

**Reviewed range:** `be3ac3844...d9c349d95`, which holds the helper and fixture-remote renames
(`185da1d44`) and unit 6. **ROUND: 3.**

## Verdict: CLEAN WITH FIXES

All seven round-2 items are CLOSED. No BLOCKER, HIGH or MEDIUM. Five new LOW items, strictly fewer
than round 2's seven, are promoted into one batch unit, `TOOL-dLadderedRemote-7`.

## Findings

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| F1 | LOW | `tools/check-remote-literals.test.sh` | No GREEN row can tell the shell-only assignment pass from one run over every file, since both rows have spaces around `=`. A mutant running it everywhere stays green. | unit 7 |
| F2 | LOW | `tools/check-remote-literals.sh` remedy shape | A flag taking a separate value (`--depth 1`, `-o x`) hides the name, yet the header claims "any flags". | unit 7 |
| F3 | LOW | the `${...}` default and last-argument shapes | `${a.kind===origin ? ...}` in JS and `["kit", "origin"]` in Python are named, which is the variable-or-key class again. | unit 7 |
| F4 | LOW | `WIRE-INTO-PROJECT.md` | The observed-only list reads as complete, but migrate-backlog and the straggler guard also take the observed branch and only cross-check the pin. | unit 7 |
| F5 | LOW | the ban's merge step and `.githooks/pre-commit` | `sort -u -t: -k1,1 -k2,2n` collapses hits from paths containing a colon, and one comment in the guard says the refusal is never swallowed. | unit 7 |

## Nothing found

Renames missed no call site. No shipped path contains the adopter's name. Every fixture expectation
moved with the fixture remote's rename. The root-install derivation works for both passes.

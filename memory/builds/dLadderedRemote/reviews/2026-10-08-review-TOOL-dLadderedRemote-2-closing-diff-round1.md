**Serves:** diff-review TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4

# Tier-2 closing diff review — dLadderedRemote, ROUND 1

Three finder lenses run as direct agents on 2026-10-08, node `d`, each READ-ONLY, primed with one
brief covering the diff, the security model and the by-design list. The lenses were consumer-site
correctness, the ladder and ban contract, and the shipped surface adopters receive. There was no
separate skeptic agent. Every finding carried a reproduction its lens ran in a temp repo, and the
main loop re-ran the two HIGHs before folding them: the pre-commit pin by a staged break that reds
its new arm, and the evidence fixtures by reading both helpers against the runner's ladder.

**Reviewed range:** `40a8b8c32ad1e7f30f36c7be6e71d9a0a67d142a...75a55242c` (six commits). **ROUND: 1.**

## Verdict: CLEAN WITH FIXES

Two HIGH findings, both fixed in the round-1 fold. Every MEDIUM and LOW is promoted into one batch
unit, `TOOL-dLadderedRemote-5`, as M4 of the build method disposes them.

## Review shape

- Raw 22 across three lenses. After merging duplicates, 19 items: 2 HIGH, 4 MEDIUM, 13 LOW.
- Precision is not measured, because no skeptic refuted anything. Every item was reproduced, and
  none is a style judgement.

## Findings

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| 1 | HIGH | `.githooks/pre-commit` branch guard | A ladder refusal returned before `RR_BRANCH` was set, so `GOV_DEFAULT_BRANCH` was dropped and the refusal swallowed; a two-remote primary tree on a non-`main` default could not commit. Found by two lenses. | fixed in the fold, with three arms |
| 2 | HIGH | `tools/run-gates/run-gates.evidence.test.sh` `rec_repo`, `ru_repo` | Fixtures wrote remote-tracking refs with no configured remote, so the runner had no base and the skip control reds. | fixed in the fold |
| 3 | MEDIUM | `tools/check-remote-literals.sh` comment filter | A `*`-led line is a comment only in JS; shell `case` arms such as `*)` were skipped. | unit 5 |
| 4 | MEDIUM | the ban predicate | `${x#origin/}`, `removeprefix("origin/")`, `origin/<other branch>` escaped shape 2. | unit 5 |
| 5 | MEDIUM | the ban predicate | `.get(k, "origin")`, `??`, `${x-origin}`, `${x:=origin}`, an unquoted assignment, and `push`/`pull`/`remote.origin.` escaped. | unit 5 |
| 6 | MEDIUM | `tools/drift-audit/README.md` | The shipped ladder section still names only `origin` and its remedies. | unit 5 |
| 7 | LOW | both canonicals | `symbolic-ref --short` returns `heads/x` or `remotes/r/x` when a tag or branch shares the name, so the ladder misreads the upstream or the observed branch. Found by two lenses. | unit 5 |
| 8 | LOW | `tools/lib/resolve-remote.sh` | A `GOV_REMOTE` holding a newline matches through `grep -F` in shell and refuses in Python. | unit 5 |
| 9 | LOW | the truth table | The detached-HEAD refusal and the `branch.<b>.remote` refusal text are graded on neither canonical. | unit 5 |
| 10 | LOW | the ban population | `*selftest*` and `*test_*.py` exclude product code; `skills/*.js` is promised and absent; no arm under `skills/`. | unit 5 |
| 11 | LOW | the ban predicate | A variable named `origin` reds shapes 2 and 4. | unit 5 |
| 12 | LOW | `tools/gate-legs.json` | The python-resolver leg is not guarded on `.githooks/`, though two inline copies live there. | unit 5 |
| 13 | LOW | `tools/unattended/unattended.sh` `derive_liveness` | A refusal fell back to the local branch, which the site table allows only for three readers. | unit 5 |
| 14 | LOW | `run-gates.sh`, `map_lib.py` | `GOV_DEFAULT_BRANCH` newly SELECTED the base; it had never been consulted there. | unit 5 |
| 15 | LOW | `tools/runlog/model.py` | The ladder's git calls are not counted in `GIT_CALLS`. | unit 5 |
| 16 | LOW | `run-gates.sh` `base_from` | A refusal reads `no-remote`. | unit 5 |
| 17 | LOW | `govkit.py` `resolve_measurer_currency` | A `GOV_REMOTE` exported for an adopter is read against the gov checkout. | unit 5 |
| 18 | LOW | `WIRE-INTO-PROJECT.md`, `skills/session-kickoff/SKILL.md`, `tools/codebase-map/test_codebase_map*.py`, `INVENTORY-DERIVATION.md`, `tools/run-gates/README.md` | Stale origin-only prose. `GOV_REMOTE` is documented nowhere. | unit 5 |
| 19 | LOW | spec 3 | It says the `product` chunk where the leg landed in `declarations`, and the budget row's derivation text does not produce its figure. | unit 5 |

## Nothing found

Govkit's merged-block splice carries the inlined block inside the branch-guard region cleanly. No
caller of the review harness omits `base`. No reader parses `base_from`, drift's header or the
runlog key. No `RR_*` or `_rr_` name collides with an existing one. The block is safe under `set -u`.
All fifteen inline copies sit at column 0, inside the parity population.

**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "adopters": what gov costs incms and nicocares

Adopter repos are READ-ONLY: `C:/projects/incms/main`, `C:/projects/nicocares/main` (its git dir is incms's submodule dir `.git/modules/vendor/nicocares-package`). Bar timings come from the only surviving ledger rows (2026-10-09, 2026-10-20).

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`, in gov or in either adopter; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off (two ledger samples only), does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether gov main already fixed it and only the adopter lags, and say so.
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the gov commit the adopter lacks", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## adopters-1 — updates are so large that adopters stop taking them, and keep paying for slowness gov already fixed
Kits mostly at gov c83ef509 (2026-10-07); `.governance/install.json` gov_commit 1faef37c (2026-10-20); unattended 1.89 vs gov 1.123, run-gates 1.31 vs 1.47. `tools/govkit/govkit.py@37f075e4:9521` `cmd_update`; 18 `[[regenerate]]` blocks over 14 kit.toml. Since c83ef509: 807 kit commits, +147k lines. Last full update: incms 77 commits / 110k lines over 8 days; nicocares 75 / 106k. `WIRE-INTO-PROJECT.md:950` lists push-boundary savings that arrive only by update.

## adopters-2 — the adopter bar runs gov's own hook and lander self-tests
Adopter `scripts/run-gates/gate-legs.json` marks pre-push self-test, push-main self-test, pre-push bar self-test as subject=repo, no chunk; gov marks them subject=kit chunk=selftests. Hold rule incms `scripts/run-gates/run-gates.sh (lines 2087)`; guards ignored under GATE_FULL (`:299`). `.githooks/pre-push` byte-identical to gov. Ledgers: incms 5070 s (10-09), 1003 s (10-20); nicocares 1374 s. `WIRE-INTO-PROJECT.md:936-937` says these test gov files adopters never edit. PINNED 2026-11-15

## adopters-3 — the 10-commit lag bound forces a full bar on about half of adopter landings
Adopter `.githooks/pre-push:1068` `GATE_FULL_MAX_LAG=10`, `:1195` forces GATE_FULL. Median landing: incms 11 commits (22 of 43 exceed 10), nicocares 12 (59 of 118). Gov now counts first-parent landings. PINNED 2026-11-15

## adopters-4 — gov's record legs have no guard, run on every adopter push, and sat on the incms critical path until the ceiling killed them
Unattended kit gate, pass-order, brief-recorded, memory hygiene, marker contracts, drift-audit, playbook validity: no guard. incms runs them as one serial leg `gov-bar` (`scripts/gate-legs.json (lines 173-182)`, ceiling 5400; `scripts/gov-bar.sh`). incms `.git/gate-last-summary.txt` 2026-10-09: gov-bar FAIL (ceiling) after 5408 s; product legs ~2570 s; bar ~8568 s. PINNED 2026-11-15

## adopters-5 — more than half of adopter commits are governance-only
Since 2026-10-01: incms 1533 commits, 814 (53%) governance-only, 259 (17%) product-only; nicocares 1509, 897 (59%) governance-only, 146 (10%) product-only. memory/ holds 5051 of 8761 tracked files (incms), 3195 of 4632 (nicocares). PINNED 2026-11-15

## adopters-6 — every adopter records commit pays 12-16 s in pre-commit plus a whole build-index render
`.githooks/pre-commit:84-95`; adopter `scripts/check-memory-hygiene.sh (lines 1076-1078)`. Hygiene `--staged` with nothing staged: incms 16.0 s, nicocares 12.6 s; `gen_build_index.py --check` 11.6 s / 4.8 s. ~196 / 207 memory commits a week. Claimed 90 / 60 min/week.

## adopters-7 — naming and record-format reds surface only at the close bar; the lexicon guard skips the product code it grades
No pre-commit lexicon / `--check-format` / citation check. Emitted lexicon leg guarded on `scripts/`, `.githooks/`, `.claude/`, `.lexicon.conf` while `tools/lexicon/lexicon.py@8de47e40:411` walks `git ls-files` and `.lexicon.conf:25` grades py/ts/js. Commit subjects: lexicon/rename 47 (incms) / 37 (nicocares); red/reds 59 / 68.

## adopters-8 — kickoff-manifest re-stamp commits recur in nicocares
`scripts/manifest-check.sh (lines 1140-1158)` (fail 5); watch list `.claude/SESSION-KICKOFF.md:7` includes the files merges and updates move. 25 re-stamp commits in nicocares since 2026-10-01.

## adopters-9 — adopter sessions load a 52 KB v3.x charter plus a 25-39 KB CLAUDE.md PINNED 2026-11-15
incms AGENTS.md 52,724 B + CLAUDE.md 25,445 B; nicocares 52,122 + 38,911; gov template now 8,970 B. ~20-23k tokens per agent start. PINNED 2026-11-15

## adopters-10 — install-integrity checks run on every push though their subjects move only on a govkit update
~18 unguarded legs (`adopt-*.sh --check`, receipt sync, kit version markers, verdict epoch, render wiring, kit/dogfood parity, review-protocol parity). incms 74-300 s, nicocares ~371 s per bar. PINNED 2026-11-15

## adopters-11 — every Bash call spawns three node hooks (duplicates sessionhooks-3/-6 for adopters)
scratch-guard 345 ms, gate-guard 234 ms per call (incms, 5-run mean, baseline 0.677 s/10).

## adopters-12 — memory-only incms landings pay the whole product bar because GATE_DOC_PATHS is not declared
incms `.githooks/gate-env.sh` lacks `GATE_DOC_PATHS` (nicocares declares `memory/`); 5 of 43 incms landings were memory-only; product legs ~2570 s. PINNED 2026-11-15

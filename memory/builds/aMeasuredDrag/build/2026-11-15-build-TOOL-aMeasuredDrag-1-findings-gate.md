**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "gate": git hooks and expensive legs

Base `aebbb4a72`. Each item is a researcher's claim. Spawn baselines during the find phase: 33-65 ms per 10 `/usr/bin/true`, quiet node.

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` at base `aebbb4a72` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off, does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether it is already fixed on main (`git log -S`, grep) or on `branch/speedups-9c2e63` (build aTrimmedWait), or already filed as an ask (`grep -r` over `memory/builds/*/BACKLOG.md`).
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost. Several findings overlap across lenses; say which ids describe the same mechanism.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the commit/branch/ask", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## githooks-1 — a one-file records commit re-renders the whole build index in pre-commit
`.githooks/pre-commit:228-230` runs `check-memory-hygiene.sh --staged` on any staged memory path; check 9 calls `gen_build_index.py --check --staged` (`check-memory-hygiene.sh:1494-1497`). The skip `check_staged_render` (`gen_build_index.py:977-1024`) rarely fires because `check_index_input` (`:917-927`) calls almost every records path structural (2251 of 2545 memory commits since 2026-10-15). The builder already ran `--write` (`tools/workflows/unattended-build.js:1274`); no stamp passes forward. Measured: `--check --staged` 47.8 s for 3224 artifacts; whole hygiene `--staged` 78.7 s; nicocares 13.9 s / 21.8 s. Claimed ~6.7 h/week gov. Fix: `--write` records an input digest; `--check --staged` skips on a match; push boundary renders in full.

## githooks-2 — carries coverage derived twice per staged commit, the second time grading zero specs
Under `--staged`, checks 9, 29, 30 run as three generator processes (`check-memory-hygiene.sh:1497, :1944, :1985`); `--with-verdicts` is refused beside `--staged` (`gen_build_index.py:8847-8852`). `--check-coverage --staged` measured 19.5 s, "graded 0 INPROGRESS chain specs". Claimed ~3 h/week. Fix: allow `--check --staged --with-verdicts`, or skip the coverage derivation when no chain spec is INPROGRESS.

## githooks-3 — ~81 s fixed hook cost per records commit; 1537 records commits/month
Straggler prelude (`.githooks/pre-commit:111-134`), policy guard (`:200-216`), hygiene `--staged` (`:228-230`), manifest staged leg (`:256-257`), commit-msg RUN.md scan (`.githooks/commit-msg:52-54`). Green output 13 lines / 2.1 KB per commit into agent context. Claimed ~7.8 h/week (overlaps 1 and 2). Fix: fold a unit's closing records into one commit; print only non-ok lines.

## githooks-4 — every landing pays two local bars; `covered` reuse fired 0 of 39 pushes
`.githooks/pre-push:24-27, :2102-2204` can skip on an identical green tree; the close bar runs on the branch tip (`tools/unattended/unattended.sh:11421-11467`), then `tools/push-main.sh:1219, :1399` reconciles and merges, so the pushed tree never equals the graded one. `pushes.log`: 39 lander pushes in 30 days, scoped mean 1642 s, full mean 2546 s, covered 0. aBriskDeclaration: close bar 19 min at 7e771ae9e, then full pre-push bar 25 min at aebbb4a72. Claimed ~4.9 h/week. Fix: run `--prepare` before the close's bar so the close grades the merged tree and the push reads `covered`.

## githooks-5 — straggler guard ~2.4 s per commit re-answering a settled migration
`.githooks/pre-commit:111-115` → `.githooks/straggler-guard.sh:194-287` (cat-file, rev-parse, merge-base --all per commit). Measured 2.36 s, answer `postflip`. Claimed ~25 min/week. Fix: short-circuit when HEAD's conf already reads `BACKLOG_MODE=builds`.

## githooks-6 — remote CI re-runs a GATE_FULL bar and whole-history hygiene on the sha pre-push just graded green
`.github/workflows/remote-ci.yml` bar job `GATE_FULL=1 ... run-gates.sh` and a history-audit hygiene on every push to main. Claimed ~6.9 h/week hosted-runner time. Fix: nightly/sampled CI bar.

## githooks-7 — adopters pay the staged render too (nicocares 21.8 s per memory commit)
nicocares `.githooks/pre-commit:53-55`, incms `.githooks/pre-commit:85-87`. Claimed ~50 min/week nicocares.

## legs-1 — "routed commits" runs a report-only deviation join: one full-history `git log -S` per rescope row (1040)
`tools/memory-tree/routed_commits.py:531` returns the exit before appending `check_deviation_join` lines (docstring `:79-80` "never moves the exit"); armed by `.memory-tree.conf:1083-1085`; `deviation_join.py:629-637` → `read_row_commit` (`:332`) spawns a pickaxe per row. 30 sampled pickaxes mean 0.21 s → ~219 s/bar. Leg `guard: []`. Ledger median 591 s, 25 retry-after-timeout. Fix: drop the join from the leg (it cannot move the verdict) or one batched `git log -p` pass.

## legs-2 — pass-order and brief-recorded re-read every build README and RUN.md, ~15 spawns per build, RANGE mode too
`tools/unattended/check-pass-order.sh:319-378`, `check-brief-recorded.sh:361-396`, `lib-unattended.sh:1277-1278, 1449-1463`. 127 builds past cutoff; 1366 CLOSED units (memory note's 89-108 is stale). Replay of per-build reads 110 s. Ledger medians 294 s and 236 s. Fix: one `git cat-file --batch`; in RANGE mode grade only builds whose ids appear in the range.

## legs-3 — memory hygiene check 9 re-renders the whole index and computes carries coverage twice in one process
`check-memory-hygiene.sh:1479-1482`; `gen_build_index.py:2748` and `:2967` both call `read_carries_coverage`; 11.2M `unfenced_lines` calls; `--print-bindings` re-parses (check 21, `:1597`). Measured 66.5 s quiet. Fix: memoize per process; blob-sha cache.

## legs-4 — "instruction edits" runs the whole tags check inside itself, so every bar pays tags twice, both near their 420 s ceiling
`tools/playbook/instructions_edit.py:526` → `run_tag_check` (`:425-433`) → `gov_tag.run_kit_verb(root, 'check')`, the same verb as the tags leg (gate-legs.json). Ledger: medians 291 s / 263 s, retried 5/10 each; health.log 13 + 6 retry-after-timeout, co-timeouts on 2026-11-14. Fix: drop the embedded call or the separate leg.

## legs-5 — fixture-only legs (marker contracts, spawn budget) have no guard and rerun on records-only bars
`tools/memory-tree/marker-contract.test.sh` and the fork-count leg read only kit source and fixtures; no `guard`; unguarded legs keyed on the whole-tree fingerprint (`run-gates.sh:3274, 3297-3298`). Medians 138 s + 255 s. Fix: add guards.

## legs-6 — transition-audit and straggler-guard suites sit in `declarations`, not `selftests`, for one repo-reading arm each; straggler-guard is the most-retried leg
`transition-audit.test.sh:12-16`, `straggler-guard.test.sh:15` (8 `git init`, 21 arms); guards compare against BASE = merge-base with origin/main (`run-gates.sh:523-539`). health.log: 37 retry-passed for straggler-guard (300 s ceiling). Fix: split the repo-reading arm into its own leg; move the rest to `selftests`.

## legs-7 — govkit acceptance matrix is an install-and-run self-test in the per-bar chunk with a guard narrower than its reads
`tools/govkit/matrix.py:712-1047` (7 repo shapes; shape 5 runs every installed kit leg). Chunk `declarations`. Median 676 s, max 3184 s. Fix: move to `selftests`, or widen guard to `tools/`.

## legs-8 — unattended kit gate costs ~34 min median when a --close sets GATE_SELFTESTS, and is the critical path
`tools/unattended/unattended.sh:10867` exports `GATE_FULL=1 GATE_SELFTESTS=1`; `check-unattended.sh:885, :1327, :4184, :4431` loop all 131 RUN files; 684 forks on an empty fixture. Median 2039 s, max 7933 s. Suspected, not profiled.

## legs-9 — class: 7 of the 13 costliest legs can never be skipped or reused on a records-only commit
No guard / `guard: []` falls through at `run-gates.sh:3274`; reuse keyed on whole-tree fingerprint (`:3297-3298`); `routed_commits.py:402-403` grades WHOLE beside RANGE every push. ~2560 leg-seconds/bar. Fix: guards, blob caches, per-commit verdict cache for history legs.

## bar-1 — legs run 3-8x slower than alone because the host is oversubscribed; the turnstile does not cover pass bars or the preamble
`run-gates.sh:1655` `TS_SLOTS=${PROF_SLOTS:-1}`; pass bars run `GATE_TURNSTILE=0` (`tools/run-gates/pass-legs.sh:333`); `regen.py --check` runs before the queue (`run-gates.sh:1545-1580`); width 8 uncalibrated (`gate-profiles.txt:119`). Census field 8 of 7048 `.leg` rows: 92% of leg runs / 97% of leg-hours ran beside foreign gate work. Alone vs loaded: govkit matrix 316 s vs 1205-3709 s; hygiene 201 vs 621-1022; routed commits 434 vs 1331-2509. CI's uncontended GATE_FULL bar: 21.5 min end to end. Claimed 7-9 h/week of bar wall is contention. Caveat: census can over-count (`run-gates.sh:3044-3049`).

## bar-2 — one slot per host: bars wait up to 2 h before the first leg
Run headers' `queued` key (`run-gates.sh:2255-2265`): 2026-11-14 waits 2728, 1494, 5094, 4648, 290 s; summaries show 7223 and 7192 s. Claimed ≥4-7 h/week of serial latency.

## bar-3 — a full bar's wall is its longest leg (govkit acceptance matrix, one serial process); width 8 is about half idle
`tools/govkit/matrix.py:111,153-159,449,913,958,1025-1040`; chunk=declarations escapes the hold (`run-gates.sh:3259`). Longest leg in 14 of 14 retained runs since 11-13; leg-sum/wall 3.5-4.5 at width 8. Claimed ~4.7 h/week. Fix: one leg per shape, or hold it.

## bar-4 — a unit runs the bar ~5 times locally plus CI (same mechanism as githooks-4)
pre-push skips only on `covered` (`.githooks/pre-push:2196-2206`); FULL forced when the green is >10 landings back (`:1401`, `GATE_FULL_MAX_LAG=10`) and on 13 other predicates (`:1560-1725, 2083-2097`); CI `remote-ci.yml:136`. gates.log since 10-15: 199 bars for ~40 landings (78 pass, 46 close, 39 push, 36 plain). Adopters: incms 4/4 pushes full, nicocares 2/2 full.

## bar-5 — leg caching almost never fires
Unguarded legs keyed on whole-tree `FPRINT_START` (`run-gates.sh:3343-3345`); cache off under GATE_FULL except lineage (`:3451-3458`). 87 of 95 default-bar legs unguarded (summed medians 4029 s). gates.log: 4 of 199 bars reused any leg. Claimed 2-3 h/week wall.

## bar-6 — per-leg ceilings fire on contention, not hangs; each costs the ceiling plus a serial solo retry
`run-gates.sh:4004-4023` (`timeout -k 5s`), retry `:4532-4730`, called `:5291`. health.log since 10-15: 86 retry-passed, 44,770 s of wasted first attempts. Pairs: instruction edits 420 s timeout then 404 s pass; pass-order 5406 s then 5401 s. Claimed ~2.2 h/week wall + 2.8 leg-h. Fix: idle/CPU hang detector; whole-run wall already bounds.

## bar-7 — ceilings re-declared to chase legs that grow with history
`tools/run-gates/derive-ceilings.py` is monotone. routed commits 300→760→3540; spec tokens 180→390→940; instruction edits 180→420. 7 raise commits since 10-15. Claimed 2-3 session-h/week. Fix: require a spawn count before a raise; cache history passes.

## bar-8 — no fail-fast: 60% of bars are red and the first red lands ~0.3 into the wall
No fail-fast in `run-gates.sh`; reporting in manifest order (`memory/guides/MERGE-BAR.md:38-39`). gates.log: 120 of 199 red, 40.6 h of red wall, median 2 failed legs. First-red/wall pairs median ~0.3; first reds mostly cheap records legs. Claimed ~6 h/week. Fix: opt-in `GATE_FAIL_FAST` for closes/plain bars; or cheap records legs first.

## bar-9 — a ~130 s `regen.py --check` preamble before every bar, longer than the pass bar's own legs, duplicating ~9 legs
`run-gates.sh:1560-1580`; timed 144 s (gotchas INDEX 136 s, LIVE index 47 s). Pass bars: wall 181-329 s vs leg wall 83-96 s. Claimed 1.4 h/week; halves pass-bar latency. Fix: skip in pass bars; check only outputs whose inputs moved.

## bar-10 — self-test suites ride every full bar because they are filed `declarations`, not `selftests`
transition-audit, straggler-guard, marker contracts, review-protocol parity, kit/dogfood parity, codebase-map coverage, run-selftests --check, testsuite counts: ~745 leg-s per bar. Hold rule by label (`run-gates.sh:3259-3262`). Fix: re-file as `selftests`.

## bar-11 — remote CI is red on every run, so its cost buys no signal
`remote-ci.yml:103-136`; `spawn budget` leg grades fork counts calibrated on node a (`memory/project/fork-ceilings.txt`) and fails on the runner. `gh run list`: last 28 push runs and last 12 scheduled runs all failed. Claimed ~14 runner-h/week with zero protection. Fix: make spawn budget node-relative / exclude on CI; then let a green CI satisfy the full-bar obligation.

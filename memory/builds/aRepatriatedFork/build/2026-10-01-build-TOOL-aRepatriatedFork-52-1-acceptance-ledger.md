# TOOL-aRepatriatedFork-52 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-52

Written by the unit pass on node a, 2026-10-01. No merge bar and no self-test runner ran, and the
redesigned leg never ran whole. Each criterion ran its direct check: every population row run once
at gov's prefix with `FOREIGN_PREFIX_PROBE=1`, and the leg sliced with `--kit` in a scratch clone
whose staged break was committed there and discarded with the clone. The harness suite ran whole,
alone, for AC2 and for its own red-first. The spec moved to rev-2 and rev-3 in records commits
before the code each governs.

**Evidences:** TOOL-aRepatriatedFork-52
- AC1 — `--kit micro-format` — a scratch clone whose `check-microformats.test.sh` reads its gate as `$(git rev-parse --show-toplevel)/tools/check-microformats.sh` makes the leg exit 1 with `[scripts] micro-format gate selftest · probe · rc 1 · 1s · RED, exit 1`; with the literal restored the same slice exits 0 with `PASS (3 assertions)` after one green line at each prefix
- AC2 — `foreign-prefix-probe: stopped after 1 arm` — `bash tools/lib/lib-selftest.test.sh` prints `PASS (18 assertions)` without the flag and, with it, the marker and `PASS (1 assertions)`; the python suite `tools/drift-audit/selftest.py`, run by the main loop at f21e441b, prints `all checks passed (315 executed, floor 277)` without the flag in 331 s and, with it, the marker and `PASS (1 assertions)`
- AC3 — `foreign-prefix-probe: stopped after 1 arm` — the micro-format row, which prints that marker, declared whole in a scratch clone reds as `a stale whole-run declaration: it printed the probe marker`, and the kit-placeholders suite with its site deleted reds as `an undeclared whole run: it printed no probe marker, so it ran every arm`, each exit 1
- AC4 — `not run` — AC1's break, which reds at `scripts/`, prints `[vendor/gov] not run — scripts was red` and `[root] not run — scripts was red`, and the leg exits 1
- AC5 — `[<prefix>]` — AC10's run printed 81 `[scripts]`, 81 `[vendor/gov]` and 81 `[root]` lines, one per row of the 82 that `run-selftests.sh --list` prints less the leg's own, each carrying `probe` or `whole`; the root's `govkit selftest` line reads `not graded · gov layout`, per rev-6
- AC6 — `gate-run` — a fabricated `fake-1` record at the clone's HEAD marking the micro-format row `fail` makes the leg name it red at gov's prefix in that run and print `not graded` for it at each prefix, exit 0; with no record it prints `no recorded bar run covers this tree` once
- AC7 — `git diff --stat` — in place of a diff, the leg compares the blob of the budget file and of `gate-legs.json` at each move commit against HEAD's and reds on a difference; no slice redded on it, and the leg no longer edits either file in the clone
- AC8 — `REFUSING to re-spell blind` — each move printed `152 declaration file(s) re-spelled`, and a clone whose `check-install-prefix.sh --list` lists nothing makes the leg print the refusal and `FAIL  could not move the tool root to scripts`, exit 1
- AC9 — `WHAT THIS DOES NOT CHECK` — the leg's header names history-bound arms, the probe arm's choice, gov's own prefix and non-head spellings of the old root
- AC10 — `PASS (3 assertions)` — `bash tools/run-gates/foreign-prefix.gov.test.sh`, no argument, alone at 19ef4230 on node a, exit 0 in 2494 s: all 81 rows graded green at `scripts/` and at `vendor/gov/`, 80 at the root with `govkit selftest` declared not graded there. Four earlier whole runs redded and are the VERIFYING repair R3; the per-suite table is below
- AC11 — `derive-ceilings.py --check` — exits 0 after `--write --reset --observed` recorded 2494 s for the leg, written from a clone with no gate-run readings; the manifest ceiling is 7500 and the budget 3750, both below the 21600 s wall
- AC12 — `bash tools/check-kit-versions.sh` — exits 0 with check-wiring at 1.23, memory-tree at 2.114, kickoff-manifest at 1.16 and unattended at 1.52, and `python tools/govkit/govkit.py epoch --base 56c7befa` names no versioned kit moved without its version

Other direct checks: every one of the 82 population rows except the leg's own and its ten declared
whole rows was run at gov's prefix under the flag and printed the marker with exit 0. That covers
check-unattended's eight shards, one site each. The harness arm was observed RED against the base
`lib-selftest.sh`. `run-selftests.sh --check`, `derive-ceilings.py --check`,
`check-testsuite-counts.sh`, `check-install-prefix.sh`, `govkit selfcheck`, `lexicon.py --check`,
`check-arms.py --check`, `check-line-length.sh`, `gen_build_index.py --check` and `--check-format`,
`manifest-check.sh` and `test_codebase_map.py` exit 0.

## AC10 per-suite table

Seconds per row at each prefix from the run at 19ef4230. A `whole` row ran alone after its prefix's
probe pool drained; every other row ran in the 8-wide pool.

| Row | Kind | scripts/ | vendor/gov/ | root |
|---|---|---|---|---|
| agent-cap restatement self-test | probe | 10 s | 8 s | 8 s |
| agent-cap self-test | probe | 4 s | 3 s | 2 s |
| agent-instructions self-test | probe | 7 s | 6 s | 7 s |
| backlog migration selftest | whole | 224 s | 106 s | 214 s |
| branch-guard self-test | probe | 8 s | 6 s | 7 s |
| build-index selftest | whole | 122 s | 31 s | 49 s |
| check-arms selftest | whole | 24 s | 6 s | 10 s |
| check-wiring self-test | probe | 32 s | 29 s | 23 s |
| codebase-map adopter e2e | probe | 9 s | 11 s | 7 s |
| codebase-map kit selftest | probe | 1 s | 2 s | 1 s |
| corpus-ids selftest | whole | 290 s | 107 s | 106 s |
| dead-path carriers self-test | probe | 23 s | 20 s | 15 s |
| drift-audit selftest | probe | 2 s | 3 s | 4 s |
| extract-arms self-test | probe | 8 s | 8 s | 8 s |
| gotchas selftest | whole | 12 s | 12 s | 11 s |
| govkit selftest | probe | 50 s | 51 s | not graded |
| hook destinations self-test | probe | 85 s | 92 s | 69 s |
| install-prefix self-test | probe | 17 s | 15 s | 11 s |
| kit-placeholders self-test | probe | 6 s | 5 s | 4 s |
| lexicon selftest | probe | 4 s | 3 s | 3 s |
| line-length gate selftest | probe | 17 s | 15 s | 12 s |
| manifest-check self-test | probe | 26 s | 26 s | 19 s |
| memory-hygiene self-test | probe | 140 s | 169 s | 136 s |
| memory-recall kit selftest | probe | 2 s | 1 s | 2 s |
| method-carriers self-test | probe | 8 s | 11 s | 6 s |
| micro-format gate selftest | probe | 11 s | 14 s | 10 s |
| placeholder-catalogue self-test | probe | 6 s | 7 s | 4 s |
| playbook parity selftest | probe | 28 s | 27 s | 21 s |
| playbook render selftest | whole | 1 s | 1 s | 1 s |
| pre-push bar self-test | probe | 15 s | 15 s | 11 s |
| pre-push run-log line | probe | 19 s | 18 s | 14 s |
| pre-push self-test | probe | 18 s | 19 s | 15 s |
| process-monitor adopter selftest | probe | 11 s | 11 s | 10 s |
| process-monitor census selftest | probe | 2 s | 1 s | 1 s |
| profile-bar selftest | probe | 34 s | 38 s | 31 s |
| push-main self-test | probe | 15 s | 17 s | 14 s |
| pytest-guardrails self-test | probe | 7 s | 7 s | 7 s |
| python resolver (behaviour + inline parity + idiom ban) | probe | 6 s | 6 s | 5 s |
| recall floor arms | probe | 8 s | 8 s | 8 s |
| review-join self-test | probe | 11 s | 17 s | 12 s |
| row-grammar selftest | whole | 29 s | 21 s | 25 s |
| row-keyed merge driver replay | probe | 23 s | 24 s | 20 s |
| run-gates adopter e2e | probe | 9 s | 11 s | 7 s |
| run-gates canary | probe | 93 s | 99 s | 90 s |
| run-gates evidence | probe | 33 s | 37 s | 30 s |
| run-gates gov canary | probe | 5 s | 7 s | 5 s |
| run-gates run-log line | probe | 30 s | 34 s | 28 s |
| run-gates turnstile | probe | 98 s | 113 s | 93 s |
| run-selftests self-test | probe | 16 s | 18 s | 14 s |
| runlog selftest | probe | 6 s | 4 s | 3 s |
| scratch-guard self-test | probe | 8 s | 11 s | 7 s |
| selftest harness self-test | probe | 4 s | 4 s | 3 s |
| settings-merge selftest | whole | 6 s | 4 s | 5 s |
| shell-hygiene selftest | whole | 1 s | 0 s | 0 s |
| spec-tokens self-test | probe | 10 s | 13 s | 10 s |
| template size gate selftest | probe | 5 s | 8 s | 6 s |
| testsuite counts self-test | probe | 7 s | 10 s | 6 s |
| tier2-review self-test | whole | 1 s | 2 s | 2 s |
| unattended adopter e2e | probe | 26 s | 36 s | 27 s |
| unattended arms-groups selftest | probe | 3 s | 4 s | 2 s |
| unattended brief-recorded selftest | probe | 21 s | 28 s | 23 s |
| unattended cross-component | probe | 6 s | 8 s | 6 s |
| unattended driver selftest | probe | 49 s | 61 s | 47 s |
| unattended gate selftest shard 1/8 | probe | 180 s | 183 s | 165 s |
| unattended gate selftest shard 2/8 | probe | 174 s | 177 s | 159 s |
| unattended gate selftest shard 3/8 | probe | 177 s | 175 s | 159 s |
| unattended gate selftest shard 4/8 | probe | 186 s | 178 s | 170 s |
| unattended gate selftest shard 5/8 | probe | 183 s | 173 s | 165 s |
| unattended gate selftest shard 6/8 | probe | 186 s | 159 s | 157 s |
| unattended gate selftest shard 7/8 | probe | 181 s | 154 s | 154 s |
| unattended gate selftest shard 8/8 | probe | 173 s | 141 s | 147 s |
| unattended gate-guard selftest | probe | 12 s | 9 s | 7 s |
| unattended pass-order selftest | probe | 25 s | 28 s | 30 s |
| unattended playbook selftest | probe | 33 s | 34 s | 37 s |
| unattended resume-tick selftest | probe | 6 s | 6 s | 5 s |
| unattended runlog-writer selftest | probe | 20 s | 19 s | 18 s |
| unattended stall-recorder selftest | probe | 9 s | 8 s | 7 s |
| unattended stop-guard selftest | probe | 6 s | 11 s | 6 s |
| unattended-build self-test | probe | 7 s | 8 s | 5 s |
| verdict-epoch self-test | probe | 14 s | 16 s | 14 s |
| verifier fan-out self-test | probe | 9 s | 12 s | 9 s |

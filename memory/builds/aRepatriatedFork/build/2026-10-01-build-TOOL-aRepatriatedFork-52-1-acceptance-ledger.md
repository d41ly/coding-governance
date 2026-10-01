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
- AC2 — `foreign-prefix-probe: stopped after 1 arm` — `bash tools/lib/lib-selftest.test.sh` prints `PASS (18 assertions)` without the flag and, with it, the marker and `PASS (1 assertions)`; the python suite `tools/runlog/selftest.py` prints the marker and `PASS (1 assertions)` under the flag. The python suite's run without the flag is owed to the main loop, since a pass runs no whole suite beyond one
- AC3 — `foreign-prefix-probe: stopped after 1 arm` — the micro-format row, which prints that marker, declared whole in a scratch clone reds as `a stale whole-run declaration: it printed the probe marker`, and the kit-placeholders suite with its site deleted reds as `an undeclared whole run: it printed no probe marker, so it ran every arm`, each exit 1
- AC4 — `not run` — AC1's break, which reds at `scripts/`, prints `[vendor/gov] not run — scripts was red` and `[root] not run — scripts was red`, and the leg exits 1
- AC5 — owed to the main loop: one `[<prefix>]` line per row is AC10's run to observe. Every slice this pass ran printed one line per selected row at each prefix, each carrying `probe`, and the 82 rows of `run-selftests.sh --list` less the leg's own are each either sited or on `WHOLE_RUN`, checked by script
- AC6 — `gate-run` — a fabricated `fake-1` record at the clone's HEAD marking the micro-format row `fail` makes the leg name it red at gov's prefix in that run and print `not graded` for it at each prefix, exit 0; with no record it prints `no recorded bar run covers this tree` once
- AC7 — `git diff --stat` — in place of a diff, the leg compares the blob of the budget file and of `gate-legs.json` at each move commit against HEAD's and reds on a difference; no slice redded on it, and the leg no longer edits either file in the clone
- AC8 — `REFUSING to re-spell blind` — each move printed `152 declaration file(s) re-spelled`, and a clone whose `check-install-prefix.sh --list` lists nothing makes the leg print the refusal and `FAIL  could not move the tool root to scripts`, exit 1
- AC9 — `WHAT THIS DOES NOT CHECK` — the leg's header names history-bound arms, the probe arm's choice, gov's own prefix and non-head spellings of the old root
- AC10 — owed to the main loop: `PASS` after all three prefixes, from `bash tools/run-gates/foreign-prefix.gov.test.sh` with no argument, run once alone. Slices this pass ran took 70 s for three pre-push rows and 168 s for one gate shard, clone and three moves included
- AC11 — owed to the main loop: `python tools/run-gates/derive-ceilings.py --write --observed` from AC10's reading, then `--check`. The budget row still carries the sized 60000 s of the first design
- AC12 — `bash tools/check-kit-versions.sh` — exits 0 with check-wiring at 1.23, memory-tree at 2.114, kickoff-manifest at 1.16 and unattended at 1.52, and `python tools/govkit/govkit.py epoch --base 56c7befa` names no versioned kit moved without its version

Other direct checks: every one of the 82 population rows except the leg's own and its ten declared
whole rows was run at gov's prefix under the flag and printed the marker with exit 0. That covers
check-unattended's eight shards, one site each. The harness arm was observed RED against the base
`lib-selftest.sh`. `run-selftests.sh --check`, `derive-ceilings.py --check`,
`check-testsuite-counts.sh`, `check-install-prefix.sh`, `govkit selfcheck`, `lexicon.py --check`,
`check-arms.py --check`, `check-line-length.sh`, `gen_build_index.py --check` and `--check-format`,
`manifest-check.sh` and `test_codebase_map.py` exit 0.

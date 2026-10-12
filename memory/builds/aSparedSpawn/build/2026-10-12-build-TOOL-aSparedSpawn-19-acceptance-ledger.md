# Acceptance ledger — TOOL-aSparedSpawn-19

**Serves:** journal TOOL-aSparedSpawn-19

Node `a`, 2026-10-12, bash 5.3 under MSYS. The pass ran no merge bar, no suite, no held leg and no
slice of a suite. Each criterion was observed by running `tools/gate-lint/fork-count.sh` directly,
over the real ceilings file or over hand-built ceilings files in the scratch root: one row for bash
`9.9` whose setup and command are `true`, and one row for bash 5.3 whose setup is `exit 1`. Every run
was repeated over the base script, `git show HEAD:tools/gate-lint/fork-count.sh` at `6c42ceec`
(unchanged since `8444f597`), to observe the red each criterion names. The selftest's three new arms
were also run over a staged break, a copy of the changed script with both new decisions replaced by
`if false; then`, and all three printed `SELFTEST FAIL`. The whole `spawn budget (forks per hot
entrypoint)` leg over the tree did not run here; it is owed at VERIFYING with the bar.

**Evidences:** TOOL-aSparedSpawn-19
- AC1 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only no-such-id` — changed script: exit 2, the refusal naming `--only no-such-id` and listing all seven declared ids. Base script: exit 0 with `0 passed · 0 red · 0 skipped`, the red the criterion names.
- AC2 — `bash tools/gate-lint/fork-count.sh failed.txt <scratch>` over a one-row file for bash 5.3 whose setup is `exit 1` — changed script: the row's `skipped` line, the summary, then exit 2 with the refusal naming bash 5.3. Base script: exit 0 with `0 passed · 0 red · 1 skipped`.
- AC3 — `bash tools/gate-lint/fork-count.sh other99.txt <scratch>` over a one-row file for bash 9.9 — changed script: exit 0, the `skipped — gamma · no ceiling is declared for bash 5.3` line, and `fork-count: NOT MEASURED — no row declares bash 5.3, so the spawn budget was not measured on this bash`. Base script: exit 0 with no NOT MEASURED line.
- AC4 — `grep -n 'NOT MEASURED' tools/gate-lint/fork-count.sh tools/gate-lint/README.md` — printed the header's rule at line 38 of the script and the README's `fork-count.sh` section at line 178, beside the code and selftest lines.
- AC5 — `bash tools/gate-lint/fork-count.sh --selftest` — exit 0 printing `PASS (5 assertions)`. Over the staged break it exited 1 with three `SELFTEST FAIL` lines, one per new arm, each showing the base behaviour's exit 0.

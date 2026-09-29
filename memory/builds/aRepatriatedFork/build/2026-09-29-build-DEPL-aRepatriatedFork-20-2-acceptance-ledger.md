# DEPL-aRepatriatedFork-20 — acceptance ledger, the landing

**Serves:** journal DEPL-aRepatriatedFork-20

The passes after the first one finished the owed work on inCMS branch `converge/aRepatriatedFork-20`
and landed it on inCMS `origin/main` at `6e19a07b9` on 2026-09-29, through inCMS's own lander, with
BLOCK-aLanternedFoyer-7's commits in the same push by the owner's ruling. AC6 is answered by the first
ledger, `2026-09-24-build-DEPL-aRepatriatedFork-20-1-acceptance-ledger.md`. This ledger answers the
other six, each from an observation at the landed sha or on the branch tip that became it.

**Evidences:** DEPL-aRepatriatedFork-20
- AC1 — `govkit.py update` — from gov `41a874cf`, `adopt --re-adopt --write` recorded `gov_commit 41a874cf` with 33 of the 34 unattributed rows pinned by role or declared `[[own]]`; the read-only update then read `41a874cf -> 41a874cf`, and no memory-tree row is `unattributed` or `adopter-owned` except the declared `.claude/hooks/recall-opened.js`. One non-memory-tree row, `.githooks/pre-push`, stays unattributed (`TOOL-aRepatriatedFork-43`), so later write runs withhold their own re-stamp.
- AC2 — `memory-hygiene` — the leg's argv runs gov's `scripts/check-memory-hygiene.sh`, and it exited 0 inside both full bars at `e10b35a39` and `6e19a07b9`; `check-docs-hygiene.sh` is deleted.
- AC3 — `gen_build_index.py --check-format` — at the landed tree both `--check` and `--check-format` exit 0 over every build README, 332 at the last migration, the 41 nested READMEs cleared by `TOOL-aRepatriatedFork-21`.
- AC4 — `recall-regression` — green in both final bars, 275/275 targets and 1613/1613 alias ids anchored once `TOOL-aRepatriatedFork-40` made recall anchor a spec H1; the `lexicon` leg green at pin 9810.
- AC5 — `check-docs-hygiene.sh` — every check it defined has a disposition in the convergence journal, and the eight kept checks (13, 16, 19, 21, 26, 29, 30, 32) run as inCMS's memory-local leg, `check-memory-local.sh`, and each was observed red on a staged violation in a throwaway clone before the landing.
- AC7 — `bash scripts/gate.sh` — `govkit update --write` from gov `41a874cf` wrote 0 files, and with no edit between, the full bar at `6e19a07b9` printed GATE PASSED (1157 s, 49 legs, no red); inCMS's pre-push bar at the push printed GATE PASSED again in the primary tree.

**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "records": the memory tree and its renderer

Base `aebbb4a72`. Timings taken beside a live unattended run (dDeclaredLoop), spawn baseline 38-63 ms per spawn. githooks-1/2 in the gate batch overlap records-1/3.

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` at base `aebbb4a72` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off, does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether it is already fixed on main (`git log -S`, grep) or on `branch/speedups-9c2e63` (build aTrimmedWait), or already filed as an ask (`grep -r` over `memory/builds/*/BACKLOG.md`).
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost. Several findings overlap across lenses; say which ids describe the same mechanism.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the commit/branch/ask", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## records-1 — the pre-commit hook re-renders the whole build index on 89% of memory commits
`.githooks/pre-commit:228-230` → `check-memory-hygiene.sh:1494-1497` → `gen_build_index.py --check --staged`; `check_staged_render` (`gen_build_index.py:977-1064`) renders on any add/delete (`:1025-1026`) or structural path (`check_index_input`, `:895-927`). Temp-index one-file records commit: hygiene `--staged` 83.6 s; render 45.9 s; coverage 17.7 s. 2270 of 2547 memory commits since 2026-10-15 force the render. Claimed ~12 h/week. Fix: render only the staged builds plus LIVE.md; full render at push.

## records-2 — every records commit renders the index twice, and `--write` rewrites all 3224 files when nothing changed
`tools/workflows/unattended-build.js:1274` runs `--write` then commit; hook re-renders. `cmd_write` (`gen_build_index.py:3227-3229`) → `write_text` (`:296-301`) opens `wb` unconditionally. `--check` 49.8 s. Prior: `--write` 68-106 s, +3 s to the next `git status`. Claimed ~7.9 h/week. Fix: compare before write (S); `--write` fingerprint accepted by `--check --staged` (M).

## records-3 — the staged hook computes carries coverage twice
`check-memory-hygiene.sh:1496` withholds `--with-verdicts` under `--staged`; check 29 spawns `--check-coverage --staged` (`:1944`) → `read_carries_coverage` (`gen_build_index.py:2967`) again after `plan()` (`:2748`). 17.7 s, graded 0 specs. cProfile: `read_carries_coverage` 31.1 s of 89.9 s. Claimed ~2.5 h/week. Fix: pass `--with-verdicts` under `--staged`.

## records-4 — a unit owes ~3-4 records commits per product commit; the records phase outlasts the product work
Subjects since 2026-10-15: records 1537, spec 504, build 264, tool 176, fix 38, feat 19 → 3.3 records commits per product commit over 45 builds. TOOL-aBriskDeclaration-1: 9 records/spec commits vs 3 product; memory +126.6 KB vs tools +16.0 KB; open 14:06, last product 15:36, last records 18:48 (3 h 11 min of records/review after the last product edit). Red-fix records (`tools/memory-tree/build_records.py:376-418`, check 31). Claimed ~13 h/week of commit wall; ~8x product output tokens. Fix: two records commits per unit (open, close).

## records-5 — a generated records table inside every spec turns each new record into a spec revision
`gen_build_index.py:2807-2832` renders `gen:spec-records` (marker `:174`) into specs; whole-history spec-revision walks (`deviation_join.py:577-590`, strip `:401-412`) grow with it. 14,561 spec revisions since 2026-10-15, 5,632 (39%) from records commits. Derived. Fix: move the table to the build README or on-demand print.

## records-6 — routed-commits re-runs one whole-history pickaxe per ledger line and rescope row on every bar (same as legs-1)
`routed_commits.py:529-554`; `deviation_join.py:322-333, :611-637`. 340 ledger lines + 1,459 rescope rows; pickaxe 0.23-0.39 s. Gate ledgers last 7 days: 12 runs, 11,814 s. Fix: memoise per (row, path); or one `git log -p` pass.

## records-7 — full memory hygiene re-grades the 12k-file tree in ~12 processes every bar
`check-memory-hygiene.sh:652, :1497, :1597, :1869, :1903, :2015, :3209, :3229, :3246, :3266, :3283`. Standalone: `gotchas.py --check` 132 s, `corpus_ids.py --check` 85.9 s, render 49.8 s, `--print-bindings` 11.4 s, `transition_audit` 14.5 s. Gate ledgers last 7 days: 13 runs, 10,777 s. Fix: per-check memo keyed on blob sha; one shared corpus read. (L)

## records-8 — the index renderer is O(builds × tracked files) pure Python with no parse cache
`gen_build_index.py:1199-1200, :1211-1212` (12.68M genexpr iterations, 8.2 s), `rosters()` `:831` / `extract_roster_ids` `:884`; 39,134 file opens; only 52 subprocesses. Adopters: incms 13.1 s, nicocares 6.6 s. Claimed ~3.4 h/week from the grouping alone. Fix: group by slug once (S); blob-sha cache (M).

## records-9 — rendered handoff prompts are committed though only the indexer reads them after the spawn
`tools/hooks/agent-cap.js:19-33, :710` reads the worktree file at spawn time. 2,889 prompt files, 21.5 MB; 218k changed lines since 2026-10-15 (17% of memory churn). Suspected. Fix: gitignore role-rendered handoffs; commit only the authored brief.

## derived-1 — the recall index is 402 MB per worktree under a 512 MB budget, so almost every query in a new tree or after a commit rebuilds it from scratch (96 s)
`tools/memory-recall/query.py:717-745` (`ensure_cache`, digest of every corpus file's mtime+size incl. untracked, `:285-290`, `:718`), full `build_cache` (`:397`), per-worktree cache dir (`:293-300`), eviction `:756` vs `RECALL_CACHE_BUDGET_MB="512"` (`.memory-tree.conf:663`); README `tools/memory-recall/README.md:126` assumes ~115 MiB. Measured build 95.8 s, 342,828 chunks, 402 MB. `.git/recall/queries.jsonl`: 682 queries since 2026-10-18, 181 after a worktree switch, 76 after a HEAD move. Claimed ~1.8 h/week. Fix: content-keyed incremental store shared in the common dir; stopgap: raise the budget.

## derived-2 — a chain packet commits its own HEAD sha and a blob pin every pass moves, so a 2-line re-render commit follows every pass
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py:415` (`rendered at`), `:504-520` (byte compare). 213 "packet re-rendered" commits since 2026-10-15 (e.g. fd52a1e27, 4afb98bbb, b85308fbd: 2+/2-). Claimed 0.9-3.2 h/week. Fix: drop the volatile lines from committed bytes.

## derived-3 — the kickoff manifest watches the hottest files, forcing ~10 re-stamp commits a week
`skills/session-kickoff/manifest-check.sh:1843-1861` (check 5), `:1953-1968` (check 9); watch list in `memory/guides/SESSION-KICKOFF.md` includes `tools/gate-legs.json` (78 commits since 2026-10-15), `run-gates.sh`, `run-selftests.sh`, `check-memory-hygiene.sh`; `skills/session-kickoff/SKILL.md:99-125`. 41 standalone/merge re-stamps in 4.3 weeks. Fix: drop gate-legs.json and run-gates.sh from the watch list; accept merges whose watched changes came from stamped parents.

## derived-4 — check-wiring --session spends 27 s per start, 11 s on a report-only straggler inventory (duplicates sessionhooks-4, spawns-6)
`tools/check-wiring.sh:2050-2131` (`check_backlog_stragglers`, comment `:2026-2040` says report-only) → `tools/memory-tree/migrate_backlog.py:2594`; card loads the 15.5k-line driver twice (`manifest-check.sh:580-614, :702-758`). `--check` 27.4 s; stragglers 10.85 s.

## derived-5 — `transition_audit.read_modes` parses `.memory-tree.conf` once per commit (17,647 parses) after deduplicating the blobs
`tools/memory-tree/transition_audit.py:364-381` → `read_mode` (`:151-169`) per commit; Walks at `:447-456` from SessionStart, `.githooks/commit-msg:73-110`, `.githooks/pre-push:1005-1030`, hygiene check 26. Walk 3.81 s, read_modes 3.03 s; 2 modes in all history. ~6 min/week. Fix: memoize per blob.

## derived-6 — the pre-commit map gate skips .sh-only commits though symbols.json is 31% shell; the map walks untracked files while the lexicon walks tracked ones
`.githooks/pre-commit:298` (`*.py`/`*.js` only; comment `:292-293`), `tools/codebase-map/map_extractors.py:295-333` (shell layer), os.walk at `map_extractors.py:320`, `map_lib.py:255,339,465,540,936` vs `tools/lexicon/lexicon.py:414, :2266` (`git ls-files`). symbols.json rows: py 4,280, sh 2,126, js 442; regen-only commits d08106d4d, 85a4a8d8f, abc1eaab4, c55c8b4e4. Hook comment says ~1.5 s, measured 7.6 s. Fix: add `*.sh`; switch to `git ls-files`.

## derived-7 — reuse_lookup rebuilds the whole-tree reference index on every call (5.8 of 7.0 s), ~225 calls a week
`tools/codebase-map/reuse_lookup.py:895-912` → `map_lib.py:920-950`. 994 lookups since 2026-10-15. ~22 min/week. Fix: persist keyed by tree id + dirty digest.

## derived-8 — `drift_report.py --check` re-tokenizes the lexicon corpus three times per bar and appends to drift-history.tsv
`tools/drift-audit/drift_report.py:1278, :1467, :1417, :1658`; leg `tools/gate-legs.json:1107-1121`. cProfile 136 s: lexicon parsing ~50 s avoidable; `--check` writes 27 history rows. Leg median 132.6 s. Fix: shared blob-keyed parse cache; `--check` writes nothing.

## suites-1 — the govkit acceptance matrix is a deployer self-test riding the per-push bar as a repo-subject leg; the bar's longest leg (duplicates bar-3, legs-7)
`tools/govkit/matrix.py:712-1000` (7 serial shapes, `:913, :958` run installed legs, `:976` full `git clone --local` of gov); hold ruling `run-gates.sh:3243-3262` bypassed by chunk=declarations. Ran in 12 of 19 bars last 7 days, 16,356 leg-s; clone of gov 24.6 s. Fix: subject=kit, or parallel shapes + `fork_gov` (`tools/govkit/selftest.py:12162`) instead of a full clone.

## suites-2 — fixtures copy or clone the whole gov tree, so suite cost grows with memory/, not code
`tools/govkit/selftest.py:6966` (copytree + init/add/commit), `:5523` (clone), `skills/session-kickoff/manifest-check.test.sh:891` (clone + 2 worktrees), `matrix.py:976`. copytree 18.7 s / 232 MB; `git add -A && commit` of the copy 5 m 52.6 s (may include AV); tracked files 4,568 (10-15) → 12,622 (11-15). Fix: copy only the tool surface; sparse/no-checkout clones.

## suites-3 — agents run self-test suites directly in sessions, outside the bar's last-green cache: ~4.2 h/week foreground
Cache exists: `run-gates.sh:3070-3093` + `<common-dir>/gate-selftest-last` (63 records, all 2026-10-13). gate-guard blocks suites only in unattended passes (`tools/unattended/gate-guard.js:20-40`). Transcripts (14 days): 1,254 suite calls, 30,271 s; W44/45/46 = 111/421/722 calls. Fix: `run-selftests.sh --changed <row>` that reports "unchanged since last green".

## suites-4 — repo-subject suites and fixture checks run every bar, kept there by one arm or no guard (overlaps legs-5/-6, bar-10)
transition-audit.test.sh (header `:11-16`, `:108` cp x13), straggler-guard.test.sh (`:14-18`, `:136-162`), marker-contract.test.sh (no guard, `:154-200, :296-340`), spawn budget (no guard), `run-selftests.sh --check`, testsuite counts. Last 7 days: 15,471 leg-s. Fix: split the repo arm; guard the rest.

## suites-5 — adopter bars run gov's kit self-tests and duplicated legs (overlaps adopters-2)
nicocares `scripts/gate-legs.json`: hook self-tests subject=repo; 7 argvs present twice (hygiene, test_codebase_map, protocol parity, dogfood parity, review-join, drift_report, adopt-memory-recall) because govkit dedupes by `name` (2e8bdd97). nicocares ledger: pre-push self-test 3,692 s, push-main 1,484 s. Fix: emit chunk=selftests; dedupe by argv.

## suites-6 — check-unattended.test.sh runs the whole 51-check checker ~458 times to grade one check per arm
`tools/unattended/check-unattended.test.sh:396` `run()`; `run_scoped` (`:401`) has 0 callers; 13 `--only` sites. Shard readings sum 10,595 s (~23 s per run). Held suite. Fix: default `run` to `--only <arm's check>`.

## suites-7 — the held population cannot be paid: 107 rows, 33.7 h of budgets; the "owed" flagged bar never runs
`tools/run-gates/run-selftests.sh:12-20`; `.unattended.conf:40` `SELFTESTS_OWED_PATHS="tools/"`; `unattended.sh:10802-10832`. Budgets 121,419 s (`selftest-budgets.txt`). Zero self-test rows in 1,914 ledger rows; all 103 run windows have empty `selftests`. Suites grew 11,654 → 145,902 lines (08-15 → 11-15). Fix: replace "owed" with `GATE_SELFTESTS=changed` over the run's range.

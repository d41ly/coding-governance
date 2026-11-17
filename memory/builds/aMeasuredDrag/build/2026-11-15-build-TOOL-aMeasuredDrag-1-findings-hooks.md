**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "hooks": Claude Code session hooks

Base `aebbb4a72`. Durations come from `stop_hook_summary` / hook attachment records in coding-governance transcripts since 2026-10-15 (4.43 weeks), and from piped fixtures. Spawn baselines 40-118 ms per spawn (another run live).

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` at base `aebbb4a72` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off, does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether it is already fixed on main (`git log -S`, grep) or on `branch/speedups-9c2e63` (build aTrimmedWait), or already filed as an ask (`grep -r` over `memory/builds/*/BACKLOG.md`).
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost. Several findings overlap across lenses; say which ids describe the same mechanism.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the commit/branch/ask", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## sessionhooks-1 — stop-guard spawns the driver's `--liveness` on every Stop of a bound session
`tools/unattended/stop-guard.js@44860d32:221-224` → `runLiveness` (`:107-115`) before the cheap allows in `checkStop` (`:139-155`, `background_tasks` at `:151`); the lease's `phase:` is parsed (`tools/unattended/run-lease.js@8a5aa9d7:161`) but unused; N leases → N serial runs (comment `:219` says that cannot happen; sessions 2588f719 and 0394fa33 hold 3 leases each). Transcripts: 7,094 Stops, median 7.5 s, p90 17.9 s, 19.3 h total (4.0-6.0 h/week). Fix: test `background_tasks` and terminal phase first; cache the verdict keyed on RUN.md mtime + HEAD + remote ref. (Overlaps pipeline-5.)

## sessionhooks-2 — format-guard blocks ~78 turn ends a week, 86% only to make the model re-type a line the hook already rendered
`tools/hooks/format-guard.js@90a3f894:685-692` grades new commits; `:700-713` blocks; the block reason already carries the derived line (`deriveOwedLines`, `:563-604`, `:705-708`); `:534-543` spawns `python handoff.py agents`; `scanTurnRecords` (`:328-330`) reads the whole transcript. 345 blocks since 2026-10-15 (95, 117, 55, 78 per week); median 10.6 s to the next assistant record; ~1,371 chars of feedback. Fix: allow the Stop and emit/append derived lines when those are the only defects.

## sessionhooks-3 — procmon-hook spawns git on every Bash call before its throttle check, contrary to its docstring; its census injects ~1 KB of unactionable rows PINNED 2026-11-15
`tools/process-monitor/procmon-hook.js@293e9e0d:21-24` (docstring: throttle is one stat), `:79` `execFileSync('git', ['rev-parse','--git-common-dir'])` reached from `main()` `:105` before `checkThrottled` `:110`; census output `:142-152` lists the desktop app's own idle processes. 2,277 printing censuses (avg 1,041 B), ~26.3k Bash calls/week. Claimed ~69 min/week + ~134k tokens/week. Fix: resolve the common dir with fs as `tools/memory-recall/recall-opened.js@17e45cf9:131-136` does; filter app processes. PINNED 2026-11-15

## sessionhooks-4 — SessionStart pays ~25 s median (p90 2-3 min, 6 runs cancelled at 600 s) re-verifying wiring and writing the card PINNED 2026-11-15
`.claude/settings.json@b236e993:41-72`; `tools/check-wiring.sh` re-runs the full detector, incl. `check_backlog_stragglers` (`:2050-2094`, `migrate_backlog.py --stragglers` 11.0 s over 40 branches); `skills/session-kickoff/manifest-check.sh@4d3d63c0:702-712` reads claims through the driver, `:787-795` runs `load_sets.py`. Transcripts: check-wiring startup n=135 median 17.5 s p90 173.5 s + 5 cancelled; card n=66 median 25.4 s p90 128 s. Fix: stamp the last clean verdict keyed on wiring-file hashes; move the straggler arm to the bar. PINNED 2026-11-15

## sessionhooks-5 — agent-cap rule 6 admits no ad-hoc helper
`tools/hooks/agent-cap.js@44d881b5:691-749` (built-in types never admitted `:698-701`; prompt byte-equal to a rendered `## Task` `:708-736`; sha `:737-738`; description `:744-747`); Workflow only by listed harness, never inline (`:759-779`). This review: refusal → first admitted spawn 339 s, an owner question, ~16 tool calls, an untracked build folder. 75 Agent + 6 Workflow rule-6 refusals since 2026-10-15. Fix: admit a read-only built-in type, or a `--adhoc` render under the git dir. PINNED 2026-11-15

## sessionhooks-6 — every gated tool call pays 1-2 cold node starts (100-160 ms)
`.claude/settings.json@b236e993:13-28, :76-91`; `tools/unattended/gate-guard.js@e58690cf:821` reads the 58 KB gate-legs.json per call. Fixtures: bare node 91 ms, scratch-guard 103-148 ms, gate-guard 128 ms, recall-opened 158 ms. ~32k gated calls/week. Claimed ~1.2 h/week. Fix: one dispatcher process requiring the guards as modules. PINNED 2026-11-15

## sessionhooks-7 — ~180 refusals a week that the handoff could have prevented
`tools/hooks/scratch-guard.js@7c31933f:1631-1636, :1686-1692` (role gate), `:1849-1863` (routed write gate), `:1877-1883` (/tmp), `:779-809` (orientation). Since 2026-10-15: role-gate 316, write gate 152, /tmp 134, orientation 11. Fix: render each role's allowed checks and the scratchpad path into the handoff.

## spawns-1 — every Bash call starts 3 node hooks and 1 git, the git even when throttled (duplicates sessionhooks-3/-6)
`tools/process-monitor/procmon-hook.js@293e9e0d:79, :105, :108`; `tools/unattended/gate-guard.js@e58690cf:735` already reads `.git` with no spawn. Pair ~150 ms per hook, throttled procmon 180 ms; ~31k Bash calls/week (11-08..15). Claimed 2.8 h/week quiet, ~13 h loaded.

## spawns-2 — a records commit runs the whole index render in 3 Python processes; CPU, not spawns (duplicates githooks-1/-2, records-1/-3)
`.githooks/pre-commit:228-230`; `tools/memory-tree/gen_build_index.py@5a0864b8:1026` (any add → full render); `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1497, :1944, :1985`; `tools/memory-tree/gen_build_index.py@5a0864b8:1990` → `tools/check-spec-tokens.py@f1d1d958:1242` `derive_carries_coverage` (15,262 binding blocks, 0 INPROGRESS). `--check` 52.6 s (90.4M calls, 52 subprocesses); `--check-coverage` 21.6 s; `--check-asbuilt` 2.4 s; pre-commit floor 4.2-4.9 s. Claimed ~8.8 h/week quiet.

## spawns-3 — the unattended kit gate loops all RUN files and per-commit conf history with per-iteration spawns
`tools/unattended/check-unattended.sh@434b64be:2402-3338` (131 RUN files, ~55 forkable lines per iteration), `:2203-2215`, `:2159-2166`; GIT wrapper `tools/unattended/lib-unattended.sh@a3e03db6:62`. Ledger median 2039 s, max 7933 s; fixture count 684 forks (`memory/project/fork-ceilings.txt`). Suspected (not run). PINNED 2026-11-15

## spawns-4 — brief-recorded spends 4-6 spawns per build README for a date cutoff (overlaps legs-2)
`tools/unattended/check-brief-recorded.sh@626764ee:361-374, :383-406`; `printf | sort -C` at `:366` instead of a bash string compare. 211 READMEs, ~1.0-1.3k spawns before grading. Ledger median 236 s. PINNED 2026-11-15

## spawns-5 — `--liveness` costs 93 forks; the remote ladder re-resolves 6 times per call (overlaps sessionhooks-1)
`tools/unattended/unattended.sh@7c95cec6:2725-2753` (6 calls x 6 forks), `:8620` `stat` per dirty path. `--liveness` 8.85 s; `--version` 1.76-1.90 s. Fix: memoize RR_* per process; batch stat. PINNED 2026-11-15

## spawns-6 — check-wiring runs its whole check at every SessionStart: 274 forks, ~31-36 s (overlaps sessionhooks-4)
`tools/check-wiring.sh@e7cfeeba:258-260, :2148`; per-file loops `:1306` (x52), `:207-209` (x56), `:1868-1871` (x31). Fork-ceilings fixture declares 45 forks: real tree ~6x the gated count.

## spawns-7 — the spawn-budget leg costs ~255 s per bar re-counting forks of untouched files (overlaps legs-5) PINNED 2026-11-15
`tools/gate-lint/fork-count.sh` over `memory/project/fork-ceilings.txt` (7 rows), no guard. Ledger median 255 s. PINNED 2026-11-15

## spawns-8 — the Python launcher is re-resolved in every bash leg and fixture run, through the WindowsApps alias
`tools/lib/resolve-python.sh@9ec71b5b:36-43` no cache; `tools/run-gates/run-gates.sh@bfc3ad49:338` resolves but does not export; `.githooks/pre-push:535` drops GOV_PYTHON. Alias 256-298 ms vs direct exe 119-131 ms; 67 of 93 bash legs; ~504 resolutions per `check-unattended.test.sh`. Small.

## spawns-9 — a 4-5 s pre-commit floor (84 forks) on every commit (overlaps githooks-3/-5)
`.githooks/pre-commit` runs `git diff --cached` 5 times (`:204/:220, :228, :265, :274, :298`), `resolve_python` twice (`:243, :304`); `manifest-check.sh --staged` ~1 s to decide to skip. ~640 commits/week. PINNED 2026-11-15

## spawns-10 — remedy check, WSL2: 27-50x cheaper bash/git spawns quiet (not 500x), 7x for python; cannot reach per-commit or per-call costs
`claude-u26`: true 1.4 ms, git 2.5 ms, python 17 ms vs MSYS 30-77 / 117-145 / 119-131 ms. Seam `tools/run-gates/run-held-wsl.sh` runs only the held tier. Rank after batching.

## spawns-11 — remedy check, in-process Python consolidation: only where one corpus is re-parsed several times
81 of 175 legs are python argv (~10 s/bar of starts, noise). Win: hygiene checks 9/29/30 and `--print-bindings` (`tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1497, :1597, :1944, :1985`) re-load the corpus four times. PINNED 2026-11-15

**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "pipeline": the unattended driver and build flow

Base `aebbb4a72`. Driver costs are from `C:/projects/coding-governance/.git/runlog/driver.log` (last 7 days unless stated). Spawn baselines 32-41 ms per spawn, quiet.

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` at base `aebbb4a72` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off, does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether it is already fixed on main (`git log -S`, grep) or on `branch/speedups-9c2e63` (build aTrimmedWait), or already filed as an ask (`grep -r` over `memory/builds/*/BACKLOG.md`).
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost. Several findings overlap across lenses; say which ids describe the same mechanism.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the commit/branch/ask", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## pipeline-1 — dispatch, audit and check-commit walk git per dispatch key, terminal keys included
`read_open_passes` (`tools/unattended/unattended.sh@7c95cec6:14192-14211`) calls `check_pass_open` (`:14199`) before the terminal/deferred test (`:14200-14208`); `check_pass_open` (`:14227-14245`) → `pass_commit` (`tools/unattended/lib-unattended.sh@a3e03db6:1027-1096`): rev-parse, log, per-commit diff-tree, `read_brief_paths` (`lib:986-999`). Used by `--dispatch` (`:14829`), `--audit` (`:8692`), `--check-commit` (`:14302-14310`). Measured: `read_open_passes` on dOrderedCharter's RUN.md (89 keys) 124.9 s, 0 open passes. Runlog: dispatch n=210 median 522 s (25.9 h), audit n=666 median 32.6 s (8.2 h), check-commit n=606 median 41.9 s (8.9 h). Claimed 20-30 h/week saved. Fix: skip terminal keys before the walk; one `git log` walk into a cache. PINNED 2026-11-15

## pipeline-2 — `--dispatch` runs the whole-tree spec-token checker though only the dispatching build's lines can refuse
`tools/unattended/unattended.sh@eb567029:14496` (sync fallback `:14528`) unscoped; `check_spec_token_hits` (`:14402-14434`) refuses only own-build hits (`:14419-14422`); key includes HEAD (`:14446`); refusal records no key (`:14538`). Measured whole-tree 74.6 s vs `--spec` 2.6 s. Claimed 4.2 h/week. Fix: `--spec` over the build's own specs; key on spec blobs.

## pipeline-3 — `--check-commit` walks every unit before reading the trailer that usually ends the check
`check_commit_message` (`tools/unattended/unattended.sh@eb567029:14263-14378`) builds rows at `:14301-14310`, tests `Pass: none` at `:14311`. Runlog n=606 median 41.9 s, 8.9 h/week. Fix: parse trailer first; walk only named units.

## pipeline-4 — the 10-minute idle-wake cron runs a model turn plus `--resume` and `--audit` even while a Workflow runs
`.claude/skills/unattended/SKILL.md:17-18`; `resume-tick.sh` exists but is not registered. Runlog: resume n=797 (5.5 h), audit n=666 (8.2 h); stop-guard sidecars: 5240 of 5804 stops allowed for `background-tasks`. Prior: 666 ticks = 24.5 h main-loop busy, 795k output tokens. Fix: skip `--audit` when a task is registered; or out-of-process keepalive; or 30-min cadence.

## pipeline-5 — stop-guard spawns `--liveness` before reading `background_tasks`, which decides 90% of stops
`tools/unattended/stop-guard.js@44860d32:107-115` (`runLiveness`), called at `:223`; `background_tasks` read at `:151`. Runlog: session-bound `--liveness` n=1999, mean 11.2 s (6.2 h/week). Fix: short-circuit when `background_tasks.length > 0`.

## pipeline-6 — `--close` grades the full bar first, keeps going after a cheap item is unmet, reruns the whole bar on retry
`DOD_CORE` lists gates-green first (`tools/unattended/unattended.sh@eb567029:1011`); loop `:11099-11160`; retry strips `GATE_REUSE` (`:11357-11363`). 30 days: 52 closes, 34 refused (25.6 h). aCarriedStop: 7 closes, 9.4 h, one red leg (`routed commits` contended timeout). Claimed 6 h/week. Fix: cheap items first; on re-close at the same tree rerun only red legs.

## pipeline-7 — units build strictly one at a time
Order gate `tools/unattended/unattended.sh@eb567029:14588-14629`; condition 1 (`:14885-14897`) refuses overlapping declared paths; shared generated files (LIVE.md, build README, SESSION-KICKOFF.md, symbols.json) overlap in most passes; `GENERATED_INDEXES` (`.unattended.conf:418`) lists one file. aNimbleMend: orders 1..16, edge depth 5, units 1-12 serial over 5.3 h. Suspected. Fix: exempt generated indexes; derive `order` from edge depth. PINNED 2026-11-15

## pipeline-8 — builders may not run the cheap pass legs; two in three passes come back red and cost a whole new pass
`tools/workflows/unattended-unit.js@71852dc0:313-323` bans gates; main loop runs `pass-legs.sh` after commit (`:386-400`). gates.log 30 days: pass-leg runs n=79, 52 RED (66%), mostly static diff checks (writing practice 27, install-prefix 23, runbook parity 22). aNimbleMend 2.75 dispatches per unit. Claimed ~4 h/week. Fix: let the builder run `pass-legs.sh` once before committing.

## pipeline-9 — every driver call re-parses ~18k lines of bash
`unattended.sh` 15541 lines + `lib-unattended.sh` 2479; `--version` 1.81 s; ~4600 calls/week. Claimed 2.3 h/week. Fix: a small entry for hook-hot read-only verbs. PINNED 2026-11-15

## pipeline-10 — landing runs the bar twice (same as githooks-4)
pre-push has no "already green at this tree" decision (`.githooks/pre-push:1473-1913`); pushes.log decisions full 42, scoped 42, never reuse. 39 push bars in 30 days, mean 1547 s. Claimed 3.8 h/week. PINNED 2026-11-15

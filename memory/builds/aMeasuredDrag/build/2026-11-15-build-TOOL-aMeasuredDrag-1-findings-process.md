**Serves:** research TOOL-aMeasuredDrag-1

# Findings to refute — batch "process": pipeline, ceremony and contention

Base `aebbb4a72`. The pipeline items are in `2026-11-15-build-TOOL-aMeasuredDrag-1-findings-pipeline.md` beside this file; judge them as part of this batch. Ceremony token figures come from transcript usage fields under `C:/Users/daily-agent/.claude/projects/` (31 days, 3430 agents).

## How to judge — the harness's rules for this batch

You are read-only: run no gate leg, bar, `*.test.sh` suite, `--write`, `--land`, `--close`, `--prepare` or `--dispatch`; you may time single read-only commands under about 3 minutes beside a spawn baseline (10 x `/usr/bin/true`). For EACH finding below:
1. Open the cited `path:line` at base `aebbb4a72` and confirm the mechanism is there as described.
2. Challenge the cost: is the frequency real, is the per-event figure inflated by load or a one-off, does the weekly arithmetic hold? Re-measure when cheap.
3. Check whether it is already fixed on main (`git log -S`, grep) or on `branch/speedups-9c2e63` (build aTrimmedWait), or already filed as an ask (`grep -r` over `memory/builds/*/BACKLOG.md`).
4. Say what the proposed fix would weaken.
Default to REFUTED when the mechanism is not where it is cited; PLAUSIBLE when the mechanism is real but the cost cannot be checked; CONFIRMED only when you verified both the mechanism and a material cost. Several findings overlap across lenses; say which ids describe the same mechanism.

Return exactly one fenced `json` block: `{"verdicts": [{"id": "...", "verdict": "CONFIRMED|PLAUSIBLE|REFUTED", "corrected_cost": "your own weekly estimate, saying whether the finder over- or under-stated it", "already_addressed": "none, or the commit/branch/ask", "fix_risk": "what the fix weakens", "duplicates": "ids of the same mechanism, or none", "reason": "the check you ran and what it showed"}]}` with one verdict per finding id, every id.

## ceremony-1 — spec authoring costs more tokens than building
`AGENTS.md:97` [spec], `:120` [roles], `:184`; `memory/TEMPLATE-SPEC.md:137` full skeleton. 31 days: gov-spec-writer 901 agents 84.2M output tokens (41.8%); gov-builder 603 agents 65.4M (32.5%); reviewers 41.0M. aBriskDeclaration: 543-line spec for 136 product + 76 test lines; aTrimmedWait-5: 328-line spec for 24 product lines. Spec lines 531k vs non-test product 151k since 2026-10-15. Fix: micro-spec by default.

## ceremony-2 — 86% of specs are Tier-2 because the kickoff's local tier rule makes any kit change Tier-2
`memory/TEMPLATE-SPEC.md:386-390` vs `memory/guides/SESSION-KICKOFF.md:122-126` (two tier definitions). Status lines on main: 2594 Tier-2 vs 410 Tier-1. aBriskDeclaration and aTrimmedWait ("No verdict moves") both Tier-2. Fix: one tier definition; behaviour-preserving changes with a verdict-equality fixture are Tier-1.

## ceremony-3 — the main loop carries the whole build in one context
aTrimmedWait session 10535f0f: 746 turns, mean context 391k, max 710k, 292M context tokens summed; aBriskDeclaration da280880: 506 turns, 131M. Bookkeeping (status flips, renders, pass legs, index writes, notifications) all in the main loop. Fix: per-unit bookkeeping inside `tools/workflows/unattended-unit.js`; reset between units.

## ceremony-4 — 82% of commits touch no product code
2745 non-merge commits since 2026-10-15, 485 touch `tools/**` or `skills/**`. INPROGRESS gate `tools/hooks/scratch-guard.js:817, :972`; per-pass commits `BUILD-METHOD.md:189`; ledger `:285-287`. 406b9015a is a whole commit of `SPECCED->INPROGRESS` in 3 files. Transcript tool wall: `git commit` ~2.0 min each; `gen_build_index --write` ~1.8 min each. Claimed ≥17 h/week. Fix: status transitions ride the work commits.

## ceremony-5 — every MEDIUM and LOW finding is promoted to a new unit, never folded
`memory/guides/BUILD-METHOD.md:144`. aTrimmedWait round 1: no BLOCKER/HIGH, 7 MEDIUM + 2 LOW → units 8 and 9 (441- and 470-line specs, ~755k output tokens, 1h38m, 7 commits). Counter-case: aBriskDeclaration filed its three as asks (74085e0e8). Derived ~10 h/week. Fix: promote only BLOCKER/HIGH.

## ceremony-6 — [risk] is not honoured at the close: unattended runs owe the full multi-agent review whatever the tier
`AGENTS.md:115`, `TEMPLATE-SPEC.md:386-388` (Tier-1: no multi-agent review) vs `tools/unattended/unattended.sh:1011, :1201, :11965-12029` (no tier read). Review fan-out per run: 12-13 agents, 130k-290k output tokens. Fix: accept a self-review record when every unit is Tier-1, or a light intensity (`tools/workflows/tier2-review.js:306-313`).

## ceremony-7 — record-format legs drive fix passes and pin-only commits
`tools/playbook/writing_practice.py:206, :241` reds bare figures in records. aTrimmedWait: 5 reopen-for-fix-pass commits, 4 writing-practice prompt records spawning spec writers to add `PINNED` comments; 56 pin/practice subjects on main since 2026-10-15. Fix: autofix the pin, or warn on records.

## ceremony-8 — a role agent and a committed prompt record to paste an owner's one-word answer into a spec
`AGENTS.md:120, :184`; aTrimmedWait `prompts/...-5-ruling.md` (41-line brief to write "Batch hashing" into §8); 39 prompt records (~3,480 lines) for 9 units; 20 spec writers. Suspected ~2 h + 1M tokens/week. Fix: mechanical record edits applied inline.

## ceremony-9 — fixed floor for a 10-line fix: ~7 commits, ~15 agents, 3 bars, ~6 records, ~6 h
aBriskDeclaration: first commit 14:06 → landing 20:03 (5h57m) vs 28 min of builder time; CLOSED at 15:41, then 4h22m of review, observations, pin commit, reconcile, landing; 17 agents; 1,530 record lines vs 212 code+test. Fix: a declared Tier-1 fast lane (micro-spec + code in one commit, self-review, pass legs, lander).

## ceremony-10 — fixed prefix (charter + MEMORY.md) ~11.5k tokens per turn; MEMORY.md 19 KB / 148 entries
Low priority. Fix: prune MEMORY.md entries its own text calls fixed.

## ceremony-11 — format-guard still forces re-sent turns at full context
aTrimmedWait session: 6 Stop `hook_blocking_error` events from format-guard (the auto-memory claims dPavedRoad-2 fixed re-sends). Overlaps sessionhooks-2. Fix: the hook appends the derived lines itself.

## contention-1 — bars wait ~7 h a week to enter a one-slot host turnstile that still does not stop them contending (overlaps bar-1/-2)
`tools/run-gates/run-gates.sh:1587-1648` (host key), `gate-profiles.txt:67-72` (slots default 1), `:2165-2170` (runs unqueued after TS_MAXWAIT), `:2260-2284, :3644` (`queued`); pass runs bypass (`tools/run-gates/pass-legs.sh:18, :333`). Week-46 headers: queued 25,797 s, 11 bars, mean 2,345 s, max 7,192 s; health.log 3 `turnstile-expired` at ~7,200 s.

## contention-2 — work outside the turnstile makes legs ~2.2x slower; 7 of 63 bars ran without it (overlaps bar-1)
Leg `.leg` field `foreign` (`run-gates.sh:3028-3049`); 6,918 first-attempt rows: 97% of leg-seconds at foreign ≥ 1; 18-leg median ratio foreign=0 vs ≥3: 2.23 (confounded by tree growth). Session caps `.claude/settings.json:133-134` are per session; 21 claude.exe alive. Claimed 10-17 h/week. Fix: a host leg-slot pool every gate entry takes; cheapest step: pass-legs takes `--hold` (`run-gates.sh:121-124`).

## contention-3 — one 2.2 GB tag index per node, one locked writer holding the lock through a 61 s cleanup scan; three legs time out together
`tools/playbook/tag_index.py:7, :509-520` (journal_mode DELETE), `:666-676` (`remove_unheld_rows` inside `BEGIN IMMEDIATE`), `:696-714` (full anti-join), `:117` (BUSY_TIMEOUT 600 s > 420 s leg ceilings). Read-only SELECT of the anti-join: 61.4 s, 0 rows. index-s3.db 2.2 GB (+ stale index.db 1.77 GB). health.log week 46: instruction edits 13, tags 6 retries; six co-timeouts on 2026-11-14; timed-out `.out` files hold only `exit 124`. Claimed ~3.9 h/week. Fix: move `remove_unheld_rows` to `--gc` only; WAL; BUSY_TIMEOUT below the ceiling. (Competes with legs-4's explanation of the same co-timeouts.)

## contention-4 — ceilings come from solo readings while 92% of leg time runs contended, so legs time out by design and ceilings get raised again and again (overlaps bar-6/-7)
`run-gates.sh:3033-3034` (derive from foreign=0), `:4532-4538` (retry "alone" within its bar only). Week 46: 48 retry-passed, 23,580 burnt ceiling-seconds; 35 ceiling commits since 2026-10-20; summed ceilings 152,620 → 215,924 s since 2026-09-06.

## contention-5 — RED bars hold most of the single slot: 35 of 61 bars red, 20.5 h of 32.0 h (overlaps bar-8)
Top fail legs: memory hygiene 15, tags 11, instruction edits 11, install-prefix 9, routed commits 9. Fix: require a green pass-legs record for the same HEAD before a bar takes a ticket.

## contention-6 — each reconcile merge changes the tree, so a whole new bar is owed plus a re-stamp commit
`.githooks/pre-push:1521-1525` (green by tree). Reconcile merges per week 1, 6, 7, 5, 11 (weeks 42-46). Fix: reuse verdicts of legs whose declared `reads` did not move.

## contention-7 — parked WIP (26 DEFERRED builds, 34 worktrees, 14 idle since before 2026-11-01) pins state that every index build scans
`check-memory-hygiene.sh:2326, :2540` count DEFERRED as LIVE; `tag_index.py:700` keeps every worktree HEAD's tree. LIVE.md builds 17 (09-01) → 48 (10-22) → 43 (11-15); 1,213 of 3,007 specs DEFERRED. Suspected.

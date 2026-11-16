**Serves:** research TOOL-aMeasuredDrag-1

# aMeasuredDrag — why gov and its adopters deliver work slowly

Reviewed: gov at base `aebbb4a72` on node a (Windows + MSYS), with adopters incms and nicocares read only. Twelve researcher lenses and five skeptic batches contributed. Inputs are in `memory/builds/aMeasuredDrag/build/`. Every `path:line` below is at `aebbb4a72` unless it names a branch.

## Verdict: CLEAN WITH FIXES

The skeptics adjudicated 109 findings by their per-line verdicts: 48 CONFIRMED, 55 PLAUSIBLE and 6 REFUTED. The 103 that stand merge into 65 items. Each PLAUSIBLE item stays outstanding: its mechanism is real, but nobody has checked its cost. The verdict means fixes are owed. None of the items breaks what lands. The closest is remote CI, which was red on all 45 runs from 11-01 to 11-14 (bar-11), so the remote half of the bar gives no signal.

The six refuted findings are dropped and not counted:
- adopters-12: incms `scripts/gate.sh (lines 334-350)` already scopes memory-only landings.
- legs-8: the unattended kit gate has been held off automatic bars since `3203e2ac4`.
- sessionhooks-6: the PreToolUse hooks already run in parallel.
- sessionhooks-7: the handoff already renders a role's gates.
- pipeline-9: `bash -n` parses the driver in 65 ms.
- pipeline-10: `covered` exists at `.githooks/pre-push:2197-2204`.

## 1. Diagnosis

Of the six candidate root causes, four hold, one holds only in part and one is supported by a single case.

**Whole-tree work with no incremental cache (confirmed).** This is the largest class.
- The pre-commit render and carries coverage run on about 89% of memory commits (githooks-1, records-1, githooks-2, records-3).
- Full hygiene re-grades the whole tree on every bar (records-7).
- Rows trigger per-row history pickaxes (legs-1, records-6), and builds are re-read one by one (legs-2).
- The driver walks git once per dispatch key (pipeline-1, pipeline-3).
- SessionStart re-verifies all wiring (sessionhooks-4).
- Index queries rebuild their index on each call (derived-1, derived-7).
- The leg cache that should absorb this keys on the whole tree, and it reused a leg in only 4 of 201 bars (bar-5, PLAUSIBLE).

**About five bars per unit, plus CI that is always red (in part).** The count holds: 201 bars for about 40 landings (bar-4). The wall-clock claim does not, because pass bars are short. The repeat that costs real time is two full bars per landing, because the `covered` reuse fired on 0 of 40 lander pushes (githooks-4, PLAUSIBLE). The cause of that is not established. CI red on every run is confirmed (bar-11, githooks-6).

**Ceremony scaled to Tier-2 for nearly every unit (supported by one case).**
- Confirmed: the per-unit floor, 5h57m end to end for 28 minutes of building (ceremony-9).
- Confirmed per instance: minor findings are promoted to new units (ceremony-5).
- PLAUSIBLE only: the 95% Tier-2 share (ceremony-2), spec tokens exceeding build tokens (ceremony-1), and 3.1 records commits per product commit (records-4).

**Host contention (confirmed).**
- 92% of leg rows ran beside foreign gate work (bar-1).
- Bars queue at least 4 h a week for a one-slot turnstile that pass bars bypass (bar-2).
- Ceilings fire on contention, then retry (bar-6).
- One measurement cuts the other way: serial runs were measured faster than concurrent ones (contention-1).

**Adopters on an old kit vintage (confirmed per fix).** Both adopters lack gov's fixes for the lag bound (adopters-3), self-test filing (adopters-2), the staged render (adopters-6) and the charter size (adopters-9). The claim that update size is why they lag is PLAUSIBLE only (adopters-1).

**Speed fixes built as full Tier-2 builds (supported).** aTrimmedWait's round-1 minor findings became units 8 and 9, with 441- and 470-line specs (ceremony-5). That followed the owner's ruling at `memory/guides/BUILD-METHOD.md:144`. Builds marked "no verdict moves" are still filed Tier-2 (ceremony-2).

## 2. Where a unit's wall-clock goes

The sample is aBriskDeclaration (TOOL-aBriskDeclaration-1). It opened at 14:06 and landed at 20:03, 5h57m (357 min) end to end, of which building took 28 min (ceremony-9). Its other times were the last product commit at 15:36, CLOSED at 15:41 and the last records commit at 18:48 (records-4).

| Row | Minutes | Arithmetic and source | Confidence |
|---|---|---|---|
| Building | 28 | Builder time (ceremony-9); 28 / 357 = 7.8% of the wall | high |
| Owner turns | 52 | One owner ruling (ceremony-9) | high |
| Bar runs | 44, plus untimed pass bars | Close bar 19 min at `7e771ae9e` + pre-push bar 25 min at `aebbb4a72` (githooks-4). Pass bars were not timed for this unit; gov-wide, a pass bar's wall is 181-329 s (bar-9) | high for the 44 |
| Records commits and hooks | ~12 | 9 records/spec commits (records-4) x ~81 s fixed hook cost per records commit (githooks-3, PLAUSIBLE, a gov-wide figure) | low | PINNED 2026-11-15
| Queue and contention | ≤31 | 18:48 to 20:03 = 75 min, less the 44 min of bars. The remainder also covers the reconcile merge and the lander | low |
| Orchestration verbs | inside the residual below | Gov-wide per-call medians over 7 days: `--dispatch` 522 s, `--check-commit` 41.9 s, `--audit` 32.6 s (pipeline-1; dominated by dOrderedCharter). This unit's calls were not counted | low | PINNED 2026-11-15
| Spec and review ceremony | ~190 | Residual: 357 − 28 − 52 − 44 − 12 − 31. It covers spec authoring, dispatch, passes, a 17-agent review, observations and the pin commit (ceremony-9) | medium as a total, low on its split |

Only 124 of the 357 minutes are directly measured: building, the owner turn and the two bars. The largest row, about 190 min, is ceremony that nobody has attributed.

## 3. Ranked findings

**How to read the costs.**
- Costs are the skeptics' corrected figures, never the finders'.
- Units differ:
  - **h/wk** is session or agent wall-clock time.
  - **leg-h/wk** is leg time that runs concurrently inside a bar, so it is not wall-clock time.
  - **runner-h/wk** is hosted CI time.
  - **slot-h/wk** is time spent holding a bar slot.
- A cost that sits inside another row is marked "inside #n" and is not added. The table gives no grand total.
- Rows 1-34 have a weekly figure. Rows 35-65 have none and are ordered by verdict, then by size.
- **Effort** is this synthesis's estimate, except where the finder gave one (see §8).
- **Verdicts:** C is CONFIRMED and P is PLAUSIBLE. A merged row lists the minority verdict by id.

| # | Ids | Title | Verdict | Corrected weekly cost | Payer | Fix | Effort | What the fix trades |
|---|---|---|---|---|---|---|---|---|
| 1 | bar-11, githooks-6 | Remote CI re-runs a GATE_FULL bar on a sha that pre-push already graded, and fails every time | C | ~18 runner-h/wk with no signal: 45 of 45 runs failed from 11-01 to 11-14, mean 46 min (bar-11). The `spawn budget` leg reads `check-wiring measured 47 · ceiling 45`. githooks-6's ~13 runner-h/wk covers push runs only and is inside this figure | gov | Make the spawn-budget ceilings node-relative or exclude that leg on CI (`memory/project/fork-ceilings.txt`, `.github/workflows/remote-ci.yml:103-136`). Then let a green CI stand for one local full bar | S-M | CI stops grading fork counts calibrated on node a |
| 2 | bar-1, bar-2, contention-1, contention-2 | A one-slot host turnstile serialises bars, while pass bars, suites and the preamble bypass it | C (contention-1/-2 P) | 7-9 h/wk of contended bar wall (bar-1) + ≥4 h/wk of queue (bar-2). Week 46 measured 7.2 h of queue (contention-1). Every leg cost below is inflated by this | gov | One host leg-slot pool that every gate entry takes, including pass bars (`tools/run-gates/pass-legs.sh@02af8ab9:333` sets `GATE_TURNSTILE=0`). The cheapest first step is for pass-legs to take `--hold` (`tools/run-gates/run-gates.sh@bfc3ad49:121-124`) | M | Pass-leg latency rises. Serial was measured faster than concurrent (`tools/run-gates/run-gates.sh@bfc3ad49:1588-1592`), so set the width by measurement |
| 3 | pipeline-1, pipeline-3 | `--dispatch`, `--audit` and `--check-commit` walk git for every key, terminal keys included, before reading the trailer that usually ends the check | C | 8-15 h/wk. dOrderedCharter accounts for 18.9 of the 25.9 dispatch-hours and 7.1 of the 8.2 audit-hours. pipeline-3's ~5 h/wk (65% of run commits carry `Pass: none`) is inside this figure | gov | Test terminal/deferred (`tools/unattended/unattended.sh@eb567029:14200-14208`) before `check_pass_open` (`:14199`). Test `Pass: none` (`:14311`) before building rows (`:14301-14310`). Later, one `git log` walk into a cache | S, M for the cache | Nothing, provided a terminal key never holds an open pass. The measurement found 0 open over 89 closed keys |
| 4 | githooks-1, records-1, records-2, spawns-2 | A one-file records commit re-renders the whole build index in pre-commit | C (spawns-2 P) | 6.6-6.8 h/wk: 2268-2272 of ~2545 memory commits force the render, at 46-54 s each (githooks-1, records-1). records-2's spec-commit double render (1.6-2.9 h/wk) overlaps this figure and is not added | gov | `--write` records an input digest, and `--check --staged` skips on a match (githooks-1). The push boundary renders in full. Do not use records-1's alternative of rendering only the staged builds: it misses cross-build roster moves | M | A records commit no longer proves the index is current at commit time. The push bar still does |
| 5 | records-4, ceremony-4 | A unit owes about 3 records commits per product commit, and 81% of commits touch no product code | P | ~8 h/wk of commit wall (records-4, corrected from 13). Most of it is #4, #13 and #30's hook time; the increment beyond them is unmeasured | gov | Two records commits per unit (open, close), with status flips riding the work commits. scratch-guard reads the spec from the working tree, so the separate INPROGRESS commit is a method rule, not a hook rule (ceremony-4) | M | A coarser audit trail per pass | PINNED 2026-11-15
| 6 | bar-4, githooks-4, contention-6 | A landing pays two full bars because the pushed tree never equals the graded one | C (githooks-4, contention-6 P) | ~4.5-5 h/wk (githooks-4). 201 bars for ~40 landings (bar-4). `covered` fired on 0 of 40 lander pushes. The cited cause conflicts with `LANDER_MODE="in-place"` (`tools/unattended/unattended.sh@eb567029:750-754`), and the real cause is not established | gov | Run `--prepare` before the close's bar, so the close grades the merged tree and the push reads `covered`. Reuse leg verdicts whose declared `reads` did not move across a reconcile (contention-6) | M | The close grades a tree that can still move before the push. Leg reuse is only as sound as each leg's `reads` |
| 7 | adopters-2, suites-5 | The adopter bar runs gov's own hook and lander self-tests as repo-subject legs | C (suites-5 P) | ~5.2 slot-h/wk, derived: ~1374 slot-s per forced-full run x (3.5 incms + 10 nicocares) runs/wk. It runs only on forced-full bars, so it is inside #8 | adopters | Take gov `894952cb6` (2026-10-09). Dedupe emitted legs by argv as well as by name (`tools/govkit/govkit.py@37f075e4:4268-4275`) | S (update) | Adopters stop testing gov files they do not edit (`WIRE-INTO-PROJECT.md:936-937`) |
| 8 | adopters-3 | A 10-commit lag bound forces a full bar on about half of adopter landings | C | ~3.5 forced-full bars/wk at incms (22 of 43 landings) and ~10/wk at nicocares (59 of 118). The per-bar cost was not measured. The skeptic ranks it the largest adopter item | adopters | Take gov `89c20a6a7` + `a01f7ed90` (the bound counts first-parent landings) | S (update) | None beyond the update's churn |
| 9 | bar-3, legs-7, suites-1 | The govkit acceptance matrix, a deployer self-test, rides the per-push bar and is its longest leg | C (legs-7 P) | ~4.5 leg-h/wk: 16,356 leg-s in 12 of 28 runs over 7 days (suites-1). It is the longest leg in 13 of 20 recent runs, with leg-sum/wall at 1.9-5.9 (bar-3) | gov | One leg per repo shape, and `fork_gov` (`tools/govkit/selftest.py@866a0710:12162`) in place of the full clone (`tools/govkit/matrix.py@8bb81dbe:976`). Do not hold it: no GATE_SELFTESTS bar has run since 2026-10-15, so a held leg never runs | M | The leg count rises. Its guard is narrower than what it reads (legs-7), a correctness gap to close at the same time |
| 10 | suites-4, legs-5, legs-6, bar-10, spawns-7 | Repo-subject suites and fixture-only legs run on every bar, kept there by one arm or by having no guard | C (legs-5, bar-10, spawns-7 P) | ~3.9 leg-h/wk (14k leg-s/wk, suites-4). legs-6's ~0.5 leg-h/wk of wasted first attempts is inside #13 | gov | Split each repo-reading arm (`tools/memory-tree/transition-audit.test.sh@6b5b736b:12-16`, `.githooks/straggler-guard.test.sh@9a59dd9e:15`) into its own leg, and guard the rest. Re-filing them to `selftests` means they never run (bar-10) | M | Guarded legs skip on bars whose diff misses their paths |
| 11 | records-7, spawns-11 | Full memory hygiene re-grades the 12k-file tree in about 12 processes on every bar, re-loading one corpus four times | C | ~3 leg-h/wk (10,777 leg-s over 13 runs, records-7) | gov | A per-check memo keyed on blob sha, and one shared corpus read (`tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1497, :1597, :1944, :1985`) | L (finder) | A check that trusts a cache entry instead of recomputing |
| 12 | sessionhooks-1, pipeline-5 | stop-guard spawns `--liveness` before reading `background_tasks`, which decides about 90% of Stops | C | 2.2-3.4 h/wk of wall (sessionhooks-1); ~5.6 h/wk of driver CPU (pipeline-5). 5,492 of 5,653 bound Stops had background tasks | gov | Test `background_tasks` and the terminal phase before `runLiveness` (`tools/unattended/stop-guard.js@44860d32:221-224`, read at `:151`). Leases above 1 per session do occur, so drop the comment at `:219` | S | None: the cheap allows already decide those Stops |
| 13 | bar-6, bar-7, contention-4 | Per-leg ceilings fire on contention, not hangs, so each fire costs a ceiling plus a solo retry and the ceilings keep getting raised | C (bar-7, contention-4 P) | ~2.8 leg-h/wk of wasted first attempts (bar-6). Week 46 had 48 retries. 11 ceiling commits since 10-20 (contention-4). Routed commits went 510→760→3540 (bar-7) | gov | Detect hangs by idle CPU and keep the whole-run wall as the bound. Require a spawn count before any raise | M | A slow but progressing leg runs until the whole-run wall |
| 14 | githooks-2, records-3, legs-3 | Carries coverage is derived twice per staged commit, the second time grading 0 specs | C (legs-3 P) | 2.1-2.8 h/wk (githooks-2, ~15 s each; records-3 ~2 h/wk is the same cost). In the bar, 10-20 min/wk (legs-3) | gov | Admit `--with-verdicts` beside `--staged` (`tools/memory-tree/gen_build_index.py@5a0864b8:8847-8852`, `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1496`), and memoise `read_carries_coverage` per process (`tools/memory-tree/gen_build_index.py@5a0864b8:2748, :2967`). The flag alone recovers little (records-3) | S-M | None if the memo is exact | PINNED 2026-11-15
| 15 | legs-4 | The "instruction edits" leg runs the whole tags check inside itself, so every bar pays for tags twice | C | ~2 leg-h/wk duplicated + 19 timeouts | gov | Drop the embedded `run_tag_check` call (`tools/playbook/instructions_edit.py@57e11a29:526`); the tags leg runs the same verb | S | A standalone `instructions_edit.py` run no longer grades tags |
| 16 | adopters-6, githooks-7 | Every adopter records commit pays a hygiene `--staged` run plus a whole index render | C (githooks-7 P) | ~85 min/wk at incms and ~65 at nicocares, ~2.5 h/wk together (adopters-6). The render re-timed at 8.9 s / 4.5 s. nicocares hooks were not found at the cited path (githooks-7) | adopters | Take gov `a55426071` (staged render skip) | S (update) | Same as #4 |
| 17 | legs-1, records-6 | "routed commits" runs a report-only deviation join, one whole-history pickaxe per row | C | 1.2-1.6 leg-h/wk, plus its timeouts (records-6, legs-1). An armed join that measures nothing can still exit 2 | gov | One `git log -p` pass in place of per-row pickaxes (records-6; memoising per row buys nothing). Alternatively, take the join out of the leg (`tools/memory-tree/routed_commits.py@5e29003b:531`) | M (S to drop) | Dropping it loses the join's report and its exit-2 path |
| 18 | bar-9 | A ~130 s `regen.py --check` preamble runs before every bar, longer than a pass bar's own legs | C | ~1.5 h/wk (118 s regen) | gov | Skip it in pass bars (`tools/run-gates/run-gates.sh@bfc3ad49:1560-1580`), or check only outputs whose inputs moved | S / M | Pass bars stop catching a stale generated file. The close bar still catches it | PINNED 2026-11-15
| 19 | spawns-5 | `--liveness` costs about 93 forks | P | ~1 h/wk from a batched `stat` (~0.75 s per call). The remote resolver runs once per call, not 6 times | gov | Batch the per-path `stat` (`tools/unattended/unattended.sh@eb567029:8620`) | S | None |
| 20 | legs-2, spawns-4 | pass-order and brief-recorded re-read every build's README and RUN.md, and spend 4-6 spawns per README on a date cutoff | C | ~0.8 leg-h/wk saveable (legs-2), of which the cutoff is 30-80 s per run (~1k spawns, spawns-4) | gov | A bash string compare in place of `printf \| sort -C` (`tools/unattended/check-brief-recorded.sh@626764ee:368`). One `git cat-file --batch` read. In RANGE mode, grade only builds named in the range | S / M | None for the compare. RANGE scoping skips builds whose ids are absent from the range |
| 21 | derived-2 | A chain packet commits its own HEAD sha and a blob pin, so a 2-line re-render commit follows every pass | C | 0.6-0.9 h/wk now, and falling (60/106/34/23 commits per week) | gov | Drop the volatile lines from the committed bytes (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py@cab3bff1:415, :504-520`) | S | The packet is a pinned instrument, so this needs an owner repin |
| 22 | sessionhooks-3, spawns-1 | procmon-hook spawns git on every Bash call before its throttle check, and its census injects about 1 KB of unactionable rows | C | ~44-50 min/wk quiet (the git spawn alone, spawns-1) | gov | Call `checkThrottled` (`tools/process-monitor/procmon-hook.js@293e9e0d:110`) before the git spawn (`:79`, reached from `:105`). Resolve the common dir with fs, as `tools/memory-recall/recall-opened.js@17e45cf9:131-136` does | S | None | PINNED 2026-11-15
| 23 | records-8 | The index renderer is O(builds x tracked files) pure Python with no parse cache | C | ~45 min/wk (grouping 3.0 s, not 8.2 s), inside #4 | gov | Group by slug once (`tools/memory-tree/gen_build_index.py@5a0864b8:1199-1200, :1211-1212`) | S (finder) | None |
| 24 | derived-1 | The recall index is 402 MB per worktree under a 512 MB budget, so a query in a new tree or after a commit rebuilds it from scratch | C | ~35 min/wk (build 32.5 s, not 96 s) | gov | Stopgap: raise `RECALL_CACHE_BUDGET_MB` (`.memory-tree.conf:663`). Real fix: a content-keyed store in the common dir | S / M | Disk use | PINNED 2026-11-15
| 25 | derived-3 | The kickoff manifest watches the hottest files, forcing re-stamp commits | P | 15-30 min/wk (7-10 re-stamps) | gov | Drop `tools/gate-legs.json` and `run-gates.sh` from the watch list. Accept merges whose watched changes came from stamped parents | S | The kickoff no longer re-reads those two files after they change |
| 26 | derived-7 | reuse_lookup rebuilds the whole-tree reference index on every call | C | ~22 min/wk (6.5 s per lookup, ~225 lookups/wk) | gov | Persist the index keyed by tree id + dirty digest (`tools/codebase-map/reuse_lookup.py@d149e19f:895-912`, `tools/codebase-map/map_lib.py@8ce0356d:920-950`) | M | None if the key is complete |
| 27 | sessionhooks-2, ceremony-11 | format-guard blocks a turn end to make the model re-type a line the hook has already derived | P | ~14 min/wk + ~107k chars. The 86% share is unverifiable | gov | Allow the Stop and append the derived lines when they are the only defect (`tools/hooks/format-guard.js@90a3f894:700-713`) | S-M | The model no longer types its own owed line |
| 28 | sessionhooks-4, spawns-6, derived-4 | SessionStart re-verifies the whole wiring and writes the card | C (derived-4 P) | ~13 min/wk + a tail. The two hook groups run in parallel, so the cost is max(card 25.4 s, wiring 17.5 s). p90 is 2-3 min, and 6 runs were cancelled at 600 s | gov | Stamp the last clean verdict keyed on wiring-file hashes. Move the straggler arm (6.5 s) to the bar | M | A session trusts a stamp for unchanged wiring | PINNED 2026-11-15
| 29 | githooks-5 | The straggler guard re-answers a settled migration on every commit | P | 5-15 min/wk (1.77 s under load) | gov | Short-circuit when HEAD's conf reads `BACKLOG_MODE=builds` (`.githooks/straggler-guard.sh@56c0452c:194-287`) | S | None after the flip |
| 30 | spawns-9, githooks-3 | A fixed 4-5 s pre-commit floor: `git diff --cached` 5 times and `resolve_python` 3 times | C (githooks-3 P) | 4-6 min/wk (spawns-9). githooks-3's ~7.9 h/wk is about 95% #4, #14 and #29, so it is not added | gov | One staged diff and one python resolution in `.githooks/pre-commit` (`:204/:220, :228, :265, :274, :298`; `:243, :304`). Print only non-ok lines | S | None |
| 31 | derived-5 | `transition_audit.read_modes` parses `.memory-tree.conf` once per commit | C | ~6 min/wk | gov | Memoise per blob (`tools/memory-tree/transition_audit.py@419c2700:364-381`) | S | None |
| 32 | spawns-8 | The Python launcher is re-resolved through the WindowsApps alias in every bash leg | C | Small: ~2 min per `check-unattended.test.sh` run | gov | Export the resolved python from `tools/run-gates/run-gates.sh@bfc3ad49:338`, and keep `GOV_PYTHON` through `.githooks/pre-push:535` | S | None |
| 33 | pipeline-2 | `--dispatch` runs the whole-tree spec-token checker | P | <1 h/wk now | gov | Largely fixed by `4fed38fe1` | — | — |
| 34 | adopters-11 | Every adopter Bash call starts three node hooks | P | ~0.35 s per Bash call when quiet (the finder figure was 2x too high). Weekly volume not measured | adopters | Same class as #22 | S | None |
| 35 | ceremony-9 | Fixed floor for a 10-line fix: 12 commits, 17 agents, ~3 bars, 5h57m | C | Per unit, 5h57m vs 28 min of building, including a 52-min owner ruling and a reconcile | gov | A declared Tier-1 fast lane: micro-spec and code in one commit, self-review, pass legs, then the lander | L | Fewer reviewers on low-risk changes | PINNED 2026-11-15
| 36 | ceremony-5 | Every MEDIUM and LOW finding is promoted to a new unit, never folded | C | Per instance, ~1h19m and 441/470-line repair specs (aTrimmedWait units 8, 9) | gov | Promote only BLOCKER/HIGH and fold the minors | M | Reverses the owner ruling at `BUILD-METHOD.md:144` (DIFF, 2026-10-04) |
| 37 | bar-8, contention-5 | No fail-fast, and red bars hold most of the single slot | C | Week 46: 35 of 61 bars red, 20.5 of 32.0 bar-hours. 117 of 201 bars red overall, with the first red at 0.26 of the wall. The saving is below the finder's figure (median 2 failed legs) | gov | Opt-in `GATE_FAIL_FAST` for close and plain bars, or cheap records legs first. A green pass-legs record gate catches less than claimed, because tags, instruction edits and routed commits are not pass legs | M | A fail-fast bar reports fewer reds per run |
| 38 | ceremony-7, pipeline-8 | Record-format legs drive fix passes, and 52 of 80 pass runs come back red | C (pipeline-8 P) | Writing practice causes 28 of 52 pass-run reds, ahead of install-prefix (24) and runbook parity (23). Not costed | gov | Autofix the pin, or warn on records (`tools/playbook/writing_practice.py@c129baaa:206, :241`). Let the builder run `pass-legs.sh` once before committing | S-M | Records can land with an unpinned figure if the leg only warns |
| 39 | adopters-4, adopters-10 | Gov's record legs and install-integrity checks have no guard and run on every adopter push | C (adopters-10 P) | ~880 slot-s per nicocares push (10-20). 14 unguarded legs, a small share of the wall. Weekly figure not given | adopters | Guard them. Pass-order, brief-recorded, hygiene, marker contracts, drift-audit and playbook validity are still unguarded in gov too | M | Adopters edit settings, hooks and guides, so the guards must cover them (adopters-10) |
| 40 | adopters-9 | Adopter sessions load a 52 KB v3.x charter plus a 25-39 KB CLAUDE.md | C | 78-91 KB, ~20-23k tokens per agent start | adopters | Take the 8,970 B template (`9760fb746`), and trim each CLAUDE.md by hand | S | None | PINNED 2026-11-15
| 41 | ceremony-2, ceremony-1 | Two tier definitions make any kit change Tier-2, so spec authoring outweighs building | P | 1,582 Tier-2 vs 77 Tier-1 since 10-15. Spec lines are 498k vs 133k for product. The token split was not re-measured | gov | One tier definition (`TEMPLATE-SPEC.md:386-390` vs `SESSION-KICKOFF.md:122-126`). A behaviour-preserving change with a verdict-equality fixture is Tier-1 | M | Fewer multi-agent reviews |
| 42 | ceremony-6 | An unattended close owes the full multi-agent review whatever the tier | P | Small today, because Tier-1 is rare. 12-13 agents per review fan-out | gov | The close reads the tier (`tools/unattended/unattended.sh@eb567029:1011, :1201, :11965-12029`). A `light` intensity already exists (`tools/workflows/tier2-review.js@bf4613bb:306-313`) | S-M | A self-review stands in for a fan-out on Tier-1 |
| 43 | ceremony-8 | A role agent and a committed prompt record are used to paste an owner's one-word answer into a spec | P | 31 prompt records / 2,646 lines (the finder figure was too high) | gov | Apply mechanical record edits inline | S | Bends the roles rule at `AGENTS.md:120` for mechanical edits | PINNED 2026-11-15
| 44 | ceremony-3 | The main loop carries a whole build in one context | P | 367 turns, 146M context tokens, mostly cache (the finder figure was 2x too high) | gov | Do per-unit bookkeeping inside `unattended-unit.js` and reset between units | M | Less cross-unit memory in the main loop |
| 45 | pipeline-6 | `--close` grades the full bar first and reruns all of it on retry | P | 19 closes / 15.6 h over 7 days | gov | Cheap DOD items first (`tools/unattended/unattended.sh@eb567029:1011`) | S-M | Re-running only red legs conflicts with the purpose of the `GATE_REUSE` scrub (`:11357-11363`) |
| 46 | pipeline-4 | The 10-minute idle-wake cron runs a model turn plus `--resume` and `--audit` while a Workflow runs | P | Its audit hours are #3's walk. Turn tokens are real but unmeasured. `gov-resume-tick` is registered but has been disabled since 2026-10-21 | gov | Skip `--audit` while a task is registered | S | None |
| 47 | pipeline-7 | Units build strictly one at a time | P | Unmeasured. README declared in 32/43 (aNimbleMend) and 95/127 (dOrderedCharter) dispatches | gov | Exempt generated indexes from the overlap test (`tools/unattended/unattended.sh@eb567029:14885-14897`, `.unattended.conf:418`) | M | Concurrent writes to generated files |
| 48 | bar-5, legs-9 | The leg cache keys on the whole-tree fingerprint, so it almost never fires | P | Below the claim. 4 of 201 bars reused any leg. Only marker contracts, spawn budget and tags (~650 s) are guard candidates | gov | Read-keyed reuse (`tools/run-gates/run-gates.sh@bfc3ad49:3274, :3297-3298, :3343-3345`) | M | Reuse is only as sound as `reads` | PINNED 2026-11-15
| 49 | contention-3 | One tag index of 2.2 GB, whose locked writer holds the lock through a cleanup scan | P | Cleanup scans take 5.3 s warm (not 61.4 s). Co-timeouts are real | gov | Move `remove_unheld_rows` to `--gc`, use WAL, and set BUSY_TIMEOUT below the ceiling (`tools/playbook/tag_index.py@46bfe37d:117, :509-520, :666-676`) | M | It competes with #15 to explain the same co-timeouts |
| 50 | records-5 | A generated records table inside every spec turns each new record into a spec revision | P | ~17% of spec revisions (not 39%) | gov | Move the table to the build README | M | Reverses a deliberate choice (TOOL-dFramedEntrypoint-6) |
| 51 | records-9 | Rendered handoff prompts are committed | P | The premise is wrong: handoffs are read after the spawn (`tools/roles/handoff.py@26689d0b:1043-1046`, `tools/memory-tree/deviation_join.py@c793df78:558`) | gov | — | — | — |
| 52 | derived-6 | The pre-commit map gate skips `.sh`-only commits | P | Adding `*.sh` is likely a net slowdown; its value is left-shift | gov | — | — | — |
| 53 | derived-8 | `drift_report.py --check` re-tokenises the lexicon three times per bar | P | Leg median ~176 s | gov | A shared blob-keyed parse cache | M | Its `--check` history write is deliberate (TOOL-aMendedFleet-48) | PINNED 2026-11-15
| 54 | suites-2 | Fixtures copy or clone the whole gov tree, so suite cost grows with memory/ | P | Tracked files went from 4,627 to 12,622 in a month. Fixture cost was not re-measured | gov | Copy only the tool surface; use sparse clones | M | Fixtures see less of a real tree |
| 55 | suites-3, suites-7 | Held suites never run, while agents run suites in sessions outside the cache | P | Remote CI pays for them daily (`remote-ci.yml:40-41, :155-257`). No GATE_SELFTESTS bar has run since 2026-10-15 | gov | The existing `GATE_SELFTESTS=changed` over the run's range. A new flag would re-implement it | S | — |
| 56 | suites-6 | `check-unattended.test.sh` runs the whole checker to grade one check per arm | P | Held suite. `run_scoped` has ~17 callers | gov | Default `run` to `--only` | S-M | — |
| 57 | spawns-3 | The unattended kit gate loops over every RUN file with spawns per iteration | P | Not measured. The leg has been held since `3203e2ac4` | gov | — | — | — |
| 58 | spawns-10 | Remedy check: WSL2 spawns are 27-50x cheaper but reach only the held tier | P | A remedy assessment, not a cost | gov | Rank it after batching | — | — |
| 59 | sessionhooks-5 | agent-cap rule 6 admits no ad-hoc helper | P | ~18 refusals/wk. This review's governed route took ~6 min before the first agent ran, then rendered 17 handoffs of ~3 KB, ~1.5 KB of each the same practices block (synthesis brief). The per-refusal cost rests on one session | gov | Admit a read-only built-in type, or an `--adhoc` render under the git dir (`tools/hooks/agent-cap.js@44d881b5:691-749`) | M | Less provenance on helper spawns | PINNED 2026-11-15
| 60 | adopters-1 | Updates are so large that adopters stop taking them | P | No weekly figure of its own. It is the root cause behind #7, #8, #16 and #40. 899 kit commits, +145k lines since `c83ef509` | adopters | — | L | — |
| 61 | adopters-5 | More than half of adopter commits are governance-only | P | incms 829/1576, nicocares 881/1509 | adopters | — | — | — |
| 62 | adopters-7 | Naming and record-format reds surface only at the close bar | P | Not quantifiable. Subjects: lexicon 48/25, red 68/74 | adopters | — | — | Gov's lexicon guard has the same shape |
| 63 | adopters-8 | Kickoff-manifest re-stamp commits recur in nicocares | P | ~4 small commits/wk | adopters | Same as #25 | S | — |
| 64 | contention-7 | Parked WIP pins state that every index build scans | P | Unmeasured | gov | — | — | — |
| 65 | ceremony-10 | The fixed prefix (charter + MEMORY.md) is ~11.5k tokens per turn | P | Low | gov | Prune MEMORY.md entries that its own text calls fixed | S | — |

## 4. Quick wins

These are S effort, CONFIRMED and decision-preserving, listed by saving.

1. **Driver walks** (#3, pipeline-1, pipeline-3). In `tools/unattended/unattended.sh`, test terminal/deferred at `:14200-14208` before `check_pass_open` at `:14199`. Test `Pass: none` at `:14311` before building rows at `:14301-14310`. Saves 8-15 h/wk.
2. **stop-guard** (#12, sessionhooks-1, pipeline-5). In `tools/unattended/stop-guard.js@44860d32:221-224`, read `background_tasks` (`:151`) and the terminal phase before `runLiveness`. Saves 2.2-3.4 h/wk of wall-clock.
3. **Carries coverage** (#14, githooks-2, records-3). Admit `--with-verdicts` beside `--staged` at `tools/memory-tree/gen_build_index.py@5a0864b8:8847-8852` and `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1496`, and memoise `read_carries_coverage` at `tools/memory-tree/gen_build_index.py@5a0864b8:2748, :2967`. Saves 2.1-2.8 h/wk.
4. **Instruction edits** (#15, legs-4). Drop `run_tag_check` at `tools/playbook/instructions_edit.py@57e11a29:526`. Saves ~2 leg-h/wk and 19 timeouts.
5. **procmon-hook** (#22, sessionhooks-3, spawns-1). Move `checkThrottled` (`tools/process-monitor/procmon-hook.js@293e9e0d:110`) ahead of the git spawn at `:79`, and resolve the common dir with fs. Saves 44-50 min/wk.
6. **Renderer grouping** (#23, records-8). Group by slug once at `tools/memory-tree/gen_build_index.py@5a0864b8:1199-1200, :1211-1212`. Saves ~45 min/wk, inside #4.
7. **Recall budget** (#24, derived-1). Raise `RECALL_CACHE_BUDGET_MB` at `.memory-tree.conf:663` above the 402 MB index. Saves ~35 min/wk and costs disk. PINNED 2026-11-15
8. **brief-recorded cutoff** (#20, spawns-4). Replace `printf | sort -C` at `tools/unattended/check-brief-recorded.sh@626764ee:368` with a bash compare. Saves 30-80 s per run.
9. **transition_audit** (#31, derived-5). Memoise `read_mode` per blob at `tools/memory-tree/transition_audit.py@419c2700:364-381`. Saves ~6 min/wk.
10. **pre-commit floor** (#30, spawns-9). Run one `git diff --cached` and one `resolve_python` in `.githooks/pre-commit` (`:204/:220, :228, :265, :274, :298`; `:243, :304`). Saves 4-6 min/wk.
11. **Python launcher** (#32, spawns-8). Export the resolved python at `tools/run-gates/run-gates.sh@bfc3ad49:338`. The saving is small.

## 5. Structural changes

**CI as a bar that can pass** (#1)
- The change: make spawn budgets node-relative or exclude them on CI. Then let a green CI stand for one local full bar.
- What it trades: CI stops grading fork ceilings calibrated on node a.
- Owner ruling: none known. Open asks TOOL-aNimbleMend-26 and TOOL-aSparedSpawn-26 already cover it.
- Effort is S-M, but it is listed here because it moves CI's verdict.

**Content-keyed caches for whole-tree checks** (#4, #11, #17, #26, #24, #48)
- The change: `--write` stamps an input digest that `--check` accepts, and history legs make one `git log -p` pass.
- What it removes: the class behind the largest share of hook and bar hours.
- What it trades: a check that trusts a stamp instead of recomputing. The push boundary keeps a full run.
- Owner ruling: none.

**Grade the landing tree once** (#6)
- The change: run `--prepare` before the close's bar, and reuse leg verdicts across a reconcile when their declared `reads` did not move.
- What it trades: the close grades a tree that can still move. Reuse depends on `reads` being complete.
- Owner ruling: none.

**One host slot pool, with hang detection in place of wall ceilings** (#2, #13)
- The change: every gate entry, including pass bars and suites, takes a slot. Hang detection replaces wall ceilings, and a ceiling raise requires a spawn count.
- What it trades: pass-leg latency, and a slow leg that runs until the whole-run wall.
- The open question: serial was measured faster than concurrent (contention-1), so the pool width has to be measured, not assumed.

**Tier by risk** (#35, #36, #41, #42, #43, #5)
- The change:
  - One tier definition, with a Tier-1 fast lane.
  - The close reads the tier.
  - Status flips ride the work commits.
  - Mechanical record edits go inline.
  - Minor findings fold.
- What it trades: fewer reviewers and a coarser audit trail on low-risk work.
- Owner rulings it reverses:
  - `memory/guides/BUILD-METHOD.md:144` (owner, DIFF, 2026-10-04: MEDIUM and LOW findings are promoted, never folded).
  - The roles rule at `AGENTS.md:120` as applied to one-word edits.

**File suites by what they read** (#9, #10, #54, #55)
- The change: split out the repo-reading arms, guard the rest, one matrix leg per shape, `fork_gov` in place of clones, and `GATE_SELFTESTS=changed` for the held population.
- Constraint: "hold it in selftests" means it never runs, so holding is not a fix.

**Adopter updates small enough to take** (#60)
- The case for it: four confirmed adopter costs (#7, #8, #16, #40) are already fixed in gov.
- The cost: the last full update was 77 commits / 110k lines (adopters-1). PINNED 2026-11-15

**Fail-fast and cheap legs first** (#37, #38, #45)
- What it trades: fewer reds reported per run.
- Constraint: the `GATE_REUSE` scrub's purpose stands against re-running only the red legs.

## 6. What adopters pay without benefit

**Tests of gov's own files.** The adopter bar runs gov's hook and lander self-tests as repo-subject legs (#7, adopters-2, suites-5). Those legs test files that `WIRE-INTO-PROJECT.md:936-937` says adopters never edit. The cost is ~1374 slot-s per forced-full run. Gov fixed this at `894952cb6`.

**Costs gov already removed.** Adopters still pay four costs that gov has fixed:
- The lag bound forces full bars at ~3.5/wk (incms) and ~10/wk (nicocares) (#8). Fixed at `89c20a6a7` + `a01f7ed90`.
- The staged render costs ~2.5 h/wk (#16). Fixed at `a55426071`.
- The 20-23k-token charter load (#40). Fixed at `9760fb746`.
- The CLAUDE.md files still need a hand trim.

**Partly unprotective.**
- Unguarded record and install legs run on every push, memory-only pushes included (#39).
- Seven argvs run twice in nicocares's bar, because govkit dedupes by name, not by argv (suites-5).

**Of unclear benefit.**
- Three node hooks run per Bash call (#34).
- Kickoff re-stamps run about 4 times a week (#63).
- More than half of adopter commits are governance-only (#61).

The refuted adopter finding (adopters-12) is not a cost: incms already scopes memory-only landings.

## 7. Already fixed or in flight

Do not rebuild these.

**On gov main:**
- `894952cb6`: self-test filing (#7).
- `89c20a6a7` + `a01f7ed90`: first-parent lag count (#8).
- `a55426071`: staged render skip for adopters (#16). In gov itself the skip rarely fires (#4).
- `9760fb746`: 8,970 B charter template (#40). PINNED 2026-11-15
- `3203e2ac4`: unattended kit gate held off automatic bars, TOOL-aShelvedLeg-1 (legs-8 refuted, #57, #39 in part).
- `4fed38fe1`: dispatch spec-token scoping, TOOL-aBriskDeclaration-1 (#33).
- aSwiftRefusal, aSmoothedDispatch and aBatchedPacket: the earlier dispatch costs (evidence brief).

**On `branch/speedups-9c2e63` (aTrimmedWait, tip `057f26ba4`):**
- `b2c96fea3` (TOOL-aTrimmedWait-4): `--write` rewrites only changed bytes (#4, records-2). It does not skip the check, so #4 stands.
- TOOL-aTrimmedWait-2/-3/-4/-8: part of spawns-2 (#4). TOOL-aTrimmedWait-3 adds a render.
- TOOL-aTrimmedWait-2/-3: part of spawns-11 (#11).
- `519bc24db` (TOOL-aTrimmedWait-7): caches handoff parses (part of #27).
- TOOL-aTrimmedWait-6/-9: role-gate refusals (sessionhooks-7, refuted on these grounds).

**Filed asks:**
- Leg guards (#10, #48): the open ask `TOOL-aTimedTurnstile-2`.
- SessionStart (#28): the open ask `TOOL-aBriskPreflight-8`.
- TOOL-aNimbleMend-26 and TOOL-aSparedSpawn-26: CI spawn budget (#1).
- Held suites (#55): `TOOL-dDerivedDocket-32`.
- incms ARCH-aYieldedFork-2: memory-only scoping (adopters-12).

**Existing modes that a fix should use instead of re-implementing:**
- `GATE_SELFTESTS=changed` (#55).
- `light` review intensity (#42).
- The WSL seam `tools/run-gates/run-held-wsl.sh` (#58).

## 8. Gaps

**No grand total.** Wall-hours, concurrent leg-hours, runner-hours, slot-hours and CPU-hours do not add up to one number. No lens measured the overlap between #2's contention and every leg cost it inflates.

**Most of the unit wall is unattributed.** In §2, only building, the owner turn and two bars are measured. About 190 of the 357 minutes are a residual, and orchestration verbs and pass bars were not timed for that unit.

**Token costs are unmeasured.** The token split in #41, the turn tokens in #46 and the context cost in #44 were not re-measured by any skeptic.

**Adopter bar costs rest on two ledger samples** (2026-10-09 and 2026-10-20), and the incms one is load-inflated. The per-bar cost of #8's forced-full bars was not measured.

**The host was not quiet.** The gate skeptic saw the host 6-10x busier than during the find phase. Per-event timings carry that noise, and the evidence brief records a kernel-pool leak precedent on node a.

**The cause behind #6 is unknown.** It is not established why `covered` fired 0 of 40 times. The one cause offered came from a refuted finding (pipeline-10), so it is flagged here and not used.

**The pool width question is open.** Serial runs were measured faster than concurrent ones (contention-1), which leaves the right turnstile width unsettled.

**The skeptic batch headers disagree with their own per-line verdicts.** This report uses the lines.

| Batch | Header | Per-line |
|---|---|---|
| gate | 14 C / 12 P / 1 R | 15 / 11 / 1 |
| hooks | 9 / 10 / 2 | 9 / 7 / 2, 18 lines | PINNED 2026-11-15
| records | 13 / 12 / 0 | 12 / 12 / 0 |
| process | 8 / 17 / 3 | 7 / 19 / 2 |

**The aTrimmedWait unit count does not match the synthesis brief.** The brief says "9 units plus 2 repair units". The findings show only units 8 and 9 as the round-1 repair units (ceremony-5), and do not settle whether there were 9 units or 11. PINNED 2026-11-15

**Effort is mostly this synthesis's estimate.** The skeptic briefs did not carry the finders' effort fields. Only records-2, records-7 and records-8 kept theirs.

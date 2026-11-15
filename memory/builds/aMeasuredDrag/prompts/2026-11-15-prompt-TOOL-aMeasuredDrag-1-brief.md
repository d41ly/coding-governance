# Brief — aMeasuredDrag: the performance review's eleven quick wins

**Serves:** research TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11

## The prompt

> Build quick wins

The owner chose that answer for the question "Start a governed build for the 11 quick wins here?". The quick wins are §4 of `memory/builds/aMeasuredDrag/reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-performance.md`.

## The brief

### Goal
Land the eleven small, confirmed, decision-preserving speed fixes from the 2026-11-15 performance review. Each fix is measured before and after, and no verdict, refusal or printed line moves.

### Items
1. `TOOL-aMeasuredDrag-1` — in `tools/unattended/unattended.sh`, `read_open_passes` (`:14192-14211`) tests a key's terminal or deferred status (`:14200-14208`) BEFORE it calls `check_pass_open` (`:14199`). `check_commit_message` (`:14263-14378`) parses its `Pass:` trailer and returns on `none` (`:14311`) BEFORE it builds rows (`:14301-14310`), and walks only the units the trailer or subject names. Findings pipeline-1 and pipeline-3. Keep the stderr naming of keys that a status skip releases (`:14186`), and keep the `O` amend case for named closed units.
2. `TOOL-aMeasuredDrag-2` — in `tools/unattended/stop-guard.js`, decide the allows that need no driver, `background_tasks > 0` (`:151`) and a terminal lease phase (`tools/unattended/run-lease.js@8a5aa9d7:161`), BEFORE `runLiveness` (`:107-115`, called at `:221-224`). The block/allow decision stays identical for every input. Findings sessionhooks-1 and pipeline-5. Only the sidecar line's phase and verdict fields may read `unknown` for those stops.
3. `TOOL-aMeasuredDrag-3` — in `tools/memory-tree/gen_build_index.py`, `read_carries_coverage` (`:1990`; called at `:2748` and `:2967`) is derived once per process. Under `--staged`, `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1496` passes `--with-verdicts` too (the refusal at `tools/memory-tree/gen_build_index.py@5a0864b8:8847-8852` lifted), so checks 29 and 30 read check 9's section and spawn no second generator. Findings githooks-2 and records-3. When a staged render skips, each verb still prints its held line. The memo must key on the same resolve stub the selftest arms inject (`:4872-4906`).
4. `TOOL-aMeasuredDrag-4` — `tools/playbook/instructions_edit.py@57e11a29:526` stops calling `run_tag_check` (`:425-433`) inside the `check` verb when it runs as the bar leg, because the separate `tags (the resolver's checks)` leg already runs the same `gov_tag` check verb. Finding legs-4. The tags leg must stay unguarded on every bar that runs instruction edits. Say what a caller running `instructions_edit check` alone loses.
5. `TOOL-aMeasuredDrag-5` — `tools/process-monitor/procmon-hook.js` decides its throttle (`checkThrottled`, `:110`) before any spawn. It resolves the git common dir by reading files (the worktree `.git` file, then `gitdir`, then `commondir`), as `tools/memory-recall/recall-opened.js` `gitCommonDir` does, instead of `execFileSync('git', …)` at `:79`. Findings sessionhooks-3 and spawns-1. The throttle stamp stays shared across worktrees.
6. `TOOL-aMeasuredDrag-6` — `tools/memory-tree/gen_build_index.py@5a0864b8:1199-1200` and `:1211-1212` group the tracked list by build slug ONCE, instead of scanning the whole list per build per record kind. Finding records-8. The rendered artifacts stay byte-identical.
7. `TOOL-aMeasuredDrag-7` — raise `RECALL_CACHE_BUDGET_MB` (`.memory-tree.conf:663`, currently 512) above two gov recall indexes (one is about 402 MB), so the two hottest worktrees stop evicting each other. Finding derived-1. Record the disk this costs, and keep the README at `tools/memory-recall/README.md:126` true. Touching `.memory-tree.conf` owes the kickoff-manifest re-stamp in the same commit. PINNED 2026-11-15
8. `TOOL-aMeasuredDrag-8` — `tools/unattended/check-brief-recorded.sh@626764ee:368` compares the README's `opened:` date to the cutoff in the shell (`[[ ]]` after the `:365` shape check), not with `printf | sort -C`. Finding spawns-4. Either move the sibling cutoffs the `:366-367` comment names too, or state why this one differs.
9. `TOOL-aMeasuredDrag-9` — `tools/memory-tree/transition_audit.py@419c2700:364-381` maps each distinct conf blob through `read_mode` (`:151-169`) once, then each commit through that map. Finding derived-5. Verdicts are byte-identical, because `read_mode` is a pure function of the blob text.
10. `TOOL-aMeasuredDrag-10` — `.githooks/pre-commit` reads the staged name list once (`git diff --cached` now runs at `:204/:220`, `:228`, `:265`, `:274`, `:298`) and resolves python once (`:210`, `:243`, `:304`). Each leg keeps its own filter (`--diff-filter=ACMR` at `:228`, `--no-renames` through `with_hook_index` at `:204/:220`). Finding spawns-9. Open ask TOOL-aTrimmedHook-8 targets this hook.
11. `TOOL-aMeasuredDrag-11` — `tools/run-gates/run-gates.sh@bfc3ad49:338` exports the python it resolved, under a runner-set variable, to its legs, so `tools/lib/resolve-python.sh@9ec71b5b:36-43` echoes it without a probe. Finding spawns-8. `.githooks/pre-push:530-535` drops `GOV_PYTHON` on purpose (TOOL-aRepatriatedFork-49), so an inherited value must never be admitted.

### Acceptance
Per unit:
- An equality observation that the changed code's output (stdout, stderr, exit status, written bytes) over the real tree, or over the unit's existing fixtures, is identical before and after. The command is named in the spec.
- A timed before and after of the changed call, each beside a spawn baseline (10 x `/usr/bin/true`).

### Gates
The pass legs (`bash tools/run-gates/pass-legs.sh`), run by the main loop after each unit commit. The full merge bar once, at the close.

### Non-goals
- Every structural change the review lists in its §5: content-keyed caches, the turnstile pool, the tier rule, CI repair, fail-fast, and adopter updates.
- Anything that moves a verdict, a refusal or a printed line.
- The build folders and branches of aTrimmedWait (`branch/speedups-9c2e63`), aLightenedLoop (`branch/alightenedloop-eb7b8b`) and the live run dDeclaredLoop.
- The adopter repositories.
- ANY SELF-TEST SUITE OR BAR INSIDE A PASS, a sliced suite included. A pass verifies with a probe or a fixture of its own code.

### Limitations
- Three unlanded branches edit `unattended.sh`, `stop-guard.js`, `gen_build_index.py`, `check-memory-hygiene.sh` and `.githooks/pre-commit`. Keep each change to the lines it needs, so that their landings reconcile with this one.
- Every spec line that states a figure with a unit carries the word PINNED or a commit sha on that line.
- A spec's acceptance section cites no path that its own unit has not built yet.

### Reuse
- Each item's seam is the function its finding cites, edited in place. Item 5 reuses `gitCommonDir` in `tools/memory-recall/recall-opened.js`.
- Recall returned TOOL-dDerivedDocket-61 (one lease record) and TOOL-aBriskPreflight-9. The asks probe named TOOL-aTrimmedHook-8 for item 10.
- Recall terms: pass_commit check_pass_open liveness stop-guard staged render carries coverage memo throttle procmon recall budget.
- The evidence for every item is in the review record and its research records under `memory/builds/aMeasuredDrag/build/`: `...-findings-*.md` holds the findings and `...-verdicts.md` the skeptics' corrected costs and fix risks.

## Drawn from the session

> Build quick wins
— owner, the turn after the review's wrap-up

> All 11 now
— owner, answer to "Which quick wins go in this build?"

> Unattended (Recommended)
— owner, answer to "How should this build run?"

> No audit
— owner, answer to "Declare spec-audit: for this build?"

## Owner confirmation

Asked: Start a governed build for the 11 quick wins here?
Answer: Build quick wins

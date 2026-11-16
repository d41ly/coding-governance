# Brief — aHastenedSweep: the hygiene suite's assertion floor pinned to the count the close measured

**Serves:** research TOOL-aHastenedSweep-7

## The prompt

> Background (from the session that started this one):
> coding-governance dogfoods its own governance kits, and the memory-hygiene runner `tools/memory-tree/check-memory-hygiene.sh` has become a major build cost: `about 800–1100 s` per full bar, `about 95 s` per records commit, and hours of spec-writer reruns. An analysis session on 2026-11-15 measured, on node a (Windows, Git-Bash, `about 0.75 s` per spawn), that check 25's by-name pass alone takes `about 347 s`, and that `gotchas.py` and `corpus_ids.py` each rescan the whole tree once per item, through hot spots that can be memoized exactly. The owner's constraint is unchanged verdicts: no weakened check, no skipped population, no exemption. Never touch the live unattended run's worktree `unattended-declared-loop-d56bf0`, its branch or its RUN.md.

> Task:
> Open a build, through `/session-kickoff` and then this repo's normal build flow, that lands the exact-verdict hygiene speed-ups R1–R4 from the analysis at `C:\Users\daily-agent\AppData\Local\Claude-Data\claude_pzs8sxrjxfjjc\side-session-notes\local_7a2e6d9c-5cfa-46ca-baeb-d00446155090\hygiene-perf-analysis.md`. Read that report first: it holds the measurements, each change's invariant, and the red case for each.

> Units, one per change:
> 1. **R1, check 25.** In `tools/memory-tree/check-memory-hygiene.sh` (~`:3100`, check 25's by-name END loop), add an `index(ln, pl[i]) &&` guard ahead of `test_whole_token`. Measured `347–507 s → 41.7 s`, with `cmp`-identical output.
> 2. **R2, `gotchas.py`.** In `selectable()` in `tools/memory-tree/gotchas.py`, compute each path's basename once per process and the anchor's basename once per call. In `tools/memory-tree/corpus_ids.py`, compute `_roots(tracked_set)` once per walk, not once per citation at `:569`. Measured `227 s → 34.5 s`, output identical.
> 3. **R3, `corpus_ids.py`.** When the hygiene shell launches `corpus_ids.py --check`, hand down the `INDEX_SET` the shell already computed (`:1176`), and only when checks 1–5 recorded no failure. This replaces `ask_shell("--print-index-set")` re-entering the shell. The standalone CLI keeps today's path.
> 4. **R4, one shared walk.** Run checks 13–16 and 17–19 in one Python process with one memoized, frozen `walk()`, keeping each check's output and exit mapping.

> Every unit must:
> - keep verdicts byte-identical;
> - carry an A/B parity check on the live tree (shipped against changed, `cmp`-equal);
> - keep the report's named red cases red: tFixture-208/209/216 and the word-boundary fixtures in `check-memory-hygiene.test.sh`, the `gotchas.py --selftest` dead-anchor and `selectable` arms, and `corpus_ids`' "answered with findings" refusal.

> Done means:
> - each unit is CLOSED with its parity evidence recorded;
> - the full `memory hygiene` leg is re-measured on node a, against `805–1093 s` in today's bar ledgers;
> - landing goes through `bash tools/push-main.sh` only on the owner's ask.

> R5 (commit recipe and the render stamp) and the spec-writer prompt scope are owner decisions. Leave them out unless the owner says otherwise.

The task came from the session that started this one, on the owner's request, and is quoted whole except its pointer to a shared notes folder; its figures are set in code spans, the only change, so the pinned-facts arm reads them as quoted.

## The brief

### Goal
The hygiene suite's assertion floor equals the count a full run prints, so stranding any block of arms reds the floor. Today it sits below the count, and the floor arm `TOOL-aHastenedSweep-6` added cannot go red.

### Items
1. `TOOL-aHastenedSweep-7`, order 6, a Tier-1 unit closing the gap the close found in `TOOL-aHastenedSweep-6`'s floor arm: `FLOOR_ASSERTIONS` in `tools/memory-tree/check-memory-hygiene.test.sh` moves from 719 to the count the suite printed at `0c1935569`, `PASS (742 assertions)` (PINNED, 2026-11-16, node a), with a RAISED line that says the floor sat below the count before this build began and that this unit pins it to the measured count; unit 6's spec is CLOSED and stays frozen, so this unit's spec carries the correction [planned TOOL-aHastenedSweep-7]

### Acceptance
- `grep -cx` for the new floor line prints 1, and its RAISED line names `TOOL-aHastenedSweep-7`.
- The main loop observes the floor arm at the close: the full suite prints `PASS` with a count equal to the floor, and with unit 3's block wrapped in `if false; then … fi` the floor's `FAIL executed` line appears.

### Gates
The floor arm, observed by the main loop at the close; the merge bar once at the close, without the self-test suites.

### Non-goals
- Any other arm, assertion or suite change.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS. The pass runs `bash -n` and the grep; the main loop observes the floor red and green at the close.
- A pass commit without its acceptance ledger at `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-7-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED.

### Limitations
- In records, name a hygiene check by what it checks, never by its number, and put PINNED on any line stating a figure with a unit.
- The floor's comparison is `n + n_skip` against the floor; a node that skips arms counts them in `n_skip`, so the pinned count holds there too.

### Reuse
- The floor line and its RAISED history in `tools/memory-tree/check-memory-hygiene.test.sh`.
- Recall terms used: `hygiene check 25 by-name readers test_whole_token corpus_ids walk gotchas selectable print-index-set INDEX_SET ask_shell`.

## Drawn from the session

> PASS (742 assertions)
— agent, the main loop's full hygiene suite run at `0c1935569`, 2026-11-16

## Owner confirmation

Asked: not asked. An unattended run adopts a beneficial discovery into the running build at once, by the build method's M10, with no owner turn.
Answer: none — the mandate committed at `f25308f01` covers it.

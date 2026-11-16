# Brief — aHastenedSweep: the closing review's round-1 items, promoted to two units

**Serves:** research TOOL-aHastenedSweep-5 TOOL-aHastenedSweep-6

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
Close every confirmed item of the closing review's round 1, `memory/builds/aHastenedSweep/reviews/2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md`, by severity as `doc.build-method#m8-closing-the-build` disposes them: its HIGH item becomes a unit whose mechanism closes it, and its MEDIUM and LOW items are batched into one unit. Every verdict stays byte-identical, as the build's first brief requires.

### Items
Two units, built in sequence because each one's CLOSED flip re-renders the build README, which `--dispatch` refuses to two open siblings. Read the review report whole first; each item below names its finding by the report's label, and the report's Fix text (the skeptic's corrected fix where it gives one) is the starting design, to be verified against the code at the build's tip.

1. `TOOL-aHastenedSweep-5`, order 4, closing H1: the memory-tree kit contract names every `gotchas.py` verb the hygiene shell launches. In `tools/memory-tree/kit.toml`, the `memory-tree/gotchas` contract gains clauses whose `consumer` is `check-memory-hygiene.sh`, one per verb the shell calls, `--check` and `--check-with-ids`, as `imports` or as a read-only probe whose `expect` matches the output shape. The spec verifies with the govkit verbs that grade contract clauses that an adopter-owned `gotchas.py` predating `--check-with-ids` is named as missing the clause. The shell keeps unit 4's loud red on a frame that does not split; no silent two-launch fallback [planned TOOL-aHastenedSweep-5]
2. `TOOL-aHastenedSweep-6`, order 5, consuming from unit 5 only by order, closing M1, M2, M3, M4, L1, L2, L3 and L4: every arm this build added can go red on the regression it names, and every comment and map line describes the one-process launch. M1: `FLOOR_ASSERTIONS` raised to cover unit 3's five arms, unit 4's two and this unit's new ones, with a RAISED line naming the three units. M2: two one-red `--offenders` arms, one per side, each going red with the two rc reads swapped in the split. M3: an arm driving the frame-failure fallback through a `GOV_PYTHON` wrapper that answers only `--check-with-ids` with an unframed line, keyed loud under the 13-16 offender key. M4 and L2: the `gotchas.py --selftest` with-ids arm gains a verb that writes stderr and a verb that raises inside the per-verb loop, asserting each frame byte for byte. L1: the docstring and comment of `cmd_check_with_ids` say the crash path's traceback is the in-process one, in this process's stream encoding, placed ahead of stdout. L3: the test-file exemption note, the `corpus_ids.py` docstring and the shell comment name the hand-down on both launches. L4: the dossier bullet in `memory/map/features/memory-tree-hygiene.md` places the hand-down on the unscoped run's `gotchas.py --check-with-ids` launch. Spec 4 is CLOSED and stays frozen; this unit's spec carries the corrections [planned TOOL-aHastenedSweep-6]

### Acceptance
- Unit 5: a fixture target whose `gotchas.py` predates `--check-with-ids` is named by govkit as missing the new clause, and gov's own tree passes the contract.
- Unit 6: each new or corrected arm is green at the tip and red under the staged break its spec names; the hygiene suite prints `PASS` with an assertion count equal to the raised floor.
- Every new arm is observed red, then green, by the main loop at the close, and the live-tree A/B of the whole hygiene run stays `cmp`-identical.

### Gates
The new arms, run directly by the main loop at the close; `check-arms` over the hygiene suite; the govkit contract checks, the lexicon and the codebase-map legs the change owes; the merge bar once at the close, without the self-test suites.

### Non-goals
- The report's left-shift gates (a private-verb contract leg, a floor-count check, a one-red-arm rule, a Red-when staged-break rule, a crash-path identity row, an Observed-by rule, a folded-launch grep, a non-goal map grep) are not built here: each spec lists them for the main loop to file as asks.
- Any kit version move on the branch: the lander mints it.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS, A SLICED SUITE INCLUDED. A pass runs only direct checks: `bash -n`, `python -m py_compile`, `check-arms`, the lexicon, the changed code invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. New arms are written and checked with `bash -n`; the main loop observes each red and then green at the close.
- A pass commit without its acceptance ledger: each pass commit carries `memory/builds/aHastenedSweep/build/2026-11-16-build-TOOL-aHastenedSweep-<n>-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aHastenedSweep-<n>` block naming each criterion with the backticked token the criterion itself spells.
- An edit after the commit that sets a spec CLOSED: every edit lands first, and the status flip is the last change of the pass.

### Limitations
- Verdicts byte-identical on the live tree and on every existing fixture.
- In records, name a hygiene check by what it checks, never by its number, and put PINNED on any line stating a figure with a unit.
- Verify every line the report cites against the build's tip before relying on it; the report pins `cf64f39df`.

### Reuse
- `tools/memory-tree/kit.toml`'s existing `[[contract.clause]]` shapes (`probe` with `expect`, and `imports`), graded by the govkit kit.
- The suite's `_b1` fixture and its `--offenders` arms from units 3 and 4; `load_counted` in the `gotchas.py` selftest.
- Recall terms used: `hygiene check 25 by-name readers test_whole_token corpus_ids walk gotchas selectable print-index-set INDEX_SET ask_shell`.

## Drawn from the session

> **Verdict: CLEAN WITH FIXES.** There are 9 items from 10 confirmed findings, with ids 1 and 7 merged as one defect: the assertion floor sits five below unit 3's arms.
— agent, the closing review's synthesis, 2026-11-16, round 1

## Owner confirmation

Asked: not asked. An unattended run promotes a closing review's confirmed findings by the build method's M8, with no owner turn.
Answer: none — the mandate committed at `f25308f01` covers it.

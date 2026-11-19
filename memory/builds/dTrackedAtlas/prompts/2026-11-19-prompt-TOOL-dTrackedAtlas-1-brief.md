# Brief — dTrackedAtlas: the Closed Loop Atlas derives the actual state of the project and the chain

**Serves:** research TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4

The prompt arrived as a file from the session that started this one, on the owner's instruction:
`C:/Users/d41ly/AppData/Local/Temp/claude/abaae6cd36b7dece/bc821d4c-b305-40e3-bf2f-7dc1519c57f1/scratchpad/atlas-fix-prompt.md`.
Its bytes are quoted whole below, because that scratchpad is not durable, but for two editorial insertions in square
brackets, `[PINNED]`, which mark the measured figures as the writing-practice gate requires.

## The prompt

> # Prompt: the Closed Loop Atlas always shows the project's and the chain's actual state
>
> ## The owner's words (2026-11-19, verbatim)
>
> > Gather all the relevant details are launch an unattended atlas fix to always account for the actual
> > state of the project+build in a handoff session
>
> The owner asked the day before: "When was the Atlas last updated, does it still represent the actual state of
> the project?" The answer is below; this run fixes what it found.
>
> ## What was measured (node d, origin/main 9e21ac760, 2026-11-18/19)
>
> - **The page:** `C:/projects/coding-governance-atlas/closed-loop-atlas.html`, 16,856,190 B [PINNED], last written
>   2026-11-03 23:25. Regenerated from origin/main 9e21ac760 it is **byte-identical**: current against every input
>   the generator reads, and blind to everything that changed since.
> - **The generator:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py` (723 lines [PINNED]),
>   template `...-atlas.html` beside it, procedure and probes in `...-atlas-instruments.md`. It reads only
>   dClosedLoop's own records: `memory/builds/dClosedLoop/README.md`, `build/*.md` minus every `-brief`,
>   `-return-` and `-as-built` file, and `reviews/*.md`. `SOURCES`, `LAYER_RECORDS` and the `AREAS` table name them.
> - **The "today" side is a frozen snapshot.** Each `AREAS` entry's `today` points at a measured section,
>   `current-state-measured-2026-10-14` or a layer record's `current` section. Nothing updates it as builds land.
> - **What the page cannot show, today:**
>   - Six of the 22 chain builds' build runs have landed: dTrueNorth, dGroundRules, dSafePassage (3ada42ab1),
>     dFairHearing (0a760477e), dOrderedCharter (9760fb746), dDeclaredLoop (9e21ac760, 102 `Pass:` commits).
>     All 22 spec runs are done. The page shows none of it.
>   - The owner's 2026-11-05 picks on 47 forks (740e19214) and the cross-read re-grounds (0d1c1dda4, 206272de9,
>     the dConvergedCharter re-ground, c0a17df12) live in the chain builds' specs, which the generator never reads.
>   - Deviation records (`deviations.py --report`) and the as-built view
>     (`build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, rendered by `...-asbuilt.py`, whose docstring already
>     says "later the help and atlas renders, read it in place of the design record") are skipped by name.
>   - Live and held run claims (`refs/gov/runs/<slug>`), the next runs that can start, the generation commit.
> - **The one existing "is this build run done" derivation is wrong.**
>   `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` `tree_state()` calls a build done only when every spec's
>   **Status:** is CLOSED or WONTDO. dDeclaredLoop and dSafePassage each carry one legitimately DEFERRED spec
>   (TOOL-dDeclaredLoop-34, "advances TOOL-dDeclaredLoop-35"; TOOL-dSafePassage-61, "advances TOOL-dSafePassage-14"),
>   so the script reports "builds landed 4" when 6 have landed and still plans both runs. The owner has been
>   answered "what can start" by hand twice because of it.
>
> ## Goal
>
> The Atlas is generated from the tree as it is, so the page always states the actual state of the project and of
> every chain build, and a page that no longer matches the tree is detectably stale.
>
> ## Scope the owner asked for
>
> 1. **Actual state, derived:** per chain build, its spec run and build run state, the landing merge, unit counts by
>    status, open forks, spec revisions and deviation records; per comparison area, which landed builds have changed
>    "today" since the 2026-10-14 baseline, with the as-built view in place of v2's `[chain]` where they differ.
>    The 2026-10-14 measurements stay, labelled as the baseline, never presented as today.
> 2. **One derivation of build state** (charter [one-fact], [reuse]): the Atlas and the schedule script read the
>    same predicate, and it counts a landed build run as landed. Fix `tree_state()` or replace it with the shared
>    predicate, so both read 6 landed at 9e21ac760. Read the DEFERRED semantics from the build method before
>    choosing: a DEFERRED spec that advances a later ask is not an unbuilt unit.
> 3. **Always:** the page embeds the commit and an input digest it was generated from; `--check` reds when the tree
>    has moved past it; and regeneration happens without anyone remembering to run it, on node d, after a landing
>    onto main. Every such behaviour is a switchable policy whose default is the answer (owner principle).
>
> ## Out
>
> - Publishing anywhere. The page's home stays `C:/projects/coding-governance-atlas/closed-loop-atlas.html`,
>   outside every git tree; the claude.ai artifact stays at v77; the generated page is never committed.
> - v2's text (frozen at 59ff8f2ac), any chain build's specs, and the other dClosedLoop instruments beyond the
>   schedule script's build-state read.
> - The design map (`...-map.py`) unless the shared predicate lands in a place it already reads.
>
> ## Acceptance
>
> - At the run's base, the regenerated page names the six landed build runs and their merges, the two that can
>   start now (dWitnessedBar, dPlacedRequest), and the generation commit; a planted landing (a fixture ref) moves
>   each of those and reds the old page's `--check`.
> - The schedule script prints "builds landed 6" at 9e21ac760 and no longer plans dSafePassage or dDeclaredLoop.
> - Each red case observed red before green, recorded beside its result.
>
> ## Constraints from the owner's standing rules
>
> - Role work only in role agents; agent effort medium by default; spec-audit disposal at high.
> - Units run no gates; the bar runs once after every unit is built. Never run the unattended kit self-tests
>   (`--selftests`); `GATE_SELFTESTS` stays unset.
> - No hook bypass, no `git add -A`. Commit trailer per the charter.
> - The template keeps its own doctype, charset, viewport and body margin (without them the page renders in
>   quirks mode with every `·` as `Â·`).
> - The browser pane refuses a `file://` open of a page this size: serve the folder over a temporary
>   `.claude/launch.json` (`python -m http.server`) and delete it afterwards.

## The brief

### Goal
The Closed Loop Atlas is generated from the tree as it is, so the page states the actual state of the
project and of every chain build, and a page that no longer matches the tree is detectably stale.

### Items
1. Per chain build, its spec run and build run state, landing merge, unit counts by status, open forks, spec revisions, deviation records and run claims, derived from the tree [planned TOOL-dTrackedAtlas-1]
2. One build-state derivation read by both the Atlas and the schedule script, counting a landed build run as landed, so both read 6 landed at `9e21ac760` [planned TOOL-dTrackedAtlas-1]
3. The Atlas renders that state, and per comparison area the landed builds that moved "today" past the 2026-10-14 baseline, with the as-built view in place of v2's `[chain]` where they differ, the baseline labelled as the baseline [planned TOOL-dTrackedAtlas-2]
4. The page embeds the commit and an input digest it was generated from, and `--check` reds when the tree has moved past them [planned TOOL-dTrackedAtlas-3]
5. The page regenerates on node d after a landing onto main without anyone running it, a switchable behaviour whose default is the answer [planned TOOL-dTrackedAtlas-4]

### Acceptance
- At BASE `9e21ac760` the regenerated page names the six landed build runs (dTrueNorth, dGroundRules, dSafePassage, dFairHearing, dOrderedCharter, dDeclaredLoop) with their landing merges, the two runs that can start now (dWitnessedBar, dPlacedRequest) and the generation commit.
- A planted landing on a fixture ref moves each of those, and reds the old page's `--check`.
- The schedule script prints `builds landed 6` at `9e21ac760` and plans no run for dSafePassage or dDeclaredLoop.
- After a landing onto main on node d, the page at `C:/projects/coding-governance-atlas/closed-loop-atlas.html` carries the new commit with no command typed for it; with the switch off, it does not.
- Each red case observed red before green, recorded beside its result in the unit's acceptance ledger.

### Gates
The merge bar, `bash tools/run-gates/run-gates.sh`, once at the close and without self-test flags; per unit, the direct check its spec names (the schedule script at `9e21ac760`, the generator's `--check` and its plants), never a suite.

### Non-goals
- Publishing anywhere: the claude.ai artifact stays at v77, and the generated page is never committed.
- v2's text (frozen at `59ff8f2ac`), any chain build's specs, and dClosedLoop's other instruments beyond the schedule script's build-state read.
- The design map (`…-map.py`), unless the shared derivation lands where it already reads.
- The policy kit's `derive_landed_owners`, which shares the DEFERRED miscount, is filed as an ask, not fixed.

### Limitations
- No path under `tools/`: `SELFTESTS_OWED_PATHS` would owe a `GATE_SELFTESTS=1` bar, and the run may not run the kit self-tests.
- No new file under `memory/builds/dClosedLoop/build/`: dClosedLoop's spec is held at its size high-water and grows a generated row per record there.
- The template keeps its own doctype, charset, viewport and body margin.
- Role work runs in role agents at effort medium; units run no gates; no hook bypass and no `git add -A`.
- A look in the browser pane serves the page folder over a temporary `.claude/launch.json`, deleted afterwards.

### Reuse
- The schedule script's `tree_state` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py#tree_state`) is the predicate to fix; `tools/chain-packet.py` answers its git reads.
- The as-built view `build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, rendered by `…-asbuilt.py` and `tools/memory-tree/asbuilt_view.py`, is the "today" source to read in place of the design record.
- `tools/memory-tree/tree_lib.py` `TERMINAL` and `CENSUS_TERMINAL` name the status sets; `tools/policy/check_policy.py` `derive_landed_owners` is a second copy of the miscounting rule.
- `tools/loop/position.py` derives one build's position from witnesses; the research record `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-atlas.md` states what an as-built atlas should show.
- Recall returned PLAY-dClosedLoop-2 (a spec run carries its units forward to its build run), PLAY-dClosedLoop-8 (re-run the schedule at each landing) and TOOL-dGroundRules-8 S1 (the landed-owner set, read from `tree_state`).
- Recall terms used: dClosedLoop schedule tree_state landed DEFERRED carry-forward atlas regenerate as-built position spec-run build-run

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt

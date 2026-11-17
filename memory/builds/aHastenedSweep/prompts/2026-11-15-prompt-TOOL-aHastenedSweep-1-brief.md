# Brief — aHastenedSweep: the memory-hygiene runner's per-item rescans removed, every verdict byte-identical

**Serves:** research TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4

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
Cut the `memory hygiene` leg's wall clock by removing four kinds of work repeated once per item in `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/gotchas.py` and `tools/memory-tree/corpus_ids.py`, while every check keeps its population, its output bytes, their order and its exit code.

### Items
1. R1: in check 25's by-name END loop of `tools/memory-tree/check-memory-hygiene.sh`, the condition `!(pl[i] in got) && test_whole_token(ln, pl[i])` gains `index(ln, pl[i]) &&` before `test_whole_token`; exact because `test_whole_token` opens with a `while ((p = index(substr(s, q+1), w)) > 0)` loop from `q = 0`, so it already returns 0 whenever `index(ln, pl[i])` is 0; the U and N sets, their order, the `D` completion sentinel last and the whole-word rule over the same reader allowlist are unchanged; a gawk alternation prefilter was measured slower and is not the design [planned TOOL-aHastenedSweep-1]
2. R2: in `tools/memory-tree/gotchas.py#selectable`, `os.path.basename(anchor)` is computed once per call and each path's `os.path.basename` once per process through a dict, with the same predicate, the same function and the same self-exclusion of the catalogue folder; in `tools/memory-tree/corpus_ids.py#walk`, `_roots(tracked_set)` is computed once before the citation loop instead of once per citation, exact because `_roots` is a pure function of a set the loop never mutates; one change to `walk` serves both `corpus_ids.py --check` and `gotchas.py --check`, which reaches `walk` through `load_defined_ids` [planned TOOL-aHastenedSweep-2]
3. R3: when `check-memory-hygiene.sh` itself launches `corpus_ids.py --check`, it hands down the index set it already computed (the `INDEX_SET` its prologue builds), for example as a file named by an environment variable that `corpus_ids.py#ask_shell` (or its `--print-index-set` caller) reads before it spawns the shell; the shell hands it down only when checks 1 to 5 recorded no failure in that run, and otherwise `corpus_ids` takes today's path so its "answered with findings" refusal still fires; the set handed down is byte-identical to the one `--print-index-set` prints for the same tree; the standalone CLI, with no hand-down, keeps today's path [planned TOOL-aHastenedSweep-3]
4. R4: checks 13 to 16 (`corpus_ids.py --check`) and 17 to 19 (`gotchas.py --check`) run in one Python interpreter launched once by the hygiene shell, in that order, with `corpus_ids.walk` memoized per (root, conf) and its result frozen or copied so neither verb can mutate what the other reads (the `[class]` guard-shares-state hazard); each verb prints its own block and returns its own exit code to the shell's existing `fail` and offender-key branch for its own check numbers, so the output bytes, their order and the exit mapping are unchanged; the memory-tree kit version moves once, in this last unit [planned TOOL-aHastenedSweep-4]

### Acceptance
- Unit 1: check 25's by-name pass, shipped against changed, prints `cmp`-identical output on the live tree; tFixture-208, tFixture-209 and tFixture-216 and the word-boundary fixtures (`count_shard`, `tRerun()`, `shard_rows`, `--dry`) in `tools/memory-tree/check-memory-hygiene.test.sh` keep their verdicts.
- Unit 2: `gotchas.py --check` and `corpus_ids.py --check`, shipped against changed, print `cmp`-identical output with identical exit codes on the live tree; the `gotchas.py --selftest` arms for check 19's dead anchor, the `--report` dead anchor, `selectable`'s basename arm and catalogue self-exclusion, and the inert anchor stay as they are, and `corpus_ids.py --selftest`'s read-path and dead-citation arms stay red on their fixtures.
- Unit 3: the hygiene run's checks 13 to 16 block is `cmp`-identical with and without the hand-down on the live tree; a seeded structure failure in checks 1 to 5 still makes `corpus_ids` raise "answered with findings" rather than accept an empty set; the standalone `corpus_ids.py --check` still spawns the shell's print mode.
- Unit 4: the whole hygiene output, shipped against changed, is `cmp`-identical on the live tree with the same exit code; a fixture seeding a dangling id for checks 13 to 16 and a dead anchor for checks 17 to 19 reds both in one run, each under its own check number.
- The build: each unit CLOSED with its live-tree parity evidence in its acceptance ledger, and the full `memory hygiene` leg's wall re-measured on node a against the `805–1093 s` range in the 2026-11-15 bar ledgers (PINNED).

### Gates
The merge bar `bash tools/run-gates/run-gates.sh` once at the close, without the self-test suites; within it `memory hygiene`, the kit version legs and the lexicon and codebase-map legs the change owes. The named arms of `check-memory-hygiene.test.sh`, `gotchas.py --selftest` and `corpus_ids.py --selftest` observed by the main loop at the close.

### Non-goals
- R5 (the records-commit recipe and the render stamp), R6 (`gen_build_index.py` grouping and check 2's `[ -f ]` calls) and the spec-writer prompt's hygiene scope: owner decisions, out of this build.
- Any weakened check, skipped population, exemption, cache across commits, or stamp of a full-mode result.
- `memory/builds/dDeclaredLoop/`, the live run's worktree `unattended-declared-loop-d56bf0`, its branch and its run-state file.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS, A SLICED SUITE INCLUDED. A pass runs only direct checks: `bash -n`, `python -m py_compile`, `check-arms`, the lexicon, the changed code invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. The live-tree A/B parity runs and the arms' red-then-green are the main loop's, at the close, recorded in each unit's acceptance ledger under a `Pass: none` commit.
- A pass commit without its acceptance ledger: each pass commit carries `memory/builds/aHastenedSweep/build/2026-11-15-build-TOOL-aHastenedSweep-<n>-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aHastenedSweep-<n>` block naming each criterion with the backticked token the criterion itself spells, and the live-tree parity and arms named as owed to the main loop.
- Spec and code in one commit: the spec lands first in a records commit, the code in a later one.
- An edit after the commit that sets a spec CLOSED: every edit lands first, and the status flip is the last change of the pass.

### Limitations
- Verdicts byte-identical: same populations, same output bytes and order, same exit codes, on the live tree and on every fixture of the three suites.
- A spec's acceptance criteria cite no path the unit has not built yet: cite a new file by its basename in section 6.
- Every spec line stating a figure with a unit carries the word PINNED or a commit sha on that line.
- No `--no-verify`, and no landing on a red bar.
- Local main has diverged from `origin/main`, whose `aMeasuredDrag` bumped the memory-tree kit and added a `resolve_python` memo to the same shell; the reconcile is owed at landing.

### Reuse
- `tools/memory-tree/corpus_ids.py#walk`, `#_roots`, `#ask_shell` and `#load_defined_ids`; `tools/memory-tree/gotchas.py#selectable`; the hygiene shell's `INDEX_SET` and its launch of the two Python checkers: every change extends these seams, and no new module is owed unless unit 4's spec shows the one-process entry point cannot live in either existing file.
- Records: `TOOL-dTotalRecall-23` (the shell's Python delegations and `walk` run twice per hygiene run), `TOOL-aReplayedCard-10` (`--print-defined-ids` is a corpus walk plus the shell probe), `TOOL-aScouredKit-19` (the Python readers re-parse the conf), and the 2026-10-08 `aMeteredSweep` memory-tree suites research (`ask_shell("--print-index-set")` cost).
- Recall terms used: `hygiene check 25 by-name readers test_whole_token corpus_ids walk gotchas selectable print-index-set INDEX_SET ask_shell`.

## Drawn from the session

> `test_whole_token` opens with `while ((p = index(substr(s, q+1), w)) > 0)`, with `q = 0`, so it already returns 0 whenever `index(s, w) == 0`. The guard only skips the `substr` copy of the line plus the function call.
— agent, the analysis session's report `hygiene-perf-analysis.md`, 2026-11-15, R1

> It is handed over only when checks 1–5 recorded no failure in the parent. Otherwise `corpus_ids` takes today's path, so its "answered with findings" refusal (`:411`) still fires.
— agent, the analysis session's report `hygiene-perf-analysis.md`, 2026-11-15, R3

> Each check's output bytes, their order, and their exit-code mapping are unchanged. Neither verb may mutate the walk result: the result must be frozen or copied, which is the guard-shares-state hazard `[class]` warns about.
— agent, the analysis session's report `hygiene-perf-analysis.md`, 2026-11-15, R4

> fully unattended
— owner, 2026-11-15, the kickoff's answer to how the build should run

## Owner confirmation

Asked: How should the hygiene speed-up build run? Your brief says landing waits for your ask, and an unattended run lands and pushes on its own.
Answer: fully unattended

# Phase 0 builder brief: the opening script

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 239 renders from this brief record, through `handoff.py render --role gov-builder`, with this
file as its `input:spec`. Phase 0 is the unit's remaining work, S4 of `spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`,
and the owner approved it (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[walk]`, `[handoff]`).

## The prompt

Build P0.5's opening script, `build/2026-10-20-build-PLAY-dClosedLoop-1-open.py`, as
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]` states it in P0.5, with P0.6's minting rules
1 and 2, P0.7's checks and red tests that read the opening, and P0.8 row 9's `--carriers` list. The plan is the spec
for this unit: follow it as written.

## The brief

### Goal

`open.py --write` writes every file of the opening for all 22 chain builds of v2's `[chain]`, and `open.py --check`
reds on any byte or summary disagreement. Its `--summary`, `--families`, `--driver-builds` and `--carriers [--check]`
modes print what P0.5 and P0.8 row 9 say they print. The script is committed with its red tests seen in a scratch
clone; the opening itself is NOT committed by this unit (the main loop commits it beside the decision rows).

### Items

1. **What it writes**, per P0.5's table, from the named sources: each README (front matter, H1 and stage, the five
   slots, the build-level rules 1 to 8 with rule 8 only in driver-changing builds, `roster:units`), each `BACKLOG.md`
   with its one carry-forward ask and `SEV` row (none for dTrueNorth), each packet through the packet instrument's
   render function (`build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`; import it by path, never copy it), the 22
   bound rows in `memory/project/readme-contract.txt`, and dClosedLoop's own `memory/builds/dClosedLoop/BACKLOG.md`
   with one clean-reading ask per driver-changing build (P0.6 rule 1), each with its `SEV` row.
2. **Reuse.** Import `tools/memory-tree/gen_build_index.py`'s heading canon and marker pairs (the plan cites
   `:73`, `:85`, `:125-131`); write the authored half only, and leave the generated regions to `gen_build_index.py
   --write`. Read v2 through `carries.py`'s `design()` where it already parses what you need. Read the format every
   record you write must take from `memory/HYGIENE.md`, an existing build README and `BACKLOG.md` (for example
   `memory/builds/dAlignedCarrier/`), and the readme-contract file's own header.
3. **Ids, fixed for Phase 0.** Each chain build's roster ids are `<FAMILY>-<slug>-1` to `-<n>` in clause order, the
   family derived by P0.5's rule (PLAY, KICK, DEPL or TOOL); dTrueNorth's seventh row, its extra unit, is
   `missing:TOOL-dTrueNorth-7` if its derived family is TOOL, carrying `**Derived:** PLAY-dClosedLoop-2`. Each carry-forward
   ask takes the build's next id after its roster. dClosedLoop's decision rows are `PLAY-dClosedLoop-2` (P0.8 row 1)
   to `PLAY-dClosedLoop-10` (row 9), the grant being `PLAY-dClosedLoop-3`; every `may:` line cites
   `PLAY-dClosedLoop-3`, and dTrueNorth's also `PLAY-dClosedLoop-2`. dClosedLoop's clean-reading asks are
   `PLAY-dClosedLoop-11` onward, one per driver-changing build in v2 `[chain]` order. The main loop writes the
   decision rows themselves after this unit, from `--carriers`'s output for row 9.
4. **Its read-only modes**, each printing from the files the opening writes or would write: `--summary` (P0.5's
   per-build summary, every column it lists), `--families` (the five-column table), `--driver-builds` (the predicate
   and its clauses), `--carriers` (P0.8 row 9's selectors over the tree at HEAD; `--carriers --check` reds a tracked
   path under a selector the list omits).
5. **Compare with the plan.** The plan's family table, driver-changing table and carrier list came from a scratch
   probe at `a93477abc`. Record where your derivation differs from each, and why; never change the plan.

### Acceptance

- In a `git clone --shared` scratch clone of your tree: `open.py --write`, then `python
  tools/memory-tree/gen_build_index.py --write`, then `open.py --check` exits 0, and `gen_build_index.py --check` and
  `--check-format` exit 0.
- P0.7's red tests, each seen red in that clone: a one-byte README edit reds `open.py --check`; a roster missing one
  clause reds the arm that reads every clause in exactly one row; a `parents:` typo raises; a removed contract row
  reds `gen_build_index.py --check-format`; a planted README whose family differs from its summary row reds
  `open.py --check`; a planted new kit directory reds `--carriers --check`.
- The generator-grammar bare-id predicate `build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py` (a sibling unit's;
  run it if your tree has it) prints nothing after the clone's `--write`.
- `packet.py --check <slug>` exits 0 for all 22 in the clone.
- A record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-open-instruments.md` (first line
  `**Serves:** research PLAY-dClosedLoop-1`) lists every command you ran for an acceptance check or red test, in
  order, with its exit and the line that proves it, then `--families`, `--driver-builds`, `--carriers` and
  `--summary` whole, then the comparison item 5 asks for. Commit it with the script.

### Gates

None of the bar's legs, no suite and no kit self-test. Run the script's own modes, the sibling instruments' check
modes in the scratch clone, and the naming lexicon (`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`)
before naming a new function. The pre-commit hook still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree is the main loop's worktree, `C:/projects/coding-governance/.claude/worktrees/unruffled-aryabhata-d89ede`,
  your session's own folder. Another agent may leave an untracked record in it: stage your own paths by name, never
  `git add -A`. This brief is your spec input: read it whole, then the plan sections it names.
- No file committed but `open.py`, the record above, and the `memory/builds/dClosedLoop/README.md` and `memory/LIVE.md`
  renders `gen_build_index.py --write` makes, which the pre-commit's hygiene check 9 requires. The opening's files are
  written only in the scratch clone.
- No change to the sibling instruments, v2, the execution plan or any record. If `packet.py` or another instrument
  needs a change for the opening, name it in your return.
- No decision row, no product code, no unit spec of a chain build.
- No merge, no push, no rebase onto another branch.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d239/` only; never delete anything outside it.

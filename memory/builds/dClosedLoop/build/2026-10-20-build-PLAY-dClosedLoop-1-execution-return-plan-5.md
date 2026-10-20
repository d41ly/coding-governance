# Return: the execution plan's writer, resumed to fold the fold review

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 229's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

All 22 fold rows from the second review pair are now in the plan and the schedule script, and the two refuted rows change nothing. The script's output is unchanged: re-run at HEAD `d26d19a8e` it exits 0 and matches the pasted block. Nothing is committed. Two things are not settled by this fold: the pin-guard gap that only the owner's landing-diff check covers, and the cost of the report-switch step (see "Left open").

- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` (126 KB)
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` (21 KB)

## The highs
- **`pin-check-arm-missing`** (applied):
  - P0.3: `--write` now keeps the pins, and `--check` gets a separate pin arm that compares each pin with `git rev-parse HEAD:<instrument>`.
  - P0.3 also gets the `packet.py --repin <instrument>` command: refused inside a chain run, run only in an owner-asked landing on its own, and recorded as a decision row.
  - P0.1 row 10's plant now exercises the escape the pin guards (re-rendering for another cause while keeping pins), with two controls.
  - [handoffs] names the re-pin step.
- **`pin-overclaim`** (applied): [handoffs], P0.1 row 10 and "What nothing catches" no longer claim the pin holds against a run. A hand edit of the pin line, or of `packet.py`, still moves it.
  - The owner's landing-diff check now also covers changed pin lines in any `*-packet.md`, in "What the owner sees" and both [owner] landing rows.
  - New [cannot] row. Phase 0 tries the hand edit once and records the result (expected green); it is never planted as a red.
- **`whole-run-read-as-spec-run`** (applied, using the open-ask route): a run is a spec run only if the build's `BACKLOG.md` holds an open ask at the run's baseline and a roster unit is `MISSING`. dTrueNorth has no such ask, so its whole run never qualifies. The rule is the same in README rule 1 and the extra unit's text, and red case 8 covers it.
- **`outside-paths-range-undefined`** (applied): P0.2 now defines the run's range once. `P` is the prepared merge's first parent, the remote tip `check_prepared_merge` reads.
  - Paths come from `git diff --name-only P..HEAD`, and trailers from `git log --format=%B P..HEAD`.
  - A plant shows other builds' landings are not listed, while the run's own cross-build write is. That plant is seen red first against `<base>..HEAD`.
- **`retirement-report-edit-no-route`** (applied): the retirement table now has a "report-switch step".
  - The landing build files an ask in dClosedLoop's `BACKLOG.md`.
  - dClosedLoop's session then edits `deviations.py --report` and runs `packet.py --repin deviations.py`, and the two land together, alone, recorded as a decision row.
  - Every row whose report reading switches names its landing. The five matching [sync-points] rows and a new [owner] row name the same step.

## The other 17 rows
- **Applied as written:**
  - P0.2 and README rule 6 changes:
    - `marks-arm-two-readings`: a `none` mark is no entry. There are three exit-1 cases, the full set of plants, and the residual is named in "What nothing catches". Rung 5 and D7 put a goal-bound-only choice, marked `widens: none`, among the other forks.
    - `ruling-list-two-wordings`: rule 6 and P0.2 now list the same rulings.
    - `outside-paths-no-product-source`: a build run's product paths come from its recorded `--dispatch --writes` sets.
    - `rule7-forbids-shared-renders`: `LIVE.md`, the ledgers, re-rendered generated files and ask rows are exempt.
    - `ordering-plants-cannot-red`: each ordering plant uses a renderer stub, seen red with the arm on and green with it off.
    - `deviation-record-shape-stale`: the record keys are `**Bound:**`, `**Tier:**`, `**Surface:**` and `**Reason:**` everywhere.
  - Extra-unit changes:
    - `once-witness-counts-aborted`: only landed rotated records count; red case 9.
    - `red-case5-plant-unreachable`: the full README rule 1 plant, with before and after messages.
    - `fallback-refusals-unplanted`: red case 10.
    - `baseline-units-callers-untested`: red cases 11 to 13, plus check 24 run in case 5's fixture. "What the pilot proves" now says thirteen.
  - `owner-ask-reaches-no-packet` and `field9-records-no-source`.
  - The three script rows:
    - `schedule-b-claim-phantom-node`: a claim on a node the figure leaves out is left unpinned. Seen red on the old code, which gave "a and d alone" 216; now 273.
    - `stale-claim-printed-fresh`: the table cell and the first-wave line read "take over (stale)".
    - `unreadable-beat-pinned-untested`: printed and kept pinned.

    The three script cases and the old-code red were observed in the scratch clone and recorded in P0.4's table, and the docstring is updated.
- **Applied with a note:**
  - `owner-ask-mints-chain-slug`: dClosedLoop's session mints the "no" ask under its own slug and files it as a foreign row. When the build has already landed, the ask goes in dClosedLoop's `BACKLOG.md`. I made field 9 carry every such ask in **every** packet, because a landed build's packet is never read again.
  - `baseline-units-caller-miscited`: I re-grepped all three callers. `unattended.sh:5173` and `:13257` are as cited; `check-unattended.sh:3907` is check 24. Each caller's verdict under the fallback is tied to red case 11 or 12.
- **Not applied:** `surviving-option-misread` and `packet-runs-retired-coverage`, the two refuted rows.

## The sweep
I grepped the whole plan for the old wording of every rule this fold changed, and found four leftovers, all now fixed:
- Phase 1's owner row still said "the next chain run's packet names it"; it now says field 9.
- P0.8 row 5 still said every marked choice is listed first; it now says non-`none` only.
- The schedule preamble described the previous fold; it now names both folds and `d26d19a8e`.
- The bare-id population line now records the re-run at `d26d19a8e`, same result: 25 citations in 7 files.

I also checked, and found no conflicts in:
- the old spec-run test, the old witness and the old caller citation;
- the old keys and the ruling list;
- the old "listed first" and pin wording, and "four" or "seven red cases";
- a `<base>` range (it now appears only as the planted red);
- duplicate answers across README rule 1 and the extra unit, rule 6 and P0.2, and [handoffs], P0.3 and the retirement step.

The plan still has one H1, no bare unminted ids, and no prose line over the wrap width.

## Left open
- **The pin is only partly guarded.** A run can still hand-edit its packet's pin line or `packet.py`. Until a chain unit adds a merge-bar check, only the owner's landing-diff check catches it. Phase 0 must try the hand edit once and record the result.
- **The report-switch step costs five owner-asked landings.** These are dClosedLoop-only landings, one after each of dTrueNorth, dOrderedCharter, dDeclaredLoop, dIndexedDesign and dScopedBuild. Until each lands, `--report` keeps reading the instrument it used before.
- **The validating arm can't see a mislabelled veto-3 choice.** A veto-3 choice under ER:240 marked `widens: none` passes, because a goal-bound-only choice is legitimately marked that way.
- **Two facts rest on reading, not running:** that `check_prepared_merge` accepts commits stacked on the prepared merge, and every `baseline_units` red case. The extra unit's own run is the first to exercise them.

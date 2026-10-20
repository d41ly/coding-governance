# Return: the execution plan's writer, resumed to fold the owner's answers

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 220's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

I've folded the owner's answers from the execution record's `[answers-2]` (ER:166-286) into the plan and the schedule script. The script runs clean (exit 0) and its new output is pasted into `[schedule]`. Nothing is committed.

Files:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` (88,145 bytes)
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` (17,634 bytes)

## What changed, section by section
- **Intro:** says the `[answers-2]` choices are folded in, with each decided item quoting its answer.
- **[answer]:**
  - Residual forks now follow the owner's "Standing ruling" (ER:240). A choice that widens a surface is marked and listed first in its build's departures report. Only a fork with no option at all is still carried forward (new D10).
  - The carry-forward problem is now fixed by "dTrueNorth's extra unit (Recommended)" (ER:232).
  - The two readings are settled by the owner (ER:181, :189).
  - b is "Spec runs only" (ER:219).
  - The run count is now 43 starts at 37 moments, each typed by the owner (ER:270).
  - The plan in brief now has dTrueNorth as one whole run, and dGroundRules as the first split pair.
- **[constraints]:** new row for the carry-forward term that refuses added units (`unattended.sh:5156`, `:5177-5184`).
- **[phase-0]:**
  - P0.2: the departures report now lists `widens:` choices first, with a new red case for that ordering.
  - P0.3: dTrueNorth's packet now names the extra unit and the two records its run writes.
  - P0.4: the model now declares the answers (`WHOLE`, `EXTRA`, `SPEC_ONLY`), and the red tests are re-run under it.
  - P0.5:
    - every `may:` line cites the grant decision row, and dTrueNorth's also cites the extra unit's row;
    - dTrueNorth's roster has a seventh, derived unit and no carry-forward ask;
    - the README rules now cover the whole run and the `widens:` mark.
  - P0.6: the minting rule includes the extra unit.
  - P0.8: the decision rows are rewritten, each quoting its answer.
- **[phase-1]:** rewritten. dTrueNorth is one whole seven-unit run. The extra unit is specified with its four red cases, goes last in the run, and dTrueNorth lands through it. Proofs the pilot no longer gives (the spec-run close and the build run's pickup) move to dGroundRules' two runs.
- **[phase-2]:**
  - The spec run carries review-promoted units forward, and the build run must build them.
  - A discovery a spec run would adopt is filed as an ask instead (D9).
  - Fork rung 5 is now the standing ruling; rung 6 is a fork with no option at all.
- **[schedule]:** new output pasted. The dispatch rule now says b takes spec runs only; first wave, load, b's share and the run counts are updated.
- **[sync-points]:** the dTrueNorth row adds the extra unit's driver change. The dPlacedRequest row is the spec test, with a drain as fallback (ER:264). The dOrderedCharter row now says its principles take over from the standing ruling.
- **[deviations]:** the owner's rule now quotes the answers. A new table names every owner-approved departure, where it is recorded and when:
  - **Record 1:** the departure from `cl-dClosedLoop-0004`, in `memory/builds/dTrueNorth/build/…-deviation-1.md`. dTrueNorth's run writes it in that unit's spec commit; the approval lands as a decision row in the opening.
  - **The extra unit:** its approval and `**Derived:**` source is a decision row landed in the opening; the unit is minted on dTrueNorth's roster in the opening. **Record 2** is written in dTrueNorth's run, in the extra unit's spec commit.
  - **Two more records:** dPlacedRequest's spec test and dWellOiledMachine's in-flight test, each written in its own spec run.
  - D3's planted cases are carried, not asked.
- **[per-node] / [owner]:** b takes spec runs only; start times have shifted. The owner's steps are rewritten for 43 typed starts and the read of dTrueNorth's whole-run report.
- **[cannot]:** six rows rewritten as designed around by the answers. The no-option fork remains a "cannot".
- **[defaults]:** three groups: decided (R1, R2, R3, D1, D2, D4, the replaced D6, D7 and node b, each quoted); carried for the walk (R6, D3, D5, D8); and left open (D9, D10).
- **[disagreements]:** the b row and the BLOCKED row are updated, and a new row records that the override route is dropped.

## Schedule script

Run from the worktree root at HEAD `8d4db98a3`, exit 0:

```
$ python -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
claims cached on chain builds: none live or held
makespan 271 units; with unlimited nodes 198; whole builds after their parents land 277; serial on one node 510 (v2's 509 and 1 unit beyond it)
node a: busy 261 of 271 (96%), work 261 of 510 units, 21 runs: 8 spec, 12 build, 1 whole
node d: busy 208 of 271 (77%), work 208 of 510 units, 16 runs: 7 spec, 9 build, 0 whole
node b: busy 162 of 271 (60%), work 41 of 510 units, 6 runs: 6 spec, 0 build, 0 whole
first wave: a whole dTrueNorth at 0 · d spec dSafePassage at 11 · b spec dFairHearing at 18
runs the owner starts, 43, at 37 distinct times
b's pace swept: 0.25 → 271, 0.30 → 265, 0.35 → 261, 0.40 → 254, 0.45 → 247, 0.50 → 243 (spec runs only); a and d alone: 273
```

This is a summary of the main lines. The full output, including the per-build table, run list and landings list, is pasted verbatim into the plan's `[schedule]` block. I checked that block against a fresh run and they are identical.

I re-ran the planted cases with the changed script in a scratch clone:

| Planted case | Result |
|---|---|
| A clause dropped from the design | exit 1 |
| dTrueNorth's specs present but deferred | its whole run still starts at 0 |
| dTrueNorth's specs closed | dTrueNorth reads done |
| A live claim by b's user on dGroundRules | that spec run is pinned to b |
| A claim naming an unknown user | exit 1 |

One limit is stated in the script and the plan: the extra unit carries no clause, so the script cannot see its spec. dTrueNorth reads as landed once its six clauses' specs are closed.

## Questions the answers leave open
- **D9. A discovery a spec run would adopt.** The owner's fix admits only units "from the reviews (either spec or closing diff)" (ER:196-197). An adopted discovery is also a unit the run adds, so a spec run that adopts one still cannot close.
  - (a) File it as an ask for the build run to adopt. This departs from the protocol's "adopt now" rule.
  - (b) Widen the extra unit's condition to admit adopted discoveries once as well.
  - I recommend (a), and the README rule applies it until the owner answers.
- **D10. A fork with no option at all.** If every option fails an acceptance criterion or a non-goal, the standing ruling has nothing to take. The plan carries the unit forward and asks the owner for a ruling; does the owner want a different rule?
- **Record placement and approver wording.** For records 1 and 2, the approval is landed at the opening as a decision row, but the record file is written later, in dTrueNorth's own spec commit, as `cl-dClosedLoop-0004` requires. Is that placement right? Each record names "owner" as approver and cites the answer; is that the wording the owner wants?
- **Unverified points, now moved to dGroundRules.** Since dTrueNorth runs whole, it no longer tests these: whether the build harness re-audits specs the spec run already audited, and the ask row that holds the carry-forward ask open. dGroundRules' two runs are now the first test of both.

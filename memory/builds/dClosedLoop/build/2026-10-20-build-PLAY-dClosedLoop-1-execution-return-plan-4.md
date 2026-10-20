# Return: the execution plan's writer, resumed to fold the paired review

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 225's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

The review fold is applied to the plan and the schedule script; nothing is committed. All 36 fold rows are applied, both forks are folded as the owner answered, and the one no-fold row changes nothing. The script's output didn't change: re-run at HEAD `8d33694d7` (exit 0), it prints the same output as before the fold.

Files:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`

## Fold rows

**Applied as written:**
- `instrument-pin-rerendered`: B's skeptic's fix, in P0.1 row 10, [handoffs], the spec-run row, the owner's landing check, "What nothing catches" and a new [cannot] row.
- `close-cross-build-unrefused`: [handoffs] now says no gate refuses a run's own write to another build (fail 66, `unattended.sh:10540`). New README rule 7, a P0.2 block listing outside paths with its red test, and the [cannot] path-exclusion row cites that block.
- `rung5-drops-only`: [answer], rung 5, D7 and P0.8 row 5 now say "passes veto 1 and fails only…", quoting ER:237-238.
- `base-roster-unreadable`: the extra unit's starting-roster reading (`baseline_units`, the caller at `unattended.sh:13257`), red case 5 and its standing fixture. The unit's specification says this is inside the owner's approval; P0.8 row 1 and record 2's row name it.
- `once-guard-no-source` (witness: the rotated `RUN.*.md`, red case 3) and `spec-run-closes-no-unit` (a spec run is the README's "any unit MISSING" rule, red cases 6 and 7; the pilot now proves seven cases).
- P0.2's six rows (`report-order-unchecked`, `relaxes-completeness-unchecked`, `unmarked-ruling-choice`, `departures-name-collides`, `report-check-no-caller`, `record-step-prose-only`): one validating arm separate from the byte compare, the `tier:` field, the `widens:`/`relaxes:` key on every ruling trailer, reports named `-departures-spec.md` / `-departures-build.md`, and the planted red tests.
- `report-sources-no-arm`: two new population arms in P0.1, for rescope rows and hand-backs, with their plants (B's skeptic's fix).
- `report-before-prepare`: README rule 4 now holds one close sequence, run after the final `--prepare`. It is wired into phase 1, both phase-2 tables, [deviations], the reconcile step and the [cannot] departures row.
- `retirement-misses-report`: the retirement table now says, for each instrument, what the report and packet read instead, and that the `--report` mode itself outlives the join.
- `dead-before-truenorth-clauses`, `disagreement-ask-sink` (asks go to the successor build; [coordination]'s ask rule updated), `approver-cites-er-line`, and `owner-approver-any-row` (B's skeptic's fix, with plants).
- `welloiled-in-flight-unapproved`: that test leaves the owner-approved table and is recorded as author-approved.
- `owner-reject-no-route`: B's skeptic's fix, as a new P0.6 rule 5 plus the [owner] and phase-1 rows.
- `override-row-778`, `opening-gate-constant`, `field9-no-source`, `p08-acceptance-omits-answers3`, `phase1-precondition-omits-row2`, `shared-path-rate-caveat`.
- The script rows: `python-check-cannot-fail`, `fetch-leaves-claim-cache-stale`, `schedule-stale-claim-pinned`, `claim-pin-bypasses-spec-only`, `spec-only-untested`, `offfleet-claim-dropped`, `schedule-extra-doc-stale`, `whole-landed-doc-looser`. I implemented each and observed its plant in the scratch clone, and P0.4's table records them.

**Applied with a note:**
- `bare-id-predicate-grammar`: the generator's own grammar finds 25 citations on 22 lines in 7 files, not the old 16 lines in 4. The three new files are the main loop's records: the reviews-compared record (line 170) and the two review records. Phase 0 re-runs the predicate before the opening.
  - The `x:`-prefixed plant is described in words, because writing the id would join the plan itself to dTrueNorth's roster.
- `disagreement-ask-sink`, coordination part: I added one sentence the row doesn't spell out. A problem found in an already-landed build becomes an ask in the finding run's own `BACKLOG.md`, since only a later close disposes of an ask.
- Retirement table: it originally said the packet "drops" a retired instrument's pin. I changed that to "keeps it", so it doesn't contradict [handoffs]' rule that a re-render keeps the pins it carries.

**Not applied:** `truenorth-extra-cite`, the no-fold row. Nothing changed.

## The forks, as folded
- **`veto2-fork-unruled`**: "Standing ruling takes it (Recommended)" (ER:388). Updated in [answer] item 2 (now four kinds of fork), rungs 3 and 5, the "nothing parks" lines, D7 plus a new "Veto 2 outside the grant" entry, the [cannot] residual-fork row, [disagreements] and P0.8 row 5.
  - A choice the grant lifted carries `grants: <decision id> <change>`. P0.2 lists it first, and a red test covers a grant-lifted choice the report omits.
- **`override-after-key-live`**: "The adding build (Recommended)" (ER:396). Updated in the dDeclaredLoop, dKeptSession and dScopedBuild rows of [sync-points], P0.8 row 3, the [owner] row (now "nothing to set"), [deviations] and [defaults].
- The intro, [owner] and [defaults] also record "Review the fold, then approve" (ER:404).

## Schedule script
The fold changed only how the script reads claims, not its runs, durations or ordering, and no chain claim is cached on node d. The `[schedule]` block now shows the `$PY` invocation the fold asks for:

`. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`

Its output is identical to the pasted block. How the script now treats claims:
- A live claim older than `RESUME_STALE_BOUND` (read from `.unattended.conf`) is reported stale and left unpinned.
- A node-b claim pins only a spec run.
- A node-c claim is held off-fleet and stays off every node's table.

## Left open
- **The marks rely on the run.** A choice that cites no ruling at all, or a grant-lifted choice the run never marks `grants:`, can't be listed first. The validating arm only reds a trailer that cites a ruling but carries no mark.
- **Two facts read from comments, not run:**
  - `check_prepared_merge` accepts single-parent commits stacked on the prepared merge (`push-main.sh:505-538`), which the new close sequence relies on.
  - The new red cases for `baseline_units` are a specification only; the extra unit's run is what first exercises them.
- **Clock and pace assumptions.** The stale-claim check uses the node's own clock against `beat-utc`. An off-fleet holder's run is modelled as finishing at full pace.
- **Who mints the owner's "no".** The decision row behind an owner's "no" (P0.6 rule 5) is minted under dClosedLoop's slug by the owner's own session; no run holds that slug. Confirm that's acceptable.

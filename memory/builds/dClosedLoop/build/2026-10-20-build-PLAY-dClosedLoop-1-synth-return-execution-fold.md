# Return: the execution plan's fold review compared

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 228's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-58-synthesizer.md`.

---

I wrote the comparison record. All 53 findings are placed: 28 from run A and 25 from run B. The map has 24 defect rows and no forks.

**Record:** `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-fold-reviews-compared.md`

**Rows by disposition:**
- **Fold, 22.** Seven of them fold a skeptic's corrected fix, all from run B's skeptics:
  - `pin-check-arm-missing`
  - `pin-overclaim`
  - `outside-paths-range-undefined`
  - `baseline-units-caller-miscited`
  - `baseline-units-callers-untested`
  - `retirement-report-edit-no-route`
  - `schedule-b-claim-phantom-node`
- **Fork, 0.**
- **No fold, 2.** Both were refuted and run A alone raised them: `surviving-option-misread` (A9) and `packet-runs-retired-coverage` (A11).

**Forks:** none.

**Unplaced finding ids:** none. I checked this with a script against both appendices.

Where the two runs' fixes differed, I picked one route and recorded why in the `[fold]` row:
- **Rule-6 marks (`marks-arm-two-readings`):** an ER:240 trailer marked `widens: none` passes, as run B's plant has it, because a choice that only fails the goal bound is legitimate. Run A's route would have failed every such trailer.
- **Phantom node b in the schedule (`schedule-b-claim-phantom-node`):** a node-b claim in the "a and d alone" run is left unpinned (B's corrected fix). Run A's hidden `speed['b*']` key is not taken.
- **Spec-run test (`whole-run-read-as-spec-run`):** a run counts as a spec run only if its build's `BACKLOG.md` holds an open ask at the run's baseline commit. The opening files no such ask for dTrueNorth, so its whole run never qualifies. I did not use a README marker, because a new front-matter key would have to be added to dTotalRecall's schema.

Run A's finding A14 was refuted, but it sits on the `field9-records-no-source` row. That row folds because run B confirmed the same defect (B24): the earlier fold row named the records half of the problem and the plan never fixed it. A28 lands on two rows, `red-case5-plant-unreachable` and `fallback-refusals-unplanted`.

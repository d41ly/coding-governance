# Return: the execution plan's writer, resumed to correct the self-test waiver's scope

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 231's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

I've applied the correction to the plan. Every close whose range touches `tools/` exports `GATE_FULL=1 GATE_SELFTESTS=1` again, the seven driver builds included. Rule 8 now waives only the unattended kit's own on-demand suites. The schedule block still matches a re-run.

I checked the correction against the sources before applying it:
- `tools/unattended/run-unattended-gates.sh:2` says the kit's suites run "on demand and never on the merge bar"; lines 28-31 say the kit's Definition of Done wants their verdict in the landing report.
- `unattended.sh:10528` is where the driver tells a run it owes `GATE_FULL=1 GATE_SELFTESTS=1`.
- `.githooks/gate-env.sh:25` holds the Definition of Done comment.

**What changed in the plan**
- **README rule 8** is now dAlignedCarrier's rule as written: the suites are waived for the landing, a criterion they would observe is amended citing the rule, and their clean reading is owed with an ask.
  - The rule names what it waives: the `--selftests` verdict the landing report would otherwise carry. It keeps targeted probes, planted tests and the acceptance-ledger note in place of the suites. It states outright that the close is unchanged, still exporting `GATE_FULL=1 GATE_SELFTESTS=1`.
  - It applies to the seven derived driver-changing builds only.
- **New ask per driver build.** dAlignedCarrier owed its clean reading with another build's ask, so P0.6 rule 1 now has the opening file one such ask per driver-changing build in dClosedLoop's own `BACKLOG.md`. The per-build summary shows that ask's id.
- **Phase 1** has the flagged bar restored in its prose and its close step. The landing report carries no `--selftests` verdict. The red-case fixture stays in the kit's on-demand suite and runs as a targeted probe.
- **The seven driver rows in [sync-points]** now say the README waives the on-demand suites while the build run still closes under `GATE_FULL=1 GATE_SELFTESTS=1`.
- **[constraints]**: the `tools/` row now separates what `GATE_SELFTESTS=1` runs (the bar's held kit legs) from the unattended suites, which are on no leg.
- **P0.8 row 6** still quotes "Waive in each README" (ER:476), now worded to this scope, citing the correction at ER:544-557. It also says the close still runs the flagged bar.
- **[defaults]**: the waiver item now carries the corrected scope. My open question is moved under a new heading, "Closed after the walk": it has no subject, because a `tools/` build that doesn't change the driver owes the flagged bar and no unattended suite. The [owner] "Now" row is updated to match.
- **[disagreements]**: the "cheap landings" row now says a spec run, which touches no `tools/` path, skips only the held kit legs `GATE_SELFTESTS=1` adds.

**Sweep.** I grepped the plan for every mention of `GATE_SELFTESTS`, self-test, waiver and "left open":
- Every close under `GATE_FULL=1` without `GATE_SELFTESTS=1` is gone.
- Every claim that `GATE_SELFTESTS=1` runs the unattended suites is gone.
- The "Left open by the walk" item is gone.

The remaining mentions all state the corrected scope. I also checked the rest:
- No prose line runs past the wrap width.
- The plan still has one H1.
- The bare-id predicate is unchanged at 25 citations in 7 files, none of them in the plan.

**Schedule script.** Unchanged by this correction. Re-run at HEAD `05601ee4c` it exits 0, and its output matches the pasted block exactly (ignoring line endings).

The only file I changed is `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`. The script `…-schedule.py` is untouched since its last commit.

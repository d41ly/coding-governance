# Return: the execution plan's writer

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 219's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

I've written the plan and the schedule script; nothing is committed. They take the two new files only. Two of the main loop's readings of the owner's answers don't hold as written. A third gap, not in the five returns, blocks the ratified spec-run close whenever its audit or closing review confirms a finding. The plan applies neither wrong reading, so the opening and dTrueNorth's spec run both wait on the owner.

**Files**
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` (78,751 bytes)
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` (16,086 bytes)

## Schedule script

Run from the worktree root at HEAD `b6a6c650d`: `python -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`. It exits 0, and its output matches the block pasted in the plan's `[schedule]` section line for line (only line endings differ). The main figures:
- **Size:** 22 builds and 509 clauses, both asserted by the script.
- **Makespan:** 270 units. That compares with 197 on unlimited nodes, 276 for whole builds after their parents land, and 509 run serially on one node.
- **Load:** node a is busy 96% of the time (260 units of work, 22 runs), node d 77% (208 units, 16 runs), node b 60% (41 units, 6 spec runs, no build run).
- **First wave:** a takes dTrueNorth's spec run at 0; d takes dSafePassage's spec run at 10; b takes dFairHearing's spec run at 17.
- **Runs the owner starts:** 44, at 38 distinct moments.
- **Node b's pace swept:** the makespan is 270, 261, 260, 253, 243 and 241 as b's pace goes from 0.25 to 0.50 in steps of 0.05. With a and d alone it is 272.

I checked the script against planted cases in a scratch clone:

| Planted case | Result |
|---|---|
| One clause dropped from the design | exit 1 |
| dTrueNorth's specs present, all deferred | its spec run reads done |
| dTrueNorth's specs all closed | both its runs read done |
| A live claim cached on dGroundRules | that run is pinned to its node |
| A claim naming an unknown user | exit 1 |

## Readings found wrong or incomplete, as questions for the owner
- **R1 (wrong).** Answer 2 asks for grants "derived from the paths of the nodes it owns", but those nodes have no paths. In the design's map every owned node is a key with only an owner relation. Should each build's grant be one decision id, the path tokens in its own clauses (9 builds would get none, dDeclaredLoop among them), or paths typed per build? **Recommend the decision id.**
- **R2 (wrong).** Answer 3 does change a clause. `cl-dClosedLoop-0004` fixes dTrueNorth's stand-in join to the by-risk approval table. Should that join instead read your values, as a deviation you approve? **Recommend yes.**
- **R3 (incomplete).** The `report` setting lets an unrecorded departure land, yet you said departures "are recorded". Should the join refuse until the run has written a record (still never waiting on you), or stay at report? **Recommend report, as read.**
- **R4 (incomplete).** "Nothing is parked or blocked" goes beyond what today's driver can do. A fork whose only options widen a security surface, one with no surviving option, and one that would amend the build's goal still park. Answered by D7.
- **R5 (incomplete, the gap above).** The carry-forward close works only for the units a spec run started with. The harness turns every confirmed audit or review finding into a new unit, and an added unit is never carried forward. Answered by D6.
- **R6 (incomplete).** The readings leave `design.coverage` unset. The plan keeps `refuse`, since the run can always clear a coverage red itself. Does that count as "blocked"? **Recommend keep refuse.**

## Default decisions, with the recommended option
- **D1, the builds that rewrite their own driver:** order the driver-touching units last and let the build land through its own new code; hand the landing to the owner only if that code refuses it.
- **D2, dPlacedRequest's claim migration:** its spec carries the test that a live claim on another node survives, with draining all runs as the fallback.
- **D3, replacing the instruments:** the product join takes the instruments' planted cases as its acceptance, rather than adding bootstrap legs first.
- **D4, who starts runs:** the owner types `/unattended <slug>` on the named node, 44 times.
- **D5, the two deviation keys after the chain:** back to `refuse` and `by-risk`.
- **D6, a spec run that adds units:** an owner ruling lets it close with `--override build-complete`.
- **D7, forks the driver still parks:** carry the affected unit forward so its build still lands.
- **D8, who mints chain ids:** the opening mints every roster id and carry-forward ask. This is forced by the carry-forward rules.

## Not settled, and what would settle it
- **Re-audit in the build run.** I didn't establish whether the build harness re-audits specs the spec run already audited. The dTrueNorth pilot's build run, or a full read of the harness's audit-subject logic, would settle it.
- **The ask's lifecycle.** I didn't verify the backlog row grammar that holds the spec run's ask open, or that the last unit's `closes` marks it CLOSED. The pilot or a read of the ask generator's fold would.
- **Filing in another build's backlog.** Whether a run may file an ask in another build's `BACKLOG.md` rests on the coordination return; the asks guide addresses only a foreign ask's dispositions. A hygiene fixture would settle it.
- **The override itself.** I didn't read whether the unattended bar leg reds the `--override build-complete` in D6.
- **Spec share and b's pace.** Both are unmeasured: no unit's wall time is recorded. The pilot's two runs give the first measurement.
- **Which rule the owner prefers.** The schedule return's 262 comes from a planner that holds a node for an upcoming critical run. The script applies the return's own stated rule and gets 270.

I ran none of the bar's legs and didn't run the hygiene gate. The scratch probes are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\exec\d219\`.

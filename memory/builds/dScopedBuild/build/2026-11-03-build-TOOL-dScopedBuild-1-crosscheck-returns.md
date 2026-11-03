**Serves:** research TOOL-dScopedBuild-1 TOOL-dScopedBuild-7

# dScopedBuild — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck`](2026-11-03-build-TOOL-dScopedBuild-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dScopedBuild-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group, led by spec 1 (specs 1 and 7)

Specs 1 and 7 make 8 assumptions about the revised parent units. 6 AGREE, 1 is a MISMATCH that predates the revision, 1 is UNKNOWN UNTIL BUILT, and rule RH binds neither spec. Commit `66f7b8d32` changed only wm6's header, records table, §2 S6 and S7, §8 F4 and §9 (`git diff 5f0b11f12 66c5b8dbf -- …-6.md`). Neither spec cites any of those sections, and S1 and S8 are byte-identical at both commits.

1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | wm6, "the executor", owns the file-backed transition record for `build.exit` | cite | MISMATCH | sb1:108 against wm6, which has no transition record (`grep -c -i transition` prints 0 at `5f0b11f12` and at `66c5b8dbf`). Its only item witness is a reconcile row's landed effect (wm6:118-119). The writer is TOOL-dDeclaredLoop-3 S5 `write_transition` (dl3:60), called through `loop_transition.py record` as wm3:60 and wm46:84 do |
| 7 | wm6 S1 and S8 own the executor, its beat and its adapter contract | cite | AGREES | sb7:91 against wm6:45-54 (S1, the supervisor and its beat) and wm6:113-122 (S8, the adapter contract). Neither section moved in `66f7b8d32` |
| 7 | wm6 S8 supplies `point.command-adapters` | cite | AGREES | sb7:102 against wm6:6 (`**Carries:** node:point.command-adapters`) and wm6:113 |
| 7 | S6's row (`point`, `name`, `class = "idempotent"`, `run`) fits the S8 contract | cite | AGREES | sb7:73-76 against wm6:114-116 ("declares `run`, an argv, and `class`, `idempotent` or `reconcile`", with `probe` only for `reconcile`). The `point =` and `name =` keys follow wm20's `[[adapter]]` shape (wm20:148-150) |
| 7 | The supervisor runs Build's `build.core` item, an `executor`-actor item (flow-steps:298), through that row | cite | AGREES | sb7:75-76 against wm6:52 and :118 ("runs a command item only through its row"). wm25:93 routes `executor` like `command`, "a command item run through its adapter row (its S8)" |
| 7 | The supervisor matches the item to S6's row by `name = "build.core"`, and runs `run` as `--build-core <slug>` with the build's slug | cite | UNKNOWN UNTIL BUILT | sb7:54, :74-75 against wm6:113-122. S8 states neither how a command item finds "its row" nor whether a `run` argv takes a per-build argument. The three rows wm6 registers (lander, record door, bar) take no slug |
| 7 | `python supervise.py --check-adapters` passes S6's row and refuses it once `class` is removed (AC7) | cite | AGREES | sb7:241-244 against wm6:116-118 (`check_command_adapter_row` refuses a row with no `class`, and `--check-adapters` runs it over every row) and wm6:296-299 (AC7) |
| 7 | wm6's `points.toml` is a build-run precondition for S6's row | cite | AGREES | sb7:174-176 against wm6:229 (`tools/runtime/points.toml`: the `point.command-adapters` row). The file itself comes from wm20 (wm6:169), which wm6 already consumes |
| 1 | No read of a lease's session, `lease`-mode class or epoch | RH | AGREES | sb1 contains no lease, epoch, `--claims`, `read_claims`, holder or `refs/gov` term. Its one "mine" (sb1:162) is attribution's "not mine", not a lease class |
| 7 | No read of a lease's session, `lease`-mode class or epoch | RH | AGREES | sb7 contains none of those terms. Its beat and fence are wm6's (sb7:91), and it reads no lease itself |

2. MISMATCH

- **sb1:108.** The spec says: "A file-backed transition record for `build.exit`: the executor's (TOOL-dWellOiledMachine-6)." wm6 never names a transition record. Its witness wording is "a `reconcile` row's probe first, a landed effect recorded as the item's witness and not run again" (wm6:118-119). The record is TOOL-dDeclaredLoop-3's: "The writer, `write_transition`" (dl3:60). dWellOiledMachine's units record through it by subprocess, for example "the loop kit's verb `python loop_transition.py record --build <slug> --from <state> --item" (wm3:60). Flow-steps:299 makes `build.exit` a `command` item whose output is "the transition record".
  Change: re-point the non-goal's owner to TOOL-dDeclaredLoop-3's `write_transition`, reached through `loop_transition.py record`, which the `build.exit` command item runs. Drop the wm6 attribution, so a builder does not expect the supervisor to write that record.
  Cause: pre-existing. wm6 already had no transition record at `5f0b11f12`.

3. UNKNOWN UNTIL BUILT

- sb7 S6's `name`-to-item match and its `run` argv carrying `<slug>` depend on wm6 S8 as built. Its build run decides how `supervise.py` finds a command item's row and whether a `run` argv takes the build's slug.

4. Rule-wide hits RH does not bind

- The specs use "lease" for something else. sb5:6, :32-50, sb12:160-161, sb34:27, :48, sb35:88-89, :161, :219, :335-336, :409, sb38:27, :65, :76, sb40:28 and sb41:97 all mean the unit write-set lease (`item.build.unit-lease`, `routed_commits.py --unit-lease`, `readUnitLease`). sb3:268 is a rejected alternative, also about the unit write lease. None of these reads a build lease's session, class or epoch. This list corrects the brief: its probe reported spec 5's "§8 F6" as the one hit, but `lease` alone returns all of these.
- Parent-text observations, not rows:
  - wm6:179's external edge still reads "the epoch read §8 F4 asks for" and does not name tr2 F6 (a)'s holder verb, which S6 and S7 now name.
  - wm6's rev-5 re-points its F6 citation to `tr2:337-354`, but tr2's F6 runs from :340 to :357; :337-339 is F5.

5. Revised parent sections cited but not depended on

- **Spec 1:** it cites TOOL-dWellOiledMachine-6 with no section. None of the revised sections (S6, S7, §8 F4) is cited or depended on.
- **Spec 7:** it cites wm6 S1 and S8, both unrevised. It cites none of the revised sections. S1's beat starts with "S7's fence read" (wm6:48), but spec 7 only names the beat as a non-goal (sb7:91) and relies on nothing in S7.

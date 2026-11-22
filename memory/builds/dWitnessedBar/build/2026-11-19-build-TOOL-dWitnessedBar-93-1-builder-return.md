**Serves:** journal TOOL-dWitnessedBar-93

# TOOL-dWitnessedBar-93 — builder return 1 (run `wf_731cf43b-9d4`), committed 4bb681e94

## Why

Spec rev-2 can be built as written. Its claims match the tree: at 3ffc6c67c, spec-92 lines 314-328 hold the note check, its placement line is the `grep -qvE ... && {` line, and lines 296-299 hold the four shared-label `92|S4` rows. Unit 92's ledger has exactly one `- AC4` line, and it reads OWED. This is a records-only unit: no code file, no function minted. The brief was already on record, unchanged, at 23bb5b96a1ff. No write was needed outside the declared set.

## Summary

TOOL-dWitnessedBar-93 is committed as 4bb681e94 on base 2ac88ccaf, with subject naming the unit and a `Pass: TOOL-dWitnessedBar-93` trailer beside Co-Authored-By. The commit-msg and staged memory-hygiene hooks passed; the hook also added `Commit-Checked: unattended@1.129`.

What the commit holds:
- New acceptance ledger at C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-93-1-acceptance-ledger.md, with one line per criterion, each opening with a backticked token from that criterion: AC1 `NOTES OK 2`, AC2 `MISPLACED 92 S4 resolve_python:`, AC3 `NOTES OK 1`. All three are marked OWED to the close.
- The spec status header moved from INPROGRESS to CLOSED. The date stays 2026-11-21, which is today, and nothing else in the spec was hand-edited.
- RUN.md, with its already-staged dispatch row.
- Files rewritten by `gen_build_index.py --write`: memory/LIVE.md, memory/backlog/TOOL.md, the build README, and the spec's gen:spec-records region, which gained the ledger row. With no unit left INPROGRESS, the generator now shows the build and TOOL-dWitnessedBar-31 as DEFERRED, with TOOL-dWitnessedBar-31's advanced-by pointer moved to TOOL-dWitnessedBar-28. Unit 92's pass commit 27a6568ef made the same flip.

The check that ran, a fixture probe (standing in for AC1 and AC2, which the close owes): I cut 92 §4's note check from spec-92 at 3ffc6c67c into the scratchpad. I made a copy with S1's line swapped in, and diff showed that this one line was the only change. I then ran both from a scratch root holding a fake 88 ledger with the `TOOL-dWitnessedBar-92 S4` note under `- AC6` and under `- AC18`, fed both `92|S4|88` rows:
- S1's script printed `NOTES OK 2` and exited 0.
- The original script printed `MISPLACED 92 S4 resolve_python:` twice and exited 1.
- With the AC18 note removed, S1's script printed `MISPLACED 92 S4 resolve_python:` once and exited 1, so the failing case was seen.

These pass-time results are recorded in the ledger, marked PINNED, beside the OWED marks.

Owed to the main loop at the close:
- AC1 and AC2 fixture runs, with the fragments from units 94, 96 and 97 combined with S1's line.
- S3's note: a continuation line labelled `TOOL-dWitnessedBar-93 S3` carrying `NOTES OK 2`, under `- AC4` in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md.
- AC3's run of the note check fed `93|S3|92|AC4|NOTES OK 2`.
- The section 7 gates: `memory hygiene`, `recall floor`, `recall floor arms`.

The spec declares no `New arm:` line, so no first-failure observation of a new arm is owed. No gate, suite or bar ran.

Bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) exited 0 and selected 28 classes. The ones that apply here were checked:
- Each ledger token sits on one physical line.
- No pipe sits inside a table cell.
- No inline fence.
- `**Serves:**` is present.
- The probe's failing case was observed.

No other class needed action.

help/reference/drive.md and help/reference/units.md were already modified in the worktree before this pass. I left them unstaged and untouched.

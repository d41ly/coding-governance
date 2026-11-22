**Serves:** journal TOOL-dWitnessedBar-92

# TOOL-dWitnessedBar-92 — builder return 1 (run `wf_4d5a4d22-af9`), committed 27a6568ef

## Why

TOOL-dWitnessedBar-92 is built and committed. It writes records only, as rev-3 says. I found no divergence: before any write I checked the spec's claims against the tree at 1e38f6eb1 and every one held. (1) The anchored count `grep -c 'sha)[[:space:]]*rec_sha="' .githooks/pre-push` printed 0. (2) The suite's `rgf_ok` case-line count printed 2. (3) The three floor comments each counted 1, at lines 696, 20 and 412. (4) `GENERATED_INDEXES` names none of LIVE.md, ledger or backlog. (5) This unit's dispatch row names its own spec file and never the spec directory. (6) Pass commits 05fdf49d3 and b5a33a39c each change only their own spec under `spec/`. The orientation card calls the unit "Tier-2 at DEFERRED", but that is out of date: the spec header read INPROGRESS. The `--brief` call answered "already recorded, unchanged".

## Summary

Commit 27a6568ef is the pass for TOOL-dWitnessedBar-92. It changes 6 files: the new acceptance ledger, the spec's status header and its gen:spec-records region, `RUN.md` (the dispatch row that was already staged), and the README, `memory/backlog/TOOL.md` and `memory/LIVE.md` as `gen_build_index.py --write` rendered them. The trailer block carries `Pass: TOOL-dWitnessedBar-92` and Co-Authored-By. The only spec edit is CLOSED in the status header; its date was already 2026-11-21.

The regenerated index now shows the build and TOOL-dWitnessedBar-31 as DEFERRED, and the -31 backlog row names TOOL-dWitnessedBar-28. That follows from unit 28 being the only open unit; I did not edit it.

New ledger: C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md. It has one answer per criterion, AC1 to AC12, each opening with a backticked token taken from that criterion.

Checks that ran here (probes, no gate):
- **AC1:** the anchored grep on the built hook printed 0. It stands in for the close-time AC1 reading.
- **AC8:** each of the three `grep -c` probes printed 1, and the suite was never run. This is S9's pass-time reading.
- **AC5 dispatch half:** the dispatch row piped to the spec-directory count printed 0, before and after the commit. The pass-commit read covered 0 paths. The `GENERATED_INDEXES` read came back clean.
- **AC7 positive half, after the commit:** `gen_build_index.py --write` through `resolve_python` printed rc=0, and `git status --porcelain --untracked-files=no -- memory/` printed nothing.

All of these stand in for the `memory hygiene` leg's view of this unit's records. The commit hook's staged hygiene, including check 23 over this unit, let the commit through.

Owed to the main loop at the close:
- every note in the ledgers of units 87 to 90 (note rows 90|* and 92|*), and every run of §4's note check behind AC1 to AC12;
- AC2: the two scratch clones from 90 AC1 plus the third clone;
- AC3, AC4, AC6 and AC12: their scratch-ledger stagings;
- AC5: the scratch clone's three `--check-commit` stagings;
- AC7: the `py=false` staging;
- AC11: §4's owner derivation on the built tree and its stagings;
- AC10: the absent-phrase read;
- the gates `memory hygiene`, `recall floor` and `recall floor arms`.

There are no new arms, so no RED-first observation is owed.

`gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 28 classes. I checked the ones that apply. No ledger token is wrapped: every answer is one physical line. There is no triple-backtick fence and no table pipe. The `**Serves:**` line is present. The backslashes in the AC2 grep came through the write intact. Nothing needed fixing.

No command timed out and nothing was skipped. `help/reference/drive.md` and `help/reference/units.md` were already modified in the working tree before this pass; I left them unstaged and untouched.

**Serves:** journal TOOL-dWitnessedBar-95

# TOOL-dWitnessedBar-95 — builder return 1 (run `wf_98e38fc9-a02`), committed 5ec78f578

## Why

TOOL-dWitnessedBar-95 is built as its rev-2 spec says. It changes records only: no code file, no function. The pass writes the unit's acceptance ledger and moves its status to CLOSED. AC1 was observed at the pass, and the spec's Rollout puts the rest at the close.

## Summary

The unit is committed as 5ec78f578 on top of base 4cd455e5c. AC1 was observed at the pass; AC2 and AC3 were probed and still owe their runs at the close; AC4 and its note are owed to the close.

**Pre-build check:** the spec's claims about the code hold in the tree. `read_pass_declarations` prints every key unless given `current`, and `covers` and `is_repo_root` behave as the spec says (both in `tools/unattended/lib-unattended.sh`). `check_commit_message` in `tools/unattended/unattended.sh` reads the declarations in `current` mode and admits a path through `covers`. The run-state file has one dispatch row for unit 92, `item 5518fe43`. No divergence was found.

**What the commit holds** (files staged by name; the unstaged `help/reference/drive.md` and `help/reference/units.md` were left alone):
- the new ledger `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-95-1-acceptance-ledger.md`, one line per criterion, each opening with a token that criterion spells
- the spec's status changed from INPROGRESS to CLOSED; its date was already 2026-11-21
- the `RUN.md` dispatch row the main loop had staged
- the files `gen_build_index.py --write` rewrote: `memory/LIVE.md`, `memory/backlog/TOOL.md`, `memory/builds/dWitnessedBar/README.md`, and one new row in the spec's generated records table
- the `Pass: TOOL-dWitnessedBar-95` trailer and one `Decided:` line

The `--brief` verb answered "brief already recorded, unchanged". The commit hooks passed.

**Checks run** (these stand in for the acceptance criteria; no gate, suite or bar ran):
- **AC1, observed:** the spec's §4 grant check, cut from the spec and run over the live `RUN.md`, printed `ROWS 1 WIDE 0`, exit 0.
- **AC2, probed:** a scratch copy with a unit-92 row declaring `memory/builds/dWitnessedBar/` printed `GRANTS SPEC memory/builds/dWitnessedBar/` and `ROWS 2 WIDE 1`, exit 1. With `memory` in its place it printed `GRANTS SPEC memory` and `ROWS 2 WIDE 1`, exit 1. Unit 92 AC5's literal count printed 0 over both copies.
- **AC3, probed:** with every unit-92 dispatch row removed, it printed `ROWS 0 WIDE 0`, exit 1.
- **AC4, probed:** unit 92's note check fed the two `95|S3` rows printed `NO NOTE` twice, exit 1, over the live ledger. Over a scratch copy holding the S3 note it printed `NOTES OK 2`, exit 0, both with spec-92's script and with unit 94's continuation-line pattern.

The probes stand in for the spec's legs of §7 (`memory hygiene`, `recall floor`, `recall floor arms`), which are the main loop's at the close.

**Owed at the close:**
- the AC2 and AC3 scratch-copy runs
- the S3 note, a continuation line labelled `TOOL-dWitnessedBar-95 S3` under `- AC5` in `2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md`, carrying the backticked `WIDE 0` and the word `covers`, and AC4's note-check read of it
- the legs of §7

This unit adds no new arm, so no RED-first observation is owed.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 28 classes. I checked the ones this commit could hit: each ledger token is on one line and spelled by its own criterion, the record carries its Serves line, AC3 shows an empty read reds rather than passing, and the heredoc commit message has no backslashes. Nothing needed fixing. No command timed out or was skipped.

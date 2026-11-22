**Serves:** journal TOOL-dWitnessedBar-96

# TOOL-dWitnessedBar-96 — builder return 1 (run `wf_55c93f59-2d0`), committed 73fc3773b

## Why

TOOL-dWitnessedBar-96 is records only. The spec's claims about current code all held at base. Spec-92's note check and the resolve-python.sh lines it cites have not changed since 3ffc6c67c (git diff --stat printed nothing). The spec's lines 317 and 321, rows 284 and 296 to 299, and the one `- AC4` answer in unit 92's ledger match what the spec says. So there was no divergence, and the unit was committed as its spec and brief describe.

## Summary

Commit 73fc3773b holds the pass for TOOL-dWitnessedBar-96, with a `Pass: TOOL-dWitnessedBar-96` trailer, two `Decided:` lines and the Co-Authored-By trailer. Its files:
- the new acceptance ledger C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-96-1-acceptance-ledger.md, one line per criterion AC1 to AC4, each opening with a backticked token that criterion spells and each marked OWED to the close;
- the spec's status header, INPROGRESS to CLOSED, date 2026-11-21;
- memory/builds/dWitnessedBar/RUN.md, holding the dispatch and brief rows;
- the files `gen_build_index.py --write` rewrote: memory/LIVE.md, memory/backlog/TOOL.md, memory/builds/dWitnessedBar/README.md, and the spec's gen:spec-records region, which gained the ledger row as the spec's Files touched allows.

Every path is inside the declared `--dispatch` write set. The `--brief` verb reported the brief already recorded and unchanged.

Side effect to note: unit 96 was the last INPROGRESS unit, so the generator now derives the build status, and TOOL-dWitnessedBar-31's backlog row, as DEFERRED (units 28 and 97 remain DEFERRED). It is recorded as a `Decided:` line.

**What ran (probes only):** I cut spec-92's note check (lines 315 to 327) into the scratchpad as note92.sh, plus a copy with S1's three fragments as note96.sh. I ran them from scratch roots under C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u96. These probes stand in for the close-time fixture runs of AC1 to AC4; they are not a gate leg.
- **AC1:** `NOTES OK 1`, exit 0. It also passed with the real absolute python.exe path `resolve_python` printed on this node.
- **AC2:** `NO NOTE 92 S4 resolve_python:`, exit 1, through S1 with S3's row; `NOTES OK 1`, exit 0, through the unreplaced script.
- **AC3:** `NO NOTE 90 S10 AC4 AC6 AC7 AC10 AC12`, exit 1, and `NOTES OK 1` on the five-criterion span.
- **AC4:** `NO NOTE`, exit 1, over the live unit-92 ledger, which is expected because S5's note is not written yet; `NOTES OK 1` over a scratch ledger holding S5's note.

**Owed to the main loop at the close:**
- the fixture runs of AC1 to AC3;
- S5's note in the 2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md ledger, as a continuation line under `- AC4` labelled `TOOL-dWitnessedBar-96 S5` and carrying the backticked `resolve_python: , exit 0`;
- AC4's read of that note;
- the §7 gate legs `memory hygiene`, `recall floor` and `recall floor arms`.

The unit declares no `New arm:` line, so no RED-first observation is owed. The commit-msg hook's staged hygiene ran during the commit and passed. No merge bar, suite or self-test ran, and no command timed out or was skipped.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 28 classes. I checked the ones that apply, and none needed a change:
- each ledger token sits on one physical line, so no token wraps across lines;
- the ledger has no triple-backtick fence;
- the ledger carries its `**Serves:**` line;
- the pipe-holding token is in a list line, not a table cell;
- AC1 was also probed with the real resolver value, not only a made-up one.

The uncommitted help/reference/drive.md and help/reference/units.md changes were already in the tree before this pass. They are not this unit's, and I did not stage them.

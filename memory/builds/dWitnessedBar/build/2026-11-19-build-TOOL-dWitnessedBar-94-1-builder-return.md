**Serves:** journal TOOL-dWitnessedBar-94

# TOOL-dWitnessedBar-94 — builder return 1 (run `wf_6ba08f04-2a9`), committed 58b8e5283

## Why

TOOL-dWitnessedBar-94 is a records-only unit at rev-2, status INPROGRESS. Every claim its spec makes about the current tree checked out before the first write. Spec-92 line 321 carries the unanchored `k="TOOL-dWitnessedBar-` fragment. Lines 330-331 and line 433 carry the own-line limit and the risk clause. Unit 92 is CLOSED at rev-3. Unit 92's ledger is the one file its glob matches, and `grep -cE '^- AC3 '` over it prints 1. So the spec builds as written and there was no divergence. The orientation card's 'Tier-2 at DEFERRED' was stale: the spec header already read INPROGRESS.

## Summary

TOOL-dWitnessedBar-94 is committed as 58b8e5283 on base 05ab4b7fc. It changes records only, no code file. The commit's last trailer lines are `Pass: TOOL-dWitnessedBar-94` and the Co-Authored-By line.

**What the commit holds:**
- A new acceptance ledger, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-94-1-acceptance-ledger.md. It has one line per criterion, AC1 to AC4, each opening with a backticked token that criterion spells.
- The spec's status header moved from INPROGRESS to CLOSED, with the date already 2026-11-21. The only other change in the spec is the ledger's new row in its generated records region.
- `gen_build_index.py --write` output: memory/LIVE.md, memory/backlog/TOOL.md and memory/builds/dWitnessedBar/README.md.
- The `--dispatch` row already staged in RUN.md.

All paths were in the declared write set. The `--brief` row for this unit was already in RUN.md, so I did not run that command again.

**One generated change to look at:** with this unit CLOSED and units 95 and 96 still DEFERRED, the index now derives build dWitnessedBar as DEFERRED where it said INPROGRESS. TOOL-dWitnessedBar-31's row also moved to DEFERRED, and its blocker column now names TOOL-dWitnessedBar-28. I committed it as the generator wrote it.

**Checks that ran:** a probe of the spec's own script, standing in for the fixture runs AC1 to AC3 owe at the close. I cut spec-92 lines 315-327 into a script, made a copy with S1's pattern `^  +TOOL-dWitnessedBar-$u $s([^0-9]|\$)`, and ran both over scratch roots under the scratchpad's u94 folder. Every result matched the spec:
- **AC1:** S1's pattern printed `NO NOTE 90 S1`, exit 1; the unchanged script printed `NOTES OK 2`, exit 0, on the same input.
- **AC2:** with the two-space continuation note added, it printed `NOTES OK 2`, exit 0.
- **AC3:** S1's pattern printed `NO NOTE 90 S1`, exit 1; the unchanged script printed `NOTES OK 1`.
- **AC4 setup:** over the live unit-92 ledger it printed `NO NOTE 94 S3 NO NOTE 90 S1`, exit 1. Over a scratch copy with S3's note under `- AC3` it printed `NOTES OK 1`, exit 0.
- **Extra probe:** a note written one space in reads as no note, as the spec's risk line says.

The commit-msg hook ran the staged memory-hygiene check and passed it (exit 0), with its whole-tree and push-boundary parts held back until the push. `gotchas.py --for-diff HEAD~1..HEAD` selected 28 bug classes; I checked the ones that touch these files:
- Each ledger token sits on one physical line.
- There are no tables or inline fences.
- Each fixture has a control that comes out the opposite way, so none passes by finding nothing.
- The ledger has its Serves line.

Nothing needed fixing.

**Owed to the main loop at the close:**
- The runs of AC1, AC2 and AC3, with the fragments of units 93, 96 and 97 composed beside S1's pattern.
- S3's note, labelled `TOOL-dWitnessedBar-94 S3`, in unit 92's ledger: two spaces in under its `- AC3` answer, carrying the backticked `NO NOTE 90 S1`.
- AC4's read of that note, which should print `NOTES OK 1`.
- Spec section 7's legs: memory hygiene, recall floor and recall floor arms.

This unit declares no `New arm:` line, so no RED-first observation is owed for it. No gate, suite or bar ran, and nothing timed out or was skipped.

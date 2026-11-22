**Serves:** journal TOOL-dWitnessedBar-82

# TOOL-dWitnessedBar-82 — builder return 1 (run `wf_38852847-053`), committed e8cdc8e3c2318f057c10735ecee3e95119d46a24

## Why

The spec builds as written. Every claim it makes about current code still holds at HEAD 0e50d28b: tools/run-gates/run-gates.gov.test.sh has not changed since 0e5103294. Lines 243, 246, 247, 1263 and 1265, the counted lines at 999 and 1012, the fourth-record arm at 1002-1014 and the `_rg_v:1}` call at 951-952 are all where it says. check-testsuite-counts.sh requires a bare `^FLOOR_ASSERTIONS=[0-9]+$` line, unattended-build.js sorts by order then id, 28 specs carry the New-arm line, and sh_hygiene counts code lines only. The Files touched list covers every path written. The generated index outputs (README, LIVE, the TOOL backlog shard, the spec's records block) were in the dispatch set. RUN.md went in the same commit.

## Summary

Built TOOL-dWitnessedBar-82 as one pass commit, e8cdc8e3c, on base 0e50d28b. The commit carries the `Pass: TOOL-dWitnessedBar-82` trailer and moves the spec's status from INPROGRESS to CLOSED, with no other change to the spec.

**What changed**
- **The floor (S1):** in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh the `FLOOR_ASSERTIONS=` line now reads 74 instead of 72 and stays bare. A new `# RAISED 72 -> 74 by TOOL-dWitnessedBar-82 on 2026-11-21` comment sits directly below it. It says the floor counts every arm built through order 43: unit 73's 72, plus unit 78's two new records (S7's every-key record and S13's line-rule record) at one each. Units 74, 76, 77, 79 and 80 add none. Only comment lines and the value changed, so the suite's shell-role row stands and no widen record was written.
- **The three ledger lines (S3):** the acceptance ledgers of units 76, 77 and 78 each gained one line naming `FLOOR_ASSERTIONS` and TOOL-dWitnessedBar-82 S1. I wrote them in this pass because Files touched and the brief both name them as this unit's writes. The main loop should not write them again at the close: AC3 wants exactly one such line per ledger.
- **This unit's ledger:** C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-82-1-acceptance-ledger.md has one line each for AC1, AC2 and AC3. It deliberately does not contain the phrase `below the pinned floor`, so the close's AC2 grep prints only the two lines the main loop adds.
- The index generator (gen_build_index.py --write) rewrote four files, all committed. They now show the build's status as DEFERRED, because no unit is in progress any more.

**Checks run (no gate, suite or bar ran)**
- `bash -n` on the suite passed.
- A counting script, C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/count82.py, counts each `a=$((a+k))` line and multiplies a line inside a loop by the loop's word list. It found 74 on the built suite and 72 on unit 73's version at 563d828df. This stands in for the `run-gates gov canary` PASS count that AC1 needs.
- The same script over two scratch copies stands in for the AC2 red runs:
  - with unit 78's fourth-record arm deleted it counts 73, one short of the floor, so that copy should fail;
  - with unit 79's length-variant call deleted it counts 74, so that copy still passes at this pass, as S2 says. It only fails after unit 85 makes the variants count.
- The AC3 grep printed exactly one line in each of the three ledgers, each naming TOOL-dWitnessedBar-82. This stands in for the close's AC3 grep and the `memory hygiene` leg.
- The commit hook's staged hygiene checks passed. The bug-class checklist (gotchas.py --for-diff HEAD~1..HEAD) selected 30 classes. I went through the relevant ones, including tokens wrapped across lines, a count that must match what the grader counts, and a criterion asserting what its command cannot show; none needed a change.
- Nothing hit its timeout and nothing was skipped.

**Owed to the main loop at the close**
- AC1: in a scratch clone at e8cdc8e3c, the arm prints `PASS (74 assertions)`, matching the `FLOOR_ASSERTIONS=` grep.
- AC2, which is also the New-arm line's RED-first observation: in a scratch clone whose suite copy lacks unit 78 S13's fourth-record arm (lines 1008-1020 after this edit), the arm prints the `below the pinned floor` line and exits non-zero. A copy lacking the `'${_rg_v:1}'` call (lines 957-958) prints PASS at this pass. Unit 86 S2 records that, and it only fails once unit 85 lands. Both resulting lines go in this unit's ledger, plus a seen-red line.
- The legs of §7: `run-gates gov canary` (needs GATE_SELFTESTS), `memory hygiene`, `recall floor` and `recall floor arms`.

**Serves:** research TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37

# The promoted-fix pass's return — dRankedPlan round 2

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

All three hits are fixed in place. `check-memory-hygiene.sh --only 2,12,25` now exits 0, and no finding names a dRankedPlan file. It still prints "check 25 did not grade … READER NOT IN TREE covers it" lines for units 2, 3, 10, 16 and 29. Those are notices, not findings: they were in the run before my edits and sit on specs outside this brief.

None of the hits was a real retirement, so I added no `**Readers:**` clause; each fix was a reword. Every `**Carries:**` line, §3 edge, §8 mark and status header is as it was, and nothing is committed.

**Hit 1: hygiene check 25.** In each file the retirement word sat beside a backticked token without retiring anything named. The run before my edits flagged these same three items, and a copy of the trigger I ran over every dRankedPlan spec now finds no other.
- **`-32.md` S2:** "dropped", next to `*.sh`, described how comments are read. The text was "`shlex.split` with comments dropped" and is now "with comments ignored".
- **`-33.md` S2:** "removes" and "replaces" described what three plants set up, next to `tFix`. They now read: `plan-record-absent` "leaves the build with no record", `plan-record-unread` "leaves the repository with no copied memory-tree kit", and `plan-record-open-probe` "writes its own record with its eleven fields in place of the seed".
- **`-37.md` S15:** "dropped", next to the `unattended.test.sh` path, described a test needle. "reds when the flag is dropped" is now "reds on a recipe that lacks the flag".

**Hit 2: `[handoff]` for `ratify.py "$slug"`.** Unit 37 really does read this invocation. Its S16 is the item for finding 31, and its `caller-shell-bare` plant is exactly that bare hook call (`"$py" "$d/ratify.py" "$slug"`). So the fix is in unit 37 and unit 32's bullet stands. S16 now says "the bare `ratify.py "$slug"` form `TOOL-dRankedPlan-32` S2 reads". A grep finds the token once in `-37.md`.

**Hit 3: `[path]` in `-37.md` §6.** AC11 now names the files by basename: the loop kit's `ratify.py`, and the memory-tree kit's `plan_record.py` and `plan_fields.py`, "each under `{prefix}` as S13 spells it". The full `{prefix}/…` paths are unchanged in §2 S13, and `tools/memory-tree/plan_fields.py` is unchanged in Files touched.

I did not run `check-spec-tokens.py`; the main loop re-runs it. Hit 2's token is confirmed by grep, and none of the paths left in §6 of `-37.md` is one of the three the hit named.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-32.md
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-33.md
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-37.md

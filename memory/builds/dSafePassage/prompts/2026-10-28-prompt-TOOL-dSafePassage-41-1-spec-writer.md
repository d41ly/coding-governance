**Serves:** research TOOL-dSafePassage-41

# Brief: TOOL-dSafePassage-41's AC2 observes the live tree during the pass, not after the build closes it

## The prompt

No owner prompt. The build run's builder handed TOOL-dSafePassage-41 back as a DIVERGENCE (`wf_9320419a-545`, HEAD `c2ee6f0f5`), and the run revises the spec under M2.

## The brief

### Goal

AC2 observes the `ac-order` join grading a non-empty live population on the real tree. It does not depend on specs that the unattended harness flips straight from DEFERRED to CLOSED.

**What the builder measured.**
- The join grades only the specs that `LIVE` matches (`tools/check-spec-tokens.py:331`: OPEN, SPECCED, INPROGRESS, BLOCKED). The module docstring counts a DEFERRED spec as terminal.
- Under the build run, every dSafePassage spec is CLOSED or DEFERRED. The one exception is the unit being built, which is INPROGRESS during its pass.
- No other build has a live spec dated 2026-10-23 or later: dDeclaredLoop's are DEFERRED, and dClosedLoop's is dated 2026-10-20.
- A probe of the join's own predicate over the tree, run with this spec at INPROGRESS (`C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/ao41_pred.py`), graded 1 of 37 live specs, this one, with 0 out of order.
- Once the pass commit flips this spec to CLOSED, the count is 0. That is AC2's own red case, and the empty population the `[gate]` rule forbids reading as coverage.
- AC1 is buildable as written. The builder's join patch is kept at `scratchpad/TOOL-dSafePassage-41-join.patch`, and its fixture runs are recorded in the hand-back.

**The main loop's disposition.**
- AC2 is observed during the pass, with this spec at INPROGRESS: the join's run line grades at least 1 live spec dated on or after the key, and finds 0 out of order.
- AC2 states that the same line at the close may grade 0, because the harness closes every spec. Under `[gate]`, that 0 is not coverage. Coverage is AC1's fixture plus this pass-time observation.
- Cite hygiene check 29's identical note: "under the unattended harness a spec goes OPEN to CLOSED in its build commit, so this check grades attended builds only".
- Do not widen `LIVE`, and do not move the key. Both are non-goals, and TOOL-dSafePassage-34's.

### Items

1. **Revise TOOL-dSafePassage-41** as a rev bump dated 2026-10-28, still `DEFERRED`:
   - restate AC2 and its Red-when as above;
   - correct §1's and §4's order-table claim that the join grades specs dated 2026-10-23 or later, so it says which of those are live and when;
   - add one §9 line naming this brief.
2. **Cross-read** TOOL-dSafePassage-34 §4's "a join seen grading nothing is not a gate", and TOOL-dSafePassage-46 and -42, which read 41's join. Fix a DEFERRED disagreement in place. CLOSED specs are read-only.
3. **Commit nothing.** Return the files you wrote.

### Acceptance

- AC2 names the INPROGRESS observation, the close-time 0, and check 29's note.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code.
- No change to `LIVE` or to the key.
- No edit to a CLOSED spec.
- No commit, and no stage into the real index.

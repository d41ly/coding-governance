**Serves:** research PLAY-dOrderedCharter-55

# Brief: specs 39, 49 and 55 — the spec-shape and readers checks over their pre-check folds

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The commit of the pre-check folds of specs 39 (rev-5), 49 (rev-9) and 55 (rev-7) was refused by memory
hygiene's pre-commit checks 12 and 25; specs 31 and 54 committed without them.

## The brief

### Goal

Fix the scratch copies of specs 39, 49 and 55 so memory hygiene's checks 12 and 25 pass over each, with no change in what the spec
builds.

### Items

1. **Where you write.** Edit only these scratch copies; write nothing under the repository:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold39/2026-10-24-spec-PLAY-dOrderedCharter-39.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold49/2026-10-24-spec-PLAY-dOrderedCharter-49.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold55/2026-10-24-spec-PLAY-dOrderedCharter-55.md`
2. **The failures, as the pre-commit hook printed them:**
   - Check 12, spec 49: acceptance bullets AC13, AC50 and AC60 name no backticked witness, required at or after `SPEC_WITNESS_CUTOFF`.
   - Check 25, spec 39: S3 retires a named thing and carries no **Readers:** clause.
   - Check 25, spec 39: S1's `by name:` half lists `git grep -n -F "agent-instructions wiring"`, which no reader spells and no
     tracked path is or ends with; name a reader that spells it, or write READER NOT IN TREE and a reason on that half.
   - Check 25, spec 49: S34's `by value:` half names no backticked reader and carries no NO VALUE READERS followed by a reason.
   - Check 25, spec 55: S12's `by value:` half, the same.
3. Every reader you name is a grep at HEAD. A witness is the backticked token the criterion observes.
4. To check without touching the repository, copy each fixed spec into a scratch clone or fixture of your own and run
   `bash tools/check-memory-hygiene.sh --only 12` and `--only 25` there, or read both checks in `tools/check-memory-hygiene.sh` and
   apply them by hand; say which in your return.
5. The spec-token rules still hold for any acceptance bullet you touch: no untracked path in a command's words, no `path#symbol`, no
   suite as the observation, each backticked span on one line.

Bump no rev: add a revision-log line to each spec's current rev naming this brief and the items it touches.

### Acceptance

- Checks 12 and 25 pass over all three scratch copies, and each change has a revision-log line.

### Gates

None run on the repository. The main loop copies the specs in and commits them through the pre-commit hook.

### Non-goals

- No code. No edit outside the three scratch copies. No change to what any scope item or criterion builds.

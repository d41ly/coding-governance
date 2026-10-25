**Serves:** research TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67

# Round-6 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-66-1-spec-writer.md`, run direct/a34a00e1f86b95e5a, one per stop, extracted from its transcript by script.

## Return 1

I've cleared all three check-25 hits from units 66 and 67. None of the three items actually retired a name. Each one described a staged break: the fault the test plants on a scratch copy to show it can fail. So I reworded each to keep its meaning, and added no `**Readers:**` clause.

| Unit | Item | What I did |
|---|---|---|
| TOOL-dWitnessedBar-66 | S4 | **Reworded.** "the CR strip removed from `read_green_file`'s `sha` read, and that read restored to printing every match" now reads "a `read_green_file` whose `sha` read keeps the CR, and one whose `sha` read prints every match again". Same two breaks, same variable (`rec_sha`). |
| TOOL-dWitnessedBar-67 | S2 | **Reworded.** "the CR strip removed from `read_green_file`'s `fingerprint` read" now reads "a `read_green_file` whose `fingerprint` read keeps the CR". It still reaches `rec_fp`. |
| TOOL-dWitnessedBar-67 | S3 | **Reworded.** "the `OSError` catch dropped … `is_file(follow_symlinks=False)` replaced by an existence test" now reads "a sweep with no `OSError` catch … a sweep that tests existence where unit 65 S11's sweep calls `is_file(follow_symlinks=False)`". That call is not in the tree yet (`git grep` under `tools/run-gates/` finds nothing); unit 65 S11 (spec line 101) adds it. |

**Checks**
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now prints no dWitnessedBar finding. It does still print five "check 25 did not grade … READER NOT IN TREE covers it" notices about units 20 (S2) and 24 (S14). Those were there before I started, they don't make the check fail, and those units are outside this brief.
- I could not confirm that `python tools/check-spec-tokens.py` still reads 0 dWitnessedBar hits. My role is blocked from running it, so the main session needs to run it. It should be unaffected: the three edits add no new backticked token, and only reuse ones already in the specs.

**Scope**
- Only those three §2 items changed (7 lines in, 7 out). No rev bump and no change to any `order` verb (64 at 36, 65 at 37, 66 at 38, 67 at 39). No other spec or deviation record touched. Nothing staged or committed, and the build-index generator was not run.
- In both units, the acceptance criteria and §7 `New arm:` lines still use the old "removed" wording for the same breaks (66 AC2; 67 AC2, AC9 and AC17). Check 25 only grades §2 and the brief said to change nothing else, so I left them.

**Byte count:** TOOL-dWitnessedBar-51 is 48697 bytes (`wc -c`, not edited).

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-66.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-67.md

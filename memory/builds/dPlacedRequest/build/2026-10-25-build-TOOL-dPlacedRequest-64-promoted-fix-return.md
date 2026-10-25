**Serves:** research TOOL-dPlacedRequest-64

# The promoted-fix pass — dPlacedRequest round 9, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-12-spec-writer.md`, run direct/a69cd3b69d4683057, extracted from its transcript by script.

I fixed the check 25 hit by rewording one scope item in TOOL-dPlacedRequest-64. After the fix, `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0. The "did not grade" notices it prints are all on other specs and do not gate.

**The hit on S14:** the item said "The claim that 57 AC2's `sed` range is the seam extended is dropped." "Dropped" is on the check's list of retirement verbs. S14 also cites code names (`extract_run_facts` and `tools/unattended/lib-unattended.sh`), which is what makes the check fire. But S14 retires nothing named: it corrects a reuse claim in 62 §10. So, following check 25 as the round-6 brief states it, I reworded the item rather than adding a `**Readers:**` clause.

**The edits, all to `C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-64.md`:**
- **S14** now reads "62 §10 makes no claim that 57 AC2's `sed` range is the seam extended." It means the same thing without a retirement verb, and AC14, which checks it, does not change.
- **Status header:** rev-1 became rev-2.
- **§9:** a rev-2 line records the rewording and why no `**Readers:**` clause is owed.

S12 also uses "drops", but it cites no code name in backticks, so the check passes it.

I staged the spec with `git add` so the hygiene run would see it. There is no commit, no index render and no other file touched.

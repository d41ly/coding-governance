**Serves:** research TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62

# Round-3 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-58-1-spec-writer.md`, run direct/ace6e5a56bad767bd, one per stop, extracted from its transcript by script.

## Return 1

I fixed all three findings in the round-3 fix brief. Each change is a single in-place edit at rev-1 with no rev bump, and I changed no other text. Units 59 and 61 were not edited.

The hygiene check `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now prints no dWitnessedBar finding and exits 0. I did not run `check-spec-tokens.py` because my role doesn't allow that gate. Instead I read its bar pattern and path rule and grepped the specs: none of the three flagged tokens is left, and both new path tokens are tracked files.

**TOOL-dWitnessedBar-60, check 25 on S3: reworded, because nothing is retired.** S3 retires no name. It only keeps an inherited `GATE_BASE_FROM` value away from the bar, and the word "dropped" is what tripped the check. I changed "and only an inherited one is dropped" to "and an inherited one never does", so the sentence still says the driver's own value reaches its bar and an inherited one does not. Since nothing is retired, no `**Readers:**` clause is needed.

**TOOL-dWitnessedBar-58, the [bar] hit in AC2.** AC2's opening said "When `run-gates.sh` runs scoped in a clean scratch clone". It now says "When the runner runs scoped over S2's one-leg fixture manifest in a clean scratch clone". That is the fixture run S2 describes, not the merge bar. The suite is still named on its existing `New arm:` line in §7, so no new arm was needed. The `run-gates.sh:<line>` citations elsewhere in the spec are not runs and were never flagged.

**TOOL-dWitnessedBar-62, the two [path] hits.**
- **AC18:** the backticked `--home sub/.git` is now "with `--home` naming the git dir of a nested repository beside it", so the fixture path is out of backticks.
- **AC21:** the colon-joined token is now "the pair of `memory/LIVE.md` and `tools/memory-tree/gen_build_index.py`, joined by a colon". Both paths are tracked at HEAD.

**TOOL-dWitnessedBar-51 byte count:** 48521 bytes, against the 49152 ceiling. I did not edit it.

As the brief said, I did not stage or commit, and did not run the build-index generator. My edits to 58, 60 and 62 are only in the working tree (git shows them as `AM`), so they need staging before the commit. The hygiene check read the working-tree files.

Files edited:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-58.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-60.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-62.md

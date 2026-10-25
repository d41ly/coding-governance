**Serves:** research TOOL-dWitnessedBar-51

# Round-10 size pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md`, run direct/a5c02543a8efcd064, one per stop, extracted from its transcript by script.

## Return 1

TOOL-dWitnessedBar-51 is trimmed from **49203 bytes to 47744** (`wc -c` on the whole file), under the 47800 target. The changes are in the working tree only: nothing staged or committed, and I did not run the generator.

**What I cut, by section** (scope items, criteria, Edges, `**Carries:**` tokens, `New arm:` lines and the `gen:` region are untouched; `git diff -U0` shows changes only in §1, §4, §8 and §9):

- **§1:** Merged the opening paragraph and the "That is 37 MEDIUM and 13 LOW" line into one. Dropped the sentence about the hands-off bullet, which §3's Edges already carry. Dropped "before the close's bar", and the review path still points at the audit.
- **§4:**
  - "Why one unit" is shorter but still lists all six write-set joins.
  - "The declarative keys" drops the row-hash and release-compare restatement, which S36 and S48 already say.
  - Migration drops a `run-gates.sh:3225` citation that Evidence already holds.
  - Rollout is shortened, and the `owed_rows.py` instruction is kept.
  - Alternatives drops the "one unit per minor" bullet, which §3's Non-goals already cover, and shortens the second one.
  - Evidence, Inventory, the shell-role derivation block and Files touched are unchanged.
- **§8:** I removed the option lists from F1, F2 and F4 and the past-tense context from F3. Every outcome is unchanged: each pick, its rung and reason, every `widens:`/`relaxes:` line, F2's full Bound/Tier/Reason bounding text, F3's `grants:` line, and F2's citations to `pre-push` and `unattended.sh`.
- **§9:** rev-1 and rev-2 are shortened (their details are in §1 and §3), and rev-3 is shortened to its unit 62 hands-off. The rev stays at rev-3, and the trim is recorded in rev-3 as one line: "Prose of §1, §4, §8 and §9 trimmed for the size ceiling; nothing else moved."

**Gates I ran:**
- **Lexicon `--check`:** passes.
- **Memory hygiene:** fails check 9, because the build index is out of date for the dWitnessedBar `README.md` and for spec 51. My edits didn't cause this. Two prompts you wrote this round serve unit 51 and are not yet in its records table: `prompts/2026-10-25-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md` and `prompts/2026-10-25-prompt-TOOL-dWitnessedBar-51-round10-size-brief.md`. Your re-render clears it.

**Watch the size after your re-render.** Those two new rows add about 342 bytes, so the spec should come out near 48086. That is still about 1066 under the 49152 ceiling, but at 100 to 150 bytes per round it buys roughly 7 to 10 more rounds, not a full 10.

Path: `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-51.md`

**Serves:** research TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63

# Round-5 fix pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-7-spec-writer.md`, run direct/a379f850674354f0b, extracted from its transcript by script.

I fixed both reds, one in each spec the brief names. Both specs stay `rev-1`, and nothing is committed. I ran the memory hygiene gate over the tree after the edits and it exited 0. I did not run the spec-tokens checker or regenerate the build index, so the M1 fix still needs a spec-tokens run to confirm it.

- **M1, `TOOL-dBoundRoles-62`:** §6 no longer spells `tools/roles/spawn-guard.test.sh`; the full path stays in §2, §4, Files touched and the §7 `New arm:` line.
  - **AC1** now greps the floor line over "the spawn-guard suite unit 25 adds" (path in S1 and Files touched). It then runs a scratch shell on just the floor and comparison lines, copied out by `grep`, with the count one below the floor and then equal to it. It says outright that no suite runs.
  - **AC4** now uses `grep -n '^New arm: .*spawn-guard'` over spec 58, which drops the code span with the trailing quote.
  - A search of §6 now finds 0 matches for the path.
- **M2, `TOOL-dBoundRoles-63`, S16:** the mention is now plain prose ("the Readers line of 53's S1"), followed by a real `**Readers:**` clause with both halves.
  - **by name:** spec 53's line 45, backticked as a tracked path so check 25 can resolve it; that is the line this item clears. The other hits from the `git grep` are listed in prose, without backticks so check 25 does not try to resolve them:
    - spec 53's line 41, which S11 clears;
    - spec 53's lines 26 and 76, which S11 keeps;
    - spec 59's lines 27, 52, 60, 82 and 164, which stay.
  - **by value:** `NO VALUE READERS`, because the item changes a citation in a spec's prose and no code reads it. The parse it pointed at stays in `tools/roles/handoff.py`, and spec 53 now cites it through `parse_read_key`.

Files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-62.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-63.md

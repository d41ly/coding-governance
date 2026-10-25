**Serves:** research TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57

# Round-2 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-1-spec-writer.md`, run direct/afc56d51d53055cc5, one per stop, extracted from its transcript by script.

## Return 1

Every finding in the round-2 fix brief is cleared, and unit 51 is now **47418 bytes**, under the 47500 target. I edited specs 51, 53, 55, 56 and 57. None got a rev bump, I touched no deviation record, and nothing is staged or committed.

The hygiene gate (`--only 2,12,25`) now shows no dWitnessedBar finding; the only dWitnessedBar lines left are the pre-existing "did not grade" notices on units 20 and 24. I did not run `check-spec-tokens.py`, because my role admits only the hygiene gate and the lexicon. Instead I fed my new criterion tokens to that file's own `BAR` and path checks: none hits, but the main loop still needs to run the real check.

**1. Check 25: all eight items were reworded; none got a `**Readers:**` clause.** None of them retires a named thing that a reader spells:
- **53 S1**: "removes the homes" is a test step that clears copied homes. It now reads "clears each home from the work tree".
- **55 S1**: "one trailing CR dropped" is byte cleanup. It now reads "cut".
- **56 S2**: "drops one trailing CR" now reads "cuts".
- **56 S13**: "removes a temp", and unit 42's skip of temps being "replaced", describe a behaviour, not a name. It now reads "unlinks a temp …; this rule supersedes unit 42's skip of temps".
- **56 S15**: a temporary signers file "removed after the read" now reads "unlinked".
- **57 S4**: "the predicate drops" now reads "excludes", and "removes it" now reads "takes that line out". The thing removed is a `refuse_wrong_shell || exit 2` call line; the name stays defined.
- **57 S13**: the old `.toml` basename's retirement belongs to unit 16, whose S6 already carries the Readers clause. S13 now speaks of the "pre-rename `.toml` basename, whose readers unit 16 S6 answers for".
- **57 S15**: "drops `fix-of`" is a change to a derived tuple; the kind itself stays. It now reads "leaves `fix-of` out as well".

**2. Spec-token hits**
- **56 AC15**: the gate-legs file is now passed as `sys.argv[1]` instead of sitting inside a quoted Python literal. The command takes the leg name and the suite basename as arguments and prints `True`, so the suite is no longer the thing observed. I ran it at HEAD and it printed `True`. A new §7 line covers the move: `New arm: tools/run-gates/run-gates.gov.test.sh · covers AC15 · …`.
- **56 AC16**: now names `guard.py` by basename; its full path stays in S18. Basenames are not graded at gov's tool root.
- **57 AC14**: the command now reads `--shell-role <ledger>`, with the ledger cited as `shell-role.txt`. Its full path stays in §4 Files touched.

**3. Unit 51: 50817 down to 47418 bytes**
- **Compressed:** the prose of §1, §3 non-goals, §4 (Why one unit, Evidence, the derivation block, declarative keys, Inventory as one line, Migration, Rollout, Alternatives), §5, §7's waiver sentence, §8 F1, F2 and F4, and §10, which is now just the seam, the probe result and the recall terms. I dropped Evidence entries that only repeated a citation already in a scope item.
- **Unchanged, checked byte for byte against a copy taken first:** the Status header, §2, Edges, Files touched, §6, and §7's leg and `New arm:` lines. Every fork outcome is kept, and F3's `grants: PLAY-dClosedLoop-3` line still matches AC36's grep.
- **Brief deviation, edges not merged:** I did not merge §3 edge bullets as the brief suggested. The hygiene edge parser reads only the first backticked target of each bullet (`tools/memory-tree/check-memory-hygiene.sh:2479-2481`), and the mirror join (`:2714-2716`) expects one bullet per target. A merged bullet would quietly lose edges and break the matching hands-off lines in the other units.
- **§9:** I extended the existing uncommitted rev-2 line to say that this prose moved and that no scope item, criterion, edge, fork outcome or touched path did.

Files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-51.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-53.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-55.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-56.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-57.md

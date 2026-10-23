**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33

# Edge-fix pass — the spec writer's return

I fixed all 27 check-12 hits. `bash tools/memory-tree/check-memory-hygiene.sh --only 12` now prints no dOrderedCharter line, reports no FAILED and exits 0. Three dOrderedCharter lines still appear on stderr, but they are check 25's "did not grade … READER NOT IN TREE" notes on specs 19, 30 and 34, and they were there before my edits.

I edited §3 Edges in specs 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 21 and 30, plus one acceptance criterion in spec 33. There is no rev bump, nothing is staged or committed, no deviation record was touched, and the index was not regenerated.

**Reverse edges added (the brief's default fix):**
- **1:** consumes-from 7 (the practice conformance gate and the meta-check's practice population), consumes-from 15 (`resolve_practices`), hands-off 11, hands-off 23 (`practice.land`), hands-off 30.
- **2:** consumes-from 12 (the document check), consumes-from 20 (the renderer of record's `charter` scope), hands-off 5, hands-off 30.
- **3:** consumes-from 20 (`INSTRUCTION_PATHSPECS`), hands-off 29 (the document registry).
- **5:** hands-off 8 (the ranked envelope order).
- **6:** hands-off 31 (the check that reads `CODEX_MAX`), hands-off 37 (the drive table's rows).
- **7:** hands-off 12 and hands-off 13 (the `enforces` key).
- **8:** hands-off 14 (the card file).
- **9:** hands-off 15 (`read_units`).
- **12:** hands-off 15 (`check_statement`).
- **13:** hands-off 12 (the module `instruction_units.py`).
- **21:** consumes-from 20 (the work-order template's slots).

**First edge removed, because the sibling neither produces nor needs what it names:**
- **1 hands-off 32:** unit 32 takes nothing from the catalogue, and its AC2 refuses a `practice.` tag in the overlay. A repository writes `repo.` units, not practices.
- **11 hands-off 14:** unit 14 uses none of unit 11's code. It measures the index against its own `memory.load-budget` default. The pointer in 11's non-goals stays.
- **9 hands-off 4:** the map lists registered documents per level, from `LEVELS` and unit 3's registry. Unit 4's non-goals say so; it never reads unit rows.

**Order hit:** 30's hands-off 21 is now **consumes-from 21**: the reach units unit 21 derives at render from whatever catalogue rows exist, which 30's `reach.<step>` entries join as data. Unit 21 gains the matching **hands-off 30**, which says a row landing later joins with no change to unit 21. Both edges now follow the build order (21 at 23, 30 at 28). Unit 30 also gains hands-off 29 for its `rules` field, which completes the 29↔30 pair.

**Unit 33 AC6:** now reads "a change record whose `**Successor:**` line names `<new tag>`", spelled as unit 15 spells it.

**Left alone, per "change nothing else" — for the spec review:**
- **Unit 1 will turn the meta-check red when it lands.** Unit 7's S3 counts `practices.toml` rows as the practice population, and a practice no leg's `enforces` names is red unless `tools/playbook/core-pending.txt` excuses it. Unit 1's design adds no pending rows, so each of its 39 seeded practices not enforced by a leg would go red. Its new consumes-from-7 edge now states the dependency.
- **Unit 33, line 43** still writes the field in lowercase in prose ("a record whose `successor` is one tag").

Edited files, all in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- 2026-10-23-spec-PLAY-dOrderedCharter-1.md
- 2026-10-23-spec-PLAY-dOrderedCharter-2.md
- 2026-10-23-spec-PLAY-dOrderedCharter-3.md
- 2026-10-23-spec-PLAY-dOrderedCharter-5.md
- 2026-10-23-spec-PLAY-dOrderedCharter-6.md
- 2026-10-23-spec-PLAY-dOrderedCharter-7.md
- 2026-10-23-spec-PLAY-dOrderedCharter-8.md
- 2026-10-23-spec-PLAY-dOrderedCharter-9.md
- 2026-10-23-spec-PLAY-dOrderedCharter-11.md
- 2026-10-23-spec-PLAY-dOrderedCharter-12.md
- 2026-10-23-spec-PLAY-dOrderedCharter-13.md
- 2026-10-23-spec-PLAY-dOrderedCharter-21.md
- 2026-10-23-spec-PLAY-dOrderedCharter-30.md
- 2026-10-23-spec-PLAY-dOrderedCharter-33.md

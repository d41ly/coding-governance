**Serves:** research PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-55

# Mark re-wrap pass — the spec writer's return

All seven marks with values other than `none` now have their whole `widens`/`relaxes`/`grants` run on the line that starts `RESOLVED (`. The change is whitespace only: with all whitespace removed, every changed file is identical to its staged version. Nothing is staged or committed, there is no rev bump, and the index wasn't rendered.

**Re-wrapped this round:**
- spec 34 F4 → line 337
- spec 46 F3 → line 181
- spec 55 F3 → line 443
- spec 12 F3 → line 225
- spec 26 F2 → line 261
- spec 34 F1 → line 319
- spec 47 F2 → line 156

The last four weren't on your list. A scan of every §8 mark in specs 1 to 55 found them: each has a value other than `none` that sat below its `RESOLVED (` line, so the instrument couldn't see it. Spec 53 F2 was already done last round (line 146).

**Left alone: specs 8 (:337), 10 (:240), 32 (:322) and 37 (:243).** Their lines end in `widens:`, but in each the next line reads `none · relaxes: none`. All four marks are all-`none`, so I followed your "leave the all-`none` marks alone". Re-wrapping them would be harmless if you want it anyway.

**Values as the instrument reads them.** I ran `deviations.py`'s own `KEY` regex (`:147`) and `read_keys` (`:583`, which also strips outer backticks) over each `RESOLVED (` line. Only values other than `none` are listed; each sits between the brackets, verbatim.

- **spec 12 F3** (`2026-10-23-spec-PLAY-dOrderedCharter-12.md:225`), grants: [PLAY-dClosedLoop-3 the kickoff Skill and the deployer runbook read the provenance lock where they read the rendered marker.]
- **spec 26 F2** (`2026-10-23-spec-PLAY-dOrderedCharter-26.md:261`), grants: [PLAY-dClosedLoop-3 the review protocol, the diff reviewer's role and the three review prompts name the blob-pinned line where they named file:line.]
- **spec 34 F1** (`2026-10-23-spec-PLAY-dOrderedCharter-34.md:319`), grants: [PLAY-dClosedLoop-3 the marked part in every level-3 to level-5 document the clause names.]
- **spec 34 F4** (`2026-10-23-spec-PLAY-dOrderedCharter-34.md:337`):
  - relaxes: [the owner rules each practice of the census one by one before any moves]
  - grants: [PLAY-dClosedLoop-3 the shipped foundation set's change.]
- **spec 46 F3** (`2026-10-24-spec-PLAY-dOrderedCharter-46.md:181`), widens: [the renderer may read a caller-named overlay file on a render verb]
- **spec 47 F2** (`2026-10-24-spec-PLAY-dOrderedCharter-47.md:156`), relaxes: [unit 26 S3's red, for a build record whose adding commit does not descend from the check's landing]
- **spec 53 F2** (`2026-10-24-spec-PLAY-dOrderedCharter-53.md:146`), relaxes: [unit 26 S3's red, for a reference whose line a commit outside `L`'s descendants wrote]
- **spec 55 F3** (`2026-10-24-spec-PLAY-dOrderedCharter-55.md:443`), widens: [the `playbook-render` entry's leg set gains `agent-instructions wiring` for every adopter]

**Things that matter when you write the records:**
- The three grants values in specs 12 F3, 26 F2 and 34 F1, and spec 34 F4's grants value, end with a period. It is part of the value, because the regex only cuts at ` · `, `; `, the next key, or end of line.
- The backticks inside spec 53's and spec 55's values stay in the value; only backticks around the whole value would be stripped.
- Spec 12 F3 and spec 26 F2 carry only `grants:`. Their marks have no `widens:` or `relaxes:` anywhere, so the instrument reads those two as absent, which means `none`.

Changed this round, all in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`: the 2026-10-23 specs 12, 26 and 34, and the 2026-10-24 specs 46, 47 and 55.

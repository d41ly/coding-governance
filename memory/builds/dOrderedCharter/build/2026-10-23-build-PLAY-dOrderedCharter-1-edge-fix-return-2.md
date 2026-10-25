**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33

# Edge-fix pass, second turn — the spec writer's return

I fixed both check-spec-tokens hits by rewording the two bullets I had added, so specs 15 and 29 are unchanged. Specs 12 and 30 were edited in place, with no rev bump, no staging, no commit and no index render. I can't run check-spec-tokens, so the confirmation is by grep.

1. **Spec 12's hands-off to 15** now reads "the grammar check the write command's S6 runs before every write". It has no backticked token apart from the unit id, and it is close to unit 15's own wording ("unit 12's grammar", "the grammar check S6 runs"). `check_statement` is no longer in the bullet. It still appears three times in spec 12's own design, which is fine.
2. **Spec 30's hands-off to 29** now reads "the additive `rules` field, each rule read as a tag under its row, which the `practice.writing` row uses". Both backticked tokens appear verbatim in spec 29: `rules` in its S1 and its edge back, and `practice.writing` throughout. `practice.<name>.<rule>` is no longer in the bullet; it still appears twice in spec 30's own body.

I also grepped every backticked token in the edge bullets of specs 1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 21 and 30 against the sibling each bullet names. Every token in the bullets I added is now in its sibling. Four misses remain, all in bullets I didn't touch; your report showed only the two hits above, so the tool may not check these:
- spec 1's consumes-from 19: `practice.`
- spec 6's consumes-from 9: `drive`
- spec 12's consumes-from 24: `<hash8>` and `units`

Check 12 (`--only 12`) still exits 0 after these edits.

Changed in this round, in `C:\projects\coding-governance\.claude\worktrees\unattended-dorderedcharter-10a315\memory\builds\dOrderedCharter\spec\`:
- 2026-10-23-spec-PLAY-dOrderedCharter-12.md
- 2026-10-23-spec-PLAY-dOrderedCharter-30.md

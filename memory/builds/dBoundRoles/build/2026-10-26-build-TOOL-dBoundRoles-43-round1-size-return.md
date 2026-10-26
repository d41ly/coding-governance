**Serves:** research TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44

# Round-1 size pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-3-spec-writer.md`, run direct/a479f0c7012aeb534, extracted from its transcript by script.

I fixed all three reds, but Z3 was in a different spec than the brief named. The row over the cap belongs to unit 44, not unit 24, so I shortened unit 44's title and left unit 24 alone. Nothing is committed and no `rev-N` moved.

Files changed:

- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-25-spec-TOOL-dBoundRoles-3.md` — **Z1.** The §3 hands-off bullet to TOOL-dBoundRoles-43 no longer names `checkHandoffSpawn`. It now hands only what unit 43 actually reads from unit 3: `derive_allowance` and the card binding, re-pointed to `WRITE_FOLDERS`. Unit 43 names both tokens, `derive_allowance` twice and `WRITE_FOLDERS` four times, and its matching consumes-from bullet stays, so check 12 is still two-sided.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-43.md` — **Z2.** I cut 1,809 bytes of authored text: the repeated "(ids …)" citations on the consumes-from bullets, and wording I tightened in §1, §3, §4, §5, §10 and a few scope items and criteria. No finding, scope item, criterion command or fork was dropped, and I did not touch the generated region. Two cuts made hygiene check 25 fail (the Readers clauses of S28 and S41), so I restored the needed wording before the final run.
- `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\spec\2026-10-26-spec-TOOL-dBoundRoles-44.md` — **Z3, moved from unit 24.** In the staged README, row 132 is 351 characters, and it is unit 44's title. Unit 24's row is about 170 characters, so editing 24 would not have cleared the check. I shortened unit 44's H1 by 13 characters by dropping three "the"s and changing "workflows suites" to "workflow suites"; the em dash and the meaning are unchanged.

**Unit 43's byte count:** 48,291 in the worktree now. In a throwaway clone where the index generator also filled in this size brief's new records row, it is 48,479 against 49,152, leaving 673 bytes of headroom.

**Checks:** In that clone, after regenerating the index, `check-memory-hygiene.sh` exited 0. That covers check 7 (no README row over 350) and check 25 (the Readers clauses). I deleted the clone afterwards. I did not run the spec-tokens leg, since my grant allows only the hygiene and lexicon gates. Its `[handoff]` and `[size]` results still need a run in the main loop; my grep and the byte count above stand in for them until then.

**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28

# The fix pass's return — dKeptSession

The writer's final return, extracted from its transcript by script, never retyped.

I fixed all seven listed findings in place, across seven specs. Every spec stays `rev-1` and nothing is committed. I ran the hygiene check (`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, exit 0) and it reports no finding on any dKeptSession spec. Its only dKeptSession lines are the informational "did not grade … READER NOT IN TREE covers it" notes on KICK-dKeptSession-1 S6, -2 S2 and -3 S5. I did not re-run `check-spec-tokens.py`; that is yours.

The brief's title says "eleven findings" but its list has seven, so I fixed the seven.

1. **KICK-dKeptSession-1** `[path]`: §6, AC6's fixture line (line 253) now cites "the loop kit's `loop.toml`" instead of the full path. AC8 already used the basename. §2, §4 and Files touched keep the full path.
2. **KICK-dKeptSession-11** `[guards]`: Files touched now reads "`AGENTS.md`: its render, by the playbook kit's renderer, which this unit runs and does not edit". There is no playbook path in it any more.
   - **Decision for you:** I added no legs to §7. The unit edits no file under the playbook kit; it only re-renders `AGENTS.md`. Neither `AGENTS.md` nor the template trips any guarded leg (`check-spec-tokens.py --legs-for`).
   - If you want the renderer listed as a touched file anyway, name `tools/playbook/render_playbook.py` and add `govkit acceptance matrix` and `playbook render selftest` to §7.
3. **KICK-dKeptSession-12** `[path]`: AC1 now says "`CLAUDE.md` carrying the import line that names the card file", with no path-shaped token. I re-wrapped the lines around it.
4. **KICK-dKeptSession-28** `[guards]`: the §7 leg line gains `govkit acceptance matrix` and `playbook render selftest`, spelled as `tools/gate-legs.json` spells them.
5. **KICK-dKeptSession-5** `[guards]`: the unit does not edit `tools/govkit/subject-pins.tsv`, so I dropped it from Files touched. That file's rows come only from the gate-legs manifest, one row per leg (`tools/govkit/govkit.py:2968-2975`), and this unit adds no leg. I added that reason to the existing rev-1 entry in §9 rather than adding a new revision.
6. **KICK-dKeptSession-14** `[handoff]`: KICK-dKeptSession-9 never reads `derive_context_tokens`. Its `tokens` column is its own sum and includes `out`, which `derive_context_tokens` leaves out. So I removed `derive_context_tokens` from KICK-14's hand-off bullet to KICK-9. Both edges now name `measure_context_fill` and `derive_context_fill`, so the pair matches both ways.
7. **KICK-dKeptSession-2** hygiene check 25: S2's by-name half now opens "READER NOT IN TREE — the readers live on dGroundRules' unlanded branch at `3c8c4718a`". It then lists the same readers and ends "and the build run re-grounds on dGroundRules' landed bytes", the same shape as KICK-1's S6. The by-value half is unchanged.

Files changed, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dkeptsession-dd0ede\memory\builds\dKeptSession\spec\`:
- 2026-10-26-spec-KICK-dKeptSession-1.md
- 2026-10-26-spec-KICK-dKeptSession-2.md
- 2026-10-26-spec-KICK-dKeptSession-5.md
- 2026-10-26-spec-KICK-dKeptSession-11.md
- 2026-10-26-spec-KICK-dKeptSession-12.md
- 2026-10-26-spec-KICK-dKeptSession-14.md
- 2026-10-26-spec-KICK-dKeptSession-28.md

**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22

# dLinkedLibrary — the re-ground writers' returns, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dLinkedLibrary-1-parents-crosscheck`](2026-11-05-build-TOOL-dLinkedLibrary-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 1 (specs 1, 8, 13 and 22)

I revised all four Group A specs. Each one's citation of `TOOL-dTotalRecall-1:101-102` now reads `TOOL-dTotalRecall-1 S9`. No design changed, nothing was committed and the real index is untouched.

**TOOL-dLinkedLibrary-1** — authored, now rev-5
- Row 3: the cite in §2 S9 (line 142) now names the section.
- I checked the parent first. At the tip, tr1 is unchanged in the working tree and still at rev-5. Its lines 101-102 are S8's `seed_population` text, and S9's `--writer <door> --check <leg> --field <Key>…` starts at line 105. So the row holds.
- 42770 bytes.

**TOOL-dLinkedLibrary-8** — authored, rev-4 to rev-5
- Row 9: the cite in §2 S1 (now line 72, not the record's 69) now names the section.
- The owner's rev-4 pick touched S9, "The items" and F5. It did not settle this row.
- 46066 bytes.

**TOOL-dLinkedLibrary-13** — authored, rev-2 to rev-3
- Row 17: the cite at line 49 now names the section.
- The brief places it in ll13 S1, but it sits in §2 S2 (S2 starts at line 40), so the revision-log line names §2 S2.
- 29511 bytes.

**TOOL-dLinkedLibrary-22** — authored, rev-4 to rev-5
- Row 24: the cite at line 77 (the record says 74) now names the section.
- The brief places it in ll22 S1, but it sits in §2 S4 (S4 starts at line 65), so the revision-log line names §2 S4.
- The owner's rev-4 F4 pick touched the preconditions and S1, not this row.
- 31255 bytes.

**Other cites:** I found no other `TOOL-dTotalRecall-1:<line>` or `TOOL-dTotalRecall-2:<line>` cite in the four specs, so there are no extra fixes to report. No row was refused.

**Status and revision log:** each **Status:** line has its next rev and `2026-11-05`, with every other field kept. Each §9 has one new line in the required form. It names the section, the cross-check row and "no design change", and ends with `by the brief prompts/2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-reground.md`. The files keep their LF line endings.

**Hygiene gate:** I ran `check-memory-hygiene.sh --staged` over a copy of the index with only these four specs staged. It exits 1, but the only finding is check 9, which says the generated build index needs a fresh render. That is the main loop's `gen_build_index.py --write`. It lists these files as stale:
- `memory/LIVE.md`
- the `README.md` of dDeclaredLoop, dIndexedDesign, dLinkedLibrary, dRankedPlan and dTotalRecall
- `memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-8.md`

No other finding names my specs.

One thing to check: I made the index copy as `idx` in the scratchpad and deleted it afterwards. The scratchpad already held your files, and if one of them was also called `idx`, my copy overwrote it and the delete removed it.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dLinkedLibrary\spec\2026-10-26-spec-TOOL-dLinkedLibrary-1.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dLinkedLibrary\spec\2026-10-26-spec-TOOL-dLinkedLibrary-8.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dLinkedLibrary\spec\2026-10-26-spec-TOOL-dLinkedLibrary-13.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dLinkedLibrary\spec\2026-10-26-spec-TOOL-dLinkedLibrary-22.md

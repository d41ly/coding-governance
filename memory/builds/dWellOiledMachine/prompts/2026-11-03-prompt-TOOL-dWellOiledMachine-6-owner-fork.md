**Serves:** research TOOL-dWellOiledMachine-6

# Brief: TOOL-dWellOiledMachine-6 follows the owner's 2026-11-03 pick on TOOL-dTotalRecall-2 §8 F6

## The prompt

> fix, take recommendations on the forks, land it

— owner, 2026-11-03, on the report of the parents cross-check of dMindYourWords, dShippedRelease,
dScopedBuild and dTendedCadence. The owner took its recommendation:
TOOL-dTotalRecall-2 §8 F6 (a)'s holder verb is TOOL-dPlacedRequest-34 S22's read-only
`unattended.sh --lease status`. Its ask to dPlacedRequest narrows to one appended column, the
`lease`-mode class. The question and the recommendation are in
`memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
under "Parked for the owner". The parent spec's rev-8 lands in the same commit, by the brief
`memory/builds/dTotalRecall/prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md`.

## The brief

### Goal

TOOL-dWellOiledMachine-6 reads the build lease's epoch through the surface tr2 F6 now picks, cites
that fork by name rather than by line, and names the surface on its consumes-from edge. S6 and S7
keep their design.

### Items

All in `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md`.

1. **§8 F4's citation.** F4 cites tr2 F6 as `tr2:337-354`. F6 now runs from line 340 and moves again
   with tr2's rev-8. Cite it as `TOOL-dTotalRecall-2 §8 F6` with no line range. Restate F4's last
   sentence so the verb that serves F4 is TOOL-dPlacedRequest-34 S22's `--lease status build
   <slug>`. That verb already prints `<epoch>` as its sixth TAB field, and tr2 F6 picked it on
   2026-11-03. Keep F4's `RESOLVED (owner, 2026-10-29)` mark as it reads. This build still files no
   epoch row of its own.
2. **S6 and S7 (lines 97-109).** "the holder verb TOOL-dTotalRecall-2 §8 F6 (a) picked" stays true.
   Name `--lease status`'s sixth TAB field as the epoch S6 compares and S7 re-reads each beat. S7
   still reads fleet tag and status through `--claims`, unless `--lease status` already carries both
   in one read. If it does, say so in the return and leave S7's `--claims` read as it is: changing it
   is a design change, and this pass makes none.
3. **The consumes-from external edge (line 179).** "the epoch read §8 F4 asks for" names no surface.
   Make it "TOOL-dPlacedRequest-34 S22's `--lease status`, the holder verb TOOL-dTotalRecall-2 §8 F6
   picked, for the lease's epoch". Keep it inside that one external bullet. Add no new edge bullet to
   a unit id: that would need a mirror in dPlacedRequest, and this pass edits no dPlacedRequest spec.

### Each revision

- Bump the **Status:** line from `rev-5` to `rev-6`, dated 2026-11-03. Keep the status word
  `DEFERRED` and every other field.
- Add one §9 line in the existing form, naming the items moved and this brief.
- Re-open no fork and resolve none.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-6`, and §9 holds the new line.
- `grep -n "tr2:337-354" <spec>` prints only the rev-5 line in §9, which is history.
- `grep -n -- "--lease status" <spec>` prints lines in §2, §3's edge and §8 F4.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`. It names none of your spec's lines. A finding
  that only a `gen_build_index.py --write` render cures belongs to the main loop: name it and leave it.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside spec 6. No commit, no staging into the real index and no deviation record.
- No edit to TOOL-dWellOiledMachine-58 or -41. Both cite tr2 F6 (a) by name, so the pick reaches them
  through that one fact.
- No edit to any dTotalRecall or dPlacedRequest spec.

### Reuse

`memory/builds/dWellOiledMachine/prompts/2026-10-28-prompt-TOOL-dWellOiledMachine-1-parents-reground.md`
is the precedent for a re-ground revision.

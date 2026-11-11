**Serves:** research TOOL-dTotalRecall-2 TOOL-dTotalRecall-1

# Brief: the owner's 2026-11-03 pick on TOOL-dTotalRecall-2 §8 F6's surface, and two parent-text fixes

## The prompt

> fix, take recommendations on the forks, land it

— owner, 2026-11-03, on the report of the parents cross-check of dMindYourWords, dShippedRelease,
dScopedBuild and dTendedCadence. That report parked one question and four parent-text defects. The
question and its recommendation are in
`memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
under "Parked for the owner". The owner took the recommendation: name `--lease status` as tr2 F6
(a)'s verb, and narrow the ask to the one column that verb lacks.

## The brief

### Goal

TOOL-dTotalRecall-2 stops asking dPlacedRequest for a new holder verb. It reads the build lease's
holder through the read-only verb TOOL-dPlacedRequest-34 S22 already specs. TOOL-dTotalRecall-1 stops
promising a door its sibling never registers. Nothing else in either design changes.

### Items

Items 1-4 revise spec 2, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md`.
Item 5 revises spec 1, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md`.

1. **§8 F6's resolution.** S22 specs `unattended.sh --lease status <kind> <name> [<sub>]` as
   read-only. It prints one TAB line, `<tail> <fleet tag> <session> <status> <verdict> <epoch>`, or
   `lease — none · <tail>` (`dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:106-109`,
   with AC22 at `:468-470`). That covers three of the four fields F6 (a) asks a new verb for:
   `fleet-tag`, `session` and `epoch`. It lacks one, the `lease`-mode class, `mine` or foreign.
   Re-mark F6 `RESOLVED (owner, 2026-11-03): (a), served by TOOL-dPlacedRequest-34 S22's --lease
   status`, keeping the 2026-11-02 pick's history in a clause after the mark. Then change the fork's
   last paragraph in three ways:
   - The holder verb is S22's `--lease status build <slug>`.
   - The ask narrows to one column: a seventh TAB field holding the `lease`-mode class (`mine` or
     foreign, TOOL-dPlacedRequest-1:90-92), appended after `<epoch>`. The six-field prefix stays as
     it is, because `read_lease_epoch` (DEPL-dShippedRelease-138 S48) reads the sixth field.
   - Replace the row text the build run files with: "a seventh TAB field on TOOL-dPlacedRequest-34
     S22's `--lease status`, the lease's `lease`-mode class (`mine` or foreign), the six-field prefix
     kept".

   Keep the rest of the fork's content as it reads now: one ask, filed once by this build's run,
   serving TOOL-dWellOiledMachine-58 S4 (c) and S5, TOOL-dWellOiledMachine-41 S2's driver check, and
   TOOL-dWellOiledMachine-6 S6 and S7. The `widens:` value changes from the verb's `epoch` field to
   the `--lease status` class column.
2. **F6's served-sections list.** tr2:352 says the ask "serves this unit's S2 and S9". Neither reads a
   lease: S2 reads the kind's row and S9 rewrites registry `writer` cells. The lease read is S6, by §4
   "Minting". Re-point the clause to S6 and §4 "Minting".
3. **§4 "Minting" and §3's external edge (lines 129-131 and 193-194).** Both describe the holder as
   read "through the read-only holder verb §8 F6 (a) asks dPlacedRequest for". Change both to read
   through TOOL-dPlacedRequest-34 S22's `--lease status build <slug>`, §8 F6's pick. "Minting" keeps
   its four named fields; the class is the column F6 asks for. Keep every other sentence of the
   authority rung, including the `--claims` reasoning and the remote fetch.
4. Fix any other sentence in spec 2 that names a new holder verb, so it reads as item 1 decides.
   Leave the forks of TOOL-dTotalRecall-18 and -20 alone: their "F6 (a)" is a different fork.

5. **tr1:193-194.** "`hand` is legal until TOOL-dTotalRecall-2 registers a door" contradicts
   TOOL-dTotalRecall-2 S9. S9 moves only `fields`-form `hand` rows onto `gov_record.py new <kind>`.
   A `hand` row of any other form keeps `hand`, and the pass names its door's owner in a `Decided:`
   trailer. Restate the rule so `hand` stays legal for any row S9 does not move, and drop "until".
   The cross-check that found this is
   `memory/builds/dMindYourWords/build/2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck.md`
   (row 2, where TOOL-dMindYourWords-11 rev-3 already reads tr2 S9 that way).

### Each revision

- Spec 2 bumps its **Status:** from `rev-7` to `rev-8`, and spec 1 from `rev-4` to `rev-5`. Date
  both 2026-11-03, keep the status word `DEFERRED`, and leave every other field alone.
- Add one §9 line in the existing form, naming the items moved and this brief.
- Re-open no fork, and resolve none other than F6's re-mark.
- Each writer revises only the spec its handoff names: spec 2 takes items 1-4, spec 1 takes item 5.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads the new rev, and §9 holds the new line.
- Spec 2: `grep -n "asks dPlacedRequest for" <spec>` prints no line of §3 or §4.
  `grep -n "this unit's S2 and S9" <spec>` prints nothing. `grep -n -- "--lease status" <spec>`
  prints lines in §3, §4 and §8 F6.
- Spec 1: `grep -n "until TOOL-dTotalRecall-2 registers a door" <spec>` prints nothing.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`. It names none of your spec's lines. A finding
  that only a `gen_build_index.py --write` render cures belongs to the main loop: name it and leave it.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside your one spec. No commit, no staging into the real index, no deviation record and
  no `BACKLOG.md` row: the main loop writes those, and the build run files the ask.
- No edit to TOOL-dPlacedRequest-34 or any other dPlacedRequest spec. The column is an ask, not a
  revision of S22.
- No change to what either unit builds beyond the surface the holder is read through.

### Reuse

`memory/builds/dTotalRecall/prompts/2026-11-02-prompt-TOOL-dTotalRecall-2-owner-fork.md` is the
precedent for this fork's re-mark. TOOL-dPlacedRequest-34 S22 is the surface this pick reuses.

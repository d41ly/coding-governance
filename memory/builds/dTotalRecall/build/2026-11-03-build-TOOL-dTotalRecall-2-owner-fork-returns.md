**Serves:** research TOOL-dTotalRecall-2 TOOL-dTotalRecall-1

# dTotalRecall — the owner-fork writers' returns, verbatim

The `gov-spec-writer` returns for the brief [`2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork`](../prompts/2026-11-03-prompt-TOOL-dTotalRecall-2-owner-fork.md), the owner's 2026-11-03 pick on spec 2's §8 F6 surface, extracted by script from the agents' transcripts and not retyped.

## Spec 2

I revised spec 2, `TOOL-dTotalRecall-2`, now at rev-8. I did not touch item 5 (spec 1): it belongs to the sibling handoff for `TOOL-dTotalRecall-1`.

**Spec 1 is out of my scope.** My brief says "no file outside your one spec", and my input spec is spec 2. A separate handoff (`2026-11-03-prompt-TOOL-dTotalRecall-1-1-spec-writer.md`) carries the same items, has spec 1 as its input, and is the unit that owns spec 1. So the tr1:193-194 `hand` fix belongs to that writer. The spec 1 acceptance grep (`until TOOL-dTotalRecall-2 registers a door`) will still match until that writer's edit lands.

**What changed in spec 2:**
- **Status line:** now `DEFERRED · rev-8 · 2026-11-03`.
- **§3, the external edge (line 131):** the lease holder is now read through `TOOL-dPlacedRequest-34` S22's read-only `--lease status build <slug>`, §8 F6's pick.
- **§4 "Minting" (lines 193-195):** reads the holder the same way. It keeps the four named fields and says the class is the column §8 F6 asks for. The `--claims` reasoning and the remote-fetch sentences are unchanged.
- **§8 F6:**
  - **Mark:** re-marked `RESOLVED (owner, 2026-11-03): (a), served by TOOL-dPlacedRequest-34 S22's --lease status`. The 2026-11-02 pick's history, including the `epoch` and `TOOL-dWellOiledMachine-6` §8 F4 lineage, follows the mark as a clause.
  - **Ask:** narrowed to one seventh TAB field holding the `lease`-mode class, keeping the six-field prefix that `read_lease_epoch` (`DEPL-dShippedRelease-138` S48) reads.
  - **Served sections:** re-pointed from "S2 and S9" to S6 and §4 "Minting".
  - **Row text and `widens:`:** the filed row text is replaced as the brief gives it, and `widens:` now reads `the --lease status class column`.
- **§9:** a rev-8 line names the brief by its stem.

I checked every citation against the source files: `TOOL-dPlacedRequest-34` lines 106-109 (S22) and 468-470 (AC22), `TOOL-dPlacedRequest-1` lines 90-92 (the `lease` mode), and `DEPL-dShippedRelease-138` line 78 (S48 reads the sixth field).

**Item 4:** the phrase "holder verb" survives in only two places, and I left both as history. One is option (a)'s original wording at line 344; the other is the rev-7 log line at 384. The forks of `TOOL-dTotalRecall-18` and `TOOL-dTotalRecall-20` were not touched.

**Acceptance checks:**
- `wc -c` gives 39221, under 49152.
- `grep "asks dPlacedRequest for"` prints nothing.
- `grep "this unit's S2 and S9"` prints nothing.
- `grep -- "--lease status"` prints lines 131 (§3), 194 (§4), 350-365 (§8 F6) and 388 (§9).
- The memory hygiene gate ran with `--staged` over a copied index with only spec 2 staged, and exited 1. It flagged none of the spec's lines. Its only finding is check 9: the build index is out of date for `memory/LIVE.md`, `memory/builds/dTotalRecall/README.md` and `memory/builds/dWellOiledMachine/README.md`. Only a `python tools/memory-tree/gen_build_index.py --write` render fixes that, so it is the main loop's.
- I did not run the naming lexicon because the edit adds no new identifiers.

Nothing was committed or staged in the real index.

Files:
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md (authored, rev-8)
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-1.md (item 5, left for the sibling handoff)

## Spec 1

I revised TOOL-dTotalRecall-1 to rev-5. This handoff covered only spec 1, so I did item 5 alone. Items 1–4 change spec 2, and I left spec 2 untouched for its own writer, which is already editing it in this worktree.

Spec: `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-1.md`

**Changes:**
- **Status line:** now reads `rev-5 · 2026-11-03`; nothing else in the header moved.
- **§4 writer rule (was lines 194-195):** "until TOOL-dTotalRecall-2 registers a door" is gone. The rule now says `hand` is legal on any row TOOL-dTotalRecall-2 S9 does not move. It also says S9 moves only the `fields`-form `hand` rows onto its door. A `hand` row of any other form keeps `hand`, and that pass's `Decided:` trailer names who owns its door. This matches tr2:80-84 as it reads now.
- **One sentence beyond the brief, the note under "The rows" (was line 220):** it said "TOOL-dTotalRecall-2 replaces each with its door". That makes the same false promise about every `hand` row, so I fixed it too. It now says S9 replaces the `fields`-form ones, and `backlog-row` and `dossier` keep `hand`. It fits the goal ("stops promising a door its sibling never registers") but goes past the line range in item 5, so a reviewer may want to confirm it.
- **§9:** a new rev-5 line names both edits and cites row 2 of `2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck`. It also says nothing the unit builds changes.

Left alone: line 187 ("`hand` for a kind no command writes yet") and line 87. Neither promises tr2 a door for a row S9 keeps.

**Acceptance:**
- **Size:** `wc -c` is 40122, under 49152.
- **Phrase grep:** `grep -n "until TOOL-dTotalRecall-2 registers a door"` prints nothing (exit 1). My first wording of the §9 line quoted that phrase and made the grep match, so I reworded it.
- **Hygiene gate:** I ran `check-memory-hygiene.sh --staged` with only this spec staged into a copied index through `GIT_INDEX_FILE` (the copy is in the scratchpad). The only failure is check 9: "generated build index differs from a fresh render". It lists `memory/LIVE.md` and the dShippedRelease, dTotalRecall and dWellOiledMachine `README.md` files as stale. Only a `gen_build_index.py --write` render clears that, which is the main loop's job. No finding names a line of this spec.
- **Naming lexicon:** not run. It's allowed but optional, and this edit added no new names.

I did not commit, stage into the real index, render any index, or write any record or `BACKLOG.md` row.

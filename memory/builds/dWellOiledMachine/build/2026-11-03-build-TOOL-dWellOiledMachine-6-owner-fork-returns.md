**Serves:** research TOOL-dWellOiledMachine-6

# dWellOiledMachine — the owner-fork writer's return, verbatim

The `gov-spec-writer` return for the brief [`2026-11-03-prompt-TOOL-dWellOiledMachine-6-owner-fork`](../prompts/2026-11-03-prompt-TOOL-dWellOiledMachine-6-owner-fork.md), which follows the owner's 2026-11-03 pick on TOOL-dTotalRecall-2 §8 F6, extracted by script from the agent's transcript and not retyped.

## Spec 6

I've authored rev-6 of TOOL-dWellOiledMachine-6. S6 and S7 keep their design, no fork was reopened or resolved, and nothing outside the spec was touched or staged in the real index. The memory hygiene gate has one remaining finding, a build-index render that the main loop owes.

**Spec:** `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-6.md` (18 lines added, 10 removed)

- **Status line:** now reads `DEFERRED · rev-6 · 2026-11-03`. Every other field is unchanged.
- **§8 F4:**
  - The `(tr2:337-354)` line range is gone. F4 now cites `TOOL-dTotalRecall-2 §8 F6` by name only.
  - `RESOLVED (owner, 2026-10-29)` reads as before.
  - The last sentence now says F4 is served by TOOL-dPlacedRequest-34 S22's read-only `--lease status build <slug>`. That verb already prints `<epoch>` as its sixth TAB field, tr2 §8 F6 picked it as its holder verb on 2026-11-03, and this build files no epoch row of its own.
- **§2 S6:** keeps "the holder verb TOOL-dTotalRecall-2 §8 F6 (a) picked". It now names the epoch it compares as the sixth TAB field of `--lease status build <slug>` (TOOL-dPlacedRequest-34 S22).
- **§2 S7:** each beat re-reads the epoch as the sixth TAB field of that same verb. Fleet tag and status are still read through `--claims`.
- **§3 external edge:** "the epoch read §8 F4 asks for" became "TOOL-dPlacedRequest-34 S22's `--lease status`, the holder verb TOOL-dTotalRecall-2 §8 F6 picked, for the lease's epoch". This stays inside the one external bullet, and no new edge bullet was added.
- **§9:** new rev-6 line naming §2 S6 and S7, §3's external edge and §8 F4, plus the brief `prompts/2026-11-03-prompt-TOOL-dWellOiledMachine-6-owner-fork.md`.

**`--lease status` already carries fleet tag and status in one read.** S22 (`memory/builds/dPlacedRequest/spec/2025-10-25-spec-TOOL-dPlacedRequest-34.md:106-107`) prints one TAB line: `<tail> <fleet tag> <session> <status> <verdict> <epoch>`. Fleet tag is field 2 and status is field 4, so S7 could get all three from one read. As the brief says, S7's `--claims` read is left as it is, because changing it would be a design change.

**Acceptance:**
- `wc -c` gives 43806, under 49152.
- The Status line reads `rev-6`, and §9 holds the rev-6 line.
- `grep -n "tr2:337-354"` prints only line 369, the rev-5 line in §9.
- `grep -n -- "--lease status"` prints lines 100 and 109 (§2 S6 and S7), 181 (§3's edge), 351 (§8 F4) and 374 (§9).
- **Memory hygiene gate:** I ran `check-memory-hygiene.sh --staged` with a copied index (`GIT_INDEX_FILE`) holding only this spec staged. It exits 1 on check 9 alone: a fresh build-index render is owed. The stale files are `memory/LIVE.md` and the `README.md` of dShippedRelease, dTotalRecall and dWellOiledMachine. Only `python tools/memory-tree/gen_build_index.py --write` cures this, so I've left it for the main loop. No finding names a line of the spec.
- **Naming lexicon:** `python tools/lexicon/lexicon.py` reports `lexicon OK` and exits 0. It does not grade `.md` files ("dark" in its coverage list), so it says nothing about this spec's text.

**For the dispatcher:** in the working tree, tr2 §8 F6 still reads "RESOLVED (owner, 2026-11-02)" and does not name S22. The brief says tr2's rev-8 lands in the same commit, and this spec cites F6 by name, so it stays correct either way.

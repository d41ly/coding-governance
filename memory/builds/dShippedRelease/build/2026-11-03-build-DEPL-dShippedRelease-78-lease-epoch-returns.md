**Serves:** research DEPL-dShippedRelease-78

# dShippedRelease — the lease-epoch surface writer's return, verbatim

The `gov-spec-writer` return for the brief [`2026-11-03-prompt-DEPL-dShippedRelease-78-lease-epoch-surface`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-78-lease-epoch-surface.md), extracted by script from the agent's transcript and not retyped.

## Spec 78

I've rewritten S59 in spec 78. It now names the read-only surface for the run lease's epoch, and the exit-3 behaviour is unchanged.

**DEPL-dShippedRelease-78: authored, rev-4.**

- **Unit 15 agrees with the brief.** In DEPL-dShippedRelease-15 the lease call is in S6 at line 81, `--lease acquire run release <E>`. So the kind, name and sub are `run release <E>`, as the brief said, and I kept them.
- **S59 (lines 176–181)** is still one bullet and still ends with `Observed by AC49.` It now says exit 3 re-reads the epoch of unit 15 S6's run lease. It does this through TOOL-dPlacedRequest-34 S22's read-only `unattended.sh --lease status run release <E>`, taking the sixth TAB field. That is the same field of the same verb that DEPL-dShippedRelease-138 S48's `read_lease_epoch` reads, but S48 only handles `build <slug>` and S59 leaves it that way. A `lease — none · <tail>` answer reads as not the holder. I checked the field order in S22 (dPlacedRequest-34, lines 106–107): `<epoch>` is the sixth field. No other S-item changed.
- **Status and revision log:** the header reads `rev-4 · 2026-11-03`, and §9 has a new rev-4 line (line 549) saying what changed.

**Acceptance checks:**
- `wc -c` gives 47380, under 49152.
- `grep -n -- "--lease status"` prints S59's line 177, and also the new §9 line 549.
- **Hygiene gate:** I staged only spec 78 into a copy of the index through `GIT_INDEX_FILE` and ran `check-memory-hygiene.sh --staged`. It exits 1 on one finding, check 9. None of its findings name a line of spec 78.
  - Check 9 means the generated build index is out of date: `memory/LIVE.md` and the `README.md` files for dShippedRelease, dTotalRecall and dWellOiledMachine differ from a fresh render.
  - Only `python tools/memory-tree/gen_build_index.py --write` fixes it, so I left it for the main loop.

I touched no other file, staged nothing into the real index, made no commit and wrote no deviation record. The copied index is in my scratchpad and the real index was not touched.

Changed file:
C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-78.md

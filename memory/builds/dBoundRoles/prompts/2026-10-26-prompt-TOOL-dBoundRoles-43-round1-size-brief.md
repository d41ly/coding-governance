**Serves:** research TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-43

# Round-1 size brief — dBoundRoles, three reds left after the round-1 fix pass

After the round-1 fix pass the main loop staged every spec and ran `python tools/memory-tree/gen_build_index.py
--write`, `python tools/check-spec-tokens.py` and `bash tools/memory-tree/check-memory-hygiene.sh`. Three reds
remain. Fix each in the spec it names and nothing else; the spec brief
`memory/builds/dBoundRoles/prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md` still binds, and no spec's
`rev-N` moves for these (each is either uncommitted or already carries a pending rev line from this round's folds).

## Z1 · unit 3's hand-off token (spec-tokens `[handoff]`)

`2026-10-25-spec-TOOL-dBoundRoles-3.md` has a §3 bullet handing `checkHandoffSpawn` to TOOL-dBoundRoles-43, and 43's
spec no longer names that token since the split. Either name the token 43 actually reads from unit 3 (as 43 spells
it) on unit 3's bullet, or, if 43 now reads nothing of unit 3's, remove the bullet from unit 3 and 43's matching
`consumes-from` back, so check 12 stays two-sided.

## Z2 · TOOL-dBoundRoles-43 over the spec ceiling again (spec-tokens `[size]`)

It reads 50100 bytes against 49152. The index generator writes a `gen:spec-records` region into each spec, and that
region added about 1.2 KB after you measured 48868. Bring the authored text down by at least 1.5 KB more, so the
spec stays under the ceiling with the region filled and some headroom left. Cut restated prose, duplicated
citations and long examples; never drop a finding, and do not hand-edit the generated region.

## Z3 · unit 24's index row over its cap (hygiene check 7)

The README's generated unit index renders each spec's H1 title into one row, capped at 350 characters; unit 24's row
is 351. Shorten `2026-10-25-spec-TOOL-dBoundRoles-24.md`'s H1 title (keep the em dash form) by at least ten
characters, keeping its meaning.

## Return

The files you changed, one line each with the Z-items taken, and 43's byte count after your cut. Commit nothing; run
the build-index generator only in a throwaway clone.

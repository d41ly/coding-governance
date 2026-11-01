**Serves:** research TOOL-dTendedCadence-49 TOOL-dTendedCadence-59

# Promoted-fix brief — dTendedCadence, the round-2 promotions' mechanical reds

The round-2 spec audit's disposal authored eleven promoted units, TOOL-dTendedCadence-49 to -59, under
`memory/builds/dTendedCadence/spec/`, staged and NOT committed. The main loop ran `tools/check-spec-tokens.py` over
them, and every red below is a token finding in exactly one spec. Fix each in place, in the spec it names, and
nothing else: no design change, no new scope, no edit to a spec this list does not name. These specs have never been
committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dTendedCadence/prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md`, section "What the last
spec runs had to fix after their writers returned", its first bullet, before the first edit: a file this build will
CREATE is cited in §6 by its basename, and keeps its full path in §2, §4 and Files touched.

## Paths a criterion cites that do not exist at HEAD

- TOOL-dTendedCadence-49 §6 cites `help/maintain.md` (the criterion near line 175). Cite it in §6 as `maintain.md`,
  or have the command take the path as an argument, and keep `help/maintain.md` in §2, §4 and Files touched.
- TOOL-dTendedCadence-59 §6 cites `help/maintain.md` (AC36, line 389) and `tools/drift-audit/maintain-session.sh`
  (AC9 line 294, AC26 line 355, and the criterion near line 280). Apply the same rule to each: the basename
  `maintain-session.sh` and `maintain.md` in §6, the full paths kept in §2, §4 and Files touched.

## When you finish

Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,25` and fix any red it prints on these files.
Return the specs you edited and each fix. Commit nothing and do not run the index generator.

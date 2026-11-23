**Serves:** journal TOOL-dBoundRoles-44

# TOOL-dBoundRoles-44 — the main loop's decision on the builder's divergences of round one

The builder of round one (`wf_74c1c83a-fbf`) read the spec at rev-6 against the tree at `6358098d6`, wrote nothing,
and handed back one path the commit needs and two places where the spec's text does not settle the build. The main
loop read each against source:
- `skills/session-kickoff/SKILL.md` is on the kickoff manifest's `watch:` list in `memory/guides/SESSION-KICKOFF.md`.
- Unit 13's Skill line in `tools/unattended/SKILL.template.md` reads "with `facts` from `handoff.py facts`".
- The spec-audit arm of `tools/workflows/tier2-review.test.sh` reads its finder role from the FULL map.

Each answer below is the option no worse than the others on any principle (P18), decided rather than parked. Each
binds over the spec as the owner's ruling `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling` does, and the
builder records each departure in its deviation record.

1. **The manifest re-stamp joins the write set.** S4 edits a watched file, so the pass re-stamps
   `memory/guides/SESSION-KICKOFF.md`'s `last-audit` in the same commit, as unit 25's pass did at `00a96bb43`.
2. **AC7 greps the line unit 13 wrote.** AC7 is observed by `grep -n "handoff.py facts"` over the template, which names
   unit 13's line, and by the render measuring within its row (11454 against 11455 at `6358098d6`, PINNED). The pass
   neither extends that line nor trims the template, since S7 owes a trim only where the render exceeds the row.
3. **The spec-audit arm stays able to fail.** S2 re-keys FULL's finder roles to `gov-reviewer`. The arm checking
   that a spec audit spawns its finders as `specFinder`, never `diffFinder`, runs over FULL with `diffFinder` set to
   a distinct role, as `kFullB` already does with `gov-other-reviewer`, so the arm still reds when the harness reads
   the wrong key. No arm is weakened.

widens: the write set of TOOL-dBoundRoles-44, by the kickoff manifest guide · relaxes: none.

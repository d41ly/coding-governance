# Acceptance ledger — TOOL-aNimbleMend-10

**Serves:** journal TOOL-aNimbleMend-10

Built against spec rev-2 in one pass commit. Each line is a probe of the changed code the builder made in the pass: the verb run as a CLI, and `check_routed_commits` called from a probe script, over a hand-built scratch repository holding the spec's c1 to c7. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the RED-first and GREEN observation of the new arm in `tools/memory-tree/routed_commits.py`, whose self-test arms were written and not run.

**Evidences:** TOOL-aNimbleMend-10
- AC1 — `L1` — the verb exited 0 for c2, and 1 for c3 and for c4, c3's line reading `L1 size: 4 path(s), 4 line(s); the bound is 3 and 60` and c4's `L1 size: 1 path(s), 61 line(s); the bound is 3 and 60`; a second fixture's commit of 60 lines over three routed paths, a fourth path outside `ROUTED_PATHS` beside them, exited 0. (PINNED, 2026-11-12)
- AC2 — `.governance/policy.toml` — the verb exited 1 for c5 naming `L2 guarded policy file: .governance/policy.toml`, exited 1 with the same line when the guarded-list reader was stubbed to resolve no policy kit, and exited 0 when it was stubbed to a list naming another path.
- AC3 — `L3` — the verb exited 1 for c6 naming `L3 spec edit:` and the spec's path under `memory/builds/tFix/spec/`.
- AC4 — `L4` — the verb exited 1 for c7 naming `L4 new surface: src/e.txt`, and no line for c2 to c6, which change paths and add none, named L4.
- AC5 — `ROUTED_COMMIT_WAIVED` — blank, the leg's function exited 1 and listed c3 to c7 under the limits header and not c2; with those five shas waived it exited 0 and its summary read `5 waived`; with c2's sha added it exited 1 naming that sha as stale. At a resolvable push base the RANGE half still listed the five waived commits.
- AC6 — `routed_commits.GIT_SPAWNS` — over trailer-free fixtures of 3 and of 30 routed commits the counter rose by 7 graded WHOLE and by 11 graded beside a RANGE, the same at both sizes, and `red-fix limits · graded 0` printed once per population; the c1 to c7 fixture cost 8 and 13, one more per population. (PINNED, 2026-11-12)
- AC7 — `routed-commits REFUSED` — the verb exited 2 for a rev naming no commit, its line saying the rev names no commit in this clone, and exited 2 for c1, its line saying the commit carries no `Red-fix:` trailer.

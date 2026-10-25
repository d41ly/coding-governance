**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56

# Brief: dDeclaredLoop's specs cross-checked against dOrderedCharter's re-grounded specs

## The prompt

> Cross-check and re-ground three landed dClosedLoop chain spec sets against their re-grounded
> ancestors, in dependency order, and land each one. dDeclaredLoop first, the root.

— the dClosedLoop housekeeping session, 2026-10-25, relaying the owner's hold on the dBoundRoles,
dTotalRecall and dKeptSession spec runs until this re-ground lands.

## The brief

### Goal

Classify every assumption the 21 exposed dDeclaredLoop specs make about a dOrderedCharter unit as
AGREES, MISMATCH or UNKNOWN UNTIL BUILT, against dOrderedCharter's specs as they stand on origin/main
at `462d20f35`. dDeclaredLoop's spec run began at `96526383c`, before dOrderedCharter's re-ground
(`555e623a7`) and the owner's fork picks (`1e9b2dad5`), both landed (`c63aabbb4`, `60d60e694`); 27
dOrderedCharter units were revised: 1, 2, 3, 4, 6, 7, 9, 11, 14, 15, 19, 20, 25, 26, 27, 30, 31, 32,
33, 34, 35, 36, 37, 46, 49, 50 and 55. Each revised spec's §9 rev-4 and rev-5 lines, and its
`build/2026-10-25-build-PLAY-dOrderedCharter-<n>-deviation-*.md` records, say what moved.

The exposed specs, by the dOrderedCharter units each cites (`PLAY-dOrderedCharter-<n>` or a bare
`dOrderedCharter-<n>`): 1 (6) · 2 (15) · 3 (7) · 4 (7, 19) · 5 (19) · 6 (7) · 12 (11) · 16 (7) ·
17 (7) · 18 (6, 11, 19) · 22 (7) · 24 (7, 15, 35, 36, 46) · 25 (35, 36) · 26 (7, 15, 19, 34, 35,
36, 46) · 27 (7, 15, 19, 35, 36, 37) · 28 (15, 35, 36) · 33 (7, 35, 36) · 34 (33) · 46 (7) · 55
(35) · 56 (50).

Verdicts:

- **AGREES:** the dOrderedCharter text the assumption names says the same thing today, whether or not
  the re-ground touched that unit.
- **MISMATCH:** today's dOrderedCharter text says something different: a renamed surface, a moved
  reader, a fork now resolved another way, a key read at another revision, a refusal the parent now
  states, a file that no longer exists. Quote both sides with `file:line` and state the change the
  dDeclaredLoop spec needs, in one or two sentences.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only dOrderedCharter's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group; check
every spec of that group, and no other:

- **Group A, led by spec 1:** specs 1, 3, 6, 16, 17, 22 and 46 (dOrderedCharter 6 and 7).
- **Group B, led by spec 2:** specs 2, 24, 25, 26 and 28 (dOrderedCharter 7, 15, 19, 34, 35, 36, 46).
- **Group C, led by spec 4:** specs 4, 5, 27, 33 and 55 (dOrderedCharter 7, 15, 19, 35, 36, 37).
- **Group D, led by spec 12:** specs 12, 18, 34 and 56 (dOrderedCharter 6, 11, 19, 33, 50).

The spec files are `memory/builds/dDeclaredLoop/spec/2026-10-2?-spec-TOOL-dDeclaredLoop-<n>.md` and
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every mention
of a dOrderedCharter unit in each of your specs, then the cited dOrderedCharter text at the lines it
names, its §9 rev lines first. Use `git show 555e623a7 -- <oc spec>` and `git show 1e9b2dad5 -- <oc
spec>` to see what each revision moved.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about dOrderedCharter | Verdict | Evidence |`,
   with `dlN:L` for line L of dDeclaredLoop spec N and `ocN:L` for dOrderedCharter spec N.
2. Per MISMATCH, a bullet: both sides quoted with `dlN:L` and `ocN:L`, then `Change:` and the
   revision the dDeclaredLoop spec needs.
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. One line per spec: its counts, and the dOrderedCharter units it cites that the re-ground revised
   but which none of its assumptions depend on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a dOrderedCharter revision restates
  one of their surfaces that the dDeclaredLoop spec relies on through it.
- No defect in dDeclaredLoop's own design that the parent does not cause: those are out of scope.
- No verdict about a dOrderedCharter unit the re-ground did not revise, unless the exposed spec's
  assumption about it depends on a revised unit.

**Serves:** research TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84

# Brief: dWitnessedBar's specs cross-checked against dOrderedCharter's and dDeclaredLoop's re-grounded specs

## The prompt

> Then dWitnessedBar (26 of 88 exposed) and dPlacedRequest (12 of 63 exposed). [...] Re-derive both
> lists against dDeclaredLoop as re-grounded in step 1, not as it stands now.

— the dClosedLoop housekeeping session, 2026-10-25, relaying the owner's hold on the dBoundRoles,
dTotalRecall and dKeptSession spec runs until this re-ground lands.

## The brief

### Goal

Classify every assumption the 26 exposed dWitnessedBar specs make about a dOrderedCharter unit or a
dDeclaredLoop unit as AGREES, MISMATCH or UNKNOWN UNTIL BUILT. Compare against dOrderedCharter's specs
as they stand on origin/main at `462d20f35`, and against dDeclaredLoop's specs as this branch's
dDeclaredLoop re-ground commit leaves them (`git log -1 -- memory/builds/dDeclaredLoop/spec`).

dWitnessedBar's spec run began at `ad002a024`, which holds neither dOrderedCharter's re-ground
(`555e623a7`, landed as `c63aabbb4`) nor the owner's fork picks (`1e9b2dad5`, landed as
`60d60e694`). Those two commits revised 27 dOrderedCharter units: 1, 2, 3, 4, 6, 7, 9, 11, 14, 15,
19, 20, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 46, 49, 50 and 55. Each revised spec's §9 rev-4
and rev-5 lines say what moved. dDeclaredLoop's re-ground revised 20 units: 1 to 6, 12, 16, 17, 18,
22, 24 to 28, 33, 34, 46 and 56. Its record,
`memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`,
and each revised spec's new §9 line say what moved.

The exposed specs, by the units each cites (`oc` dOrderedCharter, `dl` dDeclaredLoop, each as
`<FAMILY>-<build>-<n>` or a bare `<build>-<n>`): 1 (oc7) · 2 (oc7) · 3 (oc7, dl12) · 4 (dl3, dl12)
· 6 (oc6, dl2, dl6) · 7 (dl6, dl12) · 8 (oc7, dl16) · 11 (oc1, oc7, oc19, oc50) · 12 (oc15, oc19,
oc50, dl18) · 13 (oc19) · 14 (oc7, oc50) · 15 (dl1, dl12) · 16 (oc50) · 17 (oc50) · 18 (oc19, oc20,
oc26, oc50) · 19 (oc50) · 22 (oc7, oc19, oc50) · 23 (dl12, dl22) · 24 (oc7, oc19, oc30) · 25 (oc7)
· 28 (oc35, oc36) · 30 (dl16, dl33) · 46 (oc50) · 51 (oc50) · 56 (dl2) · 84 (oc3).

Verdicts:

- **AGREES:** the parent text the assumption names says the same thing today, whether or not a
  re-ground touched that unit.
- **MISMATCH:** today's parent text says something different: a renamed surface, a moved reader, a
  fork resolved another way, a key read at another revision, a refusal the parent now states, a
  file that no longer exists. Quote both sides with `file:line`, and state in one or two sentences
  the change the dWitnessedBar spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check
every spec of that group, and no other:

- **Group A, led by spec 1:** specs 1, 2, 11, 13, 14, 16, 17 and 18 (dOrderedCharter only).
- **Group B, led by spec 19:** specs 19, 22, 24, 25, 28, 46, 51 and 84 (dOrderedCharter only).
- **Group C, led by spec 3:** specs 3, 4, 6, 7, 8, 12, 15, 23, 30 and 56 (both parents).

The spec files are `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-<n>.md`,
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md` and
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md`. Read every mention of
a parent unit in each of your specs, then the cited parent text at the lines it names, its §9 rev
lines first. For dOrderedCharter, `git show 555e623a7 -- <spec>` and `git show 1e9b2dad5 -- <spec>`
show what each revision moved. For dDeclaredLoop, `git show <its re-ground commit> -- <spec>` does.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Verdict | Evidence |`,
   with `wbN:L` for line L of dWitnessedBar spec N, `ocN:L` for dOrderedCharter spec N and `dlN:L`
   for dDeclaredLoop spec N.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dWitnessedBar spec
   needs, then `Cause:` either the re-ground (the parent text moved after `ad002a024`) or
   pre-existing (it already read so at `ad002a024`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. One line per spec: the revised parent units it cites that none of its assumptions depend on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent revision restates one of their
  surfaces that the dWitnessedBar spec relies on through it.
- No defect in dWitnessedBar's own design that a parent does not cause.
- No verdict about a parent unit no re-ground revised, unless the exposed spec's assumption about it
  depends on a revised unit.

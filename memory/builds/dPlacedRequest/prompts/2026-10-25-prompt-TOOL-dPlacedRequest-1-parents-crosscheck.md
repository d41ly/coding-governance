**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-34

# Brief: dPlacedRequest's specs cross-checked against dDeclaredLoop's and dOrderedCharter's re-grounded specs

## The prompt

> Then dWitnessedBar (26 of 88 exposed) and dPlacedRequest (12 of 63 exposed). [...] Re-derive both
> lists against dDeclaredLoop as re-grounded in step 1, not as it stands now.

— the dClosedLoop housekeeping session, 2026-10-25, relaying the owner's hold on the dBoundRoles,
dTotalRecall and dKeptSession spec runs until this re-ground lands.

## The brief

### Goal

Classify every assumption the 14 exposed dPlacedRequest specs make about a dDeclaredLoop unit or a
dOrderedCharter unit as AGREES, MISMATCH or UNKNOWN UNTIL BUILT. Compare against dDeclaredLoop's
specs as this branch's dDeclaredLoop re-ground commit leaves them
(`git log -1 -- memory/builds/dDeclaredLoop/spec`), and against dOrderedCharter's specs as they stand
on origin/main at `462d20f35`.

dPlacedRequest's spec run began at `5352805c8`, which holds dOrderedCharter's re-ground
(`c63aabbb4`) but not the owner's fork picks (`1e9b2dad5`, landed as `60d60e694`). For
dOrderedCharter, check only the units those picks revised: 1, 6, 7, 11, 15, 19, 31, 32, 33, 34, 35,
36 and 46 (`git show 1e9b2dad5 -- <spec>`). dDeclaredLoop's re-ground revised 20 units: 1 to 6, 12,
16, 17, 18, 22, 24 to 28, 33, 34, 46 and 56. Its record,
`memory/builds/dDeclaredLoop/build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`,
and each revised spec's new §9 line say what moved (`git show <that commit> -- <spec>`).

The exposed specs, by the units each cites (`dl` dDeclaredLoop, `oc` dOrderedCharter, each as
`<FAMILY>-<build>-<n>` or a bare `<build>-<n>`): 1 (dl3) · 2 (dl3, dl6, oc7) · 3 (dl1, dl12, dl16,
dl24, dl33) · 4 (dl16, dl27) · 5 (dl16) · 6 (dl12, dl18, oc19) · 7 (dl6, dl12, dl17, dl26, oc7) · 8
(dl1, dl12, dl24, oc36) · 9 (dl3, oc15, oc31, oc32) · 10 (dl3, dl27) · 14 (dl33) · 18 (oc19) · 21
(dl3, dl16, dl27, dl33, oc7) · 34 (oc19).

Verdicts:

- **AGREES:** the parent text the assumption names says the same thing today, whether or not a
  re-ground touched that unit.
- **MISMATCH:** today's parent text says something different: a renamed surface, a moved reader, a
  fork resolved another way, a key read at another revision, a refusal the parent now states, a
  file that no longer exists. Quote both sides with `file:line`, and state in one or two sentences
  the change the dPlacedRequest spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check
every spec of that group, and no other:

- **Group A, led by spec 3:** specs 1, 2, 3, 4, 5, 10 and 14.
- **Group B, led by spec 7:** specs 6, 7, 8, 9, 18, 21 and 34.

The spec files are `memory/builds/dPlacedRequest/spec/2026-10-2?-spec-TOOL-dPlacedRequest-<n>.md`,
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-<n>.md` and
`memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`. Read every mention
of a parent unit in each of your specs, then the cited parent text at the lines it names, its §9 rev
lines first.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Verdict | Evidence |`,
   with `prN:L` for line L of dPlacedRequest spec N, `dlN:L` for dDeclaredLoop spec N and `ocN:L`
   for dOrderedCharter spec N.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dPlacedRequest spec
   needs, then `Cause:` either a re-ground (the parent text moved after `5352805c8`) or pre-existing
   (it already read so at `5352805c8`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. One line per spec: the revised parent units it cites that none of its assumptions depend on.

### Non-goals

- No file is written: every probe reads.
- No verdict about dSafePassage or dGroundRules, except where a parent revision restates one of their
  surfaces that the dPlacedRequest spec relies on through it.
- No defect in dPlacedRequest's own design that a parent does not cause.
- No verdict about a parent unit no re-ground revised, unless the exposed spec's assumption about it
  depends on a revised unit.

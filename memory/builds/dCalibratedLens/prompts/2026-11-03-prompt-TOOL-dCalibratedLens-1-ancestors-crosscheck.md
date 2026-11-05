**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-48

# Brief: dCalibratedLens's specs cross-read against dTotalRecall and dDeclaredLoop

## The prompt

> go with (b) for row 9, rest with recommendations

— the owner, 2026-11-03, answering the parents cross-check's parked items. One recommendation was:
"a second pass over dTotalRecall and dDeclaredLoop, once `0d1c1dda4` lands". It landed on origin/main
the same day.

## The brief

### Goal

Classify every assumption the named dCalibratedLens specs make about a dTotalRecall or dDeclaredLoop
unit, surface, verb, record or rule as AGREES, MISMATCH or UNKNOWN UNTIL BUILT, against those builds'
DEFERRED specs as they stand on origin/main at `0d1c1dda4`. Both are deeper ancestors of
dCalibratedLens, which the first pass scoped out: its record is
`memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md`.
This is a full cross-read, not a delta.

dCalibratedLens's spec run began at `22a8efac3`. Since then
`git diff --name-only 22a8efac3 0d1c1dda4 -- memory/builds/dTotalRecall/spec/ memory/builds/dDeclaredLoop/spec/`
names two files:

- **tr2, TOOL-dTotalRecall-2:** rev-7 (`66f7b8d32`, §8 F6 resolved by the owner to one read-only holder
  verb), then rev-8 (`58b395b6e`, the holder is read through TOOL-dPlacedRequest-34 S22's
  `--lease status`, and the F6 ask narrows to a seventh TAB field).
- **TOOL-dTotalRecall-1 rev-5** (`58b395b6e`): `hand` stays legal on any row tr2 S9 does not move.

`git show 22a8efac3:<spec>` reads an ancestor as this build's spec run read it. A MISMATCH whose
ancestor text moved in one of those two commits has Cause `revision`; any other is `pre-existing`.

The population is by citation: every spec that cites a dTotalRecall or dDeclaredLoop unit, as
`TOOL-<build>-<n>`, a bare `<build>-<n>` or a continuation list, outside the generated records
tables. 24 specs. A mention by name with no unit id is an assumption too: find the unit that owns
what it names. The name-only hits are cl1:40, :108, :128 and :436-441, cl3:325 and :527-530,
cl5:147, cl6:80, :286 and :338-342, cl7:93, cl19:122, cl20:75, and the H1 lines of cl32 and cl42.

Two checks ride the citations:

- **Asks filed on these builds.** cl1 §8 F4, cl3 §8 F2, cl6 §8 F4 and cl7 §8 F2 each name an ask that
  dTotalRecall or dDeclaredLoop is to serve. Check that the named BACKLOG row exists in that build's
  `BACKLOG.md` and says what the spec relies on, and whether the ancestor's DEFERRED spec already
  serves or refuses it. A spec that relies on an ask no BACKLOG holds is a MISMATCH.
- **RB, a shared file's ancestor-changed fact.** Where a dCalibratedLens spec states a fact about a
  file at base (a constant, function, grammar, key, verb or flag, not a line number) that a CITED
  dTotalRecall or dDeclaredLoop unit's §2 Scope changes, the spec must name that unit or say why the
  fact survives it. Compare each of your specs' "Files touched" with the cited units' §2 only. A
  line-number drift alone is never a row.

The lease rule RH of the first pass is not re-run: `0d1c1dda4` moves no row it read, and no
dCalibratedLens spec cites tr2.

Verdicts:

- **AGREES:** today's ancestor text says what the assumption says.
- **MISMATCH:** today's ancestor text says something else: a renamed or retired surface, a different
  verb or grammar, a section renumbered, a fork resolved another way, a refusal the ancestor states,
  or an ask no BACKLOG holds. Quote both sides with `file:line`, and state in one or two sentences
  the change the dCalibratedLens spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the ancestor's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, led by spec 14:** specs 14, 13, 9, 10, 11 and 15. Cited: dl1 dl7 dl16 dl20 dl24 dl26
  dl27 dl28 dl32 tr9 tr11 tr12 tr17.
- **Group B, led by spec 6:** specs 6, 5, 28, 48 and 8. Cited: dl2 dl12 dl20 tr1 tr9 tr12 tr14 tr17
  tr35 tr42.
- **Group C, led by spec 7:** specs 7, 33, 34 and 32. Cited: dl20 tr1 tr11 tr42 tr53.
- **Group D, led by spec 16:** specs 16, 2, 19 and 4. Cited: dl1 dl2 dl3 dl7 dl12 dl27 dl30 tr1 tr9
  tr42.
- **Group E, led by spec 1:** specs 1, 35, 3, 20 and 42. Cited: dl12 dl19 dl20 dl50 tr1 tr11 tr18 tr42
  tr53.

The spec files are `memory/builds/dCalibratedLens/spec/2026-11-0?-spec-TOOL-dCalibratedLens-<n>.md`.
An ancestor's is `memory/builds/<build>/spec/*-spec-TOOL-<build>-<n>.md`. Read every mention in each
of your specs, then the cited ancestor text, its §9 rev lines first. Seventeen specs were revised by
the first pass's re-ground on 2026-11-03: read them as they stand now, rev lines included. The
first-pass record shows the shape and the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |`,
   with `clN:L` for line L of dCalibratedLens spec N, and `trN:L`, `dlN:L` for dTotalRecall and
   dDeclaredLoop spec N (`prN:L` and the first pass's short forms for any other build a cited line
   leads to). `Rule` is `cite` for a citation assumption (by id or by name), `ask` for an ask check,
   else `RB`. Group a spec's citations of one ancestor section into one row where they rest on the
   same fact.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dCalibratedLens
   spec needs, then `Cause:` either `revision` (the ancestor text moved in `66f7b8d32` or
   `58b395b6e`) or `pre-existing`.
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Ancestor text that looks wrong, one line each with `file:line`: never a row, never edited.

### Non-goals

- No file is written: every probe reads.
- No defect in dCalibratedLens's own design that no ancestor text causes.
- No verdict on an ancestor spec: text that looks wrong is one line under 4, never a row.
- No build other than dTotalRecall and dDeclaredLoop as a row's subject; a first-pass parent is
  read only where a cited line leads to it.
- No line-number drift alone as a row.

**Serves:** research TOOL-dScopedBuild-1 TOOL-dScopedBuild-7

# Brief: dScopedBuild's specs cross-checked against the parent specs revised by merge `362790f10`

## The prompt

> Cross-read and re-ground four dClosedLoop chain builds' specs against their parents:
> `dMindYourWords`, `dShippedRelease`, `dScopedBuild` and `dTendedCadence`. The owner asked for this
> on 2026-11-03 even though an earlier triage said no re-ground was owed. Do the full pass anyway, not
> a spot check.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask.

## The brief

### Goal

Classify every assumption the named dScopedBuild specs make about a revised parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`66c5b8dbf`. dScopedBuild's spec run began at `5f0b11f12`, the parent of its first spec commit
`807775940`. That base holds every earlier re-ground merge (dWitnessedBar `191ba7ab5`, dTotalRecall
`2bd5e10d4`, dLinkedLibrary `933e67399`, dFurnishedOrders `57bc3b918`, dWellOiledMachine `0c0f3a183`,
dRankedPlan `7d0f5b756`) and the fork picks `ccd1292ea`. It does not hold merge `362790f10`
(2026-11-02, commit `66f7b8d32`), the owner's pick on TOOL-dTotalRecall-2 §8 F6. That one commit is the
only change to any spec of the four parents (dIndexedDesign, dWitnessedBar, dWellOiledMachine,
dFurnishedOrders) between `5f0b11f12` and `66c5b8dbf`; `git diff --name-only 5f0b11f12 66c5b8dbf --
memory/builds/<parent>/spec/` names nothing else, and dIndexedDesign's specs are byte-identical. It
revised three parent units, and one grandparent unit they read:

- **TOOL-dWellOiledMachine-6 rev-5:** §8 F4's epoch ask is served by tr2 F6 (a)'s holder verb; §2 S6
  and S7 read the epoch through it (wm6:97-111, :338-351, :366-369).
- **TOOL-dWellOiledMachine-58 rev-5:** §8 F5 resolved through tr2 F6 (a); §2 S4 (c) and S5 read the
  build lease's holder through the holder verb (wm58:76-84, :353-359, :372-374).
- **TOOL-dWellOiledMachine-41 rev-4:** §2 S2's driver check, §5 and §10 read the lease holder through
  the picked verb (wm41:45-55, :172-173, :239-242, :247-248).
- **TOOL-dTotalRecall-2 rev-7** (not a parent; the three above read it): §8 F6 RESOLVED (owner,
  2026-11-02) to (a), one read-only holder verb over `read_claims`, widened by `epoch`
  (tr2:340-356).

The deviation records are
`memory/builds/dTotalRecall/build/2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md` and
`memory/builds/dWellOiledMachine/build/2026-11-02-build-TOOL-dWellOiledMachine-{6-deviation-64,41-deviation-413,58-deviation-584}.md`.
`git show 66f7b8d32 -- <spec>` shows what moved; `git show 5f0b11f12:<spec>` reads a parent as this
build's spec run read it.

The first population is by citation: every spec that cites a revised unit, as `TOOL-<build>-<n>` or a
bare `<build>-<n>` (2 specs): 1 (wm6, the executor's transition record) · 7 (wm6 S1 and S8,
`point.command-adapters`, `points.toml`). None cites wm58, wm41 or tr2.

The second population is by rule. The revision applies one rule that binds specs which never cite the
unit stating it:

- **RH, the lease holder and epoch read.** A build lease's `session`, its `lease`-mode class (`mine` or
  foreign) and its `epoch` are read through the one read-only holder verb over `read_claims` that
  tr2 §8 F6 (a) picked, which dTotalRecall's build run asks of dPlacedRequest once (tr2:348-356).
  `unattended.sh --claims` prints fields 1 to 5 only, and none of them is `session` or `epoch`
  (pr1:204-208). No unit files a second ask or builds an epoch read of its own (wm6:348-351). A spec
  that reads a session, `lease`-mode class or epoch through `--claims`, parses a lease commit itself,
  files a second ask, or still reads tr2 F6, wm58 F5 or wm6 F4 as open, is a MISMATCH when it relies
  on one of the revised units for that read.

A text probe for `--claims`, `read_claims`, `holder`, `epoch`, `refs/gov/leases`, `lease` and `§8 F6`
over all 34 specs named no candidate: its one hit, spec 5's "§8 F6", is that spec's own fork. Apply RH
to specs 1 and 7 anyway, and if, reading them, you meet a lease read elsewhere in the set, report it
under 4 with its `file:line`.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not the revision touched
  it.
- **MISMATCH:** today's parent text says something else: a moved reader, a fork resolved another way,
  a section renumbered, or RH broken. Quote both sides with `file:line`, and state in one or two
  sentences the change the dScopedBuild spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

One group, one reviewer, led by spec 1: specs 1 and 7. Check every assumption each makes about wm6
(and any wm58, wm41 or tr2 surface it reaches through it), and RH.

The spec files are `memory/builds/dScopedBuild/spec/2026-11-01-spec-TOOL-dScopedBuild-<n>.md`. The
revised parents' are `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-{6,41,58}.md`
and `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md`. Read every mention of a
revised unit in each of your specs, then the cited parent text, its §9 rev lines first. The precedent
cross-check,
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`,
shows the shape.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `sbN:L` for line L of dScopedBuild spec N, `wmN:L` for dWellOiledMachine spec N and `trN:L`
   for dTotalRecall spec N. `Rule` is `cite` for a citation assumption, else `RH`.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dScopedBuild spec
   needs, then `Cause:` either the revision (the parent text moved in `66f7b8d32`) or pre-existing (it
   already read so at `5f0b11f12`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit RH does not bind, one line saying why.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules the earlier re-grounds applied (dWellOiledMachine's brief's R1 to R9): those
  parents were in this build's base, and its own spec run read them.
- No defect in dScopedBuild's own design that no revised parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 4, never a row.

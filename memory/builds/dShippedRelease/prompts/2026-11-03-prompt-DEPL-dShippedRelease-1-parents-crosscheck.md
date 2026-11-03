**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-15 DEPL-dShippedRelease-30 DEPL-dShippedRelease-58 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-78 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-123 DEPL-dShippedRelease-125 DEPL-dShippedRelease-129 DEPL-dShippedRelease-138 DEPL-dShippedRelease-144

# Brief: dShippedRelease's specs cross-checked against the parent specs revised by merge `362790f10`

## The prompt

> Cross-read and re-ground four dClosedLoop chain builds' specs against their parents:
> `dMindYourWords`, `dShippedRelease`, `dScopedBuild` and `dTendedCadence`. The owner asked for this
> on 2026-11-03 even though an earlier triage said no re-ground was owed. Do the full pass anyway, not
> a spot check.

— the dClosedLoop session's hand-off to this session, 2026-11-03, relaying the owner's ask.

## The brief

### Goal

Classify every assumption the named dShippedRelease specs make about a revised parent unit as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`66c5b8dbf`. dShippedRelease's spec run began at `5d1c82ac0`, the parent of its first spec commit
`63ca805ed`. That base holds every earlier re-ground merge (dWitnessedBar `191ba7ab5`, dTotalRecall
`2bd5e10d4`, dLinkedLibrary `933e67399`, dFurnishedOrders `57bc3b918`, dWellOiledMachine `0c0f3a183`,
dRankedPlan `7d0f5b756`) and the fork picks `ccd1292ea`. It does not hold merge `362790f10`
(2026-11-02, commit `66f7b8d32`), the owner's pick on TOOL-dTotalRecall-2 §8 F6. That one commit is the
only change to any spec of the six parents (dWitnessedBar, dTotalRecall, dBoundRoles,
dWellOiledMachine, dLinkedLibrary, dFurnishedOrders) between `5d1c82ac0` and `66c5b8dbf`; `git diff
--name-only 5d1c82ac0 66c5b8dbf -- memory/builds/<parent>/spec/` names nothing else. It revised:

- **TOOL-dTotalRecall-2 rev-7:** §8 F6 RESOLVED (owner, 2026-11-02) to (a), one read-only holder verb
  over `read_claims`, widened by `epoch`; §3's external edge and §4 "Minting" read the picked verb
  (tr2:130, :193-196, :340-356, :375-377).
- **TOOL-dWellOiledMachine-58 rev-5:** §8 F5 resolved through tr2 F6 (a); §2 S4 (c) and S5 read the
  build lease's holder through the holder verb (wm58:76-84, :353-359, :372-374).
- **TOOL-dWellOiledMachine-41 rev-4:** §2 S2's driver check, §5 and §10 read the lease holder through
  the picked verb (wm41:45-55, :172-173, :239-242, :247-248).
- **TOOL-dWellOiledMachine-6 rev-5:** §8 F4's epoch ask is served by the same verb; §2 S6 and S7 read
  the epoch through it (wm6:97-111, :338-351, :366-369).

The deviation records are
`memory/builds/dTotalRecall/build/2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md` and
`memory/builds/dWellOiledMachine/build/2026-11-02-build-TOOL-dWellOiledMachine-{6-deviation-64,41-deviation-413,58-deviation-584}.md`.
`git show 66f7b8d32 -- <spec>` shows what moved; `git show 5d1c82ac0:<spec>` reads a parent as this
build's spec run read it. An earlier triage said the specs citing wm58 rely on sections other than F5;
do not trust it, check it.

The first population is by citation: every spec that cites a revised unit, as `TOOL-<build>-<n>` or a
bare `<build>-<n>` (6 specs): 1 (wm58 S10, S2) · 4 (wm58 S5, S6, S9, F4/F5's asks; wm6 S8) · 5 (wm58)
· 12 (wm58's door) · 30 (wm58 S4 (a)) · 58 (wm6 S8). None cites tr2 or wm41.

The second population is by rule. The revision applies one rule that binds specs which never cite the
unit stating it:

- **RH, the lease holder and epoch read.** A build lease's `session`, its `lease`-mode class (`mine` or
  foreign) and its `epoch` are read through the one read-only holder verb over `read_claims` that
  tr2 §8 F6 (a) picked, which dTotalRecall's build run asks of dPlacedRequest once (tr2:348-356).
  `unattended.sh --claims` prints fields 1 to 5 only, and none of them is `session` or `epoch`
  (pr1:204-208). The verb serves tr2 S2 and S9, wm58 S4 (c) and S5, wm41 S2's driver check and wm6
  S6 and S7, and no unit files a second ask or builds an epoch read of its own (wm6:348-351). A spec
  that reads a session, `lease`-mode class or epoch through `--claims`, parses the lease commit
  itself, files a second ask for the same verb, or still reads tr2 F6, wm58 F5 or wm6 F4 as open,
  is a MISMATCH when it relies on one of the revised units for that read.
- **A parent tension to weigh, not to edit.** dPlacedRequest unit 34 S22 already specs
  `unattended.sh --lease status <kind> <name> [<sub>]`, read-only, printing one TAB line `<tail>
  <fleet tag> <session> <status> <verdict> <epoch>` (pr34:106-109), while tr2 F6 says no read-only
  verb of dPlacedRequest prints a lease's `session` (tr2:341-342) and asks for one. dShippedRelease's
  `read_lease_epoch` reads the epoch through `--lease status` (sr138 S48). Decide by the parent text
  whether a dShippedRelease spec now reads one fact (a lease's epoch or holder) through a different
  surface than a revised parent unit it relies on reads the same fact through. If it does, that is a
  MISMATCH; if the spec relies on no revised unit for the read, it is a rule-wide hit RH does not
  bind. Either way, report what pr34 S22 and tr2 F6 say about each other in one line under 4.

A text probe for `--claims`, `read_claims`, `holder`, `epoch` and `refs/gov/leases` on a line naming
a lease or claim, over the other specs, named these candidates: 6, 11, 15, 68, 69, 78, 94, 95, 123,
125, 129, 138 and 144. The main loop judged the other probe hits unbound and you need not re-read
them: 3, 7, 13, 26 and 63 cite their own §8 F6; 8, 10, 17, 21, 25, 65, 66, 67, 100, 106, 119 and
145 mean a placeholder, a kit's version `epoch`, a lock's holder or a field name. The probe is a
heuristic. Verify every hit: a hit RH does not bind, such as a release-cadence lease the spec takes
and holds itself with no read of another holder, is a line in your return, not a row.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not the revision touched
  it.
- **MISMATCH:** today's parent text says something else: a moved reader, a fork resolved another way,
  a section renumbered, or RH broken. Quote both sides with `file:line`, and state in one or two
  sentences the change the dShippedRelease spec needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, citation, led by spec 1:** specs 1, 4, 5, 12, 30 and 58. Check every assumption each
  makes about wm58, wm6 (and any tr2 or wm41 surface it reaches through them), and apply RH to the
  same specs.
- **Group B, rule-wide, RH only, led by spec 95:** specs 6, 11, 15, 68, 69, 78, 94, 95, 123, 125,
  129, 138 and 144.

The spec files are `memory/builds/dShippedRelease/spec/2026-1?-??-spec-DEPL-dShippedRelease-<n>.md`.
The revised parents' are `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md` and
`memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-{6,41,58}.md`; the
others you may need are `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`.
Read every mention of a revised unit in each of your specs, then the cited parent text, its §9 rev
lines first. The precedent cross-check,
`memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `srN:L` for line L of dShippedRelease spec N, `trN:L` for dTotalRecall spec N, `wmN:L` for
   dWellOiledMachine spec N and `prN:L` for dPlacedRequest spec N. `Rule` is `cite` for a citation
   assumption, else `RH`.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dShippedRelease spec
   needs, then `Cause:` either the revision (the parent text moved in `66f7b8d32`) or pre-existing (it
   already read so at `5d1c82ac0`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit RH does not bind, one line saying why; and one line on pr34 S22 against tr2 F6.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules the earlier re-grounds applied (dWellOiledMachine's brief's R1 to R9): those
  parents were in this build's base, and its own spec run read them.
- No defect in dShippedRelease's own design that no revised parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 4, never a row.

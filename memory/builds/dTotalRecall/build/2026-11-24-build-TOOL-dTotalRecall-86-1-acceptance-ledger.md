# TOOL-dTotalRecall-86 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-86
**Caused-by:** TOOL-dTotalRecall-86

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`d9d4b040f2b9c122921e93081ac91b3e2c3f7300` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's first fence, its body verbatim, with the first bash fence of unit 81 §4 sourced, both extracted from
the two specs into files under the scratch directory and run from a script file there.

The reads' lines in the fence's order (DERIVED 2026-11-24, that run at the base). The lines before the first `live`
line are S1's and S2's, each at the parent of the pass its `pass` line names; the rest are S3's, each under the spec it
read.

```text
pass 52 926526b1c9125added7b6b2edbde490d99c0a3f4
7d07249b5b8d82025de9643aee58e5db61e6b7e2 1 no base re-key is built
pass 59 47afc89374e539d933728b5f0a06b9678a4ac388
206422580b7363ab9582e37ffe7de7c25773a721 0 it replaces unit 52's absorbed-population arm
pass 46 63f283ddd38397f94a706bf942859d31179fd515
254057fa6d5bbc19cd48329737487c88a10b0085 1 ZED-aFoo-2
254057fa6d5bbc19cd48329737487c88a10b0085 1 This unit's pass builds no body and observes that one
254057fa6d5bbc19cd48329737487c88a10b0085 1 whose body unit 54 builds and this unit's criteria observe
254057fa6d5bbc19cd48329737487c88a10b0085 0 whose body this unit rebuilds
254057fa6d5bbc19cd48329737487c88a10b0085 0 rebuilds the parser on that regex
pass 55 5b5895a493d4a47a0be4e417b1c5550cde92b001
b9f735339150e39be311a1b75d9cbc755ecc8aa7 1 The eight rows move out of `CAUSE_WRITER_KEPT`
pass 56 798f98fc1fa2c4af9feb68f8324f11c9d5339c8f
1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9 1 The row moves out of `ALIAS_COMPARE_KEPT`
pass 57 5ff76c2e273faa46b4490bde40ecb26478205de9
c736ff00f780c01f19115b40ef84efc8b7009590 1 this one follows units 55 and 56
red rows of 999 red 999 no pass commit
live spec 52 strings 52
653bed738685c8d41ee71fbf740a5e3654bdd703 0 no base re-key is built
live spec 59 strings 59
653bed738685c8d41ee71fbf740a5e3654bdd703 1 it replaces unit 52's absorbed-population arm
live spec 46 strings 46
653bed738685c8d41ee71fbf740a5e3654bdd703 0 ZED-aFoo-2
653bed738685c8d41ee71fbf740a5e3654bdd703 0 This unit's pass builds no body and observes that one
653bed738685c8d41ee71fbf740a5e3654bdd703 0 whose body unit 54 builds and this unit's criteria observe
653bed738685c8d41ee71fbf740a5e3654bdd703 1 whose body this unit rebuilds
653bed738685c8d41ee71fbf740a5e3654bdd703 1 rebuilds the parser on that regex
live spec 55 strings 55
653bed738685c8d41ee71fbf740a5e3654bdd703 0 The eight rows move out of `CAUSE_WRITER_KEPT`
live spec 56 strings 56
653bed738685c8d41ee71fbf740a5e3654bdd703 0 The row moves out of `ALIAS_COMPARE_KEPT`
live spec 57 strings 57
653bed738685c8d41ee71fbf740a5e3654bdd703 0 this one follows units 55 and 56
live spec 62 strings 52
653bed738685c8d41ee71fbf740a5e3654bdd703 1 no base re-key is built
live spec 62 strings 59
653bed738685c8d41ee71fbf740a5e3654bdd703 1 it replaces unit 52's absorbed-population arm
live spec 63 strings 46
653bed738685c8d41ee71fbf740a5e3654bdd703 5 ZED-aFoo-2
653bed738685c8d41ee71fbf740a5e3654bdd703 0 This unit's pass builds no body and observes that one
653bed738685c8d41ee71fbf740a5e3654bdd703 0 whose body unit 54 builds and this unit's criteria observe
653bed738685c8d41ee71fbf740a5e3654bdd703 0 whose body this unit rebuilds
653bed738685c8d41ee71fbf740a5e3654bdd703 0 rebuilds the parser on that regex
live spec 64 strings 46
653bed738685c8d41ee71fbf740a5e3654bdd703 0 ZED-aFoo-2
653bed738685c8d41ee71fbf740a5e3654bdd703 1 This unit's pass builds no body and observes that one
653bed738685c8d41ee71fbf740a5e3654bdd703 1 whose body unit 54 builds and this unit's criteria observe
653bed738685c8d41ee71fbf740a5e3654bdd703 2 whose body this unit rebuilds
653bed738685c8d41ee71fbf740a5e3654bdd703 0 rebuilds the parser on that regex
live spec 61 strings 55
653bed738685c8d41ee71fbf740a5e3654bdd703 1 The eight rows move out of `CAUSE_WRITER_KEPT`
live spec 61 strings 56
653bed738685c8d41ee71fbf740a5e3654bdd703 1 The row moves out of `ALIAS_COMPARE_KEPT`
live spec 61 strings 57
653bed738685c8d41ee71fbf740a5e3654bdd703 1 this one follows units 55 and 56
live spec 55 strings 52
653bed738685c8d41ee71fbf740a5e3654bdd703 0 no base re-key is built
live spec 55 strings 59
653bed738685c8d41ee71fbf740a5e3654bdd703 0 it replaces unit 52's absorbed-population arm
live spec 55 strings 46
653bed738685c8d41ee71fbf740a5e3654bdd703 0 ZED-aFoo-2
653bed738685c8d41ee71fbf740a5e3654bdd703 0 This unit's pass builds no body and observes that one
653bed738685c8d41ee71fbf740a5e3654bdd703 0 whose body unit 54 builds and this unit's criteria observe
653bed738685c8d41ee71fbf740a5e3654bdd703 0 whose body this unit rebuilds
653bed738685c8d41ee71fbf740a5e3654bdd703 0 rebuilds the parser on that regex
live spec 55 strings 56
653bed738685c8d41ee71fbf740a5e3654bdd703 0 The row moves out of `ALIAS_COMPARE_KEPT`
live spec 55 strings 57
653bed738685c8d41ee71fbf740a5e3654bdd703 0 this one follows units 55 and 56
```

S4: each row with a wanted value reads it, so no record of unit 46, 52, 55, 56, 57 or 59 is owed and none is written.
Every verified count equals the one unit 76 recorded, and every sha it recorded is a prefix of the verified one, so no
record of unit 76 is owed and none is written. No target was red but the staged 999.

Unit 76's figures are its AC2 line's in `2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md`, whose S5 half
spells its revision `pass(T)^`. Its sha column is that ledger's twelve digits for the same parent: S6's for 46, AC1's
for 55, 56 and 57. For 52 and 59 it records no parent; its sweep block records the passes `926526b1c9125added7b6b2edbde490d99c0a3f4`
and `47afc89374e539d933728b5f0a06b9678a4ac388`, the two `pass_of` printed above. Unit 70's figures are its
`2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md` lines: AC1's "printed its wanted count", and AC8's 0 for
the two strings of S2.

| T | String | Verified | Unit 76 | Unit 70 | Agree (DERIVED 2026-11-24) |
|---|---|---|---|---|---|
| 52 | `no base re-key is built` | `7d07249b5b8d82025de9643aee58e5db61e6b7e2` 1 | no sha, 1 | wanted 1 | yes |
| 59 | `it replaces unit 52's absorbed-population arm` | `206422580b7363ab9582e37ffe7de7c25773a721` 0 | no sha, 0 | wanted 0 | yes |
| 46 | `ZED-aFoo-2` | `254057fa6d5bbc19cd48329737487c88a10b0085` 1 | `254057fa6d5b` 1 | wanted 1 | yes |
| 46 | `This unit's pass builds no body and observes that one` | `254057fa6d5bbc19cd48329737487c88a10b0085` 1 | `254057fa6d5b` 1 | wanted 1 | yes |
| 46 | `whose body unit 54 builds and this unit's criteria observe` | `254057fa6d5bbc19cd48329737487c88a10b0085` 1 | `254057fa6d5b` 1 | wanted 1 | yes |
| 46 | `whose body this unit rebuilds` | `254057fa6d5bbc19cd48329737487c88a10b0085` 0 | `254057fa6d5b` 0, in S5 and S6 | wanted 0, and 0 in AC8 | yes |
| 55 | `` The eight rows move out of `CAUSE_WRITER_KEPT` `` | `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 1 | `b9f735339150` 1 | wanted 1 | yes |
| 56 | `` The row moves out of `ALIAS_COMPARE_KEPT` `` | `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` 1 | `1e9a5ebabf0d` 1 | wanted 1 | yes |
| 57 | `this one follows units 55 and 56` | `c736ff00f780c01f19115b40ef84efc8b7009590` 1 | `c736ff00f780` 1 | wanted 1 | yes |
| 46 | `rebuilds the parser on that regex` | `254057fa6d5bbc19cd48329737487c88a10b0085` 0 | `254057fa6d5b` 0 | 0 in AC8 | yes |

**Evidences:** TOOL-dTotalRecall-86
- AC1 — `git rev-parse "$(pass_of T)^"` — printed `7d07249b5b8d82025de9643aee58e5db61e6b7e2` for 52, `206422580b7363ab9582e37ffe7de7c25773a721` for 59, `254057fa6d5bbc19cd48329737487c88a10b0085` for 46, `b9f735339150e39be311a1b75d9cbc755ecc8aa7` for 55, `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` for 56 and `c736ff00f780c01f19115b40ef84efc8b7009590` for 57, the sha each row of its T printed above and the one §4 pins; the ten counts are §4's. Every liveness pair above is §4's last column, and every read over spec 55 at `653bed738` printed 0. The 999 read printed `red rows of 999 red 999 no pass commit` (DERIVED 2026-11-24, the run above).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-86" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. Verified beside unit 76's (`2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md`) and unit 70's (`2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md`), row by row in the table above: 52 `7d07249b5b8d82025de9643aee58e5db61e6b7e2` 1 beside 1 and wanted 1; 59 `206422580b7363ab9582e37ffe7de7c25773a721` 0 beside 0 and wanted 0; 46 `254057fa6d5bbc19cd48329737487c88a10b0085` 1, 1, 1, 0 and, for S6's second string, 0 beside `254057fa6d5b` 1, 1, 1, 0 and 0 and beside wanted 1, 1, 1 and 0 with AC8's 0 for each of S6's two; 55 `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 1 beside `b9f735339150` 1 and wanted 1; 56 `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` 1 beside `1e9a5ebabf0d` 1 and wanted 1; 57 `c736ff00f780c01f19115b40ef84efc8b7009590` 1 beside `c736ff00f780` 1 and wanted 1. No row fails or differs, and §4's write-once read printed nothing, exit 1, for each of the ten strings over its target and for unit 76; with `dTotalRecall [roster]` it printed the roster record of each of units 46, 52, 55, 56, 57 and 59, and with the `PLAY-dClosedLoop-2` cause line `2026-10-26-build-TOOL-dTotalRecall-76-deviation-761.md`, so it was seen both ways (DERIVED 2026-11-24, these commands).

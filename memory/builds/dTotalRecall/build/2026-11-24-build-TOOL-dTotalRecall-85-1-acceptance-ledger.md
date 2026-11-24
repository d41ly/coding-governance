# TOOL-dTotalRecall-85 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-85
**Caused-by:** TOOL-dTotalRecall-85

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`52aa70457c4329d95d79af4cd9368dd4fa76c115` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's fence, its body verbatim, with the first bash fence of unit 81 §4 sourced, both extracted from the
two specs into files under the scratch directory and run from a script file there.

The reads' lines in the fence's order (DERIVED 2026-11-24, that run at the base). The lines before the first `live`
line are S1's: row 1, row 2 and the control over spec 55, rows 3 and 4 over spec 56, row 5 over spec 57 (DERIVED 2026-11-24), each at the
parent of the pass `pass_of` resolves. The rest are S2's, each under the spec it read.

```text
b9f735339150e39be311a1b75d9cbc755ecc8aa7 1 holding only the build-folder rows this unit moves
b9f735339150e39be311a1b75d9cbc755ecc8aa7 1 git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools
b9f735339150e39be311a1b75d9cbc755ecc8aa7 0 git grep -n CAUSE_WRITER_KEPT -- tools
1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9 1 **hands-off** `TOOL-dTotalRecall-57`
1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9 1 git grep -n ALIAS_COMPARE_KEPT -- tools
c736ff00f780c01f19115b40ef84efc8b7009590 1 **consumes-from** `TOOL-dTotalRecall-56`
live spec 55
653bed738685c8d41ee71fbf740a5e3654bdd703 0 holding only the build-folder rows this unit moves
653bed738685c8d41ee71fbf740a5e3654bdd703 0 git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools
653bed738685c8d41ee71fbf740a5e3654bdd703 0 git grep -n CAUSE_WRITER_KEPT -- tools
live spec 56
653bed738685c8d41ee71fbf740a5e3654bdd703 0 **hands-off** `TOOL-dTotalRecall-57`
653bed738685c8d41ee71fbf740a5e3654bdd703 0 git grep -n ALIAS_COMPARE_KEPT -- tools
live spec 57
653bed738685c8d41ee71fbf740a5e3654bdd703 0 **consumes-from** `TOOL-dTotalRecall-56`
live spec 61
653bed738685c8d41ee71fbf740a5e3654bdd703 1 holding only the build-folder rows this unit moves
653bed738685c8d41ee71fbf740a5e3654bdd703 0 git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools
653bed738685c8d41ee71fbf740a5e3654bdd703 1 git grep -n CAUSE_WRITER_KEPT -- tools
live spec 61
653bed738685c8d41ee71fbf740a5e3654bdd703 1 **hands-off** `TOOL-dTotalRecall-57`
653bed738685c8d41ee71fbf740a5e3654bdd703 1 git grep -n ALIAS_COMPARE_KEPT -- tools
live spec 76
aec378661b8f32c99c069f40d3ff67053a077d54 2 holding only the build-folder rows this unit moves
aec378661b8f32c99c069f40d3ff67053a077d54 2 git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools
aec378661b8f32c99c069f40d3ff67053a077d54 2 git grep -n CAUSE_WRITER_KEPT -- tools
live spec 72
af814dba898546b5628b442898669b3d17f711ba 3 **consumes-from** `TOOL-dTotalRecall-56`
```

`pass_of` printed `5b5895a493d4a47a0be4e417b1c5550cde92b001` for 55, `798f98fc1fa2c4af9feb68f8324f11c9d5339c8f` for 56
and `5ff76c2e273faa46b4490bde40ecb26478205de9` for 57, the passes §4 pins. An empty revision and a bare `^` each
printed a `red no revision before its parent mark` line and returned 1 (DERIVED 2026-11-24, that run).

S3: every numbered row reads 1, so no record of unit 55, 56 or 57 is owed and none is written. Every row's verified sha
and count equal unit 76's recorded ones, so no record of unit 76 is owed and none is written. No row was red.

| Row | T | Verified | Unit 76's AC1 line, `2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md` | Agree (DERIVED 2026-11-24) |
|---|---|---|---|---|
| 1 | 55 | `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 1 | `b9f735339150` 1 | yes |
| 2 | 55 | `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 1 | `b9f735339150` 1 | yes |
| control | 55 | `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 0 | `b9f735339150` 0 | yes |
| 3 | 56 | `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` 1 | `1e9a5ebabf0d` 1 | yes |
| 4 | 56 | `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` 1 | `1e9a5ebabf0d` 1 | yes |
| 5 | 57 | `c736ff00f780c01f19115b40ef84efc8b7009590` 1 | `c736ff00f780` 1 | yes |

**Evidences:** TOOL-dTotalRecall-85
- AC1 — `git rev-parse "$(pass_of T)^"` — printed `b9f735339150e39be311a1b75d9cbc755ecc8aa7` for 55, `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` for 56 and `c736ff00f780c01f19115b40ef84efc8b7009590` for 57, the sha each row of its T printed above and the one §4 pins. The five rows printed 1 each and the control 0. The liveness reads printed 0 for every string over its own spec at `653bed738`, and over the holding text 1 for row 1, row 3, row 4 and the control (spec 61), 2 for row 2 (spec 76 at `aec378661`) and 3 for row 5 (spec 72 at `af814dba8`), §4's last column. In the same shell the row read with 999 printed `red row 999 red 999 no pass commit` (DERIVED 2026-11-24, the run above).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-85" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. Verified beside unit 76's, whose line is in `2026-11-24-build-TOOL-dTotalRecall-76-1-acceptance-ledger.md`: rows 1 and 2 are `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 1 and 1 beside `b9f735339150` 1 and 1; the control is `b9f735339150e39be311a1b75d9cbc755ecc8aa7` 0 beside `b9f735339150` 0; rows 3 and 4 are `1e9a5ebabf0dfda59fc2e9ce55e263c23aa4e0f9` 1 and 1 beside `1e9a5ebabf0d` 1 and 1; row 5 is `c736ff00f780c01f19115b40ef84efc8b7009590` 1 beside `c736ff00f780` 1. Each twelve digits are a prefix of the verified sha and each count is equal, so no row read 0 and none differs. §4's write-once read printed nothing, exit 1, for each of the five strings and for unit 76; with `dTotalRecall [roster]` it printed `2026-10-26-build-TOOL-dTotalRecall-55-deviation-551.md`, `2026-10-26-build-TOOL-dTotalRecall-56-deviation-561.md` and `2026-10-26-build-TOOL-dTotalRecall-57-deviation-571.md`, and with `PLAY-dClosedLoop-2` for the cause `2026-10-26-build-TOOL-dTotalRecall-76-deviation-761.md`, so it was seen both ways (DERIVED 2026-11-24, these commands).

# TOOL-dTotalRecall-90 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-90
**Caused-by:** TOOL-dTotalRecall-90

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`c1203e18c9ed856f807ee6c8dc68b9386c92e491` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's fences, their bodies verbatim, with the first bash fence of unit 81 §4 sourced and the strings files
written by the heredocs of units 82, 83 and 84 §4, all extracted from the specs into files under the scratch directory.

The block's lines, in the fence's order (DERIVED 2026-11-24, that run at the base):

```text
s1-67 56390bab8cce52668b940893b8378621df78e4b7 1 **consumes-from** `TOOL-dTotalRecall-56`
s1-59 206422580b7363ab9582e37ffe7de7c25773a721 1 `absorbs` is absent
s1-46 254057fa6d5bbc19cd48329737487c88a10b0085 0 Minted: `SUFFIX_RE`
live-59 653bed738685c8d41ee71fbf740a5e3654bdd703 0 `absorbs` is absent
live-62 653bed738685c8d41ee71fbf740a5e3654bdd703 1 `absorbs` is absent
live-46 653bed738685c8d41ee71fbf740a5e3654bdd703 1 Minted: `SUFFIX_RE`
live-64 653bed738685c8d41ee71fbf740a5e3654bdd703 0 Minted: `SUFFIX_RE`
```

The two red reads' lines (DERIVED 2026-11-24, that run), no part of the block. The second ends in spec 999's path, left
out here because the index would mint its stem as an id of this build:

```text
s1-999 red 999 no pass commit
s1-bad red no blob at 56390bab8cce52668b940893b8378621df78e4b7:
```

S3: each labelled line beside the S1 its unit's ledger records, and the decision made again from the labelled line. No
`s1-*` line is red. Every count below is DERIVED 2026-11-24, from the block above and the ledger named.

| Labelled line | Unit's ledger and its S1 | Agree | Decision (DERIVED 2026-11-24) |
|---|---|---|---|
| `s1-67` 1 | `2026-11-22-build-TOOL-dTotalRecall-82-1-acceptance-ledger.md` AC1: "sha `56390bab8cce52668b940893b8378621df78e4b7`, count 1" | yes | spec 82's second row: unit 67's tip figure 1, so no record of unit 67 |
| `s1-59` 1 | `2026-11-24-build-TOOL-dTotalRecall-83-1-acceptance-ledger.md` AC1: "`206422580b7363ab9582e37ffe7de7c25773a721`, the sha the first read printed with the count 1" | yes | spec 83's third row: no record of unit 59, none unowed |
| `s1-46` 0 | `2026-11-24-build-TOOL-dTotalRecall-84-1-acceptance-ledger.md` AC1: "`254057fa6d5bbc19cd48329737487c88a10b0085`, the sha the first read printed with the count 0" | yes | spec 84's second row, unit 70's AC8 figure 0: no record of unit 70 |

Unit 74's lines in `2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md`, `s1-59 206422580b73 1` and
`s1-46 254057fa6d5b 0`, hold prefixes of the two labelled shas and the two labelled counts, so no record of unit 74 is
owed (DERIVED 2026-11-24, that ledger). Units 83 and 84 recorded their labelled lines, so no record of either is owed.

S4: no decision owes a record, no unit wrote an unowed one, and this pass writes none. The guards it ran, each with
`has_deviation` over the build folder (DERIVED 2026-11-24, §4's "The guards"):

| Unit | Token | Printed (DERIVED 2026-11-24) |
|---|---|---|
| 67 | `TOOL-dTotalRecall-56` | 0 |
| 59 | `` `absorbs` is absent `` | 0 |
| 70 | `SUFFIX_RE` | 0 |
| 74 | `s1-59` | 0 |
| 74 | `SUFFIX_RE` | 0 |
| 83 | `audit-77 id 22 s1-59` | 0 |
| 84 | `audit-77 id 22 s1-46` | 0 |

With `spec changed at` for the token, units 70 and 83 printed 1 each, so the probe is seen both ways over the real
folder (DERIVED 2026-11-24, that run).

**Evidences:** TOOL-dTotalRecall-90
- AC1 — `s1-67` — with `s1-59`, `s1-46`, `live-59`, `live-62`, `live-46` and `live-64`, each led exactly one of the block's seven lines above, each with the sha and count §4 pins. The red reads printed one line each, `s1-999 red 999 no pass commit` and one opening `s1-bad red no blob at`. Every value was taken by its label. `pass_of` printed `56390bab8cce52668b940893b8378621df78e4b7` for 67, `47afc89374e539d933728b5f0a06b9678a4ac388` for 59 and `63f283ddd38397f94a706bf942859d31179fd515` for 46, and `git rev-parse` of the parents of the last two printed the shas of `s1-59` and `s1-46` (DERIVED 2026-11-24, that run).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-90" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. `s1-67` `56390bab8cce52668b940893b8378621df78e4b7` 1 beside 1 in `2026-11-22-build-TOOL-dTotalRecall-82-1-acceptance-ledger.md`; `s1-59` `206422580b7363ab9582e37ffe7de7c25773a721` 1 beside 1 in `2026-11-24-build-TOOL-dTotalRecall-83-1-acceptance-ledger.md`; `s1-46` `254057fa6d5bbc19cd48329737487c88a10b0085` 0 beside 0 in `2026-11-24-build-TOOL-dTotalRecall-84-1-acceptance-ledger.md`. The decisions are spec 82's second row, spec 83's third and spec 84's second, none owing a record; none is owed of units 74, 83 or 84. `has_deviation` printed 0 for each guard: 67 `TOOL-dTotalRecall-56`, 59 `` `absorbs` is absent ``, 70 `SUFFIX_RE`, 74 `s1-59`, 74 `SUFFIX_RE`, 83 `audit-77 id 22 s1-59` and 84 `audit-77 id 22 s1-46` (DERIVED 2026-11-24, these commands).
- AC3 — `has_deviation` — over a scratch folder, for unit 59 and `audit-77 id 22 s1-59`: 0 with the quoting ledger alone, 1 with the first record added, 1 with an uncommitted second record whose `**Supersedes:**` names the first, and 2 with that line taken out. It printed 0 for `audit-77 id 1` with a trailing space and for units 590 and 5 in all four states (DERIVED 2026-11-24, that run).

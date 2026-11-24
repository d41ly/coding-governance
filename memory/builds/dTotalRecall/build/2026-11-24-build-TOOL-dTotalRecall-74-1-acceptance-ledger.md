# TOOL-dTotalRecall-74 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-74
**Caused-by:** TOOL-dTotalRecall-74

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`377e10e612e0f8744c331527aabc0f53ef95277d` on node a, 2026-11-24. The pass edits no code, and every blob read below is
at a literal revision. §7's legs are the close's. The probe is §4's, its body verbatim, run from a script file.

The probe's seven lines (DERIVED 2026-11-24, §4's probe at the base):

```text
s1-59 206422580b73 1
s1-46 254057fa6d5b 0
live-59 653bed738685 0
live-62 653bed738685 1
live-46 653bed738685 1
refused ''
refused '^'
```

S3: `s1-59` reads 1, so unit 59 built from unit 62's amended text, no deviation record of `TOOL-dTotalRecall-59` is
owed, and none is written. Unit 70's S3 decides the same. The key units 83 and 95 read is §4's: a record of unit 59
for this departure would name in its Evidence `pass(59)`, the string, unit 62's §4 "The amendments to unit 59", unit
70's AC1 line and the `s1-59` count. No such record exists (AC2).

S4: no false certification by unit 70 stands in either string. Unit 70's AC1 line gives the first string no figure of
its own, so the comparison is with the row of unit 70 rev-4 §4's table that line says was met.

**Evidences:** TOOL-dTotalRecall-74
- AC1 — `git log` — printed `63f283ddd38397f94a706bf942859d31179fd515` first for unit 46 and `47afc89374e539d933728b5f0a06b9678a4ac388` first for unit 59; the probe printed the seven lines above, each as §4 pins it, and no `unrefused` line. `s1-59` read 1 for `` `absorbs` is absent `` at `206422580b73`; unit 70's AC1 line records that "Every row of §4's table printed its wanted count at pass(T)^", that row wanting at least 1, so they agree and unit 70 recorded no 0. `s1-46` read 0 for ``Minted: `SUFFIX_RE` `` at `254057fa6d5b`; unit 70's AC8 line records "each printed 0" for it and two more strings, so they agree (DERIVED 2026-11-24, both commands and unit 70's ledger).
- AC2 — `grep -lE 'pass\(59\)|47afc8937'` — over unit 59's deviation records printed nothing, exit 1; the same grep for `TOOL-dTotalRecall-59` printed `2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md` alone. `git grep -n "absorbs" -- legacy_ledger.py` from `tools/lib/` and `git grep -n "absorbs" -- tools/govkit/registry.toml` from the root each printed nothing, exit 1; each path is tracked and read, `git grep -c` counting 33 lines of `def ` in the first and 17 of `ledger` in the second (DERIVED 2026-11-24, these commands).
- AC3 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-74" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone, and the AC1 line under it names `s1-59` and `s1-46`, their shas, and the counts unit 70 recorded for the same strings (DERIVED 2026-11-24, this command).

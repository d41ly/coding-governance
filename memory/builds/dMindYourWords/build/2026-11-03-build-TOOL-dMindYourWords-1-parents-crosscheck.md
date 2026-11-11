**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-11

# dMindYourWords' specs against the parent specs revised by merge `362790f10`: a read-only cross-check

Node d, 2026-11-03, base `66c5b8dbf` (origin/main). dMindYourWords' spec run began at `ba8b3c8c4`,
the parent of its first spec commit `7fba335c5`. That base holds every earlier re-ground merge
(`191ba7ab5`, `2bd5e10d4`, `933e67399`, `57bc3b918`, `0c0f3a183`, `7d0f5b756`) and the fork picks
`ccd1292ea`; `git merge-base --is-ancestor` puts each inside it and `362790f10` outside it. Between
`ba8b3c8c4` and `66c5b8dbf` one commit, `66f7b8d32` (merge `362790f10`), moved any spec of the four
parents: TOOL-dWellOiledMachine-6, -41 and -58, beside TOOL-dTotalRecall-2 rev-7, a grandparent unit
this build cites directly. `git diff --name-only ba8b3c8c4 66c5b8dbf -- memory/builds/<parent>/spec/`
names nothing for dWitnessedBar, dLinkedLibrary or dFurnishedOrders. The owner asked for this pass on
2026-11-03 although an earlier triage said none was owed. This record is not an audit: no spec was
edited by it, and its one mismatch feeds the re-ground brief
[`2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground.md).

**Counts:** 4 assumptions · 2 AGREES · 1 MISMATCH · 1 UNKNOWN UNTIL BUILT, over 1 spec (11, the one
citation spec; the rule probe named no candidate). 1 spec holds a MISMATCH: 11. By rule: 1 citation.
It is pre-existing: tr2's S9 already left a non-`fields` `hand` row at `hand` at `ba8b3c8c4`. No
mismatch comes from the revision.

## Method

- **Population by citation.** `grep -P` over `spec/*.md` for the four revised units, both
  `TOOL-<build>-<n>` and the bare `<build>-<n>`, plus continuation lists and `wm`/`tr` aliases: 1
  spec, 11 (tr2, myw11:114). None cites wm6, wm41 or wm58, and none cites by `:<line>`.
- **Population by rule.** The revision applies one rule, RH: a build lease's `session`, `lease`-mode
  class and `epoch` are read through the one read-only holder verb over `read_claims` that tr2 §8 F6
  (a) picked, never through `--claims`' five fields, and no unit builds a second read or files a
  second ask. A probe for `--claims`, `read_claims`, `holder`, `epoch`, `refs/gov/leases`, `lease`
  and `§8 F6` over all 48 specs named no candidate; the reader confirmed each hit unbound (myw14's
  `holder` is a JavaScript variable, myw4, myw6 and myw8 name the `kit epoch` leg, myw17's are
  `placeholder`, myw1's "§8 F6" is its own fork).
- **Reader.** One `gov-spec-reviewer` agent, read-only, by the brief
  [`2026-11-03-prompt-TOOL-dMindYourWords-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-crosscheck.md),
  its handoff beside it. Its return, the MISMATCH's both sides quoted with its `Change:` and `Cause:`,
  is
  [`2026-11-03-build-TOOL-dMindYourWords-1-crosscheck-returns`](2026-11-03-build-TOOL-dMindYourWords-1-crosscheck-returns.md).
- **The main loop** assembled the table below from the return's table by script, derived the counts
  from it, and re-read row 2's both sides (myw11:110-115; tr2:55-58, :78-84). It changed no verdict.
- **Aliases:** `mywN:L` is line L of `spec/2026-10-29-spec-TOOL-dMindYourWords-N.md`; `trN:L` and
  `wmN:L` of dTotalRecall's and dWellOiledMachine's spec N; all at `66c5b8dbf`.
- **What it does not check:** the rules the earlier re-grounds applied, all in this build's base;
  anything a parent's build run decides; the 47 specs the citation population did not reach beyond
  the rule probe. No skeptic re-ran the verdicts; the writer re-reads both sides before it edits.

## Summary table

| # | Spec | Group | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | myw11 | A | S10's `lexicon-declaration` row (form `rows`) may carry `writer = hand`, and tr2 leaves it there | cite | AGREES | myw11:110-115 "schema form `rows` … the writer is `hand`". tr2:80-84 "a `hand` row of another form keeps `hand`". tr2:300-301: AC9 checks only the `fields` rows. tr1:194 "`hand` is legal until TOOL-dTotalRecall-2 registers a door". |
| 2 | myw11 | A | tr2 will later register a door for the declaration, so `hand` is temporary ("until TOOL-dTotalRecall-2 registers a door") | cite | MISMATCH | myw11:114-115 against tr2:57-58, tr2:80-84, tr2:175-176 and tr2:350-351 (the ordering) |
| 3 | myw11 | A | The stand-in `build_records.py new change` writes gov's first vocabulary record (S10, AC10) and is the command S7's refusal names. tr2 S1 makes that verb its door's adapter. | cite | UNKNOWN UNTIL BUILT | myw11:37-40, :90-92, :117-119, :344-346. tr2:44-46 "The factory's own stand-in verb `build_records.py new <kind>` … calls the same function". tr2:48-53 refuses "a kind whose `writer` names another door". tr2:185: `<n>` is minted under "the build's lease or claim". tr2:356 "The pass builds the lease rung of §4 "Minting" against that verb". At base, `ba8b3c8c4` read "the pass builds no lease rung before the pick". |
| 4 | myw11 | A | RH: the spec reads no lease `session`, `lease`-mode class or `epoch`; it does not read `--claims` or a lease commit, files no ask, and does not read tr2 F6 as open | RH | AGREES | The probe for `--claims\|read_claims\|holder\|epoch\|refs/gov/leases\|\blease\b\|§8 F6` over spec 11 found no match. Its only tr2 text is myw11:114. Any lease read happens inside tr2's door (tr2:192-199), and spec 11 adds none. |

## The mismatch, both sides quoted

Row 2 is quoted in section 2 of the return. myw11:113-115 says S10's `lexicon-declaration` row has
writer `hand` "until TOOL-dTotalRecall-2 registers a door". tr2 S9 (tr2:80-84) moves only `fields`
rows off `hand`, and says "a `hand` row of another form keeps `hand`"; S10's row is form `rows`, and
tr2 adds only `build-readme` and `spec` (tr2:175-176). The "until" points at a door tr2 never adds.

## UNKNOWN UNTIL BUILT

- Row 3: whether the factory's stand-in `build_records.py new change`, which tr2 S1 makes its door's
  adapter (tr2:44-46), passes S2's writer refusal for the `change` row, and whether it mints under the
  lease rung now built against the holder verb (tr2:192-199, :356), is tr2's build run's. The rung
  moved in the revision: at `ba8b3c8c4` tr2 read "the pass builds no lease rung before the pick".

## Parked for the owner

- **Parent text that looks wrong (not edited):** tr2:352 says the one ask "serves this unit's S2 and
  S9", but tr2's lease read sits in S6 and §4 "Minting" (tr2:70, :192); S2 and S9 are the writer
  refusal and the `hand`-row rewrite.

## For the re-ground

One spec, by one row: myw11, row 2 (drop "until TOOL-dTotalRecall-2 registers a door"; the row keeps
`hand` by tr2 S9). Brief:
[`2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground.md).

## After the re-ground

The writer's return is
[`2026-11-03-build-TOOL-dMindYourWords-1-reground-returns`](2026-11-03-build-TOOL-dMindYourWords-1-reground-returns.md).
It refused no row and re-read both sides (tr2:57-58, :80-84, :175-176). myw11 moved to rev-3: S10's
`lexicon-declaration` row keeps `writer = hand` as a `rows` kind tr2 S9 leaves at `hand`, with no door
planned; row 3, an UNKNOWN, was left alone. The spec stays `DEFERRED`, at 35750 bytes, and carries one
spec-revised record,
[`2026-11-03-build-TOOL-dMindYourWords-11-deviation-114`](2026-11-03-build-TOOL-dMindYourWords-11-deviation-114.md).
No fork was opened or resolved.

The writer flagged one more parent line, not edited: tr1:194 says "`hand` is legal until
TOOL-dTotalRecall-2 registers a door", which reads as if every `hand` row were temporary, while tr2 S9
keeps a `rows`-form `hand` row at `hand`. It is dTotalRecall's to reconcile, beside tr2:352 above.

## Owner ruling, 2026-11-03

The owner answered this pass's report with "fix, take recommendations on the forks, land it".

- **tr2:352's "S2 and S9":** TOOL-dTotalRecall-2 rev-8 says its §8 F6 ask serves S6 and §4
  "Minting". Record:
  [`deviation-25`](../../dTotalRecall/build/2026-11-03-build-TOOL-dTotalRecall-2-deviation-25.md).
- **tr1:194's "until … registers a door":** TOOL-dTotalRecall-1 rev-5 keeps `hand` legal on any row
  TOOL-dTotalRecall-2 S9 does not move, as row 2 and TOOL-dMindYourWords-11 rev-3 read it. Record:
  [`deviation-13`](../../dTotalRecall/build/2026-11-03-build-TOOL-dTotalRecall-1-deviation-13.md).

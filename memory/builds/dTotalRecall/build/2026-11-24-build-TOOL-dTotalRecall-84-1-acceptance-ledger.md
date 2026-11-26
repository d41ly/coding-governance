# TOOL-dTotalRecall-84 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-84
**Caused-by:** TOOL-dTotalRecall-84

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`65b104e2e0cf053333fc35a4fe9cde45173a88b2` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's fence, its body verbatim, with the first bash fence of unit 81 §4 sourced, both extracted from the
two specs into files under the scratch directory and run from a script file there.

The three reads' lines, in the fence's order (DERIVED 2026-11-24, that run at the base): the first is S1, over spec 46
at the parent of the pass `pass_of 46` resolves; the second and third are S2, over specs 46 and 64 at `653bed738`.

```text
254057fa6d5bbc19cd48329737487c88a10b0085 0 Minted: `SUFFIX_RE`
653bed738685c8d41ee71fbf740a5e3654bdd703 1 Minted: `SUFFIX_RE`
653bed738685c8d41ee71fbf740a5e3654bdd703 0 Minted: `SUFFIX_RE`
```

`pass_of 46` printed `63f283ddd38397f94a706bf942859d31179fd515`, the one commit whose `Pass:` trailer names unit 46.
An empty revision and a bare `^` each printed a `red no revision before its parent mark` line and returned 1 (DERIVED
2026-11-24, that run).

S3: S1 reads 0 and unit 70 recorded 0, so the second row of §4's comparison table holds and no record of unit 70 is
owed. Unit 74's sha and count equal S1's, so the third row holds and no record of unit 74 is owed. Neither is written.

**Evidences:** TOOL-dTotalRecall-84
- AC1 — `git rev-parse "$(pass_of 46)^"` — printed `254057fa6d5bbc19cd48329737487c88a10b0085`, the sha the first read printed with the count 0; the other two printed `653bed738685` with 1 over spec 46 and 0 over spec 64. In the same shell the first read with 999 printed `red 999 no pass commit` (DERIVED 2026-11-24, the run above).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-84" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. S1 is `254057fa6d5bbc19cd48329737487c88a10b0085` with the count 0; unit 74's line in `2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md` is `s1-46 254057fa6d5b 0`, its twelve digits a prefix of S1's sha and its count S1's; unit 70's AC8 line in `2026-11-24-build-TOOL-dTotalRecall-70-1-acceptance-ledger.md` is "`whose body this unit rebuilds`, `rebuilds the parser on that regex` and ``Minted: `SUFFIX_RE` `` each printed 0". The three readings agree, so §4's table owes no record. §4's write-once read printed nothing for unit 70, exit 1, and nothing for unit 74, exit 1; with `roster` for the string it printed `2026-10-26-build-TOOL-dTotalRecall-70-deviation-701.md` and `2026-10-26-build-TOOL-dTotalRecall-74-deviation-741.md` (DERIVED 2026-11-24, these commands).

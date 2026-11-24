# TOOL-dTotalRecall-83 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-83
**Caused-by:** TOOL-dTotalRecall-83

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-4 over base
`594b406d34f9906f38831df00ba0f42aab03ba0f` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's fence, its body verbatim, with the first bash fence of unit 81 §4 sourced, both extracted from the
two specs into files under the scratch directory and run from a script file there.

The three reads' lines, in the fence's order (DERIVED 2026-11-24, that run at the base): the first is S1, over spec 59
at the parent of the pass `pass_of 59` resolves; the second and third are S2, over specs 59 and 62 at `653bed738`.

```text
206422580b7363ab9582e37ffe7de7c25773a721 1 `absorbs` is absent
653bed738685c8d41ee71fbf740a5e3654bdd703 0 `absorbs` is absent
653bed738685c8d41ee71fbf740a5e3654bdd703 1 `absorbs` is absent
```

`pass_of 59` printed `47afc89374e539d933728b5f0a06b9678a4ac388`, the one commit whose `Pass:` trailer names unit 59.
An empty revision and a bare `^` each printed a `red no revision before its parent mark` line and returned 1 (DERIVED
2026-11-24, that run).

S3: S1 reads 1, so unit 59 built from unit 62's amended text and the third row of §4's decision table holds, a count of
1 or more with no record of unit 59 naming the departure. No record of unit 59 is owed, none is written, and none is
named as fabricated. S4: unit 74's sha and count equal S1's, so no record of unit 74 is owed and none is written.

**Evidences:** TOOL-dTotalRecall-83
- AC1 — `git rev-parse "$(pass_of 59)^"` — printed `206422580b7363ab9582e37ffe7de7c25773a721`, the sha the first read printed with the count 1; the other two printed `653bed738685` with 0 over spec 59 and 1 over spec 62. In the same shell the first read with 999 printed `red 999 no pass commit` (DERIVED 2026-11-24, the run above).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-83" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. S1 is `206422580b7363ab9582e37ffe7de7c25773a721` with the count 1; unit 74's line in `2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md` is `s1-59 206422580b73 1`, its twelve digits a prefix of S1's sha and its count S1's, so the two readings agree. The row of §4's decision table that holds is the third, `1 or more`, none, action none. §4's write-once read printed nothing for unit 59, exit 1, and nothing for unit 74, exit 1; with `roster` for the pattern it printed `2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md` and `2026-10-26-build-TOOL-dTotalRecall-74-deviation-741.md` (DERIVED 2026-11-24, these commands).

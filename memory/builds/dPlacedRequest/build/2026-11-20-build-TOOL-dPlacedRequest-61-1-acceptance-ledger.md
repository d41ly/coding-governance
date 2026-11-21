# TOOL-dPlacedRequest-61 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-61

The unit was observed from its spec at rev-6 on base `435fd5664`. It builds nothing and touches no
product file: every criterion reads spec 59's text, frozen at its close, or spec 57's, through the
readers `bullet`, `sec` and `entries` cut from the fence of spec 59's `### The criterion readers`
section and sourced unchanged. The items its spec marks NOT OBSERVED are resolved in its §4 and
carry no criterion. No gate, suite or bar ran in this pass. Every reading below is the criterion's
own read over the tree, or over a scratch copy made under the run's scratch directory and removed
after.

**Evidences:** TOOL-dPlacedRequest-61
- AC1 — `grep -L -E '^\*\*Status:\*\* (CLOSED|WONTDO)'`: the read of `sec 59 '### The live sweep'` holds it as a fixed string. (DERIVED)
- AC1 — `fixture's`: `bullet 59 AC2` and `bullet 59 AC21` each name it. (DERIVED)
- AC3 — `prints nothing`: `bullet 59 AC3` names it, and names a scratch copy of the folder over which the sweep `prints that bullet`. (DERIVED)
- AC4 — `oracle[^.]*(runs|run |prints|exits)`: the read of `sec 59 '### The live sweep'` holds it as a fixed string. (DERIVED)
- AC4 — `RUN\.md|fixture's( later)? base`: the same read holds it as a fixed string. (DERIVED)
- AC5 — `index\([^,)]*, *(s|": "|":")\)`: `bullet 59 AC7` holds it; over a scratch copy of spec 59 with the group narrowed to `(s|": ")`, the bullet's read held it zero times. (DERIVED)
- AC5 — `CLAIM_KV_AWK='`: `bullet 59 AC7` holds it. (DERIVED)
- AC6 — `p = index(s, ": ")`: `bullet 59 AC7` names it, and `two lines` in the joined text, where the source breaks the line between `the grep` and `prints two lines`. (DERIVED)
- AC10 — `extract_run_facts`: `bullet 57 S1` names it, and the bullet piped to `grep -c '/\^## Run facts/'` printed 0; a line holding `/^## Run facts/` piped to the same grep printed 1. (DERIVED)
- AC11 — `sub(/\r$/, "", line)`: the read of `sec 59 '### The shared key reader'` holds it, and `loose,   s, p, k, x)` with its three blanks. (DERIVED)
- AC11 — `61's S11`: `bullet 59 S7` names it. (DERIVED)
- AC12 — `printf 'the merge-base\n'`: piped to `grep -cE "RUN\.md|fixture's( later)? base"` it printed 0; `the fixture's base` and `RUN.md` each printed 1 through the same grep. (DERIVED)
- AC12 — `RUN\.md|fixture's( later)? base`: the read of `sec 59 '### The live sweep'` holds the alternation. (DERIVED)
- AC13 — `### The oracle's head`: `bullet 59 AC13` names it, and `neither CLOSED nor WONTDO`. (DERIVED)
- AC13 — `61's S13 and S20`: `bullet 59 S21` names it. (DERIVED)
- AC15 — `subject test`: `bullet 59 S1` names it, and `61's S15` in its joined text. (DERIVED)
- AC16 — `if (loose) { sub(/^[[:blank:]]+/`: the read of `sec 59 '### The shared key reader'` holds it. (DERIVED)
- AC16 — `live |5`: the read of `sec 59 "### The suite's rows"` names it. (DERIVED)
- AC17 — `Four review items`: `grep -c` over spec 59 printed 1, and `Five review items` printed 0; over a scratch copy respelling the first as the second they printed 0 and 1. (DERIVED)
- AC18 — `under a hundred lines`: `grep -c` over spec 57 printed 0. (DERIVED)
- AC18 — `one filter over the run-state file`: the read of `sec 57 '## 5.'` names it; over a scratch copy cutting the phrase to `one filter` the same read did not. (DERIVED)
- AC20 — `merge-base --is-ancestor`: in the read of `sec 59 '### The one version oracle'` the first line holding `[ "$own" = 0 ]` is line 9 and the first holding this is line 10. (DERIVED)
- AC20 — `[ "$own" = 0 ]`: over a scratch copy of spec 59 with those two lines swapped inside that section alone, the same read put it on line 10 and the ancestor test on line 9. (DERIVED)

## Readings beside the criteria

- A label no bullet carries, `bullet 59 AC99`, and a heading no section opens each read empty, so every `holds` above is a read that can come back without its token. (DERIVED)
- The first swap staged for AC20 moved S21's prose line, which names both tokens on one line, so the swap was confined to the oracle's section, the population the criterion reads. (DERIVED)
- Unit 59's ledger records its AC3 red half as diverged; this unit's AC3 reads that bullet's text only and is unaffected. (DERIVED)
- The bug-class checklist over the pass commit selected `fixture-passes-by-finding-nothing`: every hold above has a read that came back without its token, the empty label and heading, or a scratch copy. (DERIVED)
- It selected `ledger-token-wrapped-across-a-line-joins-nothing`: every answer keeps its tokens on one line, each contained in a token its criterion names. (DERIVED)
- It selected `staged-break-substitutes-a-synthetic-value`: AC20's swap moves the shipped lines themselves, and the other copies cut or respell the shipped phrase. (DERIVED)
- It selected `inline-fence-swallows-the-rest-of-the-file` and `pipe-in-a-code-span-splits-a-table-cell`: this record holds no fence and no table. (DERIVED)

## Items diverged

None.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec declares no new arm.

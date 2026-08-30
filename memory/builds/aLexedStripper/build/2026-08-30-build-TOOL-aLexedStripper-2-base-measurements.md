# BASE measurements and the rev-2 design proof — `TOOL-aLexedStripper-2`

**Serves:** build TOOL-aLexedStripper-2

Node `a`, 2026-08-30, BASE `19d9b328`. Every verdict below is `node <hook> <<< {tool_name:Workflow,
tool_input:{script}}`, taking the exit code: `0` ADMIT, `2` DENY. The BASE column runs
`git show 19d9b328:tools/hooks/agent-cap.js`.

This record exists because §7 requires a gate's failing case to be OBSERVED before it is wired, and
because rev-1's design was refuted by measurement rather than by argument. The numbers are here so
the next reader does not have to re-derive them.

## 1. The false-positive class at BASE

A CORRECT five-element lens array, fanned through `boundedParallel(…, MAX_VERIFIERS)`. Only the
prose of one prompt differs. Every row SHOULD admit.

| prose contains | multi-line array | one-line array |
|---|---|---|
| a literal `...` | 2 DENY | 2 DENY |
| an unmatched `[` | 2 DENY | 2 DENY |
| an unmatched `]` | 2 DENY | 0 |
| an unmatched `)` | 2 DENY | 0 |
| an unmatched `}` | 2 DENY | 0 |
| an unmatched `(` | 0 | 0 |
| an unmatched `{` | 0 | 0 |
| two ASCII apostrophes | 0 | 0 |
| U+2019 apostrophes | 0 | 0 |
| an em dash | 0 | 0 |

Five spellings deny in the multi-line array, which is the shape every shipped harness writes.

**Two corrections to the records this build inherited.** `ABL-dPinnedVintage-4` attributes the
denial to two apostrophes eating a `)`, and the adopter's gotcha
`guard-blanks-quoted-strings-before-counting-brackets.md` prescribes U+2019 in place of ASCII `'`.
Both rows admit at BASE in both shapes, so the diagnosis is stale at 1.8 and the workaround
addresses nothing. And the round-1 spec audit reported that NO unmatched-`)` shape denies, having
run 17 one-line variants; the multi-line column refutes that, and the row survived into rev-2 with
its deciding array shape now named.

## 2. Why rev-1's design was withdrawn

Rev-1 said `fanoutFindings` should read `blankLiterals(script)`. Two shapes, both reproduced here,
say otherwise. Each is DENIED at BASE and ADMITTED under that reading.

| shape | BASE | rev-1's S1 |
|---|---|---|
| an unbounded fan below an unterminated backtick | 2 DENY | 0 ADMIT |
| an `agent(` inside a multi-line interpolation | 2 DENY | 0 ADMIT |

The first is `blankLiterals`' `let mode` at `agent-cap.js:506`, declared outside the per-line loop at
`:507`: one unmatched backtick blanks every later line, so rule 2 finds no fan-out site at all. The
second is that `blankLiterals` blanks interpolation bodies, and rule 5's per-line span view cannot
restore them for a rule whose walks are line-indexed.

Both were found by the round-1 spec audit and both were re-measured before folding rather than taken
on the report's word.

## 3. The rev-2 design, proven

`renderCodeView` prototyped against the shipped hook: line-aligned, interpolation bodies copied,
`${…}` nesting tracked, and a fail-closed branch when the scan ends inside a template literal.
29 shapes, one per acceptance criterion, BASE against prototype.

| criterion | shapes | result |
|---|---|---|
| AC1–AC4 prose must ADMIT | 20 | all pass; the five BASE denials become admits |
| AC5 six lenses must DENY | 1 | pass, unchanged |
| AC6a single-line interpolation must DENY | 1 | pass, unchanged |
| AC6b multi-line interpolation must DENY | 1 | pass, unchanged — the shape rev-1 would have opened |
| AC6c bounded fan inside an interpolation must ADMIT | 1 | pass, unchanged |
| AC7 unbounded fan below an unterminated backtick must DENY | 1 | pass, unchanged — the other shape rev-1 would have opened |
| AC8 nested template must ADMIT | 1 | pass — the fail-closed branch adds no false positive |
| AC9 prior escapes must stay DENY, correct harness stay ADMIT | 3 | pass, unchanged |

**29/29.** No verdict moved except the five false positives the unit exists to remove.

AC8 is the row worth keeping in view: a fail-closed branch on "ended inside a template literal" is
only safe because the nesting in S2 makes `` `a${`b`}c` `` balance. Without it that legal script
would end the scan in template mode and be denied, and the unit would have traded one false-positive
class for another.

## 4. A defect in this record's own harness, found and fixed

The first run of the verification script annotated every `BASE 2 -> prototype 0` transition as
`FAIL-OPEN!`. For the twenty prose rows that transition IS the fix, and the label would have made a
correct result read as twenty regressions. The verdict column was computed against the wanted value
and was never wrong, so nothing was mis-decided — but the annotation would have gone into this
record. It now fires only when the WANTED verdict is DENY. Noted because it is the
`fixture-passes-by-finding-nothing` family one step over: a harness whose reporting cannot
distinguish a fix from a regression is not reporting.

## 5. The corpus figures for `TOOL-aLexedStripper-1`

Recall and precision against stdlib `tokenize` NAME tokens, which is the exact set the tokenizer
approximates. Enumerated by `git ls-files '*.py'`, files that fail to tokenize skipped.

| corpus | current chain | candidate scanner |
|---|---|---|
| this repo, 46 files | recall 88.6% · precision 37.6% | recall 99.3% · precision 99.6% |
| `d41ly/incms` at `069f0459`, 1167 files | recall 97.5% · precision 39.0% | recall 99.5% · precision 99.3% |

Worst files under the current chain — this repo: `tools/lexicon/lexicon_conf.py` 55.6% recall,
`tools/codebase-map/selftest.py` 57.3%, `tools/lexicon/lexicon.py` 61.5%. inCMS:
`services/api/app/main.py` 18.8%, which is `ABL-bCandidLoupe-1`'s 81.3% loss.

12 files in this repo and 34 in inCMS lose more than 10% of their real identifiers. The adopter's
row says "24 .py files affected" and does not mention this repo at all.

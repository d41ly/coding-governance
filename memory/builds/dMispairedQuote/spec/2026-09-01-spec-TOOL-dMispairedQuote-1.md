# TOOL-dMispairedQuote-1 — one quote-opening decision, shared by every view in `agent-cap.js`

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dMispairedQuote-1.md](../prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md) | research | TOOL-dMispairedQuote-2 |

<!-- /gen:spec-records -->

## 1. Goal

`agent-cap.js` reads three views of a workflow script and each one pairs a quote with the next quote
of the same kind on the line. An apostrophe in prose earlier on that line takes the pairing, and the
span blanked between the two carries the fan-out. All three rules are defeated by it, at exit 0. This
unit gives the file ONE decision about what opens a string literal, and applies it in all three.

## 2. Scope (IN)

- **S1** — Add `opensLiteral(line, i)` and `literalEnd(line, i)` to `tools/hooks/agent-cap.js`. A
  quote opens a string literal only where one may legally BEGIN: `opensLiteral` is false when the
  character immediately before it is `[A-Za-z0-9_$)\]\\]`. `literalEnd` returns the index of the
  unescaped partner on the same line, or `-1` when the quote does not open a literal or has no
  partner. Escapes are consumed two characters at a time, as every existing branch already does.
- **S2** — `stripStrings` becomes one ordered pass over the line using `literalEnd`, replacing the
  two independent `replace()` passes. It skips a same-line backtick span whole rather than scanning
  inside it, so template prose contributes no false opener. It does NOT blank template contents:
  rule 1's fail-closed ceiling for a primitive named inside a template is `TOOL-aLexedStripper-3`'s
  and is out of scope here.
- **S3** — `stripStrings` fails CLOSED per line: when any quote is emitted as text rather than
  consumed as one half of a pair, it returns the line UNBLANKED. A pairing it could not complete is
  a pairing it cannot vouch for.
- **S4** — `renderCodeView`'s code-mode quote branch calls `literalEnd`. A quote it cannot pair marks
  that line untrusted, and the line is rendered as `stripStrings(raw).split('//')[0]` instead of the
  blanked view. Mode tracking is unchanged; only that line's OUTPUT changes.
- **S5** — `blankLiterals`' quote branch calls `literalEnd`, with the same per-line fail-closed. This
  also removes its run-to-end-of-line swallow, which is the defect `addc6169` fixed in
  `renderCodeView` and left here, named as out of scope by that round's own review record.
- **S6** — Every byte of S1 to S5 is mirrored into `.claude/hooks/agent-cap.js`, the wired copy.
- **S7** — Regression arms in `tools/hooks/agent-cap.test.sh`, each staged RED against the tip before
  it lands, covering the CLASS in all three rules: the apostrophe-shares-the-line shape for rule 1
  (regex literal, double-quoted string, block comment, template literal), for rule 2, and for rule 3,
  plus the unpaired-double-quote shape for rule 3. Each carries a control with the apostrophe removed.

## 3. Non-goals (OUT)

- `TOOL-aLexedStripper-3` — rule 1 denying a primitive written inside a lens PROMPT. That is a
  FALSE POSITIVE and widening rule 1's blind spot needs fixtures in both directions. S2 deliberately
  leaves the ceiling where it is.
- `TOOL-aLexedStripper-4` — `blankLiterals`' `let mode` sitting outside the per-line loop, so one
  unterminated template blanks every later line. A different defect in the same function; S5 touches
  the quote branch and not the mode.
- Modelling regex literals. Section 4 records the test that rejected it.
- Any change to what rules 1, 2 or 3 DECIDE. This unit changes only what they can SEE.

## 4. Design

The file holds three string views and each has its own quote handling: `stripStrings` (rule 1, two
regex passes), `renderCodeView` (rule 2, an ordered per-line scan), `blankLiterals` (rule 3, an
ordered scan with a block-comment mode). They disagree about what a quote is, which is why the same
apostrophe defeats them in three different ways and why one repair has now twice fixed one of them.

### Data model

`literalEnd(line, i)` is the whole contract. It answers one question — where does the literal opening
at `i` end, if one opens there — and every view asks it instead of walking the line itself.

```js
function opensLiteral(line, i) {
  const p = i - 1
  return p < 0 || !/[A-Za-z0-9_$)\]\\]/.test(line[p])
}
```

In valid JavaScript a string's opening quote is never glued to the character that ENDS an expression.
`don't`, `won't`, `it's` and `y'all` all put the apostrophe immediately after an identifier
character, so the predicate is exact for the realistic corpus and does not depend on which construct
the prose sits in. `\` excludes an escaped quote reached in code position.

### Alternatives rejected

Four candidates were built as patched copies of the shipped hook and measured against a 21-case
corpus for rules 1, three cases for rule 2 and three for rule 3. Scores are rule-1 corpus.

| candidate | rule 1 | rule 2 | rule 3 | the test that rejected it |
|---|---|---|---|---|
| model regex literals in `stripStrings` | 16/21 | ADMIT | ADMIT | `W2`, `W3`, `W4`, `W6` — a block comment, a template literal and mid-line prose carry the same apostrophe and no regex, and all four still admit |
| the opener rule alone, no fail-closed | 20/21 | ADMIT | ADMIT | `W6` — `/* run 'em */` puts the apostrophe in a legal opener position, so the opener rule alone does not stop the mispair |
| opener + fail-closed, `stripStrings` only | 21/21 | ADMIT | ADMIT | `R2` — `renderCodeView` carries the same mispairing and rule 2 still admits an unbounded receiver |
| the above plus `renderCodeView` | 21/21 | DENY | ADMIT | `R5`, `R6` — `blankLiterals` carries it too, and rule 3 admits a declared bound of 50 |

The chosen candidate is the fourth plus `blankLiterals`. It scores 21/21, denies `R2`, `R5` and `R6`,
and leaves the shipped suite at 105 passed / 0 failed.

`R6` is the one worth naming separately: it needs no apostrophe at all. An unpaired double quote in
code position makes `blankLiterals` run to end of line and synthesize a closer the source never had,
which is the defect `addc6169` repaired in `renderCodeView`. Rule 3 then reads no bound and admits
`boundedParallel(B.map(...), 50)`.

### Files touched (estimate)

| file | why |
|---|---|
| `tools/hooks/agent-cap.js` | S1 to S5 |
| `.claude/hooks/agent-cap.js` | S6, verbatim mirror |
| `tools/hooks/agent-cap.test.sh` | S7 |

## 5. Production-readiness checklist

- security — this IS the security surface. The change moves every measured case toward DENY and none
  toward ADMIT; the 21-case corpus and the shipped suite are the evidence in both directions.
- perf / scale — one linear pass per line replacing two regex passes. The hook already runs per tool
  call and the script is bounded by what a caller sends.
- a11y — N/A — a stdin/stderr hook with no interface.
- i18n — N/A — the predicate is over ASCII source syntax, not over prose language.
- error / empty / loading states — unchanged. `main()` exits 0 on unparseable stdin, which S1 to S5
  do not touch.
- observability — unchanged. Every denial keeps the existing per-rule stderr explanation.
- risks — the fail-closed halves can turn a line that used to blank into one that denies. Measured
  against `tools/workflows/*.js` and the shipped suite; no case moved.
- testing + left-shift gates — S7, and the `agent-cap self-test` leg already on the bar.
- migration / rollback — none. The file is deployed verbatim and a revert is a file revert.
- user docs — `TOOL-dMispairedQuote-2` carries the prose. Not this unit.

## 6. Acceptance criteria

- **AC1** — When the three reported probes run against `tools/hooks/agent-cap.js`, all three exit 2;
  the third is `const re = /won't/; const r = await parallel([() => agent('a'), () => agent('b')])`
  and exits 0 today.
- **AC2** — When the same fan-out is preceded on its line by `"don't"`, `/* don't */`,
  `` `don't` `` or `/* run 'em */`, each exits 2 through rule 1's `offendingLines`.
- **AC3** — When `const re = /won't/; const r = await boundedParallel(all.map((f) => () => agent('x')), 5)`
  runs, it exits 2 — rule 2's `renderCodeView` sees the `agent(` the apostrophe used to hide.
- **AC4** — When a script declares a bound of 50 on a line carrying an apostrophe or an unpaired
  double quote, it exits 2 — rule 3's `blankLiterals` sees the bound.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, it reports 0 failed and a pass count
  strictly above 105, the count recorded at BASE.
- **AC6** — When each new arm from S7 is staged against the tip WITHOUT the fix, it FAILS; the RED
  observation is recorded in this build's `RUN.md` before the arm lands.
- **AC7** — When `diff .claude/hooks/agent-cap.js tools/hooks/agent-cap.js` runs, it is empty, and
  the suite's own two-copy parity arm passes.

## 7. Gates

- `agent-cap self-test` — `tools/hooks/agent-cap.test.sh`, the leg that owns this file.
- `verifier fan-out` — `tools/workflows/check-verifier-fanout.sh`, which delegates to this hook.
- `agent-cap restatement` — `tools/check-agent-cap-restatement.sh`, the five values compared against
  the sources that own them.
- `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

- **F1 — how far does the repair reach: one view, two, or all three?** Rule 1 is where the report
  landed, but rules 2 and 3 read their own views and carry the same defect. Options: `stripStrings`
  only; `stripStrings` and `renderCodeView`; all three.
  RESOLVED (agent, 2026-09-01, delegated): all three. This is a FACT-QUESTION and the probe that
  decides it is stated: run the same mispairing shape against each rule's own verdict. The
  observation can produce a negative — rule 3 could have been immune, as it is to `/* don't */`,
  which it blanks. It was not: `R5` and `R6` admit a declared bound of 50 at HEAD and deny under the
  chosen candidate. Fixing two of three views would leave the class open one rule over, which is §7's
  gate-the-instance shape.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft, written after the five-candidate measurement in §4.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "strip string literals from a line of javascript before scanning
it for a call"` ranks `stripStrings`, `blankLiterals`, `offendingLines` and `renderCodeView` — all four
in `tools/hooks/agent-cap.js`, all fan-in 0. The seam this unit extends is `renderCodeView`, the
newest and most correct of the three views: it already does the ordered single pass the other two
approximate, and `literalEnd` is the decision lifted out of it so the other two can ask the same
question. No new file and no new module. `memory/map/features/agent-cap.md` is the dossier.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap.js blank string literals
per line instead of lexing the script, and what was decided about the unpaired quote repair" --terms
"agent-cap stripStrings renderCodeView blankLiterals unpaired quote fan-out fail-open template
literal regex literal line-aligned view rule 1 raw primitive"` — 31 hits. The two that bind:
`TOOL-aLexedStripper-3` and `-4`, both OPEN, both named in §3 as out of scope.

# TOOL-dMispairedQuote-3 — every rule is evaluated over both views, so no denial can be lost

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Correcting what counts as a string literal does not only un-hide fan-outs. It un-hides every OTHER
character the old mispairing was blanking, and two of this file's rules walk brackets and balance
parens ACROSS lines. Three DENY-to-ADMIT moves were reproduced against `TOOL-dMispairedQuote-1`'s
mechanism alone. This unit makes the change monotone in the DENY direction by construction.

## 2. Scope (IN)

- **S1** — Keep the three SHIPPED views in `tools/hooks/agent-cap.js` VERBATIM, renamed
  `stripStringsShipped`, `renderCodeViewShipped` and `blankLiteralsShipped`. Verbatim is the whole
  point: a paraphrase would be a second implementation whose disagreement with the original is
  exactly what this unit exists to rule out.
- **S2** — Each of the four rule functions takes a `shipped` selector choosing which view it reads:
  `offendingLines` (rule 1), `fanoutFindings` (rule 2), `capFindings` (rule 3) and
  `scanJoinFindings` (the ref-keyed-join ban). The fourth is in scope because it reads
  `blankLiterals` too, at `agent-cap.js:977`, which unit 1's own files-touched missed.
- **S3** — `main()` evaluates every rule over BOTH views and takes the union of their findings, keyed
  on the line number each finding already carries so one line reports one row. A denial from EITHER
  view stands.
- **S4** — The union helper is one function, `union(a, b)`, used by all four call sites. Not four
  inline merges.
- **S5** — Mirror every byte into `.claude/hooks/agent-cap.js`.
- **S6** — A regression arm per reproduced shape, each staged RED against unit 1's mechanism WITHOUT
  this unit: the backtick-inside-a-regex script above a multi-line cap-50 call; the regex-borne `)`
  on a multi-line call's argument line; and the `//` inside a quoted span inside a same-line
  template above a raw `parallel(`.
- **S7** — A PROPERTY arm over the tracked corpus, not a fixture: every tracked file fed to the
  shipped hook and to this one, asserting no file moves from exit 2 to exit 0. That is the class;
  S6's three are the instances that produced it.

## 3. Non-goals (OUT)

- Removing the shipped views once the new ones are trusted. The union IS the mechanism; deleting
  half of it deletes the guarantee.
- Modelling regex literals. That is the root of all three reproduced moves — a regex's contents
  supply the backtick, the `)` and the `//` — and closing it properly is a separate unit with its
  own division-versus-regex disambiguation. This unit bounds the damage without modelling.
- Reducing the union's FALSE POSITIVES. The union inherits the shipped view's false positives, which
  are the status quo, plus the new view's, which are measured at zero over the tracked corpus.
- `TOOL-aLexedStripper-3` and `-4`, as in unit 1.

## 4. Design

### Data model

Four rules, two views, one composition rule:

```js
const bad = ONLY === null ? union(offendingLines(script), offendingLines(script, true)) : []
```

`union` merges on the `n` (line number) field every finding already carries, so a rule that fires on
both views reports one row rather than two. The union is never empty when the shipped view alone
would have denied, which IS the guarantee.

### Alternatives rejected

| candidate | the test that rejected it |
|---|---|
| blank the union of what either view blanks | hides the fan-out again: the mispaired span the shipped view blanks is exactly the span carrying `parallel(`, so intersecting the EMITTED text restores the defect unit 1 removes |
| apply the opener decision to the BACKTICK branch too | closes the backtick half of the reproduction and neither the regex-borne `)` nor the `//`, and it costs tagged templates |
| model regex literals | the correct root fix and a bigger unit: it needs division-versus-regex disambiguation, which is its own heuristic with its own residual. Named in §3 as the follow-up |
| three fixtures, no property | the shapes were found by review, not by a rule. §7's gate-the-CLASS rule refuses a fixture set as the answer to a property |

### Measured

| measurement | result |
|---|---|
| the three reproduced moves | all three DENY under this unit, all three ADMIT without it |
| rule-1 shape corpus | 21/21, unchanged from unit 1 alone |
| rules 2 and 3 probes | 6/6, unchanged from unit 1 alone |
| shipped suite | 105 passed / 0 failed |
| every tracked file fed to both hooks | 1263 files, **0 flips to ADMIT**, 3 flips to DENY, all markdown records |

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `.claude/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` ·
`memory/map/generated/symbols.json` (regenerated — the shipped views add three top-level definitions
this file already contributes rows for).

## 5. Production-readiness checklist

- security — this unit IS a safety property. It cannot make the guard weaker than it is today, by
  construction, and S7 asserts that over the whole corpus rather than over a sample.
- perf / scale — every rule runs twice. The hook already runs once per tool call over a script bounded
  by what a caller sends; the shipped suite's wall time is the observation, not an estimate.
- a11y — N/A — a stdin/stderr hook with no interface.
- i18n — N/A — the predicate is over ASCII source syntax.
- error / empty / loading states — unchanged.
- observability — a finding reported from the shipped view carries that view's own explanation, which
  is the message an operator sees today. No new message text.
- risks — the union inherits BOTH views' false positives. Measured: 3 flips to DENY over 1263 tracked
  files, every one a markdown review record and none a workflow script.
- testing + left-shift gates — S6 and S7. Both land in `tools/hooks/agent-cap.test.sh`, whose leg is
  `subject = kit` and therefore HELD off an ordinary bar: this unit's Definition of Done runs
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and `GATE_FULL` alone does not
  lift the hold.
- migration / rollback — none. A revert is a file revert.
- user docs — `TOOL-dMispairedQuote-2` carries the prose, extended to name this unit's shipped-view
  block.

## 6. Acceptance criteria

- **AC1** — When `const re = /it's` + a backtick + `don't/` sits above a multi-line
  `boundedParallel(L.map(...), 50)`, the hook exits 2; without this unit it exits 0 and at BASE it
  exits 2.
- **AC2** — When a multi-line `boundedParallel(x, 50)` carries a regex-borne `)` between two prose
  apostrophes on its argument line, the hook exits 2.
- **AC3** — When a same-line template containing a quoted `'http://x'` sits before a raw
  `parallel(all.map(f))`, the hook exits 2.
- **AC4** — When every tracked file in this repo is fed to the shipped hook and to this one, the
  count of files moving from exit 2 to exit 0 is `0`.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, it reports 0 failed.
- **AC6** — When `grep -c 'function stripStringsShipped' tools/hooks/agent-cap.js` runs it reports 1,
  and `diff` of the two copies is empty.
- **AC7** — When each S6 arm is staged against a tree carrying unit 1 WITHOUT this unit, it FAILS,
  and the observation is recorded under `memory/builds/dMispairedQuote/build/`.

## 7. Gates

- `agent-cap self-test` — held off an ordinary bar; run it directly and with
  `GATE_SELFTESTS=1` at the Definition of Done.
- `verifier fan-out` · `agent-cap restatement` · `lexicon naming predicates` ·
  `codebase-map coverage + freshness` for the regenerated `symbols.json`.
- `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Promoted from spec-audit round 2's NON-CONVERGENT exit,
  blockers 1, 8 and 17, per BUILD-METHOD M4.

## 10. Reuse audit

No existing seam fits, and the evidence is the shape of the file rather than a miss:
`tools/codebase-map/reuse_lookup.py "strip string literals from a line of javascript before scanning
it for a call"` ranks the four view and rule functions of `tools/hooks/agent-cap.js` itself, all
fan-in 0, and this unit's mechanism is a COMPOSITION over them rather than a new view. What it
extends is the file's own rule-function signature, which already carries the finding shape
(`{ n, line, why }`) the union keys on — so the merge is four characters of selector and one helper,
not a new abstraction. The dossier is `memory/map/features/agent-cap.md`.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap.js blank string literals
per line instead of lexing the script, and what was decided about the unpaired quote repair" --terms
"agent-cap stripStrings renderCodeView blankLiterals unpaired quote fan-out fail-open template
literal regex literal line-aligned view rule 1 raw primitive"` — the same 31-hit query unit 1
records, re-run per M7. `TOOL-aLexedStripper-5` is the record that binds: it ratified a
cannot-regress argument about one view, and this unit is that argument made enforceable for all four
rules instead of asserted about one.

# TOOL-dMispairedQuote-3 — every rule is evaluated over both views, so no denial can be lost

**Status:** OPEN · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-TOOL-dMispairedQuote-3-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-3-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Correcting what counts as a string literal does not only un-hide fan-outs. It un-hides every OTHER
character the old mispairing was blanking, and two of this file's rules walk brackets and balance
parens ACROSS lines. Three DENY-to-ADMIT moves were reproduced against `TOOL-dMispairedQuote-1`'s
mechanism alone. This unit makes the change monotone in the DENY direction by construction.

## 2. Scope (IN)

- **S1** — Keep the three SHIPPED views in `tools/hooks/agent-cap.js` VERBATIM, as
  `renderShippedLine`, `renderShippedView` and `renderShippedBlanks`. Verbatim is the whole point: a
  paraphrase would be a second implementation whose disagreement with the original is exactly what
  this unit exists to rule out.
- **S2** — **A DISPATCHER, not a threaded selector.** The three view NAMES every rule already calls
  become one-line dispatchers over a module-level `VIEW_MODE`, and **no rule function changes at
  all**. The first cut threaded a `shipped` flag through each rule, which needs a CENSUS of which
  rule reads which view — and round 1 measured that census wrong for two of the four:
  `fanoutFindings` reads the lexed view AND the per-line one on its fallback branch, and
  `scanJoinFindings` reads the blanked view AND the per-line one. A census that has to be right is a
  census that can be wrong, and getting it wrong drops half the guarantee silently.
- **S3** — `runBothViews(rule, script)` runs one rule under `lexed`, flips `VIEW_MODE` to `shipped`,
  runs it again, restores the mode in a `finally`, and merges. A denial from EITHER pass stands.
- **S4** — The merge keys on `n` **and on `why`**, not on `n` alone: `capFindings` can push more than
  one finding for a single line, and keying on the line number alone drops the second. Rule 1's
  finding shape is `{ line, n }` with no `why` at all, which the key handles as the empty string.
- **S5** — All FOUR rule call sites route through `runBothViews`: `offendingLines` (rule 1),
  `fanoutFindings` (rule 2), `capFindings` (rule 3) and `scanJoinFindings` (rule 5, the
  ref-keyed-join ban). Rule 5's call site is NOT wrapped in the `ONLY === null` guard the other three
  carry — that is deliberate in the shipped file, because `--only=join` selects exactly that rule —
  and this unit preserves the asymmetry rather than tidying it away.
- **S6** — **Every new name leads with a verb the lexicon declares**, and the two dispatchers take
  the place of the file's two existing verb offenders. Measured: the `lexicon naming predicates` leg
  moves from `offenders=463` to `461` against a shrink-only pin, so the pin FALLS.
- **S7** — Mirror every byte into `.claude/hooks/agent-cap.js`.
- **S8** — A regression arm per reproduced shape, each staged RED against unit 1 WITHOUT this unit:
  the backtick-inside-a-regex script above a multi-line cap-50 call (rule 3); the regex-borne `)` on
  a multi-line call's argument line (rule 3); the `//` inside a quoted span inside a same-line
  template above a raw `parallel(` (rule 1); and an `agent(` fan whose receiver is hidden the same
  way (rule 2). Rule 5 gets one too, so no rule is covered only by the property.
- **S9** — **The PROPERTY arm**, over the whole tracked corpus and against the BASE BLOB. It reads
  the shipped hook as `git show <BASE>:tools/hooks/agent-cap.js` into a temp file — NOT from the
  working tree, where after landing the two would be the same file and the assertion would degrade
  to "a superset contains its own subset", which is true of any merge and is this repo's
  assertion-between-two-derived-values class. In a tree where that blob does not resolve — an
  adopter that copy-installed the kit — the arm ANNOUNCES A SKIP naming why, rather than passing.
- **S10** — A byte arm: each `renderShipped*` body equals the corresponding function in the BASE
  blob, so "verbatim" is checked rather than asserted. Same blob, same skip rule.

## 3. Non-goals (OUT)

- Removing the shipped views once the new ones are trusted. The dual evaluation IS the mechanism;
  deleting half of it deletes the guarantee.
- Modelling regex literals. That is the root of all three reproduced moves — a regex's contents
  supply the backtick, the `)` and the `//` — and closing it properly is a separate unit with its
  own division-versus-regex disambiguation. This unit bounds the damage without modelling.
- Reducing the merged FALSE POSITIVES. The merge inherits the shipped view's, which are the status
  quo, plus the new view's, measured at 3 files over the tracked corpus and named in §5.
- `TOOL-aLexedStripper-3` and `-4`, as in unit 1.
- Unit 2's carrier list. Round 2's blocker 8 left a prose half — unit 2's S1 replacement text says
  "its line is still blanked", which is untrue inside a template span. That is assigned to
  `TOOL-dMispairedQuote-2`, whose §2 S1 now carries it, and unit 2 is sequenced last so it describes
  what both code units actually did.

## 4. Design

### Data model

Three dispatchers, one mode, one runner:

```js
let VIEW_MODE = 'lexed' // 'lexed' | 'shipped'
function renderStrippedView(line) {
  return VIEW_MODE === 'shipped' ? renderShippedLine(line) : renderStrippedLine(line)
}
```

A module-level mode is safe here and is nowhere near a general licence: this file is a one-shot CLI
that reads stdin, decides and exits. There is no concurrency, no second script in flight, and
`runBothViews` is the only writer, in a `try`/`finally`.

### Alternatives rejected

| candidate | the test that rejected it |
|---|---|
| blank the union of what either view blanks | hides the fan-out again: the mispaired span the shipped view blanks is exactly the span carrying `parallel(`, so intersecting the EMITTED text restores the defect unit 1 removes |
| a `shipped` parameter threaded through each rule | round 1 measured the required census wrong for two of four rules — the two that read a SECOND view on a fallback branch. Reproduced against the built candidate |
| a per-line delimiter-conservation property in the views | unit 1's round 2 proposed it; it constrains the VIEW where the defect is in the VERDICT, and a view that may not emit a `(` the shipped view blanked cannot emit `parallel(` either |
| apply the opener decision to the BACKTICK branch too | closes the backtick half of the reproduction and neither the regex-borne `)` nor the `//`, and it costs tagged templates |
| model regex literals | the correct root fix and a bigger unit: it needs division-versus-regex disambiguation, which is its own heuristic with its own residual. Named in §3 as the follow-up |
| three fixtures, no property | the shapes were found by review, not by a rule. §7's gate-the-CLASS rule refuses a fixture set as the answer to a property |

### Measured

Every row below was run against the built candidate, not estimated.

| measurement | result |
|---|---|
| the three reproduced DENY-to-ADMIT moves | all three DENY with this unit; all three ADMIT with unit 1 alone; all three DENY at BASE |
| rule-1 shape corpus | 21/21, against 14/21 at BASE |
| rules 2 and 3 probes | 6/6, against 3/6 at BASE |
| shipped suite | 105 passed / 0 failed, the same count as BASE |
| `lexicon naming predicates` | `offenders=461`, below the shrink-only pin of 463 |
| every tracked file fed to the BASE BLOB and to this candidate | 1265 files, **42 DENY at BASE**, **0 flips to ADMIT**, 3 flips to DENY |
| that sweep's wall clock | 140 s, plus the suite's 21 s, against the leg's declared ceiling of 740 s |

The at-risk population is 42, not zero: only a file that DENIES at BASE can regress, and 42 do. The
three flips toward DENY are markdown review records, never workflow scripts.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `.claude/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` ·
`memory/map/generated/symbols.json` (regenerated).

## 5. Production-readiness checklist

- security — this unit IS a safety property. It cannot make the guard weaker than BASE, by
  construction, and S9 asserts that over the whole corpus rather than over a sample.
- perf / scale — the runtime hook runs every rule twice; one whole-corpus sweep is 140 s and the
  hook's own per-call cost is doubled from a few milliseconds. Both measured, both stated above.
- a11y — N/A — a stdin/stderr hook with no interface.
- i18n — N/A — the predicate is over ASCII source syntax.
- error / empty / loading states — unchanged. `runBothViews` restores the mode in a `finally`, so a
  rule that throws cannot leave the next one reading the wrong view.
- observability — a finding reported from the shipped pass carries that view's own explanation, which
  is the message an operator sees today. No new message text.
- risks — the merge inherits BOTH views' false positives. Measured: **3** flips to DENY over 1265
  tracked files, every one a markdown review record and none a workflow script. That figure is `3`
  everywhere it appears in this spec.
- testing + left-shift gates — S8, S9 and S10, all in `tools/hooks/agent-cap.test.sh`, whose leg is
  `subject = kit` and therefore HELD off an ordinary bar: this unit's Definition of Done runs
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and `GATE_FULL` alone does not
  lift the hold.
- migration / rollback — none. A revert is a file revert.
- user docs — `TOOL-dMispairedQuote-2` carries the prose, extended to name this unit's dispatcher
  block and to correct the ceiling sentence unit 1's round 2 left standing.

## 6. Acceptance criteria

- **AC1** — When `const re = /it's` + a backtick + `don't/` sits above a multi-line
  `boundedParallel(L.map(...), 50)`, `node tools/hooks/agent-cap.js` exits 2; with unit 1 alone it
  exits 0 and at BASE it exits 2. **Rule 3.**
- **AC2** — When a multi-line `boundedParallel(x, 50)` carries a regex-borne `)` between two prose
  apostrophes on its argument line, it exits 2 and the message names the CALL SITE bound. **Rule 3.**
- **AC3** — When a same-line template containing a quoted `'http://x'` precedes a raw
  `parallel(all.map(f))`, it exits 2 and the message names the raw primitive. **Rule 1.**
- **AC4** — When an `agent(` fan whose receiver is hidden by the same mispairing runs, it exits 2 and
  the message names the verifier-arity rule. **Rule 2.**
- **AC5** — When a ref-keyed join hidden the same way runs, it exits 2 and the message names the join
  ban, and `--only=join` still selects that rule alone. **Rule 5.**
- **AC6** — When every tracked file is fed to `git show d65da7ab:tools/hooks/agent-cap.js` and to the
  built hook, the count of files moving from exit 2 to exit 0 is `0`, and the count DENYING at BASE
  is reported and is greater than zero — a population of zero would make the assertion vacuous.
- **AC7** — When each `renderShipped*` body is compared byte-for-byte with its counterpart in the
  BASE blob, they are equal.
- **AC8** — When `bash tools/hooks/agent-cap.test.sh` runs, it reports 0 failed and a pass count of
  at least 105, the count measured at BASE.
- **AC9** — When `python tools/lexicon/lexicon.py --check` runs, `P1 verb` reports `offenders` no
  greater than `VERB_OFFENDER_PIN`, and the measured value is 461.
- **AC10** — When each arm from S8 **and** the property arm from S9 is staged against a tree carrying
  unit 1 WITHOUT this unit, it FAILS. The property arm included: a class-level guard that has never
  been observed RED is §7's own could-not-fail shape. Each observation is recorded under
  `memory/builds/dMispairedQuote/build/`.
- **AC11** — When the BASE blob does not resolve, the property and byte arms print a line matching
  `skip ` that names the missing blob, and `bash tools/hooks/agent-cap.test.sh` reports 0 failed.

## 7. Gates

- `agent-cap self-test` — held off an ordinary bar; run it directly and with `GATE_SELFTESTS=1` at
  the Definition of Done. Declared ceiling 740 s; measured 161 s with S9 added.
- `verifier fan-out` · `agent-cap restatement` · `lexicon naming predicates` ·
  `kit version markers` · `codebase-map coverage + freshness`.
- `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Promoted from unit 1's spec-audit round 2 NON-CONVERGENT exit,
  blockers 1, 8 and 17, per BUILD-METHOD M4.
- rev-2 · 2026-09-01 · folded spec-audit round 1 over this unit: 5 blockers, 4 highs, 5 mediums.
  The selector became a DISPATCHER after the census it needed was measured wrong for two of the four
  rules; the property arm now reads the BASE BLOB rather than an in-tree copy and announces a skip
  where that blob does not resolve; AC10 quantifies over the property arm too; every new name was
  respelled with a declared verb and the pin measured FALLING to 461; unit 2 took blocker 8's carrier
  half. Highs: per-rule acceptance criteria including rules 2 and 5, the at-risk population measured
  at 42 rather than assumed empty, a pass-count floor on the suite, and the false-positive figure
  stated as `3` in every section. Mediums: the byte arm comparing the shipped bodies to BASE, rule
  5's deliberately unguarded call site named, the merge keyed on `n` and `why`, the cost measured at
  161 s against a 740 s ceiling, and rule 1's `{ line, n }` shape stated correctly.

## 10. Reuse audit

No existing seam fits, and the evidence is the shape of the file rather than a miss:
`tools/codebase-map/reuse_lookup.py "strip string literals from a line of javascript before scanning
it for a call"` ranks the view and rule functions of `tools/hooks/agent-cap.js` itself, all fan-in 0,
and this unit's mechanism is a COMPOSITION over them rather than a new view. What it extends is the
file's own rule-function signature: three of the four rules push `{ n, line, why }` and rule 1 pushes
`{ line, n }`, so the merge key is `n` plus a `why` that may be absent — nine lines, not a new
abstraction. The dossier is `memory/map/features/agent-cap.md`.

Naming consult: `python tools/lexicon/lexicon.py --suggest` was run for every name this unit
introduces — `renderStrippedView`, `renderStrippedLine`, `renderShippedLine`, `renderLexedView`,
`renderShippedView`, `renderBlankedLiterals`, `renderBlankedView`, `renderShippedBlanks` and
`runBothViews` — and all nine answer OK. The rev-1 spellings `stripStringsShipped`,
`blankLiteralsShipped` and `bothViews` were refused, and the `--check` leg measured them RED.

Recall terms used: `python tools/memory-recall/query.py "why does agent-cap.js blank string literals
per line instead of lexing the script, and what was decided about the unpaired quote repair" --terms
"agent-cap stripStrings renderCodeView blankLiterals unpaired quote fan-out fail-open template
literal regex literal line-aligned view rule 1 raw primitive"` — the same 31-hit query unit 1
records, re-run per M7. `TOOL-aLexedStripper-5` is the record that binds: it ratified a
cannot-regress argument about one view, and this unit is that argument made enforceable for all four
rules instead of asserted about one.

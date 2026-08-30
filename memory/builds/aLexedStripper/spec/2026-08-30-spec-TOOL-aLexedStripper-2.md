# TOOL-aLexedStripper-2 — `agent-cap`'s lens counter reads a template-aware view

**Status:** SPECCED · rev-2 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md) | spec-audit | TOOL-aLexedStripper-1 |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round2.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round2.md) | spec-audit | TOOL-aLexedStripper-1 |

<!-- /gen:spec-records -->

## 1. Goal

`fanoutFindings` in `tools/hooks/agent-cap.js` must count a lens array's elements over a view that
knows what a template literal is, so ordinary English in a lens prompt stops being counted as code
structure and a correct five-lens harness stops being denied for its prose. No verdict the guard
reaches today may move in either direction: not a DENY becoming an ADMIT, which is a fail-open on
the only mechanical control against an unbounded agent burst, and not an ADMIT becoming a DENY,
which is the false-positive class this unit exists to close reappearing one construct over.

## 2. Scope (IN)

- **S1** — Add `renderCodeView(script)` to `tools/hooks/agent-cap.js`: a LINE-ALIGNED view, one
  output line per input line, in which template-literal PROSE is blanked and `${…}` interpolation
  bodies are kept verbatim as code. `fanoutFindings` reads it instead of the per-line
  `stripStrings(l).split('//')[0]` at `:259`.
- **S2** — `renderCodeView` tracks `${…}` nesting. A backtick inside an interpolation opens a nested
  template, and its close returns to the outer one, so `` `a${`b`}c` `` is one balanced construct and
  not three mode flips. Nesting depth is tracked, not assumed to be one.
- **S3** — `renderCodeView` reports whether the scan ENDED inside an unterminated template literal.
  When it did, `fanoutFindings` treats the script as unmeasurable and DENIES. This is the fail-closed
  half, and it is scope rather than an optimisation: without it S1 is a measured deny-to-admit
  regression.
- **S4** — Rules 1, 3 and 5 are untouched and keep the views they read today. `blankLiterals` keeps
  its two existing consumers, so its three dozen measured arms are not re-baselined.
- **S5** — Fixtures in `tools/hooks/agent-cap.test.sh`, table-driven, one row per shape, covering
  BOTH directions: every prose spelling in §4's measured table with its expected verdict, and every
  fail-open shape that must stay DENIED.
- **S6** — Bump `KIT_AGENT_CAP_VERSION`.

## 3. Non-goals (OUT)

- Not touching rule 1 `offendingLines`, rule 3 `capFindings` or rule 5 `scanJoinFindings`.
- Not changing `CAP`, `MAX_VERIFIERS` or `MAX_LENSES`. No number moves.
- Not fixing `TOOL-aCandidStub-1` (an empty array literal grown by a later `push`) or
  `TOOL-aNumeralWarden-2` (the enclosing-opener walk defeated by distance). Both are open rows
  against this file and both are a different mechanism.
- Not fixing `TOOL-dFramedEntrypoint-1`, which is two prose sentences in `AGENTS.md` §8 and
  `tools/hooks/README.md`, not a code change.
- Not making rule 3 fail closed on an unterminated template literal. It reads `blankLiterals` today
  and is already blind there; widening that is a second unit's work, filed as
  `TOOL-aLexedStripper-4`.

## 4. Design

### The mechanism

Rule 2 blesses an identifier as a bounded receiver when it is assigned from an array literal whose
top-level element count is at or under `MAX_LENSES`. It measures that over `code`, built per line by
`stripStrings`, which blanks `'…'` and `"…"` and deliberately leaves backticks alone. Lens prompts
ARE backticked template literals full of English, so their punctuation reaches two counters that
expect code: the `[`/`]` join-forward walk at `:326` and `topLevelArgs` at `:562`.

### What reproduces at BASE — measured, both array shapes

Every script below is a CORRECT five-element lens array fanned through
`boundedParallel(…, MAX_VERIFIERS)`; only the prose of one prompt differs. Run against
`git show 19d9b328:tools/hooks/agent-cap.js`. `0` is ADMIT and is the right answer for every row.

| prose contains | multi-line array | one-line array | mechanism |
|---|---|---|---|
| a literal `...` | **2 DENY** | **2 DENY** | the `:344` spread guard reads prose punctuation as a spread |
| an unmatched `[` | **2 DENY** | **2 DENY** | opens the `[`/`]` join-forward walk at `:326` and never closes |
| an unmatched `]` | **2 DENY** | 0 | closes the walk early, truncating the literal |
| an unmatched `)` | **2 DENY** | 0 | drives `topLevelArgs` depth negative |
| an unmatched `}` | **2 DENY** | 0 | same depth shift, brace arm |
| an unmatched `(` | 0 | 0 | shifts depth the other way and UNDER-counts, which passes |
| an unmatched `{` | 0 | 0 | same |
| two ASCII apostrophes | 0 | 0 | the blanked span eats no bracket in this shape |
| U+2019 apostrophes | 0 | 0 | not matched by `stripStrings` at all |
| an em dash | 0 | 0 | no structural character |

Five spellings deny in the multi-line array, which is the shape every shipped harness uses because
every one of them is prettier-formatted. Two of those five also deny on one line.

**Two corrections this table makes to rev-1**, both from the round-1 audit and both re-measured
before folding. Rev-1 listed only `...` and `)`; the audit found that `[`, `]` and `}` also deny and
that rev-1 shipped them untested, which is correct and is folded above. The audit also claimed no
unmatched-`)` shape denies at all, and that is refuted by the multi-line column: 17 one-line variants
admitting does not reach the shape the harnesses actually write. The row stays, with the array shape
that decides it now named.

**The apostrophe rows matter as a negative result.** `ABL-dPinnedVintage-4` attributes the denial to
two apostrophes eating a `)`, and the adopter's gotcha prescribes U+2019 as the workaround. Both
rows are `0` in both shapes at BASE: the diagnosis is stale and the workaround addresses nothing.

### Why not `blankLiterals` itself

Rev-1's S1 named `blankLiterals` directly. The round-1 audit confirmed two measured deny-to-admit
regressions in that reading, and both were reproduced against BASE for this revision.

| # | shape | verdict at BASE | verdict under rev-1's S1 |
|---|---|---|---|
| 1 | an unterminated backtick above `boundedParallel(all.map(…agent…), 5)` where `all = args.everything` | **2 DENY** | 0 ADMIT |
| 2 | an `agent(` inside a multi-line `${ await Promise.all(\n all.map(…) \n) }` | **2 DENY** | 0 ADMIT |

Shape 1 is `blankLiterals`' `let mode` at `agent-cap.js:506`, declared OUTSIDE the per-line loop at
`:507`. One unmatched backtick leaves every later line blanked to `''`, `fanoutFindings` finds no
fan-out site, and the hook exits 0 on a script BASE denies. S3 answers it by failing closed.

Shape 2 is why S2 exists rather than rev-1's "adopt rule 5's second view". Rule 5's second view is
`stripStrings(raw).split('//')[0]` then `.match(/\$\{[^}]*\}/g)` — per LINE, feeding three
context-free regex bans. Rule 2's judgement is not context-free: it needs the line-indexed `[`/`]`
join-forward walk at `:326`, the enclosing-opener window built as `code[k] + '\n' + win`, and an
`ok` set accumulated over two full passes of the whole line array. A flat list of span strings
cannot feed any of those, and a multi-line span has no `}` on its opening line so the per-line regex
matches nothing at all. The interpolation body must therefore be preserved IN PLACE, on the line it
occupies, which is what a line-aligned view gives and a span list cannot.

Rule 5's own header at `:888` records that its ceiling is acceptable because "the outer views still
carry the identifier ban". Rule 2 has no outer fallback: once template contents are blanked, an
`agent(` inside `${…}` is gone from every view rule 2 reads. The precondition does not transfer,
which is why the mechanism could not simply be adopted.

### `renderCodeView`

One left-to-right pass, same state machine shape as `blankLiterals`, three differences:

1. Output is line-aligned — one output line per input line, so every positional walk in rule 2
   indexes as it does today.
2. In `tmpl` mode, a `${` switches to code mode and its body is COPIED; the matching `}` returns to
   `tmpl`. Depth is counted, so a nested template inside an interpolation is handled and
   `` `a${`b`}c` `` is balanced rather than leaving the scan in `tmpl`.
3. It returns the view together with a boolean saying whether the scan ended in `tmpl` mode.

Comments and quoted strings are handled exactly as `blankLiterals` handles them; that half is not
re-derived.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — `renderCodeView`, the view swap at `:259`, the fail-closed branch,
  the `blankLiterals` header comment (which says "the two rules above" and after S1 means one), and
  `KIT_AGENT_CAP_VERSION`.
- `tools/hooks/agent-cap.test.sh` — the table-driven fixtures.

### Alternatives rejected

- **`blankLiterals` unchanged, as rev-1 specified.** Rejected on measurement: the two deny-to-admit
  shapes above.
- **Teach `stripStrings` about backticks.** Rejected: it is per line and a template literal spans
  lines, so it cannot be made correct without becoming a state machine.
- **Track a `tmpl` flag inside rule 2's own two loops.** Rejected: it puts the same state machine in
  two counters, and `topLevelArgs` has a second caller that would then disagree with the first.
- **Widen `MAX_LENSES`.** Rejected: the count is not wrong, the counter is, and the constant's own
  comment records that it was once raised to fit a miscount.

## 5. Production-readiness checklist

- security — this IS the security surface, and §6 is written around what must stay DENIED. The
  guard is the only mechanical control against an unbounded agent burst; two of this unit's criteria
  exist because rev-1 would have opened one.
- perf / scale — one extra pass over the script, bounded by its length. `blankLiterals` already runs
  twice per invocation for rules 3 and 5.
- a11y — N/A, no user interface.
- i18n — the class includes non-ASCII prose. U+2019 admits at BASE, so the adopter's workaround was
  never load-bearing and nothing here depends on it.
- error / empty / loading states — an unterminated template literal is the dominant error state and
  is answered by S3, fail-closed, checked by AC7. An empty script yields an empty view and no
  finding, as today.
- observability — the hook writes its verdict to stderr and exits 2; unchanged.
- risks — a fail-open regression, in the two shapes §4 tables. Both have a criterion and a fixture.
- testing + left-shift gates — table-driven fixtures, one row per shape, both directions, each
  staged and observed at BASE before the wiring.
- migration / rollback — none; single-file revert.
- user docs — the `blankLiterals` header comment at `:499-503` states an arity of its own consumers
  and becomes stale on S1. It is in §4's files-touched and is rewritten in the same commit.

## 6. Acceptance criteria

- **AC1** — When a five-element lens array whose prose contains a literal `...` is passed to
  `node tools/hooks/agent-cap.js` as a `Workflow` script, it exits `0`, in BOTH the multi-line and
  one-line array shapes, against `2` and `2` at BASE.
- **AC2** — When that array's prose contains an unmatched `[`, it exits `0` in both shapes, against
  `2` and `2` at BASE.
- **AC3** — When that array's prose contains an unmatched `]`, `)` or `}`, the multi-line shape exits
  `0`, against `2` at BASE for each.
- **AC4** — When that array's prose contains an unmatched `(`, an unmatched `{`, ASCII apostrophes,
  U+2019 apostrophes or an em dash, it exits `0`, as it does at BASE — the ADMIT rows do not move.
- **AC5** — When a SIX-element lens array is run through `bash tools/hooks/agent-cap.test.sh`, it
  exits `2`.
- **AC6a** — When an `agent(` fan over an unbounded receiver is written inside a SINGLE-line `${…}`
  interpolation, `node tools/hooks/agent-cap.js` exits `2`, as at BASE.
- **AC6b** — When the same fan is written inside a `${…}` interpolation spanning three or more
  lines, it exits `2`, as at BASE. Under rev-1's S1 this exits `0`.
- **AC6c** — When a PROVABLY BOUNDED five-element fan is written inside a `${…}` interpolation, it
  exits `0`, as at BASE. This is the ADMIT counterpart that stops S1 becoming a blanket deny.
- **AC7** — When a script fans out over an unbounded receiver BELOW an unterminated template
  literal, `node tools/hooks/agent-cap.js` exits `2`, as at BASE. The criterion pins the verdict,
  not the absence of a crash.
- **AC8** — When a script contains a nested template `` `a${`b`}c` `` followed by a correct
  five-element lens fan, it exits `0` — S2's nesting, and the false positive S3 would otherwise
  introduce.
- **AC9** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm that passes at BASE still
  passes, including the `TOOL-dTieredTribunal-11` round-2 finding-4 script
  (`ALL.filter((L) =>` `` `(`.length > 0).reduce((acc, b) => args.big, [])`` marked
  `gov:fixed-verifiers`), which exits `2` at BASE and must keep doing so.
- **AC10** — When each new fixture is staged against the code at BASE, its BASE verdict is the one
  §4's tables record, observed with `bash tools/hooks/agent-cap.test.sh`, and written into this
  unit's acceptance ledger.
- **AC11** — When `bash tools/check-kit-versions.sh` runs, `KIT_AGENT_CAP_VERSION` is bumped and
  well-formed.

## 7. Gates

`agent-cap self-test` · `agent-cap restatement` · `kit-versions` · `playbook parity` ·
`lexicon naming predicates` · and the full bar at the push boundary.
`tools/check-playbook-parity.sh` machine-compares five agent-cap values against the charter, so a
constant that moved without its prose would red there; this unit moves no constant except the
version. `renderCodeView` leads with `render`, a declared verb, so the shrink-only
`VERB_OFFENDER_PIN` of 463 does not move.

## 8. Open questions

- **F1 — should rule 1 `offendingLines` take the same view?** A raw `parallel(` written inside a
  lens prompt is prose and is denied today, which is the same false-positive class one rule over.
  Against that: rule 1's ceiling is documented as deliberately fail-closed in the file header, and
  widening its blind spot is the one direction this unit's own §5 forbids without its own fixtures.
  RESOLVED (agent, 2026-08-30, delegated): out of scope here, filed as `TOOL-aLexedStripper-3` in
  `memory/backlog/TOOL.md`. It is a preference between two defensible readings rather than something
  an observation decides, and M3's rule sends a fork with no feature-richness difference to the
  option with fewer follow-ups.
- **F2 — where does the interpolation view live?** Rev-1 said "at the call site, mirroring rule 5".
  The round-1 audit measured that rule 5's per-line span view cannot feed rule 2's line-indexed
  walks. RESOLVED (agent, 2026-08-30, delegated): inside `renderCodeView`, line-aligned, per S2. The
  observation decides it — a span list has no line index and a multi-line span has no `}` on its
  opening line — so this is a FACT-QUESTION outcome and not a preference.
- **F3 — should rule 3 `capFindings` also fail closed on an unterminated template literal?** It
  reads `blankLiterals` today and is already blind there, so the gap predates this unit and is not
  introduced by it. Widening it means re-baselining rule 3's arms, which S4 exists to avoid.
  RESOLVED (agent, 2026-08-30, delegated): out of scope, filed as `TOOL-aLexedStripper-4`. Veto 3
  is not reached — this unit narrows a surface and declines to widen a different one — and M3's
  tie-break prefers the option leaving fewer open questions inside this unit's own diff.

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, written from a measured reproduction at BASE `19d9b328` and
  from the prior closing-diff review that specified the same fix.
- rev-2 · 2026-08-30 · folded the round-1 spec audit
  (`2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round1.md`, verdict BLOCKED, 2 blockers).
  Blocker 1 and blocker 25 both reproduced against BASE and both accepted: S1 no longer names
  `blankLiterals`, S2 and S3 are new, and AC6/AC7 now pin verdicts instead of the absence of a
  crash. §4's BASE table re-measured across both array shapes — three spellings added, and the
  audit's claim that no unmatched-`)` shape denies is refuted with the multi-line column. F1's
  filing renumbered to `TOOL-aLexedStripper-3` after the audit found it colliding with this build's
  own unit id. Highs 36, 31 and 11 folded into §4, AC6c and §5.

## 10. Reuse audit

`python tools/memory-recall/query.py` with the terms below returned, as its second hit,
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff-round2.md:174`,
which states rev-1's fix in the same words: *give `fanoutFindings` the `blankLiterals(script)` lines
instead of `stripStrings`*. The seam is `blankLiterals` at `agent-cap.js:504` and this unit still
extends it — `renderCodeView` is that state machine with the two properties rule 2 needs and rules
3 and 5 do not. `tools/codebase-map/reuse_lookup.py` independently ranked `blankLiterals` and
`stripStrings` as the top two candidates for the same behaviour phrase.

Recall terms used, for M7 re-runs: `agent-cap stripStrings blankLiterals template literal lens array
bounded receiver interpolation view fan-out counter prose`.

**Two hits that were STALE, recorded because M5 requires it.** That review's own suggested fix is
one of them: taken literally it is rev-1's S1, and rev-1's S1 is measured to open two deny-to-admit
shapes. A prior review's fix is prior art, not a verdict, and this is the case M5 warns about — the
hit was right about the seam and wrong about the wiring. The second is
`ABL-dPinnedVintage-4`, which names version 1.6 and attributes the denial to two apostrophes eating
a `)`; at 1.8 an apostrophe pair admits in both array shapes, and its prescribed U+2019 workaround
admits too. The adopter's row and its gotcha both need correcting from §4's table once this lands.

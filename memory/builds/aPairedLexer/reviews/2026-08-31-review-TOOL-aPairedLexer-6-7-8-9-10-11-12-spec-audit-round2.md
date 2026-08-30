**Serves:** spec-audit TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

# Spec audit round 2 — the same seven units at rev-2, checked against their own fold

*Node a, 2026-08-31, round 2. Round 1 returned BLOCKED with 7 blocker rows over 4 distinct blocking
defects; every one of its findings was folded into a rev-2 of the spec that owned it. This round
audits the FOLD: whether each closure closed, and what the closure introduced. The central amendment
moved the declined-slash LEAK report out of `TOOL-aPairedLexer-6` and into `TOOL-aPairedLexer-8` S3's
shared predicate, reordering the build to 8, then 7, then 6 — so the audit aimed at that predicate,
at the reachability of the criteria the reorder left behind, and at the two units the reorder does
not touch. A parallel fan of primed finder lenses over the seven specs, the two scanners they change,
the extractor the seventh changes, `memory/guides/BUILD-METHOD.md` M2, and the shipped suite they
inherit, then skeptics prompted to REFUTE each finding against the source at the pinned base. Every
behavioural claim below was re-derived by the synthesis pass: a predicate implemented exactly as its
spec words it and run over the spec set's own fixtures, an exit code measured by piping a real
`Workflow` payload into the real hook, or a Python value printed by calling the real extractor.*

Reviewed subjects, each pinned at the blob actually read:

- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-6.md@165b90b2035f`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-7.md@460f3ddaa99c`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-8.md@da7631c6ef64`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-9.md@33b257fc92a5`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-10.md@ae0d90f99d8f`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-11.md@11f4a1c56fe6`
- `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-12.md@5693e35a9a9d`

Round 2.

## Verdict: BLOCKED

The counts sit here rather than on the heading, because that line's token is a closed set and a tally
appended to it turns a structural check into a semantic one.

**5 blockers and 5 highs stand.** Read the drop from 7 to 5 carefully before treating it as
convergence. Round 1's 7 was 7 ROWS over 4 distinct blocking defects; this round's 5 is 5 rows over
5 distinct blocking defects, because duplicate rows naming one address with one fix are consolidated
here rather than padded out. Row-to-row the count fell, 5 against 7. Defect-to-defect it ROSE, 5
against 4. Both numbers are stated because the M4 comparison is only meaningful between counts
measured the same way, and the two ways disagree about the direction. On the substance there is no
ambiguity: three of the five blockers did not exist before rev-2. The fold introduced them.

**Review shape:** raw 28, confirmed 18, refuted 10, unverified 0, precision 0.64. The 18 confirmed
findings consolidate into the 10 adjudicated rows below; each row names the finder ids it absorbs.
Four independent finders reported the ordering violation (B2), three reported the unit 12 ceiling
inversion (H2), two each reported the S3 over-fire (B1), the member guard (B3) and the unit 11 view
pair (H1) — the clustering is itself a signal about how reachable these defects are from a cold read.

**The load-bearing sentence.** rev-2 correctly diagnosed round 1's central defect — one question,
two views, two answers — and correctly moved the leak report into a shared predicate. What it did
not do is bound the predicate it created. S3's leak test as worded is a raw character scan with no
closure test, so it fires on ordinary division; unit 6 §4 argues it does not, from a one-slash line;
and both precision controls in the set are one-slash lines, so nothing anywhere in the seven units
can observe the class. The fold answered the precision question with a fixture on the wrong side of
the boundary it was written to pin.

## What the fold DID close

Stated first because it is real and because the promoted work should not re-do it.

- **Finding 26/1/30 — the routing.** Unit 6 S2 now folds one `dirty` into both
  `renderCodeView.unterminated` and `blankLiterals.clean`. Verified against the shipped file that
  this reaches all four rules: rules 1 and 2 read `view.unterminated` (`agent-cap.js:92`, `:364`),
  rule 3 reads `_bl.clean` (`:726`, `:732`, `:742`), rule 5 reads `_bl.clean` (`:1049`, `:1050`).
  Unit 6 S2's claim that all four rules now fall back is TRUE. rev-1's zero-widening defect is gone.
- **Findings 36/18 — the opener set.** S3's set is a backtick, a quote, `/*` and `*/`, not a backtick
  alone, and unit 6 AC5 pins the block-opener row. `TOOL-aLexedStripper-5` is cited in unit 8 §10 for
  the reason. Closed.
- **Finding 37 — unit 11's borrowed trigger.** AC1 now names its trigger literally (an
  ambiguous-position declined slash HOLDING A BACKTICK), says in §4 why rule 2's trigger differs
  from its siblings', and states measured verdicts per version. Closed.
- **Findings 21/31 — unit 12's design.** rev-1's compensating pass inside a phantom span is gone and
  replaced by modelling regex literals. The design is right; only its stated CONSEQUENCE is wrong
  (H2).
- **Finding 16/6 — unit 9's interface.** S1 now states which view supplies the line set, detection,
  bindings and reporting, and which supplies joins. That half is closed; what S2b then does with a
  call site the paren-safe view cannot show is B5.

## Findings

| # | Sev | Unit · address | Defect | Absorbs |
|---|---|---|---|---|
| B1 | blocker | `-8` §2 S3 · `-6` §4, §6 AC6 | S3's leak test has no closure test, so ordinary division on a line carrying a closed string, template or block comment reports a LEAK — and the fold routes that into all four rules | 2, 22 |
| B2 | blocker | `-8` §3 (3rd non-goal), §6 AC6 · `-7` §6 AC2 · `-6` §2 S4 | The reorder puts units 8 and 7 at steps 5 and 6, but both depend on the `--selftest` seam unit 6 S4 adds at step 7 — M2's ordering axis, in two documents | 3, 8, 14, 26 |
| B3 | blocker | `-8` §2 S1 and S2 · §6 AC4 · §5 | The member guard's subject is unstated and its `^` alternative is fail-OPEN: against a bare word it never fires, against a line prefix it re-opens the span on a member access split after the dot | 15, 28 |
| B4 | blocker | `-6` §4 (absent) · §6 AC1–AC4 | Unit 6 has no fixture-discipline paragraph, and AC1–AC4's trigger is the same `return`-position span unit 8 dissolves two steps earlier — all four class arms go green with unit 6 unimplemented | 10 |
| B5 | blocker | `-9` §2 S2b · §6 AC5 | S2b turns a call site the paren-safe view cannot show into an ambiguity DENY, but the block-comment arm's call-site line is exactly that — so AC5's demand that the denial "still names the width" is unreachable | 9 |
| H1 | high | `-11` §2 S1, S2 · §6 AC3 | The hoisted merge is defined entirely against `_bl` and handed to a caller that has no `_bl`; the view pair is never respelled, and AC3 asserts an agreement the two scanners measurably cannot deliver | 4, 24 |
| H2 | high | `-12` §4 (retirement ¶) · §6 AC4 | Only ONE of the two pinned LOSS ceilings retires. Ceiling 2 does not stop losing — it inverts into a raised `MapError`, an undeclared new failure mode of `enumerate_exports` | 5, 12, 19 |
| H3 | high | `-9` §2 S2b, §6 AC4/AC7 · `-10` §6 AC4 | S2b flips a shipped ADMIT arm at step 8, one step before the unit that claims the re-baseline; unit 10 AC4 then asserts a DENY already true | 11 |
| H4 | high | `-10` §6 AC6 | AC6's own fixture cannot bind `K` in either view, so the criterion written to make S2 non-optional still passes with S1 alone — round-1 finding 10 unclosed | 25 |
| H5 | high | `-6` §6 AC6 · §5 risks | The declared precision control has no later slash on its line, so S3's predicate cannot fire on it under any reading — a control on the wrong side of the boundary it is said to pin | 23 |

---

### B1 — blocker — S3's leak test fires on ordinary division

**Address.** `memory/builds/aPairedLexer/spec/2026-08-31-spec-TOOL-aPairedLexer-8.md` §2 S3 and §4
("Why S3 lives here"), against `…-6.md` §4 and §6 AC6.

**What.** S3 defines the leak as "a later `/` on the same line with an opener (a backtick, a quote,
`/*` or `*/`) strictly between the two". It never asks whether that opener CLOSES before the later
slash. A line holding two divisions with any quoted text between them satisfies it, as does a single
division sharing a line with a closed block comment or a closed string containing a slash. Unit 6 S2
routes the flag into both `renderCodeView.unterminated` and `blankLiterals.clean`, so one such line
moves all four rules onto the per-line fallback — the view whose prose-in-a-lens-prompt false
positives `TOOL-aPairedLexer-2` was built to remove.

**Evidence.** S3's predicate was implemented exactly as worded (existential over later slashes, the
literal reading of "is there a later `/`") and run over the set's own fixtures:

- `const rate = done / total; log('tick'); const inv = total / done;` → LEAK, mid
  `" total; log('tick'); const inv = total "`.
- `const half = args.n / 2; /* the half we fan over */` → LEAK, mid `" 2; /* the half we fan over *"`.
- `const half = args.n / 2; const p = 'docs/a.md'` → LEAK, mid `" 2; const p = 'docs"`.
- ``const pct = done / total; log(`a/b`)`` → LEAK.
- The true leaks still report: ``if (a) /x`y/.test(s)``, `if (a) /x[/*]y/.test(s)`,
  `if (a) /won't/.test(s)`.

Downstream cost measured at the tip: the legal four-line script `const LENSES = ['sec','corr']` / a
lens prompt naming ``parallel(items.map(f))`` / `const rate = done / total; log('tick'); const inv =
total / done;` / `boundedParallel(LENSES.map(...), 5)` exits `0` today. Its third line is a LEAK by
S3's wording, which under unit 6 S2 puts rule 1 on the per-line view, where `stripStrings` does not
touch backticks and the prose inside the lens prompt reads as a raw primitive. That is the ADMIT→DENY
flip `TOOL-aPairedLexer-2` removed, re-entering through the fix promoted to bound it. Unit 6 §4's
"Ordinary division does not match" is argued only from a ONE-slash line and is false of the class.

**Fix.** Narrow S3: a declined slash leaks only if an opener inside its would-be regex span is still
OPEN under a code-mode lex of the rest of the line, or leaves a quote unpaired. A balanced pair
inside the span cannot leak anything. Verified over the set's own fixtures that this narrowing keeps
every true leak above and drops all four false ones. While there, drop `*/` from the opener list: it
opens nothing in code mode and only widens the between-test.

**Left-shift gate.** A two-row table arm in `tools/hooks/agent-cap.test.sh` over the predicate
directly, one row per side of the boundary — a closed opener between two slashes must report NO leak,
an unclosed one must report LEAK — with the two-division and closed-block-comment lines above as
named rows. The gate is the CLASS, not the instance: it must fail if the closure test is ever dropped
again.

---

### B2 — blocker — units 8 and 7 depend on a seam that lands after them

**Address.** `…-8.md` §3 third non-goal and §6 AC6; `…-7.md` §6 AC2; `…-6.md` §2 S4. Status headers
and the README's generated build-order table.

**What.** M2 states the axis verbatim: *no sub-spec depends on a unit sequenced after it*. Unit 8 is
order 5, unit 7 order 6, unit 6 order 7. Unit 8 §3 explicitly declines the seam ("Not the test seam —
that is `TOOL-aPairedLexer-6` S4") while its own AC6 requires running "through the `--selftest` seam
`TOOL-aPairedLexer-6` S4 adds". Unit 7 AC2 names the same seam. Unit 6 S4 says outright that "every
'structural' criterion in this build's set depends on it", which is the ordering violation stated as
a feature.

**Evidence.** Build order confirmed in the README's `gen:build-order` table (5 `-8`, 6 `-7`, 7 `-6`)
and in all three status headers. Seam confirmed ABSENT at the tip: `tools/hooks/agent-cap.js` has
zero occurrences of `module.exports` and zero of `--selftest`; the only `process.argv` use is the
`--only=` branch at line 1096; `main()` runs unconditionally on line 1247, the file's last line. So
AC6 and unit 7 AC2 name no invocable command at the step their unit lands.

The cost is not cosmetic. AC6 is the criterion rev-2 wrote to close round-1 finding 9, replacing a
`grep -c` that a one-scanner patch satisfied with a by-RUN agreement assertion. Unit 7 AC2 is the
criterion rev-2 wrote to close round-1 finding 4, replacing one that named no runnable command. Both
folds are relocated behind a dependency, not closed. The dependency is also mutually circular in
prose: unit 6 §4 says "`-8` now lands first because S1 consumes its predicate", so reordering cannot
satisfy both.

**Fix.** Move the seam, not the order. Add the `--selftest` argv branch guarding `main()`, in BOTH
copies, to unit 8 as S6; delete unit 8 §3's third non-goal; reduce unit 6 S4 to a citation of `-8` S6
and drop its "every structural criterion depends on it" claim; retarget unit 7 AC2 to cite `-8`.
Unit 8 lands first and two of the three consumers are itself and unit 7, so this is the cheapest
edit. Bump `-8`, `-7` and `-6` with §9 lines naming the ordering axis.

**Left-shift gate.** Make the ordering axis machine-checkable rather than cross-read: a check that
parses each spec's `order` header and greps its §6 for `TOOL-aPairedLexer-<n>` references, failing
when a criterion cites a unit with a higher order. It reds today on `-8` AC6 and `-7` AC2, which is
the observed failing case a new gate owes before it lands.

---

### B3 — blocker — the member guard's `^` alternative is fail-open, and its subject is unstated

**Address.** `…-8.md` §2 S1 and S2, §5 ("one trailing-word buffer per scanner"), §6 AC4.

**What.** S2 pins a verbatim regex —
`(?:^|[^.\w$])(return|typeof|case|in|of|instanceof|new|delete|void|throw|yield|await)\s*$` — and
never states the string it is applied to. S1 defines the predicate's input as "the trailing WORD when
there is one, else the previous significant character", an exclusive either/or that never carries the
character BEFORE the word. Both candidate subjects fail, in the direction §5 names dangerous.

**Evidence.** The regex was run verbatim against both candidates.

Against a bare trailing word — S1's first clause and §5's "trailing-word buffer" — `in`, `of`,
`delete`, `new`, `case`, `return`, `instanceof` and `await` ALL report KEYWORD via the `^`
alternative. The guard can never fire, so `obj.in / 2` opens a regex span over live code: the exact
fail-open S2 was added to close.

Against the line-so-far prefix, the same regex correctly rejects `obj.in`, `x.of`, `m.delete`,
`p.new`, `r.case` and accepts `  return` — but `^` then matches a keyword at the START of a line, and
a member access split after the dot is legal JavaScript (confirmed with `new Function` that
`const obj={in:4};const y = obj.` NEWLINE `in / 2; const z = 9 / 3` parses). `prev` is declared
outside the per-line loop in both scanners, so the file's own state genuinely crosses line
boundaries; the regex does not. Measured with S2's regex wired into both scanners, that script goes
from exit `2` at the tip to exit `0`, the rendered view being
`["const y = obj.","in                                            3",""]` — the raw `parallel(`
blanked by a span from the slash after `in` to the slash in `9 / 3`. The spaced-dot form `obj . in`
also reports KEYWORD.

AC4's negative table is five SINGLE-LINE member accesses, so no criterion in the set fails on either
manifestation. §4's "S2 stops the fix opening a new one" and §8's "S2 closes the latter" are
unqualified as written.

**Fix.** Drop the `^` alternative. Decide the member case from the scanner's carried previous
significant character, which is already `.` at that point because `prev` persists across lines: a
keyword whose preceding significant token is `.` is a property name whatever line the dot sits on.
State in S1 that the guard's subject is the emitted code-view buffer up to the slash, not a bare
word, and change §5 to "one line-so-far buffer per scanner". Add `const y = obj.` NEWLINE
`in / 2; parallel(items.map(f)); const z = 9 / 3` as a sixth row of AC4's negative table, and either
extend the guard past optional whitespace or declare `obj . in` as a named ceiling.

**Left-shift gate.** Extend AC4's negative table into a multi-line arm: every row is a two-line
member access split after the dot, asserted DIVISION, run through both scanners. A single-line-only
table is the instance arm this defect walked straight through.

---

### B4 — blocker — unit 6's class arms are satisfied by unit 8's code

**Address.** `…-6.md` §4 (no fixture-discipline paragraph) and §6 AC1 through AC4. Compare §4 of
units 9, 10 and 11, which each carry one.

**What.** AC1–AC4 are the one-arm-per-RULE class arms §5 names as unit 6's gate. None of them says
the trigger must be an AMBIGUOUS-position declined slash, and the phantom span they describe is the
same `return /` + backtick + `/` shape unit 8 AC1 names. Unit 8 lands at step 5 and makes `return` a
regex position, dissolving that span two steps before unit 6 lands.

**Evidence.** Measured at the tip: the script ``function a(s) { return /`/.test(s) }`` /
`const results = parallel(thunks)` / ``function b(s) { return /`/.test(s) }`` exits `0`, and its
trigger-deleted control exits `2` — precisely AC1's stated verdicts. The ambiguous-position variant
``if (s) /`/.test(s)`` ALSO exits `0` at the tip, so AC1's stated verdicts do not discriminate
between the two triggers and nothing in AC1–AC4 pins one. Once unit 8 lands, the `return`-position
fixture exits `2` with unit 6 unimplemented, and AC2–AC4 say "the same span" and inherit it. Unit 6
is the unit whose entire content is the declined-slash signal, so all four of its rule-class arms
would observe nothing. This is the build README's own rule ("a fix that removes its own fixture's
TRIGGER is unverified") and the reason units 9 and 10 carry fixture-discipline paragraphs after round
1 confirmed the same class against unit 10. Unit 6, now sequenced after both lexer repairs, got none.
Only AC5 spells an ambiguous trigger.

**Fix.** Add a "Fixture discipline" paragraph to §4 in the wording units 9 and 10 use, and spell
AC1's trigger literally as an ambiguous-position declined slash carrying a backtick — after `)`, an
identifier or a number, never a keyword position — stating its measured verdicts at the tip AND under
`-8`+`-7` alone, as unit 11 AC1 now does. Bump to rev-3.

**Left-shift gate.** Each of AC1–AC4 becomes a paired arm: the fixture, plus the same fixture with
the sibling lexer units' repairs simulated, asserted to still require unit 6's signal. That is the
only shape that fails when a sibling deletes the trigger.

---

### B5 — blocker — unit 9's denial cannot name the width AC5 demands

**Address.** `…-9.md` §2 S1 and S2b, against §6 AC5.

**What.** S1 sources `topLevelArgs` from `_bl.code`, and S2b converts a call site the paren-safe view
cannot show at all into an ambiguity DENY. For the block-comment arm, `_bl.code` for the call-site
line is empty — AC5 quotes it itself — so the cap ARGUMENT is unreadable and the denial can only name
the ambiguity. AC5 demands the message "still names the width" 500 and glosses itself as what
separates a real denial from "one that lost the number".

**Evidence.** `blankLiterals` extracted from the tip and run on that arm's fixture returns
`["const c = ","","",""]`, so `joinCall` has no line to walk and S2b fires. The shipped hook today
prints `the cap argument at the boundedParallel() CALL SITE is 500`, which `capFindings` derives via
`joinCall`/`topLevelArgs` over the FALLBACK view (`code = _bl.clean ? _bl.code : lines.map(...)`,
`agent-cap.js:732`). Under S1+S2b that path is gone. A builder reconciling the two either weakens S1
back to reading arguments from the fallback view — re-opening the paren-unbalanced join this unit
exists to fix — or drops AC5's message assertion, which is the failure AC5 was written to catch. The
two sibling arms have the same unasserted conflict.

**Fix.** Add S2c: when `_bl.code` cannot show the call site, the cap ARGUMENT is read from the
fallback view and the denial names it, while the AMBIGUITY is still recorded. S2b then covers only
the case where neither view resolves an argument, and AC5 becomes satisfiable as written. Bump to
rev-3 and name the S2b/AC5 conflict in §9.

**Left-shift gate.** Assert the denial MESSAGE, not the exit code, on all three arms where the
paren-safe view blanks the call-site line. An exit-code-only assertion cannot distinguish a denial
that kept the number from one that lost it, which is the whole content of this criterion.

---

### H1 — high — unit 11 hands a `_bl`-shaped merge to a caller that has no `_bl`

**Address.** `…-11.md` §2 S1 and S2, §6 AC3.

**What.** Unit 10 writes the merge literally against `_bl` — S1 "when `!_bl.clean`", S2 "sweep over
`_bl.code`". Unit 11 hoists that same code and gives it a second caller, `fanoutFindings`, whose gate
is `renderCodeView.unterminated` and whose trusted view is `renderCodeView.code`. No sentence
respells the pair for rule 2 — M2's interface axis, one name reused for a different machine. AC3 then
asserts the two rules resolve the SAME const table, which is TRUE under a cross-machine reading and
FALSE under a per-rule one, so the criterion actively selects the wrong answer.

**Evidence.** The two signals are measurably not interchangeable. Over this repo's ten tracked `.js`
files, `tools/workflows/drift-audit-state.js` — a shipped harness — gives
`renderCodeView.unterminated = false` while `blankLiterals.clean = false`. Two further counterexamples
on `node --check` clean scripts: `renderCodeView` emits `${…}` interpolation bodies as CODE while
`blankLiterals` drops them, so a const declared inside an interpolation binds in one table and not
the other with no fallback and no merge involved — rule 2 `[["K",5]]` against rule 3 `[["K",500]]`,
both views clean. On a script where `renderCodeView` is unterminated but `blankLiterals` is clean, a
verbatim hoist skips rule 2's merge entirely and D6's fabricated cap survives all seven units. This
is the defect `agent-cap.js` records in its own words at `blankLiterals`' return: *a signal read from
a different view than the one being fixed reports on the wrong machine*. Unit 11 §3 explicitly
refuses to unify the scanners, so nothing in this unit can make AC3's "so the two cannot diverge
again" true.

**Fix.** State in S1 that the hoisted helper takes `(fallbackCode, trustedCode, isClean)` as
arguments and that each caller supplies its OWN scanner's triple — `renderCodeView` for
`fanoutFindings`, `blankLiterals` for `capFindings`. Rewrite AC3 to assert what is actually
invariant: for a script both views call clean the two tables are equal, and for a script neither
calls clean the two tables are equal. Add a criterion asserting rule 2 runs the merge whenever rule 2
itself falls back, on a fixture where the two scanners' signals differ, and declare the
interpolation-body divergence as a named ceiling or fold it into `TOOL-aPairedLexer-5`.

**Left-shift gate.** An arm that runs both scanners over every tracked `.js` in the repo and asserts
the `unterminated`/`clean` pair agrees, listing the disagreements as declared ceilings. It reds today
on `tools/workflows/drift-audit-state.js`, which is the observed failing case.

---

### H2 — high — only one of unit 12's two pinned ceilings retires

**Address.** `…-12.md` §4 (the retirement paragraph, "the two pinned ceilings RETIRE, and that is a
measured outcome rather than a waiver") and §6 AC4.

**What.** AC4 says both pinned LOSS ceilings invert to "no longer lose anything". Ceiling 1 does.
Ceiling 2 does not stop losing — it converts the loss into a raised `MapError`, because the
regex-borne `//` was the thing MASKING the multi-declarator guard. AC4 names no expected value for
the inverted row, and unit 12 declares the new failure mode nowhere.

**Evidence.** Reproduced by monkeypatching a conservative regex-aware `render_comment_free` into
`map_lib` and running `enumerate_exports`. Ceiling 1 (`export const RX = /a\/*b/;` with a later real
`*/`) goes `{RX, AFTER}` → `{RX, AFTER, LOST}`: retires cleanly, exactly as §4 says. Ceiling 2
(`export const U = /^https?:\/\//, ALSO = 1;`) does NOT return `{U, ALSO}` — it raises
`web-ts: m.ts: unmodelled multi-declarator export`, and `ALSO` is still not indexed. Cause verified
directly against the real code: `map_lib._has_top_level_comma` returns `True` on both the raw and the
post-model spelling of that line, and the raise site is `tools/codebase-map/map_lib.py:645`. The
selftest arm's own comment says the same thing from the other side — the regex-borne `//` "MASKS the
multi-declarator guard… the guard it disables is the one that exists to refuse exactly this silence".
Remove the mask and the guard fires.

So AC4's stated observable is unreachable for that row, and the only edit that reaches it literally
is weakening `_has_top_level_comma`, which re-opens the green-by-absence hole that guard exists to
close. §3's non-goal withholds a DIFFERENT mask (`_has_top_level_comma`'s unterminated-quote
handling, D8), not this one. §5's risks name only the over-recognition direction, so the new refusal
class is unpriced: `enumerate_exports` starts RAISING on a form it previously swallowed, which for an
adopter reds `gen_map.py --write` on a legal file. AC6's identical-symbol-set corpus arm cannot see
it, because an exception is not a symbol set — confirmed separately that over this repo's own tracked
`.js`/`.ts` the definition set is byte-identical with and without the model, so AC6 is green either
way and the gate impact here is adopter-hypothetical. The AC-is-wrong half stands on its own, and a
half-right criterion is worse than a wrong one: a builder gets one true row and one false one.

**Fix.** Split AC4 into two rows with their measured values. Ceiling 1: the block opener no longer
loses, `{RX, LOST, AFTER}`. Ceiling 2: the line-comment opener no longer MASKS the multi-declarator
guard, so `enumerate_exports` RAISES `MapError` naming the multi-declarator form — assert the raise.
Correct §4 to say that one ceiling retires into a recovery and the other into a refusal. Add the
refusal to §5's risks and to §2 as an intended fail-closed behaviour change, with a migration line: a
`.ts` file whose export line carries a regex-borne `//` before a second declarator changes from
silent-drop to `MapError`.

**Left-shift gate.** Extend AC6's corpus arm to assert that no tracked file NEWLY raises, not only
that the symbol set is identical. A symbol-set comparison cannot observe an exception, which is
exactly why this inversion was invisible to the criterion written to catch it.

---

### H3 — high — unit 9 flips a shipped arm one step before the unit that re-baselines it

**Address.** `…-9.md` §2 S2b, §6 AC4 and AC7; `…-10.md` §6 AC4.

**What.** S2b flips the shipped arm `rule3: an exposed const resolves the cap and the script admits`
from ADMIT to DENY at step 8. Unit 9 never declares that re-baseline — the only unit claiming it is
unit 10 S3, at step 9. AC4's claim that "this unit does not change it alone" is false, and AC7's
escape ("except any this unit's sibling re-baselines by name") points forward at a unit that has not
landed, which is not an escape.

**Evidence.** `blankLiterals` run on that arm's fixture returns ``["const t = `","","","",""]`` — the
call-site line is blank in `_bl.code` exactly as the block-comment arm's is, so S2b's "a call site the
paren-safe view cannot show AT ALL is a DENY" fires. Unit 9's own direct gate,
`bash tools/hooks/agent-cap.test.sh`, is therefore red at its landing. Downstream, unit 10 AC4 — the
criterion for its S3 re-baseline — then asserts a DENY that is already true, so unit 10's S1 merge
can ship half-implemented against it. That is the "green DENY proving nothing" class round 1
confirmed as finding 37, one unit over.

**Fix.** Name the arm in unit 9 §2 as an S2b consequence and in AC7's exception list. Strengthen unit
10 AC4 to assert the MESSAGE — that the denial names `K` as unresolvable because a binding visible
only to the distrusted view does not resolve a cap — rather than the exit code, so it fails against
unit 9's ambiguity denial. Bump both to rev-3.

**Left-shift gate.** Every re-baselined arm carries its new expected MESSAGE, not just its new exit
code, and the unit that causes the flip is the unit that declares it. A re-baseline declared in a
later unit is a red gate in the earlier one.

---

### H4 — high — unit 10's AC6 still passes with S1 alone

**Address.** `…-10.md` §6 AC6, the criterion rev-2 added to fold round-1 finding 10.

**What.** AC6 states it "FAILS with S1 alone — without it S2 could be omitted entirely and nothing
would red". Its own fixture makes that unreachable: AC6 requires a name "bound by BOTH views", and
the fixture's real declaration is `const K = args.width`, which is not an integer binding.

**Evidence.** Against `intConsts` (`tools/hooks/agent-cap.js:155`) the binder requires
`=\s*(\d+)\s*$`, so `const K = args.width` binds NOTHING in either view. Running AC6's fixture
through the file's own `blankLiterals`/`stripStrings`/`intConsts`: the fallback view binds `{K:5}`
from the prose, `_bl.code` binds `{}`. K is therefore a one-bound name, S1 deletes it, `boundedK`
already denies naming K unresolvable, and applying S2's sweep changes the table by nothing. AC6's
premise is self-contradictory against the mechanism, and round-1 finding 10 is not closed.

**Fix.** Replace AC6's fixture with one where both views DO bind K to an integer and the clean view
additionally SEES a declaration it refuses: a `const K = 5` visible to both, plus a later
`const K = args.width` outside any mis-lexed span. Under S1 alone that admits, because the max keeps
5; only S2's sweep deletes K and denies. Assert both verdicts.

**Left-shift gate.** The project's own rule, applied to a criterion rather than a gate: a criterion
claiming to fail without a scope item must be RUN with that scope item stubbed out and observed RED
before the unit lands. A criterion only ever seen pass is an assertion about nothing.

---

### H5 — high — unit 6's precision control cannot fire

**Address.** `…-6.md` §6 AC6, and the §5 risks line that leans on it ("AC6 is the control that pins
the bound").

**What.** AC6's fixture is ``log(`progress ${done / total}`)``. There is no later `/` anywhere on
that line, so S3's predicate cannot fire on it under any reading of "an opener strictly between the
two". The criterion is a control that cannot fail, and §5's claim that it pins the precision bound is
unsupported — it pins rev-1's discarded backtick-anywhere condition, not rev-2's extent-scoped one.

**Evidence.** Zero leak hits on the AC6 line under the S3 predicate as spelled (measured alongside
B1's fixtures). Independently, with S3 plus unit 6's routing applied to a copy of `agent-cap.js`,
`bash tools/hooks/agent-cap.test.sh` reports 123 passed, 0 failed, while B1's fixture flips 0 to 2 —
so neither the shipped suite nor the seven-unit AC set observes the ADMIT→DENY class B1 measures.
This is separate from B1 and survives B1's fix: narrowing the predicate does not make this criterion
able to fail.

**Fix.** Make AC6 a two-row table over the boundary. Keep the current line as the no-later-slash row,
and add the two measured shapes that DO carry a later slash and must still ADMIT —
`const half = n / 2; /* why */` and ``const pct = done / total; log(`a/b`)`` — each with a lens
prompt naming a primitive, asserted at exit `0`.

**Left-shift gate.** Every "precision control" in this set states, in the criterion itself, what it
would look like RED. A control whose red state cannot be written down is not a control.

---

## Checked and NOT confirmed

Recorded because a promoted build should not re-audit these.

- **Ordering hazard among units 9, 10 and 11 created by the 8-7-6 reorder.** Not confirmed. Units 9
  and 10 each carry an explicit fixture-discipline paragraph requiring an ambiguous-position trigger
  for the stated reason, and unit 11 AC1 names its own trigger literally with per-version verdicts.
  One residual observation, below the bar for a finding: unit 11 AC1's measured verdict list stops at
  "under simulated `-6`+`-7`+`-8`" and does not state the verdict under `-9`+`-10`, which land at
  steps 8 and 9, between that simulation and unit 11 at step 10. The mechanism suggests it is
  unchanged, and no measurement contradicts AC1, so it is noted rather than raised.
- **M2 scope axis across the seven.** Clean. Nothing a sub-spec puts IN is OUT in a sibling; unit 8's
  declining of the seam and unit 6's owning of it agree on ownership and disagree only on ORDER,
  which is B2.
- **M2 acceptance axis.** No disagreement found beyond the criteria already named in B4, B5, H2, H4
  and H5.
- **Unit 6 S2's "all four rules fall back" claim.** TRUE, verified against the shipped file's rule →
  signal mapping. See "What the fold DID close".
- **Unit 12 AC6's corpus arm as a gate risk.** The claim that modelling regexes would red
  `gen_map.py --write` in THIS repo does not reproduce: the tracked `.js`/`.ts` symbol set is
  identical with and without the model. The exposure is adopter-side, and only the AC-is-wrong half
  of H2 is carried above.

## Method

Predicates were implemented exactly as their spec words them and run over the spec set's own
fixtures, rather than argued about. Exit codes were measured by piping a real `Workflow` payload into
`node tools/hooks/agent-cap.js` at the pinned tip. Python claims were measured by importing
`tools/codebase-map/map_lib.py` and calling the real functions. The 10 refuted findings were
dominated, as in round 1, by prose-only arguments that did not survive a run — no refuted finding is
carried here, and no confirmed finding is carried without a run or a grep behind it.

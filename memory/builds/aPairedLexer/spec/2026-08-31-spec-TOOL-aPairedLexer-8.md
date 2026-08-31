# TOOL-aPairedLexer-8 — ONE regex-position predicate, keyword-aware and member-guarded

**Status:** SPECCED · rev-6 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md) | diff-review | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`!/[A-Za-z0-9_$]/.test(prev)` cannot distinguish `return` from an identifier. Every keyword that
cannot end an expression — `return typeof case in of instanceof new delete void throw yield await` —
therefore puts the following `/` in a DIVISION position. `return /re/.test(s)` is the commonest regex
position in real JavaScript. Round-2 review **D2**, a measured DENY→ADMIT against the shipped 1.9.

**rev-2 makes this unit the FOUNDATION rather than one of three lexer fixes.** The spec audit
measured that a per-scanner repair leaves the two views answering one question differently, and that
disagreement produced three of this file's four fail-opens. So the predicate this unit creates is the
single place the regex/division question is answered, and `TOOL-aPairedLexer-6` and `-7` consume it
instead of each carrying a copy. This unit therefore lands FIRST.

## 2. Scope (IN)

- **S1** — ONE predicate answering, for a given position, whether a `/` starts a regex. It decides on
  the previous TOKEN: the trailing WORD when there is one, else the previous significant character.
- **S2** — the keyword set is closed and is `return typeof case in instanceof new delete void
  throw`. **`of`, `await` and `yield` are CONTEXTUAL keywords and legal identifiers, so they are
  excluded**: the round-4 audit patched a copy with S1+S2 as rev-4 worded them and measured a
  DENY-to-ADMIT on all three — `const of = 5; x = of / 2` reads the `of` as a keyword, opens a
  regex over live code, and blanks the primitive. Dropping them keeps `return /re/`, which is D2's
  actual defect. A keyword preceded by `.` is NOT a keyword.
  **The SUBJECT of the guard is the running CODE TEXT emitted so far, not the current line and not
  a bare trailing word.** Against a bare word every keyword matches and the guard never fires;
  against a line prefix, `obj.` on one line and `in / 2` on the next is legal JavaScript the guard
  would miss. The `^` alternative therefore means START OF INPUT, never start of line. The test is:
  the code text ends with one of the keywords, and the character before that keyword is absent (start of input) or is not `.`, a word character or a dollar sign.
- **S3** — the predicate reports, for every slash it DECLINES, that the LINE IS AMBIGUOUS when that
  line also carries a later slash **IN CODE MODE**. No opener test and no closure test: see §8,
  where the fork is resolved and both are refuted by measurement.
  **The span is scanned as a REGEX BODY, and ambiguity requires an opener inside it.** Scanning it
  as CODE was the first implementation and it FAILED its own sibling criteria: a backtick in the
  body reads as a string opener that swallows the closing slash, so unit 6's four rule arms all
  reported clean. Measured. So the scan respects escapes and character classes the way a regex body
  is read, finds the closer, and reports ambiguity only when the span carried a backtick, a quote or
  a `/*`.

  **This is NOT round 2's refuted opener test**, and the difference is the whole reason the cost is
  bearable. That test scanned the REST OF THE LINE as code; this scans the SPAN as a regex body.
  The hook's own mandated `Math.ceil(x.length / MAX_VERIFIERS)) // gov:fixed-verifiers` idiom has a
  later slash but no opener between, so it ADMITS — where the rest-of-line reading denies it and 3
  of this repo's 4 tracked workflow harnesses with it. A span with no closer at all was never a
  regex and reports nothing.
- **S3-RETIRED** — the leak test three revisions tried to write.
  Retired unbuilt. rev-2 tested for an opener between two slashes and produced false LEAKS on
  ordinary division; rev-3 added a closure test and produced false NO-LEAKS on a balanced opener
  pair that still blanks live code. Both measured. The audit then showed the two shapes are
  IDENTICAL, so one input class was required to answer two ways. The span cannot classify itself,
  and §8 records the resolution.
- **S4** — both `renderCodeView` and `blankLiterals` call it. Neither keeps a keyword list, a member
  guard, or a leak test of its own.
- **S4b** — **a CLOSING QUOTE ends an expression.** `renderCodeView` treats `"`, `'` and a closing
  backtick as regex positions today, so `const x = "a" / 2; await parallel(D.map((d) => agent(d)));
  const y = "b" / 3` consumes the primitive inside a phantom regex literal and ADMITS — measured at
  the tip AND under an S1+S2 patch, with the bare primitive exiting `2`. No slash is DECLINED on
  that line, so S3 cannot reach it; the fix belongs in the position predicate itself.
- **S5** — a TABLE-DRIVEN arm over the keyword class in BOTH directions, positive and negative.
- **S6** — **the test SEAM**, moved here from `TOOL-aPairedLexer-6` because this unit lands FIRST
  and both this unit and `-7` state criteria that call the scanners directly. A `--selftest` argv
  branch guarding `main()`, in BOTH copies or the mirror-drift arm reds.

## 3. Non-goals (OUT)

- Not full JavaScript lexing. After an identifier, a number or a closing bracket, `/` stays DIVISION.
  That residual is real, and `TOOL-aPairedLexer-6` is what makes it announce itself — using S3.
- Not merging the two scanners wholesale (`TOOL-aPairedLexer-5`). S1 extracts the ONE predicate D2
  and the audit force; the rest of the duplication stays tracked.
- Not the routing of the leak report into the four rules — that is `TOOL-aPairedLexer-6`. This unit
  ANSWERS the question; that one acts on the answer.

## 4. Design

**The member-access guard is not a detail; without it this unit ships a fresh fail-open.** The audit
measured it: with the predicate written as a bare word match,
`const y = obj.in / 2; parallel(items.map(f)); const z = 9 / 3` goes from exit `2` to exit `0`, the
raw `parallel(` blanked out by a span running from the slash after `obj.in` to the slash in `9 / 3`.
The keyword-free control `q.z / 2` stays at `2`.

**And the error direction is fail-OPEN, not fail-closed.** rev-1's §5 said the opposite. The file
states the rule verbatim at `offendingLines`: *"Seeing LESS is safe for a rule whose findings are
permissions and dangerous for a rule whose findings are denials, and this is the second kind."*
Over-recognising a regex BLANKS code, and blanked code cannot be denied. That is why S5's table needs
a negative column, and why AC5 alone was not enough — it pins only the closing-bracket case, which
never reaches a member-access keyword.

**Why S3 lives here.** `TOOL-aPairedLexer-6` needs to know when a declined slash leaked. If each
scanner computed that itself, the two would answer differently for one line — exactly the failure the
audit measured against rev-1, where unit 6 widened one scanner's signal while rules 3 and 5 gated on
the other's. One predicate, one answer, both callers.

## 5. Production-readiness checklist

- security — closes a wide, ordinary-looking admit path, and S2 stops the fix opening a new one.
- perf / scale — one trailing-word buffer per scanner; no change in cost class.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — denial text unchanged.
- risks — **over-recognition is FAIL-OPEN for rules 1 and 2**, which is why S2 exists and why S5's
  table is two-directional. Under-recognition costs precision only and is `-6`'s subject.
- testing + left-shift gates — S5 gates the CLASS both ways; AC6 gates the AGREEMENT of the two
  scanners by RUN, not by `grep`, because every fail-open in this file so far was a behaviour copy
  rather than a string copy.
- migration / rollback — revert restores the character test.
- user docs — the dossier's ceiling paragraph is narrowed to what actually remains.

## 6. Acceptance criteria

- **AC1** — When the `return /` backtick `/.test(s)` fixture with a raw `parallel(D.map(...))`
  between two such functions is fed to `node tools/hooks/agent-cap.js`, it exits `2`. At 1.9 it exits
  `2`, at the tip `0`.
- **AC2** — When the markdown-fence fixture is fed to the hook, it exits `2`; `0` at the tip.
- **AC3** — When `bash tools/hooks/agent-cap.test.sh` runs the POSITIVE table, each of
  `return /re/`, `typeof /re/`, `case /re/:`, `throw /re/` and `yield /re/` has its literal blanked.
- **AC4** — When the same arm runs the NEGATIVE table, each of `obj.in / 2`, `x.of / 2`,
  `m.delete / 2`, `p.new / 2` and `r.case / 2` is DIVISION and nothing is blanked. Specifically
  `const y = obj.in / 2; parallel(items.map(f)); const z = 9 / 3` exits `2` — which it does at the
  tip and would NOT under a bare word match, measured by the audit.
- **AC5** — When `rule1: after a closing bracket a slash is division, not a regex` runs, it stays
  green.
- **AC6** — When a script containing `return /re/` is rendered by both scanners through this unit's
  own `--selftest` seam (S6), `renderCodeView` and `blankLiterals` BOTH blank the literal. Asserted
  by RUN over a corpus of regex-position fixtures, never by counting copies of a string.
- **AC7** — When a declined slash shares its line with a later slash IN CODE MODE, the predicate
  reports AMBIGUITY; when the only later slash is inside a comment or a string, it does NOT. The
  binding fixture is the hook's own `Math.ceil(x.length / MAX_VERIFIERS)) // gov:fixed-verifiers`
  idiom, which must report NO ambiguity — under the raw reading it reports ambiguity and 3 of this
  repo's 4 workflow harnesses deny. This is S3's only acceptance criterion, and rev-4 left S3 —
  the whole basis of the §8 resolution — shipping at order 5 with none, because AC7 was byte-
  unchanged and still mandated the retired test.
- **AC10** — When `const x = "a" / 2; await parallel(D.map((d) => agent(d))); const y = "b" / 3` is
  fed to the hook, it exits `2`. S4b's criterion. Measured `0` at the tip and under an S1+S2 patch.
- **AC9** — When `node tools/hooks/agent-cap.js --selftest` is invoked, the seam exists and returns
  the scanners' output for a given script, in BOTH copies. S6's own criterion, and the one every
  structural criterion in this build depends on.
- **AC8** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is
  green after it.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`,
`bash tools/check-kit-versions.sh`.

## 8. Open questions

- **F1 — how should a DECLINED slash be classified?** Three revisions of one test, each refuted by
  measurement. rev-2 tested for an opener between two slashes: false LEAKS on ordinary division.
  rev-3 added a closure test: false NO-LEAKS on a balanced opener pair that still blanks live code.
  The round-3 audit then showed the two shapes are IDENTICAL, so no test over the span can separate
  them — one input class was being required to answer two ways.

  Options seen. (a) Treat the span as DIVISION, the status quo: live code may open phantom constructs,
  which is the fail-open this build was promoted to close. (b) Treat it as a REGEX and blank it:
  blanks possibly-live code, which §5 of this spec establishes is ALSO fail-open for rules 1 and 2 —
  the file's own words, "seeing LESS is safe for a rule whose findings are permissions and dangerous
  for a rule whose findings are denials, and this is the second kind". (c) Report AMBIGUITY whenever a
  declined slash shares a line with a later slash, and let the four rules fall back to the per-line
  view.

  RESOLVED (agent, 2026-08-31, delegated): **(c)**, under the TOKEN reading S3 makes binding — the
  raw reading was measured to route 3 of 4 harnesses and is refused. It is the only option that is
  not fail-open, and
  M3 ratifies the most feature-rich survivor after the vetoes — (a) and (b) both fail the acceptance
  criteria already written into `TOOL-aPairedLexer-6`, which is veto 1. No new dependency, surface or
  governance change, so vetoes 2 and 3 do not fire.

  **The cost is real and is named rather than discovered.** A legal script with two ordinary slashes
  on one line now routes to the per-line view, whose false positives are the class
  `TOOL-aPairedLexer-2` removed. `TOOL-aPairedLexer-6` AC6 is re-baselined from admit to deny to
  record it, and the workaround is one character: end the statement before the ambiguous regex, or
  bind it to a name. That is the trade this file has been avoiding for three revisions by looking for
  a test that does not exist.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D2.
- rev-2 · 2026-08-31 · folded spec-audit findings 27 and 9, and REORDERED to land first. 27: the
  predicate as §4 worded it made a keyword used as a PROPERTY NAME open a regex span over live code,
  measured ADMIT — a fail-open introduced by the unit meant to narrow the lexer; S2 adds the member
  guard and §5's error-direction sentence is corrected from fail-closed to fail-OPEN. 9: AC4's
  `grep -c` was satisfied by a one-scanner patch, so S4 and AC6 now assert the two scanners AGREE by
  running them. S3 is new and absorbs the decline signal from `TOOL-aPairedLexer-6`, per audit
  finding 26's recommendation that it live where both views must read one answer.
- rev-3 · 2026-08-31 · folded round-2 audit B1, B3 and B2. B1: S3 had no CLOSURE test, so ordinary
  division with a closed string, template or block comment between two slashes reported a LEAK —
  measured on three fixtures — which `-6` S2 then routed into all four rules. B3: the member
  guard's SUBJECT was unstated and its `^` alternative was fail-open both ways. B2: the seam moves
  here from `-6`, because this unit lands at order 5 and `-7` at order 6 both state criteria that
  need it, while `-6` added it at order 7 — a dependency pointing backwards.
- rev-4 · 2026-08-31 · folded round-3 B1 and B2 by RESOLVING the fork they expose rather than
  amending the test a fourth time. B1: the span ended at "the next slash on the same line" and
  `/*` is a slash first, so the `/*` row could never report. B2: the closure test answered NO LEAK
  on a balanced opener pair that still blanks live code, and that shape is identical to the
  precision control — one input class required to answer two ways. Three revisions of one test,
  each refuted by measurement, is the same shape this build already named: stop mitigating and
  decide. §8 carries the decision.
- rev-5 · 2026-08-31 · folded round-4 B1, B3, B4 and H3 after M4 ruled the loop NON-CONVERGENT.
  B3: S3 never said whether "a later slash" was a raw character or a code-mode token, and the two
  readings differ by the ENTIRE population — the token reading is now binding, measured. B4: `of`,
  `await` and `yield` are contextual keywords and legal identifiers, measured DENY-to-ADMIT, and
  are dropped from the set. B1: AC7 was byte-unchanged and still mandated the retired test, leaving
  S3 with no criterion at all. H3: a closing quote is treated as a regex position, which ADMITS a
  raw primitive with no declined slash anywhere — S4b and AC10 close it.
- rev-6 · 2026-08-31 · BUILT, and the spec moved first because the build diverged. rev-5 said 'a
  later slash IN CODE MODE' with no opener test; implemented literally that fails unit 6's four rule
  arms, because a backtick in the regex body reads as a string opener and swallows the closer. The
  rule that works scans the SPAN as a regex body and requires an opener inside it — which is not
  round 2's refuted test, since that one scanned the rest of the LINE as code. Measured both ways:
  the working rule admits the `// gov:fixed-verifiers` idiom and denies every phantom-span fixture.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **No existing seam fits, and the probe
says why**: `renderCodeView` and `blankLiterals` are both `fan-in 0`, so there is no shared scanner to
wire through — the shape of a duplicated grammar rather than a reused one. This unit creates the
first shared predicate between them and is therefore the beginning of `TOOL-aPairedLexer-5`'s answer
rather than another copy.

`TOOL-aLexedStripper-5` is the record that DELETED `renderCodeView`'s block-comment branch, because a
`/*` inside a regex literal was indistinguishable from a real one. It is cited here because S3's leak
set includes `/*` and `*/` for exactly that reason; the audit noted no spec in the set cited it.

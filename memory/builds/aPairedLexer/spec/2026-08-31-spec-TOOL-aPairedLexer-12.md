# TOOL-aPairedLexer-12 — model regex literals, so the phantom span never exists

**Status:** SPECCED · rev-3 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md) | diff-review | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |

<!-- /gen:spec-records -->

## 1. Goal

`render_comment_free` models strings and templates but no REGEX LITERAL. A regex holding a backtick
opens a PHANTOM template span, and the template arm emits its contents verbatim on close — so real
comments inside it are never blanked and a commented-out `export` is scanned as LIVE code, ADDING a
symbol that does not exist to the committed `symbols.json` a coverage ratchet then demands be
claimed.

Round-2 review **D7**, reproduced end to end: a `.ts` file yields `['GHOST', 'RX', 'T']` at the tip
and `['RX', 'T']` at base `14e21399`.

**rev-2 changes the FIX, not the defect.** rev-1 proposed blanking comments inside the span and
argued it was safe because "a definition cannot live inside a template literal". The spec audit
measured that argument as unsound: it is about a REAL template, while the whole premise is that the
span is PHANTOM and therefore holds LIVE CODE. Implemented as written it LOST a real `export`.

## 2. Scope (IN)

- **S1** — `render_comment_free` models regex literals, so a regex-borne backtick, quote or comment
  opener cannot open anything. Same conservative rule as the JavaScript side: a `/` starts a regex
  only after a token that cannot END an expression; after an identifier, a number or a closing
  bracket it is DIVISION.
- **S2** — the existing ceiling arm becomes a TABLE with one row per direction: the ghost ADDED, a
  definition lost to a regex-borne line comment, a definition lost to a regex-borne block comment.
- **S3** — a CORPUS arm: `enumerate_exports` plus `scan_js_definitions` over this repo's tracked
  `.js` produce a symbol set identical to the pre-change run. That makes the eight-definition
  regression this function's own docstring records RUNNABLE rather than remembered.
- **S4** — correct the docstring's safety claim, which is about DELETION and does not cover
  un-blanking.

## 3. Non-goals (OUT)

- Not the JavaScript predicate. The two languages share a rule and not an implementation; unifying
  them across languages is not on the table and no seam exists.
- Not `_has_top_level_comma`'s unterminated-quote masking (round-2 D8, a MEDIUM, outside scope).

## 4. Design

**Model the thing rather than compensating for it — this build's own rule, applied to itself.** The
build README carries it because three revisions of the JavaScript view each mitigated a missing regex
model and each was defeated. rev-1 proposed the same shape one language over: a compensating pass
inside a span whose existence is itself the bug. Removing the phantom span removes the ghost, and it
also removes both LOSS directions the current ceiling arm pins — a regex-borne `/*` and a regex-borne
`//` stop being comment openers at all.

**So the two pinned ceilings RETIRE, and that is a measured outcome rather than a waiver** — the same
shape `TOOL-aPairedLexer-4` met when modelling regexes retired the block-comment ceiling. The arms
are kept and inverted, with the reason recorded, so the suite still records that the rows changed.

**The residual is the regex/division ambiguity**, identical to the JavaScript side and stated as a
ceiling: a regex in an ambiguous position is still mis-modelled. The Python side has no `dirty`
signal and no fallback view, so the residual here is a straight limit rather than a routed one. S2's
table gains no row for it, because the direction is not measurable from the extractor's output alone
— it is declared in the docstring and that is what S4 covers.

## 5. Production-readiness checklist

- security — N/A; this is inventory integrity, not a guard.
- perf / scale — one extra branch in a walk the function already performs.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged; line count is still preserved.
- observability — the selftest arms are the signal.
- risks — over-recognising a regex would blank live code and LOSE a definition, which is the
  direction the audit caught rev-1 in. The conservative rule bounds it, and S3's corpus arm is what
  actually observes it: an identical symbol set over this repo's own tracked `.js`.
- testing + left-shift gates — S2's table completes a class arm whose title already names the class;
  S3 makes the historical eight-definition regression runnable.
- migration / rollback — revert restores verbatim emission; `symbols.json` is re-rendered either way.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When the D7 `.ts` file (`export const RX = /` backtick `/;`, a block comment holding
  `export const GHOST = 1`, then ``export const T = `x`;``) is run through `enumerate_exports`, the
  result is `['RX', 'T']`. At the tip it is `['GHOST', 'RX', 'T']`.
- **AC2** — When the audit's LOSS fixture (`export const RX = /` backtick `/;` · `const s = "/*";` ·
  `export const KEEP = 1;` · `const t = "*/";` · ``export const T = `x`;``) is run, `KEEP` is
  PRESENT. Under rev-1's design it was lost — this is the criterion rev-1 had no way to fail.
- **AC3** — When the audit's second LOSS fixture (`export const RX = /` backtick `/;` ·
  `const R = /a\/*b/;` · `export const REAL = 1;` · `const x = 2; /* real */` ·
  ``export const T = `x`;``) is run, the result is `['REAL', 'RX', 'T']`.
- **AC4** — When `test_enumerate_exports_regex_borne_comment_opener` runs, ceiling 1 (the
  regex-borne BLOCK opener) is retired and loses nothing. **Ceiling 2 does NOT retire — it
  INVERTS into a raised `MapError`**, and that is a new failure mode this unit must declare rather
  than discover. The regex-borne `//` was MASKING the multi-declarator guard by truncating the
  line before the comma; modelling regexes removes the truncation, the guard sees the comma, and
  `export const U = /^https?:` + `\/\/` + `/, ALSO = 1;` raises where it previously returned
  the single-name result. That is the guard working, so the arm asserts the RAISE.
- **AC5** — When `render_comment_free` processes any fixture, its output line count equals its input
  line count — the statement-leading contract `JS_DEFINITION_RULES` depends on.
- **AC6** — When `enumerate_exports` and `scan_js_definitions` run over this repo's tracked `.js`,
  the symbol set is IDENTICAL to the pre-change run AND neither raises. Measured for this repo:
  identical with and without the model, so the arm is a REGRESSION guard here rather than evidence
  the change is needed — the need is adopter-facing and AC1–AC3 carry it. A symbol-set comparison
  cannot see an EXCEPTION, which is why the no-raise half is stated separately.
- **AC7** — When `python tools/codebase-map/selftest.py` runs, it reports `PASS`, and
  `python tools/codebase-map/test_codebase_map.py` exits 0.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct:
`python tools/codebase-map/selftest.py`, `python tools/codebase-map/test_codebase_map.py`,
`python tools/codebase-map/gen_map.py --write`.

## 8. Open questions

none — rev-1's open question was implicit and the audit answered it: the no-regex-model argument does
not survive, so the model is built.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D7.
- rev-2 · 2026-08-31 · folded spec-audit findings 21 and 31, which together refuted rev-1's design.
  21: the safety argument was about a REAL template applied to a PHANTOM span, and the fix as written
  LOST a real `export` between two string-borne comment delimiters. 31: a regex-borne `/*` inside the
  phantom span, balanced by a real `*/`, lost another. Both are the same root — the span should not
  exist — so S1 now models regex literals instead of compensating inside the span, which is this
  build's own stated rule applied one language over. The two pinned LOSS ceilings retire as a
  measured consequence, and S3 adds the corpus arm the audit asked for.
- rev-3 · 2026-08-31 · folded round-2 audit H2. Only ceiling 1 retires. Ceiling 2 inverts into a
  raised `MapError`, because the regex-borne `//` was masking the multi-declarator guard by
  truncating the line before the comma — an undeclared new failure mode, now AC4's subject. AC6
  also could not have seen it: a symbol-set comparison is blind to an exception.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **The seam is the conservative
regex-position rule `TOOL-aPairedLexer-8` states for JavaScript**, reused as a RULE here rather than
as code — the two languages share no runtime and `reuse_lookup.py` reports no Python counterpart.
`render_comment_free` is `fan-in 1` with callers `scan_js_definitions` and `enumerate_exports`;
neither changes signature and both benefit.

rev-1 cited "the code path's blanking, one branch over" as its seam. The audit measured that reuse as
the defect: the code path's blanking is correct OUTSIDE a span and destructive INSIDE a phantom one,
so the citation was wrong and is withdrawn here.

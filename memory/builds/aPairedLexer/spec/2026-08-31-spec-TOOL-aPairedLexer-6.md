# TOOL-aPairedLexer-6 — a DECLINED slash announces itself

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`renderCodeView` returns `unterminated: stack.length > 0 || mode !== 'code'` — an EOF-only signal
answering "what mode was I in when the file ran out". `blankLiterals` was given `dirty` in
`TOOL-aPairedLexer-4` for exactly this reason, and its own comment says `clean` must mean "nothing
was blanked that should not have been", not merely "the file did not end mid-construct".
`renderCodeView` never got that half, so rules 1 and 2 read a view that can be silently gutted.

This is round-2 review **D3**, and it is the unit that holds whatever the regex heuristic decides.
The `/` in `if (a) /` + backtick follows `)`, a position this file DELIBERATELY declines — declining
is defensible; declining SILENTLY is not. Two mis-lexed backticks balance, `unterminated` stays
false, the fallback never fires, and a raw `parallel(` between them is blanked out of the view.

## 2. Scope (IN)

- **S1** — `renderCodeView` sets a per-line `dirty` flag when a `/` is DECLINED as a regex start and
  a backtick occurs later on that same line.
- **S2** — it returns `unterminated: stack.length > 0 || mode !== 'code' || dirty`, so both consumers
  (`offendingLines`, `fanoutFindings`) fall back to the per-line view — which is the shipped 1.9
  verdict and cannot regress in either direction.
- **S3** — arms pinning the SIGNAL, not only the verdict.

## 3. Non-goals (OUT)

- Not changing which positions are regex positions. That is `TOOL-aPairedLexer-7` and `-8`.
- Not touching rules 3 or 5, whose fallback keys on `blankLiterals`.
- Not unifying the two scanners (`TOOL-aPairedLexer-5`).

## 4. Design

The fix is deliberately NOT "decline less often". It is "when you decline, say so". A declined slash
is the file's own stated ceiling; what makes it dangerous is that the ceiling is invisible to the
mechanism built to cover it. Announcing the decline routes the script to the per-line view, which is
exactly the verdict the shipped 1.9 gave — so the change cannot regress in either direction, and it
holds no matter what `-7` and `-8` decide about the heuristic.

Order matters: this lands FIRST or alongside `-7` and `-8`. The review measured that repairing the
lexer removes the trigger the `-9`, `-10` and `-11` fixtures rely on, and this unit is the one repair
that survives that.

## 5. Production-readiness checklist

- security — this is the security surface: it restores the fallback on a view that could be gutted.
- perf / scale — one boolean per line; no change in cost class.
- a11y · i18n — N/A, no interface, byte-oriented scanner.
- error / empty / loading states — unchanged; an unparseable payload still exits 0 by design.
- observability — a fallback is now REACHED where it silently was not; denial text is unchanged.
- risks — over-triggering `dirty` costs PRECISION only: the script is judged at the per-line view's
  accuracy, never admitted. Fail-closed by construction.
- testing + left-shift gates — S3 pins the signal so a refactor keeping the verdict by accident reds.
- migration / rollback — revert restores the prior behaviour; no artifact or contract shape changes.
- user docs — `memory/map/features/agent-cap.md` gap list is refreshed in the same commit.

## 6. Acceptance criteria

- **AC1** — When the D3 script (`const a = 1` / `if (a) /` backtick `/.test(s)` / a raw
  `parallel(D.map(...))` / the same declined-slash line again) is fed to the hook, it exits `2`. At
  the tip it exits `0`, and at 1.9 it exits `2` — a measured DENY→ADMIT regression this closes.
- **AC2** — When `renderCodeView` is called on a script holding one declined-slash-plus-backtick
  line, `.unterminated === true`. This pins the SIGNAL, so a later refactor that keeps the verdict by
  accident still reds.
- **AC3** — When the fixture's declined-slash lines are removed, the script still exits `2` — the
  control proving the fix is not simply "deny everything".
- **AC4** — When a lens prompt carries prose naming a primitive and no ambiguous slash, it still
  exits `0`: `rule1 prose: naming parallel( in a lens prompt admits` stays green, so `-2`'s win is
  not undone.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is green
  after it.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`,
`bash tools/check-kit-versions.sh`.

## 8. Open questions

*(none — the fix and its ordering were measured by the round-2 review, and both directions are pinned
by AC1 and AC3.)*

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D3.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "lexing javascript source into a comment-free code view
for a static guard"` and `python tools/memory-recall/query.py` with terms `agent-cap fanout regex
literal division blankLiterals renderCodeView fail-open lexer prev token stripStrings capFindings
unterminated`, both run 2026-08-31.

**The seam EXISTS and this unit extends it**: `blankLiterals` already carries exactly this
`dirty`/`clean` pair, added by `TOOL-aPairedLexer-4`, and its comment states the rationale. This unit
copies that shape into `renderCodeView` rather than inventing one. The probe reports both functions
at `fan-in 0` in the same file, which is the duplication `TOOL-aPairedLexer-5` tracks — noted, not
resolved here.

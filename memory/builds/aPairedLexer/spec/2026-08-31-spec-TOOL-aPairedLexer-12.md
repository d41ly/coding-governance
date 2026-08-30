# TOOL-aPairedLexer-12 — a phantom template may not RESURRECT a comment

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 |

<!-- /gen:spec-records -->

## 1. Goal

`render_comment_free` models strings and templates but no regex literal. A regex holding a backtick
opens a template span, and the string/template arm emits `text[i:j+1]` VERBATIM when that span
closes — so real comments inside it are never blanked, and a commented-out `export` is scanned as
LIVE code.

Round-2 review **D7**, reproduced end to end through `enumerate_exports`: a `.ts` file yields
`['GHOST', 'RX', 'T']` at the tip and `['RX', 'T']` at base `14e21399`.

This is a **third** regex-borne direction and is not one of the two ceilings pinned by
`test_enumerate_exports_regex_borne_comment_opener`. That arm pins two LOSSES; this one silently ADDS
a symbol that does not exist — corrupting the committed `symbols.json` a coverage ratchet then
demands be claimed. It is the map's own "a claim naming a dead key" failure, arriving through the
extractor rather than through a dossier.

## 2. Scope (IN)

- **S1** — blank comment text INSIDE a template span the same way it is blanked outside one, so a
  phantom span can never resurrect a comment.
- **S2** — a third arm on `test_enumerate_exports_regex_borne_comment_opener`, asserting `GHOST` is
  absent. The arm name already promises the class; it currently pins two of its three directions.
- **S3** — correct the docstring's safety claim, which is about DELETION and does not cover
  un-blanking.

## 3. Non-goals (OUT)

- **Not modelling regex literals in Python.** S1 is strictly safer and cannot lose a real definition,
  because a definition inside a template literal is not one. Modelling regexes here would import the
  whole ambiguity `TOOL-aPairedLexer-8` is managing in JavaScript, for no gain.
- Not the two pinned LOSS ceilings — they stay ceilings.
- Not `_has_top_level_comma`'s unterminated-quote masking; that is round-2 D8, a MEDIUM, and outside
  the owner's named scope.

## 4. Design

The template arm currently emits its span verbatim on close. It should emit the span with comment
text blanked, exactly as the code path does. A definition cannot live inside a template literal, so
blanking there can only ever remove noise — which is what makes this the safe direction and why it
does not need a regex model to be correct.

**Adopter-facing rather than local.** This repo's map has no `.ts` layer, so its own `symbols.json`
is unaffected today. That is why it is HIGH and not a blocker, and it is also why the arm matters:
nothing in this tree would notice the regression.

## 5. Production-readiness checklist

- security — N/A; this is inventory integrity, not a guard.
- perf / scale — one blanking pass over template spans; the function already walks them.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged; line count is still preserved.
- observability — none needed; the selftest arm is the signal.
- risks — over-blanking inside a template cannot lose a definition, by the §4 argument. Line count
  must not move, which AC4 pins.
- testing + left-shift gates — S2 completes a class arm that already names the class.
- migration / rollback — revert restores verbatim emission; `symbols.json` is re-rendered either way.
- user docs — the docstring correction is S3.

## 6. Acceptance criteria

- **AC1** — When the D7 `.ts` file (`export const RX = /` backtick `/;` then a block comment holding
  `export const GHOST = 1` then ``export const T = `x`;``) is run through `enumerate_exports`, the
  result is `['RX', 'T']`. At the tip it is `['GHOST', 'RX', 'T']`.
- **AC2** — When the same file is run at base `14e21399`, the result is `['RX', 'T']` — this restores
  the pre-diff behaviour rather than inventing one.
- **AC3** — When the two pinned LOSS ceilings run, they still hold:
  `test_enumerate_exports_regex_borne_comment_opener` keeps its existing two directions.
- **AC4** — When `render_comment_free` processes any of the fixtures, its output line count equals
  its input line count — the statement-leading contract.
- **AC5** — When `python tools/codebase-map/selftest.py` runs, it reports `PASS`.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct:
`python tools/codebase-map/selftest.py`, `python tools/codebase-map/test_codebase_map.py`.

## 8. Open questions

none — the safe direction is argued in §4 and does not depend on a regex model.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D7.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **The seam is
`render_comment_free`'s own code-path blanking, and S1 applies it in the template arm** — the same
mechanism, one branch over. `reuse_lookup.py` reports `render_comment_free` at `fan-in 1`, its two
callers being `scan_js_definitions` and `enumerate_exports`; neither changes, and both benefit.

# TOOL-aLexedStripper-6 — a seventh profile field: the interpolation pair

**Status:** SPECCED · rev-3 · 2026-08-30 · node a · Tier-2 · base 19d9b328 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-build-TOOL-aLexedStripper-1-acceptance-ledger.md](../build/2026-08-30-build-TOOL-aLexedStripper-1-acceptance-ledger.md) | journal | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-7-closing-diff-round2.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-7-closing-diff-round2.md) | diff-review | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 TOOL-aLexedStripper-7 |
| [2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-closing-diff-round1.md](../reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-closing-diff-round1.md) | diff-review | TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aLexedStripper-1`'s profile must stop deleting the code inside a Python f-string replacement
field. Those braces hold real identifiers with real cross-file fan-in, and blanking them is the
same under-count class that unit exists to remove, in a different spelling.

## 2. Scope (IN)

- **S1** — Add a seventh field to the profile, `interpolation_pair`: the open/close token pair whose
  BODY is scanned as code rather than blanked, or `None`. Python gets `{` / `}`, active only inside
  a string whose prefix carries `f`. C-family gets `${` / `}` inside a template literal.
- **S2** — Brace DEPTH is tracked inside a replacement field, so `f"{d['k'] if x else y}"` closes on
  its own `}` and not on a nested one. A doubled `{{` or `}}` is a literal brace and opens nothing.
- **S3** — A `.py` selftest arm asserting `f"{alpha_ident}"` returns `alpha_ident`, staged RED
  against the current code first.
- **S4** — Re-state `TOOL-aLexedStripper-1` AC3's `selftest.py` half against the figure the design
  now reaches, since the 100% it names was unreachable before this unit and is the number this unit
  is measured by.

## 3. Non-goals (OUT)

- No format-spec parsing. `f"{x:>{width}}"` nests a replacement field inside a format spec; S2's
  depth counting handles the braces, and no meaning is assigned to the spec itself.
- Not touching the C-family row's behaviour. `${…}` is already scanned as code by
  `TOOL-aLexedStripper-2`'s `renderCodeView` in the JavaScript scanner; this field is what makes the
  Python scanner's rule the SAME rule rather than a second one.
- Not chasing the `f` prefix letter itself, which the tokenizer reports as part of the string token
  and which `_IDENT_TOKEN_RE` picks up as a one-character identifier. It costs precision, not
  recall, and it is named in §4 as a residual.

## 4. Design

### The defect

`TOOL-aLexedStripper-1` §4 declares six fields and none of them can say "the body of this construct
is code". `marker_needs_word_start` was introduced there as "the field the naive rule cannot
express"; an f-string replacement field is a second such construct in the same family, and the
`quote_chars` rule blanks the whole literal including the expression.

Measured with a faithful implementation of that §4 over `git ls-files '*.py'` in this repo, against
stdlib `tokenize` NAME tokens:

| figure | value |
|---|---|
| ground-truth identifiers dropped | **73** |
| files affected | **25** |
| `tools/codebase-map/selftest.py` recall | 99.7%, sole miss `or` at `selftest.py:1139` |

Every one of the 73 is an f-string replacement field. Named instances: `AFFORDANCE_HEADING` and
`stale_claims` in `test_codebase_map.py`, `escape` from `map_lib.py`'s own
`rf"^\s*{re.escape(marker)}\b"` at `:527`, `read_gloss` and `render_negative` in
`scaffold_lexicon.py`. These are cross-file identifiers losing fan-in edges.

### Why this is one rule and not two

The C-family scanner already treats `${…}` as code — that is
`TOOL-aLexedStripper-2` S1's whole point, and the reason its `renderCodeView` is line-aligned. A
Python f-string is the same construct with different delimiters and a prefix condition. Declaring it
as a profile FIELD keeps one rule in one place; declaring it as a Python special case would put the
same idea in two scanners with two spellings, which is the class the bug checklist selects on every
diff this build has made.

### The prefix condition

A replacement field is active only inside a string whose prefix contains `f`, case-insensitively:
`f"…"`, `rf"…"`, `F"""…"""`, `fr'…'`. A plain `"…{x}…"` holds no code and its braces are literal
text. The scan therefore reads the prefix letters immediately before the opening quote.

### Residuals, stated rather than discovered later

- The `f`, `r`, `b` prefix letters are still returned as one-character identifier tokens. Precision
  cost only, and `_STOPWORDS` and the length filter in `stems` drop them downstream.
- A format spec's own nested field is walked as braces, not parsed.
- An f-string left unterminated is abandoned under `TOOL-aLexedStripper-1` S5, unchanged.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py` — the seventh field, the three profiles, the scan branch.
- `tools/codebase-map/selftest.py` — the S3 arm.
- `memory/builds/aLexedStripper/spec/2026-08-30-spec-TOOL-aLexedStripper-1.md` — AC3's restatement,
  as a rev bump with its §9 line.

### Alternatives rejected

- **Accept the loss and restate AC3.** The round-2 report offered this as the second route. Rejected:
  73 identifiers is the same order as the damage this build exists to remove on some files, and the
  fix is one field on a table §3 already names as the sole owner of the field set.
- **Use `ast` for Python.** Rejected for the reason `TOOL-aLexedStripper-1` §4 already records: it
  fails closed on a file that does not parse, and this scan must not.

## 5. Production-readiness checklist

- security — N/A. No new input surface.
- perf / scale — one branch in a pass that already walks every character.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an unterminated replacement field ends with the string; `S5` of
  `TOOL-aLexedStripper-1` governs an unterminated literal and is unchanged.
- observability — N/A.
- risks — over-capture. A brace inside an f-string that is NOT a replacement field is `{{`, handled
  by S2. Anything else the walk reads as code is prose promoted to an identifier, which costs
  precision and is bounded by AC2's floor.
- testing + left-shift gates — the S3 arm staged RED, plus AC2's corpus floors, which move only if
  this field works.
- migration / rollback — none; revert is a single-file revert.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a `.py` source holds `msg = f"hi {name.upper()} and {other or fallback}"`,
  `_identifier_tokens` returns `name`, `upper`, `other`, `or` and `fallback`. At BASE and under
  `TOOL-aLexedStripper-1` rev-2 it returns none of `upper`, `or`, `fallback`.
- **AC2** — When this repo's Python corpus is measured by the arm in
  `python tools/codebase-map/selftest.py`, the ground-truth identifiers missed fall from **73 to 0**
  and the files affected from **25 to 0**.
- **AC3** — When `tools/codebase-map/selftest.py` is scanned, recall is 100%, which
  `TOOL-aLexedStripper-1` AC3 demands and which no implementation of that unit's rev-2 design can
  reach.
- **AC4** — When a `.py` source holds `s = "{not_code}"` with no `f` prefix, `not_code` is NOT
  returned — the prefix condition, and the negative arm that stops the field becoming a blanket.
- **AC5** — When a `.py` source holds `f"{d['k'] if flag else other}"`, `d`, `flag` and `other`
  are returned and `k` is NOT — S2's depth tracking through a nested quote, whose CONTENT is a
  string and not an identifier. Stdlib `tokenize` reports `k` as a STRING token, so returning it
  would be over-capture measured against the same oracle this unit is graded by.
- **AC6** — When a `.py` source holds `f"{{literal}}"`, `literal` is NOT returned — the doubled
  brace is text.
- **AC7** — When the S3 arm is staged against the code at BASE, `python
  tools/codebase-map/selftest.py` reports it RED, and the observation is recorded in the acceptance
  ledger.
- **AC8** — When `python tools/codebase-map/selftest.py` runs whole, it passes.

## 7. Gates

The legs are read from `tools/gate-legs.json` at emission time. This unit's subject is the
`codebase-map` kit; `python tools/codebase-map/selftest.py` is the direct invocation AC7 and AC8
name.

## 8. Open questions

- **F1 — should the C-family row's `${…}` move onto this field too?** The JavaScript scanner is a
  different file (`agent-cap.js`) with its own state machine, so the field would be declared in
  `map_lib.py` and consumed nowhere for that row. RESOLVED (agent, 2026-08-30, delegated): declare
  it for the C-family row in `map_lib.py`, because `map_lib` scans `.ts` and `.js` files too and the
  same construct appears there; `agent-cap.js` keeps its own implementation, which §4 already says
  is a shape copied rather than shared.
- **F2 — does this field change `TOOL-aLexedStripper-1`'s AC1 corpus floor?** It can only raise
  recall. RESOLVED (agent, 2026-08-30, delegated): AC1's 99% floor stands and is measured again
  after this unit; AC2 here is the tighter figure.

## 9. Revision log

- rev-1 · 2026-08-30 · promoted from the round-2 spec audit's blocker 26+30 at the NON-CONVERGENT
  exit, per `BUILD-METHOD.md` M4. Both figures were reproduced before this spec was written: 73
  identifiers across 25 files, and `selftest.py` at 99.7% with `or` as the sole miss.
- rev-3 · 2026-08-30 · AC5 AMENDED, and the amendment is a correction to this spec rather than to
  the code. It demanded `k` from `f"{d['k'] …}"`, and `k` is the CONTENT of a string literal:
  stdlib `tokenize` reports it as a STRING, not a NAME, so the criterion asked for over-capture
  against the oracle §6 is measured by. It was caught by the closing review's round-2 finding
  that the interpolation walk counted braces inside nested strings — fixing that leak made the
  arm fail, and the arm was wrong. The nested string is now blanked inside the interpolation
  body, which is what stops a `{` inside one inflating the depth so the real closer never
  matches and the walk runs on consuming comments and strings as code. Reproduced before the
  fix: a `.ts` template holding `${ name.replace('{', '') }` leaked a following comment's prose
  and a following string's content into the index.
- rev-2 · 2026-08-30 · S4 recorded as a NO-OP after the build, with the reason, because a scope item
  that silently evaporates is indistinguishable from one nobody did. S4 was to restate
  `TOOL-aLexedStripper-1` AC3 against "the figure the design now reaches". That figure turned out to
  be 100%, which is exactly what AC3 already demanded — so the criterion stands unamended and the
  DESIGN moved to meet it instead. No edit to `-1` was owed and none was made.

## 10. Reuse audit

The seam is the interpolation handling `TOOL-aLexedStripper-2`'s `renderCodeView` already
implements for JavaScript: enter code mode at the open token, track depth, return at the close. This
unit declares the same rule as DATA in `map_lib.py`'s profile table rather than writing a second
walk, which is why it is one field and one branch.

`python tools/codebase-map/reuse_lookup.py "scan the code inside an interpolated string literal"`
was run for this unit. Its ranked hits are `scan` (`tools/memory-tree/row_grammar.py`, fan-in 9),
`scan_js_definitions` (`tools/codebase-map/map_lib.py`, fan-in 2), `agent-cap.topLevelArgs` and
`blankLiterals`. The two `map_lib` and `agent-cap` hits are the ones that matter and both were
already read for this build; `scan_js_definitions` is a definition extractor over whole files and
shares no lexing with the token scan, so it is a near-miss recorded rather than a seam. There is no
Python-side interpolation seam to extend, which is why §4 declares the rule as profile DATA
consumed by the existing pass rather than importing anything.

Recall terms used, for M7 re-runs: `codebase-map identifier tokens f-string interpolation
replacement field profile suffix scanner fan-in recall precision tokenize`.

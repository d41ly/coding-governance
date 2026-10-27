# TOOL-dRankedPlan-80 — a JavaScript declarator that opens with a destructuring pattern ends at its value, so the declarator after it is bound

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-80-deviation-801.md](../build/2026-10-27-build-TOOL-dRankedPlan-80-deviation-801.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 68 to 77
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`) confirmed
**finding 15 at HIGH**, item **H2**. `TOOL-dRankedPlan-72` S1 has rules only for an open declarator
whose first token is a `word`. A `{` or `[` pattern declarator has none, so in `const { a } = o, s =
path.join(kit, "ratify.py");` a walk built as written ends or stalls at the pattern, `s` is never
bound, and `spawnSync(py, [s, slug])` passes the deny-by-default ban while Node runs `ratify.py`. The
non-goals of units 64, 67 and 72 withhold only the destructured names, never a plain declarator after
them. This unit gives the walk a rule for every token that can open a JavaScript declarator. It
repairs `TOOL-dRankedPlan-72`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The pattern declarator. In `TOOL-dRankedPlan-72` S1's walk, at an open declarator whose
  first token is a `{` or `[` op, the pattern runs to its matching closer: the first `}` or `]` op at
  which a depth counted over the `(`, `[` and `{` ops and their closers, starting at 1 on the opener,
  returns to 0. The pattern binds no name, as `TOOL-dRankedPlan-64` §3 and unit 72 §3 state. When the
  token after the closer is an `=` op, the declarator's value runs from the token after the `=` to
  `read_js_binding_end(toks, k, c, l)` of `TOOL-dRankedPlan-71` S1, and the declarator ends there;
  otherwise it ends at the token after the closer. A declarator that ends at a depth-0 `,` op opens
  the next one by unit 72 S1's rule. A pattern with no matching closer before the end of the tokens
  ends the list. This supersedes unit 72 S1's opening rule as one stated for a `word` alone. Observed
  by AC1 to AC3.
- **S2** — The opener classes. A JavaScript declarator opens with a binding identifier or a binding
  pattern, so after S1 the walk has a rule for every first token the language allows: a `word` by
  unit 72 S1 and a `{` or `[` op by S1. Any other first token is a malformed declaration and ends the
  list, as unit 72 §5 states. Observed by AC1 and AC2.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.js` file ending in `spawnSync(py,
  [s, slug]);`, or with `"--exit"` last in that array where stated. Observed by AC1 to AC3.
  - `caller-js-bound-after-destructure` holds `const { a } = o, s = path.join(kit, "ratify.py");`. It
    is refused with exit 1.
  - `caller-js-bound-after-array-pattern` holds `let [a, b] = o, s = path.join(kit, "ratify.py");`,
    whose pattern holds a depth-1 `,`. It is refused with exit 1.
  - `caller-js-bound-after-destructure-exit` holds the first plant's declaration with `"--exit"` last
    in the array. It is admitted.

## 3. Non-goals (OUT)

- Binding the names a pattern destructures: unread, as `TOOL-dRankedPlan-64` §3 and
  `TOOL-dRankedPlan-72` §3 state.
- Where a binding ends, and the word declarator's rule: `TOOL-dRankedPlan-71` and
  `TOOL-dRankedPlan-72`, unchanged; `TOOL-dRankedPlan-81`'s item for finding 4 names the binding-end
  reader in unit 72 S1.
- A spec-audit check that a token walk's rules cover every token class that can open its unit: the
  audit's left-shift gate, a check over the spec corpus that the close's left-shift step owns.

### Edges

- **consumes-from** `TOOL-dRankedPlan-72` — S1's declarator walk, to which S1 adds the pattern opener; without it there is no walk to extend
- **consumes-from** `TOOL-dRankedPlan-71` — S1's `read_js_binding_end`, at which a pattern's value ends; without it a continued value ends early

## 4. Design

### Evidence

- A probe run 2026-10-27 at 753f09a8 over `scan_ts_tokens('const { a } = o, s = path.join(kit,
  "ratify.py");\n')` from `tools/lexicon/lexicon.py` printed `const`, `{`, `a`, `}`, `=`, `o`, `,`,
  `s`, `=`, `path`, … `;`, and `read_ts_expr_end(toks, 5, c, l)` returned 6, the `,`. The same over
  `let [a, b] = o, s = …` printed `let`, `[`, `a`, `,`, `b`, `]`, `=`, `o`, `,`, `s`, and the extent
  from 7 returned 8. The outputs are PINNED.
- `read_ts_expr_end` started inside a pattern returns at its depth-0 `,` (index 3 in the second
  probe), so it cannot find the closer, and S1 counts depth itself.
- `TOOL-dRankedPlan-48` §5 prices one tokenizer pass per `*.js` file the check reads, and its plants
  are `.js` files, so no TypeScript annotation follows a declarator's name here.

### The reading after this unit

| JavaScript | Bindings | Answer for `[s, slug]` |
|---|---|---|
| `const { a } = o, s = path.join(kit, "ratify.py");` | the pattern none, `s` to the call | caller |
| `let [a, b] = o, s = path.join(kit, "ratify.py");` | the pattern none, `s` to the call | caller |
| the first with `"--exit"` last in the array | the same | not a caller |
| `const { s } = o;` | none, the list ends at `;` | unchanged, unread |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-after-destructure`, `caller-js-bound-after-array-pattern`, `caller-js-bound-after-destructure-exit` | `ratify.py` fixture plants | none |

No item mints a function. S1 is a branch of unit 72's walk.

### Rollout

Live at landing, at order 25, the order after `TOOL-dRankedPlan-72`'s. Units 67, 73 to 76 share the
order and write `tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Name a declarator after a pattern as unread.** The ban would certify an absence over a shape the
  language writes, and a pattern then a plain path binding is one line.
- **Skip to the next depth-0 `,` from the pattern's opener.** The pattern's own `,` sits at depth 1,
  but its default values hold expressions whose extent only `read_ts_expr_end` knows once the `=` is
  reached, so the closer is counted and the value is read by the reader.

## 5. Production-readiness checklist

- security — narrows: a script path bound after a destructuring declarator is read by the ban.
- perf / scale — one depth counter over the pattern's tokens.
- error / empty / loading states — a pattern with no closer ends the list; the file holds no call
  after it that the list could bind.
- observability — the refusal names the file and the array's first line.
- risks — a pattern followed by neither `=` nor `,` ends the list, as a malformed declaration does.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-after-destructure` runs, the check
  exits 1 naming the planted `.js` file.
  Red when: the walk ends the list at a declarator whose first token is not a `word`.
- **AC2** — When the plant `caller-js-bound-after-array-pattern` runs, the check exits 1 naming the
  planted `.js` file.
  Red when: the pattern's depth-1 `,` opens a declarator, so `b` and not `s` follows it.
- **AC3** — When the plant `caller-js-bound-after-destructure-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a call whose bound path follows a pattern is refused with `--exit` last.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · the first two plants, staged by a walk that ends the list at a non-word declarator, and for AC2 by one that opens a declarator at the pattern's `,`; AC3 is green-only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 68 to 77, finding 15
  (HIGH, item H2), repairing `TOOL-dRankedPlan-72`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-72` S1's declarator walk, and the value is ended by
`TOOL-dRankedPlan-71` S1's `read_js_binding_end` over `read_ts_expr_end`
(`tools/lexicon/lexicon.py:1587`). `python tools/codebase-map/reuse_lookup.py "skip a bracketed
token group to its matching closer"`, run 2026-10-27, ranked `skip` (`tools/drift-audit/selftest.py`),
`resolve_prefix_token` and `match_expr`, none of which balances JavaScript tokens, so no existing
seam fits and S1's depth counter is new. The recall query returned units 63, 64, 70 and 72 and this
audit's H2 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript declaration list continue after a destructuring pattern declarator" --terms "declarator destructuring pattern binding read_js_binding_end read_ts_expr_end comma walk caller ratify"`

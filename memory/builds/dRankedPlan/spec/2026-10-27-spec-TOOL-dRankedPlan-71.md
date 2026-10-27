# TOOL-dRankedPlan-71 — a JavaScript binding ends no earlier than the language ends it, through one binding-end reader

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-71-deviation-711.md](../build/2026-10-27-build-TOOL-dRankedPlan-71-deviation-711.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 22 at HIGH**, item **H1**, which it shares with findings 1, 8 and 16. The failure-envelope
lens found that a binding which ends before the expression does fails OPEN: `const s = ok` then `  ?
path.join(kit, "ratify.py")` binds `s` to `ok`, and the call passes the deny-by-default ban. Both of
`TOOL-dRankedPlan-63`'s plants continue at a trailing `(`, which the reader sees without any fact, so
no criterion can tell a reading that ends early from one that does not. With the facts of
`TOOL-dRankedPlan-68` one continuation is still dropped: `read_ts_expr_end`'s docstring names a line
opening with `(` or `[` after an operand as its ceiling, read as a new statement, while JavaScript
inserts no semicolon there. So `const s = path.join` then `(kit, "ratify.py");` binds `s` to
`path.join`. This unit reads every binding through one reader that continues across that ceiling,
and plants each continuation the reader must see. Finding 1 is `TOOL-dRankedPlan-68`'s, finding 8
`TOOL-dRankedPlan-69`'s and finding 16 `TOOL-dRankedPlan-70`'s. This unit repairs
`TOOL-dRankedPlan-63`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The binding-end reader. `read_js_binding_end(toks, k, c, l)` in `tools/loop/ratify.py`
  returns `e = read_ts_expr_end(toks, k, c, l)`, and while `toks[e]` is an `(` or `[` op on a later
  line than `toks[e - 1]`, it continues with `e = read_ts_expr_end(toks, e, c, l)`. It returns the
  first `e` that is not such a token. `TOOL-dRankedPlan-63` S1's binding and every declarator of
  `TOOL-dRankedPlan-64` S1 end at it, which supersedes their direct `read_ts_expr_end` calls.
  `read_ts_expr_end` is unchanged, so `parse_ts_source` keeps its ceiling. Observed by AC1 to AC4.
- **S2** — The plants. Four cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.js` file ending in `spawnSync(py,
  [s, slug]);`. Observed by AC1 to AC4.
  - `caller-js-bound-ternary` holds `const s = ok`, then `  ? path.join(kit, "ratify.py")`, then `  :
    other;`. It is refused with exit 1.
  - `caller-js-bound-logical-or` holds `const s = base`, then `  || path.join(kit, "ratify.py");`. It
    is refused with exit 1.
  - `caller-js-bound-paren-line` holds `const s = path.join`, then `(kit, "ratify.py");`. It is refused
    with exit 1.
  - `caller-js-bound-paren-line-exit` holds the same with `"--exit"` last in the array. It is admitted.

## 3. Non-goals (OUT)

- The facts and the calls that pass them: `TOOL-dRankedPlan-68`, `-69` and `-70`, the same item.
- Moving the ceiling inside `read_ts_expr_end`. `parse_ts_source` relies on it to keep a
  semicolon-free arrow body from swallowing the next statement, and that reading is not a ban.
- A binding by destructuring: unread, `TOOL-dRankedPlan-67`'s item for finding 33.

### Edges

- **consumes-from** `TOOL-dRankedPlan-63` — S1's binding extent, which S1 reads through the new reader; without it there is no binding to end
- **consumes-from** `TOOL-dRankedPlan-64` — S1's per-declarator extent, which S1 ends at the same reader
- **consumes-from** `TOOL-dRankedPlan-68` — S1's facts, without which the ternary and logical plants end at line 1
- **hands-off** `TOOL-dRankedPlan-80` — S1's binding-end reader, at which that unit ends a destructuring declarator's value (spec audit of units 68 to 77, id 15)
- **hands-off** `TOOL-dRankedPlan-81` — S1, §3, §5 and §7, which that unit's items for findings 4, 11 and 3 correct; carry S4, S7 and S15 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- `read_ts_expr_end`'s docstring (`tools/lexicon/lexicon.py:1587-1605`) says "The ceiling that
  remains is a line opening with `(` or `[` after an operand, read as a new statement". ECMAScript's
  automatic semicolon insertion inserts none before a line opening with `(` or `[`, so the language
  reads one expression there.
- A probe run 2026-10-27 at a76dbde6 returned, without and with the facts: 4 and 12 for the ternary,
  4 and 10 for the leading `||`, and 5 and 5 for the `(` line, whose `(` is token 5 on line 2. The
  outputs are PINNED.

### The reading after this unit

| JavaScript | Binding of `s` | Answer for `[s, slug]` |
|---|---|---|
| `const s = ok` then `  ? path.join(kit, "ratify.py")` then `  : other;` | through the `;` | caller |
| `const s = base` then `  \|\| path.join(kit, "ratify.py");` | through the `;` | caller |
| `const s = path.join` then `(kit, "ratify.py");` | through the `;` | caller |
| the same with `"--exit"` last in the array | the same | not a caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_js_binding_end` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_js_binding_end --as py.function` answered OK |
| `caller-js-bound-ternary`, `caller-js-bound-logical-or`, `caller-js-bound-paren-line`, `caller-js-bound-paren-line-exit` | `ratify.py` fixture plants | none |

The minted function is rendered into `memory/map/generated/symbols.json` by `gen_map.py --write`, as
`TOOL-dRankedPlan-61` S1 states.

### Rollout

Live at landing, at order 24, after `TOOL-dRankedPlan-68` and `TOOL-dRankedPlan-70` inside that step.
Units 62, 65, 66, 68, 69, 70 and 72 share the order and write `tools/loop/ratify.py`, so by
BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `memory/map/generated/symbols.json`: the render of S1's function

### Alternatives rejected

- **Plant only, with no reader change.** The ternary and logical plants pass on unit 68's facts, but
  the `(` line stays open, and the finding's class is a binding that ends before the expression.
- **Read to the first depth-0 `;`.** It swallows every semicolon-free statement after the binding,
  the reading `read_ts_expr_end`'s docstring rejects.

## 5. Production-readiness checklist

- security — narrows: a binding continued on a line opening with `(` or `[` is read whole.
- perf / scale — at most one extra `read_ts_expr_end` call per such line.
- error / empty / loading states — a binding with no end runs to `len(toks)`, which fails closed.
- observability — the refusal names the file and the array's first line.
- risks — a semicolon-free statement that opens with `(` after a binding joins it, as JavaScript
  itself joins them; a wrong join holds more tokens and fails closed.
- testing — the four plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-ternary` runs, the check exits 1
  naming the planted `.js` file.
  Red when: the extent is read without the facts, so `s` binds `ok` alone.
- **AC2** — When the plant `caller-js-bound-logical-or` runs, the check exits 1 naming the planted
  `.js` file.
  Red when: the extent is read without the facts, so `s` binds `base` alone.
- **AC3** — When the plant `caller-js-bound-paren-line` runs, the check exits 1 naming the planted
  `.js` file.
  Red when: the binding ends at one `read_ts_expr_end` call, at the `(` opening line 2.
- **AC4** — When the plant `caller-js-bound-paren-line-exit` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: a continued binding's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the four plants: a two-argument extent call reddens AC1 and AC2, and a single `read_ts_expr_end` call with no `(` or `[` continuation reddens AC3; AC4 is green-only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 22
  (HIGH, item H1, shared with findings 1, 8 and 16), repairing `TOOL-dRankedPlan-63`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-80` and the hands-off edge to `TOOL-dRankedPlan-81`, each the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam reused is `read_ts_expr_end` (`tools/lexicon/lexicon.py:1587`), called again from the token
its ceiling stops at; the seam extended is the binding collector of `TOOL-dRankedPlan-60` S1 through
units 63 and 64. `python tools/codebase-map/reuse_lookup.py "pass the lexer continuation facts to
the expression end reader"`, run 2026-10-27, ranked name stems only (`read`, `read_text`,
`read_conf`), none of which reads JavaScript, so no existing seam ends a binding past the ceiling and
S1's loop is new. The recall query returned this audit's H1 item and units 63 and 64, and they agree
with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when a line continues after an operator the lexer drops" --terms "read_ts_expr_end conts lits scan_ts_tokens strs continuation ASI binding declarator caller ratify"`

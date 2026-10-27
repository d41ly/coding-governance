# TOOL-dRankedPlan-63 — a JavaScript binding runs to the end its expression reader finds, across lines

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-63-deviation-631.md](../build/2026-10-27-build-TOOL-dRankedPlan-63-deviation-631.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) | spec-audit | TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 53 to 62
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`) confirmed
**finding 32 at HIGH**, item **H1**, which it shares with finding 21. `TOOL-dRankedPlan-60` S1 ends a
binding at the first depth-0 `;` or at the last depth-0 token on the declaration's line. Prettier
writes `const s = path.join(` and puts the arguments on the next line, so the binding stops at the
`(` and never holds the `"ratify.py"` string. `spawnSync(py, [s, slug])` then passes the
deny-by-default ban. This unit ends a binding where `read_ts_expr_end` ends the expression, so a
binding written across lines holds all of its tokens. Finding 21, the declarator list and the
typed-rule reuse half of the same item, is `TOOL-dRankedPlan-64`'s. This unit repairs
`TOOL-dRankedPlan-60`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The binding extent. A binding of `TOOL-dRankedPlan-60` S1 runs from the token after its `=`
  op, at index `k`, up to `read_ts_expr_end(toks, k)`, called from the loop kit's `extract_code.py`
  over the same `scan_ts_tokens(text, strs=True)` stream. That reader ends at a depth-0 `;` or `,`, at
  an unbalanced closer, or at a line break that ends the statement under ASI. A line ending in `(`,
  `,` or another continuing op does not end the binding. This supersedes unit 60 S1's sentence "The
  binding's tokens run from that `=` to the first `;` op at bracket depth 0 or to the last token on
  the declaration's line at depth 0, whichever comes first". Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-js-bound-multiline` plants a `.js` file holding `const s = path.join(`, then `  kit,
    "ratify.py");` on the next line, then `spawnSync(py, [s, slug]);`. It is refused with exit 1.
  - `caller-js-bound-multiline-exit` plants the same with `"--exit"` as the array's last element. It
    is admitted.

## 3. Non-goals (OUT)

- A declaration list `const a = 1, s = …`: `TOOL-dRankedPlan-64`, the same item, which starts a
  binding at each declarator over S1's end.
- Destructuring, such as `const { s } = …`: `TOOL-dRankedPlan-67`'s item for finding 33 names it as
  unread.
- A change to `read_ts_expr_end` itself. It is read as moved verbatim, and this unit only calls it.

### Edges

- **consumes-from** `TOOL-dRankedPlan-60` — S1's declaration collector and S2's resolution, whose binding extent S1 restates; without them there is no binding to bound
- **hands-off** `TOOL-dRankedPlan-64` — S1's extent, which ends at a depth-0 `,` and over which that unit starts each later declarator's binding
- **hands-off** `TOOL-dRankedPlan-68` — S1's extent call, to which that unit passes the lexer's `conts` and `lits` (spec audit of units 63 to 67, id 1)
- **hands-off** `TOOL-dRankedPlan-71` — S1's extent, which that unit reads through one binding-end reader past the ceiling of a line opening with `(` or `[` (spec audit of units 63 to 67, id 22)
- **hands-off** `TOOL-dRankedPlan-77` — §4 Evidence and §5, which that unit's item for finding 9 restates; carry S15 of that unit into this unit's pass (spec audit of units 63 to 67)

## 4. Design

### Evidence

- `read_ts_expr_end` is `tools/lexicon/lexicon.py:1587`. `parse_ts_source` calls it at :1824 for a
  brace-less arrow body. TOOL-dTotalRecall-13 S1 moves "the TypeScript helpers" between
  `scan_ts_tokens` (:950) and `parse_ts_defs` (:1693) verbatim into the canonical `extract_code`
  block, and the loop kit carries a copy of that block.
- A probe run 2026-10-27 at c22908a6 over `scan_ts_tokens('const s = path.join(\n  kit,
  "ratify.py");\nspawnSync(py, [s, slug]);\n')` returned 9 from `read_ts_expr_end(toks, 3)`, the `;`
  on line 2. The same form with no semicolons returned 9 too, the `spawnSync` word on line 3. Unit 60
  S1's rule stops at index 5, the `(` that ends line 1. The outputs are PINNED. The default stream
  was probed, because `strs` lands with `TOOL-dRankedPlan-48`, and a `str` token adds no op, so no
  depth or `;` moves.

### The reading after this unit

| JavaScript | Binding of `s` | Answer for `[s, slug]` |
|---|---|---|
| `const s = path.join(` then `  kit, "ratify.py");` | lines 1 and 2, through the `;` | caller |
| the same with `"--exit"` last in the array | the same | not a caller |
| `const s = path.join(kit, "ratify.py");` | line 1, through the `;` | caller, unchanged |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-multiline`, `caller-js-bound-multiline-exit` | `ratify.py` fixture plants | none |

No item mints a function. S1 calls `read_ts_expr_end` and adds no reader of its own.

### Rollout

Live at landing, at order 23. Units 53, 54, 56, 61, 63 and 64 share order 23. This unit and units 53,
54, 56 and 64 write `tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside
that step, this unit before unit 64, which consumes from it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Extend unit 60's typed rule to the declaration's last line.** That is a third hand-written
  extent rule beside `read_ts_expr_end` and `read_ts_brace_end`, and it still needs ASI to find the
  last line. The reader that already answers ASI is the one to call.

## 5. Production-readiness checklist

- security — narrows: a JS binding written across lines is read whole by the deny-by-default ban.
- perf / scale — one forward scan per declaration, bounded by the statement.
- error / empty / loading states — a declaration with no end runs to the stream's end, which
  `read_ts_expr_end` returns as `len(toks)`, so the binding fails closed.
- observability — the refusal names the file and the array's first line.
- risks — a binding that swallows a following statement under the ASI ceiling the reader's
  docstring names holds more tokens, which fails closed.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-multiline` runs, the check exits 1
  naming the planted `.js` file.
  Red when: the binding stops at the last token of the declaration's first line and passes.
- **AC2** — When the plant `caller-js-bound-multiline-exit` runs, the check exits 0 and prints `ratify
  — callers:`.
  Red when: a multi-line bound `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 · `caller-js-bound-multiline` and its `--exit` twin, staged by unit 60 S1's extent rule as written, which reddens AC1 and leaves AC2 green · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 53 to 62, finding 32 (HIGH,
  item H1, shared with finding 21), repairing `TOOL-dRankedPlan-60`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-68`, the hands-off edge to `TOOL-dRankedPlan-71`, the hands-off edge to `TOOL-dRankedPlan-77`, each the reciprocal of that promoted unit's own edge (spec audit of units 63 to 67, `reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam reused is `read_ts_expr_end` (`tools/lexicon/lexicon.py:1587`), the ASI-aware expression-end
reader `parse_ts_source` already calls, reached through the loop kit's `extract_code.py` copy, and the
seam extended is `TOOL-dRankedPlan-60` S1's collector. `python tools/codebase-map/reuse_lookup.py
"find where a javascript expression ends across lines under automatic semicolon insertion"`, run
2026-10-27, ranked name stems only (`check_line`, `render_line`, `parse_conf_line`), none of which
reads JavaScript, so the map's probe missed the reader. The source read found it: finding 21 cites
`lexicon.py:1587`, and the file holds `read_ts_expr_end` there at c22908a6. The recall query
returned this audit's H1 item and `TOOL-dRankedPlan-60`, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when its declaration spans lines" --terms "read_ts_expr_end ASI expression end declaration binding scan_ts_tokens strs argv array caller ratify"`

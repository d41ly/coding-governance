# TOOL-dRankedPlan-64 — each declarator of a JavaScript declaration list is its own binding

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-64-deviation-641.md](../build/2026-10-27-build-TOOL-dRankedPlan-64-deviation-641.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) | spec-audit | TOOL-dRankedPlan-63 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 53 to 62
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`) confirmed
**finding 21 at HIGH**, item **H1**, which it shares with finding 32. `TOOL-dRankedPlan-60` S1 types
its own extent rule instead of reusing `read_ts_expr_end`, and it collects only the first `NAME =`
of a declaration. In `const a = 1, s = path.join(kit, "ratify.py");` only `a` is declared, its
binding runs to the `;` and swallows the `ratify.py` string, and `s` is never collected, so
`spawnSync(py, [s, slug])` passes the deny-by-default ban. `TOOL-dRankedPlan-63` makes the extent
`read_ts_expr_end`'s, which ends at the declarator `,`. This unit starts a binding at each later
declarator, so every name of a list is bound to its own tokens. Finding 33 is the medium face of the
same defect, and its item in `TOOL-dRankedPlan-67` names destructuring as unread. This unit repairs
`TOOL-dRankedPlan-60`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The declarators. After a `word` token `const`, `let` or `var`, and after each depth-0 `,`
  op at which `TOOL-dRankedPlan-63` S1's extent ends, a `word` token followed by an `=` op opens a
  declarator binding that name, whose tokens run from the token after that `=` to its own
  `read_ts_expr_end`. A `word` followed by `,` or `;` declares a name with no value and binds nothing.
  The list ends at the first extent end that is not a `,`. This supersedes the single-name shape of
  `TOOL-dRankedPlan-60` S1, "a `word` token for the name, and an `=` op", for every declarator after
  the first. Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-js-bound-multi-decl` plants a `.js` file holding `const a = 1, s = path.join(kit,
    "ratify.py");` and then `spawnSync(py, [s, slug]);`. It is refused with exit 1.
  - `caller-js-bound-multi-decl-other` plants `const s = path.join(kit, "guard.py"), t =
    path.join(kit, "ratify.py");` and then `spawnSync(py, [s, slug]);`. It is admitted, because `s` is
    bound to `guard.py` alone.

## 3. Non-goals (OUT)

- Where one binding ends: `TOOL-dRankedPlan-63`, the same item.
- Destructuring, `const { s } = …` or `const [s] = …`: unread, the ceiling `TOOL-dRankedPlan-67`'s
  item for finding 33 names in unit 60's §3 and §4.
- A `for (let i = 0, n = …;` header. Its declarators are read by S1 like any other, and none binds a
  script path in the tree.

### Edges

- **consumes-from** `TOOL-dRankedPlan-63` — S1's extent through `read_ts_expr_end`, whose depth-0 `,` end is where S1 opens the next declarator; without it the first binding swallows the list
- **consumes-from** `TOOL-dRankedPlan-60` — S1's collector and S2's resolution, which S1 gives one binding per declarator
- **hands-off** `TOOL-dRankedPlan-70` — S1's per-declarator `read_ts_expr_end` call, which that unit gives the lexer's facts (spec audit of units 63 to 67, id 16)
- **hands-off** `TOOL-dRankedPlan-71` — S1's per-declarator extent, which that unit ends at its binding-end reader (spec audit of units 63 to 67, id 22)
- **hands-off** `TOOL-dRankedPlan-72` — S1's declarator loop, whose opening rule that unit restates so a valueless declarator opens the next (spec audit of units 63 to 67, id 19)
- **hands-off** `TOOL-dRankedPlan-77` — §4's table, AC2 and §7, which that unit's items for findings 2 and 3 correct; carry S5 and S6 of that unit into this unit's pass (spec audit of units 63 to 67)

## 4. Design

### Evidence

- A probe run 2026-10-27 at c22908a6 over `scan_ts_tokens('const a = 1, s = path.join(kit,
  "ratify.py");\n…')` printed `word const`, `word a`, `op =`, `word 1`, `op ,`, `word s`, `op =`, …
  `op ;`, and `read_ts_expr_end(toks, 3)` returned 4, the `,` op. The output is PINNED.
- `TOOL-dRankedPlan-60` S1 names the declaration shape as one keyword, one name and one `=`, and its
  §3 and §4 table name no declaration list.

### The reading after this unit

| JavaScript | Bindings | Answer for `[s, slug]` |
|---|---|---|
| `const a = 1, s = path.join(kit, "ratify.py");` | `a` to `1`, `s` to the `path.join` call | caller |
| `const s = path.join(kit, "guard.py"), t = path.join(kit, "ratify.py");` | `s` to `guard.py`, `t` to `ratify.py` | not a caller |
| `let a, s = path.join(kit, "ratify.py");` | `a` unbound, `s` to the call | caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-multi-decl`, `caller-js-bound-multi-decl-other` | `ratify.py` fixture plants | none |

No item mints a function. S1 is a loop inside unit 60's collector.

### Rollout

Live at landing, at order 23, after `TOOL-dRankedPlan-63` inside that step, because both write
`tools/loop/ratify.py` and this unit consumes from it. Units 53, 54 and 56 write the same file at the
same order and are sequenced by BUILD-METHOD M6 clause 1.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Split the declaration at every depth-0 `,` before reading it.** That restates the extent rule a
  second time beside `read_ts_expr_end`, the defect finding 21 names, and the two would drift on
  depth and ASI.

## 5. Production-readiness checklist

- security — narrows: a script path bound by a later declarator is read by the deny-by-default ban.
- perf / scale — one `read_ts_expr_end` call per declarator.
- error / empty / loading states — a declarator with no `=` binds nothing, and an element naming it
  is read as `TOOL-dRankedPlan-48` S3 reads an unbound word.
- observability — the refusal names the file and the array's first line.
- risks — none beyond `TOOL-dRankedPlan-60`'s fail-closed reuse of a name.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-multi-decl` runs, the check exits
  1 naming the planted `.js` file.
  Red when: only the first declarator of a list is collected, so `s` is never bound.
- **AC2** — When the plant `caller-js-bound-multi-decl-other` runs, the check exits 0 and prints
  `ratify — callers:`.
  Red when: the first declarator's binding runs to the `;` and holds the next declarator's
  `ratify.py` string.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `caller-js-bound-multi-decl` reddened by a collector that reads the first declarator only, and `caller-js-bound-multi-decl-other` reddened by unit 60 S1's extent to the first depth-0 `;` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 53 to 62, finding 21 (HIGH,
  item H1, shared with finding 32), repairing `TOOL-dRankedPlan-60`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-70`, the hands-off edge to `TOOL-dRankedPlan-71`, the hands-off edge to `TOOL-dRankedPlan-72`, the hands-off edge to `TOOL-dRankedPlan-77`, each the reciprocal of that promoted unit's own edge (spec audit of units 63 to 67, `reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam reused is `read_ts_expr_end` (`tools/lexicon/lexicon.py:1587`), through
`TOOL-dRankedPlan-63`'s extent, whose depth-0 `,` end is the declarator boundary; the seam extended
is `TOOL-dRankedPlan-60` S1's collector. `python tools/codebase-map/reuse_lookup.py "split a
javascript declaration list into its declarators"`, run 2026-10-27, ranked name stems only
(`declares`, `read_id_list`, `declared_list`), none of which reads JavaScript, so no existing seam fits
beyond the reader and the collector. The recall query returned this audit's H1 item and
`TOOL-dRankedPlan-60`, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when its declaration spans lines" --terms "read_ts_expr_end ASI expression end declaration binding scan_ts_tokens strs argv array caller ratify"`

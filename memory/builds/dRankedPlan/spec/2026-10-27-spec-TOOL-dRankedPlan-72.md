# TOOL-dRankedPlan-72 — a JavaScript declarator opens after every depth-0 comma that ends a declarator, valued or not

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-72-deviation-721.md](../build/2026-10-27-build-TOOL-dRankedPlan-72-deviation-721.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 19 at HIGH**, item **H2**. Finding 3, item M3, is its medium face, and its item in
`TOOL-dRankedPlan-77` corrects unit 64's design table. `TOOL-dRankedPlan-64` S1 opens a later
declarator only "after each depth-0 `,` op at which `TOOL-dRankedPlan-63` S1's extent ends". A
valueless declarator has no extent, so in `let a, s = path.join(kit, "ratify.py");` the `,` after
`a` opens nothing, `s` is never bound, and `spawnSync(py, [s, slug])` passes the deny-by-default ban,
while unit 64's §4 row 3 promises "caller". This unit opens a declarator after every depth-0 `,` that
ends one, valued or not. It repairs `TOOL-dRankedPlan-64`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The declarator walk. In a declaration led by a `word` token `const`, `let` or `var`, a
  declarator opens at the token after the keyword. At an open declarator, a `word` followed by an `=`
  op binds that name to the tokens from after the `=` to the binding's end, and the declarator ends
  there. A `word` followed by any other token declares the name, binds nothing, and the declarator
  ends at that token. When a declarator ends at a depth-0 `,` op, the next declarator opens at the
  token after it; when it ends anywhere else, the list ends. This supersedes `TOOL-dRankedPlan-64` S1's
  "after each depth-0 `,` op at which `TOOL-dRankedPlan-63` S1's extent ends" and its "The list ends
  at the first extent end that is not a `,`". Observed by AC1 and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.js` file ending in `spawnSync(py,
  [s, slug]);`. Observed by AC1 and AC2.
  - `caller-js-bound-unvalued-first` holds `let a, s = path.join(kit, "ratify.py");`. It is refused
    with exit 1. It is the plant finding 3's fix names `caller-js-bound-multi-decl-novalue`; one is
    built, under this name.
  - `caller-js-bound-unvalued-middle` holds `let a = 1, b, s = path.join(kit, "ratify.py");`. It is
    refused with exit 1.

## 3. Non-goals (OUT)

- Where a binding ends: `TOOL-dRankedPlan-63`, `-68` and `-71`.
- Unit 64's §4 row 3 and AC2's staged break: `TOOL-dRankedPlan-77`'s items for findings 3 and 2.
- Destructuring and a `for (let …;` header: as `TOOL-dRankedPlan-64` §3 states.

### Edges

- **consumes-from** `TOOL-dRankedPlan-64` — S1's declarator loop, whose opening rule S1 restates; without it no later declarator is collected
- **hands-off** `TOOL-dRankedPlan-77` — S2's `caller-js-bound-unvalued-first`, which that unit's item for finding 3 names in unit 64's §4 row 3
- **hands-off** `TOOL-dRankedPlan-80` — S1's walk, to which that unit adds the pattern declarator's rule (spec audit of units 68 to 77, id 15)
- **hands-off** `TOOL-dRankedPlan-81` — S1 and §3, which that unit's item for finding 4 corrects; carry S4 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- A probe run 2026-10-27 at a76dbde6 over `scan_ts_tokens('let a, s = path.join(kit,
  "ratify.py");\n')` printed `let`, `a`, `,`, `s`, `=`, `path`, … `;`. No extent is read for `a`, so
  the `,` at index 2 is reached by no extent end. The output is PINNED.
- `TOOL-dRankedPlan-64` §4 "The reading after this unit" row 3 answers "caller" for this form, and
  its two plants each open with a valued declarator.

### The reading after this unit

| JavaScript | Bindings | Answer for `[s, slug]` |
|---|---|---|
| `let a, s = path.join(kit, "ratify.py");` | `a` unbound, `s` to the call | caller |
| `let a = 1, b, s = path.join(kit, "ratify.py");` | `a` to `1`, `b` unbound, `s` to the call | caller |
| `let a;` | `a` unbound, the list ends at `;` | unchanged |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-unvalued-first`, `caller-js-bound-unvalued-middle` | `ratify.py` fixture plants | none |

No item mints a function. S1 restates unit 64's loop condition.

### Rollout

Live at landing, at order 24. Units 62, 65, 66 and 68 to 71 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Split the list at every depth-0 `,`.** It restates the extent rule beside `read_ts_expr_end`, the
  defect unit 64's finding named, and an initializer's own commas sit at depth 0 only after its
  extent ends, which only the extent knows.

## 5. Production-readiness checklist

- security — narrows: a script path bound after a valueless declarator is read by the ban.
- perf / scale — none: one token look-ahead per declarator.
- error / empty / loading states — a name followed by a token that is neither `=` nor `,` ends the
  list, as a malformed declaration does.
- observability — the refusal names the file and the array's first line.
- risks — none beyond `TOOL-dRankedPlan-60`'s fail-closed reuse of a name.
- testing — the two plants.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-unvalued-first` runs, the check
  exits 1 naming the planted `.js` file.
  Red when: a declarator opens only after an extent end, so `s` is never bound.
- **AC2** — When the plant `caller-js-bound-unvalued-middle` runs, the check exits 1 naming the
  planted `.js` file.
  Red when: a valueless declarator between two valued ones ends the list.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · both plants, staged by a walk that continues only after an extent end · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 19
  (HIGH, item H2; finding 3 is its medium face), repairing `TOOL-dRankedPlan-64`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-80` and the hands-off edge to `TOOL-dRankedPlan-81`, each the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-64` S1's declarator loop inside `TOOL-dRankedPlan-60` S1's
collector; the binding end it reads is `read_ts_expr_end` (`tools/lexicon/lexicon.py:1587`) through
units 63, 68 and 71. `python tools/codebase-map/reuse_lookup.py "pass the lexer continuation facts to
the expression end reader"`, run 2026-10-27, ranked name stems only (`read`, `read_text`,
`read_conf`), none of which walks a JavaScript declaration, so no existing seam fits beyond unit 64's
loop. The recall query returned this audit's items and units 63 and 64, and they agree with the
source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when a line continues after an operator the lexer drops" --terms "read_ts_expr_end conts lits scan_ts_tokens strs continuation ASI binding declarator caller ratify"`

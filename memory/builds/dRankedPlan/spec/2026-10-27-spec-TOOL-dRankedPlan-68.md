# TOOL-dRankedPlan-68 — the JavaScript reader scans once with the lexer's continuation facts, and a binding's extent reads them

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-68-deviation-681.md](../build/2026-10-27-build-TOOL-dRankedPlan-68-deviation-681.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md) | research | TOOL-dRankedPlan-70 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-68-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md) | research | TOOL-dRankedPlan-70 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 1 at HIGH**, item **H1**, which it shares with findings 8, 16 and 22. `TOOL-dRankedPlan-63`
S1 ends a binding at `read_ts_expr_end(toks, k)` and passes neither `conts` nor `lits`. The lexer
emits no op for `.`, `||`, `&&`, `??`, `?` or `+`, so without `conts` the reader ends a binding at a
line break beside any of them. A Prettier member chain, `const s = path` then `  .join(kit,
"ratify.py");`, binds `s` to `path` alone, and `spawnSync(py, [s, slug])` passes the deny-by-default
ban. This unit has the JavaScript reader collect both facts from its one scan and hand them to the
extent call, as `parse_ts_source` does. Finding 8 is `TOOL-dRankedPlan-69`'s, finding 16
`TOOL-dRankedPlan-70`'s and finding 22 `TOOL-dRankedPlan-71`'s. This unit repairs
`TOOL-dRankedPlan-63`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The facts. `read_js_callers` takes its tokens from one call, `scan_ts_tokens(text,
  strs=True, conts=c, lits=l)`, with `c` a new `set` and `l` a new `dict`, from the loop kit's
  `extract_code.py`. `TOOL-dRankedPlan-63` S1's binding extent becomes `read_ts_expr_end(toks, k, c,
  l)`. This supersedes `TOOL-dRankedPlan-48` S1's clause "and `read_js_callers` passes none of
  `calls`, `conts` or `lits`" for `conts` and `lits`, unit 48 S3's call `scan_ts_tokens(text,
  strs=True)`, and unit 63 S1's `read_ts_expr_end(toks, k)`. `calls` stays unpassed. Observed by AC1
  and AC2.
- **S2** — The plants. Two cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1 and AC2.
  - `caller-js-bound-chain` plants a `.js` file holding `const s = path`, then `  .join(kit,
    "ratify.py");`, then `spawnSync(py, [s, slug]);`. It is refused with exit 1.
  - `caller-js-bound-chain-exit` plants the same with `"--exit"` as the array's last element. It is
    admitted.

## 3. Non-goals (OUT)

- Where a `str` token of the `strs` stream puts the facts: `TOOL-dRankedPlan-69`, the same item.
- The per-declarator extent of `TOOL-dRankedPlan-64` S1: `TOOL-dRankedPlan-70`, the same item.
- A line opening with `(` or `[`, and the ternary and logical plants: `TOOL-dRankedPlan-71`, the same
  item.
- A change to `read_ts_expr_end` or `scan_ts_tokens`. This unit only passes arguments both already
  take.

### Edges

- **consumes-from** `TOOL-dRankedPlan-63` — S1's binding extent, to which S1 hands the facts; without it there is no extent call to give them to
- **consumes-from** `TOOL-dRankedPlan-48` — S3's `scan_ts_tokens(text, strs=True)` call in `read_js_callers`, which S1 gives the two containers
- **hands-off** `TOOL-dRankedPlan-69` — S1's facts, under which that unit pins where a `str` token of the `strs` stream puts them
- **hands-off** `TOOL-dRankedPlan-70` — S1's `c` and `l`, which that unit passes to unit 64's per-declarator extent
- **hands-off** `TOOL-dRankedPlan-71` — S1's facts, over which that unit's ternary and logical plants are read

## 4. Design

### Evidence

- `read_ts_expr_end(toks, k, conts=frozenset(), lits=None)` is `tools/lexicon/lexicon.py:1587`. Its
  docstring says a line continues the one before it when its first token is in `conts`, an operator
  the lexer does not emit having been the last thing consumed. `parse_ts_source`
  (`tools/lexicon/lexicon.py:1739`) collects both facts at :1794-1796 and passes them at :1824.
- A probe run 2026-10-27 at a76dbde6 over `const s = path\n  .join(kit, "ratify.py");\nspawnSync(py,
  [s, slug]);\n` returned 4 from `read_ts_expr_end(toks, 3)`, the `join` word on line 2, and 9, the
  `;`, from the same call with the facts, which held `conts` `{4}`. The outputs are PINNED. The default
  stream was probed, because `strs` lands with `TOOL-dRankedPlan-48`; that stream's own facts are
  `TOOL-dRankedPlan-69`'s.

### The reading after this unit

| JavaScript | Binding of `s` | Answer for `[s, slug]` |
|---|---|---|
| `const s = path` then `  .join(kit, "ratify.py");` | lines 1 and 2, through the `;` | caller |
| the same with `"--exit"` last in the array | the same | not a caller |
| `const s = path.join(` then `  kit, "ratify.py");` | lines 1 and 2, unchanged | caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-chain`, `caller-js-bound-chain-exit` | `ratify.py` fixture plants | none |

No item mints a function. S1 passes two arguments to two existing calls.

### Rollout

Live at landing, at order 24. `TOOL-dRankedPlan-62`, `-65`, `-66`, `-69`, `-70`, `-71` and `-72`
share order 24 and write `tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced
inside that step, this unit before units 69, 70 and 71, which consume from it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2

### Alternatives rejected

- **Have `read_ts_expr_end` collect the facts itself.** It receives tokens and never the source, so it
  cannot, and changing its signature moves `parse_ts_source`'s call for one new caller.
- **Wrap the scan and its two containers in a helper in the shared block.** The facts are two
  arguments and no logic; the call is the reuse, and a wrapper adds a third name to the block for it.

## 5. Production-readiness checklist

- security — narrows: a JS binding continued by an operator the lexer drops is read whole by the
  deny-by-default ban.
- perf / scale — the same single scan, now filling one set and one dict.
- error / empty / loading states — unchanged: a declaration with no end runs to `len(toks)`, which
  fails closed.
- observability — the refusal names the file and the array's first line.
- risks — the facts only lengthen a binding where JavaScript continues the expression, so a wrong
  continuation holds more tokens and fails closed.
- testing — the two plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-chain` runs, the check exits 1
  naming the planted `.js` file.
  Red when: the extent is read without `conts`, so the binding ends at `path` on line 1.
- **AC2** — When the plant `caller-js-bound-chain-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a continued binding's `--exit` call is refused.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 · `caller-js-bound-chain` and its `--exit` twin, staged by unit 63 S1's two-argument `read_ts_expr_end` call, which reddens AC1 and leaves AC2 green · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 1 (HIGH,
  item H1, shared with findings 8, 16 and 22), repairing `TOOL-dRankedPlan-63`.

## 10. Reuse audit

The seams reused are `scan_ts_tokens`'s `conts` and `lits` containers (`tools/lexicon/lexicon.py:950`)
and `read_ts_expr_end`'s two fact parameters (`tools/lexicon/lexicon.py:1587`), passed exactly as
`parse_ts_source` passes them at :1824. `calls` is omitted because no JavaScript reader here asks a
call from a grouping parenthesis. `python tools/codebase-map/reuse_lookup.py "pass the lexer
continuation facts to the expression end reader"`, run 2026-10-27, ranked name stems only (`read`,
`read_text`, `read_conf`), none of which reads JavaScript, so the map's probe missed the reader and
the source read found it. The recall query returned this audit's H1 item and units 63 and 64, and
they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when a line continues after an operator the lexer drops" --terms "read_ts_expr_end conts lits scan_ts_tokens strs continuation ASI binding declarator caller ratify"`

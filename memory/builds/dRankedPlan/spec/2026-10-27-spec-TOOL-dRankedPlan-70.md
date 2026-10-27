# TOOL-dRankedPlan-70 — every expression-end call of the JavaScript reader passes the lexer's facts, each declarator's included

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md) | research | TOOL-dRankedPlan-68 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 |
| [2026-10-27-build-TOOL-dRankedPlan-70-deviation-701.md](../build/2026-10-27-build-TOOL-dRankedPlan-70-deviation-701.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md) | research | TOOL-dRankedPlan-68 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 16 at HIGH**, item **H1**, which it shares with findings 1, 8 and 22. The reuse lens found
that `read_ts_expr_end` is reused without the two arguments its existing caller passes, and that
`TOOL-dRankedPlan-64` S1 inherits the defect: each later declarator ends "at its own
`read_ts_expr_end`", a second call of the same reader. `TOOL-dRankedPlan-68` passes the facts at unit
63's call only, so `const a = 1, s = base ||` then `  path.join(kit, "ratify.py");` still binds `s`
to `base` and the call passes the deny-by-default ban. This unit makes every call of the reader in
the JavaScript reader pass the facts, the declarator's call included, and checks the class over the
file. Finding 1 is `TOOL-dRankedPlan-68`'s, finding 8 `TOOL-dRankedPlan-69`'s and finding 22
`TOOL-dRankedPlan-71`'s. This unit repairs `TOOL-dRankedPlan-64`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The declarator's call. `TOOL-dRankedPlan-64` S1's per-declarator extent becomes
  `read_ts_expr_end(toks, k, c, l)`, over `TOOL-dRankedPlan-68` S1's `c` and `l`. This supersedes unit
  64 S1's "to its own `read_ts_expr_end`" as a call with no facts. Observed by AC1.
- **S2** — The class. Every call of `read_ts_expr_end` in `tools/loop/ratify.py` passes four
  arguments, so every reading of a JavaScript extent carries the facts. Observed by AC2.
- **S3** — The plant. `caller-js-bound-multi-decl-or` joins `ratify.py --fixture --plant <case>` in
  its own scratch repository laid out from `TOOL-dRankedPlan-30`'s anchors. It plants a `.js` file
  holding `const a = 1, s = base ||`, then `  path.join(kit, "ratify.py");`, then `spawnSync(py, [s,
  slug]);`, and it is refused with exit 1. Observed by AC1.

## 3. Non-goals (OUT)

- Which `,` opens a declarator: `TOOL-dRankedPlan-72`, item H2.
- The facts themselves and unit 63's call: `TOOL-dRankedPlan-68` and `TOOL-dRankedPlan-69`.
- A spec-audit check that a reused seam is called as its existing caller calls it: the audit's
  left-shift gate, a check over the spec corpus that the close's left-shift step owns.

### Edges

- **consumes-from** `TOOL-dRankedPlan-64` — S1's per-declarator extent call, which S1 gives the facts; without it no later declarator is bound
- **consumes-from** `TOOL-dRankedPlan-68` — S1's `c` and `l` from the reader's one scan; without them there are no facts to pass
- **hands-off** `TOOL-dRankedPlan-78` — S2's four-argument class, which that unit states as a predicate counting every call's arguments (spec audit of units 68 to 77, id 16)
- **hands-off** `TOOL-dRankedPlan-79` — S2's observation and AC2, which that unit moves onto a loop selftest arm; carry S2 of that unit into this unit's pass (spec audit of units 68 to 77, id 1)
- **hands-off** `TOOL-dRankedPlan-81` — §3, into which that unit's item for finding 4 carries the hands-off edge back from unit 72; carry S4 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-64` S1 writes "whose tokens run from the token after that `=` to its own
  `read_ts_expr_end`", and its §4 Evidence probes the two-argument call.
- A probe run 2026-10-27 at a76dbde6 over `const a = 1, s = base ||\n  path.join(kit,
  "ratify.py");\nspawnSync(py, [s, slug]);\n` returned 8 from `read_ts_expr_end(toks, 7)`, the `path`
  word on line 2, and 14, the `;`, with the facts, which held `conts` `{8}`. The outputs are PINNED.

### The reading after this unit

| JavaScript | Binding of `s` | Answer for `[s, slug]` |
|---|---|---|
| `const a = 1, s = base \|\|` then `  path.join(kit, "ratify.py");` | `base` through the `;` | caller |
| `const a = 1, s = path.join(kit, "ratify.py");` | the call, unchanged | caller |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-multi-decl-or` | `ratify.py` fixture plant | none |

No item mints a function.

### Rollout

Live at landing, at order 24, after `TOOL-dRankedPlan-68` inside that step, because it reads that
unit's facts. Units 62, 65, 66, 68, 69, 71 and 72 share the order and write `tools/loop/ratify.py`,
so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Fold the declarator's call into unit 68's.** Unit 68 owns unit 63's call; a second unit claiming
  unit 64's call keeps one mechanism per spec, and S2 is what holds the two together.
- **Default the reader's facts to the last scan's.** Module state carried between calls makes one
  file's reading depend on the file read before it.

## 5. Production-readiness checklist

- security — narrows: a later declarator continued by a dropped operator is read whole.
- perf / scale — none: the same call with two more arguments.
- error / empty / loading states — unchanged.
- observability — the refusal names the file and the array's first line.
- risks — as `TOOL-dRankedPlan-68`: a wrong continuation fails closed.
- testing — the plant of AC1 and the grep of AC2.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-js-bound-multi-decl-or` runs, the check
  exits 1 naming the planted `.js` file.
  Red when: the declarator's extent is read without the facts, so `s` binds `base` alone.
- **AC2** — When `grep -cE 'read_ts_expr_end\(toks, [a-z_]+\)'` runs over the loop kit's `ratify.py` at
  this unit's tip, it prints 0, and `grep -c 'read_ts_expr_end(toks, '` prints at least 1.
  Red when: any extent call of the JavaScript reader passes two arguments.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 · `caller-js-bound-multi-decl-or`, staged by unit 64 S1's two-argument declarator call · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 16
  (HIGH, item H1, shared with findings 1, 8 and 22), repairing `TOOL-dRankedPlan-64`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-78`, the hands-off edge to `TOOL-dRankedPlan-79` and the hands-off edge to `TOOL-dRankedPlan-81`, each the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam reused is `read_ts_expr_end` (`tools/lexicon/lexicon.py:1587`) with the facts its existing
caller `parse_ts_source` passes at :1824, now at every call in the JavaScript reader. `python
tools/codebase-map/reuse_lookup.py "pass the lexer continuation facts to the expression end
reader"`, run 2026-10-27, ranked name stems only (`read`, `read_text`, `read_conf`), so no seam fits
beyond the reader and unit 68's scan. The recall query returned this audit's H1 item and units 63 and
64, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when a line continues after an operator the lexer drops" --terms "read_ts_expr_end conts lits scan_ts_tokens strs continuation ASI binding declarator caller ratify"`

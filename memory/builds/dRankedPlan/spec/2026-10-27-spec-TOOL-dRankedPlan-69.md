# TOOL-dRankedPlan-69 — a `str` token of the `strs` stream carries the continuation facts its silent literal carried

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 24 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-69-deviation-691.md](../build/2026-10-27-build-TOOL-dRankedPlan-69-deviation-691.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 8 at HIGH**, item **H1**, which it shares with findings 1, 16 and 22. `TOOL-dRankedPlan-63`
grounds its extent on the default token stream, while the reader runs on the `strs` stream of
`TOOL-dRankedPlan-48`, whose S1 says a string is emitted as a `str` token and says nothing of the
two facts `read_ts_expr_end` reads. Today a literal is silent: the string branch clears `pend` and
records `lits` at the index the next token takes. Emitted naively, a `str` token opening a line
after a silent `+` is in neither `conts` nor `lits`, so `const s = kit +` then `  "/ratify.py";`
binds `s` to `kit` alone and the call passes the deny-by-default ban. This unit pins where a `str`
token puts both facts, so the `strs` stream reads like the default one. Finding 1 is
`TOOL-dRankedPlan-68`'s, finding 16 `TOOL-dRankedPlan-70`'s and finding 22 `TOOL-dRankedPlan-71`'s.
This unit repairs `TOOL-dRankedPlan-63`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The facts of a `str` token. In `scan_ts_tokens`'s string branch, under `strs=True`, the
  `str` token of `TOOL-dRankedPlan-48` S1 is emitted through `add_token`, at the line the literal
  opened on, while `pend` still holds its value from before the literal, so a `str` token that opens a line after a silent operator is in
  `conts`. `pend` then clears, and `lits` records the line the literal ended on at `len(toks)` after
  the emission, which is the index of the token after the `str` token. With `strs=False` the stream,
  `conts` and `lits` are byte for byte what they are today. This completes unit 48 S1, which states
  neither fact. Observed by AC1, AC2 and AC3.
- **S2** — The copies. Every copy of the block carries S1 byte for byte, the set `TOOL-dRankedPlan-48`
  S2 names. Observed by AC4.
- **S3** — The plant. `caller-js-bound-concat` joins `ratify.py --fixture --plant <case>` in its own
  scratch repository laid out from `TOOL-dRankedPlan-30`'s anchors. It plants a `.js` file holding
  `const s = kit +`, then `  "/ratify.py";`, then `spawnSync(py, [s, slug]);`, and it is refused with
  exit 1. Observed by AC5.

## 3. Non-goals (OUT)

- Passing the facts to the extent call: `TOOL-dRankedPlan-68`, the same item.
- A change to `read_ts_expr_end`. It reads the facts as it does today.
- A template literal. It stays silent and unread, unit 48's ceiling.

### Edges

- **consumes-from** `TOOL-dRankedPlan-48` — S1's `strs` mode and S2's copy set, which S1 and S2 complete; without them there is no `str` token
- **consumes-from** `TOOL-dRankedPlan-68` — S1's facts handed to the extent call; without them the marks S1 places are never read
- **hands-off** `TOOL-dRankedPlan-77` — S1's `lits` rule, which that unit's item for finding 9 cites in unit 63's §4 Evidence and §5
- **hands-off** `TOOL-dRankedPlan-81` — AC4, which that unit's items for findings 6 and 23 correct; carry S16 and S17 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- `scan_ts_tokens`'s string branch is `tools/lexicon/lexicon.py:1251-1259` at a76dbde6. It sets `pend
  = False` and then records `lits[len(toks)] = line` without emitting. `add_token`
  (`tools/lexicon/lexicon.py:1026-1037`) marks `conts` only when `pend` is set as it emits.
- `read_ts_expr_end` (`tools/lexicon/lexicon.py:1613-1617`) decides a line break at token `j` by
  `lits[j]` when `j` is in `lits`, and otherwise by the text of token `j-1`, whatever its kind.
- A probe run 2026-10-27 at a76dbde6 over the default stream of `const s = kit +\n
  "/ratify.py";\n…` printed `kit` then `;` with `conts` empty and `lits` `{4: 2}`, and
  `read_ts_expr_end` returned 4, the `;`. The outputs are PINNED. In the `strs` stream the `str` token
  takes index 4, so without S1 the extent ends at 4 before it.

### The reading after this unit, `strs=True`

| JavaScript | `str` token | Facts | Extent from `kit` |
|---|---|---|---|
| `const s = kit +` then `  "/ratify.py";` | index 4, line 2 | 4 in `conts`, `lits` `{5: 2}` | through the `;` |
| `const a = f()` then `'x';` | index 6, line 2 | 6 in neither, `lits` `{7: 2}` | ends at 6 |
| `const a = ","` then `b;` | index 3, line 1 | `lits` `{4: 1}` | ends at 4 |

The third row is why `lits` keys the token after the `str` token: the reader then decides that break
by the record and never by the text `,`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-js-bound-concat` | `ratify.py` fixture plant | none |

No item mints a function. S1 orders two statements of an existing branch.

### Rollout

Live at landing, at order 24, after `TOOL-dRankedPlan-68` inside that step, because the plant needs
the facts passed. Units 62, 65, 66, 68, 70, 71 and 72 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it. The kits whose
shipped bytes move here take their version bump from `govkit.py mint` at the lander.

### Files touched (estimate)

- `tools/lib/extract_code.py`: S1
- `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`,
  `tools/memory-tree/extract_code.py`, `tools/loop/extract_code.py`: S2, the re-synced copies
- `tools/loop/ratify.py`: S3

### Alternatives rejected

- **Key `lits` at the `str` token's own index.** A `str` token opening a line after an operand is then
  in `lits` with its own line, so the reader continues the statement, and the token after a `str`
  ending a line falls back to the `str` token's text: a string `","` reads as a continuing op.
- **Mark `conts` from the reader instead.** The reader sees tokens only, and `pend` is lexer state.

## 5. Production-readiness checklist

- security — narrows: a JS binding continued by a string after a silent operator is read whole.
- perf / scale — none: two statements reordered in one branch.
- error / empty / loading states — unchanged.
- observability — the refusal names the file and the array's first line.
- risks — the default stream must not move; AC1 compares it with the pinned probe.
- testing — the probes of AC1 to AC3, the parity of AC4 and the plant of AC5.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a probe calls `scan_ts_tokens` from the loop kit's `extract_code.py` on `const s =
  kit +\n  "/ratify.py";\n` with `strs=True` and both containers, index 4 is `("str", "/ratify.py",
  2)` and is in `conts`, `lits` is `{5: 2}`, and `read_ts_expr_end(toks, 3, c, l)` returns 5; with
  `strs=False` the stream, `conts` and `lits` equal the §4 probe's.
  Red when: the `str` token is emitted after `pend` clears, so the extent ends at 4.
- **AC2** — When the same probe runs on `const a = f()\n'x';\n`, `read_ts_expr_end(toks, 3, c, l)`
  returns 6, the `str` token.
  Red when: `lits` keys the `str` token's own index, so the statement swallows line 2.
- **AC3** — When the same probe runs on `const a = ","\nb;\n`, `read_ts_expr_end(toks, 3, c, l)`
  returns 4, the `b` word.
  Red when: the token after the `str` token is not in `lits`, so the text `,` reads as a continuing op.
- **AC4** — When `git grep -l "^# >>> extract_code" -- '*.py'` runs at this unit's tip, `cmp` of each
  listed copy's block with the canonical block reports no difference.
  Red when: a copy lacks S1's order.
- **AC5** — When `python ratify.py --fixture --plant caller-js-bound-concat` runs, the check exits 1
  naming the planted `.js` file.
  Red when: the `str` token on line 2 is outside `conts`, so `s` binds `kit` alone.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `build-index selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC5 · `caller-js-bound-concat`, staged by an emission placed after `pend` clears · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 8 (HIGH,
  item H1, shared with findings 1, 16 and 22), repairing `TOOL-dRankedPlan-63`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-81`, the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `scan_ts_tokens`'s string branch (`tools/lexicon/lexicon.py:1251-1259`) and its
`add_token` (:1026), whose `conts` mark and `lits` record S1 orders for the `str` token
`TOOL-dRankedPlan-48` adds; `read_ts_expr_end` reads both unchanged. `python
tools/codebase-map/reuse_lookup.py "pass the lexer continuation facts to the expression end
reader"`, run 2026-10-27, ranked name stems only (`read`, `read_text`, `read_conf`), none of which
lexes JavaScript, so no seam fits beyond the lexer's own branch. The recall query returned this
audit's H1 item, units 63 and 64, and TOOL-aGradedDialect-10's record of why `lits` exists, and they
agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "where does a javascript binding end when a line continues after an operator the lexer drops" --terms "read_ts_expr_end conts lits scan_ts_tokens strs continuation ASI binding declarator caller ratify"`

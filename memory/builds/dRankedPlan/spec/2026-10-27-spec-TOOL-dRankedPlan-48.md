# TOOL-dRankedPlan-48 — the TypeScript tokenizer emits string literal text behind an opt-in keyword, so the JavaScript reader reads argv arrays

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 21 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-48-deviation-481.md](../build/2026-10-27-build-TOOL-dRankedPlan-48-deviation-481.md) | deviation | — |
| [2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) | spec-audit | TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-49 TOOL-dRankedPlan-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 8 at HIGH**, item **H2**. `TOOL-dRankedPlan-45` S16 has `read_js_callers` read array literals
from `scan_ts_tokens`, which it says "already emits" what the reader needs. It does not: the tokenizer
consumes a string literal without emitting it, so `["python3",\n "ratify.py", slug]` yields `[ , ,
slug ]` and no element can be compared with `ratify.py`. Built as written, every JavaScript invocation
passes the deny-by-default ban, and unit 45 AC11 cannot go green. This unit adds an opt-in keyword to
`scan_ts_tokens` that emits each string literal's text, leaves the default stream unchanged, and
points `read_js_callers` at it. It repairs `TOOL-dRankedPlan-45`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The string mode. `scan_ts_tokens(src, jsx=False, calls=None, conts=None, lits=None,
  strs=False)` in the canonical block of `tools/lib/extract_code.py` (TOOL-dTotalRecall-13 S1) gains
  the keyword `strs`. With `strs=False` the token stream is byte for byte what it is today. With
  `strs=True`, each single- or double-quoted string literal in code, outside a suppressed span, is
  emitted as `("str", <its text between the quotes, escapes kept>, <the line it opened on>)`. The
  docstring's kind sentence reads `word`, `op` or `jsx`, and also `str` under `strs=True`. No current
  caller passes `strs`, and `read_js_callers` passes none of `calls`, `conts` or `lits`. Observed by
  AC1.
- **S2** — The copies. Every copy of the block carries S1 byte for byte, as TOOL-dTotalRecall-13 S3's
  parity row holds them. The copy set is whatever `git grep -l "^# >>> extract_code" -- '*.py'` lists
  at the pass, which the parents and `TOOL-dRankedPlan-41` S2 make five. Observed by AC3.
- **S3** — The reader re-pointed. `read_js_callers` (`TOOL-dRankedPlan-32` S3, `TOOL-dRankedPlan-45`
  S16) calls `scan_ts_tokens(text, strs=True)` from the loop kit's `extract_code.py`. An array is the
  span from a `[` op to its matching `]` op, and an element is the run of tokens between `[` or `,`
  and the next `,` or `]` at that depth. An element names `ratify.py` when one of its `str` tokens
  ends in `ratify.py`, and the array is a caller unless one of its `str` tokens is in
  `RATIFY_MODE_FLAGS`. This supersedes unit 45 S16's "which already emits `[`, `]` and `,`" as the
  account of where the element text comes from. Observed by AC2.

## 3. Non-goals (OUT)

- A template literal element, such as `` `${kit}/ratify.py` ``. Its text stays consumed, and the form is
  unread, the reader's ceiling in §4. No tracked `*.js` file invokes a kit's Python script at base
  (`TOOL-dRankedPlan-32` S3).
- The shell tokenizer: `TOOL-dRankedPlan-41` and `TOOL-dRankedPlan-52`'s items.
- Moving the tokenizer. Its home is TOOL-dTotalRecall-13's, read here and extended by one keyword.

### Edges

- **consumes-from** `TOOL-dRankedPlan-45` — S16's `read_js_callers` reading and the `caller-js-argv` plant, whose source of element text S3 restates; without them there is no JavaScript reader to feed
- **consumes-from** external — dTotalRecall's `tools/lib/extract_code.py`, its `scan_ts_tokens` and its parity row (TOOL-dTotalRecall-13 S1, S3), built before this build run
- **hands-off** `TOOL-dRankedPlan-60` — S1's `str` tokens and S3's array elements, over which that unit resolves a same-file binding (spec audit of units 46 to 52, id 31)
- **hands-off** `TOOL-dRankedPlan-62` — §4's probe and §7, which that unit's items for findings 11 and 24 correct; carry S6 and S20 of that unit into this unit's pass (spec audit of units 46 to 52)

## 4. Design

### Evidence

- `scan_ts_tokens` (`tools/lexicon/lexicon.py:950` at base) consumes a code string at :1251-1259, with
  `read_string` and no `add_token`, and records only the index the next token takes in `lits`. Its
  docstring lists string literals among what it "CONSUMES WITHOUT EMITTING".
- A probe run 2026-10-27 at base 0689e7fa, `scan_ts_tokens('const a = ["python3",\n  "ratify.py",
  slug];\n')`, printed `('op','[',1) ('op',',',1) ('op',',',2) ('word','slug',2) ('op',']',2)` among
  its tokens, and no string. The output is PINNED.
- TOOL-dTotalRecall-13 S1 moves `scan_ts_tokens` into the block, and TOOL-dTotalRecall-8 adds the
  memory-tree kit's copy, `tools/memory-tree/extract_code.py`.

### The reading after this unit

| JavaScript | Element texts | Answer |
|---|---|---|
| `[py, "ratify.py", slug]` | `ratify.py` | caller |
| `["python3",\n "ratify.py", slug]` | `python3`, `ratify.py` | caller |
| `[py, "ratify.py", slug, "--exit"]` | `ratify.py`, `--exit` | not a caller |
| `` [py, `${kit}/ratify.py`, slug] `` | none | unread, the ceiling |

The upgrade is a template literal's text segments emitted under the same keyword, once the tree writes
a JavaScript call to a kit script.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `strs` | keyword parameter of `scan_ts_tokens` | none |
| `str` | token kind under `strs=True` | none |

### Rollout

Live at landing, at order 21. Units 46 to 49 share order 21 and all write `tools/loop/ratify.py`, so
by BUILD-METHOD M6 clause 1 they are sequenced inside that step. The kits whose shipped bytes move here
take their version bump from `govkit.py mint` at the lander.

### Files touched (estimate)

- `tools/lib/extract_code.py`: S1
- `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`,
  `tools/memory-tree/extract_code.py`, `tools/loop/extract_code.py`: S2, the re-synced copies
- `tools/loop/ratify.py`: S3

### Alternatives rejected

- **A string scanner inside `ratify.py`.** It would be a second, weaker tokenizer beside the one the
  lexicon is tested against, the defect `TOOL-dRankedPlan-41` §4 rejected for shell.
- **Emit strings by default.** The stream is a contract of `parse_ts_defs` and the indices in
  `calls`, `conts` and `lits`, so every current caller would move.

## 5. Production-readiness checklist

- security — narrows: a JavaScript argv array that names `ratify.py` is read by the deny-by-default
  ban.
- perf / scale — one tokenizer pass per `*.js` file the check reads.
- error / empty / loading states — a `SyntaxError` exits 2, as unit 45 S16 states.
- observability — the refusal names the file and the array's first line.
- risks — the default stream is a contract of the lexicon and the map. S1 leaves it unchanged, and
  their selftests read it.
- testing — AC1's token probe, the `caller-js-argv` plant, and the parity row over the copies.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a probe calls `scan_ts_tokens` from the loop kit's `extract_code.py` on
  `const a = ["python3",\n  "ratify.py", slug];\n` with `strs=True`, the stream holds `("str",
  "python3", 1)` and `("str", "ratify.py", 2)`, and without the keyword it equals the §4 probe's
  output.
  Red when: a string is not emitted in string mode, or the default stream changes.
- **AC2** — When `python ratify.py --fixture --plant caller-js-argv` runs, its `.js` file holding
  `["python3", "ratify.py", slug]` across two lines is refused with exit 1.
  Red when: the JavaScript reader misses a string element naming `ratify.py`.
- **AC3** — When `git grep -l "^# >>> extract_code" -- '*.py'` runs at this unit's tip, `cmp` of each
  listed copy's block with the canonical block reports no difference.
  Red when: a copy lacks the `strs` keyword.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `python resolver (behaviour + inline parity + idiom ban)` · `build-index selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC2 · the `caller-js-argv` plant, staged by a reader that calls `scan_ts_tokens` without `strs` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 8 (HIGH,
  item H2), repairing `TOOL-dRankedPlan-45`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-60`, the hands-off edge to `TOOL-dRankedPlan-62`, each the reciprocal of that promoted unit's own edge (spec audit of units 46 to 52, `reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `scan_ts_tokens`, today `tools/lexicon/lexicon.py:950` and, once
TOOL-dTotalRecall-13 lands, the canonical block in `tools/lib/extract_code.py` with one inline copy per
kit. It gains one opt-in keyword, as `TOOL-dRankedPlan-41` S1 extends `scan_shell_tokens`, so its
current callers keep their stream. `python tools/codebase-map/reuse_lookup.py "find which command a
shell heredoc or wrapper function runs and read its script argument"` ranked name stems only (`read`,
`run`, `run_git`), and no candidate emits string text, so no seam fits beyond the block. The recall
query returned units 38, 40 and 41 and TOOL-dTotalRecall-13's scout row, and they agree with the
source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`

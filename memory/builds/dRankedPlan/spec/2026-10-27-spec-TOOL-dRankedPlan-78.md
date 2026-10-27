# TOOL-dRankedPlan-78 — the four-argument class of the JavaScript reader's extent calls is a predicate that counts arguments over every call

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-78-deviation-781.md](../build/2026-10-27-build-TOOL-dRankedPlan-78-deviation-781.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-78-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-78-promoted-fix-return.md) | research | TOOL-dRankedPlan-79 TOOL-dRankedPlan-81 |
| [2026-10-27-prompt-TOOL-dRankedPlan-78-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-78-1-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-78-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-78-promoted-fix-brief.md) | research | TOOL-dRankedPlan-79 TOOL-dRankedPlan-81 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 68 to 77
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`) confirmed
**finding 16 at HIGH**, item **H1**, which it shares with finding 1. `TOOL-dRankedPlan-70` S2 says
every `read_ts_expr_end` call in `tools/loop/ratify.py` passes four arguments, and its AC2 greps
`read_ts_expr_end\(toks, [a-z_]+\)`. That regex matches only a two-argument call whose index is one
bare lowercase name, so `(toks, eq + 1)`, `(toks, k, c)` and `(toks, k, conts=c)` all leave it at 0.
The facts are optional in the reader's signature (`tools/lexicon/lexicon.py:1587`), so each of those
runs, drops facts, and the deny-by-default ban passes while AC2 certifies the class. Its second clause
asks for at least one call and pins no count. This unit states the class as a predicate that counts
every call's arguments, refuses every other reference to the reader, and reports how many calls it
read, so a reading that matched nothing cannot pass. Finding 1 is `TOOL-dRankedPlan-79`'s, which
runs this predicate at every close. This unit repairs `TOOL-dRankedPlan-70`, so it sits one order
above it.

## 2. Scope (IN)

- **S1** — The predicate. `read_extent_call_arities(src)` in `tools/loop/selftest.py` parses `src`
  with the stdlib `ast` module and returns `(calls, misses)`. `calls` counts every `ast.Call` whose
  callee is the `Name` or `Attribute` `read_ts_expr_end`. `misses` is the sorted list of line numbers
  of every such call whose `len(args) + len(keywords)` is not 4 or that passes a `*` or `**` argument,
  of every other `Name` or `Attribute` reference to `read_ts_expr_end`, and of every import of that
  name under an `as` alias. It counts by argument and never by spelling, so the index expression, the
  first argument's name and a call wrapped across lines do not move it. This supersedes
  `TOOL-dRankedPlan-70` AC2's regex as the statement of unit 70 S2's class. Observed by AC1 to AC3.
- **S2** — The floor. A reading whose `calls` is 0 is a failure, never a pass. At
  `TOOL-dRankedPlan-70`'s tip the floor is 2: unit 63 S1's binding extent, given the facts by
  `TOOL-dRankedPlan-68` S1, and unit 64 S1's per-declarator extent, given them by unit 70 S1.
  `TOOL-dRankedPlan-71` S1 moves both calls inside `read_js_binding_end`, so the number after it is
  the builder's spelling of that loop, and only the zero floor holds across every later tip. Observed
  by AC3.

## 3. Non-goals (OUT)

- Running the predicate at the close over `tools/loop/ratify.py`: `TOOL-dRankedPlan-79`, the same
  item.
- Making `conts` and `lits` required in `read_ts_expr_end`'s signature: §4 Alternatives rejected.
- Which spellings of unit 70's AC2 the regex misses, item M1: `TOOL-dRankedPlan-81`'s items for
  findings 10 and 14 observe this predicate over them.

### Edges

- **consumes-from** `TOOL-dRankedPlan-70` — S2's four-argument class, which S1 states as a predicate; without it the predicate checks a rule nobody wrote
- **hands-off** `TOOL-dRankedPlan-79` — S1's `read_extent_call_arities` and S2's floor, which that unit runs over `tools/loop/ratify.py` at every close (spec audit of units 68 to 77, id 1)
- **hands-off** `TOOL-dRankedPlan-81` — S1's predicate, over whose misses that unit's items for findings 10 and 14 plant the spellings unit 70's regex let through

## 4. Design

### Evidence

- `read_ts_expr_end(toks: list, k: int, conts=frozenset(), lits=None)` is
  `tools/lexicon/lexicon.py:1587` at 753f09a8, so a call that omits either fact runs without error.
  `git grep -n read_ts_expr_end -- ':!memory/builds'` printed one call outside the loop kit,
  `parse_ts_source`'s at :1824, which passes all four.
- A prototype of S1, run 2026-10-27 over a text holding an `import` of the name, one four-argument
  call, `(toks, eq + 1)`, `(toks, k, c)`, `(toks, k, conts=c)`, `(toks,` then `eq + 1)` across two
  lines, a bare alias `f = read_ts_expr_end` and `(toks, k, conts=c, lits=l)`, returned `(6, [3, 4,
  5, 6, 8])`: six calls, the four short ones and the alias missed, and the keyword form with both
  facts passed. The output is PINNED.
- `tools/loop/` is absent at base 0689e7fa, so the predicate's input exists only once the loop kit and
  units 63, 64, 68 and 70 have built.

### Data model

```
read_extent_call_arities(src: str) -> tuple[int, list[int]]
    # (calls to read_ts_expr_end, sorted line numbers of every miss)
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_extent_call_arities` | function, `tools/loop/selftest.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest read_extent_call_arities --as py.function` answered OK |

The minted function is rendered into `memory/map/generated/symbols.json` by `gen_map.py --write`, as
`TOOL-dRankedPlan-61` S1 states.

### Rollout

Live at landing, at order 25, the order after `TOOL-dRankedPlan-70`'s. `TOOL-dRankedPlan-79` writes
the same file and consumes from this unit, so by BUILD-METHOD M6 clause 1 it follows this unit inside
order 25.

### Files touched (estimate)

- `tools/loop/selftest.py`: S1, S2
- `memory/map/generated/symbols.json`: the render of S1's function

### Alternatives rejected

- **Make `conts` and `lits` required in `read_ts_expr_end`.** It is the root of the optional facts, and
  it moves the lexicon kit's signature for one caller outside it. A call that drops a fact would then
  raise `TypeError`, whose uncaught exit code is 1, the refusal code, so a refused plant could not tell
  the crash from the refusal.
- **A sharper regex.** Every grep over source spells a call one way. Keyword facts, an expression
  index and a wrapped call each need their own alternative, and the audit names three.
- **Pin an exact call count across every tip.** `TOOL-dRankedPlan-71` S1 leaves the count to how its
  builder writes the loop, so only the zero floor is derivable after it.

## 5. Production-readiness checklist

- security — narrows: an extent call that drops a fact is found, whatever its spelling, so a
  continued binding cannot be read short unseen.
- perf / scale — one `ast.parse` of `tools/loop/ratify.py`, milliseconds.
- error / empty / loading states — a source `ast` cannot parse raises `SyntaxError`, which fails the
  run loudly; a source with no call returns `calls` 0, which S2 makes a failure.
- observability — each miss is a line number of `tools/loop/ratify.py`.
- risks — a call through a name bound at run time, such as `getattr`, is not seen; no unit writes one.
- testing — the probes of AC1 to AC3.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a probe imports `read_extent_call_arities` alone from the loop kit's self-test module,
  running no case of it, and calls it on the eight-line text of §4 Evidence planted as a string, it
  returns `(6, [3, 4, 5, 6, 8])`.
  Red when: arguments are counted by a pattern over the text, so the keyword or wrapped call is missed.
  figure: PINNED from the 2026-10-27 prototype.
- **AC2** — When the same probe calls it on `x = read_ts_expr_end(toks, k, c, l)`, it returns `(1,
  [])`, and on `x = read_ts_expr_end(toks, k, *f)` it returns `(1, [1])`.
  Red when: a four-argument call is missed, or a starred argument is counted as one argument.
- **AC3** — When the same probe calls it on the text of the loop kit's `ratify.py` at this unit's tip,
  it returns a `calls` of at least 1 and an empty `misses`, and on `x = 1` it returns `(0, [])`.
  Red when: the reading over the loop kit's `ratify.py` misses a call, or finds none.
  figure: the floor of 2 holds at `TOOL-dRankedPlan-70`'s tip only; DERIVED from units 63, 64 and 70.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`loop selftest` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/selftest.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

This unit adds no suite arm: S1 is a function the suite does not yet call, and AC1 to AC3 observe it
directly. The arm that runs it at every close is `TOOL-dRankedPlan-79` S1's
`extent-calls-carry-facts`, declared on that spec's own §7 arm line.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 68 to 77, finding 16
  (HIGH, item H1, shared with finding 1), repairing `TOOL-dRankedPlan-70`.

## 10. Reuse audit

The seam reused is the stdlib `ast` module, which counts a call's arguments as the interpreter will
bind them; the property it checks is unit 70 S2's, over the calls units 63, 64, 68, 70 and 71 write.
`python tools/codebase-map/reuse_lookup.py "count the arguments of every call to a function in a
python source file"`, run 2026-10-27, ranked `counts`, `resolve_python`, `measure_typed_counts` and
`python_symbols` (`tools/codebase-map/map_lib.py`), which lists definitions and counts no call's
arguments, so no existing seam fits and S1 is new. The recall query returned units 68, 70 and 72 and
the H1 item of the audit of units 63 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how is every extent call of the javascript reader checked to pass the lexer facts" --terms "read_ts_expr_end conts lits arity four arguments ast call class predicate ratify selftest"`

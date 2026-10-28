# TOOL-dRankedPlan-79 — the loop selftest re-checks the four-argument class over the JavaScript reader at every close

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-78-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-78-promoted-fix-return.md) | research | TOOL-dRankedPlan-78 TOOL-dRankedPlan-81 |
| [2026-10-27-build-TOOL-dRankedPlan-79-deviation-791.md](../build/2026-10-27-build-TOOL-dRankedPlan-79-deviation-791.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-78-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-78-promoted-fix-brief.md) | research | TOOL-dRankedPlan-78 TOOL-dRankedPlan-81 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 68 to 77
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`) confirmed
**finding 1 at HIGH**, item **H1**, which it shares with finding 16. Besides the regex finding 16
names, the coherence lens found that `TOOL-dRankedPlan-70` AC2 runs once, at unit 70's tip, and is no
gate. Its `New arm:` line covers AC1 alone. Units 71 and 72 rewrite the same calls later inside order
24, and `TOOL-dRankedPlan-80` rewrites the declarator walk at order 25, so none of them is checked
against unit 70 S2's class. This unit makes the class an arm of the loop selftest, so every close
re-reads `tools/loop/ratify.py` whatever unit last wrote it. Finding 16 is `TOOL-dRankedPlan-78`'s,
whose predicate this arm runs. This unit repairs `TOOL-dRankedPlan-70`, so it sits one order above
it.

## 2. Scope (IN)

- **S1** — The arm. `tools/loop/selftest.py` gains the case `extent-calls-carry-facts`. It reads the
  loop kit's `ratify.py` beside it, calls `TOOL-dRankedPlan-78` S1's `read_extent_call_arities` on its
  text, and fails, printing `extent-calls-carry-facts: <path>:<line>` for each miss, when `misses` is
  not empty or `calls` is 0. It passes printing `extent-calls-carry-facts: <calls> calls, 4 arguments
  each`. Observed by AC1 and AC2.
- **S2** — The record in unit 70. `TOOL-dRankedPlan-70` S2 is observed by this unit's arm and no
  longer by a grep at unit 70's tip: its "Observed by AC2" becomes "NOT OBSERVED in this unit:
  `TOOL-dRankedPlan-79`'s arm `extent-calls-carry-facts` observes it at every close", and AC2 is
  withdrawn. This supersedes unit 70 AC2 and the clause of S2 that names it. Unit 70 carries both into
  its pass. Observed by AC3.

## 3. Non-goals (OUT)

- The predicate itself: `TOOL-dRankedPlan-78`, the same item.
- A spec-audit check that a criterion observing an "every X" class enumerates X: the audit's left-shift
  gate, a check over the spec corpus that the close's left-shift step owns.
- Unit 70's AC1 and its plant: unchanged.

### Edges

- **consumes-from** `TOOL-dRankedPlan-78` — S1's `read_extent_call_arities` and S2's floor, which S1 runs; without them the arm has no predicate
- **consumes-from** `TOOL-dRankedPlan-70` — S2's class and AC2, which S2 moves onto this arm; without them there is no class to re-check

## 4. Design

### Evidence

- `TOOL-dRankedPlan-70` §7 reads `New arm: tools/loop/ratify.py · covers AC1 · …`, so AC2 is re-run by
  nothing after unit 70's pass.
- `TOOL-dRankedPlan-71` §4 Rollout orders it after units 68 and 70 inside order 24, and its S1 rewrites
  both `read_ts_expr_end` calls. `TOOL-dRankedPlan-72` §4 Rollout shares the order and writes the
  same declarator loop.
- `TOOL-dRankedPlan-9` S7 and `TOOL-dRankedPlan-22` S3 make `tools/loop/selftest.py` the runner of the
  loop kit's checks, inside the `loop selftest` leg once dDeclaredLoop's legs are in the manifest.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `extent-calls-carry-facts` | `tools/loop/selftest.py` case | none |

No item mints a function. S1 calls the function `TOOL-dRankedPlan-78` mints.

### Rollout

Live at landing, at order 25, after `TOOL-dRankedPlan-78` inside that step, because it calls that
unit's predicate and writes the same file. By BUILD-METHOD M6 clause 1 the two are sequenced.

### Files touched (estimate)

- `tools/loop/selftest.py`: S1

### Alternatives rejected

- **Keep the class as a criterion of unit 70 and re-run it from each later unit.** Every later unit
  that writes an extent call must then remember to, and the audit's finding is that one did not.
- **A `ratify.py --fixture` plant.** A plant lays out a scratch repository and runs the check over it;
  this arm reads the check's own source, which no plant does.

## 5. Production-readiness checklist

- security — narrows: a later rewrite that drops a fact from an extent call reds the selftest.
- perf / scale — one `ast.parse` per selftest run.
- error / empty / loading states — an absent `ratify.py` is a failure of the case, never a skip.
- observability — each miss prints the path and line.
- risks — the arm reds a correct build only if a unit adds a non-reader use of the name; none does.
- testing — the staged break of AC1, the green read of AC2 and the grep of AC3.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When a probe copies the loop kit's `ratify.py` to the run's scratch directory, appends
  `_x = read_ts_expr_end(toks, k, c)`, and calls the `extent-calls-carry-facts` case's function alone
  from the loop kit's self-test module on the copy, running no other case, the case fails and prints
  the appended line's number.
  Red when: the case reads a fixed list of call sites, or passes on a three-argument call.
- **AC2** — When the same probe calls the case on the loop kit's unmodified `ratify.py` at this unit's
  tip, it passes and prints `extent-calls-carry-facts:` with a call count of at least 1.
  Red when: a call written by units 63 to 72 drops a fact, or the case reads no call.
- **AC3** — When `grep -A3 '^- \*\*S2\*\*'` runs over unit 70's spec, piped to `grep -c
  'extent-calls-carry-facts'`, it prints at least 1, and `grep -c 'a-z_'` over the same spec prints 0.
  Red when: unit 70 S2 still names a tip-only grep as its observation.
  figure: PINNED 0 and 1 at 753f09a8.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/selftest.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/selftest.py · covers AC1 AC2 · the `extent-calls-carry-facts` case, staged by a three-argument `read_ts_expr_end(toks, k, c)` added to `tools/loop/ratify.py` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 68 to 77, finding 1 (HIGH,
  item H1, shared with finding 16), repairing `TOOL-dRankedPlan-70`.

## 10. Reuse audit

The seam extended is `tools/loop/selftest.py`, the loop kit's runner that `TOOL-dRankedPlan-9` S7 and
`TOOL-dRankedPlan-22` S3 already add checks to, and the predicate reused is `TOOL-dRankedPlan-78`'s.
`python tools/codebase-map/reuse_lookup.py "count the arguments of every call to a function in a
python source file"`, run 2026-10-27, ranked `counts`, `resolve_python`, `measure_typed_counts` and
`python_symbols`, none of which runs a check over a kit's own source, so no existing seam fits beyond
the selftest runner. The recall query returned units 68, 70 and 72 and the H1 item of the audit of
units 63 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how is every extent call of the javascript reader checked to pass the lexer facts" --terms "read_ts_expr_end conts lits arity four arguments ast call class predicate ratify selftest"`

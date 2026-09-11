---
slug: dMuffledSentinel
node: d
opened: 2026-09-11
streams: tooling
roster: TOOL
ids: TOOL-dMuffledSentinel-1
authorized-by: prompt
---

# dMuffledSentinel — hygiene check 21 read a parse that never ran as a clean corpus

## The problem this build exists to solve

Check 21 delegates its parse to `gen_build_index.py --print-bindings` and captured it with
`2>/dev/null || true`. Every other delegate in the engine fails on its exit status; this one threw
the status away. inCMS carries a forked generator that never gained the mode, so the call exited 2
there and all four population branches read an empty string. Measured over inCMS's 1531 records,
check 21 printed one line, from the one branch that does not read the parse.

## Expected improvements

- A parse that exits non-zero, or exits zero without its `N` row, fails check 21 by name.
- The refusal carries the delegate's own last lines, so an adopter sees the missing mode at once.
- The class is catalogued, so a review of any gate that delegates is asked about it.

## Detriments if this is not built

- Any adopter whose generator lacks the mode, or crashes on its corpus, keeps a check that cannot
  fail and reads as green.
- The engine keeps one delegate whose failure is silent, beside four that are not.

## Build-level rules

- **The adopter half is not here.** inCMS's forked generator gained the mode in its own repo, as
  `ARCH-dMuffledSentinel-1`. This build changes only what the engine does when a generator cannot
  answer, and that change is right for every adopter, forked or not.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dMuffledSentinel-1` | 1 | check 21 refuses a bindings parse that did not complete |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-09-11 · streams tooling
ids TOOL-dMuffledSentinel-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMuffledSentinel-1 — check 21 refuses a bindings parse that did not complete](spec/2026-09-11-spec-TOOL-dMuffledSentinel-1.md) | — | 1 | CLOSED | rev-2 | 2026-09-12 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dMuffledSentinel-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

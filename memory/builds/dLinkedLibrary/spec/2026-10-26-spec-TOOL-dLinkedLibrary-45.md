# TOOL-dLinkedLibrary-45 — govkit's `find_block` and `write_block` re-pointed to the factory, and a census arm that sees a parser with no marker constant

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 3 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-45-deviation-451.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-45-deviation-451.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 30 at HIGH**, report item **R9**. No other id shares the item; id 20 (item R7, the census's
constant and awk arms) is `TOOL-dLinkedLibrary-43`'s.

`tools/govkit/govkit.py` `find_block` (:5776) and `write_block` (:5806) reproduce the region contract by
hand, its docstring says so ("REPRODUCES the shipped splice's refusal table, deliberately"), and their
markers come from `marker_pair()`, not module constants, so neither census query of
`TOOL-dLinkedLibrary-18` §4 matches them. That unit's AC8 and standing census arm would certify `0
site(s) outside the factory` while govkit splices adopter files with its own parser.

This unit re-points both to `find_pair` and `splice_region`, keeps govkit's one divergence as a caller-side
test, and adds a census arm keyed on behaviour, so a parser that takes its markers as arguments is seen.
It repairs `TOOL-dLinkedLibrary-18` and builds one step after it (order 3).

## 2. Scope (IN)

- **S1** — The re-point. `tools/govkit/govkit.py` carries the `region_py` block inline once
  (`TOOL-dLinkedLibrary-18` S6's rule for a kit module that reads a region), and `find_block` returns
  `None` when no line of the text `is_marker_line` reads as the open or the close mark, which is the
  first-apply case govkit supports and the shipped splice does not; otherwise it calls `find_pair` and
  raises govkit's `Refusal` carrying the `RegionError`'s rule. `write_block` splices through
  `splice_region`. Their names, signatures and messages stay. Observed by AC1 and AC2.
- **S2** — The behavioural arm. `region.py --census` gains a third arm over tracked Python files under
  `tools/` and `skills/`: inside a function that splits a text into lines, an `==` comparison one of whose
  operands is a parameter of that function or of a function nested in it, named with `mark`, `open` or
  `close`, read with `ast`. A hit inside the factory or its inline blocks is not a site. Observed by AC3
  and AC4.
- **S3** — The planted parser. The census arm's plants in the parity suite gain a module whose
  `find_thing(text, open_m, close_m)` slices with `line == open_m` and holds no marker constant; the
  census names it. Observed by AC4.
- **S4** — govkit's version moves with its shipped bytes, `KIT_GOVKIT_VERSION` in
  `tools/govkit/govkit.py`. NOT OBSERVED by a criterion here: the `kit version markers` leg grades it at
  the close.

## 3. Non-goals (OUT)

- `marker_pair()` and the marker styles it synthesizes: unchanged, read as before.
- The constant and awk arms of the census and their exclusions: `TOOL-dLinkedLibrary-43`'s (id 20).
- `scan_hold_region` in `tools/govkit/selftest.py`: `TOOL-dLinkedLibrary-18`'s table re-points it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-18` — `find_pair`, `splice_region`, `is_marker_line`, the `region_py` block and `region.py --census`, which S1 calls and S2 widens (id 30)
- **hands-off** `TOOL-dLinkedLibrary-64` — `find_block` and the behavioural arm, which unit 64 corrects (ids 32, 10 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:5776` `find_block`: column 0, one trailing CR, exactly one open and one close,
  close after open, and "zero opens AND zero closes returns None rather than raising". `:5806`
  `write_block` splices between the two indexes `find_block` returns.
- A probe at HEAD `823440497` over every tracked Python file under `tools/` and `skills/`, keeping
  functions that call `split` or `splitlines` and compare with `==` a parameter named with `mark`,
  `open` or `close`, finds one site: `tools/govkit/govkit.py:5792`, `find_block`'s `_is`. With `in` also
  read it adds `tools/govkit/selftest.py:1549` (in `TOOL-dLinkedLibrary-18`'s table) and
  `tools/policy/check_policy.py:3244` (`render_said`, one marker found in output lines, no region), which
  is why S2 reads `==` alone. PINNED at that commit.

### `find_block` after S1

```python
def find_block(text, open_m, close_m):
    lines = text.split("\n")
    if not any(is_marker_line(l, open_m) or is_marker_line(l, close_m) for l in lines):
        return None                                   # first apply: govkit's one divergence
    try:
        return find_pair(lines, open_m, close_m)
    except RegionError as exc:
        raise Refusal(str(exc)) from exc
```

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S4
- `tools/lib/region.py`: S2
- `tools/lib/resolve-python.test.sh`: S3's plant

### Alternatives rejected

- **Catching every `RegionError` as `None`.** It turns a doubled or reversed pair into "no block", and
  `write_block` would then append a second pair, the truncation class the factory exists to refuse.
- **Adding govkit's two names to the census by path.** It sees these two and no third; S2 sees the shape.

## 5. Production-readiness checklist

- security — `write_block` writes adopter files; after S1 it refuses every malformed pair the factory
  refuses, before writing, and keeps its no-join append.
- perf / scale — one pass per call, as before; the census arm adds one `ast` parse per Python file.
- error / empty / loading states — no marker: `None`, as before; a malformed pair: `Refusal` naming the
  factory's rule.
- observability — the census names each behavioural site.
- risks — a govkit apply that accepted a malformed pair now refuses it; AC2 runs govkit's own fixtures.
- testing — AC1 to AC4.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports govkit and calls `find_block` over a text with no marker, one
  well-formed pair, a doubled open and a reversed pair, it returns `None`, the two indexes, and raises
  `Refusal` twice naming the factory's rule.
  Red when: a malformed pair returns indexes, or no pair raises.
- **AC2** — When `python tools/govkit/govkit.py --help` and govkit's apply fixtures that splice a marked
  block run after S1, each exits as it did at base.
  Red when: a well-formed adopter block is refused or spliced differently.
- **AC3** — When `python region.py --census` runs from `tools/lib` before S1, it names `find_block`'s line;
  after S1 it names neither govkit function.
  Red when: a constant-free parser is outside the census's sight.
- **AC4** — When the census runs over a scratch tree holding S3's planted `find_thing`, it exits 1 naming
  it; with the plant's `==` turned into a call of `is_marker_line`, it names nothing there.
  Red when: the planted parser passes, or a factory call is read as a site.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC4 · the planted constant-free `find_thing`, the failing case staged by a census without the behavioural arm · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 30
  (HIGH, item R9).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-18`'s factory (`find_pair`, `splice_region`,
`is_marker_line` and the `region_py` block) and its census in `tools/lib/region.py`; govkit's two
functions become thin callers, as that unit's §4 makes `gen_build_index.py`'s. `python
tools/codebase-map/reuse_lookup.py "census of region parsers outside a factory"` ranked `parse`,
`parse_args`, `census` and `parse_conf`, none a region reader, so no existing seam fits beyond the
factory.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

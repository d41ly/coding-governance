# TOOL-dTrueNorth-9 — `_expand_ids` keeps its two-value return for all four callers, and the audit pins come from a sibling reader

**Status:** CLOSED · rev-2 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 3

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-9-deviation-8.md](../build/2026-10-21-build-TOOL-dTrueNorth-9-deviation-8.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-9-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-9-ledger.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-9-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-9-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 11 at HIGH**, its item **H2**. `TOOL-dTrueNorth-5` §4 S3 makes `_expand_ids`
return `(ids, bad, pins)` and names only its two call sites in `read_bindings`. Two more callers
unpack two values: `read_idlist`, and `backlog.read_header_verbs` through the lambda the generator
hands it. Built as written, both raise `ValueError`, and the build-index generator then fails on
every spec header carrying `closes` or `advances` and on every id list, which takes the build index
down for the whole tree. This unit keeps the two-value contract for every caller and puts the pin
capture in a sibling reader that `read_bindings` alone calls. It repairs `TOOL-dTrueNorth-5`. The same
defect at MEDIUM, id 27 (item M12), is batched into `TOOL-dTrueNorth-16`.

## 2. Scope (IN)

- **S1** — `_expand_ids(rest, alt)` (`tools/memory-tree/gen_build_index.py:599`) returns
  `(ids, bad)`, the shape it has at base, for all four of its call sites. This supersedes
  `TOOL-dTrueNorth-5` §4 S3's first bullet, which gave it a third value. Where that unit's pass
  shipped the three-value return, this unit restores the two-value one and moves the third value
  into S2's reader. Observed by AC1 and AC2.
- **S2** — `read_id_pins(rest, alt)` returns `{id: N}`, the highest `N` each id carries as
  `@rev-N` on the line, and nothing for a range token, which carries no pin. `read_bindings` calls it
  beside its `_expand_ids` call for the kind line (`:681`) and sets the record's `pins` from it, the
  key `TOOL-dTrueNorth-5` S3 defines and `TOOL-dTrueNorth-4`'s population reads. Observed by AC3.
- **S3** — One spelling of the id token: `build_id_token_re(alt)` compiles the single-id pattern
  with its optional `@rev-(\d+)` group, and both `_expand_ids` and `read_id_pins` match through it, so
  the reader of the ids and the reader of their pins cannot disagree on what an id is. Observed by
  AC1 and AC3.
- **S4** — The arm in the generator's self-test: a fixture spec whose status header carries
  `closes` and `advances`, a fixture `ids:` list read through `read_idlist`, and a `spec-audit`
  record whose Serves line pins one id twice at two revisions and names a range. Observed by AC2 and
  AC3.

## 3. Non-goals (OUT)

- Any change to `backlog.py`. Its `read_header_verbs` keeps reading `ids, bad = expand(value)`
  (`tools/memory-tree/backlog.py:744`); the contract on its side is `TOOL-dTrueNorth-16`'s item for
  id 27.
- The `P` and `Q` rows and the cutoff: `TOOL-dTrueNorth-5`, and `TOOL-dTrueNorth-13` and
  `TOOL-dTrueNorth-14` where they amend them. This unit reads pins and grades nothing.
- A checklist entry requiring a `git grep` of a function's callers in §10, the finding's suggested
  left-shift. The class has its record, `memory/gotchas/a-spelling-change-strands-its-readers.md`,
  and S4's arm is the gate that would have caught this instance.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-5` — the `pins` key of a `read_bindings` record and its grading in `cmd_print_bindings`; without that unit there is no pin to read and nothing calls this reader
- **hands-off** `TOOL-dTrueNorth-20` — AC3's three distinct ids, which `read_bindings` yields once that unit folds a repeated id there: this pass keeps `_expand_ids`' list as base returns it and observes AC3's `pins` half, and that unit re-observes the ids and adds the duplicate case to S4's arm (the round-2 spec audit's ids 13 and 35)

## 4. Design

### Evidence

`git grep -n '_expand_ids(' -- tools/memory-tree/gen_build_index.py` at base prints five lines:

| Line | Site | Unpack |
|---|---|---|
| `:479` | `_read_backlog_verbs`, the lambda handed to `backlog.read_header_verbs` | `ids, bad = expand(value)` at `tools/memory-tree/backlog.py:744` |
| `:599` | the definition | returns `ids, bad` |
| `:663` | `read_bindings`, the `**Commissions:**` line | `cids, bad` |
| `:681` | `read_bindings`, the kind line | `ids, bad` |
| `:2917` | `read_idlist` | `got, wrong` |

The single-id pattern at `:603` already admits `(?:@rev-\d+)?` and drops the revision, so S3 adds a
capture group and changes no match.

### Data model

```python
def build_id_token_re(alt: str):  # one id, with an optional @rev-N pin
    return re.compile(r"^(?P<fam>" + alt + r")-(?P<slug>[A-Za-z0-9]+)-(?P<seq>\d+)(?:@rev-(?P<rev>\d+))?$")

def read_id_pins(rest: str, alt: str) -> dict:   # {"TOOL-x-1": 3}
    ...
```

`read_bindings` gives every record a `pins` dict, empty when no token is pinned, and only the kind
line feeds it: a `**Commissions:**` line carries no audit pin.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `read_id_pins` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |
| `build_id_token_re` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, OK |

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

### Alternatives rejected

- **All four call sites take the third value.** It is a change at four sites and in `backlog.py`,
  a second module, to carry a value only one of them reads; the next caller added would be stranded
  the same way.
- **A wrapper returning three values beside an unchanged `_expand_ids`.** Two functions would then
  expand ranges, and the pin reader would still re-parse the line.

## 5. Production-readiness checklist

- security — no new input: the same Serves line, read once more by a pure function.
- perf / scale — one extra regex pass over each record's Serves line.
- error / empty / loading states — a line with no pin yields `{}`; a range yields no pin.
- observability — unchanged; `--print-bindings`' rows are `TOOL-dTrueNorth-5`'s.
- risks — a future caller of `_expand_ids` expecting pins gets none; S3's shared pattern makes
  `read_id_pins` the place to read them.
- testing — AC1 to AC3 as probes; the arm under §7.
- migration — none.
- user docs — none; no page under `help/` covers the generator's internals.

## 6. Acceptance criteria

- **AC1** — When a probe loads `tools/memory-tree/gen_build_index.py` by path and calls
  `_expand_ids("TOOL-x-1@rev-2 TOOL-x-2..3", alt)` with `alt` the probe's family alternation, it
  returns a pair, `(["TOOL-x-1", "TOOL-x-2", "TOOL-x-3"], [])`.
  Red when: the call returns three values, as `TOOL-dTrueNorth-5` S3 wrote it.
- **AC2** — When the same probe calls `read_idlist(["TOOL-x-1@rev-2", "-3"], alt)` and
  `_read_backlog_verbs` on a header ending `· closes TOOL-x-4 · advances TOOL-x-5`, both return
  without raising, the first `["TOOL-x-1", "TOOL-x-3"]`, the second both verbs.
  Red when: either raises `ValueError` from an unpack of three values.
- **AC3** — When the probe runs `read_bindings` over a fixture git repository under `%TEMP%` whose
  one record reads `**Serves:** spec-audit TOOL-tPin-1@rev-2 TOOL-tPin-1@rev-3 TOOL-tPin-2..3`, the
  record's `pins` is `{"TOOL-tPin-1": 3}` and its `ids` are `TOOL-tPin-1`, `TOOL-tPin-2` and
  `TOOL-tPin-3`.
  Red when: `pins` holds a range id, keeps the lower revision, or is absent.
  fixture: a fixture repository built the way the generator's self-test builds its own; the tree
  holds none today.

## 7. Gates

`build-index selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC2 AC3 · a header carrying closes and advances, an ids list and a doubly pinned record, each red against a three-value _expand_ids · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Does the build's grant lift veto 2 for the generator edit?** The generator is a governance
  carrier by `PLAY-dClosedLoop-10`'s list, and `cl-dClosedLoop-0005` names the `@rev-N` pin on a
  Serves line, whose reader this is. RESOLVED (agent, 2026-10-21, delegated): lifted by
  `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the build-index generator's Serves-line pin
  reader cl-dClosedLoop-0005 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 11 (HIGH, item H2).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "keep a function's return shape for every caller
and add a sibling reader"` ranked `read`, `read_text` and `read_conf_key` by name stem and named no
seam for a token reader, so the seam was found by reading source: `_expand_ids` and its single-id
pattern in `tools/memory-tree/gen_build_index.py:599-616`, which S3 lifts into one builder both
readers share, and `read_bindings` (`:619`), which gains the one call. The four call sites were read
by `git grep -n '_expand_ids('`, the evidence the finding's left-shift asks a spec to cite. No hit
disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`

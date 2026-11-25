# TOOL-dTotalRecall-120 — the causes leg grades everything once its legacy population is drained

**Status:** CLOSED · rev-2 · 2026-11-25 · node d · Tier-2 · base acbb74bb · streams tooling · order 48

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-120-1-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-120-1-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-120-2-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-120-2-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-120-2-builder-return.md](../build/2026-11-25-build-TOOL-dTotalRecall-120-2-builder-return.md) | journal | — |
| [2026-11-25-build-TOOL-dTotalRecall-120-widen-31.md](../build/2026-11-25-build-TOOL-dTotalRecall-120-widen-31.md) | widen | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-120-build-2-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-build-2-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-120-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief.md) | journal | TOOL-dTotalRecall-121 |

<!-- /gen:spec-records -->

## 1. Goal

H6 of the closing review (finding 17): once the last causes row of the armed legacy home is drained, the causes leg
prints `unarmed` and exits 0 with nothing read, the writer census among it. Draining is what the ratchet rewards. This
unit makes an armed home with no row an empty set, so every record is graded.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/record_causes.py#read_legacy_paths` returns an empty set for a home whose state is `armed`, with
  a note saying no legacy row is left, and keeps None for no registration and for an absent or unarmed home (§4).
  Observed by AC1 and AC2.
- **S2** — The docstring's exit line no longer lists an empty population as unarmed, and the reader's says what each
  answer means. Observed by AC3.
- **S3** — The plant `legacy-drained`: the causeless plant's tree with its home drained through
  `legacy_ledger.py#write_rows`, `--check` exiting 1 and `--backfill` writing, with its arm in
  `tools/memory-tree/check-memory-hygiene.test.sh` (§4). Observed by AC1 and AC4.
- **S4** — The suite's `FLOOR_ASSERTIONS` rises by the assertions added and its `shell-role` row takes the measured count.
  Observed by AC4.

## 3. Non-goals (OUT)

- The `record_kinds.py` slice of the population, whose reader already answers a set.
- Draining, seeding or moving any row of the live home.
- A home whose rows are malformed, or a registration with no `check` field: each stays the refusal it is.

### Edges

- **consumes-from** external — the closing review's report and the landed units whose code it read
- **consumes-from** `TOOL-dTotalRecall-115` — its bytes of the symbol map, the shell-role rows, edited after it
- **consumes-from** `TOOL-dTotalRecall-116` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, edited after it
- **consumes-from** `TOOL-dTotalRecall-117` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, edited after it
- **consumes-from** `TOOL-dTotalRecall-118` — its bytes of the symbol map, edited after it
- **consumes-from** `TOOL-dTotalRecall-119` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, the causes module, edited after it
- **hands-off** `TOOL-dTotalRecall-121` — this unit's bytes of the symbol map, the shell-role rows, the hygiene suite and its floor
- **hands-off** external — the close's next bar, the held suites and the landing, each the main loop's

## 4. Design

Read at `acbb74bb` on 2026-11-25. The report holds. Run over the causeless plant's fixture with its home cut to its
header, `read_home_state` read `armed`, `run_check` printed the one `unarmed` line and exited 0, and `--backfill` wrote
nothing; with the empty set in its place the check exited 1 naming the new record and the two former legacy ones, and the
backfill wrote three (DERIVED 2026-11-25, that run).

### The reader

```python
paths = {k[0] for k in rows if k[1] == LEGACY_SECTION}
if not paths:
    return paths, f"0 record row(s) (-), {len(rows)} section row(s): {reg.home} is drained, and every record is graded"
return paths, f"{len(paths)} record row(s) (-), {len(rows) - len(paths)} section row(s)"
```

Every reader of the answer is safe with the empty set: `run_check` and `write_missing_causes` test `is None`;
`check_kept_instrument` reads `legacy or ()`; the rest test membership or intersect. An adopter whose population seeded
empty is graded whole, which is what an empty legacy population states.

### The plant

`legacy-drained` joins `PLANTS` and takes the causeless plant's record. After the seed, the fixture calls
`legacy_ledger.write_rows(root, reg, {})`, the writer a drain ends in, so the state is one production reaches. The
argument is the empty mapping: `write_rows` iterates its items, and a list raises `AttributeError`, as the first pass
found. Over the causeless plant the call left the header alone, `read_home_state` `armed` (DERIVED 2026-11-25, a probe). The
plant's lines are `run_check`'s, then `write_missing_causes`'; it passes, exit 0 with a PASS line, when the check exits 1
naming the new record under `causes`, prints the writer census's count line and no `unarmed`, and the backfill's count
line reads at least one written.

### Inventory

Minted: the plant `legacy-drained`; no function but the plant's check, `check_drained_plant` (python-function, verb
`check`).

### Files touched (estimate)

- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/project/shell-role.txt`
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (the widen record and this unit's ledger)

### Alternatives rejected

- **A red for an empty home.** A full drain is the admitted end, never a defect.
- **The header line cut by hand in the fixture.** The factory's writer is what a drain runs.

## 5. Production-readiness checklist

- security — a gate stops passing vacuously.
- perf / scale — N/A, the same walk over the same records.
- error / empty / loading states — the empty population is graded; the unregistered and unarmed ones print as they do.
- observability — the note names the home drained.
- risks — the day the live home drains, every remaining causeless record is red at once; that is the drain's own claim.
- testing — AC1 to AC4 by the pass; §7's arm by the main loop.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --fixture --plant legacy-drained` runs from `tools/memory-tree/`, it prints the
  new record under `causes`, the `cause-writer ·` count line, a `backfilled` line and `fixture legacy-drained · PASS`, and
  exits 0.
  Red when: the armed empty home reads unarmed. Today the check prints one `unarmed` line.
- **AC2** — When the plants `legacy`, `causeless` and `none` run there, each prints what it prints at `acbb74bb`; and a
  probe calling `read_legacy_paths` over a tree with no registration answers None.
  Red when: an unregistered or unarmed population is graded.
- **AC3** — When `grep -n 'an empty population' tools/memory-tree/record_causes.py` runs, it prints no line listing it among
  the unarmed exits.
  Red when: the docstring still promises the vacuous green.
- **AC4** — When `grep -n 'plant legacy-drained' tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints the arm, and the
  floor and the `shell-role` row carry the added assertions and lines.
  Red when: the plant is declared and no suite runs it.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `ratchet (never gains)` · `ratchet (both ways)` · `memory-hygiene self-test` · `record causes (causes and orphans over the legacy population)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 · the `legacy-drained` plant, red on today's reader, which exits 0 reading nothing · `FLOOR_ASSERTIONS` by the assertions added

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-114` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's H6.
- rev-2 · 2026-11-25 · §4 · the first pass's divergence folded: the plant hands `write_rows` the empty mapping; from
  `2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief`.

## 10. Reuse audit

The seams, each read at `acbb74bb`: `record_kinds.py#read_legacy_keys`, which answers a set in the same situation;
`legacy_ledger.py#read_home_state` and `legacy_ledger.py#write_rows`; the plant tables of `record_causes.py`.
`python tools/codebase-map/reuse_lookup.py "read a ledger home's rows and its armed state"` ranked `read_rows`, which
`read_ledger` already calls. `record_causes.py#check_cause_writers` is run unchanged by the armed path.

Recall terms used: `python tools/memory-recall/query.py "a ledger home whose population drained reads unarmed" --terms "legacy home armed empty population drain vacuous selector record-kinds-legacy"`

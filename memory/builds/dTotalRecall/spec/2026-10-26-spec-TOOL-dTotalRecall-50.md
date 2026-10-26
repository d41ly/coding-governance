# TOOL-dTotalRecall-50 — the cause census reads the build folders' instruments, and the pinned departures writer is a declared row that drains when its owner repins

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 32 at HIGH**, its item **H6**, alone in that item. The pinned instrument
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` (blob `30a1f15b`)
writes the departures record's head `**Serves:** journal {s['first']}` at `:806` with no cause line.
The README's close runs it with `--write` and commits that record under a new name, so the record has
no legacy row and reds `record causes`. `TOOL-dTotalRecall-36` S7's census reads only the tool root,
never `memory/builds/*/build/*.py`, so its AC6 is green over the writer. The instrument is the owner's:
only `packet.py --repin` moves its pin, and its `--check` compares the record's bytes
(`deviations.py:871-875`), so a cause line added by hand reds the close. This unit widens the census
to the build folders' scripts, declares the pinned writer, files the ask its owner answers, and reads
the departures record's cause from its Serves unit until that ask lands. It repairs
`TOOL-dTotalRecall-36`.

## 2. Scope (IN)

- **S1** — The census reads the instruments. `check_cause_writers` in
  `tools/memory-tree/record_causes.py` also reads every tracked `memory/builds/*/build/*.py`, skipping
  the file's own binding head, the first `BIND_HEAD_LINES` lines `tree_lib.BIND_RE` matches, which is
  the record's binding and not a literal it writes. Each hit is disposed as unit 36's are, by
  `CAUSE_WRITER_KEPT`, or by S2's row. Observed by AC1.
- **S2** — The pinned-writer row. `CAUSE_WRITER_PINNED` in the same module holds one row per pinned
  instrument that writes a record with no cause: the instrument's path, the glob of the records it
  writes, and the id of the ask that asks its owner for the line. The deviations row's glob is
  `memory/builds/*/build/*-build-*-departures-*.md`, as `deviations.py:883-889` names the record. A row
  is red when its instrument spells `Caused-by` (drain it), or when its ask id is not a filed ask.
  Observed by AC2.
- **S3** — The interim read. `check_causes` reads a record that a standing row's glob matches, and
  that carries no `Caused-by`, as caused by its first Serves id, the reading `TOOL-dTotalRecall-19` S8
  gives a legacy record. A record outside every row's glob is graded as before. Observed by AC3.
- **S4** — The ask. One ask row in `memory/builds/dClosedLoop/BACKLOG.md`, which the README's write rule
  admits outside this build's folder: the departures instrument writes `**Caused-by:** <first>` on the
  line after its Serves line, and its owner repins it with `packet.py --repin`; accept that line in a
  departures record the repinned instrument writes, and S2's row red until it drains. Its id is the
  one S2's row names. Observed by AC2.

## 3. Non-goals (OUT)

- Editing a pinned instrument or moving its pin: the owner's, through S4's ask.
- Hand-writing a cause line into a departures record: its `--check` compares bytes.
- The other writers and the census's tool-root half: `TOOL-dTotalRecall-36`'s.
- The as-built instrument `asbuilt.py`: its one record is a legacy view, kept as
  `TOOL-dTotalRecall-49` keeps its product successor.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — `check_cause_writers` and `CAUSE_WRITER_KEPT`, whose
  population this unit widens to the build folders' scripts
- **consumes-from** `TOOL-dTotalRecall-19` — `check_causes` and the legacy reading of a record's cause,
  which S3 applies to a declared glob
- **hands-off** `TOOL-dTotalRecall-53` — `CAUSE_WRITER_PINNED` and the widened census, which that unit's census table and keep marker read (ids 29 and 34)
- **hands-off** `TOOL-dTotalRecall-55` — the eight build-folder hits of §4, which that unit keeps by a path-keyed row outside their bytes (the round-1 audit of units 44 to 53, id 37)
- **hands-off** `TOOL-dTotalRecall-60` — `CAUSE_WRITER_PINNED`'s ask and the dClosedLoop ask row, which that unit resolves through `check_hold_live` and re-renders (the round-1 audit of units 44 to 53, ids 25 and 35)

## 4. Design

### The reading at base

At base `462d20f3`, nine tracked `memory/builds/*/build/*.py` files spell `**Serves:** ` below their
first 12 lines (PINNED, 2026-10-26, by an `awk 'NR>12'` pass over `git grep -l`): six in dClosedLoop
(`deviations.py`, `walk.py`, `asbuilt.py`, `fold-inventory.py`, `packet.py`, `walk-seed.py`), two in
aMendedFleet and one in dDerivedDocket. Only `deviations.py` writes a record under a new name at this
build's close; the pass disposes each of the other eight by `CAUSE_WRITER_KEPT` with its reason, and
records each in its commit's `Decided:` trailer.

### The row

```python
CAUSE_WRITER_PINNED = (
    ("memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py",
     "memory/builds/*/build/*-build-*-departures-*.md",
     "<the ask id S4 files>"),
)
```

### Inventory

Minted: `CAUSE_WRITER_PINNED` in `tools/memory-tree/record_causes.py`; the fixture plants
`pinned-writer-drained` and `departures-pinned`; one ask in dClosedLoop's backlog. Naming cell: none,
the lexicon declaring no constant cell.

### Files touched (estimate)

- `tools/memory-tree/record_causes.py`
- `memory/builds/dClosedLoop/BACKLOG.md`

`TOOL-dTotalRecall-47` and `TOOL-dTotalRecall-49` also write `record_causes.py` at order 18, so
BUILD-METHOD M6 sequences the three passes.

### Alternatives rejected

- **Hand-backfill the departures record.** Its `--check` re-renders it and compares bytes.
- **Seed the departures record into the legacy population.** It does not exist at the seed, and the
  ledger is shrink-only.

## 5. Production-readiness checklist

- security — no new write surface: one ask row and one constant.
- perf / scale — one more `git ls-files` glob per census run.
- error / empty / loading states — a pinned row that has drained, or names no filed ask, is red and
  named; a census with no build-folder hit prints its count.
- observability — `--check` prints each pinned row with its ask id and the records its glob reads.
- risks — while a row stands, a departures record reads its cause from its Serves unit; the row reds
  the day the instrument writes the line, so the interim read cannot outlive its reason.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --check` runs at the pass tip, its census lists `deviations.py`
  under `CAUSE_WRITER_PINNED` and each other build-folder hit of §4 as kept, and lists no `.py` record
  for its own binding head.
  Red when: the census reads only the tool root, or reds a probe record for the binding it carries.
- **AC2** — When `python record_causes.py --fixture --plant pinned-writer-drained` builds a fixture
  whose pinned instrument writes `**Caused-by:**`, `--check` exits 1 naming the row; with the row's ask
  id cut from the fixture's backlog, it exits 1 naming the id.
  Red when: a drained row, or one with no filed ask, still passes.
- **AC3** — When `python record_causes.py --fixture --plant departures-pinned` builds a fixture holding a
  causeless `-departures-build.md` record under a standing row, `--check` passes it; with the row cut,
  it exits 1 naming the record.
  Red when: the departures record reds while its writer's row stands, or passes once the row is gone.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/memory-tree/record_causes.py · covers AC2 AC3 · the plants `pinned-writer-drained` and `departures-pinned`, staged by skipping the row's drain test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does the close's departures record carry a cause while its writer is pinned?** Options:
  (a) the ask alone, the causes leg red from the close until the owner repins; (b) the ask and S3's
  interim read under a draining row; (c) a cause line added to the record by hand, which reds the
  README's `deviations.py --check` at the close and fails veto 1. (b) meets every criterion here and
  keeps the leg green with no rule unread: the record's cause is named, read as the legacy reading
  names one, and the row reds once the instrument writes the line. RESOLVED (agent, 2026-10-26,
  delegated): (b), rung 3, the most feature-rich option surviving the vetoes. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 32
  (HIGH, item H6).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-55, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dTotalRecall-36` S7's `check_cause_writers`, whose population widens, and
`TOOL-dTotalRecall-19` S8's legacy reading, which S3 applies to a declared glob; the ask is an ordinary
row of an existing backlog. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a
record head after its binding line"` ranked name-stem neighbours and no declaration of pinned writers,
so no existing seam fits for S2's row.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`

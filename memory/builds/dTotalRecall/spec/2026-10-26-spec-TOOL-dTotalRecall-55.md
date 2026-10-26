# TOOL-dTotalRecall-55 — the cause census keeps the build folders' scripts by a path-keyed row held outside their bytes

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 37 at HIGH**. It shares item **H1** with ids 4, 15 and 24, which
`TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-56` and `TOOL-dTotalRecall-58` close.
`TOOL-dTotalRecall-53` S34 retires `CAUSE_WRITER_KEPT` for an in-file marker, `# census: kept`, on
each kept line, and its AC34 requires the constant gone from `tools`. But `TOOL-dTotalRecall-50` §4
keeps eight build-folder scripts by that constant. At base `462d20f3` they are, verified by an
`awk 'NR>12'` pass over `git ls-files 'memory/builds/*/build/*.py'`: dClosedLoop's `asbuilt.py`,
`packet.py`, `walk.py`, `fold-inventory.py` and `walk-seed.py`, aMendedFleet's `harness.py` and
`ab.py`, and dDerivedDocket's `signer.py`. None of them can take a marker. `asbuilt.py` and
`packet.py` are pinned instruments (`packet.py:90-94`), and README:38-39 makes a moved instrument
blob a stop. Every one sits outside the write set README:50 and the packet's non-goals give this
build. So S34 leaves these eight with no keep path. This unit declares their keep outside their
bytes, in one path-keyed table the census reads. It repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The table. `CENSUS_KEPT_PATHS` in `tools/memory-tree/tree_lib.py` holds one row per
  census and file as `(census, path, reason)`. The census is named by its function,
  `check_cause_writers` or `check_alias_compares`. The path is one tracked file, and the reason is
  printed beside the hit. The accessor `read_kept_path(census, path)` in the same module returns the
  row's reason or `None`, and it is the only reader of the table. Observed by AC1.
- **S2** — The cause census reads it. `check_cause_writers` in `tools/memory-tree/record_causes.py`
  keeps a hit in a file under `memory/builds/*/build/` only when `read_kept_path` answers for it, and
  prints `kept <reason>`. Such a hit is red otherwise. The departures instrument stays under
  `CAUSE_WRITER_PINNED` (`TOOL-dTotalRecall-50` S2) and takes no row here. Observed by AC1.
- **S3** — The eight rows. `asbuilt.py` and `packet.py` carry the reason `pinned instrument`, being
  in the packet's `INSTRUMENTS`. The other six carry `outside the write set`. Each row is written
  from the census's output at the pass base, and the pass commit's `Decided:` trailer names the
  eight. Observed by AC1.
- **S4** — A row cannot outlive its hit. A `check_cause_writers` row whose file no longer spells a
  `**Serves:** ` literal below its binding head is red, naming the row, so the table drains as the
  owners add cause lines. Observed by AC2.

## 3. Non-goals (OUT)

- The marker and its reader for files under `tools/`: `TOOL-dTotalRecall-53` S34's.
- The alias census's row for `deviations.py`: `TOOL-dTotalRecall-56`'s.
- Refusing a row that names an editable file: `TOOL-dTotalRecall-57`'s.
- Refusing a marker written into a build-folder file: `TOOL-dTotalRecall-58`'s.
- A row's falsity test against the records its file writes, and `CAUSE_WRITER_PINNED`'s ask
  resolution: the batch `TOOL-dTotalRecall-60` holds those for ids 44 and 25.
- Editing any build-folder script, or filing an ask for its cause line.

### Edges

- **consumes-from** `TOOL-dTotalRecall-53` — S34's retirement of `CAUSE_WRITER_KEPT` and its marker,
  which leaves the build-folder hits this unit keeps with no keep path
- **consumes-from** `TOOL-dTotalRecall-50` — the census widened to `memory/builds/*/build/*.py` and
  `CAUSE_WRITER_PINNED`, whose eight other hits this unit disposes
- **hands-off** `TOOL-dTotalRecall-56` — `CENSUS_KEPT_PATHS` and `read_kept_path`, which the alias
  census reads for its build-folder hit
- **hands-off** `TOOL-dTotalRecall-57` — `CENSUS_KEPT_PATHS`, whose rows that unit holds to files no
  pass may edit
- **hands-off** `TOOL-dTotalRecall-60` — the table's rows and reasons, which that unit keys to the
  records each file writes (id 44) and beside which it resolves the pinned row's ask (id 25)
- **consumes-from** `TOOL-dTotalRecall-61` — S2 as that unit amends it in step 19, so this pass moves the last rows of `CAUSE_WRITER_KEPT` into the table (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-65` — `CENSUS_KEPT_PATHS` and `read_kept_path`, whose rows that unit moves into a project registry (the round-1 audit of units 54 to 60, id 27)
- **hands-off** `TOOL-dTotalRecall-66` — S4's drain, which that unit keys on the census's own hit (the round-1 audit of units 54 to 60, ids 4 and 40)
- **consumes-from** `TOOL-dTotalRecall-67` — S2 and AC1 as unit 61 amends them, read by their own text at step 20 and written there if unit 61's pass left them out (the round-1 audit of units 61 to 66, id 1)

## 4. Design

### The table

```python
CENSUS_KEPT_PATHS = (
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py",
     "pinned instrument"),
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py",
     "pinned instrument"),
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py",
     "outside the write set"),
    # ... fold-inventory.py, walk-seed.py, the two aMendedFleet scripts and dDerivedDocket's signer.py
)
```

The table lives in `tree_lib.py` because both censuses already read their bindings through that
module, `record_causes.py` through `tree_lib.BIND_RE` (unit 50 S1) and `record_kinds.py` through
`tree_lib.read_bindings` (unit 53 S21). One table and one accessor give the two censuses one keep
grammar for a file they may not edit, beside S34's one marker for a file they may.

### Inventory

Minted: `CENSUS_KEPT_PATHS` and `read_kept_path` in `tools/memory-tree/tree_lib.py`; the fixture
plant `kept-row-drained` in `record_causes.py --fixture`. Naming cells: `read_kept_path` is asked of
`python tools/lexicon/lexicon.py --suggest read_kept_path --as py.function` at the pass, and a
flagged name takes the suggestion before a caller is written; the constant has no cell.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

`TOOL-dTotalRecall-56`, `-57` and `-58` also write these modules at order 30, so BUILD-METHOD M6
sequences the four passes, this one first, since two of them read its table.

### Alternatives rejected

- **Mark the eight files.** Two are pinned, and all eight are outside this build's write set.
- **Keep `CAUSE_WRITER_KEPT` for build-folder rows.** It leaves two file-keyed constants beside one
  marker. One table read by both censuses is one grammar for the same case.
- **A `[[ledger]]` population with `keep:<ask>` rows.** No owner ask exists for the seven files
  outside the pinned departures writer, and the ledger factory (`TOOL-dWitnessedBar-13`) is a
  baseline of counted sites, not a keep list.

## 5. Production-readiness checklist

- security — no new surface: a read-only census over tracked files.
- perf / scale — one tuple lookup per build-folder hit.
- error / empty / loading states — an unkept build-folder hit and a drained row are each red and
  named.
- observability — each kept hit prints its row's reason.
- risks — a reason is an author's statement; the batch `TOOL-dTotalRecall-60` keys its falsity test
  per file (id 44).
- testing — AC1 and AC2 by the pass; the arm of §7 at the close.
- migration — none: the rows replace unit 50 §4's disposition one for one.
- user docs — none under `help/`: no page covers the census.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --check` runs from `tools/memory-tree/` at the pass tip,
  its census lists each of the eight files of §1 as `kept` with its row's reason, lists
  `deviations.py` under `CAUSE_WRITER_PINNED`, and reds none of the nine.
  Red when: a build-folder hit is red, unlisted, or kept by a marker in its own bytes.
- **AC2** — When `python record_causes.py --fixture --plant kept-row-drained` runs from
  `tools/memory-tree/` and builds a fixture whose kept build-folder script spells no `**Serves:** `
  literal, `--check` exits 1 naming the row.
  Red when: a row with no hit behind it still passes.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC2 · the plant `kept-row-drained`, staged by skipping the drained-row test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 37
  (HIGH, item H1 shared with ids 4, 15 and 24).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-65, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-67, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `check_cause_writers` (`TOOL-dTotalRecall-36` S7, widened by
`TOOL-dTotalRecall-50` S1), whose keep test gains a second source for the one population S34's
marker cannot reach. The table sits beside `tree_lib.BIND_RE` (`tools/memory-tree/tree_lib.py:410`),
the shared module both censuses import. `python tools/codebase-map/reuse_lookup.py "keep a census hit in a file that cannot be edited"`
ranked name-stem neighbours and no path-keyed keep list, so no existing seam fits for the table
itself; `backlog.check_hold_live` resolves asks, and no row here names one.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`

# TOOL-dTotalRecall-49 — the as-built view keeps the pinned instrument's bytes, and its writer is kept off the cause census by a stated reason

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 31 at HIGH**, its item **H5**, alone in that item. `asbuilt_view.py:14-18`
promises that the view renders byte for byte what the pinned instrument `asbuilt.py` (dClosedLoop,
blob `97c8f8fb`, which only the owner's `packet.py --repin` moves) renders, head included.
`TOOL-dTotalRecall-36` S4 adds `**Caused-by:** {serves}` to `VIEW_HEAD` (`:150-152`) alone, which
ends that parity: `gen_build_index.py --write` re-renders the view at `.memory-tree.conf:1018`'s
`DESIGN_VIEW` with a line the instrument does not render, and the instrument's `--check` is red from
then on. The view is dated 2026-10-19, before unit 19's seed, so it is a legacy record and gains
nothing from the line, and the edit contradicts unit 36's own non-goal "Rewriting a legacy record".
This unit keeps `VIEW_HEAD` on the instrument's bytes and keeps its module off the cause census by a
stated reason. It repairs `TOOL-dTotalRecall-36`.

## 2. Scope (IN)

- **S1** — `VIEW_HEAD` in `tools/memory-tree/asbuilt_view.py` carries no cause line: its text is the
  instrument's head as `asbuilt.py:74-77` renders it. Where `TOOL-dTotalRecall-36`'s pass wrote the
  line, this pass takes it out, and where that pass re-rendered the view, this pass renders it again
  with `asbuilt_view.py --write`. Observed by AC1 and AC2.
- **S2** — The census keeps the module by a stated reason. `CAUSE_WRITER_KEPT` in
  `tools/memory-tree/record_causes.py` lists `tools/memory-tree/asbuilt_view.py` with the reason
  `renders a pinned instrument's bytes; its one output is a legacy record`, and the reasons the
  constant admits gain that one beside unit 36's fixture and instruction text. Observed by AC3.
- **S3** — The census refuses the reason where it is false. A file kept for that reason is red when
  the record it writes, `DESIGN_VIEW`, has no `<path> -` row in the legacy population, so the reason
  cannot outlive the record it was true of. Observed by AC3.

## 3. Non-goals (OUT)

- A cause line on the view. If one is wanted, the instrument's owner changes `asbuilt.py:75` and
  repins, and the view follows at the report switch; this build files no ask for it, because the view
  is legacy and the causes check reads its cause from its Serves unit.
- The writer census itself: `TOOL-dTotalRecall-36` S7's.
- The other writers' cause lines: unit 36's S1 to S4, the run record's head being
  `TOOL-dTotalRecall-48`'s.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — `VIEW_HEAD`'s cause line, which this unit takes back out,
  and `CAUSE_WRITER_KEPT`, whose admitted reasons it widens by one
- **hands-off** `TOOL-dTotalRecall-53` — the view's instrument bytes and the kept reason, which that unit re-observes and carries into the census marker (ids 4, 15, 29 and 43)
- **hands-off** `TOOL-dTotalRecall-60` — the kept reason, which that unit admits for `asbuilt_view.py` alone (the round-1 audit of units 44 to 53, id 44)

## 4. Design

### Why the view stays legacy

The view's name is `2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`, written before unit 19's seed,
so the seed gives it a `<path> -` row and `check_causes` never asks it for a cause. Re-rendering it with
a new line rewrites a legacy record for no reader. The parity docstring (`asbuilt_view.py:14-18`) and
the kit README's `asbuilt_view` row (`tools/memory-tree/README.md:28`) stay true, so neither is edited.

### Inventory

Minted: the kept reason `renders a pinned instrument's bytes; its one output is a legacy record`.

### Files touched (estimate)

- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/record_causes.py`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (only where unit 36's pass moved its bytes)

`TOOL-dTotalRecall-47` and `TOOL-dTotalRecall-50` also write `record_causes.py` at order 18, so
BUILD-METHOD M6 sequences the three passes.

### Alternatives rejected

- **Keep the line and update the docstring.** The pinned instrument's `--check` then reds at every
  close, and the instrument is the owner's to move.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one ledger lookup per kept file of this reason.
- error / empty / loading states — a kept file whose output has no legacy row is red and named.
- observability — `--check` prints each kept file with its reason.
- risks — none beyond unit 36's census.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — the view's bytes return to the instrument's where unit 36's pass moved them.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python asbuilt_view.py --check` runs at the pass tip, it exits 0, and so does the
  pinned instrument `2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check`.
  Red when: the two tools render the view's head differently.
- **AC2** — When `grep -c "Caused-by" tools/memory-tree/asbuilt_view.py` runs at the pass tip, it
  prints `0`.
  Red when: `VIEW_HEAD` still writes a cause line.
- **AC3** — When `python record_causes.py --check` runs at the pass tip, it lists `asbuilt_view.py` as
  kept with S2's reason; in a scratch copy whose legacy home has the view's row cut, it exits 1 naming
  `asbuilt_view.py`.
  Red when: the reason keeps a writer whose output is not legacy.
  fixture: a scratch copy under the run's scratch directory; the pass makes it.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/memory-tree/record_causes.py · covers AC3 · the plant `kept-instrument-not-legacy`, staged by skipping the legacy-row test for the reason · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 31
  (HIGH, item H5).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams extended are `VIEW_HEAD` in `tools/memory-tree/asbuilt_view.py:150` and unit 36's
`CAUSE_WRITER_KEPT` in `record_causes.py`, whose reason set gains one value read against unit 19's
legacy population. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a record head
after its binding line"` named no parity mechanism beside the docstring's own promise, so no existing
seam fits for S3's test, which reads the ledger unit 19 already seeds.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`

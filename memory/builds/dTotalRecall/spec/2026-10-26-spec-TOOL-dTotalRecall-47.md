# TOOL-dTotalRecall-47 — the cause backfill is a verb run at the tip after the step-17 group, so no record written between the seed and the writers' change stays causeless

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-19`
(order 16) seeds the legacy population and lands the `record causes` leg. `TOOL-dTotalRecall-36`,
which makes the writers emit `Caused-by`, runs at order 17 in parallel with `TOOL-dTotalRecall-21` and
`TOOL-dTotalRecall-39`, and its S6 backfills only the records causeless at its own pass base. The
records unit 19's own pass writes after its seed, and those the peers' passes write after unit 36's
base, keep no cause, so the leg is red at the close. This unit makes the backfill a verb of the causes
module and runs it at its own pass tip, after the whole step-17 group, so every record written between
the seed and the writers' change gains its cause. It repairs `TOOL-dTotalRecall-36`.

## 2. Scope (IN)

- **S1** — The verb. `python record_causes.py --backfill` writes `**Caused-by:** <first Serves id>`, the
  id bare with any `@rev-<n>` pin cut, on the line after the Serves line of every tracked `.md` record
  that `check_causes` would red for having no cause: no `<path> -` legacy row, a kind that is not a
  root, and no `Caused-by`. It prints each path it wrote and a count, writes nothing else, and a second
  run writes nothing. Observed by AC1.
- **S2** — The verb refuses to guess. A record whose Serves line names no id, or that is not `.md`, is
  listed under `not backfilled` with its reason and left as it is; a non-markdown record's comment form
  is `TOOL-dTotalRecall-51`'s. Observed by AC1.
- **S3** — The tip backfill. This unit's pass runs `--backfill` at its tip and commits the records it
  wrote, which are those the passes of units 19, 21, 36 and 39 left causeless. Observed by AC2.

## 3. Non-goals (OUT)

- The causes check, the legacy population and the root column: `TOOL-dTotalRecall-19`'s.
- The writers' own cause lines: `TOOL-dTotalRecall-36`'s.
- A cause richer than the first served unit, as `TOOL-dTotalRecall-36` §3 states.
- Re-seeding the legacy population. It is shrink-only, and a re-seed would launder exactly these
  records.
- An order check over the build index. Order is the README's derived region, and this unit closes
  the instance at the step the order rule gives it.

### Edges

- **consumes-from** `TOOL-dTotalRecall-36` — S6's backfill rule, the line placement and target its
  writers emit, which this verb applies at a later tip
- **consumes-from** `TOOL-dTotalRecall-19` — `check_causes`, the `legacy-records` population and the
  `root` column, which decide what the verb writes
- **hands-off** `TOOL-dTotalRecall-53` — `record_causes.py --backfill`, which that unit names as the remedy in `check_causes`' finding (id 42)
- **hands-off** `TOOL-dTotalRecall-60` — `--backfill`, `write_missing_causes` and its fixture, which that unit scopes to one build, extends to the prefixed form and re-observes (the round-1 audit of units 44 to 53, ids 7, 8, 26, 31 and 38)

## 4. Design

### The selection

The verb selects exactly what `check_causes` reds for an absent cause, by calling the same selection
and not a copy of it; a record whose cause is present but unresolved is the check's to report and is
never rewritten. The line is placed as `TOOL-dTotalRecall-36` §4 "The head each writer emits" places
it, inside the first `BIND_HEAD_LINES` (12) lines that `read_header_edges` reads.

### Inventory

Minted: `--backfill` and `write_missing_causes(root)` in `tools/memory-tree/record_causes.py`. Naming
cell: `py.function`, where `python tools/lexicon/lexicon.py --suggest write_missing_causes --as
py.function` answers OK; `backfill` is not a declared verb, so the function leads with `write`.

### Files touched (estimate)

- `tools/memory-tree/record_causes.py`
- `memory/builds/dTotalRecall/build/` (S3's backfill)
- `memory/builds/dTotalRecall/prompts/` (S3's backfill)
- `memory/builds/dTotalRecall/reviews/` (S3's backfill)

`TOOL-dTotalRecall-49` and `TOOL-dTotalRecall-50` also write `record_causes.py` at order 18, so
BUILD-METHOD M6 sequences the three passes.

### Alternatives rejected

- **Move unit 36 before unit 19.** Its census needs `record_causes.py`, which unit 19 mints, and the
  order of a promoted repair is fixed one above the unit it repairs.
- **Backfill by hand again at this pass.** The next window between a seed and a writer change would
  need a third hand pass; a verb is run, not rewritten.

## 5. Production-readiness checklist

- security — the verb writes one line into records already tracked; it touches no other file.
- perf / scale — one `check_causes` selection and one write per selected record.
- error / empty / loading states — an empty selection prints `0 backfilled` and exits 0.
- observability — each written path and each `not backfilled` reason is printed.
- risks — the first served unit may be a weaker cause than the true one; the legacy reading assumes
  the same (`TOOL-dTotalRecall-19` S8).
- testing — AC1 and AC2 by the pass; the arm of §7 at the close.
- migration — S3's backfill of this run's own records.
- user docs — none under `help/`: no page covers record heads.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --backfill` runs in the unit 19 fixture
  (`record_causes.py --fixture`) holding a causeless `.md` record, a legacy record, a root-kind record, a
  `.sh` record and a record whose Serves line names no id, it writes the cause line into the first
  only, lists the last two under `not backfilled`, and `record_causes.py --check` then prints
  `0 causeless`; a second `--backfill` prints `0 backfilled`.
  Red when: the verb writes a legacy, root or non-markdown record, or a second run writes again.
- **AC2** — When `python record_causes.py --check` runs at this unit's pass tip, it prints
  `0 causeless`, and `git show --stat HEAD` lists the records `--backfill` wrote, among them records
  added by the passes of units 19, 21 and 39.
  Red when: a record written after unit 19's seed still carries no cause at this tip.
  figure: DERIVED at the tip by the verb's own count.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/memory-tree/record_causes.py · covers AC1 · the fixture plant `backfill-selection`, staged by letting the verb write a legacy record · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 3
  (HIGH, item H2).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `check_causes` in `tools/memory-tree/record_causes.py` (`TOOL-dTotalRecall-19` S8),
whose selection the verb calls, and `TOOL-dTotalRecall-36` S6's line rule, which it applies.
`python tools/codebase-map/reuse_lookup.py "insert a cause line into a record head after its binding line"`
ranked name-stem neighbours (`records`, `check_line`, `render_line`, `render_record`) and no record
rewriter, so no existing seam fits for the write itself.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`

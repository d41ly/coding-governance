# TOOL-dWellOiledMachine-71 — a one-fragment settings-merge upserts its packs into the pack table and re-renders every entry from the whole table

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 12 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-71-deviation-711.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-71-deviation-711.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 46, item H8, at HIGH. TOOL-dWellOiledMachine-10 S3 says `settings-merge.py` is called once
with every fragment, but govkit's `run_fragment_merges` calls it once per landed fragment and the
runbook tells adopters to run `settings-merge.py --fragment <one>` per kit; the spec never says how a
one-fragment render merges into an existing `.claude/hook-packs.json`. Rendered from one kit's packs
alone, a one-kit `govkit update` or a manual runbook step rewrites the table and silently unwires
every other kit's hooks. This unit makes every one-fragment call an upsert into the table, orders the
table by a stable key, and proves that rendering B after A still lists A.

## 2. Scope (IN)

- **S1** — The upsert. `settings-merge.py <settings> --fragment <f>` reads the existing pack table,
  replaces every row whose `fragment` is `<f>` with `<f>`'s packs, adds them where none was, and
  re-renders the dispatcher entries of `<settings>` from the whole resulting table, so a call never
  drops a row of another fragment. A table that does not exist starts empty. Observed by AC1.
- **S2** — The stable order. Within each event the table's rows are ordered by their fragment path,
  then by pack name, the order `run_fragment_merges` already passes fragments in (`sorted` over the
  receipt rows' paths, `tools/govkit/govkit.py:6125-6128`), so the order of a full render and of any
  sequence of one-fragment calls is the same. `registration order` in 10 S2 and S3 means this order.
  Observed by AC2.
- **S3** — The one-fragment check and unwire. `--check --fragment <f>` exits 0 when `<f>`'s rows in
  the table equal its current packs and the settings entries equal the whole table's render;
  `--unwire --fragment <f>` removes `<f>`'s rows and re-renders. `run_fragment_merges`' stale probe
  (`govkit.py:6156-6162`) copies the pack table beside the settings copy into its scratch directory,
  so the probe's `--unwire` reads the table it would change. Observed by AC3.
  **Readers:** by name: `tools/govkit/govkit.py` (`run_fragment_merges`) and `tools/settings-merge.py`. by value: `.claude/settings.json`, the render the unwire rewrites.
- **S4** — The runbook. `WIRE-INTO-PROJECT.md`'s one-fragment steps (`:632-643`, `:894-897`,
  `:2121-2122`) state that each call adds or refreshes that kit's packs and keeps every other kit's.
  Observed by AC4.

## 3. Non-goals (OUT)

- No change to the pack contract, the dispatcher or the event entries' shape: 10 S1 to S3 stand.
- No change to which fragments govkit selects: `run_fragment_merges`' population stands.
- No merge of two fragments' packs that share a name: a pack's tag is `hook.<fragment name>` (10 S15),
  unique per fragment.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-10` — S3's pack table and dispatcher-entry render, which this unit makes incremental
- **hands-off** `TOOL-dWellOiledMachine-82` — S3's scratch copy of the pack table, which govkit's stale probe compares (finding 18)
- **hands-off** `TOOL-dWellOiledMachine-90` — the pack table's location rule and the normalised `fragment` key (finding 60)

## 4. Design

### Evidence

- `run_fragment_merges` builds `frags` sorted by path from the landed receipt rows (`govkit.py:6125-6128`)
  and runs `settings-merge.py <settings> --fragment <p>` once per fragment, with a per-fragment
  `--check` (`:6143-6147`) and a scratch `--unwire` stale probe (`:6156-6162`).
- `WIRE-INTO-PROJECT.md:894-897` and `:2121-2122` run one `--fragment` per kit by hand.
- 10 S3 says "called once … with every fragment" and orders rows by "the order `run_fragment_merges`
  passes the fragments" (`spec-10.md:54-61`); its Migration speaks only of a full re-render
  (`spec-10.md:230-236`).

### Files touched (estimate)

- `tools/settings-merge.py`: S1 to S3
- `tools/govkit/govkit.py`: S3's stale probe copying the table
- `WIRE-INTO-PROJECT.md`: S4

### Alternatives rejected

- **Requiring every call to pass every fragment.** The runbook's per-kit steps and govkit's
  per-fragment rollback (`remove_wired_fragments`) both rest on one-fragment calls.
- **Ordering by call order.** It makes the table depend on the history of calls, so two nodes that
  adopted kits in different orders render different tables from the same fragments.

## 5. Production-readiness checklist

- security — no pack is silently unwired, so no kit's guard drops out on another kit's update.
- perf / scale — one table read and write per call.
- error / empty / loading states — an unparseable table refuses the call, exit 2, naming the file,
  never rendering from an empty table over it.
- observability — each call prints the rows it added, refreshed or removed.
- risks — a hand-edited table row survives an upsert of another fragment; `--check` of its own
  fragment names it.
- testing — AC1 to AC3 and the arm in §7.
- migration — none beyond 10's: the first full render writes the table in S2's order.
- user docs — the runbook lines of S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/settings-merge.py <scratch>/settings.json --fragment A` runs, then the
  same with `--fragment B` alone, the scratch `hook-packs.json` lists A's packs and B's, and the
  settings entries' matchers cover both.
  Red when: the second call rewrites the table from B's packs alone.
- **AC2** — When `python settings-merge.py` renders the scratch table once from A and B together and once by the two
  one-fragment calls in the order B then A, the two tables are byte-identical.
  Red when: the order of calls changes the table.
- **AC3** — When `--unwire --fragment A` runs on the two-fragment table, B's rows remain and
  `--check --fragment B` exits 0; govkit's stale probe on a scratch target reports A's stale command
  without touching the target's table.
  Red when: an unwire removes another fragment's rows, or the probe writes the target's table.
- **AC4** — When `grep -n "keeps every other kit" WIRE-INTO-PROJECT.md` runs, it names the upsert at
  each one-fragment step.
  Red when: the runbook omits it.

## 7. Gates

`settings-merge selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `check-wiring self-test` · `memory hygiene`

New arm: tools/settings-merge.py · covers AC1 AC2 AC3 · the sequential render staged against a render that writes the table from the call's fragment alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 46 (H8).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-82, TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam extended is `settings-merge.py`'s one-fragment call, which every caller already makes, and
`run_fragment_merges`' sorted population, whose order S2 adopts. The probe
`python tools/codebase-map/reuse_lookup.py "merge one hook fragment into an existing pack table"`
ranked `merge` (`tools/settings-merge.py`) and `run_fragment_merges` (`tools/govkit/govkit.py`), the
two this unit extends; no table merge exists beside them.

Recall terms used: `python tools/memory-recall/query.py "how does settings-merge wire one fragment per
govkit call" --terms "settings-merge fragment pack table hook-packs run_fragment_merges upsert
dispatcher entry render"`

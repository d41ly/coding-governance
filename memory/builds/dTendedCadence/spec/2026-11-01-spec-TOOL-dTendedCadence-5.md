# TOOL-dTendedCadence-5 — map freshness on the caller map, each stale dossier one keyed `regenerate stale` patch

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 11 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0446@617f13e8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md) | research | TOOL-dTendedCadence-7 TOOL-dTendedCadence-12 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |

<!-- /gen:spec-records -->

## 1. Goal

The map goes stale: 28 of 31 feature dossiers are older than the paths they claim (gap-maint-06,
research-maintain:85, PINNED there), and drift-audit's reading of it only reports. This unit makes
"map freshness" a Maintain reading that runs on its caller map, the core `code` record
TOOL-dTotalRecall-8 derives (v2:1990 `[owed]`), so an anchored dossier reads stale only when a
definition it anchors changed its body, and routes each stale dossier, under one stable key, to the
safe fix `regenerate stale` through `maintain.patch`.

## 2. Scope (IN)

Build-run preconditions: TOOL-dTotalRecall-8 S12, which makes `measure_dossier_staleness` read an
anchored dossier by body hash; TOOL-dTendedCadence-8 (the `[[reading]]` row, I3; the offender key, I5;
the patch intake, I6); TOOL-dTendedCadence-3 (the fix name `regenerate stale` and its `act-patch`
route, I11); and TOOL-dWellOiledMachine-27 S1, the intake filer I6 calls.

- **S1** — The reading on the caller map. `dossiers_older_than_their_paths`, read by
  `build_stale_dossiers` (`tools/drift-audit/drift_report.py:3441-3466`) through
  `read_stale_dossiers` (`:3423-3438`), which runs `map_diff.py --stale-dossiers --json`
  (`tools/codebase-map/map_diff.py:278-297`), which calls `measure_dossier_staleness`
  (`tools/codebase-map/map_lib.py:1812-1858`). Once TOOL-dTotalRecall-8 S12 lands, that rule reads a
  dossier whose `[paths]` table holds `symbols` keys `<path>::<qualified name>` as stale only when an
  anchored definition's body hash at HEAD differs from its hash at the dossier's last commit, and an
  unanchored dossier as today, by ancestry over its claimed paths. This unit adds no rule of its own:
  the reading takes the parent's rule as it lands, and the body-hash comparison inside it is the one
  TOOL-dTendedCadence-12 extracts as `check_body_moved` at its second caller, in the `extract_code` block
  (`tools/lib/extract_code.py` and its kit copies, TOOL-dTendedCadence-12 S1), since codebase-map imports
  no sibling kit; this reading calls it only through `measure_dossier_staleness`. Observed by AC1.
- **S2** — One stable key per stale dossier. `build_stale_dossiers` keeps, from each stale row the map
  returns, exactly `dossier`, `feature` and `refreshed`, the dossier's own last commit, in the map's
  most-behind-first order; the counts `behind` and `touched` and the sha `newest` stay in the map's own
  JSON, read there. So the offender key `render_drift_offenders` derives from the row (I5) is constant
  from the commit that stales a dossier until the commit that refreshes it, and `maintain.patch` files
  one intake per stale dossier and a `seen` clause on each later period, never a second intake (§8
  F1). Observed by AC2.
- **S3** — The row. The `[[reading]]` row (I3) of `dossiers_older_than_their_paths` in
  `tools/drift-audit/kit.toml` carries `scope = "repo"`, `kind = "dossier"` (TOOL-dTotalRecall-1's
  row, so the owner derives from the memory contract), and `fix = "regenerate stale"`, so a dossier in
  the act band routes `act-patch` (TOOL-dTendedCadence-3 S3) and `item.maintain.patch` files it
  through `python tools/runtime/intake.py file --origin cadence --filer item.maintain.patch` (I6), the
  intake rendered from the row: the dossier to refresh and the commit it was last refreshed at. Its
  pin stays the `drift-pins.txt` entry for the signal, 26 at this base
  (`tools/drift-audit/drift_signals.py:357`).
  Observed by AC3 and AC4.
- **S4** — The docs: the README signal table row for `dossiers_older_than_their_paths`
  (`tools/drift-audit/README.md:148`) says the detail rows are one per stale dossier keyed by the
  dossier and its last refresh, that the reading's fix is `regenerate stale` filed as a patch, and that
  an anchored dossier is read by body hash. Observed by AC5.

## 3. Non-goals (OUT)

- The staleness rule, the `symbols` key and the anchoring of any dossier: TOOL-dTotalRecall-8 S12,
  cited and run. No dossier gains anchors here; a `regenerate stale` patch build may add them as part of
  its refresh.
- The body-hash helper: TOOL-dTendedCadence-12 extracts it at its second caller as `check_body_moved` in
  the `extract_code` block (I16, its home refined by that unit's §8 F1 from `code_record.py`).
- The fix name, its route and the empty `maintain.fixes` case: TOOL-dTendedCadence-3.
- The intake's renderer, its key and the `seen` recurrence: TOOL-dTendedCadence-8 (I5, I6).
- The pin's value, the band edges on its `[[reading]]` row (TOOL-dTendedCadence-14 S1) and which offenders a period reaches
  once the value passes the pin: TOOL-dTendedCadence-14 and the pins' own drain, never this unit.
- `code_record.py --check`, the code record's own freshness leg: TOOL-dTotalRecall-8 S8 and S13.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — the `[[reading]]` row S3 is, the offender key (I5) S2 keeps stable, and `item.maintain.patch` with its intake (I6), the route a stale dossier takes; without them the reading files nothing
- **consumes-from** `TOOL-dTendedCadence-18` — `maintain.reading-tree` (I14): the reading is repo-scoped, so it is taken in the clean checkout at the base or in the node's worktree as that key says
- **consumes-from** `TOOL-dTendedCadence-3` — `regenerate stale`, the fix name S3's row declares, and its `act-patch` route
- **hands-off** `TOOL-dTendedCadence-12` — `measure_dossier_staleness`, whose body-hash comparison that unit extracts into `check_body_moved` and re-points this reading's rule at, AC1's verdict unchanged
- **consumes-from** external — TOOL-dTotalRecall-8 S12 (the anchored staleness rule) and TOOL-dWellOiledMachine-27 S1 (`intake.py file`)

## 4. Design

### Evidence

At this base `measure_dossier_staleness` (`tools/codebase-map/map_lib.py:1812-1858`) reads a dossier
as stale when a commit touching a path it claims is not an ancestor of the dossier's last commit,
path granularity only. `render_stale_dossiers` (`map_diff.py:183-212`) emits each row as `feature`,
`dossier`, `refreshed`, `stale`, `behind`, `newest`, and `build_stale_dossiers`
(`drift_report.py:3441-3466`) keeps every stale row whole as its detail. `render_drift_offenders`
(`:3985-4000`) keys a detail row by its JSON with sorted keys, dropping only line locators, so
today's key of a stale dossier carries `behind` and `newest`, which move with every commit that
touches a claimed path. The signal is report-only, pinned at 26 (`drift_signals.py:352-357`) with a
shrink-only `RATCHETS` row (`:460`). TOOL-dTotalRecall-8 S12 is the "caller map" of v2:1990: its
record replaces the optional symbols and callers (v2:1774, cl-0219), and its §1 records that no caller
index exists today.

### The key, and what the patch reads

| Field | In the key | Why |
|---|---|---|
| `dossier` | yes | the thing the patch refreshes |
| `feature` | yes | the map's own name for it, constant with the path |
| `refreshed` | yes | the dossier's last commit: constant while it is stale, and the base the patch build reads the change from |
| `behind`, `touched`, `newest`, `stale` | no | each moves with a commit touching a claim, or is constant; `map_diff.py --stale-dossiers` still prints them |

The patch build regenerates the dossier from what moved since `refreshed`, and its landing moves
`refreshed`, which ends the key: the next staleness of that dossier is a new key and a new patch.

### Inventory

No name minted: the row's fields are I3's, the fix name I11's, the patch item I6's.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/kit.toml`
- `tools/drift-audit/README.md`

### Alternatives rejected

- **The row kept whole** (§8 F1 option b). Rejected by S2's test: two periods with one more commit
  touching a claimed path between them give two different keys for one dossier, so `maintain.patch`
  files a second intake while the first is open.
- **A per-signal key declaration in `render_drift_offenders`** (§8 F1 option c). Rejected: it changes
  I5, TOOL-dTendedCadence-8's shared spelling, for one reading whose row can carry a stable key itself.
- **A freshness rule of this unit's own over the code record.** Rejected: `measure_dossier_staleness` is
  the map's one answer to which dossier owns a path (its docstring, `map_lib.py:1828-1829`), and a
  second rule would let the map and Maintain disagree.
- **Anchoring every dossier in this unit.** Rejected: it rewrites 31 dossiers' content outside a
  reading's mechanism; anchoring is what a refresh does, inside the patch the reading files.

## 5. Production-readiness checklist

- security — N/A: the reading reads git history and the map; the patch is filed through the intake
  filer, whose write surface TOOL-dWellOiledMachine-27 priced.
- perf / scale — one `map_diff.py --stale-dossiers` run, today's cost; the narrowed rows cost nothing.
- error / empty / loading states — unchanged from `build_stale_dossiers`: not asked with no map kit or
  no adopted map, dead probe on a shallow clone or a garbled answer (`drift_report.py:3441-3466`).
- observability — the detail rows name each stale dossier and its last refresh; the map's JSON keeps
  the counts.
- risks — a reader expecting `behind` in drift-audit's detail: none at this base, the one arm reads
  `feature` (`tools/drift-audit/selftest.py:3246-3292`).
- testing — S2's arm in drift-audit's selftest; §7 New arm.
- migration — N/A: no stored record changes shape; `drift-history.tsv` keys on the signal name.
- user docs — drift-audit's README signal table (S4); no `help/` page covers drift-audit at this base.

## 6. Acceptance criteria

The map fixture is TOOL-dTotalRecall-8 AC9's: a scratch git repository under `%TEMP%` with a short
name, an adopted codebase map, `a.py` defining `f` and `g`, and a dossier whose `[paths]` table holds
`symbols = ["a.py::f"]`, committed after `a.py`. The probe imports the worktree's `drift_report` and
calls `build_stale_dossiers` with a namespace ctx whose `root` is the fixture and whose `pins` hold the
signal at 0.

- **AC1** — When the probe's `build_stale_dossiers` runs after a commit changing only `g`'s body, it
  reads value 0; after a commit changing `f`'s body, it reads value 1, its one detail row naming the
  dossier.
  Red when: the commit to `g` stales the anchored dossier, path granularity read for an anchored one.
  fixture: needs TOOL-dTotalRecall-8 S12 landed; before it, the first commit stales the dossier.
- **AC2** — When the probe's `build_stale_dossiers` runs after a further commit changing `f`'s body
  again, its detail row is byte-identical to AC1's, `dossier`, `feature` and `refreshed` and no other
  field; after a commit refreshing the dossier, value 0.
  Red when: the row carries `behind` or `newest`, so its key moves with a commit touching a claim.
- **AC3** — When `grep -n -A6 'name = "dossiers_older_than_their_paths"' tools/drift-audit/kit.toml`
  runs, the row carries `scope = "repo"`, `kind = "dossier"` and `fix = "regenerate stale"`.
  Red when: the row lacks the fix, so a stale dossier is filed as an ask.
- **AC4** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs over the map fixture
  with the stale dossier in the act band, it routes `dossiers_older_than_their_paths` `act-patch` to
  the patch item; a second dry run after a further commit to `f` routes the same key.
  Red when: the dossier routes `act-file`, or the two runs route two keys.
  fixture: needs TOOL-dTendedCadence-1, -3, -8 and -14 built; the row carries `edges = [0, 0]` and the
  fixture's pin sits one below its stale count, so the one stale dossier over it is in the act band.
- **AC5** — When `grep -n "regenerate stale" tools/drift-audit/README.md` runs, the
  `dossiers_older_than_their_paths` row matches.
  Red when: the README still calls the reading report-only with no fix.

## 7. Gates

`drift-audit selftest` · `policy fixtures` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC2 · `test_stale_dossiers` gains a canned row carrying `behind` and `newest` and asserts the detail keeps `dossier`, `feature` and `refreshed` only, staged by returning the row whole · none

## 8. Open questions

- **F1 — How does a stale dossier keep one key while its patch is open?** (a) The detail row narrowed
  to `dossier`, `feature` and `refreshed`; (b) the row kept whole, as today; (c) a declaration of key
  fields per signal in `render_drift_offenders`. The test: across two periods with a commit touching a
  claimed path between them, does the dossier keep one key? (b) does not, since `behind` and `newest`
  move, so `maintain.patch` files a second intake for one dossier, against the patch item's "none
  where a patch is open for the same key" (layer-expansions:225); (c) changes I5 for every reading to
  serve one; (a) keeps the key and every field a patch build needs. Rung 3, the most feature-rich
  survivor. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F2 — What does "map freshness runs on its caller map" ask of this unit?** (a) The reading runs
  `measure_dossier_staleness` as TOOL-dTotalRecall-8 S12 lands it, the code record's body hashes
  deciding an anchored dossier; (b) a rule of this unit's own over the code record. v2:1990 names the
  caller map as dTotalRecall's, and v2:1774 cl-0219 makes the code record that map, so (a) is v2's
  answer. Rung 1. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.

## 10. Reuse audit

The seams extended: `build_stale_dossiers` and `read_stale_dossiers`
(`tools/drift-audit/drift_report.py:3423-3466`), whose detail rows this unit narrows;
`measure_dossier_staleness` (`tools/codebase-map/map_lib.py:1812`) as TOOL-dTotalRecall-8 S12 changes
it, read through `map_diff.py --stale-dossiers --json` (`tools/codebase-map/map_diff.py:278-297`);
and I3, I5, I6 and I11 from this build's siblings. The probe `python
tools/codebase-map/reuse_lookup.py "read feature dossiers as stale when a claimed definition body
changed"` ranked name-stem neighbours first (`read`, `read_text`, `claims`) and named
`measure_dossier_staleness`, `build_stale_dossiers`, `read_stale_dossiers` and `render_stale_dossiers`
among its candidates, the seams above; no new seam is needed. Where records disagree with source at
this base: TOOL-dTotalRecall-8 S12 cites `measure_dossier_staleness` at `map_lib.py:1798`, and it is at
`:1812`, as scout C's record says; its `:3423-3470` (the function ends at `:3466`), `drift_signals.py:357` and `:460` hold.

Recall terms used: `python tools/memory-recall/query.py "how is a dossier read as stale against the
code record and refreshed by a patch" --terms "dossier stale measure_dossier_staleness anchored symbols
body hash code record caller map regenerate patch"`

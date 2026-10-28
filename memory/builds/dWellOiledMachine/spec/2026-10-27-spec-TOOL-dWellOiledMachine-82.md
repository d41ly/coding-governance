# TOOL-dWellOiledMachine-82 — govkit's stale probe asks the pack table whether a fragment was wired, so a pre-existing guard is never recorded as added

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 13 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-82-deviation-821.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-82-deviation-821.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 18, item H3, at HIGH. `run_fragment_merges` decides whether a fragment that fails `--check`
was already wired by running `--unwire` on a scratch copy of settings and comparing the settings
bytes before and after (`tools/govkit/govkit.py:6158-6167`). Under TOOL-dWellOiledMachine-10 the
truth lives in the pack table and settings holds one dispatcher entry per event whose matcher is the
union of the packs', so unwiring a fragment whose events other packs share leaves settings
byte-identical. TOOL-dWellOiledMachine-71 S3 only copies the table into the scratch directory and
still compares settings. A wired fragment then reads `stale=False`, is recorded as ADDED (`:6175`),
and a later rollback (`remove_wired_fragments`) unwires a kit's hooks that existed before the update,
silently dropping a guard. This unit makes the probe compare the scratch pack table too.

## 2. Scope (IN)

- **S1** — The probe reads the table. In `run_fragment_merges`' stale probe, `stale` is true when the
  scratch `--unwire` changed the scratch settings copy OR the scratch copy of the pack table that
  71 S3 places beside it: a fragment with rows in the table was wired before, whatever the settings
  render shows. Only a fragment with no rows in the table and no settings entry is recorded in
  `added`. Observed by AC1, AC2.
  **Readers:** by name: `tools/govkit/govkit.py` (`run_fragment_merges`, the one probe). by value:
  `remove_wired_fragments` (`tools/govkit/govkit.py:6180`), which unwires exactly the `added` set this
  probe decides.
- **S2** — An absent table is no evidence. Where the target holds no pack table yet, the probe reads
  the settings comparison alone, as today, so a target adopted before TOOL-dWellOiledMachine-10 keeps
  its reading. Observed by AC3.

## 3. Non-goals (OUT)

- No change to where the table lives or how a fragment is spelled: finding 60 (M28), carried by the
  minors batch TOOL-dWellOiledMachine-90; this unit uses the location 71 S3 copies.
- No change to `remove_wired_fragments` or to the rollback order.
- No change to settings-merge's `--check`, `--unwire` or upsert: 71 S1 to S3 stand.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-71` — S3's one-fragment `--unwire` and the scratch copy of the pack table its probe makes, which this unit reads
- **hands-off** `TOOL-dWellOiledMachine-94` — AC2's rollback and the stale probe's table and exit handling (findings 1, 10, 33, 40)

## 4. Design

### Evidence

- The probe writes the target's settings into a scratch `settings.json`, runs `--unwire --fragment <p>`
  there, and sets `stale = probe.read_bytes() != (target / settings).read_bytes()`
  (`tools/govkit/govkit.py:6158-6167`); a non-stale fragment is appended to `added` (`:6175-6176`).
- 10 S3 renders one dispatcher entry per event, its matcher the union of the packs' matchers and its
  command `dispatch.js <Event>` (`spec-10.md:54-61`), so removing one pack whose events and matchers
  others carry leaves the entry unchanged.
- 71 S3 copies the pack table beside the settings copy and keeps the settings compare
  (`spec-71.md:38-43`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `shared-event-rewire`, `no-table` | `tools/govkit/selftest.py` cases | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/selftest.py`: the two cases

### Alternatives rejected

- **A `settings-merge.py --has-rows --fragment <f>` verb.** It adds a verb for a fact the probe's own
  scratch table already shows by its bytes.

## 5. Production-readiness checklist

- security — a rollback never removes a guard the update did not add.
- perf / scale — one more file read and compare per probed fragment.
- error / empty / loading states — S2's absent table keeps today's reading.
- observability — the `wired` line keeps its `(a stale command rewritten)` suffix, now true for a
  fragment the table held.
- risks — none beyond the probe's existing scratch copy.
- testing — AC1 to AC3 and the arm in §7.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When the `shared-event-rewire` fixture case, on its §7 `New arm:` line, wires fragments A and B
  whose packs share one event and matcher, changes A's pack, and runs an update of A's kit, the
  returned `added` map is empty and the line reads `(a stale command rewritten)`.
  Red when: A is recorded as added because the settings bytes did not move.
- **AC2** — When the same case then runs `govkit.py rollback` on A's kit, B's rows and A's original rows stay in the
  table.
  Red when: the rollback unwires A's pre-existing hooks.
- **AC3** — When the `no-table` fixture case, on its §7 `New arm:` line, updates a target holding settings and no pack table, a fragment
  with no settings entry is recorded as added.
  Red when: the absent table makes every fragment read as stale.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the shared-event case staged against a probe comparing settings bytes alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  18 (H3).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is `run_fragment_merges`' own scratch probe (`tools/govkit/govkit.py:6158-6167`),
given the second file it already copies under 71 S3. The probe `python
tools/codebase-map/reuse_lookup.py "decide whether a fragment was already wired before a merge"`
ranked `merge` (`tools/settings-merge.py`) and `wired` (`tools/check-wiring.sh`); neither reads the
pack table, so the probe is extended in place.

Recall terms used: `python tools/memory-recall/query.py "how does govkit tell a stale fragment from an
added one" --terms "run_fragment_merges stale probe unwire scratch settings pack table added rollback
remove_wired_fragments"`

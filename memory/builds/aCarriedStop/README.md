---
slug: aCarriedStop
node: a
opened: 2026-11-13
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3 TOOL-aCarriedStop-4 TOOL-aCarriedStop-5 TOOL-aCarriedStop-6 TOOL-aCarriedStop-7 TOOL-aCarriedStop-8 TOOL-aCarriedStop-9 TOOL-aCarriedStop-10
---

# aCarriedStop — a build run carries the owner's ended spec-audit chain past the dispatch gate through a recorded row

## The problem this build exists to solve

Past `SPEC_FOLD_CUTOFF`, `--dispatch` refuses every pass while the spec-audit chain verdict is not
STOP, and the verdict reads only the build's tracked `-chain-rounds.md` record. A chain build whose
spec run audited and landed before that record existed has none, so its build run reads every live
spec as unreviewed and dispatches nothing, although the owner ended that chain in a tracked prompt
record. The only remedy the gate names is a re-audit of every spec. `--close` has an override for
this case and the dispatch gate has no counterpart. The prompt is recorded under `prompts/`.

## Expected improvements

- A build run passes the dispatch gate on the owner's recorded chain stop, with no README or
  run-state edit and no re-audit.
- The stop is one row in the record the verdict already reads, citing the owner's tracked record.
- With no such row the gate refuses as it does today.

## Detriments if this is not built

- Every chain build run started past the cutoff with `spec-audit:` declared stops at its first unit.
- Each stop costs the owner a hand edit of a README key and a pinned run fact.
- The hand edit erases the declaration that the audit ran, so `specs-audited` reads not owed.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: it changes the unattended kit's
  contract. One mechanism: the owner-stop row, with its writer, its reading and its verb entry.
- **Stands alone, outside the chain.** It is no row of the dClosedLoop design.
- `memory/builds/dDeclaredLoop/` and its run branch are never written: a live run holds them.
- No new check number: every refusal is a value of check 118's one site.
- Kit versions move through the lander's `mint`, once, after the unit.
- No spec audit: none is declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aCarriedStop-1` | the owner-stop row: `--record-round` appends it citing the owner's tracked record, and the one chain verdict `--dispatch` and `--chain-verdict` share reads it as STOP |
| 2 | `TOOL-aCarriedStop-2` | promoted from the closing review's HIGH: the owner-stop path is held to one rule, so the writer admits no path its reader refuses |
| 3 | `TOOL-aCarriedStop-3` | promoted from the closing review: its remaining mediums and its lows, batched |
| 4 | `TOOL-aCarriedStop-9` | added on the owner's order of 2026-11-14: the routed-commits leg's ceiling raised over a recorded reading, so the close's bar can finish it |
| 5 | `TOOL-aCarriedStop-10` | adopted at the third close under M10: the chain-packet door reaches the memory-tree kit through `resolve_kit_dir`, so the install-prefix leg the close and the push bar run is green |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node a · opened 2026-11-13 · streams tooling
ids TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3 TOOL-aCarriedStop-4 TOOL-aCarriedStop-5 TOOL-aCarriedStop-6 TOOL-aCarriedStop-7 TOOL-aCarriedStop-8 TOOL-aCarriedStop-9 TOOL-aCarriedStop-10

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aCarriedStop-2 — the owner-stop path answers to one class: the writer refuses, before any byte, a whole path its reader's grammar would not admit](spec/2026-11-13-spec-TOOL-aCarriedStop-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-11-13 |
| [TOOL-aCarriedStop-3 — the closing review's mediums and lows, batched: the count test on the audit route only, the owner-stop arms the suite lacks, the base driver's reading and the usage header's padding](spec/2026-11-13-spec-TOOL-aCarriedStop-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-11-13 |
| [TOOL-aCarriedStop-9 — the routed commits leg's ceiling raised to 3540 s over its recorded contended readings, so the close's bar can finish it](spec/2026-11-14-spec-TOOL-aCarriedStop-9.md) | 4 | 1 | CLOSED | rev-1 | 2026-11-14 |
| [TOOL-aCarriedStop-10 — the chain-packet door reaches the memory-tree kit through `resolve_kit_dir`, so the install-prefix leg reads no spelled kit path in it](spec/2026-11-14-spec-TOOL-aCarriedStop-10.md) | 5 | 1 | CLOSED | rev-1 | 2026-11-14 |
| [TOOL-aCarriedStop-1 — the owner-stop row: `--record-round --owner-stop` appends it citing the owner's tracked record, and the one chain verdict reads it as STOP](spec/2026-11-13-spec-TOOL-aCarriedStop-1.md) | — | 2 | CLOSED | rev-2 | 2026-11-13 |
<!-- /gen:build-units -->

Records: 28 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aCarriedStop-1 TOOL-aCarriedStop-2 TOOL-aCarriedStop-3 TOOL-aCarriedStop-10 TOOL-aCarriedStop-9.

Ids whose spec moved past its audited revision: none — 0 of 5 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 2 | `TOOL-aCarriedStop-2` | no |
| 3 | `TOOL-aCarriedStop-3` | no |
| 4 | `TOOL-aCarriedStop-9` | no |
| 5 | `TOOL-aCarriedStop-10` | no |

Unordered: `TOOL-aCarriedStop-1`.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

---
slug: aCarriedStop
node: a
opened: 2026-11-13
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aCarriedStop-1
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-11-13 · streams tooling
ids TOOL-aCarriedStop-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aCarriedStop-1 — the owner-stop row: `--record-round --owner-stop` appends it citing the owner's tracked record, and the one chain verdict reads it as STOP](spec/2026-11-13-spec-TOOL-aCarriedStop-1.md) | — | 2 | INPROGRESS | rev-2 | 2026-11-13 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aCarriedStop-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

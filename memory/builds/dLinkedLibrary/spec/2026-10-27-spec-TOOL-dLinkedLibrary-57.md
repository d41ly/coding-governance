# TOOL-dLinkedLibrary-57 — the reuse-lookup step's witness keyed on the `MAP_CLI` value its before-image recorded

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 26 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-57-deviation-571.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-57-deviation-571.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 4 at HIGH**, report item **H2**. Id 29 shares the item and is its own unit,
`TOOL-dLinkedLibrary-58`.

`TOOL-dLinkedLibrary-42` S2 tightens the `codebase-map/retire-reuse-lookup` step's witness to exit 0 only
when `house_index.py` exists and `MAP_CLI` names it. The step lives in `tools/codebase-map/kit.toml`
(`TOOL-dLinkedLibrary-3` S6), a kit that requires only `memory-tree` (:7). `MAP_CLI` is the unattended
kit's key, and its shipped example reads `MAP_CLI=""` (`tools/unattended/.unattended.conf.example:202`),
while `up` re-points only a `MAP_CLI` that names the lookup. So a codebase-map adopter with a blank
`MAP_CLI` gets a witness that exits 1 on every update, and the step fails or repeats for ever.

This unit keys the witness on the `MAP_CLI` value the step's before-image recorded: unit 3's witness
where that value named no lookup, unit 42's where it named the lookup. It repairs `TOOL-dLinkedLibrary-42`
and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — The recorded value. `retire_reuse_lookup.py up` (`tools/govkit/steps/retire_reuse_lookup.py`,
  `TOOL-dLinkedLibrary-3` S6) reads `MAP_CLI` from the `.unattended.conf` bytes its before-image keeps
  (TOOL-dSafePassage-1 §4, `.governance/steps/<entry>/<slug>.before.json`), the last `MAP_CLI=` line
  winning, a value in double quotes or bare. Observed by AC1.
- **S2** — The witness table, `witness` reading the value S1 reads from the image and the target's
  `MAP_CLI` now:

  | `MAP_CLI` in the before-image | `witness` exits 0 when |
  |---|---|
  | blank, or no `MAP_CLI=` line | both lookup files are absent and `MAP_CLI` names no lookup |
  | names the lookup | both files are absent, `{prefix}/codebase-map/house_index.py` exists, and `MAP_CLI` names it |
  | names any other file | both files are absent and `MAP_CLI` is unchanged |

  Any other state exits 1 naming the file or the value. Observed by AC1, AC2 and AC3.
- **S3** — `up` keeps 42's re-point: it rewrites only a `MAP_CLI` naming the lookup, and leaves a blank
  or foreign value byte for byte. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- A target holding no `.unattended.conf` at all: `TOOL-dLinkedLibrary-58`'s (id 29), the same table's
  absent-file row.
- Which file `MAP_CLI` names in gov's own conf: `TOOL-dLinkedLibrary-42` S1, unchanged.
- `down`: it restores the before-image as TOOL-dSafePassage-1 §4 states, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-42` — S2's re-point of `MAP_CLI` and its tightened `witness`, which S2 keys on the before-image (id 4)
- **consumes-from** `TOOL-dLinkedLibrary-3` — `retire_reuse_lookup.py` and its before-image, which S1 reads (id 4)
- **hands-off** `TOOL-dLinkedLibrary-69` — S1's read of `MAP_CLI` and S2's witness table, which unit 69 re-points onto `read_map_cli` (id 19 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-70` — S3's re-point rule for `up`, which unit 70 tests through `read_map_cli` and widens to every spelling (id 35 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — the before-image read and the witness, which unit 74 completes (ids 13, 36 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/codebase-map/kit.toml:7`: `requires = ["memory-tree"]`; `tools/unattended/kit.toml:12` requires
  memory-tree, review-harness, settings-merge and kickoff-manifest, so the map installs without the
  unattended kit.
- `tools/unattended/.unattended.conf.example:202`: `MAP_CLI=""`.
- TOOL-dSafePassage-1 §4 "The before-image": every path an up will write or remove, with its bytes,
  base64, `null` for absent; an existing image is never overwritten.

### Rollout

Order 26 beside `TOOL-dLinkedLibrary-58` and `TOOL-dLinkedLibrary-40`. This unit and unit 58 both write
`retire_reuse_lookup.py`, so BUILD-METHOD M6's clause 1 sequences the two passes; each owns its own rows
of S2's table and neither reads the other's output.

### Files touched (estimate)

- `tools/govkit/steps/retire_reuse_lookup.py`: S1 to S3

### Alternatives rejected

- **The witness reads the target's `MAP_CLI` alone.** A blank value after `up` cannot tell an adopter
  that never declared the map from one whose re-point was undone; the image records which it was.
- **`up` writes `MAP_CLI` for every map adopter.** It declares the unattended kit's key in a tree that
  may not hold that kit, a write surface the step's `surfaces` line does not price.

## 5. Production-readiness checklist

- security — the witness reads; `up`'s write set is 42's, unchanged.
- perf / scale — one more read of a file the image already holds.
- error / empty / loading states — an image that does not parse exits 1 naming it.
- observability — each non-zero witness names the row of S2 it failed and the value it read.
- risks — an operator who hand-edits `MAP_CLI` after `up` gets a witness that names the edit.
- testing — AC1 to AC3 over scratch targets.
- migration — S2 is the step's own migration contract.
- user docs — none under `help/`: the step program's docstring states the table.

## 6. Acceptance criteria

- **AC1** — When `python retire_reuse_lookup.py up <target>` runs over a scratch target
  under `%TEMP%/rl57a` holding both lookup files, `house_index.py` and a `.unattended.conf` reading
  `MAP_CLI=""`, then `witness <target>`, the witness exits 0 and `MAP_CLI=""` is unchanged.
  Red when: a blank `MAP_CLI` fails the witness.
- **AC2** — When the target under `%TEMP%/rl57b` holds a `MAP_CLI` line naming the map kit's
  `reuse_lookup.py` by its repository path, `up` re-points it to `house_index.py` and `witness` exits 0; with `house_index.py` then removed, `witness`
  exits 1 naming it.
  Red when: the lookup-naming row passes over a `MAP_CLI` that names nothing.
- **AC3** — When the target under `%TEMP%/rl57c` holds a `MAP_CLI` line naming another kit's `cli.py`
  under `tools/other`, `up` leaves it and
  `witness` exits 0; with `MAP_CLI` hand-edited back to the lookup after `up`, `witness` exits 1 naming
  the value.
  Red when: a foreign value is rewritten, or a re-named lookup passes.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the step program has no test home at base, since `tools/govkit/steps/` is absent until
unit 3 and TOOL-dSafePassage-1 land, so AC1 to AC3 are this pass's probes over scratch targets.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 3 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 4 (HIGH, item
  H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-69, TOOL-dLinkedLibrary-70, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-1's before-image, which every step's `up` writes and which already
holds `.unattended.conf`'s prior bytes; the witness reads it rather than adding a record. `python
tools/codebase-map/reuse_lookup.py "find which kit directory an installed file lives in"` ranked
`resolve_kit_dir`, `kit_rel` and `kit_dir`; the witness tests a repo-relative conf value with a file test,
so none is the seam here, and no existing seam fits beyond the image and the step being repaired.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`

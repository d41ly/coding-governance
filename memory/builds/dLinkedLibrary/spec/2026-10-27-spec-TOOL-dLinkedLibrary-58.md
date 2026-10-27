# TOOL-dLinkedLibrary-58 — the reuse-lookup step over a target that holds no `.unattended.conf`: nothing created, the witness green

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 26 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-58-deviation-581.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-58-deviation-581.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 29 at HIGH**, report item **H2**. Id 4 shares the item and is its own unit,
`TOOL-dLinkedLibrary-57`.

Id 29 is the failure-envelope half of the item. The `codebase-map/retire-reuse-lookup` step sits in
`tools/codebase-map/kit.toml` (`TOOL-dLinkedLibrary-3` S6), and that kit requires only `memory-tree`
(:7), so the map installs into targets that hold no unattended kit and no `.unattended.conf`.
`TOOL-dLinkedLibrary-42` S2's witness demands that `MAP_CLI` names `house_index.py`, which such a target
never holds, so its witness exits 1 on every update. 42's §5 places that failure on adopters "without
the codebase-map kit", the one population where the step never runs, and its AC2 plants only a target
holding `MAP_CLI`.

This unit states the absent-file case end to end: `up` creates no conf, the before-image records the
file absent, the witness reads absence as a conf naming no lookup, and `down` leaves the file absent. It
repairs `TOOL-dLinkedLibrary-42` and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — `up` over a target with no `.unattended.conf`: the before-image records the path with bytes
  `null` (TOOL-dSafePassage-1 §4), `up` takes out the two lookup files exactly as unit 3's S6 states,
  whose S1 answers for their readers, writes no `.unattended.conf`, and exits 0. Observed by AC1.
- **S2** — The witness's absent-file row. Where the before-image holds `.unattended.conf` as `null` and
  the target holds none now, `witness` exits 0 when both lookup files are absent; where the target holds
  a conf now that the image recorded absent, `witness` exits 0 only when that conf's `MAP_CLI` names no
  lookup, and 1 naming the value otherwise. Observed by AC1 and AC2.
- **S3** — `down` over that image restores the two files and leaves `.unattended.conf` absent, deleting
  nothing `up` did not write. Observed by AC1.
- **S4** — The risk stated where it lives. The step program's docstring names the population: a
  codebase-map adopter without the unattended kit holds no `.unattended.conf`, and the step passes there.
  Observed by AC3.

## 3. Non-goals (OUT)

- A conf that exists with a blank, lookup-naming or foreign `MAP_CLI`: `TOOL-dLinkedLibrary-57`'s rows
  (id 4).
- The step's `surfaces` line: `conf-key:.unattended.conf#MAP_CLI` stays, read by TOOL-dSafePassage-1 as
  a surface the step may touch, never one it must find.
- Seeding `.unattended.conf` in a map-only target: the unattended kit's adopter owns that file.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-42` — S2's tightened `witness`, whose absent-file case S2 states (id 29)
- **consumes-from** `TOOL-dLinkedLibrary-3` — `retire_reuse_lookup.py`, its `up`, `down` and before-image, which S1 and S3 run over a target with no conf (id 29)
- **hands-off** `TOOL-dLinkedLibrary-74` — the absent-conf image and `down`, which unit 74 completes (id 37 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/codebase-map/kit.toml:7`: `requires = ["memory-tree"]`.
- `tools/unattended/kit.toml:12`: the unattended kit requires memory-tree, review-harness, settings-merge
  and kickoff-manifest, and `.unattended.conf` is its file.
- TOOL-dSafePassage-1 §4 "The before-image": bytes base64, `null` for absent; a down restores each path
  only where its bytes are the image's after-hash or before bytes, else exits 1 naming it.

### Rollout

Order 26 beside `TOOL-dLinkedLibrary-57` and `TOOL-dLinkedLibrary-40`. This unit and unit 57 both write
`retire_reuse_lookup.py`, so BUILD-METHOD M6's clause 1 sequences the two passes; S2 here is the
absent-file row of unit 57's table and neither reads the other's output.

### Files touched (estimate)

- `tools/govkit/steps/retire_reuse_lookup.py`: S1 to S4

### Alternatives rejected

- **The step moved into the unattended kit.** It would stop removing the two lookup files in a map-only
  target, which is the codebase-map kit's own retirement.
- **`up` writes a `.unattended.conf` holding `MAP_CLI=""`.** It installs one kit's conf from another kit's
  step, an install surface the clause does not price.

## 5. Production-readiness checklist

- security — `up` writes less than before over this target; nothing new is created.
- perf / scale — none.
- error / empty / loading states — an absent conf is a stated row, never an exception.
- observability — `up` prints `no .unattended.conf — MAP_CLI not declared here` once.
- risks — a codebase-map adopter that later adopts the unattended kit gets that kit's example conf, whose
  `MAP_CLI` the unattended adopter sets, not this step.
- testing — AC1 to AC3 over a scratch target.
- migration — S1 to S3 are the step's own behaviour on the absent case.
- user docs — none under `help/`: S4's docstring.

## 6. Acceptance criteria

- **AC1** — When `python retire_reuse_lookup.py up <target>` runs over a scratch target
  under `%TEMP%/rl58` holding both lookup files and `house_index.py` and no `.unattended.conf`, it exits
  0, `test -e <target>/.unattended.conf` fails, `witness <target>` exits 0, and `down <target>` restores
  both files and leaves no `.unattended.conf`.
  Red when: the step creates, requires or fails on the absent conf.
- **AC2** — When the same target gains, after `up`, a `.unattended.conf` whose `MAP_CLI` line names the
  map kit's `reuse_lookup.py` by its repository path, `witness <target>` exits 1 naming the value.
  Red when: a lookup-naming value written after `up` passes.
- **AC3** — When `grep -n "unattended.conf"` runs over the step program `retire_reuse_lookup.py` (its path
  in Files touched), it prints the docstring sentence naming the map-only population.
  Red when: the step's own text places the failure on adopters without the map.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the step program has no test home at base, since `tools/govkit/steps/` is absent until
unit 3 and TOOL-dSafePassage-1 land, so AC1 to AC3 are this pass's probes over a scratch target.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 3 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 29 (HIGH, item
  H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-1's before-image and its `null` for an absent path, which already
expresses "this file was not here"; the step reads it rather than probing the unattended kit. `python
tools/codebase-map/reuse_lookup.py "find which kit directory an installed file lives in"` ranked
`resolve_kit_dir`, `kit_rel` and `kit_dir`; none answers whether a conf existed before an upgrade, so no
existing seam fits beyond the image and the step being repaired.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`

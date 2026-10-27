# TOOL-dLinkedLibrary-38 — several reuse parts per feature, so each dossier seam becomes its own entry

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 11 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-26-build-TOOL-dLinkedLibrary-38-deviation-381.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-38-deviation-381.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 1 at HIGH**, report item **R2**. No other id shares the item.

`TOOL-dLinkedLibrary-19` S3 files each of the 82 `seam:` lines as `propose --feature <feature> --name
<feature>-<ordinal>`, several entries per dossier. `TOOL-dLinkedLibrary-1` S1 to S3 make `--feature` a
bare flag and a feature part exactly `<feature>.reuse.toml` beside `<feature>.md`, tag
`unit.reuse.<stem>` and `reuse.tag` `feature.<stem>`. An accepted `alpha-1.reuse.toml` is red under
`check_reuse_entries`, since no `alpha-1.md` exists and `feature.alpha-1` is no feature node, and the
reuse view and the anchor join read its entry under the wrong feature.

This unit settles one model in both: a feature holds several parts, `<feature>.<n>.reuse.toml`, keyed to
the feature by the file name's stem before its first dot, and `--feature` stays the bare flag. It repairs
`TOOL-dLinkedLibrary-19` and builds one step after it (order 11).

## 2. Scope (IN)

- **S1** — The part name. A feature part is `memory/map/features/<feature>.reuse.toml` or
  `memory/map/features/<feature>.<n>.reuse.toml`, `<n>` a positive integer with no leading zero. Its file
  stem is the name less `.reuse.toml`, so its tag is `unit.reuse.<feature>.<n>`, a tag the grammar's
  `seg` admits. `check_reuse_entries` (`TOOL-dLinkedLibrary-1` S2) reads the feature as the stem's part
  before its first dot: the part's `reuse.tag` must be `feature.<feature>` and a dossier `<feature>.md`
  must sit beside it. A stem whose part after the first dot is not such an integer is refused, naming
  the part. Convention parts are unchanged. Observed by AC1 and AC2.
- **S2** — The proposal record. `reuse_entries.py propose --name <feature>.<n> --feature …` writes
  `<date>-build-<unit id>-reuse-proposal-<feature>-<n>.md`, the dot spelled as a hyphen because the
  record-name tail admits none (`REC_TAIL`, `tools/memory-tree/check-memory-hygiene.sh:577`), and refuses
  exit 2 when that record already exists, naming it. Observed by AC3.
- **S3** — The caller. `dossier_move.py apply` (`TOOL-dLinkedLibrary-19` S3) calls `python
  reuse_entries.py propose --feature --name <feature>.<ordinal>` for each `seam:` line, `--feature` the
  bare flag `TOOL-dLinkedLibrary-1` S3 spells; its fixture's stub records the names `alpha.1` and
  `alpha.2`. Observed by AC4.
- **S4** — The migration's proposals. Where `TOOL-dLinkedLibrary-19`'s pass filed proposals under the
  `<feature>-<ordinal>` name, this pass re-files each through S3's spelling and marks the earlier one
  `- **Disposition:** rejected <date> — re-filed as <feature>.<n> by TOOL-dLinkedLibrary-38` through
  `reuse_entries.py reject`, so no proposal is left that the owner could accept into a red part.
  Observed by AC5.

## 3. Non-goals (OUT)

- The entry's fields, its states and the owner's proof: `TOOL-dLinkedLibrary-1`'s, unchanged.
- The anchor join and the reuse view: they read `reuse.tag`, which S1 keeps `feature.<feature>`.
- Merging a dossier's seams into one part: §4 "Alternatives rejected".
- `apply`'s build and unit arguments: `TOOL-dLinkedLibrary-50`'s (id 65).

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-19` — `dossier_move.py apply`, whose `propose` call S3 re-spells and whose filed proposals S4 re-files (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-1` — `check_reuse_entries` and `propose`, whose feature rule S1 keys on the stem before the first dot and whose record name S2 fixes (id 1)
- **hands-off** `TOOL-dLinkedLibrary-52` — `<feature>.<n>`, the name unit 52's re-run of `apply` keys on (id 66)
- **consumes-from** `TOOL-dLinkedLibrary-60` — `propose`'s part name `<feature>.<n>` and S2's record name, which unit 60 lands at order 9, so S4 finds no hyphenated proposal to re-file (id 2 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — S4's re-filed proposals, whose names unit 64 keeps apart and counts (ids 19, 25 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-1` §4 "The entry" shows `memory/map/features/media-picker.reuse.toml` holding
  one `[[unit]]` with tag `unit.reuse.media-picker`, and S2 refuses a part holding other than one.
- The tag grammar is `<ns>.<seg>(.<seg>)*`, `seg` `[a-z0-9][a-z0-9-]*` (PLAY-dOrderedCharter-19 S1), so
  `unit.reuse.alpha.1` parses.
- At base no dossier name carries a dot (`ls memory/map/features`, 32 dossiers), and the dossiers hold
  82 `seam:` lines, PINNED at `5fede642` by `grep -c "^seam:"` over the folder.
- `REC_TAIL='(-[a-z0-9][a-z0-9-]*)?'` admits no dot in a record name's tail.

### The parts of one feature

```
memory/map/features/roles.md               the dossier, the feature.roles node
memory/map/features/roles.1.reuse.toml     unit.reuse.roles.1   reuse.tag = "feature.roles"
memory/map/features/roles.2.reuse.toml     unit.reuse.roles.2   reuse.tag = "feature.roles"
```

### Files touched (estimate)

- `tools/memory-tree/reuse_entries.py`: S1, S2, and their fixture cases
- `tools/codebase-map/dossier_move.py`: S3 and its stub's expectation
- `memory/builds/dLinkedLibrary/build/`: S4's re-filed proposal records and the earlier ones' dispositions

### Alternatives rejected

- **One part per feature holding every seam.** A part's `text` is one `MUST` line on a `line` budget; 82
  seams in 32 lines lose each seam's own `needs` and `anchors`, which the reuse view and the anchor join
  read per entry.
- **A valued `--feature <feature>` beside a free `--name`.** It spells the feature twice in one call,
  and a call where the two disagree needs its own refusal.

## 5. Production-readiness checklist

- security — no new write path: `propose` writes its record as before, and nothing under the map.
- perf / scale — one more split per part name; the parts read once per check.
- error / empty / loading states — a malformed ordinal and a re-filed record name each refuse, naming the
  part or record.
- observability — each refusal names the part; S4 prints every re-filed and rejected proposal.
- risks — 82 re-filed proposals reach the owner beside 82 rejected ones; the reuse view lists only the
  live ones.
- testing — AC1 to AC5 by fixture and probe.
- migration — S4.
- user docs — none under `help/`; `TOOL-dLinkedLibrary-1`'s docs name the part shape, and this pass
  amends that sentence where it names one part per feature.

## 6. Acceptance criteria

- **AC1** — When `python reuse_entries.py --fixture --plant feature-parts` runs `check` over a map holding
  `alpha.md`, `alpha.1.reuse.toml` and `alpha.2.reuse.toml`, each `reuse.tag` `feature.alpha`, it exits 0.
  Red when: a numbered part is read as the feature `alpha.1`, or two parts of one feature collide.
- **AC2** — When the plant holds `alpha.x.reuse.toml`, or `alpha.1.reuse.toml` whose `reuse.tag` is
  `feature.alpha.1`, `check` exits 1 naming the part.
  Red when: a malformed ordinal or a stem-shaped feature tag passes.
- **AC3** — When `python reuse_entries.py propose --name alpha.1 --feature …` runs twice in a scratch
  build, the first writes `…-reuse-proposal-alpha-1.md` and the second exits 2 naming it.
  Red when: the record name carries a dot, or a second proposal overwrites the first.
- **AC4** — When `python dossier_move.py --fixture --plant move` runs, the stub `propose` records the
  names `alpha.1` and `alpha.2` and the bare `--feature` flag.
  Red when: the call passes a value after `--feature`, or a hyphenated name.
- **AC5** — When `python reuse_entries.py check` runs at this pass's tip, it exits 0, and
  `git grep -l "Disposition:\*\* rejected .* re-filed as" -- memory/builds/dLinkedLibrary/build/` counts one record per
  proposal `TOOL-dLinkedLibrary-19` filed under a hyphenated name.
  Red when: a proposal under the old name is left live.
  figure: DERIVED at the pass from the proposals that unit filed; 0 where it filed none.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/reuse_entries.py · covers AC1 AC2 AC3 · the `feature-parts` plant with its malformed ordinal, the failing case staged by keying the feature on the whole stem · none
New arm: tools/codebase-map/selftest.py · covers AC4 · the `dossier_move.py --fixture` stub's recorded names, the failing case a hyphenated name · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 19 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Several parts per feature, or one part holding a dossier's seams?** Options: (a) numbered parts
  keyed by the stem before the first dot; (b) one part per feature, its seams merged. (b) loses each
  seam's `needs` and `anchors` (veto 1 against unit 5's per-entry rows). RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 1
  (HIGH, item R2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-60, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-1`'s `check_reuse_entries` and `propose` in
`tools/memory-tree/reuse_entries.py`, and `TOOL-dLinkedLibrary-19`'s `dossier_move.py apply`; the part
grammar reuses the tag grammar's `seg` and the record-name tail `REC_TAIL` rather than minting either.
`python tools/codebase-map/reuse_lookup.py "count the parts of a feature's reuse entries"` ranked
`counts`, `measure_typed_counts`, `build_counted_values` and `build_record_parts`, none a part-name
reader, so no existing seam fits beyond the two modules being repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`

---
slug: dTracedLattice
node: d
opened: 2026-09-05
streams: tooling
roster: TOOL
ids: TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5
---

# dTracedLattice — whether the codebase map should carry relations, and what its relation data is actually worth

## The problem this build exists to solve
The owner asked for relations in the codebase map and for the recall tools to read the map. Testing
the premise found the relation machinery already present and the reason it is uncommitted already
ratified, in `bConvergentLodestar` review finding 4, on a rate nobody had measured. Measuring it
refuted the stated reason and then a skeptic round refuted the measurement, which had described the
token reference index rather than the import graph the design proposed to commit. What survived is
narrower and worse: `reuse_lookup` ranks by a fan-in whose top band is right 7.2% of the time, and
`memory/TEMPLATE-SPEC.md` §10 makes citing that ranking mandatory for every Tier-2 spec. Four further
defects in the map kit were observed while measuring, none of them about relations.

## Expected improvements
- The mandatory §10 reuse probe stops ranking its worst answers first.
- `TOOL-aScouredKit-16` is amended before it is built, so the harmful half of it is not shipped.
- A gate that passes while comparing nothing announces the skip instead.
- Three claims in the record that are false at HEAD stop being cited as true.

## Detriments if this is not built
- Every Tier-2 spec keeps citing a seam chosen by a 7.2%-precision ranking, and the §10 audit keeps
  looking satisfied.
- `TOOL-aScouredKit-16` gets built as written, halving the precision it was filed to raise.
- The freshness gate keeps passing with a tier uncompared, on this tree and in every adopter.
- The map kit keeps writing an untracked file into a tracked directory.

## Build-level rules
- **The relations question is ANSWERED, and the answer is no.** Not on staleness grounds — those were
  measured weak at every granularity — but on `AGENTS.md` §12: every consumer is same-language and
  in-process, derivation is sub-second, and the artifact would be five kit-to-kit rows. No unit here
  commits a relation artifact, and a unit that wants to must first reverse §12, not finding 4.
- **Rev-1 of the dossier is wrong and is kept.** It recommended committing a coarse import graph on a
  measurement that described a different artifact. The record of what was refuted is the build's main
  value and is not to be tidied away.
- **No unit re-files an existing row.** `TOOL-aScouredKit-16` is AMENDED by unit 1's measurement;
  `TOOL-aProvenReuse-4` records its own refusal and its own cheap shape, and no unit re-proposes it.
  `drift_report.py` flags `live_backlog_rows_per_shard` at 268/4, so findings ride specs, not rows.
- **Units 2 to 5 are independent of unit 1 and of each other.** Their write sets do not intersect, so
  M6 clause 1 is satisfied and they may run concurrently. Unit 1 touches `map_lib.py` and
  `reuse_lookup.py`; unit 2 the gate; unit 3 `map_diff.py`; unit 4 the adopter; unit 5 the conf reader.

## Parked decisions
- **`TOOL-aSurfacedLexicon-2` is SPECCED at order 1 to delete this tree's only AST import resolver** —
  `resolve_import` plus seven functions, 164 lines, with a directional kit-to-kit rule. If a relation
  capability is ever wanted, that is the code. Rescuing it into `codebase-map` or letting it go is a
  cross-build decision this run has no authority to take, and the deletion is scheduled first.
- **Map coverage is capped by rule, not by effort.** 1303 of 1510 tracked files are unmapped, and
  `memory/map/README.md` says path globs are digest-only and shared mega-modules are never
  glob-claimed. So no path-keyed orientation feature can be worth much until that contract changes.
  The `attribute_paths` promotion and the recall annotation are parked on this, not abandoned.
- **The churn producer is not on disk.** The exhaustive 150-pair run is unreproducible from any named
  script; the analyzer re-runs and the raw records are self-describing. Anything depending on those
  figures re-derives them. Unit scope excludes rebuilding the harness.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dTracedLattice-1` | OPEN | fan-in stops counting homonyms and stops discarding real dotted references |
| 2 | `TOOL-dTracedLattice-2` | OPEN | the freshness gate announces a tier it did not compare |
| 3 | `TOOL-dTracedLattice-3` | OPEN | the reinvention backlog is tracked, or is not written into a tracked directory |
| 4 | `TOOL-dTracedLattice-4` | OPEN | an adopter's frozen gate copy is compared against the template that moved |
| 5 | `TOOL-dTracedLattice-5` | OPEN | a dark layer is derived from the corpus instead of asserted in prose |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 5 unit(s) · node d · opened 2026-09-05 · streams tooling
ids TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTracedLattice-1 — fan-in stops counting homonyms and stops discarding real dotted references](spec/2026-09-05-spec-TOOL-dTracedLattice-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-05 |
| [TOOL-dTracedLattice-2 — the freshness gate announces a tier it did not compare](spec/2026-09-05-spec-TOOL-dTracedLattice-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-09-05 |
| [TOOL-dTracedLattice-3 — the reinvention backlog is tracked, or is not written into a tracked directory](spec/2026-09-05-spec-TOOL-dTracedLattice-3.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-05 |
| [TOOL-dTracedLattice-4 — an adopter's frozen gate copy is compared against the template that moved](spec/2026-09-05-spec-TOOL-dTracedLattice-4.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-05 |
| [TOOL-dTracedLattice-5 — a dark layer is derived from the corpus instead of asserted in prose](spec/2026-09-05-spec-TOOL-dTracedLattice-5.md) | 5 | 2 | SPECCED | rev-1 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTracedLattice-1` | no |
| 2 | `TOOL-dTracedLattice-2` | no |
| 3 | `TOOL-dTracedLattice-3` | no |
| 4 | `TOOL-dTracedLattice-4` | no |
| 5 | `TOOL-dTracedLattice-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

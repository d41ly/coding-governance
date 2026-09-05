---
slug: dTracedLattice
node: d
opened: 2026-09-05
streams: tooling
roster: TOOL
ids: TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6
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
- **Rev-1 of the dossier is wrong and is kept.** It recommended a committed graph on a measurement
  that described a different artifact. What was refuted is the build's main value, not clutter.
- **No unit re-files an existing row.** Unit 1 AMENDS `TOOL-aScouredKit-16`; nothing re-proposes
  `TOOL-aProvenReuse-4`, which records its own refusal. `drift_report.py` already flags this repo's
  backlog over budget, so findings ride specs rather than new rows.
- **Three owner rulings, 2026-09-05, and each one closed a fork a run may not take.** The lexicon
  kit's AST import resolver is RESCUED into `codebase-map` before `TOOL-aSurfacedLexicon-2` deletes
  it, which is why unit 6 exists and takes order 1 across two builds. `RECALL_DARK_LAYERS` is
  re-declared in EXTENSIONS, with a migration and a refusal on the old spelling. The reinvention
  backlog moves OUTSIDE the worktree, reversing `bConvergentLodestar` F7: nobody has read rows in a
  file that never existed.
- **The units are SEQUENCED, and an earlier revision of this bullet claimed the opposite.** The write
  sets intersect on `map_diff.py`, on `reuse_lookup.py`'s banner, and on one row of
  `memory/backlog/TOOL.md` that M6 clause 3 forbids two passes to touch at all. Clauses 2 and 3
  govern, not clause 1, and the generated build-order block below is the authority. Each spec names
  the collision it carries.

## Parked decisions
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
| 6 | `TOOL-dTracedLattice-6` | OPEN | the AST import resolver is rescued before the lexicon kit deletes it |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 6 unit(s) · node d · opened 2026-09-05 · streams tooling
ids TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dTracedLattice-6 — the AST import resolver is rescued into codebase-map before P3 deletes it](spec/2026-09-05-spec-TOOL-dTracedLattice-6.md) | 1 | 2 | SPECCED | rev-1 | 2026-09-05 |
| [TOOL-dTracedLattice-1 — fan-in stops counting homonyms and stops discarding real dotted references](spec/2026-09-05-spec-TOOL-dTracedLattice-1.md) | 2 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-dTracedLattice-2 — the freshness gate announces a tier it did not compare](spec/2026-09-05-spec-TOOL-dTracedLattice-2.md) | 3 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-dTracedLattice-3 — the reinvention backlog is tracked, or is not written into a tracked directory](spec/2026-09-05-spec-TOOL-dTracedLattice-3.md) | 4 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-dTracedLattice-4 — an adopter's frozen gate copy is compared against the template that moved](spec/2026-09-05-spec-TOOL-dTracedLattice-4.md) | 5 | 2 | SPECCED | rev-4 | 2026-09-05 |
| [TOOL-dTracedLattice-5 — a dark layer is derived from the corpus instead of asserted in prose](spec/2026-09-05-spec-TOOL-dTracedLattice-5.md) | 6 | 2 | SPECCED | rev-4 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: TOOL-dTracedLattice-6.

Ids no `spec-audit` record has ever named: TOOL-dTracedLattice-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dTracedLattice-6` | no |
| 2 | `TOOL-dTracedLattice-1` | no |
| 3 | `TOOL-dTracedLattice-2` | no |
| 4 | `TOOL-dTracedLattice-3` | no |
| 5 | `TOOL-dTracedLattice-4` | no |
| 6 | `TOOL-dTracedLattice-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

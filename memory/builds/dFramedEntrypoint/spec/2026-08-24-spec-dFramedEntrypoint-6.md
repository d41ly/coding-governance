# TOOL-dFramedEntrypoint-6 — every record renders inside the spec it serves

**Status:** CLOSED · rev-5 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · order 7 · streams tooling · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-TOOL-dFramedEntrypoint-6-acceptance.md](../build/2026-08-25-build-TOOL-dFramedEntrypoint-6-acceptance.md) | journal | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's ruling is that a research report or a review means nothing at the entrypoint and everything
beside the unit it serves. Unit 5 removes both listings from the build README; this unit puts each
record where its reader is, as a GENERATED region inside the spec whose id the record's binding names.
The binding data already exists and is already parsed — this unit inverts the map that is built today
and renders the other side of it.

## 2. Scope (IN)

- **S1** — a new generated region, `gen:spec-records`, rendered into every tracked spec that carries a
  status header. The population is NOT narrowed to specs named by a record: S5 requires an unnamed spec
  to render an explicit empty case, and the two together previously declared opposite populations for
  one region.
- **S2** — the region's POSITION is between the spec's status header and its first numbered section.
  That location was measured against the spec-format check on a scratch clone before this unit was
  written: it passes, because the section-equality comparison never looks there and the empty-body walk
  has not started.
- **S3** — the region renders one row per record naming this spec's id: the record's filename linked by
  a path relative to the spec, its kind, and the other ids the same record serves.
- **S4** — the inversion is built from the bindings map `plan` already computes for the whole tree, so a
  record filed under one build folder but naming a spec in another renders at the spec, which is where
  a reader looks. Measured: 789 id-to-record edges over 248 ids, 17 of them crossing a build boundary.
- **S5** — a spec named by no record renders the region with an explicit empty-case line, never an
  absent region, because an absent region is indistinguishable from a spec nobody has recorded against.
- **S6** — `--write` creates the pair where it is missing and `--check` never demands one, the same
  asymmetry the build-README regions already rely on, so this region ships without demanding a
  corpus-wide render.
- **S6b** — `--write` today is whole-corpus with no path scoping, so the incremental convergence S6
  describes has no mechanism: the first `--write` after this lands creates every region at once. This
  unit ships a path-scoping argument with stated semantics, OR the incremental claim is dropped and the
  one-shot corpus write is stated plainly with unit 5's atomicity reasoning. The choice is F3 below;
  what is not permitted is the spec promising convergence that the verb cannot perform.
- **S7** — selftest arms for the position, the empty case, the cross-build edge, and a spec whose
  status header is absent.
- **S-EPOCH** — this unit moves `tools/memory-tree/gen_build_index.py`, which is inside the
  verdict-epoch gate's scan set, so its landing carries a `KIT_MEMORY_TREE_VERSION` bump. The carrier
  set is DERIVED, never read off the epoch gate's remedy text: bump the constant and its inline marker
  in the engine, then every carrier `git grep -l 'gov:kit memory-tree@'` returns over tracked paths
  outside `memory/builds/` and `memory/archive/`, then re-render the live copies with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The remedy string names three paths and
  the parity harness three pairs; their union is five, and there are SEVEN carriers — the two it cannot
  reach are kit SOURCES rather than dogfood copies. Following the remedy exactly reds the unguarded
  `kit version markers` leg, which is `TOOL-dSettledRoster-4` in the backlog, recorded as having cost a
  full-bar cycle twice. The rule binds per PUSH RANGE, not per commit: units landing in one push need
  one correctly-placed bump, on the LAST engine-moving commit in that range. It is stated in every
  engine-moving unit rather than once, because a rule written in one spec is a rule the other seven do
  not carry.

## 3. Non-goals (OUT)

- No ELEVENTH SPEC SECTION. A `## 11` heading would need a new section canon plus a dated cutoff, and
  every landed spec would then lack the region. The marker pair above the first section needs neither.
- No change to the ten-section canon, to hygiene check 12, or to any cutoff. The position is chosen
  precisely so none of them move.
- No change to the `**Serves:**` grammar or to the check that grades it.
- No rendering into the five headerless legacy specs. They carry no status header, so they are not
  units; whether they get a pointer at all is unit 5's open fork.
- No back-fill of bindings. A record that names no id today still names none after this unit.

## 4. Design

### Data model

The inversion is a map from spec id to the list of records naming it, built by walking the same
bindings the generator reads today and grouping the other way. Nothing new is parsed.

### Inventory

The rendered region is a table of record, kind, and co-served ids. It deliberately carries the
co-served ids: a review that covers six units is one record, and a reader at any one of those specs
needs to know the review was not written about their unit alone.

### Migration

The region is created on write. Because check never demands an absent pair, nothing forces a render —
but `--write` has no path scoping today, so a bare run creates every region at once. Whether that is
one reviewable mechanical commit or an incremental convergence depends on F3. The population is every
tracked spec carrying a status header, which is smaller than the 248 figure an earlier draft used: that
was the id count, not the header-carrying spec count, and the real figure is measured before the
commit rather than asserted here.

### Rollout

Inert until the pair exists. A spec with no pair renders unchanged, so the landing is invisible until
the first write, and a partial corpus is a legal state at every point.

### Alternatives rejected

**Rendering the records into the spec's section 4 or a sub-head under it.** Rejected because the
section bodies are authored and the empty-body walk grades them; a generated block inside an authored
section makes the two indistinguishable to the check that grades emptiness.

**Leaving the listing at the build level in a slimmer form.** That is what the ruling rejected, and it
keeps the property the owner objected to: a list of filenames that means nothing without the unit.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` for the inversion, the renderer, the region constants and the
arms · `tools/memory-tree/SPEC-TEMPLATE.template.md` with `memory/TEMPLATE-SPEC.md` re-rendered, to
document where the pair sits and that it is generated · the `build-readme-surface` dossier or a new one
if the surface has outgrown it.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one inversion over a map already built once per run; the render adds one region per
  spec that has a pair.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S5 is this line: the empty case renders explicitly, because an
  absent region reads as coverage.
- observability — the co-served id column is what makes a shared review legible at every spec it
  touches.
- risks — the real hazard is the region's position. It is validated by measurement rather than by
  reading the check, and the arm that proves it must assert check 12 passes with the pair present, not
  merely that the pair was written.
- testing + left-shift gates — four arms, including a spec with no status header, which must render
  nothing rather than raise.
- migration / rollback — rollback is deleting the region entry and running the write verb, which leaves
  orphaned pairs; the same one-commit rule unit 5 records applies to any later removal, and it is
  stated here so the next person removing a region does not rediscover it.
- user docs — the spec template documents the pair and that it is generated.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs on a spec named by records,
  a `gen:spec-records` region renders between its status header and its first numbered section.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over a spec carrying the region,
  check 12 passes, demonstrated on a real tracked spec rather than a fixture alone.
- **AC3** — When a record names ids in two builds, its row renders in the specs of BOTH after `--write`, with the
  co-served ids column naming the others.
- **AC4** — When a spec carrying a status header is named by no record, its `gen:spec-records` region
  renders the empty-case line — the same population S1 declares, with no narrowing clause between them.
- **AC5** — When a spec carries no status header, `--write` renders no region into it and does not
  raise.
- **AC6** — When `--check` runs over a spec that has no region pair, it reports nothing about that spec,
  preserving the create-on-write asymmetry.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, all four new arms pass,
  each observed RED against a staged break first.
- **AC8** — When the inversion is measured over the tracked tree, the edge count and the cross-build
  edge count are recorded from `--print-bindings` in this build's acceptance ledger with the command that produced them.

## 7. Gates

`build-index selftest` · `memory hygiene` · the spec-template parity harness · `build README slot
contract` · `check-kit-versions.sh` (leg `kit version markers`, unguarded) · `check-verdict-epoch.sh` ·
`kit/dogfood doc parity` · map freshness.

## 8. Open questions

- **F1 — does the region carry the record's kind, or only its link?** The kind is what lets a reader
  tell a research report from a spec audit without opening it, and the coverage joins already key on it.
  RESOLVED (agent, 2026-08-24, delegated): carry the kind. It is what lets a reader tell a research report
  from a spec audit without opening it, and the coverage joins already key on it.
- **F3 — does `--write` gain path scoping, or does the corpus render in one commit?** Scoping keeps
  every intermediate state small and matches what §4 Migration promises; one commit matches unit 5's
  shape and needs no new argument. Recommendation: one commit, verified by re-running the verb rather
  than by reading the diff, and the incremental language deleted. RESOLVED (agent, 2026-08-24, delegated): one
  commit, no path scoping. A new verb argument bought for a single migration is a mechanism with a
  fan-in of one, which is below this repo's own threshold for calling something a seam.
- **F2 — should a spec's region also name the records that serve its BUILD but no unit?** An unbound
  record has a reason recorded in its own binding line and belongs to the build, not to a spec.
  Rendering it at every spec would repeat one fact N times. RESOLVED (agent, 2026-08-24, delegated): no. An
  unbound record belongs to the build rather than to a spec, and repeating one fact N times is the
  duplication this build exists to remove.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the owner's fork-3 ruling. The region position was measured
  against the spec-format check on a scratch clone during verification, before this unit was written.
- rev-2 · 2026-08-24 · folded spec-audit round 1. S1 and S5 declared opposite populations for one
  region; the population is now every header-carrying spec, with no narrowing clause. The
  incremental-convergence promise gains a mechanism or gets deleted — `--write` has no path scoping
  today, so the claim had none. The 248 figure is dropped: it was an id count standing in for a spec
  count.
- rev-3 · 2026-08-24 · folded spec-audit round 2. The kit-version carrier set becomes a derivation,
  and `kit version markers` joins the gate list.
- rev-4 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-5 · 2026-08-25 · BUILT and CLOSED. The region renders into every header-carrying spec, above the first numbered section, and check 12 passes over the whole tracked corpus rather than over a fixture. Two defects of mine were caught by checks: an absolute path used as a repo-relative artifact key, and a repo-relative fallback that made every cross-build link resolve to nothing. Ledger: `build/2026-08-25-build-TOOL-dFramedEntrypoint-6-acceptance.md`.

## 10. Reuse audit

The seam is the bindings map built inside `plan` in `tools/memory-tree/gen_build_index.py`, which
already resolves every `**Serves:**` line in the tree to a set of ids, and `apply_region`, which already
splices a marker-delimited region into any authored markdown file with three named refusals. Both are
used unchanged. The only new code is the inversion and the renderer; the reuse audit's finding is that
this unit is a second consumer of an existing map rather than a new data path, which is why it costs no
parsing and no schema.

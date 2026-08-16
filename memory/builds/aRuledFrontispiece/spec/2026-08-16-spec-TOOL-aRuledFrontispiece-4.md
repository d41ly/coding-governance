# TOOL-aRuledFrontispiece-4 — the build README gets a generated document inventory

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Give every build README a rendered list of the records the build actually holds, linked. The
generated index region names a build's UNITS, which are the specs carrying a status header; the
reviews, the build logs, the prompts and the five specs that carry no header are reachable only by
listing the folder. This region makes the build's own documents navigable from the document that
opens the build.

## 2. Scope (IN)

- **S1** — a generated region, `<!-- gen:build-docs -->` and `<!-- /gen:build-docs -->`, lists every
  tracked file under the build's `spec/`, `build/`, `reviews/` and `prompts/` folders, at any depth,
  one row per file.
- **S2** — the region is opt-in by presence, spliced through the `apply_optional_region` helper unit 2
  introduces. This unit adds no second presence probe and no second splice implementation.
- **S3** — only the kinds a build HAS are rendered. The renderer iterates `build["kinds"]`, which
  `collect` already derives from the tracked set, so the 37 builds with no `prompts/` folder render no
  prompts rows and no empty heading. A build with no records at all renders the region with no table.
- **S4** — the renderer parses no part of a record's NAME. It has no date column, no sequence column
  and no kind field taken from the filename, so the five grandfathered names registered in
  `memory/project/legacy-files.txt` need no special case and no waiver lookup: they list like any
  other record.
- **S5** — every link is relative to the build README's own directory and targets a path `git ls-files`
  returned, so hygiene check 2 resolves each one.
- **S6** — a nested record renders the path BELOW its kind folder as the link text, so two files
  sharing a basename in different subfolders stay distinguishable rows.
- **S7** — a record that is not markdown is listed like any other. One exists at
  `memory/builds/aMooredAnchor/build/2026-08-11-build-aMooredAnchor-1-repro.sh`, and excluding it
  would make the region's claim to list the build's records false in exactly one place.

## 3. Non-goals (OUT)

- The README byte and line caps. Fork 3 resolved the tier and unit 5 owns it. This unit measures its
  own contribution and hands the number over; §4's Inventory records where the two collide.
- Suppressing a spec the index region already lists. A population that shrinks when a spec gains a
  status header would be a rule nobody could predict from the region's own heading.
- Reading `memory/project/legacy-files.txt`. That registry is the hygiene gate's, it is shrink-only,
  and a renderer that consumed it would gain a second consumer for a list written to narrow one gate.
- Listing the build-root files. `README.md` is this region's carrier, `RUN.md` belongs to the
  unattended kit, and `STATUS.md` is deleted by unit 7 under fork 6.
- Ordering the generated regions relative to one another. Unit 6's leg may pin a sequence; each pair
  is spliced where the author put it.
- Retrofitting any existing README (unit 10) and making the region mandatory on the bar (unit 6).

## 4. Design

### Data model

One table, one row per tracked record, grouped by kind and ordered inside a kind by path:

```
<!-- gen:build-docs -->
**Records:** 23 file(s) under `spec/` and `build/`.

| Kind | Record |
|---|---|
| spec | [2026-08-14-spec-cBriefedPilot-1.md](spec/2026-08-14-spec-cBriefedPilot-1.md) |
| build | [2026-08-14-build-cBriefedPilot-1-design-pass.md](build/2026-08-14-build-cBriefedPilot-1-design-pass.md) |
<!-- /gen:build-docs -->
```

The Kind column takes its values and its order from `RECORD_KINDS` at
`tools/memory-tree/gen_build_index.py:45`, through the `kinds` list `collect` already computes at
`gen_build_index.py:341-342`. That list is derived from the tracked paths, which is why S3 costs no
new code: the folder-claim sentence the module already renders is built from the same list.

The link text is the record's path below its kind folder and the target is the path relative to the
build folder. Rendering the basename alone would collide across the 21 nested records; rendering the
full relative path in both halves would repeat the kind segment in every row.

### Inventory

Measured at `base 96141aed` with `git ls-tree -r --name-only`, and every figure below is this unit's
sizing input rather than a fact worth writing into the region:

| Quantity | Value |
|---|---|
| tracked files under `memory/builds/` | 235 across 38 builds |
| records in the four kind folders | 194 — 118 spec, 53 reviews, 22 build, 1 prompts |
| the remaining 41 | 38 `README.md`, 2 `RUN.md`, 1 `STATUS.md` |
| largest build | `cBriefedPilot`, 24 tracked files, 23 of them records |
| records nested below their kind folder | 21, all under a `spec/units/` sub-folder |
| records that are not markdown | 1 |
| builds with a `prompts/` folder | 1 — `aGuardedTally` |
| specs carrying no parseable status header | 5, so the index region cannot reach them |
| grandfathered names in `memory/project/legacy-files.txt` | 5 |

Rendered at the row shape above, the longest row in the whole corpus is 144 characters, comfortably
inside fork 3's 350-character tier and inside check 7's current 300-character budget as well.

**The region and fork 3's byte tier collide on one build, and the collision is measured rather than
predicted.** `cBriefedPilot`'s README is 24715 bytes today against fork 3's 25600-byte tier, which is
885 bytes of headroom. Its 23 rows measure 2101 bytes and the region's header, table head and markers
add about 132 more, so the rendered README lands near 26948 bytes — roughly 1348 over. Two things
follow. The overrun is not caused by this region alone: that README is already at 96.5% of the tier
with no region present, so a couple of further specs would breach it anyway. And the remedy is unit
5's, not this unit's — a `memory/project/curation-debt.txt` row is the mechanism check 6 already uses
for exactly this, and curating that README is the alternative. This unit states the number so unit 5
chooses knowingly.

Functions this unit writes: a new `render_docs_region`, one added call to `apply_optional_region` in
`plan`, one added per-build key in `collect` holding the record paths by kind, and the pair's two
marker constants. Unit 2 writes the same module and touches `parse_spec`, `HDR_RE`'s reader,
`render_order_region` and `apply_optional_region`. The overlap is the module's constant block and the
per-build body of `plan`; neither unit calls into the other's renderer, and the presence probe is
introduced once, by unit 2, and reused here.

### Migration

None for the corpus. No tracked README carries a `gen:build-docs` pair, so every one of the 38 takes
S2's absent branch and renders byte-identically. Unit 10 owns the retrofit, and it is that commit —
not this one — that first exposes the byte collision recorded above.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms · `memory/HYGIENE.md` and
`tools/memory-tree/HYGIENE.template.md` as a byte-paired edit, for the slot the region occupies.

### Alternatives rejected

Deriving each record's date and sequence from its filename, for a sortable Date column, was rejected.
The recording grammar lives in check 5 of `check-memory-hygiene.sh`, five tracked names are
permanently exempt from it, and a renderer that parsed it would need either its own copy of the
grammar or a read of the exemption registry. A column nobody asked for is not worth either.

Rendering a per-kind heading instead of a Kind column was rejected: headings inside a generated
region interleave with the README's authored heading structure, and unit 1's slot contract is about
keeping those two apart.

Reusing `strip_records_sentence`'s derived folder-claim sentence as the region's header line was
rejected. That sentence is written OUTSIDE the marker pair, into the authored body, and the two would
then state the same fact in two places — the class the module's own docstring exists to remove.

## 5. Production-readiness checklist

- security — N/A. Every listed path comes from `git ls-files` over the memory root, which the renderer
  already reads.
- perf / scale — the tracked list is already in memory in `collect`; the region adds one grouping pass
  per build over at most 23 paths.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Markers and column heads are ASCII literals.
- error / empty / loading states — a build with no records renders the region with no table; a build
  missing one kind renders no row for it. Both are arms.
- observability — the region's header line reports the record count and names the kind folders, so a
  reader can tell an empty region from an absent one.
- risks — this region is the first thing in the corpus to generate links at volume, so a path bug
  breaks hygiene check 2 across many files at once rather than in one. Mitigated by targeting only
  paths `git ls-files` returned and by AC5, which runs the check over a rendered fixture.
- testing + left-shift gates — arms in `gen_build_index.py --selftest`, one per S1 through S7; the
  binding leg is unit 6, and hygiene check 2 covers the links on the bar.
- migration / rollback — revert is a single-file revert plus the paired doc edit; no corpus bytes
  change in this unit.
- user docs — the region's slot lands in `memory/HYGIENE.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip, it
  reports clean at the same artifact count it reports at `base 96141aed`.
- **AC2** — When a build has a `spec/` folder and no `prompts/` folder, `--write` renders no row whose
  Kind cell reads `prompts` and no empty prompts heading inside `<!-- gen:build-docs -->`.
- **AC3** — When a build holds two records with the same basename in `spec/` and `spec/units/`,
  `--write` renders two rows with different link texts, proved by a `--selftest` fixture.
- **AC4** — When a build holds a record whose name carries no date prefix, `--write` lists it and
  `--check` stays clean, proved by a fixture carrying the shape the five rows in
  `memory/project/legacy-files.txt` carry.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over a tree whose README
  carries a rendered region, check 2 reports no broken relative link.
- **AC6** — When a build holds a record that is not markdown, `--write` renders a row for it, proved
  by a fixture ending in `.sh`.
- **AC7** — When a README carries no `<!-- gen:build-docs -->` marker, `--write` leaves it
  byte-identical to its render at `base 96141aed`, proved by a fixture asserting byte equality.
- **AC8** — When the region is rendered for `cBriefedPilot`, the bytes between its two markers exceed
  the 885 bytes of headroom that README has under fork 3's 25600-byte tier, so the collision unit 5
  must price is an observation and not a prediction.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · `bash tools/memory-tree/check-memory-hygiene.sh`,
whose check 2 grades every link this region emits · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the paired `HYGIENE.md` edit · `bash tools/memory-tree/marker-contract.test.sh`, because a third
generated pair enters the contract that test drives · `bash tools/memory-tree/check-verdict-epoch.sh`,
which unit 10 discharges for the whole build.

## 8. Open questions

none — fork 1 resolved what the authored plan may hold and fork 3 resolved the cap tier this region is
priced against. The one number this unit cannot settle, whether `cBriefedPilot` takes a curation-debt
row or a curation pass, is unit 5's to decide and is recorded with its measurement in §4 rather than
parked here.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `generated region record
kinds inventory relative link check 2 legacy grandfathered recording grammar tracked files byte cap
curation debt`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| which record folders a build has | `kinds` in `collect` at `gen_build_index.py:341-342` | REUSE unchanged — it is derived from the tracked set and already feeds a rendered sentence |
| the kind vocabulary and its order | `RECORD_KINDS` at `gen_build_index.py:45` | REUSE unchanged — a second spelling would be the two-answers class |
| splice into a named marker pair, optionally | `apply_optional_region`, introduced by unit 2 | REUSE unchanged — this unit adds a call, not a probe |
| render a table of relative links | `render_region` at `gen_build_index.py:358` | REUSE THE SHAPE — same row grammar, same build-relative link form |
| enumerate a build's tracked files | the `tracked` list in `collect` at `gen_build_index.py:298` | REUSE unchanged — one added grouping over a list already in memory |

The `tools/codebase-map/reuse_lookup.py` probe for "render a generated region listing a build's record
files with relative links" returned `render_region`, `render_live`, `render_shards` and `apply_region`
in `gen_build_index.py` as the only marker-region seams in the corpus, and returned no seam that
enumerates a build's records — `collect`'s `kinds` derivation is the closest, and it answers presence
rather than membership. Every count in §4's Inventory was measured against
`git ls-tree -r --name-only 96141aed -- memory/builds/` at writing time; the byte figures for
`cBriefedPilot` were measured against its tracked README and a rendering of the row shape above.

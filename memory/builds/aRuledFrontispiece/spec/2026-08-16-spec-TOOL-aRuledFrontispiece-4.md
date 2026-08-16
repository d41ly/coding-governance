# TOOL-aRuledFrontispiece-4 — the build README gets a generated document inventory

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

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
- **S2** — the region is spliced through `apply_optional_region`, the create-or-splice helper
  `TOOL-aRuledFrontispiece-2` introduces at position 3. The marker pair is never hand-inserted: that
  helper creates a missing pair at the slot position `TOOL-aRuledFrontispiece-1` defines, so this unit
  adds a call and no second presence probe, no second splice implementation and no placement rule of
  its own.
- **S3** — only the kinds a build HAS are rendered. The renderer iterates `build["kinds"]`, which
  `collect` already derives from the tracked set, so every build with no `prompts/` folder renders no
  prompts rows and no empty heading — `aGuardedTally` is the only build in the corpus that has one, so
  every other build exercises that branch, and the population is counted from the tracked set rather
  than from a figure written here. A build with no records at all renders the region with no table.
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
- **S8** — the `--write` output over the tracked corpus lands in this unit's own commit. S2's creation
  reaches every build README, so a fresh render stops equalling the committed bytes the moment this
  renderer exists; deferring the re-render would leave hygiene check 9 red from this unit's tip until
  some later one, which is the M6 violation the build README's ordering section re-sequenced this
  build to avoid.

## 3. Non-goals (OUT)

- The README byte and line caps. Fork 3 resolved the tier and `TOOL-aRuledFrontispiece-5` owns it at
  position 6. This unit measures its own contribution and hands the number over; §4's Inventory
  records where the two collide, and AC8 makes the collision readable off the tree.
- Suppressing a spec the index region already lists. A population that shrinks when a spec gains a
  status header would be a rule nobody could predict from the region's own heading.
- Reading `memory/project/legacy-files.txt`. That registry is the hygiene gate's, it is shrink-only,
  and a renderer that consumed it would gain a second consumer for a list written to narrow one gate.
- Listing the build-root files. `README.md` is this region's carrier, `RUN.md` belongs to the
  unattended kit, and `STATUS.md` is deleted by `TOOL-aRuledFrontispiece-7` under fork 6.
- Ordering the generated regions relative to one another. `TOOL-aRuledFrontispiece-6`'s leg may pin a
  sequence at position 11; a pair the author placed stays where it is, and a pair the generator
  creates goes at the slot position the contract defines.
- Inserting the `gen:build-docs` marker pair into any README by hand. The generator creates a missing
  pair at the slot position the contract defines, and `TOOL-aRuledFrontispiece-1` owns that behaviour;
  this unit renders into a pair it never places.
- Making the region mandatory on the bar. `TOOL-aRuledFrontispiece-6` is the leg, at position 11.
- The kit version bump and the closing corpus re-render. `TOOL-aRuledFrontispiece-10`, at position 10
  of the order, owns both; this unit carries only the re-render its own renderer causes, per S8.

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

**The region and fork 3's byte tier collide on one build, and under S2 the collision becomes an
OBSERVATION at this unit's tip rather than a prediction handed forward.** `cBriefedPilot`'s README is
24715 bytes at this unit's base against fork 3's 25600-byte tier, which is 885 bytes of headroom. Its
23 rows measure 2101 bytes and the region's header, table head and markers add about 132 more, so the
rendered README lands near 26948 bytes — roughly 1348 over. Because the pair is created rather than
opted into, that render lands in this unit's own commit, and `TOOL-aRuledFrontispiece-5` at position 6
installs the cap one position later, over a file that already carries the region. AC8 reads the size
off the tree rather than off this paragraph.

Three things follow. The overrun is not caused by this region alone: that README is already at 96.5%
of the tier with no region present, so a couple of further specs would breach it anyway. The collision
is one file's — measured at this unit's parent, the next-largest build README carries more than 6 KiB
of headroom against the same tier. And the remedy is `TOOL-aRuledFrontispiece-5`'s, not this unit's: a
`memory/project/curation-debt.txt` row is the mechanism check 6 already uses for exactly this, and
curating that README is the alternative. This unit states the number so that unit chooses knowingly.

Functions this unit writes: a new `render_docs_region`, one added call to `apply_optional_region` in
`plan`, one added per-build key in `collect` holding the record paths by kind, and the pair's two
marker constants. `TOOL-aRuledFrontispiece-2`, at position 3, writes the same module and touches
`parse_spec`, `HDR_RE`'s reader, `render_order_region` and `apply_optional_region`, and
`TOOL-aRuledFrontispiece-3` at position 4 adds the edges renderer. The overlap is the module's
constant block and the per-build body of `plan`; no unit calls into another's renderer, and the
create-or-splice helper is introduced once, at position 3, and reused here.

### Migration

The corpus moves in this unit's own commit, and an earlier revision of this section said it did not.
No tracked README carries a `gen:build-docs` pair, so under S2 every build README gains one the first
time `--write` runs after the renderer exists, and hygiene check 9 compares committed bytes against a
fresh render. S8 puts that re-render here, and it is this commit — not a later one — that exposes the
byte collision recorded above.

The artifact COUNT does not move: the region lands inside files this render already produces and
creates none. The population that gains rows is read from `--check` at both ends of the commit, never
from a figure quoted here.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms ·
`tools/memory-tree/HYGIENE.template.md`, for the slot the region occupies, with `memory/HYGIENE.md`
re-rendered from it by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` and never
hand-edited — that harness byte-pairs the two after substituting this install's prefix, and its
declared direction is template to live copy · every tracked build README, as the `--write` output S8
lands in this commit.

### Alternatives rejected

Deriving each record's date and sequence from its filename, for a sortable Date column, was rejected.
The recording grammar lives in check 5 of `check-memory-hygiene.sh`, five tracked names are
permanently exempt from it, and a renderer that parsed it would need either its own copy of the
grammar or a read of the exemption registry. A column nobody asked for is not worth either.

Rendering a per-kind heading instead of a Kind column was rejected: headings inside a generated
region interleave with the README's authored heading structure, and `TOOL-aRuledFrontispiece-1`'s slot
contract is about keeping those two apart.

Reusing the derived folder-claim sentence as the region's header line was rejected, and the reason
given at rev-1 was wrong about where that sentence lives. It is GENERATED, by `render_region` at
`gen_build_index.py:379-382`, and it renders INSIDE the `gen:build-index` pair — in
`memory/builds/cBriefedPilot/README.md` the markers sit at lines 292 and 321 and the sentence at 320.
`strip_records_sentence` at :396 is the remover for AUTHORED copies found outside that pair, which is
the opposite relation to the one rev-1 asserted. Both facts were re-read at source.

Against the real seam the alternative fails twice, and worse than rev-1 claimed. Reusing the sentence
means either moving it or copying it. Moving it out of `render_region` changes the `gen:build-index`
slice in every build README — the exact slice `check_authorization` in the unattended kit byte-compares
against a pinned BASE and the slice `TOOL-aRuledFrontispiece-8`'s carve-out at position 2 is about — so
a header line buys a corpus-wide edit to a region no unit here otherwise touches. Copying it is worse:
`strip_records_sentence` computes its skip range from the `gen:build-index` markers alone, so a second
`Records live under …` sentence inside the `gen:build-docs` pair sits INSIDE the remover's scan scope.
It becomes a hit like any other, and a README that also carries an authored copy then trips the
more-than-one-match refusal at :457-461 — a file that renders cleanly today would refuse because this
region was added.

The header line therefore carries its own wording, `**Records:** <n> file(s) under …`. It does restate
the kind list the index region's sentence carries, but both are rendered from one source — the `kinds`
list `collect` derives at `gen_build_index.py:341-342` — so they cannot disagree, which is not the
two-answers class the module's docstring exists to remove.

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
- testing + left-shift gates — arms in `gen_build_index.py --selftest`, one per S1 through S7, plus
  AC7 over the real corpus for S2 and S8; the binding leg is `TOOL-aRuledFrontispiece-6`, and hygiene
  check 2 covers the links on the bar.
- migration / rollback — one `git revert` of this unit's commit, which carries the engine change, the
  rendered `HYGIENE.md` pair and the corpus re-render together, so no half state is reachable.
- user docs — the region's slot lands in `memory/HYGIENE.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip, it
  exits 0, and the artifact count it prints equals the count the same command prints at this unit's
  PARENT commit. Both counts are read from the gate, never from a figure quoted in a document: this
  build's own folder was created after `base 96141aed` and adds one artifact, so the base count is not
  the comparand.
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
- **AC7** — When `--write` runs over the tracked corpus at this unit's tip, every build README carries
  exactly one `<!-- gen:build-docs -->` pair, `git diff` shows no change outside those pairs, and a
  second `--write` leaves the tree clean under `git diff --exit-code`. This is the corpus observation,
  not a fixture: it is what S2's creation and S8's re-render assert together.
- **AC8** — When this unit's commit has landed, `wc -c memory/builds/cBriefedPilot/README.md` exceeds
  fork 3's 25600-byte tier, so the collision `TOOL-aRuledFrontispiece-5` must price at position 6 is
  read off the tree rather than predicted from §4's arithmetic.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.
- **AC10** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at this unit's tip, it
  passes with no `--render` left to do, so `memory/HYGIENE.md` is the render of the edited
  `tools/memory-tree/HYGIENE.template.md` and not a hand-edit.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · `bash tools/memory-tree/check-memory-hygiene.sh`,
whose check 2 grades every link this region emits and whose check 9 grades the corpus re-render S8
lands here · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the paired `HYGIENE.md` edit · `bash tools/memory-tree/marker-contract.test.sh`, because a third
generated pair enters the contract that test drives · `bash tools/memory-tree/check-verdict-epoch.sh`,
which `TOOL-aRuledFrontispiece-10` discharges for the whole build at position 10.

## 8. Open questions

none — fork 1 resolved what the authored plan may hold and fork 3 resolved the cap tier this region is
priced against. The one number this unit cannot settle, whether `cBriefedPilot` takes a curation-debt
row or a curation pass, is `TOOL-aRuledFrontispiece-5`'s to decide and is recorded with its
measurement in §4 rather than parked here; AC8 makes it a reading off the tree at this unit's tip
rather than a figure handed forward in prose.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit. §4's rejected alternative misread the folder-claim
  seam: the sentence is GENERATED by `render_region` INSIDE the `gen:build-index` pair, and
  `strip_records_sentence` removes AUTHORED copies from outside it — the opposite of what rev-1 said.
  Re-argued the header line against the real seam, where copying the sentence into this region puts a
  generated string inside the remover's own scan scope. The marker pair's insertion was deferred to
  the retrofit unit, which never carried it — the set's largest blocker — so S2 states that the
  generator creates a missing pair and cites `TOOL-aRuledFrontispiece-1` as its owner, and new S8
  lands the corpus re-render that creation causes in this unit's own commit rather than leaving check
  9 red across later units. That also turns the `cBriefedPilot` byte collision into an observation at
  this unit's tip, so AC8 now reads the file's size instead of predicting it. Restated the paired
  `HYGIENE.md` edit as a template edit followed by `--render`, the direction
  `kit-dogfood-parity.test.sh` declares, and added AC10 for it. Retargeted AC1 onto this unit's parent
  commit rather than a base count the build's own folder postdates, and replaced the byte-identity AC
  with a corpus observation.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `generated region record
kinds inventory relative link check 2 legacy grandfathered recording grammar tracked files byte cap
curation debt`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| which record folders a build has | `kinds` in `collect` at `gen_build_index.py:341-342` | REUSE unchanged — it is derived from the tracked set and already feeds a rendered sentence |
| the kind vocabulary and its order | `RECORD_KINDS` at `gen_build_index.py:45` | REUSE unchanged — a second spelling would be the two-answers class |
| splice into a named marker pair, optionally | `apply_optional_region`, introduced by `TOOL-aRuledFrontispiece-2` | REUSE unchanged — this unit adds a call, not a probe |
| place a pair a README does not carry | the slot-position insertion `TOOL-aRuledFrontispiece-1` ships | REUSE unchanged — this unit spells no position of its own |
| the folder-claim sentence, as a header line | `render_region` at `gen_build_index.py:379-382` | REJECT — it renders inside the index pair, and copying it puts a generated string inside `strip_records_sentence`'s scan scope |
| render a table of relative links | `render_region` at `gen_build_index.py:358` | REUSE THE SHAPE — same row grammar, same build-relative link form |
| enumerate a build's tracked files | the `tracked` list in `collect` at `gen_build_index.py:298` | REUSE unchanged — one added grouping over a list already in memory |

The `tools/codebase-map/reuse_lookup.py` probe for "render a generated region listing a build's record
files with relative links" returned `render_region`, `render_live`, `render_shards` and `apply_region`
in `gen_build_index.py` as the only marker-region seams in the corpus, and returned no seam that
enumerates a build's records — `collect`'s `kinds` derivation is the closest, and it answers presence
rather than membership. Every count in §4's Inventory was measured against
`git ls-tree -r --name-only 96141aed -- memory/builds/` at writing time; the byte figures for
`cBriefedPilot` were measured against its tracked README and a rendering of the row shape above. At
rev-2 the folder-claim seam was re-read at source before the rejection was re-argued: `render_region`
emits the sentence at `gen_build_index.py:379-382`, one line above `MARK_CLOSE`; `cBriefedPilot`'s
markers sit at lines 292 and 321 with the sentence at 320; and `strip_records_sentence` derives its
skip range at :419-421 from the `gen:build-index` markers alone. The README's 24715 bytes and its 23
records were re-measured against the tracked blob at the same time.

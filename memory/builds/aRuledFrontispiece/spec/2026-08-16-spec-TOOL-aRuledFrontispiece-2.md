# TOOL-aRuledFrontispiece-2 — build order and parallel groups become a header verb and a region

**Status:** WONTDO · rev-3 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · superseded by TOOL-aRuledFrontispiece-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-TOOL-aRuledFrontispiece-1-1.md](../reviews/2026-08-16-review-TOOL-aRuledFrontispiece-1-1.md) | spec-audit | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-6 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |
| [2026-08-17-review-TOOL-aRuledFrontispiece-1-2.md](../reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-2.md) | spec-audit | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-6 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |
| [2026-08-17-review-TOOL-aRuledFrontispiece-1-3.md](../reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-3.md) | diff-review | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-6 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |

<!-- /gen:spec-records -->

## 1. Goal

Make a build's execution order a derived fact instead of a paragraph. Today the order lives in
authored prose — this build's own README argues it across two sections — and nothing compares that
prose to the units it describes. A unit declares its position in its own status header, and the
build README renders the total order and the parallel groups from those declarations.

## 2. Scope (IN)

- **S1** — the status header's pointer tail admits one new verb, `· order <n>`, where `<n>` is one or
  more decimal digits, at least 1, with no leading zero. The verb is PERMITTED and never required,
  which is fork 5's resolution: this unit ships no required-arm and no dated cutoff key.
- **S2** — units sharing an `order` value ARE the build's parallel group at that step. The group is
  the tie itself, not a second verb, so a group cannot contradict the position it sits in.
- **S3** — `gen_build_index.py` reads the verb with a second regex over the same header line `HDR_RE`
  already matched. `HDR_RE` is not widened. `parse_spec` gains one key, `order`, holding an `int` or
  `None`.
- **S4** — a generated region, `<!-- gen:build-order -->` and `<!-- /gen:build-order -->`, renders one
  row per unit as `| Step | Unit |`, sorted by step and then by the id's sequence component. A unit
  carrying no verb renders last, at step `—`, so the region accounts for every unit the index region
  lists.
- **S5** — the marker pair is never hand-inserted. `--write` CREATES a missing generated-region pair
  at the slot position the contract defines, and `TOOL-aRuledFrontispiece-1` owns that behaviour and
  builds at position 1, so this unit ships a renderer and its refusals and no insertion of its own. A
  README carrying ONE marker of the pair is not a missing pair: it keeps every refusal `apply_region`
  makes today.
- **S6** — a header carrying `order` with a value outside S1's shape is a named refusal naming the
  spec path and the offending value. A silent skip would make the region under-report an order the
  author believes they declared.
- **S7** — the verb is added to `tools/memory-tree/SPEC-TEMPLATE.template.md` in its status-header
  section, and `memory/TEMPLATE-SPEC.md` is then re-rendered from it by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` and never hand-edited: that harness
  byte-pairs the two after substituting this install's prefix, and its declared direction is template
  to live copy. That section states today that the tail holds pointers only, which the verb
  contradicts until it is amended.
- **S8** — the `--write` output over the tracked corpus lands in this unit's own commit. Because S5's
  creation reaches every build README, a fresh render stops equalling the committed bytes the moment
  the renderer exists, so deferring the re-render would leave hygiene check 9 red from this unit's tip
  until some later one — the M6 violation the build README's ordering section re-sequenced this build
  to avoid.

## 3. Non-goals (OUT)

- Requiring the verb, or dating a cutoff for it. Fork 5 put the requirement in a follow-up commit.
- A second `group` verb. §4's Alternatives rejected records why one verb carries both facts.
- Rendering a unit that has no spec. The authored plan inside the `roster:units` pair is where a
  pending unit lives, and `TOOL-aRuledFrontispiece-1` forbids the generator writing there.
- Ordering the generated regions relative to one another. A pair the author placed stays where it is,
  and a pair the generator creates goes at the slot position the contract defines; pinning a canonical
  sequence among the generated regions is `TOOL-aRuledFrontispiece-6`'s leg, at position 11.
- Enforcing the verb's shape on the merge bar. This unit ships the refusal and its arms;
  `TOOL-aRuledFrontispiece-6` makes it binding.
- Rewriting M6's parallelism clause. `TOOL-aRuledFrontispiece-9` owns that, at position 8, and this
  unit only supplies the data it needs.
- Changing `LIVE.md` or the ledger shards. Fork 8 resolved those to no change.
- Inserting the `gen:build-order` marker pair into any README by hand, here or in the corpus. The
  generator creates a missing pair at the slot position the contract defines, and
  `TOOL-aRuledFrontispiece-1` owns that behaviour; this unit renders into a pair it never places.
- Declaring an `order` verb on another build's specs. The verb is permitted and never required, so a
  build that declares none renders every unit at step `—` until an author writes one.
- The kit version bump and the closing corpus re-render. `TOOL-aRuledFrontispiece-10`, at position 10
  of the order, owns both; this unit carries only the re-render its own renderer causes, per S8.

## 4. Design

### Data model

A unit's position is authored once, in the unit's own file, and read from there:

| Fact | Where it lives | Who writes it |
|---|---|---|
| the unit's step | `· order <n>` in the spec status header | the spec's author |
| the parallel group at a step | every unit carrying the same `<n>` | nobody — it is the tie |
| the row key | the id's sequence component, e.g. `1` in `TOOL-aRuledFrontispiece-1` | the id |
| the rendered order | `<!-- gen:build-order -->` in the build README | `gen_build_index.py --write` |

The step is the authored `order` value and nothing else. The id's sequence component is the row key
WITHIN a step — a stable tie-break so two units sharing a step render in a fixed sequence — and it is
never the step itself. An earlier revision of this section asserted that the sequence IS the authored
plan's `#` column. The build README separates the two emphatically, and this build is the
counter-example rather than a case where they agree: `TOOL-aRuledFrontispiece-8` is minted eighth and
builds at position 2. The same separation reproduces in another build's corpus, where
`memory/builds/aFoldedQuarry/spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md` is that
build's unit 6 at sequence 2 and its `-3-u1-flatten` sibling is unit 1 at sequence 3, measured at
`base 96141aed`.

**The region does not replace the authored plan, and cannot while a build holds an unspecced unit.**
A planned unit with no spec has no status header, so it carries no verb and gets no row here; the
`roster:units` plan is the only place it is named. That is the build README's own measured constraint
— an id cited but never defined reds hygiene check 14 — and it is why the plan table carried
`*pending*` rows while these specs were being written. The two documents answer different questions:
the plan names every unit the build intends, the region orders the units that have a spec.

The region renders one header line, a blank line, and a table. The header line is
`**Build order:** <k> step(s) · <m> of <n> unit(s) declare one.`, where `<k>` counts distinct declared
steps, `<m>` counts units carrying the verb, and `<n>` is the unit population the index region already
renders. The table head is `| Step | Unit |`, and the Unit cell is the same label-and-relative-link
form `render_region` emits at `gen_build_index.py:374-375`. Rows collate by step ascending, then by
the id's sequence component; every unit carrying no verb collates AFTER every unit carrying one, as a
single trailing block at step `—`, ordered among themselves by the same key. A build where no unit
declares a step renders `0 step(s) · 0 of <n> unit(s) declare one.` with every row at `—`.

`HDR_RE` at `tools/memory-tree/gen_build_index.py:74-78` ends at `base (?P<base>[0-9a-f]{8,})` with no
`$` and no trailing group, so it matches a PREFIX of the header line. Verified against source. Every
tracked spec therefore parses unchanged today, and a header carrying the new verb parses unchanged
too — the verb costs nothing at the parse site and is read separately.

Check 12's header predicate at `tools/memory-tree/check-memory-hygiene.sh:559` is unanchored in the
same way, ending at the eighth spelled-out `[0-9a-f]`. Verified against source. Its `streams`
extraction matches `streams [A-Za-z0-9]+(\+[A-Za-z0-9]+)*`, which stops at the first byte outside that
class, so a tail reading `· streams tooling · order 2` still yields `tooling`. The consequence is
worth stating because it is easy to assume otherwise: **check 12 needs no edit for the verb to be
legal**. What does need editing is `memory/TEMPLATE-SPEC.md`, which tells an author the tail holds
pointers only.

### Inventory

| Site | Change |
|---|---|
| `HDR_RE` | none — verified unanchored, so it already admits the tail |
| new `ORDER_ANCHOR` | the plain literal `· order `, matched by substring and never by shape |
| new `ORDER_RE` | the legal VALUE shape — the anchor, decimal digits with no leading zero, then a terminator |
| `parse_spec` | one added key, `order`; the refusal in S6 fires here, where the value is read |
| new `MARK_ORDER_OPEN` / `MARK_ORDER_CLOSE` | the second generated pair's two constants |
| new `render_order_region` | the table, mirroring `render_region`'s shape |
| new `apply_optional_region` | create-if-missing, then delegation to `apply_region` |
| `plan` | one added splice per build |

**Two constants, not one, and the split is what makes S6's message producible.** A single extracting
regex has one negative outcome, so "this unit declares no step" and "this unit declares a step this
parser refuses" arrive as the same event and the refusal can only be silence. That is the shape
`strip_records_sentence` already solved one anchor over: `RECORDS_SENTENCE` at
`gen_build_index.py:392` carries the full shape, `RECORDS_ANCHOR` at :393 is the bare literal, and the
remover raises at :450-454 for a line that carries the anchor without matching the shape. The verb
reads the same way. A header line carrying neither yields `order: None`. A line `ORDER_RE` matches
yields the step. A line carrying `ORDER_ANCHOR` that `ORDER_RE` does not match is S6's refusal, and
the offending value it prints is the text from the end of the anchor to the next `·` or end of line.

`ORDER_RE` is `· order ` followed by `[1-9][0-9]*` followed by a lookahead for ` ·` or end of line.
The terminator is load-bearing and not decoration: without it `· order 2x` matches on its leading `2`
and the region renders a step the author never wrote. With it, every value that is not wholly decimal
digits is a non-match, and the anchor turns each one into a named refusal instead of a wrong row.

`apply_optional_region` counts the pair's opening and closing markers with the same column-0 equality
`apply_region` uses. Both counts zero means the pair is absent, and the helper then inserts it at the
slot position `TOOL-aRuledFrontispiece-1` defines before splicing — this unit adds no second placement
rule and spells no position of its own. Any other count delegates straight to `apply_region`, so a
half-present pair still meets the unequal-counts refusal and an inverted pair still meets the ordering
refusal. It does NOT make the existing pair optional: `gen:build-index` keeps its own direct call and
its no-marker-pair refusal, which is the branch that stops a README leaving the index silently.

`TOOL-aRuledFrontispiece-4`, at position 5, writes this same module. It adds a renderer and one more
`apply_optional_region` call and it extends `collect`; it does not touch `parse_spec`, `ORDER_RE` or
`render_order_region`. `TOOL-aRuledFrontispiece-3`, at position 4, does the same for the edges region.
All three overlap at exactly two sites — the module's constant block and the per-build body of `plan`
— and `apply_optional_region` is introduced HERE, at position 3, precisely so that neither later unit
adds a second presence probe.

### Migration

The corpus moves in this unit's own commit, and an earlier revision of this section said it did not.
No tracked README carries a `gen:build-order` pair, so under S5 every build README gains one the first
time `--write` runs after the renderer exists. That is a byte change in every one of them, and hygiene
check 9 compares committed bytes against a fresh render, so the re-render cannot be deferred to a
later unit without leaving the bar red in between. S8 puts it here.

No tracked spec carries the verb, so every unit renders at step `—` on that first pass and the added
region is the header line, the table head and one row per unit. The counts in this paragraph are
claims about the corpus, so the arm is AC6 running over the real tree rather than this text.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms ·
`tools/memory-tree/SPEC-TEMPLATE.template.md`, with `memory/TEMPLATE-SPEC.md` re-rendered from it by
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` · every tracked build README, as the
`--write` output S8 lands in this commit.

### Alternatives rejected

A second `group <label>` verb beside `order` was rejected. Two verbs create a contradiction class the
tie does not have — two units at the same step with different labels, or one label spanning two steps
— and each shape needs its own refusal branch. Neither buys a fact the tie fails to carry, and the
rendered region is identical either way. An earlier revision of this paragraph cited the build
README's row for this unit as reading "status-header verbs" in the plural; that row now reads "build
order — one status-header verb and its region", so the plan and this spec agree and the reduction is
recorded here rather than left for a reviewer to find unused. Park P4 in that README resolved the
same question the same way; §8 records it.

Widening `HDR_RE` with an optional trailing group was rejected. That regex decides what a valid header
IS for the 113 specs that parse at `base 96141aed`, and a widened pattern that fails to match returns
`None` for the whole header rather than for the verb, which would silently drop a unit from the index
region as well.

Deriving the order from the id sequence alone, with no verb, was rejected on measured evidence: the
`aFoldedQuarry` files named under Data model mint sequence 2 for unit 6, so the sequence is a mint
order and not a build order.

Reading the order out of the authored `roster:units` plan block was rejected. The module's docstring
pins three sources and names reading its own output as the defect it exists to remove; the plan is not
an output, but adding a fourth source would make the region's population depend on a table shape no
gate validates until `TOOL-aRuledFrontispiece-6` lands at position 11.

## 5. Production-readiness checklist

- security — N/A. The verb is read from tracked files the renderer already opens; no new trust
  boundary.
- perf / scale — one regex per spec header already in memory, and one extra splice per README.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The verb and the markers are ASCII literals; the `·` separator is already in the header.
- error / empty / loading states — a build where no unit carries the verb renders every row at step
  `—`; a build with no units renders the region with no table. Both are arms.
- observability — the S6 refusal names the spec path and the offending value; the region's header line
  reports the distinct step count and how many of the build's units declare one.
- risks — the tie-is-the-group rule means an author who mistypes a step silently joins another group
  rather than failing. The rendered region is the mitigation: a wrong tie is visible as two units on
  one row, which prose never made visible at all.
- testing + left-shift gates — arms in `gen_build_index.py --selftest`, one per S1 through S6, plus
  AC6 over the real corpus for S5 and S8; the binding leg is `TOOL-aRuledFrontispiece-6`.
- migration / rollback — one `git revert` of this unit's commit, which carries the engine change, the
  rendered template pair and the corpus re-render together, so no half state is reachable.
- user docs — the verb lands in `memory/TEMPLATE-SPEC.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip, it
  exits 0, and the artifact count it prints equals the count the same command prints at this unit's
  PARENT commit. Both counts are read from the gate, never from a figure quoted in a document: this
  build's own folder was created after `base 96141aed` and adds one artifact, so the base count is not
  the comparand.
- **AC2** — When a spec header carries `· order 3`, `--write` renders that unit at step `3` inside
  `<!-- gen:build-order -->` in its build's README.
- **AC3** — When two specs in one build both carry `· order 3`, `--write` renders both at step `3`,
  ordered by the id's sequence component, emits no additional row, and writes the header line
  `**Build order:** 1 step(s) · 2 of 2 unit(s) declare one.`, proved by a `--selftest` fixture.
- **AC4** — When a spec carries no `order` verb, `--check` stays clean, that unit renders at step `—`
  after every row carrying a step, and the header line counts it in the `of <n>` half and not in the
  `<m>` half.
- **AC5** — When a header carries `· order 0x2`, `--check` fails naming the spec path and the value
  `0x2`, and when it carries `· order 2x` the same refusal names `2x` rather than rendering step `2`.
  Both messages are reachable only through §4's anchor/value split.
- **AC6** — When `--write` runs over the tracked corpus at this unit's tip, every build README carries
  exactly one `<!-- gen:build-order -->` pair, `git diff` shows no change outside those pairs, and a
  second `--write` leaves the tree clean under `git diff --exit-code`. This is the corpus observation,
  not a fixture: it is what S5's creation and S8's re-render assert together.
- **AC7** — When a README carries a `<!-- gen:build-order -->` opening marker and no closing marker,
  `--check` fails with the wording `apply_region` already uses for an unequal marker count.
- **AC8** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at this unit's tip, it
  passes with no `--render` left to do, so `memory/TEMPLATE-SPEC.md` is the render of the edited
  `tools/memory-tree/SPEC-TEMPLATE.template.md` and not a hand-edit.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · `bash tools/memory-tree/check-memory-hygiene.sh`,
whose check 12 grades every status header this build writes and whose check 9 grades the corpus
re-render S8 lands here · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the rendered `TEMPLATE-SPEC.md` pair · `bash tools/memory-tree/marker-contract.test.sh`, because a
second generated pair enters the contract that test drives ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which `TOOL-aRuledFrontispiece-10` discharges for the
whole build at position 10.

## 8. Open questions

none — fork 5 resolved the rollout to permitted-now and required-later, and fork 1 resolved what the
authored plan may hold.

The build README's park P4, one verb or two, is RESOLVED (owner, 2026-08-16): one `order` verb, and
the unit that edits the build-method contract these verbs live under must not introduce a second.
This spec already ships one verb, so nothing here changes; the resolution is recorded because §4's
Alternatives rejected argued the reduction rather than citing a decision, and a later reader needs to
know it was decided rather than defaulted.

## 9. Revision log

- rev-3 · 2026-08-17 · SUPERSEDED into `TOOL-aRuledFrontispiece-1`. This unit and the slot
  contract both write `tools/memory-tree/gen_build_index.py`, and their acceptance criteria
  referenced each other's commit tips, so neither could be built, graded or reviewed alone.
  Two review rounds each dissolved the previous round's cross-unit contradictions and produced
  new ones — the second round's blocker that two documents both claimed to be where the new
  regions first enter the corpus, with no document naming the loser, is this defect stated
  exactly. The scope below is not withdrawn: it moves intact into the successor's generated
  surface, which is one mechanism rendered by one commit. Nothing here is abandoned; the
  DECOMPOSITION is.
- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit. The deferral of the marker pair's insertion to the
  retrofit unit was the set's largest blocker — no unit carried it — so S5 now states that the
  generator creates a missing pair and cites `TOOL-aRuledFrontispiece-1` as its owner, and new S8
  lands the corpus re-render that creation causes in this unit's own commit rather than leaving check
  9 red across later units. Split `ORDER_RE` into an anchor and a value shape, because one extracting
  regex cannot tell "no verb" from "malformed verb" and so cannot produce AC5's message; the split
  mirrors `RECORDS_SENTENCE` and `RECORDS_ANCHOR`. Dropped §4's claim that the id sequence IS the
  plan's `#` column — this build is the counter-example — and stated that the region cannot replace
  the authored table while an unspecced unit exists. Pinned the header line's shape and the
  step/no-step collation, which were unspecified. Restated the paired doc edit as a template edit
  followed by `--render`, the direction `kit-dogfood-parity.test.sh` declares. Retargeted AC1 onto
  this unit's parent commit rather than a base count the build's own folder postdates, and replaced
  the byte-identity AC with a corpus observation. Recorded park P4's resolution, and dropped §4's
  stale claim that the build README's row for this unit names its verbs in the plural — that row
  reads singular now.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `status header verb pointer
tail order parallel group marker region apply_region opt-in presence sequence key derived render`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| splice into a named marker pair | `apply_region` at `gen_build_index.py:493` | REUSE the parameterised form `TOOL-aRuledFrontispiece-1` ships; add only the create-or-splice wrapper |
| place a pair a README does not carry | the slot-position insertion `TOOL-aRuledFrontispiece-1` ships | REUSE unchanged — this unit spells no position of its own |
| refuse an anchored value the shape pattern does not match | `strip_records_sentence` at `gen_build_index.py:396` | REUSE THE SHAPE — an anchor literal beside a shape pattern, refusing on the difference |
| render a table from unit records | `render_region` at `gen_build_index.py:358` | REUSE THE SHAPE — same row grammar and same relative-link form |
| sort units by numeric sequence | `_roster_sort_key` at `gen_build_index.py:254` | REUSE unchanged — it already splits an id and coerces the sequence to `int` |
| read a field out of a status header | `parse_spec` at `gen_build_index.py:200` | EXTEND — one added key, read from the line `HDR_RE` already matched |

The `tools/codebase-map/reuse_lookup.py` probe for "parse a verb out of a spec status header and
render a build order table" returned `render_region`, `render_live` and `render_shards` in
`gen_build_index.py` as the only marker-region renderers in the corpus, and returned no seam that reads
a named field out of a status header — `parse_spec` is the sole reader. The claims that `HDR_RE` and
check 12's header predicate are both unanchored at the end, and that `_roster_sort_key` coerces the
sequence numerically, were each verified against source at writing time. At rev-2 the anchor/value
split was re-read at source before being adopted: `RECORDS_SENTENCE` and `RECORDS_ANCHOR` are two
constants at `gen_build_index.py:392-393`, and the anchored-without-a-match refusal is raised at
:450-454, separately from the more-than-one-match refusal at :457-461.

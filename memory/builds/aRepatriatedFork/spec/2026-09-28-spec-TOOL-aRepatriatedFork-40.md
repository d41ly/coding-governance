# TOOL-aRepatriatedFork-40 — recall anchors an id on the spec H1 that defines it

**Status:** SPECCED · rev-1 · 2026-09-28 · node a · Tier-1 · base d486ea50 · streams tooling · order 19

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The recall extractor anchors an id only on an H2-H6 heading, a list row or a table row that opens
with it. A spec H1 is not an anchor. The index generator's `spec_ids` reads that same H1 as the one
place an id is defined, and after inCMS rewrote its check-13 claim lines, it is the only defining
line many ids have left. At inCMS 8 ids lost their recall anchor that way, two graded fixture targets
stopped resolving, and the alias check fell to 1610/1613. Owner ruling, 2026-09-28: the extractor
treats a spec file's H1 under `<MEMORY_ROOT>/builds/<slug>/spec/` as an anchor, and it decides that
with the predicate `spec_ids` uses, not a copy of it.

## 2. Scope (IN)

- **S1** — The predicate moves into the memory-tree kit's `tree_lib.py` as one function. It takes a
  repo-relative path, the file's text, the memory root and the family prefixes, and returns the line
  and id of the first unfenced H1 that defines an id, or nothing. The path must sit under
  `<MEMORY_ROOT>/builds/<slug>/spec/` at any depth. `spec_ids` in `gen_build_index.py` becomes a loop
  over it. Observed by AC3.
- **S2** — `extract_records` in the recall kit anchors that H1. It reaches `tree_lib.py` through the
  sibling-kit resolver `TOOL-aRepatriatedFork-2` built, carried inline as the gated byte-identical
  block. The import happens on the first call, so a program that reads only the grammar never needs
  the sibling kit. When the resolver finds no memory-tree kit, the call raises and names where it
  looked. Observed by AC1 and AC2.
- **S3** — The H1 record owns its own line down to the next heading of any level. That is the title,
  the status header and the preamble, never the whole file. Observed by AC1.
- **S4** — A query naming such an id returns the defining spec's record first, ahead of a file that
  only cites the id. Observed by AC4.
- **S5** — The recall selftest's fixture repo lays the memory-tree kit's `tree_lib.py` beside the
  recall kit, which is the layout `requires = ["memory-tree"]` already declares. memory-recall and
  memory-tree take a version bump in every carrier. Observed by AC5.

## 3. Non-goals (OUT)

- Check 13's definition in `corpus_ids.py`. It already counts any H1 as defining, a wider set, and
  this unit does not narrow it.
- An H1 outside a build's `spec/` folder. A journal or review titled with an id stays a citation, as
  it is for `spec_ids`.
- Chunk rollup. A spec's chunks keep rolling up by path, so sub-specs sharing one H1 id stay
  distinct parents.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the inCMS corpus whose check-13 rewrite left these ids
  defined only by a spec H1. That unit's recall-regression leg is where the two lost targets and the
  1613 alias ids are graded.

## 4. Design

### Evidence

At inCMS `63439e269`, the recall-regression leg exits 1. It reports that `ARCH-dHushedEmbargo-2` and
`ARCH-aLeasedGauntlet-1` resolve to nothing, and prints `1610/1613 alias ids anchored`. Each of the
eight ids has a spec H1 under its own build's `spec/` folder. Before `4d34ae6d9`, another build's
table row or heading carried the id in its first cell, and the extractor anchored that instead.

The extractor rejected H1 anchors on purpose. An H1 anchor owns the whole file down to the next H1,
and the comment at `A_HEADING` measured that as a jump in indexed characters. S3 keeps the record to
the preamble, so that cost does not come back.

### The kit boundary

memory-recall declares `requires = ["memory-tree"]` in its `kit.toml`, and it already reads that kit's
conf. So recall reaching into memory-tree is the declared direction. memory-tree's `corpus_ids.py`
and `merge-rows.py` reach the other way, into `extract.py`, for the grammar only. `tree_lib.py`
imports nothing from either kit, so no import cycle forms. The lookup goes through
`resolve_kit_dir`, which reads the install receipt first. That is how inCMS finds `tree_lib.py` at its
`scripts/` prefix.

The import is deferred to the first `extract_records` call. The merge driver's fixtures and
check-wiring's smoke copy `extract.py` without memory-tree beside it, and they only read the grammar.

### Inventory

One new function, `parse_spec_h1`, in `tree_lib.py`. `spec_ids` keeps its name and signature.
`extract.py` gains the inline resolver block and a deferred loader for the function.

### Files touched (estimate)

`tree_lib.py`, `gen_build_index.py`, `extract.py`, and the recall selftest. The two kits' version
carriers and any map dossier that claims the new key.

### Alternatives rejected

- A copy of the H1 regex in `extract.py`, pinned to `spec_ids` by an arm. The owner asked for one
  predicate, and the resolver makes sharing possible.
- Moving the predicate into `extract.py`. `gen_build_index.py` would then need the recall kit, which
  memory-tree does not require.
- Letting the H1 own its section to the next H1. That is the whole file, the cost the extractor's
  own comment measured.

## 6. Acceptance criteria

- **AC1** — In the recall selftest, a fixture holds a spec whose H1 is the only defining line for its
  id, and another file that only cites the id. The built extractor writes a record for the id at the
  spec's path, and that record stops before the spec's first `##`. The citing file writes no record.
  The d486ea50 extractor writes no record for the id.
  Red when: the spec H1 does not anchor, or the record runs past the preamble.
- **AC2** — In the same selftest, an H1 carrying an id under a build's `build/` folder writes no
  record, and neither does an H1 inside a fenced block of a spec.
  Red when: an H1 outside a spec's defining position anchors.
- **AC3** — Over that fixture, the set of ids the extractor anchors on an H1 equals what
  `gen_build_index.spec_ids` returns.
  Red when: the two readers disagree.
- **AC4** — In the recall selftest, a `query.py` search for the id returns the spec's record as
  hit 1.
  Red when: a citing file outranks the defining spec.
- **AC5** — Gov's `check-recall.py` and `test_recall_floor.py` read the same or better than at
  d486ea50. At a read-only clone of inCMS `63439e269` carrying the new `extract.py` and `tree_lib.py`,
  the recall-regression leg reports both targets resolving and `1613/1613 alias ids anchored`.
  `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch --base
  f8fdd873` reports no FAILED entry.
  Red when: a carrier keeps the old version, or a floor falls.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `build-index selftest` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: `tools/memory-recall/selftest.py` · `a spec H1 anchors the id it defines` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft, from the owner's ruling.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the id a spec file's H1 defines under builds spec"`
ranked name-stem neighbours only. It named neither `spec_ids` nor `anchor_at`, and it cannot see
shell. The predicate this unit shares was found by grep, in `gen_build_index.py`, and this unit moves
it rather than writing a second one.

Recall terms used: `H1 anchor spec_ids extract_records anchor_at grammar_for defined id spec H1 byte
profile records check 13`.

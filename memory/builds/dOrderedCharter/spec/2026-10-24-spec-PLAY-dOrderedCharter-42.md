# PLAY-dOrderedCharter-42 — the bindings reader admits every kind the record factory mints, joined to its file name both ways

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 12 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-42-deviation-421.md](../build/2026-10-24-build-PLAY-dOrderedCharter-42-deviation-421.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 31 at HIGH**, its item **H4**. Units 7, 2 and 15 write records headed
`**Serves:** exception|override|change <unit id>` through unit 7's factory, but
`RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`) admits only `spec-audit`, `diff-review`,
`journal`, `research` and `deviation`, and `read_bindings` marks any other first token malformed
(`:561-565`). Every record written through the three new doors would then print an `A` row from
`gen_build_index.py --print-bindings` and red memory-hygiene check 21: the change record unit 15
writes on every instruction edit, and the one unit 31 S6 writes per census move. This unit adds the
three kinds to the reader, makes the factory's kind list and the reader's one list, and extends the
deviation kind's file-name join to every typed kind. It repairs unit 7 and is built right after it,
before unit 15 (order 16) and unit 2 (order 20) mint their kinds.

## 2. Scope (IN)

- **S1** — The tokens. `tools/memory-tree/tree_lib.py` gains `TYPED_RECORD_KINDS = ("deviation",
  "exception", "override", "change")`, the kinds whose records the factory names
  `<date>-build-<unit id>-<kind>-<n>.md` in a build's `build/` folder, and `RECORD_KIND_TOKENS`
  becomes `("spec-audit", "diff-review", "journal", "research") + TYPED_RECORD_KINDS`, so
  `**Serves:** exception <unit id>`, `override` and `change` bind. Observed by AC1.
- **S2** — One list. Unit 7's factory, `tools/memory-tree/build_records.py`, imports
  `TYPED_RECORD_KINDS` from `tree_lib` as its kind list, and its per-kind table of required fields and
  closed sets is refused at import, naming the kind, when its keys differ from that tuple. A kind
  added to the factory without the reader, or to the reader without the factory, fails on load.
  Observed by AC2.
- **S3** — The file-name join, every typed kind. The deviation rule `read_bindings` applies today
  (`tools/memory-tree/tree_lib.py:566-576`, TOOL-dTrueNorth-4 S2) is generalised to each member of
  `TYPED_RECORD_KINDS`: a file named `-<kind>-<n>.md` in a `build/` folder whose Serves kind is not
  `<kind>` is malformed, and a record whose Serves kind is a typed kind and whose file is not so named
  is malformed, each naming the kind. The deviation wording is kept for the deviation kind.
  Observed by AC3.
- **S4** — The round trip, armed. The factory gains `python tools/memory-tree/build_records.py
  --fixture --plant typed-kinds`, in the shape of `deviation_join.py --fixture`: it writes one record
  of every kind `TYPED_RECORD_KINDS` names into a build folder of a scratch git repository, through the
  factory's own `new <kind>` verb where the kind has one and through its record writer otherwise, and
  asserts that `read_bindings` returns each as `bound` and that `gen_build_index.py --print-bindings`
  over that repository prints no `A` row. Observed by AC4.
- **S5** — The doc. The closed kind list of `tools/memory-tree/HYGIENE.template.md:628-630`, rendered
  into `memory/HYGIENE.md`, gains `exception`, `override` and `change`, each with a half-line naming
  the unit that mints it. Observed by AC5.

## 3. Non-goals (OUT)

- The factory itself, its name grammar and the exception kind's fields: unit 7's (S7, S8).
- The override and change kinds' fields and writers: units 2 and 15. This unit admits their tokens
  before they land, so their first record binds.
- Single-line field values at the factory's write boundary: a minor of the same review, batched in
  `PLAY-dOrderedCharter-49`.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-7` — the record factory module and its per-kind table, which S2 binds to the reader's list and S4 drives; without it there is no factory to round-trip
- **hands-off** `PLAY-dOrderedCharter-2` — the override kind's token, admitted here before that unit's first override record is written
- **hands-off** `PLAY-dOrderedCharter-15` — the change kind's token, admitted here before that unit's first change record is written

## 4. Design

### Evidence

Read at `ce13efbe`. `RECORD_KIND_TOKENS` is the five-member tuple at `tools/memory-tree/tree_lib.py:406`;
`read_bindings` takes the first token of a Serves line as the kind when it is a member (`:544`) and
otherwise sets `state = "malformed"` naming the five (`:561-565`). `gen_build_index.py` imports the
tuple (`:187`), and `cmd_print_bindings` (`:682`) is the predicate check 21 reads. The deviation
kind's both-ways file-name join is `deviation_named` (`tools/memory-tree/tree_lib.py:491`) and its use
at `:566-576`. Unit 7 S7 extracts the factory from `tools/memory-tree/deviation_join.py` into
`build_records.py`, in the same kit as `tree_lib.py`; S8 writes `**Serves:** exception <unit id>`.
Unit 2 S4 writes `**Serves:** override <unit id>` and unit 15 S7 `**Serves:** change <unit id>`;
neither spec names `tree_lib.py`.

### Data model

```python
# tools/memory-tree/tree_lib.py
TYPED_RECORD_KINDS = ("deviation", "exception", "override", "change")
RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal", "research") + TYPED_RECORD_KINDS
```

The order of `RECORD_KIND_TOKENS` is unchanged for its first five members, so the malformed reason
`read_bindings` prints lists them as it does today, the new three after.

### Why the list lives in tree_lib

`tree_lib.py` is the kit's base module: `gen_build_index.py`, `deviation_join.py` and the factory all
read it, and it imports none of them. Putting the list in the factory would make the reader import
the factory, a cycle through `deviation_join.py`. The factory reads the list; the reader owns it.

### Inventory

Minted: the tuple `TYPED_RECORD_KINDS`; the kind tokens `exception`, `override` and `change` in
`RECORD_KIND_TOKENS`. No file. Naming cells: `lexicon naming predicates` grades the constant.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/gen_build_index.py` (its selftest's bindings fixture, if it enumerates kinds)
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md` (its render, never edited)

### Rollout

Live at landing, order 12, after unit 7 at order 11. The kit's version bump is minted by
`push-main.sh` into the prepared merge, as `tools/memory-tree/check-verdict-epoch.sh` states in its
header.

### Alternatives rejected

- **Adding each token in the unit that first mints its kind**, the review's first fix. Three edits
  of one tuple by three writers, and the two later units' specs do not name the file; one edit here,
  joined to the factory, cannot be forgotten by a fourth kind.
- **Deriving the reader's list by importing the factory.** The import cycle above.

## 5. Production-readiness checklist

- security: no new write path; the reader admits three more tokens and grades their file names.
- perf / scale: none measurable; one tuple membership and one regex per record, as today.
- error / empty / loading states: a factory whose kind table disagrees with the tuple refuses at
  import, naming the kind; a mis-named typed record is malformed with its reason.
- observability: check 21's malformed reason names the kind and the expected file name.
- risks: a record already in the tree named `-exception-<n>.md` or similar with another kind would now
  red; none exists (`git ls-files` over `memory/builds/*/build/` for the three name shapes printed
  nothing at `ce13efbe`, PINNED 2026-10-24).
- testing: AC1 to AC4 by probe and fixture; the round trip is a selftest arm (§7).
- migration: none.
- user docs: S5, the closed kind list in `tools/memory-tree/HYGIENE.template.md`, rendered into
  `memory/HYGIENE.md`.

## 6. Acceptance criteria

- **AC1** — When a probe at this repo's root imports `tree_lib` and calls `read_bindings` over a
  scratch git repository holding one tracked record of each of `exception`, `override` and `change`,
  each correctly named, every record's state is `bound` and its kind is its token.
  Red when: a token is missing from `RECORD_KIND_TOKENS`, so its record reads `malformed`.
- **AC2** — When a probe imports `build_records` from a scratch copy of `tools/memory-tree/` whose
  factory kind table carries a fifth kind `widget`, the import raises naming `widget`; with the table
  as shipped, `set(build_records.KINDS) == set(tree_lib.TYPED_RECORD_KINDS)` prints `True`.
  Red when: the factory's kinds and the reader's list can differ and load.
- **AC3** — When the probe of AC1 adds a file `<date>-build-<unit id>-change-1.md` whose Serves line
  says `journal`, and a file `notes.md` in a `build/` folder whose Serves line says `exception`, both
  read `malformed`, each reason naming the kind.
  Red when: a typed kind's name and its Serves kind can disagree and bind.
- **AC4** — When `python build_records.py --fixture --plant typed-kinds` runs, it
  writes one record per member of `TYPED_RECORD_KINDS` into a scratch repository and reports
  `gen_build_index.py --print-bindings` printing no `A` row.
  Red when: a kind the factory mints is not admitted by the reader.
  figure: DERIVED, the kinds read from the tuple at run time.
- **AC5** — When a probe reads the bullet of `tools/memory-tree/HYGIENE.template.md` that opens with
  the closed `<kind>` list, it names every member of `TYPED_RECORD_KINDS` as a backticked kind.
  Red when: the doc's closed list still stops at `deviation`, or a word elsewhere in the file passes
  for the kind.

## 7. Gates

`memory hygiene` · `build-index selftest` · `memory-hygiene self-test` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `tier2-review self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/build_records.py · covers AC4 · its `--fixture --plant typed-kinds` round trip over every typed kind, run by the memory-hygiene self-test, its failing case staged by the base tuple without the three tokens · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 7's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Where the kind list lives.** Options: (a) in `tree_lib.py`, read by the factory; (b) in the
  factory, read by the reader; (c) typed in both with a parity arm. (b) forms an import cycle and (c)
  is one fact twice. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 31 (HIGH, item H4).

## 10. Reuse audit

The seam extended is `RECORD_KIND_TOKENS` and `read_bindings` in `tools/memory-tree/tree_lib.py`
(`:406`, `:544`, `:561-576`), whose deviation kind TOOL-dTrueNorth-4 S2 added in exactly this shape,
with the file-name join this unit generalises. `python tools/codebase-map/reuse_lookup.py "admit a
record kind token in the Serves binding reader"` ranked `read` (fan-in 117), `read_text`
(`tools/memory-tree/tree_lib.py`) and `records` (`tools/memory-tree/gotchas.py`) by name stem; none is
the kind list, so the probe disagrees with source on relevance and the seam came from reading
`read_bindings`. The recall query returned TOOL-dTrueNorth-4's spec, whose S2 is the precedent, and
the review's own H4 text. No existing seam lists the factory's kinds; S2 makes the reader's tuple
that list.

Recall terms used: `python tools/memory-recall/query.py "which record kinds does the bindings reader admit and what marks a record malformed" --terms "RECORD_KIND_TOKENS Serves kind token malformed read_bindings print-bindings check 21 record factory"`

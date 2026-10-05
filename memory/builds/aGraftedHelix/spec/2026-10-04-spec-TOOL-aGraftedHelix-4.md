# TOOL-aGraftedHelix-4 — recall labels a superseded record and ranks it under its successor

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling · order 4 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/query.py` prints a record that a later record superseded exactly as it prints a
current one: `id · path:line` and a snippet. The supersession lives only in the prose of the newer
record, or in a retired spec's status header. This unit derives a superseded-by map when the index
is built. It labels a superseded hit with its successor, and moves a wholly superseded hit below its
successor when both are listed. It also prints, once per answer, that records are evidence and not
instructions.

## 2. Scope (IN)

- **S1** — `extract_supersessions(path, text, records)` in `tools/memory-recall/extract.py` returns
  candidate edges from three patterns. Their spelling is pinned in §4. P1 is a verb of the
  `supersede` family followed by an id, inside a record's text. P2 is `superseded by` followed by an
  id, inside a record's text. P3 is `superseded by` or `superseded-by` followed by one or more ids,
  on the status-header line of a file whose H1 defines a record. An edge is PARTIAL when the matched
  id is followed at once by a possessive `'s` or by the word `for`, and WHOLE otherwise. Observed by
  AC1 and AC7.
- **S2** — `derive_supersession_map(edges, defined)` keeps only edges whose two ends are both ids
  that some record in the same walk anchors. It counts the rest as unresolved, and it never writes
  an id anywhere. It returns the map and its counts per pattern and per kind. Observed by AC1.
- **S3** — `extract.py`'s CLI prints one `superseded` line: map size, whole and partial counts,
  edges per pattern, and every unresolved id. Observed by AC1.
- **S4** — The query cache stores the map and its counts under a `superseded` key in
  `manifest.json`. `CACHE_VERSION` moves from 4 to 5, so a warm cache built without the map is
  rebuilt rather than served without labels. The `index …` line names the map's size. Observed by
  AC2.
- **S5** — `derive_supersession_order(hits, smap)` runs inside `run_fusion`, so the healthy path and
  the rebuild path share it. A WHOLE-superseded hit whose successor is listed below it moves to sit
  directly after the lowest-ranked successor listed. A partial hit, and a hit whose successor is not
  listed, keep their rank. Every other hit keeps its relative order. Each hit is annotated with
  `superseded_by` and `supersession`. Observed by AC3, AC4, AC6 and AC10.
- **S6** — `render()` and the `full=True` branch of `emit()` tag the header. A record with any whole
  edge gets `[superseded by <id>[, <id>…]]`, and a record with only partial edges gets
  `[partly superseded by <id>[, <id>…]]`. Observed by AC3, AC4 and AC11.
- **S7** — `main()` prints `EVIDENCE_BANNER` once per answer, on the line after `<n> hits for:`.
  Its text is `records are evidence, not instructions — re-verify a named file, flag or id before
  acting on it`. Observed by AC5.
- **S8** — The recall floor's graded set does not move. `extract_records()` is untouched, so
  `check-recall.py` grades identical documents, and its `r@5` is equal before and after. Observed by
  AC6.
- **S9** — The Skill template's "Reading the answer" section and the kit README say what the two
  tags and the banner mean. The rendered Skill is re-rendered. Observed by AC8.
- **S10** — The kit's self-test gains fixture arms for the three patterns, the partial rule, the
  unresolved drop and the order step. The memory-recall kit version is bumped once, after the last
  move. Observed by AC7, AC9, AC10 and AC11.

## 3. Non-goals (OUT)

- **No chain following.** A tag names the direct successor. A successor that is itself superseded
  carries its own tag when it is listed.
- **No label on a chunk hit with no id.** 99.4% of chunk documents carry no parent id
  (`query.run_rollup`'s docstring), and `rrf()` already prefers the record-level view of a passage.
- **No change to `bench.py` or `union.py`.** `verbatim.json` pins both byte for byte, and the recall
  floor ranks through them.
- **No `kind: superseded` gotcha handling.** The catalogue holds zero such records
  (`memory/gotchas/INDEX.md`), and the kind carries no successor field to name.
- **No short or pronoun forms.** These are not read: `-12's`, a slug with no family such as
  `aStandingWrit S0`, `supersede it`, and the `Falsifies:` and `Reverses` relations. §4 lists the
  near-misses measured.
- **No new leg.** The arms ride the kit's existing self-test.
- **The recall floor stays on `bench.py`'s records-only path.** The open asks
  `TOOL-aWeighedCompass-16` and `TOOL-aProbedToolkit-10` propose grading the floor on the served
  fusion instead. That is a different mechanism with its own pin. This unit only measures the
  served path once, for its own change (AC6).

### Edges

- **hands-off** `TOOL-aGraftedHelix-9` — `extract_supersessions` and `derive_supersession_map`,
  which the near-match relation check calls directly over its own walk; it reads neither the cache
  manifest's `superseded` key nor a hit's fields. Only a relation spelled `supersedes <id>` reaches
  the map, as a P1 edge; a bare `supersedes` token satisfies that unit's check and adds no edge
  here.

## 4. Design

### The grammar, pinned

```python
W = r"[`*\[]*"                                   # optional wrapping before an id
P1 = r"\bsupersed(?:e|es|ing)\s+" + W + "(" + ID + r")\b"          # old = the cited id, new = this record
P2 = r"\bsuperseded\s+by\s+" + W + "(" + ID + r")\b"              # old = this record, new = the cited id
P3 = r"\bsuperseded[ -]by\s+((?:" + W + ID + r"\b[`*\]]*[\s,]*)+)" # on a `**Status:** ` line in a file's first five lines; old = the H1 id
PARTIAL = r"^[`*\]]*(?:['’]s\b|\s+for\b)"                     # matched against the text right after the id
```

All three are case-insensitive, and so is `PARTIAL`, because this corpus writes `SUPERSEDES` in
capitals and can write the clause after it the same way. `ID` and `ID_RE` are the module's own grammar, and P3's H1 id comes
from `load_parse_spec_h1()`, the predicate `extract_records` already calls. P3 reads the status
line's text and no status grammar. It needs no token check, because a header tail carries pointers
and declared verbs only (`memory/TEMPLATE-SPEC.md`), so a `superseded by <id>` there is a pointer
whatever the status. A self-edge is skipped.

### Measured over the real corpus

PINNED: 2026-10-04 at `89bcefc8` on node `a`, by a read-only scratch probe that applies exactly the
patterns above to `E.corpus_files` and `E.extract_records`. Re-derived by AC1 at the pass.

| pattern · kind | edges kept |
|---|---:|
| P1 · partial | 8 |
| P1 · whole | 1 |
| P2 · whole | 3 |
| P3 · whole | 13 |
| unresolved | 0 |
| self-edges | 0 |

The map holds 23 superseded ids: 15 carry a whole edge and 8 are partial only. The corpus has 2732
files, 2132 records and 1567 defined ids. Every P1 match except one is possessive or `for`-qualified,
for example `SUPERSEDES TOOL-aWidenedGuide-1's PREMISE, not its value`. The PARTIAL rule
classifies all 8 of those correctly. The one whole P1 edge is the `TOOL-aSurfacedLexicon-18` row,
which opens with `SUPERSEDES` followed by the backticked `TOOL-dScaffoldedMirror-18` and a colon.
Whole-edge precision is 16 of 17. The miss is
`TOOL-dMispairedQuote-7`, whose row quotes its own retracted pointer ("this row read SUPERSEDED BY
`TOOL-aClosedDocket-4`"). It is kept as a measured residual, because the only rules that exclude it
are positional or lexical guesses fitted to one row. P3 contributes the retired-spec headers, for
example `TOOL-aClosedDocket-4 → TOOL-dFoldedVerdict-1, -2, -3`. Before P3 existed, the records'
text could not see these headers, because a spec's H1 record is its title row only.

Near-misses the grammar leaves out on purpose, from the same probe: 46 records mention
`supersed`. Beyond the 11 P1/P2 matches, the shapes are an id after intervening words (`SUPERSEDES
the finding in`), a sequence with no slug (`SUPERSEDES -12's`), a slug with no family
(`superseded by aStandingWrit S0`), a pronoun (`this row and … supersede it`), and prose with no id
at all.

### The order step — and why it is not a score multiplier

`rrf()` scores a hit one source found at rank `r` as `1/(60 + r)`, where `RRF_K` is 60 and `k` is 20
per source. Multiplying a superseded hit's score by helixir's 0.6 places it below any undemoted
single-source hit at rank `s` whenever `s < 40 + 1.67r`. Every single-source hit has `s ≤ 20`, so
the inequality holds for every `r`. The multiplier therefore sinks every single-source
whole-superseded hit below every other single-source hit in a pool of up to 40. The reader then meets
the label far from the successor it names, or never meets it once the byte budget cuts the list.
The rare hit both sources found, which needs the same path, line and leading 60 characters in both
sets, can keep the top rank under the same multiplier. So its effect is not even uniform across
what it demotes. That arithmetic over the shipped constants is the test that rejected the
multiplier (§8 F1). The order step instead puts a successor first and keeps the label beside it:

```text
before:  [1] TOOL-dScaffoldedMirror-18   [2] memory/DECISIONS.md:133   [3] TOOL-aSurfacedLexicon-18
after:   [1] memory/DECISIONS.md:133     [2] TOOL-aSurfacedLexicon-18  [3] TOOL-dScaffoldedMirror-18 · …  [superseded by TOOL-aSurfacedLexicon-18]
```

The `before` row is PINNED from a live query at `89bcefc8`, the one AC3 names. The step moves a hit
DOWN only, and only past its own successor. No other hit can lose rank to it.

### What the recall floor can and cannot see

`RECALL_FLOOR` is `records:fts5:r@5>=0.81`. `check-recall.py` ranks the `records` set through
`bench.py`'s fts5, and that path never calls `query.run_fusion`. So the floor cannot see the order
step, and asking it to measure the demotion would be a test that cannot fail. What it CAN see is
whether this unit moved the extracted documents, so S8 holds it as a conservation check: 0.8333 at
`89bcefc8`, measured 2026-10-04 in 5.4 s.

The demotion's own measurement is on the served path, over the fixture's 12 expected ids. None of
them is whole-superseded. One, `TOOL-aWidenedGuide-1`, is partial, so the step never moves it. The
step only moves a hit down, so no expected id can rank lower. AC6 observes that over all 12
questions instead of trusting the derivation.

### Cache and manifest

`_docs()` already walks every file through `extract_records`. It gains the `extract_supersessions`
call per file and one `derive_supersession_map` call after the walk. The manifest's `superseded`
key holds `{"edges": {old: [[new, kind], …]}, "counts": {...}}`. At 23 ids that is about 2 KB.
`ensure_cache` keys freshness on `CACHE_VERSION`, and the move to 5 forces one rebuild of 6-15 s
(PINNED from the live manifests' `built_s` on node `a`). The `index` line becomes
`index <r> records + <c> chunks · superseded <n> (<w> whole, <p> partial) (<cached|rebuilt …>)`.

### Inventory

| identifier | where | cell |
|---|---|---|
| `extract_supersessions` | `extract.py` | `py.function` |
| `derive_supersession_map` | `extract.py` | `py.function` |
| `derive_supersession_order` | `query.py` | `py.function` |
| `render_supersession_tag` | `query.py` | `py.function` |
| `EVIDENCE_BANNER` | `query.py` | constant |
| `superseded_by`, `supersession` | keys on a hit dict | n/a |

`render_supersession_tag(hit)` is the one spelling of the S6 tag, which `render()` and `emit()`'s
`full=True` branch both print; a copy in each would be two answers to one question. `run_fusion`
takes the map as a fourth parameter, `smap`, which `main()` passes from the manifest on both the
healthy and the rebuild call, and an empty map moves nothing.

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-04 and answered OK; `render_supersession_tag` on 2026-10-05. No new file, leg, conf key or gotcha, so the map gains no inventory
key.

### Files touched (estimate)

- `tools/memory-recall/extract.py`
- `tools/memory-recall/query.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md`
- `memory/map/features/memory-recall.md`

Both ported modules' docstrings list their forked constructs, so a re-pull stays a three-way merge.
`extract.py` gains a seventh and `query.py` an eighth.

### Alternatives rejected

- **A 0.6 score multiplier, helixir's constant.** The arithmetic above shows it buries the label far
  from the successor it names.
- **Demoting partial supersessions too.** Seven of the eight possessive or `for` edges supersede one
  clause, for example a premise or a value. Their records stay half-current, and one of them,
  `TOOL-aWidenedGuide-1`, is a fixture expected id.
- **Excluding `TOOL-dMispairedQuote-7` by position or by the word `read`.** Either rule is fitted to
  one row, and it would fire on the next row written differently.
- **A separate `superseded.json` beside the databases.** The manifest is already read on every query
  and is atomic, so a second file is a second freshness question.

## 5. Production-readiness checklist

- security — N/A: read-only derivation over tracked prose, printed to the caller.
- perf / scale — three regex passes per record at build time, inside a walk that already reads every
  file. The query path adds one list pass over at most 40 hits. One forced rebuild of 6-15 s.
- error / empty / loading states — an empty map prints `superseded 0`, never omits the clause. A
  cache missing the key is stale by `CACHE_VERSION`, never served unlabelled.
- observability — the `extract.py` report line and the `index` line's map size, so a map that
  derived nothing reads as zero out loud.
- risks — one measured false whole edge, labelled and moved. Partial edges are never moved, so a
  wrong partial costs a label, not a rank.
- testing — fixture arms in the kit self-test (S10), each observed red with its predicate disabled.
- migration — the cache rebuilds once; no tracked data changes.
- user docs — the Skill's "Reading the answer" section and the kit README.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/extract.py . <scratch dir>` runs on the built tree, it
  prints a `superseded` line reporting the map size, whole and partial counts, edges per pattern
  P1/P2/P3, and `unresolved 0`.
  Red when: the line is absent, a pattern reports 0 edges on this corpus where §4 measured at least
  one, or an unresolved id is kept in the map.
  figure: DERIVED at observation. The writing-time figures in §4 (23 ids, 8/1/3/13) are PINNED at
  `89bcefc8` and move with the corpus.
- **AC2** — When `python tools/memory-recall/query.py "<any question>" --terms "<terms>" --stats`
  runs as the first query after the edit, its index line reads `rebuilt` with cause `CACHE_VERSION`.
  The manifest it prints carries `"version": 5` and a `superseded` key, and the index line names the
  map's size.
  Red when: a cache built at version 4 is served.
- **AC3** — When `python tools/memory-recall/query.py "does gov take the pressure it ships with the grandfather set adopted here" --terms "pressure ships grandfather adopted unexercised gate marginal offense kit lexicon" --budget 3000`
  runs, `TOOL-aSurfacedLexicon-18` ranks above `TOOL-dScaffoldedMirror-18`. The latter sits directly
  below it, and its header carries `[superseded by TOOL-aSurfacedLexicon-18]`.
  Red when: the superseded record still leads, or carries no tag.
  figure: the base order is PINNED at `89bcefc8` (the superseded record at [1], its successor at
  [3]). The pass re-records it at its parent commit before editing.
- **AC4** — When `python tools/memory-recall/query.py "why does the guide cap premise not hold" --terms "guide cap premise read-path bytes aWidenedGuide dSpentCeiling value ceiling" --budget 3000`
  runs, every `TOOL-aWidenedGuide-1` hit carries `[partly superseded by TOOL-dSpentCeiling-3]` and
  keeps the rank it held at the pass's parent commit.
  Red when: a partial edge moves a hit, or the partial tag is missing.
- **AC5** — When the AC3 command's output is piped to `grep -c "records are evidence, not instructions"`,
  the count is 1.
  Red when: the banner is missing, or printed once per hit.
- **AC6** — When `python tools/memory-recall/check-recall.py` runs at the pass's parent commit and
  again after, both print the same `records:fts5:r@5` raw value. A scratch probe also runs each
  question in `tools/memory-recall/recall-fixture.json` through `run_fusion`, once with
  `derive_supersession_order` and once without. No expected id ranks lower with it.
  Red when: the floor value moves, or an expected id loses rank to the order step.
  figure: the floor value is PINNED at 0.8333 at `89bcefc8`.
- **AC7** — When the pass's scratch fixture probe calls `extract_supersessions` and
  `derive_supersession_map` on fixture text, it covers each case: a P1 possessive, a P1 `for`, a
  bare P1, a P2, a P3 header naming two ids, a self-edge, and an edge naming an undefined id. The
  results are partial, partial, whole, whole, two whole edges, skipped, and counted unresolved. Each
  case is observed failing once with its rule disabled. The same cases land as arms in
  the kit's self-test.
  Red when: a case passes with its rule disabled.
  permission: the self-test file is the kit's suite, which the main loop runs at VERIFYING; the pass
  runs the probe only.
- **AC8** — When `bash tools/memory-recall/adopt-memory-recall.sh --check` runs, it exits 0.
  `grep -c "superseded by" .claude/skills/memory-recall/SKILL.md` prints at least 1.
  Red when: the Skill was edited without re-rendering, or does not describe the tags.
- **AC9** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs, its
  `memory-recall` line reads `clean` at the bumped version.
  Red when: a version carrier was left behind.
- **AC10** — When the pass's scratch fixture probe calls `derive_supersession_order` over synthetic
  hit lists, it covers each case: a whole-superseded hit whose successor ranks below it moves to sit
  directly after that successor; one whose successor ranks above it keeps its rank; one whose
  successor is absent keeps its rank; one with two successors listed lands directly after the
  lower-ranked of them; and a partial hit keeps its rank. In every case the other hits keep their
  relative order. Each case is observed failing once with its rule disabled, and the same cases land
  as arms in the kit's self-test.
  Red when: a case passes with its rule disabled, or a move reorders a hit it did not pass.
  permission: the self-test file is the kit's suite, which the main loop runs at VERIFYING; the pass
  runs the probe only.
- **AC11** — When the pass's scratch probe calls `emit` with `full=True` over a hit list carrying a
  whole-superseded hit, as the kit's self-test already calls it at `selftest.py:2124`, the hit's
  header carries `[superseded by <id>]`. When it calls `render()` over a hit annotated with two
  whole successors, both ids appear in one `[superseded by <id>, <id>]` tag. Both land as arms in
  the kit's self-test.
  Red when: the full branch omits the tag, or a record with two successors shows one.
  permission: as AC10.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `memory-recall skill wiring` · `kit version markers` · `check-wiring self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness`

New arm: tools/memory-recall/selftest.py · each supersession rule disabled in the working tree · none
New arm: tools/memory-recall/selftest.py · AC10's order cases and AC11's full-branch and two-successor tags; stage each order rule disabled, the full branch's tag deleted and the tag cut to its first id · none

## 8. Open questions

- **F1 — How is a superseded hit demoted: helixir's 0.6 score multiplier, a fixed rank offset, or a
  move to just below its listed successor?**
  The multiplier sinks every single-source whole-superseded hit below every other single-source
  hit (§4 arithmetic). That puts the label far from the successor it names, and past the budget's
  cut on a long answer. It also leaves the rare dual-source hit on top. A fixed offset is a second tuning knob with nothing to measure it
  against. The move satisfies both stated aims, successor first and the label shown, and changes no
  other hit's relative order. RESOLVED (agent, 2026-10-04, delegated): the move, as S5 states.
- **F2 — Are partial supersessions demoted?** Demoting moves records whose other half still stands,
  and one is a fixture expected id. Labelling alone keeps them findable and tells the reader to open
  the successor. RESOLVED (agent, 2026-10-04, delegated): label only, never moved.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 4 section, with the grammar measured
  over the corpus at `89bcefc8`.
- rev-2 · 2026-10-04 · §3 §6 §7 · S5 S6 S10 · AC10 AC11 · folded the round-1 spec audit's findings
  on this unit: 16 (AC10, the order step's fixture cases); 17 (AC11, the `full=True` tag and the
  two-successor tag); and 34 (the hands-off edge to `TOOL-aGraftedHelix-9` rewritten to the
  interface that unit consumes, with the bare-token sentence corrected).
- rev-3 · 2026-10-05 · §4 · the build pass's divergences, before the code: the inventory gains
  `render_supersession_tag`, the one spelling of the tag both renderers print; `run_fusion` takes
  the map as an `smap` parameter; and `PARTIAL` is case-insensitive like the three patterns.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "mark a retrieved record as replaced by a newer decision"`
ranked name-stem neighbours. Of those, `extract_records` in `tools/memory-recall/extract.py` is the
seam this unit extends, and `records` in `tools/memory-tree/gotchas.py` is unrelated. Extended:
`extract_records`'s per-file walk, by calling a sibling beside it and leaving it unedited;
`load_parse_spec_h1`, for P3's H1 id; `_docs()` and `_build_cache()`, for the manifest key;
`run_fusion()`, the one fusion call site; and `render()` and `emit()`. No existing supersession
reader exists. `gotchas.py`'s `superseded` kind is a label with zero records, and the memory-tree
kit's WONTDO successor rule checks only that a successor or reason exists in the tail. Recall
surfaced the two open asks `TOOL-aWeighedCompass-16` and `TOOL-aProbedToolkit-10`. Both measured
that the recall floor grades a configuration the CLI does not serve. That is the fact §4's floor
paragraph rests on, and it is why AC6 measures the served path separately. Reading `extract.py`,
not recall, surfaced the H1-record rule (`TOOL-aRepatriatedFork-40` in its comments): a spec's H1
anchors only its title row. That is why P3 must read the status line itself, since the record text
never contains it.

Recall terms used: superseded SUPERSEDES supersedes recall query render demote snippet rrf fusion WONTDO successor anchor

The question passed with them: "how does recall show that a decision record was superseded by a later one".

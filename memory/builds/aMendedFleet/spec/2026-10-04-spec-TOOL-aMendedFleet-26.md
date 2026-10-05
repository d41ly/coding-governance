# TOOL-aMendedFleet-26 — a `missing:` citation form names an id that has no record, with its own count

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 26

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A record cannot name an id that has no record. Spelled in a present-tense file, the id is cited and
never defined, so hygiene check 14 counts an orphan and the bar reds at a pin of 0. Spelled in any
tracked file, the index generator files it on the roster of the build its slug names. So agents
paraphrase, "node d's build, its unit 25", which no reader can follow and no tool can count. This
unit adds one citation form, the literal prefix `missing:` written immediately before the id, that
both readers recognise: it is not a citation for check 14, it joins no roster, and the corpus
walker counts it on its own. Citing an id that HAS a record is unchanged.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/tree_lib.py`, the kit's shared helper module both readers already
  import, gains `scan_missing_citations`. Given a line or a text and the caller's own id regex, it
  returns the ids written in the form, and the text with each form and its id blanked to spaces of
  the same length, so offsets and line numbers hold. The prefix is spelled once, there. Observed by
  AC1, AC3.
- **S2** — `walk` in `tools/memory-tree/corpus_ids.py` runs each line through S1 before its id
  citation loop, so a marked id never reaches check 14's citation map. The marked ids land in a
  separate map keyed by id, recording the citing files, over every file the walk reads. Observed by
  AC1.
- **S3** — Check 14 gains one clause: a marked id in a PRESENT-tense file that the corpus DEFINES is
  a finding, `marked missing but defined`, naming both files. A record of a moment is not graded,
  because an id defined later was missing when that record was written. Observed by AC2.
- **S4** — `--report` prints the marked count and ids on a line of its own beside the orphan line,
  and `--check` prints nothing new while the clause of S3 holds. Observed by AC1.
- **S5** — `rosters` in `tools/memory-tree/gen_build_index.py` runs each file's text through S1
  before its id scan, so a marked id joins no build's `ids:` roster. Observed by AC3.
- **S6** — Check 14's catalogue entry in `tools/memory-tree/HYGIENE.template.md` gains two
  sentences, the form and its stale clause, and `memory/HYGIENE.md` is re-rendered from it by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Observed by AC4.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- The memory-recall extractor's own orphan report, which counts every id-shaped token in the
  corpus and is not a gate. A marked id stays in it; whether it should leave is that kit's call.
- Product source outside the memory tree. drift-audit's `source_cited_ids_resolving_to_no_record`
  reads it, and a marked id in source is a separate ask.
- A pin on the marked count. The count is reported, not gated: a marked id is a declared gap, and
  the stale clause is what keeps a marker from outliving its gap.
- Rewriting the paraphrases already in the corpus into the form.
- Moving the memory-tree kit version, which this build moves once after the last pass that touches
  the kit.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; none of the files below moved between it and `580dc980`.

- `walk` in `tools/memory-tree/corpus_ids.py` adds every `E.ID_RE` match on a present-tense line to
  its citation map, after the line's anchor test and before its path tokens. The present-tense
  corpus is the memory root's own documents, the build `BACKLOG.md` files under `builds` mode, the
  ledger, `project/` and `guides/`, LESS every append-only path: the hygiene gate's
  `--print-append-only-ere` names `DECISIONS.md` here, so the decision log is NOT graded by check
  14. Specs and reviews are records of a moment.
- `E.ID_RE` is word-bounded, and a colon is a word boundary, so a plain regex cannot tell a marked
  id from a cited one; the reader has to see the prefix.
- `rosters` in `tools/memory-tree/gen_build_index.py` scans EVERY tracked file with its own
  family-alternation regex and files each id on its slug's roster, skipping only its own outputs.
  A citation in a spec reaches a roster; the anchor patterns, which need the id first on its line,
  never match a marked id, so the form defines nothing either.
- `memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md` records both failure modes,
  the head that defines and the body that orphans, and the paraphrase that is today's only escape.
- `python tools/memory-tree/corpus_ids.py --report` at `580dc980`: 1598 ids defined, 978 cited,
  0 orphans. PINNED, measured 2026-10-04.

### Mechanism

```
missing:<the id, with no space between>
```

`scan_missing_citations(text, id_re)` builds one pattern, the escaped prefix followed by the
caller's regex, finds every match, and blanks it. Each reader passes the regex it already uses, so
the form needs no second id grammar. The report line:

```
missing-form ids : <n>  [<ids>]
```

### Inventory

- `scan_missing_citations` in `tools/memory-tree/tree_lib.py`, cell `py.function`.
  `python tools/lexicon/lexicon.py --suggest` answered OK on 2026-10-04.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A waiver row per foreign id.** That is what `memory/project/id-orphan-waiver.txt` is, and its
  pin is shrink-only at 0; each row is a separate edit with a reason, for a gap that is routine.
- **A second id grammar for the form in each reader.** Two spellings of one predicate drift; the
  shared helper takes the caller's regex instead.
- **Counting marked ids against the orphan pin.** The point of the form is that a declared gap is
  not an undeclared one, so mixing the counts loses the distinction it exists to keep.

## 5. Production-readiness checklist

- security — N/A: a text classifier over tracked files; no input boundary, no write path.
- perf / scale — one extra regex pass per line already read; no new file reads.
- error / empty / loading states — no marked id prints a zero count; a marked id that is defined
  in a present-tense file reds by S3.
- observability — S4's report line.
- risks — the form hides a real typo of an existing id; S3 reds when the typo'd id is defined, and
  an undefined typo is exactly what the marker declares.
- testing — direct runs on a scratch clone; the suites are named under §7.
- migration — N/A: an opt-in spelling; no existing citation changes meaning.
- user docs — S6's sentences in the hygiene catalogue.

## 6. Acceptance criteria

- **AC1** — When, in a `git clone --local` of the unit's branch under `%TEMP%`, one line citing an
  id whose slug and sequence no record defines is appended to `memory/README.md` and committed,
  `python tools/memory-tree/corpus_ids.py --check` reds check 14 naming that id as an orphan; when
  the same line is rewritten with the `missing:` prefix, `--check` exits 0, and
  `python tools/memory-tree/corpus_ids.py --report` prints a marked count of 1 naming that id.
  Red when: the prefixed id still counts as an orphan, or the report omits it.
  cost: three runs of a few seconds each.
- **AC2** — When, in that clone, the prefixed line instead names an id the corpus defines,
  `python tools/memory-tree/corpus_ids.py --check` exits 1 with a check 14 line naming the id as
  marked missing but defined. Red when: the stale marker passes.
- **AC3** — When, in that clone, a spec under `memory/builds/aMendedFleet/spec/` gains a line citing
  a sequence of build `aTunedCompass` that its README roster does not hold, and the change is
  committed, `python tools/memory-tree/gen_build_index.py --check` reports that README stale; with
  the citation prefixed, `--check` reports it fresh. Red when: the prefixed citation still moves the
  roster. fixture: the generator reads tracked files only, so each edit is committed before the run.
- **AC4** — When `grep -n "missing:" memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md` runs,
  both print the same sentences inside check 14's entry. Red when: the two copies disagree, which
  the parity leg reds at the close.

## 7. Gates

`memory hygiene` · `corpus-ids selftest` · `build-index selftest` · `memory-hygiene self-test` · `verdict-epoch self-test` · `row-keyed merge driver replay` · `kit/dogfood doc parity` · `gotchas selftest` · `row-grammar selftest` · `backlog migration selftest` · `check-arms selftest` · `transition-audit arms` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

The memory-tree legs past the first four are owed by the kit-directory guard, which the checker
excludes as broad; they are named so the close reads one list.

New arm: tools/memory-tree/corpus_ids.py --selftest · a fixture corpus with a prefixed undefined id in a present-tense file and a prefixed defined id, staged red by skipping S1 in walk · none

New arm: tools/memory-tree/gen_build_index.py --selftest · a fixture whose spec cites a prefixed id of another fixture build, staged red by skipping S1 in rosters · none

## 8. Open questions

- **F1 — Which readers honour the form?**
  Options: check 14 alone; check 14 and the roster derivation; those two plus the recall
  extractor's orphan report and drift-audit's source signal. Check 14 alone leaves a marked id in a
  spec on another build's roster. The last two are report-only readers in other kits.
  RESOLVED (agent, 2026-10-04, delegated): check 14 and the roster derivation.
- **F2 — Does a marked id that is defined red?**
  Options: never; in present-tense files only; everywhere. Everywhere reds history, since a planned
  unit is specced after another record named it. Never lets a marker outlive its gap.
  RESOLVED (agent, 2026-10-04, delegated): in present-tense files only.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `walk`, `rosters`, the anchor patterns and the
  foreign-id gotcha at base, and a corpus report.
- rev-2 · 2026-10-04 · §2 S7 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
- rev-3 · 2026-10-05 · §4 Evidence · §6 AC1 · the build pass: the decision log is append-only here,
  so `walk` never grades it and AC1 as written could not red; AC1 now appends to `memory/README.md`,
  a present-tense file check 14 does grade, and AC2 inherits it as "that clone".

## 10. Reuse audit

The seams are `walk` in `tools/memory-tree/corpus_ids.py`, check 14's one citation loop, and
`rosters` in `tools/memory-tree/gen_build_index.py`, both extended by one call into
`tools/memory-tree/tree_lib.py`, which both already import for the kit's conf parser and spec H1
predicate. `python tools/codebase-map/reuse_lookup.py "cite an id that has no record without creating an orphan"`
returned only name-token neighbours, `records` and the runlog record writers first, and no citation
classifier, so no existing seam encodes a declared-gap form; read in source, `walk` and `rosters`
are the two readers. Recall returned `TOOL-aWeighedCompass-9`, which measured 211 of 889 cited ids
with no record in the recall extractor's orphan list, `TOOL-aTetheredRecord-1`, which drained the
orphan waiver to 0 by defining ids, and the foreign-id gotcha. Where the report and the tree agree:
only citations of ids with no record are forced into prose, and citing an existing id works.

Recall terms used: `python tools/memory-recall/query.py "how should a record cite an id that has no record without orphaning or defining it" --terms "orphan ids check 14 ORPHAN_ID_PIN cited never defined paraphrase dangling id roster foreign build waiver citation form"`

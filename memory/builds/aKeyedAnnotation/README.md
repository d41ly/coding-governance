---
slug: aKeyedAnnotation
node: a
opened: 2026-09-05
streams: tooling
roster: TOOL
ids: TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 TOOL-aKeyedAnnotation-5 TOOL-aKeyedAnnotation-6 TOOL-aKeyedAnnotation-7 TOOL-aKeyedAnnotation-8 TOOL-aKeyedAnnotation-9 TOOL-aKeyedAnnotation-10
---

# aKeyedAnnotation — the annotation layer this repo already has, made correct instead of made bigger

## The problem this build exists to solve
Code annotations were never in scope for the orientation kits, and the assumption behind that was
wrong in both directions. Product source cites unit ids densely and `drift_report.py:466` already
consumes them as evidence a unit shipped, so an annotation layer exists and is load-bearing; nobody
declared it, nothing grades it, and its one dangling pointer has resolved to nothing for its whole
life. Meanwhile the design pass established that the obvious remedy — a grammar, a marker, a
mandate — breaks that same consumer, observed rather than argued. The build that follows is
therefore not the integration the question implied. It repairs the reader that exists, makes live a
validated field that already owns the code-to-decision link, and writes the convention down once.

## Expected improvements
- The one source citation resolving to no record is repaired, and its comment survives the id.
- The repo has one id regex rather than two, and a `.test.sh` citation stops certifying a spec as
  shipped.
- The dossier `decisions` field stops being a validated inert key nothing fills.
- A source-cited id that resolves to nothing becomes visible, at report level, gating nothing.

## Detriments if this is not built
- The next session asking "should annotations cite builds" re-derives the same refutation from
  scratch, having spent the same measurements.
- The shipped-evidence oracle keeps a latent divergence and a self-citing pin comment.
- The reuse audit keeps returning a seam with no rationale while the field holding the rationale
  sits empty and passing.

## Build-level rules
- **The design pass's refusals bind every unit.** No unit adds an id grammar, a marker kind, a
  source-side gate, a recall corpus entry or a tokenizer change. The record states why for each;
  a unit that wants one re-opens the design pass rather than arguing in a spec.
- **Annotation stays VOLUNTARY.** The whole build rests on it: the spec-status oracle discriminates
  only because citation is sparse and late, and unit 2's own signal is the thing that proves it.
- **Unit 1 is prose and lands first.** The convention has to exist before units 2 to 4 write
  comments that must obey it, and it is the only deliverable a reader of the record will look for.
- **Every unit here touches a signal or a pin, so every unit re-measures it in the same commit.**
  A pin copied rather than measured is vacuous or permanently red, and both have shipped here.
- **Units 2, 3 and 4 are ALL sequenced, and unit 4 only became so at the round-1 fold.** Units 2 and
  3 both write `tools/drift-audit/drift_report.py`, so clause 1 of the parallelism rule was already
  unsatisfied for that pair. The audit then established that unit 4's shrink-only pin has no
  mechanism without a ratchet row, and that row lives in `tools/drift-audit/drift_signals.py` —
  which unit 2 also writes, for its narrowed globs and its pin comment. Unit 4 was declared disjoint
  from both and is not. Nothing in this build may now run in parallel, which is a smaller build
  rather than a broken one, and is recorded here because a stale disjointness claim is exactly what
  the `--dispatch` declaration would have been checked against.

## Parked decisions
- **The `gov:` marker vocabulary is unclosed.** Ten kinds are in use with their own consumers and
  nothing grades the vocabulary, so a misspelled marker is silence from every reader. Real, and
  adjacent: no unit here adds a kind, so closing it is a backlog row rather than a prerequisite.
- **A declared recall source can yield nothing, silently.** One declared source does today. The
  extractor reports an absent file and not a present-but-empty one. Filed rather than folded — this
  build declares no source into that corpus, so the defect is not on its path.
- **Supersession has no machine grammar.** The decision log is append-only and only some
  supersession rows name their target in a parseable form, so an annotation can outlive the record
  it cites with no signal. Not addressed here: a structured field is a memory-tree contract change
  and would need its own design pass. Retrofitting the existing rows by regex is explicitly refused.
- **`TOOL-aLexedStripper-7` is a prerequisite for any `map_lib` stripping work.** Unit 4 touches the
  dossier reader and the reuse audit's output, never the strippers, and must stay on that side.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aKeyedAnnotation-1` | OPEN | the annotation convention, written once, and the citation it repairs |
| 2 | `TOOL-aKeyedAnnotation-2` | OPEN | the shipped-evidence oracle reads one grammar and stops certifying itself |
| 3 | `TOOL-aKeyedAnnotation-3` | OPEN | a report-only signal for a source-cited id that resolves to no record |
| 4 | `TOOL-aKeyedAnnotation-4` | OPEN | the dossier `decisions` field becomes live and shrink-only |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 4 unit(s) · node a · opened 2026-09-05 · streams tooling
ids TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 TOOL-aKeyedAnnotation-5 TOOL-aKeyedAnnotation-6 TOOL-aKeyedAnnotation-7 TOOL-aKeyedAnnotation-8 TOOL-aKeyedAnnotation-9 TOOL-aKeyedAnnotation-10

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aKeyedAnnotation-1 — the annotation convention, written once, and the citation it repairs](spec/2026-09-05-spec-TOOL-aKeyedAnnotation-1.md) | 1 | 2 | CLOSED | rev-7 | 2026-09-05 |
| [TOOL-aKeyedAnnotation-2 — the shipped-evidence oracle reads one grammar and stops certifying itself](spec/2026-09-05-spec-TOOL-aKeyedAnnotation-2.md) | 2 | 2 | CLOSED | rev-7 | 2026-09-05 |
| [TOOL-aKeyedAnnotation-3 — a report-only signal for a source-cited id that resolves to no record](spec/2026-09-05-spec-TOOL-aKeyedAnnotation-3.md) | 3 | 2 | OPEN | rev-3 | 2026-09-05 |
| [TOOL-aKeyedAnnotation-4 — the dossier `decisions` field becomes live and shrink-only](spec/2026-09-05-spec-TOOL-aKeyedAnnotation-4.md) | 4 | 2 | OPEN | rev-5 | 2026-09-05 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aKeyedAnnotation-1` | no |
| 2 | `TOOL-aKeyedAnnotation-2` | no |
| 3 | `TOOL-aKeyedAnnotation-3` | no |
| 4 | `TOOL-aKeyedAnnotation-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

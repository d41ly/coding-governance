# TOOL-dTracedLattice-5 — a dark layer is derived from the corpus instead of asserted in prose

**Status:** SPECCED · rev-1 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 |

<!-- /gen:spec-records -->

## 1. Goal

`RECALL_DARK_LAYERS` is an authored conf string with exactly one consumer, which splits it and prints
a banner. Nothing derives it from the languages actually present and nothing reds when a layer appears
undeclared. A repo that adds a language and forgets the declaration gets a confident answer from a
probe that never read that layer — the failure `AGENTS.md` §7 names, in the mechanism this repo uses
to claim it is not making that failure.

## 2. Scope (IN)

- **S1** Derive the language layers PRESENT in the corpus, from the same file walk the index already
  performs, rather than trusting a declaration.
- **S2** Compare derived-present against declared-dark and against the extractors actually
  registered, and refuse when a present layer is neither covered nor declared dark.
- **S3** The refusal names the layer, the file count, and the two ways to clear it — register an
  extractor, or declare it dark — so the remedy is in the message.
- **S4** `reuse_lookup`'s banner reports the DERIVED set, so the notice a session reads is the
  measured one.

## 3. Non-goals (OUT)

- No new extractors. This unit makes an uncovered layer visible; covering it is separate work per
  language.
- No change to `map_extractors.py`'s interface or to what counts as a symbol.
- Not the coverage reporting inside `fan_in` — `TOOL-dTracedLattice-1` S3 owns that, and the two must
  not both report the same fact in different words.

## 4. Design

### Data model

The derived set is `{extension -> file count}` over the same tracked walk the index uses, mapped to
layer names by the extension table the extractors already imply. Declared-dark stays a conf value; it
becomes an ACKNOWLEDGEMENT of a derived fact rather than the source of the fact.

### Alternatives rejected

Keeping the declaration authoritative and adding a gate leg that greps for new extensions. That is a
second population derived by a second method, which is this repo's `two-answers-to-one-question`
class, and it puts the check somewhere other than where the answer is produced.

### Rollout

S1 and S2 first, refusing. S4 after, because changing the banner without changing the source of the
set would print a derived number beside an authored one.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the extension histogram falls out of a walk already performed; no second scan.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a corpus with one layer and no declaration is the common adopter
  case and must pass silently, not refuse.
- observability — S4.
- risks — S2 reds an adopter who adds a language, which is the intent; the message must make clearing
  it a one-line conf edit.
- testing + left-shift gates — a fixture corpus carrying an undeclared layer, observed RED first, and
  a second fixture where the same layer is declared dark and passes.
- migration / rollback — this tree declares `bash` dark today and would continue to; no data moves.
- user docs — `.codebase-map.conf.example` explains that the key acknowledges rather than defines.

## 6. Acceptance criteria

- **AC1** — When a fixture corpus contains a layer with no registered extractor and no
  `RECALL_DARK_LAYERS` entry, the run REFUSES naming that layer and its file count, and this arm is
  observed RED before the fix lands.
- **AC2** — When the same layer is added to `RECALL_DARK_LAYERS`, the run passes and the banner names
  it as dark.
- **AC3** — When a layer named in `RECALL_DARK_LAYERS` is absent from the corpus entirely, the run
  reports the stale declaration rather than silently honouring it.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py` runs on this tree, its dark-layer notice
  is derived from the corpus walk and names `bash` because bash files are present and uncovered, not
  because `.codebase-map.conf` says so.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` ·
`harness arms (fail branches armed or pinned)`.

## 8. Open questions

- **Q1 — what is a layer?** Extension, or language? `.sh` and `.bash` are one language; `.js`, `.mjs`
  and `.cjs` are one layer with one extractor. Mapping many extensions to one name needs a table, and
  a table is a declaration of the kind this unit exists to reduce. RESOLVED (agent, 2026-09-05,
  delegated): the layer name is whatever the extractor registry already keys on, so the table is the
  registry and no second one is introduced; an extension no registry entry claims is reported by
  extension, which is honest and needs no table at all.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round.

## 10. Reuse audit

The seam this unit extends is `map_lib.build_reference_index`'s existing extension filter, which
already computes the set of suffixes present from the symbol file list and is the natural place for a
derived layer histogram. Cited from `python tools/codebase-map/reuse_lookup.py "declare which language
layers a scan could not read"`, which returns no seam above the threshold for the declaration itself —
the evidence being that `RECALL_DARK_LAYERS` has exactly one consumer in the tree, at
`tools/codebase-map/reuse_lookup.py:172`, verified against source at writing time. Extending the
existing filter is therefore reuse; adding a parallel scan would not be.

Recall terms used: recall dark layers declaration extractor coverage liveness probe corpus extension
bash uncovered banner reuse_lookup

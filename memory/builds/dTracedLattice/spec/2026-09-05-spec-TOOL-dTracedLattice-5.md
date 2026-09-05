# TOOL-dTracedLattice-5 — a dark layer is derived from the corpus instead of asserted in prose

**Status:** SPECCED · rev-2 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 |

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
- **S4** Supply the derived set to `reuse_lookup`'s banner. `TOOL-dTracedLattice-1` AC3 owns the
  banner rewrite; this unit provides the value it prints. Rev-1 had both units rewriting the same
  output, which is why this unit is sequenced after unit 1.

## 3. Non-goals (OUT)

- No new extractors. This unit makes an uncovered layer visible; covering it is separate work per
  language.
- No change to `map_extractors.py`'s interface or to what counts as a symbol.
- Not the coverage reporting inside `fan_in` — `TOOL-dTracedLattice-1` S3 owns that, and the two must
  not both report the same fact in different words.

## 4. Design

### Data model

**The vocabulary is EXTENSION, and that choice has a cost this spec must not hide.** Three
vocabularies are in play and they do not reconcile: `SYMBOL_EXTRACTORS` keys on `kit-py` and `kit-js`
in the PROJECT-owned `map_extractors.py`, so each adopter authors its own; `symbols.json` carries no
layer tag at all, so nothing downstream can recover a registry key from the artifact; and
`.codebase-map.conf:27` declares `RECALL_DARK_LAYERS="bash"`, a language name
matching neither, while the kit's own fixture at `selftest.py:957` spells a third dialect, `web-ts`.

Extension is the only vocabulary BOTH sides can produce, because the derived set comes from a file
walk and a registry key exists only inside a project's own Python. The consequence, stated rather than
discovered later: `RECALL_DARK_LAYERS` values are re-declared as extensions, this repo's `bash`
becomes `.sh`, and every adopter who has written a value needs a named migration. §8 Q1 raises that as
the owner fork it is.

The derived set is therefore `{extension -> file count}` over the same tracked walk the index uses.
Declared-dark stays a conf value and becomes an ACKNOWLEDGEMENT of a derived fact rather than its
source.

### Alternatives rejected

Keeping the declaration authoritative and adding a gate leg that greps for new extensions. That is a
second population derived by a second method, which is this repo's `two-answers-to-one-question`
class, and it puts the check somewhere other than where the answer is produced.

**The lexicon kit already ships this design and rev-1 did not cite it.** `AGENTS.md` §12 requires a
declared COVERAGE MODE per language — parser, probe, or explicitly dark — with an undeclared one a
named refusal, and `tools/lexicon/` implements exactly that. This unit deliberately keeps a TWO-state
model rather than adopting the three-mode vocabulary, because codebase-map has no probe tier to
declare: an extractor either exists for a layer or it does not. That is a narrowing of a landed
sibling's design, taken knowingly, and not an independent invention.

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
- migration / rollback — data DOES move under either choice, which rev-1 denied. This tree's
  `RECALL_DARK_LAYERS` value is not valid in the chosen extension vocabulary, so gov's conf changes to
  `.sh` and adopters need the named migration Q1 owns.
- user docs — `.codebase-map.conf.example` explains that the key acknowledges rather than defines.

## 6. Acceptance criteria

- **AC1** — When a fixture corpus contains a layer with no registered extractor and no
  `RECALL_DARK_LAYERS` entry, the run REFUSES naming that layer and its file count, and this arm is
  observed RED before the fix lands.
- **AC2** — When that layer's EXTENSION is added to `RECALL_DARK_LAYERS`, the run passes and the
  banner names it as dark.
- **AC3** — When a layer named in `RECALL_DARK_LAYERS` is absent from the corpus entirely, the run
  reports the stale declaration rather than silently honouring it.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py` runs on this tree AFTER the Q1 migration,
  its dark-layer notice is derived from the corpus walk and names `.sh` because those files are
  present and uncovered, not because `.codebase-map.conf` says so.
- **AC5** — When an arm asserts that every `RECALL_DARK_LAYERS` token is either a registered extractor
  key or an extension present in the corpus, it reds on this tree TODAY against the shipped value, and
  that red is observed before the migration lands.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` ·
`harness arms (fail branches armed or pinned)`.

## 8. Open questions

- **Q1 — re-declaring `RECALL_DARK_LAYERS` as extensions.** §4 picks extension as the only vocabulary
  both sides can produce. That re-declares what the key's VALUES are for every adopter who has already
  written one: this repo's `bash` becomes `.sh`, and the kit's own fixture `web-ts` becomes a set of
  extensions. Changing a kit's shipped INPUT contract is veto 2 in `memory/guides/BUILD-METHOD.md` M3,
  so it is an owner turn and this run does not take it. Options: re-declare as extensions and ship a
  migration; keep language names and add the extension-to-language table §4 argues against; or accept
  both spellings for a deprecation window. Recommendation: re-declare, with AC5's arm reddening first
  so the decision is forced before the unit lands rather than after. **NOT RESOLVED.**

  Rev-1 marked this RESOLVED and picked the extractor-registry vocabulary. That was wrong twice: the
  registry keys live in a project-owned file so they are not a shared vocabulary at all, and the
  resolution silently contradicted AC2, AC4 and the §5 migration row.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round.
- rev-2 · 2026-09-05 · folded the round-1 spec audit: B3 (§4 picks the extension vocabulary and states
  its cost, Q1 is un-resolved as the owner turn it always was, AC2 and AC4 re-worded, AC5 added to red
  on the shipped value, and §5's false migration row corrected), H8 (§4 and §10 cite the lexicon kit's
  landed coverage-mode design and record this as a knowing narrowing), B1 (S4 feeds the banner unit 1
  owns rather than rewriting it).

## 10. Reuse audit

The seam this unit extends is `map_lib.build_reference_index`'s existing extension filter, which
already computes the set of suffixes present from the symbol file list and is the natural place for a
derived layer histogram. Cited from `python tools/codebase-map/reuse_lookup.py "declare which language
layers a scan could not read"`, which returns no seam above the threshold for the declaration itself —
the evidence being that `RECALL_DARK_LAYERS` has exactly one consumer in the tree, at
`tools/codebase-map/reuse_lookup.py:172`, verified against source at writing time. Extending the
existing filter is therefore reuse; adding a parallel scan would not be.

Prior art not cited at rev-1: `tools/lexicon/` implements `AGENTS.md` §12's declared-coverage-mode
rule — parser, probe, or explicitly dark, with an undeclared mode a named refusal — and this unit
narrows that three-mode design to two states for the reason §4 gives.

Recall terms used: recall dark layers declaration extractor coverage liveness probe corpus extension
bash uncovered banner reuse_lookup

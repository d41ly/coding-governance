# TOOL-dClosedLexicon-2 — wiring the verb table into the map ratchet and the drift signal set

**Status:** SPECCED · rev-2 · 2026-08-16 · node d · Tier-2 · base a9bd87d5 · streams tooling

## 1. Goal

`TOOL-dClosedLexicon-1` ships a closed verb table that is closed only by convention: nothing stops it
growing a verb per exception until it is a synonym list, and nothing notices when a verb outlives the
code that justified it. This unit wires the table into the two kits that already answer those two
questions — `codebase-map` for the growth direction and `drift-audit` for the outliving direction —
and writes down the teardown path that adding an inventory creates.

Split from unit 1 at its rev-3 because §1 does not let one unit carry a cross-stream contract change.
This unit depends on unit 1 landing first and is inert without it.

## 2. Scope (IN)

- **S1** — `lexicon-verbs` declared as an inventory in this repo's `map_extractors.py:EXTRACTORS`,
  reading the `VERBS` keys from `.lexicon.conf`. The declaration is project-owned code and is
  therefore per-adopter; it is never added to `map_extractors.template.py`.
- **S2** — a dossier under `memory/map/features/` claiming the `lexicon-verbs` keys, ratified over
  the `baseline.toml` route at rev-2 (§8 F2). Every verb is claimed in prose that says why the table
  carries it, and the both-directions ratchet applies from the first landing.
- **S3** — two `drift-audit` signals in `tools/drift-audit/drift_signals.py`, each seeded at a
  MEASURED pin and each carrying the clean-and-violating fixture pair `selftest.py` requires: a verb
  DECLARED in `VERBS` but used by no definition in the corpus, and a `ratified` stamp older than the
  last change to the declared language surface.
- **S4** — teardown detection: `bash tools/lexicon/adopt-lexicon.sh --check` names an orphaned
  `lexicon-verbs` extractor when `.lexicon.conf` is absent, and `tools/lexicon/README.md` documents
  the uninstall order. Removing an optional kit must not red a different optional kit's gate.
- **S5** — the `EXTRACTORS`-versus-`SYMBOL_EXTRACTORS` choice recorded where an implementer reads it:
  the verb table goes in `EXTRACTORS`, because `SYMBOL_EXTRACTORS` is declared recall-only and
  `map_extractors.py:129` states that a new symbol there never fails CI.

## 3. Non-goals (OUT)

- Anything in `tools/lexicon/` itself. Unit 1 owns the kit.
- A pin-direction guard. Cut at unit 1's rev-3 and filed as a shared follow-up; this unit inherits
  that decision rather than reopening it.
- Inverting the dependency so `codebase-map` CONSUMES a lexicon-owned definition census. That would
  also close `TOOL-aNumeralWarden-4` and it is a bigger change than this unit; see §8 F1.
- A waiver-staleness drift signal. Unit 1's S8 already reds a stale waiver inside the gate, and a
  second asker of the same question is the duplicate-fact class §5 bans.

## 4. Design

### What each direction actually buys

The map ratchet is two rules and they are not equally strong here.

The ADDITION direction — a new key reds until a dossier claims it — is weaker for a hand-authored
vocabulary than for a code inventory. For code, claiming a key means describing a real moving part
discovered from source. For a verb, the claim is a one-line dossier edit by the same author who added
the verb in the same commit. What it buys is VISIBILITY in the diff, not cost.

The DELETION direction — a claim naming a key that no longer exists reds — is the load-bearing half,
and it is the one no other mechanism here provides. A verb removed from `VERBS` while a dossier still
describes it is exactly the map-rots-into-fiction case the ratchet was built for.

Unit 1's §4 called the ratchet "the only pressure a closed table has against growth". Review R1 found
that oversold in one direction and silent in the other. This spec is the correction.

### Data model

No new conf keys. S1 reads `VERBS` from `.lexicon.conf`; S3's pins live beside the existing ones in
`drift_signals.py:PINS`.

### Why the drift signals are not gate predicates

Unit 1's S6 keeps the empty-population check INSIDE `lexicon.py`, because a gate that cannot read its
corpus must not pass green on the run where that is true. The two signals here are different in kind:
a declared-but-unused verb is not a violation of anything, and a stale `ratified` stamp does not make
this run's verdict wrong. Both are record-versus-reality questions, which is `drift-audit`'s subject,
and both are the sort of thing that is true for weeks before anyone should act on it.

### The day-one seed will not be zero

`--scaffold` derives the table by frequency and a human then curates it, and curation adds
aspirational verbs the corpus does not yet use. The declared-but-unused signal therefore measures
non-zero on the first run, and its pin is seeded there. That is the same shape as
`non_terminal_specs_cited_by_product_source: 2`, whose comment records a known residual rather than
proven rot. An implementer reading a non-zero first measurement is reading a correct measurement, not
a failed build, and the pin comment says so.

### Files touched (estimate)

`tools/codebase-map/map_extractors.py`, `tools/drift-audit/drift_signals.py`,
`tools/drift-audit/selftest.py`, `tools/lexicon/adopt-lexicon.sh`, `tools/lexicon/README.md`, one
dossier under `memory/map/features/`, and `memory/map/generated/` as a re-render.

### Alternatives rejected

- **Declaring the verbs under `SYMBOL_EXTRACTORS`.** That tier feeds the recall corpus only and never
  the ratchet, so the closure question it was added to answer would go unanswered.
- **A third drift signal for stale waivers.** Duplicates unit 1's S8 inside the gate.
- **Shipping the extractor in `map_extractors.template.py`.** It would break every adopter who takes
  `codebase-map` without the lexicon, which is most of them.

## 5. Production-readiness checklist

- security — N/A. Reads two conf files and tracked source.
- perf / scale — one extra inventory over a table of tens of rows; negligible against the existing map.
- a11y — N/A — no user interface.
- i18n — N/A — operates on the declared table, not on prose.
- error / empty / loading states — an absent `.lexicon.conf` is S4's teardown case and must be a named
  refusal, never a raise from `all_inventories()`.
- observability — a red names the verb and which direction of the ratchet fired.
- risks — the main one is coupling two optional kits, addressed by S4. The secondary one is a
  ratchet that reads as stronger than it is, addressed by writing down which direction carries weight.
- testing + left-shift gates — S3's fixture pairs, plus the existing map coverage test.
- migration / rollback — reverting is deleting the extractor, the dossier claim and the two signals;
  no data shape changes.
- user docs — the uninstall order in `tools/lexicon/README.md`, per S4.

## 6. Acceptance criteria

- **AC1** — When a verb is added to `VERBS` with no dossier claiming it,
  `python tools/codebase-map/test_codebase_map.py` reds.
- **AC2** — When a dossier claims a verb that has since been deleted from `VERBS`, the same test reds
  from the other direction.
- **AC3** — When a verb is declared but no definition in the corpus uses it above the seeded pin,
  `python tools/drift-audit/drift_report.py --check` reds.
- **AC4** — When the `ratified` stamp predates the last change to the declared language surface, the
  same `--check` reds.
- **AC5** — When each new signal is run against its clean fixture it is silent, and against its
  minimal violating fixture it fires, both asserted by `python tools/drift-audit/selftest.py`.
- **AC6** — When `.lexicon.conf` is deleted while the `lexicon-verbs` extractor remains,
  `bash tools/lexicon/adopt-lexicon.sh --check` names the orphaned extractor and
  `python tools/codebase-map/test_codebase_map.py` does not raise an unhandled `MapError`.
- **AC7** — When `bash tools/run-gates.sh` runs on the landing commit, the map coverage leg and both
  drift legs appear in the green line by name.

## 7. Gates

Existing legs that must stay green: `python tools/codebase-map/test_codebase_map.py`,
`python tools/codebase-map/selftest.py`, `python tools/drift-audit/selftest.py`,
`python tools/drift-audit/drift_report.py --check`, and `python tools/lexicon/selftest.py` from unit 1.

This unit adds no new leg. It adds signals and an inventory to legs that already ride the bar, which
is the point — an integration that needs its own gate has not integrated.

## 8. Open questions

- **F1 — should `codebase-map` consume a lexicon-owned definition census?** `map_lib.python_symbols`
  indexes only public symbols and `TOOL-aNumeralWarden-4` records that the JavaScript side indexes no
  non-exported function, so the map's recall corpus has a known hole that a lexicon census would
  fill. Inverting the dependency is the larger design and would make the lexicon a prerequisite of a
  fuller map. RECOMMENDATION: leave inverted until the lexicon has a measured corpus in at least one
  adopter, then reopen with numbers rather than with an argument.
- **F2 — dossier or baseline for S2?** A dossier makes each verb claimable in prose and costs a real
  authoring pass; `baseline.toml` is shrink-only and costs nothing now but records nothing either.
  RESOLVED (owner, 2026-08-16): dossier. The whole value of the addition direction is that a claim
  exists to be read, and a baseline entry is exactly the silent growth this unit is here to prevent.
  The cost lands on whoever curates the table, which is the correct place for it.

## 9. Revision log

- rev-1 · 2026-08-16 · split from `TOOL-dClosedLexicon-1` rev-3 per review-dClosedLexicon-1 R7,
  carrying that spec's S14 and the record-versus-reality half of its S6, plus R1's correction and
  R2's teardown gap.
- rev-2 · 2026-08-16 · owner ratified F2 to the dossier route; S2 drops the baseline alternative.
  F1 stays open by design — it cannot be decided without a measured corpus, so this spec stays
  SPECCED while `TOOL-dClosedLexicon-1` moves to DEFERRED.

## 10. Reuse audit

This unit is reuse by construction — it adds no mechanism, only declarations inside two existing
kits. From `codebase-map`, the `EXTRACTORS` ratchet and the dossier/baseline pair. From
`drift-audit`, the `{record, source, probe}` signal shape with measured `PINS` and the
clean-plus-violating fixture contract its `selftest.py` enforces. `python tools/codebase-map/reuse_lookup.py naming vocabulary gate`
ranked `registry.toml` first, and its declaration-not-listing doctrine is the reason S1 reads the
table from conf rather than enumerating a directory. No new seam is created here, which is the
strongest evidence available that the split was along the right line.

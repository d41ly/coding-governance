# TOOL-dClosedLexicon-2 — wiring the verb table into the map ratchet and the drift signal set

**Status:** BLOCKED · rev-3 · 2026-08-16 · node d · Tier-2 · base a9bd87d5 · streams tooling

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
  reading the `VERBS` keys from `.lexicon.conf` **through unit 1's single reader
  `tools/lexicon/lexicon_conf.py`** — reached by an explicit `sys.path` insert against the install
  prefix, never by a second parser. `.lexicon.conf`'s block grammar is not the sibling `KEY=VALUE`
  one, so `map_lib.load_conf()` cannot read it and a hand-rolled parser here would be a second answer
  to a question unit 1 already answers. The declaration is project-owned code and is therefore
  per-adopter; it is never added to `map_extractors.template.py`.
- **S2** — a dossier under `memory/map/features/` claiming the `lexicon-verbs` keys, ratified over
  the `baseline.toml` route at rev-2 (§8 F2). Every verb is claimed in prose that says why the table
  carries it, and the both-directions ratchet applies from the first landing.
- **S3** — two `drift-audit` questions, each carrying the clean-and-violating fixture pair
  `selftest.py` requires: a verb DECLARED in `VERBS` but used by no definition in the corpus, and a
  `ratified` stamp older than the last change to the declared language surface. **The MECHANISM is
  PARKED at F3 and this scope item cannot be built until it is decided.** rev-2 said "two signals in
  `tools/drift-audit/drift_signals.py`, each seeded at a MEASURED pin"; that file is the project-owned
  DATA layer and cannot declare a signal — `SIGNALS` is a hardcoded engine list at
  `drift_report.py:488`, the project surface is validated for exactly four attrs at `:117`, and `PINS`
  is keyed by the name the ENGINE emits, so a key naming a project-invented signal is silently inert.
  Built literally it produces two probe functions nothing calls: a green gate over a dead instrument,
  which is the class this kit exists to prevent.
- **S4** — teardown as an ORDERED PROCEDURE, not a goal. "Removing an optional kit must not red a
  different optional kit's gate" is unachievable as a property once S2 chooses the dossier route: all
  three degradation routes red the map leg — an extractor returning `[]` makes every dossier claim
  stale, removing the `EXTRACTORS` entry makes the dossier claim an id outside `inventory_ids()` and
  `map_lib` raises, and the generated re-render moves either way. So the uninstall ORDER is the
  mechanism: remove the dossier's `lexicon-verbs` claims block, then the `EXTRACTORS` entry, then
  re-render `memory/map/generated/`, then delete `.lexicon.conf`. `tools/lexicon/README.md` carries
  that order verbatim, and `bash tools/lexicon/adopt-lexicon.sh --check` names an orphaned
  `lexicon-verbs` extractor as the MID-teardown safety arm.
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

F3's engine route would add `tools/drift-audit/drift_report.py`, `tools/drift-audit/README.md` and
the whole `drift-audit` kit-version bump — the `KIT_DRIFT_AUDIT_VERSION` constant, every
`gov:kit drift-audit@` marker, and both `tools/workflows/drift-audit-{code,state}.js` `meta.version`
fields. That the two routes have different Files-touched sets is itself the evidence that F3 is a
scope fork rather than an implementation detail.

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
  `python tools/drift-audit/drift_report.py --check` reds. *(Unobservable until F3 is decided: on the
  project-layer route both questions share one pin and "above the seeded pin" names nothing per-signal.
  This AC is written against the engine route and must be rewritten if F3 goes the other way.)*
- **AC4** — When the `ratified` stamp predates the last change to the declared language surface, the
  same `--check` reds. *(Same F3 dependency as AC3.)*
- **AC5** — When each new signal is run against its clean fixture it is silent, and against its
  minimal violating fixture it fires, both asserted by `python tools/drift-audit/selftest.py`.
- **AC6** — When the documented uninstall order is followed to completion,
  `python tools/codebase-map/test_codebase_map.py` exits 0 and
  `bash tools/lexicon/adopt-lexicon.sh --check` is silent. This is the property S4 promises; rev-2's
  wording observed only that the map test "does not raise an unhandled `MapError`", which the
  degrade-to-empty route satisfies while the leg is red on a plain assert.
- **AC6b** — When `.lexicon.conf` is deleted while the `lexicon-verbs` extractor remains — the
  MID-teardown state — `bash tools/lexicon/adopt-lexicon.sh --check` names the orphaned extractor and
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

*The `RESOLVED` mark sits on each bullet's FIRST line deliberately. The hygiene gate counts an item
per `- `/`### ` line and increments `resolved` only when that SAME line matches `RESOLVED`;
continuation lines are never scanned. rev-2 carried F2's resolution three lines down, which scored
items=2 resolved=0 and would have made this spec unable to go terminal at wrap-up with no owner turn
available to fix it.*

- **F1 — should `codebase-map` consume a lexicon-owned definition census?** DEFERRED (agent,
  2026-08-16, delegated): leave inverted, reopen with numbers. `map_lib.python_symbols` indexes only
  public symbols and `TOOL-aNumeralWarden-4` records that the JavaScript side indexes no non-exported
  function, so the map's recall corpus has a known hole a lexicon census would fill. It cannot be
  decided without a measured corpus in at least one adopter. At close this is marked in place as
  `RESOLVED (agent, <date>, delegated)` with the deferral tracked as a `memory/backlog/TOOL.md` row
  filed in the same commit; the mark lands on this line.
- **F2 — dossier or baseline for S2?** RESOLVED (owner, 2026-08-16): dossier. A dossier makes each
  verb claimable in prose and costs a real authoring pass; `baseline.toml` is shrink-only and costs
  nothing now but records nothing either. The whole value of the addition direction is that a claim
  exists to be read, and a baseline entry is exactly the silent growth this unit is here to prevent.
  The cost lands on whoever curates the table, which is the correct place for it.
- **F3 — how are S3's two questions actually declared?** PARKED (agent, 2026-08-16): **this is a
  SCOPE decision and the standing mandate does not delegate scope.** rev-2's answer was mechanically
  impossible (see S3). Two options survive and they differ in what gets built. **(a) The engine
  route:** append two signal functions to the SHIPPED `drift_report.py:SIGNALS`, each with its own
  `PINS` key and each reporting `gateable: False` with a "not asked" reason when `.lexicon.conf` is
  absent, on the `signal_closed_specs_untraceable` model. It works, and the absent-conf guard means no
  adopter inherits a dead gateable signal — but it makes a generic shipped engine NAME an optional
  kit, which is the coupling this spec's own §4 Alternatives rejects for `map_extractors.template.py`,
  and it changes what every `drift-audit` adopter receives. **(b) The project-layer route:** declare
  both as `HANDKEPT` rows. No engine edit, but every row folds into the single
  `handkept_inventories_disagreeing_with_source` signal with ONE shared pin — currently drained to 0
  — so §4's own prediction that the day-one seed is non-zero forces that pin up, blinding the
  charter-completeness ratchet that rides the same signal and which unit 1 depends on staying at 0.
  **Refused because** (a) changes a shipped kit's public surface and reverses a doctrine this spec
  states, and (b) degrades an existing gate to buy a new one. Neither is a resolver call, and there is
  no third option that is merely the least bad. The owner decides; this unit does not build until then.

## 9. Revision log

- rev-3 · 2026-08-16 · folded review-dClosedLexicon-2, the M4 audit at rev-2. S3's mechanism is
  PARKED as F3 and the status moves SPECCED to BLOCKED (R2): `drift_signals.py` is the project-owned
  data layer and cannot declare a signal, and the two routes that can differ in what gets built, so
  the choice is scope rather than a resolver call. S4 becomes an ordered uninstall PROCEDURE and AC6
  is rewritten to observe the property S4 promises, with the mid-teardown arm split out as AC6b (R7).
  S1 names unit 1's `lexicon_conf.py` as the single reader instead of implying a second parser (R8).
  Both §8 marks move onto their bullets' first lines (R9) — the hygiene gate never scans a
  continuation line, so rev-2 could not have gone terminal.
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

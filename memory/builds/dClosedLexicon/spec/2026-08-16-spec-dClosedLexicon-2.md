# TOOL-dClosedLexicon-2 — wiring the verb table into the map ratchet and the drift signal set

**Status:** CLOSED · rev-5 · 2026-08-16 · node d · Tier-2 · base a9bd87d5 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-PLAY-dClosedLexicon-1-7.md](../reviews/2026-08-16-review-PLAY-dClosedLexicon-1-7.md) | diff-review | PLAY-dClosedLexicon-1 TOOL-dClosedLexicon-1 |
| [2026-08-16-review-TOOL-dClosedLexicon-1-2.md](../reviews/2026-08-16-review-TOOL-dClosedLexicon-1-2.md) | spec-audit | TOOL-dClosedLexicon-1 |

<!-- /gen:spec-records -->

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
- **S3** — two `drift-audit` signals, appended to the shipped `drift_report.py:SIGNALS` per F3's
  owner-resolved ENGINE route, each with its own `PINS` key in `drift_signals.py` and each carrying
  the clean-and-violating fixture pair `selftest.py` requires: a verb DECLARED in `VERBS` but used by
  no definition in the corpus, and a `ratified` stamp older than the last change to the declared
  language surface. With `.lexicon.conf` ABSENT both return `gateable: False` with a "not asked"
  reason, so an adopter without the lexicon inherits nothing live.
  *(rev-2 said "two signals in `drift_signals.py`, each seeded at a MEASURED pin". That file is the
  project-owned DATA layer and cannot declare a signal — `SIGNALS` is a hardcoded engine list, the
  project surface is validated for exactly four attrs, and `PINS` is keyed by the name the ENGINE
  emits, so a key naming a project-invented signal is silently inert. Built literally it produced two
  probe functions nothing calls. The correction is recorded rather than deleted because the wrong
  version was specific enough to look buildable.)*
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

F3's ratified engine route ADDS `tools/drift-audit/drift_report.py`, `tools/drift-audit/README.md`
and the whole `drift-audit` kit-version bump — the `KIT_DRIFT_AUDIT_VERSION` constant, every
`gov:kit drift-audit@` marker, and both `tools/workflows/drift-audit-{code,state}.js` `meta.version`
fields. That the two routes had different Files-touched sets is itself why F3 was a scope fork rather
than an implementation detail.

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

- **F1 — should `codebase-map` consume a lexicon-owned definition census?** RESOLVED (agent,
  2026-08-16, delegated): leave the dependency as it is, tracked as `TOOL-dClosedLexicon-12`. The
  condition rev-2 set — "reopen with numbers once the lexicon has a measured corpus" — is now
  HALF met: this repo has one (485 tracked files, 22 verbs, 417 graded definitions), but one adopter
  is not two, and inverting the dependency would make the lexicon a PREREQUISITE of a fuller map,
  which is a scope call this unit's §3 already puts out. What the measurement adds is that the census
  is now cheap to produce, so the follow-up is smaller than when it was parked. `map_lib.python_symbols`
  indexes only public symbols and `TOOL-aNumeralWarden-4` records the JavaScript side indexing no
  non-exported function; a census would close both.
- **F2 — dossier or baseline for S2?** RESOLVED (owner, 2026-08-16): dossier. A dossier makes each
  verb claimable in prose and costs a real authoring pass; `baseline.toml` is shrink-only and costs
  nothing now but records nothing either. The whole value of the addition direction is that a claim
  exists to be read, and a baseline entry is exactly the silent growth this unit is here to prevent.
  The cost lands on whoever curates the table, which is the correct place for it.
- **F3 — how are S3's two questions actually declared?** RESOLVED (owner, 2026-08-16): the ENGINE
  route. Two signal functions are appended to the shipped `drift_report.py:SIGNALS`, each with its own
  `PINS` key in `drift_signals.py`, and each returns `gateable: False` with a "not asked" reason when
  `.lexicon.conf` is absent — the shape `signal_closed_specs_untraceable` already uses for an unset
  `TRACE_CUTOFF`, and for the same reason: NOT ASKED is neither clean nor dead, and doing it in the
  ENGINE rather than through the project layer's `DECLARED_EMPTY` keeps the distinction reaching an
  adopter who has edited nothing. The project-layer alternative was refused because both questions
  would fold into `handkept_inventories_disagreeing_with_source`'s single shared pin, currently
  drained to 0, and this spec's own §4 predicts a non-zero day-one seed — buying a new signal by
  blinding the charter-completeness ratchet that rides the same signal.

  What the route COSTS, recorded because §3 rejects the same coupling for `map_extractors.template.py`:
  a generic shipped engine now names an optional kit. The absent-conf guard is what makes that
  acceptable here and not there — an adopter without the lexicon inherits two signals that report
  "not asked" and gate nothing, whereas a template extractor would RAISE on `all_inventories()`. The
  asymmetry is the guard, not the intent.

## 9. Revision log

- rev-5 · 2026-08-16 · BUILT and CLOSED. All five scope items land: the `lexicon-verbs` inventory in
  `EXTRACTORS` reading through unit 1's single reader; the dossier claiming all 22 verbs (and every
  OTHER dossier gaining an empty `lexicon-verbs` list, because a new inventory id must appear in every
  `[claims]` block); two engine signals with measured pins; the uninstall ORDER in the kit README with
  its mid-teardown orphan arm; and the `EXTRACTORS`-vs-`SYMBOL_EXTRACTORS` reasoning recorded at the
  declaration. drift-audit 1.3 -> 1.4, lexicon 1.0 -> 1.1. The unused-verb pin seeds at 3 — `measure`,
  `print` and `set`, aspirational verbs curation added — which is the non-zero day-one seed §4
  predicted, and its comment says so in place so a reader does not mistake it for debt.

- rev-4 · 2026-08-16 · owner ratified F3 to the ENGINE route, and the unit BUILDS. S3 becomes two
  signal functions on the shipped `drift_report.py:SIGNALS`, each with its own `PINS` key and each
  returning `gateable: False` with a "not asked" reason when `.lexicon.conf` is absent — the shape
  `signal_closed_specs_untraceable` already uses, so an adopter without the lexicon inherits nothing
  live. The project-layer route was refused because both questions would have folded into one shared
  pin that is drained to 0, buying a signal by blinding the charter ratchet unit 1 depends on. S3's
  rev-2 text is kept as a correction rather than deleted: it was specific enough to look buildable.

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

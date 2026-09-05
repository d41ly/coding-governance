# TOOL-aKeyedAnnotation-3 — a report-only signal for a source-cited id that resolves to no record

**Status:** OPEN · rev-1 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing today notices when source cites a unit id that no record defines: the memory-tree orphan
check's population is the memory tree by construction, so its honest zero says nothing about code.
Add the missing half as a report-only drift signal, keyed on whether the id's slug resolves in the
corpus — a discriminator measured on this tree to separate every fixture from every real finding with
no waiver list at all.

## 2. Scope (IN)

- **S1** A new signal in `tools/drift-audit/drift_report.py`, registered in the module's signal
  registry beside its siblings: for every id cited by tracked source outside the memory root, report
  the ones that no anchored record defines.
- **S2** The discriminator is slug-resolvability. An id whose slug anchors at least one record in the
  corpus is a finding; an id whose slug anchors none is a fixture and is filtered. Derived from the
  definitions map the memory-tree walk already builds — never from a directory listing, which goes
  stale the first time a build is archived.
- **S3** A liveness assertion the signal carries on every run: the count of known slugs and the count
  of scanned source files. A zero finding count is only meaningful beside a non-empty slug set and a
  non-empty file set; with either empty the signal reports itself dead rather than clean.
- **S4** Report-only, with its own tolerance pin, in the shape the kit already ships for signals that
  are true but not yet gateable. It gates nothing and adds no leg.
- **S5** The family enum is read from the memory-tree conf rather than spelled, so a foreign family
  cited in shipped adopter-facing text cannot make the signal permanently red in a tree that does not
  declare it.
- **S6** A self-test arm that plants a fabricated id under a slug that DOES resolve and asserts the
  signal moves, and a second arm that plants one under a slug that does not and asserts it does not.
  Both observed before the signal is registered.

## 3. Non-goals (OUT)

- **No widening of the memory-tree orphan check.** Its pin sits at its floor with an empty waiver;
  a source population would force either a pin raise the kit's own ratchet list treats as weakening,
  or a waiver registry on day one. The design pass records the guard blast radius as the second
  reason: the legs guarded on that kit are among the most expensive on the bar.
- **No gate.** The signal reports. Promoting it is a later decision with its own measurement.
- **No repair of what it finds.** Unit 1 repairs the citation it already knows about; anything else
  this signal surfaces becomes a backlog row.
- **No path-based test-file exclusion.** Measured on this tree: this repo puts selftest arms inside
  product modules, so a path predicate is wrong in whichever direction it is set. The slug
  discriminator is chosen precisely because it is not a path predicate.

## 4. Design

### The discriminator, and why it is not a glob

Measured at this base with the shipped id grammar over every tracked non-memory source file: sixty
cited ids resolve to no record. Filtered by slug-resolvability against the corpus's known slugs, two
survive and fifty-eight are dropped, and the two survivors are genuine — an id triple from one build
that was minted, cited from a comment and from a test, and never recorded. Zero waiver rows are
required. A path-based split cannot reach that, because the fixture ids live inside product modules.

The population it reports is therefore small and every member is actionable, which is what makes a
report-only signal drainable rather than decorative.

### Inventory

One signal function, one registry row, one pin row, two self-test arms. No new file, no new leg, no
new committed artifact — the answer is derived live on each run, which is the repo's stated
preference when the only consumer is same-language.

### Rollout

The signal ships at the measured value with the reading recorded beside the pin. Because its
population is expected to be small and the members actionable, the pin is a drain target from the
first commit rather than a permanent tolerance.

### Alternatives rejected

A committed inventory of source citations was rejected: nothing cross-language reads it, so it would
be an artifact to keep fresh where a live derivation cannot drift. A marker-scoped population was
rejected with the marker. Excluding by path was rejected on the measurement above.

## 5. Production-readiness checklist

- security — N/A: read-only over tracked files.
- perf / scale — one grammar pass over tracked source; the census script in this build's own folder
  runs the same walk in a few seconds, and the signal rides a report that already costs tens of
  seconds. Re-measure and record it in the commit rather than asserting it here.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 is exactly this: the empty case must announce itself.
- observability — the signal's own report line; plus the census script for the full breakdown.
- risks — a false zero from an empty population is the whole hazard, and S3 plus the two self-test
  arms are the controls. The second hazard is a foreign family making the signal permanently red in
  an adopter tree; S5 is that control.
- testing + left-shift gates — two arms in the kit self-test, both observed before landing. No leg.
- migration / rollback — additive; removing the signal restores the prior report exactly.
- user docs — one entry in the kit README's signal list, which already enumerates them.

## 6. Acceptance criteria

- **AC1** When `python tools/drift-audit/drift_report.py --check` is run after this unit, the new
  signal appears with a non-zero judgeable population and reports the two ids measured at this base,
  and no fixture id among them.
- **AC2** When a fabricated id is planted in a tracked source comment under a slug that anchors a
  record, the signal's count rises by one; when it is planted under a slug that anchors none, the
  count does not move. Both observed with `python tools/drift-audit/selftest.py` arms.
- **AC3** When `python tools/drift-audit/drift_report.py --check` is run against a scratch tree whose
  memory root is empty, the signal reports itself
  dead rather than reporting zero findings.
- **AC4** When the family enum in `.memory-tree.conf` is changed in a scratch tree, the signal's
  population changes accordingly — proving the enum is read and not spelled.
- **AC5** When `python tools/memory-tree/corpus_ids.py --report` is run after this unit, its orphan
  count is unchanged from this base — proving the memory-side check was not widened.
- **AC6** When `bash tools/run-gates/run-gates.sh` is run on this unit's commit it is green, and the
  `drift-audit records` leg's recorded seconds are compared against its declared ceiling.

## 7. Gates

Existing legs that must stay green: the full bar. Load-bearing here — `drift-audit records`, the
drift-audit kit self-test, and `memory hygiene` (which must not move, per AC5). Read
`tools/gate-legs.json` for the names. No new leg; a new signal inside an existing report is
deliberately cheaper than a leg, and the leg it rides is unguarded so it already runs on every bar.

## 8. Open questions

- **F1 — does the signal read tracked source, or the product globs unit 2 declares?** Product globs
  exclude some tracked source and include configuration. Options: (a) all tracked non-memory source,
  which is the census's population and the honest one for "does this citation resolve"; (b) the
  narrowed product population, which aligns with the shipped-evidence oracle. Recommendation: (a) —
  the question here is citation integrity, not shipped evidence, and a dangling id in a test file is
  as wrong as one in a module. Note that (a) is what surfaced the second finding at this base.
- **F2 — the pin's shape.** Its siblings use two forms, a tolerance and a shrink-only pin. Given the
  population is small and every member is actionable, shrink-only is the closer fit. Recommendation:
  shrink-only, seeded at the measured value, with the reading recorded beside it.
- **F3 — whether the two findings are repaired by this build.** They belong to another node's build
  whose records were never written, so repairing them means writing records for work this session did
  not do. Recommendation: file them as backlog rows against that build and let the signal carry them
  until its owner drains it; unit 1 repairs only the comment prose it touches.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` returned `inventory_ids` and `build_reference_index` as the ranked seams; both
belong to codebase-map, which the design pass rules out of scope, so neither fits. The seams this
unit actually extends were found by reading the kits: the signal registry and pin machinery in
`tools/drift-audit/drift_report.py`, and the definitions map plus id grammar already built by
`tools/memory-tree/corpus_ids.py`. The discriminator is derived from that existing map rather than
from a new one, and no new inventory is committed.

Recall terms used: orphan id waiver shrink-only pin drift signal liveness dead probe source citation
slug resolvability fixture population report-only.

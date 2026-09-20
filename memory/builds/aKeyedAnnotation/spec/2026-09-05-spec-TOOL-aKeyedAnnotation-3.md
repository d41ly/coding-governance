# TOOL-aKeyedAnnotation-3 — a report-only signal for a source-cited id that resolves to no record

**Status:** CLOSED · rev-4 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-3-acceptance.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-3-acceptance.md) | journal | — |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round2.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round3.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round3.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-4 |

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
- **S3** A liveness assertion the signal carries on every run. **CORRECTED at build time, because
  the obvious second half is vacuous.** The pair was to be the count of known slugs and the count of
  scanned source files; the file count can never reach zero in a tree with this kit installed, since
  the report is itself a tracked non-memory file. That was found by writing the arm to observe it RED
  and watching it refuse to go dead — the only way the vacuous-selector class ever surfaces. The
  half that CAN collapse is the CITED set: a grammar bound to the wrong families matches nothing
  while every file is still scanned, which is the confident zero this signal exists to refuse. So
  liveness keys on the slug set and the cited set, and the scanned-file count stays REPORTED as the
  denominator a reader needs while deciding nothing.
- **S4** Report-only, with its own SHRINK-ONLY pin, in the shape the kit already ships for signals
  that are true but not yet gateable. It gates nothing and adds no leg. The word matters and an
  earlier revision had it wrong: this item said "tolerance pin" while §8 F2 resolves the fork to
  shrink-only by name and treats the two as distinct shapes, and §4 Rollout independently calls the
  pin a drain target rather than a permanent tolerance. One spec, three sections, one answer now.
- **S7** SHRINK-ONLY NEEDS A MECHANISM. A report-only signal is `gateable: False`, so it can never
  enter the report's over-tolerance set or its dead set, and the check pass's only remaining lever is
  a ratchet row: the kit says so in prose beside its one existing report-only pin, whose gloss is
  that being ungateable is precisely what makes RAISING it land in the ratchet list. That list is an
  explicit opt-in — sibling pin keys carry no row — so a new pin is unratcheted by default and can be
  raised silently in the same commit that raises the population, which would make §4's "a drain
  target from the first commit" false. This unit lands the ratchet row naming the signals module and
  the new key, weakening upward, and §4's Inventory carries it. Sibling unit 4 spends a scope item
  and a criterion on this same rule in this same kit in this same build; both units now agree.
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
- **No gate.** The SIGNAL reports and stays ungateable; promoting it is a later decision with its
  own measurement. This bounds the signal's own verdict and NOT its pin: S7's ratchet row makes an
  unjustified RAISE of the pin red, which is a different question from whether crossing the pin
  blocks a merge, and sibling unit 4 draws the same line for the same kit. An earlier revision of
  this bullet said only "No gate", which read as forbidding the one mechanism that makes S4's
  shrink-only word true.
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

One signal function, one registry row, one pin row, one ratchet row, one dependency declaration and
five self-test arms — S6's two plus the three §6 wires, which is where they are enumerated rather
than counted again here. No new file, no new leg, no new committed artifact — the answer is derived live
on each run, which is the repo's stated preference when the only consumer is same-language.

**The definitions map crosses a KIT BOUNDARY and that is a declaration, not an implementation
detail.** The report module imports stdlib only and says so at its head, deliberately COPYING a
sibling kit's conf loader rather than importing it. Reaching straight into the memory-tree corpus
walker breaks that: its grammar accessor raises outright when the recall extractor is absent, and it
shells out to the hygiene script through a bash resolver that is itself a named failure path on a
node where no bash resolves. Drift-audit's descriptor requires memory-tree and declares no
memory-recall edge, and memory-tree puts memory-recall behind a conditional that is FALSE at apply
time because the pins ship blank — so the adopter configuration this kit's own requires permits is
exactly the one where that walk raises. The blast radius is the whole leg, not one signal: the report
evaluates every signal in one unguarded comprehension, so an exception there takes `drift-audit
records` down for that adopter instead of producing the dead-signal report S3 promises. §8 F4
resolves how the boundary is crossed; the kit's existing optional-kit idiom — a guarded import with
a not-asked verdict — is the shape, and the dependency edge is declared in
`tools/drift-audit/kit.toml`.

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
- **AC5b** S3 declares TWO liveness counts and AC3 exercises only one. In a scratch tree where the
  signal's SOURCE WALK resolves to no tracked file — the slug set left full — running
  `python tools/drift-audit/drift_report.py --check` reports the signal DEAD rather than zero
  findings. That is the unit's own stated hazard, a false zero from an empty population, and it is
  the half no other criterion reached. Observed RED first, and wired as a self-test arm beside S6's
  two, mirroring the criterion sibling unit 2 carries for the same class.
- **AC5c** When `python tools/drift-audit/drift_report.py --check` is run in a scratch tree holding
  drift-audit and memory-tree and NOTHING ELSE — no recall extractor, pins blank, which is the
  adopter configuration this kit's own descriptor permits — the signal reports itself DEAD and the
  `drift-audit records` leg still returns. It must not raise, and it must not take the other signals
  with it. Observed against the unguarded form first, which does.
- **AC5d** When the new pin is raised with no old-to-new marker beside it, `python
  tools/drift-audit/drift_report.py --check` REDS naming both values; with the marker present it
  does not. Observed both ways, which is what makes shrink-only a mechanism here rather than a word.
  **The observation needs a BASE that already carries the pin**, and that is a property of the
  ratchet rather than a quirk of the test: it compares the working value against the value at the
  base ref and skips a key the base does not have, so a pin is UNRATCHETED on the very branch that
  introduces it and binds from the next one onward. Stated because the obvious way to observe this
  criterion — raise the pin on this branch and expect a red — passes green and looks like a broken
  ratchet.
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
  RESOLVED (agent, 2026-09-05, delegated): (a). It is the more feature-rich option on the
  measurement already in §4 — it satisfies AC1's requirement to report the two ids measured
  at this base, which (b) would not reach — and it trips no veto, because it reads a
  population that is already tracked and widens no write surface.
- **F2 — the pin's shape.** Its siblings use two forms, a tolerance and a shrink-only pin. Given the
  population is small and every member is actionable, shrink-only is the closer fit. Recommendation:
  shrink-only, seeded at the measured value, with the reading recorded beside it.
  RESOLVED (agent, 2026-09-05, delegated): shrink-only. A tolerance pin permits the
  population to sit where it is forever, which fails §4's stated intent that the pin be a
  drain target from the first commit — a criterion the other option cannot satisfy.
- **F3 — whether the two findings are repaired by this build.** They belong to another node's build
  whose records were never written, so repairing them means writing records for work this session did
  not do. Recommendation: file them as backlog rows against that build and let the signal carry them
  until its owner drains it; unit 1 repairs only the comment prose it touches. RESOLVED
  (agent, 2026-09-05, delegated): backlog rows, and no records invented. Writing records for
  another node's unbuilt work would put fiction into the corpus that every consumer in this
  build then reads as truth, and unit 1's S4 already commits to the same disposition —
  resolving this fork the other way would leave two specs in disagreement.

- **F4 — how the definitions map crosses the kit boundary.** Drift-audit is copy-installed and must
  not hard-import a kit an adopter may not have; the memory-tree corpus walker raises when the recall
  extractor is absent. Options: (a) adopt sibling unit 2's F1 resolution by reference — import when
  importable, fall back to a local copy the kit self-test byte-compares against the original, and
  report the signal DEAD rather than raising when neither is available; (b) rebuild the definitions
  map inside drift-audit from the grammar unit 2's S1 already binds; (c) declare a hard dependency
  edge and let the leg fail for adopters without it. RESOLVED (agent, 2026-09-05, delegated): (a),
  BY REFERENCE and not by re-deciding. F1 of unit 2 settled this exact boundary question one unit
  earlier in this same build and this same kit, and answering it differently here would leave two
  units applying two rules to one boundary. (c) fails veto 1 outright — it breaks a leg the spec's
  own §7 requires green. (b) survives the vetoes but satisfies strictly fewer criteria: it duplicates
  a walk that already exists where (a) reuses it, and AC5c is written against (a)'s dead-report
  behaviour. The dependency edge is still declared, so the descriptor stops permitting a
  configuration the code cannot serve.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.
- rev-2 · 2026-09-05 · §8 forks resolved under the standing mandate; no scope change.
- rev-3 · 2026-09-05 · round-2 fixes folded: the ratchet row, the kit-boundary fork, and two liveness arms.
- rev-4 · 2026-09-05 · AC5d states the base condition the ratchet needs; §4's liveness pair corrected at build time.

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

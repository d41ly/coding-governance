# TOOL-aKeyedAnnotation-4 — the dossier `decisions` field becomes live and shrink-only

**Status:** OPEN · rev-2 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |

<!-- /gen:spec-records -->

## 1. Goal

The code-to-decision link this build was asked to invent already exists: every codebase-map dossier
carries a required, shape-checked `decisions` list of unit ids. Measured at this base, most dossiers
declare it empty, no consumer reads it, it appears in neither generated artifact, and the scaffolder
seeds a new dossier with an empty one. Make it live, so an orienting agent running the reuse audit
gets the seam AND the reasoning behind it.

## 2. Scope (IN)

- **S1** The reuse audit prints a dossier-sourced candidate's `decisions` ids. The dossier loader in
  `tools/codebase-map/reuse_lookup.py` already has the parsed dossier in hand and the candidate
  already carries a human-context detail field; this extends that field rather than adding one.
- **S2** A new CHECK inside the existing codebase-map test module, not a new leg: the count of
  dossiers whose `decisions` list is empty, pinned shrink-only. The manifest records that a check
  inside an existing gate is far cheaper than a leg, and the leg that carries it is unguarded and
  among the cheapest on the bar.
- **S3** The pin is MEASURED on this corpus and recorded with its reading beside it. An adopter
  scaffolding the kit gets the row with no value, the way the kit's other measured pins ship — a
  number copied from this tree is either vacuous or permanently red elsewhere.
- **S4** The scaffold template in `tools/codebase-map/gen_map.py` stops emitting an empty list as the
  finished state. It either emits the key with a comment naming what belongs there, or the check's
  message names the scaffold as the source when a fresh dossier trips it — whichever keeps the
  scaffolder honest without making a legitimately new dossier unlandable.
- **S5** Populate the `decisions` list for the dossiers this build has already read closely enough to
  fill honestly, and only those. A guessed id is worse than an empty list, because the empty list is
  visibly empty and a wrong id resolves.
- **S6** The failing case observed before landing: blank the `decisions` list on the one dossier that
  carries several ids today, confirm the check reds, restore it.

## 3. Non-goals (OUT)

- **No annotation in code.** This unit is the design pass's answer to "where does the code-to-decision
  link live", and the answer is the dossier, not a comment.
- **No tokenizer or stripper change in `map_lib`.** The open backlog row against the definition
  stripper is a prerequisite for any work in there, and this unit stays on the dossier-reader side.
- **No new generated artifact.** The field is read live from the dossier; committing a second copy is
  the artifact-with-no-cross-language-consumer shape the charter refuses.
- **No bulk backfill of every empty dossier.** The pin drains as dossiers are touched by the work that
  can fill them honestly. Filling twenty in one commit is guesswork dressed as coverage.
- **No change to the dossier schema.** The field is already required and already validated.

## 4. Design

### Data model

Unchanged. `decisions` is a list of unit ids, already validated against the project id grammar at
parse time. What changes is that something reads it and something grades how many are empty.

### The vacuous-selector shape being closed

An empty list passes validation, so nothing has ever failed on the field, so nobody fills it, so the
reuse audit returns a seam with no rationale. That is the repo's own vacuous-selector class: a rule
that binds nothing reports clean forever. The shrink-only pin is what converts "legal" into
"declining", and it is the same idiom the memory-tree kit already uses for its orphan population.

### Rollout

S1 is output-only and cannot break a gate. S2 lands with the measured pin. S5 lowers it by whatever
this build can fill honestly, in the same commit as the reading. S4 is the forward-looking half so the
pin does not immediately grow back.

### Alternatives rejected

Making the field non-empty a hard schema requirement was rejected: it makes a legitimately new dossier
unlandable before its decisions exist, and a required field with an escape hatch is a waiver registry
by another name. Emitting the field into the generated inventories was rejected as a committed second
copy with no cross-language consumer.

## 5. Production-readiness checklist

- security — N/A: read-only over tracked files.
- perf / scale — the check counts a field over the dossier set the test module already parses; the
  leg's recorded seconds are low and the addition is a loop over an existing parse. Re-measure and
  record rather than asserting.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the check must assert the dossier population is non-empty before
  reporting a count, or a map root that resolves to nothing reports a perfect score.
- observability — the reuse audit's own output carries the ids from S1; the check's message carries
  the count and the pin.
- risks — the main one is S5 becoming guesswork. The control is that only dossiers whose decisions
  this build actually read may be filled, and §6 names the evidence for each.
- testing + left-shift gates — one new check inside the existing test module, with its failing case
  observed per S6. No new leg.
- migration / rollback — additive; the pin row and the check revert together.
- user docs — the kit README's dossier-format section gains one line saying the field is read and
  graded, replacing whatever it says about the field being informational.

## 6. Acceptance criteria

- **AC1** When `python tools/codebase-map/reuse_lookup.py "<any phrase returning a dossier candidate>"`
  is run after this unit, a candidate sourced from a dossier with a non-empty `decisions` list prints
  those ids, and one from an empty dossier prints no decisions clause rather than an empty one.
- **AC2** When `python tools/codebase-map/test_codebase_map.py` is run, the new check reports the
  measured count of empty-`decisions` dossiers against a pin equal to that measurement, and exits 0.
- **AC3** When the `decisions` list is blanked on the dossier that carries several ids today, the
  check REDS; when restored, it exits 0. Observed before the check is wired, per S6.
- **AC4** When `python tools/codebase-map/test_codebase_map.py` is run against a map root holding no
  dossiers, the check reports a dead population
  rather than a zero count.
- **AC5** When a dossier is scaffolded with `python tools/codebase-map/gen_map.py` after this unit,
  the emitted `decisions` key does not read as a finished empty declaration.
- **AC6** When each id added by S5 is looked up with `git grep -w -F` against the memory root, it
  resolves to a record that genuinely governs that dossier's feature — recorded per id in the unit's
  acceptance ledger, not asserted in bulk.
- **AC7** When `bash tools/run-gates/run-gates.sh` is run on this unit's commit it is green.

## 7. Gates

Existing legs that must stay green: the full bar. Load-bearing here — `codebase-map coverage +
freshness` and the codebase-map kit self-test, plus `memory hygiene` for the dossier prose. Read
`tools/gate-legs.json` for the names. No new leg: the check joins the module the coverage leg already
runs, and that leg is unguarded so it runs on every bar.

## 8. Open questions

- **F1 — where the pin is declared.** The kit has its own conf and the memory-tree conf carries the
  repo's other measured pins. Options: (a) the codebase-map conf, keeping a kit's pin with its kit;
  (b) the memory-tree conf, keeping every corpus pin together. Recommendation: (a) — the kit is
  copy-installed and its pin must travel with it, and an adopter without memory-tree must still be
  able to declare it. RESOLVED (agent, 2026-09-05, delegated): (a), the kit's own
  conf. Verified at this base that the file exists and already carries this kit's other
  measured pins, so (a) extends a seam where (b) would create a cross-kit read an adopter
  without the memory-tree kit could not satisfy at all.
- **F2 — how S4 keeps a new dossier landable.** A scaffolded dossier legitimately has no decisions
  yet, so a check that reds on it blocks the map's own convergence rule. Options: (a) the scaffold
  emits the key with a comment and the check counts it like any other empty, since the pin is
  shrink-only and one new empty is a visible movement; (b) date-grandfather new dossiers. (a) is
  simpler and the pin already tolerates a temporary rise as a recorded raise. Recommendation: (a).
  RESOLVED (agent, 2026-09-05, delegated): (a). Option (b) is a date-grandfather term, which
  is the waiver-registry-by-another-name shape §4 rejects one paragraph above for the schema
  question; taking it here would contradict that rejection inside one spec.
- **F3 — which dossiers S5 may fill.** FACT-QUESTION · decided by reading, not judgement: a dossier
  may be filled only where this build read the governing records directly. Everything else stays
  empty and drains later. RESOLVED (agent, 2026-09-05, delegated): that rule, applied per
  dossier at build time, with AC6 as the observation — each id grepped against the memory
  root and recorded in the acceptance ledger. Liveness: the grep returns nothing for an id
  that does not resolve, which is what makes a guessed id fail rather than pass, and the
  honest outcome of the sweep may be that no dossier qualifies.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.
- rev-2 · 2026-09-05 · §8 forks resolved under the standing mandate; no scope change.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` ranked `inventory_ids` and `build_reference_index` first, and reading them
established that neither carries the decision link — but the same read surfaced the actual seam,
which is the dossier parser's own required `decisions` field and the candidate detail field the reuse
audit already prints. Both are extended in place; nothing new is introduced, which is the whole point
of this unit — the seam existed and was inert.

Recall terms used: codebase-map dossier decisions field reuse audit seam vacuous selector shrink-only
pin inventory key coverage claim orientation rationale.

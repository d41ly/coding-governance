# TOOL-aKeyedAnnotation-4 — the dossier `decisions` field becomes live and shrink-only

**Status:** CLOSED · rev-6 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-4-acceptance.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-4-acceptance.md) | journal | — |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round2.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round3.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round3.md) | diff-review | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 |

<!-- /gen:spec-records -->

## 1. Goal

The code-to-decision link this build was asked to invent already exists: every codebase-map dossier
carries a required, shape-checked `decisions` list of unit ids. Measured at this base, 17 of 20
dossiers declare it empty and the scaffolder seeds a new one empty. ONE consumer reads it —
`tools/codebase-map/map_diff.py` prints the first few ids per feature in the range digest — and the
orientation path this build cares about, the reuse audit, does not. An earlier draft of this
sentence said no consumer reads it at all, which the tree refutes and which would have made the
unit's causal story rest on a false premise. Make the field live on the reuse-audit path too, so an
orienting agent gets the seam AND the reasoning behind it.

## 2. Scope (IN)

- **S1** The reuse audit prints a dossier-sourced candidate's `decisions` ids, read from the dossier
  TEXT the module already loads and carried in a NEW candidate field printed on its own line. Both
  premises an earlier draft stated here were false against the file. That module loads dossier text
  WITHOUT parsing the toml claims, deliberately — its header declares it portable, needing no
  project-side extractor — so reaching for the parsed `decisions` tuple would drag in exactly the
  project code the module disclaims. And its `detail` field is a single OVERLOADED string branched on
  per source to resolve a candidate back to its dossier or inventory, so extending it corrupts that
  branch. A front-matter read of the already-loaded text costs neither. S1 states the truncation
  policy explicitly: print every id, where the range digest truncates to the first few, because the
  audit's reader is deciding whether to extend a seam and a hidden id is a hidden reason.
- **S2** A new CHECK inside the existing codebase-map test module, not a new leg: the count of
  dossiers whose `decisions` list is empty, pinned shrink-only. The manifest records that a check
  inside an existing gate is far cheaper than a leg, and the leg that carries it is unguarded and
  among the cheapest on the bar. **That module is a byte-identical PAIR and the check lands in the
  TEMPLATE**, `tools/codebase-map/test_codebase_map.template.py`, with the dogfood copy re-copied in
  the same commit — the template is what the kit's adopter script installs, so a check landing only
  in the dogfood copy is run by this repo and received by no adopter, while §5 ships a kit-README
  line claiming the field is graded. Nothing on the bar compares the two files: the memory-tree
  parity leg's pair list covers only that kit's docs, so codebase-map has no parity leg at all, and
  the copy relation can end silently. A sibling build makes the template an explicit write target for
  this same reason.
- **S3** The pin is MEASURED on this corpus — 17 empty of 20 dossiers at this base — and recorded
  with its reading beside it. An adopter scaffolding the kit gets the row with no value: a number
  copied from this tree is either vacuous or permanently red elsewhere. The kit conf carries no other
  measured pin today, so this is the first rather than one more of a set, and §8 F1's resolution now
  says so too.
  **The adopter's carrier is named and the unset behaviour is specified, because neither was.** The
  row lands in `tools/codebase-map/.codebase-map.conf.example`, which the kit's adopter script copies
  to an adopting repo's root, carrying an empty value and its documentation comment — the same
  dogfood-versus-shipped split S2 closes one file over. With the key ABSENT OR EMPTY the check reports
  the count as UNGRADED and says so on stdout: never a bare zero, which is the vacuous selector this
  unit exists to close, and never a red, which would break a fresh adopter's first gate run and the
  kit's own self-test, since that self-test execs the gate template from scratch trees carrying no
  conf at all. Announcing an ungraded count is the repo's existing idiom for a check that was not
  asked.
- **S8** SHRINK-ONLY NEEDS A MECHANISM, and naming it in a comment is not one. The only mechanism in
  this repo is a ratchet row in the drift-audit signals module, read during that report's check pass,
  which reds a raise unless a nearby marker spells the old and new values. Without one, anyone raises
  the number with no justification and no gate — the invisible-raise defect that ratchet was built to
  close — and §4's claim that the pin converts "legal" into "declining" does not hold. This unit
  lands that row naming the kit conf and the new key, and records what an adopter WITHOUT drift-audit
  gets: a declared pin and no enforcement, which is a documented gap rather than a silent one. The
  kit's own registry idiom under the map root was not taken because it exempts NAMED subjects from a
  rule, where this is a COUNT that must decline; the two are not interchangeable.
- **S4** AMENDED at build time: the file this item names scaffolds only the FOUNDATION document,
  which the dossier loader EXCLUDES from the population the check grades, and there is no
  feature-dossier scaffolder anywhere to change. The guidance therefore lands beside the check that
  reads the population instead. What follows is the item as written, kept so the amendment has
  something to be an amendment to. The scaffold template in `tools/codebase-map/gen_map.py` stops emitting an empty list as the
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
- **No change in `tools/drift-audit/` beyond the single ratchet row S8 names.** S8 puts a second
  copy-installed kit into this unit's write set, and §5 cited this section as the bound on it while
  this section said nothing about that kit at all — a control asserted rather than written, which is
  this build's recurring shape. It is written now, so the citation resolves.

## 4. Design

### Data model

Unchanged. `decisions` is a list of unit ids, already validated against the project id grammar at
parse time. What changes is that something reads it and something grades how many are empty.

### The vacuous-selector shape being closed

An empty list passes validation, so nothing has ever failed on the field, so nobody fills it, so the
reuse audit returns a seam with no rationale — and the one consumer that does read it, the range
digest, prints an empty clause for 17 of 20 features. That is the repo's own vacuous-selector class:
a rule that binds nothing reports clean forever. The shrink-only pin converts "legal" into
"declining", and it is the same idiom the memory-tree kit already uses for its orphan population —
but only once S8's ratchet row exists, because a pin with no ratchet behind it is a comment.

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
  observed per S6, plus S8's ratchet row and the raise-without-a-marker observation AC9 makes, and
  the portability arm AC8 makes permanent. No new leg. Note that S8 puts a second kit,
  `tools/drift-audit/`, into this unit's write set; §3's non-goals bound what may change there to
  the one ratchet row.
- migration / rollback — additive; the pin row and the check revert together.
- user docs — the kit README's dossier-format section gains one line saying the field is read and
  graded, replacing whatever it says about the field being informational.

## 6. Acceptance criteria

- **AC1** When `python tools/codebase-map/reuse_lookup.py "<any phrase returning a dossier candidate>"`
  is run after this unit, a candidate sourced from a dossier with a non-empty `decisions` list prints
  those ids, and one from an empty dossier prints no decisions clause rather than an empty one.
- **AC2** When `python tools/codebase-map/test_codebase_map.py` is run, the new check reports the
  measured count of empty-`decisions` dossiers against a pin equal to that measurement, and exits 0.
  The check itself is authored in the template sibling and copied to this path, per S2.
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
- **AC8** When `python tools/codebase-map/selftest.py` is run it exits 0 with a NEW ARM that runs the
  reuse audit in a scratch tree with the project-side extractor REMOVED, asserting it still runs and
  still prints the decisions line. The arm is what makes the property permanent; an earlier form of
  this criterion described a one-off build-time run and called it permanent, which its own closing
  sentence condemns — a declared property with no arm asserting it is a comment. Observed RED against
  a decisions line that reads the parsed dossier. That module ships as a pair, so the arm lands in
  the copy adopters receive and the dogfood copy is re-copied, exactly as S2 requires of the gate.
- **AC8b** When `bash tools/codebase-map/adopt-codebase-map.sh` is run into a scratch adopter tree
  and the installed gate is then run with the new pin UNSET, it reports the count as ungraded and
  says so, rather than a traceback, a bare zero or a red — S3's adopter behaviour, observed on the
  path an adopter actually takes.
- **AC9** When the new pin is raised in the kit conf with no old-to-new marker beside it and
  `python tools/drift-audit/drift_report.py --check` is run, the `drift-audit records` signal REDS;
  with the marker present it does not. Observed both ways, which is what makes S8's ratchet row a
  mechanism rather than a claim.
- **AC10** When `cmp tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py`
  is run after this unit it reports the two files identical — the observation that catches a check
  landing in one copy and not the other, which nothing else on the bar would notice.

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
  conf, on ONE ground: the kit is copy-installed, so its pin must travel with it, where (b) would
  create a cross-kit read an adopter without the memory-tree kit could not satisfy at all.
  An earlier form of this resolution added a second ground — that the file already carries this
  kit's other measured pins — and stamped it "verified at this base". It is false. That conf holds
  a map root, a gate file, a digest command, a dark-layers list, a clone-count path and a fan-in
  threshold whose own comment says it was never re-measured. This is the conf's FIRST measured pin,
  which is exactly why S3 spells out that an adopter gets the row with no value. S3 announced this
  correction before it was made, so for one revision the false claim stood while a sibling section
  certified it fixed; the pick itself never depended on it.
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
- rev-3 · 2026-09-05 · round-1 spec-audit fixes folded in.
- rev-4 · 2026-09-05 · §5 carries S8's second kit and the two arms the fold added.
- rev-5 · 2026-09-05 · round-2 fixes folded: F1's false ground removed, the adopter carrier named, the arm made permanent.
- rev-6 · 2026-09-05 · S4 and AC5 amended at build time: the file they named scaffolds no feature dossier.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` ranked `inventory_ids` and `build_reference_index` first, and reading them
established that neither carries the decision link — but the same read surfaced the actual seam,
which is the dossier parser's own required `decisions` field and the candidate detail field the reuse
audit already prints. Both are extended in place; nothing new is introduced, which is the whole point
of this unit — the seam existed and was inert.

Recall terms used: codebase-map dossier decisions field reuse audit seam vacuous selector shrink-only
pin inventory key coverage claim orientation rationale.

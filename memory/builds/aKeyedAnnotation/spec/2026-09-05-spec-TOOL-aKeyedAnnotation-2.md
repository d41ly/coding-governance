# TOOL-aKeyedAnnotation-2 — the shipped-evidence oracle reads one grammar and stops certifying itself

**Status:** OPEN · rev-5 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md) | spec-audit | TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |

<!-- /gen:spec-records -->

## 1. Goal

The drift-audit signal that reads a unit id out of product source is this repo's only working
annotation consumer, and three defects make it read things it should not: it uses a hand-typed id
regex that diverges from the shipped grammar, its population includes test files, and the comment
documenting its pin cites the very ids it counts. Fix all three so the annotation layer has a correct
reader before anything else is built on it.

## 2. Scope (IN)

- **S1** Replace the hand-typed `_OWN_ID` pattern in `tools/drift-audit/drift_report.py` with one
  built from the shipped id grammar the recall extractor owns — via the extractor's per-root grammar
  ACCESSOR, bound to the tree being classified, and never the module-level constants, which bind at
  import to the repo the KIT lives in. `memory/gotchas/grammar-bound-to-the-wrong-root.md` records
  the measured incident and names that accessor as the fix, one accessor and no second grammar. The
  hazard is live inside this unit's own harness: the kit self-test copies the report into a scratch
  tree carrying fixture ids and no memory-tree conf, which is exactly where a wrongly-bound grammar
  reports a confident zero, and two of the criteria below run there. Keep both capture groups: group
  1 the unit id, group 2 the slug. The session era in the shipped grammar admits a trailing lowercase
  correction suffix that the hand-typed digits-then-boundary form cannot match; adopting the shipped
  grammar inherits that fix rather than re-deriving it.
- **S2** Give the shipped-evidence oracle its own narrower globs, on the same reasoning already
  written beside the trace globs in `tools/drift-audit/drift_signals.py`: a citation from a test file
  is the house's own bookkeeping certifying the bookkeeping. The narrowing is declared beside the
  existing one, never inlined at the call site — and in BOTH carriers the trace globs already use.
  `drift_signals.py` is the kit descriptor's `role = "project-owned"` file; the `role = "seed"` file
  adopters actually receive is `tools/drift-audit/drift_signals.template.py`, which carries the trace
  globs as an empty row with its own documentation block. A declaration added only to the first
  reaches this repo and nobody else, so every copy-installed drift-audit would keep the
  self-certifying oracle this unit exists to correct while the kit README advertises the correction.
  The template row ships EMPTY, and the reader takes the name with getattr-and-fallback to the
  product globs exactly as the trace globs do, so an older adopter's project layer does not trip the
  required-attribute check. **An empty row falling back to the product globs hands the adopter the
  unnarrowed oracle — the outcome this item exists to prevent — so the empty row is declared as a
  HOLE in `tools/drift-audit/kit.toml`, with a discharge probe, beside the two that kit already
  carries for exactly this shape.** Without that, adopters receive the declaration and no forcing
  function to fill it, while §5 has the kit README record the correction as shipped. The kit's
  existing hole for its trace cutoff is worded "correct on day one, and permanently inert if nobody
  ever fills it", which is the same sentence about this row.
- **S3** Stop the pin comment in `drift_signals.py` from spelling the ids it counts. Verified at this
  base: `drift_signals.py` is itself in the citation set returned for BOTH pinned ids, so the pin
  cannot be drained by removing the annotations it describes. Route the reader to the report's own
  detail output instead of naming the ids in a file inside the population.
- **S4** Re-measure the pin in the same commit as the change, and record what moved and why beside it.
  MEASURED AT THIS BASE, and stated here so a builder is not misled by it: S1, S2 and S3 are each
  expected to move the value by ZERO on this corpus, because both pinned ids keep non-test product
  citations that none of the three touches. The recorded line must SAY so. Three identical readings
  are then a confirmed result rather than evidence the change did not work — which is how the earlier
  wording here, that each step moves the population independently, would have been read.
- **S5** FIVE regression arms in the kit's existing self-test, each observed RED before it is wired,
  one per criterion that observes a change this unit makes: a correction-form spec header that the
  old pattern scores unkeyed; a spec cited only from a test file; for S3, a scratch tree with EVERY
  remaining product citation of both pinned ids deleted — the set enumerated by the invocation AC4
  prints, never a count typed into this spec — asserting the signal's VALUE reaches zero while its
  judgeable population does not; for S6, a scratch tree with the narrowed declaration EMPTIED,
  asserting the signal reports itself dead rather than a live zero; and a scratch fixture declaring
  an id family this repo does not declare, asserting S1's pattern still classifies it. The count is
  stated in three places in this spec and they must agree; an earlier draft said three here and four
  below, which is the two-answers-to-one-question class inside one document.
- **S6** A SECOND liveness half, owned by the narrowed declaration: the count of tracked files those
  globs actually resolve to. The signal's existing half counts non-terminal keyed SPECS and is
  computed before any glob is read, so a glob set matching nothing leaves it live and full-sized
  while the value falls to zero — the reassuring zero, wearing a live flag. Only a count of what the
  narrowed globs resolve to can see that hazard.

## 3. Non-goals (OUT)

- **No new gate leg.** The `drift-audit records` leg is unguarded and already on every bar.
- **No change to the signal's meaning or its gateable flag.** This unit makes the existing question
  answerable correctly; it does not ask a different one.
- **No annotation grammar, marker, or filter on marked lines.** The design pass records that the
  marker proposal is only needed under a mandate the build refuses.
- **No touching `PRODUCT_GLOBS` itself.** Other signals read it and this unit has not measured them;
  the narrowing is a second declaration, the way the trace globs already are.
- **No pin raise to make a number look tidy.** If the re-measurement raises it, that is a finding for
  §8, not an edit.

## 4. Design

### Data model

One id regex in the repo, imported rather than mirrored. The two capture groups stay because two
signals ask two different questions off one match — the unit for "did this unit ship", the slug for
the build-level question — and that projection is what keeps the recorded slug over-flag from
returning.

### Inventory

Four sites: the pattern definition, the oracle's grep call, the pin comment, and the globs
declaration — which lands TWICE. It joins the existing declaration in the project-owned signals
module, not the report module, AND ships as an empty documented row in that module's seed template,
which is the copy adopters receive. The trace globs already ship in exactly that pair, so this
follows a precedent rather than inventing one.

### Migration

The one-change-one-measurement-one-recorded-line order stands, but not for the reason this paragraph
used to give. It opened "The population moves under each of S1, S2 and S3", which is the exact
wording S4 was rewritten to repudiate and which AC4 refutes in the spec's own vocabulary: the
judgeable population counts non-terminal keyed specs, and nothing done to annotations touches it.
The expected movement of the VALUE under each of S1, S2 and S3 is ZERO on this corpus, so three
identical readings are the confirmed result. The discipline exists so that an UNEXPECTED movement is
attributable to one change, not because movement is expected.

### Alternatives rejected

Filtering the oracle on a marked line was rejected with the marker itself. Widening the pin to absorb
the test-file citations was rejected: it preserves the defect and spends the ratchet. Deleting the pin
comment outright was rejected because the residual ambiguity it records — a built-but-unmerged unit is
arguably INPROGRESS — is real and a later reader needs it.

## 5. Production-readiness checklist

- security — N/A: a read-only report over tracked files.
- perf / scale — the greps are per-spec and already run; narrowing the globs can only shrink them.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the signal's EXISTING liveness half cannot see S2's hazard, and
  saying otherwise was the defect. It counts non-terminal keyed specs before any glob is read, so a
  narrowed set matching nothing leaves it True at full size while only the value falls. S6's second
  half is the control that can see it, and §6 asserts both — the judgeable population stays
  non-empty, and emptying the declaration makes the signal report itself dead.
- observability — the report prints the population and the pin on every run; that is the observation.
- risks — the real hazard is a silent population collapse: a narrowed glob that matches nothing
  reports a reassuring zero. S6's second liveness half is the control; the pre-existing one is not,
  and §6 asserts the difference by emptying the declaration in a scratch tree.
- testing + left-shift gates — five regression arms, each observed RED first, plus two left-shifts
  the round-1 audit named and this unit owns: a self-test arm that, for EVERY signal whose
  declaration is a glob set, empties that declaration and asserts its liveness flag goes False —
  which gates the class rather than this instance — and a ban-grep so no module outside the recall
  extractor imports its module-level grammar constants. No new leg.
- migration / rollback — pure revert; the pin value moves with the code that changed it.
- user docs — the kit README records both corrections it already carries; this adds the third.

## 6. Acceptance criteria

- **AC1** When a spec header carrying a correction-form id (a numeric seq with a trailing lowercase
  letter) is placed in a scratch tree and `python tools/drift-audit/drift_report.py` is run, that spec
  is counted as keyed rather than reported as unkeyed. Observed RED against the current pattern first.
- **AC2** When `python tools/drift-audit/drift_report.py` is run and a non-terminal spec's id is
  cited ONLY from a file matching the test population, the
  shipped-evidence signal does not count it; when the same id is cited from a product file, it does.
- **AC3** When `git grep -l -w -F` is run for each id named by the pin comment after this unit, the
  file holding that comment is not in the result.
- **AC4** When, in a scratch tree, EVERY remaining product citation of both pinned ids is deleted and
  `python tools/drift-audit/drift_report.py --check` is run, the shipped-evidence signal's VALUE
  reaches zero while its judgeable population stays at its measured size. The criterion PRINTS the
  `git grep -l -w -F` invocation over the narrowed globs that enumerates the set, so the population
  is derived at run time and no count is typed here. The value is what citations move; the judgeable
  population counts non-terminal keyed specs and nothing done to annotations touches it, which is
  what lets AC5 demand that same number stay non-empty without contradicting this one.
- **AC5** When `python tools/drift-audit/drift_report.py --check` is run after this unit, the
  shipped-evidence signal reports a live, non-empty judgeable population AND a non-empty count of the
  files its narrowed globs resolve to, and its pin equals the re-measured value with the movement
  recorded beside it.
- **AC6** When `python tools/drift-audit/selftest.py` is run it exits 0 with the five new arms
  present, and each arm has been observed failing against the pre-change code.
- **AC7** When `bash tools/run-gates/run-gates.sh` is run on this unit's commit it is green.
- **AC8** When the narrowed glob declaration is emptied in a scratch tree and
  `python tools/drift-audit/drift_report.py --check` is run, the shipped-evidence signal reports
  itself DEAD rather than reporting zero findings. Observed RED against the pre-change code, where
  the same emptying yields a live zero.
- **AC9** When `python tools/drift-audit/selftest.py` is run against a scratch fixture declaring an
  id FAMILY this repo does not declare, the new pattern classifies that fixture's ids — proving the
  grammar is bound to the tree under test and not to the kit's own repo. Observed failing against a
  module-constant binding.
- **AC10** When the seed template is read after this unit it carries the narrowed-glob row empty with
  its documentation block, and a scratch adopter tree whose project layer declares neither name still
  runs `python tools/drift-audit/drift_report.py --check` without a required-attribute refusal.

## 7. Gates

Existing legs that must stay green: the full bar. Load-bearing here — `drift-audit records` and the
drift-audit kit self-test, plus whatever `tools/gate-legs.json` guards on `tools/drift-audit/` and on
`tools/memory-recall/` if the grammar import crosses that boundary. Read the manifest for the names.
No new leg.

## 8. Open questions

- **F1 — how the grammar crosses the kit boundary.** drift-audit is copy-installed and must not
  import from a kit an adopter may not have. Options: (a) import the recall extractor's grammar when
  importable and fall back to a local copy that the kit self-test byte-compares against it, which
  keeps one source and fails loudly on divergence; (b) keep a local copy with a parity arm only;
  (c) move the grammar into a shared location both kits read. Recommendation: (a) — it is the shape
  this repo already uses for a value two kits must agree on, and (c) is a cross-kit contract change
  that would need its own design pass. RESOLVED (agent, 2026-09-05, delegated): (a).
  Option (c) trips M3's veto 2 — a cross-kit contract is a new public surface — so it is
  discarded rather than chosen. Between the two survivors (a) satisfies strictly more of
  §6: it keeps one source AND fails loudly on divergence, where (b) only reports.
- **F2 — whether the narrowed globs belong to this signal alone or to a named second population.**
  The trace globs are already a second declaration for one signal, so the precedent says per-signal.
  Recommendation: follow the precedent and declare a third, rather than inventing a shared "non-test
  product" set that no measurement supports yet. RESOLVED (agent, 2026-09-05,
  delegated): declare a third per-signal population beside the trace globs. A shared set
  would rest on no measurement, and §3 already forbids touching the existing product globs
  that other, unmeasured signals read.
- **F3 — what the pin becomes.** Unknown until S1 to S3 are measured. FACT-QUESTION · run the report
  after each change and take the reading; do not predict it here. RESOLVED (agent, 2026-09-05,
  delegated): the pin is whatever S4's measurement returns, taken one change at a time and
  recorded beside the value. That IS the pick — the number is data the probe produces, not
  an option anyone chooses — and §3 already forecloses the one choice available here by
  refusing a raise made to tidy the figure. Liveness: the reading can move in either
  direction, and a raise is a §8 finding rather than an edit.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.
- rev-2 · 2026-09-05 · §8 forks resolved under the standing mandate; no scope change.
- rev-3 · 2026-09-05 · round-1 spec-audit fixes folded in.
- rev-4 · 2026-09-05 · the regression-arm count reconciled across §2, §5 and §6.
- rev-5 · 2026-09-05 · round-2 fixes folded: §4 Migration reconciled with S4, and the seed row declared a hole.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` returned `build_reference_index` and `inventory_ids` as seams, neither of which
this unit extends — both belong to codebase-map, which the design pass rules out of scope. The seam
this unit actually rides was found by reading the kit: the id grammar already published by
`tools/memory-recall/extract.py` and already consumed through a resolver by the memory-tree kit, and
the second-globs declaration precedent already present in `tools/drift-audit/drift_signals.py`. Both
are extended, neither is duplicated.

Recall terms used: drift-audit spec-status oracle product globs shipped evidence id grammar
correction era pin shrink-only self-citing bookkeeping.

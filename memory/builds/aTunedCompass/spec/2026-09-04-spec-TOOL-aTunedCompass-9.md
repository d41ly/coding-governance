# TOOL-aTunedCompass-9 — a recall fixture that can tell the two-set ensemble from its records half

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Build a graded question set that can distinguish the served two-set ensemble from its `records` half
alone. The committed fixture cannot: with terms at `k=20`, `records:fts5` scores recall 1.000 by
itself, so every ensemble scores 1.000 too and no floor derived from it carries information. Until a
fixture exists that can tell the two apart, no pin over the ensemble means anything, which is why the
owner blocked `TOOL-aTunedCompass-2` and `TOOL-aTunedCompass-3` on this unit.

## 2. Scope (IN)

- **S1** — questions whose correct answer is a PASSAGE inside a record rather than the record's own
  anchor. That is the discriminating shape: a chunk hit is the right answer and a whole-record hit is
  not, so the chunk half has something to contribute that the record half cannot supply.
- **S2** — `expected_paths` becomes the mechanism for expressing that expectation.
  `tools/memory-recall/bench.py` (`:349`) already reads the field and no committed fixture sets it,
  so the capability ships today and is exercised by nothing. This unit uses what is there rather than
  inventing a second expectation vocabulary.
- **S3** — questions are SAMPLED from the live query log rather than hand-authored. The log at the
  git common dir holds 130 distinct real questions with the terms their session supplied and the
  paths each was shown. Sampling from it removes the authorship bias the parent report flagged in its
  own measurement, where the terms were written by someone who had just read the corpus.
- **S4** — a declared, defensible n, with the reason written beside it. The committed fixture is 12
  and every figure this build quotes carries that n; this unit states what n it targets, why that
  number, and what it costs to grade.
- **S5** — the fixture's `_README` gains a section stating what a DISCRIMINATING question is, so a
  later author extending the set cannot silently add saturating ones back.
- **S6** — a report, recorded as this build's journal, giving the ensemble comparison the parent
  report could not: `records:fts5` alone against `records:fts5+chunks:fts5` and against
  `records:fts5+chunks:roll`, at a `k` with headroom, over the new set.

## 3. Non-goals (OUT)

- Not moving `RECALL_FLOOR`. This unit produces the instrument; pinning against it is
  `TOOL-aTunedCompass-3`, which is sequenced after and blocked on this one.
- Not replacing the committed fixture. The existing 12 questions grade the `records` half and grade
  it correctly; this unit ADDS a set rather than retiring one. Whether the two merge is a later call.
- Not deciding the chunk set's fate. This unit makes that decision possible and does not take it. The
  build README parks it explicitly.
- Not changing any substrate. `roll` is `TOOL-aTunedCompass-4`'s business.

## 4. Design

The saturation is the whole problem, so the design is chosen to remove it rather than to work around
it. A question whose expected answer is an anchored record is answerable from `records` alone, and
`records:fts5` answers all twelve. A question whose expected answer is a specific passage — a
paragraph of reasoning inside a long spec, a gotcha's mechanism sentence, one row of a table — is not
answerable by returning the enclosing record, because the enclosing record is up to tens of KB and
the reader still has to find the passage. That is precisely the work the chunk half exists to do, and
it is the work no current fixture question asks for.

Sampling from the live log matters for a reason beyond bias. The log records what was SHOWN for each
question, so a sampled question arrives with a candidate answer set already attached, and the
authoring work becomes judging which shown passage actually answered it rather than inventing an
expectation from nothing.

The honest risk, stated because it decides whether this unit is worth building: it is possible that
after all this the chunk half still adds nothing, and the answer is to drop it from the ensemble. That
is a legitimate outcome and the unit is worth building for it — a measured decision to drop a set that
costs 116% more snippet bytes is worth more than an unmeasured decision to keep it.

## 5. Production-readiness checklist

Observability: the report in S6 states its n beside every figure, per the build README's rule.
Testing: an arm asserting that at least one question in the new set is NOT answerable from `records`
alone, which is the property the whole unit exists to create and the one a later edit could silently
destroy. Migration: none, the set is additive. Cost: grading a larger set costs wall clock in
`bench.py`, and this repo requires a suite to declare a ceiling.

## 6. Acceptance criteria

1. The new set is graded by `bench.py` and `records:fts5` alone does NOT score 1.000 on it at the
   `k` the report uses. A set that saturates has failed this unit's only real requirement.
2. At least one question resolves through `expected_paths` rather than `expected_ids`, and
   `bench.py`'s `ceiling` for the `chunks` set on the new questions is 1.00, proving the expected
   passages exist in that set at all.
3. The report in S6 records all three ensembles with both byte accountings from `union.py`, at a `k`
   with headroom, and states n.
4. Questions are traceable to the live log: the record names the `qid` each sampled question came
   from, so the sampling is auditable and not an assertion.
5. `python tools/memory-recall/check-recall.py` still exits 0 on the existing fixture. This unit adds
   a set and must not disturb the floor that already passes.
6. The fixture's `_README` states what makes a question discriminating, and an arm in
   `tools/memory-recall/selftest.py` fails if a question is added that `records` alone answers.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `recall floor` and `memory hygiene` the legs that bind.
The kit's own self-test suite is `subject = kit` and is held by default, so exercising S6's arm needs
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and the record must say it was run that way.

## 8. Open questions

**F1 RESOLVED (agent, 2026-09-05, delegated): agent judgement, recorded per question, with a declared
spot-check rate the owner reads at the wrap-up.** The owner-authors option cannot be executed by a run
with no owner turn, and restricting to the 17 `in_shown: true` rows is refused on the unit's own
terms: S4 requires a defensible n and §8 already calls 17 "probably too few", so that option risks
failing AC1 by leaving too small a set to demonstrate non-saturation. The surviving option is also the
most feature-rich — it keeps S3's sampling, satisfies AC4's per-question `qid` traceability, and adds
the spot-check rate as a stated number rather than an implied one. The judgement for each question is
written into the fixture record so it can be re-read and overturned without re-deriving the set.

**F2 RESOLVED (agent, 2026-09-05, delegated): a second file beside the existing fixture.** This was the
recommendation and it is also the only option AC5 makes safe: the existing floor must still exit 0 on
the existing fixture, and a single merged corpus with a per-question kind field puts that guarantee at
the mercy of every later edit. A second file makes AC5 true by construction, and `TOOL-aTunedCompass-3`
then pins against a named population rather than one that can silently grow.

- **F1 — who judges which shown passage answered a sampled question?** The log gives the question and
  what was shown, never which hit the session used — the `opened` rows are heuristic and one per
  query at best. So an author still has to read and decide. Options: an agent judges and a human
  spot-checks a sample; the owner authors all of them; or the set is restricted to questions whose
  `opened` row exists and is `in_shown: true`, which is 17 rows and probably too few.
  Recommendation: agent judgement with a declared spot-check rate, and the judgement recorded per
  question so it can be re-read. Left open because it decides whether this fixture is trustworthy
  enough to pin a floor against, which is the entire downstream use.

- **F2 — does the new set live beside the existing fixture or inside it?** A second file keeps the
  passing floor undisturbed and makes the two purposes legible. One file with a per-question kind
  field keeps a single corpus and one `_README`. Recommendation: a second file, because
  `TOOL-aTunedCompass-3` will pin against one of them and a pin whose population silently grew is the
  shape this build exists to remove. Left open because the owner may prefer one corpus.

## 9. Revision log

- rev-1 · 2026-09-05 · first draft. Added by the restructure recorded in the build README after the
  owner blocked `TOOL-aTunedCompass-2` and `-3` on a discriminating fixture rather than pin a floor
  against saturation. Drains the backlog row `TOOL-aWeighedCompass-18`.
- rev-2 · 2026-09-05 · F1 and F2 resolved under the standing mandate, M3's rule. F1's owner-authors
  option is unexecutable in a run with no owner turn and the 17-row restriction risks AC1; F2's
  single-corpus option puts AC5 at the mercy of later edits. Both survivors were the fork's own
  recommendation. No scope, acceptance or gate text moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a retrieval fixture whose expected answer is a passage
inside a record"` returned `expected_by_target` in `tools/memory-recall/bench.py` at rank 1 of its
candidates, which is the seam this unit extends: it is the function that resolves a question's
expected documents, and the `expected_paths` branch inside it at (`:349`) is the passage-level
mechanism that already ships and that no fixture uses. `extract_records` and `zero_record_diagnosis`
in `tools/memory-recall/extract.py` also returned and were read; neither is extended, because this
unit changes what is ASKED and not how documents are built. No new scorer is written.

Recall terms used: fixture recall floor pin saturation ensemble chunks records expected_paths
discriminating query log sampling bench union

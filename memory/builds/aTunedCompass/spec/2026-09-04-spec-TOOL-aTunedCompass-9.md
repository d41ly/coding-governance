# TOOL-aTunedCompass-9 — a recall fixture that can tell the two-set ensemble from its records half

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |

<!-- /gen:spec-records -->

## 1. Goal

Build a graded question set that can distinguish the served two-set ensemble from its `records` half
alone. The committed fixture cannot: with terms at `k=20`, `records:fts5` scores recall 1.000 by
itself, so every ensemble scores 1.000 too and no floor derived from it carries information. Until a
fixture exists that can tell the two apart, no pin over the ensemble means anything, which is why the
owner blocked `TOOL-aTunedCompass-2` and `TOOL-aTunedCompass-3` on this unit.

## 2. Scope (IN)

- **S1** — questions whose correct answer is a PASSAGE in a file that carries NO ANCHORED RECORD.
  That restriction is what makes the set discriminating, and it is a structural property rather than
  a hope: `extract_records` emits one document per anchored id, so a file with no anchored id
  contributes ZERO documents to the `records` set, and a target naming it cannot be satisfied from
  that set at all. Measured over the tracked corpus, 1279 of 1324 memory `.md` files are in that
  state, and they include every long document in the tree — review reports up to 205 KB, design
  passes, long specs — which is exactly the population where a passage is the right answer and a
  whole-file answer is useless.
- **S2** — `expected_paths` is the mechanism, RESTRICTED to the S1 population and only there.
  `tools/memory-recall/bench.py` (`:349`) already reads the field and no committed fixture sets it,
  so the capability ships and is exercised by nothing. The restriction is load-bearing and the reason
  is at source: `expected_by_target` resolves a path target by whole-FILE equality
  (`:362`-`:365`, `hits = {i for i, r in enumerate(docs) if r["path"] == tp}`) and a record-level
  document carries its enclosing file's path (`tools/memory-recall/extract.py` `:499`). So on an
  ANCHORED file the `records` set satisfies a path target by returning the record — the case this
  unit's §4 argues is impossible — and the mechanism discriminates nothing. On an unanchored file
  there is no record document to return, and the same mechanism discriminates perfectly. No second
  expectation vocabulary is invented; the population is narrowed instead.
- **S2b** — the sampled questions are FILTERED BY MEASUREMENT before they enter the set: a candidate
  is kept only when `records:fts5` alone fails to retrieve the judged answer at the report's `k`
  while `chunks:fts5` retrieves it. AC1 is then true by construction rather than by ranking luck,
  which is what "a set that saturates has failed this unit's only real requirement" actually demands.
- **S3** — questions are SAMPLED from the live query log rather than hand-authored. The log at the
  git common dir holds 130 distinct real questions with the terms their session supplied and the
  paths each was shown. Sampling from it removes the authorship bias the parent report flagged in its
  own measurement, where the terms were written by someone who had just read the corpus.
- **S4** — a declared, defensible n, with the reason written beside it. The committed fixture is 12
  and every figure this build quotes carries that n; this unit states what n it targets, why that
  number, and what it costs to grade.
- **S5** — the fixture's `_README` gains a section stating what a DISCRIMINATING question is, so a
  later author extending the set cannot silently add saturating ones back. It states the S1
  restriction explicitly, because "a passage question" without "in an unanchored file" is the version
  that does not work.
- **S5b** — the new set states which of the committed fixture's two authoring rules it inherits, and
  where it does not, the waiver is written down with its reason. The committed `_README` carries a
  PROVENANCE RULE — each answer determined by a person writing a record that states it, cited in
  `from` — and `check-recall.py --audit-fixture` enforces an anti-tautology bound against
  `OVERLAP_MAX` (`:87`). F1's resolution has an agent judge the expected passage from what the log
  SHOWED, which is a weaker provenance than the committed set's and must be recorded as such rather
  than left to be assumed equivalent. The anti-tautology bound is inherited outright: nothing about
  agent judgement makes a tautological question acceptable.
- **S5c** — `--audit-fixture` iterates every fixture the kit holds rather than the single
  `FIXTURE_NAME` constant it defaults to at `tools/memory-recall/check-recall.py` (`:303`). Without
  this, a second fixture is unaudited on the day it lands and stays unaudited until somebody
  remembers to widen a constant — and `TOOL-aTunedCompass-3` is to pin the merge bar against this
  population, so an unaudited set would become the bar's basis. Derive over author.
- **S5d** — the new fixture path is claimed as `role = "project-owned"` in
  `tools/memory-recall/kit.toml`, beside the three gov-only files already withheld there, and added
  to the removal line at `WIRE-INTO-PROJECT.md` (`:364`). That kit claims its directory with
  `[[files]] include = "**" role = "engine"` and `govkit.py`'s `LANDABLE_ROLES` is `(engine, seed)`,
  so an unclaimed fixture ships to every adopter — a question set sampled from THIS repo's query log
  and keyed on THIS repo's record ids, which is the outcome that `kit.toml` comment forbids by name,
  citing `memory/gotchas/pin-copied-from-another-corpus.md`.
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
`records:fts5` answers all twelve.

**Where rev-1's argument was wrong, stated plainly because the whole unit rested on it.** It claimed
a passage "is not answerable by returning the enclosing record, because the enclosing record is up to
tens of KB and the reader still has to find the passage". That is an argument about a reader's
EXPERIENCE, and `bench.py` does not measure experience — it measures whether a document satisfying
the target appeared in the top `k`. On an anchored file the enclosing record IS such a document, by
whole-file path equality, so the metric credits `records` for exactly the question shape rev-1 said
it could not answer. AC2 was worse than weak under that design: "the `chunks` ceiling is 1.00,
proving the expected passages exist" is true of any file that has chunks at that path, which is every
file.

**What actually discriminates is the absence of a record document, and it is structural.**
`extract_records` emits one document per ANCHORED id. A file with no anchored id therefore
contributes nothing to the `records` set, and no target naming it can be satisfied from that set —
not by ranking luck, but because the candidate does not exist. Measured over the tracked corpus:

| Population | Files |
|---|---|
| tracked `.md` under the memory root | 1324 |
| files contributing at least one `records` document | 45 |
| files contributing NONE — the S1 population | 1279 |

The restriction costs almost nothing, because the unanchored set is where the long documents live:
the ten largest run from 71 KB to 205 KB and are review reports, design passes and long specs. Those
are the documents a passage question is worth asking about, and the ones where returning "the file"
is the least useful possible answer.

The second half of the design is S2b's filter. Structural unsatisfiability makes a records-alone
answer impossible for the TARGET; it does not by itself guarantee `records:fts5` scores below 1.000,
since recall is measured per question over whatever targets that question declares. Keeping only
candidates that records-alone demonstrably misses at the report's `k` is what turns AC1 from a
measurement that might come out right into a property the set is built to have.

Sampling from the live log matters for a reason beyond bias. The log records what was SHOWN for each
question, so a sampled question arrives with a candidate answer set already attached, and the
authoring work becomes judging which shown passage actually answered it rather than inventing an
expectation from nothing.

The honest risk, stated because it decides whether this unit is worth building: it is possible that
after all this the chunk half still adds nothing, and the answer is to drop it from the ensemble. That
is a legitimate outcome and the unit is worth building for it — a measured decision to drop a set that
costs 116% more snippet bytes is worth more than an unmeasured decision to keep it.

## 5. Production-readiness checklist

- security — N/A as a runtime surface, but NOT as a distribution one: the set is sampled from this
  repo's own query log and keyed on its record ids, so S5d withholds it from adopters. A fixture that
  ships is a corpus leak dressed as a default.
- perf / scale — grading a larger set costs wall clock in `bench.py`. The set is bounded by S4's
  declared n, and the report states the cost it measured.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The questions are English, sampled from an English corpus; no localisation surface.
- error / empty / loading states — the state that matters is a fixture question whose targets resolve
  to NOTHING in a set, which `bench.py` reports as a `ceiling` below 1.00. AC2 reads that number
  rather than assuming the passages exist.
- observability — the report in S6 states its n beside every figure, per the build README's rule, and
  AC4 makes every question traceable to the `qid` it was sampled from.
- risks — the honest one is that the chunk half still adds nothing once the set discriminates, and the
  answer is then to drop it from the ensemble. That is a legitimate outcome and the unit is worth
  building for it. The second is provenance: agent judgement is weaker than the committed fixture's
  person-authored `from` rule, which S5b records rather than glosses.
- testing + left-shift gates — an arm asserting at least one question is NOT answerable from
  `records` alone, which is the property the whole unit creates and the one a later edit could
  silently destroy. The durable left-shift is S5c: `--audit-fixture` iterating every fixture rather
  than one constant, so a second set is audited the day it lands.
- migration / rollback — none; the set is additive and the committed fixture is untouched, which AC5
  observes. Rollback is deleting one file and one `kit.toml` rule.
- user docs — N/A. `help/` pages cover user-facing features; the fixture's own `_README` is the
  documentation, and S5 requires it to state what makes a question discriminating.

## 6. Acceptance criteria

- **AC1** — The new set is graded by `bench.py` and `records:fts5` alone does NOT score 1.000 on it
  at the `k` the report uses. A set that saturates has failed this unit's only real requirement.
- **AC2** — EVERY question in the new set names an `expected_paths` target whose file contributes no
  document to the `records` set, verified by running `extract_records` over that file and observing
  zero. That is the S1 restriction stated as an observation, and it replaces rev-1's criterion — a
  `chunks` ceiling of 1.00 — which was true of any file that has chunks at that path, i.e. every
  file, and so could not fail.
- **AC3** — `bench.py`'s `ceiling` for the `records` set over the new questions is 0.00 and for the
  `chunks` set is 1.00. The pair is the discrimination made numeric: the expected documents are
  unreachable in one set and present in the other. A `records` ceiling above 0.00 means a question
  slipped past AC2.
- **AC4** — The report in S6 records all three ensembles with both byte accountings from `union.py`,
  at a `k` with headroom, and states n.
- **AC5** — Questions are traceable to the live log: the record names the `qid` each sampled question
  came from, so the sampling is auditable and not an assertion. Each also records the judgement made
  and the declared spot-check rate, per F1's resolution, so a later reader can overturn a judgement
  without re-deriving the set.
- **AC6** — `python tools/memory-recall/check-recall.py` still exits 0 on the existing fixture. This
  unit adds a set and must not disturb the floor that already passes.
- **AC7** — `python tools/memory-recall/check-recall.py --audit-fixture` audits the NEW fixture
  without being told its name, and every question in it is under `OVERLAP_MAX`. The first half is
  S5c's derivation; the second is the anti-tautology bound the committed set already carries.
- **AC8** — The fixture's `_README` states what makes a question discriminating, including the
  unanchored-file restriction and the provenance the set actually has, and an arm in
  `tools/memory-recall/selftest.py` fails if a question is added whose target file contributes a
  `records` document.
- **AC9** — When `govkit` applies the memory-recall kit to a scratch target, the new fixture is NOT
  written there, `tools/memory-recall/kit.toml` names it `project-owned` beside the existing three,
  and `WIRE-INTO-PROJECT.md`'s removal line names it.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `recall floor`, `memory hygiene` and `kit version markers`
the legs that bind. The kit's own self-test suite is `subject = kit` and is held by default, so
exercising the `selftest.py` arm AC8 requires — which is S5's arm, not S6's; S6 is a report and has no
arm — needs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and the record must say it was run
that way.

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
- rev-3 · 2026-09-05 · round-1 spec audit folded, findings B1, H3, M1, M2, M3 and M7. B1 was the
  set's hardest: `expected_paths` resolves by whole-FILE equality (`bench.py` `:362`-`:365`) and a
  record-level document carries its enclosing file's path (`extract.py` `:499`), so on an ANCHORED
  file the `records` set satisfies a path target by returning the record — the exact case §4 argued
  was impossible — and AC2 ("the chunks ceiling is 1.00") was true of every file and could not fail.
  The fix narrows the POPULATION rather than inventing an expectation vocabulary: S1 now admits only
  files carrying NO anchored record, which contribute zero `records` documents by construction, so
  the target is structurally unsatisfiable from that set. Measured for this fold: 1279 of 1324
  tracked memory `.md` files qualify, and they include every long document in the tree, the ten
  largest running 71 KB to 205 KB — so the restriction costs nothing and lands the unit on exactly
  the documents a passage question is worth asking about. S2b adds the empirical filter that makes
  AC1 true by construction rather than by ranking luck, and AC2 and AC3 now observe the property
  (zero `records` ceiling against a 1.00 `chunks` ceiling) instead of asserting it. H3 — the new
  fixture would have shipped to every adopter through the kit's `include = "**" role = "engine"`
  rule, carrying this repo's own query log and record ids; S5d withholds it and AC9 observes the
  apply. M3 — the set inherited neither the committed fixture's provenance rule nor its
  anti-tautology audit, and nothing on the bar would have audited it anyway because `--audit-fixture`
  defaults to one constant; S5b records the weaker provenance honestly, S5c makes the audit iterate
  every fixture, AC7 observes both. That one matters most downstream: `TOOL-aTunedCompass-3` is to
  pin the merge bar against this population. M1 — §6 relabelled `- **ACn** — `, since this spec's own
  resolutions cite AC1, AC4 and AC5 and check 23 reds at CLOSED. M2 — §7 pointed at S6's "arm" when
  S6 is a report; it now names the `selftest.py` arm AC8 actually requires. M7 — §5 restored to the
  full ten labelled lines, which surfaced the distribution risk H3 found independently.

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

# TOOL-aTunedCompass-2 — the recall fixture carries the terms every real query supplies

**Status:** BLOCKED · rev-4 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 2 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |

<!-- /gen:spec-records -->

## 1. Goal

Make the graded question set send the query shape a session actually sends, so every recall figure
this repo publishes is measured on it. `tools/memory-recall/recall-fixture.json` carries twelve
questions and no terms, while `tools/memory-recall/query.py` refuses a query without `--terms` and
all 148 queries in the live log supplied them at a mean of 12.8.

## 2. Scope (IN)

- **S1** — every fixture question gains a `terms` array of single words, 8 to 14 of them, the band
  `tools/memory-recall/query.py` (`:21`) declares in its own usage string.
- **S2** — the fixture's `query` field becomes the composed graded string: the question, one space,
  then the terms space-joined, with no separator word. No separator, because `bench.terms` would
  tokenise one and add a junk term to every query in the set.
- **S3** — `check-recall.py --audit-fixture` asserts the composition. A question with no `terms`
  key, a `query` that does not end with those terms joined by single spaces, or a term count outside
  the declared band each REFUSE by name, in `read_fixture` (`tools/memory-recall/check-recall.py`
  `:94`) beside the refusals it already raises for an absent or question-less fixture.
- **S4** — `measure_overlap` (`tools/memory-recall/check-recall.py` `:213`) takes its denominator
  from the QUESTION half, which is `query` with the terms suffix stripped. `OVERLAP_MAX` keeps the
  meaning it has today and no ceiling is loosened to accommodate this change.
- **S5** — `check_audit` (`:244`) states what it does not check. The terms half is deliberately this
  corpus's jargon, so it is not graded for overlap; a ceiling on it would red the feature rather
  than a fault, and no ceiling derived from twelve hand-written term lists would be honest.
- **S6** — each question's `hits` field is re-derived from the measurement with terms, because the
  audit reds on a disagreement between the declared value and the measured one.
- **S7** — `h` and `R` are re-derived and the literal assertions in
  `tools/memory-recall/test_recall_floor.py` (`:306` and the three single-direction arms) are
  updated in the same commit. `RECALL_FLOOR` in `.memory-tree.conf` (`:286`) is NOT moved, per F1.
  What changes beside that key is its comment block alone, which today carries the measured `h`, `R`
  and worst case as literals and would otherwise describe a derivation the new fixture refutes. The
  restated block names the new figures, states that the held pin is now conservative by the
  difference, and points the re-derivation at the units that own it.
- **S8** — the fixture's `_README` gains the terms rule beside its provenance rule: what the terms
  are, the band, how they are authored, and that `query` is the composed string every instrument
  grades. `tools/memory-recall/README.md`'s recall-floor section gains one line naming that field.
- **S9** — three arms in `tools/memory-recall/test_recall_floor.py`, one per refusal in S3, each
  observed RED before the arm asserting it is written.
- **S10** — the kickoff manifest is re-stamped, because `.memory-tree.conf` sits on the `watch:`
  line of `memory/guides/SESSION-KICKOFF.md` and this unit edits it.
- **S11** — `KIT_MEMORY_RECALL_VERSION` in `tools/memory-recall/recall_conf.py` moves, and
  `memory/map/features/memory-recall.md` is refreshed. This unit edits three files that dossier
  claims as inventory keys, so the touch owes both the marker and the prose. The obligation is the
  one `TOOL-aTunedCompass-3`, `-4` and `-5` each carry for the same kit.

## 3. Non-goals (OUT)

- Not editing `tools/memory-recall/bench.py` or `tools/memory-recall/union.py`. See §4 for why the
  fork discipline forbids it.
- Not moving the pinned cell off `records:fts5`. Grading the two-set ensemble the CLI serves is
  `TOOL-aTunedCompass-3`, and it is sequenced after this unit for the reason the build README gives.
- Not switching the chunk substrate to `roll`. That is `TOOL-aTunedCompass-4`.
- Not adding, removing or rewriting questions. n stays 12. The fixture that can discriminate the
  chunk half is `TOOL-aTunedCompass-9`, which this unit is BLOCKED on, and whose backlog row is
  `TOOL-aWeighedCompass-18`.
- Not moving `RECALL_FLOOR`, and not re-deriving it. The floor is `TOOL-aTunedCompass-9`'s business
  first, because a pin derived against a fixture that saturates at records-alone is a pin derived
  from saturation, and then `TOOL-aTunedCompass-3`'s, which grades the ensemble the CLI actually
  serves and sets the pin against it. This unit hands both of them a fixture whose query shape is
  the served one and claims nothing about the floor.
- Not shipping the fixture to adopters. `tools/memory-recall/kit.toml` withholds it, the floor is a
  gov-only leg, and that stays true.
- Not re-measuring the parent's tables. This unit cites them and produces exactly the new numbers
  the re-derivation in S6 and S7 requires.

## 4. Design

### Data model

| Field | Read by | Meaning |
|---|---|---|
| `query` | `bench.rank_with`, `union.py` (`:114`), `check-recall.measure_run` | the graded string: question then terms |
| `terms` | `check-recall.check_audit` | the terms half, so the composition is assertable rather than eyeballed |
| `expected_ids` | `bench.expected_by_target` | unchanged |
| `from` | the provenance rule | unchanged |
| `hits` | `check-recall.check_audit` | re-derived, per S6 |

`terms` is not a second copy of anything. It is the half of `query` that a machine otherwise cannot
find, because a question with its terms appended is indistinguishable from a long question. S3's
suffix assertion is what keeps the two in agreement, so the duplication is closed by a check rather
than by trust.

### Why the fixture composes and not the harness

`bench.py` and `union.py` are **verbatim** upstream. `tools/memory-recall/README.md` (`:196`) says
they are re-pulled wholesale on any fix and never merged, `verbatim.json` pins their LF-normalised
digests, and `test_verbatim_files` (`tools/memory-recall/selftest.py` `:1156`) reds on an edit.
Teaching `bench.py` to compose a question and a terms list would convert a wholesale re-pull into a
three-way merge, which is the cost `tools/memory-recall/extract.py` (`:4`) documents at six
constructs for one forked file. Composing in the fixture costs zero edits to either verbatim file
and makes all three readers grade the same string.

The near-miss alternative is worse than it looks and is worth naming: a `terms` field that only
`check-recall.py` composes leaves `bench.main` grading the bare question. The gate and the tuning
instrument would then disagree about what was measured, which is the defect this unit exists to
remove, one level up.

### What the composed string is and is not

`query_expr` (`tools/memory-recall/query.py` `:622`) builds `match_expr(question)` OR one quoted
phrase per supplied term, plus a quoted phrase per id found in either. `bench.match_expr`
(`tools/memory-recall/bench.py` `:160`) ORs the de-duplicated tokens of whatever single string it is
given. For single-word terms those two produce the same OR of the same tokens, which is why S1 fixes
the terms to single words. They still differ in two places, stated rather than papered over: a
multi-word term stays one phrase in the CLI and becomes separate tokens here, and the CLI does not
de-duplicate a term that the question already contains while `match_expr` does. Neither difference
is reachable from a single-word term list, and the fixture is not the CLI.

### How the committed terms are authored

The terms this build measured with were written by an author who had just read the corpus, which
biases them optimistic and is why none of the parent's with-terms figures is treated here as a
target. The committed terms are pre-registered instead. They are written from the question text and
the symptom vocabulary alone, in one pass, without opening the target record, and committed BEFORE
any measurement run. The re-derived `hits`, `h`, `R` and pin land in a second commit that cites the
first. The ordering is visible in git, which is the only mechanical honesty available here; a
predicate cannot tell a term written from a question apart from one written from an answer.

Two residuals, because a bound that is not stated is not a bound. Nothing prevents a later edit from
tuning the terms after the fact. And n is 12, so every figure this fixture produces moves in steps
of roughly 0.08, which is one question.

### Files touched (estimate)

`tools/memory-recall/recall-fixture.json`, `tools/memory-recall/check-recall.py`,
`tools/memory-recall/test_recall_floor.py`, `tools/memory-recall/README.md`, `.memory-tree.conf`,
`tools/memory-recall/recall_conf.py` for the version marker,
`memory/map/features/memory-recall.md` for the dossier refresh, and the manifest stamp in
`memory/guides/SESSION-KICKOFF.md`. Eight files, one of them a stamp.

### Alternatives rejected

Editing `bench.py` to compose: rejected on the verbatim contract above.

Dropping the question and grading the terms alone: rejected. The CLI sends both, and the question
half is what the anti-tautology overlap audit grades.

Raising `OVERLAP_MAX` so the composed string fits under it: rejected. That loosens the guard against
a question copied out of its own record in order to admit terms that legitimately share the target's
vocabulary, which trades a real property for a bookkeeping convenience.

## 5. Production-readiness checklist

- security — N/A. The kit is offline and stdlib-only, and this unit reads and writes tracked files.
- perf / scale — the graded string grows by at most fourteen tokens per question, so the FTS5 match
  expression widens and the corpus does not. The `recall floor` leg's declared ceiling is 300 s and
  its cost is dominated by the `extract.py` run that builds the data dir, not by the match.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the three S3 conditions refuse at the precondition, by name, the
  way `read_fixture` already refuses an absent, unreadable or question-less fixture. None of them
  may fall through to a `KeyError` inside the scoring path, which is the failure mode that
  function's own comment records.
- observability — `--audit-fixture` prints the term count and the question-half overlap per
  question, so a reader can see which half moved.
- risks — moving `h` moves the DERIVATION under a pin this unit no longer touches, per F1. The
  residual is one-directional and is checked rather than assumed: the held `0.81` stays safe while
  the re-derived worst case sits above it, and AC5 is what observes that. Should the re-derivation
  come back BELOW the held value, this unit stops and reports rather than moving the pin, because
  moving it is what the owner blocked. The second risk is the authorship bias above, bounded by
  pre-registration and not removed by it.
- testing + left-shift gates — S9's three arms, each with its RED observed before the arm lands.
  The class being left-shifted is "the fixture grades a shape the CLI does not send", and after this
  unit that class fails a gate instead of being noticed by a research pass.
- migration / rollback — one commit, revertable. Nothing outside this repo reads the fixture.
- user docs — S8's two prose edits. The kit README is the shipped surface and gains one line.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-recall/check-recall.py --audit-fixture` runs on the committed
  fixture, it exits 0 and prints a term count per question, every count inside the declared band.
- **AC2** — When a question's `terms` key is removed and the audit re-run, it refuses naming that
  question's index, and the refusal is observed before the arm in `test_recall_floor.py` is written.
- **AC3** — When one term is deleted from a question's `query` string but left in its `terms` array,
  `--audit-fixture` reds naming the composition mismatch.
- **AC4** — When `python tools/memory-recall/bench.py` and `python
  tools/memory-recall/check-recall.py --data-dir` are run over the same extracted dir with the
  fixture at `--sets records --subs fts5 --ks 5`, the two report the same `records:fts5:r@5` figure.
- **AC5** — When `--audit-fixture` prints its derivation line, the `h` and `R` it reports equal the
  literals asserted in `tools/memory-recall/test_recall_floor.py`, and `RECALL_FLOOR` in
  `.memory-tree.conf` sits at or below the printed one-retirement worst case.
- **AC6** — When terms are appended to a single question and `--audit-fixture` is re-run, that
  question's `overlap` figure is unchanged, proving the denominator is the question half.
- **AC7** — When `python tools/memory-recall/selftest.py` runs, `test_verbatim_files` passes, so
  `bench.py` and `union.py` are byte-identical to their pinned digests.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs after the `.memory-tree.conf`
  edit, it exits 0 against the re-stamped `last-audit`.
- **AC9** — When `python tools/memory-recall/test_recall_floor.py` runs, every arm passes, including
  the three new refusal arms and the re-derived `h` and `R` literals.
- **AC10** — When the fixture's `_README` is read, it states the terms rule, the band, and that
  `query` is the composed string every instrument grades.

## 7. Gates

`recall floor` (`python3 tools/memory-recall/check-recall.py`) and `kickoff-manifest ratchet`
(`bash skills/session-kickoff/manifest-check.sh`) run on an ordinary bar and must stay green.
`recall floor arms` (`python3 tools/memory-recall/test_recall_floor.py`) and `memory-recall kit
selftest` (`python3 tools/memory-recall/selftest.py`) are both `chunk = selftests`, so they are held
off the ordinary bar and this unit's Definition of Done owes them under `GATE_SELFTESTS=1`, which is
what the charter requires of kit work. `kit version markers` and `codebase-map coverage + freshness`
cover S11's marker and dossier refresh. `memory hygiene` and `spec tokens (a spec's own names
resolve)` cover the records half. The full bar is `bash tools/run-gates/run-gates.sh`. This unit
adds no leg: the three new refusals are arms on legs that already exist.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): pin nothing, and block this unit on `TOOL-aTunedCompass-9`.** The owner
declined all three options this fork offered and took a fourth: no floor is derived from a fixture
that saturates at records-alone. `RECALL_FLOOR` therefore does not move here, and the terms work is
correct on its own and unchanged. What this unit no longer claims is any movement of the pin.

- **F1 — does `RECALL_FLOOR` move with the fixture?** With terms the parent measured `records:fts5`
  at a perfect recall@20 against 0.83 bare, so `h` at the pinned `r@5` cell is expected to rise and
  the current 0.81 becomes conservative. The pin's definition is the one-retirement worst case
  `(h-1)/(R-1)`, so a pin left where it is has stopped meaning what `tools/memory-recall/README.md`
  says it means.
  Options: re-derive the pin from the new `h` and `R`; hold 0.81 and let the arms carry the new
  figures; hold it and record the slack in the conf comment.
  Recommendation: re-derive, because a derived pin that is no longer derived is a number nobody can
  re-check. The counter-argument is real and belongs to the owner: on twelve questions a high pin
  reds on one question's churn as readily as on a retrieval regression, and this build's own rule is
  that a pin set here is a pin set on n=12.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · M2 cross-read. `TOOL-aTunedCompass-3`, `-4` and `-5` each state that a touch
  of the memory-recall kit owes the `recall_conf.py` version marker and the
  `memory/map/features/memory-recall.md` refresh. This spec edits three files that dossier claims
  and carried neither obligation, so it was the document that disagreed. S11, two entries in Files
  touched and two leg names added.
- rev-4 · 2026-09-05 · F1 resolved by the owner against all three offered options: pin nothing and block on
  the new `TOOL-aTunedCompass-9`. Status to BLOCKED, `RECALL_FLOOR` removed from scope, and the
  non-goals now name unit 9 as the blocker rather than a backlog row.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade the recall fixture on the query shape the CLI
actually serves"` returned the seam this unit extends: `read_fixture` in
`tools/memory-recall/check-recall.py` (`:94`), which already refuses an absent, unreadable,
question-less or malformed fixture by name, so S3's three refusals belong inside it rather than in a
new validator. The probe also returned `test_absent_fixture_reds`, `test_empty_fixture_reds` and
`test_tautological_fixture_reds` in `tools/memory-recall/test_recall_floor.py`, which are the arm
shape S9 copies, and the two `gate-legs` inventory keys `recall floor` and `recall floor arms`. The
second seam, found by reading rather than by the probe, is `measure_overlap` (`:213`): it already
resolves its target set from the run rather than re-implementing resolution, which is why S4 is a
change to one denominator and not to the audit's structure.

Recall terms used: `recall fixture bench verbatim upstream terms rewrite floor pin overlap tautology
chunks fts5 query`, against the question of why the fixture grades a bare question when the CLI
refuses a query without terms. It returned 40 hits; the binding ones are the open row recording this
defect, the parent's finding 3b, and the closing record of the build that derived the floor pin as
the one-retirement worst case.

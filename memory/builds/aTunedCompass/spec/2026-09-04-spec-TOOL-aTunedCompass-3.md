# TOOL-aTunedCompass-3 — the recall floor grades the two-set ensemble the CLI serves

**Status:** BLOCKED · rev-3 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |

<!-- /gen:spec-records -->

## 1. Goal

Make `tools/memory-recall/check-recall.py` grade the document sets `query.py` actually fuses,
instead of the one set it grades today. The leg is the only merge-bar check asking whether
orientation returns the right thing, and about 52.5 percent of the slots a session reads come from
a half it never scores.

## 2. Scope (IN)

- **S1** — the `RECALL_FLOOR` grammar takes an ENSEMBLE head: one or more `<set>:<substrate>` pairs
  joined by `+`, then the existing `:<metric>@<k>>=<value>` tail. A single-pair pin is a legal
  one-member ensemble, so the shipped `records:fts5:r@5>=0.81` and every adopter conf carrying that
  shape parse unchanged. A malformed head still REFUSES naming the offending set or substrate, which
  means the parser enumerates the pairs rather than reporting a bare "does not parse".
- **S2** — the set and substrate vocabularies come from `union.SETS` and `union.SUBS`, and
  `check-recall.py`'s own byte-identical copies of those two tuples are deleted. One vocabulary, one
  place, and the import is the first line of code in this repo that reads `union.py` at all.
- **S3** — precondition 3 applies to EVERY member set. A member absent from the data dir, or present
  and empty, refuses and names that member. Without it a member contributing nothing leaves the pin
  reading as satisfied, which is `memory/gotchas/vacuous-selector-empty-population.md` arriving
  through the gate written to close that class. The empty member is constructed with
  `build_filtered` in `tools/memory-recall/test_recall_floor.py` and never by naming `spine`:
  `TOOL-aTunedCompass-5` is ordered ahead of this unit and makes `spine` non-empty, so an arm
  resting on that emptiness would depend on a defect its own build has already fixed.
- **S4** — `measure_run` ranks each member pair with `bench.rank_with` at the pinned `k` and unions
  the covered TARGETS across members. A question scores a hit under metric `r` when at least one
  target is covered by any member, and under metric `f` when every target is. That is exactly what
  `union.py`'s `recall` and `full` columns mean, so the two readers agree by construction rather
  than by comment.
- **S5** — the per-id predicate resolves an expected id against the UNION of the member sets. An id
  is unresolved only when no member set can resolve it, so a record-level id stops being reported as
  missing merely because a chunk-level member cannot carry it.
- **S6** — the leg REPORTS `bytes_full` and `bytes_snippet` for the pinned ensemble, the second
  through `union.snippet_bytes`, and pins neither. The parked question of whether the chunk half
  earns its bytes needs that number on every run to become answerable; a floor over it would be a
  decoration, for the reason the `METRICS` comment in `check-recall.py` already records about `b`.
- **S7** — `--audit-fixture` resolves its overlap targets over the same union. The NOT MEASURED
  refusal for a question resolving no target anywhere survives unchanged, because a question that
  the ensemble cannot resolve is the one row that must never average in as a perfect 0.000.
- **S8** — the pin in `.memory-tree.conf` is re-derived against the ensemble and its comment block
  restated. The comment carries the ensemble, the measured cell value, the `(h-1)/(R-1)` headroom,
  and the fixture size the derivation rests on.
- **S9** — the docstring of `check-recall.py` states what the leg still does NOT check: the fused
  ORDER, because the ensemble scorer models the merged pool and not `rrf()`; and the emitted
  PREFIX, because `query.py` cuts the fused list at `DEFAULT_BUDGET` bytes and nothing here does.
- **S10** — arms in `tools/memory-recall/test_recall_floor.py` for the new refusals and for the
  ensemble scoring, each one observed RED before it is wired.

## 3. Non-goals (OUT)

- Not modelling `rrf()`. Fusion changes the ORDER of the merged pool and recall over that pool is
  order-independent, so reproducing the fusion buys no different verdict at the same `k`.
- Not modelling the byte budget. Grading what a session is actually EMITTED means grading a
  truncated prefix of the fused list, which needs the emission path rather than the ranking path.
  That is a separate unit and the follow-up is named in S9's docstring text.
- Not deciding whether the chunk half belongs in the served ensemble at all. The build README parks
  that on a discriminating fixture and an owner call, carried at `TOOL-aWeighedCompass-18`.
- Not changing what `query.py` serves. Unit `TOOL-aTunedCompass-4` owns the chunk source; this unit
  only grades whatever the CLI fuses.
- Not shipping a graded floor to adopters. `kit.toml` withholds the fixture, the program and the
  arms as `project-owned`, and an adopter's floor still has to be measured against their own corpus.
- Not adding a gate leg. `recall floor` already exists and already runs this program.

## 4. Design

### Why this depends on unit 2

The fixture carries terms on none of its twelve questions, while `query.py` REFUSES a query without
`--terms` and all 148 logged queries supplied them. So every figure available for setting an
ensemble pin today was taken on a query shape no session sends. `TOOL-aTunedCompass-2` puts the
terms in the fixture; setting this pin before that lands would pin the leg to the shape this build
exists to stop measuring against.

### The pin grammar

The head is validated pair by pair against `union.SETS` and `union.SUBS`, and the tail is unchanged.
`union.is_ensemble` answers the same question with a bool and is therefore not enough on its own,
because a refusal that cannot name the offending field is the one this program replaced during its
own build. The two grammars still cannot drift, because the vocabularies they read are now the same
two tuples.

### What the ensemble hit means

`bench.expected_by_target` already maps each expected target to the documents of ONE set that
satisfy it. The ensemble reuses it per member and takes the union of the covered targets. Nothing
new decides what a target is, and the record-level and chunk-level target resolutions that already
exist stay exactly as they are.

### The `ceiling` the earlier design could not express

`TOOL-aWalkedCorpus-3` rejected grading through `union.py` on the ground that it reports no
`ceiling` and takes one `k`. That objection is about `union.py` as a PROGRAM, not about the ensemble
semantics. Reading those semantics through `bench` primitives inside `check-recall.py` keeps the
`ceiling`, keeps the one-retirement derivation, and keeps every refusal naming its own field.

### Files touched (estimate)

`tools/memory-recall/check-recall.py`, `tools/memory-recall/test_recall_floor.py`,
`.memory-tree.conf`, `tools/memory-recall/README.md` for the adopter-facing pin example,
`memory/map/features/memory-recall.md` for the dossier claim that the graded ensemble is not the
served one, and `memory/guides/SESSION-KICKOFF.md` for the `last-audit` re-stamp that a
`.memory-tree.conf` edit owes. The kit version constant in `recall_conf.py` bumps with the body
change, in every carrier the govkit stamp check names.

### Alternatives rejected

- **Running `union.py --json` and reading the report.** The docstring of `check-recall.py` already
  argues this for `bench.py` and every word of it holds harder here: the report is aggregate-only,
  it rounds to four decimals, and it carries neither per-question data nor a `ceiling`, so neither
  the per-id predicate nor the headroom derivation is computable from it.
- **A pin key per set, `RECALL_FLOOR_RECORDS` beside `RECALL_FLOOR_CHUNKS`.** Floated in the
  aWalkedCorpus round-1 review. Two keys grade two configurations and neither of them is the served
  one, which is the whole defect being closed.
- **Pinning a byte ceiling.** A new comparison direction in the grammar, in the same unit that
  changes what is graded, for a decision the build README parks.
- **Grading the ensemble in a NEW program beside `check-recall.py`.** Two programs answering "does
  retrieval still work" is `memory/gotchas/two-answers-to-one-question.md`, and only one of them
  would be on the bar.

## 5. Production-readiness checklist

- security — N/A. The program reads tracked files and writes only inside `mkdtemp()`, unchanged.
- perf / scale — ranking runs once per member set instead of once, so the ranking half roughly
  doubles for a two-member pin. Extraction dominates the leg and is unchanged. The declared ceiling
  for the `recall floor` leg lives in `tools/gate-legs.json` and the build re-measures against it
  rather than assuming the doubling fits.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — an empty member set refuses per S3, and a `ceiling` of 0 still
  prints `not evaluated` rather than dividing by zero or skipping silently.
- observability — S6's byte columns are the new signal, and they are the number the parked
  chunk-fate decision needs on every run rather than once in a build report.
- risks — the real risk is a pin re-derived from a saturated fixture, which is F1 in §8 and is not
  this unit's to resolve. A secondary risk is a member set that silently contributes nothing, which
  S3 turns into a refusal.
- testing + left-shift gates — S10, with each arm's red observed before it is wired, per the
  charter's rule that a gate whose failing case was never seen is an assertion about nothing.
- migration / rollback — the grammar is a superset, so reverting the program leaves every existing
  conf parsing. Reverting an ensemble pin without reverting the program leaves a one-member pin,
  which is the current behaviour exactly.
- user docs — `tools/memory-recall/README.md` carries the pin example an adopter copies, and it must
  show both the single-pair and the ensemble forms.

## 6. Acceptance criteria

- **AC1** — When `.memory-tree.conf` declares `RECALL_FLOOR="records:fts5:r@5>=0.81"` and
  `python3 tools/memory-recall/check-recall.py` runs, the reported cell value and normalised score
  are identical to the values the same command prints at base `c4fcf5ad`.
- **AC2** — When the pin names an ensemble and the command runs, the `cell` line names every member
  pair, and the run reports one recall over the merged pool rather than one line per member.
- **AC3** — When the pin names an ensemble one of whose members was emptied by `build_filtered` in
  the arm's own data dir, `python3 tools/memory-recall/check-recall.py` REFUSES with exit 2, and the
  message names that member and the data dir. The refusal is observed before the arm asserting it is
  written. The emptied member is constructed, never `spine`, which `TOOL-aTunedCompass-5` has
  already filled by the time this unit is built.
- **AC4** — When the pin's head carries a pair whose substrate is not in `union.SUBS`, the run
  refuses naming that substrate, not the whole pin string.
- **AC5** — When `python3 tools/memory-recall/test_recall_floor.py` runs, it exits 0, and its
  single-direction arms still fire ALONE: the floor arm reds with the per-id predicate green, and
  the per-id arm reds with the floor green.
- **AC6** — When the leg runs, its output carries `bytes_full` and `bytes_snippet` for the pinned
  ensemble, and no code path compares either against a threshold.
- **AC7** — When `grep -n "SETS\|SUBS" tools/memory-recall/check-recall.py` is read, the two
  vocabularies resolve through `union`, and no local tuple restates them.
- **AC8** — When the docstring of `tools/memory-recall/check-recall.py` is read, it names the fused
  order and the emitted byte-budget prefix as things this leg does NOT check.
- **AC9** — When `python tools/memory-recall/selftest.py` runs it exits 0, and
  `tools/memory-recall/verbatim.json` still matches `union.py` and `bench.py` byte for byte, because
  this unit imports both and edits neither.
- **AC10** — When `bash skills/session-kickoff/manifest-check.sh` runs after the `.memory-tree.conf`
  edit, it is green, because the `last-audit` stamp was re-taken in the same unit.

## 7. Gates

`recall floor`, `recall floor arms`, `memory-recall kit selftest`, `memory-recall skill wiring`,
`govkit selfcheck`, `memory hygiene`, `kickoff-manifest ratchet`, and
`codebase-map coverage + freshness` because the dossier prose is refreshed on touch. The full bar is
`bash tools/run-gates/run-gates.sh`, and the kit self-tests need `GATE_SELFTESTS=1` because this is
kit work. No new leg is added.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): pin nothing until `TOOL-aTunedCompass-9` reports.** The owner rejected
both deriving at a smaller `k` and accepting a ceiling-hugging pin at `k=20`, taking the option this
fork itself called the honest alternative. That costs the build this unit for now, which the fork
text already priced, and it is why the status is BLOCKED rather than SPECCED.

**F2 REMAINS OPEN, deliberately.** It was not put to the owner with the others, because a unit that
cannot be built until unit 9 reports does not need its internal design settled today, and answering
it now would fix a `union.py` decision against a fixture that does not yet exist. It is resolved when
this unit unblocks.

- **F1 — what value should the ensemble pin carry, and on what evidence?** The floor's derivation is
  the one-retirement worst case `(h-1)/(R-1)` over the graded fixture, which is why the shipped
  `0.81` is not a taste judgment. The problem is the fixture: with terms at `k=20`, `records:fts5`
  alone already scores recall 1.000, so the ensemble scores 1.000 too and a pin derived from that
  run is a pin derived from saturation. Options: derive the pin at a SMALLER `k` where the records
  half still has headroom, so the number carries information; derive it at `k=20` and accept a
  ceiling-hugging pin that only a real regression can break; or block this unit on
  `TOOL-aWeighedCompass-18`'s discriminating fixture and pin nothing until it exists.
  Recommendation: the first. A pin at `r@5` keeps the derivation meaningful on the fixture that
  exists, and the fixture is 12 questions, so whatever is picked is stated with its n beside it per
  the build README's rule. Blocking is the honest alternative and costs this build its second unit.

- **F2 — does `union.py` stay unedited?** This unit imports its vocabularies and its snippet
  accounting but re-expresses its scoring loop against `bench` primitives, because the loop lives
  inside `main()` and is not importable. That leaves the ensemble semantics stated in two places,
  which is the class `memory/gotchas/second-implementation-is-not-a-second-opinion.md` names.
  Options: leave `union.py` untouched and accept the second expression, keeping `verbatim.json`
  intact; extract the loop into a function in `union.py`, import it, and re-stamp the digest, which
  declares a fork of a file the kit currently re-pulls wholesale from upstream; or move the loop
  into `check-recall.py` and leave `union.py` as the exploratory harness it is today.
  Recommendation: the first, because `verbatim.json` exists precisely so an edit here is a decision
  somebody made out loud rather than a drift, and this is a ten-line loop over a shared
  `expected_by_target`. The owner may reasonably prefer the second, and this is the turn to say so.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · M2 cross-read, ordering axis. S3 and AC3 both used `spine`'s emptiness as the
  demonstration of the empty-member refusal, while `TOOL-aTunedCompass-5` is ordered ahead of this
  unit and exists to make `spine` non-empty — that spec's own S5 removes the identical dependence
  from `test_recall_floor.py`. This spec was the document that disagreed; both now construct the
  empty member with `build_filtered`.
- rev-3 · 2026-09-05 · F1 resolved by the owner: pin nothing, block on `TOOL-aTunedCompass-9`. Status to
  BLOCKED. F2 left open on purpose and now says so, so a later reader does not read it as missed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade the two-set ensemble the recall CLI serves against
a pinned floor"` returned `is_ensemble` in `tools/memory-recall/union.py` and the `check-recall.py`
affordance seam of the `memory-recall` dossier, which are the two seams this unit extends. The probe
also returned `parse_floors` in `tools/memory-tree/check-arms.py` on a name stem, and that one is a
different thing: it parses gate-arm floors, not retrieval pins. The seam is confirmed by reading:
`check-recall.py` already imports `bench.load`, `bench.build_index`, `bench.expected_by_target`,
`bench.rank_with` and `bench.score`, so the ensemble is a union over calls it already makes, and
`union.py` (`:41`) holds the two vocabularies it currently duplicates.

Recall terms used: `RECALL_FLOOR check-recall union.py ensemble records chunks fts5 reciprocal rank
fusion pin floor merge-bar`. The question was why the recall floor grades one document set when the
CLI fuses two. It returned 39 hits, and the ones that bind are the open row recording that the only
ensemble scorer is run by nothing, the earlier floor spec's rejection of grading through `union.py`
on the ground that it reports no ceiling, and the conf comment deriving the shipped pin.

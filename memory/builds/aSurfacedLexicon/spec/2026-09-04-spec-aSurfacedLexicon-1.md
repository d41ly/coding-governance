# TOOL-aSurfacedLexicon-1 — the design pass: measure the kit, then design and judge its rebuild

**Status:** CLOSED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 0 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aSurfacedLexicon-1-convention-predicate-probe.md](../build/2026-09-04-build-TOOL-aSurfacedLexicon-1-convention-predicate-probe.md) | research | — |
| [2026-09-04-build-TOOL-aSurfacedLexicon-1-owner-rulings.md](../build/2026-09-04-build-TOOL-aSurfacedLexicon-1-owner-rulings.md) | journal | — |
| [2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md](../build/2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Establish by measurement what the shipped lexicon kit does against its five stated goals, then design
the rebuild and put its forks to the owner. This is the Tier-2 Definition-of-Ready design pass for
the whole build, written after the fact because the renumber that resolved this build's id collision
left three records citing an id no spec defined.

## 2. Scope (IN)

- **S1** — Measure the shipped kit: which predicates exist, what population each grades, which are
  structurally incapable of firing, and what the three pins mean.
- **S2** — Determine the surface set G1 implies, and mark per surface whether a VOCABULARY constraint
  makes sense or only a CONVENTION one. A loop variable has a case convention and no useful verb.
- **S3** — Design the convention predicate that has never existed, and measure what the shipped
  idiomatic defaults would cost on this corpus.
- **S4** — Mine the ratified record so the rebuild neither re-litigates settled questions nor
  silently reverses a ruling, and report whether any in-repo record concludes the tool is better
  retired than maintained.
- **S5** — Determine what the rebuild owes the codebase map, the spec templates and the gate surface.
- **S6** — Produce competing designs, judge them adversarially, and synthesize one recommendation
  with a unit breakdown and the owner's open forks.
- **S7** — Observe the convention predicate RED on a staged break rather than asserting it, since a
  gate seen only to pass is an assertion about nothing.

## 3. Non-goals (OUT)

- Building any part of the rebuild. Every mechanism this pass designed is a later unit in this build,
  and the prototype written for S7 lives in the session scratchpad and lands nothing.
- Editing `.lexicon.conf`, any pin, or `tools/lexicon/`. This pass is read-only over the kit.
- Fixing the three `TOOL-aFlaggedScaffold` govkit defects that break the kit's install on a real
  adopter. Routing around them is this build's problem; fixing them belongs to that kit.
- Deciding whether the pressure chain is abandoned. Owner ruling Q8 settled which carrier states the
  arithmetic, not what the next reading will say.

## 4. Design

### Method

Five read-only measurement lenses over the kit, its record and its neighbours, then three competing
rebuild designs from deliberately different angles, then one adversarial judge per design, then one
synthesis. The lenses were bounded at five concurrent by `tools/hooks/agent-cap.js`, which refused two
earlier fan-out spellings before admitting the third.

The method rule that decided the output's worth: MEASURE, never estimate. The prior research pass on
this kit estimated one predicate's population at 484 and the kit's own extractor measured 6, so every
number here carries the command that produced it and every disagreement between a lens and the
synthesis is printed rather than resolved silently.

### Inventory

This unit mints no identifiers. Its artifacts are records, and the prototype it wrote is not tracked.

### Alternatives rejected

Reading the kit and writing a design without running it. Rejected because the defect this kit is
known for — a standard derived from the corpus it grades — is invisible to reading and obvious to
measurement, and because the one claim that reframed the build (the convention defaults cost zero
here) would have been a guess.

## 5. Production-readiness checklist

- security — N/A. Read-only research; no write path, no surface, no credential.
- perf / scale — N/A. The prototype grades 1394 tracked files in seconds.
- a11y — N/A. No user interface.
- i18n — the identifier splitter is ASCII-only, which truncates an accented name and skips a
  non-ASCII one with no report. Filed as `TOOL-aSurfacedLexicon-16` rather than fixed here.
- error / empty / loading states — N/A. No runtime.
- observability — the liveness assertion is the deliverable: every measured cell prints its
  population, and a predicate whose population is zero is a refusal rather than a pass.
- risks — the main one is a design that reads well and cannot be built. Mitigated by one adversarial
  judge per design, each required to name fatal flaws separately from weaknesses.
- testing + left-shift gates — the observed RED in S7. The predicate's own gate arrives with U5.
- migration / rollback — N/A. Records only; git holds every byte.
- user docs — N/A. No user-facing change.

## 6. Acceptance criteria

- **AC1** — When the five lenses complete, a record exists carrying a measured evidence table in
  which every number names its command or `file:line`. Observed: `2026-09-04-build-TOOL-aSurfacedLexicon-1-rebuild-research.md`.
- **AC2** — When the convention predicate's shipped defaults are run over this tree, the identifier
  cells report zero violations and the filename cells report the offenders, measured rather than
  asserted. Observed via `conv_probe.py`: 925 `py.function`, 39 `py.type`, 0 violations each.
- **AC3** — When one convention cell is re-graded against a convention it should fail, the count is
  non-zero, proving the predicate can fail. Observed: `py.function` as camel violates 691 of 925.
- **AC4** — When a deliberately bad name is staged into a tracked path, the predicate REDS naming it,
  and when unstaged the tree returns to its baseline. Observed with `git add tools/lexicon/_conv_break.py`.
- **AC5** — When the record corpus is searched for a conclusion that the tool is better retired than
  maintained, the answer is reported either way with its citation. Observed: none exists;
  `TOOL-dScaffoldedMirror-16` concludes the opposite.
- **AC6** — When the design pass ends, every open fork is put to the owner with a recommendation, and
  the rulings are recorded with their consequences. Observed: `2026-09-04-build-TOOL-aSurfacedLexicon-1-owner-rulings.md`.

## 7. Gates

- `memory hygiene` — this spec and the three records it defines.
- `build-index format` — the build README's slot budgets and its generated regions.
- `spec tokens` — this spec's own machine-facing citations resolve.
- No new gate leg. Every gate this build adds arrives with the unit that adds it.

## 8. Open questions

none — the ten forks this pass raised were put to the owner on 2026-09-04 and all ten resolved.
RESOLVED (owner, 2026-09-04): recorded individually in this build's owner-rulings record, four of
them against the recommendation.

## 9. Revision log

- rev-1 · 2026-09-04 · written after the pass it describes, and the reason is worth recording rather
  than hiding. The build's thirteen unit specs were first written as ids 1 through 13 while this
  design pass already held id 1 in three merged commits. Section 2's residual tie-break renumbered
  the unmerged specs to 2 through 14, which left this id cited by three records and defined by no
  spec — a state the hygiene gate's checks 14 and 21 both refuse. The collision had been MASKING
  that refusal, so resolving it surfaced a gap that was always there.

## 10. Reuse audit

- `python tools/codebase-map/reuse_lookup.py "measure a naming gate against its stated goals and
  design a rebuild"` returns no seam this unit extends: its ranked candidates are `read_gate_verdicts`
  and `resolve_measurer_currency` in `tools/govkit/govkit.py` and `read_object_state` in
  `tools/lexicon/lexicon.py`, all at fan-in 1, which is below the threshold of 3 that makes a seam.
  No existing seam fits, and correctly so — this unit ships no code and extends nothing. The
  prototype it wrote reuses `ast` and the kit's own extractor shape rather than any repo seam.
- Recall terms used: `python tools/memory-recall/query.py "what decides whether a naming gate's
  standard may be derived from the corpus it grades" --terms "lexicon canon mirror derived standard
  corpus allowlist scaffold frequency exogenous prescriptive verb table offender pin"` — which
  returned the `dScaffoldedMirror` research record and README plus the backlog rows for that build's
  units 1 and 8, and those are the records that bind this pass.

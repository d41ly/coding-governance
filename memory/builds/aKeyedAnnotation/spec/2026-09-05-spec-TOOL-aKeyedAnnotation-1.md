# TOOL-aKeyedAnnotation-1 — the annotation convention, written once, and the citation it repairs

**Status:** OPEN · rev-1 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |

<!-- /gen:spec-records -->

## 1. Goal

Write this repo's code-annotation convention down once, as a memory-tree guide the kit renders into
adopters, and demonstrate it by repairing the two source citations that resolve to no record.
Every later unit writes comments that must obey it, so it lands first.

## 2. Scope (IN)

- **S1** A new guide at `memory/guides/ANNOTATION-STYLE.md`, rendered by the memory-tree kit from a
  `ANNOTATION-STYLE.template.md` beside `BUILD-METHOD.template.md`, wired into
  `tools/memory-tree/adopt-memory-tree.sh` at the same seam that renders the build method.
- **S2** The guide carries exactly four things and nothing else: the MUST / MAY / MUST NOT list; the
  three dispositions under which a number is safe in a comment (frozen by its conditions, gated by a
  pin, pointed at its owner); the delete-the-id test; and the statement that annotation is voluntary,
  with the reason — the shipped-evidence oracle discriminates only because citation is sparse.
- **S3** The guide POINTS at what other files own and restates none of it: the id grammar belongs to
  the recall extractor, the charter owns the derived-count ban, and the design pass record owns the
  measurements. Each is named, none is copied.
- **S4** Repair both dangling citations — in `tools/unattended/lib-unattended.sh` and in
  `tools/unattended/unattended.test.sh` — by rewriting each block so its evidence is named in the
  comment and the id is a trailing pointer. Each block must read completely with its id deleted.
  The ids belong to another node's build and its records were never written, so this unit repairs
  the PROSE and files the missing records as a backlog row rather than inventing them.
- **S5** Delete the mechanism paragraphs that two gotcha records absorbed verbatim from call-site
  comments, leaving each record its class name, its frozen incident and its reach. The design pass
  names both records and establishes direction from git.
- **S6** Register the guide as a method carrier if and only if the kit's carrier registry demands it;
  read `tools/memory-tree/adopt-memory-tree.sh` for whether a second guide joins that population.

## 3. Non-goals (OUT)

- **No line in the charter template.** Measured at this base: it is 8 bytes under its gate ceiling,
  so even a one-line pointer needs a trim or an owner ceiling decision. §8 carries the fork; the unit
  ships without it and the guide is reachable from the kickoff manifest instead.
- **No annotation grammar, marker kind, or scanner.** The design pass refuses all three.
- **No sweep over the corpus rewriting comments to the new style.** The convention is forward-looking
  and the two named repairs are its demonstration, not the start of a pass.
- **No change to any consumer.** Units 2 to 4 own those.

## 4. Design

### Data model

The guide is prose. It has no schema, no parser and no gate, deliberately: a style convention that a
machine could grade would be a rule, and every rule this pass considered was refused on measurement.
What makes it stick is that it is short, rendered into adopters with the kit, and reachable from the
one document a session already loads.

### Rollout

The kit's adopter script renders the build-method guide from a template beside it. The annotation
guide rides that seam exactly: one template file, one render line, and whatever the carrier registry
requires. Nothing else in the kit changes.

### Alternatives rejected

Putting the convention in `memory/HYGIENE.md` was rejected: that file grades RECORDS, and a
code-comment convention filed under a record-hygiene gate reads as gated when it is not. Putting it
in the charter was rejected on the measured 8 bytes. Putting it in a gotcha record was rejected
because a gotcha is a bug class selected per-diff, and this is a writing convention that applies
everywhere.

## 5. Production-readiness checklist

- security — N/A: prose, no execution path.
- perf / scale — N/A: no runtime.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the render is observable by the kit's own adopter run; a missing render shows as an
  absent file, which the adopter script's existing conditional already tolerates.
- risks — the real risk is drift: the guide restating something the charter or the extractor owns.
  S3 is the control, and §6 asserts it by name.
- testing + left-shift gates — no new leg. The existing memory-hygiene and kit-version legs grade the
  files this unit touches; a new leg for a prose guide would be the structural-check-reads-as-semantic
  shape the charter warns about.
- migration / rollback — the guide is additive; deleting it restores the prior state exactly. The two
  record deletions are ordinary reverts.
- user docs — the guide IS the doc.

## 6. Acceptance criteria

- **AC1** When `bash tools/memory-tree/adopt-memory-tree.sh` is run against a scratch clone, the
  target tree holds a rendered `memory/guides/ANNOTATION-STYLE.md` whose bytes match the render of
  `ANNOTATION-STYLE.template.md`.
- **AC2** When `memory/guides/ANNOTATION-STYLE.md` is read, it carries all four of the MUST/MAY/MUST-NOT list, the three
  number dispositions, the delete-the-id test, and the voluntary-annotation statement with its
  reason — and nothing that duplicates the charter's derived-count ban beyond naming it.
- **AC3** When `python memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py`
  is run after this unit, each repaired block reads completely with its id removed, and the census
  reports no unresolvable id that was not present at this base.
- **AC4** When each repaired block in `tools/unattended/lib-unattended.sh` and
  `tools/unattended/unattended.test.sh` is read with its trailing id removed, its evidence is still named
  and the paragraph still states the incident it records.
- **AC5** When `python tools/memory-tree/gotchas.py --check` is run after the two record deletions it
  exits 0, and each edited record still carries its class name and its incident.
- **AC6** When `bash tools/run-gates/run-gates.sh` is run on this unit's commit it is green.

## 7. Gates

Existing legs that must stay green: the full bar. Load-bearing here — `memory hygiene`,
`kit versions`, `codebase-map coverage + freshness`, `drift-audit records`, and whichever legs
`tools/gate-legs.json` guards on `tools/memory-tree/`. Read the manifest for the names; none is
typed here. No new leg.

## 8. Open questions

- **F1 — the charter pointer.** The template is 8 bytes under its gate ceiling at this base, so a
  one-line pointer to the guide does not fit without a trim or a ceiling raise, and the manifest
  records that raising it is an owner decision rather than an edit. Options: (a) ship without a
  charter pointer and reach the guide from the kickoff manifest's §B, which is not byte-gated;
  (b) trim non-instructional prose elsewhere in the template to buy the line; (c) ask the owner to
  raise the ceiling. Recommendation: (a) now, and let a later unit that is already trimming the
  template carry the pointer for free.
- **F2 — carrier registration.** Whether a second rendered guide must join the kit's method-carrier
  registry is a fact the adopter script decides, not a judgement. FACT-QUESTION · read
  `tools/memory-tree/adopt-memory-tree.sh` at the carrier-registry block and follow what it demands.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` returned no seam for a comment-convention document — the ranked candidates were
id and index builders (`inventory_ids`, `build_reference_index`, `build_form_index`), none of which a
prose guide extends. The seam this unit actually rides is the adopter script's existing
`BUILD-METHOD.template.md` render line, found by reading `tools/memory-tree/adopt-memory-tree.sh`,
and it is extended rather than duplicated. No existing seam fits for the guide's CONTENT, which is
correct for a documentation-shaped unit.

Recall terms used: annotation comment docstring slug spec id orientation reuse-audit codebase-map
memory-recall marker keying.

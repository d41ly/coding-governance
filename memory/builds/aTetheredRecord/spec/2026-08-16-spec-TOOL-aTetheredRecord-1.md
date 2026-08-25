# TOOL-aTetheredRecord-1 — mint the five missing spec ids, and drain the orphan waiver

**Status:** CLOSED · rev-2 · 2026-08-20 · node a · Tier-1 · base 96141aed · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-17-review-TOOL-aTetheredRecord-1-1.md](../reviews/2026-08-17-review-TOOL-aTetheredRecord-1-1.md) | spec-audit | TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7 |

<!-- /gen:spec-records -->

## 1. Goal

Make the resolution target real before anything resolves against it. Five tracked spec files carry no
family-qualified H1 id, so the ids their builds are known by are cited across the corpus and defined
nowhere. Adding the H1 line mints each id, drains `memory/project/id-orphan-waiver.txt` to empty, and
lets `ORPHAN_ID_PIN` fall from 5 to 0.

## 2. Scope (IN)

- **S1** — Add an H1 line carrying the family-qualified id, followed by the file's existing title, to
  each of the five spec files below. The id for each is the one already cited for that build and
  already listed in the waiver:

  | Spec file | Id to mint |
  |---|---|
  | `memory/builds/aDeployScout/spec/governance-deployer-research.md` | `DEPL-aDeployScout-1` |
  | `memory/builds/aKitHardener/spec/2026-07-14-spec-aKitHardener-1.md` | `DEPL-aKitHardener-1` |
  | `memory/builds/aLeanRework/spec/template-v2-rework-spec.md` | `PLAY-aLeanRework-1` |
  | `memory/builds/aPortableWarden/spec/2026-07-13-spec-aPortableWarden-1.md` | `TOOL-aPortableWarden-1` |
  | `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md` | `KICK-aRatchetForge-1` |

- **S2** — Delete all five rows from `memory/project/id-orphan-waiver.txt`, leaving the header
  comment and no rows. Set `ORPHAN_ID_PIN="0"` in `.memory-tree.conf`, recording the drain in the
  comment above it as a measured fall from 5.
- **S3** — Re-run `python tools/memory-tree/gen_build_index.py --write` and stage the result.

## 3. Non-goals (OUT)

- **No content edit to the five specs beyond the H1 line.** Four of them predate
  `SPEC_FORMAT_CUTOFF` and are grandfathered by filename date; retrofitting them to the current spec
  format is explicitly not this unit and is not queued by it. `memory/TEMPLATE-SPEC.md` says never
  retrofit a grandfathered spec, and minting an H1 is not a format retrofit.
- **No change to `memory/project/legacy-files.txt`.** Three of the five keep historical filenames and
  stay exempt from the recording-name check; this unit changes what is INSIDE them, not their names.
- **No new status header.** These specs stay unparseable to the build index, which is why their
  builds carry an authored `status:` key. Adding a status header would change three build READMEs'
  derived state and belongs to whoever decides those builds' current standing.

## 4. Design

### Data model

An id becomes DEFINED when a corpus line anchors it. `tools/memory-tree/corpus_ids.py:195` compiles
an H1 pattern — a level-one heading whose first token is an id, optionally wrapped in backticks or
asterisks — and `:215-220` records a match as a definition keyed to that file and its build folder.
Adding the heading is therefore the whole mechanism; nothing else needs to change for the id to
resolve.

The five ids are not chosen. Each is already the id its build is cited by, and each already sits in
the waiver as a row whose stated exit condition is "when its build gains a conforming spec".

### Migration

The waiver's header comment says "The four below", while the file carries five rows — a stale count
from when the fifth was added for `aPortableWarden`. The comment is deleted with the rows rather than
corrected, because the file's working state after this unit is empty.

`ORPHAN_ID_PIN` is shrink-only with a stale-entry guard: a waived id that now resolves reds. All five
resolve after S1, so the pin MUST move to 0 in the same commit — leaving it at 5 with an empty
registry reds on the stale-row arm, and this is the one ordering constraint in the unit.

### Files touched (estimate)

Five spec files (one line each), `memory/project/id-orphan-waiver.txt`, `.memory-tree.conf`, and
whatever `--write` re-renders. The re-render is expected to be a no-op on build READMEs: the ids move
from cited-only to defined, and the roster derivation already counted them.

### Alternatives rejected

**Waive them permanently.** The waiver is shrink-only by design and its rows carry an exit condition
that this unit satisfies for one line each. A permanent waiver would keep five ids unresolvable
forever and would make the check-14 resolution that unit 4 depends on unreliable for those builds.

## 5. Production-readiness checklist

- security — N/A, no executable surface changes.
- perf / scale — N/A, five lines.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the waiver's empty state is its working state, already documented
  in `memory/HYGIENE.md`; no consumer distinguishes absent from empty for this file.
- observability — `python tools/memory-tree/corpus_ids.py --measure` reports the live orphan count.
- risks — one ordering constraint (pin and rows move together). No data loss, no rollback hazard;
  reverting is a revert of one commit.
- testing + left-shift gates — the existing check-14 arms cover both directions already.
- migration / rollback — single commit, revertible.
- user docs — the waiver header comment is deleted, not rewritten.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/corpus_ids.py --check` runs with `ORPHAN_ID_PIN="0"` and
  an empty `memory/project/id-orphan-waiver.txt`, it exits 0.
- **AC2** — When a first-match H1 id scan runs over `git ls-files 'memory/builds/*/spec/*'`, all five
  minted ids appear, and the count of distinct ids is exactly five higher than the same scan on the
  parent commit. The assertion is RELATIVE on purpose: an absolute figure here was wrong within the
  hour, because this build's own seven specs moved the number the same day it was written.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --check` runs after S3, it is clean,
  and `git diff --stat` over the build READMEs shows no change — the citations moved, the rosters
  did not.
- **AC4** — When `bash tools/run-gates.sh` runs on the resulting tree, every leg is green.

## 7. Gates

`memory hygiene (20 checks)` — checks 13 and 14 in particular · `bash tools/run-gates.sh` at the push
boundary. No new gate; this unit moves a pin that an existing gate already reads in both directions.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, authored in the design pass this build opened with.
- rev-2 · 2026-08-17 · AC2 made RELATIVE during the build. It asserted an absolute count of 118,
  derived as a measured 113 plus five; the live scan read 125, because the baseline predated this
  build's own seven specs. The criterion, not the tree, was wrong.

## 10. Reuse audit

The seam is `tools/memory-tree/corpus_ids.py`'s existing definition scan — the H1 anchor at `:195`
and the definition record at `:215-220`. Nothing is added to it; this unit supplies input it already
reads. A `python tools/codebase-map/reuse_lookup.py "bind a build artifact to the spec id that
warranted it"` pass returned `row_grammar.id_pattern` and `corpus_ids` as the id-shaped seams, and
`corpus_ids` is the one that owns definition-versus-citation. Recall terms used for the set:
`build slug spec artifact filename header adversarial review closeout journal bookkeeping convergence
naming hygiene`.

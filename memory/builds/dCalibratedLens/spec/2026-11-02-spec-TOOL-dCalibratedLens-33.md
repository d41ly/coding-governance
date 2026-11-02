# TOOL-dCalibratedLens-33 — the three Loop Review homes observed disjoint by listing each home, never inferred from the record-kind check

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 4 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-33-deviation-331.md](../build/2026-11-02-build-TOOL-dCalibratedLens-33-deviation-331.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2, HIGH, of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). The report merges ids 2, 11 and
26 into its item H1; ids 11 and 26 are `TOOL-dCalibratedLens-34` and `TOOL-dCalibratedLens-32`. Unit
19 S1 claims the three id-rule globs match disjoint file sets, and its `three-homes` arm reads as the
coverage of that claim. The arm only runs `record_kinds.py --check`, which grades by Serves kind
(TOOL-dTotalRecall-42 S5) and is green whether the homes overlap or not, so the claim is observed by
nothing. This unit observes the claim itself: it lists what each home matches and reds a path two
homes list. It repairs `TOOL-dCalibratedLens-19`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 19's text (rev-2, id 2): S1's
  disjointness sentence names this unit's case as what observes it, and unit 19's `three-homes`
  check run is stated to observe the field grading only. Observed by AC1.
- **S2** — The case `disjoint-homes` of the `three-homes` plant in `tools/loop/loop_review.py`. In
  the plant's scratch worktree, with its planted records committed, it reads every
  `[[record-kind]]` row of the scratch `record-kinds.toml` with `tomllib`, keeps the rows whose
  `home` starts `memory/loop-review/`, and lists each such home with `git ls-files -- <home>`, the
  listing TOOL-dTotalRecall-1 uses for a home glob. It counts, per listed path, the homes listing it.
  The case holds when every planted path is listed exactly once; it prints `disjoint-homes — ok`,
  and otherwise one `disjoint-homes — FAIL · <path> · <n> homes` line per path listed 0 or 2 or more
  times. A failed `git ls-files` prints `disjoint-homes — unread · <why>` and fails the plant.
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Refusing two `fields` homes that match one path in `record_kinds.py`. TOOL-dTotalRecall-42 rejected
  that check in its own design, and this unit does not re-open an ancestor's ruling; the case grades
  this build's three rows only.
- The bare-folder red twin: `TOOL-dCalibratedLens-32`, id 26.
- A record graded by no row: `TOOL-dCalibratedLens-35`, id 1.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-19` — the `three-homes` plant, its scratch worktree and its committed records, which the case lists; without them there is no path to count

## 4. Design

### Evidence

- Unit 19 §4 Evidence: the id-rules `<date>-value-ledger-<key>.md`, `<date>-loop-review-<key>.md`
  and `<date>-keep-<key hash>[-<n>].md`, with keys held to forms that spell none of the three words.
- TOOL-dTotalRecall-1 lists a home glob with `git ls-files`: its §5 perf line,
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:297`, reads "one git
  ls-files per home glob". The case lists with the pathspec semantics the registry check uses.
- TOOL-dTotalRecall-42 §4 "Alternatives rejected": "deciding by the Serves kind needs no disjoint
  homes", which is why the check cannot observe disjointness.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `disjoint-homes` | case of the `three-homes` plant | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2

### Alternatives rejected

- **`fnmatch` over the planted names.** A second glob dialect beside git's pathspec; a name the two
  read differently would pass the case and overlap in the check.
- **Drop the disjointness claim from unit 19.** The review offers it. The disjoint globs are what
  keeps each home naming its own kind, the claim TOOL-dTotalRecall-42 S1 makes for the shape-run home;
  a claim worth stating is worth observing.

## 5. Production-readiness checklist

- security — reads only; one `git ls-files` per home under the scratch worktree.
- perf / scale — three listings per plant run.
- error / empty / loading states — a path no home lists is a FAIL line too, so an empty listing never
  reads as disjoint.
- observability — each failing path is named with its count.
- risks — a fourth kind under `loop-review/` joins the listing by its home prefix and is held to the
  same rule.
- testing — AC1 and AC2 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant three-homes` runs from the loop kit
  directory, it prints `disjoint-homes — ok`.
  Red when: a planted path is listed by two homes or by none.
  fixture: the snapshot and record writers are units 2 and 3's, built before this order.
- **AC2** — When the case runs with every `loop-review/` home of the scratch `record-kinds.toml`
  rewritten in place to `memory/loop-review/*.md`, it prints one FAIL line per planted path, each
  naming `<n> homes` with n the number of rows rewritten: 2 at this unit's order, 3 once unit 5
  lands the `keep` row.
  Red when: overlapping homes pass the case.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 · the `disjoint-homes` case, staged red by rewriting every `loop-review/` home to one overlapping glob · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 2 (HIGH, item H1, shared with ids 11 and 26) of
  the round-2 spec audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 19 amended at
  the disposal (its rev-2).

## 10. Reuse audit

The seam extended is unit 19's `three-homes` plant, and the listing is TOOL-dTotalRecall-1's own
`git ls-files` over a home glob, so the case and the registry check read one glob dialect. `python
tools/codebase-map/reuse_lookup.py "render an optional bracket group of a shape definition into an
emitted line"`, run once for this disposal's set, ranked name stems only; no existing seam counts
the homes listing a path, and `record_kinds.py` is absent at base. The recall probe returned
TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`

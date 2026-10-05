# TOOL-aEvidencedLens-13 — no diff-kind probe, lens or skeptic prompt moved from BASE through unit 6, observed once with the review key masked

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-13-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-13-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Shared invariant 2 says the diff kind's prompts do not move in this build. Each harness unit observes
it for its own step only, against the render at HEAD before its pass, and unit 6's AC7 compared
against "the render at the pass's base", which no document defined. The round-1 spec audit confirmed
finding 25 at HIGH: read as the header's base `028b5cac`, that comparison is red on a correct build,
because `TOOL-aEvidencedLens-1` moves `REVIEW_SHAPE` and so the review key every finder and skeptic
DURABILITY line carries, and a builder chasing the red may revert that move. This unit states the
rule the build was missing, that a comparison to BASE masks the review key and a per-pass one binds
to the pass-start render, and makes the one BASE comparison the build lacks: from BASE to the tree
after unit 6, every diff-kind probe, lens and skeptic prompt byte-identical with the key masked, and
red when it is not. It closes finding 25 (HIGH) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — THE RULE. In this build, a criterion comparing a render of
  `tools/workflows/tier2-review.js` against an earlier one names its fixture as either the
  PASS-START render, the `git show` of that file at HEAD before the pass's first edit, compared
  unmasked; or the BASE render, the `git show` of that file at BASE `028b5cac`, compared with
  each run's own `result.key` masked as one fixed token in its prompts. "The pass's base" means
  the pass-start render wherever a build brief of this build spells it. `TOOL-aEvidencedLens-6`
  AC7 already reads as the pass-start form after that unit's rev-2. Observed by AC1 and AC2.
- **S2** — THE CUMULATIVE OBSERVATION. After `TOOL-aEvidencedLens-6` lands, a stub run of the
  BASE render and one of the render at this pass's HEAD, over the same diff-kind args, once at round
  1 with `checklist` and `specs` and once at round 2 with `priorFindings`, produce byte-identical
  `resume:probe`, `find:` and `verify:` prompts once each run's key is masked. `synth` is excluded
  by design: `TOOL-aEvidencedLens-6` S8 adds the per-lens block to it on both kinds. Observed by AC1.
- **S3** — LIVENESS. The same pair compared UNMASKED differs, and only on the key; and a copy of
  the HEAD render with one diff lens brief edited by one word reds the masked comparison. Without
  both, a green comparison cannot be told from one that compares nothing. Observed by AC2 and AC3.
- **S4** — The figures, the args and the two renders' blob ids are written to this unit's
  acceptance ledger in the build folder, so the observation is a record and not a transcript.
  Observed by AC4.

## 3. Non-goals (OUT)

- Any change to `tools/workflows/tier2-review.template.js` or its render. This unit observes; a red
  here is a defect in the unit that moved the prompt, fixed there.
- A standing suite arm. A self-test cannot reach a sha of this repository's history from an
  adopter's copy, so a BASE comparison is a build-time observation, not a gate.
- The spec kind. Units 1 to 4 and 12 move the spec kind's prompts by design.
- Editing the build briefs under `prompts/`. They are records; S1 says how their phrase reads, and
  each brief already says its spec wins where the two disagree.
- Comparing renders of units ordered after this one. None of them edits the review harness.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-6` — the landed per-lens yield, the last harness unit
  ordered before this one; without it the HEAD render is not the tree the build ships.
- **consumes-from** `TOOL-aEvidencedLens-1` — the `REVIEW_SHAPE` move that makes the unmasked BASE
  comparison differ; S3's liveness half rests on it.

## 4. Design

### Evidence

Read at `b3950dc7` on 2026-10-05, whose `tools/` tree equals BASE `028b5cac`:
`git diff --stat 028b5cac b3950dc7 -- tools/` prints nothing.

- `REVIEW_SHAPE = 'lenses5-r1'` joins `inputPrint`, which joins the review key, and the key is
  interpolated into every finder's DURABILITY line and every skeptic's, on both kinds
  (`TOOL-aEvidencedLens-1` §4 Evidence). An unmasked BASE comparison therefore differs on a correct
  build, which is finding 25.
- `TOOL-aEvidencedLens-1` AC5 already masks the key against its own pass-start render, and units 2,
  3 and 4 compare unmasked against theirs; this unit's mask is that AC5's, applied to BASE.
- The build briefs of units 1, 2, 3, 4 and 6 each say the pass "diffs the diff-kind finder and
  skeptic prompts against a render taken at the pass's base", and each says its spec wins.

### The masked comparison

```text
for render in (BASE, HEAD):
  for args in (diff round 1 + checklist + specs, diff round 2 + priorFindings):
    run stub -> prompts{label: text}, key
    prompts = { label: text.split(key).join('<KEY>') }
compare BASE vs HEAD over labels resume:probe, find:*, verify:*  -> byte-identical
liveness: unmasked compare differs, and only where <KEY> sat; a one-word brief edit reds the masked compare
```

### Files touched (estimate)

None under `tools/`. The pass writes its acceptance ledger in the build folder and nothing else; the
stub driver and both renders live in the run's scratch directory.

### Alternatives rejected

- **A lint refusing an unbound `<base>` in an acceptance criterion.** Run over the tree,
  `grep -rlF '<base>' memory/builds/*/spec/` hit 35 files, most of them a legitimate `<base>..HEAD`
  range in prose or a command; the predicate cannot tell a fixture from a range without reading
  intent, and it would red specs nobody is changing.
- **Leaving the BASE comparison out and relying on the per-pass ones.** A chain of per-pass
  comparisons misses a move made between passes, by a fold commit or a merge, and none of them
  states how a BASE comparison must be read, which is the defect.

## 5. Production-readiness checklist

- security — N/A: no code and no write outside the build folder's ledger.
- perf / scale — four stub runs of a harness render, seconds each.
- error / empty / loading states — a stub run that throws reds the observation and is reported
  with its message; an empty label set is refused by the liveness half.
- observability — the ledger names both blobs, the args and every label compared.
- risks — a red here names a unit already landed; the main loop routes it to that unit.
- testing — the observation is the test; S3 is its liveness.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

`u13-check.js` lives in the run's scratch directory, outside the tree. It is the `runReview`
AsyncFunction driver shape of `tools/workflows/tier2-review.test.sh` with recording stubs, plus the
masking step of §4; it is not the suite and runs in seconds.

- **AC1** — When `node u13-check.js --mask base.js tools/workflows/tier2-review.js` runs the two
  diff-kind arg sets, where `base.js` is the `git show` of `tools/workflows/tier2-review.js` at BASE
  `028b5cac`, every `resume:probe`, `find:` and `verify:` prompt is byte-identical between the two
  renders, and the driver prints the number of labels compared, at least the five `find:` labels
  of each arg set.
  Red when: a diff-kind probe, lens or skeptic prompt moved anywhere from BASE through unit 6.
  fixture: `base.js` is saved to the scratchpad from the object database, never from a working copy.
- **AC2** — When the same driver runs without `--mask`, the comparison differs, and every differing
  byte range lies where the masked run wrote `<KEY>`.
  Red when: the unmasked comparison is green, which means the key did not move and `TOOL-aEvidencedLens-1`
  S3 did not land, or a difference lies outside the key.
- **AC3** — When `node u13-check.js --mask base.js broken.js` runs, where `broken.js` is a scratch copy
  of the HEAD render with one word of the first diff lens brief changed, the masked comparison is red
  and names that lens's `find:` label.
  Red when: the masked comparison stays green on a staged break, so it compares nothing.
- **AC4** — When the pass's acceptance ledger in `memory/builds/aEvidencedLens/` is read, it names the
  two blob ids of `tools/workflows/tier2-review.js`, at BASE `028b5cac` and at the pass's HEAD, each
  read with `git rev-parse`, the label count of AC1, and the outcome of AC2 and AC3.
  Red when: the observation lives only in the transcript.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy (§3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, promoted from the round-1 spec audit's finding 25 (HIGH),
  repairing `TOOL-aEvidencedLens-6`.

## 10. Reuse audit

The seam reused is the masked prompt comparison `TOOL-aEvidencedLens-1` AC5 specifies, and the
`runReview` stub shape of `tools/workflows/tier2-review.test.sh`, both applied to BASE instead of to
a pass-start render. No tool is built.
`python tools/codebase-map/reuse_lookup.py "compare prompts of two harness renders with the review key masked"`
returned name-stem neighbours only (`key`, `render_inventories_json`, `render_map_md`) and printed
`unscanned layers: .sh`; none compares prompts. The recall probe returned `TOOL-aSightedSkeptic-5`,
which replaced a lens set under one review-shape bump, and this build's own unit 1, 3 and 6 specs,
whose pass-start fixtures are the per-pass half of S1; no record had stated how a BASE comparison is
read after a shape bump.

Recall terms used: invariant diff-kind prompts byte-identical render pass-start BASE REVIEW_SHAPE review key DURABILITY mask tier2-review

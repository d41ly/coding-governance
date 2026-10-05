# TOOL-aEvidencedLens-13 — no diff-kind lens or skeptic prompt moved from BASE through unit 12, observed once with the review key masked

**Status:** CLOSED · rev-2 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-aEvidencedLens-13-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-aEvidencedLens-13-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-13-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-13-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-closing-diff-review-round1.md) | diff-review | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-14 TOOL-aEvidencedLens-15 TOOL-aEvidencedLens-16 TOOL-aEvidencedLens-17 TOOL-aEvidencedLens-18 TOOL-aEvidencedLens-19 TOOL-aEvidencedLens-20 |
| [2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-12 TOOL-aEvidencedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Shared invariant 2 says the diff kind's prompts do not move in this build. Each harness unit observes
it for its own step only, against the render at HEAD before its pass, and unit 6's AC7 compared
against "the render at the pass's base", which no document defined. The round-1 spec audit confirmed
finding 25 at HIGH: read as the header's base `028b5cac`, that comparison is red on a correct build,
because `TOOL-aEvidencedLens-1` moves `REVIEW_SHAPE` and so the review key every finder and skeptic
DURABILITY line carries, and a builder chasing the red may revert that move. This unit states the
rule the build was missing, that a comparison to BASE masks the review key and a per-pass one binds
to the pass-start render, and makes the BASE comparison the build lacks for the lens and skeptic
prompts: from BASE to the tree after unit 12, the last unit that edits the review harness, every
diff-kind `find:` and `verify:` prompt byte-identical with the key masked, and red when it is not.
The `resume:probe` half is `TOOL-aEvidencedLens-15`'s, because that prompt spells the key as a
template rather than carrying it whole. It closes finding 25 (HIGH) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — THE RULE. In this build, a criterion comparing a render of
  `tools/workflows/tier2-review.js` against an earlier one names its fixture as either the
  PASS-START render, the `git show` of that file at HEAD before the pass's first edit, compared
  unmasked; or the BASE render, the `git show` of that file at BASE `028b5cac`, compared with
  every value derived from `REVIEW_SHAPE` masked as one fixed token in its prompts. In a prompt
  that carries each run's own `result.key` whole, as every `find:` and `verify:` prompt does, that
  value is the key; the diff-kind `resume:probe` carries `inputPrint` and not the key, and its mask
  is `TOOL-aEvidencedLens-15`'s. The phrase "a render taken at the pass's base", in the build briefs
  of units 1, 2, 3, 4 and 6, means the pass-start render. "Against the pass's base" in a brief's
  refusal-observation line keeps meaning the pass-start HEAD of the file under change.
  `TOOL-aEvidencedLens-6` AC7 already reads as the pass-start form after that unit's rev-2. Observed
  by AC1 and AC2.
- **S2** — THE CUMULATIVE OBSERVATION. After `TOOL-aEvidencedLens-12` lands, the last unit of this
  build that edits the review harness, a stub run of the BASE render and one of the render at this
  pass's HEAD, over the same diff-kind args, once at round 1 with `checklist` and `specs` and once at
  round 2 with `priorFindings`, produce the same SET of `find:` and `verify:` labels per arg set, and
  byte-identical prompts under each label once each run's key is masked. A label present on one side
  only is red by name. `resume:probe` is compared by `TOOL-aEvidencedLens-15`, not here. `synth` is
  excluded by design: `TOOL-aEvidencedLens-6` S8 adds the per-lens block to it on both kinds.
  Observed by AC1.
- **S3** — LIVENESS. The same pair compared UNMASKED differs, and only on the key; and a copy of
  the HEAD render with one diff lens brief edited by one word reds the masked comparison. Without
  both, a green comparison cannot be told from one that compares nothing. Observed by AC2 and AC3.
- **S4** — The figures, the args and the two renders' blob ids are written to this unit's
  acceptance ledger,
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-13-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-13` and an `**Evidences:** TOOL-aEvidencedLens-13`
  block, so the observation is a record that hygiene check 23 reads and not a transcript. Observed by
  AC4.

## 3. Non-goals (OUT)

- Any change to `tools/workflows/tier2-review.template.js` or its render. This unit observes; a red
  here is a defect in the unit that moved the prompt, fixed there.
- A standing suite arm. A self-test cannot reach a sha of this repository's history from an
  adopter's copy, so a BASE comparison is a build-time observation, not a gate.
- The spec kind. Units 1 to 4 and 12 move the spec kind's prompts by design.
- The diff-kind `resume:probe` prompt. It spells the key as
  `<kind>-r<round>-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-<inputPrint>`,
  so a key mask leaves `inputPrint` standing in it; `TOOL-aEvidencedLens-15` compares it under the
  mask of the whole class.
- Editing the build briefs under `prompts/`. They are records; S1 says how their phrase reads, and
  each brief already says its spec wins where the two disagree.
- A harness edit made after this unit. No unit ordered after this one edits the review harness:
  `TOOL-aEvidencedLens-11`, which shares this order, writes documents only, and
  `TOOL-aEvidencedLens-15` observes. A fold commit or merge that moves a diff-kind prompt after this
  pass is caught by no BASE comparison; the closing diff review reads it.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-6` — the landed per-lens yield; without it the HEAD render
  is not the tree the build ships.
- **consumes-from** `TOOL-aEvidencedLens-12` — the last unit of this build that edits the review
  harness, ordered before this one so the observation covers the harness the build ships.
- **consumes-from** `TOOL-aEvidencedLens-1` — the `REVIEW_SHAPE` move that makes the unmasked BASE
  comparison differ; S3's liveness half rests on it.
- **hands-off** `TOOL-aEvidencedLens-15` — the BASE comparison of the diff-kind `resume:probe`
  prompt, which carries `inputPrint` and not the key, so this unit's key mask cannot reach it (the spec
  audit of units 12 to 14, ids 1, 5 and 14, HIGH).

## 4. Design

### Evidence

Read at `b3950dc7` on 2026-10-05, whose `tools/` tree equals BASE `028b5cac`:
`git diff --stat 028b5cac b3950dc7 -- tools/` prints nothing.

- `REVIEW_SHAPE = 'lenses5-r1'` joins `inputPrint`, which joins the review key, and the key is
  interpolated into every finder's DURABILITY line and every skeptic's, on both kinds
  (`TOOL-aEvidencedLens-1` §4 Evidence). An unmasked BASE comparison therefore differs on a correct
  build, which is finding 25.
- `${inputPrint}` is interpolated in two places only (`tools/workflows/tier2-review.template.js:702`
  and `:720` at `14850417e`): `deriveReviewKey`, whose result every `find:` and `verify:` prompt
  carries whole, and the diff-kind `resume:probe`'s hand-spelled directory, which carries it alone.
  The `verify:` prompt's `batch` print hashes ids, claims and fixes and not `REVIEW_SHAPE` (`:1045`,
  BASE `:869`), so the key is the only shape-derived value in a `find:` or `verify:` prompt.
- `TOOL-aEvidencedLens-1` AC5 masks the key against its own pass-start render over `find:`,
  `verify:` and `synth`, and units 2, 3 and 4 compare unmasked against theirs; this unit's mask is
  that AC5's, applied to BASE, over the labels it covers.
- The build briefs of units 1, 2, 3, 4 and 6 each say the pass "diffs the diff-kind finder and
  skeptic prompts against a render taken at the pass's base", and each says its spec wins.

### The masked comparison

```text
for render in (BASE, HEAD):
  for args in (diff round 1 + checklist + specs, diff round 2 + priorFindings):
    run stub -> prompts{label: text}, key
    prompts = { label: text.split(key).join('<KEY>') for label in find:*, verify:* }
for args: labels(BASE) == labels(HEAD), else red naming each one-sided label; print both counts
compare BASE vs HEAD per shared label -> byte-identical
liveness: unmasked compare differs, and only where <KEY> sat; a one-word brief edit reds the masked compare
```

### Files touched (estimate)

None under `tools/`. The dispatch write set is the acceptance ledger of S4, the regenerated
`memory/builds/aEvidencedLens/README.md`, and this spec's own `gen:spec-records` region, both of
which move when a record serving this unit lands. The stub driver and both renders live in the run's
scratch directory.

### Alternatives rejected

- **A lint refusing an unbound `<base>` in an acceptance criterion.** Run over the tree,
  `grep -rlF '<base>' memory/builds/*/spec/` hit 35 files, most of them a legitimate `<base>..HEAD`
  range in prose or a command; the predicate cannot tell a fixture from a range without reading
  intent, and it would red specs nobody is changing.
- **Leaving the BASE comparison out and relying on the per-pass ones.** A chain of per-pass
  comparisons misses a move made between passes, by a fold commit or a merge, and none of them
  states how a BASE comparison must be read, which is the defect.
- **Keeping order 6 and naming unit 12 as covered by its own AC2 only.** Unit 12's AC2 compares to
  its predecessor, so a move between steps 6 and 7 would escape every comparison; ordering this unit
  after unit 12 covers it at the cost of one later step.

## 5. Production-readiness checklist

- security — N/A: no code and no write outside the build folder's ledger and its generated regions.
- perf / scale — four stub runs of a harness render, seconds each.
- error / empty / loading states — a stub run that throws reds the observation and is reported
  with its message; an empty label set is refused by the liveness half, and a one-sided label by S2.
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
  diff-kind arg sets after `TOOL-aEvidencedLens-12` has landed, where `base.js` is the `git show` of
  `tools/workflows/tier2-review.js` at BASE `028b5cac`, the two renders produce the same set of
  `find:` and `verify:` labels per arg set, every prompt under a shared label is byte-identical, and
  the driver prints each side's label count, at least the five `find:` labels of each arg set.
  Red when: a diff-kind lens or skeptic prompt moved anywhere from BASE through unit 12, or a label
  is present on one side only, which the driver names.
  fixture: `base.js` is saved to the scratchpad from the object database, never from a working copy.
- **AC2** — When the same driver runs without `--mask`, the comparison differs, and every differing
  byte range lies where the masked run wrote `<KEY>`.
  Red when: the unmasked comparison is green, which means the key did not move and `TOOL-aEvidencedLens-1`
  S3 did not land, or a difference lies outside the key.
- **AC3** — When `node u13-check.js --mask base.js broken.js` runs, where `broken.js` is a scratch copy
  of the HEAD render with one word of the first diff lens brief changed, the masked comparison is red
  and names that lens's `find:` label.
  Red when: the masked comparison stays green on a staged break, so it compares nothing.
- **AC4** — When `2026-10-05-build-TOOL-aEvidencedLens-13-1-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-13` and an
  `**Evidences:** TOOL-aEvidencedLens-13` block naming the two blob ids of
  `tools/workflows/tier2-review.js`, at BASE `028b5cac` and at the pass's HEAD, each read with
  `git rev-parse`, both label counts of AC1, and the outcome of AC2 and AC3.
  Red when: the observation lives only in the transcript, or in a file check 23 does not read.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy (§3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, promoted from the round-1 spec audit's finding 25 (HIGH),
  repairing `TOOL-aEvidencedLens-6`.
- rev-2 · 2026-10-05 · §1 §2 §3 §4 §6 §7 S1 S2 S4 AC1 AC4 · fold of the spec audit of units 12 to 14
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md`). Ids 4, 6 and 9 (MEDIUM):
  the non-goal "none of them edits the review harness" was false once unit 12 moved to order 7, so
  this unit moves from order 6 to 8, consumes from unit 12, and S2 and AC1 name unit 12 as the last
  harness unit observed. Id 17 (MEDIUM): S2, §4 and AC1 require the two renders' label sets equal per
  arg set and red a one-sided label by name. Id 12 (MEDIUM): S4 and AC4 name the ledger's `build/`
  path, its Serves and Evidences lines, and §4 lists the generated README and records regions in the
  dispatch write set, so §7 names the two `recall floor` legs that path guards. Id 13 (LOW): S1's rebinding of "the pass's base" is scoped to the
  render-comparison phrase in the briefs of units 1, 2, 3, 4 and 6. Ids 1, 5 and 14 (HIGH) are
  promoted to `TOOL-aEvidencedLens-15`; this unit hands it the `resume:probe` comparison, drops that
  label from S2 and AC1, and says in S1 and §4 which value the key mask reaches.

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

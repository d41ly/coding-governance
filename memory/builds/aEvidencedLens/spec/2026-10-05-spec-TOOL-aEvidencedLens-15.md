# TOOL-aEvidencedLens-15 — the diff-kind resume probe is observed from BASE with every REVIEW_SHAPE-derived value masked, its review key and its input print

**Status:** SPECCED · rev-2 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-review-TOOL-aEvidencedLens-15-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-15-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aEvidencedLens-13` compares the diff kind's prompts at BASE with the build's, masking each
run's `result.key`. The spec audit of units 12 to 14 confirmed ids 1, 5 and 14 at HIGH: the
diff-kind `resume:probe` prompt never carries `result.key`. It spells the key's directory as a
template, `<kind>-r<round>-<the first 12 hex of the base sha>-<the first 12 hex of the head sha>-<inputPrint>`
(`tools/workflows/tier2-review.template.js:720` at `14850417e`, `:634` at BASE), and `inputPrint`
hashes `REVIEW_SHAPE`, which `TOOL-aEvidencedLens-1` moves from `lenses5-r1` to `lenses5-r2`. A key
mask therefore masks nothing in that prompt, the comparison is red on a correct build, and the only
way to turn it green is to revert the shape move. This unit masks the CLASS, every value derived
from `REVIEW_SHAPE`, which for the probe is its `inputPrint`; compares the probe from BASE to the
tree after unit 12 under that mask; and proves the mask reached the probe, so the comparison cannot
pass by masking nothing. It closes ids 1, 5 and 14 (HIGH) of that audit.

## 2. Scope (IN)

- **S1** — THE CLASS MASK. For each stub run, the driver derives `print` as the last `-`-separated
  field of that run's `result.key`, and rewrites every prompt by replacing the whole key first and
  then every remaining occurrence of `print`, each with the token `<KEY>`. Replacing the key first
  keeps one token per key rather than a token nested inside a partly masked key. Observed by AC1 and
  AC2.
- **S2** — THE PROBE OBSERVATION. After `TOOL-aEvidencedLens-12` lands, a stub run of the BASE
  render and one of the render at this pass's HEAD, over the two diff-kind arg sets
  `TOOL-aEvidencedLens-13` S2 names, each produce exactly one `resume:probe` prompt, and the two are
  byte-identical under S1's mask. Observed by AC1.
- **S3** — THE MASK REACHED THE PROBE. For each run and each arg set the driver prints the number of
  `<KEY>` tokens the mask wrote into `resume:probe`, and reds when it is zero: a mask that wrote
  no token into the label it compares is the could-not-pass class. The same pair under a key-only mask,
  `TOOL-aEvidencedLens-13`'s, differs, and the red names the label and the `inputPrint` value it left
  standing. Observed by AC1 and AC2.
- **S4** — LIVENESS. A copy of the HEAD render with one word of the probe's instruction text changed
  reds the class-masked comparison and names `resume:probe`. Observed by AC3.
- **S5** — The figures, the args, the two renders' blob ids and both prints are written to this
  unit's acceptance ledger,
  `memory/builds/aEvidencedLens/build/2026-10-05-build-TOOL-aEvidencedLens-15-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-aEvidencedLens-15` and an `**Evidences:** TOOL-aEvidencedLens-15`
  block. Observed by AC4.

## 3. Non-goals (OUT)

- Any change to `tools/workflows/tier2-review.template.js` or its render. This unit observes; a red
  here is a defect in the unit that moved the probe, fixed there.
- The `find:` and `verify:` prompts. They carry the key whole and `TOOL-aEvidencedLens-13` compares
  them under the key mask, which reaches every shape-derived value they hold.
- The spec kind's probe. Units 2 and 4 move it by design.
- A standing suite arm. A self-test cannot reach a sha of this repository's history from an
  adopter's copy (`TOOL-aEvidencedLens-13` §3).
- Dropping `resume:probe` from the BASE comparison. It loses the probe half of shared invariant 2,
  which is the alternative the audit judged weaker.

### Edges

- **consumes-from** `TOOL-aEvidencedLens-13` — the BASE-comparison rule, the two diff-kind arg sets
  and the stub driver shape this unit extends with the class mask; that unit hands this one the
  `resume:probe` label its key mask cannot reach.
- **hands-off** `TOOL-aEvidencedLens-18` — the completion of this unit's observation: the HEAD
  render read from the object database, a staged break on step 3's masked line, every print per arg
  set, and the edges and closing write set the spec audit of this unit found missing. That unit
  re-runs `u15-check.js` and names `resume:probe` in each red.

## 4. Design

### Evidence

Read at `14850417e` on 2026-10-05.

- `const inputPrint = deriveFnv1a(renderCanonical({ shape: REVIEW_SHAPE, ... }))` (`:696`), and
  `deriveReviewKey` returns `` `${kind}-r${round}-${...}-${inputPrint}` `` (`:701-702`). The print
  is the key's last `-`-separated field, so the driver reads it from `result.key` and needs no copy
  of the hash.
- `${inputPrint}` is interpolated in two places only, `:702` and `:720`. The second is the diff-kind
  probe's step 3, which writes the two sha fields as literal placeholder text, so the print is the
  only run-dependent value in that line.
- BASE (`git show 028b5cac:tools/workflows/tier2-review.js`) has `REVIEW_SHAPE = 'lenses5-r1'` at
  `:609` and the same template at `:634`; HEAD has `'lenses5-r2'` at `:687`. For the diff args the
  two prints differ only by shape, and they do differ.

### The class mask

```text
for render in (BASE, HEAD):
  for args in (diff round 1 + checklist + specs, diff round 2 + priorFindings):
    run stub -> prompts{label: text}, key
    print = key.split('-').pop()
    probe = prompts['resume:probe'].split(key).join('<KEY>').split(print).join('<KEY>')
    tokens = count of '<KEY>' in probe          # zero is red (S3)
compare BASE vs HEAD probe per arg set -> byte-identical
liveness: key-only mask differs and names the print left standing; a one-word probe edit reds
```

### Files touched (estimate)

None under `tools/`. The dispatch write set is the acceptance ledger of S5, the regenerated
`memory/builds/aEvidencedLens/README.md`, and this spec's own `gen:spec-records` region. The stub
driver and both renders live in the run's scratch directory.

### Alternatives rejected

- **Masking `REVIEW_SHAPE`'s literal instead of its derived values.** The literal appears in no
  prompt; only its hashes do, so the mask would replace nothing.
- **Normalising the probe's step 3 line by regex.** A pattern loose enough to match the template
  also matches a moved instruction on that line, so a real move would read green.
- **Folding the class mask into `TOOL-aEvidencedLens-13`'s spec.** The finding is HIGH, and the method
  promotes a HIGH to a unit whose mechanism closes it rather than folding it as text.

## 5. Production-readiness checklist

- security — N/A: no code and no write outside the build folder's ledger and its generated regions.
- perf / scale — four stub runs of a harness render, seconds each.
- error / empty / loading states — a stub run that throws, a run with no `resume:probe` label, and a
  mask that wrote no token each red the observation with its reason.
- observability — the ledger names both blobs, both prints, the args and every token count.
- risks — a print value occurring by chance elsewhere in the probe is masked too; it is a 32-bit FNV
  hex and the probe is one prompt, so the effect is a masked coincidence, never a hidden move of
  instruction text.
- testing — the observation is the test; S3 and S4 are its liveness.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

`u15-check.js` lives in the run's scratch directory, outside the tree. It is the driver shape
`TOOL-aEvidencedLens-13` §6 describes, the `runReview` AsyncFunction stubs of
`tools/workflows/tier2-review.test.sh` with recording stubs, plus S1's class mask; it is not the
suite and runs in seconds.

- **AC1** — When `node u15-check.js --mask-class base.js tools/workflows/tier2-review.js` runs the two
  diff-kind arg sets after `TOOL-aEvidencedLens-12` has landed, where `base.js` is the `git show` of
  `tools/workflows/tier2-review.js` at BASE `028b5cac`, each render produces exactly one
  `resume:probe` prompt per arg set, the two are byte-identical, and the driver prints, per run and
  arg set, a `<KEY>` token count of at least 1.
  Red when: the probe moved anywhere from BASE through unit 12, a run has no `resume:probe` label, or
  the mask wrote no token into it.
  fixture: `base.js` is saved to the scratchpad from the object database, never from a working copy.
- **AC2** — When the same driver runs with `--mask-key` in place of `--mask-class`, the comparison
  is red, names `resume:probe`, and prints the HEAD run's print value as the difference left
  standing.
  Red when: the key-only comparison is green, which means the print did not move or the probe
  carries the key whole, and the class mask is proving nothing the key mask did not.
- **AC3** — When `node u15-check.js --mask-class base.js broken.js` runs, where `broken.js` is a
  scratch copy of the HEAD render with one word of the probe's step 1 instruction changed, the
  comparison is red and names `resume:probe`.
  Red when: the class-masked comparison stays green on a staged break, so it compares nothing.
- **AC4** — When `2026-10-05-build-TOOL-aEvidencedLens-15-1-acceptance-ledger.md` under the build's
  `build/` folder is read, it carries `**Serves:** journal TOOL-aEvidencedLens-15` and an
  `**Evidences:** TOOL-aEvidencedLens-15` block naming the two blob ids of
  `tools/workflows/tier2-review.js`, at BASE `028b5cac` and at the pass's HEAD, each read with
  `git rev-parse`, both prints, the token counts of AC1, and the outcome of AC2 and AC3.
  Red when: the observation lives only in the transcript, or in a file check 23 does not read.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: a self-test cannot read this repository's BASE from an adopter's copy (§3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, promoted from the spec audit of units 12 to 14
  (`reviews/2026-10-05-review-TOOL-aEvidencedLens-12-spec-audit-round1.md`), ids 1, 5 and 14 (HIGH),
  repairing `TOOL-aEvidencedLens-13`.
- rev-2 · 2026-10-05 · §3 · gains the hands-off to `TOOL-aEvidencedLens-18`, the minors batch the
  spec audit of this unit (`reviews/2026-10-05-review-TOOL-aEvidencedLens-15-spec-audit-round1.md`)
  promoted for ids 4 and 5 (MEDIUM) and 1, 2, 3 and 6 (LOW). Nothing else moves; this unit builds as
  written.

## 10. Reuse audit

The seam reused is `TOOL-aEvidencedLens-13`'s BASE comparison and its stub driver, which is the
`runReview` stub shape of `tools/workflows/tier2-review.test.sh`; this unit adds one masking step and
one token count. No tool is built.
`python tools/codebase-map/reuse_lookup.py "mask every value derived from a review shape in a prompt comparison"`
returned name-stem neighbours only (`shape`, `derive_scope`, `deriveSidecarPath`) and printed
`unscanned layers: .sh`; none compares prompts, which matches unit 13's probe of the same seam. The
recall probe returned this build's unit 13 spec, whose mask is the key alone, the audit finding
itself, and `TOOL-dTieredTribunal-16`, a prompt-text ask on the same harness that masks nothing; no
record had masked a print that a prompt spells outside the key.

Recall terms used: resume probe inputPrint REVIEW_SHAPE review key mask class BASE render diff-kind byte-identical tier2-review DURABILITY

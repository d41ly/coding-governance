# TOOL-aMouldedFolio-3 — the build README's folder claim becomes derived, because 15 of 17 are false

**Status:** CLOSED · rev-2 · 2026-08-11 · node a · Tier-2 · base 7890becf · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-build-TOOL-aMouldedFolio-3-3-followups-controls.md](../build/2026-08-16-build-TOOL-aMouldedFolio-3-3-followups-controls.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Stop the build README from asserting which record folders it holds. Measured at this spec's base: 17
READMEs make the assertion, 15 of them are wrong, and the fact is derivable from the tree.

## 2. Scope (IN)

- **S1** — the `Records live under …` sentence is DERIVED from the record folders that hold tracked
  files under the build, and rendered inside the generated region.
- **S2** — the authored sentence is removed from every README carrying one, BY THE GENERATOR, in the
  same pass. No file is hand-edited.
- **S3** — the removal is SENTENCE-scoped, never line-scoped. Measured: in 17 of 17 the sentence
  shares its physical line with the opening clause of the next sentence, so deleting the line
  destroys unrelated prose in every file.
- **S4** — a build with no record folders renders no sentence rather than an empty list.
- **S5** — an arm per branch, each proven by a negative control.

## 3. Non-goals (OUT)

- **The `Node · opened · streams` restatement is NOT absorbed.** Measured at this base: 19 of 31
  READMEs carry it and only 2 disagree with their own front matter, both cosmetically. It duplicates
  the generated region, which is a minor two-answers, but it is not WRONG anywhere, and this unit's
  justification is a false claim. An accurate sentence does not get to ride it.
- No prose template for the authored narrative — 19 of 31 READMEs carry no `##` heading at all.
- No change to `ids:`, the roster, the unit table, or the rest of the region.

## 4. Design

### Data model

The sentence is a function of one input: which of `spec`, `build`, `reviews`, `prompts` hold at least
one TRACKED file under the build. Directory-on-disk and holds-tracked-files give identical answers
for all 31 builds today — measured, so the two readings rev-1 mixed are not a live ambiguity — and
the tracked reading is the one that binds, because the generator already has that list.

MEASURED at base `7890becf`, and this is the justification, not background:

| | Count |
|---|---:|
| tracked build READMEs | 31 |
| carrying the sentence | 17 |
| **carrying a WRONG sentence** | **15** |
| disagreements: claims a folder that is absent | 19 |
| disagreements: omits a folder that is present | 2 |
| **total disagreements** | **21** |

The two clean carriers are `aMooredAnchor` and `aSealedCaravan`. The failure is structural rather than
careless: the sentence is written when a build opens, predicting the folders it will grow, and nothing
revisits it when the prediction is wrong. Seven READMEs claim a `build/` that was never created.

### Migration

THE REMOVAL IS SENTENCE-SCOPED. Measured: in 17 of 17 carriers the line reads

```
Records live under `spec/`, `build/` and `reviews/`. The table below is
```

— the sentence ends mid-line and the next sentence begins on the same line, wrapping to the next.
rev-1 bounded the removal to "a single LINE, anchored", called that a safety property, and it was the
wrong unit: a conforming implementation would delete `The table below is` from all 17 files and orphan
`GENERATED from the status header …` on the following line, with every rev-1 acceptance criterion
green. That is the prose destruction the bound was written to prevent.

The removal therefore:

1. matches the SENTENCE — from `Records live under` to its terminating period — plus at most one
   following space, and never a newline;
2. runs only OUTSIDE the marker pair, so the generated region is untouched;
3. refuses, naming the README and both offsets, if the sentence matches more than once outside the
   region;
4. leaves the physical line in place when text remains on it, and removes the line only when the
   sentence was the whole of it.

### Rollout

One commit; check 9 fails if the generator change and the regenerated artifacts are split.

### Files touched (estimate)

| File | Why |
|---|---|
| `tools/memory-tree/gen_build_index.py` | S1–S4 and the arms |
| 31 build READMEs | regenerated; 17 also lose one sentence |
| `memory/map/generated/*` | the new function enters the symbol corpus — the freshness leg reds without a regen, which rev-1 omitted |
| `tools/memory-tree/check-memory-hygiene.sh` + both rule-set halves | the version pair — see §8 |
| `.claude/SESSION-KICKOFF.md` | the audit stamp; the hygiene engine is watch item 1 |

### Alternatives rejected

- **Validate the sentence instead of deriving it.** A validator over a fact the tree knows, redding 15
  READMEs on day one with no remedy but hand-editing all of them.
- **Delete the sentence and render nothing.** It carries real information a reader uses.
- **Line-scoped removal** (rev-1). Destroys prose in 17 of 17; see §Migration.
- **Absorb the `Node · …` line here.** It is accurate; see §3.

## 5. Production-readiness checklist

| Concern | Position |
|---|---|
| Prose destruction | Sentence-scoped, outside the markers, refuses on a second match, and never deletes a line carrying other text. The 17 diffs are the review surface. |
| Self-reference | The derived sentence lives INSIDE the markers and the remover runs only outside them, so the remover cannot match its own output on the next run. |
| Empty population | A build with no record folders renders no sentence (S4) — legal for a young build. |
| Idempotence | Two consecutive writes produce identical bytes, including on an already-cleaned README. |
| Ordering | Folders render `spec`, `build`, `reviews`, `prompts`, not filesystem order. |
| Moving corpus | Other nodes land builds continuously, so AC counts are expressed as invariants over the corpus AT BUILD TIME, not as frozen integers — see AC1 and AC7. |
| Reversibility | Every deletion is in git. |

## 6. Acceptance criteria

- **AC1** — after the write, ZERO builds disagree between the rendered sentence and the folders holding
  tracked files. Stated as an invariant, not as "21 repaired", because the corpus moves.
- **AC2** — no README retains an authored `Records live under …` sentence outside the markers.
- **AC3** — for every README the remover touched, the text that followed the sentence on its line
  SURVIVES, byte for byte. Asserted over the whole regenerated corpus, and it is the criterion rev-1
  lacked.
- **AC4** — no README loses a physical line unless the sentence was the entire line; measured as
  deleted-line count equal to the number of such READMEs, which is 0 today.
- **AC5** — a build with no record folders renders no sentence and is otherwise unchanged.
- **AC6** — adding a record folder changes the rendered sentence on the next write; removing one
  changes it back.
- **AC7** — a README carrying the sentence twice outside the region causes a named refusal, not two
  removals.
- **AC8** — the generator performs the removal: with the remover disabled, the run REDS. This is S2's
  acceptance, which rev-1 had none for — its criteria were all satisfiable by 17 hand-edits.
- **AC9** — the writer is idempotent: a second consecutive run writes zero changed bytes.
- **AC10** — every new failure branch has a positive arm naming its own text, each proven by a negative
  control.

## 7. Gates

`bash tools/run-gates.sh` green on a QUIESCENT tree at the push boundary. Affected legs: memory
hygiene (check 9 byte-compares every artifact), the build-index selftest, codebase-map coverage +
freshness, the kit-version and verdict-epoch pair, kit-dogfood parity, and the kickoff ratchet. The
recurring-bug-class checklist runs over the diff before review — `apply_region`'s prose-eating warning
is the class this unit sits closest to.

## 8. Open questions

- **RESOLVED (agent, 2026-08-11, delegated): version value and landing order.** The three follow-up
  units bump one constant, and an identical bump on two branches merges without conflict while the
  epoch gate stays satisfied. They land SEQUENTIALLY on one branch; this unit takes **3.0** if it
  lands after `-5` and `-4`, and re-bumps rather than reusing a value if the order changes.
- **RESOLVED (agent, 2026-08-11, delegated): the wording once derived.** The majority variant wins — `Records live under <list>.` with an Oxford-free `and` before the last item, matching the 9-of-17 spelling. It is one string in one function and changeable without touching a README.

## 9. Revision log

- rev-1 · 2026-08-11 · first draft, written after measuring the corpus rather than from the backlog
  row's framing.
- rev-2 · 2026-08-11 · Tier-2 review fold, 5 blockers across the three specs. Two were this unit's.
  §1 claimed "wrong in 17 of the 17" where the measurement is 15 of 17, and contradicted this spec's
  own arithmetic — a measured falsehood in the justification of a unit that exists to remove measured
  falsehoods. And the removal was LINE-scoped: in 17 of 17 the sentence shares its line with the next
  sentence's opening clause, so the rev-1 bound would have destroyed prose in every file while all its
  criteria passed. Every denominator was stale at 25 — inherited from the parent build's census at
  `af6de231`, never re-measured — against 31 today. AC3, AC4 and AC8 are new; AC1 became an invariant
  because the corpus moves; the codebase-map freshness leg was missing from Files touched and Gates.

## 10. Reuse audit

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| List a build's tracked files | `collect`'s existing list | REUSE; no new source |
| Splice into the generated region | `apply_region` | REUSE unchanged |
| Rewrite one anchored span in an authored file | `apply_front_matter_ids` | REUSE THE SHAPE — anchored, single-match, refuse-on-ambiguity — applied to a SENTENCE outside the markers rather than a line inside the front matter |
| Skip fenced blocks when searching | `unfenced` in the same module | REUSE, so a sentence quoted inside a fence is not removed |
| Byte-compare the result | hygiene check 9 | REUSE; no new leg |
| Prove an arm is not vacuous | the negative-control practice | REUSE as AC10 |

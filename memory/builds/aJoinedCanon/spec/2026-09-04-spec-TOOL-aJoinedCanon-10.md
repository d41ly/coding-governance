# TOOL-aJoinedCanon-10 — the template stops claiming a declaration that is not there

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-1 · base 750ca0ca · streams tooling · order 10 · ratified 2026-09-05

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/TEMPLATE-SPEC.md:16` sends a reader to `.memory-tree.conf` for a key this repo's conf does
not declare, and counts the siblings it would sit beside. Both halves break a charter rule, in the
document that teaches the spec format: point at the source rather than restating it, and write no
count of a derived population in prose. Nothing is broken at runtime and the fix is small; it is
worth a unit because a format document that breaks the rules it teaches is the cheapest kind of
drift to fix and the most expensive kind to leave standing.

## 2. Scope (IN)

- **S1** — the count leaves line 16 of both template halves. The sentence stops saying "beside the
  three other cutoffs" and puts no other count in its place. It KEEPS the location claim, which S2
  makes true, and keeps the shipped value; what it may not keep is a number no check derives.
- **S2** — `.memory-tree.conf` declares `SPEC10_CUTOFF="2026-08-04"`, which makes the location half
  of the sentence true in this tree as it already is in a fresh adopter's. Placed beside
  `SPEC10_EVIDENCE_CUTOFF` at `:104`, whose own comment at `:101` already names `SPEC10_CUTOFF`
  without declaring it. Behaviour is unchanged: the value is identical to the preset at
  `check-memory-hygiene.sh:42`, so the forward resolution at `:90` simply stops firing.
- **S3** — both halves move together. `memory/TEMPLATE-SPEC.md` is rendered from
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, so the template is the edited file and the live
  copy is regenerated rather than hand-edited.

## 3. Non-goals (OUT)

- **The other prose-stated counts in the same section are OUT, and that is a deliberate cut.**
  Lines 22, 24 and 29 of both halves say "its three siblings", "Those three" and "the four cutoffs".
  Each is stale by the same arithmetic. They are a separate concern because they are historical
  claims about the population at `TOOL-aDeclaredBound-2`'s time, whereas line 16 is a live
  navigation instruction that fails a reader today. Follow-up: one `TOOL` backlog row, "the
  SPEC10_CUTOFF section states four counts of a population nothing derives". Leaving them is a
  knowingly deferred instance of the same class, said plainly rather than implied away.
- No change to check 12, to the canon selection, or to `SPEC10_CUTOFF`'s value. This unit moves
  prose and one inert declaration; the gate must grade every spec in the tree exactly as it does now.
- No `KIT_MEMORY_TREE_VERSION` bump. `tools/check-kit-versions.sh:132-147` asserts every tracked
  `tools/memory-tree/*.template.md` marker EQUALS the constant; it never demands the constant move
  on a body change. Both files already carry `memory-tree@2.59`. A bump is a judgment call for the
  owner, not a gate obligation, and this unit does not take it.
- No retrofit of any landed spec, and no new dated cutoff. Nothing here changes what the gate demands
  of any file, so the build's cutoff rule has nothing to bind.

## 4. Design

### The verified facts

Run at writing time against this worktree at base `750ca0ca`.

| Claim | Where | Verified state |
|---|---|---|
| `SPEC10_CUTOFF` declared in `.memory-tree.conf` | `TEMPLATE-SPEC.md:16` | ABSENT from this repo's conf |
| `SPEC10_CUTOFF` preset in the checker | `check-memory-hygiene.sh:42` | present, `"2026-08-04"` |
| shipped value captured before the conf source | `check-memory-hygiene.sh:43` | `_SPEC10_SHIPPED` |
| blank resolves forward | `check-memory-hygiene.sh:90` | `: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"` |
| the key IS in the shipped example conf | `tools/memory-tree/.memory-tree.conf.example:44` | `SPEC10_CUTOFF="2026-08-04"` |
| the two halves agree on line 16 | both files | byte-identical, confirmed by `diff` |

The last row of that table reframes the defect and is the reason S2 exists. `adopt-memory-tree.sh`
copies the example only when no conf exists and never back-fills a key into one that does, which the
checker's own comment at `:82-88` records as the reason five cutoffs are preset above the source. So
a repo adopting the kit today gets `SPEC10_CUTOFF` in its conf and the template's sentence is true
for it. The repo the sentence is false in is this one, whose conf predates
`TOOL-aDeclaredBound-2` and was never back-filled. The document did not drift away from the kit; the
dogfood tree drifted away from the example the kit ships.

### On the count, and why deleting beats updating

C6 reports six declared cutoffs from `grep -nE '^[A-Z_]+CUTOFF=' .memory-tree.conf`. That predicate
excludes any key whose name carries a digit, so it does not see `SPEC10_EVIDENCE_CUTOFF` at `:104`.
The digit-inclusive `grep -nE '^[A-Z0-9_]+CUTOFF=' .memory-tree.conf` returns seven. Both numbers are
true of their own predicate and neither belongs in a document, which is the argument for S1 in one
sentence: a count of this population has now been wrong in the template, wrong in a comment, and
ambiguous in the finding that reported it. S2 sharpens it. The key it declares carries digits, so
the digit-inclusive predicate sees it and the other cannot: the moment this unit lands the two
report six and eight instead of six and seven. A number written into line 16 would be stale by the
same commit that wrote it, which is why S1 deletes the count rather than correcting it.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | line 16, the authored edit |
| `memory/TEMPLATE-SPEC.md` | line 16, written by `--render`, never by hand |
| `.memory-tree.conf` | one added declaration (S2) |

### Alternatives rejected

- **Reword the sentence to describe the preset and the forward resolution, and leave the conf alone.**
  It is honest and it is more prose about the checker in a document whose prose-about-the-checker
  share was already measured in `aWeighedCanon`. It also leaves this tree disagreeing with the conf
  the kit ships. Carried as the §8 fork rather than rejected outright, because it was the owner's
  call whether a doc edit or a tree edit is the right half to move — ruled against on 2026-09-05.
- **Delete the whole `SPEC10_CUTOFF` section and point at the conf comment.** The section carries the
  blank-resolves-forward reasoning, which lives nowhere else in a document an author reads. Out.

## 5. Production-readiness checklist

- security — N/A, no code path, no input, no new surface.
- perf / scale — N/A, three lines of static text and one shell assignment read once per run.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — N/A, nothing executes.
- observability — N/A, the parity leg already reports the only failure mode.
- risks (concurrency, data-loss, rollback hazards) — the one real risk is hand-editing
  `memory/TEMPLATE-SPEC.md` instead of the template, which reds `kit/dogfood doc parity`; S3 names
  the direction and the leg catches the mistake.
- testing + left-shift gates — no new arm. The claim S2 corrects is prose, and a gate that reads
  prose for a key name is the paraphrase-beside-its-source shape this build already parked twice.
- migration / rollback — none needed; `SPEC10_CUTOFF` resolves to `2026-08-04` before and after, so
  reverting either half is a plain revert with no corpus effect.
- user docs — the template IS the user doc; S1 and S3 are the update.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'three other cutoffs' memory/TEMPLATE-SPEC.md
  tools/memory-tree/SPEC-TEMPLATE.template.md` runs, it matches nothing, and
  `grep -c 'DECLARED in' memory/TEMPLATE-SPEC.md tools/memory-tree/SPEC-TEMPLATE.template.md`
  returns 1 for each file — the count is gone and the location claim the ruling makes true is still
  standing, which is the half S1 must not take with it.
- **AC2** — When `grep -nE '^SPEC10_CUTOFF=' .memory-tree.conf` runs, it returns one line whose value
  is `2026-08-04`, so a reader following line 16 to the conf finds the key it names.
- **AC3** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs, it exits 0, proving
  the live copy and its shipped twin moved together.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs against the tree before and
  after S2, both runs report the same verdict on every spec, confirming the added declaration is
  inert against the preset it duplicates.
- **AC5** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with `KIT_MEMORY_TREE_VERSION`
  unchanged at `2.59`, confirming §3's no-bump decision leaves no half-bumped marker.

## 7. Gates

- `kit/dogfood doc parity` — guarded on `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/`, both of
  which S1 and S3 touch, so the leg runs on this diff without `GATE_FULL=1`.
- `memory hygiene` and `kit version markers` — both carry no `guard` in `tools/gate-legs.json`, so
  they run on every bar regardless of what this diff touches.
- No new gate. `.memory-tree.conf` is a repo-root file that no leg guard can select, recorded as
  `TOOL-aWalkedCorpus-5`; S2 therefore relies on the unguarded legs above rather than on a guard of
  its own, and this is stated so a reviewer does not read the absent guard as an oversight.

## 8. Open questions

- **F1 — which half moves to make line 16 true: the tree, or the sentence.** Option A is S2 as
  specced: declare `SPEC10_CUTOFF` in `.memory-tree.conf`, which makes the existing sentence true,
  closes the drift between what this repo ships and what it runs, and costs one inert line. Option B
  is to delete the location claim and reword the sentence around the preset at
  `check-memory-hygiene.sh:42` and the forward resolution at `:90`, leaving the conf alone. A is
  cheaper and removes a drift; B is cheaper to revert and adds no key to a conf that four other
  units in this build may also be editing. **Recommendation: A, with S1 landing under either.**
  RESOLVED (owner, 2026-09-05): Option A — the conf declares `SPEC10_CUTOFF`, so line 16's location
  claim becomes true rather than being reworded away; B's rewording around the preset and the forward
  resolution loses, and its text stays above as the record of what was weighed. S1 lands either way
  and is unchanged by the pick.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §2 · §4 · §6 · folded the owner's ruling on F1: option A, the conf
  declares `SPEC10_CUTOFF`. S1 stops offering to drop the location claim and now keeps it; §4's
  alternative is marked ruled-against rather than open, and gains the arithmetic showing S2 moves the
  digit-inclusive count from seven to eight; AC1 gained the second half that pins the location claim
  in place. §7 was re-read and needs nothing — option B would have removed S2 and with it the
  `.memory-tree.conf` bullet, and A keeps both.

## 10. Reuse audit

The probe result: no existing seam fits the *change* — a prose correction extends nothing — but the
seam this unit RIDES is real and named. `python tools/codebase-map/reuse_lookup.py "a document
states where a configuration key is declared"` ranked `kit-dogfood-parity.PAIRS` in the
`build-method` dossier among its affordance seams, which is exactly the template-to-live render pair
S3 depends on, at `tools/memory-tree/kit-dogfood-parity.test.sh:53`. Its symbol candidates are all
key-parsing and declaration-extraction functions with no bearing on editing a sentence, so nothing is
being reimplemented here. `python tools/memory-recall/query.py` returned
`TOOL-aDeclaredBound-2` as hit 2, which is the unit that authored the sentence this one corrects, and
`TOOL-aProvenReuse-1` as hits 3 and 11, whose S1 records the preset-above-the-conf-source idiom that
makes S2 inert.

Recall terms used: `SPEC10_CUTOFF forward resolution blank means off cutoff declaration memory-tree
conf preset unbound variable adopter`

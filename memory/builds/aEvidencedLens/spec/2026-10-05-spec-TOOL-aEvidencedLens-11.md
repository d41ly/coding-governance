# TOOL-aEvidencedLens-11 — the method, the memory-tree README, the Skill, the verbs entry and a decision record state what units 1 to 9 built

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-1 · base 028b5cac · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-11-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-11-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 |

<!-- /gen:spec-records -->

## 1. Goal

Units 1 to 9 change what an opted-in spec audit is and how its exit is disposed. The carriers an
operator reads still say a spec audit's mediums and lows are FOLDED, list four lens names, and send
the reader to `tools/memory-tree/README.md` for a catalogue the harness now owns. A carrier that
disagrees with the driver sends the operator into a refusal with nobody to explain it. This unit
states, in every carrier, what units 1 to 9 built and the owner's answer of 2026-10-05, and nothing
more. That scope is the owner's mandate (shared invariant 11).

## 2. Scope (IN)

- **S1** — The build method's M4, edited in `tools/memory-tree/BUILD-METHOD.template.md` and
  re-rendered into `memory/guides/BUILD-METHOD.md`. Observed by AC1 and AC2.
  - The disposition paragraph states ONE rule for both subjects. A MEDIUM or LOW is PROMOTED,
    batched into ONE unit naming them all, TWO only across two disjoint write sets by M6, never one
    per minor. That holds on a SPEC subject (owner, 2026-10-05) as on the closing DIFF review (owner,
    2026-10-04), and nothing is folded at an exit. The clause that folds a spec subject's minors and
    the separate closing-review sentence collapse into that one statement.
  - The catalogue sentence points at `SPEC_LENSES` in `{{TOOL_ROOT}}workflows/tier2-review.js` and
    lists no lens name.
  - One sentence says lenses probe read-only: no write under the repository, temporary files only
    in the run's scratch, every command bounded, and no merge bar or suite inside a lens. It
    spells `read-only` and `scratch`.
  - The "Fold fixes into the spec, then STOP" sentence says a round that is not an exit folds its
    fixes and re-invokes, and the exit disposes what stands, so the fold is never read as the
    exit's disposition. It spells the words "a round that is not an exit".
  - M2's decompose sentence says "a review's minors batch" where it says "the closing review's".
  - M4's chain-of-promotions sentence, the precision bound, is unchanged. The generation bound
    `TOOL-aEvidencedLens-8` §8 F3 parked for the owner is not stated in any carrier.
  - Deletions come first. The rendered file is no larger than at BASE.
- **S2** — `tools/memory-tree/README.md`'s section "M4 — the spec-audit lens catalogue" keeps its
  heading, and its body becomes one sentence pointing at `SPEC_LENSES` in
  `<prefix>/workflows/tier2-review.js` as the one source of the catalogue. It is the hands-off
  `TOOL-aEvidencedLens-1` declares. Observed by AC3.
- **S3** — `tools/unattended/SKILL.template.md`, re-rendered into
  `.claude/skills/unattended/SKILL.md` by `bash tools/unattended/adopt-unattended.sh`. Observed by AC4.
  - The `CONVERGED`, `NON-CONVERGENT` and `BOUNDED` bullets stop saying a MEDIUM or LOW is folded on
    a spec subject, and stop calling `--disposition promote` optional there. A terminal spec round
    records `--highs` and `--minors`, and `promote` whenever anything stood.
  - The `CONVERGING` bullet says a spec subject's fold fixes what that round confirmed, and only the
    exit promotes, as `TOOL-aEvidencedLens-8` §8 F1 resolved.
  - The counts paragraph says the counts bind every terminal round, spec subjects included, and
    stops saying "refused on any other round or subject". On a spec subject the build harness records them
    itself. Recorded by hand, they are that exit round's `highs`, and its
    `confirmed - blockers - highs` plus every UNVERIFIED finding the disposal promoted, as
    `TOOL-aEvidencedLens-8` S5 and S6 count them, with no summing across rounds, because a spec
    round's fold fixes everything that round confirmed.
- **S4** — `tools/unattended/VERBS.template.md`'s `--review` entry, re-rendered into
  `memory/guides/UNATTENDED-VERBS.md` by the same adopter, states the flags as
  `TOOL-aEvidencedLens-7` built them. `--highs` and `--minors` bind a spec subject's terminal exit
  too. `fold` is refused at every terminal exit, and survives only as the reading of a row written
  before unit 7. The sentence calling a spec subject's `promote` "ACCEPTED, never required", the
  clause refusing either count on a spec subject, and the clause saying `fold` is a row "which the
  driver reaches only at `CONVERGED`" go. The refusal wording is copied from unit 7's
  driver as built, never paraphrased from its spec. Observed by AC4.
- **S5** — `memory/DECISIONS.md` gains one row recording the owner's answer of 2026-10-05. It
  supersedes the fold half of `TOOL-aProbedUnit-9`, whose one-round default stands, and never edits
  that ratified row. The row's id is the next one this session's TOOL family mints, minted by the
  main loop when it writes the row. This spec does not spell it, because a cited id that does not
  yet exist is created as an orphan in the derived `ids:` roster. `--dispatch` refuses
  `memory/DECISIONS.md` as a shared mutable record, so the row lands in a records commit of its own
  at the main loop, as `TOOL-aBatchedMinors-4` rev-2 found. Observed by AC5.
- **S6** — The carrier sweep. After S1 to S4, the §6 AC6 grep runs over the tree outside build
  records. A hit in a file this unit owns is fixed here. A hit in a file another unit of this build
  owns is returned to the main loop in this unit's acceptance ledger and not fixed here. Observed by
  AC6.

## 3. Non-goals (OUT)

- Any rule beyond what units 1 to 9 built and the owner's answer. Anything more is a veto-2 fork.
- `memory/guides/REVIEW-PROTOCOL.md` and its template. `grep -niE 'spec[- ]audit|spec subject|prior.art|fold|MEDIUM'`
  over `tools/workflows/REVIEW-PROTOCOL.template.md` at BASE found no spec lens list and no fold, so
  the brief's condition for touching it is not met.
- `tools/workflows/README.md`'s "A spec audit keeps its four lenses". `TOOL-aEvidencedLens-1` owns it.
- The driver's exit note, comments and refusals in `tools/unattended/unattended.sh`. Unit 7 owns them.
- `TOOL-aLeakedHandle-6`, which disposes a late blocker "under M4 fold/promote". It defers to M4,
  and M4 now promotes, so it needs no superseding row.
- The governance template. It states neither the lens list nor the disposition.
- Kit version bumps. The main loop bumps every touched kit once, after the last move (shared
  invariant 7).

### Edges

- **consumes-from** `TOOL-aEvidencedLens-1` — `SPEC_LENSES` as the one source of the catalogue, and
  the lens briefs S1 and S2 point at instead of naming.
- **consumes-from** `TOOL-aEvidencedLens-2` — the read-only probe policy and the `scratch` arg S1
  describes.
- **consumes-from** `TOOL-aEvidencedLens-7` — the driver's `--highs`, `--minors` and refusals on a
  spec subject's exit, which S3 and S4 describe.
- **consumes-from** `TOOL-aEvidencedLens-8` — the harness that promotes spec-audit minors batched and
  records the counts itself, which S3 describes.

## 4. Design

### Evidence

Read at base `028b5cac`.

- `memory/guides/BUILD-METHOD.md` measured 28169 bytes against its 30720 cap, with a recorded
  high-water of 27946. `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` passed with
  an advisory growth warning. PINNED, measured 2026-10-05.
- M4's disposition paragraph is template line 142; the catalogue sentence is lines 131 to 133; the
  fold-then-STOP sentence is line 139; M2's batch exception is line 34.
- The template spells sibling-kit paths as `{{TOOL_ROOT}}workflows/…`, at line 212. The README spells
  them as `<prefix>/…`. `tools/check-install-prefix.sh` is a pure ban on a sibling literal, with no
  waiver, so both spellings are required rather than chosen.
- The README's catalogue is lines 526 to 534. No `*.sh`, `*.py` or `*.js` under `tools/` reads it;
  `git grep -nE 'memory-tree/README|M4 — the spec'` over them found only the harness comment unit 1
  deletes.
- The Skill states the fold at template lines 805 to 806 and 812, and the counts paragraph says
  "REQUIRED there and refused on any other round or subject" at lines 852 to 853.
- The verbs entry states the optional spec-subject `promote` at line 227 and refuses either count on
  a spec subject at line 239.
- `bash tools/unattended/adopt-unattended.sh --check` printed `in sync` at BASE, so S3 and S4 start
  from a clean render.

### The carrier grep this unit ran

```bash
git grep -nIiE 'four lenses|unstated[- ]assumption|FOLDED into|MEDIUM or LOW|underspecification|prior[- ]art|nothing outside the spec set|--disposition promote' \
  -- ':!memory/builds' ':!memory/archive' ':!memory/ledger' ':!memory/backlog' ':!memory/LIVE.md'
```

Its carrier hits at BASE: the method and its template (M4), `tools/memory-tree/README.md` (the
catalogue), the Skill and its template, the verbs entry and its template. The rest are owned
elsewhere: `tools/workflows/tier2-review.template.js` and `tools/workflows/README.md` by unit 1, and
`tools/unattended/unattended.sh` with its suite by unit 7. The gotchas `fold-text-is-unreviewed-surface`
and `one-value-field-records-a-mixed-outcome` describe history and stay.

### Files touched (estimate)

- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/memory-tree/README.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/DECISIONS.md`

The method is rendered by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, its render
mode, run as the renderer and not as a suite.

### The decision row

Under 300 bytes, the cap every row of the file meets. The id is the main loop's to mint.

```text
- **<minted id>** - **spec audits promote mediums and lows, batched**: owner, 2026-10-05. One batched unit (two across disjoint write sets), never folded. Supersedes the fold half of TOOL-aProbedUnit-9; its one-round default stands. Detail `builds/aEvidencedLens/`.
```

## 5. Production-readiness checklist

- testing — AC1 to AC6 are greps and two checkers. The parity and wiring legs run at the close.
- user docs — this unit is the user docs.
- risks — The method's byte cap: S1 deletes the split rule before adding the pointer and the probe
  sentence. And a carrier written from a sibling's spec rather than its build: S4 copies the
  driver's wording as built.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs after the
  render, it prints `template-size OK`. When `wc -c < memory/guides/BUILD-METHOD.md` runs, it prints
  at most 28169.
  Red when: the edit adds a paragraph rather than collapsing the split rule.
  figure: 28169 is PINNED, the BASE size measured 2026-10-05. This is a budget and is green at BASE
  by design; AC2 is the criterion that reds on today's tree.
- **AC2** — When `grep -c 'FOLDED into its spec'` runs over `tools/memory-tree/BUILD-METHOD.template.md`
  and `memory/guides/BUILD-METHOD.md`, both print 0. When `grep -c 'SPEC_LENSES'` runs over the same
  two files, both print the same non-zero count. When `grep -cE 'underspecification|unstated assumption'`
  runs over both, both print 0. Over `memory/guides/BUILD-METHOD.md`, M4 carries `read-only` and
  `scratch` in one sentence, `grep -c 'a round that is not an exit'` prints 1,
  `grep -c "a review's minors batch"` prints 1, and `grep -c "the closing review's minors batch"`
  prints 0.
  Red when: the template was edited and not re-rendered, a lens name or the fold survives, or a
  bullet of S1 was deleted without its replacement.
- **AC3** — When `grep -nE 'underspecification|unstated assumption|prior art' tools/memory-tree/README.md`
  runs, it prints nothing, and `grep -c 'SPEC_LENSES' tools/memory-tree/README.md` prints at least 1.
  Red when: the README keeps a second copy of the catalogue.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it prints `in sync`. When
  `grep -nE 'FOLDED into the spec it belongs to|ACCEPTED there, never|is ACCEPTED, never required|refuses either count on a spec subject|refused on any other round or subject|reaches only at .CONVERGED.'`
  runs over `tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md`,
  `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, it prints nothing,
  and the Skill's `CONVERGING` bullet names the spec subject's fold.
  Red when: a carrier still tells a spec subject to fold, calls its `promote` optional, refuses its
  counts, or scopes the in-loop fold to the closing diff review only.
- **AC5** — When `git diff 028b5cac -- memory/DECISIONS.md` runs after the records commit, it shows
  exactly one added line and no removed line. That line names `TOOL-aProbedUnit-9`, carries
  `2026-10-05` and is at most 300 bytes.
  Red when: the ratified row is edited, or the ruling lives only in this build's prompt record.
- **AC6** — When `git grep -nIiE 'MEDIUM or LOW is FOLDED|FOLDED into the spec|four lenses|ACCEPTED there, never|is ACCEPTED, never required'`
  runs with the exclusions of §4's grep plus `':!memory/gotchas'`, it prints no line in a file this
  unit owns, and every line it prints in a file another unit owns is listed in this unit's
  acceptance ledger as returned to the main loop.
  Red when: any carrier still states the fold for a spec subject or the four-lens count. A hit in a
  file another unit owns is returned to the main loop, not fixed in this pass.

## 7. Gates

`build-method size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `unattended skill wiring` · `install-prefix (shipped surface)` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft.
- rev-2 · 2026-10-05 · S1 S3 S4 AC2 AC4 · round-1 spec audit fold. Id 22 (MEDIUM): AC2 observes the
  read-only sentence, the not-an-exit fold sentence and M2's minors-batch wording. Id 23 (MEDIUM):
  S3 and S4 name the counts-refused clause and the `CONVERGED`-only fold clause, and AC4's
  alternation and its `CONVERGING` assertion read them. Id 29 (MEDIUM): S3's hand-recorded minors
  term adds every UNVERIFIED finding the disposal promoted, as unit 8 counts it. Id 45 (MEDIUM, its
  unit-11 half): S1 keeps M4's chain sentence unchanged, consistent with unit 8 §8 F3 parking the
  generation bound.
- rev-3 · 2026-10-05 · AC6 · build pass. AC6 as written could not pass on a correct build: its grep
  hits the two gotchas §4 says describe history and stay, and S6 routes a hit in another unit's file
  to the ledger rather than to an empty output. AC6 now excludes `memory/gotchas` and reads S6's
  ledger route.

## 10. Reuse audit

No new document. The carriers are the ones that state the rule today, and each is rendered by its
existing renderer: the memory-tree kit's parity render for the method and the unattended adopter for
the Skill and the verbs entry. The decision row follows the shape of `TOOL-aBatchedMinors-5`, the
precedent supersession for the closing review. The unit is the twin of `TOOL-aBatchedMinors-4`,
which made the same carriers state the closing-review rule.
`python tools/codebase-map/reuse_lookup.py "render the build method from its template"` returned only
Python render and build helpers of other kits, none a carrier, so the renderers were found by grep
for `BUILD-METHOD.template` and `VERBS.template`.

Recall terms used: `python tools/memory-recall/query.py "which carriers state the spec-audit lens catalogue and the fold of spec-audit mediums and lows" --terms "BUILD-METHOD M4 lens catalogue memory-tree README Skill verbs carriers fold promote spec-audit supersede"`

# TOOL-aJoinedCanon-4 — a criterion names the break that would turn it red

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 4 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Make `## 6. Acceptance criteria` ask each criterion what break would turn it red, because authors are
already answering that question in a section that never asked it. Finding A3 measured 93 of 479 specs
mentioning a staged break or a red-first run, clustering in §6 with 79 lines and in §5 with 30. The
format is collecting the answer by accident, in whichever section the author reached for, and can
therefore neither find it nor check it.

## 2. Scope (IN)

- **S1** — a per-criterion failure-mode clause, marked `Red when:`, stated in the acceptance-criteria
  body of `tools/memory-tree/SPEC-TEMPLATE.template.md`. The clause may sit on the bullet's opening
  line or on any continuation line beneath it, which is the same latitude the acceptance-witness rule
  already grants and matches this corpus's wrap style at 100 columns.
- **S2** — `SPEC_FAILURE_MODE_CUTOFF` declared in THREE carriers, not two. It is preset blank in
  `tools/memory-tree/check-memory-hygiene.sh` beside its siblings, in the block that runs from
  `STREAMS_CUTOFF=""` to `SPEC10_EVIDENCE_CUTOFF=""`; declared in `.memory-tree.conf` with its date
  and the reason for that date; and shipped BLANK in `tools/memory-tree/.memory-tree.conf.example`.
  The third is not optional: the self-test derives every `_CUTOFF=` preset out of the engine and
  fails naming any key the shipped example does not declare, so an engine-plus-conf edit reds this
  unit's own `memory-hygiene self-test` leg on its landing commit, and an adopter who never receives
  the key cannot discover it. Blank means OFF, taking `STREAMS_CUTOFF` semantics and not
  `SPEC10_CUTOFF`'s forward resolution, because this key switches one rule on rather than selecting
  between two canons.
- **S3** — the per-bullet accumulator is HOISTED, and the arm rides it. Today the acceptance-witness
  walk in `tools/memory-tree/check-memory-hygiene.sh` — the block whose comment head is
  `# ---- acceptance witnesses:` — opens with `if (wcut != "" && fdate != "" && fdate >= wcut) {` and
  builds its `acc` accumulator INSIDE that guard. Nesting a second test in there would make this
  arm's population the INTERSECTION of `SPEC_WITNESS_CUTOFF` and `SPEC_FAILURE_MODE_CUTOFF`, and in
  a tree where the witness key is blank — which is what `tools/memory-tree/.memory-tree.conf.example`
  ships — the accumulator this arm reads would never be built at all, while this arm's own key read
  as armed. So the loop moves OUT of that guard and each arm keeps its own predicate: the file's two
  liveness tests are computed once, the loop runs when EITHER is live, and at each bullet close the
  backtick test fires only under the witness predicate and the `Red when:` test only under this
  unit's. Two independent bad-lists, two independent messages, two populations that do not intersect.
  The union guard is COST, never population: every finding is emitted under its own arm's predicate
  alone, so no verdict of either arm can depend on the other key. Still no new walk, no new section,
  no new `fail` branch.
- **S4** — the rule binds BOTH tiers, like the streams and witness ratchets and unlike the section
  canon. A Tier-1 spec is exempt from the ceremony, not from meaning what it writes.
- **S5** — both halves of the template move together. `tools/memory-tree/SPEC-TEMPLATE.template.md`
  is edited and `memory/TEMPLATE-SPEC.md` is REGENERATED from it by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited, because the two
  are byte-compared after placeholder substitution.
- **S6** — six fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, `tFixture-120` through
  `tFixture-125`, which is this unit's block under the build README's `tFixture-(80 + 10N)`
  allocation. The number space has one owner because three units in this build each claimed the same
  free range once, and a duplicate there does not error — assertions are keyed by fixture name, so a
  collision silently makes one unit's assertions grade a sibling's file. Five ride the harness's
  shared scratch tree, whose conf pins BOTH `SPEC_WITNESS_CUTOFF` and `SPEC_FAILURE_MODE_CUTOFF`.
  The sixth needs the witness key ABSENT, so it takes its own scratch tree and its own conf, which is
  the idiom the §10-evidence and check-6 arms in that harness already use. The six are the WHOLE
  coverage rather than a supplement to it: §8's resolved cutoff sits ahead of every dated spec on
  every ref, so the arm grades zero live specs on the day it lands and the real corpus cannot
  exercise it at all.
- **S7** — the documentation carriers. Item 12 of `tools/memory-tree/HYGIENE.template.md` gains one
  sentence beside its existing sentence naming `SPEC_WITNESS_CUTOFF`, and `KIT_MEMORY_TREE_VERSION`
  advances by one minor in this landing — in the engine constant and in every `gov:kit memory-tree@`
  carrier, the carrier set derived with `grep -rl` at build time. No version pair is written here:
  units at a lower `order` in this build also declare a bump of that constant, so a pair recorded now
  is a no-op or a regression by the time this unit builds.

## 3. Non-goals (OUT)

- **Grading whether the named break would actually fail.** The arm reads SHAPE only. It asserts that
  a criterion NAMES a break; it cannot assert that the break exists, that staging it would red
  anything, or that anyone ran it. A criterion whose failure mode restates its own negation satisfies
  this arm. That liveness lives with whoever observes the staged red, which is the charter's §7 rule
  and the journal record, not this gate. Said here because a structural check reads as a semantic one
  to everybody who did not write it.
- **Moving any acceptance-witness verdict.** S3 restructures the walk an already-armed arm lives in,
  and that restructure is behaviour-neutral for it BY CONSTRUCTION: the witness test keeps its own
  predicate, its own bad-list and its own message, and only the accumulator is shared. AC8 observes
  it. Follow-up: none — a witness verdict that moves is a defect in this unit, not a deferred one.
- **Retrofitting the corpus.** All 479 specs stay untouched — the 414 CLOSED ones and the twenty
  dated 2026-09-04 alike. §8's resolved cutoff grandfathers every one of them by filename date.
- **A `### Failure modes` table or any other second list.** Follow-up: none — it is rejected in §4,
  not deferred.
- **Anything about the acceptance ledger or check 23.** Joining a ledger answer to its criterion's
  tokens is `TOOL-aJoinedCanon-6`. This unit writes only inside check 12.
- **Widening the marker to the phrasings the corpus already uses in prose.** Follow-up: reopen only
  if the fixtures or a later measurement show the single spelling rejecting honest criteria.
- **A new gate leg.** The arm rides check 12, which the `memory hygiene` leg already runs.

## 4. Design

### Data model

One marker, one spelling: `Red when:`. It is matched case-insensitively as the nine-byte string
`red when:` by `index()` over a `tolower()`ed accumulator, which is the dialect-free idiom the §10
terms arm in `tools/memory-tree/check-memory-hygiene.sh` already uses — the block guarded by
`if (want == canon10 && ecut != "" && fdate != "" && fdate >= ecut) {`. The file's own header records
that interval expressions are spelled out character by character to survive an awk build that does
not honour `{8}`; a substring test has no dialect surface at all.

A conforming bullet therefore looks like this, with the clause on a continuation line:

```markdown
- **AC1** — When `check-memory-hygiene.sh` runs over the fixture tree, it names `tFixture-120`.
  Red when: the fixture's only criterion carries no clause and the arm stays silent.
```

**The hoist, as shape rather than as code.** Two liveness booleans are computed once per file from
the same `fdate` the sibling ratchets already use — one for `SPEC_WITNESS_CUTOFF`, one for
`SPEC_FAILURE_MODE_CUTOFF`, each of them the `<key> != "" && fdate != "" && fdate >= <key>`
conjunction every rule cutoff in this engine carries, because blank has to mean OFF and an empty
string compares earlier than every date. The accumulator loop runs when EITHER boolean is true and
is skipped otherwise, so a tree with both keys blank pays exactly what it pays today. At each bullet
close the loop asks two questions of the SAME `acc` string and answers them into two lists: the
backtick test under the witness boolean, the `red when:` test under this unit's. The new cutoff
rides in on its own `-v` binding on the existing check-12 awk, named `mcut` because `fcut` is
already `FORK_MARK_CUTOFF`.

There is no `N/A` escape and no second form. That is the acceptance ledger's own ruling applied one
level up: in `memory/HYGIENE.md`, the bullet headed `**TWO forms and no third.**` allows exactly two
and no `N/A`, on the stated ground
that a third form is how an evidence field becomes a checkbox exercise. A criterion whose break is
merely its own negation costs one clause to write, and the author discovering that the negation is
all there is IS the finding — that is the "criteria that could not fail reached close" case A3 names.

### Inventory

| carrier | change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | one paragraph in the §6 body, beside the paragraph that begins `Once a spec's filename date reaches` |
| `memory/TEMPLATE-SPEC.md` | regenerated by `kit-dogfood-parity.test.sh --render`, never hand-edited |
| `tools/memory-tree/check-memory-hygiene.sh` | the blank preset, one `-v mcut=` on the existing check-12 awk, S3's hoist of the accumulator out of the `wcut` guard, and one test plus one message inside the hoisted loop |
| `.memory-tree.conf` | `SPEC_FAILURE_MODE_CUTOFF` with its date and the reason for that date |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, shipped blank, beside its declared siblings |
| `tools/memory-tree/check-memory-hygiene.test.sh` | `tFixture-120` through `tFixture-125`, their `hit`/`miss` assertions, and one extra scratch tree for the witness-blank fixture |
| `tools/memory-tree/HYGIENE.template.md` | one sentence in item 12; `memory/HYGIENE.md` regenerated |
| kit version | `KIT_MEMORY_TREE_VERSION` one minor forward, in the engine constant and in every `gov:kit memory-tree@` carrier `grep -rl` finds at build time |

### Migration

None. The cutoff is a date compared against a filename, and blanking the key in `.memory-tree.conf`
turns the arm inert. There is no state and no data to move.

### Rollout

Dark by construction, and gated by exactly two things once S3's hoist is in: `SPEC_FAILURE_MODE_CUTOFF`
must be non-blank and at or before the spec's filename date, and check 12's outer shell guard —
`if [ -n "$SPEC_FORMAT_CUTOFF" ]; then` — must hold, so an adopting repo with no spec-format ratchet
receives no failure-mode ratchet either. `SPEC_WITNESS_CUTOFF` is NOT a third gate, and the hoist is
the only reason that sentence is true. Written the obvious way it would have been one, silently, and
worst in exactly the tree that cannot see it: `tools/memory-tree/.memory-tree.conf.example` ships the
witness key blank, so an adopter arming this key alone would have received an arm that never runs
while its own key reads as armed — a demand that evaporates, indistinguishable from one that passed,
which is the shape this unit exists to close.

### Files touched (estimate)

The Inventory table above IS the file list; no count is written here, because the `gov:kit` carrier
set is derived at build time and a number beside it is stale on the next `grep -rl`. Most rows are a
one-line or one-paragraph edit. The engine change is the hoist — an unindent of a loop that already
exists, two boolean assignments, one test and one message — and the fixture file is the bulk of the
diff.

### Alternatives rejected

- **Leaving the test nested inside the witness guard and DECLARING the intersection** — writing down
  that the arm is armed only where the witness ratchet is armed too, and adding a scope item and a
  criterion for that narrower population. Rejected, owner ruling 2026-09-05. It is cheaper by one
  unindent and it is the wrong shape twice over: an arm whose own key reads as armed while a SECOND
  key silently narrows its population is the pass-by-finding-nothing class this build exists to
  remove, shipped inside the unit that names it; and it makes every adopter who arms this key without
  the witness ratchet — the example conf's shipped default — a silent no-op. The counter that lost is
  real and is recorded rather than paraphrased away: an intersection that is written down is honest,
  and the witness fixtures already prove the enclosing walk runs in THIS repo, so the narrower design
  would have been correct here and wrong only downstream. Downstream is where the kit ships.
- **A `### Failure modes` sub-head under §6, one row per AC.** It duplicates the AC numbering into a
  second list that goes stale the moment a criterion is renumbered, which is exactly the unjoined
  seam this build exists to remove. Rejected on the build's own premise.
- **A section-level minimum — §6 mentions one break somewhere.** One line would satisfy ten criteria.
  That is the vacuous-selector class the charter names, and BUILD-METHOD M3's counter-rule refuses an
  observation that passes by matching nothing.
- **Widening the marker to `reds when`, `would red` or `fails when`.** Measured over the tracked spec
  corpus with `git grep -ci`: `would red` appears in 92 specs, `staged break` in 43, `reds when` in
  33, `red-first` in 18. All four are prose, and admitting them would let an incidental sentence
  satisfy the arm. The §10 terms arm took this exact decision and recorded the reason in its own
  comment head, `THE TERMS ARM ACCEPTS TWO SPELLINGS AND WAS DELIBERATELY NOT WIDENED`: a false red
  names its own remedy, a false pass is silent.
- **A `Red when: n/a — <why>` escape.** Rejected on the ledger precedent above.

## 5. Production-readiness checklist

- security — N/A. The change reads tracked markdown and writes nothing.
- perf / scale — one `index()` per accumulated AC bullet inside a loop that already walks them. The
  single batched awk over the whole spec population, the one fed by the `c12_sel` path stream, is the
  shape that took check 12 from ~13 forks per spec down to one pass, and this adds no pass. S3's
  hoist does not widen it either: the loop now runs when either cutoff is live rather than when one
  is, so a tree with the witness ratchet armed pays what it pays today, and a tree with neither key
  set skips the loop exactly as it does today.
- a11y — N/A. No user interface.
- i18n — N/A, and deliberately: the marker is an ASCII literal, which is what makes it safe under a
  mojibake-prone toolchain. The corpus is English-only by construction.
- error / empty / loading states — an empty §6 is already refused by the empty-body walk, the one
  whose finding reads `(section with an empty body`; a §6 with a heading and no AC bullet is outside
  this arm and stays so.
- observability — the finding names the offending bullet's label and the cutoff key, matching the
  witness message that prints `(acceptance bullets naming no backticked witness, required at/after`.
- risks — two. The first is a false-red risk rather than a data risk: a cutoff set behind a live
  spec's filename date reds landed work. §8's resolved date forecloses that at landing, because no
  spec on any ref is dated at or after it, so the residual exposure is a LATER lowering of the key
  and not this landing. Rollback is blanking the key. The second arrived with S3's hoist and is the
  only way this unit can break something that already works: the hoist edits the walk an ARMED arm
  runs in, so a mistake there moves acceptance-witness verdicts across the live corpus. AC8 is its
  observer and the harness's existing witness fixtures are its regression net. There is no
  concurrency and no data loss surface.
- testing + left-shift gates — six fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`.
  That harness is the ONLY arm available: `tools/memory-tree/check-arms.py` cannot see a branch
  inside an awk body, which is why the fixtures are scope and not a nicety.
- migration / rollback — see §4. Blank the key.
- user docs — the §6 body of `memory/TEMPLATE-SPEC.md` and item 12 of `memory/HYGIENE.md`, both
  rendered from their kit templates.

## 6. Acceptance criteria

- **AC1** — When a Tier-2 spec dated on or after the cutoff carries an AC bullet with no `Red when:`
  clause, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 and its output names that bullet's
  label and `SPEC_FAILURE_MODE_CUTOFF`.
  Red when: the branch never fires and the run is silent about `tFixture-120`.
- **AC2** — When that same bullet gains the clause, `bash tools/memory-tree/check-memory-hygiene.sh`
  is silent about `tFixture-121`, with no other fixture change.
  Red when: the marker test matches the wrong string and reds a conforming bullet.
- **AC3** — When the identical clauseless bullet sits in a fixture dated strictly inside
  `[SPEC_FORMAT_CUTOFF, SPEC_FAILURE_MODE_CUTOFF)` in the harness's scratch tree,
  `bash tools/memory-tree/check-memory-hygiene.sh` is silent about `tFixture-122`.
  Red when: the date comparison is dropped and the arm grades the grandfathered era too.
- **AC4** — When the clause sits on a CONTINUATION line rather than the bullet's opening line,
  `bash tools/memory-tree/check-memory-hygiene.sh` is silent about `tFixture-123`.
  Red when: the test is applied to the opening line instead of to the accumulated `acc` string.
- **AC5** — When the clauseless bullet sits in a `Tier-1` spec dated after the cutoff,
  `bash tools/memory-tree/check-memory-hygiene.sh` still reports `tFixture-124`.
  Red when: the test is placed below the `if (hdr ~ /Tier-1/) next` cut, which silently narrows S4 to
  Tier-2 and leaves the harness byte-identical. That cut is cited by its source text and not by line
  number deliberately: three specs in this build gave three different numbers for this one anchor and
  only one was right, and seven units edit this file in sequence.
- **AC6** — When `SPEC_FAILURE_MODE_CUTOFF` is blank in `.memory-tree.conf`, the AC1 fixture passes
  and `bash tools/memory-tree/check-memory-hygiene.sh` prints no failure-mode finding at all.
  Red when: the blank string compares earlier than every date and arms the rule over the whole corpus,
  which is the `mcut != ""` conjunct every rule cutoff in this engine carries.
- **AC7** — When a fixture dated on or after `SPEC_FAILURE_MODE_CUTOFF` carries a clauseless AC
  bullet in a scratch tree whose conf declares that key and declares NO `SPEC_WITNESS_CUTOFF`,
  `bash tools/memory-tree/check-memory-hygiene.sh` still exits 1 naming `tFixture-125`.
  Red when: the accumulator stays nested inside the witness guard, so this arm's real population is
  the intersection of two cutoffs and an adopter arming this key alone gets a dead arm whose own key
  reads as armed. Observed before the arm lands, per AC11.
- **AC8** — When the hoist lands, `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0 and
  `git diff` over that file shows no edit to any existing assertion naming
  `acceptance bullets naming no backticked witness`.
  Red when: the hoist moves an acceptance-witness verdict and the repair taken is to re-baseline the
  assertion rather than the code.
- **AC9** — When the key lands, `grep -qE '^SPEC_FAILURE_MODE_CUTOFF=' tools/memory-tree/.memory-tree.conf.example`
  succeeds and `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0.
  Red when: the key reaches the engine and `.memory-tree.conf` but not the shipped example, which
  reds the self-test's derived example-conf parity arm on this unit's own landing commit — a leg this
  unit's §7 already owes, failing for a reason unrelated to the arm being built.
- **AC10** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs after the edit, it
  reports no drift between `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`.
  Red when: one half was edited and the other was not, which is the build's second rule.
- **AC11** — When each of the six fixtures is staged as a break and the suite is run,
  `bash tools/memory-tree/check-memory-hygiene.test.sh` is observed RED for that fixture before the
  fixture is unstaged, and the observation is recorded per item in this unit's journal record.
  Red when: an arm passes by finding nothing, which is the class this whole unit is about.

## 7. Gates

- `memory hygiene` — the leg that runs check 12 over this tree.
- `memory-hygiene self-test` — the leg that runs `tools/memory-tree/check-memory-hygiene.test.sh`,
  and therefore three things this unit owes it: the six new fixtures, the existing acceptance-witness
  fixtures that are the hoist's regression net, and the derived parity arm that reds when a new
  `_CUTOFF=` preset in the engine is missing from the shipped example conf.
- `kit/dogfood doc parity` — the byte-compare that binds the two template halves together.
- `verdict epoch (kit version dates the engine)` — a new arm changes the engine's verdicts, so
  `KIT_MEMORY_TREE_VERSION` must move in the same landing. Verified at
  `tools/memory-tree/check-verdict-epoch.sh:2-18`.
- `spec tokens (a spec's own names resolve)` — this spec's own backticked names must resolve.
- No new leg, and no new `fail` branch: this arm appends to check 12's existing finding list and
  reaches the tree through the single `fail 12` site, the line beginning `[ -n "$bad12" ] && fail 12`.
  Whether the per-gate `ARMS_FLOORS` pair moves is therefore DERIVED and not pinned — run
  `python tools/memory-tree/check-arms.py --report` at this unit's base sha and again after the
  change, and the pair for this engine must be identical between the two. No pair is written here,
  because units at a lower `order` in this build also add branches to this engine, so a pair recorded
  now is stale before this unit builds.

## 8. Open questions

- **F1 — where `SPEC_FAILURE_MODE_CUTOFF` lands, and whether this build's own specs are its first
  subjects.** Two in-corpus precedents pull opposite ways. `STREAMS_CUTOFF` and `SPEC_WITNESS_CUTOFF`
  were both set strictly ahead of every committed spec so nothing landed went retroactively red,
  which left the required arm with no live data and made the fixtures the only coverage —
  `.memory-tree.conf` records that trade in as many words, in the comment above `STREAMS_CUTOFF`
  ("the corpus does NOT exercise the required arm"). `SPEC10_EVIDENCE_CUTOFF` went the
  other way at `2026-09-01`, and 79 tracked specs are dated at or after it. Setting this one at
  `2026-09-04` would make the twenty specs dated that day its first live subjects, eleven of them
  this build's own, and every one of them would need its criteria amended before the arm could go
  green. **Recommendation: land it at the arm's landing date, strictly ahead of every dated spec on
  every live branch.** The build's third rule says every template change is a dated cutoff and never
  a retrofit, and redding twenty live spec files to buy a live example is the one outcome that makes
  this unit a net loss. The counter is real and is why this is a fork rather than a decision: the
  witness ratchet deliberately made its own spec the first subject, and that bought an example the
  fixtures cannot. Owner's call.

  RESOLVED (owner, 2026-09-05): the recommendation, ruled for the whole build at once. The cutoff
  lands strictly past the newest spec filename date on any ref, which is 2026-09-04 across every
  branch and remote-tracking ref in this tree, and strictly past today as well, because a spec
  minted today would carry today's date and would not sit behind a cutoff set at it. The declared
  value is therefore `SPEC_FAILURE_MODE_CUTOFF="2026-09-06"`. The twenty specs dated 2026-09-04,
  eleven of them this build's own, are NOT its first subjects. The accepted cost is now a fact
  rather than a tradeoff: the arm grades zero specs on the day it lands, and S6's fixtures are its
  whole coverage. The counter-argument above LOST and stays on the record — the witness ratchet did
  make its own spec the first subject and did buy an example the fixtures cannot, and that was
  weighed rather than overlooked.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §2 · §3 · §5 · folded the owner's ruling on F1: `SPEC_FAILURE_MODE_CUTOFF`
  lands at 2026-09-06, strictly past the newest spec filename date on any ref, so no landed spec is
  a subject, S6's fixtures are the arm's whole coverage, and §5's false-red risk is foreclosed at
  landing.
- rev-3 · 2026-09-05 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · folded spec-audit round 1: B1, the owner's
  ruling to HOIST the per-bullet accumulator out of the `SPEC_WITNESS_CUTOFF` guard so this arm's
  population is its own cutoff alone (S3 rewritten, §4 gains the hoist's shape and rejects the
  declare-the-intersection alternative, §3 gains the witness-verdict non-goal, §5 gains its second
  risk, AC7 and AC8 are new); H3, `tools/memory-tree/.memory-tree.conf.example` added as the third
  carrier of the new key in S2, the Inventory and AC9; H1, the fixtures move to this unit's declared
  block `tFixture-120` through `tFixture-125` and the `tFixture-86` high-water claim is gone; H2, the
  `2.59` → `2.60` pair and the `fail 12` site count are replaced by derived statements in S7 and §7;
  M4, AC5's break was named against the wrong line and is now cited by source text. Every line-number
  anchor into a file this build's units share is now a literal-text anchor, which is the only §8 edit
  — F1's ruling, its recommendation and its recorded counter-argument are untouched.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grading each acceptance criterion bullet for a required
clause behind a dated cutoff"` returned no seam that fits. Its top candidates were
`require_adopted_root` in `tools/codebase-map/map_lib.py` and a set of affordance-seam prose hits in
unrelated dossiers, all matched on name stems rather than on behaviour. That is expected and is not a
gap in the map: the seam this unit extends is an awk block inside a shell script, and the map indexes
symbols, inventory keys and dossiers, none of which reach inside `check-memory-hygiene.sh`'s single
batched awk. The seam is named directly instead, verified by reading it: the per-bullet acceptance
accumulator in `tools/memory-tree/check-memory-hygiene.sh`, the block under the comment head
`# ---- acceptance witnesses:`, which already folds each AC bullet's continuation lines into `acc`
and tests that string. The retrieval probe found the record
that built it — `memory/builds/cTracedPromise/spec/2026-08-15-spec-cTracedPromise-2.md`, whose S1
through S7 are the shape this spec deliberately mirrors, down to the doubly-gated cutoff, the
both-tiers claim and the grandfathered fixture whose date must sit strictly inside the pre-cutoff
window. Recall terms used: acceptance witness backticked token SPEC_WITNESS_CUTOFF check 12
per-bullet accumulator continuation line ratchet grandfathered fixture staged red.

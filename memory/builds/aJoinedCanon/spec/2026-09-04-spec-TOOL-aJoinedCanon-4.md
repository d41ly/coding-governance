# TOOL-aJoinedCanon-4 — a criterion names the break that would turn it red

**Status:** CLOSED · rev-6 · 2026-09-06 · node a · Tier-2 · base 750ca0ca · streams tooling · order 4 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md](../build/2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md) | journal | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Make `## 6. Acceptance criteria` ask each criterion what break would turn it red, because authors are
already answering that question in a section that never asked it. Finding A3 measured 93 of 479 specs
mentioning a staged break or a red-first run, clustering in §6 with 79 lines and in §5 with 30. Those
four figures are A3's own, measured over the corpus as it stood at `aWeighedCanon`'s base; the corpus
has grown since — this build's own eleven specs among the additions — so re-deriving them today
returns different numbers. They are cited as that finding's measurement, never as a present count.
The format is collecting the answer by accident, in whichever section the author reached for, and can
therefore neither find it nor check it.

## 2. Scope (IN)

- **S1** — a per-criterion failure-mode clause, marked `Red when:`, stated in the acceptance-criteria
  body of `tools/memory-tree/SPEC-TEMPLATE.template.md`. The clause may sit on the bullet's opening
  line or on any continuation line beneath it, which is the same latitude the acceptance-witness rule
  already grants and matches this corpus's wrap style at 100 columns. Observed by AC12, which greps
  the RENDERED `memory/TEMPLATE-SPEC.md` for the marker text. AC10 does not observe it and never
  could: a byte-compare grades SAMENESS and is equally green when neither half of the pair moved.
  This is the only thing a post-cutoff author ever meets — under §8's ratified cutoff the arm grades
  zero live specs at landing — so it is the half that least tolerates having no observer.
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
  no new `fail` branch. **The "today" in this item is the base sha, not this unit's build day.**
  `TOOL-aJoinedCanon-3` writes into the same guard one `order` step earlier, and its own round-2
  blocker moves its branch out of it, so re-read the block under the comment head
  `# ---- acceptance witnesses:` at this unit's actual base before implementing: if unit 3's fix
  already unindented the accumulator loop, this item reduces to splitting one liveness boolean into
  two. What must hold either way is the PROPERTY and not the diff — the two predicates are
  independent — and AC7 observes that property rather than the unindent.
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
  the idiom the §10-evidence and check-6 arms in that harness already use. That sixth conf declares
  `SPEC_FAILURE_MODE_CUTOFF` and NO other rule cutoff on check 12's awk — not `SPEC_WITNESS_CUTOFF`
  and not `REV_SCOPE_CUTOFF`, `TOOL-aJoinedCanon-1`'s key, which is landed by `order` 1 and so exists
  by the time this unit builds. It costs nothing to widen: those confs are written by a `printf` that
  names each key it wants, so a key it omits is already blank. It buys a second observation on the
  same fixture — AC14, the one-key-armed run — and that is the only criterion in either spec that can
  tell a shared `-v` binding from two independent ones. The six are the WHOLE
  coverage rather than a supplement to it: §8's resolved cutoff sits ahead of every dated spec on
  every ref, so the arm grades zero live specs on the day it lands and the real corpus cannot
  exercise it at all.
- **S7** — the documentation carriers. Item 12 of `tools/memory-tree/HYGIENE.template.md` gains one
  sentence beside its existing sentence naming `SPEC_WITNESS_CUTOFF`, and `KIT_MEMORY_TREE_VERSION`
  advances by one minor in this landing — in the engine constant and in every `gov:kit memory-tree@`
  carrier, the carrier set derived with `grep -rl` at build time. No version pair is written here:
  units at a lower `order` in this build also declare a bump of that constant, so a pair recorded now
  is a no-op or a regression by the time this unit builds. Observed by AC12's second grep for the
  HYGIENE sentence and by AC13 for the version bump. Both halves of this item had no observer at all
  before rev-4 while §7 stated the version obligation outright, which is how an author-facing
  deliverable ships absent with every fixture green.
- **S8** — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` moves to a fresh
  `<ISO datetime> @ <sha>` per that manifest's own stamping rule, which this spec does not restate.
  Not optional and not bookkeeping to taste. Both `tools/memory-tree/check-memory-hygiene.sh` and
  `.memory-tree.conf` sit on that manifest's `watch:` line — read there, not assumed — and this unit
  edits both, so its landing is a watched change, and check C5 of
  `skills/session-kickoff/manifest-check.sh` (`no unaudited watch drift`) is TOPOLOGICAL: it reds
  when the newest watch-touching commit is not an ancestor of the re-stamp, whatever the body delta.
  The `kickoff-manifest ratchet` leg carrying it is `subject: repo` with no `guard` in
  `tools/gate-legs.json`, so it runs on every bar and no scoping avoids the red. `last-body-change`
  does NOT move and §B gains no delta line: this unit changes no gate command, no entrypoint, no
  layout convention and no claim §B front-loads — the manifest names check 12's skeleton scan, a
  different arm, and enumerates none of check 12's rule-cutoff keys — and the charter's rule is
  "no delta → no touch". Observed by AC15. Eight of this build's eleven units owe this and none
  carried it before rev-5.

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
- **Retrofitting the corpus.** Every tracked spec stays untouched — the CLOSED ones and the ones
  dated 2026-09-04 alike. §8's resolved cutoff grandfathers every one of them by filename date. No
  size of that population is written here: `git ls-files 'memory/**/spec/*.md'` derives it, and this
  build's own eleven specs joined it after the 479 A3 measured, so the figure this section used to
  carry was already stale when it was folded.
- **A `### Failure modes` table or any other second list.** Follow-up: none — it is rejected in §4,
  not deferred.
- **Anything about the acceptance ledger or check 23.** Joining a ledger answer to its criterion's
  tokens is `TOOL-aJoinedCanon-6`. This unit writes only inside check 12.
- **Widening the marker to the phrasings the corpus already uses in prose.** Follow-up: reopen only
  if the fixtures or a later measurement show the single spelling rejecting honest criteria.
- **A new gate leg.** The arm rides check 12, which the `memory hygiene` leg already runs.
- **A self-test arm that grades the check-12 awk `-v` namespace for duplicates.** This is spec-audit
  round 3's left-shift for its blocker, and it is NOT built here. Two reasons, and both are stated
  rather than parked, because this build has no round 4. First, subject: it grades the ENGINE's awk
  invocation, not the spec format, so it belongs beside the harness's other structural self-tests
  and not inside the unit whose subject is `## 6. Acceptance criteria`. Second, the predicate the
  review proposed does not work as written, and this was found by running it rather than by reading
  it, per charter §7. `grep -o ' -v [a-z0-9]*=' tools/memory-tree/check-memory-hygiene.sh | sort |
  uniq -d` returns ` -v bp=`, ` -v cut=`, ` -v famalt=` and ` -v m=` on the tree at this unit's base:
  those are re-uses across DIFFERENT awk invocations, which are legal and correct, so the arm would
  red on a clean tree from the commit it landed. The predicate has to be scoped to a single
  invocation — the same command against the one `bad12_raw=` line alone returns empty today — and
  scoping it means teaching the arm where each invocation begins and ends, which is a real design
  question and not a one-liner. **Follow-up:** a `TOOL` backlog row against
  `tools/memory-tree/check-memory-hygiene.test.sh`, carrying both findings above so the next author
  does not re-run the same false-red. The build README's one-owner-per-shared-engine-name rule is the
  interim control, and `TOOL-aJoinedCanon-3`'s namespace registry is where it is written down.

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
rides in on its own `-v` binding on the existing check-12 awk, named **`fmcut`** — failure mode —
and CLAIMED as this unit's alone in `TOOL-aJoinedCanon-3`'s namespace registry.

**Why the name changed at rev-5, and it is the round-3 blocker.** rev-4 said `mcut`, "because `fcut`
is already `FORK_MARK_CUTOFF`". So did `TOOL-aJoinedCanon-1`, for `REV_SCOPE_CUTOFF`, three `order`
steps earlier and on the SAME awk invocation, and a second `-v mcut=` is last-wins for the whole
program: from `order` 4 onward one arm would be graded by the other arm's key while its own conf key
still read as armed. Neither spec's AC6 could see it — each blanks its own key, which under a shared
binding blanks both arms, so both criteria pass with both arms dark. That is this build's own subject
shipped as a defect, in its third disguise. Verified at base before renaming:
`grep -c mcut tools/memory-tree/check-memory-hygiene.sh` is 0, so both units introduce the name and
neither inherits it; the invocation binds `canon canon10 cut10 mroot discalt scut wcut fcut ecut`
today; `fmcut` is free in the tree and in all eleven specs. Unit 1 takes its own distinct name. The
one-letter-plus-`cut` convention is what made the collision reachable — it has four claimants in this
build alone (`jcut`, `rcut`, `bcut`, and this) — so this name is spelled from the KEY and not from a
free letter. AC14 is the observation, and it exists because the review was right that nothing else
here could distinguish a rebind from a correct build.

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
| `tools/memory-tree/check-memory-hygiene.sh` | the blank preset, one `-v fmcut=` on the existing check-12 awk, S3's hoist of the accumulator out of the `wcut` guard, and one test plus one message inside the hoisted loop |
| `.memory-tree.conf` | `SPEC_FAILURE_MODE_CUTOFF` with its date and the reason for that date |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, shipped blank, beside its declared siblings |
| `tools/memory-tree/check-memory-hygiene.test.sh` | `tFixture-120` through `tFixture-125`, their `hit`/`miss` assertions, and one extra scratch tree whose conf declares this unit's cutoff and no other rule cutoff |
| `tools/memory-tree/HYGIENE.template.md` | one sentence in item 12; `memory/HYGIENE.md` regenerated |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp only; no body delta and no `last-body-change` move (S8) |
| kit version | `KIT_MEMORY_TREE_VERSION` one minor forward, in the engine constant and in every `gov:kit memory-tree@` carrier `grep -rl` finds at build time |

**The pre-change baseline AC12 grades against.** `grep -c 'Red when:'` returns **0** on both
`memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`, measured 2026-09-05 at
this unit's base. Zero is what makes AC12 a real observation rather than a restatement: the grep
cannot be non-zero until the rule text exists, so a landing that ships the engine and skips the
template half reds on it. Re-derive rather than trust it — three units at a lower `order` write to
that pair, and any of them adding the string would move the floor off zero.

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
- **Widening the marker to `reds when`, `would red` or `fails when`.** Each spelling's incidence is
  DERIVED, never written here:
  `git grep -cil '<phrase>' -- 'memory/**/spec/*.md' | wc -l` per phrase, run when the question is
  asked. rev-3 pinned four integers and rev-4 replaced them with four fresher integers while telling
  the reader in the same sentence to re-derive rather than quote; re-running the command at rev-5
  found one of those four already moved, one round later, which settles the argument the rev-4 text
  was making against itself. Every spec landed after any measurement moves this population, and this
  build lands eleven. The argument does not rest on the sizes: all four spellings are prose,
  and admitting them would let an incidental sentence satisfy the arm. The §10 terms arm took this exact decision and recorded the reason in its own
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
  spec's filename date reds landed work. §8's resolved date forecloses that at landing — re-derived
  at rev-5, nothing on any ref is dated at or after `2026-09-07` — but the foreclosure is a
  PROPERTY that expires, not a permanent one, and the margin is now one day rather than the two §8
  was ruled with. Re-derive the newest spec filename date on the actual landing day; if it has
  reached the declared value, the ruled property obliges raising the key, not landing under it. The
  residual exposure is therefore a LATER lowering of the key, or a landing that outruns the date.
  Rollback is blanking the key. The second arrived with S3's hoist and is the
  only way this unit can break something that already works: the hoist edits the walk an ARMED arm
  runs in, so a mistake there moves acceptance-witness verdicts across the live corpus. AC8 is its
  observer and the harness's existing witness fixtures are its regression net. There is no
  concurrency and no data loss surface.
- testing + left-shift gates — six fixtures in `tools/memory-tree/check-memory-hygiene.test.sh` for
  the ARM. That harness is the only arm available for it: `tools/memory-tree/check-arms.py` cannot
  see a branch inside an awk body, which is why the fixtures are scope and not a nicety. The fixtures
  cover the engine and nothing else, so the author-facing half — the template paragraph, the HYGIENE
  sentence, the version bump — is covered by AC12 and AC13 instead, as content greps and two gate
  legs. Those three deliverables had zero coverage while all eleven earlier criteria were green.
  Two more deliverables joined at rev-5 and each names its own observer rather than leaning on the
  fixtures: the `-v` binding's exclusive ownership (AC14, on the AC7 tree with every other rule
  cutoff absent) and S8's manifest re-stamp (AC15, on the `kickoff-manifest ratchet` leg).
- migration / rollback — see §4. Blank the key.
- user docs — the §6 body of `memory/TEMPLATE-SPEC.md` and item 12 of `memory/HYGIENE.md`, both
  rendered from their kit templates, both observed by AC12.

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
- **AC6** — When the key is blanked in the HARNESS SCRATCH TREE's conf — not in this repo's
  `.memory-tree.conf` — the AC1 fixture stops being reported and
  `bash tools/memory-tree/check-memory-hygiene.sh` prints no failure-mode finding over that tree.
  Red when: the blank string compares earlier than every date and arms the rule over the whole corpus,
  which is the `fmcut != ""` conjunct every rule cutoff in this engine carries.
  The tree is named because this criterion cannot be graded on the real one: under §8's ratified
  2026-09-07 cutoff the arm grades zero live specs, so a whole-tree run is green with the key set and
  green with it blank, and a criterion whose two arms are indistinguishable observes nothing.
- **AC7** — When a fixture dated on or after `SPEC_FAILURE_MODE_CUTOFF` carries a clauseless AC
  bullet in a scratch tree whose conf declares that key and declares NO `SPEC_WITNESS_CUTOFF` and no
  other check-12 rule cutoff, `bash tools/memory-tree/check-memory-hygiene.sh` still exits 1 naming
  `tFixture-125`.
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
  It grades SAMENESS and nothing else. It is equally green when NEITHER file moved, so it observes S1
  and S5 only in company with AC12, which supplies the content half; on its own it certifies that the
  two files agree about having no rule in them.
- **AC11** — When each of the six fixtures is staged as a break and the suite is run,
  `bash tools/memory-tree/check-memory-hygiene.test.sh` is observed RED for that fixture before the
  fixture is unstaged, and the observation is recorded per item in this unit's journal record.
  Red when: an arm passes by finding nothing, which is the class this whole unit is about.
- **AC12** — When the render has run, `grep -c 'Red when:' memory/TEMPLATE-SPEC.md` returns non-zero
  against the pre-change baseline of 0 that §4's Inventory derives, that file's §6 body names the
  marker, and `grep -n 'SPEC_FAILURE_MODE_CUTOFF' memory/HYGIENE.md` finds the added sentence in item
  12, beside the existing one ending `SHAPE only — that a bullet names something, never that the
  named thing exists.`
  Red when: the engine, the conf and the fixtures all land and the author-facing half does not, which
  every other criterion in this list passes through — AC1 to AC7 and AC11 drive fixtures, AC8 the
  hoist, AC9 the example conf, AC10 a sameness compare that cannot reach `memory/HYGIENE.md` at all.
  Under the ratified cutoff the arm grades zero live specs at landing, so the template paragraph is
  the only thing a post-cutoff author meets, and it was the half with no observer.
- **AC13** — When the landing commit is HEAD, the `kit version markers` and
  `verdict epoch (kit version dates the engine)` legs both pass, which is
  `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` exiting 0:
  `KIT_MEMORY_TREE_VERSION` advanced by one minor in this same commit and every carrier the
  build-time `grep -rl 'gov:kit memory-tree@'` returns moved with it.
  Red when: the new marker test lands on an untouched constant — which is the observed red for this
  criterion, staged deliberately before the bump, since `check-verdict-epoch.sh`'s rule is
  topological and a bump made in an earlier commit than the engine edit does not satisfy it.
  §7 stated this obligation outright while §6 had nothing behind it.
- **AC14** — When the AC7 scratch tree is run — the one whose conf declares `SPEC_FAILURE_MODE_CUTOFF`
  and no other rule cutoff on check 12's awk, `SPEC_WITNESS_CUTOFF` and `REV_SCOPE_CUTOFF` both
  absent — `bash tools/memory-tree/check-memory-hygiene.sh` still exits 1 naming `tFixture-125`, and
  `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0.
  Red when: this arm's `-v` binding is shared with another arm's, so blanking the OTHER arm's key
  blanks this one and the run goes silent with its own key armed. That is the rev-4 `mcut` collision
  with `TOOL-aJoinedCanon-1` exactly, and it is the reason this criterion exists rather than a
  hypothetical: nothing else in either spec can distinguish a shared binding from two independent
  ones, because AC6 and unit 1's AC6 each blank their own key and a shared binding turns both arms
  dark, which reads as a pass on both sides. The criterion sits here and not in unit 1 because
  `order` decides it — unit 1 builds at `order` 1, when this unit's key does not exist and blanking
  it is vacuous.
- **AC15** — When the landing commit is HEAD, `bash skills/session-kickoff/manifest-check.sh` exits 0
  and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` names a sha at or after the commit that edits
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`. `last-body-change` is the SAME
  sha before and after, which is the half of this criterion that observes S8's "no delta → no touch".
  Red when: the engine and conf edits land with the old stamp — check C5, `no unaudited watch drift`,
  reds naming the watched file changed with no re-stamp at or after it. That is the observed red, and
  it is staged by reverting S8 alone. The leg is `kickoff-manifest ratchet`, which is `subject: repo`
  with no guard, so this fires on every bar rather than on a scoped one.

## 7. Gates

- `memory hygiene` — the leg that runs check 12 over this tree.
- `memory-hygiene self-test` — the leg that runs `tools/memory-tree/check-memory-hygiene.test.sh`,
  and therefore three things this unit owes it: the six new fixtures, the existing acceptance-witness
  fixtures that are the hoist's regression net, and the derived parity arm that reds when a new
  `_CUTOFF=` preset in the engine is missing from the shipped example conf.
- `kit/dogfood doc parity` — the byte-compare that binds the two template halves together.
- `verdict epoch (kit version dates the engine)` — a new arm changes the engine's verdicts, so
  `KIT_MEMORY_TREE_VERSION` must move in the same landing. Its rule is topological, not an endpoint
  comparison: the leg's own header states it under `THE RULE IS TOPOLOGICAL, not an endpoint
  comparison.`, and the bump must come at or after the commit that last moved a behaviour-bearing
  line. Observed by AC13. Cited by that literal rather than by a line range, which is the build's
  citation rule and which the rev-3 fold left standing here as `:2-18`.
- `kit version markers` — `bash tools/check-kit-versions.sh`, the other half of S7's version
  obligation: the constant and every `gov:kit memory-tree@` carrier move together. Also AC13. The
  leg was missing from this list entirely while §7's prose demanded the bump.
- `kickoff-manifest ratchet` — `subject: repo` with no `guard` in `tools/gate-legs.json`, so it runs
  on every bar. It is on this list because `tools/memory-tree/check-memory-hygiene.sh` and
  `.memory-tree.conf` are both `watch:` pathspecs of the manifest S8 re-stamps; see AC15 for the
  observed red. The leg was absent from this list while the unit's write set has always owed it.
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
  value is therefore `SPEC_FAILURE_MODE_CUTOFF="2026-09-07"`. The twenty specs dated 2026-09-04,
  eleven of them this build's own, are NOT its first subjects. The accepted cost is now a fact
  rather than a tradeoff: the arm grades zero specs on the day it lands, and S6's fixtures are its
  whole coverage. The counter-argument above LOST and stays on the record — the witness ratchet did
  make its own spec the first subject and did buy an example the fixtures cannot, and that was
  weighed rather than overlooked.

  NOTE (rev-5, 2026-09-05) — appended, not spliced: the ruling above is untouched and still holds,
  and one figure inside it no longer reproduces. It says the newest spec filename date on any ref
  "is 2026-09-04". Re-derived at rev-5 with
  `git log --all --name-only --format= -- 'memory/**/spec/*' | grep -oE '/spec/[0-9-]{10}' | sort -r`:
  the newest is now **2026-09-05**, and eleven specs carrying it are already on `main`
  (`aKeyedAnnotation`, `dTracedLattice`). Nothing on any ref is dated at or after `2026-09-07`, so
  the ruled VALUE still satisfies the ruled PROPERTY — strictly past every spec filename date and
  strictly past today — and the decision needs no re-opening. What changed is the margin: two days
  became one. §5's first risk now carries the expiry condition and the remedy, because a foreclosure
  that rests on a date is not permanent and the rev-4 text read as though it were.

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
- rev-4 · 2026-09-05 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · folded spec-audit round 2 and swept all
  twenty-three of its defect classes over this file. **Named finding H2** — the author-facing half
  had no observer: S1 and S7 now name theirs, AC12 greps `memory/TEMPLATE-SPEC.md` for the marker
  against the 0 baseline §4's Inventory now derives and `memory/HYGIENE.md` for the item-12
  sentence, AC13 puts the `kit version markers` and `verdict epoch` legs behind S7's version bump,
  AC10 is restated as the sameness compare it is, and §5's testing and user-docs rows follow.
  **Swept and HIT:** H1 (§7 demanded the version bump with no criterion and no `kit version markers`
  leg — AC13 and a new §7 row); H3 and H5 (AC10 was a byte-compare standing in for content — AC12);
  H4 and M6 (S1 and S7 had no observer at all — same); H10 (S3 argued from a block
  `TOOL-aJoinedCanon-3` restructures one `order` step earlier — S3 now says its "today" is the base
  sha and points at the property rather than the diff); M1 and M3 (§1's and §3's corpus figures were
  never swept and are stale — §1's are attributed to A3's measurement, §3's are derived); M7 (AC6
  named a whole-tree run that is green either way under the ratified cutoff — it is scoped to the
  scratch tree); L1 (§4's four `git grep` figures were low by 5, 1, 1 and 1 because this build's own
  specs moved the population — re-measured, with the command and the as-of); L2 (§7 pinned
  `check-verdict-epoch.sh:2-18` — now the literal `THE RULE IS TOPOLOGICAL`).
  **Swept and ABSENT:** B1 (this unit is where the hoist was ruled; no arm of it is nested);
  H6 (every command, flag and verb in §6 and §7 was run or read at base — `--check` and `--render`
  on `kit-dogfood-parity.test.sh`, `--report` on `check-arms.py`, the `^KEY=` form in the shipped
  example conf, the derived example-conf parity arm the self-test really carries, and all six leg
  names against `tools/gate-legs.json`); H7 (no criterion here claims an equality a leg does not
  perform; AC10's claim is narrowed rather than dropped); H8 (no criterion is driven by this
  record's own anchors); H9 (the rev-3 claim about literal-text anchors held — the one surviving
  pin was L2's, outside the shared write set, and it is gone anyway); M2 (no line pin into the
  template pair); M4 (all five §7 entries were already leg names, verified against the manifest, and
  `verdict epoch` was already present); M5 (no leg is withheld from §7 on any ground); M8 (this unit
  prescribes no header amendment); M9 (§4's worked example asserts nothing a sibling contradicts);
  M10 (no `Observed by` tag is claimed for more than it covers). Every literal this spec cites into
  `check-memory-hygiene.sh` was re-grepped at base and each one resolves; no count of them is written
  here, for the same reason §3's corpus figure is gone.
- rev-5 · 2026-09-05 · §2 · §3 · §4 · §5 · §6 · §7 · §8 · folded spec-audit round 3, the TERMINATING
  fold — the audit loop exited on M4's convergence rule, so both findings are disposed here and
  nothing is deferred to a further round. **B1, the blocker, half of it this unit's:** the `-v`
  binding is renamed `mcut` → `fmcut`, spelled from the key rather than from a free letter, because
  `TOOL-aJoinedCanon-1` claims `mcut` for `REV_SCOPE_CUTOFF` on the same check-12 awk invocation at
  `order` 1 and the last `-v` wins. §4 gains "Why the name changed", which records the collision, the
  verification that `grep -c mcut` over the engine is 0 so both units introduce it, and the claim for
  `TOOL-aJoinedCanon-3`'s registry; the Inventory row and AC6's conjunct follow. S6 widens the sixth
  scratch tree's conf to declare this key and NO other check-12 rule cutoff, which costs nothing
  because those confs are `printf`-written key by key, and AC14 rides it as the one criterion in
  either spec that can tell a shared binding from two independent ones — placed here and not in unit
  1 because at `order` 1 this key does not yet exist. **H2:** both
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf` are on the kickoff manifest's
  `watch:` line, read there, so S8 is the `last-audit` re-stamp with `last-body-change` held, AC15 is
  its criterion with check C5 as the observed red, and `kickoff-manifest ratchet` joins §7.
  **PROMOTED, not fixed:** round 3's left-shift for B1 — a self-test arm grading the awk `-v`
  namespace — is a §3 non-goal with a named destination, a `TOOL` backlog row against
  `check-memory-hygiene.test.sh`. It is not this unit's subject, and the predicate the review
  proposed was run over the tree and false-reds: unscoped it returns ` -v bp=`, ` -v cut=`,
  ` -v famalt=` and ` -v m=`, legal re-uses across different invocations; scoped to the one
  `bad12_raw=` line it is empty. Both facts are written into the non-goal so the next author does not
  re-run it. **Found by the re-read table, not by the review:** §8 → §5 fired, and §8's ruling states
  the newest spec filename date on any ref "is 2026-09-04", which no longer reproduces — it is
  2026-09-05, with eleven such specs on `main`. The ratified ruling is left intact and carries an
  appended dated note instead; the ruled value still satisfies the ruled property, the margin fell
  from two days to one, and §5's first risk now names the expiry condition and the remedy rather than
  presenting a dated foreclosure as permanent. §4's four `git grep` phrase counts are also gone: they
  were re-derived at rev-5, one of the four had already moved a round after being "re-measured", and
  the deriving command replaces all four integers.
- rev-6 · 2026-09-06 · §2 · §4 · §6 · re-derived the build-wide date at BUILD time: today is
  2026-09-06, a date this fleet can still write into, so `SPEC_FAILURE_MODE_CUTOFF` takes
  `2026-09-07`. `TOOL-aJoinedCanon-1` §4 owns the measurement; rev-5's appended NOTE is untouched
  and its ruled PROPERTY still holds under the new value.

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

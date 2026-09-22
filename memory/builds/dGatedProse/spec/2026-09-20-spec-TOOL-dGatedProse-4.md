# TOOL-dGatedProse-4 — M4 bounds the spec-audit promotion chain by review precision

**Status:** SPECCED · rev-6 · 2026-09-22 · node d · Tier-2 · base bd44d3ff · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md](../build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md) | research | TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-5 |
| [2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md](../reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md) | spec-audit | TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-5 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` M4 gains one sentence bounding the spec-audit PROMOTION chain by
review precision, so a run that keeps promoting over a class no paper audit can close stops at the
round where its own signal degraded instead of discovering the limit by exhausting it. By the
owner's ruling of 2026-09-21 the sentence is paid for two ways. One span M4 does not need is deleted,
because it restates what the unattended Skill and driver already carry, which M1 calls a defect in
M4. And the method's byte budget RISES, priced, with the reason written beside the figure. The same
ruling settles `TOOL-dLoggedFlight-35`: the budget stands, as `TOOL-aHoistedPass-3` made it
enforceable, and moves. A second ruling that day moves the budget's LINE half in the same priced
edit, because the file already stands two lines over the figure M1 states and no checker reads it.
The owner ruled both figures on 2026-09-22: 30720 bytes and 400 lines.

## 2. Scope (IN)

- **S1** — One sentence is appended to M4's `**A BLOCKED verdict has a disposition.**` paragraph in
  `tools/memory-tree/BUILD-METHOD.template.md`, immediately after `the fold is what the next round
  measures.` Its text is fixed in §4 and is 445 bytes. Observed by AC1.
- **S2** — One span is deleted from M4 in the same file, 197 bytes with the space before it, written
  in §4 VERBATIM with the carriers that keep stating it. It is the one span of rev-3's four that the
  reconciled M4 still carries. Observed by AC3, and the carriers' liveness by AC4.
- **S3** — The method's budget moves on BOTH halves. The owner's two rulings of 2026-09-21 raise
  them, and the owner's ruling of 2026-09-22 sets the figures. The byte half goes from 27648 to 30720
  in both places that spell it: the `memory/guides/BUILD-METHOD.md` row of
  `tools/template-size-limits.txt`, with a dated paragraph immediately above the row that prices the
  move and names the question it answers, and M1's `**Budget:` line. The two move in one commit
  because `tools/check-template-size.sh` reds any disagreement between them. The line half goes from
  350 to 400 in M1's `**Budget:` line, its only spelling, since no checker reads it. M1's raise
  history gains one dated entry naming both figures. This S3 is the budget raise rev-4 wrote under a
  label rev-3 used for a different item, which §3's unit-1 edge accounts for. Observed by AC5, AC6
  and AC7.
- **S4** — `memory/guides/BUILD-METHOD.md` is re-rendered from the edited template, never hand-edited,
  because the render is the direction the kit declares. Observed by AC2.
- **S5** — The edit adds no line to either file, and both land inside both raised halves: the
  render at 27936 bytes of 30720 and 352 lines of 400. The line figure covers the 352 the reconciled
  tree leaves, two over the old figure by commits this unit did not make, plus the zero lines this
  unit adds; §4 names those commits and reports what 400 does to M1's sentence on which half binds
  first. Observed by AC6 for the bytes and AC7 for the lines.
- **S6** — Two bullets of `memory/map/features/build-method.md` are refreshed, because the dossier
  describes both things this unit changes: the `M4` bullet names the new bound, and the budget bullet
  under `## Gaps` records the owner's ruling that the budget stands and moves, where it now records
  two opposed rulings and asserts neither. It is PROSE only: no `[claims]` key moves, so no generated
  map artifact goes stale. Observed by AC8.
- **S7** — The rulings get one row in `memory/DECISIONS.md` under this unit's id, carrying the new
  bound and the raise on both halves and citing the owner's rulings of 2026-09-21 and 2026-09-22,
  because `tools/check-template-size.sh:144` names that file as where a raise of this limit is
  recorded. It is this unit's only row there, and the first decision record of any of the three
  rulings. Observed by AC9.

## 3. Non-goals (OUT)

- **No gate, no arm, no checker.** The rule is a documented check. §4 states why, with the evidence,
  and the sentence claims no enforcement the tree does not have.
- **No precision plumbing.** `tools/workflows/unattended-build.js` will not start reading the
  `precision` its callee returns, and the driver's `--review` row grammar gains no field. That fork
  is F1 in §8.
- **No change to `REVIEW_ROUNDS`, to `RUNAWAY_CEILING`, or to the floor's value.** Rounds inside one
  generation stay governed by `REVIEW_ROUNDS` exactly as `TOOL-aProbedUnit-9` ruled on 2026-09-14.
- **The rule the backlog row states is not built.** `TOOL-dLoggedFlight-34` says a promoted
  generation is audited ONCE; the owner replaced that on 2026-09-20 after the dry run. Re-wording the
  row is a build-level write at landing, not this unit's code.
- **No re-wrapping of M4's long paragraph.** That line reaches 1123 CHARACTERS after S1 and S2, 1127
  bytes; the two figures differ because the line carries two em dashes. Both were measured on scratch
  copies, not computed. The file hard-wraps at about 100 elsewhere, so wrapping it would add roughly
  ten lines, about a fifth of the 48 the raised line figure leaves, and AC7 pins the count at 352.
  The long line stays and a future editor is told why here.
- **The wrong arithmetic in `tools/template-size-limits.txt:69-70` is flagged, not fixed.** F3 in §8.
- **No retroactive audit of the corpus's existing chains.** The rule binds the next run.

### Edges

Each sibling bullet below is one END OF A PAIR, and the checker that makes it one is
`tools/memory-tree/check-memory-hygiene.sh:1813-1814`: a **consumes-from** bullet reds unless the
unit it names declares **hands-off** back, and `:1830` is the message a half-declared pair prints.
A **consumes-from** naming a unit whose order is LATER than this one's reds too, at `:1816-1818`, and
every sibling here sits at an earlier order. It is stated here because all five specs of this build
are folding in the same pass — deleting one end and leaving the other is a red on the bar, not a
tidy-up. For the same reason the sibling cites below name a file and a bullet's verb rather than a
line coordinate: a sibling's own fold moves its line numbers, and `tools/check-spec-tokens.py`
resolves a citation's range without reading the cited line.

- **consumes-from** `TOOL-dGatedProse-3` — the kit version moves ONCE in this build and, under the
  main loop's R1-CORRECTED ruling of 2026-09-21, THAT unit owns the move: its S8 moves
  `KIT_MEMORY_TREE_VERSION` to the next increment in its own commit and re-stamps every carrier of the
  `gov:kit memory-tree@` marker with it, the population DERIVED by the marker grep rather than
  listed. Both files this unit edits are in that population — verified on the reconciled tree,
  `git grep -nF "gov:kit memory-tree@2.82"` puts the marker on line 1 of
  `memory/guides/BUILD-METHOD.md` and of `tools/memory-tree/BUILD-METHOD.template.md` — so at order 5
  this unit edits two ALREADY-STAMPED files and owes nothing: no bump, no re-stamp.
  Why order 4 and not order 2, re-derived at source rather than taken from the ruling:
  `tools/memory-tree/check-verdict-epoch.sh:18` states the rule topologically — the NEWEST commit in
  `base..HEAD` that moves a behaviour-bearing line of the engine must be an ancestor of, or equal to,
  the newest commit that changes the constant — and `:179` is the `git merge-base --is-ancestor` that
  tests it. The engine is `tools/memory-tree/check-memory-hygiene.sh` (`:68`) plus six named
  delegates (`:69`), units 1 and 3 both move that engine, and unit 3 is the later of the two. A bump
  at unit 1's order 2 would therefore be OLDER than the last change it claims to date, and the leg
  reds — at THIS unit's bar, the last in the range.
  Two things are relied on and each is checkable. First, that the version the re-stamp leaves is FOUR
  characters: the re-stamp is byte-neutral only while it is, and every byte figure in §4 is measured
  at base `bd44d3ff`, where the marker reads `2.82`. `2.82` and its next increment `2.83` are four
  bytes each and the carrier line is `<!-- gov:kit memory-tree@X -->` in both files, so the stamp
  rides through this unit's write set at zero cost; a five-character version would add one byte to
  each file and move §4's pair. Second, that unit 3 leaves `kit version markers` green, since that leg
  is unguarded and this unit's bar is the last one that can catch it.
  Two further crossings ride this same edge and neither is a dependency. That unit's render pass
  rewrites `memory/guides/BUILD-METHOD.md` from the template, because the render loop iterates the
  whole `PAIRS` list (`tools/memory-tree/kit-dogfood-parity.test.sh:58`, four pairs, looped at `:100`)
  rather than the pair a unit edited — which is this unit's own direction of travel in S4, so it
  reproduces rather than threatens it. And that unit raises the hygiene GUIDE class caps to the pair
  the owner re-ruled on 2026-09-21, 98304 bytes and 1200 lines, which supersedes the 81920/1000 of
  that day's first ruling, against the `61440`/`750` at `tools/memory-tree/check-memory-hygiene.sh:84`
  today, with check 6's guide selector being the `memory/guides/` prefix at `:733`. That unit folds
  after this one and states the pair itself; at 27936 bytes and 352 lines this file clears every pair
  named here, so nothing in this spec turns on which one it states. The cap that actually binds this
  file is the far tighter per-subject row at `tools/template-size-limits.txt:86`, read by a different
  checker — the row S3 moves.
- **consumes-from** `TOOL-dGatedProse-1` — that unit's marker is NOT what this unit reads, and two
  other things are. It edits the engine at order 2, which is one of the two behaviour-bearing moves
  the epoch rule above ranges over, so a mis-placed bump in this build surfaces at this unit's bar
  rather than at its own (§7). And its S8 edits `tools/memory-tree/HYGIENE.template.md` and lands
  through `memory/HYGIENE.md`, which the kit's render is the declared direction for — so its render
  pass also rewrites this unit's guide from the template, byte-identically, because nothing in this
  unit's write set has moved at order 2.
  This end of the pair exists because that unit declares **hands-off** `TOOL-dGatedProse-4`. If its
  fold drops that bullet, this one goes in the same commit — the rule at the head of this section
  reds whichever half is left alone.
  Under the owner's O2 ruling of 2026-09-21 a third thing crosses, and it is a GRADING rather than a
  write: that unit's new check 25 declares no `READER_INVENTORY_CUTOFF`, so it grades every live spec
  from the commit that lands it, and THIS SPEC is one of them. **No item of this spec fires check 25,
  and none carries a `**Readers:**` clause or owes one.** Re-derived over rev-6's §2 against the
  trigger that unit's S2 declares, O5's past tense and O6's markdown paths included: S2 carries the
  past-tense `deleted` and NO backticked token, so neither the five identifier shapes nor the
  kind-noun shape can reach it, since both test a backticked token; S1 and S3 to S7 carry no verb
  from the list.
  **The one item that did fire is DELETED, and its label now names something else.** Rev-3's S3 was
  the pointer repair to the review protocol. It carried the strict-list verb `removes` beside the
  backticked `memory/guides/REVIEW-PROTOCOL.md`, which the slash shape admits under O6, and the
  round-1 audit's M3 said so at
  `memory/builds/dGatedProse/reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md:353-354`.
  That item went with the D4 deletion it repaired (§4). Rev-4 then gave the label S3 to the budget
  raise, and the label AC5 to the check of the raised row, where rev-3's AC5 observed the pointer. So
  a statement that unit 4's S3 carries `removes`, in that record or in a sibling written against rev-3
  or rev-4, describes the deleted pointer repair and never today's S3, which carries no list verb.
  The labels stay where rev-4 put them, because moving them a third time would move again the ids the
  siblings folding after this one read. If a fold widens the trigger to an unbackticked item, the
  remedy is in this file and is two lines: S2 gains a `**Readers:**` clause, which is the
  false-positive cost that unit already prices at one line per item.
- **consumes-from** `TOOL-dGatedProse-2` — declared at rev-3, and its absence at rev-2 was a LIVE RED
  rather than an omission. Reproduced by running the gate on this tree, not inferred: at rev-2 check
  12 printed that this spec is named **hands-off** by `TOOL-dGatedProse-2` and declares no matching
  **consumes-from** back, under the heading "one author read the handoff and the other never saw it".
  Re-run after this bullet landed, it passes.
  That unit's own bullet says the crossing is "nothing" on the write side, and that is right — its
  write set, read from its own `### Files touched`, is disjoint from this unit's — but the mirror is
  still owed, and `memory hygiene` is on this unit's keep-green list in §7.
  What does cross is the same O2 consequence: that unit's `claims` join declares no cutoff either, so
  it grades every live spec from its landing commit, this one included. Read against the arms it
  declares, this spec clears, and the reading is written down so a fold that widens an arm is checked
  against it instead of re-derived. Two sentences here are claim-shaped. §4's inventory sentence
  backticks `[paths] globs` and `build-method size`, and a token carrying a SPACE is exempt from all
  three refusal classes before any other test. That same sentence also backticks the two BUILD-METHOD
  paths, which WOULD refuse as PATH if an arm matched it — none does, because every arm is anchored on
  a backticked dossier subject and needs a claim verb between that subject and the run of objects, and
  there the dossier path is followed by an em dash and the run with no verb between them. AC8's
  sentence is the other, and its verb is `is read`. If a fold widens the filler run or the verb set,
  the remedy is again in this file and is prose: the inventory sentence is re-worded so the two paths
  do not sit in a run behind a dossier subject.
- **consumes-from** `TOOL-dGatedProse-5` — declared at rev-4, and the mirror is that unit's
  **hands-off** `TOOL-dGatedProse-4`; if its fold does not carry that bullet, this one reds check 12
  and goes in the same commit. What crosses is its corpus pass. That unit lands at order 1 and writes
  a `**Readers:**` clause on every item unit 1's trigger fires on, in every live spec, this one
  included, re-deriving that population at its own base rather than trusting its census. Its census
  was first taken over rev-3, whose S3, the deleted pointer repair, fired and was rated GENUINE. Its
  rev-6 has already dropped that census row and deleted its AC15, retiring the id rather than reusing
  it, so that spec no longer counts the deleted item in its population. This spec's §2 carries no
  item that fires, per the unit-1 edge above, so the pass has nothing to write here. That spec also
  lists this spec's S2 in the class that carries a list verb and no backticked token, which is where
  the unit-1 edge puts it.
- **consumes-from** external — the precision figure this rule reads. It exists only as prose in a
  review record, written by the synthesis agent because `tools/workflows/tier2-review.js` interpolates
  it into that agent's prompt (`:506`). The run-state file carries the DISPOSITION this rule produces
  and never the PRECISION it reads: verified, `memory/builds/dMispairedQuote/RUN.md` answers zero for
  `precision` and for every one of the five figures §4 cites, while `:53` and `:63` carry
  `disposition promote` and `disposition fold` on their review rows.
- **consumes-from** external — the owner's three rulings. The first, of 2026-09-21, settles B1 and
  `TOOL-dLoggedFlight-35`: keep the rule in M4 and raise the byte cap with a priced reason, so the
  budget stands and moves. The second, the same day, moves M1's line half with the byte cap, in the
  same priced edit, and names no figure. The third, of 2026-09-22, sets both figures: 30720 bytes and
  400 lines. Together they authorise S3 and every M1 edit, the figures included, and this unit grants
  itself none of it: M1 records every budget figure as an owner call, and M3's delegation does not
  reach M1's own budget. All three reached this spec as the main loop's relay of the owner's own
  conversation, and no decision record carries any of them yet. S7's row, which the build pass
  writes citing them, is the first, and `tools/check-template-size.sh:144` names
  `memory/DECISIONS.md` as where a raise of this limit is recorded.
- **hands-off** external — whether the bound ever becomes machine-enforced. §4 records why no
  predicate should be wired on this shape today; the measurement that would change that answer is
  named there.
- **hands-off** external — the backlog row `TOOL-dLoggedFlight-34`, whose text states the superseded
  rule and is re-worded at landing.
- **hands-off** external — the backlog row `TOOL-dLoggedFlight-35`, which this unit answers and which
  closes at landing citing it, with the build README's sentence calling that row "not this build's"
  re-worded in the same landing. Both are build-level writes, as the `TOOL-dLoggedFlight-34` row is.

## 4. Design

### The sentence, verbatim

It is appended to the existing paragraph, on the same line, at the point where S2's deletion leaves
that line ending, so no line is added:

```
 **The CHAIN of promotions is bounded by PRECISION.** Each takes a FRESH subject, so `REVIEW_ROUNDS` re-arms per subject and bounds no chain of them. A PROMOTING round whose precision, which its own record states, falls below the review protocol's floor ENDS the chain: its promotions are built from their specs as written, and where `specs-audited` is owed they close under a recorded override of it, because the run CLOSES units no audit names.
```

Four words are load-bearing and each closes a defect the dry run's skeptic reproduced, as this
build's research record carries them at
`memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md:410-434`.
A fifth clause is load-bearing because the tree moved under rev-3.

**PROMOTING.** The round whose precision decides the chain is the one that disposes, not any round.
Unit 1's spec audit in `dMispairedQuote` ran two rounds at precision 0.28 then 0.57, and only the
second promoted. The two halves come from two carriers, which is the point of the table below: the
figures are at
`memory/builds/dMispairedQuote/reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md:32`
and `...-round2.md:28`, and the dispositions are at `memory/builds/dMispairedQuote/RUN.md:49`, which
carries no disposition, and `:53`, which carries `disposition promote`. A rule reading "a round" would
have ended that chain on the first, which promoted nothing.

**CHAIN, against ROUND.** Rounds inside one generation keep their `REVIEW_ROUNDS` bound, so a
generation that converges over several rounds stays correct. `TOOL-dMispairedQuote-3` is that case:
the promoted generation was audited three times at 0.48, 0.53 and 0.63
(`...-3-spec-audit-round1.md:55`, `...-round2.md:77`, `...-round3.md:72`) and exited
`disposition fold` at `memory/builds/dMispairedQuote/RUN.md:63`, the best outcome in the corpus. The backlog row's "audited once" outlaws it; this sentence does not.

**bounds no chain of them**, against the draft the skeptic refuted, which said nothing COUNTS
generations (that record, `:415-416`). Something does, and the code is explicit about it.
`tools/workflows/unattended-build.js:263` keeps `roundNo`; `:265` keys the subject
`<slug>-spec-set-r<N>` from `subjectRound`, which `:264` defaults to `roundNo` and `:285` refuses
above it — the `-r7` in `memory/builds/dLoggedFlight/RUN.md:165` IS that key. The chain is counted
too: on a promotion `:1489-1491` prescribes re-invoking at `round: roundNo + 1` **with no
`subjectRound`**, "so they take a fresh subject". What no code does is BOUND it, and `:813-818` is
why. The round handed to the reviewer is `roundNo - subjectRound + 1`, and that expression's own
comment reads "1 for a fresh generation, N for its Nth fold" — so a fresh subject resets it to 1. The
bound at `tools/unattended/unattended.sh:4833` then reads `RUNAWAY_CEILING` only when the subject is
the build slug and `REVIEW_ROUNDS` otherwise, so both counters re-arm per generation and neither ever
sees the chain.

**the review protocol's floor**, named rather than spelled. The value lives in
`memory/guides/REVIEW-PROTOCOL.md:198`, an M11 carrier, and writing `0.5` into M4 would be the defect
M1 names. M4 cites that carrier by path at `memory/guides/BUILD-METHOD.md:129`, thirteen lines above
this sentence, and the preceding `(protocol §8)` refers to `memory/guides/UNATTENDED-PROTOCOL.md:470`,
so the adjective is what keeps the two apart.

**where `specs-audited` is owed.** Rev-3 wrote the override as owed "because the run CLOSES units no
audit names", with no condition, and on the reconciled tree that ground is false for most builds.
`TOOL-aBlindedTrial-6` made the audit opt-in and `TOOL-aBlindedTrial-7` added a project-wide default,
so `specs-audited` is owed only when the build README at BASE declares `spec-audit:`, or the project
conf declares `SPEC_AUDIT_DEFAULT` and the README declares no key; otherwise it is MET with an
announced `not owed` (`memory/guides/UNATTENDED-PROTOCOL.md:357`). This repo's `.unattended.conf:221`
declares that default blank. The clause therefore names the override only where the item is owed,
which is how the unattended Skill states the same case for a promoted unit that closes un-audited
(`.claude/skills/unattended/SKILL.md:737-740`). A chain mostly forms where the audit is owed anyway,
so the condition rarely bites; it is written for the build that audits voluntarily, which M4 calls
recommended and never owed, and where an override would record nothing.

### Where precision is computed, recorded, and NOT read

| fact | site | what it means for this rule |
|---|---|---|
| computed | `tools/workflows/tier2-review.js:452` | `confirmed / (confirmed + refuted)`, unjudged findings excluded |
| logged | `tools/workflows/tier2-review.js:465` | the runner's own `precision < 0.5` note, the same floor |
| recorded | `tools/workflows/tier2-review.js:506` | interpolated into the synthesis prompt, so the RECORD states it |
| returned | `tools/workflows/tier2-review.js:684` | `precision` is a field on the success object, and `:478` on the early return |
| not read | `tools/workflows/unattended-build.js:826` | the string appears ONCE in that file, in a comment listing the callee's returns, and nowhere in code |
| not carried | `tools/unattended/unattended.sh` | the string does not appear at all; the `--review` row grammar is `verdict · blockers N · <exit> · disposition <v>`, written at `:4875` |
| the CONSEQUENCE is carried | a build's `RUN.md` | `disposition promote` / `disposition fold`, at `memory/builds/dMispairedQuote/RUN.md:53` and `:63` |

Counts DERIVED at base `bd44d3ff`: `precision` occurs 11 times over 9 lines in `tier2-review.js`, once
in `unattended-build.js`, zero times in `unattended.sh`. So the number the rule turns on is durable in
the review record and invisible to every downstream consumer, while the DISPOSITION it produces is on
the run record and machine-graded. That asymmetry is the whole basis of the next subsection, and it is
also why every figure above cites a review record rather than a `RUN.md`. One caveat on the two
disposition rows, because they are the oldest evidence here:
`memory/builds/dMispairedQuote/RUN.md:16-17` records that `--review --disposition` did not exist when
those rounds ran and that both values were RECONSTRUCTED by hand under `TOOL-dFoldedVerdict-3`.
Today's driver writes them; those two rows were written about it.

### Why this is a documented check and not a gate

One half of the consequence IS machine-forced where the audit is owed, and the sentence says only
that much: `specs-audited` is a machine DoD item (`memory/guides/UNATTENDED-PROTOCOL.md:357`) that,
when owed, refuses a CLOSED unit no tracked `**Serves:** spec-audit` record names, so a run in such a
build that stops the chain and closes the promotions must record `--override specs-audited`. That is
why the sentence ends with the ground for the override rather than asserting it is automatic: the
item grades the CLOSE, so a run that leaves the promotions non-terminal owes a different override
and no `specs-audited` one at all.

The STOP itself is enforced by nothing, and two measurements say it should stay that way.

- **"How many records state a precision" has no answer until the predicate is named, and the three
  honest predicates disagree by a factor of nine.** Derived at base `bd44d3ff` over
  `git ls-files 'memory/builds/*/reviews/*.md'` — 403 tracked records, 109 of whose filenames say
  `spec-audit` — each figure being the record count matching one `grep -lEi` pattern:

  | predicate | pattern | states | silent | spec-audit states / silent |
  |---|---|---|---|---|
  | A — the bare word | `precision` | 302 | 101 | 97 / 12 |
  | B — the word plus a 2dp figure on one line | `precision.*[0-9]\.[0-9]{2}` | 284 | 119 | 94 / 15 |
  | C — the shape line the synthesis prompt prescribes | `^- raw .*precision [0-9]\.[0-9]{2}` | 33 | 370 | 24 / 85 |

  A is too loose to be a figure at all — it matches the word in prose. C is the only one keyed on the
  grammar `tools/workflows/tier2-review.js:506` actually asks the synthesis agent for, and it finds
  33 records of 403. A checker would pass the other 370 in silence, which is the green-by-absence
  class the charter §7 names. Liveness: C's 33 include all five `dMispairedQuote` spec-audit records,
  the corpus instance this whole rule is built on, so a zero elsewhere is a finding and not a broken
  probe. At base `fcbfba5f` the same three patterns found 286, 268 and 33 of 387: sixteen records
  later C has not moved, so the prescribed line is not spreading on its own. A figure whose predicate
  is unwritten cannot be re-derived, and the SPREAD is the actual argument.
- **A predicate keyed on the review subject grades only the harness era.** The dry run's census
  reported at least four spellings of the spec-audit subject key, and its skeptic a whole era
  recorded under unit-id subjects, `dMispairedQuote`'s two-generation chain among them, which the
  census's own rule drops by construction. This build's research record carries both, at
  `memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md:401-402`
  and `:410-412`. Re-derived here rather than inherited, OWN-PROBE at base `bd44d3ff` over the 58
  tracked run-state files, with an untracked probe, so the figures are PINNED: of 260 review rows,
  142 carry a unit-id subject and 73 the bare slug of a closing review, and the spec-set generations
  are spelled `<slug>-spec-set` on 15, `<slug>-spec-set-r<N>` on 9, a bare `spec-set` on 7 and
  `<slug>-specs` on 7, while 7 more carry one-off subjects, a review-record filename stem among them.
  Stage 1 concluded that no predicate should be wired on this shape (`:401-402`), and the skeptic's
  narrowing proposes none (`:432-434`).

What would change the answer is a precision FIELD on the `--review` row, which is F1 in §8 and is
outside this unit. Until then the rule is prose, and the build README's own rules slot already binds
this build to the dry-run-before-wiring discipline.

### What it pays with

`memory/guides/BUILD-METHOD.md` measures 27641 bytes of a declared 27648 at base `bd44d3ff`, and 352
lines against the 350 M1 states. Seven bytes are free, and the sentence costs 446 with the space that
joins it to its line. Rev-3 paid for it with four deleted spans and an 18-byte pointer repair,
measured at `fcbfba5f`. On the reconciled tree three of those spans and the pointer text are gone:
`TOOL-aBlindedTrial-5` (`a33237c4`) rewrote D2, D3 and the pointer, and that build's closing-review
fold (`315201b0`) rewrote D4. The owner ruled on 2026-09-21 that the rule stays in M4 and the cap
rises, ruled the same day that the line half rises with it, and ruled both figures on 2026-09-22.
So the payment is now two things.

**First, the one deletion that survives.** D1 is still in the reconciled M4, at the end of
`memory/guides/BUILD-METHOD.md:142`, and is still what M1's own rule makes a defect in M4: "nothing
here is stated anywhere else in this repo".

| # | deleted from M4 | bytes | where it still lives |
|---|---|---|---|
| D1 | the runaway-ceiling sentence, from `A runaway ceiling backstops` to `BUILD-LEVEL RULES slot.`, PLUS the single space separating it from the sentence before — the span alone is 196, and since it ends line 142 that space would be left as trailing whitespace | 197 | `.claude/skills/unattended/SKILL.md:741-743` and its kit template `tools/unattended/SKILL.template.md:741-743` state it; `tools/unattended/unattended.sh:4884` EMITS it at the exit, and `:4691` states the backstop in the driver's own comment |

The span, VERBATIM, with the space that precedes it; it is the whole remainder of that line, and the
same bytes in the template:

```
 A runaway ceiling backstops a defect in the predicate; reaching it is itself a defect, so the run promotes and lands anyway and says so in its output AND the build README's BUILD-LEVEL RULES slot.
```

D1 needs one more note, because it restates an owner ruling and deleting it must not lose one.
`TOOL-aBoundedVerdict-1` fork F4, RESOLVED by the owner on 2026-08-19, mandated that a ceiling firing
be said loudly in TWO carriers: the run's own output and the build README. Both survive this deletion
— the driver emits the first and the Skill states the second. M4 was a third copy. What M4 alone
added is the README slot's NAME, `BUILD-LEVEL RULES`; F4 ruled "the build README" and named no slot,
so the deletion loses a specificity no ruling asked for, and the slot itself stays named in the
method by M2's classification sentence at `memory/guides/BUILD-METHOD.md:43`.

**The three spans that no longer exist, and why their successors stay.** Rev-3's D2, D3 and D4 — the
strictly-smaller illustration, the corpus observation about verdict lines, and the STOP clause — are
now aBlindedTrial's own shorter text, days old. This unit does not delete that text. The owner's
ruling chose the raise as the payment, and funding this sentence by cutting a sibling's fresh fold is
how a payment goes stale under its spec, which is what happened to rev-3. D4's successor also still
carries the STOP obligation in M4 (`then **STOP** once a synthesis pass calls the design clean`), so
the pointer repair rev-3's S3 bought protects nothing now. That item is deleted with the span it
repaired, and the label S3 now names the budget raise, a different item.

**Second, the raise.** Every figure below was measured by applying the edit to scratch copies of both
files at base `bd44d3ff` and weighing them CR-stripped, as the checker does, and re-measured at rev-6
with the owner's figures in M1.

| quantity | bytes |
|---|---|
| the render at base `bd44d3ff` | 27641 |
| the sentence, with its joining space | +446 |
| D1, with its separating space | −197 |
| M1's dated raise entry, `, then both to ≤30720 / ≤400 on 2026-09-22`, where `≤` is three bytes | +46 |
| M1's `**Budget:` byte figure, 27648 → 30720, the same digit count | 0 |
| M1's `**Budget:` line figure, 350 → 400, the same digit count | 0 |
| the render after the edit | 27936 |
| over the old row | 288 |
| the new row, 30 KiB, the owner's figure | 30720 |
| headroom left | 2784 |

M1 changes in two places, both on existing lines. Line 8's `**Budget: ≤27648 bytes, ≤350 lines**`
becomes `**Budget: ≤30720 bytes, ≤400 lines**`, a spelling check 6 parses: its sed at
`tools/check-template-size.sh:129` reads the digits before ` bytes` and nothing after them. Line 11's
`the BYTE half to ≤27648 on 2026-09-05` gains `, then both to ≤30720 / ≤400 on 2026-09-22`, the shape
the same history already uses for the 2026-08-21 raise of both halves, so it ends at the figures
line 8 states rather than one raise behind them. It is dated 2026-09-22, the day the owner ruled the
figures, because M1 records each raise as an owner call. That line becomes 144 characters and 154
bytes and stays one line. M1 gets no reason sentence: its history names each raise as an owner call,
the byte half's reason lives beside its row, and both figures are the owner's. What 400 does to M1's
sentence that the BYTE half binds first is a consequence, reported below.

**The figures are the owner's.** The owner ruled them on 2026-09-22: 30720 bytes and 400 lines. M1
records every budget figure as an owner call, "a stated constraint of a document rather than a
measurement of one" (`memory/guides/BUILD-METHOD.md:11-12`), and M3's delegation does not reach M1's
own budget (`:79-80`), so no argument in this spec decides either figure and none is offered. What
remains is what the figures measure out to. The raise is 3072 bytes, of which this landing uses 288.
30720 is 30 KiB, so the row stays on the KiB-round convention every row of
`tools/template-size-limits.txt` follows today — 48, 18, 63 and 27 KiB. And every byte of that
ceiling is a byte a run may pay at every pass boundary, because M7 re-reads this file WHOLE there,
which is M1's own reason for the budget and §5's fourth risk.

**What the 2784 are for.** About 28 lines at the ~100-byte prose line M1 names, and about 35 at the
file's measured average of 79 B. They are reserved for nothing this unit knows will land. They let
the next edits to the method pay for themselves in their own commits instead of in a deletion hunt.
Two candidates are in view and neither is promised: F1's follow-up, a precision field on the
`--review` row, would re-word this unit's own sentence; and `TOOL-dHonouredPark-5`, an OPEN row, asks
M4 to carry an orchestrator-ids rule. When the 2784 are spent, the next raise is the owner's again,
which `tools/check-template-size.sh:144` says in its own failure text.

**Where the reason lives.** Beside the figure: a dated paragraph immediately above the row in
`tools/template-size-limits.txt`, whose header requires that every movement of a value be argued next
to it (`:3-4`). It sits below the row block's existing paragraphs, so the anchors into them hold. It
NAMES the sentence it funds and does not restate it, because that file is a registered method carrier
whose descriptor at `memory/project/method-carriers.txt:21` says it never restates what the method
says. The intended text, with its measured figures re-read at landing:

```
# RAISED 27648 -> 30720 = 30 KiB, owner rulings 2026-09-21 and 2026-09-22 (TOOL-dGatedProse-4),
# which also settle TOOL-dLoggedFlight-35: the budget STANDS, as TOOL-aHoistedPass-3 made it
# enforceable, and moves. On 2026-09-21 the owner kept the M4 sentence TOOL-dGatedProse-4 adds and
# chose a raise over paying for it in deletions; on 2026-09-22 the owner ruled this figure. The
# render measures 27936 with it, 288 over the old row, and the row leaves 2784 bytes, about 28
# prose lines, reserved for nothing. Spent, it is the owner's again. The same rulings moved the
# document's LINE half with this row, in the same edit. No checker reads that half (above), so its
# figure is spelled in the document alone.
```

The same file's pair comment at `tools/template-size-limits.txt:72` spells the figure as
`**Budget: ≤27648 bytes`. It is re-worded on the same line to say the method's `**Budget:` line
spells this row's figure, without spelling a number, because a figure typed there goes stale at
every raise, this one included. M1 carries the dated figures in its raise history, and
`memory/DECISIONS.md` carries S7's row, which the build pass writes citing the three rulings. That
index's entries are capped at 300 by check 7, whose `length()` counts characters or bytes by the
awk's locale, and the intended row is 293 characters and 295 bytes, under the cap either way:

```
- **TOOL-dGatedProse-4** — **M4 bounds the promotion chain by review precision; the method's budget moves to 30720 bytes and 400 lines**: owner, 2026-09-21, keeping the rule and raising both halves over a trim; 2026-09-22, ruling the figures; the budget stands, settling TOOL-dLoggedFlight-35.
```

**This unit answers `TOOL-dLoggedFlight-35`.** That row records two opposed rulings on the method's
size budget: `TOOL-aHoistedPass-3` made it enforceable with the `build-method size` leg and the row,
and `TOOL-aHonedRuleset-6` ruled the declaration deleted. The owner's ruling of 2026-09-21 settles
it: the budget STANDS, as `TOOL-aHoistedPass-3` enforced it, and moves, to the figures the owner
ruled on 2026-09-22. So this unit edits the M1 passage rev-3 refused to touch, on those rulings
rather than on its own authority, and the row closes at landing citing this unit (§3).

**The advisory high-water behaves as F4 decided.** Re-verified on the reconciled tree:
`tools/template-size-highwater.txt:3` still holds 26941, the checker warns at +700 today and warns at
+995 after this edit, and exits 0 both times. The raise touches only the declared ceiling. The
high-water record is the other half of the separation the limits file's header draws at `:10-13`,
and this unit does not `--bump` it.

**The LINE half, whose breach it was, and what 400 does to M1's sentence.** M1 states ≤350 lines
and the file is 352 on the reconciled tree. The breach arrived on aBlindedTrial's branch: its
reconcile merge `f883bbda` joined a 348-line side to a 350-line side and produced 351, and its
closing-review fold `315201b0` made 352. It landed green because no checker reads the line half,
which `TOOL-aHoistedPass-28` prices. This unit adds no line, because the sentence takes D1's place at
the end of an existing line, so the count stays 352. The owner ruled on 2026-09-21 that the line half
rises with the byte cap in the same priced edit, so the new figure must cover 352 plus the zero lines
this unit adds, and ruled the figure on 2026-09-22: 400, which leaves 48.

M1 says the BYTE half binds first: at this file's ~100 B prose line the bytes run out well before the
line figure does, so most of that figure is headroom the bytes do not grant. That sentence has been
false since the breach. What 400 does to it is a consequence of the owner's figures to report, not a
reason for either, and it restores HALF of the sentence. After this edit the 2784 free bytes buy
about 28 lines at M1's ~100 B, running out near 380, and about 35 at the file's measured average of
79 B a line, running out near 387. Both are under 400, so the bytes run out first on both readings:
the byte half binds first again. The sentence's second clause stays false. At M1's own reading about
20 of the 48 lines the figure leaves are headroom the bytes do not grant, and at the measured average
about 13, so that headroom is a minority either way, never "most of that figure". Re-wording M1's
budget prose is the owner's under M1 and M3, so this unit reports the false clause rather than
editing it; F6 carries the question. The figure costs no byte, because 400 has the digit count of 350.

### Measured cost of the whole edit

Applied to scratch copies at base `bd44d3ff` on node d, 2026-09-21, and re-applied there on
2026-09-22 with the owner's figures in M1, which moves none of the figures below:

| file | before | after |
|---|---|---|
| `memory/guides/BUILD-METHOD.md` | 27641 B · 352 lines | 27936 B · 352 lines |
| `tools/memory-tree/BUILD-METHOD.template.md` | 27666 B · 352 lines | 27961 B · 352 lines |

446 in, 197 out and 46 into M1's history: net +295 bytes and no line on both, because every edited
line is identical in the template and the render. The sentence measures 445 bytes, and the long line
becomes 1123 characters at 1127 bytes. `render_doc` over the edited template is byte-identical to the
edited render. The checker was pointed at the edited render with a scratch limits file and a scratch
high-water row of 26941: with the row at 30720 it prints the high-water WARN and `template-size OK`
at 27936 / 30720, 2784 under, and exits 0; with the row left at 27648 while M1 says 30720 it fails
check 6 and exits 6; and with both at 27648 it fails check 2, 288 over, and exits 1. The
kit-version re-stamp `TOOL-dGatedProse-3` owns moves none of it, because `2.82` and its next
increment are four bytes each.

### The carrier — a render, not byte identity

`tools/memory-tree/BUILD-METHOD.template.md` is the authored source and
`memory/guides/BUILD-METHOD.md` is this repo's render of it. The comparison substitutes rather than
strips: `render_doc`, canonical at `tools/lib/render-doc.sh` and inlined byte-identically into the
parity test, drops CR and substitutes THREE tokens — `{{KIT_DIR}}`, `{{TOOL_ROOT}}` and
`{{READINESS_ROWS}}`. Read from the function body, not from that file's header comment, which still
says "two placeholders" and predates `TOOL-aJoinedCanon-9` adding the third. The template holds 4 of
the first, 7 of the second and 0 of the third, so at this install the render is
4×(+6) + 7×(−7) = −25 bytes, which is exactly the measured 27666 − 27641. Verified at base `bd44d3ff`
on the current pair and again on the edited pair: `render_doc` over the template is byte-identical
to the live file both times.

```bash
# the direction the kit declares: edit the template, then render template -> live
bash tools/memory-tree/kit-dogfood-parity.test.sh --render
# the direct observation AC2 names, with no suite in it
KIT_REL=tools/memory-tree TOOL_ROOT=tools/ bash -c '. tools/lib/render-doc.sh; render_doc tools/memory-tree/BUILD-METHOD.template.md' | diff - memory/guides/BUILD-METHOD.md
```

Two gate legs cover the pair, both `subject: repo`: `build-method size`, which is UNGUARDED and runs
on every bar, and `kit/dogfood doc parity`, whose guard names `memory/guides/BUILD-METHOD.md`, so this
edit arms it. `build-method size` reads the row at `tools/template-size-limits.txt:86`, and its check
6 also byte-pairs that row against the file's own `**Budget:` prose line, which S3 moves in step with
the row.

### Inventory, and the codebase-map obligation stated

This unit MINTS no identifier: no file, no leg, no conf key, no function, no flag. So it claims no
NEW inventory key, and the reason is a population rather than an absence of effort. Both files it
edits are already claimed, by name, in the `[paths] globs` of `memory/map/features/build-method.md`
— `tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` are the only two
entries in that list — and the dossier's `[claims]` block already holds every key this edit touches,
`build-method size` among them. Nothing new enters an enumerated set, so the coverage ratchet has
nothing to ask for. The limits file sits in the `[paths] globs` of the playbook dossier, whose prose
describes that file's pattern of one row per measured file with its history beside it and states no
row's figure; S3 follows the pattern, so that dossier's prose owes nothing.

What it DOES owe is the prose refresh in S6, and the leg that grades it is
`codebase-map coverage + freshness` — subject `repo`, NO guard, so it runs on every bar, `argv`
`python3 tools/codebase-map/test_codebase_map.py`. It is on this unit's keep-green list in §7. It
does NOT owe `python tools/codebase-map/gen_map.py --write`: that regen exists for CLAIM edits, and
`memory/map/generated/MAP.md` is claimant-annotated key rows only — verified, it answers zero for
the M4 bullet's own prose — so a prose-only bullet edit stales no generated artifact. A unit whose
edit moved a `[claims]` key would owe the regen in the same commit; this one does not, and saying so
is the point, because silence here reads as an oversight rather than as an answer.

The two dossier bullets S6 refreshes, and what each must carry. The `M4` bullet under `## Gaps`
gains a sentence naming the precision bound on the promotion chain and saying no checker enforces
it, since the precision lives only in the review record. The budget bullet under the same heading
keeps its first half, which says headroom is measured and not recorded there, and its closing account
of two opposed rulings becomes the owner's ruling of 2026-09-21 that the budget stands and moves,
citing this unit and `TOOL-dLoggedFlight-35`.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | the authored edit: one sentence in, one span out, M1's two budget figures and its dated raise entry |
| `memory/guides/BUILD-METHOD.md` | re-rendered from the template, never hand-edited |
| `tools/template-size-limits.txt` | the row 27648 → 30720, the dated paragraph immediately above it, and the pair comment at `:72` re-worded on its own line |
| `memory/map/features/build-method.md` | two dossier bullets refreshed |
| `memory/DECISIONS.md` | one appended row; the index is row-keyed and append-only, so a sibling's row lands additively beside it |

### Alternatives rejected

- **The backlog row's rule as written** — "a promoted generation is audited ONCE". Refuted by the dry
  run's skeptic against `TOOL-dMispairedQuote-3`, and it hard-codes a configurable named one sentence
  earlier in the same paragraph; the research record §4 cites carries both, at `:413-414` and
  `:417`. The owner replaced it on 2026-09-20.
- **A round-count bound on the chain.** `TOOL-aBoundedVerdict-1` §3 records "No round CAP as the
  loop's mechanism. Withdrawn at rev-6 on the owner's instruction", and
  `memory/builds/aBoundedVerdict/reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md:401` raises the
  same class as finding 57 and refutes it — verbatim, "the per-subject runaway ceiling cannot bound
  the promotion chain". Bounding on precision rather than on a count is what keeps this from
  reinstating the withdrawn cap.
- **Paying with M1's budget-raise history**, the fattest trim in the file. Refused at rev-3 because
  `TOOL-dLoggedFlight-35` disputed that passage. The owner's ruling of 2026-09-21 settled the dispute
  by keeping the budget, and that history is the budget's argued-in-place record, so cutting it to
  fund a sentence would delete the justification the ruling has just affirmed.
- **Paying with M4's declared-subject rule** (`tier2-review.js` audits a spec only when the call names
  the spec kind). Refused: `memory/map/features/build-method.md:94` records that this rule was already
  lost once in a deletion no record explains and restored by `TOOL-dTieredTribunal-12`.
- **Paying with aBlindedTrial's successors of D2 to D4.** Refused in "What it pays with": they are
  that build's own fold text, and the owner chose the raise.
- **Trimming the sentence instead of the file.** A version dropping the conditional override and its
  ground measures 323 bytes. With D1 out it lands the file at 27768, still 120 over the old row, so it
  no longer avoids the raise at all; and it reads as though the close needed no override where
  `specs-audited` is owed.

## 5. Production-readiness checklist

- security — N/A. The unit adds no write path, no input, no surface. Editing a shipped kit template
  changes what an adopter reads, not what any code executes.
- perf / scale — N/A on the bar: no leg is added, no argv changes, and this unit lengthens no leg.
  The ceilings of the legs §7 names are declared in `tools/gate-legs.json` and are read there.
- error / empty / loading states — N/A for prose. The nearest analogue is the empty-population class,
  and it is answered in §4: predicate C, keyed on the shape line the synthesis prompt prescribes,
  would be silent on 370 of 403 records at base `bd44d3ff`, which is why none is wired.
- observability — the rule's own input is observable only in the review record, and §4's table says
  where. Nothing reports a chain's generation count except the `-r<N>` subject key.
- risks — four, stated rather than smoothed. First, the floor may be unreachable on spec targets,
  though the measured claim is narrower than rev-1 stated:
  `memory/builds/aLexedStripper/reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-spec-audit-round2.md:24`
  records 0.29 against round 1's 0.28, and `:28` concludes that the floor is not reachable on a
  spec-audit target **by priming alone** — a result about ONE lever, on a fan primed exactly as round
  1 prescribed, and not a general claim about the target class. Taken with that qualifier the risk is
  still live, so the rule may end most chains at the first generation. That collapses to the owner's
  existing default of one round and one disposal, so it is not a defect; the value is that a
  HIGH-precision chain may continue, and `dMispairedQuote` is the corpus instance. Second, the rule
  is unenforced, so a run can ignore it; the compensating observation is that `specs-audited`, where
  owed, forces a RECORDED override at the close, which is what makes the stop auditable after the
  fact. Third, M4's long line reaches 1123 characters and 1127 bytes, and nothing wraps it. Fourth,
  the raise spends the re-read cost M1's budget exists to bound: 3072 bytes of ceiling on every whole
  re-read M7 makes, of which this landing uses 288. The figure is the owner's ruling of 2026-09-22,
  and the reason paragraph §4 writes beside the row records it. The line half's move costs no byte
  and no re-read, and the bytes still bind first.
- testing — no new arm. AC1 to AC9 are direct observations over five files, a render and one
  checker.
- migration — none. No landed record is rewritten; the corpus's existing chains are out of scope.
- user docs — none. `help/` is not part of this repo's product surface, and the governance carrier
  this unit edits IS the documentation.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` are
  each searched, as a fixed string, for the WHOLE sentence §4 fixes, from `**The CHAIN of promotions`
  to `no audit names.`, each answers exactly one line, and that line lies between the file's `## M4`
  and `## M5` headings.
  Red when: the sentence lands in the rendered copy only, so the template answers zero and every
  adopter renders a method that carries no such rule; or a variant lands in its place. The trimmed
  sentence §4 rejects, which drops the conditional override and its ground, answers zero in both
  files, while its first 46 characters still match. That prefix is what rev-3 searched for, which is
  why the whole sentence is the search string now.
  figure: DERIVED — both counts are read at observation time. Verified on scratch copies at base
  `bd44d3ff`: the whole sentence answers one in each edited file and zero in each copy carrying the
  trimmed variant, where the 46-character prefix still answers one.
- **AC2** — When `tools/lib/render-doc.sh` is sourced with the kit directory and `tools/` bound and
  `render_doc` is run over `tools/memory-tree/BUILD-METHOD.template.md`, its output is byte-identical
  to `memory/guides/BUILD-METHOD.md`.
  Red when: the template was edited and the live copy was not re-rendered, or the live copy was
  hand-edited, either of which leaves the declared pair in drift.
  fixture: none needed — both files are tracked today and the renderer is a tracked function library.
- **AC3** — When §4's D1 span, taken VERBATIM with its leading space, is searched for in
  `git show bd44d3ff:<path>` for both `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md`, it answers exactly ONE in each; and when the same two
  searches run over the working tree, each answers zero. Both halves are required, and the base half
  is what lets the criterion fail.
  Red when: the deletion is reverted — the working-tree half answers one and the M1 defect is
  restored. Red ALSO when the span answers zero at base, which means it was mis-transcribed rather
  than deleted, so the working-tree zero would prove nothing.
  figure: DERIVED — four searches, two ones then two zeros. Verified that D1 as written answers
  exactly one in both files at base `bd44d3ff`.
- **AC4** — When each carrier in §4's D1 row is searched for the statement it is credited with, each
  answers at least one: `.claude/skills/unattended/SKILL.md` and `tools/unattended/SKILL.template.md`
  for `the runaway backstop fired, which means the convergence predicate did not terminate` and for
  `record it in the build README`, and `tools/unattended/unattended.sh` for
  `THE CONVERGENCE PREDICATE DID NOT TERMINATE`.
  Red when: a credited carrier does not in fact state it, which turns the deletion from a
  displacement into a loss — the defect this criterion exists to separate from AC3's. It searches the
  FILE and not a line deliberately: the anchors in §4's table are a reader's aid, and
  `tools/check-spec-tokens.py:10` resolves a cite's existence and range without reading the cited
  line, so a drifted anchor is caught by no gate anywhere.
- **AC5** — When `tools/template-size-limits.txt` is read, the `memory/guides/BUILD-METHOD.md` row
  carries 30720; the comment paragraph immediately above that row carries `2026-09-21`,
  `2026-09-22`, `TOOL-dLoggedFlight-35`, the size AC6's run reports and 30720 minus that size; and no
  line of the file spells `**Budget: ≤27648`. And when both BUILD-METHOD files are read, M1's
  `**Budget:` line carries `≤30720 bytes, ≤400 lines` and its raise history carries
  `≤30720 / ≤400 on 2026-09-22`.
  This is the raise's criterion. Rev-3's AC5 observed the deleted pointer repair and the id was
  reused at rev-4, so a citation of AC5 written against rev-3 names that item and not this one.
  Red when: the row moves with no argued paragraph beside it, which is the number with no history
  beside it that the file's own header refuses at `:3-4`; or the pair comment at `:72` still spells
  the figure the row had; or M1's line 8 carries either new figure while its history still ends at
  27648, which is M1 contradicting itself; or any of the three spellings carries a figure other than
  the owner's, rev-5's 28672 and 370 among them.
  figure: DERIVED — the paragraph's two figures are compared with AC6's output at observation time.
- **AC6** — When `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` runs, it exits 0
  and the size it reports is at or under the 30720 declared for that subject in
  `tools/template-size-limits.txt`. The high-water WARN it prints above that line is expected output
  (F4) and is not a red.
  Red when: the rest of the edit lands while the row and M1's byte figure both stay at 27648, so the
  file measures 27936 against 27648 and the checker fails its check 2, 288 over; or the row moves and
  M1's `**Budget:` line does not, which fails check 6.
  figure: PINNED for the prediction of 27936 bytes, measured on scratch copies on node d 2026-09-21
  and re-measured there on 2026-09-22 with the owner's figures, the checker pointed at a scratch
  limits row both times; DERIVED for the verdict, which the checker measures itself.
- **AC7** — When the lines of `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md` are counted, each equals its count at base `bd44d3ff`,
  which is 352, and each is at or under the line figure that file's own `**Budget:` line states.
  Red when: the new sentence is wrapped onto its own lines, or D1's deletion takes its line break
  with it, either of which moves the count; or M1's line figure stays at 350, which leaves the file
  two lines over its own stated constraint after the ruling that moved it. No gate catches any of the
  three: `tools/check-template-size.sh:129` parses only the bytes figure out of M1's line, and
  `TOOL-aHoistedPass-28` prices the line half as ungated.
  figure: DERIVED — both counts and both line figures are read at observation time, the counts
  against `git show bd44d3ff:<path>`.
- **AC8** — When `memory/map/features/build-method.md` is read, its `M4` bullet names the precision
  bound and says no checker enforces it, and its budget bullet under `## Gaps` names the owner's
  ruling of 2026-09-21 and `TOOL-dLoggedFlight-35`; and when that file's `[claims]` block is diffed
  against base `bd44d3ff`, no key has moved.
  Red when: either bullet still describes what it did before — the M4 loop without the bound, or the
  budget as two opposed rulings asserting neither — which is the stale-claim class the map exists to
  prevent and the class this build's first unit is about. Red on the second half when a claim key did
  move, because this unit then owes the generated-artifact regen that §4 declares it does not — which
  is what keeps that refusal falsifiable rather than convenient.
- **AC9** — When `memory/DECISIONS.md` is diffed against base `bd44d3ff`, exactly one added row names
  `TOOL-dGatedProse-4`, and it names the owner's rulings of 2026-09-21 and 2026-09-22, 30720, 400
  and `TOOL-dLoggedFlight-35`.
  Red when: the cap moves with no decision row, which leaves the checker's own failure text at
  `tools/check-template-size.sh:144`, naming that file as where a raise of this limit is recorded,
  pointing at a file that does not record it; or two rows name this unit, which check 20's
  one-id-one-row rule refuses.

## 7. Gates

This unit adds and moves no gate arm, so it carries no `New arm:` line — and therefore it raises no
suite's assertion floor. Both floors this build touches are left exactly as the units owning them
leave them: `FLOOR_ASSERTIONS=374` at `tools/memory-tree/check-memory-hygiene.test.sh:2478`, which
`TOOL-dGatedProse-1` raises by the count of assertions it adds, and `FLOOR_ASSERTIONS=67` at
`tools/check-spec-tokens.test.sh:18`, which `TOOL-dGatedProse-2` raises the same way. This unit edits
neither suite and adds no arm to either, so it has nothing to raise and says so rather than leaving
the reader to infer it.

The legs it must keep green:

`build-method size` · `kit/dogfood doc parity` · `memory hygiene` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `unattended kit gate` · `spec tokens (a spec's own names resolve)` · `recall floor` · `lexicon naming predicates` · `template size <=48KiB` · `charter size` · `kickoff engine size <=18KiB`

The list is derived rather than remembered: the unguarded legs this edit can move, plus every leg in
`tools/gate-legs.json` whose `guard` a path in §4's files touched trips. The kit-subject and
self-test legs those guards also reach are held off the bar by default and are not listed.

`kit/dogfood doc parity` is the leg the template edit arms, and its guard does name this carrier:
verified in `tools/gate-legs.json`, the guard is the six paths `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`,
`tools/lib/` and `tools/memory-tree/`.

The three size legs are on the list because S3 edits the file every one of them reads.
`template size <=48KiB`, `charter size` and `kickoff engine size <=18KiB` are unguarded and look up
their own rows in `tools/template-size-limits.txt` on every bar, so a malformed row or comment in
S3's edit reds all three and not only this subject's. `recall floor` is guarded on `memory/`, which
three of this unit's paths trip, and `tools/template-size-limits.txt` is one of the recall corpus's
declared extra sources at `.memory-tree.conf:544`. `lexicon naming predicates` is guarded on the
`tools/` prefix the template and the limits file trip; it grades names in code, and this unit writes
none.

`verdict epoch (kit version dates the engine)` and `codebase-map coverage + freshness` carry no
guard, so both run on every bar, and the first matters to more than this unit: it judges the whole
`base..HEAD` range topologically, so a mis-ordered kit-version bump anywhere in the range surfaces at
THIS unit's bar, the last one in it. Under R1-CORRECTED the bump sits at order 4, which is also where
the range's newest behaviour-bearing engine move sits, so the two commits are the same one or the
engine move is its ancestor — which is what the leg asks for. This unit's own edit cannot arm it,
for the population reason in F2.

`unattended kit gate` is on that list for a reason worth stating: its check 16 body term requires M4
to spell `specs-reviewed` in backticks outside every HTML comment, because the directive registry at
`tools/unattended/unattended.sh:565` maps that handle to M4. The edit leaves that sentence untouched,
and the token was verified present once on the scratch copies.

## 8. Open questions

- **F1 — FACT-QUESTION · should the precision that bounds the chain become a field on the `--review`
  row, so the bound is machine-readable?** Probe: search `tools/workflows/unattended-build.js` and
  `tools/unattended/unattended.sh` for `precision`. Observation: one occurrence in the first, inside a
  comment listing the callee's return keys at `tools/workflows/unattended-build.js:826`, and zero in
  the second. Liveness: the same search over `tools/workflows/tier2-review.js` returns 11 occurrences
  over 9 lines, so the probe can produce a positive and a zero is a finding rather than a broken
  probe. Rev-1 said "ten", which is neither of those two figures. RESOLVED (agent, 2026-09-20): NOT in this unit. Adding the field
  means a new argument in the driver's `--review` grammar and a new key in the run-state record, which
  is a change to a governance carrier and to a kit's public surface — M3's second veto. The surviving
  option, stating the rule in prose and leaving the consequence to `specs-audited`, trips no veto, so
  it is taken and the field is declared a follow-up in §3.
- **F2 — FACT-QUESTION · does this unit owe a `KIT_MEMORY_TREE_VERSION` bump of its own?** Two
  checkers could say yes, neither does, and in each case the answer is a population. Probe 1:
  `tools/check-kit-versions.sh:135` derives its population from
  `git ls-files 'tools/memory-tree/*.template.md'` and asserts every marker EQUALS the constant; it
  never asserts the constant MOVED, so it cannot ask this unit for a bump. Probe 2:
  `tools/memory-tree/check-verdict-epoch.sh` DOES assert movement, topologically at `:16-19` — the
  newest commit moving a behaviour-bearing line must be an ancestor of or equal to the newest commit
  changing the constant — but its SCAN set at `:68-69` is `tools/memory-tree/check-memory-hygiene.sh`
  plus six named Python delegates, and NEITHER `BUILD-METHOD.template.md` nor its render is in it. So
  an edit to this carrier is not a verdict change that leg can see, and no bump is owed for it. That
  boundary is the one thing rev-1 left unwritten, and it is why this unit's template edit landing
  AFTER a bump is not the stale shape it would be for the engine. Liveness: `TOOL-dRetiredFork-7`'s
  AC5 required `kit version markers` to red with a marker reverted, and the verdict-epoch leg's own
  header records a measured red once `merge-rows.py` entered its scan set, so both probes can produce
  a positive. RESOLVED (agent, 2026-09-21): no bump of its own. The kit version moves ONCE in this
  build and, under R1-CORRECTED, `TOOL-dGatedProse-3` owns the move at order 4 and re-stamps the
  derived marker population with it, which includes both of this unit's files. This unit then edits
  an already-stamped file at order 5 and owes nothing. Declared as the `consumes-from TOOL-dGatedProse-3`
  edge in §3, which re-derives the placement from `tools/memory-tree/check-verdict-epoch.sh:18` and
  `:179` rather than restating the ruling. The owner should know this answer has now named three
  different units across three revisions — rev-1 said unit 3, rev-2 said unit 1 on R1, rev-3 says
  unit 3 again on R1-CORRECTED — and that only rev-3's reading is derived from the epoch rule's own
  source; the first two were read off a build convention.
- **F3 — FACT-QUESTION · is the placeholder arithmetic in `tools/template-size-limits.txt:69-70`
  wrong?** It says four `{{KIT_DIR}}` grow by 6 each and five `{{TOOL_ROOT}}` shrink by 7 each, a net
  −11. Probe: count both placeholders in `tools/memory-tree/BUILD-METHOD.template.md` and compare the
  computed delta with the measured difference between the template and its render. Observation: 4 and
  7, so 4×(+6) + 7×(−7) = −25, and at base `bd44d3ff` 27666 − 27641 = 25. Liveness: a wrong count
  yields a delta that does not equal the measured 25, which is how this was found. RESOLVED (agent,
  2026-09-20): flagged and declared OUT in §3. It is a second mechanism, in the file that declares
  this unit's budget, and correcting its prose in the same commit as a byte-cap-relevant edit would
  conflate two claims about the same number. Rev-4 now edits the same row block for the raise and
  still leaves these two lines alone: its paragraph sits below them, so their anchor holds, and the
  delta they misstate is the template-to-render one, which the raise does not read. Follow-up owed
  as a backlog row at landing.
- **F4 — should the advisory high-water in `tools/template-size-highwater.txt` be re-recorded?** It
  holds 26941 for this subject and therefore already warns today at 27641; after this edit it warns at
  27936. RESOLVED (agent, 2026-09-21): the row STAYS at 26941 and this unit does not `--bump` it. The
  high-water is the instrument that PRICES growth against a recorded past, so re-basing it in the same
  commit that spends the budget is the measurer moving its own baseline — and the growth the warning
  exists to show is exactly this unit's. Re-derived at rev-4 on the reconciled tree, again at rev-5
  with both halves of the raise in the edit, and at rev-6 with the owner's figures. The row is
  `tools/template-size-highwater.txt:3`, and the checker run named in AC6 prints
  `TEMPLATE-SIZE WARN — BUILD-METHOD.md grew past its recorded high-water: 26941 -> 27641 (+700)`
  above its `template-size OK` line, and exits 0 — the ratchet is advisory and never changes the
  exit code, which `tools/check-template-size.sh:149` states and `:217` implements. After this edit
  the same line reads `+995`. The raise does not touch this row: the ceiling and the high-water are
  separate files by design, which the limits file's header states at `tools/template-size-limits.txt:10-13`.
  **So that WARN is expected output of this unit's own landing, not a defect for a later reader to
  chase.** A reader who wants it gone re-records the row deliberately, in a commit that spends no
  budget. The options not taken: bump to the post-edit figure, which hides the growth, or retire the
  row, which ends the pricing for every future edit of this file.
- **F5 — what figures does M1 state once both halves rise?** The owner's rulings of 2026-09-21
  raise both halves and name no figure. This is not a fact question, and rev-5 was wrong to mark it
  one: M1 records every budget figure as an owner call and M3's delegation does not reach M1's own
  budget, so no probe decides it and no agent may. Rev-4 chose the byte figure, 28672, and rev-5 kept
  it, chose the line figure, 370, and marked this item an agent resolution; both figures are
  withdrawn. RESOLVED (owner, 2026-09-22): 30720 bytes and 400 lines.
  What the figures measure out to is in §4 and is a consequence, not a reason: 2784 bytes free after
  this edit, and the byte half still binds first, running out near line 380 at M1's ~100 B and near
  387 at the file's 79 B average, both under 400.
- **F6 — does M1's budget sentence get re-worded?** OWNER'S. M1 says the bytes run out well before the
  line figure, "so most of that figure is headroom the bytes do not grant". At 30720 bytes and 400
  lines the first half holds and the second does not: about 20 of the 48 free lines are headroom the
  bytes do not grant at M1's own ~100 B reading, and about 13 at the measured average. M1's budget
  prose is the owner's under M1 and M3, so this unit reports the false clause and does not edit it.
  OPEN until the owner rules: re-word the clause to what the figures give, or leave it as it stands.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft. Written against the owner's ruling of 2026-09-20, which
  replaced `TOOL-dLoggedFlight-34`'s "audited once" rule with a precision bound after the dry run and
  its skeptic refuted the row as written.
- rev-2 · 2026-09-21 · cross-read fold, over all four cross-reads and the main loop's rulings R1–R4.
  FOLDED, in the order of how much they moved. **The payment arithmetic, which missed by one byte.**
  Re-measured by applying all six edits to scratch copies and weighing the result: D1 is re-priced at
  197 as the span PLUS the space separating it from the sentence before, whose removal is forced
  because the span ends line 140 and leaving the space behind leaves trailing whitespace. The span
  alone is 196, which is what the cross-read measured. §4's pair is corrected 27570/27595 →
  27569/27594 and the headroom claim 76 → 78 becomes 76 → 79. Dropping D3 was the other way to close
  the gap and is now recorded as failing: the payment falls to 342 and the file lands at 27677, over
  the cap. **AC3, which could not fail for D3.** The span is written in the table as the file wraps
  it, and AC3 becomes a two-sided observation — exactly one at base `fcbfba5f`, then zero in the tree
  — so a mis-transcribed span reds instead of passing. Verified that all four spans as now written
  answer exactly one in both files at base. **The precision-figure citation**, which named
  `memory/builds/dMispairedQuote/RUN.md` for five figures that file does not carry: re-sourced to the
  five review records line by line, and §4's site table gains the row that reconciles it with the
  documented-check argument — the run record carries the DISPOSITION at `RUN.md:53` and `:63` and
  never the precision, and that asymmetry is what the argument actually rests on. **R1.** The
  `consumes-from` edge moves from `TOOL-dGatedProse-3` to `TOOL-dGatedProse-1`, names the nine-file
  derived marker population that already covers both of this unit's paths, states that this unit does
  not bump, and names the two things it relies on unit 1 having left: a four-character `2.80`, on
  which every byte figure here depends, and a green unguarded `kit version markers`. F2 is rewritten
  on that ruling and now writes down the population boundary neither spec had — the verdict-epoch
  leg's scan set at `check-verdict-epoch.sh:68-69` excludes both BUILD-METHOD files, which is WHY a
  template edit after a bump is not the stale shape it would be for the engine. A second
  `consumes-from` to unit 3 survives as a NON-dependency: that unit raises the hygiene guide caps,
  which do grade this file, and nothing here turns on the raise. **R2.** §7 states that this unit adds
  no arm and therefore raises no assertion floor, naming both floors and the units that own them.
  **R3.** §4's inventory section now says why no new inventory key is claimed — the dossier's
  `[paths] globs` already name both files — and adds `codebase-map coverage + freshness` to §7.
  **R4** needed nothing: S1 already edits the authored template and S4 re-renders. Also folded, all
  of them citations or figures that did not reproduce: the census pair 266/121 and 86/17, replaced by
  a three-predicate table whose spread from 33 to 286 of 387 IS the argument against wiring a
  predicate; `render_doc`'s token set, three and not two, read from the function body rather than the
  header comment that still says two; the `-r<N>` mechanism re-sourced to
  `unattended-build.js:250-254`, `:685-690` and `:1255-1258` instead of paraphrased, which is what
  makes "re-arms per subject" a quotation rather than a claim; F1's liveness count ten → 11
  occurrences over 9 lines; D4's carrier anchor `REVIEW-PROTOCOL.md:203-206` → `:209-211`; the
  aBoundedVerdict finding-57 anchor `:394` → `:401`; the aLexedStripper anchor `:22` → `:24` and
  `:28` with its dropped "by priming alone" qualifier restored, which narrows that risk from a claim
  about a target class to a claim about one lever; §5's perf line, which priced two legs when §7 now
  names eight; the long line stated as 1047 characters AND 1053 bytes, because conflating the two is
  how the cross-read reached 1051; and the sentence asking `TOOL-dGatedProse-3` for a mirror
  `hands-off` line it already carries, DELETED rather than annotated.
  REFUSED, one half of one finding. This unit does not run `python tools/codebase-map/gen_map.py
  --write`. `memory/map/generated/MAP.md` carries claimant-annotated key rows and not dossier prose —
  verified, it answers zero for the M4 bullet's own wording — and this edit moves no `[claims]` key,
  so the regen the sibling finding asks for would rewrite nothing. The leg belongs in §7 and the
  regen does not; AC8 now observes the claim block against base so that refusal can itself go red.
  Nothing else was refused.
- rev-3 · 2026-09-21 · owner-ruling fold, the lightest of the four and not nothing. **R1-CORRECTED**,
  the main loop's correction of its own R1 after unit 3's F2 caught it: the kit-version move belongs to
  `TOOL-dGatedProse-3` at order 3, not to `TOOL-dGatedProse-1` at order 1, because
  `tools/memory-tree/check-verdict-epoch.sh:18` requires the bump to sit at or after the range's
  newest behaviour-bearing engine move and both units 1 and 3 move that engine. Verified at source
  before folding, per the instruction not to take it on trust: `:68-69` is the scan set, `:129` finds
  W, `:150` finds S, `:179` is the ancestor test. The `consumes-from` edge moves from unit 1 to unit 3,
  the unit-1 edge is REWRITTEN to what still crosses rather than annotated with what no longer does,
  §7's verdict-epoch note says why order 3 satisfies the leg, and F2's resolution is re-derived and now
  discloses that this answer has named three units across three revisions with only this one read off
  the checker. **A LIVE RED, found while folding and CLOSED by this fold.** `memory hygiene` check 12
  was failing on this tree at rev-2: `TOOL-dGatedProse-2` declares **hands-off**
  `TOOL-dGatedProse-4` and this spec declared no mirror **consumes-from**. It passes after this
  fold, re-run to confirm. A third sibling edge is added, and the pair rule itself
  (`tools/memory-tree/check-memory-hygiene.sh:1798-1800`) is now stated at the head of §3's Edges, so
  no later fold deletes one end of a pair believing it is tidying up. **O2**, the no-cutoff ruling: it
  adds no scope here and it does add a dependency, because both new predicates then grade THIS spec
  from the commit that lands them. Both readings are written into the edges that own them — no §2 item
  trips check 25, since the only retirement-verb item carries no backticked token at all, and the two
  claim-shaped sentences clear the `claims` join on the space clause and on the absence of a claim verb
  behind the dossier subject — each with the remedy named in case a sibling's fold widens its arm.
  **O1**: the guide cap pair 81920/1000 is now cited as the owner's ruling of 2026-09-21 rather than as
  a ratified figure of unknown provenance, and this file clears it either way. **O3 and O4 need nothing
  here**, and that is stated rather than left as silence: O3 widens unit 1's trigger vocabulary, which
  this spec's §2 still cannot trip for want of a backtick, and O4 grades the content of a
  `**Readers:**` clause this spec does not carry and owes none of. **F4**, decided by the main loop
  rather than the owner: the advisory high-water stays at 26941, the WARN it prints is expected output
  of this unit's landing, and the checker's exit code is untouched — re-derived by running it.
  **Both re-verifications the fold was asked for closed.** The payment arithmetic reproduces exactly
  — 447 in, 450 out, 27572 → 27569 and 27597 → 27594 at 349 lines, headroom 76 → 79 — and it closes
  against the same real headroom after unit 3's stamp rides through the write set, because `2.79` and
  `2.80` are four bytes each. Nothing else in §4 moved.
- rev-4 · 2026-09-21 · spec-audit round 1 fold, rebased onto `bd44d3ff`, the merge of origin/main
  into this branch. `REVIEW_ROUNDS` is 1, so there is no round 2 and this fold IS the M4 disposal of
  the round's five items against this unit; the one blocker is closed by this unit's own mechanism,
  so no unit is minted. **B1, closed by redesigning the payment on the owner's ruling of 2026-09-21**,
  which keeps the rule in M4 and raises the cap. Re-derived against the reconciled M4: the sentence
  still lands after `the fold is what the next round measures.`, now on line 142; of rev-3's four
  spans only D1 survives, since `a33237c4` rewrote D2, D3 and the pointer text rev-3's S3 widened and
  `315201b0` rewrote D4, so S2 deletes D1 alone and rev-3's S3 goes with the repair it made. S3 is now
  the raise: the `build-method size` row 27648 → 28672 with a dated reason paragraph immediately
  above it, and M1's `**Budget:` line and raise history moving in step, because check 6 pairs them.
  §4 prices it — the render lands at 27919, 271 over the old row; 28672 is the smallest KiB-round
  figure above that and leaves 753 bytes, for the next edit to the method and reserved for nothing —
  and says the reason lives beside the figure. The sentence's override clause is now conditional on
  `specs-audited` being owed, since on the reconciled tree it is owed only where a build or its
  project declares the audit; the sentence is 445 bytes. AC3 reads its base half at `bd44d3ff` and
  covers D1 alone. AC5 is re-used for the raised row and its reason, since rev-3's AC5 observed the
  item that is gone. AC6 reads the raised row. AC7 now asks that the edit add no line, because the
  file is already at 352 against M1's 350; §4 names that breach as aBlindedTrial's and returns it to
  the owner with M1's now-false "BYTE half binds first". AC9 and S7 are new, for the
  `memory/DECISIONS.md` row the checker's own failure text asks for. This unit records that it answers
  `TOOL-dLoggedFlight-35` — the budget stands, as `TOOL-aHoistedPass-3` enforced it, and moves — and
  the row closes at landing (§3). F4 re-verified: the high-water row stays at 26941 and the WARN grows
  from +700 to +978, exit 0. **M3, this unit's half, closed**: §3's unit-1 edge now derives that no
  rev-4 item fires and says rev-3's S3 did; the "only S2" sentence is gone; a `consumes-from`
  `TOOL-dGatedProse-5` edge is added. This SUPERSEDES the rev-3 entry's statement that this spec
  carried no `**Readers:**` clause and owed none: it owed one for rev-3's S3, and at rev-4 it owes
  none because that item is gone. **M12, closed**: AC1 searches both files for the whole sentence,
  which the rejected trimmed sentence fails while its 46-character prefix still matches, verified on
  scratch copies. **L4, closed**: §3, §7 and §8 F2 state the orders as unit 5 at 1, unit 1 at 2, unit
  2 at 3, unit 3 at 4 and this unit at 5, say five specs, and cite unit 1's S8 for the
  `tools/memory-tree/HYGIENE.template.md` edit. **L5, closed**: §5 cites predicate C, silent on 370 of
  403 records at `bd44d3ff`, and §4's table is re-derived there, with the rev-1 figures it once
  refuted deleted from §4 rather than restated. Every line anchor into a file the merge moved was
  re-grepped on the reconciled tree — the hygiene engine's pair rule and guide selector, the harness,
  the driver, both protocols, the Skill and both suites' floors — and the marker now reads 2.82. §7
  gains `recall floor`, `lexicon naming predicates` and the three size legs that read the limits
  file, derived from the manifest's guards against §4's files touched.
- rev-5 · 2026-09-21 · the cross-spec reconcile of the round-1 folds, run one unit at a time and
  this unit first, because its relabelled S3 is where the set's contradictions start. Every figure
  and anchor this entry touches was re-derived at `bd44d3ff`, on scratch copies or at source.
  **The two labels, stated by content.** Rev-3's S3, the pointer repair to the review protocol that
  carried `removes` and fired check 25, is DELETED; rev-4 reused S3 for the budget raise and AC5 for
  its row check. §3's unit-1 edge now says so in terms, names the round-1 record's line that
  describes the deleted item, and states that no rev-5 item fires check 25 and none owes a
  `**Readers:**` clause. The labels are not moved a third time. **The unit-5 edge, corrected**:
  rev-4 said that unit's census row and AC15 still named rev-3's S3, where its rev-6 had already
  dropped the row and retired AC15. **The owner's line-half ruling of 2026-09-21, folded into S3**:
  M1's line figure moves 350 → 370 in the same edit, priced in §4 as the smallest round-ten figure at
  which M1's own sentence that the BYTE half binds first holds again, at no byte, and F5 records the
  figure as an agent resolution under the ruling. M1's history entry becomes
  `, then both to ≤28672 / ≤370 on 2026-09-21`, 46 bytes where rev-4's was 29. Re-measured on
  scratch copies: the render lands at 27936 and the template at 27961, 352 lines each, 288 over the
  old row and 736 under the new one; the checker exits 0, 6 and 1 on the three arrangements §4's
  measured-cost section names; `render_doc` over the edited template is byte-identical to the edited render; the
  high-water WARN reads +995. S5, AC5, AC6, AC7, AC9, §5's fourth risk and F4 carry the new figures,
  and rev-4's non-goal saying the line half does not move is deleted. This SUPERSEDES rev-4's
  return of the line breach and of M1's false "BYTE half binds first" to the owner, since the owner
  has now ruled on both. **The guide-cap re-ruling**:
  the unit-3 edge cites 98304/1200, which supersedes 81920/1000, and says nothing here turns on which
  pair that unit states. **Provenance**: the external edge names both rulings of 2026-09-21, says
  they reached this spec as the main loop's relay, and names S7's row as their first decision record;
  the row is re-measured at 293 characters. **The research record**: the dry-run findings §4 and the
  alternatives cite now cite
  `memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md` by line,
  the subject-key spellings are re-derived over the 58 tracked run-state files, and "both stages
  concluded" becomes what that record supports: stage 1 said no predicate and the skeptic's narrowing
  proposes none.
- rev-6 · 2026-09-22 · the owner's figures. **The owner ruled the budget figures on 2026-09-22: 30720
  bytes and 400 lines.** Rev-4 chose 28672 and rev-5 kept it, chose 370 and marked F5 an agent
  resolution, which overstepped: M1 records every budget figure as an owner call and M3's delegation
  does not reach M1's own budget. F5 is now resolved by the owner, drops the FACT-QUESTION prefix it
  never qualified for, and says both agent figures are withdrawn. Every place 28672 and 370 stood as
  this unit's budget now carries 30720 and 400, with what derives from them: §1, S3, S5, S7, the §3
  non-goal on the long line, §4's raise table, M1's `**Budget:` line and its raise entry, the
  limits-file reason paragraph, the `memory/DECISIONS.md` row, the files-touched row, §5's fourth
  risk, AC5, AC6 and AC9. The raise entry is
  now dated 2026-09-22, the day the figures were ruled, where rev-5 dated it 2026-09-21; the date is
  the same length, so no byte moves. The headroom is 2784 bytes, about 28 lines at M1's ~100 B, and
  48 lines against the unchanged 352. **The justification changed kind.** Rev-5's arguments for its
  own figures, the smallest KiB-round byte figure and the smallest round-ten line figure at which
  M1's sentence holds, no longer decide anything and are gone from §4; §4 now states the ruling and
  its date and reports the consequence a reader needs, that the byte half still binds first at 400
  lines. AC5 now also reds on a figure other than the owner's. **Re-measured on scratch copies at
  `bd44d3ff`**: 27936 and 27961 bytes at 352 lines each, unchanged, because every edited figure keeps
  its digit count and the raise entry stays 46 bytes; `render_doc` over the edited template is
  byte-identical to the edited render; the checker exits 0 at 27936 / 30720 with 2784 under, 6 with
  the row left at 27648, and 1 with both at 27648; the high-water WARN still reads +995. The
  decisions row is re-worded to cite both days and measures 293 characters and 295 bytes. The
  external edge names the third ruling and its relay provenance, and the unit-1 edge's check-25
  reading is re-derived over rev-6's §2, where it still finds no item that fires. **Also corrected**:
  the render loop of `tools/memory-tree/kit-dogfood-parity.test.sh` is cited at `:100`, where rev-5
  said `:99`, which is the line st=0. The entries above are left as written: they record 28672 and
  370 truthfully as what those revisions wrote.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound a spec-audit promotion chain by review precision"`
found no existing seam for this mechanism, and that is the answer rather than a probe failure. Over
1371 symbols, 255 inventory keys, 22 affordance seams and 24 dossiers it ranked only name-stem
matches — `build_self_chain` in `tools/process-monitor/scope.py`, `boundedParallel` in the workflow
scripts, `derive_review_exit` in `tools/runlog/model.py` — none of which is a place a rule about the
promotion chain could live, and its own header says a high rank means a name recurs rather than that
the seam is the right one. The seam this unit extends is therefore a DOCUMENT and not code: M4's
existing `**A BLOCKED verdict has a disposition.**` paragraph in
`tools/memory-tree/BUILD-METHOD.template.md`, which already states the severity disposal the new
sentence hangs off, with `memory/guides/BUILD-METHOD.md` as its render. Extending that paragraph is
what keeps this unit from minting a heading, a cutoff key or a checker. One recorded disagreement
between a hit and today's tree, per M5: the dossier bullet at `memory/map/features/build-method.md:94`
says nothing yet asserts that a spec audit HAPPENED, while `specs-audited`
(`memory/guides/UNATTENDED-PROTOCOL.md:357`) does assert it at `--close` as a lower bound, where it is
owed. The disagreement is recorded here rather than resolved, and AC8 refreshes only the sentence this
unit makes incomplete.

The raise at rev-4 extends a second existing seam and writes none.
`python tools/codebase-map/reuse_lookup.py "raise a declared byte ceiling for a rendered guide with the reason beside the figure"`,
run at base `bd44d3ff` over 1421 symbols, 265 inventory keys, 22 affordance seams and 24 dossiers,
ranks the playbook dossier's `check-template-size.sh` affordance among its candidates, and that seam
is the one S3 uses: one row in `tools/template-size-limits.txt` giving a subject's ceiling and the
reason for it. Everything else it ranked is a name-stem match on `declar`, `byt` or `render`.

Recall terms used, verbatim: `python tools/memory-recall/query.py "what bounds a spec-audit promotion
chain and where is review precision recorded" --terms "precision confirmed refuted spec-audit
promotion chain REVIEW_ROUNDS runaway ceiling specs-audited override severity disposition
BUILD-METHOD M4 floor"`. It returned 40 hits; three bind this unit. `TOOL-aProbedUnit-9` is the owner
ruling of 2026-09-14 that fixes one spec-audit round as the default, which is why the sentence leaves
rounds to `REVIEW_ROUNDS`. The aBoundedVerdict round-2 record is the prior art for the chain bound,
raised as finding 57 and refuted in 2026-08-19. The aLexedStripper round-2 record carries the measured
claim that the floor is not reachable on a spec-audit target, which §5 records as this unit's first
risk.

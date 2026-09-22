**Serves:** spec-audit TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-4 TOOL-dGatedProse-5

# dGatedProse — spec audit of the five-unit set, round 1

*Node `d`, 2026-09-21, worktree HEAD `016e87e8` on `branch/spec-prose-gates-b41f7c`. This is a
Tier-2 adversarial pass over the five specs of the `dGatedProse` build, run once before any unit is
built as BUILD-METHOD M4 requires. It used four primed finder lenses, five batched skeptic passes
prompted to REFUTE every finding, and one synthesis. The lenses were primed with a by-design set,
and nothing in it is re-reported: the owner rulings O1 to O6, the dropped checks A and B, the single
memory-tree version move in unit 3, the case-folded verb match, and the by-value half graded by
presence rather than completeness. During synthesis the load-bearing claims were re-run at source on
this tree rather than copied from a lens. That covered the `Readers:` counts, the census row, the
resolution-corpus examples, the four BUILD-METHOD spans and the cap row on both refs, and the
hygiene and spec-tokens anchors. The lens drafts that first occupied this path are superseded by
this record.*

*Ids that only `origin/main` defines are written here without their family prefix, for example
"aBlindedTrial's unit 8". This branch does not define them, so check 14 would read a full spelling as
an orphan id.*

**Round: 1.** Subjects, each pinned at the blob it was read at. All five were re-hashed with
`git hash-object` at synthesis and match the working tree at `016e87e8`:

- `memory/builds/dGatedProse/spec/2026-09-20-spec-TOOL-dGatedProse-1.md@d51fe72256da3699764cc1dce966842f5424b21a`
- `memory/builds/dGatedProse/spec/2026-09-20-spec-TOOL-dGatedProse-2.md@2383613b551b3f2df5cb7c5838aeed6aac1d9b10`
- `memory/builds/dGatedProse/spec/2026-09-20-spec-TOOL-dGatedProse-3.md@3f79dd04fd2701672ceb1a685b2ff23c9938f725`
- `memory/builds/dGatedProse/spec/2026-09-20-spec-TOOL-dGatedProse-4.md@3f59816d92dbd0416bad77de0b2d7d73370f3d42`
- `memory/builds/dGatedProse/spec/2026-09-21-spec-TOOL-dGatedProse-5.md@f8d11d8a7110706a0f094df62a752f4890c175ca`

## Verdict: BLOCKED

The thirty-one confirmed findings consolidate into twenty-three items: one blocker, four highs,
twelve mediums and six lows. Counted by raw confirmed finding, the same table is one blocker, six
highs, seventeen mediums and seven lows.

The blocker is in unit 4, and it is a stale base rather than a wording defect. The set pins base
`fcbfba5f`, and `origin/main` (`663a0dec`) is 254 commits ahead of it. On `origin/main`,
aBlindedTrial's units 5 to 7 have already rewritten M4 and made the spec audit opt-in. Three of unit
4's four deletion spans no longer exist there, and neither does the pointer text its S3 widens.
`memory/guides/BUILD-METHOD.md` is 27641 B there, against a 27648 B cap. The one surviving span pays
197 B against the 447 B the unit adds, so the unit lands about 243 B over its cap on the tree it has
to land on. The same stale base reaches unit 2 as a high. `origin/main` already carries a fifth
spec-tokens join and a floor of 67, so unit 2's join would be the sixth, and its AC11 would pass over
a wrong count.

The risk the commission named holds up. Unit 5's census still carries the escape-over-real-readers
direction in two places. The census table marks `aPacedTurnstile-14` S9 ESCAPE, while four other
statements in the spec make it GENUINE. And sixteen GENUINE items have no criterion forbidding
`NO VALUE READERS`. Unit 1 carries the same class one level down. Its resolution corpus keeps every
build record and the archive in scope, so a name resolves just by being quoted, and the census record
unit 5 commits would resolve the very tokens unit 5 writes.

**Decision needed on unit 4, because the fix has no owner-free spelling.** After the rebase, the unit
is about 243 B over the `build-method size` row. `TOOL-dLoggedFlight-35`, which is still OWNER RULING
OWED, asks whether that 27648 budget stands at all. The owner either rules -35, or picks one of three
paths. The first is new payment spans in the rewritten M4. The second is a priced raise of the cap
row. The third narrows the ruling to builds that are still audited on `origin/main`, meaning builds
whose README declares `spec-audit:` or whose project conf declares `SPEC_AUDIT_DEFAULT`. The fold
below assumes a rebase and a re-derivation, and it cannot choose among these paths.

A second fork is conditional. H4's re-measurement may push unit 1's unresolved rate past the unit's
own 5% wireability line (unit 1 §4, `:663`). If it does, the README's build rule sends the by-name
predicate back to the owner rather than into a gate.

**Review shape:** raw 53, confirmed 31, refuted 22, unverified 0, precision 0.58. The adjudicated
tally by item is 1 blocker, 4 high, 12 medium and 6 low, 23 items. By raw confirmed finding it is 1
blocker, 6 high, 17 medium and 7 low, 31 findings. Precision is above the charter's ~0.5
tighten-priming line.

**Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory
verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
Every lens and every skeptic batch came back, so the finding set is complete as far as a four-lens
fan reaches. The zero unverified count is therefore a real count, not an absence of evidence.

Unit 3 converges at round 1 once its fixes are folded. Units 1, 2, 4 and 5 do not; see Disposition.

## Findings

| # | Sev | Unit | Address | One line |
|---|-----|------|---------|----------|
| B1 | blocker | 4 | §2 S2 S3 · §4 What it pays with, Measured cost · §6 AC3 AC6 AC7 | `origin/main` rewrote M4; three of four deletion spans are gone and the unit lands ~243 B over its cap |
| H1 | high | 2 | §2 S1 S5 S8 S10 · §4 Inventory · §6 AC9 AC11 | `origin/main` already has a fifth join and a floor of 67; this join is the sixth and AC11 passes over a wrong count |
| H2 | high | 5 | §2 S4 · §6 AC5 AC12 AC13 AC15 | Sixteen GENUINE items have no criterion forbidding `NO VALUE READERS` |
| H3 | high | 5 | §4 "items rev-3 adds" table, `aPacedTurnstile-14` S9 row `:300` · `:314`–`:320` | The census row says ESCAPE; four statements and the counts under the table say GENUINE |
| H4 | high | 1, 5 | unit 1 §2 S5, §4 resolution corpus · unit 5 §2 S3 S8, §6 AC3 | Record prose resolves names by quotation, including the census record unit 5 commits |
| M1 | medium | 5 | §6 AC2 `:858` | Whole-file `Readers:` count equality cannot pass on unit 4's spec |
| M2 | medium | 5 | §2 S2 · §6 AC2 AC6 | The F1 rev bumps and the three clause markers have no criterion that can fail |
| M3 | medium | 4, 1 | unit 4 §3 `:117`–`:125` · unit 1 §3 `:212`–`:217` | Both edges say no item of unit 4 fires; S3 does, and unit 5 writes its clause |
| M4 | medium | 5 | §4 clause forms `:719`–`:729` · §6 AC3 AC9 | Unit 5 restates unit 1's resolver wrongly, and AC9 names an untracked probe |
| M5 | medium | 2 | §6 AC9 AC10 · §4 Migration · §3 Edges · §7 | Written before unit 5: four specs not five, 28 live not 29, stale orders, a pointer that does not hold |
| M6 | medium | 2, build | §3 Edges · §4 What the four arms buy · README build-level rules | The dry-run journal the rulings rest on is untracked |
| M7 | medium | 2 | §2 S1 S3 · §6 AC6 | Three of four grammar arms, and the case fold, can be dead with the canary green |
| M8 | medium | 2 | §2 S8 · §6 AC9 | A floor raise of 1 passes over a dozen new assertions |
| M9 | medium | 3 | §2 S1 | The primary home of the reason is read by no criterion |
| M10 | medium | 3 | §2 S3 · §6 AC5, AC1 red-when | The example conf's line key is unobserved; AC5's fixture sits under the retired cap |
| M11 | medium | 1 | §2 S10 · §6 AC18 AC13 | A blank `SPEC_FORMAT_CUTOFF` disarms check 25 silently |
| M12 | medium | 4 | §2 S1 · §6 AC1 | AC1 greps a 46-character prefix; the rejected trimmed sentence passes |
| L1 | low | 1 | §2 S2 against S9 | Multi-word phrases wrapped across lines are unfixtured and unnormalised |
| L2 | low | 1 | §5 error / empty | The empty-pattern failure direction is recorded inverted |
| L3 | low | 3 | §3 consumes-from unit 1 `:135`–`:137` | A phantom preset and conf-example line |
| L4 | low | 3, 4 | unit 3 §2 S8 §4 §7 §8 F2 · unit 4 §3 §7 §8 F2 | Order positions from before the renumbering, and a wrong sibling S-label |
| L5 | low | 4 | §5 error / empty `:409` | The refuted 121 of 387 figure |
| L6 | low | 5 | §3 Non-goals `:80` | "Fourteen fixtures" where unit 1 has sixteen |

The raw-id map, so the transcript reconciles: B1 = 44, H1 = 47, H2 = 1, H3 = 4 and 19, H4 = 34 and
35, M1 = 2, 23 and 37, M2 = 3, M3 = 20 and 21, M4 = 17 and 24, M5 = 18 and 25, M6 = 51, M7 = 6,
M8 = 7, M9 = 9, M10 = 10, M11 = 11, M12 = 12, L1 = 14, L2 = 42, L3 = 26, L4 = 27 and 28, L5 = 29,
L6 = 30. Consolidation moved four ids in severity. Ids 4 and 35 arrived rated medium and take high.
Ids 17 and 18 arrived rated low and take medium. Every other severity is as confirmed.

---

### B1 — blocker — unit 4 §2 S2 and S3, §4 "What it pays with" and "Measured cost of the whole edit", §6 AC3, AC6, AC7: the M4 it edits no longer exists on the tree it lands on

The spec pins base `fcbfba5f`. `origin/main` is `663a0dec`, 254 commits ahead. There,
aBlindedTrial's unit 5 (`a33237c4`) and its round-2 fold (`312213ec`) made the spec audit opt-in and
retitled M4. Its unit 6, which records the supersession, is at `memory/DECISIONS.md:192` on that ref.
At synthesis, each span was checked in `memory/guides/BUILD-METHOD.md` on both refs:

- D1 (`A runaway ceiling backstops`) is present on both refs.
- D2 (`which 2, 1, 2 satisfies forever`) is present at `fcbfba5f` and absent on `origin/main`.
- D3 (`Most existing review records carry no`) is present at `fcbfba5f` and absent on `origin/main`.
- D4 (`once a synthesis pass calls the design clean`) is present at `fcbfba5f` and absent on
  `origin/main`.
- S3's pointer text (`under its fan-out and concurrency caps, read there and not`) is present at
  `fcbfba5f` and absent on `origin/main`.

On `origin/main` the file is 27641 B and 352 lines, and its own header declares `≤350 lines`. The
`build-method size` row in `tools/template-size-limits.txt` is 27648 on both refs.

So S2 and S3 cannot be applied as written. AC3's base half is pinned to `fcbfba5f`. After the
reconcile, D2 to D4 each read one hit at the base and zero in the tree, because aBlindedTrial deleted
them, not this unit. That is a green criterion for a deletion this unit never made. Only D1's 197 B
of payment survives. 27641 + 447 − 197 = 27891 B, which is 243 B over the row, so the leg reds. With
the payment that is left, AC7's 349-line target cannot be reached from 352.

The new sentence's ground also fails. It says the override is owed "because the run CLOSES units no
audit names". On `origin/main`, `specs-audited` is owed only when the README at BASE declares
`spec-audit:`, or when the project conf declares `SPEC_AUDIT_DEFAULT` and the README declares no key
(`memory/guides/UNATTENDED-PROTOCOL.md:357` there). That ref's `.unattended.conf` sets
`SPEC_AUDIT_DEFAULT=""`, so for this project the ground is false for every build without a
`spec-audit:` key. The build README already knows `origin/main` diverges on this file: it parks
`TOOL-dLoggedFlight-35` because `origin/main` carries two opposed rulings on the build method's size
budget. Unit 4 did not carry that into its own payment arithmetic.

**Fix.** Rebase unit 4 onto `origin/main`. Run first the kit-rewrite check that
`memory/guides/SESSION-KICKOFF.md:108` records: 6 commits since the base touch
`tools/memory-tree/BUILD-METHOD.template.md`, and 16 touch `tools/memory-tree/`. Cite aBlindedTrial's
units 6 and 7 by their full ids once the rebase brings their definitions into the tree. Re-derive the
payment spans, the byte and line figures, and AC3's base half against the current M4, reading the
base half at the rebased base. Make the override clause conditional on `specs-audited` being owed.
State who owes the 352-against-350 line breach that already stands on `origin/main`. The byte gap
itself is the owner decision above.

**Left-shift.** The class is a spec whose base is behind the remote on the very files it touches.
Gate it at the transition from SPECCED to building, not at landing. For every path under a spec's
`### Files touched`, `git log <base>..<observed remote HEAD> -- <path>` must be empty, or the spec
re-derives before building. "Observed remote HEAD" is the unattended kit's own notion, read from
the remote's advertisement and never from a local ref, so the check can reuse it. Until it exists,
add this to the §10 checklist a spec audit runs: re-derive every cited span and figure on
`origin/main`, not on the pinned base.

### H1 — high — unit 2 §2 S1, S5, S8, S10; §4 Inventory; §6 AC9, AC11: the fifth join already exists

On `origin/main`, aBlindedTrial's unit 8 (`e80c95b9`, CLOSED) adds a `guards` join to
`tools/check-spec-tokens.py`, keyed on `SPEC_GUARD_LEGS_CUTOFF`. There, `memory/map/features/spec-tokens.md`
is already titled "Five joins …", and `FLOOR_ASSERTIONS` in `tools/check-spec-tokens.test.sh` is 67,
against 42 at the base. Both values were re-read at synthesis on both refs. The bar join's report line
prints on both branches of `if direct_cut:` on that ref, as it already does at the base.

After the reconcile, this unit's join is the sixth. AC11 requires the title and the `:49` body
sentence to "name five", which is then already true, so AC11 passes over a wrong count with no edit.
S8's and AC9's arithmetic "from 42" cannot reach the value the file will declare. S5's claim that its
every-run report line departs from its sibling is false on both refs. The hit-kind list "leg, path,
cite and bar" leaves out `guards`.

**Fix.** Rebase onto `origin/main`. Derive the join count and the floor base from the live files at
observation time, and write AC11 against that derived count rather than a typed "five" or "six". Cite
aBlindedTrial's unit 8 as the sibling precedent for an unconditional report line. Add `guards` to
the hit-kind list. Re-resolve the `:87`, `:258`, `:421` and `:429` anchors.

**Left-shift.** B1's base check covers the cause. For the count, add a map freshness arm that derives
the join count from `tools/check-spec-tokens.py` and compares it with the dossier title. That applies
the no-count-in-prose rule to the one place this unit edits a typed count.

### H2 — high — unit 5 §2 S4 against §6 AC5, AC12, AC13, AC15: sixteen GENUINE items may still answer `NO VALUE READERS`

S4 obliges all 28 GENUINE items to carry the readers §4 names, and it claims AC5, AC12, AC13 and AC15
observe that. Those criteria cover less:

- AC12, AC13 and AC15 observe the by-value half of 10 items.
- AC5 observes the by-name half of 3 items.
- AC7 covers the already-claused unit-3 S8.
- `aMendedLedger-8-u9` S2 is the one sanctioned `NO VALUE READERS`.

That leaves exactly sixteen GENUINE items where §4 names by-value readers but no criterion stops the
item from answering `NO VALUE READERS`:

- the BY-VALUE halves of `aMendedLedger-3-u2` S3 and S6 and `aMendedLedger-4-u3` S3 (AC5 reads only
  their by-name half);
- `aMendedLedger-2-u1` S5 and S6, `aMendedLedger-3-u2` S2, and `aMendedLedger-4-u3` S4 and S7;
- `aMendedLedger-6-u6` S1, S5, S6 and S11, and `aMendedLedger-1` S2;
- `aTunedCompass-3` S2, `dPolishedVitrine-1` S5 and `dScaffoldedMirror-9` S5.

§4 names by-value readers for every one of them. Examples are `drift_report.py:1364` for u2 S3,
`signal_ledger` for u6 S1, S5 and S6 and for `aMendedLedger-1` S2, and `lexicon.py:3280` for
`dScaffoldedMirror-9` S5. AC3 only checks that written tokens resolve, not that a half is populated.
A by-name half written as prose with no token also passes by vacuity on the 25 GENUINE items AC5 does
not name.

This is the direction every skeptic round of the census found: an escape written over real readers.
Check 25 grades the by-value half by presence only, so once such a clause lands it passes on every
run after. Unit 1's AC21 cannot see it either.

**Fix.** Replace the named samples with one criterion over the whole census. For every item the
census record marks GENUINE:

- the by-value half carries at least one backticked token from the reader list the census records
  for that item, and no `NO VALUE READERS`. `aMendedLedger-8-u9` S2 is named as the sole exception.
- the by-name half carries at least one named reader wherever §4 names one.

Store the expected tokens per item in the S8 census record, so the observation is a mechanical diff.
Correct S4's "Observed by" line to name the new criterion.

**Left-shift.** Two changes. First, make the census record data, one row per item with its expected
tokens, and make the order-1 acceptance a script that diffs the written clauses against it. That
script is also the natural check-25 dry run at order 1. Second, the class is general and cannot be
gated mechanically, so add a §10 checklist entry. An S-item quantified over a population ("all 28",
"every") must be observed by a criterion quantified over the same population, never by named
samples.

### H3 — high — unit 5 §4, the "items rev-3 adds" table, row `aPacedTurnstile-14` S9 (`:300`), and `:314`–`:320`: the census row contradicts the census

Re-read at synthesis, the row reads ESCAPE. Four statements in the same spec make it GENUINE:

- S4 (`:53`) says "a third is one rev-5 reverses".
- The sub-section "The two escapes rev-4 reverses" (`:648`) gives it by-value readers
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`.
- AC15 forbids `NO VALUE READERS` on it.
- The rev-5 log entry (`:1080`) records the reversal.

The escaped-set table also leaves the item out. Counting the rows as written gives 12 GENUINE and 3
ESCAPE, against the "thirteen and two" printed under the table at `:308`. The whole-population
figures, 28 and 10, and the reading-A figures, 10 and 1, hold only if the row is GENUINE. Separately,
`:314` to `:320` names seven items and then says "for each of the four the code below shows a
reader", describing four readers.

S8 copies each item's verdict from this table into the census record, and this table is where a build
pass reads it. A pass that trusts the row writes `NO VALUE READERS` over the check-6 dossier-cap
reader, and check 25 then passes that false escape forever. Only AC15, if someone runs it, would catch
it, and late.

**Fix.** Set the row's verdict to GENUINE and its retired thing to "the dossier's byte count against
`DOSSIER_CAP_BYTES`". Rewrite `:320` so each of the seven items is paired with its reader. In the same
fold, re-read the other fourteen rows of the table against the genuine-set prose: the fold that
reversed this item's verdict in the prose missed its row, and could have missed others.

**Left-shift.** The counts under the table are a derived population typed into prose, which breaks the
§7 rule. Render them from the table, or from the census record H2 asks for, and recount at every
fold, so a row that disagrees with its total reds instead of being read and trusted. The general
class, a fold that updates prose but misses the table row, is the fold-text-is-unreviewed-surface
gotcha. Round 2 should re-read the census table whole.

### H4 — high — unit 1 §2 S5 and §4 "The resolution corpus is the tracked tree OUTSIDE memory/builds/*/spec/" (`:666`), with unit 5 §2 S3 and S8 and §6 AC3: a name resolves by being quoted

Unit 1's content match runs over the tracked tree minus the spec folders only. Every other kind of
build record (`reviews/`, `build/`, research) stays in the corpus, and so does `$M/archive/**`.
Those files are prose that quotes spec tokens by construction. §4's premise is that a name appearing
only in other specs' prose has not been shown to exist. The pathspec does not implement that premise,
and §4 never asks whether record prose counts as a reader.

Both named examples were re-run at synthesis with the spec's own exclusion pathspec:

- `VERIFIER_CAP` resolves only through
  `memory/builds/aDeclaredBound/reviews/2026-08-18-review-TOOL-aDeclaredBound-1-2.md`.
- `union.SUBS` resolves only through
  `memory/builds/aProbedToolkit/build/2026-09-03-build-TOOL-aProbedToolkit-1-synthesis.md`.
- `union.SETS`, the sibling of `union.SUBS` from the same unbuilt module design, resolves nowhere and
  sits on §4's unresolved list.

The lens measured 376 distinct tokens. 19 were unresolved under S5's corpus, and 38 were unresolved
once `$M/builds/**` and `$M/archive/**` left the content corpus, with tracked-path identity kept.
That second figure was not re-run at synthesis.

Resolution only ever moves toward passing, and unit 5 makes it self-fulfilling. S8 commits the census
record inside this build folder with "the reader evidence by path". Every token unit 5's clauses
carry is therefore spelled in a tracked record inside the corpus, and AC3 resolves against it. A
mistyped token copied into both places passes AC3, and then passes check 25 forever. The guard shares
a variable with what it guards, which is the §7 shape.

**Fix.** In unit 1:

- Content-match against the tracked tree outside `$M/builds/**` (every record kind) and
  `$M/archive/**`.
- Keep S5's tracked-path identity test over the whole tracked set.
- State the corpus in check 25's header.
- Add a fixture whose by-name token is spelled only in a fixture review record, and which must red.
- Re-derive and classify the unresolved rate and AC4's base-rate figure under that corpus. Some of
  the newly unresolved names, `union.SUBS` among them, are true reds rather than false ones. If the
  false-red share crosses the 5% line at `:663`, the README's build rule returns the predicate to the
  owner.

In unit 5, run and record AC3 against the same narrowed corpus, and do it BEFORE the census record is
committed.

**Left-shift.** The fixture above is the gate for this class. The broader class, a resolver whose
corpus contains the records that cite the thing being resolved, belongs in the §10 checklist beside
"inputs inside the subject's reach".

### M1 — medium — unit 5 §6 AC2 (`:858`): the count equality cannot pass on a correct pass

AC2 requires `git grep -c 'Readers:'` over each edited spec to EQUAL the number of items the census
gives that file, and the count covers the whole file. Re-run at synthesis,
`memory/builds/dGatedProse/spec/2026-09-20-spec-TOOL-dGatedProse-4.md` returns 2 today, from prose at
`:124` and `:668`, both outside §2. The census gives that file one item, S3. Once the node-d commit
adds its clause, the count is at least 3 against 1, and F1's §9 entry there may add a fourth. AC6
forbids rewriting existing lines, so the prose cannot be removed to satisfy AC2, and the two criteria
conflict on that file. Unit 1's spec returns 18 against 0 items, if any pass ever edits it.

So the pass either reds on correct work or reinterprets the criterion, and the duplicate-clause defect
AC2 exists to catch goes unobserved.

**Fix.** Count `**Readers:**` markers inside the `## 2.` section range only, or count the marker lines
the pass's diff ADDS per file against the pinned base. Compare that number to the census.

**Left-shift.** Run every grep-shaped criterion against the pinned base during the spec audit and
record its output. An equality criterion whose base output already exceeds its target is
unsatisfiable before a line is written. Keep this as a §10 checklist entry until a harness does it.

### M2 — medium — unit 5 §2 S2 against §6 AC2 and AC6: two obligations no criterion can fail

The first is the rev bump where F1 binds. AC6 reds only when an UNBOUND spec's header moves, so a
bound spec left unbumped passes. F1 itself records that not bumping reds nothing on the bar, and
check 12's rev-in-§9 test still passes on an unbumped header. The second is "all three markers
present". AC2 counts only `Readers:`, and AC4, AC5, AC12, AC13 and AC15 each check one half on a
subset of items. A clause missing `by name:` or `by value:` therefore passes every unit-5 criterion.

The three F1 rev bumps can silently not happen. A malformed clause surfaces only at unit 1's AC21 at
order 2, as another unit's defect, which is the red-at-order-2 state this unit exists to prevent.

**Fix.** Add a criterion that reads each F1-bound edited spec's header rev as base+1, with a §9 entry
at that rev carrying the item's scope token. Add a second criterion that every clause the pass writes
carries `by name:` then `by value:` after `**Readers:**`.

**Left-shift.** Make the pass's own implementation of unit 1's clause-shape test part of unit 5's
order-1 acceptance, beside the trigger AC9 already re-implements. The shape check 25 grades at order
2 is then graded at order 1 first.

### M3 — medium — unit 4 §3, the consumes-from `TOOL-dGatedProse-1` bullet (`:117`–`:125`), and unit 1 §3, the hands-off `TOOL-dGatedProse-4` bullet (`:212`–`:217`): both edges disown the one sibling item the trigger fires on

Unit 4's bullet says "no §2 item fires. The only item a retirement verb governs is S2". Unit 1's
bullet says unit 4's rev-3 "reads both of those correctly", and that "check 25 grades unit 4's spec,
and no §2 item of it fires". Both are wrong about unit 4 S3 (`:28`). It carries the strict-list verb
`removes` beside the backticked `memory/guides/REVIEW-PROTOCOL.md`, and the slash shape admits that
path now that O6 has deleted the `.md` exclusion. Everything else in the build treats S3 as firing:

- Unit 1 itself lists unit 4 S3 among its triggered items, at `:568` and in F10 (`:1269`).
- Unit 5's census rates it GENUINE (`:302`), and its node-d commit writes the clause.
- AC15 observes it, and F1 bumps unit 4's rev with a §9 entry.

Unit 4's own rev-3 §9 line at `:668` says it carries no `**Readers:**` clause and owes none. Neither
unit 4 nor unit 5 declares the edge.

From order 1, unit 4's file carries a clause and a revision entry that its own §3 says it does not
owe. A later fold of unit 4 that trusts its edge can delete the clause as tidying, and check 25 then
reds at order 5. The spec that owns the trigger endorses the wrong reading, which makes that deletion
more likely.

**Fix.** In unit 4:

- State that S3 fires on `removes` plus the `.md` path under O6, and that unit 5 writes its GENUINE
  clause and the rev bump.
- Drop the "only S2" sentence.
- Supersede the `:668` line in the new rev's §9 entry rather than editing it.
- Declare consumes-from `TOOL-dGatedProse-5`, with unit 5 adding hands-off `TOOL-dGatedProse-4` so
  the reciprocity join stays closed.

In unit 1, say that S3 fires under O6 and that unit 5 writes its clause, and delete "reads both of
those correctly" for this crossing.

**Left-shift.** Run unit 1's trigger over this build's own spec folder at every fold, and record the
hit list once, in the build README, as the one place every sibling edge points to. A generated hit
list turns "no item fires" from a claim into a pointer.

### M4 — medium — unit 5 §4 "The clause forms this unit writes" (`:719`–`:729`) and §6 AC3 and AC9, against unit 1 §2 S5 (`:58`–`:64`): unit 5 restates its sibling's resolver wrongly

Unit 5 makes two claims about unit 1's predicate. It says unit 1 strips the citation tail "for the
shape test only". It also says a token resolves only when another file SPELLS it, "not when a file of
that name exists". Unit 1 S5 says the opposite on both points. The `:<line>` and `()` strip happens
"Before either test", and "A token also resolves when it IS a tracked path of that corpus". Unit 1's
AC2 even requires a `:<line>`-tailed path to resolve. `git log -S` puts both of unit 5's sentences in
one commit, `67bec01a`.

Unit 5 applies the narrower model at `:510`. There it keeps the tracked build record
`memory/builds/aQuarriedLantern/build/2026-08-03-build-TOOL-aQuarriedLantern-1-1.md` out of a
clause "because it does not resolve", although unit 1's predicate resolves it by path identity. AC3
names no resolution procedure at all. Separately, AC9 names `probe_pop_rev3.py`, which §4 (`:133`)
says is untracked in the spec author's scratchpad. Unlike AC1, AC9 offers no re-implementation
alternative, so a build pass in another session cannot run it.

The census therefore certifies clauses against a different predicate from the one check 25 lands
with. Unit 5's model is stricter, so it cannot red the bar. It does push the pass toward
`READER NOT IN TREE`, or toward dropping a tracked-path reader that no other file spells.

**Fix.**

- Replace unit 5's restatement with a pointer to unit 1 S5 (the tail and `()` strip, then content
  match OR tracked-path identity), and implement exactly that in AC3.
- Keep "bare tokens only" as house style, not as a description of check 25.
- Re-derive which tokens were withheld under the content-only reading, starting at `:510`.
- Let AC9 accept the pass's own implementation of unit 1's trigger text, as AC1 does.
- Correct `:721` to `:722`.

H4's corpus change lands in the same AC3.

**Left-shift.** Nothing mechanical. §6's "point at the source, or gate the pair" rule is the check,
because a spec that restates a sibling's contract is carrying the copy that rots. Add a §10
spec-audit entry: every sentence describing a sibling's behaviour cites that sibling's S-item and
matches it.

### M5 — medium — unit 2 §6 AC9 (`:428`) and AC10 (`:442`), §4 Migration (`:276`), §3 Edges (`:129`–`:149`), §7 (`:473`, `:478`): written before unit 5 existed

- AC10 grades "the four spec files" of `memory/builds/dGatedProse/spec/`. Five are tracked, and unit
  5's live spec has claim-verb prose beside a dossier path at its own `:385`.
- AC9 says "of the 28 live specs exactly FOUR" are dated past `SPEC_DIRECT_CUTOFF`.
  `tools/check-spec-tokens.py` on this tree reports 29 live specs, with 5 in the bar join.
- The Migration section measures 0 hits over a corpus that unit 5 changes at order 1. That pass adds
  38 clauses across 20 live specs, and the clauses carry bare `.md` basenames, which are the arms'
  own dossier-subject anchor. There is no edge to unit 5 and no re-measurement after it. This part
  is weaker, because the unguarded spec-tokens leg grades every live spec at landing anyway.
- The edges and §7 put unit 1 at order 1 and unit 3 at order 3, while unit 2's own header says
  order 3. That reads as units 2 and 3 forming a parallel group.
- §7 says unit 1's §7 "already carries that re-render". Unit 1's §7 (`:1150`–`:1186`) carries no
  `LIVE.md` or ledger re-render sentence.

So the acceptance population misses a live sibling and twenty newly edited specs, and the "no corpus
work" claim goes unverified.

**Fix.** Have AC10 read every spec file in that folder, derived at observation time, and run it over
every live spec at landing. Re-derive the Migration figure after unit 5's pass, and declare the edge.
Restate orders 2, 3 and 4. Correct AC9 to counts derived at observation time. Delete the pointer into
unit 1's §7, or add the missing sentence there.

**Left-shift.** A candidate arm for stale order references: find `order <n>` in a sentence that names
a sibling unit id, and compare it with that sibling's header order. Per §7, run it over the real tree
first and print hits and near-misses before wiring it. It would also have caught L4.

### M6 — medium — unit 2 §3 Edges (consumes-from external, the dry-run workflow) and §4 "What the four arms buy", with the build README's build-level rules and the unit 1 and unit 3 citations: the evidence the rulings rest on is not tracked

Three documents point at a record of the dry run:

- The README says the dry runs "are recorded in this folder's research record, with the skeptic that
  re-derived each count".
- Unit 3's §3 consumes-from "the dry-run measurement recorded in this build's research record".
- Unit 1 cites "the dry-run journal".

`git log --all` shows that at every commit this build folder has held only `README.md` and `spec/`.
The name `retirement-readers` appears only in unit 1's revision log. The dry-run artifacts exist only
in a session scratchpad.

The owner made every ruling conditional on this dry run, and its record cannot be reached. Unit 2
deletes its own sixteen spellings "because the journal's eleven are re-derivable by anyone and a
private sixteen is not", but the journal is exactly as private. Nobody can re-open the skeptic's 42
names, the 22-minute window, the 13 re-spellings or stage 1's 0.00 precision.

**Fix.** Commit the journal and its skeptic record into this build folder's `build/` subfolder, in
hygiene check 5's grammar, and cite them by path from units 1, 2 and 3. Otherwise, mark each of those
figures unreachable, as unit 1 already marks its untracked probes, and correct the README sentence.
Under unit 1's corpus as specified, a committed journal would also resolve every name it spells. That
is one more reason H4's fix comes first.

**Left-shift.** A presence arm: a build README or spec that says "recorded in this folder's <kind>
record" reds when no file of that kind exists under the build folder. Run it over the tree before
wiring it.

### M7 — medium — unit 2 §2 S1 and S3 against §6 AC6: three arms and the case fold can be dead with the canary green

S1 specifies four grammar arms (active, passive, noun and fronted) under a case-insensitive match.
Every sentence AC1 and AC2 use is shaped for the active arm. S3's canary is one refused claim per
refusal CLASS, three in all, plus one clear, and nothing ties those four claims to four different
arms. AC6 breaks "one arm's compiled pattern" without naming which. No criterion observes an
uppercase claim verb, although §4 measured 37 of them.

So the passive, noun and fronted arms can all be dead, or case-sensitive, with every criterion and
the canary green. That is the probe-that-cannot-move shape the canary exists to refuse.

**Fix.** Make the canary carry at least one refused claim per ARM. Have AC6 replace each of the four
arms in turn and require the canary refusal each time. Add one fixture with an uppercase claim verb.

**Left-shift.** Apply §7's "a new gate is not landed until its failing case has been observed" per arm
rather than per gate. Add a §10 entry: a predicate built from N alternations owes N staged breaks.

### M8 — medium — unit 2 §2 S8 against §6 AC9: the floor can rise by one over a dozen assertions

S8 raises `FLOOR_ASSERTIONS` "by the static count of assertions those arms add". AC9 checks only that
the RAISED comment names this unit and that the comment's own arithmetic reaches the value. The suite
compares one way only, `if [ "$total" -lt "$FLOOR_ASSERTIONS" ]` at
`tools/check-spec-tokens.test.sh:451`, and the header of `tools/check-testsuite-counts.sh` says it
runs nothing. Both were re-read at synthesis. A raise of 1 over a dozen new arms therefore passes
AC9, the suite and the bar. Unit 1's AC19 grades exactly this delta against the block's assertion
count.

**Fix.** Give AC9 the form of unit 1's AC19: the delta from the base value equals the count of
assertion calls inside the added arms' line range, derived at observation time. Read the base from
the file, per H1, rather than typing 42.

**Left-shift.** When one unit of a build has the right form of a criterion, the audit should diff the
siblings' equivalents against it. That is a spec-audit checklist entry, not a gate.

### M9 — medium — unit 3 §2 S1: the primary home of the reason is read by no criterion

S1 requires a dated reason block immediately above the cap constants, naming the ruling, the measured
growth rate and the headroom. The goal's third clause is to record the reason where a reader of the
constant finds it, and §4 calls this home the primary one. S1 says AC1 and AC2 observe it, but AC1
reads check 6's verdict and AC2 reads the 81.92 quotient. AC7 and AC8 cover the two secondary homes.
AC7's red-when assumes the engine comment exists without checking it.

So the raise can land with no comment, or with a stale one, while every criterion stays green, and
the result ships to every adopter.

**Fix.** Add a criterion that reads the lines immediately above the cap constants in
`tools/memory-tree/check-memory-hygiene.sh` and finds a dated block naming `TOOL-dLoggedFlight-33`,
the 402 B/day rate, the headroom in days, and the fact that both keys moved.

**Left-shift.** The new criterion is the observation. The class is shared with H2, M2, M11 and M12;
see the section after the findings.

### M10 — medium — unit 3 §2 S3 against §6 AC5, and AC1's red-when: the example conf's line key is unobserved

S3 moves both keys in `tools/memory-tree/.memory-tree.conf.example`, which carries
`GUIDE_CAP_LINES="750"` at `:181`. AC5's fixture is 62270 B and 701 lines, the size of
`memory/guides/UNATTENDED-PROTOCOL.md` re-measured at synthesis. That is under the retired 750-line
cap, so an example that keeps the line key at 750 leaves check 6 silent and passes AC5. AC1's red-when
says that "either cap key" keeping its retired value reds, which is false for the line key at 701
lines. AC2's quotient covers only the engine's pair. The existing example-conf parity arm
(`tools/memory-tree/check-memory-hygiene.test.sh:2101` onward) checks that keys are declared, not
their values.

A fresh adopter who copies the example inherits the 750-line cap, and the protocol reds at line 751,
about 18 days out at the spec's own rate.

**Fix.** Build AC5's fixture above 750 lines and at or under 1000, at about 62270 B, so a retired line
key in the example reds. Correct AC1's red-when to name the byte key only.

**Left-shift.** Extend the example-conf parity arm to compare VALUES for keys where the engine default
and the example must agree, starting with the `GUIDE_CAP_*` pair. Run it over the tree first to find
the keys that legitimately differ.

### M11 — medium — unit 1 §2 S10 against §6 AC18 and AC13: a blank key disarms check 25 without a word

S10 says the `SPEC_FORMAT_CUTOFF` dependency is "written into the catalog entry and the arm's own
comment and then observed". AC13 observes the behaviour, but nothing observes the written
declaration: AC18's required-word list for entry 25 leaves out `SPEC_FORMAT_CUTOFF`. The five sibling
zero-population notices that S7 copies sit inside the `if [ -n "$SPEC_FORMAT_CUTOFF" ]` block opened
at `tools/memory-tree/check-memory-hygiene.sh:1132`, re-read at synthesis. A check-25 notice "on the
same footing" is therefore skipped too when the key is blank, and AC13's blank-key run requires no
notice. The conf example ships the key blank.

**Fix.** Have AC18 require entry 25 to name `SPEC_FORMAT_CUTOFF` as the key that disarms it. Have
AC13's blank-key run require one disarmed notice printed outside that block.

**Left-shift.** Turn §7's "a skip must announce itself" into a self-test arm. For each
blank-means-off key the engine reads, a run with the key blank must print a line naming the check it
disarms.

### M12 — medium — unit 4 §2 S1 against §6 AC1: the verbatim sentence is graded by its first 46 characters

S1 fixes a 429-byte sentence verbatim in §4, and §4 calls four of its words load-bearing. AC1 searches
only for the opening `The CHAIN of promotions is bounded by PRECISION`. §4 REJECTS a 373-byte trimmed
sentence that drops the override's ground. That sentence keeps the same opening, so it passes AC1. It
also passes AC6, which is a ceiling rather than an equality, and AC7, which counts lines the sentence
does not add.

**Fix.** Have AC1 search both files for the full §4 sentence verbatim and require exactly one hit in
each. B1's re-derivation may change the sentence, but the criterion's form stands either way.

**Left-shift.** A spec-audit checklist entry: text a spec fixes VERBATIM is graded by a verbatim match,
never by a prefix.

### L1 — low — unit 1 §2 S2 against §2 S9: multi-word phrases across a wrap

No fixture carries a multi-word strict phrase such as `no longer exists` or `leaves the vocabulary`:
AC24 isolates `DROPS` and AC25 the past tense. The reused accumulator joins each continuation line
with its raw indentation (`sj_txt[sj_ni] " " L`, `tools/memory-tree/check-memory-hygiene.sh:1334` at
`fcbfba5f`), and the spec states no whitespace normalisation. The lens found one wrapped phrase in the
live population at `016e87e8`: `aQuarriedLantern-1` S6's `no longer` / `exists`. That item also
carries `deletes`, so no verdict moves today.

**Fix.** State that the arm collapses whitespace before the verb test, and add a fixture that wraps a
multi-word phrase across a line break.

**Left-shift.** The fixture.

### L2 — low — unit 1 §5 error / empty / loading states: the empty-pattern direction is recorded inverted

§5 says `git grep -f` treats an empty pattern file as matching nothing. The skeptic reproduced the
opposite at `016e87e8`, in the form the spec specifies. With the exclusion pathspec,
`git grep -l -F -f <empty file>` lists 1555 of the 1556 non-spec tracked files, and a file holding
only a newline does the same. Git is also inconsistent across modes: 0 files with a sha argument or
with no pathspec, 868 with `HEAD`. And awk's `index(s, "")` returns 1, so a token that S5's
normalisation empties, such as a bare `:12` or a backticked `()`, resolves silently in the attribution
pass.

The guard itself is right. The recorded reason is wrong, and a maintainer reading §5 would conclude
that removing the guard is harmless.

**Fix.** Say that an empty pattern file matches every file in this invocation. Drop tokens that
normalise to empty before they reach either the pattern file or the attribution pass, and add that
case to AC2's fixture.

**Left-shift.** The fixture.

### L3 — low — unit 3 §3, the consumes-from `TOOL-dGatedProse-1` bullet (`:135`–`:137`): a phantom preset

The bullet says unit 1 "adds a preset to the engine's `*_CUTOFF` cluster, a blank declaration to the
conf example above line 180". Three things contradict it: the same bullet says no
`READER_INVENTORY_CUTOFF` was declared, unit 1 S1 says no key lands in the engine, the conf or the
conf example, and unit 1's own edge (`:196`–`:200`) calls this exact claim stale. A builder who
offsets the `:180`/`:181` and `:84` anchors by the phantom lines edits the wrong lines. The
anchor-grep rule limits the harm.

**Fix.** Delete the preset and conf-example half of the sentence, and keep the fixture-block offset.

**Left-shift.** None.

### L4 — low — unit 3 §2 S8 (`:51`), §4 (`:246`–`:251`), §7 (`:606`), §8 F2 (`:643`–`:645`); unit 4 §3 (`:64`, `:76`, `:78`, `:105`, `:107`), §7 (`:519`), §8 F2 (`:557`): positions from before the renumbering

Unit 3's header says order 4. Its prose still puts its engine edit at order 3 and unit 1 at order 1,
speaks of "the build's four write sets" and "the other two units", and dates check 25 and the claims
join "from order 1 and order 2 onwards".

Unit 4's header says order 5. Its prose says "at order 4 this unit", "Why order 3 and not order 1",
"edits the engine at order 1", "the bump sits at order 3" and "all four specs". It also cites unit 1's
"own S6" for the `tools/memory-tree/HYGIENE.template.md` edit. That edit is unit 1's S8; unit 1's S6
is the `fail 25` branch.

In fact unit 1 is at order 2, the claims join arrives at order 3, and unit 5 is a fifth write set that
touches no scan-set file. The relative epoch logic survives. The positions, the §7 dating and the
pair-rule warning's citation do not.

**Fix.** Restate the orders in both specs: unit 1 at 2, unit 2 at 3, unit 3 at 4, unit 4 at 5. Cite
unit 1's S8. Say five specs, and name unit 5 as writing no scan-set file.

**Left-shift.** The order-reference arm proposed under M5.

### L5 — low — unit 4 §5 error / empty row (`:409`): a refuted figure

§5 says a predicate "would be silent on 121 of 387 records". §4's table measures 101, 119 and 354 for
predicates A, B and C (`:245`–`:247`). §4 says at `:254` that rev-1's 266/121 does not reproduce, and
the revision log (`:624`) records the replacement.

**Fix.** Cite predicate C's 354 of 387, or the spread across the three predicates.

**Left-shift.** None. The no-count-in-prose rule already covers it.

### L6 — low — unit 5 §3 Non-goals (`:80`): the sibling's fixture block is sixteen

Unit 5 says "the fourteen fixtures" are unit 1's scope. Unit 1 S9 (`:90`), its edge (`:194`), Files
touched (`:887`) and §5 (`:940`) all say sixteen, `tFixture-200` through `tFixture-215`. The
non-goal's meaning is unaffected.

**Fix.** Point at unit 1's S9 without a count.

**Left-shift.** None.

## One class under five items

H2, M2, M9, M11 and M12 share one shape, and M10's AC1 red-when is a sixth instance. In each, an
S-item's "Observed by" line names criteria that read a different artifact, or a subset, or a prefix of
what the S-item obliges. It is the most frequent confirmed class in this set. One spec-audit checklist
entry states it: for each S-item, name the artifact and the population each observing criterion
reads, and check that together they cover the obligation. It is not mechanically gateable. A
spec-tokens arm could at most check that each "Observed by" criterion exists, and that check already
runs.

## Measured at synthesis, not findings

These notes carry no id and are not in the tally. They are recorded so that the rebase B1 and H1
require starts from facts rather than from this round's findings alone.

- The stale base reaches unit prose beyond B1 and H1. Units 1, 2 and 4 spell the kit version as
  `2.79` and the move as `2.79 → 2.80`, and `KIT_MEMORY_TREE_VERSION` is 2.82 on `origin/main`. Unit
  3's own S8 and AC3 derive both values, so they are unaffected.
- `tools/memory-tree/check-memory-hygiene.sh` is 2262 lines on `origin/main` against 2244 at the base.
  cMendedVintage's unit 13 changed check 6 there, so that a live run-state file leaves check 6 by
  class. Every line anchor units 1 and 3 hold into that file needs a re-grep after the rebase. The
  caps (`GUIDE_CAP_BYTES=61440`, `GUIDE_CAP_LINES=750`) and the top hygiene check numbers are the same
  on both refs.
- The stale base does not move unit 5's census population. The 24 live specs outside this build are
  the same files on both refs and byte-identical: `git diff HEAD origin/main` over them is empty.
- `SPEC_GUARD_LEGS_CUTOFF` is `2026-09-22` on `origin/main`, and the guards join dates a spec by its
  filename. Every spec in this set is dated `2026-09-20` or `2026-09-21`, so the guards join does not
  grade them as written. A unit split into a new spec dated on or after the cutoff would be joined,
  and would then owe the leg names its Files touched trips.
- `SPEC_AUDIT_DEFAULT` is blank in `origin/main`'s `.unattended.conf`, and this build's README
  declares no `spec-audit:` key. On the reconciled tree, therefore, the protocol does not owe this
  audit. Whether round 2 is owed there is the README's declaration to make; this record applies the
  M4 the set was written against.

## What this round did not cover, said so a green row is not misread

- No code exists yet, so every finding is against a spec. The 22 refuted findings are not listed here.
- Every lens read the specs against the tree at `016e87e8`, whose base is `fcbfba5f`. Only units 2
  and 4 were read against `origin/main` by a lens. The notes above are a synthesis spot check, not an
  audit of units 1, 3 and 5 against that ref.
- H4's 38-of-376 figure is the lens's measurement and was not re-run at synthesis. Its two named
  examples were re-run.
- This synthesis did not re-derive the census verdicts. H2 and H3 are the census defects the lenses
  confirmed. H3's fix, and round 2 over unit 5, re-read the table whole.

## Disposition

- **Unit 4: BLOCKED, NON-CONVERGED.** It owes the owner decision above. After that comes a rebase and
  a re-derivation that fold B1, M3, M12, L4 and L5, and then round 2.
- **Unit 5: NON-CONVERGED.** Rev-6 folds H2, H3, M1, M2, M4 and L6, plus H4's AC3 half and M3's
  hands-off edge. Round 2 is owed, and this is the unit where round 2 earns its cost: every census
  round so far has found errors in the same direction.
- **Unit 1: NON-CONVERGED.** It folds H4, M3, M11, L1 and L2. H4 changes the resolution corpus and the
  measured rate the wireability argument rests on, so round 2 is owed, and so is the owner fork above
  if the rate crosses 5%.
- **Unit 2: NON-CONVERGED.** It rebases, then folds H1, M5, M6, M7 and M8. Round 2 is owed because the
  join count, the floor base and the sibling precedent all change on the reconciled tree.
- **Unit 3: CONVERGED at round 1**, once M9, M10, L3 and L4 are folded and its anchors into the hygiene
  engine are re-grepped after the rebase.
- **Build-wide.** M6 is filed under unit 2, but its fix belongs to the README, and units 1 and 3 cite
  the same record. The fold order is: rebase every unit onto `origin/main` (B1, H1); settle unit 1's
  resolution corpus (H4), since unit 5's AC3 must match it; then fold unit 5's census; then units 2,
  3 and 4. That way no fold re-derives against a base it is about to leave.

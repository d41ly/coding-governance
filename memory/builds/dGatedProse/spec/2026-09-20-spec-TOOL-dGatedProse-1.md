# TOOL-dGatedProse-1 — a retirement answers for its readers, as a shape a machine reads

**Status:** SPECCED · rev-6 · 2026-09-21 · node d · Tier-2 · base fcbfba5f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md](../reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md) | spec-audit | TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-4 TOOL-dGatedProse-5 |

<!-- /gen:spec-records -->

## 1. Goal

A spec scope item that retires a name, a row kind or a vocabulary member must carry a `**Readers:**`
clause with a `by name:` half and a `by value:` half, and a new numbered hygiene check refuses the
item that carries neither. The class behind three consecutive spec audits of `dLoggedFlight` is a
reader the author never typed, and no predicate over prose can find one; what a predicate CAN do is
refuse to let the question go unasked, which is what those three audits had to ask by hand.

The population is every LIVE spec from the commit that lands the check, by the owner's ruling of
2026-09-21, with no cutoff key of any kind. That gives the check corpus work on day one, and by the
owner's second ruling of that day — fix it now — the work is done BEFORE the check exists:
`TOOL-dGatedProse-5` lands at order 1 and writes a clause on every item this trigger fires on, on
every node, so this unit lands at order 2 onto a corpus its own predicate already passes. What stays
here is S14, which verifies that and clauses whatever entered the population in between.

## 2. Scope (IN)

- **S1** — the POPULATION, and NO cutoff key. The arm grades a spec of check 12's own selection when
  that spec is LIVE, liveness being the engine's own spelling at
  `tools/memory-tree/check-memory-hygiene.sh:1385` — a status header that is not `CLOSED` and not
  `WONTDO`. No `READER_INVENTORY_CUTOFF` is declared, in the engine, in `.memory-tree.conf` or in
  `tools/memory-tree/.memory-tree.conf.example`, so there is no key to arm, to grandfather with or to
  discover. Observed by AC12 and AC13.
- **S2** — the TRIGGER, per §2 scope item, built over the HOISTED item accumulator of S11. An item
  triggers when a verb from the closed retirement list governs it AND the same item carries a
  backticked token of one of five identifier shapes, none of the three shape EXCLUSIONS applying; or,
  where it carries no such token, when a backticked bare word sits beside a declared kind noun.
  The list carries the PAST TENSE beside the present and the imperative, by the owner's O5 ruling of
  2026-09-21, and no identifier shape sets a markdown path apart, by the O6 ruling of the same day.
  The verb match is CASE-INSENSITIVE over every member of the closed list, the strict phrases, the
  four stems and the five past-tense forms alike, by the owner's ruling of 2026-09-21: this corpus
  capitalises a retirement verb for emphasis and at the head of an imperative item, and a
  case-sensitive match misses those items silently. The fold is `tolower()` over a COPY of the item,
  which the verb and kind-noun tests read; the identifier shapes read the item as written.
  Observed by AC1, AC7, AC8, AC9, AC10, AC11, AC24 and AC25.
- **S3** — the KIND-NOUN set, six phrases, as ONE literal in the arm immediately beside the verb
  list, because a verb table and a noun table in two carriers can disagree and no refusal can make
  them agree. `memory/HYGIENE.md`'s catalog entry POINTS at that literal and does not restate it.
  Observed by AC11.
- **S4** — the CLAUSE and its TWO escapes, one per graded question. A triggered item carries
  `**Readers:**`, then both `by name:` and `by value:`. The by-value half carries either a backticked
  token or the escape `NO VALUE READERS` followed by a reason. Every name the by-name half lists must
  RESOLVE, or that half carries the escape `READER NOT IN TREE` followed by a reason. A clause is
  graded wherever it appears, whether or not the trigger fired on that item. An escape is a claim
  about READERS and never a verdict about the item: an item that moves a value something compares
  answers its by-value half with those readers, whether or not any name leaves the tree. Observed by
  AC1, AC2, AC3, AC4, AC5 and AC6.
- **S5** — the RESOLUTION seam, and its cost. The arm emits each by-name token as a `\004`-tagged
  record; ONE batched `git grep -l -F -f` narrows the tree to the files matching any of them and an
  awk pass over those files attributes each token, against a corpus that is the tracked tree OUTSIDE
  `memory/builds/*/spec/`. A token also resolves when it IS a tracked path of that corpus. Before
  either test the token is normalised twice and no further: a `:<line>` citation tail is stripped,
  the pattern `tools/check-spec-tokens.py:76` already names, and so is a trailing `()`. The line
  number is not graded here. The escape's every covered name is PRINTED, so a skip announces itself.
  Observed by AC2, AC4, AC5 and AC17.
- **S6** — one `fail 25` branch, split out of the check-12 awk on its own control-character tag,
  whose message names the file, the offending item label, which half is missing or which name is
  unresolved, and the escape spelling that answers it. The tag byte is `\004`: `\001` is the
  canon-diff excerpt request, `\002` the base-sha sentinel and `\003` the edge records, which that
  awk's own comment at `tools/memory-tree/check-memory-hygiene.sh:1574` states. Observed by AC1,
  AC4 and AC6.
- **S7** — the zero-population notice, keyed on the LIVE count rather than on a cutoff, on the same
  footing as the FIVE sibling notices at `tools/memory-tree/check-memory-hygiene.sh:1830`-`:1867`, so
  an arm whose whole population has gone terminal says so instead of printing a silent green.
  Observed by AC16.
- **S8** — check 25's catalog entry, authored in `tools/memory-tree/HYGIENE.template.md` and
  re-rendered into `memory/HYGIENE.md`, whose own header states WHICH HALF IS GRADED HOW — the
  by-value half by presence, the by-name half by resolution, neither by completeness — and carries
  the control that proves why, that an escape is taken on trust, that the verb match ignores case
  and reaches the past tense, and that a markdown path counts as an identifier. The same header
  names BOTH classes of verb-bearing item the trigger never reaches, each with the reason it sits
  outside: an item whose backticked tokens hold no identifier shape, and an item that carries no
  backticked token at all. At `67bec01a` the first is 4 live items and the second is 8, so a header
  naming only the first is silent on the wider class and reads as coverage of it. The header states
  the two classes and not their sizes, because a count of a live population typed into a shipped
  doc is wrong on the next commit that writes a §2 item. The check-count
  sentence at `tools/memory-tree/README.md:18` moves with it, because the unit
  that changes the number of checks is the unit that owes the count.
  Observed by AC18.
- **S9** — the sixteen-fixture block `tFixture-200` through `tFixture-215` in the gate's sibling
  fixture suite, with the positive arm that arms the new branch, the three GREEN fixtures that pin
  the false-positive classes the three exclusions answer, the one that pins the liveness filter, the
  one that pins the case fold, and the two RED fixtures that pin the owner's O5 and O6 rulings.
  Observed by AC1 through AC12 and AC23 through AC25.
- **S10** — the DECLARED dependency, written into the catalog entry and the arm's own comment and
  then observed rather than asserted: check 25's population is check 12's SELECTION, so a blank
  `SPEC_FORMAT_CUTOFF` disarms check 25 whatever else is true. That is the WHOLE inherited set after
  S11 — not `SCOPE_JOIN_CUTOFF` and not an Acceptance heading, which rev-1 got wrong. Observed by
  AC13.
- **S11** — the HOIST. The §2 item accumulator moves out of the `SCOPE_JOIN_CUTOFF` guard and out of
  the both-headings test that today enclose it, to the awk's per-file level, under a guard that is
  the UNION of its consumers' own populations: check 12's date-filtered one and check 25's live one.
  Check 12's scope-join verdict keeps its identical composite condition, so its verdicts do not move.
  Observed by AC14 and AC15.
- **S12** — `FLOOR_ASSERTIONS` in `tools/memory-tree/check-memory-hygiene.test.sh:2460` is RAISED by
  the count of assertions this unit's fixture block adds, with a comment naming
  `TOOL-dGatedProse-1`, in the same commit that adds them. Observed by AC19.
- **S13** — the author-facing rule, written in the AUTHORED template
  `tools/memory-tree/SPEC-TEMPLATE.template.md` under its `## 2. Scope (IN)` skeleton heading at
  `tools/memory-tree/SPEC-TEMPLATE.template.md:268`, beside the `SCOPE_JOIN_CUTOFF` paragraph that
  already sits there, and then re-rendered into `memory/TEMPLATE-SPEC.md`. Observed by AC20.
- **S14** — the CORPUS, VERIFIED here and written by `TOOL-dGatedProse-5`. Under S1 the arm grades
  every live spec, and the trigger fires on 38 items across 20 specs at `67bec01a`, the figure §4
  derives for unit 5's census to match. The owner ruled
  on 2026-09-21 that those clauses are written now, and unit 5 writes every one of them at order 1,
  on every node, before this arm exists. This unit's build pass runs the arm over the tree it lands
  on. Any item it names entered the population after unit 5's pass, and it gains its clause in this
  unit's commit, additively, in unit 5's clause forms and under its collision protocol, whichever
  node owns the spec. The population is RE-DERIVED at the pass and never read from a table, because
  liveness moves and one item already moved between rev-3's figure and the commit that published it.
  Observed by AC21.

## 3. Non-goals (OUT)

- **The ruled predicate is NOT built.** `TOOL-dLoggedFlight-31` ruled a check that asks whether a
  spec inventories the readers of what it retires. The dry run refuted it and the skeptic reproduced
  the refutation independently, so nothing here tries to detect a missing reader. This unit builds
  the replacement the owner re-ruled on the dry run's evidence.
- **No COMPLETENESS half, ever, and the O4 ruling does not give one.** Grading that each listed name
  resolves is not grading that the list is complete: resolution tests the names PRESENT, and the
  class this check exists for is the reader nobody typed. A carrier that could close that class reads
  the CODE the retired name flows into and computes what depends on its value. That is a different
  check, in a different carrier, and it is a fresh owner ruling rather than a follow-up this unit
  opens. §4 measures the control against the O4 rule to show the gap is still there.
- **Two classes of verb-bearing item stay outside the trigger, and this unit closes neither.** Of
  the 50 live verb-bearing §2 items at `67bec01a`, 38 trigger and 12 do not. Four are the NAMED GAP
  §4 measures: backticked tokens, none of them identifier-shaped. The other EIGHT, across six specs,
  five items on node `a` and three on node `d`, carry no backticked token at all, and over the
  641-spec selection that class is 59 items across 48 specs. An item with no token gives a shape
  nothing to test and a by-name half nothing to resolve, so its author is never asked either
  question. It stays out because reaching it takes a trigger that reads prose rather than a
  backticked token, whose plain form is the verb alone — the reading the identifier conjunct exists
  to refuse, since the dry run's raw vocabulary flagged 19 of 24 live specs before a backticked NAME
  was required — and no ruling asks for it.
  Measured, a verb-only trigger would add all twelve untriggered live items and 126 over the
  selection, and read at item level the live eight hold ONE withdrawal with a reader:
  `TOOL-dGatedProse-4` S2, which deletes 450 bytes of guide prose that
  `tools/check-template-size.sh` reads by size. §4 enumerates the eight and reads each. The class
  is named here and in check 25's own header by S8, so a reader of the gate does not take its
  silence on a token-less item for coverage.
- **NO KIT-VERSION BUMP AND NO MARKER RE-STAMP, and the reason is topological rather than a
  deferral.** `tools/memory-tree/check-verdict-epoch.sh` requires the newest commit in `<base>..HEAD`
  that moves a behaviour-bearing line of its scan set to be an ancestor of, or equal to, the newest
  commit that CHANGES `KIT_MEMORY_TREE_VERSION` — the rule is stated at `:16`-`:24` and implemented
  as `git merge-base --is-ancestor "$W" "$S"` at `:179`. This unit moves the engine at order 2 and
  `TOOL-dGatedProse-3` moves it again at order 4, so a bump here would leave the last change
  DESCENDED from the bump and red that leg from unit 3's commit through the build's tip. The single
  move is therefore unit 3's, in its own commit, together with the re-stamp of every carrier of the
  retired marker from a derived population. This unit's own commit leaves the constant at 2.79 and
  every marker with it, which reds `verdict epoch` at order 2 and order 3 and is closed at order 4
  — §7 states that plainly rather than letting a bar discover it.
- **No adopter phase-in.** With no cutoff key, an adopter installing this kit gets check 25 live over
  their own live specs on the next bar, with nothing to set. That is the owner's ruling of
  2026-09-21 and it is written here rather than softened: the compensating property is that the cost
  of a false trigger is one line of prose and the population is live specs only, never the landed
  corpus.
- **The README's check COUNT is not made derivable.** `tools/memory-tree/README.md:18` writes a count
  of a derived population in prose, which the charter's own rule forbids, and that count is already
  stale: it reads 23 while the tree implements 24, because check 24 rides `row_grammar.py` the way 20
  does and the sentence never gained it. S8 corrects the sentence to 25 and enumerates 24 beside 20
  rather than deriving either. Deriving it is a follow-up row, not a scope item, because the fix is a
  new print mode on the engine.

### Edges

- **consumes-from** `TOOL-dGatedProse-5` — the corpus. That unit lands at order 1 and writes a
  `**Readers:**` clause on every item this trigger fires on, on every node, so this arm arrives onto
  a corpus its own predicate passes and S14 is a verification plus whatever delta the population
  gained in between. Two specifics cross here. The TRIGGER is this spec's and that unit consumes it
  as a specification: a change to the verb list, the shapes, the exclusions, the kind nouns or the
  case rule after that pass moves the population under a corpus already written. The owner's O5 and
  O6 rulings of 2026-09-21 are such a change, made before that pass, and §4 derives the combined
  population as ONE figure, 38 items across 20 specs at `67bec01a`, with the chain that reaches it,
  for that unit's census to match. And the per-item record is that unit's census; this spec carries
  the population figure and the rule, and no table of items.
- **hands-off** `TOOL-dGatedProse-2` — `tools/memory-tree/SPEC-TEMPLATE.template.md`, where S13
  writes this check's author-facing line, and `memory/TEMPLATE-SPEC.md`, which this unit re-renders
  from it. Unit 2 edits both carriers for its own dossier-claims rule, must write into the TEMPLATE
  and never the render, and reads the line this unit left. The kit version does NOT cross here: the
  marker that unit reads is the 2.79 at the pinned base, unchanged by this unit, and the single move
  is unit 3's.
- **hands-off** `TOOL-dGatedProse-3` — `tools/memory-tree/check-memory-hygiene.sh` and its fixture
  suite, which this unit leaves with one new `fail 25` branch, the S11 hoist, a `\004` tag split, a
  zero-population notice, a sixteen-fixture block and a RAISED `FLOOR_ASSERTIONS`. Four specifics,
  because "read the state I left" is not actionable on its own. **THE `*_CUTOFF` CLUSTER DOES NOT
  MOVE**: rev-2 inserted a preset line above `tools/memory-tree/check-memory-hygiene.sh:84` and rev-3
  deletes that key entirely under the owner's O2 ruling, so the `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES`
  pair unit 3 cites stays on its base line, and that unit's own rev-3 statement that this unit adds a
  preset and a conf-example declaration is STALE in its favour — neither file gains a line from here,
  and `tools/memory-tree/.memory-tree.conf.example` is outside this unit's write set altogether.
  **THE SELF-TEST COORDINATES DO MOVE**, by the fixture block's own length, below its insertion
  point. **THE ASSERTION FLOOR IS NOT THE BASE VALUE**: unit 3's criterion must read the raised
  number, not 374. And **the kit version is unit 3's own**, which its S8 now owns: this unit neither
  bumps nor re-stamps, and `verdict epoch` is red from this commit until unit 3's places the move at
  or after its engine edit.
  One more crossing, in unit 3's favour: its S8 carries a `**Readers:**` clause, and the clause is
  REQUIRED. The item triggers on the strict phrase `is replaced by`, which entered that file in
  `c7750bf8` — the commit that landed this spec at rev-3 — four words ahead of its `retired`. The
  clause's by-name names must resolve or carry `READER NOT IN TREE` with a reason (S4), and unit 5's
  census verifies it without rewriting it.
- **hands-off** `TOOL-dGatedProse-4` — two crossings, neither of them a marker. This unit edits the
  engine at order 2, which is one of the two behaviour-bearing moves the epoch rule ranges over, so
  the build's single bump being mis-placed surfaces at unit 4's bar as well as at unit 3's. And this
  unit's render pass regenerates all four dogfood pairs from their templates,
  `memory/guides/BUILD-METHOD.md` included, which is unit 4's whole write set — byte-identically at
  order 2, because nothing in that write set has moved yet. Unit 4's own rev-3 reads both of those
  correctly, and it also reads the third crossing: check 25 grades unit 4's spec, and no §2 item of
  it fires.
- **consumes-from** external — the `SPEC_FORMAT_CUTOFF` declaration this repo already carries. With
  it blank the new check is disarmed, which S10 declares and AC13 observes; it is not a defect this
  unit closes.

## 4. Design

### The population, and what it costs

The owner ruled on 2026-09-21 that this arm declares no cutoff and grades every LIVE spec from the
commit that lands it. Two things follow, and both are measured rather than asserted.

Liveness is not a new predicate. The engine already carries one, for the base-sha arm at
`tools/memory-tree/check-memory-hygiene.sh:1385`, whose comment states the reason in the terms this
unit needs: "TERMINAL specs are excluded. A landed record is frozen and this repo does not rewrite
one to clear a hit, so the population is the specs a build can still change." The test is
`hdr !~ /^\*\*Status:\*\* (CLOSED|WONTDO)/`, a NEGATIVE test over the seven-value status vocabulary
the same file pins at `:844`. This arm reuses that spelling verbatim, in the same file, rather than
minting a second one.

There IS a second spelling in the tree, and the divergence is stated rather than left to be
discovered: `tools/check-spec-tokens.py:87` defines live as the positive whitelist
`OPEN|SPECCED|INPROGRESS|BLOCKED`. The two disagree on `DEFERRED`, and the disagreement is sized —
OWN-PROBE over this tree today, 37 specs are live by the engine's test and 28 by the whitelist, the
nine-spec difference being exactly the `DEFERRED` ones. This arm takes the engine's test because it
lives in the engine and because the negative form fails LOUD: an unknown status value is graded
rather than silently dropped. One of the nine is a node-`d` spec the corpus pass therefore
reaches, `dScaffoldedMirror-9`, and unit 5's census counts it.

**THE MEASUREMENT, OWN-PROBE, 2026-09-21.** The probes are `probe_final_rev3.py` and
`probe_cost_rev3.py`, re-run at rev-4 against `32f2eb71` as `probe_u1_rev4.py` and its siblings,
and at rev-5 against `67bec01a` and `32f2eb71` as `probe_u1_rev5.py` and its siblings, and at rev-6
as `probe_u1_rev6_tokenless.py` over the same two commits, all written to this session's scratchpad. They are UNTRACKED, so nothing in the
tree resolves them and a later reader cannot re-open them — which is why every figure below is
stated with what it is a count OF. The table reads `32f2eb71`; the next section carries the same
chain at `67bec01a`.

| population | size | derivation |
|---|---|---|
| tracked spec-shaped files | 642 | the engine's own check-12 path regex |
| at/after `SPEC_FORMAT_CUTOFF` 2026-07-15 | 640 | check 12's selection, which check 25 inherits |
| LIVE within that selection | 37 | the `:1385` liveness test |
| triggered items | 38 across 20 specs | the shipped trigger below: case-insensitive, past tense included, no `.md` exclusion |
| the accumulator's union population | 120 | live 37 ∪ the 89 at/after `SCOPE_JOIN_CUTOFF` |

The dry-run journal reports a different pair over a different set — "the raw verb vocabulary flagged
19 of 24 live specs, requiring a backticked NAME brought it to 14" — and those are SPECS, over a
24-spec reading of liveness. The 38 here are ITEMS, over 37. Do not conflate them; the corpus grew
and the liveness test is now the engine's rather than the journal's.

### 38 — the combined population, and the chain that derives it

The owner's two rulings of 2026-09-21 on F9 and F10 move the population together, and the two moves
do not add. So the figure is derived over the combined rule rather than summed from either ruling's
own measurement, at `67bec01a`, the commit both unit specs are folded from:

| step | count | what is counted |
|---|---|---|
| tracked spec-shaped files | 643 | the engine's check-12 path regex |
| at/after `SPEC_FORMAT_CUTOFF` 2026-07-15 | 641 | check 12's selection |
| LIVE | 38 | the `:1385` test; every one carries a `## N. Scope (IN)` heading |
| §2 items | 325 | column-0 bullets under that heading, continuations joined, fenced lines excluded |
| verb-bearing | 50 | the closed list below, folded |
| **triggered** | **38 items across 20 specs** | an identifier-shaped token, or a bare word beside a kind noun |

The same rule reads 38 across 20 at `32f2eb71`, through 642, 640, 37, 316 and 51. Between the two
commits `TOOL-dGatedProse-5` entered the live set with nine §2 items and triggers on none of them,
and this spec's own S14 left the verb-bearing set. The node split is 27 items across 14 node-`a`
specs, 3 in one node-`b` spec and 8 across 5 node-`d` specs.

The twelve verb-bearing items that do not trigger split four and eight, and the chain accounts for
every one: four are the named gap, backticked tokens with no identifier shape, and eight carry no
backticked token at all. Both classes are measured in "The NAMED GAP that remains" below. At
`32f2eb71` the thirteen split five and eight.

**Why the two figures do not add.** Every one of rev-4's 23 survives. O5 alone adds 8 items and O6
alone adds 4, and 3 more need BOTH, a past-tense verb and a markdown path as the item's only
identifier: `aMendedLedger-2-u1` S6, `aPacedTurnstile-14` S9 and `dPolishedVitrine-14` S2. So
23 + 8 + 4 + 3 = 38. O5 alone gives 31 and O6 alone 27, and 31 + 27 − 23 is 35: the three items each
ruling needs the other for are in neither ruling's own figure.

**O6 alone is 27, not the 25 rev-4's F10 printed, because the exclusion had two spellings.** rev-4
measured the drop by lifting the global `.md` test and left the dot shape's "other than `md`" clause
standing, so a markdown path with no slash stayed out. That reading admits `memory/README.md` and
refuses `README.md`, one file with two verdicts by how its author spelled the directory, and it is
not what O6 says. rev-5 deletes both clauses. The two items the second deletion adds are
`aMendedLedger-6-u6` S1 and S5, on `parallel-coding-governance.template.md` and
`WIRE-INTO-PROJECT.md`. Under the slash-only reading the combined rule would give 34 across 18; the
figure is 38.

**One label is not unique.** `aTunedCompass-9`'s item `S5c-i` enters on `removed`, and the label
derivation the arm reuses at `tools/memory-tree/check-memory-hygiene.sh:1332` cuts it to `S5c`,
which two sibling items of that spec share. A check-25 row for it names `S5c`, so unit 5's census
anchors that clause on the item's visible label, `S5c-i`. The count is unaffected: the probe counts
items, not labels.

### The trigger, and every figure it rests on

The VERB list is closed, and it starts from the strict list the dry run stated literally:
`retires`, `is replaced by`, `are replaced by`, `removes`, `deletes`, `drops`, `no longer exists`,
`no longer carries`, `no longer reads`, `stops being`, `ceases`, `goes away`, and
`leaves the` followed by `layouts`, `set` or `vocabulary`. To that list this unit ADDS the four bare
imperative stems `retire`, `delete`, `remove` and `drop`, matched at a word boundary, and the
addition is the single most consequential decision in this spec. By the owner's O5 ruling of
2026-09-21 the list also carries the five past-tense forms `retired`, `replaced`, `removed`,
`deleted` and `dropped`, each matched at a word boundary on BOTH sides, like the stems. The boundary
is measured rather than tidy: as bare substrings the past forms match inside the camel-case slug
`dRetiredFork`, and at `67bec01a` that reading pulls two items of `DEPL-dRetiredFork-2` into the
population, neither of which retires anything. EVERY member of the list is matched
case-insensitively, and the section "Case, by ruling" below states the ruling and what it measures.

Measured over the 38 live specs at `67bec01a` under the shipped shapes, OWN-PROBE and
case-insensitive: the strict list alone triggers 15 items across 10 specs; adding the imperative
stems gives 27 across 15; adding the past tense gives the shipped 38 across 20. The stems add 5
specs, the figure rev-3 measured at `85f1d6d8` and three independent readings produced at rev-2 over
a smaller corpus; their item delta is 12 here against the 10 rev-4 measured under the shapes it then
carried. The past tense is no substitute for the stems: the strict list plus the past tense reaches
none of the three items named below, and the strict list plus the stems reaches all three.

The items the stems add include every one of the three the dry run named as a real, uninventoried
retirement that a whole-spec predicate could not red — `aMendedLedger-3-u2` S6, where
`tools/workflows/drift-audit-state.js` has ten reference sites and no named reader,
`aMendedLedger-3-u2` S3, and `aMendedLedger-4-u3` S3, where `index_set()` loses two session-ledger
lines. All three are absent from the strict set and present in the stems set, so the coverage claim
is invariant. The strict list misses all three because this corpus opens a retirement scope item in
the imperative and the strict list holds only third-person and passive forms.

Two forms the dry run's lenient vocabulary admitted are deliberately REFUSED, and the reason is the
skeptic's own finding. `stops` followed by a gerund and `no longer` followed by any word both match
prose describing a runtime behaviour rather than a retirement. The measured instance is
`dPolishedVitrine-14` S5, verified at
`memory/builds/dPolishedVitrine/spec/2026-09-13-spec-TOOL-dPolishedVitrine-14.md:41`, where a test
arm "stops copying the cwd-relative `$LEG`" — a behaviour change inside a fixture, not a retirement
of anything.

The IDENTIFIER test is a closed set of five shapes, and a bare word is not one of them:

| shape | admitted because | measured instance |
|---|---|---|
| contains an underscore | snake case and shouted constants | `split_regions`, `SHARD_ARITY` |
| contains a slash | a path, to code or to a document | `tools/check-kit-versions.sh`, `memory/archive/ledger/{a,b,c}.md` |
| contains a dot whose tail segment is word characters | a qualified symbol, a script or a document | `merge.conflictStyle`, `inventories.json`, `WIRE-INTO-PROJECT.md` |
| carries an internal case transition, a lowercase letter immediately followed by an uppercase one | camel and Pascal identifiers | `conflictStyle` |
| two dashes then a letter | a long option | `--write-ratchet` |

THREE token classes are EXCLUDED by shape, and one normalisation precedes every shape test. Each
exclusion answers a measured finding, and each is re-derived at `67bec01a` under the shipped list:

- **A family-slug-seq id is never an identifier.** Measured: one backticked id sits inside a
  verb-bearing live item, `PLAY-aPrunedCeremony-5` in `aMendedLedger-1` S7, whose item closes a
  decision row and retires no name; over the 641-spec selection the exclusion keeps 14 items out.
- **A token that is only dashes and digits is never an identifier.** This is the skeptic's
  elided-slug class. §2 of the charter sanctions family-plus-seq shorthand in prose, so the pair
  `TOOL-dLoggedFlight-21` and `-24` puts a bare `-24` in backticks, and a flag-shaped test reads it
  as a retired name. Measured over the live population: ZERO such tokens sit inside a verb-bearing
  item, so the exclusion changes no verdict today and is a forward guard.
- **A token carrying a SPACE is never an identifier.** NEW at rev-3. A backticked CODE FRAGMENT or
  config line is not a name: measured, the exclusion keeps exactly one live item out,
  `aBatchedLintel-1` S3, whose only candidate token is `body=$(_unfenced "$f")`, and 7 over the
  selection. The item is innocent under the eye and would otherwise cost a real clause.
- **A `:<line>` tail is stripped before every shape test.** The normalisation, and not an exclusion.
  A shape judges the NAME, and a citation tail is not part of it: `check-spec-tokens.py:76` has a
  dot whose tail segment is `py:76`, which is not word characters, so without the strip a cited
  script or document with no slash would read as a bare word. Measured, the strip changes no live
  verdict today. It is specified anyway because S5 applies the same strip before resolution, and
  one token view for both questions is one spelling rather than two. The precedent is
  `tools/check-spec-tokens.py`'s own `CITE_TAIL` at `:76`, which exists for the same reason one file
  over.

A further exposure was looked for and is absent: a bare version token such as `2.79` would pass the
dotted-tail shape, and ZERO verb-bearing live items carry one, re-derived at `67bec01a` under the
shipped list. It is recorded rather than guarded, because a guard against a class the corpus does
not produce is a clause no fixture can observe honestly.

### Shape 6 — the bare word, admitted beside a kind noun

The skeptic's other finding is that a permissive identifier test admits row-layout vocabulary words:
over the control spec it collected 42 "retired names" including `commit`, `push`, `phase`, `brief`,
`gate`, `idle`, `verb`, `UTC`, `event`, `elided`, `checks` and `label`. Those recur in every spec
touching the runlog, so a name-bound reader test can never fail once one of them is in the set.

The owner's ruling names three kinds of retired thing, and one of them — a vocabulary member — is
often spelled as a bare lowercase word. rev-2 drafted a conditional sixth shape for it, measured it
at zero, and dropped it. **The owner reinstated it on 2026-09-21 as a PROSPECTIVE closure of the
named gap, on exactly that evidence: it fires on nothing today, so it adds no corpus work, and the
gap is then closed by a rule rather than by remembering.** So it is built, and it is built
conditional: a backticked bare word counts as the retired thing when, and only when, the same item
also carries one of six declared KIND NOUNS.

The set is six multi-word phrases: `row kind`, `vocabulary member`, `status value`, `enum value`,
`status token`, `phase name`. Matched case-insensitively as substrings of the accumulated item.

**Where it is declared: in the arm, in `tools/memory-tree/check-memory-hygiene.sh`, as ONE literal
immediately beside the verb list.** Not in `.memory-tree.conf`, and the reason is not tidiness. The
verb list and the noun set are two halves of ONE predicate; split across two carriers they can
disagree, and no refusal can make an adopter's conf agree with the kit's verbs. A conf key would
additionally need the `READINESS_ROWS` treatment — an armed rule with an empty declaration grades
nothing and must REFUSE, which `tools/memory-tree/check-memory-hygiene.sh:70`-`:75` spells out for
exactly that case — which is machinery bought for a shape that fires on nothing. The catalog entry
in `memory/HYGIENE.md` POINTS at the literal and states the noun count without listing the nouns,
so there is one text and no copy to drift.

**Why multi-word phrases and not single nouns.** Measured, OWN-PROBE: a wider ten-noun candidate set
containing the single word `marker` fired on one item over the 640-spec selection —
`memory/builds/dLoggedFlight/spec/2026-09-13-spec-TOOL-dLoggedFlight-4.md:48` S4, whose verb comes
from the decision token `skip-delete` and whose "marker" is a clean-exit marker in behaviour prose.
Under the shipped list at `67bec01a`, `marker` beside the six phrases fires on a second item,
`aBatchedTribunal-6` S1b, whose marker is a build lock written before the first read and cleared in
a `finally`. Neither item retires anything. The six-phrase set fires on ZERO items over the live
population AND zero over all 641 selected specs, re-derived at `67bec01a` under the shipped list,
which is the property the owner's ruling rests on and for which the fixture `tFixture-207` is the
whole coverage.

### Case, by ruling — and what the fold does not reach

**The verb match is case-insensitive, by the owner's ruling of 2026-09-21.** This corpus writes a
retirement verb in capitals for emphasis and opens an imperative item with a capital, and it does
both on the items that matter most. A case-sensitive trigger misses those silently, which is the
false-pass direction a shape check exists to close; a case-insensitive one costs, at worst, a clause
on an item that retires nothing.

Measured at `67bec01a` under the shipped list and shapes, OWN-PROBE, four readings over the same 38
live specs:

| reading | triggered | what it loses against the ruling |
|---|---|---|
| every member folded, the ruling | 38 items across 20 specs | nothing |
| strict list exact, the rest folded | 37 across 20 | `dPolishedVitrine-1` S5 and its `DROPS` |
| past tense exact, the rest folded | 36 across 20 | `aMendedLedger-2-u1` S6 and `aMendedLedger-6-u6` S6, both on `RETIRED` |
| everything exact | 29 across 20 | nine items |

The nine are not a random sample. Six open with a capitalised imperative stem: `aMendedLedger-2-u1`
S5 and `aMendedLedger-3-u2` S2 with `Delete`, `aMendedLedger-3-u2` S6 with `Remove`,
`aMendedLedger-4-u3` S3 with `Drop`, and `aMendedLedger-1` S2 and `aMendedLedger-4-u3` S7 with
`Retire`. The seventh is the `DROPS` above, and the last two are the `RETIRED` pair, the ruling's own
example. The corpus pass's census reads the six rev-4 carried as GENUINE retirements, two of them
among the three the dry run named as the reason this class was ruled gateable at all; the three the
rulings add are read in the precision section below.

**How it is built.** The arm folds a COPY of the accumulated item through `tolower()` and runs the
verb and kind-noun tests over that copy. That is POSIX awk, and it is the idiom the engine already
uses for `red when:` at `tools/memory-tree/check-memory-hygiene.sh:1259`. It is never gawk's
`IGNORECASE`, which mawk reads as an ordinary unset variable: the arm would stay case-sensitive,
silently, on exactly the interpreter the engine's portability note at `:1156` names. AC24 pins both.

**Where the fold stops, and why each boundary sits where it does.**

- The IDENTIFIER shapes read the item as written. Shape 4 is a lowercase-to-uppercase transition, so
  a whole-item fold would erase every camel-case identifier; AC24's second item is the arm for that.
- The MARKERS and the two escape spellings stay exact bytes. A case slip there is a false RED whose
  message prints the spelling that answers it, which is the safe direction; a case slip in the
  trigger is a silent false pass. The ruling closes the second, and the first needs no closing.
- The fold reaches CASE, and INFLECTION only where the list names it. Since O5 the list names the
  third-person present, the imperative and the past; a gerund is none of them, so `retiring` or
  `dropping` matches in no case. Measured at `67bec01a`, the five gerunds would add 2 live items. No
  ruling asks for them and none is added.

### The NAMED GAP that remains, measured

**Pinned rather than implied away.** A retirement whose backticked tokens hold no identifier shape —
a bare word with no kind noun beside it, `run()` included, a hyphenated bare word such as
`check-brief-recorded`, a family-slug-seq id, or a space-bearing fragment — is NOT triggered, so its
author is never asked the by-value question.

Measured over the live population at `67bec01a` under the shipped list and shapes, OWN-PROBE: 4
items, enumerated rather than counted so a later reader can re-judge each — `aBatchedLintel-1` S3,
`aGradedDoorway-7` S4 on `run()`, `aMendedLedger-1` S7, and `aMendedLedger-6-u6` S3. Over the whole
641-spec selection it is 67 items against rev-4's 54, because across the landed corpus the past
tense makes more items verb-bearing than O6 lets out of the gap. Read at item level, none of the
four live members retires a name: two describe behaviour, one closes a decision row, and one sweeps
a word out of prose. So the live gap holds no retirement today, and that is a measurement of this
corpus rather than a property of the rule. Shape 6 still reaches no bare word that lacks a kind
noun, because inventing one to satisfy a gate is the mirror this repo forbids elsewhere.

**A SECOND unreached class, which the gap figure does not count.** The 4 above carry backticked
tokens and none of an identifier shape. An item that carries NO backticked token is outside the
trigger for a more basic reason: there is no token for a shape to test, no bare word for shape 6 to
admit, and no name for a by-name half to resolve. It sits in neither the 38 nor the 4, and rev-5
named only the 4, which let the smaller class read as the whole of what the trigger misses.
Measured at `67bec01a` under the shipped list and shapes, OWN-PROBE: 8 live items across 6 specs,
five on node `a` and three on node `d`, which with the 38 and the 4 accounts for all 50 verb-bearing
items; over the 641-spec selection, 59 items across 48 specs. Enumerated so a later reader can
re-judge each — `aMendedLedger-1` S6, `aMendedLedger-8-u9` S3, `aTunedCompass-3` S5,
`aTunedCompass-9` S3 and S5c-ii, `TOOL-dGatedProse-3` S4 and S6, and `TOOL-dGatedProse-4` S2. The
engine's label derivation would cut S5c-ii to `S5c`, as §4 already records for its sibling S5c-i.

Read at item level, and unlike the named gap, this class holds a withdrawal with a reader:

- **four describe behaviour and retire nothing.** `aMendedLedger-8-u9` S3's verb is a driver that
  must never lose a row, `aTunedCompass-3` S5's an id no longer reported missing, `aTunedCompass-9`
  S3's a sampling method that takes out an authorship bias, and S5c-ii's the green-by-absence shape
  its build exists to refuse.
- **one points at a retirement its siblings carry.** `aMendedLedger-1` S6 re-trues the docs the
  ledger's retirement falsifies, and that retirement's own named items, the same spec's S1 and S2,
  are in the 38.
- **two move spellings of a value.** `TOOL-dGatedProse-3` S4 and S6 carry the prose and fixture
  spellings of the guide cap pair whose value that spec's S1 moves by path. S1 carries no
  retirement verb, so the move is outside the trigger at its source, and these two name no token,
  so they are outside it at the spellings too.
- **one is a withdrawal with a by-value reader, and check 25 asks nothing of it.**
  `TOOL-dGatedProse-4` S2 deletes four spans of guide prose, 450 bytes, from a file whose size
  `tools/check-template-size.sh` grades against the row at `tools/template-size-limits.txt:86`.
  Its author would name that reader if asked, and the trigger never asks, because the item names
  the file it edits only in prose.

**Why the class stays out.** Reaching an item with no token takes a trigger that reads prose rather
than a backticked token, and the plain form of that is the verb alone, which is the reading the
identifier conjunct exists to refuse: the dry run's raw vocabulary flagged 19 of 24 live specs
before a backticked NAME was required. Measured here, a
verb-only trigger adds all twelve untriggered live items, the gap's 4 and these 8, and 126 over the
selection, for one withdrawal with a reader among the live eight. No ruling asks for it and none is
added. What this unit does is SAY so: S8 puts both classes in check 25's own header, AC18 observes
the sentence, and an author's remedy is the one the named gap has — name the withdrawn thing in
backticks, and the item then triggers.

### The trigger's measured precision, reconciled with the corpus pass's census

Over the live population the shipped trigger fires on 38 items across 20 specs. The item-by-item
verdict is `TOOL-dGatedProse-5`'s census, which read rev-4's 23 against code and whose skeptic
re-read them. The 15 the owner's O5 and O6 rulings add were read HERE, at item level and not against
code, so their share of the split below is provisional until that census re-reads them. This
section asks one narrower question: did the trigger fire on a RETIREMENT, a name, row kind or
vocabulary member leaving the tree? The answer splits three ways.

- **18 are retirements.** Thirteen are rev-4's: the census's twelve GENUINE items at its rev-1, less
  `TOOL-dGatedProse-3` S8, which moves a value and sits in the next row; plus
  `bConvergentLodestar-1` S3, whose retired file lives in another repo and is exactly what the
  by-name escape exists for; plus `aMendedLedger-1` S1. That last one fires on the wrong token, the
  slug `bThriftyBellows`, but the item does retire three named paths: `memory/project/MEMORY.md`,
  `IN-FLIGHT.md` and `project/README.md`, per that spec's own migration table. The engine's comment
  at `tools/memory-tree/check-memory-hygiene.sh:497`-`:498` still spells all three. Five are new:
  `aMendedLedger-1` S2, the authored ledger moved to the archive; `aMendedLedger-6-u6` S1, which
  deletes the charter template's ledger lines, and S6, which records the ledger's retirement for
  adopters; `aQuarriedLantern-1` S5, whose fork of `query.py` withdraws a node-registry lookup; and
  `aTunedCompass-3` S2, which deletes `check-recall.py`'s two copied tuples.
- **4 move a value and retire no name.** Three are rev-4's: `aGradedDoorway-7` S2 raises
  `SHARD_ARITY`, `TOOL-dGatedProse-3` S8 moves `KIT_MEMORY_TREE_VERSION`, and `aMendedLedger-8-u9`
  S11 neutralises `merge.conflictStyle`. The fourth is `aTunedCompass-9` S5c-i, which moves the set
  an audit grades in from a pin to a per-fixture declaration and names `test_audit_green` as a
  reader in its own text. None is a retirement by the owner's taxonomy, and none may answer its
  by-value half with the escape either, because each value has a reader.
  `tools/unattended/check-unattended.test.sh:46` compares a shard count against `SHARD_ARITY`; S8's
  own clause names the version's readers; and `tools/memory-tree/merge-rows.test.sh:1209` loops two
  conflict styles through the driver. One rule decides all four, and the clause section states it.
- **16 are false triggers**, whose verb sits in behaviour, correction or creation prose and whose
  item changes nothing another file reads. Seven are rev-4's: `aQuarriedLantern-1` S6,
  `aMendedLedger-5-u5` S5, `aMendedLedger-7-u8` S5, `bConvergentLodestar-1` S2, `dPolishedVitrine-1`
  S10, and `dScaffoldedMirror-9` S6 and S7; the census escapes all seven, and its skeptic read each
  escape as honest. Nine are new: `aMendedLedger-2-u1` S4 and S6, `aMendedLedger-6-u6` S5,
  `aPacedTurnstile-14` S9, `aTunedCompass-9` S2b, `aWalkedCorpus-2` S5, `bConvergentLodestar-1` S4,
  `dPolishedVitrine-14` S2, and `TOOL-dGatedProse-4` S3, which widens a pointer.

So precision is 18 of 38 counted as retirements, and 22 of 38 counted as items whose clause has
something true to list: just under a half to just under six in ten, against rev-4's half to seven in
ten over 23.

A false trigger costs the author one line. That asymmetry is why a trigger at this precision is
wireable when the refuted predicate at precision 0.00 was not, and the owner's case, past-tense and
`.md` rulings rest on the same asymmetry read the other way: a missed retirement costs a gate that
cannot fail.

### The clause, and exactly what is graded

The shape, with invented identifiers so that nothing here reads as a claim about this tree:

```markdown
- **S4** — retire the `shard_arity` pin and the two rows it carried.
  - **Readers:** by name: `check_shard_split` and `report_shard_rows` spell the pin.
    by value: `test_fresh_three_shapes` reads a Coverage row by a cell count of six, and
    `parse_floor_raise` knows only the word `RAISED`.
```

The clause sits on the item's own opening line or on any line beneath it, which is the latitude the
acceptance-witness and failure-mode rules already grant and matches this corpus's wrap style. A
sub-bullet indented beneath a column-0 item is a continuation of that item, so the form above is one
item and is graded as one.

GRADED, and the catalog entry says so in these terms:

- the literal `**Readers:**`, then the literal `by name:`, then the literal `by value:`;
- the by-value half BY PRESENCE — either a backticked token or the literal `NO VALUE READERS`
  followed by at least one further non-space character;
- the by-name half BY RESOLUTION — every backticked token it carries must resolve in the tree, or the
  half carries the literal `READER NOT IN TREE` followed by a reason.

NOT GRADED: completeness, on either half, for the reason the next sub-section measures.

**An escape is a claim about READERS, never a verdict about the item.** `NO VALUE READERS` asserts
that nothing reads the value of what the item changes. An item the trigger fires on that retires no
name but moves a value — a pin raised, a constant's value replaced, a config neutralised — answers
its by-value half with that value's readers, and the escape there is false even though the item is
not a retirement. That is the one rule for the four value-move items of the precision section, and
it settles the pair the corpus pass's skeptic found sorted two ways. The arm grades presence, so it
cannot tell a true escape from a false one, and once written a false one passes for good; the
catalog entry says so in terms (AC18). `READER NOT IN TREE` on a by-name half that lists no names
covers nothing: the arm neither refuses it nor prints anything for it, and the honest form for an
item with no by-name reader is prose on that half, which passes by vacuity.

**A clause is graded wherever it appears, and not only where the trigger fired.** The trigger decides
where a clause is REQUIRED; the marker decides where its halves are GRADED. Otherwise a voluntary
clause with a broken by-value half passes silently, which is the same could-not-fail shape one level
down, and `tFixture-213` is the arm for it.

**TWO escape spellings, one per graded question, and that is not a widening of F4's ruling.** F4
ruled ONE escape and no second marker, and what it was protecting is that a red names its own remedy
uniquely: with two spellings for one question an author cannot tell which is wanted, and a false
pass becomes silent. That invariant is intact, because the questions are different.
`NO VALUE READERS` answers "are there any by-value readers", asked of the by-value half.
`READER NOT IN TREE` answers "why does this name not resolve", asked of the by-name half, which F4
never reached because rev-2 did not grade that half at all. One question, one escape; two questions,
two escapes. The two spellings share no substring, so neither can satisfy the other's test.

Three further properties keep the second escape from becoming a hole:

- **The by-name half may legitimately carry NO names, and that passes by vacuity** — the rule is a
  universal over the names it lists, and a freshly private helper has no by-name reader. So no third
  escape is needed for emptiness, and F4's refusal of one stands exactly as written.
- **The escape is per HALF, and every name it covers is PRINTED.** One escape legalising an
  unbounded list of unresolved names would be a silent skip; the arm therefore names each one it
  accepted under the escape, on the non-gating channel, which is the rule the charter states for
  every skip.
- **A false red names its own remedy.** When the predicate reds a name that IS a real reader —
  because the reader is being deleted in the same commit, because it lives in an adopter's tree
  rather than this one, or because the name is a prose composition rather than a tree token — the
  message prints the unresolved token AND the spelling `READER NOT IN TREE`, so the fix is one edit
  and needs no reading of the gate.

**The resolution predicate's false-red rate is measured, not hoped.** OWN-PROBE at `67bec01a` over
the tokens a by-name half draws from: every identifier-shaped token in the live specs' §2 items under
the shipped shapes, markdown paths included, 626 occurrences and 419 distinct. 62 of the distinct
carry a `:<line>` tail, the form the corpus pass cites readers in. Resolved as written, 64 fail, and
44 of those are tail-bearing, so a join without S5's normalisation would red most cited readers.
With it, 19 fail, which is 4.5%, the rate rev-4 measured over the narrower shapes:

- eight are names their builds had not yet written or members spelled as prose compositions —
  `optIn`, `roster_refusal`, `union.SETS`, `union.snippet_bytes`, `READER_INVENTORY_CUTOFF`,
  rev-2's invented key, the two labels `F:IN-FLIGHT.md` and `F:MEMORY.md`, and a report path
  written relative to its build folder;
- two are the fixture names this unit mints, and four are files already retired, which fail because
  they are retired NAMES rather than readers;
- one is `reuse-discovery.js`, a file in another repo, and one is a shell assignment with no space;
- three are `path::symbol` node ids, and they are the one shape that IS a false red: the reader
  exists and the fixed string does not. The remedy is to write the path and the symbol as two
  tokens, never the escape.

A predicate whose false-red rate is under 5% and whose remedy is one edit is wireable; the
measurement is the argument.

**The resolution corpus is the tracked tree OUTSIDE `memory/builds/*/spec/`**, because a reader is
code, a test, a conf or a doc, and a name that appears only in other specs' prose has not been shown
to exist. One measured trap, stated because it would make the arm could-not-fail if missed: the
pathspec that performs that exclusion must be VERIFIED at build time against
`git ls-files 'memory/builds/*/spec/*'`. Running the batch by hand,
`git grep -l -F -f <tokens> -- ':!memory/builds/*/spec/'` returned 2072 files against 1556 tracked
non-spec files, so the exclusion did NOT hold as written — and an exclusion that silently fails
makes every name resolve against the spec corpus that named it.

### SHAPE AND RESOLUTION, NEVER COMPLETENESS — the control, and why O4 does not close it

`TOOL-dLoggedFlight-22` at rev-3 is the document that defines this class. Its by-name inventory
missed `test_fresh_ac4_three_shapes`, `parse_floor_raise` and `test_record_placement_windows`, and it
blocked three consecutive spec audits. Both stages of the dry run implemented a reader predicate over
it independently and both PASSED it, and both also passed rev-4, the fix. The two implementations
disagreed on the count — stage 1 counted reader-naming sentences per retirement clause as
15, 4, 6, 14, 14, 1 and 7 against rev-4's 18, 5, 7, 15, 15, 2 and 9, while the skeptic counted 10
whole-spec against 12 — and the figure to carry forward is the VERDICT, not either count, because
three faithful readings of one paragraph produced 1, 2 and 3 hits. The skeptic also ran a per-item
quantifier over the control: rev-3, the defect, reds 4 items and rev-4, the fix, reds 3. Tightening
the quantifier reds the remedy.

**O4 does not change that verdict, and this is the load-bearing sentence of the section.** The
control's defect is three readers it never listed. Resolution grades the names PRESENT; every name
the control DID list resolves. So the control still passes check 25 with O4 in force, and a reader
who takes "the by-name half is graded for content" to mean "the inventory is checked" has been
misled. Hence the catalog entry states which half is graded HOW, in those words: presence on one
half, resolution on the other, completeness on neither. This is the house idiom rather than a
concession — check 12's witness arm grades that a bullet names something backticked and never that
the named thing exists, and check 22 grades the verdict token and never the judgement behind it.

### Where the arm lives — the seam, and the guard that changed shape

**rev-1 said the arm rides an item accumulator at `tools/memory-tree/check-memory-hygiene.sh:1316`.
THAT IS WRONG, and it was the load-bearing claim rather than a citation slip.** Re-derived from
source and re-verified at rev-3: `:1316` is `if (jcut != "" && fdate != "" && fdate >= jcut) {`, the
`SCOPE_JOIN_CUTOFF` date guard itself. The accumulator — `sj_hasS` / `sj_hasA` at `:1317`-`:1321`
and `sj_in` / `sj_ni` / `sj_txt` / `sj_lbl` at `:1323`-`:1335` — is built INSIDE that guard and
inside a second test, `if (sj_hasS && sj_hasA)` at `:1322`, which demands the spec carry BOTH a
`## N. Scope (IN)` and a `## N. Acceptance criteria` heading. And it is the ONLY such walker in the
file: `grep -n 'Scope' tools/memory-tree/check-memory-hygiene.sh` returns three lines, one canon
literal at `:1134` and the two regexes of this one accumulator.

**The design is therefore the HOIST, S11.** The accumulator moves out of both enclosing conditions
to the awk's per-file level, and each consumer applies its own guard to the shared items:

```awk
if ((jcut != "" && fdate != "" && fdate >= jcut) || rilive) {
  sj_hasS = 0; sj_hasA = 0; ...the heading scan, unchanged...
  if (sj_hasS) { ...accumulate sj_txt / sj_lbl, unchanged... }
  if (jcut != "" && fdate >= jcut && sj_hasS && sj_hasA) { ...check 12 verdict, unchanged... }
  if (rilive && sj_hasS)                                 { ...check 25 verdict... }
  ...delete, after the LAST consumer...
}
```

`rilive` is one boolean, computed beside the two the file already computes at `:1250`-`:1251`:
`hdr !~ /^\*\*Status:\*\* (CLOSED|WONTDO)/`. Three properties, each checkable rather than asserted.
Check 12's verdict keeps its identical composite condition, so no check-12 verdict moves and
`tFixture-115` — "no Acceptance heading, so not graded at all", at
`tools/memory-tree/check-memory-hygiene.test.sh:1050` — stays a `miss`; AC15 observes that. Check 25
does NOT inherit `sj_hasA`, because whether a spec has an acceptance section has nothing to do with
whether it inventoried a retirement's readers; AC14 observes that.

And the accumulation guard is a UNION of the two consumers' own populations rather than a bare
non-empty test, which at rev-2 kept the population at 88 and at rev-3 keeps it at **120**: the 89
specs at/after `SCOPE_JOIN_CUTOFF` plus the 37 live ones, overlapping by 6. That is 1.35x check 12's
current inner pass and 18.75% of the selection, where a form without the per-consumer disjuncts
would have walked all 640. The hoist therefore still pays, and the figure moved because the second
consumer's population is liveness-shaped rather than empty.

**The extensibility of that union is a GATE, not a thing to remember.** A third consumer that
forgets to add its disjunct gets a live-looking arm and a dead one — so the rule is that every
consumer ships a fixture arming ONLY its own population, and a consumer missing from the union reds
that fixture. AC13's second run is that fixture for check 25: with `SCOPE_JOIN_CUTOFF` blank and
`SPEC_FORMAT_CUTOFF` armed, `tFixture-200` must still be NAMED.

The arm emits its findings with the control-character tag `\004`, and the shell greps that tag out
of `bad12_raw` and fails it under its own number. That tag-out-of-`bad12_raw` seam already exists
twice, at `tools/memory-tree/check-memory-hygiene.sh:1749`-`:1750` for the `\002` base-sha sentinel
and at `:1769`-`:1770` for the `\003` edge records. What is new is a tag feeding a different check
NUMBER rather than another `fail 12`, and a tag whose post-pass does WORK rather than only routing:
the resolution join of S5 is the same batched shape the base-sha sentinel uses at `:1385`-`:1389`,
where the arm resolves nothing itself and the post-pass batches every sha through one
`git cat-file --batch-check`.

**The cost of that post-pass is measured, and one shape of it is a trap.** OWN-PROBE on node `d`,
2026-09-21, over a 498-token batch: one `git grep -l -F -f` costs **0.602 s**, while the same batch
with git printing matching LINES costs **138.4 s** for 60688 lines, and a per-token `git grep -q`
loop costs 0.047 s each, so 23 s for the same batch. The `memory hygiene` leg's last recorded run on
this node is 33.3 s, read from `<git-dir>/gate-ledger.tsv`, so the line-printing form would
QUADRUPLE a leg that runs on every bar while its declared ceiling of 12720 s — read from
`tools/gate-legs.json` — would not notice. The specified shape is therefore the `-l` narrow plus an
awk attribution pass over the named files. The ceiling is not what protects the bar here; the
measurement is.

The one price that remains is a DECLARED dependency. Check 12's whole block opens on
`if [ -n "$SPEC_FORMAT_CUTOFF" ]` at `tools/memory-tree/check-memory-hygiene.sh:1132`, and its
selection filters by that same key at `:1164`, so a blank `SPEC_FORMAT_CUTOFF` disarms check 25
whatever its own liveness test says. That is one key and not three, and it is one key BECAUSE of the
hoist. It is the exact shape `.memory-tree.conf:198` already declares for `LEDGER_LABEL_CUTOFF` and
`LEDGER_TOKEN_CUTOFF` as branches of check 23, and the same remedy applies: the dependency is
written where an adopter reads it and then OBSERVED by a fixture run rather than asserted. AC13 is
that observation.

### Alternatives rejected

- **Nest the arm inside the accumulator where it already is.** The cheapest diff, and the one rev-1
  described without noticing. Rejected on the engine's own recorded ruling at
  `tools/memory-tree/check-memory-hygiene.sh:1304`: the arm's real population would be the
  intersection of its liveness test, `SCOPE_JOIN_CUTOFF` and an Acceptance heading, while it still
  read as live. That is the defect this unit is being built to make askable, so building it into the
  unit's own arm is not a trade, it is the thing itself.
- **Its own selection and its own §2 walk.** This would free check 25 from `SPEC_FORMAT_CUTOFF`
  entirely. Rejected: a second item accumulator in awk is a second spelling of the same rule, and
  this tree has paid for a second spelling once already — check 24's shell re-spelling of the row
  grammar passed a bold-wrapped id silently, across fifteen rows of the decision index, which is why
  that check is delegated to `row_grammar.py` today.
- **Grade the by-name half in `tools/check-spec-tokens.py` instead.** It already resolves backticked
  tokens against `git ls-files`, already owns a waiver registry at
  `memory/project/spec-token-waivers.txt`, and already refuses a stale waiver — a real candidate, and
  the one O4's half most resembles. Rejected because the POPULATION is the trigger: that checker
  would have to re-spell the verb list, the five shapes, the three exclusions and the kind-noun set to
  know which items own a clause, which is the second-spelling cost one paragraph up, paid across two
  languages. The waiver registry was the attractive half; rev-3's F8 offered it for the residual
  red, and the owner ruled the corpus pass instead, so the clause stays in the spec, beside the
  retirement, where the author is.
- **A conf-declared kind-noun set.** Rejected above: two carriers for one predicate, plus the
  empty-declaration refusal machinery, bought for a shape that fires on nothing.
- **A per-run report line instead of a zero-population notice.** `tools/check-spec-tokens.py` prints
  its graded count on every run and unit 2's S5 copies that, which is the stronger shape for a
  population that MOVES with liveness. Rejected here on the engine's own contract — its header at
  `tools/memory-tree/check-memory-hygiene.sh:18` states "Exit 0 + no output = clean. Anything printed
  is a hygiene regression" — and the five sibling notices at `:1830`-`:1867` are the sanctioned
  exception, on the non-gating channel described at `:1873`. A sixth notice of the same shape costs
  nothing to read; a routine report line would renegotiate that contract for every reader of the
  gate.
- **A branch of check 12 rather than a new number.** Rejected on the ruling in
  `tools/memory-tree/check-memory-hygiene.sh:896`, written when check 22 took its own number: hanging
  a semantic-sounding assertion off a structural section-walk check makes the structural check read
  as a semantic one to everybody who did not write it. The honest home costs an entry in the hygiene
  doc, and the leg name carries no count so `tools/gate-legs.json` does not move.
- **Raising `ARMS_FLOORS`.** Not required, and the dry run was wrong to say it was.
  `tools/memory-tree/check-arms.py:290` compares `got < want` per gate, so both floors are one-sided
  upward. The pinned pair for this gate is `tools/memory-tree/check-memory-hygiene.sh:27:27` at
  `.memory-tree.conf:478`, while the gate carries 31 call sites matching the gate's own
  `fail (\d+) "` extractor today, so a 32nd branch clears the floor untouched. What IS owed is the
  ARM: a positive assertion naming a literal slice of the new branch's failure text, or a row in
  `memory/project/unarmed-branches.txt` carrying the reason it cannot be armed. This unit arms it.

### The corpus pass, and what this unit verifies

The owner's ruling of 2026-09-21 on the residual red is "fix it now", and `TOOL-dGatedProse-5`
implements it at order 1: every item this trigger fires on, on every node, gains its clause before
check 25 exists. A clause written before its checker is additive prose that grades nothing, so that
pass cannot red a bar, and this arm lands at order 2 onto a corpus its own predicate already passes.
Unit 5's census is the item-by-item record, re-derived at its own pass; this spec carries the rule
and the population figure.

What stays here is the delta. The population moves with liveness and with every commit that writes a
§2 item, and one item already moved between rev-3's figure and the commit that published it. So this
unit's build pass runs the arm over the tree it lands on, and every item it names gains a clause in
this unit's commit, in unit 5's clause forms and under unit 5's collision protocol: the item label is
the anchor, a terminal spec is never edited, and a clause another session wrote first is reconciled
additively. Writing into another node's live spec is authorised by the owner's ruling, for unit 5's
pass and for this delta alike. The rev rule is unit 5's as well, settled on its F1 on 2026-09-21: a
clause moves the edited spec's rev, with its §9 line, only where `REV_SCOPE_CUTOFF` binds by
filename date, and which specs those are is derived at the pass from that key's value, never read
from a list here.

### The codebase map — what this unit owes it, and why that is not silence

This unit claims NO new inventory key, and the reason is derivable rather than a preference. The
map's inventories are ten, enumerated at rev-2 by importing `map_extractors.all_inventories()`:
`backlog-shards`, `gate-legs`, `git-hooks`, `gotcha-classes`, `guides`, `kits`, `lexicon-verbs`,
`rendered-skills`, `skill-engines` and `workflow-scripts`. **There is no file-path inventory at
all**, so editing a shell file mints nothing; and a new check NUMBER inside an existing leg is a
member of none of the ten, because `gate-legs` keys on the leg name and this unit adds no leg —
`memory hygiene` is the leg, its name carries no count, and `tools/gate-legs.json` does not move.

What this unit DOES owe is the prose refresh on touch, which is a Definition-of-Done item and not a
claim edit. Both engine files this unit edits are already inside
`memory/map/features/memory-tree-hygiene.md`'s `[paths].globs` at
`memory/map/features/memory-tree-hygiene.md:25`-`:29`, so coverage is satisfied by construction and
the generated artifacts do not move. The dossier's own prose does: its H1 reads "the 21-check gate"
against a body at `memory/map/features/memory-tree-hygiene.md:34` that says 22 checks, and this unit
adds a 25th. The refresh REMOVES the count from the H1 rather than bumping it, per the charter's own
rule that no count of a derived population is written in prose — a bumped count is the same defect
one commit later. `TOOL-dGatedProse-3` also edits that file, at `:51`, and the two edits are disjoint
lines in one file rather than a contested region.

### Inventory

| identifier | where it is graded |
|---|---|
| check number `25` | `memory/HYGIENE.md`'s catalog and the `fail 25` branch |
| `NO VALUE READERS` | the arm's by-value half, and `tFixture-202` |
| `READER NOT IN TREE` | the arm's by-name resolution half, and `tFixture-209` |
| `**Readers:**`, `by name:`, `by value:` | the arm's three marker tests |
| the six kind nouns | the arm's own literal, and `tFixture-207` |
| `tFixture-200` … `tFixture-215` | the fixture block's own `hit` and `miss` rows |
| `\004` | the tag split, beside the `\002` and `\003` splits it copies |

Check numbers 1 through 24 are all claimed: 1 to 12 plus 21, 22 and 23 carry `fail <n>` call sites in
the engine, and `memory/HYGIENE.md`'s catalog numbers 1 to 22 and 24. 25 is the next free integer.
This repo declares no naming cell for a shell variable, so no lexicon cell grades the arm's own
awk-local names. NO new `*_CUTOFF` preset is added, which is the whole of rev-3's change to this
table: the example-conf parity loop derives its population from the engine's bare presets, and this
unit leaves that population untouched.

### Migration

None of the mechanical kind: nothing is renamed, no key is added, no adopter conf changes. The
migration is the corpus pass, a different animal from a schema change, and it is
`TOOL-dGatedProse-5`'s, landed at order 1 before this arm exists; this unit's S14 verifies it.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | the S11 hoist, the arm with the verb list and the kind-noun literal, the `\004` split, the batched resolution post-pass, `fail 25` and the zero-population notice — about 110 lines |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the sixteen-fixture block, its `hit` and `miss` rows, the positive arm, the dependency arms, the S11 regression arm, the RAISED `FLOOR_ASSERTIONS` — about 180 lines |
| `tools/memory-tree/HYGIENE.template.md` | check 25's catalog entry — about 26 lines |
| `memory/HYGIENE.md` | REGENERATED, never hand-edited |
| `tools/memory-tree/README.md` | the check-count sentence, 23 to 25 with 24 enumerated — 1 line |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S13's author-facing line in the `## 2. Scope (IN)` skeleton |
| `memory/TEMPLATE-SPEC.md` · `memory/guides/ANNOTATION-STYLE.md` · `memory/guides/BUILD-METHOD.md` | REGENERATED by the parity script, never hand-edited |
| `memory/map/features/memory-tree-hygiene.md` | the H1's derived count removed, and the body count with it — 2 lines, no claim edit |
| any live spec S14's pass finds unclaused | one additive clause per item that entered the population after unit 5's pass — none expected |

Two groups of rows are shorter than at rev-2, each for one reason. `.memory-tree.conf` and
`tools/memory-tree/.memory-tree.conf.example` leave this list entirely, because O2 deletes the key
they would have declared. The four `*.template.md` line-1 markers leave it because the re-stamp is
unit 3's. The renders are still regenerated here, because this unit edits two of the four templates
and the render loop is all-or-nothing over the `PAIRS` table at
`tools/memory-tree/kit-dogfood-parity.test.sh:58`. At rev-4 the node-`d` spec row gives way to the
delta row above, because the corpus pass is unit 5's.

## 5. Production-readiness checklist

- security — N/A for the marker tests, which are literal substring matches over tracked markdown
  already in the graded selection. ONE new surface is real and is bounded by construction: the
  resolution join passes by-name tokens to `git grep -F -f` from a FILE, never on a command line and
  never as a regex, so a token carrying shell metacharacters or a leading dash is data. The token
  file is written from the arm's own output under the run's scratch directory and is read once.
- perf / scale — three populations, and they are different numbers. The VERDICT population is the
  live specs of the selection, 37 today, so the marginal verdict work is a pass over those. The
  ACCUMULATOR population is the union of check 12's 89 and that 37, which is 120 — up from 88 at
  rev-2 and still 18.75% of the 640 a disjunct-free hoist would have walked. The RESOLUTION
  population is the by-name tokens of triggered items, 0 at the pinned base and after unit 5's pass
  whatever its thirty-eight clauses list, at a measured 0.602 s for one batched `-l` grep of 498
  tokens against 138.4 s for the line-printing form and 0.047 s per token for a loop. The leg's last
  recorded run is 33.3 s and its declared ceiling is 12720 s, which is why the ceiling is not the
  protection and the shape is.
- error / empty / loading states — a zero LIVE population prints the notice of S7 and exits 0. A
  blank `SPEC_FORMAT_CUTOFF` disarms the check, declared in two carriers and observed by AC13. A
  resolution batch with no tokens runs no grep at all rather than one with an empty pattern file,
  which `git grep -f` treats as matching nothing and would report every name unresolved.
- observability — the failure message names the file, the item label, the missing half or the
  unresolved name, and the escape spelling that answers it, so a red row is actionable without
  reading the gate. Every name accepted under the by-name escape is printed. The zero-population
  notice names the liveness test.
- risks — five. First, precision is just under a half to just under six in ten by §4's reading, so
  an author will often write a clause on an item that retires nothing; the cost is one line, and
  sixteen of the 38 live items are exactly that case. Second, the trigger leaves two classes
  unreached: the NAMED GAP, 4 live items and 67 over the selection, none of which shape 6 reaches,
  and the token-less class beside it, 8 live and 59 over the selection, which holds one withdrawal
  with a by-value reader; S8 names both in check 25's header, and neither is closed. Third, the corpus is claused by unit 5 before this arm lands, so
  what reaches this unit is the delta since that pass, which S14 owes and AC21 observes. Fourth, the
  declared dependency on `SPEC_FORMAT_CUTOFF` means an adopter can get nothing from this arm without
  a key it does not own. Fifth, S11 edits a LIVE arm
  of check 12 rather than only adding beside it; the hoist is behaviour-preserving by construction,
  and AC15 is the check that exercises that claim over the seven existing scope-join fixtures.
- testing — the failing case is staged and observed RED before the branch lands, per the charter. The
  sixteen-fixture block carries nine RED fixtures and seven GREEN ones. Three of the GREEN ones
  exist only to pin false-positive classes, so that a later widening of the identifier test reds
  rather than passing quietly, and two of the RED ones exist only to pin the owner's two widenings,
  so that a later narrowing reds too.
- migration — none of the mechanical kind, per §4; the corpus pass is unit 5's and S14 verifies it.
- user docs — N/A. Nothing here is user-facing; `memory/HYGIENE.md` is the governance carrier and S8
  updates it.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the fixture tree, it
  exits 1 and names `tFixture-200` together with the item label `S1` and the escape spelling that
  answers it, for a LIVE-status item whose text carries a retirement verb and a backticked underscore
  identifier and no `**Readers:**` clause.
  Red when: the fixture carries no clause and the arm stays silent, which is the state observed and
  recorded before the branch lands.
  fixture: the tree is built by the gate's sibling fixture suite, named in §7 under `New arm:`; no
  such fixture exists today.
- **AC2** — When that same item gains a `**Readers:**` clause carrying `by name:` with two tokens
  that resolve — a path the fixture tree tracks, written with a `:<line>` tail, and a symbol written
  with a trailing `()` — and then `by value:` with a backticked token, the run is silent for
  `tFixture-201`.
  Red when: the arm reds a conforming clause, which would make the remedy unreachable; or it reds
  either written form, which is the join taking a citation tail or a call suffix for part of the
  name — measured at `67bec01a`, that reading fails 44 of the 62 distinct tail-bearing tokens in
  live §2 items.
- **AC3** — When the by-value half reads `NO VALUE READERS` followed by a reason the run is silent
  for `tFixture-202`; when `tFixture-203` writes a `by value:` half holding neither a backticked
  token nor the escape — the bare escape with no reason after it is that case — the run names it.
  Red when: an unanswered by-value half passes, which turns an evidence field into a checkbox, or
  the reasoned escape reds, which leaves a genuine no-value retirement with no legal answer.
- **AC4** — When `tFixture-208`'s `by name:` half lists a backticked token that appears nowhere in
  the tracked tree outside `memory/builds/*/spec/`, the run names the fixture, prints that token and
  prints the spelling `READER NOT IN TREE`.
  Red when: an unresolvable name passes, which is the half O4 exists to grade; or the message omits
  the escape spelling, which leaves a false red with no remedy but reading the gate.
  figure: the resolution corpus is DERIVED at observation time by `git ls-files` minus the spec
  glob, never pinned. Measured base rate over live specs' §2 identifier tokens at `67bec01a`, under
  the shipped shapes and after S5's normalisation: 19 of 419 distinct unresolved.
- **AC5** — When `tFixture-209` carries that same unresolvable name plus `READER NOT IN TREE` and a
  reason, the run is silent for it AND stdout carries a line naming the covered name.
  Red when: the escape silences the arm without naming what it covered, which is a skip that looks
  like a pass — one escape could then hide any number of unresolved names.
- **AC6** — When `tFixture-206` carries `**Readers:**` and `by name:` and no `by value:` marker at
  all, the run names it and the message says which half is missing.
  Red when: a clause with only its by-name half passes, which is the whole defect — by-value is the
  half the three audits had to ask by hand.
- **AC7** — When a triggered-looking item's only backticked tokens are the bare words `phase` and
  `commit`, and the item carries no kind noun, the run is silent for `tFixture-204`.
  Red when: the identifier test admits a bare word unconditionally, which is the class the skeptic
  measured at 42 collected names over the control spec.
- **AC8** — When a triggered-looking item's only backticked tokens are `TOOL-dLoggedFlight-21` and
  `-24`, the run is silent for `tFixture-205`.
  Red when: the identifier test reads a dashes-and-digits token as a long option, or a
  family-slug-seq id as a name.
  figure: DERIVED at observation time from the fixture. The measured incidence of such a token
  inside a live verb-bearing item is 0, so the corpus cannot witness this and the fixture is its
  whole coverage.
- **AC9** — When a triggered-looking item's only backticked token carries a space — the fixture uses
  a shell fragment of the `body=$(_unfenced "$f")` shape — the run is silent for `tFixture-211`.
  Red when: a backticked code fragment is read as a retired name, which measured at `67bec01a`
  would charge one live item a clause, `aBatchedLintel-1` S3, and seven over the selection.
- **AC10** — When `tFixture-212` carries two LIVE §2 items, each opening with an imperative
  retirement stem and neither carrying a `**Readers:**` clause — S1, whose only backticked token is
  a path with a slash that ends in `.md`, and S2, whose only backticked token is a markdown filename
  with no slash, written with a `:<line>` citation tail — the run names `tFixture-212` with BOTH
  labels. The fixture's two tokens are named in the suite and not here, because a path-shaped token
  inside a criterion is graded against the tracked tree by `tools/check-spec-tokens.py`.
  Red when: S1 is absent, which is the slash shape still refusing a path that ends in `.md`, the
  exclusion the owner's O6 ruling deleted and the reading that kept `aMendedLedger-1` S2, one of the
  rule's motivating cases, out of the population; or S2 alone is absent, which is either the dot
  shape still refusing an `md` tail, the exclusion's second spelling, or the dot shape reading the
  token before its tail is stripped, so that a cited document with no slash reads as a bare word.
  figure: DERIVED at observation time from the fixture. The corpus witnesses the ruling too, O6
  alone moving the live population from 23 to 27 items at `67bec01a`, but the fixture is what
  binds.
- **AC11** — When `tFixture-207` carries a retirement verb, a backticked bare word and a declared
  kind noun and no clause, the run NAMES it; and a grep for each of the six noun phrases over
  `tools/memory-tree/check-memory-hygiene.sh` returns one line each, all six adjacent and
  immediately beside the verb list, while the same grep over `.memory-tree.conf` and
  `tools/memory-tree/.memory-tree.conf.example` returns nothing.
  Red when: the shape does not fire, which leaves the owner's O3 closure unbuilt; or the noun set
  exists in two carriers, which is the disagreement the single literal exists to prevent.
  figure: the set fires on 0 items of the live corpus and 0 of the 641-spec selection at
  `67bec01a` under the shipped list, DERIVED, so the fixture is its whole coverage and the corpus
  cannot witness it.
- **AC12** — When `tFixture-210` carries the identical defect as `tFixture-200` under a `CLOSED`
  status header, the run is silent for it while still naming `tFixture-200` in the same run.
  Red when: the arm grades a terminal spec, which would demand rewriting a frozen record to clear a
  hit — the reason `tools/memory-tree/check-memory-hygiene.sh:1385` states for its own arm.
- **AC13** — two runs over the same fixture tree, which together pin the dependency set at exactly
  one inherited key. With `SPEC_FORMAT_CUTOFF` blank, `tFixture-200` is ABSENT. With
  `SPEC_FORMAT_CUTOFF` armed and `SCOPE_JOIN_CUTOFF` BLANK, it is NAMED.
  Red when: the first names it, which would mean the declared dependency is not what the carriers
  say; or the second does NOT name it, which means the arm inherited `SCOPE_JOIN_CUTOFF` after all —
  the dead-invisibly state S11 exists to prevent, and the arm that proves this consumer is in the
  union guard.
- **AC14** — When the gate runs over a fixture carrying a `## 2. Scope (IN)` heading and NO
  acceptance heading, with a triggering item that has no `**Readers:**` clause, the run NAMES it
  under check 25 while check 12's scope-join arm stays silent for the same file.
  Red when: check 25 goes silent on it, which means the arm inherited the both-headings test it has
  no business inheriting.
- **AC15** — When the fixture suite runs after the S11 hoist, all seven existing scope-join rows at
  `tools/memory-tree/check-memory-hygiene.test.sh:1045`-`:1051` keep their pre-hoist verdicts:
  `tFixture-110` and `tFixture-114` hit, and `tFixture-111`, `tFixture-112`, `tFixture-113`,
  `tFixture-115` and `tFixture-116` miss. The named-cutoff assertion at `:1068` still matches, and
  the blank-`SCOPE_JOIN_CUTOFF` run at `:1355` is still silent for `scope items naming neither`.
  Red when: `tFixture-115` becomes a hit, which is the one verdict the hoist could move — it carries
  no Acceptance heading, so a hoist that drops `sj_hasA` from check 12's own condition instead of
  only from the accumulator's grades a spec that is legal under the format.
- **AC16** — When the gate runs against a fixture tree whose every spec carries a terminal status,
  stdout carries a notice saying the reader-inventory arm graded no spec and naming the
  `CLOSED|WONTDO` liveness test it applied, and the run exits 0.
  Red when: the arm grades nothing and says nothing, which is byte-identical to an arm that graded a
  corpus and found it clean — and under a liveness-shaped population that state arrives by specs
  closing rather than by configuration, so nobody is watching for it.
- **AC17** — When `python tools/memory-tree/check-arms.py --report` runs, the new branch of
  `tools/memory-tree/check-memory-hygiene.sh` is listed as ARMED, and no row naming it appears in
  `memory/project/unarmed-branches.txt`.
  Red when: the positive assertion quotes a slice of the message that the branch does not emit, in
  which case the branch reports unarmed and must be pinned with a reason instead.
- **AC18** — When `grep -n 'Readers' memory/HYGIENE.md` runs it returns at least one line inside an
  entry numbered 25; that entry contains the words "presence", "resolution" and "completeness" in
  the sentences stating what each half is graded by, names the control `TOOL-dLoggedFlight-22`,
  states the kind-noun COUNT without listing the nouns, carries the words "on trust" in a sentence
  about the escapes, "case" and "past tense" in the sentence about the verb match, ".md" in a
  sentence stating that a markdown path counts as an identifier, and "identifier shape" and "no
  backticked token" in the sentence or sentences naming the two classes of item the trigger does
  not reach, with no size printed for either, and
  `tools/memory-tree/README.md` line 18's check sentence names 25 and enumerates 24 beside 20 under
  `row_grammar.py`.
  Red when: the entry lands without the per-half grading sentence, which is how a reader concludes
  the inventory is checked; or without the trust sentence, which is how a false escape reads as a
  verified one; or it restates the noun set, which is the second copy S3 exists to
  prevent; or it names neither the past tense nor the markdown path, which is how an author reads
  the trigger narrower than the arm and leaves a required clause unwritten; or it names one
  unreached class and is silent on the other, which is how a reader takes the silent class for
  graded — at `67bec01a` a header naming only the named gap would be silent on 8 live items against
  the 4 it names; or it prints a size for either class, which is a count of a live population in a
  shipped doc; or the README keeps a
  count its own enumeration contradicts, which it does today at 23 against 24 checks.
  fixture: `memory/HYGIENE.md` is a render of `tools/memory-tree/HYGIENE.template.md`, so the
  observation is made after the re-render and the template carries the authored text.
- **AC19** — When `grep -n '^FLOOR_ASSERTIONS=' tools/memory-tree/check-memory-hygiene.test.sh` runs,
  the value it prints MINUS the value at this unit's base equals the number of assertion calls this
  unit's fixture block adds, derived by counting `hit`, `miss`, `hitl`, `chit` and `cnot` calls
  inside the block's own line range; and the comment above that constant names `TOOL-dGatedProse-1`
  as the unit that raised it and by how much. Observed statically, by grep and arithmetic, so it
  needs no suite run.
  Red when: the floor is left at the value this unit inherited, which the suite's own `-ge`
  comparison at `tools/memory-tree/check-memory-hygiene.test.sh:2461` passes silently — so a floor
  that no longer equals the printed count is a pin that has stopped pinning, against the convention
  its own comment states at `:2459`: "The pinned number is now the printed number, exactly." Red
  also when the delta and the block's own call count disagree, which is a raise guessed rather than
  counted.
  figure: both terms are DERIVED at observation time. The value raised FROM is whatever this unit
  inherits, which is 374 at the pinned base and is read rather than assumed.
- **AC20** — When `grep -c 'Readers:' tools/memory-tree/SPEC-TEMPLATE.template.md` returns at least
  1, that line sits inside the file's `## 2. Scope (IN)` skeleton section, and
  `grep -c 'Readers:' memory/TEMPLATE-SPEC.md` returns the SAME count — the render carrying it only
  because it was regenerated from the template.
  Red when: the count in the template is 0 while the render's is 1, which is the line written into
  the render instead: the next re-render deletes it without a trace and `kit/dogfood doc parity`
  reds in the meantime. A rule written into a render is a rule with a scheduled deletion date.
- **AC21** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over THIS repo after this
  unit's commit, it names ZERO item under check 25, in any spec on any node.
  Red when: an item is named, which means unit 5's pass missed one, or the population moved between
  that pass and this one and this unit's pass did not clause the delta — the case S14 exists for,
  since one item already moved between rev-3's figure and the commit that published it.
  figure: DERIVED at observation time. The 38 items across 20 specs at `67bec01a` are a measurement
  and are expected to move.
- **AC22** — When this unit's diff is read, it carries no change to `KIT_MEMORY_TREE_VERSION`, no
  edit to any `gov:kit memory-tree@` marker, and for each of the four rendered pairs `head -1` of the
  render byte-matches `head -1` of its template.
  Red when: a bump rides along here, which reds `verdict epoch` from unit 3's commit through the
  build's tip because the epoch rule is topological and unit 3's engine edit is the later one; or a
  render's line 1 diverges from its template's, which `kit/dogfood doc parity` reds and which is how
  a hand-stamped render gets silently reverted by the next re-render.
- **AC23** — When `tFixture-213` carries a `**Readers:**` clause on an item the trigger does NOT
  fire on, with a `by value:` half holding neither a backticked token nor the escape, the run names
  it.
  Red when: a voluntary clause's halves go ungraded, which is the same could-not-fail shape one
  level down — an author who copies the clause onto an untriggered item and breaks a half gets a
  green.
- **AC24** — When `tFixture-214` carries two LIVE §2 items and no `**Readers:**` clause — S1, whose
  only retirement verb is `DROPS`, with a backticked underscore identifier, and S2, which opens with
  `Retire` and whose only backticked token is a camel-case identifier — the run names `tFixture-214`
  with BOTH labels; and every line of `tools/memory-tree/check-memory-hygiene.sh` carrying
  `IGNORECASE` is a comment line.
  Red when: S1 is absent, which is the strict list matched case-sensitively — no stem reaches
  `DROPS`, because a stem needs a word boundary after it, so S1 isolates the strict list, and under
  that reading `dPolishedVitrine-1` S5 leaves the population silently; or S2 is absent, which is
  either a case-sensitive stem match, losing six live retirements that open with a capital, or a
  fold over the whole item, erasing shape 4; or `IGNORECASE` carries the fold, which mawk reads as an
  unset variable, so the arm is case-sensitive there and nothing says so.
  figure: DERIVED at observation time from the fixture. The corpus witnesses the ruling too, 38
  items case-insensitive against 29 exact at `67bec01a`, but the fixture is what binds.
- **AC25** — When `tFixture-215` carries six LIVE §2 items and no `**Readers:**` clause — S1 to S5
  each with a backticked underscore identifier and exactly one retirement verb, in turn `RETIRED`,
  `replaced`, `removed`, `deleted` and `dropped`, none of them inside a strict phrase; and S6 with a
  backticked underscore identifier, no retirement verb, and the backticked camel-case slug
  `dRetiredFork-9` — the run names `tFixture-215` with S1 through S5 and does not name S6.
  Red when: any of S1 to S5 is absent, which is the closed list without that past-tense form — the
  owner's O5 ruling unbuilt for it, and for S1 the ruling's own `RETIRED` example still matching in
  no case; or S6 is named, which is a past form matched as a bare substring, the reading that pulls
  two items of `DEPL-dRetiredFork-2` into the live population although neither retires anything.
  figure: DERIVED at observation time from the fixture. The corpus witnesses the ruling too, O5
  alone moving the live population from 23 to 31 items at `67bec01a`, but the fixture is what
  binds.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `build README slot contract`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · a fixture §2 item at a live status carrying a retirement verb and a backticked underscore identifier with no `**Readers:**` clause, staged and observed RED before the branch lands · none — both `ARMS_FLOORS` figures are one-sided and the pinned 27:27 sits below the 31 branches the gate carries today

**ONE of those legs is expected RED at this unit's commit, and it is not a defect this unit can
close.** `verdict epoch` reds because the build's single kit-version move is unit 3's and the epoch
rule is topological: at this commit the engine has moved and no commit in the range changes the
constant, which is exactly that checker's "behaviour-bearing line(s) of the engine moved … and NO
commit in the range changes KIT_MEMORY_TREE_VERSION" branch. It stays red through unit 2's commit at
order 3, whose `tools/check-spec-tokens.py` is outside that checker's scan set, and goes green at
order 4. `memory hygiene` is NOT expected red: unit 5 writes every clause at order 1, before check 25
exists, so a check-25 row at this commit names a delta S14 owes. It is stated here because the
owner's rule is that units run no gate legs and the bar runs once after every unit is built: a red
discovered there, unannounced, would read as this unit's failure.

`kit version markers` LEAVES this section, where rev-2 added it: with no bump and no re-stamp this
unit moves nothing that leg reads. `kit/dogfood doc parity` stays, because this unit edits two of the
four templates and lands through their renders.

**`memory-hygiene self-test` IS HELD BY DEFAULT, and this unit's entire S9 lives in it.** It is
subject `kit`, chunk `selftests`, guarded on `tools/lib/` and `tools/memory-tree/`, so a green bar
without `GATE_FULL=1 GATE_SELFTESTS=1` exercises none of the sixteen fixtures. That is why every
criterion above observes the engine, the checker or the grep DIRECTLY rather than naming the suite.
This unit's Definition of Done is kit work, so it owes the total run.

Two obligations sit outside this unit's own arms and are named so nobody discovers them at the bar.
The §3 reciprocity join is live on the full bar for a spec dated at or after the edges cutoff.
Units 2, 3 and 4 declare **consumes-from** this unit and unit 5 declares **hands-off** it, so all
four sibling bullets in §3 are load-bearing rather than courtesy — deleting one reds
`tools/memory-tree/check-memory-hygiene.sh:1800`'s half-declared-pair message on the sibling's file
rather than on this one. The order join holds for all four: unit 5 sits at order 1, before this
unit's order 2, and units 2, 3 and 4 sit at orders 3, 4 and 5, after it. And the four dogfood copies
are regenerated rather than hand-stamped, which is a command to run and not a diff to write: the
parity script's own render mode, whose spelling is in that script's usage header rather than copied
here, where it would read as an observation.

## 8. Open questions

- **F1 — the verb vocabulary's reach.** FACT-QUESTION · Does adding the four bare imperative stems to
  the dry run's strict list buy coverage the strict list does not have? The probe: run both
  vocabularies over the live corpus and compare the triggered item sets against the three items the
  dry run named as real, uninventoried retirements. The liveness assertion is that the probe can
  return a negative, and a sibling arm of the same probe did — the bare-word shape returned zero
  items under both vocabularies. RESOLVED (agent, 2026-09-20): the imperative stems are IN. The
  strict list reaches NONE of the three named items and the stems reach ALL THREE. Re-derived at
  rev-4 at `32f2eb71`, case-insensitive under the owner's ruling: 15 items strict, 25 with the stems,
  23 after rev-3's two shape exclusions — the stems still add 10 items and 5 specs. Matched
  case-sensitively the stems reach only one of the three, because two open with `Remove` and `Drop`.
- **F2 — the two false-positive classes the skeptic named.** FACT-QUESTION · Are they answerable by
  shape alone, and what does each exclusion cost? RESOLVED (agent, 2026-09-20): both are answered by
  shape. The row-layout class is excluded because a bare word is not one of the five identifier
  shapes, and the conditional sixth shape that admits one costs 0 items. The elided-slug class is
  excluded because a dashes-and-digits token is not a long option, at a cost of 0 changed verdicts in
  the live corpus and one in the control revision. Rev-3 adds two classes of its own, priced in §4:
  the space-bearing token, which changes two verdicts, and the `:<line>` tail, which changes none.
- **F3 — where the arm lives.** RE-RESOLVED at rev-2, because rev-1 resolved it against a seam that
  is not there: riding the accumulator AS IT STANDS takes three dependencies and not one, since the
  accumulator is built inside the `SCOPE_JOIN_CUTOFF` guard at
  `tools/memory-tree/check-memory-hygiene.sh:1316` and inside the both-headings test at `:1322`, and
  there is no second walker in the file. RESOLVED (agent, 2026-09-21): HOIST the accumulator, S11,
  and declare the one dependency that survives. The precedent for declaring it is
  `.memory-tree.conf:198`, where two keys are declared as branches of check 23 with the same
  disarming caveat. Re-derived again at rev-3 under the owner's O2 ruling, which changed the second
  disjunct of the union guard from a date test to a liveness test and its population from 88 to 120,
  and changed the answer not at all.
  The liveness assertion for this re-derivation is that it could have come back the other way, and
  the probe that settled it is a `grep -n 'Scope'` over the engine returning three lines: had it
  returned a second unguarded walker, rev-1's design would have stood as written.
- **F4 — the escape spellings.** RE-RESOLVED at rev-3, because the owner's O4 ruling grades a half
  F4 was written about not grading. RESOLVED (owner, 2026-09-21): ONE escape per GRADED QUESTION,
  which is two spellings for two questions and not two for one. `NO VALUE READERS` answers the
  by-value half's presence question; `READER NOT IN TREE` answers the by-name half's resolution
  question; an empty by-name half passes by vacuity and needs no third. The invariant F4 was
  protecting — a red names its own remedy uniquely, a false pass is never silent — is what §4
  re-derives the pair against, and the per-half escape is made non-silent by printing every name it
  covers.
- **F5 — should the by-NAME half be graded for content?** RESOLVED (owner, 2026-09-21): YES, by
  RESOLUTION and not by completeness. Each name the half lists must resolve in the tracked tree
  outside the spec corpus, with `READER NOT IN TREE` plus a reason as the escape. Measured before
  being built, and re-measured at rev-4 with paths included and S5's normalisation applied: 15 of
  336 distinct candidate tokens fail to resolve, 4.5%; at rev-5, under the widened shapes, 19 of 419,
  the same rate, each named by class in §4. What the ruling
  explicitly does NOT buy is the control revision: `TOOL-dLoggedFlight-22` rev-3 lists three
  readers fewer than it has and every name it does list resolves, so it still passes.
- **F6 — should the NAMED GAP be closed by declaring a kind-noun vocabulary?** RESOLVED (owner,
  2026-09-21): YES, prospectively. The six-phrase set of S3 fires on 0 live items and 0 of the 640
  selected specs, so it adds no corpus work today and closes the bare-word case by rule rather than
  by memory. Measured caution folded with it: a single-noun set containing `marker` fires on one
  innocent item of the selection, which is why the declared phrases are multi-word.
- **F7 — the phase-in question, as a PAIR across two units.** RESOLVED (owner, 2026-09-21): NEITHER
  new predicate takes a cutoff. This unit declares no `READER_INVENTORY_CUTOFF` and
  `TOOL-dGatedProse-2` declares no `SPEC_CLAIMS_CUTOFF`; both grade every live spec from the commit
  that lands them. The ruling was made with the consequence stated. The consequence is corpus work,
  which F8's ruling then placed in unit 5 at order 1, leaving this unit's S14 a verification.
- **F8 — the residual red on specs this unit does not own.** RESOLVED (owner, 2026-09-21): fix it
  now. `TOOL-dGatedProse-5` implements the ruling: it lands at order 1, writes a clause on every item
  this trigger fires on, on every node, and this unit moves to order 2 onto a corpus its predicate
  passes, so no bar is red on check 25 at any commit of the build. The other two options rev-3 stated
  — land red and carry it, or ship a drainable handoff registry — were not taken, and nothing here
  builds either.
- **F9 — OWNER'S, raised at rev-4. The case ruling folds CASE, not INFLECTION.** The ruling's own
  examples are `DROPS`, `RETIRED` and `REPLACED`. The first matches under the fold, and `REPLACED`
  matches inside `is REPLACED by`, but the closed list carried no past-tense form, so `RETIRED` on
  its own matched in no case — measured at `aMendedLedger-6-u6` S6, whose sentence says the sharded
  ledger "is RETIRED". RESOLVED (owner, 2026-09-21): ADD THE PAST TENSE. `retired`, `replaced`,
  `removed`, `deleted` and `dropped` join the list, folded like the rest; this spec matches each at
  a word boundary on both sides, like the stems, because as bare substrings they match inside the
  slug `dRetiredFork`. Measured at `67bec01a`, O5 alone adds 8 live items across 7 specs, 31 across
  17 in all, and read item by item in §4 they are three retirements, one value move and four false
  triggers. With O6, §4 derives the combined 38 across 20. AC25 and `tFixture-215` pin it.
- **F10 — OWNER'S, raised at rev-4. Does the `.md` exclusion stay?** Its rev-1 rationale did not
  survive re-derivation: the item it cited fires on a slug whatever the exclusion says, and the three
  stubs that item deletes are named paths with readers. RESOLVED (owner, 2026-09-21): DROP IT. The
  exclusion goes in both of its spellings, the global `.md` test and the dot shape's "other than
  `md`" clause, so a markdown path is an identifier with or without a slash. Measured at
  `67bec01a`, O6 alone moves the live population from 23 to 27 items across 15 specs; rev-4's 25
  lifted the first spelling only. Its four items are two retirements, `aMendedLedger-1` S2 — one of
  the rule's motivating cases — and `aMendedLedger-6-u6` S1, and two false triggers,
  `aMendedLedger-6-u6` S5 and `TOOL-dGatedProse-4` S3. With O5, §4 derives the combined 38 across
  20. AC10 and `tFixture-212` pin it.
  Which reading of the drop this text states is the fork `TOOL-dGatedProse-5`'s F7 put to it.
  RESOLVED (agent, 2026-09-21): reading B, both spellings, as rev-5 already wrote. The main loop
  settled it from the owner's own words rather than by a new choice: the ruling was to drop the
  exclusion, and the slash-only reading keeps half of it, so one markdown file would pass or fail by
  whether its author spelled a directory. Under reading B the population is 38 items across 20 specs
  at `67bec01a`; the slash-only reading would give 34 across 18.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, written against the dry-run journal for the `retirement-readers`
  strand and against this session's own probe over the 24 live specs.
- rev-2 · 2026-09-21 · the cross-read fold, and it MOVED THE DESIGN rather than the prose. The seam:
  rev-1's claim that `tools/memory-tree/check-memory-hygiene.sh:1316` holds a rideable §2 item
  accumulator is FALSE — re-derived, that line is the `SCOPE_JOIN_CUTOFF` guard and the accumulator
  sits inside it and inside a both-headings test, with no second walker in the file — so §4's "Where
  the arm lives" was rewritten, the trigger and dependency items re-stated, F3 re-resolved, and a new
  HOIST item added so the inherited dependency set is one key and not three. Also folded: the single
  kit-version move and its derived marker population, the assertion-floor raise, the codebase-map
  derivation, the author-facing template line, three rewritten edges, and OWN-PROBE marks with stated
  bands on every trigger, bare-word, gap and precision figure.
- rev-3 · 2026-09-21 · the owner's four rulings of 2026-09-21 and one correction from the main loop,
  each naming what it moved. **O2 — no cutoff.** The `READER_INVENTORY_CUTOFF` key is DELETED rather
  than argued with: gone from the scope items, from §4's Inventory, Migration and the deleted Rollout
  sub-head, from §5's perf and empty-state rows, from `.memory-tree.conf` and the conf example in
  Files touched, and from rev-2's AC6 and AC7, which graded nothing else and are deleted with it. In
  its place S1 declares the POPULATION as check 12's selection filtered by the engine's own liveness
  test at `tools/memory-tree/check-memory-hygiene.sh:1385`, with the `check-spec-tokens.py:87`
  divergence sized at nine `DEFERRED` specs; and S14 is the corpus work the ruling creates — the
  trigger fires on 22 items across 13 live specs, the five in two node-`d` specs are written by this
  unit, the seventeen in eleven node-`a`-and-`b` specs are enumerated and left alone, and F8 records
  that `memory hygiene` is red until their owners write them. F7 is RESOLVED by the ruling.
  **O3 — the named gap closes with a kind-noun vocabulary.** rev-2's "why shape 6 is not built"
  section is replaced by the shape, built conditional on one of six declared multi-word noun phrases,
  declared as ONE literal in the arm beside the verb list with the conf alternative rejected in §4
  and the noun count stated in the catalog entry rather than the nouns; `tFixture-207` and AC11 are
  new; measured at 0 hits over the live corpus and over all 640 selected specs, with the single-noun
  `marker` variant's one innocent hit recorded as the reason the phrases are multi-word. F6 is
  RESOLVED by the ruling. **O4 — the by-name half is graded for content.** S4 gains the resolution
  rule, S5 the batched `git grep -l -F -f` seam with its measured 0.602 s against the 138.4 s
  line-printing form and the pathspec trap that made the exclusion under-exclude; `tFixture-208` and
  `tFixture-209`, AC4 and AC5 are new; the catalog entry must now state which half is graded how
  (AC18); and the SHAPE-ONLY section is rewritten to show that the control still passes, because
  resolution grades the names present and the control's defect is the names absent. The one-string
  rule of F4 is RECONCILED rather than dropped: one escape per graded question,
  `READER NOT IN TREE` as the second spelling, an empty by-name half passing by vacuity so no third
  is needed, and every name the escape covers PRINTED. F5 is RESOLVED by the ruling.
  **R1-CORRECTED — the version move is not this unit's.** rev-2's S9 is DELETED: the constant, the
  derived marker re-stamp and the `kit version markers` leg all leave this spec, a §3 non-goal states
  the refusal and names unit 3 and the epoch rule, AC22 observes it, and Files touched loses five
  rows. Verified at source rather than taken on the correction's word:
  `tools/memory-tree/check-verdict-epoch.sh:16`-`:24` states the rule topologically and `:179`
  implements `git merge-base --is-ancestor "$W" "$S"`, so with both this unit and unit 3 moving the
  engine and unit 3 at order 3, a bump here leaves the last change descended from the bump. §7 now
  states that `verdict epoch` is expected RED at this commit and green at order 3.
  Also rev-3's own, from re-measurement rather than from a ruling: two new shape exclusions — a
  space-bearing token, which drops two innocent items O2 would otherwise have charged a clause each,
  and a stripped `:<line>` tail, a 0-verdict forward guard on the `check-spec-tokens.py:74`
  precedent — with `tFixture-211`, `tFixture-212`, AC9 and AC10; a clause is now graded wherever it
  appears rather than only where the trigger fires, with `tFixture-213` and AC23, which makes unit
  3's voluntary clause graded surface and is declared in that edge; the fixture block grows from eight to
  fourteen; the zero-population notice is re-keyed from a cutoff to the live count, with the five
  sibling notices counted correctly where rev-2 said three; the 1-to-3 edge's line-reflow claim is
  corrected, since with no preset added the `*_CUTOFF` cluster and the conf example do not move; and
  every population, precision, gap and cost figure is re-derived over the 640-spec selection and
  marked OWN-PROBE with its script named. Scope labels shifted with the deletions: rev-2's S2, S3,
  S4, S5, S6, S7, S8, S10, S11 and S12 are rev-3's S2, S4, S6, S7, S8, S9, S10, S11, S12 and S13.
  REFUSED: nothing.
- rev-4 · 2026-09-21 · the migration unit's arrival, the owner's case ruling, and the skeptic's
  findings against the migration spec where they land on this one. **ORDER.** This unit is order 2
  now, after `TOOL-dGatedProse-5` at order 1; the header token was set by the main loop and is left
  as set. Every sentence that placed this unit first is re-stated: the §3 kit-version non-goal and the
  unit-4 edge move to order 2 and unit 3's engine edit to order 4; §7's expected red is `verdict
  epoch` alone, red at orders 2 and 3 and green at 4. §3 gains the reciprocal **consumes-from**
  `TOOL-dGatedProse-5` bullet unit 5's own edge needs, and the **hands-off** external bullet on the
  seventeen node-`a`-and-`b` items is deleted. **F8** is RESOLVED by the owner's "fix it now", which
  unit 5 implements. **S14** becomes a verification plus the delta, AC21 is re-stated to zero items
  on every node, and §4's corpus-pass section, its two node tables and the bar-cannot-be-green
  paragraph are deleted in favour of unit 5's census; §4 Migration, Files touched and §5's risks,
  perf and migration rows follow. **CASE.** S2 states the owner's ruling that the whole verb list is
  matched case-insensitively, a new §4 section measures the three readings — 23, 22 and 17 items —
  and fixes the build (`tolower()` over a copy, never `IGNORECASE`) and the fold's three boundaries;
  AC24 and `tFixture-214` are new and red on any case-sensitive reading; S9 and §5 count fifteen
  fixtures, seven of them RED; F9 records that the fold reaches case and not inflection, so the
  ruling's own `RETIRED` example is outside the list. **POPULATION.** 22 items across 13 specs
  becomes 23 across 14, reconciled in a new §4 section: the difference is `TOOL-dGatedProse-3` S8,
  which `c7750bf8` made trigger on `is replaced by`, and the §3 unit-3 edge that called its clause
  optional is re-stated. Every trigger figure is re-derived at `32f2eb71` and F1 with it. **SKEPTIC
  FINDINGS on the migration spec, answered here where they touch this spec:** the case rule is
  declared (its conditional spurious item); S4 and §4 state that an escape is a claim about readers,
  so a value move answers with its value readers, which settles the `aGradedDoorway-7` S2 against
  `TOOL-dGatedProse-3` S8 pair and the `aMendedLedger-8-u9` S11 escape in one rule, and S8 and AC18
  carry it into the catalog entry; `aMendedLedger-1` S1 is re-read as a retirement, which deletes the
  `.md` exclusion's rationale, re-states that bullet as its measured two-item effect and opens F10;
  §4's precision section is re-derived as 13 retirements, 3 value moves and 7 false triggers, where
  rev-3's count disagreed with its own listing; a vacuous `READER NOT IN TREE` is stated as inert;
  and S5 normalises a `:<line>` tail and a trailing `()` before resolution, AC2 observes both, and the
  false-red rate is re-measured with paths as 15 of 336 distinct, AC4 and F5 with it. One citation
  corrected at source: `CITE_TAIL` is `tools/check-spec-tokens.py:76`, not `:74`. The rev-2 and rev-3
  entries above are left as written. REFUSED: dropping the `.md` exclusion or adding past-tense
  forms in this revision, because either moves unit 5's population and the two specs must count one
  — both are the owner's, as F9 and F10. The migration skeptic's findings about unit 5's own table,
  collision plan and edge payload are that spec's to fold, not this one's.
- rev-5 · 2026-09-21 · the owner's two further rulings of 2026-09-21, on the forks rev-4 raised, and
  the population the two make together. **O5 — the past tense.** F9 is RESOLVED: `retired`,
  `replaced`, `removed`, `deleted` and `dropped` join the closed list, folded like the rest, and
  this spec matches each at a word boundary on both sides because the substring reading pulls two
  items of `DEPL-dRetiredFork-2` in on the slug. S2 and S8 state it; §4's trigger section lists
  the five and re-stages the list; the case table gains a past-tense row and becomes four readings;
  the inflection bullet is re-stated; and AC25 with `tFixture-215` is new, red on any missing form
  and on the substring reading. rev-4's recommendation to keep the list is overruled and deleted.
  **O6 — no `.md` exclusion.** F10 is RESOLVED: the exclusion is deleted in BOTH of its spellings,
  the global test and the dot shape's `md` clause, which rev-4's own measurement had left standing,
  so O6 alone reaches 27 items and not the 25 rev-4 printed. The exclusion bullet is deleted, the
  shape table loses both `.md` clauses, the five exclusions become three plus the `:<line>` strip,
  re-stated as a normalisation, and AC10 is INVERTED with `tFixture-212`: the fixture that had to stay
  silent on a cited `.md` path now has to be named on a slash-bearing one and a bare one, which the
  criterion describes rather than spells because a path-shaped token in a criterion is graded
  against the tracked tree.
  **POPULATION.** The combined figure is derived rather than summed: 38 items across 20 specs at
  `67bec01a` and at `32f2eb71`, super-additive because three items need both rulings. The "23
  against 22" section is replaced by the chain from 643 spec-shaped files; S14, the §3 unit-5 edge
  and AC21 carry 38; and one engine label that is not unique, `aTunedCompass-9` S5c-i cut to `S5c`,
  is stated for unit 5's anchoring. Re-derived with it: the named gap, 8 to 4 live items and 54 to 67
  over the selection; precision, 13, 3 and 7 of 23 to 18, 4 and 16 of 38, with the 15 new items read
  at item level and marked provisional; the resolution false-red rate, 15 of 336 to 19 of 419, still
  4.5%, with AC2, AC4 and F5; each surviving exclusion's effect, AC9 with it; shape 6's zero and the
  `marker` variant's second innocent hit; AC11, AC18, AC24 and the §5 rows; and the fixture block,
  sixteen with nine RED, in S9, §5, §7, Inventory, Files touched and the unit-3 edge. The rev-4
  entry above is left as written. REFUSED: nothing.
- rev-6 · 2026-09-21 · the skeptic's finding against the migration round where it lands on this
  spec, and the main loop's settlement of the reading fork. **THE TOKEN-LESS CLASS.** rev-5's
  named gap counted only verb-bearing items that carry a backticked token, so the items that carry
  none — neither triggered nor inside the gap figure — went unnamed, and a header listing one gap
  reads as coverage of the other. Re-derived here by `probe_u1_rev6_tokenless.py`, which reproduces
  the skeptic's eight label for label: 8 live items across 6 specs at `67bec01a`, the 50
  verb-bearing items accounted for as 38, 4 and 8, and 59 across 48 specs over the selection. S8
  now requires check 25's header to name both unreached classes and not their sizes, and AC18
  observes it; §3 gains a non-goal carrying the figure and the reason the class is out; §4's chain
  and named-gap sections enumerate the eight and read each — four behaviour, one pointer at a
  retirement already in the population, two value spellings, and `TOOL-dGatedProse-4` S2, a
  deletion with a by-value reader that check 25 asks nothing of; and §5's risk row carries both
  classes. **READING B.** F10 marks the fork unit 5's F7 raised as settled: both spellings go, as
  rev-5 wrote, 38 across 20. **THE REV RULE.** §4's corpus-pass section points at unit 5's F1,
  settled the same day, for when a delta clause moves another spec's rev. Also: rev-5's fold wrote
  the §9 and §10 headings twice each, and one of each is gone. The rev-5 entry above is left as
  written. REFUSED: widening the trigger to reach the token-less class, which no ruling asks for
  and which buys 12 live items and 126 over the selection for one withdrawal with a reader; and
  re-sorting §4's precision split against unit 5's census, which this finding did not reach and
  which that section already marks provisional.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a gate arm that grades a spec scope item for a required
marked clause"` returned no seam this unit can extend, and it said why in its own header: `scan
coverage: 79 files scanned | 0 parse skips | unscanned layers: .sh`. This unit's carrier is shell, so
the map is blind to it by construction and its 22 affordance seams cannot answer the question. The
seams this unit extends were found by reading source instead, and they are named by path: the §2 item
accumulator at `tools/memory-tree/check-memory-hygiene.sh:1323-1335`, whose column-0 bullet
splitting, continuation accumulation and `S`-label derivation are reused rather than re-spelled —
and the reuse costs the HOIST of S11, because that accumulator is not reachable where it sits; the
liveness test at `:1385`, reused verbatim rather than re-spelled as a positive whitelist; the
tag-out-of-`bad12_raw` seam at `:1769-1770`, which already routes one awk's tagged records into their
own post-pass; and the batched post-pass shape at `:1385-1389`, where an arm emits a sentinel and the
shell resolves the whole batch in one process — which is what S5's resolution join copies.

One candidate was read and NOT taken, and the reason is the population rather than the mechanism.
`tools/check-spec-tokens.py` already resolves backticked tokens against `git ls-files`, already owns
`memory/project/spec-token-waivers.txt`, and already refuses a stale waiver row — three of the four
things O4 needs. Taking it would have meant re-spelling the verb list, the five shapes, the three
exclusions and the kind-noun set in a second language to know which items own a clause, which is the
second-spelling cost check 24's history already priced in this tree. The waiver mechanism was the
attractive half; rev-3's F8 offered it for the residual red, and the owner ruled the corpus pass
instead.

Three stale claims found and corrected against source rather than carried. The dry run's statement
that `ARMS_FLOORS` must move for this gate is FALSE, because `tools/memory-tree/check-arms.py:290`
compares one-sided. The skeptic's statement that the near-twin arm is "check 23's
`SCOPE_JOIN_CUTOFF` arm" is FALSE as to the check NUMBER — that arm is check 12's, and check 23 is
the acceptance ledger. And `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md:108`
records that the hygiene catalog "stops at item 22 while the shell implements 23"; that record is now
STALE rather than wrong, because check 24 has since landed in the catalog out of numeric order at
`memory/HYGIENE.md:299`, so the catalog reads 1 to 22 and 24, and the shell's own README count of 23
lags the tree's 24. The record is cited as written and not rewritten; §4's Inventory states the
tree's figure, derived.

Recall terms used: `python tools/memory-recall/query.py "why does a hygiene check grade the shape of
a spec clause rather than whether the clause is complete" --terms "hygiene check shape-only cutoff
scope item clause escape spelling grandfather filename date arm witness"`. It returned 40 hits over
1136 records, of which three decided design points here: `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md:108`,
which records that the hygiene catalog is not renumbered, read with the staleness noted above;
`TOOL-aJoinedCanon-13` in `memory/backlog/TOOL.md`, which records that the example-conf parity arm
derives its key set from one engine — a record this revision uses in the negative, since O2 leaves
that population untouched; and
`memory/builds/cTracedPromise/spec/2026-08-15-spec-cTracedPromise-2.md:17`, which records the
double-gating pattern this unit's F3 adopts.

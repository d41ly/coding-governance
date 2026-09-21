# TOOL-dGatedProse-1 — a retirement answers for its readers, as a shape a machine reads

**Status:** SPECCED · rev-3 · 2026-09-21 · node d · Tier-2 · base fcbfba5f · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A spec scope item that retires a name, a row kind or a vocabulary member must carry a `**Readers:**`
clause with a `by name:` half and a `by value:` half, and a new numbered hygiene check refuses the
item that carries neither. The class behind three consecutive spec audits of `dLoggedFlight` is a
reader the author never typed, and no predicate over prose can find one; what a predicate CAN do is
refuse to let the question go unasked, which is what those three audits had to ask by hand.

The population is every LIVE spec from the commit that lands the check, by the owner's ruling of
2026-09-21, with no cutoff key of any kind. So the check has corpus work on day one rather than a
phase-in, and that work — measured, enumerated and split by owning node — is S14 rather than a
sentence.

## 2. Scope (IN)

- **S1** — the POPULATION, and NO cutoff key. The arm grades a spec of check 12's own selection when
  that spec is LIVE, liveness being the engine's own spelling at
  `tools/memory-tree/check-memory-hygiene.sh:1385` — a status header that is not `CLOSED` and not
  `WONTDO`. No `READER_INVENTORY_CUTOFF` is declared, in the engine, in `.memory-tree.conf` or in
  `tools/memory-tree/.memory-tree.conf.example`, so there is no key to arm, to grandfather with or to
  discover. Observed by AC12 and AC13.
- **S2** — the TRIGGER, per §2 scope item, built over the HOISTED item accumulator of S11. An item
  triggers when a verb from the closed retirement list governs it AND the same item carries a
  backticked token of one of five identifier shapes, none of the five shape EXCLUSIONS applying; or,
  where it carries no such token, when a backticked bare word sits beside a declared kind noun.
  Observed by AC1, AC7, AC8, AC9, AC10 and AC11.
- **S3** — the KIND-NOUN set, six phrases, as ONE literal in the arm immediately beside the verb
  list, because a verb table and a noun table in two carriers can disagree and no refusal can make
  them agree. `memory/HYGIENE.md`'s catalog entry POINTS at that literal and does not restate it.
  Observed by AC11.
- **S4** — the CLAUSE and its TWO escapes, one per graded question. A triggered item carries
  `**Readers:**`, then both `by name:` and `by value:`. The by-value half carries either a backticked
  token or the escape `NO VALUE READERS` followed by a reason. Every name the by-name half lists must
  RESOLVE, or that half carries the escape `READER NOT IN TREE` followed by a reason. A clause is
  graded wherever it appears, whether or not the trigger fired on that item. Observed by AC1, AC2,
  AC3, AC4, AC5 and AC6.
- **S5** — the RESOLUTION seam, and its cost. The arm emits each by-name token as a `\004`-tagged
  record; ONE batched `git grep -l -F -f` narrows the tree to the files matching any of them and an
  awk pass over those files attributes each token, against a corpus that is the tracked tree OUTSIDE
  `memory/builds/*/spec/`. The escape's every covered name is PRINTED, so a skip announces itself.
  Observed by AC4, AC5 and AC17.
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
  the control that proves why. The check-count sentence at `tools/memory-tree/README.md:18` moves
  with it, because the unit that changes the number of checks is the unit that owes the count.
  Observed by AC18.
- **S9** — the fourteen-fixture block `tFixture-200` through `tFixture-213` in the gate's sibling
  fixture suite, with the positive arm that arms the new branch, the three GREEN fixtures that pin
  the false-positive classes the skeptic found, the two that pin rev-3's own two, and the one that
  pins the liveness filter. Observed by AC1 through AC12 and by AC23.
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
- **S14** — the CORPUS PASS, which is this unit's work and not a follow-up. Under S1 the arm grades
  every live spec, and the trigger fires on 22 items across 13 specs today. Of those, the FIVE items
  in the TWO node-`d` specs gain a `**Readers:**` clause in this unit's own commit, additively, one
  clause per triggered item, with the by-value half derived from the code the retired name flows into
  or written as `NO VALUE READERS` with its reason. The seventeen items in the eleven specs owned by
  nodes `a` and `b` are NAMED in §4 and LEFT ALONE, because another node's live spec is another
  session's work and this build does not edit across that line. The population is RE-DERIVED at the
  build pass rather than read from §4's table, because liveness moves. Observed by AC21.

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
- **NO KIT-VERSION BUMP AND NO MARKER RE-STAMP, and the reason is topological rather than a
  deferral.** `tools/memory-tree/check-verdict-epoch.sh` requires the newest commit in `<base>..HEAD`
  that moves a behaviour-bearing line of its scan set to be an ancestor of, or equal to, the newest
  commit that CHANGES `KIT_MEMORY_TREE_VERSION` — the rule is stated at `:16`-`:24` and implemented
  as `git merge-base --is-ancestor "$W" "$S"` at `:179`. This unit moves the engine at order 1 and
  `TOOL-dGatedProse-3` moves it again at order 3, so a bump here would leave the last change
  DESCENDED from the bump and red that leg from unit 3's commit through the build's tip. The single
  move is therefore unit 3's, in its own commit, together with the re-stamp of every carrier of the
  retired marker from a derived population. This unit's own commit leaves the constant at 2.79 and
  every marker with it, which reds `verdict epoch` at order 1 and order 2 and is closed at order 3
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

- **hands-off** `TOOL-dGatedProse-2` — `tools/memory-tree/SPEC-TEMPLATE.template.md`, where S13
  writes this check's author-facing line, and `memory/TEMPLATE-SPEC.md`, which this unit re-renders
  from it. Unit 2 edits both carriers for its own dossier-claims rule, must write into the TEMPLATE
  and never the render, and reads the line this unit left. The kit version does NOT cross here: the
  marker that unit reads is the 2.79 at the pinned base, unchanged by this unit, and the single move
  is unit 3's.
- **hands-off** `TOOL-dGatedProse-3` — `tools/memory-tree/check-memory-hygiene.sh` and its fixture
  suite, which this unit leaves with one new `fail 25` branch, the S11 hoist, a `\004` tag split, a
  zero-population notice, a fourteen-fixture block and a RAISED `FLOOR_ASSERTIONS`. Four specifics,
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
  One more crossing, new at rev-3 and in unit 3's favour: its S8 carries a voluntary `**Readers:**`
  clause. A clause is graded wherever it appears, triggered or not (S4), so that clause's by-name
  names must resolve or carry `READER NOT IN TREE` with a reason. Its §2 item does not trigger under
  this unit's verb list — `retired` is in neither the strict list nor the four stems — so the clause
  is optional; its HALVES are not.
- **hands-off** `TOOL-dGatedProse-4` — two crossings, neither of them a marker. This unit edits the
  engine at order 1, which is one of the two behaviour-bearing moves the epoch rule ranges over, so
  the build's single bump being mis-placed surfaces at unit 4's bar as well as at unit 3's. And this
  unit's render pass regenerates all four dogfood pairs from their templates,
  `memory/guides/BUILD-METHOD.md` included, which is unit 4's whole write set — byte-identically at
  order 1, because nothing in that write set has moved yet. Unit 4's own rev-3 reads both of those
  correctly, and it also reads the third crossing: check 25 grades unit 4's spec, and no §2 item of
  it fires.
- **consumes-from** external — the `SPEC_FORMAT_CUTOFF` declaration this repo already carries. With
  it blank the new check is disarmed, which S10 declares and AC13 observes; it is not a defect this
  unit closes.
- **hands-off** external — the seventeen triggered items in the eleven live specs owned by nodes `a`
  and `b`, enumerated in §4. This unit names them and writes none of them. Until their owners write
  those clauses, `memory hygiene` reds — see §7 and F8.

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
rather than silently dropped. One of the nine is a node-`d` spec this unit's corpus pass therefore
reaches, `dScaffoldedMirror-9`, and S14 counts it.

**THE MEASUREMENT, OWN-PROBE, 2026-09-21.** The probes are `probe_final_rev3.py` and
`probe_cost_rev3.py`, written to this session's scratchpad. They are UNTRACKED, so nothing in the
tree resolves them and a later reader cannot re-open them — which is why every figure below is
stated with what it is a count OF.

| population | size | derivation |
|---|---|---|
| tracked spec-shaped files | 642 | the engine's own check-12 path regex |
| at/after `SPEC_FORMAT_CUTOFF` 2026-07-15 | 640 | check 12's selection, which check 25 inherits |
| LIVE within that selection | 37 | the `:1385` liveness test |
| triggered items | 22 across 13 specs | the shipped trigger below |
| the accumulator's union population | 120 | live 37 ∪ the 89 at/after `SCOPE_JOIN_CUTOFF` |

The dry-run journal reports a different pair over a different set — "the raw verb vocabulary flagged
19 of 24 live specs, requiring a backticked NAME brought it to 14" — and those are SPECS, over a
24-spec reading of liveness. The 22 here are ITEMS, over 37. Do not conflate them; the corpus grew
and the liveness test is now the engine's rather than the journal's.

### The trigger, and every figure it rests on

The VERB list is closed, and it is the strict list the dry run stated literally: `retires`,
`is replaced by`, `are replaced by`, `removes`, `deletes`, `drops`, `no longer exists`,
`no longer carries`, `no longer reads`, `stops being`, `ceases`, `goes away`, and
`leaves the` followed by `layouts`, `set` or `vocabulary`. To that list this unit ADDS the four bare
imperative stems `retire`, `delete`, `remove` and `drop`, matched case-insensitively at a word
boundary, and the addition is the single most consequential decision in this spec.

Measured over the 37 live specs, OWN-PROBE: the strict list alone triggers 14 items across 9 specs;
adding the imperative stems gives 24 across 14; applying rev-3's two new shape exclusions brings the
shipped rule to 22 across 13. The stems therefore add 10 items and 5 specs, which is the same delta
three independent readings of the rule produced at rev-2 over a smaller corpus, so the decision does
not rest on a number that moves.

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
| contains a slash, and does not end in `.md` | a code-file path | `tools/check-kit-versions.sh` |
| contains a dot whose tail segment is word characters other than `md` | a qualified symbol or a script | `merge.conflictStyle`, `inventories.json` |
| carries an internal case transition, a lowercase letter immediately followed by an uppercase one | camel and Pascal identifiers | `conflictStyle` |
| two dashes then a letter | a long option | `--write-ratchet` |

FIVE token classes are EXCLUDED by shape, three from rev-2 and two found by rev-3's own
re-derivation, and each exclusion answers a measured finding:

- **A `.md` path is never an identifier.** The dry run's own hit 2 turned on this: `aMendedLedger-1`
  S1 deletes three `.md` stub files and retires no name, while the genuine retirement one bullet
  lower is invisible because its only backticked token is an `.md` path. The exclusion keeps the
  innocent item out. It does NOT recover the genuine one, and that is a NAMED GAP below.
- **A family-slug-seq id is never an identifier.** Measured: one backticked id sits inside a
  verb-bearing live item, `PLAY-aPrunedCeremony-5` in `aMendedLedger-1` S7, whose item closes a
  decision row and retires no name.
- **A token that is only dashes and digits is never an identifier.** This is the skeptic's
  elided-slug class. §2 of the charter sanctions family-plus-seq shorthand in prose, so the pair
  `TOOL-dLoggedFlight-21` and `-24` puts a bare `-24` in backticks, and a flag-shaped test reads it
  as a retired name. Measured over the live population: ZERO such tokens sit inside a verb-bearing
  item, so the exclusion changes no verdict today and is a forward guard.
- **A token carrying a SPACE is never an identifier.** NEW at rev-3, and the only new exclusion that
  changes a verdict today. A backticked CODE FRAGMENT or config line is not a name: measured, it
  drops exactly two items whose only identifier-shaped token was one — `aBatchedLintel-1` S3, whose
  token is `body=$(_unfenced "$f")`, and `aMendedLedger-6-u6` S5, whose token is a `.gitattributes`
  line. Both are innocent under the eye, both would have cost a real clause under O2, and the
  exclusion costs nothing else: no live item triggers on a space-bearing token and nothing else.
- **A `:<line>` tail is stripped before the `.md` test.** NEW at rev-3, and a 0-verdict forward guard
  of the same kind as the dashes-and-digits one. `…template-v-2-1.md:9` is an `.md` path wearing a
  citation tail, and without the strip it passes the slash shape and reads as a code file. Measured:
  one live verb-bearing item carries such a token and it triggers on a different identifier anyway,
  so the verdict count is unchanged. The precedent is `tools/check-spec-tokens.py`'s own `CITE_TAIL`
  at `:74`, which exists for the same reason one file over.

A sixth exposure was looked for and is absent: a bare version token such as `2.79` would pass the
dotted-tail shape, and ZERO verb-bearing live items carry one. It is recorded rather than guarded,
because a guard against a class the corpus does not produce is a clause no fixture can observe
honestly.

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
That item retires nothing. The six-phrase set fires on ZERO items over the live population AND zero
over all 640 selected specs, which is the property the owner's ruling rests on and for which the
fixture `tFixture-207` is the whole coverage.

### The NAMED GAP that remains, measured

**Pinned rather than implied away.** A retirement whose only backticked token is a bare word with no
kind noun beside it, a hyphenated bare word such as `check-brief-recorded`, an `.md` path, or a
space-bearing fragment is NOT triggered, so its author is never asked the by-value question.

Measured over the live population, OWN-PROBE: 8 items, enumerated rather than counted so a later
reader can re-judge each — `aBatchedLintel-1` S3, `aGradedDoorway-7` S4 on `run()`,
`aMendedLedger-1` S2 and S7, `aMendedLedger-6-u6` S1, S3 and S5, and `TOOL-dGatedProse-4` S3, this
build's own sibling. Over the whole 640-spec selection it is 54 items. The dry run's
`aMendedLedger-1` S2 — "Retire the authored session ledger to `memory/archive/ledger/{a,b,c}.md`" —
is a genuine retirement inside that gap, and it is the member that matters: shape 6 does not reach
it, because the item carries no kind noun and inventing one to satisfy a gate is the mirror this
repo forbids elsewhere.

### The trigger's measured precision, with every innocent named

Over the live population the shipped trigger fires on 22 items across 13 specs. Read one by one,
five are innocent and one is borderline, so precision is 16 of 22, or roughly three in four — the
same band rev-2 stated, now over a re-derived population and with two false positives removed by
shape rather than by judgement. The innocents, named exhaustively:

- `aGradedDoorway-7` S2 — the item raises `SHARD_ARITY` and fixes what breaks. The verb came from
  "a shard that silently drops arms", a failure mode. The dry run judged the same item innocent.
- `aQuarriedLantern-1` S6 — "A build deletes sibling cache directories whose recorded `worktree` no
  longer exists" is runtime eviction behaviour.
- `aMendedLedger-1` S1 — deletes three `.md` stubs and gives a build slug a folder; its only
  identifier is the slug `bThriftyBellows`.
- `bConvergentLodestar-1` S2 — the `remove` is in "on symbol add/remove", describing when a
  generated artifact churns.
- `bConvergentLodestar-1` S3 — the verb sits in the design of a shortlist that is "not a hard top-K
  lexical cut".
- BORDERLINE: `aMendedLedger-8-u9` S11 neutralises `merge.conflictStyle`, which retires a config's
  effect rather than a name, and the verb that fires is in a failure-mode sentence.

The node-`d` five that S14 actually writes split the same way, and they are stated here because they
are the evidence for what a clause COSTS. `dScaffoldedMirror-9` S5 is a genuine retirement of three
`*_OFFENDER_PIN` keys with live readers in `lexicon.py`, `kit.toml` and `drift_signals.py`; its S6
deletes 70 lines of conf archaeology and its S7 ADDS two verbs, so both are false triggers whose
honest answer is the by-value escape with a reason; `dPolishedVitrine-1` S5 drops two carried ratchet
rows, which is a genuine row-kind retirement; and its S10 is a paragraph of round-3 repairs whose
verb sits in behaviour prose. Two genuine, three escaped, five lines of prose.

A false trigger costs the author one line. That asymmetry is why a trigger at this precision is
wireable when the refuted predicate at precision 0.00 was not — but under O2 the cost is no longer
hypothetical, and F8 records what it adds up to across nodes this build cannot edit.

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

**A clause is graded wherever it appears, and not only where the trigger fired.** The trigger decides
where a clause is REQUIRED; the marker decides where its halves are GRADED. Otherwise a voluntary
clause with a broken by-value half passes silently, which is the same could-not-fail shape one level
down, and `tFixture-213` is the arm for it. Unit 3's own voluntary clause is the first live instance.

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

**The resolution predicate's false-red rate is measured, not hoped.** OWN-PROBE over the tokens a
by-name half draws from — every backticked symbol-shaped token in the live specs' §2 items, 223 of
them, 147 distinct: 4 fail to resolve anywhere else in the tracked tree, and 7 fail against the
tighter corpus that excludes the spec records themselves. That is 3.1%, and the five distinct
members are exactly the escape's constituency: `optIn` and `roster_refusal`, names their own builds
had not yet written; `union.SETS` and `union.snippet_bytes`, qualified members spelled as prose
compositions; and `READER_INVENTORY_CUTOFF`, which was this spec's own invented key at rev-2 and no
longer exists anywhere. A predicate whose false-red rate is 3% and whose escape is one line is
wireable; the measurement is the argument.

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
  would have to re-spell the verb list, the five shapes, the five exclusions and the kind-noun set to
  know which items own a clause, which is the second-spelling cost one paragraph up, paid across two
  languages. The waiver registry was the attractive half, and F8 records it as one of the owner's
  three options for the residual red; the clause itself stays in the spec, beside the retirement,
  where the author is.
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

### The corpus pass, and the line this build does not cross

S14 is the work O2 creates. It is stated as a rule and a population; the tables below are a
MEASUREMENT of 2026-09-21 and are re-derived at the build pass rather than read.

**Node `d` — brought into compliance by this unit, additively, one clause per item:**

| spec | items |
|---|---|
| `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-9.md` | S5 · S6 · S7 |
| `memory/builds/dPolishedVitrine/spec/2026-09-12-spec-TOOL-dPolishedVitrine-1.md` | S5 · S10 |

Both are live work rather than records: the first is `DEFERRED` and is in the population only under
the engine's liveness test, the second is `INPROGRESS` at rev-8. So the second carries the collision
risk the charter names — a shared file two sessions may edit — and its clause is written at the build
pass after re-deriving the trigger against that file as it then stands, never from this table.

**Nodes `a` and `b` — NAMED here and left alone, seventeen items across eleven specs:**

| spec | node | items |
|---|---|---|
| `memory/builds/aGradedDoorway/spec/2026-08-29-spec-TOOL-aGradedDoorway-7.md` | a | S2 |
| `memory/builds/aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md` | a | S6 |
| `memory/builds/aMendedLedger/spec/2026-08-09-spec-aMendedLedger-1.md` | a | S1 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md` | a | S5 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-3-u2-ledger-retirement.md` | a | S2 · S3 · S6 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-4-u3-hygiene-gate.md` | a | S3 · S4 · S7 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md` | a | S5 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-6-u6-doc-truth.md` | a | S11 |
| `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-7-u8-keyed-corpus.md` | a | S5 |
| `memory/builds/aMendedLedger/spec/units/2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md` | a | S2 · S11 |
| `memory/builds/bConvergentLodestar/spec/2026-07-22-spec-bConvergentLodestar-1.md` | b | S2 · S3 |

**THE BAR CANNOT BE GREEN UNTIL THOSE OWNERS WRITE THOSE CLAUSES.** `memory hygiene` is subject
`repo` with no guard, so it runs on every bar; from the commit that lands this arm it names those
seventeen items, and nothing in this build can clear them without editing another node's live spec.
That is not a defect of the arm and it is not a reason to weaken it — it is the corpus work the
owner ruled with the consequence stated. What this unit owes is that the red is LEGIBLE: every one
of the seventeen is named above, each message names the item and the escape spelling that answers
it, and F8 carries the scheduling question, which is the owner's and not this unit's.

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
| `tFixture-200` … `tFixture-213` | the fixture block's own `hit` and `miss` rows |
| `\004` | the tag split, beside the `\002` and `\003` splits it copies |

Check numbers 1 through 24 are all claimed: 1 to 12 plus 21, 22 and 23 carry `fail <n>` call sites in
the engine, and `memory/HYGIENE.md`'s catalog numbers 1 to 22 and 24. 25 is the next free integer.
This repo declares no naming cell for a shell variable, so no lexicon cell grades the arm's own
awk-local names. NO new `*_CUTOFF` preset is added, which is the whole of rev-3's change to this
table: the example-conf parity loop derives its population from the engine's bare presets, and this
unit leaves that population untouched.

### Migration

None of the mechanical kind: nothing is renamed, no key is added, no adopter conf changes. The
migration IS the corpus pass of S14 and the residual red F8 records, which is a different animal
from a schema change and is why it is written as scope rather than here.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | the S11 hoist, the arm with the verb list and the kind-noun literal, the `\004` split, the batched resolution post-pass, `fail 25` and the zero-population notice — about 110 lines |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the fourteen-fixture block, its `hit` and `miss` rows, the positive arm, the dependency arms, the S11 regression arm, the RAISED `FLOOR_ASSERTIONS` — about 180 lines |
| `tools/memory-tree/HYGIENE.template.md` | check 25's catalog entry — about 26 lines |
| `memory/HYGIENE.md` | REGENERATED, never hand-edited |
| `tools/memory-tree/README.md` | the check-count sentence, 23 to 25 with 24 enumerated — 1 line |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S13's author-facing line in the `## 2. Scope (IN)` skeleton |
| `memory/TEMPLATE-SPEC.md` · `memory/guides/ANNOTATION-STYLE.md` · `memory/guides/BUILD-METHOD.md` | REGENERATED by the parity script, never hand-edited |
| `memory/map/features/memory-tree-hygiene.md` | the H1's derived count removed, and the body count with it — 2 lines, no claim edit |
| two node-`d` spec files | S14's five `**Readers:**` clauses — about 12 lines, additive |

Two groups of rows are shorter than at rev-2, each for one reason. `.memory-tree.conf` and
`tools/memory-tree/.memory-tree.conf.example` leave this list entirely, because O2 deletes the key
they would have declared. The four `*.template.md` line-1 markers leave it because the re-stamp is
unit 3's. The renders are still regenerated here, because this unit edits two of the four templates
and the render loop is all-or-nothing over the `PAIRS` table at
`tools/memory-tree/kit-dogfood-parity.test.sh:58`.

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
  population is the by-name tokens of triggered items, 0 today and about 40 after S14's five
  clauses, at a measured 0.602 s for one batched `-l` grep of 498 tokens against 138.4 s for the
  line-printing form and 0.047 s per token for a loop. The leg's last recorded run is 33.3 s and its
  declared ceiling is 12720 s, which is why the ceiling is not the protection and the shape is.
- error / empty / loading states — a zero LIVE population prints the notice of S7 and exits 0. A
  blank `SPEC_FORMAT_CUTOFF` disarms the check, declared in two carriers and observed by AC13. A
  resolution batch with no tokens runs no grep at all rather than one with an empty pattern file,
  which `git grep -f` treats as matching nothing and would report every name unresolved.
- observability — the failure message names the file, the item label, the missing half or the
  unresolved name, and the escape spelling that answers it, so a red row is actionable without
  reading the gate. Every name accepted under the by-name escape is printed. The zero-population
  notice names the liveness test.
- risks — five. First, precision is roughly three in four by this spec's own reading, so an author
  will occasionally write a clause on an item that retires nothing; the cost is one line and three of
  the five node-`d` items are exactly that case. Second, the NAMED GAP is 8 live items wide and shape
  6 does not reach its measured member. Third, the residual red across nodes `a` and `b` is seventeen
  items this build cannot clear — F8. Fourth, the declared dependency on `SPEC_FORMAT_CUTOFF` means
  an adopter can get nothing from this arm without a key it does not own. Fifth, S11 edits a LIVE arm
  of check 12 rather than only adding beside it; the hoist is behaviour-preserving by construction,
  and AC15 is the check that exercises that claim over the seven existing scope-join fixtures.
- testing — the failing case is staged and observed RED before the branch lands, per the charter. The
  fourteen-fixture block carries six RED fixtures and eight GREEN ones, five of the GREEN ones
  existing only to pin false-positive classes so that a later widening of the identifier test reds
  rather than passing quietly. Every fixture is named by exactly one criterion, and every criterion
  by exactly one fixture.
- migration — none of the mechanical kind, per §4; the corpus pass is S14.
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
- **AC2** — When that same item gains a `**Readers:**` clause carrying `by name:` with a token that
  resolves and then `by value:` with a backticked token, the run is silent for `tFixture-201`.
  Red when: the arm reds a conforming clause, which would make the remedy unreachable.
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
  glob, never pinned. Measured base rate over live specs' §2 tokens: 7 of 223 unresolved.
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
  Red when: a backticked code fragment is read as a retired name, which cost two real items of the
  live corpus a clause each before this exclusion was written.
- **AC10** — When a triggered-looking item's only backticked token is an `.md` path wearing a
  `:<line>` citation tail, the run is silent for `tFixture-212`.
  Red when: the `.md` exclusion is applied before the tail is stripped, which turns every cited
  document into a code path.
- **AC11** — When `tFixture-207` carries a retirement verb, a backticked bare word and a declared
  kind noun and no clause, the run NAMES it; and a grep for each of the six noun phrases over
  `tools/memory-tree/check-memory-hygiene.sh` returns one line each, all six adjacent and
  immediately beside the verb list, while the same grep over `.memory-tree.conf` and
  `tools/memory-tree/.memory-tree.conf.example` returns nothing.
  Red when: the shape does not fire, which leaves the owner's O3 closure unbuilt; or the noun set
  exists in two carriers, which is the disagreement the single literal exists to prevent.
  figure: the set fires on 0 items of the live corpus and 0 of the 640-spec selection, DERIVED, so
  the fixture is its whole coverage and the corpus cannot witness it.
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
  states the kind-noun COUNT without listing the nouns, and `tools/memory-tree/README.md` line 18's
  check sentence names 25 and enumerates 24 beside 20 under `row_grammar.py`.
  Red when: the entry lands without the per-half grading sentence, which is how a reader concludes
  the inventory is checked; or it restates the noun set, which is the second copy S3 exists to
  prevent; or the README keeps a count its own enumeration contradicts, which it does today at 23
  against 24 checks.
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
  unit's commit, it names ZERO item of any node-`d` spec under check 25, and every item it does name
  appears in the nodes-`a`-and-`b` table of §4 with its own spec and label.
  Red when: a node-`d` item is still named, which means the corpus pass missed one or worked from
  §4's table instead of re-deriving; or an item is named that the table does not carry, which means
  the population moved between this spec and the pass and the pass did not re-measure.
  figure: both sides are DERIVED at observation time — the run's own output against the table, which
  is a measurement of 2026-09-21 and is expected to move.
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
  green, and unit 3's own S8 is the first live instance of a voluntary clause.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `build README slot contract`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · a fixture §2 item at a live status carrying a retirement verb and a backticked underscore identifier with no `**Readers:**` clause, staged and observed RED before the branch lands · none — both `ARMS_FLOORS` figures are one-sided and the pinned 27:27 sits below the 31 branches the gate carries today

**TWO of those legs are expected RED at this unit's commit, and neither is a defect this unit can
close.** `verdict epoch` reds because the build's single kit-version move is unit 3's and the epoch
rule is topological: at this commit the engine has moved and no commit in the range changes the
constant, which is exactly that checker's "behaviour-bearing line(s) of the engine moved … and NO
commit in the range changes KIT_MEMORY_TREE_VERSION" branch. It goes green at order 3.
`memory hygiene` reds on the seventeen items owned by nodes `a` and `b` that §4 names and S14
refuses to edit, and it stays red until those owners write those clauses — F8 carries the question.
Both are stated here because the owner's rule is that units run no gate legs and the bar runs once
after every unit is built: a red discovered there, unannounced, would read as this unit's failure.

`kit version markers` LEAVES this section, where rev-2 added it: with no bump and no re-stamp this
unit moves nothing that leg reads. `kit/dogfood doc parity` stays, because this unit edits two of the
four templates and lands through their renders.

**`memory-hygiene self-test` IS HELD BY DEFAULT, and this unit's entire S9 lives in it.** It is
subject `kit`, chunk `selftests`, guarded on `tools/lib/` and `tools/memory-tree/`, so a green bar
without `GATE_FULL=1 GATE_SELFTESTS=1` exercises none of the fourteen fixtures. That is why every
criterion above observes the engine, the checker or the grep DIRECTLY rather than naming the suite.
This unit's Definition of Done is kit work, so it owes the total run.

Two obligations sit outside this unit's own arms and are named so nobody discovers them at the bar.
The §3 reciprocity join is live on the full bar for a spec dated at or after the edges cutoff, and
all three siblings declare **consumes-from** this unit, so all three **hands-off** bullets in §3 are
load-bearing rather than courtesy — deleting one reds
`tools/memory-tree/check-memory-hygiene.sh:1800`'s half-declared-pair message on the sibling's file
rather than on this one. And the four dogfood copies are regenerated rather than hand-stamped, which
is a command to run and not a diff to write: the parity script's own render mode, whose spelling is
in that script's usage header rather than copied here, where it would read as an observation.

## 8. Open questions

- **F1 — the verb vocabulary's reach.** FACT-QUESTION · Does adding the four bare imperative stems to
  the dry run's strict list buy coverage the strict list does not have? The probe: run both
  vocabularies over the live corpus and compare the triggered item sets against the three items the
  dry run named as real, uninventoried retirements. The liveness assertion is that the probe can
  return a negative, and a sibling arm of the same probe did — the bare-word shape returned zero
  items under both vocabularies. RESOLVED (agent, 2026-09-20): the imperative stems are IN. The
  strict list reaches NONE of the three named items and the stems reach ALL THREE. Re-derived at
  rev-3 over the 37 live specs: 14 items strict, 24 with the stems, 22 after rev-3's two shape
  exclusions — the stems add 10 items and 5 specs, the same delta three independent readings gave at
  rev-2 over a smaller corpus.
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
  being built: 7 of 223 candidate tokens over the live corpus fail to resolve, a 3.1% false-red rate
  whose five members are named in §4. What the ruling explicitly does NOT buy is the control
  revision: `TOOL-dLoggedFlight-22` rev-3 lists three readers fewer than it has and every name it
  does list resolves, so it still passes.
- **F6 — should the NAMED GAP be closed by declaring a kind-noun vocabulary?** RESOLVED (owner,
  2026-09-21): YES, prospectively. The six-phrase set of S3 fires on 0 live items and 0 of the 640
  selected specs, so it adds no corpus work today and closes the bare-word case by rule rather than
  by memory. Measured caution folded with it: a single-noun set containing `marker` fires on one
  innocent item of the selection, which is why the declared phrases are multi-word.
- **F7 — the phase-in question, as a PAIR across two units.** RESOLVED (owner, 2026-09-21): NEITHER
  new predicate takes a cutoff. This unit declares no `READER_INVENTORY_CUTOFF` and
  `TOOL-dGatedProse-2` declares no `SPEC_CLAIMS_CUTOFF`; both grade every live spec from the commit
  that lands them. The ruling was made with the consequence stated, and the consequence for this
  unit is S14 and F8.
- **F8 — OWNER'S, and new at rev-3. The residual red across two other nodes.** Under O2 the arm
  names 22 items across 13 live specs, of which 17 across 11 sit in specs owned by nodes `a` and
  `b`. This unit brings the 5 node-`d` items into compliance and names the rest, so `memory hygiene`
  — subject `repo`, no guard, on every bar — is RED from this unit's commit until those owners write
  those clauses. Three resolutions exist and the choice is scheduling rather than fact, which is why
  it is the owner's: hold this unit's landing until nodes `a` and `b` have written seventeen clauses;
  land it red and carry the red as known, which the charter's own rule against exempting a leg to
  unblock a landing argues against; or ship a drainable handoff registry beside the arm, one row per
  file-and-item pair with its owning node and reason, refused when stale, which is the mechanism
  `tools/check-spec-tokens.py` already uses for its own cross-corpus hits at
  `memory/project/spec-token-waivers.txt` and which this spec does NOT build, because naming and
  waiting is what the ruling asked for. The measurement each option needs is in §4, enumerated by
  spec and label.

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
things O4 needs. Taking it would have meant re-spelling the verb list, the five shapes, the five
exclusions and the kind-noun set in a second language to know which items own a clause, which is the
second-spelling cost check 24's history already priced in this tree. The waiver mechanism was the
attractive half, and F8 records it as one of the owner's three options for the residual red.

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

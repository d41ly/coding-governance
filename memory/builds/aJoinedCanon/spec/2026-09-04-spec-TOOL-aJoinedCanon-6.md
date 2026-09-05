# TOOL-aJoinedCanon-6 — a ledger answer is joined to its own criterion

**Status:** SPECCED · rev-5 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 6 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Check 23 pairs a spec's acceptance criteria to their ledger answers by LABEL and compares nothing
else, so a ledger line keyed `AC4` that answers `AC5`'s question passes and a ledger line keyed to a
label the spec never wrote is invisible. This unit adds the two halves of that join a machine can
actually decide: a walk of the ledger's own labels, and a token comparison between a criterion and
the answer that claims to evidence it.

## 2. Scope (IN)

- **S1** — A ledger-side label walk. Every `**Evidences:** <uid>` bullet whose `<uid>` is in check
  23's graded unit set and whose label the spec's §6 does not number becomes a named failure.
  Observed by AC1.
- **S2** — A token join. For a criterion whose label DOES appear in the ledger map, the criterion's
  backticked tokens and the answer's backticked tokens must share at least one token under
  case-folded bidirectional containment. Observed by AC2 and AC3.
- **S3** — Both arms are bullet-scoped on both sides: a criterion's tokens are collected across its
  continuation lines, and so are an answer's. Neither side is free. `alledger`'s existing `form`
  classification reads a ledger bullet's FIRST LINE only, so the LEDGER emitter is widened as well
  as the spec one, and a fold that widened only the spec side would leave half of this item
  unbuilt. Observed by AC4, which grades both sides.
- **S4** — Two new dated cutoff keys, `LEDGER_LABEL_CUTOFF` and `LEDGER_TOKEN_CUTOFF`, each compared
  against the SPEC's filename date exactly as `alcut="${ACCEPTANCE_LEDGER_CUTOFF:-}"` is in
  `tools/memory-tree/check-memory-hygiene.sh`, each blank-means-off. Each is declared in
  `.memory-tree.conf` beside its siblings AND shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`, copying unit 8's S3 — the example-conf parity arm
  in `check-memory-hygiene.test.sh` derives the engine's `*_CUTOFF` presets and the `${NAME:-}` read
  form alike and reds any key the shipped example does not declare, so a key that reaches only the
  local conf reds `memory-hygiene self-test` on this unit's own landing commit and leaves an adopter
  with a dead arm reading as armed. Each key's comment, in BOTH confs, states S9's dependency.
  Observed by AC5, AC6 and AC13.
- **S5** — Both arms announce an empty population, in the shape the existing
  `check 23 measured NO unit` line already uses, so a cutoff that grandfathers everything is not
  mistaken for a clean run. Not
  optional and not hypothetical: with both cutoffs ahead of the fleet (§4), an empty population is
  what the landing commit itself measures. Observed by AC7.
- **S6** — The ledger grammar in `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`
  states the token rule, so an author reads it where the grammar lives rather than discovering it
  from a red bar. Observed by AC14 for the CONTENT and by AC8 for the pair parity — two criteria
  because AC8 is a byte-compare and is green when the rule reached neither half.
- **S7** — A failing fixture per new `fail 23` branch in `check-memory-hygiene.test.sh`, with the
  positive `hit` assertion the harness meta-gate requires. Fixture ids come from this unit's block in
  the build README's `tFixture` allocation — `tFixture-140` upward, by that README's `80 + 10N`
  rule — which is owned there and not re-derived from the file's high-water at build time. Observed
  by AC9.
- **S8** — The kit version advances in this landing, because both arms change what the engine
  VERDICTS: `KIT_MEMORY_TREE_VERSION` in `tools/memory-tree/check-memory-hygiene.sh` moves by one
  minor, and every `gov:kit memory-tree@` carrier moves with it. The carrier set is derived at build
  time with `grep -rl 'gov:kit memory-tree@'` and is not counted here — `TOOL-dSettledRoster-4`
  records a remediation message naming three carriers when more existed. Observed by AC12.
- **S9** — Both arms are declared as what they are: BRANCHES OF CHECK 23, never independent checks.
  The block they live in opens on `if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`, so a blank
  `ACCEPTANCE_LEDGER_CUTOFF` disarms both of them whatever their own keys say, and the graded spec
  set is filtered by `alcut` before either arm sees it. That dependency is written into each new
  key's comment in both confs and is OBSERVED, not asserted — it is the one shape this build's
  round-1 blocker and round-2 blocker were both instances of. Observed by AC13 and AC15.
- **S10** — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` moves to a fresh
  `<ISO datetime> @ <sha>` per that manifest's own stamping rule, which this spec does not restate.
  Owed because TWO paths in this unit's write set are `watch:` pathspecs of that manifest —
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, both verified on its `watch:`
  line at base — and check C5 of `skills/session-kickoff/manifest-check.sh`, `no unaudited watch
  drift`, is TOPOLOGICAL: it reds when the newest watch-touching commit is not an ancestor of the
  commit that changed the stamp, whatever the body delta. `last-body-change` does NOT move and §B
  gains no delta line: this unit changes no gate command, no entrypoint, no layout convention and no
  claim the manifest front-loads — it adds two conf keys and two branches inside a check the manifest
  already names — and the charter's rule is "no delta → no touch". Copied from
  `TOOL-aJoinedCanon-2`'s S10 because the reason is the write set's, not that sibling's. Observed by
  AC16.

## 3. Non-goals (OUT)

- **The semantic half is explicitly out.** A machine cannot tell that a well-formed answer is about
  the wrong QUESTION. `DEPL-dRetiredFork-3`'s ledger `AC3` cites `classify_outcome` while its spec
  `AC3` asks about an empty artifact, and under this unit's predicate that pair would still have to
  be caught by a token disagreement, not by understanding either sentence. The row that approaches
  this from the other side is `TOOL-aBoundedVerdict-32` in `memory/backlog/TOOL.md`, which
  records that nothing gates a criterion against the TREE at close time. Neither row subsumes the
  other and this unit does not close that one. (Cited by row id, not by line: the backlog is
  mutable and this build's own landing adds rows to it.)
- **No retrofit of any landed ledger.** `DEPL-dRetiredFork-3` is CLOSED and green and its ledger
  invents a label its spec never wrote; it stays as it is. The `ACCEPTANCE_LEDGER_GRANDFATHER`
  declaration in `.memory-tree.conf` states the
  position this unit obeys — back-filling another build's ledger is not this build's to do, because
  a build's own folder owns its own prose.
- **`ACCEPTANCE_LEDGER_CUTOFF` and `ACCEPTANCE_LEDGER_GRANDFATHER` are not touched.** The
  grandfather list is declared SHRINK-ONLY with a stated admission reason that no unit here meets,
  so a new arm buys its own cutoff key instead of a new exemption row.
- **Check 12's acceptance-witness arm is not touched.** That arm
  (the `acceptance bullets naming no backticked witness` branch under `SPEC_WITNESS_CUTOFF`) decides
  whether a criterion names anything at all. This unit
  never re-grades that: a criterion with no backticked token is silent here, not doubly red.
- **HYGIENE.md's numbered catalog is not renumbered.** It stops at item 22 while the shell
  implements 23; that is `TOOL-aScouredKit-22` in `memory/backlog/TOOL.md`, cited by row id for the
  same reason, and it is a different edit to the same file pair.
- **No new check number.** Both arms are `fail 23` branches on the existing check, so the kit
  README's check count does not move.

## 4. Design

### Data model

`alledger` — the `alledger=$(git ls-files` pipeline in
`tools/memory-tree/check-memory-hygiene.sh` — emits one space-separated `<unit> <label> <form>`
triple per ledger bullet, and its `form` classification reads the bullet's FIRST LINE only. `alsel`,
the `alsel=$(printf '%s\n' "$alspecs"` pipeline below it, emits `U\t<seq>\t<uid>` per graded spec and
`L\t<seq>\t<uid>\t<label>` per §6 label, and collects no token. Both gain one field. Every anchor
into this engine is cited by its own source text rather than by line number, because units 1, 3 and
4 all edit this file at a lower `order` and move every number in it.

| Producer | New field | Content |
|---|---|---|
| `alledger` | 4th, TAB-separated | the answer's backticked tokens, backtick-joined |
| `alsel` `L` row | 5th, TAB-separated | the criterion's backticked tokens, backtick-joined |
| `alsel` `U` row | 4th and 5th | `1`/`0` for the label era and the token era |

A backtick is the field separator inside a token list because the extractor is `` `[^`]+` `` and a
captured token therefore cannot contain one. The `U` row carries the era flags rather than the
filename date, so the date comparison stays in awk beside the one `alcut` already does and bash
reads booleans.

**The two new `-v` bindings, claimed here under the build README's one-owner rule.** The era flags
mean `alsel`'s awk has to be told both dates, so this unit adds exactly two names to that
invocation — `lcut` for `LEDGER_LABEL_CUTOFF` and `tcut` for `LEDGER_TOKEN_CUTOFF` — and the last
`-v` binding of a name wins silently, which is the mechanism that blocked round 3. Both were checked
against the two populations that rule names. That invocation is `alsel=$(printf '%s\n' "$alspecs" |
grep . | awk -v cut="$alcut"`, and the names bound on it today are `cut` and `grand` and nothing
else; neither `lcut` nor `tcut` appears anywhere in the engine as a standalone name (`grep 'lcut'`
returns only the four `alcut` substrings, `grep 'tcut'` returns nothing). Across the other ten specs
of this build, only units 3, 4 and 8 mention check 23 at all and all three do so to declare it OUT
of their scope, so no sibling binds a name on this awk. The claim is recorded HERE rather than in
`TOOL-aJoinedCanon-3`'s namespace registry for two reasons, and the second is a limitation, not a
convenience: that registry surveys check 12's awk invocation, whose taken set is a disjoint one, so a
name on this invocation cannot collide with anything it lists; and this fold edits one file, so the
registry entry itself is a follow-up the unit-3 folder owns, not something this document can land.
No new criterion is owed for the pair: AC6 already arms one key while blanking the other and
requires the armed arm to keep reding, which is the one observation a rebind cannot survive — under a
shared name, blanking either key would blank the binding and take BOTH arms dark, and AC6 reds. That
is the criterion round 3 found missing on units 1 and 4, and it happens to already be here.

Both new fields are BULLET-scoped, and on the ledger side that is a change of kind rather than an
extra capture: `alledger` prints on the line matching `^- *(\*\*)?AC[0-9]+` and classifies `form`
from that line alone, so the token list has to accumulate over the answer's continuation lines until
the next bullet, `**Evidences:**` block or heading. S3 declares both halves and AC4 grades both;
widening only the spec side is the shape that would pass every other criterion here.

The existing bash reader, the `declare -A ALFORM` loop, splits a triple with `${_al% *}` and
`${_al##* }`. It gains
a leading `IFS=$'\t' read -r _altriple _altok` and then splits `_altriple` exactly as today, so the
FIRST-WINS map semantics documented there are unchanged. A parallel `ALTOK` map is filled under the
same first-wins rule and the same key.

### The two arms

**Arm A, the ledger-side walk.** The `L` walk — the loop reading `_lt _lseq _luid _llab` — gains
`ALSPECLAB["$_alk"]=1`, and the
`U` walk gains `ALUID["$_uuid"]=$labera`. A new walk over `ALFORM`'s keys reports any key whose unit
is in `ALUID` with the flag set and whose full key is absent from `ALSPECLAB`. Bash associative-array
key order is unspecified, so the collected offenders are piped through `sort` before the failure
string is built — the existing arms get byte-stable output from a sorted input stream and this
one must earn it explicitly.

**Arm B, the token join.** Inside the existing `L` walk, when the key is present in `ALFORM` and the
unit's token era is on, the criterion's tokens and `ALTOK`'s tokens are compared. A pair passes when
either token contains the other after case folding, using `[[ $a == *"$b"* ]]`, which is a bash
builtin and forks nothing. An EMPTY list on either side makes the arm silent for that criterion:
an empty spec side is check 12's acceptance-witness arm, and an empty ledger side is already the
existing `albad` branch.

Containment rather than equality is a measured choice, not a softening. The corpus writes the same
subject two ways across the join — a criterion says `tools/govkit/selftest.py` and its answer says
`python tools/govkit/selftest.py`, or a criterion names a spec file by basename and its answer names
it by repo path. Exact set intersection calls all of those disagreements.

**Arm B sets `status=1`** — it reds, per §8's resolved FORK-1, and is not an advisory count. The
risk that carries is stated here rather than only in the fork: this arm can manufacture work on a
correct ledger and then get waived, which is the failure mode of every gate whose false-positive
rate outruns its authors' patience. The rate is not hypothetical. Containment fails 25.4% of the
gradeable corpus and 18.2% of the newest closed cohort, so on today's writing habits roughly one
answer in five would have to be re-worded. Two things answer it, and neither is optimism. The
cutoffs below put both arms AHEAD of the fleet, so the population an author meets is a population
they wrote after reading the rule, not one they wrote before it existed. And S6 puts the rule in the
ledger grammar, which is where the residual form — a ledger citing a self-test arm id where the
criterion named a file — becomes a notation an author follows rather than a red they have to argue
with. If the arm still manufactures work once real specs start meeting it, the honest response is a
blank `LEDGER_TOKEN_CUTOFF`, which is the rollback below, and not a waiver row.

### Where the arms sit, and what that dependency costs

Both arms are BRANCHES of check 23, inside the block opening on
`if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`. Two consequences, and neither is optional to write
down. A blank `ACCEPTANCE_LEDGER_CUTOFF` disarms both arms however their own keys are set, and
NOTHING announces it: the `pop_guard 23` call and the `memory-hygiene: check 23 measured NO unit`
printf are inside that same block, so the check is simply dark. And each arm's population is the
INTERSECTION of `alcut` and its own key, because `alsel` drops a spec whose filename date is below
`alcut` before either arm sees a row from it. With both new keys ahead of the fleet the intersection
is their own dates in THIS repo; the shape that bites is the adopter's, and it is the one
`tools/memory-tree/.memory-tree.conf.example` ships — `ACCEPTANCE_LEDGER_CUTOFF=""` beside a
`LEDGER_TOKEN_CUTOFF` the adopter has armed, giving an arm that never executes while its own key
reads as armed. `TOOL-aJoinedCanon-4` met this shape in check 12 and hoisted out of the guard; that
is not available here (Alternatives rejected, below). So it is declared in both conf comments (S9)
and observed by a fixture (AC15), which is the option unit 4 considered and rejected and this unit
is stuck with.

### Inventory

Reproduced at base 750ca0ca with a throwaway probe mirroring check 23's own selectors (filename date
at or after the cutoff, `**Status:**` in the first six raw lines, CLOSED, Tier-2, an acceptance
heading, an H1 id, minus `ACCEPTANCE_LEDGER_GRANDFATHER`). Population: 145 CLOSED Tier-2 units,
1,241 answers whose label the spec also numbers.

| Predicate | Failing answers | Rate | Units touched |
|---|---|---|---|
| Arm A — ledger label the spec never wrote | 1 | — | 1 of 145 |
| Arm B — exact token-set intersection | 487 | 39.2% | 136 of 145 |
| Arm B — case-folded bidirectional containment | 315 | 25.4% | 116 of 145 |

Finding 19 binds at **307 of 1,377 ledger answers, 22.3%**, and this table does not reproduce that
figure. The denominators differ: 1,377 counts every ledger answer, while 1,241 counts only those
whose label the spec also numbers, which is the set arm B can grade at all. Both are recorded rather
than reconciled, and the design is sized against the larger of them.

Arm A's single corpus-wide hit is `DEPL-dRetiredFork-3` `AC8`, and it is cited by LABEL rather than
by line because the two ranges this paragraph carried at rev-3 were both wrong at base — a defect
inside the very sentence that said "verified directly". Re-derive each set with
`grep -nE '^-? *(\*\*)?AC[0-9]+'` over the file rather than trusting a number here. The spec
`memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` numbers ELEVEN criteria in
its §6, `AC1`-`AC7` and `AC9`-`AC12`, skipping `AC8`. The ledger
`memory/builds/dRetiredFork/build/2026-09-03-build-DEPL-dRetiredFork-3-1-acceptance-ledger.md`
writes TWELVE answers, `AC1`-`AC12`, and its `- AC8 — MET — default-OFF` line is the orphan. The
findings record calls that answer a thirteenth; the file carries twelve.

### Migration

**BOTH keys ship strictly AFTER the newest spec filename date in the tree at landing** — the
build-wide ruling of 2026-09-05: this build's cutoffs sit ahead of the fleet, so no landed ledger
reds. The value is derived in the landing commit rather than pinned here, because a date typed into
a spec goes stale between writing and landing:

```bash
git ls-files 'memory/builds/*/spec/*.md' | sed 's#.*/##' | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}-' \
  | cut -c1-10 | sort | tail -1
```

The landing commit states the chosen value and its reason, per the cutoff discipline the other keys
in that file already follow.

For arm B no earlier value was ever available. Measured on the six-unit cohort dated 2026-09-04 or
later, containment still fails 8 of 44 answers (18.2%) across 5 of those 6 units, so even the newest
closed work does not satisfy this arm.

For arm A this is a CHANGE from rev-1, which pinned `LEDGER_LABEL_CUTOFF="2026-09-04"` on the
measurement that six CLOSED Tier-2 specs are already dated at or after that day and arm A reds NONE
of them — the one historical hit is dated 2026-09-02 and falls outside. That measurement still
stands and is why the predicate is known not to be wild; what changed is the conclusion drawn from
it. Rev-1 argued for the live, non-empty first population that `ACCEPTANCE_LEDGER_CUTOFF`'s own
comment in `.memory-tree.conf` calls for, in the words `a gate whose first run measures an empty set
is an assertion about nothing`. The owner's ruling overrides that shape here, and the cost is real
and worth naming: arm A's first run on the real tree measures nothing, which is exactly what that
comment warns against. Two things keep it from being one. The empty population ANNOUNCES itself
per S5, so the zero is a stated measurement and not a silent green (AC7). And the observed red both
arms owe is earned in the fixtures per S7, in `check-memory-hygiene.test.sh`, which is where a
forward-cutoff arm can earn it at all.

The residual failures under containment are dominated by one legitimate answer form the predicate
cannot recognise: the ledger cites a self-test ARM ID such as `[-ST4]` where the criterion named the
file the arm lives in. That is a real answer, and it is why S6 puts the rule in the ledger grammar
where an author reads it — the fix is a notation the writer follows, not a predicate that guesses.

### Rollout

Arm A and arm B land in one commit, both setting `status=1` on a hit, and both dark over every
landed ledger because both cutoffs sit ahead of the fleet. Under rev-1 the two keys held DIFFERENT dates and that
difference was the rollout; under the 2026-09-05 ruling they land at the same derived value, so what
separates them is no longer their dates but their independent disarm. A blank value in either key
turns that arm off entirely without touching the other, which is the rollback: one conf edit, no
code revert. Two keys therefore still earn their place — they let arm B be withdrawn on a
false-positive rate while arm A, whose corpus-wide hit count is 1, stays armed.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | two awk emitters, the `-v lcut=` and `-v tcut=` bindings on `alsel`'s invocation, two bash walks, two `fail 23` branches, two announce lines, the two blank presets, and `KIT_MEMORY_TREE_VERSION` advanced by one minor |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixtures for both arms plus their `hit` assertions; the fixture conf the harness printf-writes gains both keys |
| `.memory-tree.conf` | two keys with their reasons, each comment naming S9's `ACCEPTANCE_LEDGER_CUTOFF` dependency |
| `tools/memory-tree/.memory-tree.conf.example` | the same two keys, blank, with the same dependency in each comment (AC13) |
| `memory/HYGIENE.md` | the token rule under `## Acceptance ledger` |
| `tools/memory-tree/HYGIENE.template.md` | the same bytes — `tools/memory-tree/kit-dogfood-parity.test.sh` compares the pair |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp only; no body delta and `last-body-change` unmoved (S10) |

The commit also owes the `gov:kit memory-tree@` bump in every carrier, because both arms change what
the engine verdicts and `verdict epoch (kit version dates the engine)` reads that constant's newest
commit against the engine's. Derive the carrier set at build time with
`grep -rl 'gov:kit memory-tree@'` and take no count from this spec — `TOOL-dSettledRoster-4` records
a remediation message naming three carriers when more existed.

### Alternatives rejected

- **One cutoff key for both arms.** REASON REPLACED at rev-2. Rev-1 rejected it because it forced
  the free arm to wait for the expensive one — arm A was landable against a live population and arm
  B was not landable against any date in the corpus. The 2026-09-05 ruling puts both cutoffs ahead
  of the fleet, so both arms now land against an empty first population and that reason is dead. Two
  keys survive on the reason stated under Rollout, which the ruling does not touch: independent
  disarm, so arm B can be withdrawn on a false-positive rate without taking arm A with it.
- **Add `DEPL-dRetiredFork-3` to `ACCEPTANCE_LEDGER_GRANDFATHER` and land arm A at the existing
  cutoff.** MOOT at rev-2, and kept because it records a real option. A cutoff ahead of the fleet
  never grades that unit at all, so no exemption is needed for it. Had arm A landed at the existing
  cutoff, this was still the wrong instrument: that list exempts a unit from ALL of check 23, so it
  would have traded one new finding for three existing ones, and its own declaration restricts
  admissions to units that closed while the grammar was unmerged, which this is not.
- **Fix the `DEPL-dRetiredFork-3` ledger line instead.** Ruled out by the position recorded beside
  the grandfather list: a build's own folder owns its own prose.
- **Hoisting both arms out of check 23's `alcut` guard**, the way `TOOL-aJoinedCanon-4` hoists its
  accumulator out of the witness guard. NOT AVAILABLE, rather than rejected on taste: the `ALFORM`
  ledger map, the graded unit set and the label rows exist only inside that block, so a hoist is a
  rebuild of check 23's whole pipeline and not an unindent. Declaring the dependency and observing
  it (S9, AC15) is the second-best answer and is named as such rather than presented as equivalent.
- **Exact token-set equality.** Measured at 39.2% against containment's 25.4%, and the extra 172
  answers are dominated by path-prefix and invocation-prefix variance rather than by disagreement.
- **A third form in the ledger grammar for "no shared token, and here is why".** It re-introduces
  the escape hatch `memory/HYGIENE.md` deliberately refuses in its `TWO forms and no third` rule,
  where a third form turns the ledger into a checkbox exercise.

## 5. Production-readiness checklist

- security — N/A. Both arms read tracked records already in the working tree and write nothing.
- perf / scale — no new process is spawned. Both awks gain fields on lines they already emit, and
  arm B's comparison is a bash builtin inside a loop that already runs. The wall-clock delta is
  UNVERIFIED and AC11 measures it, by recording the leg's elapsed row beside the pre-change one.
  Note when reading history here: check 23's 962.0 s figure measures the implementation
  `TOOL-aCollapsedScan-13` retired, and that record says so.
- a11y — N/A. A shell gate has no user interface.
- i18n — N/A, with one real constraint: case folding must not be locale-sensitive, so the comparison
  stays ASCII and the surrounding code sets no `LC_ALL`, matching the deliberate choice the
  `No LC_ALL` comment above the existing label sort already records.
- error / empty / loading states — an empty population per arm announces itself, which is S5. The one
  case that CANNOT announce is S9's: with `ACCEPTANCE_LEDGER_CUTOFF` blank the whole check is dark,
  announce line included, so the dependency is carried by the conf comments and AC15 instead.
- observability — each failure names the unit and the label, in the shape the existing `fail 23`
  branches use.
- risks — arm B reds (§8 FORK-1, resolved 2026-09-05), so its false-positive rate against future
  authors is now a property of the shipped gate rather than an open question. Stated plainly: 25.4%
  of the gradeable corpus and 18.2% of the newest closed cohort fail containment, and a gate that
  manufactures work on correct ledgers gets waived. What holds it down is §4's pair — a cutoff ahead
  of the fleet, so nobody meets the rule retroactively, and S6's grammar note, so the one legitimate
  form the predicate cannot recognise has a notation. There is no data-loss or rollback hazard: a
  blank cutoff disarms either arm.
- testing + left-shift gates — the harness meta-gate makes this mandatory rather than optional. Every
  `fail` branch must be ARMED by a positive assertion in `check-memory-hygiene.test.sh` naming a
  literal slice of its own failure text, or be listed in `memory/project/unarmed-branches.txt`; neither new
  branch will be listed there.
- migration / rollback — two dated cutoffs, per §4 Migration. Rollback is a conf edit.
- user docs — the ledger grammar in the `HYGIENE` pair is the doc, and it is S6, graded for content
  by AC14 and not by the pair byte-compare. The shipped example conf's two comments are the other
  adopter-facing half, and they are graded by AC13.

## 6. Acceptance criteria

- **AC1** — When a fixture ledger evidences a graded unit with a label its spec never numbers, `bash
  tools/memory-tree/check-memory-hygiene.sh` reds naming that unit and that label; removing the
  fixture line returns the run to green.
- **AC2** — When a fixture criterion names `` `alpha` `` and its ledger answer names only
  `` `beta` ``, `bash tools/memory-tree/check-memory-hygiene.sh` reds naming that pair.
- **AC3** — When that same fixture answer names `` `python alpha --write` ``, the run is green,
  because containment matches where exact intersection would not.
- **AC4** — When a fixture criterion's only backticked token sits on a CONTINUATION line rather than
  the bullet head, the run is green; the same fixture with the token deleted reds. The MIRROR case is
  graded too, on the ledger side: a fixture whose ANSWER carries its only backticked token on a
  continuation line is green, and reds with that token deleted. Both halves together are S3's
  bullet-scope assertion, and both would silently pass if the token capture stayed line-scoped the
  way `alledger`'s existing `form` classification is. Grading only the spec half is the fold that
  builds half of S3 and reads as covered.
- **AC5** — When `LEDGER_LABEL_CUTOFF` is set past a fixture spec's filename date, that spec's
  orphan ledger label stops being reported and the rest of check 23's verdict on it is unchanged.
- **AC6** — When a fixture conf blanks one new key and arms the other, the blanked arm's own red
  fixture goes GREEN while the armed arm's still reds, and restoring the key reds it again. The
  observation lives in `check-memory-hygiene.test.sh` and NOT over the real tree: with both cutoffs
  ahead of the fleet a whole-tree run is green whether either key is blank or set, so a real-tree
  green cannot fail for the reason this criterion gives and is not what grades the disarm. Stated
  because rev-3's AC6 claimed exactly that green as its proof.
- **AC7** — When every graded spec predates an arm's cutoff, that arm prints its own
  `measured NO unit` announce line, in the shape of the engine's existing
  `memory-hygiene: check 23 measured NO unit` printf. Since the
  2026-09-05 ruling puts both cutoffs ahead of the fleet, this is not a fixture-only case: it is
  what BOTH arms print on the real tree in the landing commit, and it is the only thing standing
  between an empty first population and a silent green.
- **AC8** — When the token rule lands in `memory/HYGIENE.md`, `bash
  tools/memory-tree/kit-dogfood-parity.test.sh` is green, proving ONLY that
  `tools/memory-tree/HYGIENE.template.md` carries the same bytes: landing the rule in one half reds
  it, and landing it in NEITHER half leaves it green. What the two halves say is AC14's job, and
  this criterion makes no claim about it.
- **AC9** — When `python3 tools/memory-tree/check-arms.py --check` runs, both new `fail 23` branches
  are ARMED, and neither appears in `memory/project/unarmed-branches.txt`.
- **AC10** — When `LEDGER_TOKEN_CUTOFF` is temporarily set to `ACCEPTANCE_LEDGER_CUTOFF`'s value and
  `bash tools/memory-tree/check-memory-hygiene.sh` is run, the run EXITS NON-ZERO — arm B sets
  `status=1` per §8 — and the offender count derived from that run's own `fail 23` line is written
  into this unit's build record beside §4's 315-of-1,241 probe figure. Both halves are observations
  and neither is a threshold: this criterion passes on a non-zero exit plus a recorded pair, and it
  states no tolerance, because a band nobody derived is graded by whoever runs it. The two figures
  are for a reader to compare and for §4's table to be re-derived from the landed arm rather than
  from a probe that is not committed; a gap between them is a finding to write down, not a silent
  pass. A GREEN run under that temporary value falsifies the arm outright. The temporary value is
  reverted in the same session, and no commit carries it: the ruling that no landed ledger reds is
  about what ships, and this is a measurement.
- **AC11** — When the whole bar runs, `bash tools/run-gates/run-gates.sh` is green with
  `memory hygiene` and `memory-hygiene self-test` among its legs, and the elapsed row for
  `memory hygiene` in `<git-dir>/gate-ledger.tsv` is recorded beside the pre-change one.
- **AC12** — When the landing commit is HEAD, `bash tools/check-kit-versions.sh` and
  `bash tools/memory-tree/check-verdict-epoch.sh` both exit 0: `KIT_MEMORY_TREE_VERSION` advanced by
  one minor in this same commit and every carrier the build-time
  `grep -rl 'gov:kit memory-tree@'` returns moved with it. Landing the two `fail 23` branches with
  the constant untouched reds `verdict epoch (kit version dates the engine)`, which is the failure
  this criterion exists to make impossible to reach at the push boundary.
- **AC13** — When `grep -qE '^LEDGER_LABEL_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` and
  the same grep for `LEDGER_TOKEN_CUTOFF` both succeed with a blank value, and
  `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0, the shipped example declares both
  keys. Deleting either row reds that self-test at its example-conf parity arm naming the missing
  key, which is how the arm reports that an adopter cannot discover it. A second half, because the
  parity arm grades the DECLARATION and never the comment beside it: the comment block introducing
  each new key — the contiguous `#` lines above its own `KEY=` row, which do not exist before this
  edit — names `ACCEPTANCE_LEDGER_CUTOFF` as the switch that disarms that arm regardless (S9). That
  half runs over BOTH confs, because S4 declares the comment in both and the shipped example is only
  the adopter's copy: the gov `.memory-tree.conf` is what a session on THIS repo reads when it wonders
  why a valued `LEDGER_TOKEN_CUTOFF` grades nothing, which is the confusion S9 exists to prevent.
  Four observations, then, one per (conf, key):

  ```bash
  awk '/^LEDGER_TOKEN_CUTOFF=/{printf "%s", b; exit} /^#/{b = b $0 "\n"; next} {b=""}' <conf> \
    | grep -c ACCEPTANCE_LEDGER_CUTOFF
  ```

  non-zero for each, and the same with `LEDGER_LABEL_CUTOFF`, against `.memory-tree.conf` and
  `tools/memory-tree/.memory-tree.conf.example`. A whole-file grep will not do in EITHER conf, since
  both already declare `ACCEPTANCE_LEDGER_CUTOFF` elsewhere — verified at base, where it sits at its
  own comment block and row in each. The extractor was RUN at base against that existing key in both
  files and returns the contiguous block above it, so the predicate is known to select what this
  criterion says it selects rather than to be plausible prose. The break: delete the
  `ACCEPTANCE_LEDGER_CUTOFF` sentence from any one of the four blocks and that block's grep returns
  0 while the key's own declaration still stands, which is the exact state — armed key, undocumented
  dependency — this half exists to catch. Nothing on the bar grades it in either conf; it is a read
  of the landing diff, stated as one rather than left as a claim S4 makes and no criterion covers.
  Without it, the sentence a reader needs most is the one nothing observes.
- **AC14** — When the token rule lands under `memory/HYGIENE.md`'s
  `## Acceptance ledger — how a built unit evidences its criteria` heading, that section states that
  an answer shares a backticked token with the criterion it evidences and NAMES the key that
  enforces it, so `grep -c 'LEDGER_TOKEN_CUTOFF' memory/HYGIENE.md` returns non-zero against the
  count of 0 that same grep returns at base. The key name is the anchor deliberately: the phrase
  `backticked token` is already in that section once, so grepping the concept would pass without the
  rule. This is S6's CONTENT half. AC8 proves only that the two halves of the
  pair moved together and is equally green when the rule reached NEITHER, and S6 is the one named
  mitigation for arm B's measured 25.4% containment failure — shipping it graded by a sameness
  compare would leave the answer to that rate resting on a check that cannot fail.
- **AC15** — When a fixture tree's conf arms `LEDGER_LABEL_CUTOFF` and leaves
  `ACCEPTANCE_LEDGER_CUTOFF` BLANK, the orphan-label fixture does not red and check 23 prints
  nothing at all; setting `ACCEPTANCE_LEDGER_CUTOFF` in that same tree reds it. That is S9's nesting,
  observed rather than assumed, and the blank-`ACCEPTANCE_LEDGER_CUTOFF` shape is what
  `tools/memory-tree/.memory-tree.conf.example` ships to every adopter.
- **AC16** — When `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit it
  exits 0, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` names a sha at or after the commit
  that edits `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`. The failing case is
  the revert of S10 alone: keep both engine edits, restore the old stamp, and check C5 —
  `no unaudited watch drift` — reds with `watched files changed since last-audit with no re-stamp
  at/after the change` and lists both paths. `last-body-change` is the SAME sha before and after,
  which is the half that observes the "no delta → no touch" side rather than the re-stamp side.

## 7. Gates

- `memory hygiene` — `bash tools/memory-tree/check-memory-hygiene.sh`, unguarded, and the leg both
  arms live on and will eventually red on. Check 23 is HELD under `--staged` — the engine prints
  `check 23 HELD under --staged` and skips the whole block — so these arms bind at the push boundary
  and never in pre-commit.
  On the landing commit itself this leg CANNOT red on either arm: both cutoffs sit ahead of the
  fleet per §4, so what it prints is the empty-population announce (AC7). It starts grading real
  work with the first spec dated past the cutoff. In a tree whose `ACCEPTANCE_LEDGER_CUTOFF` is
  blank this leg runs green with BOTH arms dark and nothing printed, because they are branches of
  check 23 and not checks of their own — S9, observed by AC15.
- `memory-hygiene self-test` — `bash tools/memory-tree/check-memory-hygiene.test.sh`, guarded on
  `tools/memory-tree/`, which this unit edits. Under the forward cutoffs this is where both arms'
  observed red is EARNED — the fixtures of S7, not the corpus. It also carries the example-conf
  parity arm, which reds on a new engine `*_CUTOFF` the shipped example does not declare; that is
  what S4's second declaration answers (AC13). It is also where the two blank-key fixtures of AC6
  and the nested-disarm fixture of AC15 live, since neither can be observed over the real tree.
- `kit/dogfood doc parity` — `bash tools/memory-tree/kit-dogfood-parity.test.sh`, the byte-compare
  that makes the `HYGIENE` pair move together. It is a SAMENESS leg and grades no content: what the
  pair says is AC14's grep, and this leg is green over two halves that never received the rule.
- `harness arms (fail branches armed or pinned)` — `python3 tools/memory-tree/check-arms.py --check`,
  unguarded, and the leg that refuses an unarmed new `fail` branch.
- `check-arms selftest` — `python3 tools/memory-tree/check-arms.py --selftest`.
- `verdict epoch (kit version dates the engine)` — `bash tools/memory-tree/check-verdict-epoch.sh`,
  unguarded, and the leg this unit's landing commit trips if S8 is skipped. It sets
  `ENGINE=tools/memory-tree/check-memory-hygiene.sh` and requires the newest commit moving a
  behaviour-bearing engine line to be an ancestor of, or equal to, the newest commit that changes
  `KIT_MEMORY_TREE_VERSION`. Two new `fail 23` branches are behaviour-bearing by definition, so this
  leg is owed by the change itself and not by the file being touched. Observed by AC12.
- `kit version markers` — `bash tools/check-kit-versions.sh`, unguarded, and the leg that reds if
  the constant advances and a `gov:kit memory-tree@` carrier is left behind. Observed by AC12.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`, `subject = repo`
  with no guard in `tools/gate-legs.json`, so it runs on every bar. It is on this list because
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf` are both `watch:` pathspecs of
  the manifest S10 re-stamps; see AC16 for the observed red. Its check C5 is topological, so a
  landing that skips the re-stamp reds this leg on its own commit however small the engine delta is.
- No new leg. Both arms live inside a check that already has one, and both legs above already exist
  and already run on every bar.

## 8. Open questions

- **FORK-1 · Does arm B red, or does it only report?** The measured failure rate is 25.4% corpus-wide
  and 18.2% on the newest closed cohort, both under the most forgiving cheap predicate, and the
  residual is dominated by one legitimate answer form — a ledger citing a self-test arm id where the
  criterion named a file. A forward cutoff means no landed work reds either way, so the question is
  purely what future authors face.

  Option A, red. The rule becomes real, and the notation it demands is one an author can follow once
  it is written in the ledger grammar. The risk is a gate that manufactures work on correct ledgers
  and gets waived.

  Option B, advisory. The arm prints a count and a list and never sets `status=1`, for one release,
  and the count decides whether option A is safe. The risk is a printed number nobody reads, which
  is this repo's own named class.

  **Recommendation: A.** An advisory arm has no failing case to observe, so it cannot satisfy the
  build rule that a new arm owes an observed red, and a check that cannot fail is the shape §7 of
  the charter refuses outright.

  RESOLVED (owner, 2026-09-05): option A — arm B REDS. It sets `status=1` like every other `fail 23`
  branch, on the recommendation's own reasoning: an advisory arm has no failing case to observe, so
  it could not satisfy this build's rule that a new arm owes an observed red, and a check that
  cannot fail is the shape charter §7 refuses. Option B, the advisory release, loses; its text stays
  above as the record of what was considered. The risk named against the recommendation stands and
  is not waved away — it moves into §4 and §5 as a body claim rather than living only here.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §4 Design/Migration/Rollout/Alternatives rejected · §5 · §6 AC7, AC10 ·
  §7 · header status line · folded the owner's ruling on FORK-1: arm B REDS, and the risk it carries
  moved out of the fork into §4 and §5. Applied the build-wide ruling that this build's cutoffs sit
  ahead of the fleet, which moved `LEDGER_LABEL_CUTOFF` off rev-1's pinned `2026-09-04` onto arm B's
  derived-at-landing value, emptied both arms' first population, killed the population reason under
  the rejected one-key alternative, made the grandfather alternative moot, and moved the observed
  red from the corpus to the S7 fixtures. Header gains `ratified 2026-09-05`; §8 holds no open fork.
- rev-3 · 2026-09-05 · §2 S4/S5/S7 · §2 S8 new · §3 · §4 Design/Migration/Files touched/Alternatives
  rejected · §5 · §6 AC10 · §6 AC12, AC13 new · §7 · header status line · folded spec-audit round 1:
  H4 — the two ENGINE arms now carry their kit-version obligation, as S8 (the constant plus every
  `gov:kit memory-tree@` carrier, the set derived with `grep -rl` and never counted), a Files-touched
  row and paragraph, `verdict epoch (kit version dates the engine)` and `kit version markers` in §7,
  and AC12 observing both legs. H8 — AC10's unstated "tolerance" is gone; it now grades a non-zero
  exit plus the offender count recorded beside §4's 315-of-1,241 probe figure, and §5's perf row
  stops citing AC10 for a wall-clock measurement AC11 makes. The build README's cutoff rule brought
  H3's fix with it: S4 and Files touched now name `tools/memory-tree/.memory-tree.conf.example`,
  shipped blank, observed by AC13. The README's citation rule moved every anchor into
  `check-memory-hygiene.sh`, `.memory-tree.conf` and `memory/HYGIENE.md` off line numbers and onto
  source text, since units 1, 3 and 4 move all three first; S7 now takes its fixture ids from the
  README's `tFixture` allocation instead of the file's high-water.
- rev-4 · 2026-09-05 · header status line · §2 S3, S4, S6, S7 · §2 S9 new · §3 both backlog
  citations · §4 Data model, Where the arms sit (NEW), Inventory, Files touched, Alternatives
  rejected · §5 error/empty, observability, user docs · §6 AC4, AC6, AC7, AC13 · §6 AC14, AC15 new ·
  §7 three bullets · §10 · folded spec-audit round 2 and swept all 23 of its classes over this spec.
  Named findings: H5 — S6's content now has AC14, which greps `memory/HYGIENE.md` for
  `LEDGER_TOKEN_CUTOFF` against the 0 that grep returns at base, and AC8 is restated in §6, §7 and
  S6 as the sameness compare it is. The key name is the anchor because `backticked token` already
  appears in that section, so the obvious grep would have passed with the rule absent. H9 — all three
  line pins are gone: AC7 now cites the `memory-hygiene: check 23 measured NO unit` printf by its
  text, and §10 cites `declare -A ALFORM` and the `read -r _lt _lseq _luid _llab` walk. This entry
  claims no conversion the document does not carry: `grep -nE '[a-z-]+\.(sh|md|py):[0-9]'` over this
  file returns nothing.
  Swept classes that HIT and what closed them. B1 — both arms are branches of check 23 inside
  `if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`, so a blank `ACCEPTANCE_LEDGER_CUTOFF` disarms
  them silently and their population is an intersection; that is now S9, a §4 subsection, both conf
  comments, AC13's second half, AC15, a §7 clause and a rejected-hoist alternative. M7 — rev-3's AC6
  proved a disarm with a whole-tree green that is green either way under a forward cutoff; AC6 now
  observes the blank key in the fixture suite and says why the real-tree run is not the observation.
  M10 — S3 declared bullet scope on BOTH sides while AC4 graded only the spec side; AC4 gains the
  ledger half and §4's Data model says the `alledger` emitter is widened, not just extended. M6 —
  the shipped example's two comments are adopter documentation and had no observer; AC13 grades
  them. M1 and L2 — §4's two `dRetiredFork` line ranges were both WRONG at base inside a sentence
  claiming direct verification, and are replaced by label-level citation plus the re-derivation
  command. L1 — two counts of populations this spec does not own (`the three existing arms`, `the
  three existing fail 23 branches`) are dropped; both were correct at base and neither is worth
  carrying.
  Swept classes checked and ABSENT here, each by re-running its own predicate: H1 and M4 (the
  version-bump obligation is scoped at S8, tabled in Files touched, in §7 as `verdict epoch (kit
  version dates the engine)` and `kit version markers`, and observed by AC12 — every §7 entry
  verified as a `name` in `tools/gate-legs.json`, and its unguarded/guarded claims verified against
  that manifest). H2 and H3 (S6 was the only scope item resting on a parity compare; H5 closed it).
  H4 (every scope item S1-S9 carries an `Observed by` tag). H6 (`check-arms.py --check`,
  `--selftest`, `--report` are real modes; `kit-dogfood-parity.test.sh` really pairs
  `memory/HYGIENE.md` with `HYGIENE.template.md`; the `--staged` HELD line and the announce printf
  exist verbatim; all four scripts named in §6 exist). H7 (AC13's claimed red was verified against
  the suite's example-conf parity arm, which derives bare `*_CUTOFF` presets AND `${NAME:-}` reads
  from the engine and reds naming the missing key). H8 (no criterion here grades a retrieval or
  selection result). H10 and M5 (§3's acceptance-witness parenthetical survives unit 4's hoist —
  that hoist moves the accumulator and leaves the witness test on its own boolean, verified in unit
  4's S3 and §3; no other argument here rests on a shape a lower-`order` sibling restructures). M2
  and M3 (no line pin into the template pair or `HYGIENE.md` remained after H9's conversion; the two
  backlog pins were correct at base and were dropped anyway, since the backlog is mutable and this
  build's own landing adds rows). M8 (this unit prescribes no header or contract sentence about its
  own file). M9 (the only sibling claim made here is that units 1, 3 and 4 edit the engine first,
  re-verified against their specs; unit 5 was checked and adds no arm and no cutoff).
- rev-5 · 2026-09-05 · header status line · §2 S10 new · §4 Data model, Files touched · §6 AC13 ·
  §6 AC16 new · §7 one bullet · folded spec-audit round 3, the TERMINATING fold — there is no round
  4, so both findings are disposed here and nothing is parked. H2 — two paths in this unit's write
  set, `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, are `watch:` pathspecs of
  `memory/guides/SESSION-KICKOFF.md`, verified on its `watch:` line at base, and the `last-audit`
  re-stamp they oblige was carried by no scope item, no Files-touched row, no criterion and no leg.
  Added as S10, a table row, AC16 naming check C5's own failure text as the observed red, and the
  `kickoff-manifest ratchet` leg — verified in `tools/gate-legs.json` as `subject: repo` with no
  guard, so it runs on every bar and this landing would have red it. M7 — S4's "in BOTH confs" half
  was observed in one conf only, because AC13 was scoped to the shipped example. AC13's second half
  now runs four observations, one per (conf, key), over a contiguous-comment-block extractor that was
  RUN at base against the existing `ACCEPTANCE_LEDGER_CUTOFF` block in both files and returns that
  block, and it states its own break. S4 is unchanged: the review offered narrowing it as the
  alternative and the write set already declares both confs, so widening the observer is the fix that
  keeps the two agreeing.
  The build README's one-owner rule fired where no finding pointed. §4 required the cutoff comparison
  to happen in awk and named no `-v` binding at all, which is the state that produced round 3's
  blocker one invocation over. This unit's bindings sit on check 23's `alsel` awk, whose taken names
  are `cut` and `grand`; `lcut` and `tcut` are claimed in §4 and were checked against the engine
  (`lcut` matches only the four `alcut` substrings, `tcut` matches nothing) and against the other ten
  specs, of which only units 3, 4 and 8 mention check 23 and all three place it outside their scope.
  No new criterion was needed: AC6 already blanks one key while arming the other, which no shared
  binding survives.
  NOT FIXED HERE, and it goes to the `TOOL-aJoinedCanon-3` folder rather than to a later round: the
  namespace registry in that unit's §4 lists `mcut` and `jcut` and does not list `lcut` or `tcut`.
  This fold edits one file and cannot add the entry. The claim above is the record until it does, and
  the two names cannot collide with anything that registry holds, since it surveys check 12's
  invocation and this unit binds on check 23's.

## 10. Reuse audit

No existing seam fits, and the probe says why. `python tools/codebase-map/reuse_lookup.py "join a
ledger answer to the acceptance criterion it answers"` over 645 symbols and 19 affordance seams
returns no join helper: its ranked hits are `join_aliases` in `tools/memory-recall/extract.py`
(fan-in 1, an alias-table builder), `joinCall` and `scanJoinFindings` in `tools/hooks/agent-cap.js`
(fan-in 0, both about the fan-out cap), and `signal_ledger` in
`tools/drift-audit/drift_report.py` (fan-in 0, a drift signal and not this ledger). Nothing in the
corpus compares two token sets across a document join. The seam this unit extends is therefore
check 23's own, already built and named in §4: in `tools/memory-tree/check-memory-hygiene.sh`, the
map declared at `declare -A ALFORM` and the label walk opening on
`read -r _lt _lseq _luid _llab` (its `IFS` is a literal tab, so grep the variable list), both of which
gain fields rather than callers. Cited by source text and not by line, because three lower-`order`
units insert into this file first — the rule §4 states and rev-3 left unapplied in this section. The recall query surfaced two rows worth reading before building,
and both are in §3: `TOOL-aBoundedVerdict-32` and `TOOL-aScouredKit-22`.

Recall terms used: `acceptance ledger criterion label join hygiene check 23 backticked token
OBSERVED AMENDED cutoff grandfather shape coverage`

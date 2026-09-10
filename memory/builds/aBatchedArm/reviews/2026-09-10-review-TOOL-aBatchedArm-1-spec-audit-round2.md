**Serves:** spec-audit TOOL-aBatchedArm-1 TOOL-aBatchedArm-2

# Tier-2 spec audit — TOOL-aBatchedArm-1 (fold) and TOOL-aBatchedArm-2 (new), ROUND 2

*Adversarial pre-code pass over both units this build now declares. Node `a`, 2026-09-10, ROUND 2.
Every finding below survived a skeptic prompted to REFUTE it. Each carries its address inside the
spec, the fix, and the gate that would have caught it before a reviewer had to.*

**Reviewed subjects, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md`@`8e8b662a744a92e317fcddf7b02f29d5f104826d` — rev-2, the FOLD of round 1's six confirmed findings.
- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-2.md`@`1e4ac1796fe37b7f09cce8ccb802d4d837e3f7c6` — rev-1, NEW, never reviewed.

Both pins were re-hashed against the working tree at review time and both match. Round 1's six
confirmed findings are not re-reported; unit 1 is graded on where the fold is WRONG or INCOMPLETE.

## Verdict: BLOCKED

Thirteen rows at BLOCKER, seven at HIGH, two at MEDIUM. Those 22 rows collapse to **eleven distinct
defects**, six of them blocker-class, and the table below names which rows share one defect — read
the tally as rows, not as holes. Six of the eleven are in unit 2, which has never been reviewed
before and is not a light unit: it is the merge-bar leg five of round 1's six findings were
left-shifted onto, and as specified it cannot be implemented, because its three rules carry two
definitions each, no verdict for their unresolved population, and a parse of the file that is wrong
about where a group starts.

The fold's failure has one shape and it is worth stating once. Round 1 said the safety argument was
blind to the 101 `miss` controls. Rev-2 answers with three new mechanisms — the admissibility rule
in §4, S3's exclusion list, and AC3's FAIL-set-plus-`n` oracle — and **all three key on an identifier
that is not unique**, then reason as though it were:

- The admissibility rule keys on the check NUMBER. Measured over `tools/unattended/check-unattended.sh` at BASE: **178 fail branches over 29 check numbers**, only six numbers (5, 6, 11, 21, 29, 31) carrying a single branch, check 16 carrying 34 and check 28 carrying 31. So "check N fired" does not mean "the control's branch ran" for 23 of 29 numbers.
- AC3 keys on the assertion TEXT. Measured over `tools/unattended/check-unattended.test.sh` at BASE: 377 arm lines, **314 distinct (helper, text) pairs, 38 duplicated pairs covering 101 arms** (20 `hit` pairs over 46 arms, 18 `miss` pairs over 55 arms, 0 `same`). The FAIL line IS the text, so those 101 arms are mutually indistinguishable in the oracle.
- Unit 2's rule A keys on a text→check JOIN that resolves 5 of 101 `miss` arms in the direction it borrows, and 0 of 27 `same` arms in either direction.

That is one defect class wearing three hats: a many-to-one key used as a one-to-one key. Every
blocker below is a consequence of it except D2 and D4, which are the same coverage gap round 1
already flagged, in a different place.

One coincidence to disarm before it misleads: the 101 duplicate-text-covered arms and the 101 `miss`
control arms are two different populations that happen to have the same cardinality. They are not
the same set and no argument below treats them as one.

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **5/5 returned, 0 DIED.**
- 0 contradictory verdicts demoted to unverified; 0 spurious verdicts discarded; 0 duplicates removed.
- Unverified (no usable skeptic verdict): **0.** There are no OUTSTANDING findings carried into this record.

Every lens and every skeptic batch returned, so no zero reported here is a zero-by-absence and the
finding set is complete for the lenses run. This run is complete on all six integrity counts.

## Review shape

| Metric | Value |
|---|---|
| Raw findings | 42 |
| Confirmed | 22 |
| Refuted | 20 |
| Unverified | 0 |
| Precision | 0.52 |

Precision sits just above the 0.5 floor §8 sets for tightening scope before adding agents, which is
where a two-subject round with one unreviewed subject should sit. No retune indicated.

## What this reviewer re-measured, and one correction

Five load-bearing figures were re-derived at BASE on node `a` rather than transcribed, because
several incoming findings disagreed with each other about them:

| Claim | Measured here | Verdict |
|---|---|---|
| Arm population | 249 `hit` + 101 `miss` + 27 `same` = 377 | matches the mandate |
| Duplicate (helper, text) pairs | 38 pairs over 101 arms; 20 `hit` pairs / 46 arms, 18 `miss` pairs / 55 arms, 0 `same` | id 21's impact figure is right |
| Fail branches | 178 over 29 check numbers; 6 single-branch numbers; check 16 at 34, check 28 at 31 | matches id 31 exactly |
| `gate-legs.json` | 104 legs, 56 `subject = repo`, 48 `subject = kit`; all five unattended rows `repo` | matches id 36 |
| The four-arm text | `a run-state file's generated markers are malformed` at :467, :984, :1310, :1313 as `hit`, plus :473 as a `miss` | matches, and is worse than reported |

**Correction to the confirmed set.** Finding 21's `why-real` states 42 duplicated pairs covering 125
arms including 4 `same`. That does not reproduce: the measurement here is 38 pairs over 101 arms with
**zero** duplicated `same` labels, and the reason is mechanical — `same()` at
`tools/unattended/check-unattended.test.sh:59` prints `FAIL $1: expected [$3], got [$2]`, so its FAIL
line carries the human label, which `hit` and `miss` do not. The blind population is therefore the
`hit`/`miss` arms, not all 377. This makes finding 21's conclusion *narrower and more certain*, not
weaker: 101 arms are provably indistinguishable in AC3's oracle and `same` arms are not. Findings 1,
10, 21 and 33 are all graded on the reproduced figure.

**One instance the incoming set understated.** The four-`hit` text at :467/:984/:1310/:1313 is also
carried by a `miss` at :473. `hit` prints `FAIL missing:` and `miss` prints `FAIL unexpected:`, so
that pair is distinguishable by prefix — but it means a single text spans both an assertion and its
own negation across five arms in three tree groups, which is the sharpest available demonstration
that the text is not an arm identity.

## Findings

Severity is this reviewer's adjudication. It agrees with the incoming grade on all 22 rows: each row
is independently reproducible at its own address, so each is reported at the severity its own
evidence carries. Where a row is a marginal restatement of a defect already graded higher, the row's
severity reflects only what it *adds* and the `Defect` column says which cluster owns the real
severity.

| # | Sev | Defect | Unit | Address |
|---|---|---|---|---|
| 1 | BLOCKER | D1 | 1 | §6 AC3 |
| 10 | BLOCKER | D1 | 1 | §6 AC3 |
| 21 | BLOCKER | D1 | 1 | §6 AC3 |
| 33 | BLOCKER | D1 | 1 | §6 AC3 |
| 2 | BLOCKER | D2 | 1 | §2 S1 vs §6 |
| 9 | BLOCKER | D3 | 1 | §4 admissibility rule |
| 31 | BLOCKER | D3 | 1 | §4 admissibility rule, §2 S3 |
| 11 | BLOCKER | D4 | 1 | §6 AC7 vs §2 S1, §3 |
| 5 | BLOCKER | D5 | 2 | §2 S3 with §6 AC3 |
| 34 | BLOCKER | D5 | 2 | §2 S3 and §6 AC3 |
| 12 | HIGH | D5 | 2 | §2 S3 and §6 AC3 vs unit 1 §2 S3 |
| 28 | HIGH | D5 | 2 | §2 S3, rules table C, AC3 |
| 25 | BLOCKER | D6 | 2 | §4 rule A join |
| 32 | BLOCKER | D6 | 2 | §4 rule A, §2 S1 |
| 35 | BLOCKER | D6 | 2 | §4 rule A, the `same` half |
| 13 | HIGH | D7 | 1 | §2 S1 vs §4 data model |
| 17 | HIGH | D8 | 2 | §4 unresolved bucket vs §6, §7 |
| 27 | HIGH | D8 | 2 | §2 S1, rules table A, AC1 |
| 24 | HIGH | D9 | 2 | §4 data model |
| 36 | HIGH | D10 | 2 | §2 S5 and §6 AC6 |
| 40 | MEDIUM | D9 + D8 | 2 | §4 data model and Edges |
| 41 | MEDIUM | D11 | — | `memory/builds/aBatchedArm/README.md` roster |

---

### D1 — AC3's oracle collapses the exact population the conversion targets

**Rows 1, 10, 21, 33 · BLOCKER · `spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` §6 AC3**

AC3 is the unit's only equivalence proof — §5 names it "the safety property" and it authorizes each
tranche. Its observables are the SET of FAIL lines and the executed count `n`. Both are blind to a
compensating flip between two arms sharing one assertion text, because
`tools/unattended/check-unattended.test.sh:57-58` prints `FAIL missing: $2` and `FAIL unexpected: $2`
— the text alone, with no arm ordinal, line number or helper distinction.

Measured at BASE: 38 duplicated (helper, text) pairs covering 101 arms. If a conversion makes the
:467 arm start failing and :984 stop, both emit byte-identical bytes, the SET is unchanged, and `n`
counts executions rather than verdicts so it is unchanged too. AC3 reports equivalence over a real
verdict swap.

This is not an omission. AC3 asserts the opposite in its own text — "A swap where one arm starts
failing and another stops moves the FAIL set, so the pair of observables is sufficient and is the
strongest available" — and §4 both measures the duplicate population and *endorses grouping it*
("Group two arms carrying one text and a single break satisfies both `hit`s"). Sufficiency is
claimed, the spec's own data refutes it, and the claim is not even true of the strongest available
oracle: batching is contiguous, so arm ordinals are stable and an ordinal-keyed verdict vector is
available for one line of helper edit.

**Fix.** Give the oracle an arm identity, as an explicit sub-item of S2 so the enabling edit is in
scope: prefix the FAIL lines of `hit`/`miss`/`same` at :57-59 with `${BASH_LINENO[0]}` or a per-arm
ordinal, capture the baseline *after* that edit (it changes no verdict, only the FAIL text), and
restate AC3's red-when as "any (arm-id, verdict) pair differs" over an ordered MULTISET rather than a
set. State in AC3 that the un-identified form was *proven* insufficient, with the §4 population as
the reason. If the helpers must stay byte-stable, AC3 states the residual blind class explicitly and
S3 excludes the 101 duplicate-text arms from batching — but that is the expensive branch and the
helper edit is three lines.

**Left-shift gate.** A §10 recurring-bug-class entry, because this class is not spec-specific: *an
oracle keyed on a value that is not unique in its own population*. The gate that makes it cheap is a
one-command measurement any spec proposing an oracle must record in §4 — for this file,
`awk` the arm lines and report distinct-key count against arm count, redding when the key is not
injective. The general rule already exists in AGENTS.md §7 ("run a candidate gate predicate over the
real tree before wiring it"); what is missing is that an ORACLE gets the same treatment as a
predicate, and that belongs in the spec template's §6 guidance.

---

### D2 — S1's report-channel clauses have no criterion anywhere

**Row 2 · BLOCKER · `spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` §2 S1, against §6**

S1 gives the `emitted` helper two report-channel duties: RED when a `^unattended-report:` skip line
names a check the group asserts against, and strip those lines from `$out` before the verbatim
assertions run. Neither appears in any acceptance criterion. AC1, AC2 and AC7 never mention
`GOV_UNATTENDED_REPORT`, a skip line, or the strip — though S1 names those three as its observers.

This matters because §4 argues at length that dark-vs-silent is the unsoundness round 1 proved, and
this clause is the entire defence. The obvious refutation — that the emitted-set comparison already
catches a skipped check — fails at source: `report()` at `tools/unattended/check-unattended.sh:761`
is called at per-file and per-ARM granularity, so a check can fire legitimately from one item, land
in the emitted set, and still have the specific branch a `miss` control cares about skipped. The set
comparison cannot see that. Only the skip-line clause can, and no criterion stages its failing case,
which AGENTS.md §7 requires before a gate lands.

**Fix.** Add AC8: "When a group-mate's mutation pushes a check the group asserts against onto a
`report()` skip path, the suite REDS and the message names that check and quotes the skip line.
Staged and observed before landing. Red when: the run passes, or the message shows only the set
comparison." Add AC9 or extend AC1: "When the batch emits report lines, no `hit`/`miss` in the group
matches text originating in a stripped line" — cheapest form is a staged report line carrying an
assertion's text.

**Left-shift gate.** A spec-lint leg asserting the **S↔AC bijection**: every `S<n>` scope item is
named by at least one AC, and every AC names at least one `S<n>`. The spec format already carries
"Observed by AC…" lines, so both directions are parseable today. This single leg catches D2, D4 and
half of D8 — three of the eleven defects in this report — and it is the highest-value gate suggested
anywhere in this record.

---

### D3 — the admissibility rule is keyed on the check number, and a ratified prior already measured that granularity as insufficient

**Rows 9, 31 · BLOCKER · `spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` §4 "The admissibility rule", §2 S3**

The rule admits a `miss`/`same` control when a group-mate makes its check NUMBER fire, with the
stated warrant that "the check's own firing is then the liveness assertion that the branch was
reached at all". That warrant is false wherever a number carries more than one fail branch, which is
23 of 29 numbers.

Three verified counterexamples, all in the graded checker:

- **check 16** at `check-unattended.sh:1772` is a guard — `if [ ! -f "$tmpl" ]` — whose `else` at :1773 holds the remaining ~33 `fail 16` sites. A group-mate that deletes the template puts 16 in the emitted set while no else-branch site is ever evaluated.
- **check 10** at :1605-1609 is an `if _c10rc -eq 2 … elif -ne 0` pair (and a second such pair at :1615-1619). An rc of 2 fires 10 from the missing-half branch, and the drift `elif` never runs.
- **check 4** fires at :727 from the selector branch while :1064, :1072, :1076 and :1089 sit inside a per-file loop a mis-segmented selector never enters.

In each case a `miss` control on the unevaluated branch's message is ADMISSIBLE under the rule and
green over a branch that never ran. That is round 1's blocker reproduced one level down. AC3 cannot
see it because green stays green, and §4 states the blindness itself two paragraphs later without
connecting it to the rule that depends on its opposite.

The granularity was already measured as insufficient for this exact class:
**TOOL-aDrainedSluice-5b** at `memory/archive/DECISIONS.2026-08-10.md:37` found 11 of 16 manifest
branches ALREADY firing while their arms asserted only `check N FAILED` — "which names the check, not
the branch". §5 names the short-circuit risk and assigns S3 as mitigation, but S3 excludes only arms
whose check number NO group-mate fires, a strictly smaller and different set.

**Fix.** Restate admissibility per BRANCH: a `miss` against branch *b* of check N is admissible only
when a group-mate's `hit` witnesses branch *b* itself, by its own signature. The cheap sufficient
condition is "N carries exactly one fail branch", which is derivable today from the 178 signatures
`check-arms.py` already extracts and holds for exactly six numbers. Add to S3's exclusion list every
`miss`/`same` whose check number carries more than one fail branch unless the witnessing `hit` is on
the same branch, give unit 2's rule A the same per-branch predicate, and add a scope item running
TOOL-aDrainedSluice-5b's ratified method — instrument `fail()` and measure which branches actually
fire per candidate group — before the first tranche.

**Left-shift gate.** A leg that reports, per check number, the branch count and the number of `miss`
arms admitted under a number-keyed rule; red when any admitted arm's number carries more than one
branch and no same-branch `hit` witnesses it. Concretely this is `check-arms.py --branches` joined
against the arm inventory, and it is the same query D6's fix needs, so one tool serves both.

---

### D4 — AC7 requires a RED that nothing in unit 1 can produce

**Row 11 · BLOCKER · `spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` §6 AC7, against §2 S1 and §3**

AC7 requires the suite to RED on a group whose `miss`/`same` names a check outside its `emitted` set.
No scope item in this unit can produce that red. S1's declared signature is
`emitted <check-numbers> <output>`: it receives the expected set and the captured text and never sees
the `miss`/`same` calls that follow it, so it cannot know which checks the group asserts negatively.
S1's claim to be "Observed by AC1, AC2 and AC7" is contradicted by its own signature in the same
sentence. S3 is a declaration, not code. §3 puts the structural group linter explicitly OUT of scope,
and the Edges block concedes unit 1 "states as a rule and cannot enforce per group".

§7 nevertheless stages "a group carrying a `miss` against an unnamed check … observed RED" as a new
arm in `check-unattended.test.sh`, where nothing can turn it red. An unobservable AC lands as a
green, and the left-shift silently relocates to a unit that has not landed. The same defect
undermines S1's skip-line rule (D2), which needs "the checks the group asserts against" and is handed
neither.

**Fix.** Delete AC7 from unit 1, delete `AC7` from S1's and S3's observer lists and from §7's new-arm
line, and point both at TOOL-aBatchedArm-2 AC1, which already states it. If unit 1 must be
self-guarding, add an S-item that makes `emitted` read the group's remaining arms and accept the M2
consequence of a second mechanism in one spec.

**Left-shift gate.** The S↔AC bijection leg from D2, run in the reverse direction: an AC naming no
`S<n>` that can produce its observation is the defect, and an AC whose only cited mechanism sits in
another unit's spec is the detectable shape.

---

### D5 — rule C carries two incompatible definitions, and both red code the sibling spec mandates keeping

**Rows 5, 34 (BLOCKER), 12, 28 (HIGH) · `spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` §2 S3, rules table row C, §6 AC3**

Rule C is defined twice, at two different sites, and the two do not name the same line:

- **S3 and the §4 rules table grade the ASSIGNMENT site** — "a capture assigned to a name other than that group's own `out`". That fires on `_f1_clean=$(run)` at `check-unattended.test.sh:360`.
- **AC3 grades the USE site** — "a group asserts against a capture belonging to another group". That fires on the equality arms at :371 and :378.

Verified at source: the group at :359-366 has no `out` at all, its only capture is `_f1_clean`, and
its rationale is written into the file at :349-358. The consumers at :371 and :378 are inline
`$(run)` inside `same` with no assignment, a shape S3's assignment-target predicate cannot see at
all. So the leg has two rules that disagree about which line is the violation, and zero coverage of
the shape AC3 describes.

Both readings red a pattern **TOOL-aBatchedArm-1 S3 names verbatim as un-batchable and requires to be
preserved**. §3 of unit 2 says pre-existing violations are drained by unit 1's conversion and "never
waived" — and unit 1 forbids that repair. There is no route the spec permits. A permanently red
merge-bar leg drives someone to waive it, which §3 forbids, so the leg's first day is its worst day.

The recurrence is real and not limited to one block: `dout=$(drive …)` at :1588 sits in a group with
`hit`/`same` arms, and `mout`/`gout` at :1965 and :1968 sit between the `reset_tree` at :1964 and the
next at :1971 — two captures in one group, neither named `out`. No exemption, waiver or AC covers any
of them.

Decisive on intent: round 1's own left-shift wrote rule C with a MUTATION conjunct — "a group
carrying BOTH a mutation AND a `run` capture assigned to anything other than the group's own `out`" —
and the spec dropped the conjunct. That is exactly what turns a pristine cross-group baseline into a
violation.

**Fix.** Define rule C once, on the read side, with the mutation conjunct restored: *a group asserting
against a `run` capture whose assignment lies in a different group AND which is not declared a
cross-group baseline*. Add the declaration form (a marker comment beside the assignment), name
`_f1_clean` as the sanctioned instance and `$dout`, `$mout`, `$gout` as the others, give AC3 a
synthetic foreign capture as its failing fixture instead of the live legitimate one, and add the
positive criterion: "When `check-arms-groups.sh` runs over the tracked suite as TOOL-aBatchedArm-1 S3
leaves it, rule C reports zero violations. Red when: the `_f1_clean` block is flagged."

**Left-shift gate.** A spec-lint rule with teeth: **a spec that introduces a new gate leg must carry
an AC stating the leg's measured verdict over the tracked tree at BASE**, with the number filled in.
AGENTS.md §7 already demands the predicate be run over the real tree before wiring; making it an AC
turns "should have run it" into a criterion someone has to fill, and a false red on mandated code
cannot survive that AC being written honestly. This one gate also catches D6 and D9.

---

### D6 — rule A's join resolves 5% of its population, and 0% of the `same` half

**Rows 25, 32, 35 · BLOCKER · `spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` §4 "The three rules" (rule A), §2 S1**

Rule A needs a check number for each `miss`/`same` arm and the arm does not carry one, so §4 borrows
`check-arms.py`'s text join. Reproduced by importing that module's own `branches()` over
`check-unattended.sh` (178 signatures, none under the 12-char floor):

- In the direction the module actually joins — `b['sig'] in test_line`, `check-arms.py:234-235` — **5 of 101 `miss` arms resolve**, 96 resolve to nothing, 0 to many. Rule A would grade about 5% of its subject. The cause is visible in the residue: `miss` literals are FRAGMENTS of the checker's sentence (`:366` carries `cannot read AUTH_MODES from the driver, so the mode-membership branch …`), so the signature is not contained in them. The containment direction is inverted for `miss`.
- Reversed, 64-65 resolve and ~36 do not — and `check-unattended.test.sh:1201`, `miss "$out" "recorded BASE"`, resolves to **four** check numbers (9, 13, 19, 29). That directly refutes the safety property §4 asserts of the borrowed join: "It never mis-attributes a control to the wrong check; it declines to attribute it at all." A four-way match is neither a correct attribution nor a declined one, and the stated dichotomy has no branch for it.
- `same()` at :59 takes a human LABEL as its first argument, not a fail message. Enumerated all 27 `same` arms: they compare exit codes (:302, :317, :328, :709, :1252, :1593, :3007 and the inline `run; echo $?` forms at :1009, :1505, :2069), assert emptiness (:303, :671, :683, :710, :1056, :1084, :1251, :1655, :1896, :1909, :1986, :1996), compare whole-run output against `_f1_clean` (:371, :378), or grep the TREE rather than the run (:1590, :2084, :2790). **None carries a `fail N` message**, so the join is undefined for all 27 and the `same` half of rule A is vacuous or permanently noisy.

Rule A is the unit's load-bearing rule. Unit 1's admissibility rule and AC7 both read "a `miss` or
`same` assertion against check N" and inherit the same undefined join.

**Fix.** State the join DIRECTION explicitly in §4 and record the measured resolution rate at BASE.
Drop `same` from rule A and say why, or require `same` arms to carry an explicit `# check N`
annotation the linter reads with an unannotated one REFUSING. Give ambiguous multi-check resolution
its own refusal rather than letting it pass as an attribution. Note also that the tree-asserting
`same` arms at :1590, :2084 and :2790 read neither `$out` nor `$rc` and fall outside both this rule
and unit 1 S3's enumerated categories — finding 35's claim that all 27 are already S3-excluded
overstates by those three, and the gap needs its own sentence.

**Left-shift gate.** The same BASE-population AC as D5: a spec introducing a gate states the leg's
measured coverage over the tracked tree. "Rule A resolves 5 of 101 arms" is a number nobody could
write down and still call the rule load-bearing. Additionally, a liveness assertion on the leg
itself — it prints resolved / unresolved / ambiguous counts every run — so a join that decays to
zero coverage announces itself instead of reporting clean.

---

### D7 — `emitted`'s contract is self-contradictory about whether it runs the batch

**Row 13 · HIGH · `spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` §2 S1 vs §4 data model**

S1 says the helper "runs the batch with `GOV_UNATTENDED_REPORT=1`" while declaring the signature
`emitted <check-numbers> <output>`, and §4's data model shows the caller doing `out=$(run)` then
`emitted "4 10 14" "$out"`. Both cannot be true, and the consequence is load-bearing either way. If
the helper runs, every group costs a SECOND full invocation, which attacks §1's whole premise and
AC6's 20-minute target. If it does not, no group's run is ever under `GOV_UNATTENDED_REPORT=1` —
verified at `check-unattended.sh:760-761`, `REPORT=${GOV_UNATTENDED_REPORT:-0}` and `report()` prints
only when it is 1, so the channel is silent by default — and S1's skip-line detection, the entire
defence in D2, can never fire. §5's observability bullet inherits the same ambiguity.

**Fix.** Put the variable on the run, not the helper: define `run_reported() { GOV_UNATTENDED_REPORT=1
bash "$SCRIPT" 2>&1; }` in S1, have converted groups capture with it, and reduce `emitted` to a pure
grader of captured text. Restate in S4 that invocation count per group is exactly one, which is the
figure AC6's target depends on.

**Left-shift gate.** The suite's own cost ceiling, which AGENTS.md §7 already requires ("every suite
declares a wall-clock ceiling, a runner REDS on breach"). A helper that silently doubles invocations
is caught by a declared ceiling on the first tranche rather than at the twentieth. Confirm the
unattended leg's ceiling is declared and that AC6 measures against it, not against a shard.

---

### D8 — the unresolved bucket and the `emitted`-less group have no verdict

**Rows 17, 27 · HIGH · `spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` §4, §2 S1, rules table A, AC1**

Two populations are described and neither is given a verdict.

**Unresolved texts.** §4 says an unresolvable text is "REPORTED as unresolved rather than skipped"
and §5 repeats "reported, never skipped". Neither says whether the run exits non-zero. §6's six ACs
cover rules A, B, C, zero-group, header and manifest row, with none for unresolved. §7 stages "one
staged violation per rule", which is three. The bucket is provably non-empty:
`miss "$(GOV_UNATTENDED_REPORT=1 run)" "check 31"` at `check-unattended.test.sh:1865` is a legitimate
control whose text is a report-channel string with no `fail N` signature at all, and D6's measurement
strands 36 to 96 more depending on join direction. Left green it is green-by-absence on the exact
class the unit exists to close; left red it reds correct arms permanently.

**Groups with no `emitted` call.** Rule A never says what it does with one, and that is every group in
the file at BASE plus every S3-excluded singleton forever. Read literally — "a check number the
group's `emitted` set does not name" — an absent set names nothing, so rule A reds all of them and
the leg can never be green. The unit's own Edges say the harsh reading out loud: "Without it there is
no set to link against and EVERY GROUP REDS." Read the other way, an absent `emitted` line is a
blanket exemption, and deleting one line becomes how a mis-grouped control evades the gate built to
catch it. Neither reading is written down, and the population is permanent, not transitional: §4
records 40 of the 101 `miss` arms in `reset_tree` blocks carrying no `hit` at all, and unit 1 S3
keeps every unwitnessed `miss`/`same` alone on its own tree.

**Fix.** Declare both verdicts in S1. Unresolved is RED, drained through a shrink-only waiver registry
keyed on arm text — the idiom this repo already uses — with an AC staging an unresolvable text and
that case added to §7's new-arm line beside the three rules. A group holding two or more arms and no
`emitted` call is itself a rule-A violation; a group holding exactly one arm is exempt and its count
is printed on the liveness line so the exempt population stays visible.

**Left-shift gate.** A rule with no stated verdict is the gateable shape here: extend the spec-lint
leg so that any §4 paragraph introducing a rule class must be joined to an AC carrying a
`Red when:` clause. That is the same parse the S↔AC bijection leg from D2 already performs, widened
by one field.

---

### D9 — `reset_tree` is not the file's group delimiter

**Rows 24 (HIGH), 40 (MEDIUM) · `spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` §4 data model, Edges**

§4 states flatly that "a group is the text between one `reset_tree` call and the next, which is the
same delimiter TOOL-aBatchedArm-1 batches on, SO THE TWO CANNOT DISAGREE about where a group starts."
That guarantee is false, measured in the tracked file:

- 305 lines mention `reset_tree`. Six are comments (:176, :438, :587, :640, :1501, :2022), one is the definition at :240, and four are nested inside helper bodies.
- `anchor_break` (:275), `anchor_restore` (:293) and `seed_ros` (:2712) each call `reset_tree` internally. Their call sites number 9, 9 and 6 — **24 true tree-state boundaries carrying no literal token at the call site**.
- `wreset()` at :1582 is a second reset primitive over its own `WP` fixture with five call sites (:1587, :1599, :1609, :1618, :1631).
- `if in_shard 1` at :299 and `if in_shard 2` at :1269 are hard region boundaries a group must not span.

A literal splitter merges those 24 arms into the PREVIOUS group and grades their controls against a
foreign `emitted` set — a false red where the sets differ, and a **false GREEN where they happen to
overlap**, which is the failure mode this unit exists to prevent. It also opens spurious groups
inside `anchor_break`'s and `anchor_restore`'s bodies and at six comments, and folds the `wreset`
region so that `hit "$dout"`, `miss "$out" "check 17"` and the `same` at :1590 are graded against a
foreign set. Unit 1 §4 inherits the same assumption. Nothing in either spec discloses the limit, and
no §3 non-goal withholds it — the delimiter is the linter's whole parse.

Row 40 is graded MEDIUM as a marginal row: it adds the `wreset` and `in_shard` instances to row 24's
class and restates D8's transitional half. The underlying defect is HIGH and row 24 carries it.

**Fix.** Both §4s name the delimiter SET — `reset_tree`, `wreset`, `anchor_break`, `anchor_restore`,
`seed_ros`, and the `in_shard` block boundaries — restrict recognition to non-comment call sites at
column 0 outside a function body, and make the linter **REFUSE** on any other function whose body
calls `reset_tree` or `git reset --hard`, so a fourth reset helper cannot be added silently. Refusing
is what keeps this fix from rotting the moment someone writes helper number four.

**Left-shift gate.** The refusal above IS the gate, and it is the right shape: a parser that meets an
unrecognised boundary construct stops rather than guessing. Pair it with the BASE-population AC from
D5 — running the candidate splitter over the tracked file and printing the group count would have
surfaced all four delimiter classes before a line of the linter was written.

---

### D10 — the leg is declared into the held population that a live OPEN backlog row records as going silently red

**Row 36 · HIGH · `spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` §2 S5 and §6 AC6**

S5 declares the new linter `subject = kit`. `TOOL-aQuenchedHarness-9` (OPEN, `memory/backlog/TOOL.md:420`)
already recorded what that costs, verbatim: the leg "is `subject = kit`, so it is HELD off every
default bar, and holding a self-test for COST removes the only thing that would report it breaking" —
with `unattended gate selftest` measured at 9067 s RED against a declared 3800 s and unnoticed.

Verified: `tools/gate-legs.json` carries 104 legs, 48 `subject = kit`, and **all five surviving
unattended rows are `subject = repo`**, which is the deliberate split AGENTS.md explains. AC6 only
ever observes the new leg "with the kit self-tests enabled", and AGENTS.md pins `GATE_SELFTESTS` as
on-demand with no boundary setting it — so the linter never runs at a push. §5 prices the leg at
"seconds", so the cost rationale that justified the hold does not apply here at all. Unit 1's Rollout
lands this unit first precisely because "nothing downstream re-asks whether a group's controls still
witness anything"; held, nothing does, and the left-shift for five of round 1's six findings
evaporates.

**Fix.** Declare `subject = repo` in S5 — the leg's subject is a tracked file in THIS repository that
goes stale as people edit it, which is the ruling's own test — and retarget AC6 to observe the leg on
a plain `bash tools/run-gates/run-gates.sh`, citing TOOL-aQuenchedHarness-9 as the reason the held
classification is refused.

**Left-shift gate.** A manifest lint: a leg whose guard path lies OUTSIDE its own `tools/<kit>/`
directory may not be `subject = kit`. That is mechanical against `tools/gate-legs.json` today,
catches this row at declaration time, and would have caught the row TOOL-aQuenchedHarness-9 is still
open about.

---

### D11 — the build's authored roster still declares one unit

**Row 41 · MEDIUM · `memory/builds/aBatchedArm/README.md`**

Verified verbatim. The authored `<!-- roster:units -->` block at :61-71 lists only
`TOOL-aBatchedArm-1`, and the paragraph beneath it reads "Decomposed to ONE unit deliberately" with a
rationale for that decomposition. The front matter at :7 carries
`ids: TOOL-aBatchedArm-1 TOOL-aBatchedArm-2` and the generated block at :74-81 reports "2 unit(s)"
with both spec rows. The `--rescope` that added unit 2 never reached the authored half, so the
record's two halves state opposite decompositions and the linter has no mechanism row. A reader
arriving at the build gets the pre-fold answer.

**Fix.** In the same commit as the spec, add the `TOOL-aBatchedArm-2` row to the roster table with its
mechanism, and replace the "Decomposed to ONE unit deliberately" paragraph with the two-unit
rationale (M2: a gate is not the thing it gates) that unit 2's §9 already states.

**Left-shift gate.** Cheap and exact: extend the hygiene gate to compare the authored
`<!-- roster:units -->` id set against the generated `ids:` front matter and red on a mismatch. Both
halves are already parsed by `gen_build_index.py`; this is a set comparison over data it holds in
memory, and it is "derive over author" applied to the one field that has now drifted.

---

## What the fold got right

Worth recording, because the next revision should not undo it. Rev-2's §4 measurement work is sound
and reproduced here on every figure that could be checked: the arm population, the duplicate-text
census, the branch inventory and the uniqueness of the 178 branch signatures under `check-arms.py`'s
normaliser. §4 also states the `emitted` blindness plainly rather than burying it, and the decision to
split the linter into its own unit is correct under M2 — a gate is not the thing it gates. The defect
is not that the fold measured badly. It is that three separate mechanisms were built on top of those
correct measurements while assuming a uniqueness the same measurements refute.

## Rework bar before round 3

Both specs need a revision pass, not a patch. The minimum:

1. Unit 1 §6 AC3 re-derived on an arm-identified multiset (D1), with the S2 sub-item that enables it.
2. Unit 1 §4 admissibility restated per BRANCH, with S3's exclusion list widened to match (D3).
3. Unit 1 AC7 deleted or given a mechanism (D4); S1's report-channel duties given criteria (D2); S1's run-vs-receive contract settled (D7).
4. Unit 2 rules A and C each reduced to ONE predicate, with the mutation conjunct restored to C and the `_f1_clean`, `$dout`, `$mout`, `$gout` instances named as sanctioned (D5, D6).
5. Unit 2 §4 delimiter SET enumerated, with a refusal on unrecognised reset constructs (D9).
6. Unit 2 verdicts declared for the unresolved and `emitted`-less populations (D8), and S5 moved to `subject = repo` (D10).
7. The build README's authored roster brought level with its generated half (D11).

The single highest-leverage gate across this whole record is the **S↔AC bijection spec-lint leg**: it
closes D2 and D4 outright and half of D8, and it is parseable from the spec format as it already
stands.

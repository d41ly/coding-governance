**Serves:** spec-audit TOOL-aBatchedArm-1

# Tier-2 spec audit — TOOL-aBatchedArm-1, batching the gate self-test's arms

*Adversarial pre-code pass over the one unit this build declares. Node `a`, 2026-09-10, ROUND 1.
Every finding below survived a skeptic prompted to REFUTE it; each carries its address inside the
spec, the fix, and the gate that would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md`@`1c0680087d29b3ece61edc8ae6a24ddce8e43935`

The pin was re-hashed against the working tree at review time and matches.

## Verdict: BLOCKED

Three findings at BLOCKER severity, two at HIGH, one at MEDIUM. The three blockers are not three
unrelated defects: they are three doors into ONE hole. The spec's safety argument is carried by
`emitted` plus AC3's per-arm verdict diff, and both are blind to the same population — the 101 `miss`
control arms, whose whole content is that a check does NOT wrongly fire. `emitted` grades the FAIL
channel, so a control's check number is legitimately absent from the expected set and its absence is
therefore unobservable; AC3 sees green-to-green, so no verdict flips. Batch a control behind a
group-mate's mutation and it can pass with the branch it was pointed at never evaluated, or never
reached at all. That converts up to 101 of 377 assertions into decoration with every stated property
green — which is precisely the shape the suite's own header says it exists to refuse.

This is a spec-level fault and not a fix-while-building item. §2 S3 is the partition rule, §4 is the
argument that the partition is safe, and both have to be re-derived before a tranche lands, because
the conversion is mechanical: once a group is written, nothing downstream re-asks whether its
controls still witness anything.

The medium is orthogonal and cheap: AC6 grades a shard, §1 sets the target on the suite, and the
runner that produces the verdict runs it unsharded.

## Run integrity

- Lenses: 4/4 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified; 0 spurious verdicts discarded; 0 duplicates removed.
- Unverified (no usable skeptic verdict): 0. There are no OUTSTANDING findings carried into this
  record.

Every lens and every skeptic batch returned, so no zero reported here is a zero-by-absence. The
finding set is complete for the lenses run.

## Review shape

| Measure | Value |
|---|---|
| Raw findings | 33 |
| Confirmed | 6 |
| Refuted | 27 |
| Unverified | 0 |
| Precision (confirmed / (confirmed + refuted)) | 0.18 |
| Round | 1 |

Precision at 0.18 sits well under the charter's ~0.5 tighten-scope line (§8). Read it as the target's
shape rather than as a bad run: a 198-line spec that has already absorbed four prior records
(`TOOL-aPooledSweep-3`, `TOOL-aPooledSweep-7`, `TOOL-aTracedSpawn-2`, `TOOL-aDrainedSluice-5` N17)
pre-empted most of what the lenses raised, and its §3 non-goals refuted several findings by
themselves. A round 2 on this same spec should tighten scope to §2 S3 and §4 rather than add lenses.

**Three of the six are one root class.** Findings 18, 25 and 10 are three views of "a batched `miss`
control has no witness". They are kept as separate rows because each carries evidence and a residue
the others do not — 18 owns the dark-check channel, 25 owns the ratified precedent, 10 owns the
collateral-branch trigger — but the single fix in 25 (no `miss` arm is grouped, or each grouped one
takes a paired companion) closes all three. That is why 10 is ranked below 25 despite naming the same
population: its fix is subsumed. Findings 21 and 26 are genuinely distinct classes, and 15 is
unrelated.

## Findings, severity-ranked

| # | Sev | Address in the spec | Defect |
|---|---|---|---|
| 18 | blocker | §4 "Why the set and not a count", §2 S3 | `emitted` grades only the FAIL channel; a check pushed onto a skip path is byte-identical to one correctly silent, so a batched control stays green over a dead branch |
| 25 | blocker | §2 S3 | The 101 `miss` arms are not in S3's un-batchable list, though `TOOL-dScriptedRepeat-15` S3 already ratified that classification for this exact file |
| 26 | blocker | §4 "Why the set and not a count" | The 0-collision uniqueness proof measures the CHECKER side; on the TEST side 20 assertion texts are carried by 46 separate arms, so one break can satisfy two `hit`s |
| 10 | high | §2 S3 against §4 | S3 excludes no control class while §4's own worked example batches a `miss`; a group-mate's break can make the control pass vacuously with `emitted` still content |
| 21 | high | §2 S3, observed by AC4 | S3 misses the whole-run EQUALITY arms and, worse, the non-empty baseline capture at `check-unattended.test.sh:360` that two of them compare against |
| 15 | medium | §6 AC6 against §1 Goal | §1 sets the target on the suite's verdict; AC6 grades only the longer shard, and the run that produces the verdict is unsharded |

## The class, and the gate that closes most of it

Before the per-finding detail: five of the six defects are the same authoring failure at two
altitudes. The spec reasons about arms as *breaks* — a mutation, a check that fires, a `hit` that
sees it — and every safety property it states is built on that model. But 128 of the 377 assertions
are not breaks. 101 `miss` arms assert an absence and 27 `same` arms assert an equality, and both are
falsified by a group-mate rather than by their own mutation. The spec never classifies them, so its
partition rule (S3) does not exclude them and its oracle (`emitted`) cannot see them.

*Gate.* One structural linter over `check-unattended.test.sh`, run on the bar beside the suite,
parsing each `reset_tree`-delimited group and redding on any of:

- a group carrying a `miss` or `same` assertion whose check number is not in that group's `emitted`
  set — the check's own firing is the liveness assertion §7 demands of every signal;
- a group carrying more than one arm whose assertion TEXT is identical (`grep -o` the assertion
  strings, `sort | uniq -d`; 20 texts across 46 arms today);
- a group carrying both a mutation and a `run` capture assigned to anything other than the group's
  own `out` — that is a poisoned baseline.

It grades LINKAGE, never adequacy, and its header must say so, or a structural check reads as a
semantic one to everyone who did not write it (§7). Its own failing case is one line: move a `miss`
into a neighbouring group and confirm RED before wiring it.

That linter closes 18's residue, 25, 26, 10 and 21's second half. What it cannot reach — a check that
went dark rather than staying honestly silent — needs 18's second half, and 15 needs a different gate
entirely.

## Detail

### 18 — blocker — §4 "Why the set and not a count" (and §2 S3)

`emitted` grades the FAIL channel only, and the checker's "this check went dark" states are silent by
construction. `fail()` at `tools/unattended/check-unattended.sh:93` is the ONLY emitter of
`UNATTENDED check N` — grep returns exactly one hit in the file. Check 7's own dark-notice at `:1524`
uses the lowercase `unattended: check 7` spelling, so it is not even in `emitted`'s namespace. Every
SKIP goes through `report()` at `:761`, gated on `REPORT=${GOV_UNATTENDED_REPORT:-0}` at `:760`, and
the suite's `run()` at `check-unattended.test.sh:247` is `bash "$SCRIPT" 2>&1` and never sets it.
There are 15 such skip sites, covering checks 15, 23, 24 and 31.

So a check that goes dark prints nothing on the default channel and is byte-identical, to every
assertion in this suite, to a check that correctly stayed silent. Check 24's skip at `:2150` fires
when the working build README does not carry exactly one well-formed units pair — a mutation many
arms make — so a group-mate pushing a sibling's check onto a skip path is not hypothetical.

For a `miss` control the consequence is total: the check number is legitimately absent from the
group's expected set, so `emitted` cannot distinguish "correctly silent" from "dark", and the arm
stays GREEN over a branch that was never evaluated. AC3 cannot see it either — green stays green, so
no verdict flips. §4's stated limitation ("what `emitted` does NOT check") names a different one, that
a check fired for the reason its arm intended, and says nothing about silence. Both stated safety
properties are blind to the same class, and it is the green-by-absence class this suite's own header
says it exists to refuse.

**Fix.** Add to §4 the admissibility rule that makes `emitted` load-bearing for controls: a group's
`miss` and `same` assertions against check N are admissible ONLY when N is in that group's `emitted`
set, so the check's own firing is the liveness assertion. State the residue as an S3 exclusion — a
control whose check no group-mate makes fire runs on its own tree. If a cheaper detector is wanted,
say so in S1: run the batch with `GOV_UNATTENDED_REPORT=1`, strip `^unattended-report:` lines out of
`$out` before the verbatim assertions run, and have `emitted` red on a skip line naming any check the
group asserts against.

**Left-shift.** The group linter's first rule above, plus a narrower one this finding argues for on
its own: `emitted`'s failure message must print the skip lines it saw. A helper that can distinguish
dark from silent and does not say which it saw hands the operator the same ambiguity one level up.

### 25 — blocker — §2 S3

S3's un-batchable list omits the `miss` and `same` arms as a class, and this repo has already ratified
that classification for this exact file. CLOSED record `TOOL-dScriptedRepeat-15` S3:

> SCOPING IS CLASSIFIED ON WHAT AN ARM ASSERTS ABOUT ABSENCE. An arm that asserts something is
> PRESENT (`hit`) may be scoped... An arm asserting something is ABSENT (`miss`) or comparing an exit
> code (`same`) may NOT: scoping its region away makes it pass vacuously.

S3 here excludes the three check-1 `exit` branches, the exit-code-only arms, the empty-output arms and
the anchor, PATH-stub and remote-rewriting arms. The `miss` class is not among them. Measured in the
file at BASE: 249 `hit` + 101 `miss` + 27 `same` = 377, matching §1's own figure, and 40 of the 101
misses sit in `reset_tree`-delimited blocks carrying no `hit` at all — those have no positive witness
even today, before any batching.

Batch one behind a group-mate's break that takes an earlier `elif` under the same check number, or
that flips `ADV_HEAD_OK` to 0 so the accessor at `check-unattended.sh:294` returns early, and the
`miss` passes with its emitting branch never evaluated. `emitted` sees the expected check number and
is content. AC3 diffs green-to-green. §4's mitigation is hit-only by construction — "the per-branch
`hit` lines stay exactly as they are" cannot witness an absence assertion.

The `same` half of this finding is overstated and is recorded as such: S3's exit-code and
empty-output exclusions already cover most of the 27, and the `ADV_HEAD_OK` example is arguably a
"remote-rewriting arm". The 101-arm `miss` class is the load-bearing half, and it is unexcluded and
unwitnessed. `TOOL-aPooledSweep-7` independently names the want-substring-ABSENT verb — 210 such
assertions across the two costliest suites — as the missing harness vocabulary, which is the same gap
seen from the port side.

**Fix.** Cite `TOOL-dScriptedRepeat-15` S3 in §3 as a binding prior, and add to S3: no `miss` or
`same` arm is grouped, or each grouped one takes the explicit paired companion that record already
defines. Restate the measured split (101 `miss`, 27 `same`) beside F1's 237-of-298 candidate figure,
which today counts BLOCKS and not assertion classes and therefore overstates the batchable population.

**Left-shift.** The group linter's first rule. Beyond the linter, a spec-lint worth having on its own:
a spec whose §2 declares a partition over an existing population must state that population's
composition, not its block count. F1's "80 % are candidates" is a true statement about the wrong
denominator, and nothing in the spec catches the substitution.

### 26 — blocker — §4 "Why the set and not a count"

The paragraph justifies `emitted` with: all 178 branch signatures are unique and each belongs to
exactly one numbered check, verified 2026-09-10 with `check-arms.py`'s own normaliser, 0 collisions.
That is uniqueness on the CHECKER side. It bounds `emitted`'s attribution — a fired check number maps
to one branch — and it says nothing whatever about duplication on the TEST side, which is where the
arms live.

Measured in `check-unattended.test.sh` at BASE: 20 distinct assertion texts are carried by 46 separate
arms, at multiplicities 2 to 4. `a run-state file's generated markers are malformed` is the text of
four arms, at `:467`, `:984`, `:1310` and `:1313`. The build-method text
(`a directive's cited build-method section states nothing about it...`) is carried by three, at
`:1475`, `:1479` and `:1485`, each with a different `_bm_sections` fixture. The check-23
dispatched-path text is carried by four, at `:2824`, `:2852`, `:2862` and `:2885`.

Several of those duplicate sets are ADJACENT `reset_tree`-delimited blocks, which is exactly what §4's
"contiguous run of arms delimited by `reset_tree`" would group. Batch `:1475`, `:1479` and `:1485` and
the last `>` redirect to `memory/guides/BUILD-METHOD.md` wins; one break satisfies all three `hit`s;
`emitted` sees one check number and passes; F1's widen-until-it-reds loop never reds, so the method
the spec prescribes for finding group size actively drives toward this state; and AC3 diffs
green-to-green. Two arms dead, nothing observes it. That is the exact false-green `emitted` is claimed
to prevent, and its stated justification is blind to it because it measured the wrong population.

**Fix.** Add a scope item: no two arms sharing an assertion text may share a batch, derived
mechanically rather than by review. Correct §4's justification to say that branch-signature
uniqueness bounds `emitted`'s ATTRIBUTION and not the arms' mutual independence — those are two
different claims and the spec spends one to buy the other.

**Left-shift.** The group linter's second rule, which is three shell commands and reds on
`sort | uniq -d` over the assertion texts within a group. Its failing case is already staged for free:
move `:1479` into `:1475`'s group and it reds today.

### 10 — high — §2 S3 (against §4, "Why the set and not a count")

Same population as 25, different trigger, and it lands on §4's own worked example rather than on the
prose. S3's exclusion list names no control class at all, and §4's illustration batches one directly:

```
emitted "4 10 14" "$out"
hit  "$out" "<A's own failure text>"
hit  "$out" "<B's own failure text>"
miss "$out" "<C's near-miss text>"
```

So §4's claim that "the set catches both directions" is false for the direction that matters. A
`miss` asserts that a check does NOT wrongly fire on an honest tree; sharing a tree with group-mates'
mutations destroys the premise, because the tree is no longer honest. Where a group-mate's break
drives that check into its absent-input or refusal branch, the branch the control was pointed at is
gone, the control passes vacuously, and `emitted` still sees the check number in the set — so the set
comparison is internally consistent and reports nothing.

This repo has already measured the mechanism. `TOOL-aHoistedPass-38`: a break upstream makes "every
arm downstream grade that refusal". The flip is pass-to-pass, so AC3's equivalence diff does not move,
and §5's mis-grouped-tranche mitigation observes a NON-EMPTY diff, which this case does not produce.
Every stated mitigation in the spec is keyed on an observation this failure mode does not generate.

**Fix.** Subsumed by 25: add "every arm whose only assertion is a `miss`" to S3. If a narrower rule is
preferred to keep more of the batchable population, require in S2 that each batched `miss` sit in a
group where some `hit` proves the same check number reached a LIVE branch, and state that requirement
as its own acceptance criterion with a staged red — not as prose in §4, which nothing grades.

**Left-shift.** The group linter's first rule again. The separate lesson worth writing into §10 of the
project's recurring-bug-class list: **a worked example in a design section is a specification.** §4's
snippet is the only concrete statement of what a group looks like, a builder will copy it, and it
carries the defect the surrounding paragraph denies.

### 21 — high — §2 S3, observed by AC4

S3's un-batchable list misses the whole-run EQUALITY arms, and the hole is not the arms themselves —
it is the baseline they compare against.

`same()` at `check-unattended.test.sh:59` is a whole-string equality. Two arms compare a full run to a
NON-EMPTY captured baseline: `:371` and its `HERE` sibling at `:378`, both against `$_f1_clean`, which
is captured at `:360` as a bare `_f1_clean=$(run)`. The comment at `:361-365` states outright that the
baseline is deliberately not empty — the fixture "carries whatever standing reds the suite already
has". S3 excludes exit-code arms and empty-output arms and names neither this shape nor this capture.

Batching either equality arm breaks the equality by construction, which reds, and is caught. The
hazard is one level up: the CAPTURE at `:360` is a `reset_tree`-delimited block carrying NO mutation
and no anchor, PATH-stub or env special, so F1's own measurement counts it among the 237 candidates.
Group it with mutations and both sides of both equalities carry the same mutations — the assertions
become tautologies, `emitted`'s set is internally consistent so it passes, and AC3 sees green-to-green
so no verdict flips. S3 is framed as "every arm whose break can truncate or relocate the run", and
this block has no break at all, so no stated property in the spec covers it.

The finding's second half is weaker and is recorded as such: three arms spell "the output is empty" as
`same ... "$(run; echo $?)" "0"` (`:1009`, `:2069`) and `"$(run >/dev/null 2>&1; echo $?)" "0"`
(`:1505`), which a converter selecting on the literal `"$out" ""` shape will not recognise as the
class S3 names in substance. Those arms red when batched, so they cost a tranche revert rather than a
false green.

**Fix.** Restate S3's third clause as "every arm whose assertion is an EQUALITY over a whole run —
against `""`, against a captured baseline such as `_f1_clean`, or against a run concatenated with
`$?`", and name the baseline CAPTURES themselves (`check-unattended.test.sh:360`) as un-batchable
anchors. Have AC4 grade the list against the 27 `same` call sites rather than against the phrase
"asserting the output is EMPTY", which is a description of intent and not a selector.

**Left-shift.** The group linter's third rule: a group carrying a mutation and a `run` capture bound
to anything other than its own `out` is a poisoned baseline, red. Cheap, exact, and its failing case
is `:360` moved one line down into a mutating group.

### 15 — medium — §6 AC6 (against §1 Goal)

§1 sets the target on the SUITE: "the suite reaches its verdict in under 20 minutes". AC6 grades only
"the LONGER shard". Nothing in the spec grades the unsharded run's wall clock — AC5 grades its
assertion COUNT only.

The suite's own note at `check-unattended.test.sh:3161-3162` says what this costs: "Neither shard
alone is this suite, and the whole-suite claim lives only in a run with no `--shard` argument."
`tools/unattended/run-unattended-gates.sh:157-158` is dispositive: "The suites are run UNSHARDED on
purpose ... so the whole-suite claim exists only here." And the budget row that actually books this
suite's cost — `tools/run-gates/selftest-budgets.txt:114`, `unattended gate selftest` at 13600 s —
carries the argv `bash tools/unattended/check-unattended.test.sh`, with no shard argument. AC6's §5
deliverable writes a shard reading into a row whose own argv is the unsharded run.

The shards are not bar legs; the kit's `*.test.sh` rows left `tools/gate-legs.json` at the 2026-08-23
ruling. So the run that produces a verdict is the unsharded one, and its cost is roughly the SUM of
the shards, not the max. Two shards at 19 minutes each satisfy AC6 while the suite's verdict costs 38,
and the unit can then be declared done against a target the mandate did not set — with the
`SHARD_ARITY` follow-up named in §3 never reached.

One clause of the finding is an overstatement and is recorded as such: "AC6 never misses" is false, a
single shard over 20 minutes still reds. That does not rescue the metric mismatch.

**Fix.** Make AC6 name the run it measures and make §1 match it. Either "the UNSHARDED run completes
in under 20 minutes", or "both shards run concurrently and the longer completes in under 20 minutes,
which is the verdict this leg is consumed as" — and if the second spelling is chosen, §1 must state
plainly that the whole-suite claim is not what is being bounded, since `run-unattended-gates.sh` does
not run them concurrently today.

**Left-shift.** A budgets-file gate, and it generalises past this unit: assert that each row's
recorded reading was taken from THAT ROW'S argv. The reading text already sits in column 4 of
`selftest-budgets.txt`; red when a row's argv carries no `--shard` and its reading names one, or vice
versa. It is a value-beside-its-source check of exactly the kind §6 of the charter demands, and it
catches the whole class of "measured a proxy, booked it as the subject" rather than this one instance.

## What this round did not cover

- **The conversion itself.** This is a pre-code audit of a rev-1 spec. Nothing here grades an edit to
  `check-unattended.test.sh`, because none exists at the pin.
- **Whether the 20-minute target is reachable at all.** §4 rejects the memo alternative on a measured
  10 % and §3 bounds spawn-cutting at ~2 s per invocation, and no lens re-measured either. If the
  helper lands and the number does not move, that is a finding this round could not have produced.
- **`emitted`'s own implementation.** It does not exist yet. AC1 and AC2 describe it and both were
  read as adequate for what they describe; the blockers above are about what `emitted` is CLAIMED to
  prove, not about how it would parse.
- **The 27 refuted findings.** They are not carried into this record and their texts are not
  reproduced here; a refuted finding is not evidence and this corpus does not archive it.

Three build-method constraints WERE checked against the spec and are clean, so their silence above is
a verdict rather than an omission. **M2, one mechanism per spec:** the unit declares `emitted` plus the
grouping it enables, and the re-measured floors under S4 are a re-reading of an existing constant, not
a second mechanism. **M3, a run's resolver authority:** both §8 forks carry conforming
`RESOLVED (agent, 2026-09-10, delegated)` marks, and F1 defers its figure to the build record instead
of pinning one. **M12, a rejected candidate carries the test that rejected it:** §4 rejects the
declarative arm table on the 377-assertion rewrite and the closed port, and the `run()` memo on a
measured 262 distinct states out of 293 invocations.

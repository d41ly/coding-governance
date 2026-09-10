**Serves:** spec-audit TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2

# aLeakedHandle — Tier-2 spec audit, round 2

*Adversarial pre-code pass over units 1 and 2 at rev-2, after the fold of round 1's ten defects. Node `a`, 2026-09-10, base `013b1af9`. `TOOL-aLeakedHandle-3` is NOT pinned this round and was not re-read by the lenses; one finding below repairs it anyway, because a sibling's sentence contradicts a pinned criterion. Every finding here is a defect in a document, not in shipped software.*

**Range — ROUND 2**, two subjects pinned at these blobs: `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-1.md@b9477e7f59af410889f7dee6470c73d6fdc49447`, `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-2.md@8461c3142da2d744547c07dad3efbf533392327b`.

## Verdict: BLOCKED

One blocker, and it is the unit's central predicate rather than a document defect around it. Unit 2's admission rule reads `seconds >= ceiling` as *the bound expired*, and `run-gates.sh:1393` runs every leg **unbounded** when `CEILINGS_LIVE=0` while the `.leg` row records no bound field — so on a host with no runnable `timeout`, a leg that runs long and then fails on its own is admitted as evidence, into a MONOTONE file, and only `--reset` clears it. That is the manufactured red §4 Rollout says this unit avoids, arriving by the one path the spec never considers. Two highs and three mediums sit behind it. Nothing here asks for a unit to be re-scoped or re-ordered; the blocker asks for one comparison to be bounded before anybody builds it.

### Review shape

Raw 29 · confirmed 8 · refuted 21 · unverified 0 · precision 0.28.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. No arm of this run failed to report, so the zero counts here are positive evidence rather than an absence of it, and the finding set is complete as far as four lenses reach. This run is complete.

Precision 0.28, against 0.30 in round 1 and the ~0.5 floor §8 sets. Two tightened rev-2 documents over an already-hardened area manufacture refuted noise, exactly as round 1 predicted they would; read it as a signal that a round 3 over these repairs should be scoped to the repairs themselves rather than re-swept.

### Consolidation

The eight confirmed findings describe **six distinct defects**. One cluster of three merged: raw 2, 10 and 25 are the same `consumes-from` bullet seen by three lenses, addressed once as §2 Edges and twice as §3 Edges (the `### Edges` block sits under §3; both addresses are the same eleven lines). Severities are the ones adjudicated HERE and differ from the raw labels in two places, both stated in the row: raw 18 is **promoted** from high to blocker because it is a defect in what the unit must BUILD rather than in what it must say, and raw 3 is **demoted** from high to medium to keep the ladder consistent with round 1, which rated the identical shape MEDIUM as D7. Adjudicated totals across the six rows: **1 blocker, 2 highs, 3 mediums, 0 lows.**

| # | Sev | Unit | Address | Defect | Raw ids |
|---|-----|------|---------|--------|---------|
| D1 | BLOCKER | 2 | §4 *Why the elapsed comparison is the discriminator* | `seconds >= ceiling` implies *the bound expired* only if a bound was in force; `CEILINGS_LIVE=0` runs every leg unbounded and the `.leg` row cannot tell the two apart | 18 |
| D2 | HIGH | 2 | §3 Edges, the `consumes-from TOOL-aLeakedHandle-3` bullet | The stated mechanism is refuted by source and by all three specs: `runleg` produces the SECONDS field, unit 3 edits `report_one` and produces nothing this unit reads | 2, 10, 25 |
| D3 | HIGH | 2 | §6 AC5 `fixture:` line, and the same claim in §3 Edges | `GATE_SELFTESTS=1` lifts the HOLD, not the GUARD, so the named invocation cannot refill the window for the leg AC5 names | 11 |
| D4 | MEDIUM | 1 | §2 S5, against §3 and §5 perf/scale | Two new leg rows are declared with no `chunk`, `subject`, guard or ceiling, and §3's *no ceiling is declared* contradicts §5's *a ceiling is declared with its leg row* | 6 |
| D5 | MEDIUM | 2 | §2 S4 and §6 AC7 | The docstring clause §5 risks calls *the whole of the mitigation* — the `--reset` escape — is the half AC7 does not observe | 3 |
| D6 | MEDIUM | 1 | §6 AC2 `Red when:`, against unit 3 §4 | Two specs of one set state opposite mechanisms for the wall-guard kill; unit 1 is right and unit 3's justification sentence is false | 13 |

---

## What this round found, in four sentences

**The fold worked, and it left residue.** Round 1's ten defects are closed; D2, D3 and D5 below are the residue of closing three of them, and each is smaller than what it replaced. D3 in particular is the second unrunnable instruction on the same `fixture:` line, which is worth naming as a pattern rather than a coincidence: a criterion whose observation is expensive gets its recovery instruction written from memory rather than run.

**The blocker is not residue.** D1 was reachable at rev-1 and nobody found it, this round's lens fan included until the fourth lens read `runleg` rather than `derive-ceilings.py`. The spec argues its central design choice at length — *the exit code cannot carry that distinction and the elapsed time can* — and the argument holds only under a premise the runner itself announces it sometimes breaks.

**The unit-1 findings are both about what a document does not say.** D4 leaves four mandatory manifest fields undeclared, and D6 is a correct criterion sitting next to a sibling's false sentence. Neither changes what unit 1 builds.

**Unit 3 was not re-pinned and is not certified by this record.** D6's repair lands in it. Four lenses over two rev-2 documents is a shallower sweep than round 1's four over three rev-1 ones, and the zero findings elsewhere in units 1 and 2 are bounded by that.

---

## Blocker

### D1 — BLOCKER — unit 2 §4, *Why the elapsed comparison is the discriminator, and the exit code is not*

*Raw id 18. Promoted from high: this is the only finding this round that changes code the pass has not written yet.*

The admission rule is `status == ok`, OR `seconds >= the ceiling gate-legs.json declares for that leg today`. §4 reads the second clause as a fact about the run: *a run that reached the ceiling did not stop for anything the leg decided; it stopped because the bound expired, so its seconds are a lower bound on the work.* That inference needs the bound in force at run time to have been the ceiling. Two states break it, and neither is exotic.

**The bound may never have existed.** `run-gates.sh:1393` is `[ "$CEILINGS_LIVE" = 1 ] || bound=0`, and `CEILINGS_LIVE` is a runtime capability probe — `timeout -k 1s 10 true` at line 371. On a host where that probe fails, the runner prints that every declared ceiling is INERT and runs every leg unbounded. A leg that then runs 2000 s under a 900 s ceiling and fails on its own writes `fail 1 2000.0` and is admitted by the new rule as *the bound expired; the seconds bound the work*. That is precisely the failure-duration-as-floor case the `ok`-only filter existed to prevent, and it is the case §4's own table refuses for `govkit selftest`.

**The ceiling may have moved after the row was recorded.** The comparison uses today's manifest number against a historical run. A ceiling lowered from 5400 to 900 retroactively admits every failing row between them.

**The record cannot tell you which happened.** The `.leg` row is written at `run-gates.sh:1425-1426` as name, status, rc, seconds, started, ended, key. The bound goes to `$WORK/<i>.bound`, which is scratch and does not survive into `<git-dir>/gate-run/`. Nothing retained says which bound, or whether any bound, was in force.

**The rule is least sound exactly where it fires hardest.** Under a live bound, `timeout -k 5s "$bound"` caps a row at roughly `ceiling + 5` plus teardown. So a row *materially* above its ceiling is itself evidence that the premise did not hold — and the current predicate admits those with the most enthusiasm, since `>=` is unbounded above.

Consequence, concretely: one such row admitted once holds a monotone floor under that ceiling, `leg ceilings clear their evidenced maximum` reds against a number `--check` reads from the tracked file, and §3 forbids this unit's authors to move the ceiling. Only `--write --reset <leg>` clears it. §4's *What the rule cannot tell apart* names slow, contended and hung; it does not name *the ceiling was never in force*, so neither the docstring AC7 pins nor any non-goal covers this.

**Fix.** Bound the window. Admit a non-`ok` row only when `ceiling <= seconds <= ceiling + 5 + slack`, where the 5 is the `-k` escalation and the slack is the author's number for process teardown on a loaded box. State the number and defend it in §4, and err generous: a too-tight window silently drops the evidence this unit exists to admit, which is the failure it is repairing. Then add the two breaking states by name — `CEILINGS_LIVE=0` and a ceiling edited after a row was recorded — to *What the rule cannot tell apart*, and give the exclusion a `Red when:` in AC1 or AC2 so the upper edge is observed and not merely written.

The alternative — record the bound as an eighth `.leg` field and compare against the bound that actually fired — is the structurally correct fix and is blocked by §3's *no change to what the runner records*. If the author prefers it, that non-goal has to be reopened deliberately rather than worked around.

**Left-shift gate.** An arm in `tools/run-gates/run-gates.evidence.test.sh` whose fixture carries a `fail` row at four times its leg's ceiling, asserted EXCLUDED. That gates the CLASS rather than the 900.240 s instance the spec was written from, and it is the arm that would have caught this predicate at authoring time. Cheap companion, and worth having regardless: make `--report` name the admitted non-`ok` rows beside their ceilings, so an operator can see which rows are riding the new rule instead of inferring it from a maximum.

---

## Highs

### D2 — HIGH — unit 2 §3 Edges, the `consumes-from TOOL-aLeakedHandle-3` bullet

*Raw ids 2, 10 and 25 — three lenses, one bullet.*

The bullet says: *this unit's admission rule reads a `.leg` row's SECONDS field and compares it against the declared ceiling, and unit 3 edits the reporting path that produces that field.* The verb `produces` is false, and every other passage in the set says so.

`runleg` computes `$secs` and writes the seven-field `.leg` row at `run-gates.sh:1408-1428`. `report_one` begins at line 1446, emits a summary line, and writes no `.leg` row at any point. Unit 3's S1 edits the rc=137 branch of `report_one` and nothing else on that path. Unit 3's own §3 says *the ledger is not touched*; its §4 says it *adds a third reader rather than a second source*; its Edges assert that unit 2's rule lands on an unchanged `.leg` row shape. Unit 2's own §4 Data model says *a `.leg` row is written by `runleg`*, and its §3 non-goal says *no change to what the runner records*.

The revision log records how the bullet got there: an orchestrator edit in the fold pass, added to clear check 12's reciprocity arm, and explicitly dressed up — *the mirror is written as a real dependency rather than as bookkeeping.* The reciprocity row IS required; only its justification is invented.

There is a second, quieter cost. `consumes-from` is an ordering assertion, and check 12 reds a target whose `order` is after the consumer — but that arm fires only when both `order` values are non-empty (`check-memory-hygiene.sh:1610-1614`), and `TOOL-aLeakedHandle-3`'s status header carries no `order` at all while this unit is `order 2`. So the edge declares a dependency that nothing sequences, and a reviewer sent looking for a `.leg`-producing change in unit 3's diff finds none.

**Fix.** Keep the head, replace the body with what is true: both units edit `tools/run-gates/run-gates.sh`; unit 3 re-declares no ceiling VALUE and leaves `runleg`'s `.leg` row shape and seconds semantics untouched, and this unit relies on exactly that. Then say plainly that no §6 criterion of this unit consumes anything unit 3 builds — AC1, AC2, AC3, AC6 and AC7 run on built fixtures and AC5 on the live window — so the edge carries no landing order. Unit 1's own `consumes-from` bullet already uses that honest wording; copy its shape.

**Left-shift gate.** The truth of a prose mechanism is not gateable and should not be faked. What is gateable is the shape that produced it: add to the project's §10 checklist that **an edge bullet written to clear a reciprocity red states what the sibling ASSERTS, never a mechanism the sibling implements** — the bookkeeping origin is a reason to write less, not more. A mechanical companion, deliberately NOTE-level rather than red: when a `consumes-from` target carries no `order`, print it. Check 12 is silent there by design (*absence is not disagreement*), and this should report rather than refuse.

### D3 — HIGH — unit 2 §6 AC5 `fixture:` line, and the same claim in §3 Edges

*Raw id 11. Round 1 rated the same criterion's defect HIGH as D4; this is what the fold left.*

AC5 is the unit's only live-tree criterion. Its fixture line says: *a later session restores the reading only with `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and pays that leg's own 900 s bound to do it.* The §3 Edges external bullet repeats it as *the invocation that can*. It cannot.

`memory-hygiene self-test` carries `guard: ["tools/lib/", "tools/memory-tree/"]` in `tools/gate-legs.json` alongside `chunk: selftests` and `subject: kit`. In `run-gates.sh` the hold pass and the guard pass are two separate passes: `GATE_SELFTESTS=1` gets a leg past the `subject = kit || chunk = selftests` hold, and the very next lines still evaluate the guard, whose `changed()` short-circuits on `GATE_FULL` or an unresolvable BASE only — never on `GATE_SELFTESTS`. Unit 2 touches only `tools/run-gates/`, so neither guarded path is dirty, and the leg writes `skip` with no `.leg` row and no reading.

The runner does announce it, as `GATE skip <leg> (unchanged vs <branch>)`, so this is not a silent skip. It is worse in one specific way: the session paid for a selftests bar, got an announced skip, and the spec told it that bar was the recovery.

**Fix.** Name the invocation that lifts both: `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, and say in one clause which flag lifts which pass, so a reader who sets one and sees a skip knows why. Correct the §3 Edges bullet with the same words. Worth adding while there: a direct `bash tools/memory-tree/check-memory-hygiene.test.sh` does NOT work either — only `run-gates.sh` writes `gate-run/*.leg` rows — which is the same *one invocation, deliberately* trap round 1 found in unit 1's AC2.

Note for the contrast, because it is easy to over-correct: AC4's `GATE_SELFTESTS=1` line is CORRECT. `run-gates evidence` guards on `["tools/", "tools/lib/"]`, which this unit's own diff makes dirty. The two criteria differ, and only AC5's is wrong.

**Left-shift gate.** A gotcha record — `GATE_SELFTESTS` lifts the hold, not the guard — under `memory/gotchas/`, which is what puts it in front of the next session automatically: `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` surfaces it for any diff touching `tools/run-gates/`. The mechanical version is round 1's proposed §7 leg-name join extended by one field: when a spec names an invocation for a held leg that ALSO carries a `guard`, require `GATE_FULL=1` in the same clause. `check-spec-tokens.py` already resolves §7 leg names against the manifest, so the join exists and only the guard assertion is new.

---

## Mediums

### D4 — MEDIUM — unit 1 §2 S5, against §3 non-goals and §5 perf/scale

*Raw id 6.*

S5 wires two new legs into `tools/gate-legs.json` and declares no `chunk`, no `subject`, no guard and no ceiling for either, anywhere in the spec. All four are load-bearing: every one of the 104 rows in the live manifest carries `name`, `argv`, `chunk`, `subject` and `ceiling` (61 also carry `guard`), and `tools/run-gates/run-gates.gov.test.sh:260` reds any row whose `ceiling` is absent or not a positive integer.

The spec also contradicts itself about the ceiling. §3 reads *No ceiling is declared, raised or re-derived*; §5 perf/scale reads *a ceiling is declared with its leg row*. Against the manifest the second is compulsory, so a builder following §3 literally ships two rows the gov canary refuses.

The other two fields decide behaviour the spec leaves open. `chunk` and `subject` decide whether the tree scan runs on an ordinary diff-scoped bar and whether the new self-test leg falls under the 2026-08-23 kit-self-test hold. §7's *Two of the legs above are HELD* paragraph answers that question for every pre-existing leg it names and leaves it unanswered for the two this unit mints — the one question a gate-wiring unit owes.

Rated MEDIUM rather than higher because the gov canary is itself `chunk: selftests`: a missing ceiling would not red an ordinary push, and the runner would report the rows on its unbounded-legs line rather than passing them off as bounded. The cost is a spec that cannot be built without a decision it never records.

**Fix.** State each new row's `chunk`, `subject`, guard-or-explicitly-none-with-a-reason (§4 already does exactly that for `codebase-map coverage + freshness`) and its ceiling in S5. Reconcile §3 with §5 by scoping the non-goal to EXISTING ceilings. Add one sentence to §7 saying which of the two new legs an ordinary bar runs.

**Left-shift gate.** Same join round 1 proposed, one field wider: a spec whose §4 files table names `tools/gate-legs.json` must declare `chunk`, `subject`, guard-or-none and `ceiling` for each row it adds. `check-spec-tokens.py` already parses the §4 table and resolves manifest names, so this is a presence assertion over four tokens rather than new machinery.

### D5 — MEDIUM — unit 2 §2 S4 and §6 AC7

*Raw id 3. Demoted from high: this is the exact shape round 1 rated MEDIUM as D7, and rating its residue higher would make the ladder mean nothing.*

S4 and AC7 require `read_runs`'s docstring to state the admission rule and to name slow, contended and hung as the three indistinguishable causes. AC7's `Red when:` reaches only those two — *still describes an `ok`-only filter, or states the rule while omitting what it cannot distinguish*. But §4 says the docstring also carries the `--write --reset <leg>` escape (*the docstring says all of this where the predicate is*), and §5 risks names that escape as the mitigation itself: *Mitigated by `--reset`, which exists and records the choice, and named in `read_runs`'s docstring rather than discovered by the next reader. That docstring is the whole of the mitigation, so AC7 observes it.*

So the half of the docstring that tells a reader what to DO about a surprising row can ship absent with AC7 and every other criterion green. This is not coverage perfectionism: it is verbatim the argument the rev-2 note uses to justify minting AC7 in the first place (*before rev-2 no criterion read it and the mitigation could have shipped absent*), applied one clause over.

**Fix.** Extend S4 and AC7 to require the docstring to name `--write --reset <leg>` as the way to lower an admitted row, and add its absence to AC7's `Red when:`. While there, name the substrings the arm asserts, so the witness grades content rather than a builder's choice of `grep`.

**Left-shift gate.** A §10 checklist entry, since no gate reads intent: **when §5 risks calls a written artefact *the whole of the mitigation*, a criterion names the substrings that artefact must contain.** The half-mechanical version is a lint that flags a §5 risks bullet naming a docstring, comment or record without a §6 criterion citing the same file — cheap, and it would have fired on both D7 and D5.

### D6 — MEDIUM — unit 1 §6 AC2 `Red when:`, against `TOOL-aLeakedHandle-3` §4

*Raw id 13. The pinned half is correct; the repair lands in a spec this round did not pin.*

AC2's third `Red when:` clause says a wall-guard kill means the leg *writes no `.sec` at all, so no row for it is rewritten this run*. Unit 3 §4 says the opposite: *`run_leg_reap` kills the leg's own process and leaves the `runleg` subshell to finish, so `.sec` is written there too.*

Source backs unit 1. `runleg` writes its own `$BASHPID` to `$WORK/<i>.pid` at `run-gates.sh:1366`, with a comment saying exactly why it is `$BASHPID` and not `$$`. The wall watcher feeds that pid to `run_leg_reap`, which calls `remove_descendants`; `scan_descendants` seeds `out=$1` (`run-gates.sh:429`), so the SEED is in the kill set, and `reap.py` walks depth-descending with the target last. The `runleg` subshell dies, `.sec` is never written, the ledger loop's `[ -f "$WORK/$i.sec" ] || continue` at line 1673 skips it, and the awk carry-forward at line 1690 preserves the previous run's row — which is why AC2's clause matters at all: a stale `fail` row surviving a killed run is how an observer records a green from a row the run did not produce.

Unit 3's CONCLUSION survives its false premise, which is why this is a medium and not a high: `report_one` returns early with `(no result)` when `.rc` is absent, so the rc=137 branch is unreachable on the wall path and unit 3's new `.sec` read is safe. It is safe for a different reason than the one written down.

**Fix.** Leave AC2 alone and add a one-line pointer that it contradicts unit 3 §4, so the pair is reconciled before either lands. In unit 3, replace the sentence with the true mechanism: the wall path kills the `runleg` subshell, so `.sec` and `.rc` are both absent and `report_one` reports `(no result)` rather than reaching the 137 branch — the read is safe because the branch is unreachable, not because the file exists.

**Left-shift gate.** A gotcha record: the wall guard kills the `runleg` subshell, so a wall-killed leg writes no `.sec` and the ledger carries its previous row forward. That is a reusable trap about this runner rather than about this build, and `gotchas.py --for-diff` puts it in front of the next diff that touches `run-gates.sh` — which is the only mechanism that would have reached two specs written by two agents on the same afternoon.

---

## What this record does not certify

`TOOL-aLeakedHandle-3` was not pinned and not re-read; its rev-1 clean result from round 1 stands, minus the sentence D6 refutes. Within units 1 and 2, four lenses returned and none died, so the absence of further findings is evidence — bounded by four lenses over two documents, and by a precision of 0.28 that says the sweep was working harder for less than round 1's.

Round 1 proposed three gates it would build; this round would add none of them and would build D1's exclusion arm instead. Of the six defects here, exactly one is mechanically gateable at authoring time (D4), two are already covered by round 1's proposed §7 leg-name join if it is extended by one field (D3, and D4 again), and three want a gotcha or a checklist line because they are claims about mechanism, which no lint reads.

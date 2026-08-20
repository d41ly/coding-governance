# TOOL-aBoundedVerdict-1 — the review loop converges or promotes, and no round is refused by a counter

**Status:** SPECCED · rev-9 · 2026-08-20 · node c · Tier-2 · base 098bebd9 · streams tooling · ratified 2026-08-19

## 1. Goal

The build method's review loop has no reachable exit — over 90 tracked review records the literal
clean verdict it names as the only exit occurs **zero** times, while `BLOCKED` is 36 of 90 and has no
disposition anywhere. Give the loop an exit that CAN be reached: a round ends the loop when its
confirmed blockers are empty or when they stop shrinking, and a blocker that survives that exit
becomes a spec unit in the build and is resolved rather than re-reviewed.

## 2. Scope (IN)

- **S1** — the loop's bound is a CONVERGENCE PREDICATE, not a round count. A round may re-arm the loop
  only if the previous round's fold changed code AND this round's confirmed-blocker set is strictly
  smaller than the previous round's. Two consecutive rounds whose confirmed-blocker count does not
  shrink is NON-CONVERGENT and ends the loop.
- **S1a** — a RUNAWAY CEILING remains, as a driver file constant, and is a backstop rather than the
  mechanism: it exists so a defect in the convergence test cannot produce an unbounded loop. It is set
  well above any observed converging sequence and reaching it is itself a defect worth a halt, not a
  routine outcome. Not a conf key and not an environment variable, on the argument this repo already
  recorded for its agent fan-out bound: a ceiling raisable from the environment leaves no diff behind.
- **S2** — `unattended.sh --review <slug> --subject <id-or-slug> --verdict <TOKEN> --blockers <N>`
  records the round and its confirmed-blocker count, evaluates the convergence predicate, and reports
  which of three states the loop is in: CONVERGING (re-arm), CONVERGED (blockers zero), or
  NON-CONVERGENT (stop). It REFUSES only at the runaway ceiling.
- **S3** — the verdict vocabulary is kit-owned and closed, and an unlisted verdict is refused. The
  method names three tokens in prose and no machine anywhere reads them; the corpus carries eighteen
  distinct verdict lines, five leading tokens, and 32 records with no verdict line at all.
  `TOOL-aBoundedVerdict-2` owns making that token a REQUIRED first line of a review record; this unit
  owns only the set the verb accepts, and the two must name the same set.
- **S4** — a round is recorded as one line in the PARKED region under a `review` KIND, through the
  existing park helper unchanged, carrying the subject, the verdict and the blocker count. The
  sequence is the number of `review` lines naming that subject. **No new authored fact**, so the
  region's fact pin does not move here: an append-only history of rounds is exactly what a park kind
  is for, and a tracked sibling spec set the precedent by adding a kind rather than a field for the
  same reason. `TOOL-aBoundedVerdict-2` takes the FACT route for the halt code, which is a per-run
  singleton read by key, and the two shapes are chosen deliberately rather than for consistency. The
  helper's output leads with a timestamp, so the region's anchor ban is satisfied by construction.
- **S4a** — the `review` kind is a **record** kind — the class `TOOL-aBoundedVerdict-5` S7 names and
  owns. Its surfaced-count refusal counts DECISION kinds only, so review rounds do not inflate the
  count of decisions the owner must be shown. The two class names are `decision` and `record`, taken
  verbatim from the owning spec rather than paraphrased here.
- **S5** — the SUBJECT is the spec document for a method spec-audit round, and the BUILD SLUG for the
  method's closing diff review. One predicate, two denominators, because the two review kinds have two
  denominators and a single per-unit rule would price a build-level event on a unit-level count.
- **S6** — a leg check in `check-unattended.sh`: for every tracked run-state file, the `review` lines
  in the parked region are grouped by their `item` field, no group exceeds the runaway ceiling read
  FROM the driver, and no group's blocker counts are non-decreasing across more than two consecutive
  rounds without a terminal disposition line. **There is no round-count fact to parse** — the sequence
  is derived from the line set, and the only grammar the leg splits is the park helper's own output.
- **S7** — the build method's review sections gain the stated disposition for a blocked verdict, the
  convergence rule, and the clarification that folding a round's own fixes does not by itself re-arm
  the loop. Method rules binding on any run; the convergence predicate is machine-checked in the
  driver for unattended runs and advisory for attended ones.
- **S7a** — the method's WRAP-UP derivation row is narrowed to DECISION-kind parked entries, handed to
  this unit by `TOOL-aBoundedVerdict-5` S7c because this unit already has the method in its write set
  and lands after the taxonomy exists. The row today says every parked entry with its question,
  options and reason — a shape a `review` line does not carry — so without the narrowing the wrap-up
  would demand three fields of a line that has two. This is the only place in the set that edits that
  row, and no other spec may claim it.
- **S8** — **at the exit, every confirmed unfixed blocker is PROMOTED to a spec unit in this build**,
  specced at its tier, built, and closed. It is not parked, not waived, and not re-reviewed. This is
  legal under M6's pass vocabulary already — "a spec authored" and "a unit built" are both passes —
  and it is made legal in the kit by `TOOL-aBoundedVerdict-11`, whose comparison of the generated
  units region's unit-ID SET (BASE ⊆ HEAD) is what lets a run add a unit without failing the
  non-overridable authorization check. That comparison is over IDS, not row bytes, and it must stay
  so: the region carries each unit's status and rev, which move as this unit's own promotions are
  built, so a byte-level test would refuse the run that promoted.
- **S8a** — a promoted unit is reviewed as a SPEC (M4), not by re-running the closing diff review.
  That is the whole reason promotion terminates: a spec audit is one unit's document, and the closing
  diff review runs once more at the end, scoped to the fold per `TOOL-aBoundedVerdict-14`.
- **S10** — **the ceiling firing is REPORTED, not just survived.** Under F4's resolution the run
  promotes and lands when the runaway ceiling is reached, so the ceiling stops being a halt and becomes
  a fact that must not be quiet. Two carriers, both required:
  - the run's OWN OUTPUT says the ceiling was reached, names the subject, the sequence length and the
    ceiling, and says in one sentence that the convergence predicate did not terminate — the same
    message the halt would have carried, on a path that continues;
  - the BUILD README gains a line recording it, so the fact outlives the transcript nobody reads. It
    is written where the wrap-up derives from, which is what makes M9's "problems resolved" row able
    to cite it.
  A ceiling reached with neither carrier written is the defect this scope item exists to prevent, and
  it is the one thing about the ceiling path that IS gate-checkable: the leg asserts that a run-state
  file whose review sequence reached the ceiling has both.
- **S9** — a blocker that cannot be promoted — because resolving it is outside the mandate's scope, or
  because it names a unit whose options differ in what gets built — is a PARK and the build does not
  close. This is the residual case S8 does not cover and it must be stated, or "promote everything"
  becomes a licence to widen scope without an owner.

## 3. Non-goals (OUT)

- **No cap on attended runs.** The owner decided this, shown the measurement that thirteen of
  forty-three build folders hold no review record at all on a green gate, re-measured at the merge
  base. Nothing here adds a required field to a review record, a date-cutoff ratchet, or a waiver pass
  over the existing corpus.
- **No round CAP as the loop's mechanism.** Withdrawn at rev-6 on the owner's instruction. The
  runaway ceiling in S1a is not that mechanism wearing a new name: it is a backstop that a correct
  convergence test never reaches, and the spec says plainly that reaching it is a defect. Under F4's
  resolution it does not stop the run either — it is a REPORTED defect, not a halt, so the ceiling is
  not a cap in any sense that could stall a build.
- No join from a review record on disk to the unit it reviewed. The filename carries a per-build
  counter, the driver already refuses that join in its own source having measured it wrong on seven of
  seven multi-unit builds, and this unit does not retry it.
- No parse of a review record's verdict heading. `TOOL-aBoundedVerdict-2` owns making a token
  REQUIRED going forward; retrofitting the corpus's eighteen spellings is not in any unit here.
- No change to the review harness's fan-out or concurrency caps. Those are a different bound over a
  different thing and are already enforced at the tool call.
- No claim that the sequence is unforgeable. The run calls the verb, so the run controls the record.
  §4 states the boundary rather than implying one.
- Not the fold-scoping of round N. `TOOL-aBoundedVerdict-14` owns it, and it is what makes this unit's
  convergence affordable rather than merely bounded.

## 4. Design

### Why the cap was withdrawn, measured

`grep -rh '^## Verdict' memory/builds/*/reviews/*.md` over 90 records:

| verdict | records |
|---|---|
| `BLOCKED`, bare or suffixed | 36 |
| `CLEAN WITH FIXES` | 6 |
| **`CLEAN`** | **0** |
| a bare `## Verdict` heading with no token | 9 |
| outside the method's three | 6 |
| no verdict line at all | 32 |

`BUILD-METHOD.md:104-105` states the only exit: once a synthesis pass calls the design clean, stop
reviewing. The token that satisfies it has never been written here. So the loop's engine is not a
missing count — it is an exit condition with a 0/90 hit rate and a most-common outcome with no rule.
A cap does not add an exit; it relocates the stall. `dClosedLexicon` holds 10 review records in one
day and reached ABORTED; a cap of two would have stopped it at round two with the same blockers and
the same absence of a next move.

### The convergence predicate

State is derived from the `review` line sequence for one subject, newest last:

```
blockers(N) == 0                          -> CONVERGED    (exit, clean)
blockers(N) <  blockers(N-1)              -> CONVERGING   (re-arm)
blockers(N) >= blockers(N-1)              -> NON-CONVERGENT (exit, promote)
N == 1                                    -> CONVERGING   (a first round always re-arms if blockers > 0)
sequence length == RUNAWAY_CEILING        -> CEILING: report loudly (S10), then promote and land
```

`dClosedLexicon`'s measured sequence was 1, 1, 2, 1, 2 across rounds 2-7 — non-decreasing at round 3
and again at round 5, so this predicate exits at round 3 with one blocker to promote, against the six
consecutive blocked rounds that actually happened.

**Strictly smaller, not merely different.** An oscillating count (2, 1, 2, 1) is the shape that
defeats a "changed" test, and it is present in the corpus.

### Why promotion terminates, and the honest limit

A promoted unit is new code, which earns a diff, which could earn a new closing round. The bound is
not a counter — it is the KIND of review each thing gets:

- the closing DIFF review runs once from the pinned BASE, then once per fold, fold-scoped;
- a promoted UNIT is reviewed as a spec (M4), which is one document and does not re-scan the build.

So work added by promotion is priced at spec-audit cost, and the diff review's scope shrinks each
round rather than repeating. **This is the unit's central claim and it is not proven by construction.**
The residual: a promotion whose fix introduces a blocker in the fold gets one more fold-scoped round,
and if THAT does not converge, its blocker promotes again. The sequence terminates only if each
promotion is smaller than the one before, which is likely and is not guaranteed. S1a's ceiling is what
stands behind it, and F4 is where the owner gets told if the ceiling is ever reached in practice.

### Data model

One appended line per round, in the PARKED region, under a `review` kind:

| Field | Value |
|---|---|
| kind | `review` — a `record` kind, per `TOOL-aBoundedVerdict-5`'s taxonomy |
| item | the subject: a spec document for a spec-audit round, the build slug for the closing round |
| reason | the verdict token, then the confirmed-blocker count |

The sequence is derived, not stored. Rev-1 made these AUTHORED FACTS, one key per subject, which was
wrong twice over: the binding protocol pins the authored region at a closed enumerated set of facts
and rev-1 would have added to it without naming or moving the pin, and a round history is append-only
where a fact is a mutable singleton.

The blocker COUNT is the one new field this design needs, and it rides the existing `reason` field
rather than becoming a fourth: the park helper appends one line whose last field is free text, and the
leg already splits only that helper's own grammar.

### The boundary, stated

The run calls `--review` and the run authors the run-state file, so a run that never calls the verb is
unmeasured, and one that reports a shrinking blocker count it did not earn converges on paper. This is
the same boundary the protocol's section nine draws for every other authored fact and the same one the
two agent-attested Definition-of-Done items already accept. What the mechanism buys is that stopping
becomes a recorded, dated, reviewable act with a stated next move, rather than the default behaviour of
a run following the method faithfully — which is what the measured ten-round loop was. It does not buy
prevention, and no document in this build may imply that it does.

### Inventory

| Concern | Today | After |
|---|---|---|
| the loop's exit | a verdict token with a 0/90 hit rate | a predicate over the blocker sequence |
| what a blocked verdict means | unstated | the method states it; the driver computes it |
| what bounds the loop | nothing, repo-wide | convergence, with a ceiling as a backstop |
| a residual blocker | re-reviewed forever, or an ABORTED run with no readable reason | promoted to a unit and resolved |
| a blocker outside the mandate | indistinguishable from any other | a park, and the build does not close |
| the verdict vocabulary | prose in the method, 18 spellings in the corpus | a closed set the verb refuses outside of |

### Migration

None on disk. No existing run-state file carries a `review` parked line, and S6 bounds the groups that
are present rather than asserting any exist — so today's corpus passes unchanged. That makes the check
VACUOUS over the current tree, which this repo names as its own bug class, so the arm is not the
corpus: it is explicit red and green fixtures in the leg's sibling test, the same disposition the
streams ratchet took for the same reason.

### Rollout

`TOOL-aBoundedVerdict-2`'s vocabulary first — S3 refuses outside a set that unit defines. Then
`TOOL-aBoundedVerdict-11`, because S8's promotion is refused by the authorization check until that
unit lands. Then this unit's verb and predicate, then the leg check, then the method prose.
`TOOL-aBoundedVerdict-14` may land at any point and is what makes the rounds cheap.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the verb, the predicate, the ceiling constant) ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` (S6) · `memory/guides/BUILD-METHOD.md` and
`tools/memory-tree/BUILD-METHOD.template.md` (S7, S7a, both halves) ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the verb table) ·
`tools/unattended/SKILL.template.md` and the rendered Skill · `tools/memory-tree/README.md` (receiving
any displaced paragraph) · `.memory-tree.conf` (`ARMS_FLOORS`) · the kit version constants ·
`memory/map/features/build-method.md` and `memory/map/features/unattended.md`.

### The read-path budget

`memory/guides/BUILD-METHOD.md` is 17460 bytes at this base and the hygiene cap for a
`memory/guides/` file is 61440 bytes, so the file is at 28% of the gated cap. The 20 KB and 250-line
figures are the method's OWN self-declaration, which no gate reads for a guide — the two classes were
split by a recorded decision. So the displacement obligation is EDITORIAL, not mechanical: it exists
because M7 re-reads the file whole at every pass boundary, and no gate will catch a failure to honour
it.

The budget that IS mechanical is the charter read-path ceiling: measured at this base at **91997 bytes
against a ceiling of 112987 — 20990 bytes of headroom**. `LIVE.md` is generated, so the total drifts
between renders and the figure is a snapshot, never an allowance. It is shared by more units than
before: this unit and `TOOL-aBoundedVerdict-3` grow the method; `TOOL-aBoundedVerdict-2`, `-3`, `-5`
and `-11` grow the unattended protocol at 27582 bytes; `TOOL-aBoundedVerdict-14` grows the method
again. The spender set is stated ONCE, in the README's cross-unit rules, and the builder re-measures
with `python tools/memory-tree/corpus_ids.py --report` before spending rather than treating either
figure as authority.

### Alternatives rejected

- **The two-round cap.** The rev-1 through rev-5 design. Withdrawn by the owner and refuted by its own
  measurement: it bounds the loop without giving it an exit, so it converts a late stall into an early
  one. Kept only as S1a's backstop, explicitly not as the mechanism.
- **Park the residual blockers and land.** Offered to the owner and refused. It closes the build with
  known blockers on the record, which is a different product than a build that resolved them.
- **Halt for the owner on non-convergence.** Also refused: it makes the stall explicit and readable
  but it is still the stall being reported.
- **Severity-split — fold-caused blockers halt, pre-existing ones park.** Refused on the judgement it
  needs: provenance per finding is something the harness cannot determine reliably, and a
  misclassification sends a real blocker to a park.
- **Derive convergence from the spec's rev number.** The only per-unit monotone number that exists
  today, and it counts the wrong thing: a rev bumps for any material change, review-driven or not.
- **Count from review records on disk.** Every evasion is legal under the live filename predicate, the
  sequence is unbounded, a family-qualified record is ambiguous with a unit id, and filing the review
  one folder over changes its kind. Rejected, and the driver's own source already rejects the
  underlying join.
- **A conf key for the ceiling.** Rejected on S1a's reused argument.
- **Refuse the round at the review harness instead of the driver.** The harness reviews diffs and
  cannot perform a method spec audit at all, so it sees at most one of the two review kinds.

## 5. Production-readiness checklist

- **security** — N/A as a surface. The trust boundary is stated in §4 rather than left implicit. One
  note: S8's promotion widens what a run may add to its own build, and the property that keeps it
  honest lives in `TOOL-aBoundedVerdict-11`'s unit-ID-set comparison, not here.
- **perf / scale** — N/A. One appended line per round; the predicate reads a bounded line set.
- **a11y** — N/A.
- **i18n** — the verdict tokens are identifiers.
- **error / empty / loading states** — a review on a slug with no run-state file, an unlisted verdict, a
  missing subject or blocker count, a sequence at the ceiling, and a terminal record are five distinct
  refusals. The empty case that matters: a FIRST round must not read as non-convergent for want of a
  predecessor, which the predicate's `N == 1` arm handles explicitly.
- **observability** — the verb reports the loop state by name on every call, so a run knows whether it
  is re-arming, exiting clean, or promoting. That report is the observation this unit is graded on.
- **risks** — the highest is now the inverse of rev-5's: not that the exit is unreachable, but that
  promotion does not terminate. §4 states that limit and does not claim otherwise. Second: a run that
  reports a shrinking count it did not earn, which §4's boundary covers. Third: S9's park case being
  used as an escape from ordinary work, which the method prose must phrase as a scope test rather than
  a difficulty test.
- **testing + left-shift gates** — the leg check plus red and green fixtures, an arm per refusal, and
  one arm per state of the predicate including the oscillating sequence. The left-shift for the
  vacuity risk is the fixture pair, not the corpus.
- **migration / rollback** — none needed; rollback removes the verb, the predicate and the check, and
  existing records are unaffected either way.
- **user docs** — the protocol's verb table, the rendered Skill, and the method's review sections.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --review <slug> --subject <id> --verdict BLOCKED
  --blockers 2` follows a round that reported 2, the verb reports `NON-CONVERGENT` and names promotion
  as the next move; when it follows a round that reported 3, it reports `CONVERGING`. Two arms in
  `tools/unattended/unattended.test.sh`.
- **AC1a** — When a sequence oscillates 2, 1, 2, the third call reports `NON-CONVERGENT` — the arm that
  fails under a "count changed" predicate and passes only under strictly-smaller.
- **AC1b** — When the FIRST round for a subject reports blockers above zero, the verb reports
  `CONVERGING` and not `NON-CONVERGENT`; the empty-predecessor arm.
- **AC2** — When a round reports `--blockers 0`, the verb reports `CONVERGED` and the loop's exit is
  recorded on disk as a `review` line whose reason carries the token and the count.
- **AC2a** — When a run reaches the runaway ceiling, `--review` reports `CEILING` naming the subject,
  the sequence length and the ceiling, and states that the convergence predicate did not terminate; the
  round IS recorded and the run is NOT refused. Rev-8: this criterion asserted a refusal until the
  owner resolved F4 the other way.
- **AC2b** — When the ceiling has been reached, the build README carries the line S10 requires, and
  `bash tools/unattended/check-unattended.sh` reds against a fixture whose review sequence reached the
  ceiling with no such line — the arm that makes the loud-reporting half enforceable rather than
  advisory.
- **AC3** — When the verdict is outside the kit-owned set,
  `bash tools/unattended/unattended.sh --review <slug> --subject <id> --verdict MAYBE` refuses naming
  the legal set, and that set is byte-identical to the one `TOOL-aBoundedVerdict-2` defines.
- **AC3a** — When a run-state file carries `review` lines for one subject and `decision` lines for
  another, `bash tools/unattended/unattended.sh --close <slug>` counts only the DECISION-kind lines
  against the attestation — the fixture carries at least one line of each class, so the arm fails under
  a count of all parked lines and passes only under the taxonomy-aware one.
- **AC4** — When a tracked run-state file carries a `review` group whose blocker counts are
  non-decreasing across three consecutive rounds with no terminal disposition,
  `bash tools/unattended/check-unattended.sh` reds naming the file and the subject; both the red and the
  green fixture live in `tools/unattended/check-unattended.test.sh`, because the corpus exercises
  neither.
- **AC5** — When the leg reads the ceiling, it reads it from the driver:
  `grep -c 'RUNAWAY' tools/unattended/check-unattended.sh` counts no assignment of its own.
- **AC6** — When the method's review sections are read, they state the blocked-verdict disposition, the
  convergence rule and the promotion rule; any paragraph displaced to make room is absent from
  `memory/guides/BUILD-METHOD.md` and present in `tools/memory-tree/README.md`; and
  `python tools/memory-tree/corpus_ids.py --report` shows the read path still under its ceiling.
- **AC7** — When the method template and the installed copy are compared,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green.
- **AC8** — When a promotion is exercised end to end on a fixture, the run adds a unit row to the
  generated units region, `check_authorization` returns 0, and `--close` does not refuse on
  `authorization-reachable` — the arm that joins this unit to `TOOL-aBoundedVerdict-11` and fails
  without it.
- **AC9** — `python tools/memory-tree/check-arms.py` exits 0 with the unattended `ARMS_FLOORS` entries
  raised, and `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/check-kit-versions.sh` · `python tools/memory-tree/check-arms.py` ·
`python tools/codebase-map/test_codebase_map.py` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — how does the closing DIFF review's subject interact with the predicate?** At rev-5 this fork
  asked whether the cap bound the closing review at two rounds; the owner answered "two, uniformly"
  and that answer died with the cap. Re-opened in the new frame: the closing review's subject is the
  build slug, so its blocker sequence is one sequence for the whole build, and a fold that fixes unit A
  while unit B's blocker stands reads as non-decreasing. Options: keep one build-level sequence and
  accept that a mixed fold exits early to promotion; or key the closing review's sequence by the
  FINDING set rather than the count. **Recommendation: one build-level sequence.** Exiting early to
  promotion is not a failure under S8 — promotion resolves the blocker either way, and a
  finding-keyed sequence needs a stable finding identity across rounds that the harness does not
  provide.
  RESOLVED (agent, 2026-08-19, delegated): one build-level sequence, on the recommendation's grounds.
  Mechanism-only fork; both options resolve the blocker and one needs an identity the harness cannot
  supply.

- **F2 — is the verdict token recorded, or only the blocker count?** The count alone drives the
  predicate. The token is what lets S8's disposition be chosen without re-reading the review record and
  what lets a later check ask whether an exited subject was disposed of. **Recommendation: both**, as
  S4 specifies.
  RESOLVED (agent, 2026-08-20, delegated): BOTH — the count drives the predicate and the token is
  recorded beside it. Mechanism-only fork, and the feature-rich survivor: the count alone cannot
  answer whether an exited subject was disposed of, which is exactly what F3's check needs.

- **F3 — should the leg assert that an EXITED subject was actually disposed of?** At rev-5 this was
  deferred because the disposition spanned three units' mechanisms. Under rev-6 the disposition is a
  promotion, which leaves an observable trace — a new unit row in the generated region — so the check
  is now writable. **Recommendation: yes, and it is S6's third clause.** It supersedes the backlog row
  `TOOL-aBoundedVerdict-8`, which said to write this once all three mechanisms landed; there are now
  two, and one of them is observable.
  RESOLVED (agent, 2026-08-20, delegated): YES, as S6's third clause, and it supersedes the backlog
  row named above. Mechanism-only: the promotion leaves a unit row in the generated region, so the
  assertion has a real subject rather than the prose-caller grep this repo has found vacuous twice.

- **F4 — what happens the first time the runaway ceiling is reached?** §4 states plainly that
  promotion's termination is likely and not guaranteed. Options put to the owner: halt to the owner;
  promote and land anyway; abort the run.
  RESOLVED (owner, 2026-08-19): **promote and land anyway, and say loudly what happened** — in the
  run's own output AND in the build README. S10 is the mechanism. The reasoning the owner's answer
  rests on, recorded because it overrides this spec's own recommendation: a ceiling firing is a defect
  in the PREDICATE, not a reason to keep the build's finished work off `main`, and the objection that
  "nobody finds out" is answered by making the finding-out mandatory in two carriers rather than by
  stalling.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records the owner's decision that the cap binds unattended runs
  only, taken on the measurement in §3.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. The round count and last verdict were
  specced as authored FACTS in a region the binding protocol pins closed; they become lines under a new
  non-decision park kind. The size-budget paragraph and AC6 rested on a false premise about the gated
  cap. The floor-key rejection rested on a false claim about the existing parser.
- rev-3 · 2026-08-16 · folded round 2, which found the rev-2 fold had not reached the whole spec: S6
  still specified the leg check over a round-count FACT the data model had deleted, and four further
  sites still described the fact shape.
- rev-4 · 2026-08-17 · pre-ratification pass.
- rev-5 · 2026-08-17 · ratified.
- rev-6 · 2026-08-19 · **the cap is withdrawn on the owner's instruction and replaced by a convergence
  predicate, and the residual-blocker disposition becomes PROMOTION to a spec unit.** Grounds are
  measured, not argued: the method's only stated exit occurs 0 times in 90 review records while
  `BLOCKED` is 36, so a count bounded a loop that had no exit and moved the stall earlier — which is
  the failure the owner reported. Changes: the title and §1; S1 becomes the predicate and S1a demotes
  the constant to a backstop that reaching is itself a defect; S2 gains `--blockers` and reports a loop
  state instead of refusing a round; S6 gains the non-decreasing clause; S8 becomes promotion and
  **its rev-5 wording is deleted for cause** — the close-path audit found "when the remaining units do
  not depend on it" vacuously true at the closing review, so the literal reading landed a BLOCKED diff
  and the intended one aborted without landing; S9 is new and carries the residual park case that
  "promote everything" would otherwise hide. §4 gains the withdrawal measurement, the predicate with
  `dClosedLexicon`'s real sequence replayed against it, and an explicit statement that promotion's
  termination is likely and unproven. F1 is re-opened in the new frame and resolved; F3 becomes
  writable and supersedes a backlog row; F4 is new and is the owner's. The read-path figures are
  re-measured at this base rather than carried.
- rev-7 · 2026-08-19 · the M4 spec audit's count correction, folded before any code. `BLOCKED` is
  **36** of 90, not 38: the first count read a `uniq -c` listing and absorbed the two records whose
  `## Verdict …` line is a SECTION HEADING (`Verdict up front`, `Verdict and landing order`) into the
  suffixed-BLOCKED group. Re-derived with an anchored token match. The argument is unchanged and the
  headline number was never the disputed one — bare `CLEAN` is 0 of 90, re-verified — but a spec that
  will be built from may not carry a number that does not reproduce.

- rev-8 · 2026-08-19 · **F4 resolved by the owner, against this spec's own recommendation, and the
  reversal is recorded rather than smoothed over.** The spec recommended halting to the owner; the
  owner chose promote-and-land with a loud statement in the run's output and in the build README. The
  grounds, as put: a ceiling firing is a defect in the predicate, not a reason to keep finished work
  off `main`, and "nobody finds out" is answered by making the finding-out mandatory in two carriers
  instead of by stalling. S10 is new and carries both carriers plus the one gate-checkable half — a
  sequence that reached the ceiling with no README line reds. AC2a is INVERTED: it asserted a refusal,
  and the ceiling no longer refuses. AC2b is new. §3's runaway-ceiling non-goal now says the ceiling
  cannot stall a build in any sense, which is a stronger claim than rev-6 could make.

- rev-9 · 2026-08-20 · M3 fork sweep, before any code. F2 and F3 RESOLVED under the delegated rule —
  both were mechanism-only with a stated recommendation and no veto reached either. §8's first
  non-blank line is now the machine-legal `none` form, without which this spec reds hygiene the
  moment its status goes terminal, which is the failure mode `TOOL-aBoundedVerdict-4` exists to make
  impossible to reach silently. No scope change; no acceptance criterion moved.

## 10. Reuse audit

The seam is `park()` and the parked region's kind taxonomy — this unit adds a kind, not a writer, and
`verb_park` already exists in the driver under `TOOL-cSettledDocket-1`, which shipped the verb
`TOOL-aBoundedVerdict-5` specced. That divergence is real and is recorded against unit 5 rather than
here.

The second seam, new at rev-6, is `TOOL-aBoundedVerdict-11`'s unit-ID-set comparison of the
generated units region. S8's promotion is not implementable without it: `check_authorization` refuses a
run that changes its own roster, and `verb_close` refuses to override that item. Naming the dependency
here is what keeps this unit from re-deriving a scope-integrity mechanism it does not own.

`python tools/codebase-map/reuse_lookup.py "resolve a blocked review verdict and close an unattended
run"` returned `.unattended.conf` and `UNATTENDED-PROTOCOL.md` as affordance seams and no symbol-level
seam for verdict handling — recorded as the probe's answer. Recall terms used: `closing review round
cap blocked verdict adversarial diff fold unattended close build-complete DoD stall halt`.

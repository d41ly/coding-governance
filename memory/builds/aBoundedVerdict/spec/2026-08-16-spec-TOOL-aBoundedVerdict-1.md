# TOOL-aBoundedVerdict-1 — the review loop converges or promotes, and no round is refused by a counter

**Status:** CLOSED · rev-12 · 2026-08-21 · node c · Tier-2 · base 098bebd9 · streams tooling · ratified 2026-08-19

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
  NON-CONVERGENT (stop). It refuses an unlisted verdict, a missing subject or blocker count, and a
  round on a subject whose group has already terminated; it does NOT refuse at the runaway ceiling,
  which under F4 is reported and survived (S10).
- **S3** — the verdict vocabulary is kit-owned and closed, and an unlisted verdict is refused. **The
  set is exactly three members: `CLEAN`, `CLEAN WITH FIXES`, `BLOCKED`** — the three the build method
  already names in its review-recording rule, and the floor for any later addition. No machine
  anywhere reads them today: the corpus carries eighteen distinct verdict lines, five leading tokens,
  and 32 records with no verdict line at all.
  **The canonical owner is the MEMORY-TREE kit**, because that kit is what enforces review-record
  grammar (`memory/HYGIENE.md` check 5 and `tools/memory-tree/check-memory-hygiene.sh`) and what
  renders `memory/guides/BUILD-METHOD.md`. The unattended kit cannot import from it — a
  copy-installed kit carries what it needs inline — so the driver's set is a STATED duplication of
  the memory-tree one, and the drift is ARMED rather than hoped away: one row in the case table
  `tools/memory-tree/marker-contract.test.sh` already carries, which is the same harness
  `TOOL-aBoundedVerdict-4` S2 extends. One harness, no new gate leg, and no cross-kit import.
  `TOOL-aBoundedVerdict-2` owns making that token a REQUIRED first line of a review record; this unit
  owns only the set the verb accepts, and the two spell the same three members.
- **S4** — a round is recorded as one line in the PARKED region under a `review` KIND, through the
  existing park helper unchanged, carrying the subject, the verdict and the blocker count. The
  sequence is the number of `review` lines naming that subject. **The TERMINAL LINE, defined once
  here and nowhere else:** when the predicate EXITS on a round, the verb writes the exit token it
  reported — `CONVERGED`, `NON-CONVERGENT` or `CEILING` — into that same free-text `reason` field,
  after the verdict and the count. A group's terminal line is the line whose reason carries an exit
  token, and that is the ONE observable S6 and AC4 use for "the loop stopped here". It adds no field,
  no new grammar and no new computation: S2 already derives and reports the token, and the leg still
  splits only the park helper's own output. The promoted-unit row F3 asserts on is a DIFFERENT
  observable, used by S6's third clause alone, and the two are not interchangeable. **No new authored
  fact**, so the region's fact pin does not move here: an append-only history of rounds is what a kind
  is for, and a tracked sibling spec set the precedent by adding a kind rather than a field for the
  same reason. `TOOL-aBoundedVerdict-2` takes the FACT route for the halt code, which is a per-run
  singleton read by key, and the two shapes are chosen deliberately rather than for consistency. The
  helper's output leads with a timestamp, so the region's anchor ban is satisfied by construction.
- **S4a** — the `review` kind is a **`history`** kind. The two CLASS names are `surfaced` and
  `history`, owned by `TOOL-aBoundedVerdict-5` S7 and taken verbatim from it rather than paraphrased
  here — the split exists because "decision" was doing duty as both a KIND token and a class name.
  The surfaced-count refusal counts `surfaced`-class kinds only, read from the one driver constant
  that holds that set, so review rounds do not inflate the count the owner must be shown. **The
  shipped counter is correct today** — every live kind is `surfaced`, waiver included — and it becomes
  wrong on the day this unit lands the first `history` kind. That is the whole reason the taxonomy
  must exist before this unit's verb, and it is why the Rollout sequences `TOOL-aBoundedVerdict-5`
  ahead of it. No claim of a present inflation is made here.
- **S5** — the SUBJECT is the spec document for a method spec-audit round, and the BUILD SLUG for the
  method's closing diff review. One predicate, two denominators, because the two review kinds have two
  denominators and a single per-unit rule would price a build-level event on a unit-level count.
- **S6** — a leg check in `check-unattended.sh`: for every tracked run-state file, the `review` lines
  in the parked region are grouped by their `item` field, no group exceeds the runaway ceiling read
  FROM the driver, and no group's blocker counts are non-decreasing across more than two consecutive
  rounds unless that group carries a TERMINAL LINE as S4 defines it. Its third clause is F3's: an
  exited subject was actually disposed of, observed as a unit row in the generated units region.
  **There is no round-count fact to parse** — the sequence is derived from the line set, and the only
  grammar the leg splits is the park helper's own output.
- **S7** — the build method's review sections gain the stated disposition for a blocked verdict, the
  convergence rule, and the clarification that folding a round's own fixes does not by itself re-arm
  the loop. Method rules binding on any run; the convergence predicate is machine-checked in the
  driver for unattended runs and advisory for attended ones.
- **S7a** — the method's WRAP-UP derivation row is narrowed to `surfaced`-class parked entries,
  handed to this unit by `TOOL-aBoundedVerdict-5` S7c because this unit already has the method in its
  write set and lands after the taxonomy exists. The row today says every parked entry with its question,
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
  A ceiling reached with neither carrier written is the defect this scope item exists to prevent.
  **One carrier per observer, because no gate can watch a transcript:** the LEG asserts the README
  line against a run-state file whose review sequence reached the ceiling (AC2b), and the run's own
  output line is observed at the verb by AC2a. Nothing here asks a gate to grade stdout.
- **S9** — a blocker that cannot be promoted — because resolving it is outside the mandate's scope, or
  because it names a unit whose options differ in what gets built — is a PARK and the build does not
  close. This is the residual case S8 does not cover and it must be stated, or "promote everything"
  becomes a licence to widen scope without an owner. **The non-close half is ADVISORY method prose,
  not a driver refusal:** `--close` does not refuse on a parked blocker, and making it refuse would be
  a new close-path predicate this unit does not own. What IS graded is the prose itself — AC6a — and
  the test it must state is a SCOPE test, never a difficulty test, which is the failure mode that
  turns this clause into an escape hatch.

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
A cap does not add an exit; it relocates the stall. `dClosedLexicon` holds 10 review records across
two days, 8 of them on 2026-08-16, and reached ABORTED; a cap of two would have stopped it at round
two with the same blockers and the same absence of a next move.

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
| kind | `review` — a `history` kind, per `TOOL-aBoundedVerdict-5`'s taxonomy |
| item | the subject: a spec document for a spec-audit round, the build slug for the closing round |
| reason | the verdict token, then the confirmed-blocker count, then the exit token on a terminal line (S4) |

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

In the build README's dependency order, three units precede this one and all three are hard:

- `TOOL-aBoundedVerdict-11`, because S8's promotion is refused by the authorization check until that
  unit lands.
- `TOOL-aBoundedVerdict-5`, because S4a takes its `surfaced`/`history` class names by name and AC3a
  grades its class-aware counter. A builder working an older Rollout that omitted it would implement
  the `review` kind before the taxonomy that classifies it exists, which is exactly the day the
  shipped counter starts over-counting.
- `TOOL-aBoundedVerdict-2`'s vocabulary, because S3 refuses outside a set that unit makes required.

Then this unit's verb and predicate, then the leg check, then the method prose.
`TOOL-aBoundedVerdict-14` may land at any point and is what makes the rounds cheap.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — the verb, the predicate, the ceiling constant, and the exit
  token S4 puts in the `reason` field.
- `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.sh` and
  `check-unattended.test.sh` (S6) — **including the leg's header check COUNT, moved one past the
  value `TOOL-aBoundedVerdict-2` leaves.** That header line is the ONLY carrier of the figure: the
  charter's gate-suite enumeration no longer exists (it was replaced by a pointer at
  `tools/gate-legs.json`) and the charter body is generated between `gov:playbook` markers, so a
  hand-edit there reds the playbook parity leg and a template edit is out of scope. Do not recreate
  that bullet. AC10 grades the header.
- `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` — S7, S7a and
  S9's advisory park case, both halves.
- `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` — the verb table.
- `tools/memory-tree/marker-contract.test.sh` — the one case-table row that arms the verdict-set
  duplication S3 states.
- `tools/memory-tree/README.md` — receiving any displaced paragraph.
- `.memory-tree.conf` (`ARMS_FLOORS`).
- `memory/backlog/TOOL.md` — row `TOOL-aBoundedVerdict-8` is superseded by this unit; F3 states the
  new status and the superseding text.
- `memory/guides/SESSION-KICKOFF.md` — `.memory-tree.conf` and `memory/guides/BUILD-METHOD.md` are
  both on the kickoff manifest's watch list (the list is that file's manifest-audit block), so the
  claims derived from them are re-audited and `last-audit` re-stamped in the SAME commit as this
  unit's change. The ratchet is a merge-bar leg and reds a watched file changed without the re-stamp.
- the kit version bump, which is NOT one carrier: `KIT_UNATTENDED_VERSION=` **and** its same-line
  `gov:kit` marker in both `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh`; the `gov:kit` marker in
  `tools/unattended/PROTOCOL.template.md` and in `tools/unattended/SKILL.template.md`; and the
  re-rendered `.claude/skills/unattended/SKILL.md`, which `check-wiring.sh` compares to the tracked
  template. `tools/check-kit-versions.sh` is what forces that set — read it there rather than trust a
  count typed here.
- `memory/map/features/build-method.md` and `memory/map/features/unattended.md`.

### The read-path budget

Two budgets, and only one of them is mechanical. **This section carries no figure for either**, which
is not fastidiousness: every figure it used to carry went stale twice in four days, and one of the two
is a CONSUMABLE rather than an illustration.

`memory/guides/BUILD-METHOD.md` declares its own size cap in its own opening section, and no gate
reads that declaration — the hygiene cap for a `memory/guides/` file is a separate and much larger
figure in `.memory-tree.conf`, the two classes having been split by a recorded decision. Read both
live at build time: `wc -lc memory/guides/BUILD-METHOD.md` against the cap the file itself declares.
So the displacement obligation is EDITORIAL, not mechanical: it exists because M7 re-reads the file
whole at every pass boundary, and no gate will catch a failure to honour it. **AC6 is what makes this
unit's method growth displacement-neutral by criterion rather than by good intentions** — any
paragraph displaced to make room must be absent from the method and present in
`tools/memory-tree/README.md`. Raising the method's own declared cap is an owner turn under M3's
veto 2 and is not in this unit's scope.

The budget that IS mechanical is the charter read-path ceiling, and it is a consumable that landed
units have already spent most of. The builder runs `python tools/memory-tree/corpus_ids.py --report`
immediately before spending and reads the live total, the live ceiling and the per-file split from
that output. `LIVE.md` is generated, so the total drifts between renders and no snapshot of it is ever
an allowance. This unit spends from that shared budget; the spender set and the live pair are stated
in the build README and nowhere else, this spec included.

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
- **error / empty / loading states** — a review on a slug with no run-state file, an unlisted verdict,
  a missing subject or blocker count, and a round on an already-terminated group are the distinct
  refusals. A sequence AT the ceiling is not among them: under F4 it is reported and survived, so it
  is an output path and not a refusal. The empty case that matters: a FIRST round must not read as
  non-convergent for want of a predecessor, which the predicate's `N == 1` arm handles explicitly.
- **observability** — the verb reports the loop state by name on every call, so a run knows whether it
  is re-arming, exiting clean, or promoting. That report is the observation this unit is graded on.
- **risks** — the highest is now the inverse of rev-5's: not that the exit is unreachable, but that
  promotion does not terminate. §4 states that limit and does not claim otherwise. Second: a run that
  reports a shrinking count it did not earn, which §4's boundary covers. Third: S9's park case being
  used as an escape from ordinary work, which the method prose must phrase as a scope test rather than
  a difficulty test — observed by AC6a, so this risk is graded rather than merely noted.
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
- **AC3** — When the verdict is outside the closed set,
  `bash tools/unattended/unattended.sh --review <slug> --subject <id> --verdict MAYBE` refuses naming
  the legal set, and that set is the three members S3 enumerates. The duplication against the
  memory-tree owner is not asserted by eye: a row in `tools/memory-tree/marker-contract.test.sh`'s
  case table reds when the driver's set and the memory-tree kit's set diverge, and that test is green.
- **AC3a** — When a run-state file carries `review` lines for one subject and `surfaced`-class lines
  (a `decision`, an `abort`, an `override` or a `waiver`) for another,
  `bash tools/unattended/unattended.sh --close <slug>` counts only the `surfaced`-class lines against
  the attestation — the fixture carries at least one line of each class, so the arm fails under a count
  of all parked lines and passes only under the taxonomy-aware one.
- **AC4** — When a tracked run-state file carries a `review` group whose blocker counts are
  non-decreasing across three consecutive rounds and whose lines carry no exit token — no TERMINAL
  LINE per S4 — `bash tools/unattended/check-unattended.sh` reds naming the file and the subject; the
  same group WITH a terminal line is green. Both fixtures live in
  `tools/unattended/check-unattended.test.sh`, because the corpus exercises neither.
- **AC4a** — When a `review` group carries a TERMINAL LINE as S4 defines it and the generated units
  region gained NO unit row, `bash tools/unattended/check-unattended.sh` reds naming the file and the
  subject; the same fixture WITH the promoted unit row is green. This is S6's THIRD clause — F3's
  ratified addition — and without this criterion that clause is a ratified decision no criterion
  observes, which is the class this build's own spec audit opens by naming. Both fixtures in
  `tools/unattended/check-unattended.test.sh`; the corpus exercises neither, and AC8 grades the
  promotion at the VERB rather than at the leg, so it does not stand in for this.
- **AC5** — When the leg reads the ceiling, it reads it from the DRIVER and holds no copy: the leg's
  only reference to the key is a `core_of` call taking it as the argument, sitting beside the five
  core-set reads already at `tools/unattended/check-unattended.sh:76-82`, and NO assignment of that
  key appears anywhere in the leg. Asserted as the COMPLEMENT over `grep -n`, word-anchored, with the
  sanctioned line set pinned in the arm — never as a count. A count cannot express "no assignment":
  run today the count is zero and its no-match exit is non-zero, so the arm is green by absence AND
  breaks a `&&` chain; run after a CORRECT implementation the count rises while the leg is right, so
  the metric moves the wrong way. Same shape as this build's own sibling criteria for the two other
  absence assertions in the set.
- **AC6** — When the method's review sections are read, they state the blocked-verdict disposition, the
  convergence rule and the promotion rule; any paragraph displaced to make room is absent from
  `memory/guides/BUILD-METHOD.md` and present in `tools/memory-tree/README.md`; and
  `python tools/memory-tree/corpus_ids.py --report` shows the read path still under its ceiling.
- **AC6a** — When the method's review section is read, S9's residual-park case is present and its test
  is a SCOPE test: the paragraph turns on the blocker being outside the mandate's scope or naming
  options that differ in what gets built, and it contains no difficulty or effort test. It also says
  the non-close is method prose rather than a driver refusal, so no reader expects `--close` to
  enforce it. Both halves of the method pair carry the paragraph identically, which
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` observes — this is the criterion S9 lacked, and
  it grades the prose because the prose is the whole mechanism.
- **AC7** — When the method template and the installed copy are compared,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green.
- **AC8** — When a promotion is exercised end to end on a fixture, the run adds a unit row to the
  generated units region, `check_authorization` returns 0, and `--close` does not refuse on
  `authorization-reachable` — the arm that joins this unit to `TOOL-aBoundedVerdict-11` and fails
  without it.
- **AC9** — `python tools/memory-tree/check-arms.py` exits 0 with the unattended `ARMS_FLOORS` entries
  raised, and `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.
- **AC10** — When `tools/unattended/check-unattended.sh` is read, the check count in its header line
  equals the number of checks the leg actually runs, and an arm in
  `tools/unattended/check-unattended.test.sh` DERIVES that number from the leg rather than restating
  it, so the header cannot drift silently past a check this unit adds. The arm reds against a header
  left at `TOOL-aBoundedVerdict-2`'s value.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/memory-tree/marker-contract.test.sh` · `tools/check-kit-versions.sh` ·
`python tools/memory-tree/check-arms.py` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/run-gates/run-gates.sh`.

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
  **What that supersession does to the row, stated here because a commitment nobody spells is a
  commitment nobody honours:** `TOOL-aBoundedVerdict-8` currently reads OPEN and prescribes the
  OPPOSITE of this resolution — "the check spans three units' mechanisms (cap, park verb, halt code);
  write it once all three have landed, not before". On this unit's landing the row goes **SUPERSEDED
  by `TOOL-aBoundedVerdict-1`**, with the superseding text: *the cap is withdrawn, so the row's third
  mechanism no longer exists; the disposition check is written now, as S6's third clause, against the
  promoted unit row in the generated units region.* `memory/backlog/TOOL.md` is in Files touched for
  that reason. The row's own edit is a build-level write, not this unit's code.

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

- rev-10 · 2026-08-20 · the M4 spec audit's 2026-08-20 round, folded. What was actually wrong:
  **H3** — S3 called the verdict set "kit-owned and closed" while enumerating no member and naming no
  owner, and AC3 demanded byte-identity with a set `TOOL-aBoundedVerdict-2` never spelled either, so
  two specs pointed at each other over an empty set. S3 now enumerates the three members, names the
  MEMORY-TREE kit as canonical (it owns review-record grammar via hygiene check 5 and renders the
  method), states the duplication because the unattended kit cannot import from it, and ARMS the drift
  with one row in the case table `tools/memory-tree/marker-contract.test.sh` already carries — the
  harness `TOOL-aBoundedVerdict-4` S2 extends, so no new gate leg. AC3 grades that row instead of an
  unobservable byte-identity.
  **H5, H6 and the spec-1 half of H7** — every byte figure in "The read-path budget" was measured at
  a base five landed units ago, and the charter read path is a CONSUMABLE, so the section was telling
  a builder there was headroom that had been spent. The method's "20 KB and 250-line" self-declaration
  was stale too — the file raised its own cap. Both figures are deleted and replaced by the commands
  (`python tools/memory-tree/corpus_ids.py --report` and `wc -lc memory/guides/BUILD-METHOD.md`
  against the cap the method itself declares). The competing enumeration of the spender set is
  deleted outright: it omitted `-19`, disagreed with the README's set, and did so in the same
  paragraph that cited the state-it-once rule. What is left is the obligation, the displacement
  requirement AC6 already grades, and a pointer at the README.
  **H18** — F3 committed to superseding backlog row `TOOL-aBoundedVerdict-8` whose OPEN text
  prescribes the opposite, and no spec named `memory/backlog/TOOL.md`. F3 now states the row's new
  status and the superseding text, and the file is in Files touched. The row's own edit stays a
  build-level write.
  **H19** — "a terminal disposition line" occurred nowhere in the tree except S6 and AC4, so the leg
  check could not be written and AC4's fixture could not be built. S4 now defines ONE observable, the
  TERMINAL LINE: the exit token the verb already computes, written into the `reason` field it already
  writes. Chosen over F3's promoted-unit row because it adds no field, no grammar and no cross-file
  join — the unit row stays what S6's third clause alone observes. The undefined phrase is gone from
  S6 and AC4.
  **M1** — S10 required the leg to assert BOTH ceiling carriers, one of which is the run's own stdout;
  no gate can observe a transcript. The leg now asserts the README line (AC2b) and the output line is
  observed at the verb by AC2a. One carrier per observer.
  **M2** — S9 was the escape hatch S8 depends on and had no acceptance criterion, and its "the build
  does not close" was ambiguous between prose and a `--close` refusal. Taken the narrow fix rather
  than the binding one, because binding it needs a new close-path predicate this unit does not own:
  S9 now says the non-close is advisory method prose, and new AC6a grades the paragraph — scope test,
  not difficulty test, identical in both halves of the method pair.
  **M3** — the unattended leg's header check COUNT is a two-mover coordination with
  `TOOL-aBoundedVerdict-2` that this spec named nowhere and observed with nothing. It is in Files
  touched with the "one past -2's value" instruction, and new AC10 ties the header figure to the
  number of checks the leg runs, DERIVED by the arm. Per H4 the charter is explicitly NOT a second
  carrier: that bullet was replaced by a pointer at `tools/gate-legs.json` and the body is generated
  between `gov:playbook` markers, so a hand-edit reds the parity leg.
  **M4** — the Rollout omitted `TOOL-aBoundedVerdict-5` entirely while S4a took its class names and
  AC3a graded its counter, so a builder following the Rollout alone would build the `review` kind
  before the taxonomy existed. The Rollout now lists all three hard predecessors in the README's
  dependency order with the reason for each.
  **M13** — `.memory-tree.conf` and `memory/guides/BUILD-METHOD.md` are both on the kickoff manifest's
  watch list and `memory/guides/SESSION-KICKOFF.md` was absent from Files touched, so the ratchet
  would have redded the commit. Added with the same-commit re-stamp note.
  **M15** — "`dClosedLexicon` holds 10 review records in one day" was wrong on the day count; it is 10
  across two days, 8 of them on 2026-08-16. The cap-relocation argument is unaffected.
  **Also folded, not from a finding row but from the same class as B3/M6 (a rev that reached the prose
  and missed a site):** rev-8 inverted the ceiling from a refusal into a reported survival, and two
  sites still called it a refusal — S2's "It REFUSES only at the runaway ceiling" and §5's
  error-states list. Both now agree with F4 and S10. **And D5's taxonomy rename**: S4a and AC3a said
  the class names were `decision` and `record`; the owning spec's classes are `surfaced` and
  `history`, `review` is the first `history` kind, and the shipped counter is CORRECT today with all
  four live kinds surfaced — the claim of a present inflation is withdrawn and replaced by the real
  argument, which is that the counter goes wrong the day this unit lands a `history` kind.

- rev-11 · 2026-08-20 · **built, and the leg check had THREE independent silent-skip mechanisms — every
  one of which left it GREEN.** Recorded in that order because each was found only after fixing the one
  before, and any of them alone would have shipped a check that grades nothing.
  (1) `core_of` parses only a DOUBLE-QUOTED value and the ceiling was written `RUNAWAY_CEILING=8`, so
  the leg read empty and the `if [ -n … ]` guard skipped the whole three-clause block. A guard around a
  read that can fail IS the silent-skip shape; an unreadable ceiling is a refusal now.
  (2) The middot is TWO BYTES in UTF-8, so `substr(line, i + 8)` left a stray space on every parsed
  subject name and no group ever matched its own rows. This repo's own check 12 carries the warning
  verbatim — offsetting past a middot is a property of the awk build and the ambient locale — and both
  files now compute the offset with `length()`.
  (3) S6's third clause read `ROSTER_OPEN`, which is a DRIVER variable and empty in the leg, so the
  clause F3 ratified would have passed quietly forever. The markers are spelled, and an unreadable
  region now reports that it CANNOT OBSERVE rather than passing.
  **The predicate's discriminating arm is in the suite explicitly**, not implied: a 2, 1, 2 oscillation
  satisfies "the count changed" forever and terminates only under strictly-smaller. An implementation
  testing for change passes every other arm and fails that one alone.
  **AC6's displacement was real work, not a formality.** The additions took the method to 301 lines
  against its own 290-line cap, so two paragraphs moved to the memory-tree README — what the review
  harness is NOT for, and why the parallelism rule's third clause is worded as it is — both pure
  explanation, and my own new prose was compressed rather than displacing more of the file's existing
  content. Final 288 lines / 22069 B, inside both caps, read path 111893 of 112987.
  **S10's second carrier says the ceiling has NOT fired**, rather than leaving the section blank: an
  empty section reads as "nothing to report" when it may mean "nobody wrote here".
  One message bug caught by running the verb: the first round reported "smaller than the round before
  it" when there is no round before it.

- rev-12 · 2026-08-21 · **the closing review's round 2 found the leg RED at HEAD, plus 32 more.**
  The blocker was mine and unforced: check 22's six review fixtures were written AFTER the hygiene
  suite's only `git add -A && git commit`, and the engine's population is `git ls-files`. Check 22
  shipped grading an empty population, five arms failed, and I had never re-run that sibling suite.
  The FOURTH silent-skip mechanism in this one leg check also surfaced here: the promotion clause
  tested `index(units, it)`, and the subject is a substring of every generated row, so only a
  fabricated id could fire it. It grades a unit-id DELTA against the roster at the run's pinned BASE
  now, which is what a promotion actually produces.

  Two fixes needed a second pass because the first was half-right. The §8 mark is matched over the
  JOINED section so a wrapped mark matches — 14 corpus marks wrap — but they wrap INSIDE the
  parenthesis, and the hygiene reader joins raw lines, so its blob carried the continuation's
  two-space indent and still missed all 14; both readers squeeze whitespace now. And `--review` was
  documented on all four surfaces, but the leg arm written to enforce that immediately reported
  `--attest` missing from the driver's own refusal string — the arm earning its keep on the commit
  that introduced it.

  **The per-item §8 walk is WITHDRAWN, not repaired.** It must tell a FORK bullet from an OPTION
  bullet, and this corpus does not distinguish them: of 287 §8 bullets, 69 carry descriptive labels,
  and among those are both resolved forks and genuinely open ones. A label-shape discriminator
  therefore UNDER-counts and lets a real open fork pass, which is worse than the over-counting it
  replaces — and the over-counting was measured, not hypothetical: it called a RESOLVED fork FORKED
  on a live tracked spec whose three option bullets each demanded their own mark. Making §8 regular
  enough to grade per item changes what every future spec must look like, which M3 reserves to the
  owner. Parked with all three options, and the residue is pinned as a GAP in two fixtures rather
  than left unmentioned.

  Two defects were found by fixing others rather than by the review. `marker-contract.test.sh`
  sliced `plan_state` as `start + 45`; the comments added here grew the function past that, so the
  slice had begun truncating the seven lines that decide READY vs FORKED — the bound is derived from
  the closing brace now. And `GIT_COMMON_DIR` was absent from the env-lever ban list that already
  holds `GIT_DIR`, which is its sibling; a check reading a repo location its own caller injected is
  the hole that list exists to close.

  AC6's displacement criterion was recorded MET and was not: two paragraphs were deleted rather than
  moved, leaving M6 pointing at a README section that did not exist and M4 missing its `tier2-review
  reviews DIFFS` rule while still telling the reader to run a Workflow. Both are real now. Recording
  that here because rev-11 is the entry that got it wrong.

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

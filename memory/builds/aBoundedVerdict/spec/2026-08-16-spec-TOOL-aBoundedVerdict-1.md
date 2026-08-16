# TOOL-aBoundedVerdict-1 — two review rounds, then the unit stops being reviewed

**Status:** OPEN · rev-3 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

An unattended run may review one subject at most twice; the third round is refused by the driver
rather than discouraged by prose. Separately and more importantly, the build method gains the rule
whose absence is the loop's actual engine: it states no disposition at all for a BLOCKED verdict, and
its own rule that a rev-moved spec is unreviewed means folding one round's fixes re-arms the next.

## 2. Scope (IN)

- **S1** — a review-round cap as a FILE CONSTANT in the unattended driver, value two. Not a conf key
  and not an environment variable, reusing the argument this repo already recorded for its agent
  fan-out bound: a ceiling raisable from the environment leaves no diff behind.
- **S2** — `unattended.sh --review <slug> --subject <id-or-slug> --verdict <TOKEN>`, which increments
  that subject's round count, records the verdict, and REFUSES the call that would exceed the cap.
- **S3** — the verdict vocabulary is the build method's own three, kit-owned: clean, clean with
  fixes, blocked. An unlisted verdict is refused. The three exist in the method as prose today and in
  no machine anywhere.
- **S4** — a round is recorded as one line in the PARKED region under a new `review` KIND, through
  the existing park helper unchanged, carrying the subject and the verdict. The count is the number
  of `review` lines naming that subject. **No new authored fact**, so the region's fact pin does not
  move here: an append-only history of rounds is exactly what a park kind is for, and a tracked
  sibling spec set the precedent by adding a kind rather than a field for the same reason.
  `TOOL-aBoundedVerdict-2` takes the FACT route for the halt code, which is a per-run singleton read
  by key, and the two shapes are chosen deliberately rather than for consistency. The helper's output
  leads with a timestamp, so the region's anchor ban is satisfied by construction.
- **S4a** — the `review` kind is a **record** kind — the class `TOOL-aBoundedVerdict-5` S7 names and
  owns. Its surfaced-count refusal counts DECISION kinds only, so review rounds do not inflate the
  count of decisions the owner must be shown. The two class names are `decision` and `record`, taken
  verbatim from the owning spec rather than paraphrased here.
- **S5** — the SUBJECT is the spec document for a method spec-audit round, and the BUILD SLUG for the
  method's closing diff review. One counter, one cap, two denominators, because the two review kinds
  have two denominators and a single per-unit cap would price a build-level event on a unit-level
  count.
- **S6** — a leg check in `check-unattended.sh`: for every tracked run-state file, the `review` lines
  in the parked region are grouped by their `item` field and no group exceeds the cap read FROM the
  driver. **There is no round-count fact to parse** — the count is derived from the line set, and the
  only grammar the leg splits is the park helper's own output.
- **S7** — the build method's spec-audit section gains a stated disposition for a blocked verdict,
  and the clarification that folding a round's own fixes does not make the spec unreviewed for the
  purpose of the round count. Both are method rules binding on any run; neither is machine-checked.
- **S7a** — the method's WRAP-UP derivation row is narrowed to DECISION-kind parked entries, handed
  to this unit by `TOOL-aBoundedVerdict-5` S7c because this unit already has the method in its write
  set and lands after the taxonomy exists. The row today says every parked entry with its question,
  options and reason — a shape a `review` line does not carry — so without the narrowing the wrap-up
  would demand three fields of a line that has two. This is the only place in the set that edits that
  row, and no other spec may claim it.
- **S8** — at the cap with a subject still not clean, the run does not review it again. It parks the
  subject and continues when the remaining units do not depend on it, and otherwise halts with the
  review-budget halt code. Both mechanisms are other units' and this unit only names the disposition.

## 3. Non-goals (OUT)

- **No cap on attended runs.** The owner decided this, shown the measurement that twelve of
  thirty-eight build folders hold no review record at all on a green gate. Nothing here adds a
  required field to a review record, a date-cutoff ratchet, or a waiver pass over the existing
  fifty-three.
- No join from a review record on disk to the unit it reviewed. The filename carries a per-build
  counter, the driver already refuses that join in its own source having measured it wrong on seven
  of seven multi-unit builds, and this unit does not retry it.
- No parse of a review record's verdict heading. The corpus's headings include four spellings
  outside the method's three and thirty-one records carry none at all.
- No change to the review harness's fan-out or concurrency caps. Those are a different bound over a
  different thing and are already enforced at the tool call.
- No claim that the count is unforgeable. The run calls the verb, so the run controls the count. §4
  states the boundary rather than implying one.

## 4. Design

### Data model

One appended line per round, in the PARKED region, under a new `review` kind:

| Field | Value |
|---|---|
| kind | `review` — a `record` kind, per `TOOL-aBoundedVerdict-5`'s taxonomy |
| item | the subject: a spec document for a spec-audit round, the build slug for the closing round |
| reason | the verdict, one of the three kit-owned tokens |

The count is derived, not stored: the number of `review` lines naming the subject. Rev-1 made these
two AUTHORED FACTS, one key per subject, which was wrong twice over. The binding protocol pins the
authored region at a closed set of facts and enumerates them, and rev-1 would have made these the
ninth and tenth without naming or moving the pin — while a tracked sibling spec had already declined
an eighth fact by name for this exact reason and added a park kind instead. And a round count is
append-only HISTORY, which is what the parked region is; a fact is a mutable singleton, which a round
count is not.

Rev-1 also priced the per-subject keys against the run-state file's line cap. The region that grows
carries its OWN byte budget with a spill rule, and that is the budget this spends.

### The boundary, stated

The run calls `--review` and the run authors the run-state file, so a run that simply never calls the
verb is uncounted, and one that calls it with a different subject string each time is uncapped. This
is the same boundary the protocol's own section nine draws for every other authored fact, and the
same one the two agent-attested Definition-of-Done items already accept. What the mechanism buys is
that exceeding the cap becomes a visibly deliberate act with a refusal on the record, rather than the
default behaviour of a run following the method faithfully — which is what the measured five-round
loop was. It does not buy prevention, and no document in this build may imply that it does.

### Why a rule matters more than the number

The loop's engine is not a missing count. The method says a spec whose rev moved since its last
review is unreviewed; the only stated exit is a synthesis pass calling the design clean; and no
disposition exists for a blocked verdict. So a clean-with-fixes round is folded, the fold bumps the
rev, the rev makes the spec unreviewed, and the loop re-arms — while a blocked round has no exit at
all. Measured on the newest build in the tree: five consecutive spec-audit rounds over one seven-unit
set in one day, verdicts clean-with-fixes, blocked, blocked, blocked, clean-with-fixes, and a sixth
closing round that was also blocked. A cap alone would have stopped that at two and left the run with
no rule for what to do next. S7 is that rule and S8 is where it disposes.

### Inventory

| Concern | Today | After |
|---|---|---|
| the number of rounds a subject may get | nothing, repo-wide | a driver constant, refused at the verb |
| what a blocked verdict means for the run | unstated | the method states it |
| whether folding a round's fixes re-arms the loop | it does, by the method's own rev rule | it does not, for the round count |
| the verdict vocabulary | prose in the method, four unlisted spellings in the corpus | three kit-owned tokens, refused at the verb |
| what happens at the cap | nothing | park the subject, or halt with the review-budget code |

### Migration

None on disk. No existing run-state file carries a `review` parked line, and the leg check bounds the
groups that are present rather than asserting any exist — so today's corpus passes it unchanged.
That makes the check VACUOUS over the current tree, which this repo names as its own bug class, so
the arm is not the corpus: it is explicit red and green fixtures in the leg's sibling test, which is
the same disposition the streams ratchet already took for the same reason and recorded in the conf.

### Alternatives rejected

- **Count from review records on disk.** Every evasion is legal under the live filename predicate,
  the sequence is unbounded, a family-qualified record is ambiguous with a unit id, and filing the
  review one folder over changes its kind and hides it. Rejected, and the driver's own source already
  rejected the underlying join.
- **Derive the count from the spec's rev number.** The only per-unit monotone number that exists
  today, and it counts the wrong thing: a rev bumps for any material change, review-driven or not.
- **A conf key for the cap.** Rejected on S1's reused argument.
- **Extend the existing core-set floor key to carry the cap.** Rev-1 rejected this because a third
  field is "dropped in silence", which is FALSE and was refuted against source: the parser matches a
  three-field value on its reject arm and fires a named refusal wanting two integers separated by a
  colon. The rejection stands on the grounds that hold — the key is a two-field contract whose
  malformed-value guard is written for exactly two fields, so widening it means editing that guard
  and its arm, against a file constant that costs neither.
- **Two authored facts per subject.** Rev-1's shape. Rejected in §4 Data model on the protocol's fact
  pin and on the singleton-versus-history distinction.
- **Refuse the third review at the review harness instead of the driver.** The harness reviews diffs
  and cannot perform a method spec audit at all, so it sees at most one of the two review kinds.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` and the installed protocol ·
`tools/unattended/SKILL.template.md` and the rendered Skill · `memory/guides/BUILD-METHOD.md` and
`tools/memory-tree/BUILD-METHOD.template.md` · `tools/memory-tree/README.md`, receiving the
displaced paragraph · `tools/unattended/check-unattended.sh`'s header check COUNT and the matching
count in `AGENTS.md`'s gate-suite bullet, which S6 moves by one and which no gate observes ·
`.memory-tree.conf` (arms floors) · `memory/guides/SESSION-KICKOFF.md` (the manifest re-stamp; the
conf and the build method are both on its watch list) · the kit version constants.

### The method document's size budget — measured, and not what rev-1 said

Rev-1 asserted the method file was at its line cap and made the displacement a gate requirement.
Measured at base: `memory/guides/BUILD-METHOD.md` is 236 lines and 16466 bytes, and the hygiene
gate's cap for a `memory/guides/` file is 61440 bytes and 750 lines — the file is at 31% of the
gated cap with 514 lines of margin. The 20 KB and 250-line figures are the method's OWN line-8
self-declaration, which no gate reads for a guide, because the two classes were split by a recorded
decision.

So the displacement obligation is EDITORIAL, not mechanical: it is M1's growth rule, machine-checked
by nothing, and it exists because the file is re-read whole at every pass boundary. This spec honours
it and says plainly that no gate will catch a failure to.

The budget that IS mechanical is the charter read-path ceiling, measured at 70262 bytes against a
ceiling of 86476 — **16214 bytes of headroom**. It is shared by FOUR units, not two: this unit and
`TOOL-aBoundedVerdict-3` grow the method, and `TOOL-aBoundedVerdict-2`, `TOOL-aBoundedVerdict-3` and
`TOOL-aBoundedVerdict-5` grow the unattended protocol, which is a read-path member at 18214 bytes.
The spender set is stated ONCE, in the README's cross-unit rules, rather than in each spec. This
unit's share is the method prose S7 adds, and the builder re-measures with the corpus reporter before
spending rather than treating either figure as authority.

## 5. Production-readiness checklist

- security — N/A as a surface. The trust boundary is stated in §4 rather than left implicit.
- perf / scale — N/A. One appended line per review round.
- a11y — N/A.
- i18n — the verdict tokens are identifiers.
- error / empty / loading states — a review on a slug with no run-state file, an unlisted verdict, a
  missing subject, a count already at the cap, and a terminal record are five distinct refusals.
- observability — the refusal at the cap is the observation, and it names the subject and the count.
  A run that hits it and then parks leaves the round's line and the park's line on the record.
- risks — the highest is that the cap is met and the disposition is not taken, leaving a unit
  silently unbuilt. S8 names the disposition and the halt code names it again at the terminal; the
  residual is that neither is machine-enforced, which §4 states.
- testing + left-shift gates — the leg check plus its fixtures, and an arm per refusal branch. The
  left-shift for the vacuity risk is the fixture pair, not the corpus.
- migration / rollback — none needed; rollback removes the verb and the check, and existing records
  are unaffected either way.
- user docs — the protocol's verb table, the rendered Skill, and the method's spec-audit section.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --review <slug> --subject <id> --verdict
  BLOCKED` is called a third time for one subject, it refuses naming the subject and the cap, and the
  round count on disk is unchanged. Asserted on the on-disk effect, not the exit code alone; arm in
  `tools/unattended/unattended.test.sh`.
- **AC2** — When the same run reviews a SECOND subject, that subject's first call succeeds — the cap
  is per subject, and one fixture in `tools/unattended/unattended.test.sh` exercises both subjects to
  prove it.
- **AC3** — When the verdict is outside the three kit-owned tokens,
  `bash tools/unattended/unattended.sh --review <slug> --subject <id> --verdict MAYBE` refuses naming
  the legal set.
- **AC3a** — When a run-state file carries `review` lines for one subject and `park` lines for
  another, `bash tools/unattended/unattended.sh --close <slug>` counts only the DECISION-kind lines
  against the attestation — the fixture carries at least one line of each class, so the arm fails
  under a count of all parked lines and passes only under the taxonomy-aware one.
- **AC4** — When a tracked run-state file carries more than the cap's worth of `review` lines for one
  subject,
  `bash tools/unattended/check-unattended.sh` reds naming the file and the subject; both the red and
  the green fixture live in `tools/unattended/check-unattended.test.sh`, because the corpus exercises
  neither.
- **AC5** — When the leg reads the cap, it reads it from the driver:
  `grep -c 'REVIEW_CAP=' tools/unattended/check-unattended.sh` is zero.
- **AC6** — When the method's spec-audit section is read, it states a disposition for a blocked
  verdict and the round-count clarification; the paragraph displaced to make room is absent from
  `memory/guides/BUILD-METHOD.md` and present in `tools/memory-tree/README.md`; the file's line count
  is no higher than before; and `python tools/memory-tree/corpus_ids.py --report` shows the read path
  still under its ceiling.
- **AC7** — When the method template and the installed copy are compared,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is green.
- **AC8** — `python tools/memory-tree/check-arms.py --check` exits 0 with both unattended
  `ARMS_FLOORS` entries raised, and `GATE_FULL=1 bash tools/run-gates.sh` is green.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/check-kit-versions.sh` · `python tools/memory-tree/check-arms.py` ·
`python tools/codebase-map/test_codebase_map.py` · `bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does the cap bind the closing diff review at two rounds, or at one plus one fix
  re-review?** The method mandates exactly one closing review and then a re-review of the fix, which
  is two, so the numbers coincide today. They stop coinciding if a second blocker appears in the
  fix. Options: two, uniformly, and a second blocker is a park; or an explicit allowance for the fix
  re-review chain. Recommendation: two, uniformly — the owner's instruction was a maximum of two and
  a chain allowance is the unbounded case wearing a bound's clothing.
- **F2 — is the verdict token recorded at all, or only the count?** The count alone enforces the cap.
  The verdict is what lets S8's disposition be chosen without re-reading the review record, and what
  lets a future check ask whether a capped subject was disposed of. Options: both, as specced; count
  only, which is smaller and leaves the disposition unevidenced. Recommendation: both.
- **F3 — should the leg additionally assert that a subject AT the cap with a non-clean verdict was
  disposed of?** It is the check that would make S8 mechanical rather than advisory. Against it: the
  disposition may be a park in another unit's mechanism or a halt in a third's, so the check spans
  three units and would couple them. Recommendation: not in this unit; raise it as a backlog row once
  all three have landed, so it is written against mechanisms that exist.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Records the owner's decision that the cap binds unattended runs
  only, taken on the measurement in §3, so the absent corpus-wide enforcement is a decision rather
  than an oversight.
- rev-2 · 2026-08-16 · folded the M4 spec audit's first round. No unit-only defect survived
  verification; all three folds are set-level. The round count and last verdict were specced as the
  ninth and tenth AUTHORED FACTS in a region the binding protocol pins closed and enumerates, which
  rev-1 neither named nor moved — they become lines under a new non-decision park kind, which is
  what a tracked sibling spec already chose for the same question, and the pin does not move here.
  The size-budget paragraph and AC6 rested on a false premise: the file is at 31% of the gated cap,
  not at it, and the displacement obligation is editorial with no gate behind it — the mechanical
  budget is the read-path headroom, now allocated explicitly against the other unit that spends it.
  The floor-key rejection rested on a false claim about the existing parser and is restated on
  grounds that hold.
- rev-3 · 2026-08-16 · folded round 2, which found that the rev-2 fold had not reached the whole
  spec. S6 still specified the leg check over a round-count FACT that rev-2's own data model had
  deleted — two scope items describing mutually exclusive on-disk shapes, the same class round 1
  filed against the predicate unit — and four further sites still described the fact shape: the
  migration paragraph, the perf line, the observability line and the reuse audit's named seam, which
  is `park()` and not the fact writer. The park kind's class was called `non-decision` here and
  `record` in the spec that owns the taxonomy, under a sentence claiming the two were spelled
  identically. Added the arm that actually exercises the taxonomy, the four-unit read-path spender
  set, and the Files-touched entries the rev-2 acceptance criteria had already started depending on:
  the displacement's receiving file, the manifest re-stamp, and the leg's own check count, which this
  unit moves and which no gate observes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound how many times a review may run for one unit"`
returns the review protocol, the review harness and the fan-out leg, and no counter of any kind —
consistent with the repo-wide grep for a numeric review bound returning nothing. Three existing
seams are extended rather than duplicated: the driver's core-constant idiom with the leg reading it
through the same helper that already reads the core phase and Definition-of-Done sets; `park()`,
unchanged — its kind argument and its two existing callers are what make S4 free, and taking a kind
rather than a field is what keeps the authored region's fact pin still; and the driver's shared
terminal-record refusal. No existing seam fits the counting itself, and the evidence for that is the
absence above rather than a failure to look.

Recall terms used, recorded for the reground: review round cap blocked verdict spec audit rev bump
unreviewed re-review loop unattended driver run-state fact subject denominator.

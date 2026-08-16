# TOOL-aBoundedVerdict-1 — two review rounds, then the unit stops being reviewed

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

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
- **S4** — the round count and last verdict are authored facts, one key per subject, written through
  the existing fact writer. The key embeds the subject id and the line therefore does not lead with a
  dash or a pipe, which is what the authored region's anchor ban requires.
- **S5** — the SUBJECT is the spec document for a method spec-audit round, and the BUILD SLUG for the
  method's closing diff review. One counter, one cap, two denominators, because the two review kinds
  have two denominators and a single per-unit cap would price a build-level event on a unit-level
  count.
- **S6** — a leg check in `check-unattended.sh`: every round-count fact in every tracked run-state
  file parses as an integer and is at or under the cap read FROM the driver.
- **S7** — the build method's spec-audit section gains a stated disposition for a blocked verdict,
  and the clarification that folding a round's own fixes does not make the spec unreviewed for the
  purpose of the round count. Both are method rules binding on any run; neither is machine-checked.
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

Two authored facts per subject, written through the driver's existing fact writer, which rewrites a
key's line in place or appends it under the run-facts heading:

| Fact | Value |
|---|---|
| the subject's round count | an integer, at or under the cap |
| the subject's last verdict | one of the three kit-owned tokens |

One key per subject rather than one key holding every subject's count. The per-subject shape reuses
the fact writer unchanged and needs no parsing at all on the read side; a single packed key would
need a read-modify-write the driver does not currently have. A build with twenty-two units costs
forty-four lines in a file capped at two hundred and fifty, which the size budget absorbs.

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

None on disk. No existing run-state file carries either fact, and the leg check is a bound on values
that are present rather than an assertion that they exist — so today's corpus passes it unchanged.
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
- **Extend the existing core-set floor key to carry the cap.** That key parses by taking the text
  before the first colon and after the last, so a third field is dropped in silence.
- **Refuse the third review at the review harness instead of the driver.** The harness reviews diffs
  and cannot perform a method spec audit at all, so it sees at most one of the two review kinds.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` and the installed protocol ·
`tools/unattended/SKILL.template.md` and the rendered Skill · `memory/guides/BUILD-METHOD.md` and
its kit template · `.memory-tree.conf` (arms floors) · the kit version constants.

### The method document's size budget

The method file is capped in lines and bytes and its own rule is that it grows only by displacement,
because it is re-read whole at every pass boundary. S7 adds prose to it. The displacement is
identified and made in the same commit, and the current margin is read from the gate rather than
carried in this spec — a number written here would rot between the writing and the build.

## 5. Production-readiness checklist

- security — N/A as a surface. The trust boundary is stated in §4 rather than left implicit.
- perf / scale — N/A. Two fact writes per review round.
- a11y — N/A.
- i18n — the verdict tokens are identifiers.
- error / empty / loading states — a review on a slug with no run-state file, an unlisted verdict, a
  missing subject, a count already at the cap, and a terminal record are five distinct refusals.
- observability — the refusal at the cap is the observation, and it names the subject and the count.
  A run that hits it and then parks leaves both facts on the record.
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
- **AC4** — When a tracked run-state file carries a round count above the cap,
  `bash tools/unattended/check-unattended.sh` reds naming the file and the subject; both the red and
  the green fixture live in `tools/unattended/check-unattended.test.sh`, because the corpus exercises
  neither.
- **AC5** — When the leg reads the cap, it reads it from the driver:
  `grep -c 'REVIEW_CAP=' tools/unattended/check-unattended.sh` is zero.
- **AC6** — When the method's spec-audit section is read, it states a disposition for a blocked
  verdict and the round-count clarification, and `bash tools/memory-tree/check-memory-hygiene.sh`
  is green — which requires the displacement, since the file is at its line cap.
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

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound how many times a review may run for one unit"`
returns the review protocol, the review harness and the fan-out leg, and no counter of any kind —
consistent with the repo-wide grep for a numeric review bound returning nothing. Three existing
seams are extended rather than duplicated: the driver's core-constant idiom with the leg reading it
through the same helper that already reads the core phase and Definition-of-Done sets; the authored
fact writer, unchanged, which is what makes S4's per-subject key shape free; and the driver's shared
terminal-record refusal. No existing seam fits the counting itself, and the evidence for that is the
absence above rather than a failure to look.

Recall terms used, recorded for the reground: review round cap blocked verdict spec audit rev bump
unreviewed re-review loop unattended driver run-state fact subject denominator.

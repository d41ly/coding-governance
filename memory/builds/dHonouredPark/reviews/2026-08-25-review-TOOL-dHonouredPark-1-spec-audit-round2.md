**Serves:** spec-audit TOOL-dHonouredPark-1..4

# Spec audit round 2 — the four dHonouredPark specs at rev-2

*Node d, 2026-08-25, base 60ba1d60. One agent per spec, each given round 1's record so it hunted NEW
defects rather than re-reporting known ones, each prompted to REFUTE and to default to refuted. Four
agents, inside the charter's cap.*

## Verdict: BLOCKED

49 findings. **Zero confirmed blockers**, down from two. One was raised at BLOCKER and is regraded
HIGH here, with the reasoning below.

Round 1 confirmed 2 blockers; round 2 confirms 0. The convergence condition is met on the strict
reading — the confirmed-blocker count is strictly smaller — and the verdict stays BLOCKED because 15
HIGH findings is not a landable spec set.

| Spec | Findings | HIGH |
|---|---|---|
| [TOOL-dHonouredPark-1](../spec/2026-08-25-spec-dHonouredPark-1.md) | 14 | 5 |
| [TOOL-dHonouredPark-3](../spec/2026-08-25-spec-dHonouredPark-3.md) | 13 | 5 |
| [TOOL-dHonouredPark-2](../spec/2026-08-25-spec-dHonouredPark-2.md) | 11 | 2 |
| [TOOL-dHonouredPark-4](../spec/2026-08-25-spec-dHonouredPark-4.md) | 11 | 4 |

## The regraded blocker

**Unit 2, §8 F1.** rev-2's prose withdrew a resolution stamp by QUOTING it verbatim. `plan_state`
decides FORKED against READY by matching the stamp's pattern anywhere in the squeezed section-8 text,
so the withdrawal re-asserted the thing it withdrew. Measured: `--plan` printed unit 2 READY while its
three siblings printed FORKED.

Regraded HIGH rather than BLOCKER because unit 2's F1 IS genuinely settled — no gate, deliberately —
so READY was the right answer reached by the wrong derivation. A classification that is correct by
accident is a serious defect and not a stop-the-build one.

It has a second life as a defect in the CLASSIFIER, not in the spec: **any spec that discusses a
resolution mark is classified as resolved.** `plan_state`'s own comment enumerates what it cannot see
and does not list this. Filed as `TOOL-dHonouredPark-7`.

## The dominant class, and it is the author's

Round 2's largest single category is **precision that rots**: line-number citations, authored counts
of derived populations, and coordinates naming code that is not there.

rev-2 carried 51 line-number citations across four specs. Round 2 found at least six wrong, and two
were verified by hand afterwards:

- Unit 1's S7 quoted `[ -n "$want" ] || return 0` at coordinates holding `[ -f "$rel" ] || return 0`
  and a `grep -qF` guard. The quoted construct exists once, in a different function.
- Unit 1's AC8 cited the `len(tracked)` print one line above where it is.
- Unit 2 cited the already-shipping clause at a line holding a different sentence — the exact failure
  that item exists to prevent, since an implementer checking the citation adds the duplicate.
- Unit 3's S4 cited a range that stops three lines before the code it calls the largest part of its
  diff.
- Unit 4 authored "eleven assertions" for a population that is 22 calls across 9 invocations.

rev-3 removes the class rather than fixing instances: name the function and the file, locate by grep,
and derive counts at build time. The repo's own rule already said so — a value stated in prose beside
the source that owns it rots between changes — and these specs broke it while citing it.

## HIGH — unit 1

- **The migration ORDER contradiction survived two folds.** §4 stated engine-first in one sentence and
  migration-first in the next. Round 1 found it, rev-2 rewrote the surrounding figure and left the
  contradiction standing. rev-3 states the order as a numbered list.
- **The withdrawn non-goal survived under a new name.** §1 declared non-goal 4 withdrawn on the
  owner's ruling; a bullet reading "No requirement that the contract's EXEMPT rows gain anything"
  remained, which is the same claim and contradicts S1 and S6 outright.
- **S5's fix reached no consumer.** `roster_ids`' pipeline ends in `sort -u`, not `grep`, so it takes
  sort's status — and no caller tests that status at all: both assign or substitute and then test for
  emptiness, and the script sets `set -u` without `set -e`. Propagating a status out of the function
  changes nothing observable, and the acceptance criterion asserting only the function's own status
  would have gone green over a surviving vacuous pass.
- **And the obvious fix breaks the legal case.** `set -o pipefail` on that pipeline turns a well-formed
  EMPTY pair — which §5 declares legal and meaningful — into a refusal, because `grep -oE` exits 1 on
  no match. No criterion pinned the empty case. rev-3 adds one.
- **rev-2 created a dependency on arms nothing runs.** Round 1 exonerated this unit on the
  gates-cannot-run-the-arms finding precisely because rev-1 named no test file. rev-2's new items put
  arms in `unattended.test.sh`, which the kit gate skips outright, which no bar leg invokes, and which
  a standing owner instruction forbids running. rev-3 adds the declared skip and compensating check
  that unit 4 already carries.

## HIGH — unit 3

- **The staleness rule as written is not computable.** "A row whose needle left the derivation"
  requires per-row needle attribution the checker never performs — it greps one alternation and
  reduces to path:line tokens — and two of the eight waived LINES name two needles each, for which
  "any needle left" and "all needles left" give opposite verdicts. rev-3 restates it as a membership
  test against the hit set, which is what ships and needs no attribution.
- **AC5 asserted an outcome the checker's own shipped arm contradicts.** Waiving one of two identical
  hit-carrying lines leaves the other an unwaived carrier, and an unwaived hit reds. N identical lines
  need N rows. rev-3 says so and rewrites the criterion.
- **AC3's message never prints.** The unwaived-carrier report comes first and exits, so a rewording —
  which makes a line both a hit and no longer waived — never reaches the stale-row loop. rev-3 asserts
  the message the checker actually emits and adds a section stating the refusal order, deliberately
  without reordering it.
- **The grammar contradicted its own arms.** The ordinal is mandatory in S1 and in the four-field parse
  rule, and two arms required a row "with no ordinal" — which that rule cannot represent, since a
  three-field row assigns the text to the ordinal slot. rev-3 makes the ordinal mandatory and gives a
  malformed one its own refusal.
- **The prior art cited as validation documents the opposite.** `unarmed-branches.txt`'s ordinal is
  POSITIONAL — `check-arms.py` keys on a number plus an ordinal within it — and that file's own header
  records a row's ordinal moving 2→4 because branches were inserted above it. rev-2 cited it as proof
  of insertion-stability. rev-3 borrows the shape and explicitly refuses the counting rule.

## HIGH — unit 4

- **The second `NOT A UNIT` diagnostic was misdescribed.** The branch tests whether the heading's id
  token parses. It is not "a spec whose heading and status header disagree", and cannot be — the status
  header carries no id for a heading to disagree with. Verified by reading the branch.
- **And it has zero live instances.** All 277 tracked specs parsed with the driver's own two awk
  programs: five produce the no-status-header row, none produce the other. The driver's own comment
  beside the branch already says so. rev-2's single criterion could not cover both; rev-3 splits them
  and marks the second as needing a staged fixture.
- **The protocol guide is a RENDER and editing it directly reds a gate.**
  `memory/guides/UNATTENDED-PROTOCOL.md` is byte-identical to `tools/unattended/PROTOCOL.template.md`
  (verified: same size, CR-stripped diff empty) and `adopt-unattended.sh` exits 1 on drift — which is
  the `unattended skill wiring` leg the spec lists as green.
- **There is a third copy.** `tools/unattended/SKILL.template.md` carries the same description, rendered
  into the installed skill and diffed by the same check. Neither template appeared in any list.

## HIGH — unit 2

- **The mean-line denominator counted blanks.** 450 B divided by a 77 B whole-file mean gave ~5.8
  lines; the 240 lines that carry prose average 100 B, so it is about 4.5, and the byte cap binds near
  line 316. rev-2 overstated the remaining room by about 30%, in the record this unit exists to leave.
- (The regraded blocker above is unit 2's other HIGH.)

## MEDIUM and LOW — folded without discussion

Unit 1: the degenerate-pair inventory was wrong in both directions (one build's under-population
missed entirely, and the prescribed remedy is a no-op for two builds that have one spec each); AC2
asked for a per-condition message AND reuse of a message that distinguishes none; AC4 is green at BASE
and unmarked, and its "and says so" has no producer; AC8's added half is a tautology once S1's refusal
exists; the read-path charge was a checklist bullet rather than declared scope.

Unit 2: the 153 B margin is a deliberate DEPARTURE from the tool's printed jump, used by the five most
recent movements — not "the margin every prior movement uses"; the parent build left three
unit-attributed movements plus one unattributed, not two; the kit-version bump is unforced and, if
taken, forces two re-renders that would red the parity leg; no criterion covered the decision row's
placement inside the measured window; §7 omitted four guarded self-test legs the diff trips; the
file was three lines over at the parent build's base and that build reduced it to two, the reverse of
what rev-2 said.

Unit 3: the read-path charge was not declared scope; only ONE of the three waived-hit files carries a
tab, not two; the install-prefix dossier claims this unit's paths and both its gate legs, so the
dossier refresh and the unguarded codebase-map leg both bind; the fourth documentation site sits above
the range S6 named; three of the seven arms are green by construction and cannot be observed RED.

Unit 4: the run-state precondition is short — the verb also refuses a file declaring no phase, and the
harness's own helper writes none; the fixture work forces changes to shared helpers every `--plan`,
`--status` and `--preflight` arm depends on; a region row whose id has no tracked spec is unclassified
once S1 makes the region the set; files-touched omitted the two files the unit's own checklist requires
it to edit; "both are priced" appeared with no measurement anywhere in the file, when the round-1
finding WAS the missing measurement.

## What the fold did

All four specs are at rev-3. Every finding above is folded. The changes that are more than wording are
named in each spec's revision log.

Two structural changes apply across the set. Line-number citations are replaced by grep-locatable
names, and authored counts of derived populations are replaced by derivations. AC numbering was
resequenced in units 1 and 4, and each revision log now records that its earlier entries' AC labels
refer to the numbering of the revision that wrote them.

## Whether a round 3 is owed

The blocker count went 2 → 0, so the loop's re-arm condition is satisfied and this record does not
demand another round on that ground.

The honest counter-argument is the trend in everything else: 67 findings over rev-1, 49 over rev-2, and
a consistent pattern that each fold introduces fresh defects in the prose it newly writes. Two of round
2's HIGH findings are round-1 findings that rev-2 recorded as folded and did not fix. That pattern does
not obviously terminate by folding harder.

Recorded as the owner's call rather than decided here: another spec round, or build unit 2 — the
smallest, a Tier-1, and the one whose remaining findings are all folded — and let a real diff review
grade the design that survives contact with the code.

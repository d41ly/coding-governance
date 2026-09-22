**Serves:** spec-audit TOOL-aClosedDocket-4

# aClosedDocket — spec audit of TOOL-aClosedDocket-4, round 1: the promoted unit

*Node `a`, 2026-08-31. A Tier-2 adversarial pass over ONE document — the unit promoted out of
`TOOL-aClosedDocket-1` when the set's audit loop exited NON-CONVERGENT at four blockers. Under
BUILD-METHOD M4 a promoted unit is audited as a spec, and that audit is what makes promotion
terminate, so this is the terminating step and not another lap of the set's loop. A primed finder
fan, a skeptic stage prompted to REFUTE each finding, one synthesis. Every claim any finding made
about existing code was re-checked at source during synthesis; the two claims that moved on that
re-check are named inside the findings that carried them.*

**Round: 1.** Subject, pinned at the blob it was read at:

- `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-4.md@b96255795d62aae3d7e68d6149daa5d960c31bae`

## Verdict: BLOCKED

One blocker and three highs. The blocker is not a wording slip: S1 keys the whole unit's trigger
condition on "the verdict it computes", and `verb_review` computes no verdict. `--verdict` is
caller-supplied and screened against the closed set `REVIEW_VERDICTS="CLEAN|CLEAN WITH FIXES|BLOCKED"`
(`unattended.sh:444`, refused at `:3533-3535`); what the verb computes is the STATE returned by
`review_state` at `:3578`, whose members are CONVERGED, NON-CONVERGENT, CEILING and CONVERGING. Read
literally against the driver's own vocabulary, S1's "REQUIRED when the verdict is NON-CONVERGENT or
CEILING" can never fire and "refused otherwise" fires always. AC3 then makes the damage material
rather than editorial: it observes that `--verdict CONVERGING` is refused, which is already true
today from the closed-set check, so AC3 passes byte-identically with the unit unbuilt. That is this
repo's own could-not-fail class sitting in the section whose job is to be the unit's observable.

The three highs are all one shape — the unit changes the RULE and leaves the SENTENCES that assert
the old rule standing, owned by neither this unit nor its sibling. The driver's own NON-CONVERGENT
success line still tells the agent that promotion is the only disposition. The gate's failure text
still says "exited without promoting". And AC6, the single criterion separating "clause 3 accepts a
fold" from "clause 3 stopped checking", demands a message naming the subject that clause 3's
promotion arm structurally cannot emit.

The unit's core design is sound and should survive the fixes intact. The driver-writes-it argument,
the reason the flag is required only at the exit, the three rejected alternatives, and N2's decision
to file the vacuity rather than fold it are all correct and well-evidenced. Two of the three hunt
questions this audit was pointed at came back clean, and they are recorded below as such.

**Review shape:** raw 37 · confirmed 13 · refuted 24 · unverified 0 · precision 0.35. The thirteen
confirmed findings consolidate into the seven below: four reports of the §5 Observability claim, three
of the kit-version carrier set, and two of AC6 were the same defect seen from different angles.

## Findings

| # | Sev | Address | One line |
|---|-----|---------|----------|
| B1 | blocker | §2 S1 · §6 AC3 | The flag's trigger is keyed on a "verdict" the verb does not compute, and AC3 cannot fail |
| H1 | high | §6 AC6 · §2 S3 | AC6 demands a message naming the subject that clause 3's promotion arm cannot emit |
| H2 | high | §4 Inventory vs §2 S1 | `verb_review`'s own success line hard-codes promotion as the only disposition, and no unit owns it |
| H3 | high | §2 S4 · §4 Inventory | S4 fixes the driver's refusal text and leaves the GATE's "exited without promoting" standing |
| M1 | medium | §4 Inventory (S6) · §6 AC8 | The kit-version carrier set omits a third template, its render, and both constant lines |
| M2 | medium | §7 Gates · §4 Inventory | The unguarded `check-arms` merge-bar leg this unit incurs appears nowhere |
| M3 | medium | §5 Observability | Both named readers of the disposition are false at source |

---

### B1 — blocker — §2 S1, and §6 AC3: the trigger names a vocabulary the verb does not have, and the criterion that guards it cannot fail

S1 says the flag "is REQUIRED when the verdict it computes is NON-CONVERGENT or CEILING and refused
otherwise". `verb_review` computes no verdict. The verdict arrives from the caller and is screened at
`tools/unattended/unattended.sh:3533-3535` against the closed set declared at `:444`:
`REVIEW_VERDICTS="CLEAN|CLEAN WITH FIXES|BLOCKED"`. What the verb computes is the STATE, from
`review_state` (defined `:3500-3507`, called at `:3578`), returning CONVERGED, NON-CONVERGENT,
CEILING or CONVERGING. NON-CONVERGENT and CEILING are states and are never verdicts.

Read literally, no legal `--verdict` value is ever NON-CONVERGENT or CEILING, so "REQUIRED" fires
never and "refused otherwise" fires always — a builder implementing S1 as written builds a flag that
is refused on every call. §4's "Why the driver writes it and not the run" repeats the error
("`--review` already computes the NON-CONVERGENT verdict"), so it is the spec's consistent
understanding rather than one loose sentence.

AC3 is where this stops being a naming problem. It observes that the call "with a CONVERGING verdict
is REFUSED". `--verdict CONVERGING` is refused TODAY by the pre-existing closed-set check at `:3535`.
The criterion therefore passes identically before and after the unit is built, and cannot distinguish
the new refusal from the one already there. §7's own "what no gate here checks" paragraph is honest
about intent grading; this is the AC section failing a much cheaper test.

**Fix.** Restate S1 over the STATE `review_state` returns, and pin the refusal's site explicitly:
after `state=$(review_state "$prior" "$blockers")` at `:3578` and before the `park` call, because
every existing refusal in the verb precedes that line and the new one structurally cannot. Rewrite
AC3 as a FIRST round for a fresh subject with `--blockers` non-zero — `--verdict BLOCKED
--disposition fold`, which `review_state` returns CONVERGING for — and require the refusal message to
be textually distinct from the closed-set one, so the criterion observes the new branch and not the
old.

**Left-shift.** `python3 tools/memory-tree/check-arms.py --check` already refuses a `fail` branch with
no positive assertion naming its own failure text; requiring AC3 to assert the new branch's message
puts this class under that existing gate rather than under a reader's attention. The general form —
an AC whose observation is satisfied by the pre-change tree — has no gate and belongs in §10's
checklist as a spec-audit class: *for every AC, name the pre-change behaviour it distinguishes from*.

---

### H1 — high — §6 AC6 (and §2 S3/S4 behind it): the criterion asks for text the arm cannot emit

AC6 requires the fold-less fixture to still red `check-unattended.sh` "naming the subject". Clause 3's
promotion arm names no subject. Both of its messages, at `tools/unattended/check-unattended.sh:299`
and `:301`, print `f` — the run-state FILE — and integer counts:

```
%s (%d subject(s) EXITED without converging and the generated units region gained only %d unit id(s)
this run BASE lacked, so at least one blocker was neither fixed nor promoted)
```

The awk's own comment at `:293-297` states why: the count is taken across subjects because a
per-subject attribution "is not available - the region records ids, not which subject promoted them".
Only the runaway-ceiling and stalled-loop arms print `(subject %s: …)`, and neither of those is the
promotion clause — which is plainly where AC6's phrasing came from.

Under S3 as scoped, removing the disposition from the fixture returns that subject to `nneed`, and
the same count message re-fires. The fixture DOES red; it just does not name a subject. So AC6 as
written is unobservable, and AC6 is the only criterion proving clause 3 did not simply stop checking.
A builder has two bad options: write an arm asserting text that never appears (permanently red), or
add a per-subject promotion message that §2 never scopes and §4's inventory never budgets — and that
rewrite strands `tools/unattended/check-unattended.test.sh:710`, which asserts the `:301` sentence
verbatim, contradicting S3's "the existing promotion arm is untouched".

**Fix.** Restate AC6 against the message the arm actually emits: with the disposition removed, one
subject exited, the run reds naming the file with `1 subject(s) EXITED without converging and the
generated units region gained only 0 unit id(s)`. If the message is instead to name subjects, that is
a scope item in S3 plus an inventory line requiring the `check-unattended.test.sh:710` literal to move
in the same commit.

**Left-shift.** This is the recorded `arm-literal-strands-on-message-edit` class, and it already has a
gate: `check-arms.py` reds when a message is reworded out from under its pinned signature. What has no
gate is the spec-side half — an AC quoting gate output that the gate does not produce. Add to §10:
*an AC that quotes or paraphrases a checker's message is verified against the checker's format string
at authoring time, by grep, not from memory of what a sibling arm prints.*

---

### H2 — high — §4 Inventory against §2 S1: the driver's success line still says promotion is the only disposition

S1 makes `fold` a legal disposition. `verb_review`'s own NON-CONVERGENT success message, at
`unattended.sh:3591`, ends:

> `every blocker still standing is PROMOTED to a unit of this build, specced at its tier and built. Not parked, not waived, not re-reviewed`

and its CEILING twin at `:3592` says `The run promotes and lands anyway`. The same claim also sits in
the block comment above `review_state` at `:3487-3499`.

So the call that records `--disposition fold` prints, on the same stdout, a sentence asserting
promotion is the only outcome — on the one line an unattended agent actually reads at the exit. §4's
`unattended.sh` row scopes only "the flag, its refusal, the round row"; N1 hands only "the M4 sentence
and the SKILL carriers" to `TOOL-aClosedDocket-1`, whose own inventory lists the two templates, their
renders and the memory-tree version, not the driver's stdout. The line belongs to neither unit, and no
AC covers it. This is the kit's own named anti-pattern — two answers to one question — shipping one
line from the change.

**Fix.** Add `unattended.sh:3591` and `:3592` (and the `review_state` block comment) to the
`unattended.sh` inventory row, and an AC over them: a fold-recorded NON-CONVERGENT exit prints a line
naming the disposition it recorded rather than asserting promotion.

**Left-shift.** `tools/check-playbook-parity.sh` is the existing mechanism for machine-comparing a
stated value against the source that owns it. The disposition vocabulary is now a value with two
carriers (the driver's flag validation and the driver's own exit prose); the cheap gate is a grep
asserting that any file naming `PROMOTED to a unit` also names the fold. Failing that, §10 gets the
class: *when a rule's enumeration widens, grep the tree for prose asserting the old enumeration
before calling the unit scoped.*

---

### H3 — high — §2 S4 and §4 Inventory: the refusal is fixed on the side nobody reads, and left standing on the side they do

S4 requires the refusal to name both dispositions "rather than being told it failed to promote". The
sentence that says exactly that is the GATE's, not the driver's: `check-unattended.sh:301` prints "so
at least one blocker was neither fixed nor promoted", and the clause summary at `:305` reads "review
loops that ran past the ceiling, stalled without recording it, or exited without promoting".

§4's inventory assigns S4 to `tools/unattended/unattended.sh` alone; `check-unattended.sh` appears
only for S3's second arm. After this unit lands, a run that recorded neither disposition is refused by
the driver naming both — and the bar reader, who sees the gate's text instead, is still told the
failure is a failure to PROMOTE, with fold unnamed. That is S4's own stated concern left standing one
file over, and it is the document/gate contradiction §1 says this unit exists to close. No non-goal
covers the gate's message text.

**Fix.** Add clause 3's `:301` message and the `:305` summary to S4 and to the `check-unattended.sh`
inventory row, plus a note that the `check-unattended.test.sh:710` assertion literal moves in the same
commit. Sequence this with H1: both edits land on the same format string, and doing them separately
reds the arm twice.

**Left-shift.** Same gate as H2's suggestion — a grep asserting the fold is named wherever promotion
is named as the outcome — plus the `check-arms` signature pin, which already forces the test literal
to move with the message.

---

### M1 — medium — §4 Inventory (S6 row) and §6 AC8: the version move has more carriers than the table lists

AC8 requires `bash tools/check-kit-versions.sh` to exit 0 after the version move. That gate DERIVES
its population rather than naming it: `tools/check-kit-versions.sh:159` iterates
`git ls-files 'tools/unattended/*.template.md'` and reds any member whose marker disagrees with
`KIT_UNATTENDED_VERSION`; `:149-158` additionally requires the constant AND a same-line `gov:kit
unattended@` marker in BOTH `unattended.sh` and `check-unattended.sh`.

The tracked template set is three, all at `@1.13`: `PROTOCOL.template.md:1`, `SKILL.template.md:5`,
and `PLAYBOOK-TEMPLATE.template.md:1`. §4's inventory lists the first two. The third is also rendered
— `kit.toml:28-30` ships it to `memory/guides/PLAYBOOK-TEMPLATE.md:1`, which `kit.toml:154` pins for
byte-comparison and `adopt-unattended.sh:186` calls "the THIRD artifact". Neither the template nor its
render appears in the spec.

Two consequences. The listed edits alone red AC8 with `marker != KIT_UNATTENDED_VERSION`. And AC8's
other invocation does not catch it either: `run-unattended-gates.sh` defaults `ONLY=--selftests`
(`:54`), so the no-arg call runs the five self-test suites and skips the `checks` legs, including
`adopt-unattended.sh --check` that compares the playbook render. The build discovers its own carrier
set by failing a gate. This is the recorded "stamps are not one stamp" trap, paid at the landing
rather than at authoring time, and it is a repeat: `aBoundedVerdict`'s H20 refused the phrase "the kit
version constant" for naming one file where the gate forces several.

**Fix.** Add `tools/unattended/PLAYBOOK-TEMPLATE.template.md` and `memory/guides/PLAYBOOK-TEMPLATE.md`
to the S6 row, marker-only, and both `KIT_UNATTENDED_VERSION=` constant lines. Better, copy sibling
`TOOL-aClosedDocket-1`'s S5 hedge and delegate: `check-kit-versions.sh` is the authority on which
carriers move, not this table. Change AC8's second invocation to
`bash tools/unattended/run-unattended-gates.sh --all`, or add `bash tools/unattended/adopt-unattended.sh --check` exits 0.

**Left-shift.** The gate already exists and already derives the set; nothing new is needed at the code
level. The spec-side rule belongs in §10: *a spec whose scope includes a version move never enumerates
the carriers — it names the checker that derives them.*

---

### M2 — medium — §7 Gates and §4 Inventory: the arms leg this unit incurs is invisible in the spec

`python3 tools/memory-tree/check-arms.py --check` is a `subject: repo` leg in `tools/gate-legs.json`
("harness arms (fail branches armed or pinned)") with NO `guard` key, so it runs on every bar. Its
docstring is explicit about what satisfies it: "A POSITIVE assertion naming the branch's OWN failure
text" — a bare mention, an absence assertion or a comment all fail to arm. The pin at
`memory/project/unarmed-branches.txt` declares itself SHRINK-ONLY, so no exemption can be added for a
new branch.

S1, S2 and S4 add two or three new `fail 37` branches to `verb_review`. Each needs a positive arm in
`unattended.test.sh` naming its message. §7 names only `unattended kit gate` and `unattended skill
wiring` as the unguarded legs reaching this unit, and its "what no gate here checks" clause never
mentions the arms obligation; §4's `unattended.test.sh` row says only "S5 — both directions", which is
the clause-3 fixtures, not the driver refusals. AC3 as written asserts only that a call is refused,
not what it says, so at least one branch can land unarmed and red the main bar.

**Fix.** Add the arms leg to §7's list. Expand the `unattended.test.sh` inventory row to "one positive
assertion per NEW fail branch". Add `python3 tools/memory-tree/check-arms.py --check` exits 0 to AC8.
Note in S6 or the rollout that `ARMS_FLOORS` in `.memory-tree.conf` currently pins
`tools/unattended/unattended.sh:104:101` and must rise in the same commit, or the floor goes slack by
exactly the branches this unit adds.

**Left-shift.** The gate is already there and already binds; the gap is the spec's Gates section
claiming a set of legs narrower than the one that will run. §10 class: *a §7 that enumerates legs
enumerates them from `tools/gate-legs.json` filtered by guard, never from the two whose names contain
the kit's own.*

---

### M3 — medium — §5 Observability: both named readers are false

§5 states "the round row carries the disposition, so `--status` and the wrap-up derivation read it
with everything else on that line". Neither half is true.

`verb_status` (`unattended.sh:2591-2641`) parses no field of any parked row. It prints slug, phase,
witness, halt-code and the next non-terminal unit, then appends two COUNTS obtained by `grep -cE` over
kinds. `review` is in `PARK_KINDS` (`:350`) but not `PARK_KINDS_OWED` (`:356`), so a review round lands
in the undifferentiated `· noted N` tally and no part of the row is ever printed.

The wrap-up derivation excludes it by rule. BUILD-METHOD M9's derivation table (`:258`) says
`history`-class entries — "a review round, say" — are append-only sequence, carry no question, and are
not the owner's to adjudicate; the `problems resolved` row (`:257`) derives from each review RECORD's
`## Verdict` line, not from the round row.

Grepping the driver, the only readers of `review · item ` rows are `review_counts` and `verb_review`'s
own terminal guard, both inside `--review` itself. So the disposition's only reader outside the verb
that writes it is clause 3. The unit is credited in its production-readiness section with an
observability surface the kit does not have — which is precisely the claim a later session acts on
without re-checking, and the reason nobody builds the surface that would deliver it.

**Fix.** Replace the bullet with the true statement: the disposition is read by clause 3 and by a
human opening the run-state file; `--status` reports it only inside an undifferentiated `noted` count,
and the wrap-up derivation excludes review rounds by M9's rule. If a status-line surface is wanted,
that is a scope item with its own arm, not a checklist claim.

**Left-shift.** No gate reaches a false sentence in a spec's readiness section, and inventing one is
not worth it. §10 class instead: *every §5 Observability bullet names a reader, and a named reader is
verified by grepping for the field it claims to read.*

---

## Hunt items that came back clean

Three of the five questions this audit was pointed at produced no finding, and the negatives are worth
as much as the findings.

**S3's second arm IS buildable, and the awk's limitation does not apply to it.** The comment at
`check-unattended.sh:291-297` says a per-subject attribution is unavailable *for the id delta*, and
the reason is specific: `newids` is a per-FILE delta computed outside the awk, so consuming it
per-subject let one promotion satisfy every exited subject in the file. The disposition has no such
problem — it sits on the exit ROW, which the awk already keys by `it` when it sets `needs[it]`.
Clearing `needs[it]` on a row matching `disposition fold` is a per-subject fact by construction, and
`nneed` then counts only the subjects that owe an id. S3 is implementable exactly as specified. The
open question Q1 asked was the right one and its answer holds.

**N4 verified against the real corpus.** Nine tracked run-state files record a NON-CONVERGENT or
CEILING exit: `aBoundedVerdict`, `aClosedDocket`, `aLexedStripper` (three subjects),
`aPrimedKeepalive`, `aProvenReuse` (two), `aScouredKit`, `dPromptedSeam` (two), `dTieredTribunal`,
`dUnstalledConvoy`. S3 adds a disjunct to a passing predicate and touches neither the id delta nor the
promotion arm, so every one of them is graded by exactly the arm that grades it today. N4 holds. One
observation worth recording rather than filing as a finding: `dTieredTribunal`'s subject is literally
`dTieredTribunal-run2-fold`, a fold smuggled into the subject STRING because there was no field for
it. That is this unit's own motivation, already in the corpus.

**Q1's claim about the two readers is true, with one nuance.** `review_counts`
(`unattended.sh:3511-3523`) and clause 3's awk both use `index(rest, " · reason ")`, which returns the
FIRST occurrence, then regex the tail — so a field appended inside the reason tail is parsed by
neither as an item name. There is a THIRD reader Q1 does not mention: `verb_review`'s terminal guard
at `:3574` pipes through `sed 's/.* · reason //'`, which is GREEDY and therefore splits at the LAST
occurrence. It agrees with the other two for any tail not containing a literal ` · reason `, which the
driver already refuses in the subject, so it is not a defect this unit introduces. Naming it in Q1
would keep the next session from re-deriving it.

**Q2's argument for a separate flag is sound**, and B1 strengthens it rather than weakening it.
`REVIEW_VERDICTS` describes what the round FOUND and is caller-supplied; the disposition describes what
the run DID about a terminal STATE the driver derived. Folding them would put `CLEAN` and `fold` in one
enum answering two questions. That the spec's own prose then confuses verdict with state is exactly
the confusion the separate flag is there to prevent.

## What the fixes cost

Six of the seven are edits to this document. B1 additionally pins where the refusal goes and rewrites
one AC; H1 and H3 are one coordinated edit to clause 3's format string and its test literal; H2 is two
echo strings and an AC. Nothing here questions the design, the alternatives, or N2's decision to file
the vacuity — those survived the fan intact.

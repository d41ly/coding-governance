**Serves:** spec-audit TOOL-aGradedMandate-10 TOOL-aGradedMandate-11

# aGradedMandate — spec audit of the TWO PROMOTED units

*Adversarial Tier-2 pass over the two units the spec-audit loop promoted, node `a`, 2026-08-31. The
loop over this build's other nine units ran two rounds, went 2 blockers then 2, and exited
`NON-CONVERGENT`, so both standing blockers became units under the build method's M4 exit rule.
**This is the audit that makes promotion TERMINATE** — a spec audit of the two new specs, not a third
round of the loop that produced them. Round-2 findings against the other nine are not re-raised.
Every claim below was re-derived in this worktree against the driver
(`tools/unattended/unattended.sh`), its suite (`tools/unattended/unattended.test.sh`), the gate leg
(`tools/unattended/check-unattended.sh`) and the tracked run-state records, at the line numbers
cited. One probe was EXECUTED — `TOOL-aGradedMandate-1` S1's predicate over all 28 tracked `RUN.md` —
and its output is reproduced under H1. `TOOL-aGradedMandate-10` depends on `TOOL-aGradedMandate-5`,
which is not built: it is judged against the design spec-5 rev-3 states, and every claim about
spec-5 below is a claim about a SPEC, never about shipped bytes. Round 2:
`reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md`. Binding contract:
`memory/guides/UNATTENDED-PROTOCOL.md`. Method: `memory/guides/BUILD-METHOD.md`.*

**Range:** two spec records, each pinned at the blob reviewed —
`spec/2026-08-31-spec-TOOL-aGradedMandate-10.md@4e8f75a3a387afb6736d905aa8263392ed3aa7ea` ·
`spec/2026-08-31-spec-TOOL-aGradedMandate-11.md@7c39af7af69c8e0502db415705a08708c85942fe`.

**ROUND:** 1.

## Verdict: BLOCKED

One blocker, three highs, two mediums — six distinct defects across two specs. **Review shape.** Raw
36, confirmed 13, refuted 23, unverified 0, precision 0.36. The 13 confirmed findings collapse to
those six: four independent finders reported the unfalsifiable AC3 (B1) and three the non-terminal
`aThawedCorpus` (H1), which is corroboration rather than volume. Precision fell from 0.75 to 0.36
against a surface a quarter the size, which is what a narrow, already-audited target does to a wide
fan — the lesson is a smaller fan next time, not a lower bar.

The blocker is the one that matters and it is worth stating without hedging. **Unit 11 was promoted
to end "a criterion answered from memory instead of from the run", and its own AC3 is a criterion
answered from memory.** `grep -c 'a fourth hit'` over spec-1 returns 0 today, before unit 11 exists,
because round 2's own fold already deleted the phrase. Half the unit's deliverable — the rewrite of
spec-1's AC7 — is observed by that criterion and by nothing else in section 6, so unit 11 can ship
with spec-1 untouched and every AC passes. That is round 2's R5 shape reproduced inside the fix for
round 2, and section 5 of the very same spec institutes the rule it breaks.

The two units also contradict each other on the acceptance axis. Unit 11 section 5 writes the
build-level rule — *a grep-shaped or census-shaped criterion is not accepted until its value has been
MEASURED and written down* — and unit 10's AC4 is a grep-shaped criterion whose pre-edit count is
already 2 and whose expected value is written nowhere (H3).

## Are the acceptance criteria falsifiable?

The question this audit was commissioned to answer, criterion by criterion. Pre-state is measured on
this worktree at the pinned blobs.

| AC | Falsifiable? | Measured pre-state | Note |
|---|---|---|---|
| 11 AC1 record exists + `**Serves:**` line | yes | RED — no such record is tracked | `--print-bindings` is both report and gate predicate |
| 11 AC2 verdicts reproducible + both counts named | yes | RED — no record to reproduce | this is the unit's real liveness assertion |
| 11 AC3 spec-1 AC7 names no count, points at the record | **NO** | GREEN before the unit exists | **B1** |
| 11 AC4 every NON-TERMINAL record named with its verdict | yes | RED | falsifiable, but fires against section 3's own prose — **H1** |
| 11 AC5 memory hygiene green over the new record | conditional | vacuous until AC1 holds | acceptable only because AC1 pins existence; on its own it is green-by-absence |
| 10 AC1 retire row prints `parked 1`, no non-zero `noted` | yes | RED today and RED after spec-5 | the instance arm, correctly anchored |
| 10 AC2 partition over a one-row-per-kind fixture | **underdetermined** | GREEN or RED depending on an act AC2 never pins | **H2** |
| 10 AC3 both arms observed RED before the fix | yes | — | unsatisfiable against the fixture AC2 describes, which is H2's other half |
| 10 AC4 `grep -c 'park_kinds_unowed'` | **NO** | GREEN — returns 2 today, expected value unwritten | **H3** |
| 10 AC5 kit gate + selftests green | yes | — | ordinary |

Two of the ten cannot fail and one cannot be evaluated from what the spec writes down. Unit 10's
instance arm (AC1) is the healthiest criterion in either spec: it is red today, red after the
dependency lands, and green only after the fix.

## Findings

| # | Sev | Subject | Address |
|---|---|---|---|
| B1 | BLOCKER | unit 11 | `spec-…-11.md` §6 AC3, against §2 S2 |
| H1 | HIGH | unit 11 | `spec-…-11.md` §3 non-goal 3, against §2 S2 and §6 AC4 |
| H2 | HIGH | unit 10 | `spec-…-10.md` §6 AC2, against §2 S3 and §6 AC3 |
| H3 | HIGH | unit 10 | `spec-…-10.md` §6 AC4, against §5 risks |
| M1 | MEDIUM | unit 10 | `spec-…-10.md` §10 Reuse audit ¶3, against §4 Inventory |
| M2 | MEDIUM | unit 10 | `spec-…-10.md` §5 error / empty / loading states, against §6 |

---

### B1 — BLOCKER · `spec/2026-08-31-spec-TOOL-aGradedMandate-11.md` §6 AC3, against §2 S2

AC3 reads:

> `TOOL-aGradedMandate-1` AC7 names no expected-hit count of its own and points at this record,
> verified by `grep -c 'a fourth hit'` over that spec returning 0.

Measured in this worktree:

```
$ grep -c 'a fourth hit' memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-1.md
0                                        # rc 1, blob fcb62cb4dd9485d455f8ebee29e4bf0fe64daecd
```

The phrase is already gone. Spec-1 is at rev-3 and round 2's own fold replaced AC7 with a
supersession note, so **AC3's only executable observation is green before unit 11 exists**, and it
stays 0 after the edit, so it can never go red in either direction.

On the same blob both propositions AC3 asserts are FALSE. Spec-1 AC7 now reads, at lines 134-137:

> **AC7** — SUPERSEDED by `TOOL-aGradedMandate-11`, which round 2 promoted out of this criterion. The
> census pinned here was answered from memory rather than from the tree and was wrong by eighteen:
> executed over all 28 tracked `RUN.md`, the predicate passes 7 and refuses 21.

That names two expected-hit counts of its own (`7` and `21`) — AC3 asserts it names none — and it
points at unit 11 rather than at the census record — AC3 asserts it points at the record. So the
criterion's claim is false today while its named verifier reads green. The observation and the claim
are decoupled; nothing joins them.

The second clause is verified by nothing at all. "Points at this record" names no command: no
observation in section 6 greps spec-1 for the census record's path.

**Reachability.** S2 is half the unit's deliverable and AC3 is its only observer — AC1, AC2, AC4 and
AC5 all grade the new census record, not the AC7 rewrite. The unit can therefore be built with spec-1
untouched, or not built at all, and every criterion passes. The counts typed into a spec that S2
exists to remove survive, invisible to the criterion written to remove them.

This is round 2's R5 shape verbatim (*"`grep -c 'retire' SKILL.md` returns 2 today — S6's only
observation is green before S6 exists"*), reproduced inside the unit promoted to stop exactly this,
and it is the same defect class as the R2 blocker unit 11 descends from. Section 5 of this very spec
institutes the rule against it, and `memory/builds/aGradedMandate/README.md:50` states it as a
build-level rule citing this defect by name.

**Fix.** Re-anchor AC3 on bytes S2 must INTRODUCE, never on a phrase already deleted, and split the
two claims into two observations:

- `grep -c 'build/2026-08-31-build-TOOL-aGradedMandate-11-closing-loop-census.md'` over spec-1
  returns ≥1 — pre-edit measured value **0** on 2026-08-31, written beside the criterion.
- spec-1's AC7 bullet carries no bare integer of its own (an `awk` over the AC7 bullet asserting no
  digit run outside the record path) — pre-edit measured value **RED**, because the live AC7 carries
  `7`, `21`, `28` and `eighteen`.

Record both pre-edit measurements in section 5, which is the discipline that section already
prescribes for everyone except itself.

**Left-shift.** Not a runtime gate — the population is prose. The durable left-shift is the one the
build README already carries, given teeth: **a criterion whose observation is a `grep`, `grep -c` or
census MUST carry its measured pre-edit value inline, and a pre-edit value that already satisfies the
criterion is a REFUSAL, not a note.** That is mechanically checkable over `memory/builds/*/spec/*.md`
— an AC bullet containing a backticked `grep` invocation and no adjacent measured-value phrase reds —
and it is worth wiring as a memory-hygiene check because this build has now produced the shape three
times (round 2 R5, round 2 R2, and this). Until then it is a documented check on the spec-audit
checklist: for every grep-shaped AC, run it and paste the number.

---

### H1 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-11.md` §3 non-goal 3, against §2 S2 and §6 AC4

Section 3's third bullet reads:

> **No retrofit of the refusing records.** Twenty-one tracked records would refuse and every one of
> them is terminal or is this build's own.

I executed S1's predicate over all 28 tracked `RUN.md` — `review` rows whose ` · item ` subject
equals the bare slug, at least one must exist, and the last must carry `CONVERGED` / `NON-CONVERGENT`
/ `CEILING`:

- **Pass (7)** — `aBoundedVerdict` `aGroundedOrientation` `aLexedStripper` `aScouredKit`
  `dFramedEntrypoint` `dPromptedSeam` `dScaffoldedMirror`, all `LANDED`.
- **Refuse, no-terminal-token arm (2)** — `aBoundedCeiling` `aPrimedKeepalive`, both `LANDED`.
- **Refuse, no-row arm (19)** — six `ABORTED`, eleven `LANDED`, plus `aGradedMandate` at `FOLDING`
  and **`aThawedCorpus` at `LANDING`**.

Twenty-one refuse, matching the sentence's count. But `PHASES_TERMINAL="LANDED ABORTED"`
(`tools/unattended/unattended.sh:333`), and `memory/builds/aThawedCorpus/RUN.md:15` reads
`phase: LANDING`. LANDING is not terminal, and that record is not this build's own. The disjunction
the bullet uses to justify the no-retrofit non-goal is measurably false on one record.

This is not loose wording. The same spec uses "NON-TERMINAL" in S2 in the kit's technical sense, so
the two sentences are in the same vocabulary and contradict each other. Two siblings contradict
section 3 directly: `spec-…-1.md:73` calls `aThawedCorpus` "the one live record in the tree" and
records that it WOULD BLOCK, and `spec-…-5.md:106` calls it the same.

**Reachability.** S2 makes "any record at a NON-TERMINAL phase that refuses" a finding and AC4
requires the record name every non-terminal record with its verdict. So the census fires a finding on
`aThawedCorpus` on its first execution, against a section that has pre-declared nothing is owed and
that specifies no disposition for it. The builder's two cheapest exits are to override AC4 or to
widen "terminal" to include LANDING — the second disarms, on day one, the one arm round 2's R7 says
would have caught the live-record omission. The refusal itself is already adjudicated in spec-1 §4
Migration ("accepted rather than exempted"), so the criterion classifies a decided case as new.

**Fix.** Name `aThawedCorpus` in section 3 with its measured phase and its disposition — `--close`
has already run and no verb re-closes it, so the refusal costs nothing — and rewrite the bullet as
"terminal, at LANDING with `--close` already run, or this build's own". Keep AC4 strict, and have S2
and S4 define terminal-ness by `unattended.sh:333 PHASES_TERMINAL` rather than by the word "terminal"
in prose, since the record must survive a future phase joining that set.

**Left-shift.** The census record itself is the left-shift, and it needs one property it does not
yet have: **report the non-terminal set BY PHASE, resolved from `PHASES_TERMINAL` at run time, never
by the word "terminal" typed into the record.** A record that prints `LANDING` beside a refusal
cannot be read as claiming that record is terminal, and a future phase added to `PHASES_TERMINAL`
changes the record's classification the next time the probe runs rather than silently invalidating
its prose. Fold that into S4's liveness assertion — it already names two counts, so it can name the
phase split for free.

---

### H2 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-10.md` §6 AC2, against §2 S3 and §6 AC3

AC2 pins the partition arm's fixture as "a record holding one row of every member of `PARK_KINDS`"
and never says which ACT its single `rescope` row carries. `verb_rescope`'s closed act set is
`retire|supersede|add` (`unattended.sh:3882`) and spec-5 S1 declares `PARK_ACTS_OWED="retire
supersede"`, so `rescope · item add …` is a legal row outside the owed acts.

Worked against the predicate as spec-5 leaves it — `PARK_KINDS_OWED="decision abort override waiver"`
plus spec-5's act arm on the owed side, `park_kinds_unowed` returning
`proposal rescope dispatch review` on the history side:

| the fixture's rescope act | owed | noted | rows | partition |
|---|---|---|---|---|
| `retire` or `supersede` | 5 | 4 | 8 | **RED** — 9 ≠ 8, the defect |
| `add` | 4 | 4 | 8 | **GREEN** — arm passes before the fix |

So AC2 and AC3 ("both arms observed RED against the predicate as `TOOL-aGradedMandate-5` leaves it")
cannot both be satisfied by the fixture AC2 describes. The spec has not made the decision that
determines whether its class gate can fail.

**Reachability.** The arm S3 calls the CLASS gate is satisfiable by a fixture that never exercises
the act axis — the axis this unit exists to fix. S3's stated justification for choosing it over an
instance arm, that it catches "any future kind or act landing in both alternations or in neither", is
false for a one-row-per-kind fixture: a member later added to `PARK_ACTS_OWED` is invisible unless
that single `rescope` row happens to carry it. A builder reading AC2 alone builds a partition arm
that is green before the fix and stays green after it.

**Fix.** Pin the fixture in AC2: one row per member of `PARK_KINDS`, PLUS one `rescope` row per
member of `PARK_ACTS_OWED`, plus one `rescope · item add …` row. Write the measured pre-change sums
beside it (owed + noted above the row count) so the RED is recorded rather than assumed. Then either
narrow S3's class sentence to what that fixture actually spans, or say the fixture is DERIVED from
`PARK_KINDS` × `PARK_ACTS_OWED` so a future act enters it automatically — which is the only version
of the sentence that is true.

**Left-shift.** Make the fixture derived, not typed: the arm builds its rows by iterating
`$PARK_KINDS` and `$PARK_ACTS_OWED` read out of the driver, exactly as `park_kinds_unowed`'s own
header argues for deriving the complement rather than listing it. A typed fixture is the same
second-spelling defect the driver already refuses at `unattended.test.sh:3788`, one file over. Then
the arm gates the class for real: adding an act to `PARK_ACTS_OWED` without teaching the history side
reds the suite without anybody editing the test.

---

### H3 — HIGH · `spec/2026-08-31-spec-TOOL-aGradedMandate-10.md` §6 AC4, against §5 risks

AC4 reads:

> `grep -c 'park_kinds_unowed' tools/unattended/unattended.sh` shows the function has exactly one
> consumer besides its own definition, so the risk line in §5 is measured rather than asserted.

Measured:

```
$ grep -c 'park_kinds_unowed' tools/unattended/unattended.sh
2                                        # :3352 definition, :2626 sole consumer
```

No expected value is written down. The criterion is green before any edit, its pass value is
unstated, and it observes nothing this unit does. The §5 risk line it exists to ground therefore
stays asserted, which is the precise outcome AC4 was written to prevent.

`grep -c` also counts LINES, not occurrences, so 2 is consistent with — but does not demonstrate —
"exactly one consumer besides its own definition". A second call added on the definition line would
read as 2.

**Reachability.** This is the banned shape verbatim: `memory/builds/aGradedMandate/README.md:50`
states "**A criterion is not accepted until its value has been MEASURED.** Round 2 found two written
from memory: a grep whose pre-edit count was already 2, and a census pinned at 3 against a tree that
answers 21." AC4 is a grep-shaped criterion whose pre-edit count is already 2. The two promoted units
therefore contradict each other on the acceptance axis, since unit 11 §5 writes the rule unit 10 AC4
breaks.

**Fix.** Write the measured value into AC4 — 2 on 2026-08-31, definition `:3352`, sole consumer
`:2626` — and state the post-edit expectation explicitly. If AC4 is meant to guard against a SECOND
consumer arriving, say so and state the number that reds it. If it is only evidence for a §5 risk
line, drop it from section 6 and move the measurement into section 5 as a dated observation, where a
non-falsifiable statement belongs.

**Left-shift.** Same gate as B1's, which is why the two are worth wiring together: any AC bullet
containing a backticked `grep`/`grep -c` invocation must carry its measured pre-edit value, and a
pre-edit value that already satisfies the criterion is a refusal. If the intent is genuinely
"one consumer, forever", the durable form is not a grep at all but a source-level arm in
`unattended.test.sh` of the shape already at `:3788` — a count derived at test time with a message
naming why a second consumer is a problem.

---

### M1 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-10.md` §10 Reuse audit ¶3, against §4 Inventory

Section 10 states:

> Its shape is borrowed from `unattended.test.sh`'s existing taxonomy arms, which already build a
> fixture record holding one row per kind — so the fixture is reused and only the assertion is
> written.

No such fixture exists. Measured against the suite:

- The nearest arms (`unattended.test.sh:2829-2841`) build one `decision` row plus two `proposal` rows
  and assert `· parked 1` / `· noted 2`; the second fixture there holds a single proposal.
- The other `PARK_KINDS` mention at `:3788` is a source-level presence grep for the constant, not a
  fixture.
- Rows of the other kinds live in separate, `reset_tree`/`bcreset`-scoped fixtures, one kind at a
  time.
- The file contains exactly ONE raw parked-row append — `:3771`, a single `review` row, added
  precisely because "the fixture has to carry a kind outside the taxonomy on purpose".

The verb route is blocked too: `verb_abort` writes its row and sets phase `ABORTED`, after which
`refuse_if_terminal` refuses every remaining parking verb, and override rows are appended by `--close`
after the DoD loop. So several kinds cannot be produced by a verb in a live-phase fixture at all.

**Reachability.** The §4 Inventory prices the partition arm as "only the assertion is written" when
the fixture is the whole cost and is the part that gets built wrong — H2 is that same fixture,
underdetermined. An arm priced at nothing is the arm that gets dropped, or narrowed to the AC1
instance. §10 staleness is also a repeat class for this build: round 2 flagged it as its third
instance. In a spec whose own §10 boasts of re-verifying a stale line number, an unmeasured reuse
claim is the defect, not a style note.

**Fix.** Say the fixture is NEW. Name the construction: raw-append eight
`<ts> <kind> · item … · reason …` lines in the shape of `unattended.test.sh:3771`, and state
explicitly which kinds must be raw because the verb route cannot produce them in a live-phase record
— `abort` terminates it, `override` is written by `--close`.

**Left-shift.** Procedural and cheap: **a §10 reuse claim naming a seam must cite the file and line
of the seam it claims to reuse, and the citation is re-run before the spec is called SPECCED.** This
build's own §10 already demonstrates the discipline for line numbers (it re-derived `:3352` from
spec-5's stale `:3348`); the gap is that it applies the discipline to numbers it cites and not to
seams it asserts. Unnumbered reuse claims are the ones that rot silently.

---

### M2 — MEDIUM · `spec/2026-08-31-spec-TOOL-aGradedMandate-10.md` §5 error / empty / loading states, against §6

Section 5 states:

> a record with no parked rows prints both counts as zero, which the partition arm covers as its
> degenerate case and which is stated so a zero is not read as a skip.

Both halves are false.

**The behaviour.** `verb_status` OMITS the field at zero:
`if [ "${nparked:-0}" -gt 0 ] 2>/dev/null; then parked=" · parked $nparked"; else parked=""; fi`
(`unattended.sh:2618-2619`), under the comment at `:2615` — "Omitted at zero, so the ordinary line
does not grow a `· 0`" — and `noted` is appended only on `[ "${nnoted:-0}" -gt 0 ]` (`:2629`). The
suite already pins the omission at `unattended.test.sh:2840` with `miss "$out" "· parked"`. An empty
record prints NEITHER field, not "both counts as zero", and the omission is a recorded decision the
sentence describes as its opposite.

**The coverage.** AC2's fixture holds one row of every member of `PARK_KINDS`, so it is non-empty by
construction and does not cover the empty record "as its degenerate case". No criterion in section 6
exercises an empty record.

**Reachability.** The sentence's trailing clause reasons from a printed zero the code deliberately
does not print, which inverts the actual risk. A builder writing the partition arm's degenerate case
against "prints both counts as zero" gets an assertion that can never pass, or writes the arm to read
absent fields as zero without the spec ever saying that is the contract — and the zero case is
exactly where a partition assertion over printed text is ambiguous. It is an asserted-covered state
with no criterion behind it, which is the green-by-absence shape sitting inside the arm written to
make two counts add up.

**Fix.** State the omission-at-zero behaviour and its recorded reason, and either add an AC over a
record with no parked rows asserting the status line carries neither `· parked` nor `· noted` —
reusing the `miss` shape at `unattended.test.sh:2840` — or say the degenerate case is out of scope.
Do not leave a claim of coverage with no criterion behind it.

**Left-shift.** The arm is the gate and it is three lines: extend the partition assertion so the
empty record is one of its cases, asserting ABSENCE of both fields rather than two printed zeros.
Absence is the contract; writing it down once in a test is what stops the next reader re-deriving it
wrongly from prose, which is what happened here.

---

## What is CLEAN

Said because a reader who sees only the table will misjudge two specs that are, on the axes round 2
was about, better than the nine that preceded them.

- **The line citations hold.** Unit 10 cites eight exact sites in a 4259-line driver and every one is
  right: `park_kinds_unowed` at `:3352`, `verb_status`'s history count at `:2628`, `kinds_re` at
  `:3344`, `verb_rescope`'s act case at `:3882`, and the leg's two `PARK_KINDS_OWED` readers around
  `:366` and `:1950`. Its §10 explicitly records that spec-5 rev-1's `:3348`/`:3340` had drifted and
  were re-verified — the discipline worked, and M1 is its gap rather than its refutation.
- **The dominant round-2 class is gone.** No finding here reds `unattended kit gate`, the driver
  suite, memory hygiene or `run-gates.sh` on the tree these units ship against. Unit 10's non-goals
  correctly identify that the leg reads `PARK_KINDS_OWED` and sees nothing of this edit.
- **Unit 10's AC1 is the model criterion** in either spec: red today, red after the dependency lands,
  green only after the fix — measured, not asserted.
- **Unit 11's S4 is a genuine liveness assertion** and it is the right one: naming both the examined
  count and the refusing count is what distinguishes an empty selection from a clean corpus.
- **Neither unit tunes its predicate to flatter its measurement.** Unit 11 §3 refuses to loosen S1's
  subject join and unit 10 §4 refuses the second-exclusion alternative for the right reason.
- **Unit 10's dependency handling is correct.** It consumes `PARK_ACTS_OWED` and declares both
  constants out of scope, so nothing here needs spec-5's shipped bytes to be judged.

## Method

Fan of primed finder lenses over the two specs at the pinned blobs, then a skeptic pass prompted to
REFUTE each finding, then this synthesis. Raw 36 → confirmed 13 → six distinct defects; 23 refuted,
0 unverified. Severities are this report's adjudication, not the finders' self-grading: three
findings self-graded BLOCKER were merged down into H1, and one graded MEDIUM was merged up into M1's
reachability argument. Every confirmed finding was re-derived here against source before it was
written down, including the 28-record census, which was executed rather than quoted from round 2.

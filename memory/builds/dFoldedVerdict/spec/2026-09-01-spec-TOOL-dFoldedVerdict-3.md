# TOOL-dFoldedVerdict-3 — the exit rows say which disposition they took, and `origin/main` goes green

**Status:** SPECCED · rev-4 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md) | spec-audit | TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-5 TOOL-dFoldedVerdict-6 |

<!-- /gen:spec-records -->

## 1. Goal

`bash tools/unattended/check-unattended.sh` exits 1 on check 2 against
`memory/builds/dMispairedQuote/RUN.md`, and it does so on `origin/main` rather than only in a
worktree. The red is a FALSE POSITIVE: every one of that build's six standing blockers was disposed,
three by PROMOTION and three by FOLD, and the check counts only the promotion arm. Units 1 and 2 give
the driver a disposition field and make check 2 read it, but neither can reach a record that already
exists, because every phase writer refuses a terminal one. This unit writes FOUR exit rows'
dispositions by hand — two in `dMispairedQuote` and, under the owner's cutoff ruling of 2026-09-01,
two in `dBriefedPass` — labelled as reconstructed the way two `landed-anchor` repairs already were,
and supersedes `TOOL-aClosedDocket-4`.

## 2. Scope (IN)

- **S1 — reproduce, then verify, before writing a byte.** Re-run the leg and confirm the message
  **this unit's PRE-IMAGE ships, which is not the message this spec was authored against.**
  `TOOL-dFoldedVerdict-2` lands at order 3, one unit ahead of this one, and replaces the shortfall
  sentence with an absent-disposition refusal, so a reproduction aimed at the BASE wording would
  report a sibling as
  having broken the leg. Section 4 carries both messages, each labelled with the image it belongs to,
  and the reproduction targets the second. Then re-derive the disposition of all six blockers from
  `dMispairedQuote`'s own reviews and spec revision logs. **If any blocker was silently dropped, the
  red is TRUE and this unit reports that instead of clearing it.** The verification done at authoring
  time is recorded in section 4 and is re-run at build time rather than trusted from here.
- **S2 — `dMispairedQuote`'s two exit rows gain a disposition**, in the byte shape unit 1's writer
  emits, appended to the reason tail after the terminal token. Row 33 takes the promote value and
  row 43 the fold value; the per-subject evidence for each is in section 4.
- **S2a — `dBriefedPass`'s two exit rows gain a disposition, on the same terms.** Owner ruling of
  2026-09-01 taken on Q1: the cutoff is `2026-09-01`, no date separates the two records, and this
  unit therefore labels FOUR rows across TWO landed records rather than two across one. Both of that
  build's subjects exited NON-CONVERGENT, and the `TOOL-dBriefedPass-9` backlog row states that both
  disposed every blocker by FOLDING — but that row is a CLAIM and this unit does not write from it.
  Each disposition is re-derived from `dBriefedPass`'s own reviews and spec revision logs first, on
  AC2a's terms, and a subject whose blockers cannot all be accounted for STOPS the unit exactly as
  it would in the other record. That the record is this build's own predecessor is a reason for more
  care rather than less: a run grading its own prior run is the one place a disposition is likeliest
  to be assumed instead of read.
- **S3 — a `disposition-source:` provenance block** in EACH edited record's `## Run facts` — one
  per record after S2a, never one shared block naming two files — stating why no
  verb could write those rows, what independently verifies each value, and what is deliberately not
  reconstructed. It copies `landed-anchor-source:` one key over.
- **S4 — the mixed-exit rule is written down IN A NAMED CARRIER**, because one of the two subjects
  took BOTH dispositions and a rule discovered per record is a rule nobody applies next time. The
  carrier is a new class record at `memory/gotchas/one-value-field-records-a-mixed-outcome.md`. Its
  derived anchors reach `memory/builds/dMispairedQuote/RUN.md` and both scripts that read the field,
  so `python tools/memory-tree/gotchas.py --for-diff` hands the rule to the next agent whose diff
  touches a run-state record instead of waiting to be looked up. Section 4 says why that corpus and
  not the protocol.
- **S5 — `TOOL-aClosedDocket-4` is superseded**, as a status flip with a successor pointer and never
  a deletion. Two acts, not one: the spec header flips, and the amendment is recorded on
  `aClosedDocket`'s own live run record with `--rescope --act retire --item TOOL-aClosedDocket-4`,
  naming this unit as the successor **in `--reason` and never in a `--successor` field.** Check 24's
  RETIRE arm demands that row and a `--act supersede` row would red its successor arm permanently,
  on another build's record. Section 4 carries both arms read at source and the reason the act is
  `retire`.
- **S6 — the generated artifacts are regenerated in the same commit** as the claim edit, so hygiene
  check 9 and the build README slot contract stay green over the flipped status. S4's new class
  record adds a second render to that step: `python tools/memory-tree/gotchas.py --write` re-renders
  `memory/gotchas/INDEX.md`, which hygiene check 17 byte-compares.
- **S7 — the acceptance is CORPUS-WIDE, never record-wide.** The leg is asserted to exit 0 over
  every tracked run-state record, not over `dMispairedQuote` alone. Fixing one file and scanning
  only that file certifies coverage this unit does not have, and section 8 names a live instance of
  exactly that exposure.
- **S8 — the `TOOL-dMispairedQuote-7` backlog row is repointed.** That row's text records it as
  SUPERSEDED BY `TOOL-aClosedDocket-4` — the unit S5 is about to flip to WONTDO — so without this
  item the backlog's only route from the measured defect to its fix names a WONTDO unit, and it goes
  stale in the same commit that fixes it. The pointer is repointed at `TOOL-dFoldedVerdict-1`,
  `TOOL-dFoldedVerdict-2` and `TOOL-dFoldedVerdict-3`, the three units that answer it.
  `memory/backlog/TOOL.md` is edited in place: one row's text, no new row and no new id. This item is
  owned HERE and not by `TOOL-dFoldedVerdict-2`, whose own backlog scope is the two rows that unit
  answers.

## 3. Non-goals (OUT)

- **N1 — no driver and no checker code.** The disposition flag belongs to `TOOL-dFoldedVerdict-1`
  and check 2's new predicate to `TOOL-dFoldedVerdict-2`. This unit writes records only, which is
  why no `ARMS_FLOORS` pin is touched and why `KIT_UNATTENDED_VERSION` does not move here. That bump
  is the build's LAST landing unit's — `TOOL-dFoldedVerdict-6` — by owner ruling of 2026-09-01, and
  it moves ONCE across the carriers `bash tools/check-kit-versions.sh` asserts AGREE rather than
  move. No file under `tools/` is touched by this unit at all.
- **N2 — the other eleven records with an exited subject are not retrofitted.** Measured over the
  tracked corpus: thirteen run-state files carry a `NON-CONVERGENT` or `CEILING` review row, and
  eleven of them are dated 2026-08-31 or earlier. They are unit 2's cutoff's business.
- **N3 — WITHDRAWN at rev-4, by its own trigger.** It read "`dBriefedPass` is not retrofitted here"
  and carried the condition that if unit 2's cutoff admitted that record, the scope would grow
  rather than the acceptance shrink. The trigger FIRED: the owner set the cutoff at `2026-09-01` on
  2026-09-01, which admits it, so the retrofit is IN SCOPE at S2a and this is no longer a non-goal.
  The item is kept rather than deleted, so the reason the scope moved stays readable in the spec
  instead of only in the log.
- **N4 — no per-blocker attribution.** The row carries one value per SUBJECT. A mixed exit's full
  accounting stays in the spec revision log that already holds it.
- **N5 — the hand-edit class is not gated.** `TOOL-aBoundedCeiling-11` is OPEN and records it:
  nothing refuses a hand-written terminal phase, and by the same argument nothing detects a
  hand-edited parked row in either direction — neither a label that was never earned nor a row a
  verb should have written. This unit performs that class deliberately and says so; closing it is a
  separate mechanism nobody has designed.
- **N6 — clause 3's vacuity on the prompt path is not closed here.** It is `TOOL-aClosedDocket-4`'s
  N2 and it survives the supersession as unit 2's problem.

## 4. Design

### The red, reproduced — and at WHICH image

Two messages carry this red, one per image, and only the second is the one S1 reproduces. Pinning the
first would calibrate the integrity check against text that no longer exists when it runs.

**At BASE `adc0543c`, which is NOT this unit's pre-image:**

```
UNATTENDED check 2 FAILED — review loops that ran past the ceiling, stalled without recording it, or exited without promoting:
  memory/builds/dMispairedQuote/RUN.md (2 subject(s) EXITED without converging and the generated units region gained only 1 non-WONTDO unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted. This is a LOWER BOUND: it demands one surviving id per exited SUBJECT, not one per standing BLOCKER, because the region records ids and not which subject promoted them)
```

Observed 2026-09-01 on this worktree at `adc0543c`; `bash tools/unattended/check-unattended.sh`
exited 1. The count is reproducible by hand: the generated units region of that build's README holds
three ids at HEAD and two at its run BASE `d9efe373`, so `newids` is 1 against an `nneed` of 2. The
record and the README are both on `origin/main` at `3fb57da7`, so this is not a worktree artifact.

**At this unit's PRE-IMAGE, after `TOOL-dFoldedVerdict-1` and `TOOL-dFoldedVerdict-2` land:** that
sentence is gone. Unit 2's S7 rewrites clause 3's messages for the graded path and its own Migration
section says so outright — the red changes from a shortfall claim to an **absent-disposition
refusal**, naming the file and its exited subjects and carrying no counts at all. Unit 2's AC1 states
the same expectation from the other side, naming both `memory/builds/dMispairedQuote/RUN.md` and
`memory/builds/dBriefedPass/RUN.md` under that refusal with `DISPOSITION_CUTOFF="2026-09-01"`
declared. That is the observation S1 reproduces and AC1 below asserts; the shortfall wording above is
kept only as the BASE-image record of what this design was derived from. Neither message is quoted
verbatim for the pre-image here, because unit 2 owns the wording and a second copy of it in this
document is a copy that rots — AC1 asserts the refusal's CLASS and the names it carries.

### The disposition, per subject, verified from that build's own records

Two subjects exited. Neither exit dropped a blocker.

| Exit | Subject | Blockers standing | Disposition | Where the evidence is |
|---|---|---|---|---|
| round 2 | `TOOL-dMispairedQuote-1` | 4 — findings 1, 8, 17, 24 | 3 PROMOTED, 1 FOLDED | that spec's rev-3 line; `2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round2.md` |
| round 3 | `TOOL-dMispairedQuote-3` | 2 — rows 1, 2 | both FOLDED | that spec's rev-4 line; `2026-09-01-review-TOOL-dMispairedQuote-3-spec-audit-round3.md` |

Unit 1's round-2 report names its four blockers as findings 1, 8, 17 and 24 and its exit as a rise
from 2 to 4 against a ceiling of 2. Its spec rev-3 line disposes them explicitly: findings 1, 8 and
17 PROMOTED to `TOOL-dMispairedQuote-3` because bounding what the corrected views un-hide needs a
mechanism that unit does not have, and finding 24 FOLDED by narrowing `LITERAL_OPENERS` from fourteen
members to eleven and fixturing the set. Unit 3's round-3 report holds at 2 blockers against a
ceiling of 2, calls the loop's exit in its own text, and prescribes a FOLD for both rows — "Neither
needs a capability this build lacks". Its spec rev-4 line records both as FOLDS and names the two
repairs. Six blockers, six dispositions, none parked, waived or dropped. **The red is false.**

### The mixed exit, and how one row records it

Unit 1's subject took BOTH dispositions, which the field as ratified cannot spell: the enum the build
README and the rendered Skill both declare has two members, fold and promote. The rule this unit
writes down and applies:

**A subject whose standing blockers took both dispositions records the promote value.** Promote is
the arm that leaves an id, so it is the half a machine can still corroborate — the units region
gained exactly `TOOL-dMispairedQuote-3` between that run's BASE and HEAD — and the promoted unit's
own spec is where the whole exit's accounting lives, fold half included. Recording the fold value
instead would be false about three of the four blockers and would throw away the only corroborable
claim on the row. A third enum member was rejected: see the alternatives below.

**Where the rule lives, and why not the protocol.** S4 exists because a rule discovered per record is
a rule nobody applies next time — so a rule whose only home is the `disposition-source:` block of the
one record that provoked it is buried, not written down. Round 1's audit found exactly that: the word
"mixed" occurred nowhere in this build outside this spec and the block it emits. The carrier is a new
class record under `memory/gotchas/`, and the choice is deliberate rather than convenient:

- **Not `memory/guides/UNATTENDED-PROTOCOL.md`.** That document is moved and compressed by
  `TOOL-dFoldedVerdict-5` and `TOOL-dFoldedVerdict-6`, and neither carries a scope item for this
  sentence. Writing the requirement into this spec and expecting a sibling to satisfy it is the
  producer-less handoff round 1 filed as its own finding class, one unit over. A spec may not assign
  work to a unit that owns no carrier for it.
- **Not `memory/guides/BUILD-METHOD.md` M4**, which is the sentence the rule amends. That file is a
  RENDER of a template under `tools/`, so amending it moves a shipped kit file — which N1 forbids
  here and which would make a record-only unit edit the memory-tree kit.
- **The gotchas corpus fits the shape.** The class is real and is not specific to this record: a
  field that holds ONE value is asked to record an outcome that had two, and whichever value is
  written is false about part of it. The corpus is routed by DERIVED anchors, so
  `python tools/memory-tree/gotchas.py --for-diff` hands the rule to the next diff that touches a
  run-state record rather than waiting to be remembered. Hygiene check 18 makes the record declare
  its resolution and check 19 makes it prove it can fire; N5 already states this class is ungated, so
  the record says "no gate" in as many words rather than implying one.

Section 6 observes the carrier by grep and by `--for-paths`, so a pass that writes the rule nowhere
fails a criterion instead of passing quietly.

### Why no verb can write these two rows

Three independent refusals, each read at source in `tools/unattended/unattended.sh`:

- The record is at `phase: ABORTED`, `PHASES_TERMINAL` is `LANDED ABORTED` at `:334`, and
  `verb_review` calls `refuse_if_terminal` at `:3908` before it validates anything.
- Even on a live record, `verb_review` refuses a subject that already carries a terminal token
  (`:3952`), so a second review round cannot add the field to a row that already exists.
- No verb edits an existing parked row at all. `park()` at `:3796` appends with `>>`, and
  `set_fact()` at `:2728` rewrites only lines whose first characters are the key followed by a colon
  and a space, which no parked row has.

That is why this is a hand edit and not a verb call, and it is why `TOOL-aClosedDocket-4`'s N4 —
"retrofitting the flag onto landed run-state files", refused on the ground that "Clause 3's
promotion arm still passes them" — has a false premise. That premise is already recorded as false in
the `TOOL-dMispairedQuote-7` backlog row.

### The provenance block, and the precedent it copies

`memory/builds/dCarriedReceipt/RUN.md:14-21` is the shape. A `landed-anchor: remote` line sits beside
a `landed-anchor-source:` block that names who reconstructed it and when, says why the verb could not
write it, states what independently verifies the value, and names the one field deliberately left
unreconstructed. `memory/builds/aGroundedOrientation/RUN.md:17` carries the same key as a single line
for the same class — rev-1 cited `:11`, which is that file's `## Run facts` heading; corrected here
after round 1 re-derived it. Two tracked records carry it today. The prompt for this unit said four records
were repaired that way; only two carry the key and the commit trail names two repair commits, so the
figure four is **UNVERIFIED** here and nothing in this unit rests on it.

Two things about that precedent are worth carrying and one is worth not carrying:

- The provenance key is NOT in the declared fact set. `memory/guides/UNATTENDED-PROTOCOL.md:167` says
  the authored half carries "these facts and nothing else" and defines the set as the driver's
  `set_fact` keys plus three more. `landed-anchor-source` is not among them, no verb writes it, and
  neither `unattended.sh` nor `check-unattended.sh` reads it. So the clause is prose that nothing
  enforces and two tracked records already sit outside it. This unit makes that three, and section 8
  routes the question to the protocol units rather than settling it silently.
- The key is safe against both fact readers. `fact()` at `:641` and `fact_of()` at `:491` match a
  line whose prefix is the key followed by a colon, so `disposition-source:` can never be returned
  for a read of `disposition`, exactly as `landed-anchor-source:` is never returned for
  `landed-anchor`.
- What is NOT copied: `dCarriedReceipt` carries `landed-anchor: remote` twice, at `:15` and `:22`.
  First-match-wins makes the duplicate harmless and it is still a wart. This unit writes each key
  once, appended after `base:` so no existing key's first-match position moves.

### Data model

The row shape, with the field appended to the reason tail after the terminal token:

```
2026-09-01T09:58:47Z review · item TOOL-dMispairedQuote-1 · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT · disposition promote
2026-09-01T12:04:02Z review · item TOOL-dMispairedQuote-3 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT · disposition fold
```

Appending inside the reason tail is safe against every reader of that row, verified at source rather
than assumed. Both parsers split at the FIRST reason separator — `check-unattended.sh:285-286` and
the driver's `review_counts` and `review_last_reason` — so nothing appended after it can be mistaken
for an item name. Clause 3 then regexes the tail for a blocker count and for the three terminal
tokens, and an unknown trailing field is inert to both. No other check parses a `review` row: check
17 parses `waiver` rows and check 23 parses `dispatch` rows, and both key on their own kind. This is
`TOOL-aClosedDocket-4`'s Q1 fact-question, re-derived here rather than inherited.

The provenance block, drafted in full so the review can grade the words and not the idea:

```
disposition-source: reconstructed 2026-09-01 by TOOL-dFoldedVerdict-3 — this record is at phase
  ABORTED and `verb_review` calls `refuse_if_terminal` before it writes anything, so the review verb
  cannot reach it; independently, that verb also refuses a subject that already carries a terminal
  token, so no verb could retrofit these rows on a live record either, and no verb edits an existing
  parked row at all. Both values are VERIFIED against this build's own records rather than inferred.
  Subject TOOL-dMispairedQuote-1 exited round 2 with four blockers and disposed 1, 8 and 17 by
  PROMOTING them into TOOL-dMispairedQuote-3 and 24 by FOLDING it, recorded in that spec's rev-3
  line; subject TOOL-dMispairedQuote-3 exited round 3 with two and disposed both as FOLDS, recorded
  in its rev-4 line and prescribed by that round's own review. The promote half is independently
  corroborable: the generated units region gained exactly TOOL-dMispairedQuote-3 between base
  d9efe373 and HEAD. The fold half is not, which is the whole reason the field is authored. A
  PER-BLOCKER attribution is deliberately NOT reconstructed — the row carries one value per subject,
  a mixed exit records the promote value, and the fold half's accounting stays in the rev-3 line
  named above.
```

No continuation line begins with a dash or a pipe, so the protocol's anchor ban holds and no id in
that block is anchored to this build folder.

### The supersession, which is two acts — and only one of them is a `supersede`

`TOOL-aClosedDocket-4` is RATIFIED, OPEN, and order 4 of a run stalled at `BUILDING`. The owner
authorized this build taking its scope after being shown the collision, and the build README records
that ruling; M3 does not delegate a sibling build's scope, so this is an owner act.

1. The spec header flips to `WONTDO` with the successor pointer in its tail, dated 2026-09-01. The id
   stays in the units region — a status flip, never a deletion. Its section 8 is already fully
   RESOLVED, which is what hygiene check 12 requires before a terminal status. The rev moves to rev-3
   with a section 9 line, because a successor pointer is a content change and not the pure status
   flip `memory/TEMPLATE-SPEC.md` exempts from a rev bump.
2. `bash tools/unattended/unattended.sh --rescope aClosedDocket --act retire --item
   TOOL-aClosedDocket-4 --reason "scope taken by TOOL-dFoldedVerdict-3 under the owner ruling of
   2026-09-01"` records the amendment on that build's own run record. The reason names the successor
   as a BARE id and nothing else — no path and no link, so nothing in the other run's record is
   anchored into this build folder, and the id is enough to find it. **This half is not optional.** Check 24's RETIRE arm demands a `retire` or `supersede`
   rescope row for any id that is WONTDO now and was not so at the run's pinned baseline; verified,
   that record's baseline units region at `733552e1` carries no unit rows at all, so the fallback
   baseline applies and the row is still owed. Without it this unit trades check 2's red for
   check 24's. The verb accepts it: the record is at `phase: BUILDING`, so `refuse_if_terminal`
   passes, and `TOOL-aClosedDocket-4` is in the current units region, which is the membership test
   `verb_rescope` applies to `--item` for both `retire` and `supersede`.

**Why the act is `retire` and NOT `supersede`, which is what rev-1 wrote.** Round 1's audit filed
this as its only blocker and it is confirmed at source; the reasoning rev-1 gave for the act was
inverted, so it is replaced rather than defended.

Check 24 has TWO arms over rescope rows and a `supersede` row reaches both:

- The RETIRE arm at `tools/unattended/check-unattended.sh:1770` is satisfied by either act — its
  predicate is `grep -qE "item (retire|supersede) $rsid( |$)"` over the record's rescope rows.
- The SUPERSESSION arm at `:1777-1780` then extracts every `item supersede <id> -> <succ>` and reds
  unless `id_in "$rs_now" "$rssucc"`. `rs_now` is bound at `:1713` to THAT record's own build README
  `gen:build-units` region, which for `aClosedDocket` carries `TOOL-aClosedDocket-1` through `-4` and
  nothing else. `id_in` at `tools/unattended/lib-unattended.sh:37` is a whole-token match. **A
  `dFoldedVerdict` id can never be a member of it.**

So a `--act supersede --successor TOOL-dFoldedVerdict-3` row does not clear a red, it CREATES one,
and it creates it permanently on another build's record. The record is at `BUILDING`, so the
`LANDED|ABORTED` skip never applies; `verb_rescope` membership-tests only `--item` and never the
successor, so the driver ACCEPTS the write; `park()` at `tools/unattended/unattended.sh:3796`
appends with `>>` to a record no verb rewrites, and no verb can remove a row. Only a second hand edit
could clear it, on a build this session does not own. That is the exact opposite of this unit's
purpose.

**Check 24 has no cross-build supersession shape, and that is by design rather than by omission.**
The arm's own comment reads that a supersession which never landed its replacement is a retirement
wearing a better name — `--act supersede` is a WITHIN-build mechanism whose successor is graded
against the executing roster, and no record sanctions a successor from another build. A `retire` row
carries no ` -> ` and therefore never reaches the successor arm at all, while satisfying the RETIRE
arm that actually demands it. The successor is named in `--reason`, which the leg does not parse and
which a reader of the other run does. If a true cross-build supersession record is ever wanted, it is
its own unit against `tools/unattended/check-unattended.sh:1776` with its own backlog row, and not a
scope item here.

**The flag is `--item`, not `--unit`, and the driver's own refusals misspell it.** Verified at
source: the arg loop binds `--item` to `PK_ITEM` at `tools/unattended/unattended.sh:4781` and
`--unit` to `BR_UNIT` at `:4783`, which only `--brief` reads; the dispatch at `:4852` passes
`$PK_ITEM` as `verb_rescope`'s third positional, and the driver's own usage header at `:14` spells
`--rescope <slug> --act <...> --item <id>`. Spelled `--unit`, `PK_ITEM` is empty and the verb refuses
before writing anything — reproduced by round 1, which got `check 48 FAILED — --rescope --unit is not
id-shaped by the driver's own spelling … (none)`. **The trap is worth carrying:** `verb_rescope`'s
own `fail 48` texts name the parameter `--unit` while the parser takes `--item`, so an operator who
copies the refusal is misled by it, and rev-1 of this spec copied the message rather than the parser.
The same misspelling appears in `TOOL-dUnstalledConvoy-5`'s AC1, so it reads as a house spelling
rather than a typo.

What this build discharges of that unit's scope, and what it does not:

| Item | Where it goes |
|---|---|
| S1, S1a, S2, S4, S4a | `TOOL-dFoldedVerdict-1` — the flag, its refusal, the round row, the success lines |
| S3, S4b | `TOOL-dFoldedVerdict-2`, but EXCEEDED: S3 made the disposition an OR-arm beside the id proxy and the owner ruling REPLACES the proxy |
| S5 | `TOOL-dFoldedVerdict-2` owns the gate arms; this unit owns the corpus-wide arm in section 6 |
| S6, S6a | units 1 and 2, which are the ones that move a shipped file |
| N4 | **REVERSED by this unit.** Its premise is false and the provenance block says so |
| N2 | **NOT discharged.** Clause 3's vacuity on the prompt path survives as unit 2's problem |
| N1, N3 | unchanged and still true |

### Inventory

| Path | Change |
|---|---|
| `memory/builds/dMispairedQuote/RUN.md` | S2, S3 — two row tails and one provenance block |
| `memory/gotchas/one-value-field-records-a-mixed-outcome.md` | S4 — the mixed-exit rule's carrier, a new class record |
| `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-4.md` | S5 — header flip, successor pointer, section 9 line |
| `memory/builds/aClosedDocket/RUN.md` | S5 — the `retire` rescope row, written by the verb |
| `memory/backlog/TOOL.md` | S8 — one row's successor pointer, repointed in place |
| `memory/LIVE.md`, `memory/ledger/2026-09.md`, `memory/builds/aClosedDocket/README.md`, `memory/gotchas/INDEX.md` | S6 — regenerated |

### Migration

None. Nothing reads a disposition field before unit 2 lands, so the labels are inert until then and
the record is legal at every intermediate commit.

### Rollout

Order 3, after units 1 and 2. Landing the labels before check 2 reads them leaves two inert fields;
landing check 2's new predicate before the labels leaves main red for a different reason than it is
red for now. The regeneration in S6 rewrites generated regions across the whole memory tree, so this
pass does not run concurrently with any sibling pass that writes a build README or a generated index.
S8 adds a second reason for the same isolation: `memory/backlog/TOOL.md` is a `SHARED_RECORDS`
member, and `TOOL-dFoldedVerdict-2`'s own S13 edits two other rows in it. Order 3 is after order 2,
so the two writes are sequential rather than concurrent, and neither pass may run beside the other.

### Files touched (estimate)

Five tracked files written — four by hand, one of them new, and one by a verb rather than by hand —
and four generated files re-rendered. No file under `tools/` moves.

### Alternatives rejected

- **A third enum member for a mixed exit.** It amends a sibling unit's interface from inside this
  one, and `memory/guides/BUILD-METHOD.md` M2 makes a disagreement between two specs a defect in
  exactly one document. If the owner wants it, it belongs to unit 1 and this spec follows.
- **A second review row for the folded half of unit 1's exit.** Refused twice over: the driver
  refuses a second round on a subject carrying a terminal token, and check 2 derives its sequence
  from the line set, so a second row would corrupt the blocker sequence it grades.
- **Retro-promoting the folded blockers into units to satisfy the counter.** Already refused on the
  `dMispairedQuote` record itself, and for the right reason: all six are fixed and built, and a unit
  invented to move a number is the shape this repo gates against everywhere else.
- **Waiting for node `a` to land `TOOL-aClosedDocket-4`.** That run has been stalled at `BUILDING`
  for over a day and main stays red meanwhile. The owner ruled against it.
- **Leaving the red and waiving the leg.** An exemption is not coverage, and the leg has no waiver
  channel for one record.

## 5. Production-readiness checklist

- **security** — a hand-written field that a merge-bar leg will read is exactly the
  self-certification this kit refuses elsewhere, and section 4 says so plainly rather than burying
  it. The mitigation is provenance and corroboration, not a claim of safety: the promote half is
  checkable against the id delta, the fold half is not, and the block says which is which. N5 names
  the class as ungated.
- **perf / scale** — nil. Two row tails and one block; the leg gains no work.
- **a11y** — N/A — a tracked markdown record with no rendered surface.
- **i18n** — N/A — same reason.
- **error / empty / loading states** — N/A for a record edit. The failure mode that matters is a
  malformed row, and section 6 observes the leg rather than eyeballing the bytes.
- **observability** — the disposition sits on the row where check 2 reads it and the provenance sits
  in the record a resuming agent reads. Nothing else reads either, and no reader is claimed here that
  does not read.
- **risks** — three. A byte shape that disagrees with unit 1's writer, addressed by the equality arm
  in section 6. A rescope row that reds check 24 on ANOTHER build's record — the live risk, since the
  driver accepts the write and no verb can remove the row; addressed by S5's `retire` act and by
  AC9's assertion of both arms. A cutoff that admits `dBriefedPass`, addressed by S7's corpus-wide
  acceptance and section 8 Q1. Rollback is a revert of one commit; no state moves.
- **testing + left-shift gates** — the left-shift belongs to unit 2, whose predicate is what stops
  the next correctly-folded exit redding the bar. This unit's own class, a hand-edited parked row, is
  left ungated and named, which N5 states rather than implies. A SECOND left-shift is named by round
  1 and is deliberately NOT taken here: `verb_rescope` should membership-test `--successor` against
  the same roster check 24 reads and refuse at write time, since a driver that accepts a write its
  own merge bar reds forever is a guard sharing nothing with the thing it guards. It is driver code,
  which N1 excludes, and it is recorded in this build's round-1 audit record rather than filed as a
  backlog row, because this unit mints no id. Named, not covered.
- **migration / rollback** — see the Migration and Rollout sub-heads above. Reversible by revert.
- **user docs** — none owed to `help/`, and the mixed-exit rule is NOT what that means. It is a
  governance rule with a named carrier of its own under S4, observed by AC12 and AC13; section 8 Q2
  is a different question and settles only the provenance-key form. Rev-1 routed the rule to Q2,
  which asks nothing about mixed exits; round 1 caught it.

## 6. Acceptance criteria

- **AC1** — When the leg is re-run before any edit, at THIS UNIT'S PRE-IMAGE and not at BASE,
  `bash tools/unattended/check-unattended.sh` exits 1 and its check 2 output names
  `memory/builds/dMispairedQuote/RUN.md` under `TOOL-dFoldedVerdict-2`'s ABSENT-DISPOSITION refusal —
  the record named for recording no disposition, its exited subjects named, and no shortfall counts
  in the sentence. The red is observed by this unit, not inherited from this spec. **The criterion is
  the refusal's class and the names it carries, never its bytes**, because unit 2 owns the wording
  and a literal pinned here would be a second copy of a sentence a sibling is scoped to write. If the
  pre-image still carries the BASE shortfall message quoted in section 4, unit 2 has not landed and
  this unit does not start.
- **AC2** — When `dMispairedQuote`'s six blockers are re-derived at build time, every one has a
  disposition recorded
  in section 9 of `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md` or
  of `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md`. If any has none,
  the unit STOPS and reports the red as true; a disposition invented to clear a gate is the one
  outcome this unit may not produce.
- **AC2a** — When `dBriefedPass`'s blockers are re-derived on those same terms — its spec-set
  subject exited NON-CONVERGENT at 3 blockers and its build subject at 4 — every one has a
  disposition recorded in that build's own reviews or spec revision logs, and the same STOP applies.
  The `TOOL-dBriefedPass-9` backlog row's claim that both loops folded is corroboration and is
  explicitly NOT the evidence: a criterion satisfied by a summary of the thing it grades is the
  vacuity this build exists to remove, reproduced one level up.
- **AC3** — When the rows and the provenance blocks are written, `grep -c 'disposition promote'`
  and `grep -c 'disposition fold'` over `memory/builds/dMispairedQuote/RUN.md` each return 1, and
  `grep -c '^disposition-source:'` over the same file returns 1. Over
  `memory/builds/dBriefedPass/RUN.md` the provenance count returns 1 and the promote and fold counts
  SUM to 2 — pinned here as a SUM and not as a split, because pinning the split would make this
  criterion assert the very answer AC2a exists to derive.
- **AC4** — When the record is re-read afterwards, `bash tools/unattended/unattended.sh --status
  dMispairedQuote` still reports the same phase and witness it reported before the edit, proving no
  fact key's first-match position moved.
- **AC5** — When a throwaway clone under `mktemp -d` is seeded with a non-terminal run record and
  driven to a NON-CONVERGENT exit by two `bash tools/unattended/unattended.sh --review` calls
  carrying unit 1's new flag, `diff` shows the emitted row's reason tail is byte-identical to the
  tail this unit wrote by hand. This is the byte-shape agreement with unit 1, observed rather than
  asserted, and it exercises the shipped driver and not the kit self-test suite.
- **AC6** — When the two dispositions are removed from the record and the removal is STAGED,
  `bash tools/unattended/check-unattended.sh` exits 1 again, naming that file under the same
  absent-disposition refusal AC1 observed. Without this arm the
  criterion below cannot tell a check that accepts a fold from one that stopped checking. Stage the
  break with `git add` before running, because the leg's population is the index, and restore it with
  `git stash` rather than `git checkout --`, which would restore the whole file and silently discard
  the provenance block.
- **AC7** — When the leg is run over the whole tracked corpus after units 1 and 2 have landed,
  `bash tools/unattended/check-unattended.sh` exits 0. This is asserted over EVERY tracked run-state
  record and not over the edited one, so a sibling record that unit 2's cutoff newly admits fails
  this criterion instead of hiding behind it.
- **AC8** — When the supersession is performed, the header of
  `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-4.md` reads WONTDO with a
  successor pointer in its tail, the id is still present in that build's generated units region, and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the flip.
- **AC9** — When the rescope row is written, BOTH of check 24's arms are asserted by name over
  `memory/builds/aClosedDocket/RUN.md`, because one of them is what rev-1's design would have broken:
  - the RETIRE arm is SATISFIED — `grep -F 'rescope · item retire TOOL-aClosedDocket-4'` over that
    record returns exactly one line, whose `reason` field names `TOOL-dFoldedVerdict-3`, and
    `bash tools/unattended/check-unattended.sh` reports no check 24 failure for that record;
  - the SUPERSESSION arm is NEVER REACHED — `grep -c -- ' -> ' memory/builds/aClosedDocket/RUN.md`
    returns 0 over the rescope rows, so no `item supersede <id> -> <succ>` row exists for
    `check-unattended.sh:1777` to extract and no successor is graded against that build's roster.
  Removing the row and re-running must red check 24 on the RETIRE arm, which is what proves the row
  is load-bearing rather than decorative. Writing it with `--act supersede --successor` instead must
  red the SUPERSESSION arm, which is what proves the act was chosen and not defaulted — observe that
  second arm on a throwaway clone under `mktemp -d`, never on the tracked record, because the row is
  appended to an append-only file and no verb can remove it.
- **AC10** — When the generated artifacts are re-rendered in the same commit,
  `python3 tools/memory-tree/gen_build_index.py --check` and
  `python3 tools/memory-tree/gen_build_index.py --check-format` both exit 0.
- **AC11** — When the record's size is measured after the edit, `wc -c
  memory/builds/dMispairedQuote/RUN.md` stays under `INDEX_CAP_BYTES` of 61440 from
  `.memory-tree.conf`, which is the only one of its two bounds a gate enforces, and under the 8 KB
  authored-region budget `memory/guides/UNATTENDED-PROTOCOL.md` declares in prose and nothing checks.
  Measured before the edit: 5521 bytes, with the two rows at 116 bytes each.
  `memory/builds/dBriefedPass/RUN.md` is measured the same way against the same bound at build time.
  Its pre-edit size is deliberately NOT carried here, because this spec never measured it and a
  figure written down unmeasured is exactly the class `TOOL-dFoldedVerdict-6` F3 was just resolved
  against. The per-entry budget is
  NOT a bound here and this criterion does not claim it is: hygiene check 7's exemption list excludes
  `builds/*/RUN.md` by name, which is why a 1465-byte parked row already sits in this record and
  passes.
- **AC12** — When S4's carrier is written,
  `grep -n 'records the promote value' memory/gotchas/one-value-field-records-a-mixed-outcome.md`
  returns the rule's own sentence, the record's front matter carries `name` and `description` at
  column 0, and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 — which is what asserts the
  class declares its resolution (it declares NONE, in as many words, matching N5) and that
  `memory/gotchas/INDEX.md` byte-matches a fresh render after S6.
- **AC13** — When the carrier is asked whether it can FIRE,
  `python tools/memory-tree/gotchas.py --for-paths memory/builds/dMispairedQuote/RUN.md` lists that
  class in its stdout. Anchors are DERIVED from the backticked paths in the body, so this is the arm
  that separates a rule written down from a rule written down where the next diff will meet it.
  Without it, a record naming no reachable path is only REPORTED as inert and the pass still looks
  complete.
- **AC14** — When S8's repoint is written, `grep -n 'TOOL-dMispairedQuote-7' memory/backlog/TOOL.md`
  returns one row naming `TOOL-dFoldedVerdict-1`, `TOOL-dFoldedVerdict-2` and `TOOL-dFoldedVerdict-3`
  as what answers it, with no live successor pointer at the id S5 has just flipped to WONTDO, and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the edit — the id-citation and
  one-id-one-row-per-document checks are what grade it.

## 7. Gates

Named legs, each resolved in `tools/gate-legs.json` rather than remembered:

- `unattended kit gate` — the leg that is red today and the one this unit exists to green. Unguarded,
  so it runs on every bar.
- `memory hygiene` — grades this spec's own format, the flipped status header, the record's caps and
  entry budget, and the id citations in every edited record. It is also the leg that grades S4's new
  class record — that it declares a resolution, that it derives an anchor rather than sitting inert,
  and that `memory/gotchas/INDEX.md` matches a fresh render — and S8's repointed backlog row.
- `build README slot contract` — the format check over the build READMEs S6 re-renders.
- `pass-order history` — reads the same run-state records for their pinned BASE; named because this
  unit edits two of them and the leg must be seen to stay green rather than assumed to.
- `drift-audit records` — the repo's own record-versus-reality check, which is the class this unit's
  hand edit is closest to.

No new gate. The predicate that makes the next folded exit legible belongs to
`TOOL-dFoldedVerdict-2`, and this unit deliberately adds none of its own: N5 states that the
hand-edited-row class stays ungated in both directions, and section 5 names the second candidate —
a write-time successor refusal in `verb_rescope` — as owed, unfiled and out of this unit's scope
rather than leaving it to read as covered.

**A standing owner instruction forbids running the unattended kit self-tests**, so
`tools/unattended/*.test.sh` and `bash tools/unattended/run-unattended-gates.sh --selftests` are NOT
run by this unit and no criterion in section 6 depends on them. What that costs, said plainly: the
byte shape of a retrofitted row is normally something that suite would compare, and here it is
witnessed instead by AC5's throwaway-clone run of the driver itself and by AC6's staged break
observed RED against the real leg. Both exercise the shipped code rather than a copy of it, and
neither substitutes for the arms unit 1 and unit 2 owe their own mechanisms.

## 8. Open questions

- **Q1 — does unit 2's cutoff admit `dBriefedPass`, and does this unit's scope grow by two rows if it
  does?** RESOLVED (owner, 2026-09-01): the cutoff is
  `2026-09-01`, and this unit's scope grows to FOUR rows across TWO landed records. Measured, and
  this is the load-bearing fork. Thirteen tracked run-state records carry an
  exited subject; exactly two are dated 2026-09-01, `dBriefedPass` and `dMispairedQuote`, and both
  are terminal, so no DATE cutoff can separate them. `dBriefedPass` is LANDED with two subjects that
  each exited NON-CONVERGENT — the spec-set subject at 3 blockers and the build subject at 4 — and it
  passes check 2 today only VACUOUSLY, because its prompt-mode BASE `269dacae` has an empty units
  region so every planned unit reads as a promotion. That is recorded in the `TOOL-dBriefedPass-9`
  backlog row, which also states that both its loops disposed every blocker by FOLDING. So a cutoff
  at 2026-09-01 admits both records and this unit owes four rows rather than two, while a cutoff
  after that date grandfathers `dMispairedQuote` too and the build's whole premise fails.
  **Recommendation: the cutoff is 2026-09-01 and this unit's scope grows to `dBriefedPass`'s two
  rows, both folds.** Their dispositions must be re-derived from that build's own records first, on
  AC2's terms. AC7 fails loudly if this is got wrong, which is why the acceptance is corpus-wide.
  **`TOOL-dFoldedVerdict-2` has since been read against this and agrees in both directions**, which
  is corroboration rather than a second opinion: its AC1 declares `DISPOSITION_CUTOFF="2026-09-01"`
  and names `memory/builds/dBriefedPass/RUN.md` alongside `memory/builds/dMispairedQuote/RUN.md`
  under the absent-disposition refusal, and its AC4 takes `dBriefedPass` going UNNAMED at `nneed 0`
  as its substitute observation for the fold arm — an observation that exists only once this unit has
  labelled that record's two exits. So the sibling spec both admits the record and depends on this
  unit labelling it. The fork stays OPEN pending the owner's word only because it grows this unit's
  scope; nothing in the two specs now disagrees about which way it falls.
- **Q2 — should the protocol sanction the provenance form this unit uses?** RESOLVED (owner,
  2026-09-01): yes, one sentence — and it lands in `TOOL-dFoldedVerdict-5` at order 1, whose S13
  now carries it. The assignment is this unit's only remaining stake in the question: the sentence
  exists three units before this one writes a row relying on it, and a one-sentence addition stays
  separable inside a diff that is otherwise a verbatim move, where unit 6's document-wide compression
  would leave a reader unable to tell an addition from a reword.
  `memory/guides/UNATTENDED-PROTOCOL.md:167` says the authored half carries the declared facts "and
  nothing else", no verb writes such a key, and nothing reads one — so two tracked records already
  sit outside a clause nothing enforces and this unit makes three. **Recommendation: yes, one
  sentence admitting a source-suffixed line whose value states why a verb could not write the key it
  names.** It belongs to a protocol unit and not to this one, which would otherwise be writing its
  own permission. Rev-3 named this build's protocol units as "orders 5 and 6", which the reorder
  falsified; they are orders 1 and 6, and the ruling put the sentence in the first.
- **Q3 — is this run entitled to write a rescope row into another live run's record?** RESOLVED
  (agent, 2026-09-01): write it, naming this unit in the reason. The alternative leaves a check-24
  red that only the stalled run can clear, and the owner has already authorized taking that build's
  scope, which is the act the row records rather than one it performs. The verb
  permits it: `aClosedDocket` is at BUILDING, so `refuse_if_terminal` passes, and nothing keys the
  write on which session owns the slug. The owner authorized taking that build's scope, and check 24
  demands the row. **Recommendation: write it, and name this unit in the reason so the other run's
  operator reads why its roster moved under it.** The alternative leaves a check-24 red that the
  stalled run is the only party able to clear.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. The red reproduced at `adc0543c`, all six blocker dispositions
  re-derived from `dMispairedQuote`'s reviews and spec revision logs, the three verb refusals and
  both row parsers read at source, and check 24's RETIRE arm found to demand a second act for the
  supersession.
- rev-2 · 2026-09-01 · folded the round-1 spec audit
  ([2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md)).
  Six changes, each named with the finding that drove it:
  - **B1, the blocker.** S5's second act was `--act supersede --successor TOOL-dFoldedVerdict-3`, and
    rev-1's stated reason for it was inverted at source: check 24's successor arm at
    `tools/unattended/check-unattended.sh:1777-1780` reds unless the successor is a whole token of
    that record's OWN units region, which carries only `TOOL-aClosedDocket-1` through `-4`, so the
    row CREATES a permanent red on another build's record rather than clearing one. Re-verified here
    against `rs_now`'s binding at `:1713`, `id_in` at `tools/unattended/lib-unattended.sh:37`, and
    the record's `phase: BUILDING`. The act is now `retire`, whose row carries no ` -> ` and never
    reaches that arm; the successor is named in `--reason`. Section 4 gained the two-arm reading and
    states that check 24 has NO cross-build supersession shape. AC9 was rewritten from one grep into
    an assertion of both arms by name, with the supersede case observed on a throwaway clone because
    the row is unremovable once written.
  - **H7.** The same invocation spelled `--unit`, which the parser binds to `--brief`'s `BR_UNIT` at
    `tools/unattended/unattended.sh:4783` while `--rescope` reads `PK_ITEM` from `--item` at `:4781`.
    Re-verified at source and against the usage header at `:14`. Spelled `--item` now, and section 4
    records the trap: the verb's own `fail 48` texts say `--unit`, so rev-1 copied the refusal rather
    than the parser.
  - **H5.** AC1 pinned the BASE check-2 message and its counts, which `TOOL-dFoldedVerdict-2`
    replaces at order 2 — so the ONE integrity control in this unit, reproduce-before-writing, was
    calibrated against text that will not exist when it runs. Section 4's reproduction sub-head now
    labels the BASE quote as BASE and states the pre-image outcome beside it; AC1 asserts unit 2's
    absent-disposition refusal by CLASS and by the names it carries, never by bytes a sibling owns.
    AC6 follows it.
  - **H3.** S4 required the mixed-exit rule to be "written down" and no file in scope carried it —
    the rule's only home was the provenance block, which is the burial S4 forbids. S4 now names
    `memory/gotchas/one-value-field-records-a-mixed-outcome.md` as the carrier, the Inventory carries
    it, S6 re-renders the catalogue index, and AC12 and AC13 observe both the sentence and the
    record's ability to FIRE on a diff. Section 4 records why that corpus and not the protocol or
    `BUILD-METHOD.md` M4 — both would need a scope item in a unit this one does not own, or a file
    under `tools/` that N1 excludes. Section 5's user-docs bullet no longer routes the rule to Q2,
    which asks nothing about mixed exits.
  - **M9.** Two prior-record claims corrected. Section 10 described the `TOOL-dMispairedQuote-7`
    backlog row as recording this build's supersession of the ratified predecessor; the row's own
    text records the OPPOSITE relation and names no `dFoldedVerdict` id, verified in
    `memory/backlog/TOOL.md`. The `memory/builds/aGroundedOrientation/RUN.md` citation moved from
    `:11`, which is that file's `## Run facts` heading, to `:17`, where the key actually sits. New S8
    repoints that row's successor pointer, since S5 is about to flip the id it names to WONTDO, with
    AC14 over it and `memory/backlog/TOOL.md` in the Inventory.
  - **Owner rulings of 2026-09-01, both checked against this spec.** (b) `KIT_UNATTENDED_VERSION`
    moves ONCE, on `TOOL-dFoldedVerdict-6`: N1 already said no version moves here and now names the
    owning unit, so this spec claimed no other owner and nothing was reversed. (a) At CEILING the
    driver accepts either disposition: it changes no claim in this document, because both rows this
    unit writes are NON-CONVERGENT exits and N2 leaves every CEILING row in the corpus to unit 2's
    cutoff. Recorded so a later reader can see it was checked rather than missed.
- rev-3 · 2026-09-01 · reordered to order 4 by the build's own ordering fix. No scope change: the protocol render sits at EXACTLY `GUIDE_CAP_BYTES` with zero headroom, so `TOOL-dFoldedVerdict-5`'s split moved to order 1 ahead of every unit that adds a protocol byte, and the rest shifted behind it.

- rev-4 · 2026-09-01 · the fork sweep, three owner rulings, and the scope one of them grew.
  **Q1** — the cutoff is `2026-09-01`, which admits `dBriefedPass` as well as `dMispairedQuote`, so
  this unit labels FOUR rows across TWO landed records. N3's trigger fired and N3 is withdrawn; S2a,
  AC2a and the second provenance block in S3 are the scope that replaces it, and AC3 pins the second
  record's counts as a SUM rather than a split so it cannot assert the answer AC2a must derive. One
  of the two records is this build's own predecessor, which S2a treats as grounds for more care.
  **Q2** — the protocol sanctions the provenance form, in one sentence, and it lands in
  `TOOL-dFoldedVerdict-5`'s new S13 at order 1 rather than here or in unit 6: it then exists three
  units before this one writes a row relying on it, and a one-sentence addition stays separable in a
  diff that is otherwise a verbatim move. Rev-3 called this build's protocol units "orders 5 and 6",
  which the reorder had falsified; they are orders 1 and 6. **Q3** — the rescope row is written,
  naming this unit in `--reason`. Two stale ordinals corrected in passing: S1 said unit 2 lands at
  order 2, where it is now order 3 and this unit order 4 — the substance held, only the number was
  wrong, and it is the kind of number a reader trusts without checking.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "repairing a finished unattended run-state record by hand
when no verb can write the field"` returned no seam this unit can extend. Its ranked candidates are
generic writers — `write` and `write_text` in the memory-tree kit, `run` in `tools/settings-merge.py`
— plus the protocol guide's inventory key and the `.unattended.conf` affordance seam, and none of
them reads or writes a run-state record. **No existing seam fits in code, and that is an answer
rather than a probe failure: this unit ships no code.** The seam it extends is a RECORD SHAPE, cited
by path — `memory/builds/dCarriedReceipt/RUN.md:14-21` and
`memory/builds/aGroundedOrientation/RUN.md:17`, the two tracked instances of the provenance form this
design copies one key over. Where a hit was stale: the prompt for this unit described four such
repairs, and only two carry the key in the tracked corpus, so section 4 marks the figure UNVERIFIED
and nothing here rests on it. A second staleness, found by round 1 and corrected in rev-2: the
`aGroundedOrientation` citation read `:11`, which is that file's `## Run facts` heading and not the
key.

Recall terms used: `python tools/memory-recall/query.py "how was a terminal unattended run-state
record repaired by hand when no verb could write the field, and what recorded the provenance"
--terms "unattended run-state terminal phase landed-anchor reconstructed provenance hand-edit
refuse_if_terminal park review disposition fold promote non-convergent"`. It returned the two
precedent records, the `TOOL-aBoundedCeiling-11` class row, the `TOOL-dMispairedQuote-7` row, and the
`TOOL-dBriefedPass-9` row that Q1 rests on. **What that `-7` row actually says, quoted rather than
paraphrased, because rev-1 paraphrased it backwards:** it opens `SUPERSEDED by TOOL-aClosedDocket-4`.
The relation runs the other way from the sentence rev-1 wrote — the row does not record this build's
supersession of that unit; it records itself as superseded BY it, and it names no `dFoldedVerdict` id
at all. It is nonetheless the right hit, for a reason the paraphrase hid: the row's own body already
records that `TOOL-aClosedDocket-4`'s N4 premise is FALSE, which is the fact section 4 builds on. S8
exists because S5 flips that row's stated successor to WONTDO and would otherwise strand the only
route the backlog has from this defect to its fix.

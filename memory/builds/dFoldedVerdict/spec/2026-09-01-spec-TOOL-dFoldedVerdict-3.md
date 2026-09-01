# TOOL-dFoldedVerdict-3 — the two exit rows say which disposition they took, and `origin/main` goes green

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`bash tools/unattended/check-unattended.sh` exits 1 on check 2 against
`memory/builds/dMispairedQuote/RUN.md`, and it does so on `origin/main` rather than only in a
worktree. The red is a FALSE POSITIVE: every one of that build's six standing blockers was disposed,
three by PROMOTION and three by FOLD, and the check counts only the promotion arm. Units 1 and 2 give
the driver a disposition field and make check 2 read it, but neither can reach a record that already
exists, because every phase writer refuses a terminal one. This unit writes the two exit rows'
dispositions by hand, labelled as reconstructed the way two `landed-anchor` repairs already were,
and supersedes `TOOL-aClosedDocket-4`.

## 2. Scope (IN)

- **S1 — reproduce, then verify, before writing a byte.** Re-run the leg and confirm the message.
  Then re-derive the disposition of all six blockers from `dMispairedQuote`'s own reviews and spec
  revision logs. **If any blocker was silently dropped, the red is TRUE and this unit reports that
  instead of clearing it.** The verification done at authoring time is recorded in section 4 and is
  re-run at build time rather than trusted from here.
- **S2 — the two exit rows gain a disposition**, in the byte shape unit 1's writer emits, appended
  to the reason tail after the terminal token. Row 33 takes the promote value and row 43 the fold
  value; the per-subject evidence for each is in section 4.
- **S3 — a `disposition-source:` provenance block** in that record's `## Run facts`, stating why no
  verb could write those rows, what independently verifies each value, and what is deliberately not
  reconstructed. It copies `landed-anchor-source:` one key over.
- **S4 — the mixed-exit rule is written down**, because one of the two subjects took BOTH
  dispositions and a rule discovered per record is a rule nobody applies next time.
- **S5 — `TOOL-aClosedDocket-4` is superseded**, as a status flip with a successor pointer and never
  a deletion. Two acts, not one: the spec header flips, and the amendment is recorded on
  `aClosedDocket`'s own live run record with `--rescope --act supersede`, because without that row
  check 24 reds — this unit trades one red for another otherwise.
- **S6 — the generated artifacts are regenerated in the same commit** as the claim edit, so hygiene
  check 9 and the build README slot contract stay green over the flipped status.
- **S7 — the acceptance is CORPUS-WIDE, never record-wide.** The leg is asserted to exit 0 over
  every tracked run-state record, not over `dMispairedQuote` alone. Fixing one file and scanning
  only that file certifies coverage this unit does not have, and section 8 names a live instance of
  exactly that exposure.

## 3. Non-goals (OUT)

- **N1 — no driver and no checker code.** The disposition flag belongs to `TOOL-dFoldedVerdict-1`
  and check 2's new predicate to `TOOL-dFoldedVerdict-2`. This unit writes records only, which is
  why no kit version moves and no `ARMS_FLOORS` pin is touched.
- **N2 — the other eleven records with an exited subject are not retrofitted.** Measured over the
  tracked corpus: thirteen run-state files carry a `NON-CONVERGENT` or `CEILING` review row, and
  eleven of them are dated 2026-08-31 or earlier. They are unit 2's cutoff's business.
- **N3 — `dBriefedPass` is not retrofitted here**, and it is the one non-goal with a trigger. See
  section 8 Q1; if unit 2's cutoff admits it, S7's acceptance fails and the scope grows rather than
  the acceptance shrinking.
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

### The red, reproduced

```
UNATTENDED check 2 FAILED — review loops that ran past the ceiling, stalled without recording it, or exited without promoting:
  memory/builds/dMispairedQuote/RUN.md (2 subject(s) EXITED without converging and the generated units region gained only 1 non-WONTDO unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted. This is a LOWER BOUND: it demands one surviving id per exited SUBJECT, not one per standing BLOCKER, because the region records ids and not which subject promoted them)
```

Observed 2026-09-01 on this worktree at `adc0543c`; `bash tools/unattended/check-unattended.sh`
exited 1. The count is reproducible by hand: the generated units region of that build's README holds
three ids at HEAD and two at its run BASE `d9efe373`, so `newids` is 1 against an `nneed` of 2. The
record and the README are both on `origin/main` at `3fb57da7`, so this is not a worktree artifact.

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
unreconstructed. `memory/builds/aGroundedOrientation/RUN.md:11` carries the same key as a single line
for the same class. Two tracked records carry it today. The prompt for this unit said four records
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

### The supersession, which is two acts

`TOOL-aClosedDocket-4` is RATIFIED, OPEN, and order 4 of a run stalled at `BUILDING`. The owner
authorized this build taking its scope after being shown the collision, and the build README records
that ruling; M3 does not delegate a sibling build's scope, so this is an owner act.

1. The spec header flips to `WONTDO` with the successor pointer in its tail, dated 2026-09-01. The id
   stays in the units region — a status flip, never a deletion. Its section 8 is already fully
   RESOLVED, which is what hygiene check 12 requires before a terminal status. The rev moves to rev-3
   with a section 9 line, because a successor pointer is a content change and not the pure status
   flip `memory/TEMPLATE-SPEC.md` exempts from a rev bump.
2. `bash tools/unattended/unattended.sh --rescope aClosedDocket --act supersede --unit
   TOOL-aClosedDocket-4 --successor TOOL-dFoldedVerdict-3 --reason ...` records the amendment on that
   build's own run record. **This half is not optional.** Check 24's RETIRE arm demands a `retire` or
   `supersede` rescope row for any id that is WONTDO now and was not so at the run's pinned baseline;
   that record's baseline region carries no unit rows at all, so the fallback baseline applies and
   the row is still owed. Without it this unit trades check 2's red for check 24's. The verb accepts
   it: the record is non-terminal, so `refuse_if_terminal` passes, and the unit is in the current
   units region, which is the membership test the supersede arm applies.

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
| `memory/builds/aClosedDocket/spec/2026-08-31-spec-TOOL-aClosedDocket-4.md` | S5 — header flip, successor pointer, section 9 line |
| `memory/builds/aClosedDocket/RUN.md` | S5 — the rescope row, written by the verb |
| `memory/LIVE.md`, `memory/ledger/2026-09.md`, `memory/builds/aClosedDocket/README.md` | S6 — regenerated |

### Migration

None. Nothing reads a disposition field before unit 2 lands, so the labels are inert until then and
the record is legal at every intermediate commit.

### Rollout

Order 3, after units 1 and 2. Landing the labels before check 2 reads them leaves two inert fields;
landing check 2's new predicate before the labels leaves main red for a different reason than it is
red for now. The regeneration in S6 rewrites generated regions across the whole memory tree, so this
pass does not run concurrently with any sibling pass that writes a build README or a generated index.

### Files touched (estimate)

Four tracked files edited, one of them by a verb rather than by hand, and three generated files
re-rendered. No file under `tools/` moves.

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
  in section 6. A supersession that reds check 24, addressed by S5's second act. A cutoff that admits
  `dBriefedPass`, addressed by S7's corpus-wide acceptance and section 8 Q1. Rollback is a revert of
  one commit; no state moves.
- **testing + left-shift gates** — the left-shift belongs to unit 2, whose predicate is what stops
  the next correctly-folded exit redding the bar. This unit's own class, a hand-edited parked row, is
  left ungated and named, which N5 states rather than implies.
- **migration / rollback** — see the Migration and Rollout sub-heads above. Reversible by revert.
- **user docs** — none. The mixed-exit rule is a governance rule, and section 8 Q2 routes it to the
  protocol rather than smuggling it into a record.

## 6. Acceptance criteria

- **AC1** — When the leg is re-run before any edit, `bash tools/unattended/check-unattended.sh` exits
  1 and its check 2 line names `memory/builds/dMispairedQuote/RUN.md` with the counts 2 and 1. The
  red is observed by this unit, not inherited from this spec.
- **AC2** — When the six blockers are re-derived at build time, every one has a disposition recorded
  in section 9 of `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md` or
  of `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md`. If any has none,
  the unit STOPS and reports the red as true; a disposition invented to clear a gate is the one
  outcome this unit may not produce.
- **AC3** — When the two rows and the provenance block are written, `grep -c 'disposition promote'`
  and `grep -c 'disposition fold'` over `memory/builds/dMispairedQuote/RUN.md` each return 1, and
  `grep -c '^disposition-source:'` over the same file returns 1.
- **AC4** — When the record is re-read afterwards, `bash tools/unattended/unattended.sh --status
  dMispairedQuote` still reports the same phase and witness it reported before the edit, proving no
  fact key's first-match position moved.
- **AC5** — When a throwaway clone under `mktemp -d` is seeded with a non-terminal run record and
  driven to a NON-CONVERGENT exit by two `bash tools/unattended/unattended.sh --review` calls
  carrying unit 1's new flag, `diff` shows the emitted row's reason tail is byte-identical to the
  tail this unit wrote by hand. This is the byte-shape agreement with unit 1, observed rather than
  asserted, and it exercises the shipped driver and not the kit self-test suite.
- **AC6** — When the two dispositions are removed from the record and the removal is STAGED,
  `bash tools/unattended/check-unattended.sh` exits 1 again naming that file. Without this arm the
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
- **AC9** — When the rescope row is written, `grep -F 'rescope · item supersede'` over
  `memory/builds/aClosedDocket/RUN.md` returns one line naming this unit as the successor, and
  `bash tools/unattended/check-unattended.sh` reports no check 24 failure for that record. Removing
  the row and re-running must red check 24, which is what proves the row is load-bearing rather than
  decorative.
- **AC10** — When the generated artifacts are re-rendered in the same commit,
  `python3 tools/memory-tree/gen_build_index.py --check` and
  `python3 tools/memory-tree/gen_build_index.py --check-format` both exit 0.
- **AC11** — When the record's size is measured after the edit, `wc -c
  memory/builds/dMispairedQuote/RUN.md` stays under `INDEX_CAP_BYTES` of 61440 from
  `.memory-tree.conf`, which is the only one of its two bounds a gate enforces, and under the 8 KB
  authored-region budget `memory/guides/UNATTENDED-PROTOCOL.md` declares in prose and nothing checks.
  Measured before the edit: 5521 bytes, with the two rows at 116 bytes each. The per-entry budget is
  NOT a bound here and this criterion does not claim it is: hygiene check 7's exemption list excludes
  `builds/*/RUN.md` by name, which is why a 1465-byte parked row already sits in this record and
  passes.

## 7. Gates

Named legs, each resolved in `tools/gate-legs.json` rather than remembered:

- `unattended kit gate` — the leg that is red today and the one this unit exists to green. Unguarded,
  so it runs on every bar.
- `memory hygiene` — grades this spec's own format, the flipped status header, the record's caps and
  entry budget, and the id citations in both edited records.
- `build README slot contract` — the format check over the build READMEs S6 re-renders.
- `pass-order history` — reads the same run-state records for their pinned BASE; named because this
  unit edits two of them and the leg must be seen to stay green rather than assumed to.
- `drift-audit records` — the repo's own record-versus-reality check, which is the class this unit's
  hand edit is closest to.

No new gate. The predicate that makes the next folded exit legible belongs to
`TOOL-dFoldedVerdict-2`, and this unit deliberately adds none of its own: N5 states that the
hand-edited-row class stays ungated in both directions.

**A standing owner instruction forbids running the unattended kit self-tests**, so
`tools/unattended/*.test.sh` and `bash tools/unattended/run-unattended-gates.sh --selftests` are NOT
run by this unit and no criterion in section 6 depends on them. What that costs, said plainly: the
byte shape of a retrofitted row is normally something that suite would compare, and here it is
witnessed instead by AC5's throwaway-clone run of the driver itself and by AC6's staged break
observed RED against the real leg. Both exercise the shipped code rather than a copy of it, and
neither substitutes for the arms unit 1 and unit 2 owe their own mechanisms.

## 8. Open questions

- **Q1 — does unit 2's cutoff admit `dBriefedPass`, and does this unit's scope grow by two rows if it
  does?** Measured, and this is the load-bearing fork. Thirteen tracked run-state records carry an
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
- **Q2 — should the protocol sanction the provenance form this unit uses?**
  `memory/guides/UNATTENDED-PROTOCOL.md:167` says the authored half carries the declared facts "and
  nothing else", no verb writes such a key, and nothing reads one — so two tracked records already
  sit outside a clause nothing enforces and this unit makes three. **Recommendation: yes, one
  sentence admitting a source-suffixed line whose value states why a verb could not write the key it
  names.** It belongs to whichever of this build's two protocol units, at orders 5 and 6, is already
  editing that document, and not to this unit, which would otherwise be writing its own permission.
- **Q3 — is this run entitled to write a rescope row into another live run's record?** The verb
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

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "repairing a finished unattended run-state record by hand
when no verb can write the field"` returned no seam this unit can extend. Its ranked candidates are
generic writers — `write` and `write_text` in the memory-tree kit, `run` in `tools/settings-merge.py`
— plus the protocol guide's inventory key and the `.unattended.conf` affordance seam, and none of
them reads or writes a run-state record. **No existing seam fits in code, and that is an answer
rather than a probe failure: this unit ships no code.** The seam it extends is a RECORD SHAPE, cited
by path — `memory/builds/dCarriedReceipt/RUN.md:14-21` and
`memory/builds/aGroundedOrientation/RUN.md:11`, the two tracked instances of the provenance form this
design copies one key over. Where a hit was stale: the prompt for this unit described four such
repairs, and only two carry the key in the tracked corpus, so section 4 marks the figure UNVERIFIED
and nothing here rests on it.

Recall terms used: `python tools/memory-recall/query.py "how was a terminal unattended run-state
record repaired by hand when no verb could write the field, and what recorded the provenance"
--terms "unattended run-state terminal phase landed-anchor reconstructed provenance hand-edit
refuse_if_terminal park review disposition fold promote non-convergent"`. It returned the two
precedent records, the `TOOL-aBoundedCeiling-11` class row, the `TOOL-dMispairedQuote-7` row that
records this build's supersession of `TOOL-aClosedDocket-4`, and the `TOOL-dBriefedPass-9` row that
Q1 rests on.

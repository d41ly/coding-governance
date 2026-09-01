# TOOL-dFoldedVerdict-2 — clause 3 reads the recorded disposition, behind a dated cutoff

**Status:** SPECCED · rev-4 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dFoldedVerdict-1-2-3-4-5-6-spec-audit-round1.md) | spec-audit | TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-3 TOOL-dFoldedVerdict-4 TOOL-dFoldedVerdict-5 TOOL-dFoldedVerdict-6 |

<!-- /gen:spec-records -->

## 1. Goal

Make the merge bar grade a non-convergent review exit on the disposition the record STATES, instead
of inferring one from a unit-id delta. `TOOL-dFoldedVerdict-1` gives `--review` a
`--disposition fold|promote` flag; this unit makes `tools/unattended/check-unattended.sh` check 2
clause 3 read that field and stop guessing. The proxy is wrong in both directions on measured data:
it passed `memory/builds/dBriefedPass/RUN.md` vacuously and it reds
`memory/builds/dMispairedQuote/RUN.md`, whose folded exit promoted nothing and never could.

## 2. Scope (IN)

- **S1** — the clause-3 predicate is REPLACED, not extended. For a graded record, `nneed` becomes the
  number of exited subjects whose OWN terminal row records `disposition promote`. A subject recording
  `disposition fold` demands nothing. The id delta is then demanded only of the promoting subjects.
- **S2** — an exited subject in a graded record that records NO disposition is a REFUSAL, naming the
  file and the subjects. It is not a pass. Without this arm `nneed` falls to zero on every unlabelled
  record and the clause becomes green-by-absence, which is the shape the rewrite exists to remove.
- **S3** — a disposition VALUE outside `fold|promote` is its own refusal, distinct from an absent
  one. `TOOL-dFoldedVerdict-1` validates the flag at write time, so an illegal value can only reach a
  record by hand-editing, and reading it as "absent" would report the wrong cause. The hand-edited
  record is not hypothetical — `TOOL-dFoldedVerdict-3` creates exactly that class — so this branch
  owes a fixture and a criterion of its own, and it now has both: the illegal-value fixture in S10
  and AC12. At rev-1 it had neither, which made the one branch S3 exists for the only outcome in §4's
  table that nothing observed.
- **S4** — a new declaration `DISPOSITION_CUTOFF` in `.unattended.conf`, graded on the run-state
  record's OWN FIRST-COMMIT DATE, the idiom `LANDED_ANCHOR_CUTOFF` uses at
  `tools/unattended/check-unattended.sh:943-949`. A record whose first commit is at or after the
  cutoff is graded by S1 to S3. A record before it keeps today's predicate verbatim.
- **S5** — BLANK or absent grandfathers EVERY record onto today's predicate and the leg ANNOUNCES
  that it did, on stdout, once per run, unconditionally. The precedent for an unconditional
  announcement rather than `report()` is `tools/unattended/check-unattended.sh:1189-1195`; `report()`
  is gated on `GOV_UNATTENDED_REPORT` at `:515` and would make the disabled term invisible on a
  default bar run.
- **S6** — a declared value that is not an ISO date is a `fail 2` REFUSAL, not a defaulted value. The
  shape is `tools/unattended/check-pass-order.sh:142-144`. This is the unit's one new `fail` branch,
  and it sits beside the `RUNAWAY_CEILING` refusal at `tools/unattended/check-unattended.sh:251`,
  above the record loop that consumes the value.
- **S6a** — that placement RENUMBERS three pinned branches, and the renumber is part of this unit.
  `memory/project/unarmed-branches.txt:52-54` pins `check-unattended.sh` check 2 ordinals 9, 10 and
  11 as unarmed, and `check-arms.py` assigns an ordinal by line order within a check number
  (`tools/memory-tree/check-arms.py:150-163`). Verified against `--report`: check 2 holds sixteen
  branches today, the pinned three sit at lines 392, 398 and 401, and a new branch at `:251` moves
  them to 10, 11 and 12. Left alone that reds `harness arms` four times — one row pinning a branch
  that is now armed, two stale signatures, and one unarmed branch that is no longer pinned. The three
  rows are renumbered in the same commit, signatures unchanged, count unchanged. The hazard was
  handed here by `TOOL-dFoldedVerdict-1` N1a; this scope item is the answer to it, and stating it as
  an OBLIGATION here is the point — a builder who discovers it from four red rows reads them as four
  rewordings and starts editing signatures.
- **S6b** — the renumber is SCOPED TO CHECK 2, and the scope is stated because the obvious over-fix
  is wrong. `check-arms.py` numbers branches per CHECK NUMBER, not per file
  (`tools/memory-tree/check-arms.py:157` increments `seen[num]`), so a new `fail 2` moves only
  `check 2` ordinals. The five `check 16` rows this same file pins, at
  `memory/project/unarmed-branches.txt:55-59` and ordinals 13 to 17, do NOT move and touching them is
  itself the defect. Verified against `--report` on this tree: the check-16 population is unchanged
  by any insertion into check 2. Any other leg's rows are outside the file this unit edits.
- **S7** — clause 3's three messages are rewritten for the graded path: the absent-disposition
  refusal, the illegal-value refusal, and the promote-count shortfall. The unreadable-BASE message
  keeps its shape and gains the word `promote`, because under S1 it can only be reached by a subject
  that recorded one. The PRE-CUTOFF path keeps both of today's messages byte-for-byte.
- **S7a** — the OUTER aggregate at `tools/unattended/check-unattended.sh:317` IS reworded, and this
  item exists because `TOOL-dFoldedVerdict-1` N1 handed that line here and rev-1 answered neither
  way. Today it reads `review loops that ran past the ceiling, stalled without recording it, or
  exited without promoting:`. After S2 and S3 a record can be named for recording NO disposition or
  an ILLEGAL one, and neither is any of those three things, so the header a bar reader sees FIRST
  would state the wrong cause under a clause S3 exists to make precise. Only the third clause
  changes, to `exited without accounting for their blockers`; the first two keep their bytes so the
  edit is one substitution. TWO readers move in the SAME COMMIT or the leg strands: the positive
  assertion at `tools/unattended/check-unattended.test.sh:471`, which is a `hit` on the whole
  literal, and through it the branch signature `check-arms.py` re-derives — verified at
  `tools/memory-tree/check-arms.py:232` against `armed_signatures` at `:167`, a branch is ARMED only
  while its literal run appears in a non-comment line of the paired test file. A reworded message
  with an unmoved arm sends that branch unarmed-and-unpinned and reds `harness arms`. AC11 is written
  against the new literal for the same reason.
- **S8** — the id-delta computation at `tools/unattended/check-unattended.sh:272-279` is NOT touched.
  Its `| WONTDO |` filter stays one-sided, and §4 records why that direction is the deliberate one.
- **S9** — the live defect in the arm covering this clause is repaired.
  `tools/unattended/check-unattended.test.sh:714` asserts by fixed substring
  `gained only 1 unit id(s) this run BASE lacked`; the shipped message at
  `tools/unattended/check-unattended.sh:313` says `gained only %d non-WONTDO unit id(s)`. The arm is
  RED and has been since `ccb5492c`. It is repaired to the pre-cutoff message this unit ships, which
  S7 keeps byte-identical to today's.
- **S10** — fixture arms for the graded path, in both directions, each with a green control: a
  fold-only exit passes and the same fixture unlabelled reds; a promote exit short of ids reds and
  the same fixture with the id present passes; a graded exit whose terminal row reads
  `disposition promoted` — a plausible near-miss, not a nonsense token — reds with S3's illegal-value
  message and NOT with S2's absent-disposition one; a blank cutoff restores today's verdict; a
  malformed cutoff refuses. §6 states how each is witnessed given that the suite may not be run.
- **S11** — S6's new branch is ARMED, and NO FLOOR MOVES. The deliverable is the positive assertion
  in `tools/unattended/check-unattended.test.sh` naming the malformed-cutoff refusal's own literal;
  `.memory-tree.conf` is not edited by this unit and is not in §4's Files-touched table.
  `python tools/memory-tree/check-arms.py --check` grades TEXT rather than execution
  (`tools/memory-tree/check-arms.py:231-233`), so this arm is gradeable without running the suite,
  and so are S10's. What BINDS is not a floor: `--check` reds on any unarmed branch that is not
  pinned in `memory/project/unarmed-branches.txt`, at `tools/memory-tree/check-arms.py:251-254`, so
  an unarmed new branch fails the bar by its own name and a floor adds nothing to that. Rev-1 raised
  `ARMS_FLOORS` for this leg from `101:100` to `102:101` and called the raise proof; the floors are
  one-sided minimums (`got[i] < want[i]` at `tools/memory-tree/check-arms.py:288`) and the measured
  values are 169 branches and 161 armed, so a minimum raised to 102 against 169 cannot fail. See §4's
  "The floor that proves nothing" for the measurement and the two siblings that had it right.
- **S12** — the three-way key join stays whole. `DISPOSITION_CUTOFF` is added to
  `tools/unattended/.unattended.conf.example` (blank, as its four siblings ship) and to the protocol's
  section 8 key table in BOTH `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`. Check 22 at
  `tools/unattended/check-unattended.sh:1281-1316` joins those three populations and reds on any
  disagreement.
- **S12a** — that row MOVES A NUMBER A SIBLING PINS, and this unit owns saying so.
  `TOOL-dFoldedVerdict-6` calibrates its section-8 conf-key tripwire on the key COUNT — its §4 anchor
  table at `:151` and its AC5 at `:226-229` both spell the expected value as 29. Reproduced with that
  leg's own extractor on this tree, `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'` over
  `memory/guides/UNATTENDED-PROTOCOL.md`, first table cell, backticked ALL-CAPS, `sort -u`: BASE
  `adc0543c` yields exactly 29 and this unit's row makes it 30. This unit is order 2 and unit 6 is
  order 6, so at unit 6's evaluation the extractor yields 30 under every path — F3 refuses option C,
  which is the only branch where the row would not have landed. Unit 6 pins 30, or derives the number
  from its own pre-image; this item exists so that is a decision its author makes rather than a
  criterion that is false by construction when it is graded.
- **S13** — the left-shift. `memory/gotchas/arm-literal-strands-on-message-edit.md` claims the class
  is gated by `check-arms.py --check`. This instance proves the population excludes it, and the class
  file gains that limit. The two backlog rows this unit answers, `TOOL-dBriefedPass-9` and
  `TOOL-dMispairedQuote-7`, are updated in `memory/backlog/TOOL.md`.
- **S14** — WITHDRAWN. `TOOL-dFoldedVerdict-1` S9 owns the protocol's `--review` bullet, and
  this unit does not touch it. Both folders took it independently, which is the collision M6
  clause 1 forbids and M2 calls a defect in exactly ONE document — the two specs were
  authored in parallel and could not read each other. It resolves toward unit 1 because the
  sentence "every blocker still standing is promoted" stops being true the moment `fold`
  becomes a legal RECORDABLE disposition, which is unit 1's flag; this unit's clause only
  changes who the BAR demands an id from. The byte argument points the same way: the render
  sits at EXACTLY `GUIDE_CAP_BYTES`, unit 1 measured its clause swap at -8 bytes, and this
  unit's version drafted at +36.

## 3. Non-goals (OUT)

- **N1** — the `--disposition` flag, its refusal, and the round-row field it writes. That is
  `TOOL-dFoldedVerdict-1`, order 2. This unit is the READER and depends on that writer's spelling.
- **N2** — retrofitting labels onto landed records. That is `TOOL-dFoldedVerdict-3`. This unit ships
  the cutoff that makes a retrofit possible and does not perform one.
- **N3** — PER-BLOCKER attribution. A disposition is one value per exiting round, so `promote` means
  "at least one standing blocker was promoted", and one id per promoting subject remains a lower
  bound over blockers. §4 states exactly which half of today's lower bound dissolves and which
  survives.
- **N4** — wiring `tools/unattended/check-unattended.test.sh` onto the merge bar. The owner ruling of
  2026-08-23, recorded in `tools/unattended/run-unattended-gates.sh:8-15` and in
  `tools/unattended/kit.toml`, keeps this kit's self-tests off the bar in gov and in every adopter.
- **N5** — the prompt-path BASE vacuity. `TOOL-aClosedDocket-4` N2 files it and
  `TOOL-aGradedMandate-13` measures it: on a run that authors its own build folder the units region
  is legitimately empty at BASE, so every planned unit reads as newly promoted. This unit NARROWS its
  reach to promote-labelled subjects only and does not close it.
- **N6** — a gate for the awk-composed-message class S13 records. `check-arms.py`'s population would
  have to grow, and `TOOL-aScannedThrottle-10` already carries four proposed-but-unbuilt legs of this
  family. The class file is the left-shift here.
- **N7** — the driver's own exit prose at `tools/unattended/unattended.sh:3968-3969`, which still
  names promotion as the only disposition. That IS `TOOL-dFoldedVerdict-1`'s carrier: its S5 is the
  scope item for those two success lines and its §4 Files-touched names the file. Nothing else about
  the exit prose is claimed here.
  The protocol's `--review` sentence is NOT in this non-goal any more and rev-1 was wrong to put it
  here. Rev-1 handed it to `TOOL-dFoldedVerdict-1`, which owns no protocol carrier: grepped on this
  tree, that spec never names `memory/guides/UNATTENDED-PROTOCOL.md` or
  `tools/unattended/PROTOCOL.template.md` at all, and its Files-touched table lists only
  `unattended.sh` and `unattended.test.sh`. A non-goal that hands a carrier to a unit holding none is
  not a hand-off, it is an orphan. THAT REASONING IS NOW SUPERSEDED BY THE REORDER, and the premise
  it rested on is gone: `TOOL-dFoldedVerdict-5` moved to order 1, so it carries section 7 into the
  new pair BEFORE either this unit or unit 1 touches the bullet. Unit 5 therefore still moves
  verbatim and still needs no exception carved out of its N2 — it simply moves a sentence that is
  false at that moment, and unit 1 corrects it in the new carrier one order later. The bullet is
  unit 1's S9 and is not touched here; see the withdrawn S14 for why it resolves that way.
- **N8** — adding `DISPOSITION_CUTOFF` to `tools/unattended/kit.toml`'s `[config] optional_keys`.
  Measured: none of `UNITS_REGION_CUTOFF`, `SPEC_THIN_CUTOFF`, `LANDED_ANCHOR_CUTOFF` or
  `PASS_ORDER_CUTOFF` is in that list today, so adding one member would be a new inconsistency rather
  than the removal of an old one.

## 4. Design

### The predicate today, stated exactly

Clause 3 lives in the awk sub-program at `tools/unattended/check-unattended.sh:280-315`, run once per
tracked run-state file. Its inputs are the review rows and two shell-computed values.

- `needs[it]` is set at `:293` by `if (rs ~ /NON-CONVERGENT|CEILING/) needs[it] = 1`, keyed on the
  subject `it` parsed out of the row's ` · item ` field.
- `nneed` is computed at `:296-303`: zero, then incremented once for each distinct subject present in
  `needs`. It is the count of DISTINCT SUBJECTS in this record whose reason field ever carried an
  exit token.
- `newids` is the shell's `rv_new` at `:279`: the number of unit ids present in the build README's
  `gen:build-units` region at HEAD and absent from that region at the run's pinned BASE.
- `readable` is `rv_readable` at `:275`, set only when the pinned BASE resolves as a commit.
- At `:309-314`, when `nneed > 0`, the record reds either because the BASE roster cannot be read or
  because `newids + 0 < nneed`.

So today the record reds unless the units region gained at least one non-WONTDO id per exited
subject. Nothing in the record is consulted about what the exit DID.

### The predicate after

For a record the cutoff GRADES, the loop at `:297-303` splits `needs` four ways instead of counting
it whole.

| the exited subject's terminal row | effect |
|---|---|
| carries `disposition fold` | demands nothing, and this is an EXACT claim rather than an approximation |
| carries `disposition promote` | counts one toward `nneed` |
| carries `disposition <other>` | a refusal naming the file, the subject and the illegal value |
| carries no `disposition` at all | a refusal naming the file and the subjects |

`nneed` is then compared against `newids` exactly as it is today. For a record the cutoff does NOT
grade, `nneed` is computed as it is today and both of today's messages are emitted unchanged.

### CEILING, and what this clause permits that M4 does not describe

Clause 3 sets `needs[it]` for `NON-CONVERGENT` and `CEILING` alike, at
`tools/unattended/check-unattended.sh:293`, and this unit does not narrow that. A CEILING exit is
therefore graded exactly as a non-convergent one is: a terminal row reading `disposition fold`
demands no unit id and the record passes.

That follows the owner ruling of 2026-09-01 recorded in this build's README — at CEILING the driver
accepts EITHER disposition — and its reason is the one this whole unit rests on. A forced value is a
constant, and a constant is not evidence for the clause that reads it. Were `promote` the only legal
value at CEILING, the field would carry no information there and this clause would be reading its own
default back under the name of a record.

**What that permits, stated plainly rather than left to be discovered.**
`memory/guides/BUILD-METHOD.md` M4 says of a runaway ceiling that reaching it is itself a defect, so
the run promotes and lands anyway. Under this clause a CEILING record whose exits all read
`disposition fold` is GREEN. That is a record M4's sentence does not describe, and this unit permits
it deliberately. The ruling is what authorizes it; M4 is prose in a guide the memory-tree kit renders
and is not a machine reader of this field, so nothing here silently overrules it. Reconciling the two
is neither in this unit's scope nor in any sibling's, and this spec mints no id for it — a reader who
hits M4's sentence is pointed at the build README's ruling, which is where the disagreement is
recorded.

### The floor that proves nothing

Rev-1's S11 raised `ARMS_FLOORS` for `tools/unattended/check-unattended.sh` from `101:100` to
`102:101` and AC7 made that raise the proof that S6's new branch was counted and armed. Both are
withdrawn, and the reason is measured rather than argued.

| figure | value on this tree | source |
|---|---|---|
| fail branches in `check-unattended.sh` | 169 | `python tools/memory-tree/check-arms.py --report` |
| armed branches in the same file | 161 | the same row of the same report |
| declared floors | 101 and 100 | `ARMS_FLOORS` in `.memory-tree.conf` |

The comparison is `got[i] < want[i]` at `tools/memory-tree/check-arms.py:288` — a one-sided minimum.
A minimum raised to 102 against a measured 169 cannot fail, so it grades neither the new branch nor
its arm, and a criterion that cannot fail on the absence of the change it grades is the exact shape
this build exists to remove. What DOES grade the branch is `--check`'s unarmed-and-not-pinned refusal
at `:251-254`, which names the branch and its own failure text; S11 and AC7 are rewritten onto it.

This correction already existed inside this build and did not reach rev-1. `TOOL-dFoldedVerdict-1`
AC9 records at source that the ratified `TOOL-aClosedDocket-4` AC9 asserted the opposite in both
directions and is false, and `TOOL-dFoldedVerdict-5` N6 independently measured this same file at
169/161 and concluded that no floor moves. Three siblings, two answers; the wrong one was the one
carried forward from the ratified spec.

### What this dissolves, and what survives

The comment at `:304-308` explains why the count is taken ACROSS subjects rather than per subject:
"a per-subject attribution is not available — the region records ids, not which subject promoted
them". That reasoning had to hold because the check assumed every exited subject promoted. It no
longer assumes it: a folding subject leaves the demanding population by its own record, so the
population `nneed` counts is DECLARED rather than inferred, and the false-negative half of the lower
bound is gone. The check no longer demands an id that no honest run could produce.

What survives is stated plainly rather than implied away. A `promote` label means at least one
blocker was promoted, not how many, so one id per promoting subject is still a floor over blockers,
and the region still cannot say which subject promoted which id. That residual is N3.

### The arithmetic, checked against both measured records

| record | exited subjects | dispositions, at source | `nneed` after | `newids` | verdict |
|---|---|---|---|---|---|
| `memory/builds/dBriefedPass/RUN.md` | `dBriefedPass-spec-set`, `dBriefedPass` | both FOLD | 0 | 5 | green, and no id demanded |
| `memory/builds/dMispairedQuote/RUN.md` | `TOOL-dMispairedQuote-1`, `TOOL-dMispairedQuote-3` | one PROMOTE, one FOLD | 1 | 1 | green |

`dMispairedQuote`'s split is recorded in its own build README at
`memory/builds/dMispairedQuote/README.md:52-55`, which states that unit 1's exit promoted three
blockers to unit 3 and folded one, and that unit 3's exit folded both. `dBriefedPass`'s is recorded
in backlog row `TOOL-dBriefedPass-9`, which states that both loops exited NON-CONVERGENT with every
blocker folded and nothing promoted; that is the run's own claim and not an independent reading of
its review records. Both `newids` figures were measured against this tree on 2026-09-01 by replaying
`:272-279` over every tracked record.

Under today's predicate the same two records give `nneed 2 · newids 5` and `nneed 2 · newids 1`. The
first is the vacuous pass; the second is the red on `origin/main` today, reproduced by running
`bash tools/unattended/check-unattended.sh` in this worktree.

### Data model

The disposition is read from the reason field of the subject's TERMINAL row — the one whose reason
matches `NON-CONVERGENT|CEILING`. Parsed with `match(rs, /disposition [a-z]+/)` inside the branch
that already sets `needs[it]` at `:293`, so a `disposition` token on a CONVERGING row is not read and
the subject string is never scanned. The reason field is entirely driver-composed by
`park()` at `tools/unattended/unattended.sh:3796-3806` and `verb_review` at `:3964`, and its only
free-text component is the verdict, which is validated against a closed set, so no caller-supplied
text can reach this parse.

`TOOL-dFoldedVerdict-1` writes the field as ` · disposition <value>` appended to the reason. That
spelling is the INTERFACE between the two units and is written identically in both specs.

### The cutoff

`DISPOSITION_CUTOFF` is a project declaration and not a kit constant, because the date depends on the
ADOPTER's corpus rather than on the kit: it is the day that adopter's records started being able to
carry the field. `RUNAWAY_CEILING`, which this same clause reads out of the driver, is the opposite
case — a kit-wide policy number with no per-corpus meaning.

The grading date is the record's own first commit,
`GIT log --diff-filter=A --format=%cs -- "$rvf" | tail -1`, which is what `LANDED_ANCHOR_CUTOFF` uses
at `:943`. One deliberate divergence from that site: where it treats an EMPTY first-commit date as
grandfathered, this clause treats it as GRADED. A record with no adding commit is staged and not yet
committed, which makes it newer than any past cutoff, and grandfathering it would hand the in-flight
run — the one case that can still record a disposition — the proxy this unit exists to retire.

Value of the declaration for this repo: `2026-09-01`. Measured over the thirteen tracked run-state
records carrying at least one exited subject, that date grades exactly `dBriefedPass` and
`dMispairedQuote` and grandfathers the other eleven, whose first commits fall between 2026-08-19 and
2026-08-31.

### Migration

Thirteen tracked records carry at least one exited subject and NONE can carry the field: `park()` at
`tools/unattended/unattended.sh:3796` only appends, and no verb in the driver rewrites a row. Without
a cutoff the rewrite reds all thirteen at once, on landed records no run may rewrite. With the cutoff
at `2026-09-01`, eleven are grandfathered permanently and two are handed to
`TOOL-dFoldedVerdict-3`.

The leg is RED on `origin/main` today for exactly one record, and this unit does not clear it — it
changes the sentence the red carries, from a shortfall claim to an absent-disposition refusal.
`TOOL-dFoldedVerdict-3` clears it. The build lands once, after that unit, so the intervening red
never reaches the default branch. §8 F2 carries the alternative and why it is not recommended.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | S1 to S8 — the cutoff read, its validation, the split loop, the messages, and S7a's aggregate rewording |
| `tools/unattended/check-unattended.test.sh` | S9, S10, S11 — the stale arm repaired, `:471`'s aggregate literal moved with S7a, the graded and malformed-cutoff arms added |
| `tools/unattended/.unattended.conf.example` | S12 — the key, blank, with its own header comment |
| `tools/unattended/PROTOCOL.template.md` | S12 — one row in the section 8 key table. NOT the `--review` bullet, which is unit 1's S9 |
| `memory/guides/UNATTENDED-PROTOCOL.md` | S12, S14 — the same two edits, byte-identical, for check 10 |
| `.unattended.conf` | S4 — the declaration, at `2026-09-01`, with its reason beside it |
| `memory/project/unarmed-branches.txt` | S6a, S6b — three check-2 pin rows renumbered from 9, 10, 11 to 10, 11, 12, and the five check-16 rows left alone |
| `memory/gotchas/arm-literal-strands-on-message-edit.md` | S13 — the population limit this instance proves |
| `memory/backlog/TOOL.md` | S13 — the two rows this unit answers |

### Alternatives rejected

**An OR-arm beside the proxy**, which is `TOOL-aClosedDocket-4` S3 as ratified: clause 3 is satisfied
when EITHER a new id appeared OR the row says fold. Rejected by owner ruling on 2026-09-01, recorded
in this build's README. It leaves the vacuous pass intact for every unlabelled exit, because the id
arm still discharges a subject nobody labelled, so `dBriefedPass` would keep passing for the wrong
reason. Reading the field INSTEAD of the proxy is what makes the absent-disposition refusal reachable.

**A kit constant instead of a conf key.** Rejected: the date is a property of the adopter's corpus,
and a kit constant would either grade every adopter's landed records or none of them.

**Numbering the cutoff refusal `fail 1` instead of `fail 2`.** It would be defensible — check 1 is
the conf, and no check-1 branch of this leg is pinned, so the renumber of S6a would not be needed.
Rejected: `HALT_FLOOR`'s two value refusals at `tools/unattended/check-unattended.sh:324` and `:326`
are both `fail 2`, so this kit already puts a value's validation under the check that CONSUMES it,
and splitting one clause's guard away from the clause is how a reader stops finding it. The pin
renumber is three lines and `check-arms.py --check` grades it immediately.

**Making the BASE side of the id delta filter `| WONTDO |` too.** Rejected, and the direction is
recorded because the asymmetry is easy to read as an oversight. At `:272` the HEAD set drops WONTDO
rows and at `:274` the BASE set does not, so the BASE set is the full id set at BASE, and
`comm -23` therefore yields a strictly SMALLER "new" set than a symmetric read would. Filtering both
sides would let a unit that was retired at BASE and revived at HEAD count as a promotion. The current
direction is the conservative one, this unit's population of promoting subjects is smaller than
today's, and loosening the delta in the same change would move two variables at once.

## 5. Production-readiness checklist

- **security** — N/A. The clause reads tracked records and the git object store, adds no write path,
  and the parsed field is driver-composed with no caller-supplied text reaching it.
- **perf / scale** — one extra `git log --diff-filter=A` per run-state record carrying review rows,
  thirteen today. The leg's declared ceiling in `tools/gate-legs.json` is 16040 ms and the leg
  measured well inside it on this node; the addition is bounded by the record count.
- **a11y** — N/A. A shell gate leg with no user interface.
- **i18n** — N/A. Machine-read English tokens in a records format.
- **error / empty / loading states** — three states are named rather than defaulted: a blank cutoff
  announces itself, a malformed one refuses, and an absent disposition on a graded record refuses.
  An unreadable BASE keeps today's cannot-look refusal.
- **observability** — the announcement of S5 prints unconditionally on stdout, and every refusal
  names the file and the subjects it is about. Per-leg output is persisted under
  `<git-dir>/gate-logs/` by the runner.
- **risks (concurrency, data-loss, rollback hazards)** — five, each with its owning item.
  The RENUMBERING risk is S6a and S6b: a new `fail 2` branch shifts three pinned ordinals and reds
  `harness arms` four times with messages that read like rewordings rather than like an insertion,
  which is why the pin edit is a scope item and not a cleanup.
  The ARM-STRANDING risk is S7a: rewording the aggregate at `:317` sends its branch unarmed unless
  `tools/unattended/check-unattended.test.sh:471` moves in the same commit.
  The INTERFACE risk is the field spelling shared with `TOOL-dFoldedVerdict-1`; §8 F1 carries it.
  The BYTE-CAP risk is the protocol pair, now carrying two edits rather than one; §8 F3 carries it.
  The SELF-GRADING risk is that this build's OWN review rounds, if any exit NON-CONVERGENT before
  order 1 lands, are unlabelled in a record dated at the cutoff — a red the build clears with
  `TOOL-dFoldedVerdict-3` rather than a design defect here.
  `memory/backlog/TOOL.md` is a `SHARED_RECORDS` member, so the pass that writes S13 may not be
  dispatched concurrently with any sibling pass that also writes it.
- **testing + left-shift gates** — S10's and S11's arms plus S13's class amendment. The gap is named in §6 and
  in N4: the fixture arms cannot be run under the standing owner instruction, and each acceptance
  criterion that depends on one names its substitute observation.
- **migration / rollback** — the cutoff IS the migration. Rollback is reverting the commit; no record
  is rewritten by this unit, so nothing on disk needs undoing.
- **user docs** — two edits to the operator-facing contract, both in the byte-compared protocol pair:
  the section 8 key table row (S12) and the `--review` bullet (S14). No `help/` page: this repo ships
  no such tree and the protocol is the operator-facing carrier.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs over this tree with
  `DISPOSITION_CUTOFF="2026-09-01"` declared and no labels retrofitted, it names
  `memory/builds/dBriefedPass/RUN.md` and `memory/builds/dMispairedQuote/RUN.md` for recording no
  disposition, and names none of the eleven records whose first commit falls before the cutoff.
- **AC2** — When the same command runs with `DISPOSITION_CUTOFF=""` in the working tree, the verdict
  is byte-identical to today's: `memory/builds/dMispairedQuote/RUN.md` is the only record named, it
  is named by the pre-cutoff shortfall message, and the leg additionally prints the announcement line
  naming the disabled term.
- **AC3** — When `DISPOSITION_CUTOFF="not-a-date"` is set in the working tree,
  `bash tools/unattended/check-unattended.sh` emits the S6 refusal naming the malformed value and
  grades no record under either predicate, rather than silently choosing one.
- **AC4** — When a graded record's exited subjects all record `disposition fold`, no unit id is
  demanded. Witnessed by the fold arm added to `tools/unattended/check-unattended.test.sh`, which
  CANNOT BE RUN under the standing owner instruction forbidding this kit's self-tests; the
  substitute observation is `bash tools/unattended/check-unattended.sh` over
  `memory/builds/dBriefedPass/RUN.md` once `TOOL-dFoldedVerdict-3` labels its two exits, where the
  record must go unnamed at `nneed 0` against `newids 5`.
- **AC5** — When a graded record has one promoting subject and the region gained one id, the record
  passes, and with two promoting subjects and one id it reds naming the count. Witnessed by the two
  promote arms in `tools/unattended/check-unattended.test.sh`, which may not be run; the substitute
  observation is `bash tools/unattended/check-unattended.sh` over
  `memory/builds/dMispairedQuote/RUN.md` after its labels land, where the record must go unnamed at
  `nneed 1` against `newids 1`.
- **AC6** — When the fixed string `non-WONTDO unit id(s) this run BASE lacked` is grepped for with
  `grep -F` in `tools/unattended/check-unattended.test.sh`, it matches the repaired arm, and the same
  string matches `tools/unattended/check-unattended.sh`. Today the first search returns nothing while
  the second matches, which is the defect.
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs with `.memory-tree.conf`
  UNCHANGED by this unit, it exits 0. This is the binding observation and it HAS a failing case:
  the refusal at `tools/memory-tree/check-arms.py:251-254` names any unarmed branch that is not
  pinned in `memory/project/unarmed-branches.txt`, so deleting S11's arm reds this criterion by name.
  No floor is raised. The floors are recorded beside the measurement that makes a raise meaningless —
  minimums of 101 and 100 against 169 branches and 161 armed on this tree.
- **AC7a** — When `python tools/memory-tree/check-arms.py --report` runs, the three rows of
  `memory/project/unarmed-branches.txt` naming this leg's check 2 sit at ordinals 10, 11 and 12 with
  their signatures unchanged, the five rows naming its check 16 are UNCHANGED at ordinals 13 to 17,
  and no row is reported as stale, as newly armed, or as pinning a branch that no longer exists.
- **AC7b** — When `python tools/memory-tree/check-arms.py --report` runs, the
  `tools/unattended/check-unattended.sh` row shows its branch count and its armed count BOTH risen by
  exactly one from the 169 and 161 measured at BASE `adc0543c`, and S6's malformed-cutoff branch is
  listed ARMED on its own message signature. `TOOL-dFoldedVerdict-1` N1 keeps that unit out of this
  file, so the BASE pair is still the pre-image when this unit is graded at order 2.
- **AC8** — When `grep -n '^DISPOSITION_CUTOFF=' .unattended.conf` runs it returns the declared date,
  and when `bash tools/unattended/check-unattended.sh` runs, check 22 reports no key disagreement.
  The two observations are separate because check 22 is: it grades the example conf against the
  section 8 table in BOTH directions but the PROJECT conf in one only — `proj_extra` at
  `tools/unattended/check-unattended.sh:1311` is keys the project declares that the table does not
  document, and its own inline comment says an optional key the project never sets is not a fault.
  A green check 22 therefore CANNOT witness the project declaration, and inferring it from one would
  pass a commit that adds the key to the example and the table, forgets `.unattended.conf`, and lands
  S5's blank-cutoff grandfather over the whole corpus with a green bar.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, check 6 does not name
  `memory/guides/UNATTENDED-PROTOCOL.md`, and `wc -c memory/guides/UNATTENDED-PROTOCOL.md` reports at
  most 61440 bytes with `tools/unattended/PROTOCOL.template.md` byte-identical to it. Both halves sit
  at exactly 61440 today and this unit now adds TWO things to them — S12's key row and S14's amended
  `--review` bullet — so this criterion is what forces §8 F3 to be resolved before either is written.
  Only the guide half is capped by check 6, whose selector at
  `tools/memory-tree/check-memory-hygiene.sh:449` is `^memory/guides/[^/]+\.md$`; the template half
  inherits the figure through check 10's byte-compare rather than through a cap of its own.
- **AC10** — When `grep -cF "grep -vE '\| WONTDO \|'" tools/unattended/check-unattended.sh` runs it
  returns 1, the same count as today, and the line it matches is the HEAD-side id read. The BASE-side
  read carries no such filter, and S8 leaves both unchanged.
- **AC11** — When `memory/gotchas/arm-literal-strands-on-message-edit.md` is read, its "Arming it"
  section states that a message composed inside an awk sub-program and appended to a `fail` argument
  is OUTSIDE the population `check-arms.py` signs, and names this clause as the instance. Corroborated
  by `python tools/memory-tree/check-arms.py --report`, which lists the check-2 branch whose signature
  begins `review loops that ran past the ceiling` as ARMED on that literal alone — named by its
  SIGNATURE and not by an ordinal, because S6 inserts a branch above it and moves that ordinal from 2
  to 3, and because S7a rewords the literal's tail. The head clause is the stable half of both edits.
- **AC12** — When one exited subject's terminal row in `memory/builds/dMispairedQuote/RUN.md` is
  hand-edited in the working tree to read ` · disposition promoted` and
  `bash tools/unattended/check-unattended.sh` is run, the leg emits S3's illegal-value refusal naming
  the file, that subject and the value `promoted`, and that message does NOT reuse S2's
  absent-disposition wording — so a build that folds the illegal value into the absent message fails
  here. **Taken at THIS unit's own image, order 2:** both of that record's subjects are still
  unlabelled then, so the same run emits S2's refusal for the OTHER subject and the two messages are
  compared side by side in one output. Re-run after `TOOL-dFoldedVerdict-3` labels them, the
  companion subject carries its own disposition instead and the comparison is against S2's shipped
  message text rather than against a second line of the same run. The record is STAGED before the
  edit and the edit reverted after, because a `git checkout --` restores the whole file and would
  take unrelated work with it. This is the substitute observation for the illegal-value arm S10 adds
  to `tools/unattended/check-unattended.test.sh`, which may not be RUN under the standing owner
  instruction. `promoted` is chosen over a nonsense token deliberately: the near-miss of a real value
  is the edit a hand retrofit actually makes.
- **AC13** — When `grep -n 'promoted to a unit rather than parked' memory/guides/UNATTENDED-PROTOCOL.md
  tools/unattended/PROTOCOL.template.md` runs it returns NOTHING in either file, and a grep for
  `disposition` in the same two files returns the amended `--review` bullet naming `fold` and
  `promote` as the two exits and `--disposition` as what records which, byte-identically in both.
  Corroborated by `bash tools/unattended/check-unattended.sh` reporting no check 10 pair disagreement
  and no check 26 refusal for `--review`. The negative half is what gives this a failing case: a
  commit that adds the new sentence and leaves the old one passes a grep for the new text alone.

## 7. Gates

Every leg below resolves by name in `tools/gate-legs.json`.

- `unattended kit gate` — the leg this unit rewrites. Its checks 2, 10, 22 and 26 are all in scope;
  26 joins the list at rev-2 because S14 edits a verb entry that check 26 reads.
- `harness arms (fail branches armed or pinned)` — S6's new branch and its arm, S6a and S6b's pin
  rows, and S7a's moved aggregate literal. No floor moves; §4's "The floor that proves nothing" is
  the measurement.
- `memory hygiene` — check 12 over this spec, and check 6 over the protocol's byte cap.
- `kit version markers` — the `gov:kit unattended@` carriers stay IN STEP, which is the whole of what
  `tools/check-kit-versions.sh:144-173` asserts: it compares every marker against
  `KIT_UNATTENDED_VERSION` and never demands that any of them MOVE. This unit moves no marker and
  edits no version constant; S12 and S14 change the BODY of two carriers, not their line-1 markers.
  The bump is `TOOL-dFoldedVerdict-6`'s and happens ONCE, on the build's last landing unit, by the
  owner ruling of 2026-09-01 in this build's README — an adopter sees one release, not six.
  Rev-1 said the opposite twice over, and both halves were wrong: it assigned the bump to order 1,
  and it counted the carriers. NO COUNT IS WRITTEN HERE. The population is derived — read it with
  `git grep -l 'gov:kit unattended@'` or from `TOOL-dFoldedVerdict-1` §8 Q3, which enumerates it.
  `tools/unattended/check-pass-order.sh` is the carrier a count typed from memory keeps dropping: the
  ratified `TOOL-aClosedDocket-4` S6 dropped it, unit 1's Q3 diagnosed that, and rev-1 of this spec
  reproduced the same undercount one spec over without ever seeing the diagnosis.
- `drift-audit records` — the two backlog rows S13 rewrites are records this leg reads.

This unit adds NO new gate leg. S6 adds a `fail` branch inside an existing leg, which is why
`harness arms (fail branches armed or pinned)` is the gate that grades it — through the
unarmed-and-not-pinned refusal, not through a floor.

## 8. Open questions

- **F1 — where the retrofit puts the label, and therefore how permissive this reader is.** RESOLVED (agent,
  2026-09-01): option A, the strict reader. Taken on the recommendation's own ground — a reader
  looser than its writer is a second grammar nobody declared — and the owner ruling of the same date
  makes the retrofit an authorized migration rather than a run editing its own history. The reader
  specified in §4 takes the disposition from the subject's TERMINAL row. `park()` at
  `tools/unattended/unattended.sh:3796` only appends, and `verb_review` at `:3951-3954` refuses a
  second round for a subject that already carries a terminal token, so `TOOL-dFoldedVerdict-3` cannot
  produce that row by calling a verb — it must edit the bytes of an append-only record.
  Option A: keep the strict reader and let unit 3 edit the row in place. Option B: widen the reader
  to take the disposition from the LAST row naming that subject that carries one, so unit 3 can
  append a correction row instead of editing history.
  **Recommendation: A.** A permissive reader makes a `disposition` token legal on a CONVERGING row,
  which `TOOL-dFoldedVerdict-1` refuses at write time, and a reader looser than its writer is a
  second grammar nobody declared. The append-only property is about what a RUN may do to its own
  history; a retrofit is an owner-authorized migration, and it is `TOOL-dFoldedVerdict-3`'s to state.
- **F2 — whether the declared cutoff is `2026-09-01` or a future date.** RESOLVED (owner,
  2026-09-01): `2026-09-01`. The owner took the disposition that accepts it, and
  `TOOL-dFoldedVerdict-3` Q1 carries the same ruling together with the scope consequence — four
  labelled rows across two records, not two. At `2026-09-01` the leg reds
  on two records between this unit and `TOOL-dFoldedVerdict-3`. A future date would keep the bar green
  in between, and unit 3 would lower it in the same commit as the retrofit.
  **Recommendation: `2026-09-01`.** A cutoff set ahead of the corpus grades nothing, so this unit
  would land a rule with no population and no observation of it firing, which is the could-not-fail
  shape the charter names. The leg is ALREADY red on `origin/main` for
  `memory/builds/dMispairedQuote/RUN.md`, verified by running it in this worktree, so this unit
  inherits a red rather than introducing one; the build lands once, after unit 3. A cutoff edited
  twice inside one build is also a knob whose two values disagree in the history.
- **F3 — how this unit's TWO protocol edits are paid for.** RESOLVED (agent, 2026-09-01): option B,
  and it is ALREADY TAKEN. The rev-3 reorder moved `TOOL-dFoldedVerdict-5` to order 1 and this unit
  to order 3, so the split that frees roughly 8.1 KB lands two units before either of these edits is
  written, and the zero-headroom premise stated below does not hold at the moment they are made.
  Option A's compression is therefore NOT performed here, which also dissolves the collision with
  `TOOL-dFoldedVerdict-6` that made A the harder branch. The measurement obligation survives
  untouched: AC9 still refuses a landing that has not re-measured with `wc -c`, because headroom that
  exists in a plan is not headroom observed in a tree. `memory/guides/UNATTENDED-PROTOCOL.md`
  and `tools/unattended/PROTOCOL.template.md` are each exactly 61440 bytes, measured with `wc -c` on
  this tree, and hygiene check 6 at `tools/memory-tree/check-memory-hygiene.sh:503` reds on
  `b[f]+0>cb` with `GUIDE_CAP_BYTES=61440` declared at `:63`. There is zero byte headroom; the line
  count, 725 against 750, is not the binding axis.
  The demand grew at rev-2 and the fork is restated rather than re-recommended. S12's key row is
  roughly 200 bytes and check 22 refuses the key without it. S14's `--review` amendment is the second
  claim on the same zero headroom: it names both dispositions where one was named and enumerates
  three more refusals, so it does not come out byte-neutral however tightly it is written. Both are
  measured with `wc -c` before the commit and AC9 is what refuses a landing that has not paid.
  Option A: land both in this unit and pay by collapsing the grandfather sentence repeated across the
  four existing cutoff rows into one line above the table, which drops no claim.
  Option B: resequence so `TOOL-dFoldedVerdict-5` or `TOOL-dFoldedVerdict-6` frees the bytes first.
  Option C: defer the declaration until those units land, which strands this unit's own rule.
  **Recommendation: A, coordinated with `TOOL-dFoldedVerdict-6` so the same sentences are not
  compressed twice.** C is refused outright: it makes the cutoff undeclarable and leaves the rewrite
  inert, and it is also the ONLY branch on which S12a's key count would not reach 30 before unit 6
  grades it. This fork is the one an owner or the build's fork sweep must close before any byte of
  S12 or S14 is written, because option A touches text that unit 6 also owns.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Predicate, cutoff, messages and arms grounded against
  `tools/unattended/check-unattended.sh` at BASE `adc0543c`; the arm defect at
  `tools/unattended/check-unattended.test.sh:714` reproduced by fixed-string comparison against the
  shipped message and by running the leg over this tree.
- rev-2 · 2026-09-01 · round-1 spec-audit fold, plus two owner rulings taken after rev-1 was written.
  Every claim below was re-derived against this tree before it was written down.
  **H2** — S3 gained its fixture in S10 and its criterion in AC12; the illegal-value branch was the
  only row of §4's outcome table that nothing observed.
  **H8** — S11's `ARMS_FLOORS` raise from `101:100` to `102:101` is WITHDRAWN and `.memory-tree.conf`
  left §4's Files-touched table. `check-arms.py --report` measures this leg at 169 branches and 161
  armed and `tools/memory-tree/check-arms.py:288` compares one-sidedly, so the raise could not fail.
  S11 now carries the arm itself and AC7 asserts the unarmed-and-not-pinned refusal at `:251-254`,
  which can. AC7b was added for the count movement. §4 gained "The floor that proves nothing", which
  records that `TOOL-dFoldedVerdict-1` AC9 and `TOOL-dFoldedVerdict-5` N6 both had this right before
  rev-1 was written.
  **M6** — AC8 no longer INFERS the project declaration from a green check 22. Check 22 grades the
  project conf in one direction only, at `tools/unattended/check-unattended.sh:1311`, so the direct
  grep and the gate are now two observations and the limit is stated.
  **M7** — S7a answers `TOOL-dFoldedVerdict-1` N1's hand-off of the `:317` aggregate, which rev-1
  left in neither state. It IS reworded, only its third clause, and the arm at
  `tools/unattended/check-unattended.test.sh:471` moves in the same commit or the branch strands.
  **M8** — §7's carrier count is gone. Rev-1 said eight, `tools/unattended/check-pass-order.sh` was
  the one it dropped, and it dropped it one spec after `TOOL-dFoldedVerdict-1` Q3 diagnosed the same
  omission in the ratified `TOOL-aClosedDocket-4` S6. No number replaces it.
  **L1** — AC11 no longer pins `check 2 branch 2`, an ordinal S6 itself moves to 3. It names the
  branch by the stable head of its signature instead.
  **H4, at the cause end** — S14 takes the protocol's `--review` bullet INTO this unit and N7 records
  why. Rev-1's N7 handed it to `TOOL-dFoldedVerdict-1`, which owns no protocol carrier: grepped on
  this tree, that spec never names either half of the pair. Unattended, the falsified sentence would
  have reached `TOOL-dFoldedVerdict-5`, whose S1 moves section 7 VERBATIM into a new byte-compared
  pair and whose N2 forbids rewording it. AC13 observes both halves and its negative case.
  **H6, at the cause end** — S12a states that S12's row takes the section-8 conf-key count from 29 to
  30, so `TOOL-dFoldedVerdict-6` can pin the number it will actually measure rather than the BASE one
  its §4 table and AC5 carry today. Both were reproduced with that leg's own extractor.
  **The renumber hazard** — S6b makes the ordinal scope an obligation rather than a discovery:
  `check-arms.py` numbers per CHECK NUMBER, so only the three check-2 pins move and the five check-16
  pins at `memory/project/unarmed-branches.txt:55-59` must be left alone. AC7a asserts both halves.
  **Owner ruling (a), CEILING** — §4 gained "CEILING, and what this clause permits that M4 does not
  describe". The clause grades a CEILING exit exactly as a non-convergent one, so a CEILING record
  recording `fold` is green — which `memory/guides/BUILD-METHOD.md` M4's runaway-ceiling sentence
  does not describe. Stated plainly rather than resolved silently in a predicate.
  **Owner ruling (b), the kit version** — §7's `kit version markers` bullet reversed. Rev-1 said the
  bump belonged to order 1; it belongs to `TOOL-dFoldedVerdict-6`, once, on the build's last landing
  unit, and this unit moves no marker.
  **Nothing in the round-1 report addressed to this unit is refused.** M1 to M5, M9, H1, H3, H5, H7
  and B1 are addressed to siblings and are untouched here.
- rev-3 · 2026-09-01 · S14 WITHDRAWN: it and `TOOL-dFoldedVerdict-1` S9 had both claimed the protocol's `--review` bullet, the collision M6 clause 1 forbids, produced because the two specs were authored in parallel and could not read each other. It resolves toward unit 1 on the rule and on the bytes alike. N7's supporting argument is superseded by the reorder — this unit is now order 3 and the section-7 move is order 1 — and the Files-touched row no longer claims the bullet. The reorder itself exists because S12 ADDS a section-8 key row to a render already at EXACTLY `GUIDE_CAP_BYTES`.

- rev-4 · 2026-09-01 · the fork sweep. F1, F2 and F3 marked; the spec is no longer FORKED. F2 is
  the owner's cutoff ruling of the same date and matches `TOOL-dFoldedVerdict-3` Q1 in both
  directions. **F3 changed its answer.** Rev-2 recommended option A — pay for both protocol edits
  by compressing the grandfather sentences, coordinated with `TOOL-dFoldedVerdict-6` — and the
  rev-3 reorder has since taken option B instead by moving `TOOL-dFoldedVerdict-5` to order 1. The
  split lands two units before either edit here, so no compression is performed by this unit and the
  collision with unit 6 is gone. AC9's obligation to re-measure with `wc -c` before landing is
  deliberately NOT relaxed: headroom that exists in a plan is not headroom observed in a tree.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a review loop's recorded exit disposition on the merge bar"`
ranked the `.unattended.conf` affordance seam of the `unattended` dossier first among the seams, and
that IS the seam this unit extends: the declaration channel the leg already imports at
`tools/unattended/check-unattended.sh:144-163`, and the four dated cutoffs already carried there. The
second seam extended is the clause itself, `tools/unattended/check-unattended.sh:263-317`, which
already walks every run-state record, already parses the `review` row grammar and already reports per
subject. No new file, no new leg and no new parser is introduced. The probe returned no symbol-level
candidate for the disposition read, which is correct: the row grammar is parsed in awk inside the
clause and in `review_last_reason` and `review_counts` at
`tools/unattended/unattended.sh:3874-3901`, and none of those is a reusable function this leg can
call, because the leg reads the driver as data rather than sourcing it.

Recall terms used: `python tools/memory-recall/query.py "why does the unattended kit grade a review
loop's exit by counting new unit ids instead of reading a recorded disposition" --terms "disposition
fold promote clause NON-CONVERGENT promotion proxy cutoff grandfather run-state review round units
region unit-id delta"`. It returned 39 hits; the four that changed this design are
`TOOL-dBriefedPass-9` and `TOOL-dMispairedQuote-7` in `memory/backlog/TOOL.md`, the round-1 spec audit
at `memory/builds/aClosedDocket/reviews/2026-08-31-review-TOOL-aClosedDocket-4-spec-audit-round1.md`,
which is where the `arm-literal-strands-on-message-edit` left-shift for this exact arm was already
proposed, and `TOOL-aGradedMandate-13`, which measures the empty-BASE vacuity N5 files.

One retrieval hit was STALE and the disagreement is recorded here. `TOOL-aClosedDocket-4` N4 states
that "clause 3's promotion arm still passes" every landed record; verified against source on
2026-09-01 by replaying `:272-279` over all thirteen tracked records, it does not —
`memory/builds/dMispairedQuote/RUN.md` reds at `nneed 2` against `newids 1`. Backlog row
`TOOL-dMispairedQuote-7` already records that the premise died, and this unit's cutoff is the
consequence.

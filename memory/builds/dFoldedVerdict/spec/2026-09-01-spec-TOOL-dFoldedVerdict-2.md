# TOOL-dFoldedVerdict-2 — clause 3 reads the recorded disposition, behind a dated cutoff

**Status:** SPECCED · rev-1 · 2026-09-01 · node d · Tier-2 · base adc0543c · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

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
  record by hand-editing, and reading it as "absent" would report the wrong cause.
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
  handed here by `TOOL-dFoldedVerdict-1` N1a; this scope item is the answer to it.
- **S7** — clause 3's three messages are rewritten for the graded path: the absent-disposition
  refusal, the illegal-value refusal, and the promote-count shortfall. The unreadable-BASE message
  keeps its shape and gains the word `promote`, because under S1 it can only be reached by a subject
  that recorded one. The PRE-CUTOFF path keeps both of today's messages byte-for-byte.
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
  the same fixture with the id present passes; a blank cutoff restores today's verdict; a malformed
  cutoff refuses. §6 states how each is witnessed given that the suite may not be run.
- **S11** — `ARMS_FLOORS` in `.memory-tree.conf` moves from `tools/unattended/check-unattended.sh:101:100`
  to `:102:101` for S6's branch, and the arm for it is written in the sibling test.
  `python tools/memory-tree/check-arms.py --check` grades TEXT rather than execution
  (`tools/memory-tree/check-arms.py:231-233`), so this arm is gradeable without running the suite,
  and so are S10's.
- **S12** — the three-way key join stays whole. `DISPOSITION_CUTOFF` is added to
  `tools/unattended/.unattended.conf.example` (blank, as its four siblings ship) and to the protocol's
  section 8 key table in BOTH `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`. Check 22 at
  `tools/unattended/check-unattended.sh:1281-1317` joins those three populations and reds on any
  disagreement.
- **S13** — the left-shift. `memory/gotchas/arm-literal-strands-on-message-edit.md` claims the class
  is gated by `check-arms.py --check`. This instance proves the population excludes it, and the class
  file gains that limit. The two backlog rows this unit answers, `TOOL-dBriefedPass-9` and
  `TOOL-dMispairedQuote-7`, are updated in `memory/backlog/TOOL.md`.

## 3. Non-goals (OUT)

- **N1** — the `--disposition` flag, its refusal, and the round-row field it writes. That is
  `TOOL-dFoldedVerdict-1`, order 1. This unit is the READER and depends on that writer's spelling.
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
- **N7** — the driver's own exit prose at `tools/unattended/unattended.sh:3968-3969` and the
  protocol's `--review` sentence at `memory/guides/UNATTENDED-PROTOCOL.md:503`, both of which still
  name promotion as the only disposition. Those are `TOOL-dFoldedVerdict-1`'s carriers.
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

For a record the cutoff GRADES, the loop at `:297-303` splits `needs` three ways instead of counting
it whole.

| the exited subject's terminal row | effect |
|---|---|
| carries `disposition fold` | demands nothing, and this is an EXACT claim rather than an approximation |
| carries `disposition promote` | counts one toward `nneed` |
| carries `disposition <other>` | a refusal naming the file, the subject and the illegal value |
| carries no `disposition` at all | a refusal naming the file and the subjects |

`nneed` is then compared against `newids` exactly as it is today. For a record the cutoff does NOT
grade, `nneed` is computed as it is today and both of today's messages are emitted unchanged.

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
| `tools/unattended/check-unattended.sh` | S1 to S8 — the cutoff read, its validation, the split loop, the messages |
| `tools/unattended/check-unattended.test.sh` | S9, S10 — the stale arm repaired, the graded arms added |
| `tools/unattended/.unattended.conf.example` | S12 — the key, blank, with its own header comment |
| `tools/unattended/PROTOCOL.template.md` | S12 — one row in the section 8 key table |
| `memory/guides/UNATTENDED-PROTOCOL.md` | S12 — the same row, byte-identical, for check 10 |
| `.unattended.conf` | S4 — the declaration, at `2026-09-01`, with its reason beside it |
| `.memory-tree.conf` | S11 — the `ARMS_FLOORS` pin for `check-unattended.sh` |
| `memory/project/unarmed-branches.txt` | S6a — three pin rows renumbered from 9, 10, 11 to 10, 11, 12 |
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
- **risks (concurrency, data-loss, rollback hazards)** — four. The renumbering risk is S6a: a new
  `fail 2` branch shifts three pinned ordinals and reds `harness arms` with messages that read like
  rewordings rather than like an insertion, which is why the pin edit is a scope item and not a
  cleanup. The interface risk is the field
  spelling shared with `TOOL-dFoldedVerdict-1`; §8 F1 carries it. The ordering risk is the protocol
  byte cap; §8 F3 carries it. The third is that this build's OWN review rounds, if any exit
  NON-CONVERGENT before order 1 lands, would be unlabelled in a record dated at the cutoff — that is
  a red the build must clear with `TOOL-dFoldedVerdict-3` rather than a design defect here.
  `memory/backlog/TOOL.md` is a `SHARED_RECORDS` member, so the pass that writes S13 may not be
  dispatched concurrently with any sibling pass that also writes it.
- **testing + left-shift gates** — S10's arms plus S13's class amendment. The gap is named in §6 and
  in N4: the fixture arms cannot be run under the standing owner instruction, and each acceptance
  criterion that depends on one names its substitute observation.
- **migration / rollback** — the cutoff IS the migration. Rollback is reverting the commit; no record
  is rewritten by this unit, so nothing on disk needs undoing.
- **user docs** — the protocol's section 8 key table row (S12). No `help/` page: this repo ships no
  such tree and the protocol is the operator-facing carrier.

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
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs, it is green with
  `ARMS_FLOORS` in `.memory-tree.conf` raised to `tools/unattended/check-unattended.sh:102:101`,
  proving S6's new branch is both counted and armed by a positive assertion naming its own text.
- **AC7a** — When `python tools/memory-tree/check-arms.py --report` runs, the three rows of
  `memory/project/unarmed-branches.txt` naming this leg's check 2 sit at ordinals 10, 11 and 12 with
  their signatures unchanged, and no row is reported as stale, as newly armed, or as pinning a branch
  that no longer exists.
- **AC8** — When `bash tools/unattended/check-unattended.sh` runs, check 22 reports no key
  disagreement, so `DISPOSITION_CUTOFF` is present in all three of `.unattended.conf`,
  `tools/unattended/.unattended.conf.example` and the section 8 table of
  `memory/guides/UNATTENDED-PROTOCOL.md`.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, check 6 does not name
  `memory/guides/UNATTENDED-PROTOCOL.md`, and `wc -c memory/guides/UNATTENDED-PROTOCOL.md` reports at
  most 61440 bytes. The file sits at exactly 61440 today, so this criterion is what forces §8 F3 to be
  resolved before the row lands.
- **AC10** — When `grep -cF "grep -vE '\| WONTDO \|'" tools/unattended/check-unattended.sh` runs it
  returns 1, the same count as today, and the line it matches is the HEAD-side id read. The BASE-side
  read carries no such filter, and S8 leaves both unchanged.
- **AC11** — When `memory/gotchas/arm-literal-strands-on-message-edit.md` is read, its "Arming it"
  section states that a message composed inside an awk sub-program and appended to a `fail` argument
  is OUTSIDE the population `check-arms.py` signs, and names this clause as the instance. Corroborated
  by `python tools/memory-tree/check-arms.py --report`, which lists check 2 branch 2 as ARMED on the
  `review loops that ran past the ceiling` literal alone.

## 7. Gates

Every leg below resolves by name in `tools/gate-legs.json`.

- `unattended kit gate` — the leg this unit rewrites. Its checks 2, 10 and 22 are all in scope.
- `harness arms (fail branches armed or pinned)` — S6's new branch, S6a's renumbered pin rows, and
  S11's floor.
- `memory hygiene` — check 12 over this spec, and check 6 over the protocol's byte cap.
- `kit version markers` — the eight `gov:kit unattended@` carriers stay in step. The bump is the
  BUILD's and belongs to order 1; this unit asserts the marker is already ahead of `1.14` when it
  lands, and moves it itself only if it is not.
- `drift-audit records` — the two backlog rows S13 rewrites are records this leg reads.

This unit adds NO new gate leg. S6 adds a `fail` branch inside an existing leg, which is why S11's
floor moves and why `harness arms (fail branches armed or pinned)` is the gate that grades it.

## 8. Open questions

- **F1 — where the retrofit puts the label, and therefore how permissive this reader is.** The reader
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
- **F2 — whether the declared cutoff is `2026-09-01` or a future date.** At `2026-09-01` the leg reds
  on two records between this unit and `TOOL-dFoldedVerdict-3`. A future date would keep the bar green
  in between, and unit 3 would lower it in the same commit as the retrofit.
  **Recommendation: `2026-09-01`.** A cutoff set ahead of the corpus grades nothing, so this unit
  would land a rule with no population and no observation of it firing, which is the could-not-fail
  shape the charter names. The leg is ALREADY red on `origin/main` for
  `memory/builds/dMispairedQuote/RUN.md`, verified by running it in this worktree, so this unit
  inherits a red rather than introducing one; the build lands once, after unit 3. A cutoff edited
  twice inside one build is also a knob whose two values disagree in the history.
- **F3 — how the protocol's section 8 row is paid for.** `memory/guides/UNATTENDED-PROTOCOL.md` and
  `tools/unattended/PROTOCOL.template.md` are each exactly 61440 bytes, and hygiene check 6 at
  `tools/memory-tree/check-memory-hygiene.sh:503` reds on `b[f] > cb` with `GUIDE_CAP_BYTES=61440`.
  There is zero byte headroom; the line count, 725 against 750, is not the binding axis. S12's row is
  roughly 200 bytes and check 22 refuses the key without it, so the row cannot simply be deferred.
  Option A: land the row in this unit and pay for it by collapsing the grandfather sentence repeated
  across the four existing cutoff rows into one line above the table, which drops no claim.
  Option B: resequence so `TOOL-dFoldedVerdict-5` or `TOOL-dFoldedVerdict-6` frees the bytes first.
  Option C: declare the key only after those units land, which strands this unit's own rule.
  **Recommendation: A, coordinated with `TOOL-dFoldedVerdict-6` so the same sentences are not
  compressed twice.** C is refused outright: it makes the cutoff undeclarable and leaves the rewrite
  inert. This fork is the one an owner or the build's fork sweep must close before any byte of S12
  is written, because option A touches text that unit 6 also owns.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft. Predicate, cutoff, messages and arms grounded against
  `tools/unattended/check-unattended.sh` at BASE `adc0543c`; the arm defect at
  `tools/unattended/check-unattended.test.sh:714` reproduced by fixed-string comparison against the
  shipped message and by running the leg over this tree.

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

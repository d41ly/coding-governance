# TOOL-aClosedDocket-4 — clause 3 accepts a FOLD, and the driver records one

**Status:** WONTDO · rev-3 · 2026-09-02 · node a · Tier-2 · base 733552e1 · streams tooling · order 4 · ratified 2026-08-31 · superseded by TOOL-dFoldedVerdict-1 TOOL-dFoldedVerdict-2 TOOL-dFoldedVerdict-3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aClosedDocket-4-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-4-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Make the merge bar accept the disposition `TOOL-aClosedDocket-1` writes into M4. Today
`tools/unattended/check-unattended.sh` clause 3 requires, for every review subject that exited
NON-CONVERGENT or CEILING, at least one unit id present at HEAD and absent at the run's pinned BASE —
promotion, machine-enforced as the only disposition. A fold promotes no id, so without this unit the
rule and the gate contradict each other and the first fold reds the bar permanently.

## 2. Scope (IN)

- **S1** — `--review` accepts a `--disposition fold|promote` flag, recorded on the round row it
  already writes. It is REQUIRED when the STATE `review_state` computes is `NON-CONVERGENT` or
  `CEILING`, and refused otherwise, so the fact exists exactly where the exit does and nowhere else.
- **S1a** — **the trigger is the computed STATE, never the verdict, and rev-1 had that wrong twice
  over.** `--verdict` is CALLER-SUPPLIED and validated against the closed
  `REVIEW_VERDICTS="CLEAN|CLEAN WITH FIXES|BLOCKED"` (`unattended.sh:444`, refused at `:3533-3535`);
  `NON-CONVERGENT` is not a member of it and never was. What the verb computes is the STATE, in
  `review_state` (`:3500`, called at `:3578`). Read literally, rev-1's trigger could never fire — and
  worse, its AC3 was already satisfied by the pre-existing closed-set refusal, so that criterion
  passed today with the unit unbuilt. The ORDERING follows: the flag is validated AFTER `review_state`
  returns, because before that call there is nothing to key on.
- **S2** — the flag joins the driver's existing refusal vocabulary: an unknown value is refused
  naming the legal set, on the same footing as `--verdict`'s closed `REVIEW_VERDICTS`. Round 2
  established that `verb_review` takes only slug, subject, verdict and blockers today, so this IS a
  new flag with a new refusal and a new check number — the spec says so rather than claiming the
  round row absorbs it for free.
- **S3** — clause 3 is satisfied for a subject when EITHER a new unit id appeared since BASE OR that
  subject's exit row carries `disposition fold`. The existing promotion arm is untouched.
- **S4** — the refusal text names both dispositions, so a run that recorded neither is told what is
  missing rather than being told it failed to promote.
- **S4a** — `verb_review`'s own SUCCESS lines at `unattended.sh:3591-3592` hard-code promotion as the
  only disposition, in the sentence a run reads at the moment it exits. They belong to neither
  `TOOL-aClosedDocket-1` (a document) nor rev-1 of this unit (a refusal and a gate clause), so they
  were about to be left saying the opposite of the rule. They move here.
- **S4b** — clause 3's own message at `check-unattended.sh:301,:305` says a subject "exited without
  promoting". Rev-1 fixed the DRIVER's refusal and left the GATE's wording — the same
  document-contradicts-gate defect this whole unit exists to close, one file over.
- **S5** — arms for both directions: a fold-recorded exit passes, and the same fixture with the
  disposition removed still reds. **It reds naming the FILE and the count, not the subject** — clause
  3's promotion arm at `check-unattended.sh:299,:301` deliberately prints no subject, because its own
  comment records that a per-subject attribution is not available for the id delta. Emitting one to
  satisfy a nicer assertion would strand the verbatim expectation at
  `check-unattended.test.sh:710`.
- **S6** — the unattended kit version moves. The carriers are BOTH constant lines
  (`unattended.sh`, `check-unattended.sh`) and ALL THREE shipped templates —
  `SKILL.template.md`, `PROTOCOL.template.md` and `PLAYBOOK-TEMPLATE.template.md`, the third of which
  rev-1 omitted — plus their renders. `check-kit-versions.sh` derives the template population from
  the tree rather than a list, which is why omitting one reds rather than drifting.
- **S6a** — the new `fail` branches S2 and S4 add are graded by the unguarded `check-arms` merge-bar
  leg, and `ARMS_FLOORS` pins `unattended.sh` at `104:101`. That pin moves with the branches or the
  leg reds; rev-1 named neither the leg nor the pin.

## 3. Non-goals (OUT)

- **N1** — the M4 sentence and the SKILL carriers. `TOOL-aClosedDocket-1`, and the split is why this
  unit exists.
- **N2** — clause 3's separate VACUITY on the prompt path. Measured on `aProvenReuse`: two subjects
  exited NON-CONVERGENT, the clause demanded two ids new since BASE and found three, because that
  run's BASE was its own opening commit and the units region was EMPTY there. Every original unit
  read as newly promoted and not one blocker had been. Closing that needs a signal distinguishing
  "appeared because promoted" from "appeared because first rendered", which neither the region nor
  the run-state file carries. S3 is written as a POSITIVE fact so it does not depend on the id delta
  being trustworthy, and the vacuity is filed rather than folded.
- **N3** — inferring the disposition. A run that exits without recording one gets a refusal, never a
  guess; the whole point of a driver-written fact is that an authored claim is not evidence, and an
  inferred one is worse than authored.
- **N4** — retrofitting the flag onto landed run-state files. Clause 3's promotion arm still passes
  them, which is what keeps this unit from redding every record in the tree.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1, S2, S4 — the flag, its refusal, the round row |
| `tools/unattended/check-unattended.sh` | S3 — clause 3's second arm |
| `tools/unattended/unattended.test.sh` | S5 — both directions |
| `tools/unattended/check-unattended.test.sh` | S5 — the clause-3 arms |
| `tools/unattended/PROTOCOL.template.md` and its render | S6 — clause 3 and `--review` |
| `tools/unattended/SKILL.template.md` and its render | S6 — the `--review` usage block |

### Why the driver writes it and not the run

`--review` already computes the NON-CONVERGENT verdict, already writes the round row, and is the only
actor that knows the exit occurred at the moment it occurs. A README sentence would be an authored
claim about a machine-checked item, which is the shape this kit refuses everywhere else. The cost is
honest and stated in S2: a new flag, a new refusal, a new check number.

### Why the flag is required only at the exit

A `--disposition` on a CONVERGING round would be a field with no referent — nothing has been
disposed. Requiring it exactly when the verdict is terminal-without-convergence means the fact and
the condition it describes are created by the same call, and a row carrying it in any other state is
a refusal rather than a tolerated extra.

### Alternatives rejected

- **A new `--fold` verb.** A second verb for a fact the first one already has, with its own argument
  parsing, its own refusals and its own place in the status line.
- **Reading the fold out of the spec revs.** A rev bump is evidence of an edit, not of a disposition;
  every fold round bumps revs and so does ordinary authoring.
- **Relaxing clause 3 to accept any exit.** It would retire the promotion check entirely, which is
  the half that works.

### Rollout

One commit with `TOOL-aClosedDocket-1`'s or immediately after it. Landing the gate half without the
document half leaves a flag no rule asks for; landing the document half without this one reds the bar
on the first fold. They are ordered, not optional.

## 5. Production-readiness checklist

- **Security** — N/A. One flag on a local verb and one predicate on a local gate.
- **Performance** — clause 3 gains one `grep` over a file it already reads per run-state file.
- **Error states** — S2's refusal for an unknown value; S1's refusal for the flag in the wrong state;
  S4's refusal text when neither disposition is recorded.
- **Observability** — the round row carries the disposition, and clause 3 reads it. **Rev-1 also
  claimed `--status` and the wrap-up derivation read it, and both are false**: `verb_status` only
  COUNTS review rows into `noted`, and `BUILD-METHOD` M9 excludes `history`-class entries from the
  wrap-up. Naming a reader that does not read is how a field gets built for an audience it never
  reaches.
- **Testing** — S5, both directions, on both sides of the join.
- **Migration/rollback** — N4: landed records keep passing through the promotion arm. Revert is a
  revert; no state moves.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/unattended.sh --review <slug> --subject s --verdict BLOCKED
  --blockers 4 --disposition fold` writes a round row carrying the disposition, observed by reading
  the run-state file.
- **AC2** — the same call with `--disposition nonsense` is REFUSED and the message names the legal
  set. Observed, not read off the source.
- **AC3** — the same call on a round whose computed STATE is `CONVERGING` is REFUSED by
  `bash tools/unattended/unattended.sh --review`, because the field has no referent there. **The
  fixture must drive a real CONVERGING state**, not merely pass a legal `--verdict`: rev-1's wording
  was satisfied by the pre-existing closed-set refusal at `:3533`, so it passed with the unit
  unbuilt — an acceptance criterion that could not fail.
- **AC4** — a NON-CONVERGENT exit recorded with NO disposition is refused by `--review` naming both
  options, which is S4.
- **AC5** — a fixture run-state file with a fold-recorded exit and NO new unit id since BASE passes
  `bash tools/unattended/check-unattended.sh`. The same fixture reds today, which is what makes this
  criterion the unit's whole point.
- **AC6** — the same fixture with the disposition REMOVED still reds
  `bash tools/unattended/check-unattended.sh`, naming the subject. Without this, AC5 cannot
  distinguish a clause that accepts a fold from one that stopped checking.
- **AC7** — a fixture recording a PROMOTED exit with a new id and no disposition still passes
  `bash tools/unattended/check-unattended.sh`, proving the existing arm is untouched, which is N4's
  observable.
- **AC8** — `bash tools/unattended/check-unattended.sh` exits 0;
  `bash tools/unattended/run-unattended-gates.sh --selftests` exits 0, with the flag NAMED because
  the bare call defaults away from the self-tests and skips `adopt --check`; and
  `bash tools/check-kit-versions.sh` exits 0 after S6's five carriers move together.
- **AC9** — `python tools/memory-tree/check-arms.py` exits 0 with `ARMS_FLOORS` raised to match the
  new branch count, and reds with the pin left where it is. The second half is what proves the pin
  is doing anything.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `unattended kit gate` and `unattended skill wiring` are
unguarded and both reach this unit. `bash tools/unattended/run-unattended-gates.sh` for the kit
self-tests, which that script's own header mandates for `tools/unattended/` work and which this unit
owes because it IS kit work.
What no gate here checks: whether the disposition a run recorded is the CORRECT one for its blockers.
`TOOL-aClosedDocket-1`'s S2 gives the test; no predicate reads intent, and clause 3 grades that a
disposition was recorded rather than that it was right.

## 8. Open questions

- **Q1 — does the round row's existing parser survive a new trailing field?** **FACT-QUESTION ·
  RESOLVED (agent, 2026-08-31, delegated):** the probe is reading both readers — the driver's own row
  writer and `check-unattended.sh`'s clause-3 `awk` — and the observation that decides it is where
  each splits the line. Round 2 verified both split at the first ` · reason ` and regex the tail, so
  a field appended inside the reason tail is parsed by neither as an item name. It can produce a
  negative: a reader that split on the LAST separator would have made this unbuildable as specified.
- **Q2 — should the flag be spelled `--disposition` or reuse `--verdict`'s vocabulary?**
  **RESOLVED (agent, 2026-08-31, delegated):** a separate flag. `REVIEW_VERDICTS` is a closed set
  describing what the ROUND found; a disposition describes what the RUN did about the exit. Folding
  them would make `CLEAN` and `fold` members of one enum that answers two questions, which is the
  two-guards-one-question shape this kit refuses by name.

## 9. Revision log

- rev-3 · 2026-09-02 · WONTDO, superseded by `TOOL-dFoldedVerdict-1`, `-2` and `-3`, which build
  this unit's scope in three units instead of one. Written by node `d` under the owner authorization
  recorded in `memory/builds/dFoldedVerdict/README.md`, not by this build's own operator. A successor
  pointer is a CONTENT change and not the pure status flip `memory/TEMPLATE-SPEC.md` exempts from a
  rev bump, so the rev moves and the date moves with it — the first cut flipped the header at rev-2
  and dated 2026-08-31, which nothing would have caught: hygiene check 12 asserts only that the
  header rev appears in this section, and rev-2 did.
  **TWO CONSEQUENCES FOR WHOEVER RESUMES THIS BUILD**, neither of them repairable from here and both
  filed as `TOOL-dFoldedVerdict-9`. The `--rescope --act retire` row this supersession owes on
  `RUN.md` takes that record's owed-parked count from 0 to 1 against an attested
  `parked-surfaced: yes, 0 surfaced`, so a resumed `--close` refuses on the mismatch. And with all
  four units terminal the derived work-state index no longer lists this build at all, while its
  run-state record still reads `phase: BUILDING` — so the roster change this row exists to make
  visible is invisible in the one place a resumer is told to look.

- rev-2 · 2026-08-31 · round-1 spec-audit fold, the terminating audit M4 requires of a promoted
  unit. Blocker B1: S1 keyed the flag on "the verdict it computes" and `verb_review` computes no
  verdict — `--verdict` is caller-supplied against a closed set that does not contain
  `NON-CONVERGENT`, which is a computed STATE. Read literally the trigger could never fire, and AC3
  passed today via the pre-existing closed-set refusal, with the unit unbuilt. H1 corrected S5: clause
  3's promotion arm prints no subject by design. H2 and H3 added S4a and S4b — the driver's own
  success lines and the gate's own message both still say promotion is the only disposition, and
  belonged to no unit. M1 found a third template carrier and the `--selftests` default. M2 added the
  `check-arms` leg and its `ARMS_FLOORS` pin. M3 deleted two claimed readers that do not read.
  Recorded as CLEAN and not re-derived next time: S3's second arm IS buildable, N4 holds against all
  nine tracked run-state files recording a non-convergent exit, and Q1/Q2 are sound.
- rev-1 · 2026-08-31 · authored at round 2's NON-CONVERGENT exit, PROMOTED out of
  `TOOL-aClosedDocket-1` as blocker B2's disposition. M2 states verbatim that a separate document,
  gate, adopter or generated artifact is a separate unit with its own id and spec, and rev-2 of that
  unit had a document, a gate clause and a driver fact under one id.

## 10. Reuse audit

Three seams, all extended in place. `verb_review` in `tools/unattended/unattended.sh` already
computes the verdict and writes the round row, so S1 adds a field to a line that already exists
rather than a record that does not. Its `--verdict` refusal against the closed `REVIEW_VERDICTS` set
is the shape S2 copies for `--disposition`. And clause 3 in `check-unattended.sh:246-303` already
walks every run-state file, already parses those rows and already reports per subject, so S3 is a
second arm on an existing predicate rather than a new leg.

`python tools/codebase-map/reuse_lookup.py "recording a telemetry log line when a lookup tool runs so
a later check can observe it"` was this build's map probe; it returned `cmd_check` in
`row_grammar.py` and `records` in `gotchas.py`, both inspected and REJECTED — the first grades table
rows against a declared grammar and the second selects bug classes, and neither reads or writes a
review round.

Recall terms used: `non-convergent review loop blocker promotion spec subject mechanism unit
disposition wall-clock timing assertion flake elapsed bound contention`. It returned `aScouredKit`'s
promotion of three units and `aBoundedVerdict`'s empty standing set, which are the two shapes N4
keeps passing, and `TOOL-dHonouredPark-8` on `--review` keying convergence by subject alone.

Where a hit was STALE: none, but one citation in the round-2 report was corrected against source
before being used here — the reader's `type` filter is at `unattended.sh:3270`, not `:3268`.

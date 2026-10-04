# TOOL-aEvidencedLens-7 — `--review` takes highs and minors on a spec subject's exit and requires `promote` when any stood

**Status:** SPECCED · rev-2 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-7-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-7-2-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md) | spec-audit | TOOL-aEvidencedLens-1 TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |

<!-- /gen:spec-records -->

## 1. Goal

The owner answered on 2026-10-05 that a spec audit's MEDIUM and LOW findings are PROMOTED, batched
into one unit or two, as the closing diff review's have been since `TOOL-aBatchedMinors-5`. The driver
still encodes the superseded half of `TOOL-aProbedUnit-9`: `--review` refuses `--highs` and `--minors`
on any subject that is not the build slug, saying a spec audit's mediums and lows are folded, and it
accepts `fold` at a spec subject's converged exit. This unit extends the closing review's counted exit,
built by `TOOL-aBatchedMinors-2`, to every spec subject, so a spec subject's terminal row says what
stood and a row that stood on anything must promote it.

## 2. Scope (IN)

- **S1** — In `verb_review` of `tools/unattended/unattended.sh`, the counts block that today runs only
  when the subject equals the build slug runs for EVERY subject. The refusal that fires when a
  non-slug subject carries a count, and its sentence that a spec audit's mediums and lows are FOLDED,
  are taken out of the verb. Observed by AC1.
- **S2** — At a terminal exit of any subject, `--highs` and `--minors` are REQUIRED. The terminal set
  the block tests becomes `CONVERGED`, `NON-CONVERGENT`, `CEILING` and `BOUNDED`; `BOUNDED` joins it
  for the spec subject, and stays unreachable for the slug subject, whose bound is the ceiling that
  `review_state` tests first. On a round that is not a terminal exit either count is refused, as on
  the slug subject today. Observed by AC2 and AC3.
- **S3** — At a terminal exit, `standing = blockers + highs + minors`. A non-zero `standing` requires
  `--disposition promote`, a zero `standing` refuses `promote`, and `fold` is refused at every
  terminal exit of every subject. The refusal sentences name the subject's kind: the closing diff
  review's keep their bytes, and a spec subject's say a spec audit promotes every confirmed finding,
  the MEDIUMs and LOWs batched into one unit or two. Observed by AC4 and AC5.
- **S4** — The state gate's `fold` refusal at a blocker-bearing exit, which today tells a spec subject
  that fold is legal only at `CONVERGED`, says instead that no exit folds. That sentence would
  otherwise send the operator to a refusal. Observed by AC4.
- **S5** — The row grammar is the one `TOOL-aBatchedMinors-2` S4 wrote, unchanged:
  `verdict <v> · blockers <b> · <EXIT> · highs <h> · minors <m>[ · disposition promote]`. A terminal
  promote echo prints the batched-promotion sentence and the unit floor, one per blocker and high plus
  one for the minors when any stood, for a spec subject exactly as for the slug. Observed by AC6.
- **S6** — `review_exit_note` keeps the batched-promotion sentence and the loud unreachable branch.
  Its `fold` and `promote` sentences, both of which say a MEDIUM or LOW is folded, are rewritten:
  `fold` reaches the loud branch, because no exit can record it, and `promote` prints the batched
  sentence. Every comment in `verb_review` and above `review_exit_note` saying a spec audit's minors
  fold is rewritten to the promotion rule. Observed by AC7.
- **S7** — `REVIEW_DISPOSITIONS` keeps `fold`. Rows written before this unit carry it, check 2's
  closed-set clause reads it, and the leg's suite mutates the set. The verb refuses it at write time
  by state, not by membership. Observed by AC4.
- **S8** — Rows written before this unit, with no counts, keep today's reading. The verb reads a prior
  row's blocker count only (`review_counts`), so an old row is never re-graded here. The rule S2 and
  S3 enforce at write time gets its own dated cutoff, because check 2 grades `fold` only on a counted
  row or beside a non-zero blocker count, so a countless terminal spec row carrying `fold` would
  still pass the bar after this unit. The driver declares `SPEC_COUNTS_CUTOFF`, a quoted ISO date, beside
  `FOLD_CUTOFF`, by the same idiom: strictly past the newest record any branch can still write under
  the old contract, which the builder derives from the newest spec-subject `review` row on any branch
  it can see and records in the commit message. Its comment says what it dates and that check 2
  reads it; the reading is `TOOL-aEvidencedLens-9`'s. Observed by AC8 and AC9.
- **S9** — Check 2 of `tools/unattended/check-unattended.sh` is NOT edited here. It reads a row's
  counts by their presence and never by its subject, so a counted spec row already owes one unit per
  blocker and high plus one for the minors (§4 Evidence, measured). Its prose calling a counted row a
  closing-review row is corrected by `TOOL-aEvidencedLens-9`, which holds that file this order.
  Observed by AC8.
- **S10** — The suite arms that pin the old spec-subject behaviour are rewritten in
  `tools/unattended/unattended.test.sh`, and the one terminal spec round in
  `tools/unattended/runlog-writer.test.sh` carries `--highs 0 --minors 0`. NOT OBSERVED inside the
  pass, because shared invariant 9 keeps suites out of passes; §7 declares the arms.

## 3. Non-goals (OUT)

- The build harness's record command. `TOOL-aEvidencedLens-8` makes `writeRound` pass the counts.
- Check 2's reader. It already owes the right floor; only its prose moves, in `TOOL-aEvidencedLens-9`.
- The carriers that teach the rule: the method's M4, the unattended Skill's review section and the
  `--review` verbs entry. `TOOL-aEvidencedLens-11` owns them.
- The usage header's `[--disposition fold|promote]` spelling. It names the closed set, which keeps
  `fold` (S7); check 26 grades the flag, not its values.
- Grading history with the cutoff. This unit declares `SPEC_COUNTS_CUTOFF` (S8); check 2's reading of
  it is `TOOL-aEvidencedLens-9`'s, the unit holding that file this order (§3 Edges).
- `REVIEW_ROUNDS` and its default. The owner's; `TOOL-aEvidencedLens-9` guards the key.
- A kit version bump. The main loop bumps once at the close (shared invariant 7).

### Edges

- **hands-off** `TOOL-aEvidencedLens-8` — the two count flags this unit makes legal and required at a
  spec subject's terminal exit, which the harness's round record must then pass.
- **hands-off** `TOOL-aEvidencedLens-9` — check 2's comment and its two messages that call a row
  carrying counts a closing-review row, which after this unit a spec subject's row is too; and check
  2's reading of `SPEC_COUNTS_CUTOFF`, refusing on a row first-committed on or after it a terminal
  spec-subject row that carries no counts or records `fold`.
- **hands-off** `TOOL-aEvidencedLens-11` — the Skill's spec-subject review invocation, the verbs entry
  and the method's M4, which still say a spec audit's mediums and lows fold.

## 4. Design

### Evidence

Read at base `028b5cac`, which is `origin/main` at preflight; the run branch's later commits touch only
`memory/builds/aEvidencedLens/`.

- `tools/unattended/unattended.sh:10109` refuses `--highs`/`--minors` when the subject is not the
  slug, with the sentence "a spec audit's mediums and lows are FOLDED into the spec under review".
- The counts block at `:10214` to `:10242` is guarded by `[ "$subj" = "$slug" ]` and its terminal case
  lists `CONVERGED|NON-CONVERGENT|CEILING`.
- `review_state` at `:10011` tests `CEILING` before `BOUNDED`, and `verb_review` sets the slug's bound
  to `RUNAWAY_CEILING` at `:10171`, so the slug subject never reaches `BOUNDED`.
- The state gate at `:10187` to `:10209` refuses `fold` at `NON-CONVERGENT`, `CEILING` and `BOUNDED`;
  on a spec subject its sentence ends "fold is legal only at CONVERGED".
- `review_exit_note` at `:10065` carries a `fold` sentence and a `promote` sentence that each say a
  MEDIUM or LOW is folded, and a `closing` sentence; `:10257` prints the `closing` one only when the
  counts were written.
- CHECK 2, MEASURED 2026-10-05: the awk program at `tools/unattended/check-unattended.sh:718` to
  `:816`, extracted to a scratch file and run over one row
  `review · item S1 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 1 · minors 2 · disposition promote`
  with `graded=1`, printed "against a floor of 3" at `newids=2` and nothing at `newids=3`. The floor is
  `bl + hh + (mm > 0 ? 1 : 0)` keyed on the presence of both counts (`cnt`, `:737`), never on the
  subject. Its message at `:801` and the comment at `:727` call such a row a closing-review row.
- Suite readers: `tools/unattended/unattended.test.sh` holds 37 `--review` calls on a subject that is
  not `tRun`, at `:2786` and `:5568` to `:5747`, PINNED 2026-10-05 by
  `grep -n -- "--review " tools/unattended/unattended.test.sh | grep -v -- "--subject tRun "`. The arms
  that record a terminal spec round with no counts are the C1, C2, C3, S1, D1, D2, B1 and B2 blocks and
  the arm at `:5717` that pins the old refusal. `:2786` passes a hostile subject that the newline and
  separator guards refuse before the counts block, so it does not move.
  `tools/unattended/runlog-writer.test.sh:709` records `--subject X-$SLUG-1 --verdict CLEAN --blockers 0`,
  a converged spec round with no counts, which this unit refuses.

### The verb after this unit

```text
counts flags well-formed?                          -> else refuse (unchanged)
disposition in the closed set?                     -> else refuse (unchanged)
subject guards, terminal-subject guard             -> unchanged
state gate: terminal exit with blockers > 0
   no disposition                                  -> refuse naming promote (unchanged)
   fold                                            -> refuse: no exit folds
counts block, EVERY subject:
   terminal (CONVERGED|NON-CONVERGENT|CEILING|BOUNDED)
     highs or minors missing                       -> refuse naming both
     fold                                          -> refuse: no exit folds
     standing > 0 and not promote                  -> refuse naming promote
     standing = 0 and a disposition                -> refuse: promotes nothing
   not terminal and highs or minors given          -> refuse: an exit that has not happened
```

The slug subject's refusal sentences stay byte-identical; the spec subject's name the spec audit.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/runlog-writer.test.sh`

### Alternatives rejected

- **Requiring the counts only at `BOUNDED`, the default exit.** A spec subject under a raised
  `REVIEW_ROUNDS` exits `CONVERGED` or `NON-CONVERGENT` too, and its minors stand there as much as at
  `BOUNDED`.
- **Taking `fold` out of `REVIEW_DISPOSITIONS`.** Archived rows carry it and check 2 grades a value
  outside the set as written by hand; the set would make every such row an illegal-value red.
- **Editing check 2 here.** Its reader is already right; the prose fix sits in the unit holding that
  file this order, so the two units' write sets stay disjoint.

## 5. Production-readiness checklist

- security — no new write path; the row still goes through `park()` and its guards.
- perf / scale — one string test fewer and one case member more per round.
- error / empty / loading states — a missing count, a count on a non-terminal round, `fold` at any
  exit and a promotion of nothing are each a numbered refusal (check 37) that writes no row.
- observability — the echo names the unit floor the exit owes on a spec subject as on the slug.
- risks — until `TOOL-aEvidencedLens-8` lands, the build harness's record of a terminal spec round is
  refused, because it passes no counts. Both land in this build, and this build's own round-1 audit
  is recorded by the driver at BASE, before either.
- testing — each refusal is observed against the base driver first, then against the edited one.
- migration — none: old rows keep their reading (S8).
- user docs — the Skill, the verbs entry and the method, in `TOOL-aEvidencedLens-11`.

## 6. Acceptance criteria

Each criterion runs the edited `tools/unattended/unattended.sh` `--review` verb in a scratch fixture
repository: `git init` under a short directory beneath `%TEMP%`, with a minimal `.unattended.conf` and
run-state file built as the suite's `mkconf` and `bcopen` build them, `REVIEW_ROUNDS` at 1 unless
named. Each refusal is first observed against the driver at the pass's base, read with `git show`.

- **AC1** — When `--review` runs on spec subject `S9` with `--verdict BLOCKED --blockers 1 --highs 0
  --minors 2 --disposition promote` at `REVIEW_ROUNDS` 1, it writes the row and prints `BOUNDED`.
  Red when: the base driver's refusal naming the closing diff review's counts fires.
- **AC2** — When a terminal spec round omits either count (`--blockers 0` with `--highs 1` only, and
  `--blockers 2 --disposition promote` with neither), `--review` refuses naming `--highs and --minors`
  and writes no row.
  Red when: a terminal spec row is written with no counts, the base behaviour at `CONVERGED`.
- **AC3** — When a spec subject's first round runs at `REVIEW_ROUNDS` 2 with `--blockers 3 --minors 1`,
  `--review` refuses naming an exit that has not happened.
  Red when: a count is written on a `CONVERGING` spec round.
- **AC4** — When a spec subject converges with `--blockers 0 --highs 0 --minors 3` and no disposition,
  `--review` refuses naming `promote`; with `--disposition fold` it refuses saying no exit folds; and
  at a `BOUNDED` exit with `--blockers 2 --highs 0 --minors 0 --disposition fold` the refusal no longer
  contains `fold is legal only at CONVERGED`.
  Red when: `fold` is accepted at a converged spec exit, or a sentence points at a legal fold.
- **AC5** — When a spec subject converges with `--blockers 0 --highs 0 --minors 0 --disposition
  promote`, `--review` refuses as promoting nothing; with no disposition it writes the row.
  Red when: a zero-standing promote row is written on a spec subject.
- **AC6** — When a spec subject exits `BOUNDED` with `--blockers 1 --highs 1 --minors 4 --disposition
  promote`, the row ends `blockers 1 · BOUNDED · highs 1 · minors 4 · disposition promote` and the
  echo names a floor of 3 units and the batched sentence.
  Red when: the counts follow the disposition, or the echo prints the sentence saying a MEDIUM or LOW
  is folded.
- **AC7** — When `grep -nE "FOLDED into the spec|a MEDIUM or LOW is folded|minors are folded|reachable from ONE exit, CONVERGED|ACCEPTED there and never required" tools/unattended/unattended.sh`
  runs, it prints nothing.
  Red when: a message or comment still states the spec-audit fold, the two comments at
  `review_exit_note` and in `verb_review` included.
- **AC8** — When the slug subject's existing closing-review rounds of AC2 to AC6 of
  `TOOL-aBatchedMinors-2` are replayed in the fixture, every refusal and row is byte-identical to the
  base driver's; and the row AC6 writes, run through check 2's awk program extracted as §4 Evidence
  did, prints a floor of 3 at `newids=2`.
  Red when: a closing-review sentence moved, or check 2 does not owe the counted spec row's units.
  cost: the fixture rebuild per arm is a few seconds each.
- **AC9** — When `grep -nE '^SPEC_COUNTS_CUTOFF="[0-9]{4}-[0-9]{2}-[0-9]{2}"$' tools/unattended/unattended.sh`
  runs it prints one line, sitting after the `FOLD_CUTOFF=` line, and its date is strictly later
  than the newest `review · item` row naming a spec subject in any `memory/builds/*/RUN.md` reachable
  from the pass's HEAD, a figure the commit message records.
  Red when: the constant is absent, malformed, or dated on or before a record the old contract wrote.
  figure: DERIVED at observation time from the run-state files at the pass's HEAD.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the base driver, which refuses `--minors` on a spec subject and accepts a converged spec round with no counts · none
New arm: tools/unattended/unattended.test.sh · `fold` at a converged spec exit, which the base driver accepts · none

## 8. Open questions

- **F1 — Is `fold` taken out of the disposition set, or refused by state?** Out of the set makes every
  archived `disposition fold` row an illegal value for check 2; refused by state keeps old rows legal
  and new ones impossible.
  RESOLVED (agent, 2026-10-05, delegated): refused by state at every terminal exit; the set keeps it
  (S7).
- **F2 — Does `CONVERGED` with zero standing require the counts at all?** Requiring them is what lets
  check 2 tell "nothing stood" from "nobody counted"; the harness can always pass `--highs 0 --minors
  0`, and `TOOL-aEvidencedLens-8` S4 already spells that command.
  RESOLVED (agent, 2026-10-05, delegated): required at every terminal exit, S2.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the spec brief's unit 7, the owner's 2026-10-05 answer and
  `verb_review` read at `028b5cac`.
- rev-2 · 2026-10-05 · §3 S8 AC7 AC9 · round-1 spec audit fold. Id 46 (MEDIUM): the "no cutoff"
  non-goal is replaced by `SPEC_COUNTS_CUTOFF`, declared here beside `FOLD_CUTOFF` and observed by
  AC9, and the §3 hands-off to `TOOL-aEvidencedLens-9` now carries check 2's reading of it. Id 13
  (LOW): AC7's alternation adds the two stale comments at `review_exit_note` and in `verb_review`.

## 10. Reuse audit

The seam extended is `verb_review`'s counts block, built by `TOOL-aBatchedMinors-2`: its refusals, its
`standing` sum, its row grammar and its batched echo are widened from the slug subject to every
subject, and no new verb, flag, row field or reader is added. Check 2's counted-row floor from
`TOOL-aBatchedMinors-3` is reused unedited, and was measured rather than assumed (§4 Evidence).
`python tools/codebase-map/reuse_lookup.py` prints `unscanned layers: .sh`, so it cannot see this
seam; the seam was found by reading `tools/unattended/unattended.sh`. The recall query returned
`TOOL-aProbedUnit-9`, whose fold half this unit stops encoding, `TOOL-aBatchedMinors-5`, the closing
review's promotion this unit extends, and the sibling `TOOL-aEvidencedLens-8` spec, whose record
command S2 and S3 agree with.

Recall terms used: `python tools/memory-recall/query.py "should a spec audit's mediums and lows be folded or promoted, and what does --review record at a spec subject's exit" --terms "spec-audit disposition fold promote minors highs batched BOUNDED CONVERGED verb_review severity rule"`

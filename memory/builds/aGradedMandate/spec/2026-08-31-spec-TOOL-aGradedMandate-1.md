# TOOL-aGradedMandate-1 — `closing-review-recorded` requires the closing loop to have ENDED

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

`closing-review-recorded` asks whether a review record EXISTS and never whether the review loop
ended. The run-state file already holds the answer, in a closed vocabulary, written by `--review`.
This unit makes the item read it, so a run that abandons its closing loop mid-convergence blocks at
`--close` instead of landing green.

## 2. Scope (IN)

- **S1** — Add a second term to `dod_met`'s `closing-review-recorded` arm, evaluated after the
  existing record join succeeds. It reads the `review` rows in the run-state file whose subject is
  the BUILD SLUG and requires that at least one exists and that the LAST one carries a terminal
  token from the closed set `CONVERGED` / `NON-CONVERGENT` / `CEILING`.
- **S2** — Where that last row is `CONVERGED`, require its `blockers` count to be `0`. The verb
  cannot write any other pairing today, so this is a consistency assertion over a hand-edited
  record rather than a second policy.
- **S3** — Add a reader beside `review_counts` that returns the last row's REASON text for a
  subject, since `review_counts` projects the count and discards the token. It parses the same
  grammar in the same shape, so the two cannot disagree about what a row is.
- **S4** — Four distinguishable `DOD_OUT` messages: no round at all, a live loop with no terminal
  token, a `CONVERGED` row whose count is not zero, and the existing record-join failures unchanged.
- **S5** — Re-measure and rewrite the stale justification comment at the head of the arm. It states
  that `^## Verdict: CLEAN` matches zero of a 46-record corpus; the corpus is 208 records with 170
  carrying `^## Verdict`, and the check that made it mandatory is memory hygiene check 22.

## 3. Non-goals (OUT)

- **No leg-side ratchet.** A leg clause over records at `LANDING`/`LANDED` would red
  `memory/builds/aBoundedCeiling/RUN.md` and `memory/builds/aPrimedKeepalive/RUN.md` on the default
  branch today, over finished records no verb may rewrite. That is an unlandable gate, and the
  no-machine-half residual is stated in §5 rather than built.
- **No verdict-token join on the review RECORD.** Refuted during the review: a converged loop's
  round-1 record legitimately reads `BLOCKED` and is never rewritten, and the arm selects the FIRST
  matching file, so anchoring a verdict reds honest landings.
- **No new authored fact and no new grammar.** The rows exist; only a reader is missing.

## 4. Design

### Data model

No change. A `--review` round is already an append-only `review`-kind parked line whose reason field
is `verdict <V> · blockers <N>[ · <TERMINAL>]`. `verb_review` refuses a second round on a subject
that already carries a terminal token, so "the last row" and "the terminal row" coincide whenever
one exists.

### Inventory

| Site | Change |
|---|---|
| `tools/unattended/unattended.sh` `review_counts` | unchanged; a sibling is added below it |
| `tools/unattended/unattended.sh` `dod_met` `closing-review-recorded` | the second term and its messages |
| `tools/unattended/unattended.test.sh` | arms for each of the three new refusals and the passing case |
| `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` | the §4 cell |

### Migration

None for a terminal record: every existing `LANDED` record is never re-closed.

The one live record in the tree is `memory/builds/aThawedCorpus/RUN.md`, and it WOULD BLOCK. Round 1
of the spec audit corrected an earlier reading of this section that said the opposite. That file
holds exactly one review row, `review · item TOOL-aThawedCorpus-5 · reason verdict BLOCKED ·
blockers 5`: the subject is a UNIT id rather than the build slug, so the S1 join returns no row at
all, and the row carries no terminal token either. Both S4 messages would fire.

That is accepted rather than exempted. The record is at `LANDING` with `--close` already run and
nothing re-evaluates it, so the term costs nothing today; and a record whose closing loop stopped at
five blockers is exactly the state this term exists to refuse, so carving it out would be carving
out the case.

### Alternatives rejected

Anchoring `## Verdict:` on the selected review record — see §3. Requiring `CONVERGED` specifically —
rejected because `NON-CONVERGENT` and `CEILING` are legitimate exits whose obligations the leg's
promotion clause already grades.

## 5. Production-readiness checklist

- security — N/A. The rows are written by the run and read by the run; §9 of the protocol already
  states what a check under the run's own uid buys, and this adds no new trust.
- perf / scale — N/A. One `awk` pass over a file the arm already opens.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — the empty case is a named refusal (S4), never a silent pass.
- observability — the refusal text names the subject and the last row, so an operator sees which
  loop was abandoned without opening the file.
- risks — the item stays overridable, so a genuine edge is a recorded override rather than a wedge.
  The residual is that a run which never calls `--review` at all now fails rather than passing, which
  is the intended behaviour change and is announced in the message.
- testing + left-shift gates — the three refusals and the pass are arms in `unattended.test.sh`,
  each observed RED against a staged record before the fix is called built.
- migration / rollback — reverting the term restores the previous behaviour exactly.
- user docs — the Skill's `--close` section gains one sentence in `TOOL-aGradedMandate-8`.

## 6. Acceptance criteria

- **AC1** — When a run-state file carries no `review` row for the build slug, `--close` blocks on
  `closing-review-recorded` with a message naming the absent loop, verified by an arm in
  `unattended.test.sh`.
- **AC2** — When the last `review` row for the slug carries no terminal token, `--close` blocks and
  the message quotes that row's `blockers` count.
- **AC3** — When the last row reads `CONVERGED` with a non-zero `blockers` count, `--close` blocks.
- **AC4** — When the last row carries `CONVERGED · blockers 0`, or `NON-CONVERGENT`, or `CEILING`,
  and the record join already passes, the item is MET.
- **AC5** — `grep -c "46 records" tools/unattended/unattended.sh` returns `0`, and the replacement
  sentence names the measured 208/170 pair.
- **AC6** — `bash tools/unattended/run-unattended-gates.sh --checks` stays green.
- **AC7** — Before the term is wired, the candidate predicate is run over every tracked `RUN.md`
  with `GIT ls-files`, printing hits AND near-misses, and its output is recorded in this build's
  journal record. The expected hits are `memory/builds/aBoundedCeiling/RUN.md`,
  `memory/builds/aPrimedKeepalive/RUN.md` and `memory/builds/aThawedCorpus/RUN.md`; a fourth hit is
  a finding, not a pass.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests` for the driver suite.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F1 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

- rev-2 · 2026-08-31 · round-1 fold of the spec audit's F9: section 4 Migration re-derived against the record it names, which WOULD block, plus AC7 requiring the candidate predicate be run over every tracked RUN.md before wiring.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "unattended run driver verbs and definition of done checks"`
and `python tools/memory-recall/query.py` with terms `unattended mandate driver preflight
definition-of-done attestation adversarial review directive waiver phase witness closing-review
quality regression gate` were run for the SET at orientation.

The seam is `review_counts` at `tools/unattended/unattended.sh:3434` — it already parses this exact
row grammar and is called only by `verb_review`. This unit extends that seam with a sibling reader
rather than writing a second parser, which is the defect its own header warns about ("the only
grammar split here is the park helper's own output"). The verdict-vocabulary constant
`REVIEW_VERDICTS` and the terminal-token set in `review_state` are reused verbatim.

A stale hit was found and is recorded: the arm's justification comment describes a 46-record corpus
that no longer exists. Verified against the tree at `396cd9db` rather than believed, which is why S5
exists.

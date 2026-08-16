# PLAY-aDeclaredCeiling-1 — the refuted follow-up, recorded where it was asserted

**Status:** CLOSED · rev-2 · 2026-08-16 · node a · Tier-1 · base 96141aed · streams playbook

## 1. Goal

Two landed `aSiftedPlaybook` records assert a defect at `WIRE-INTO-PROJECT.md:464` that does not
exist. Record the refutation in both, so the next reader does not mint the follow-up a third time.

## 2. Scope (IN)

- **S1 — the audit report.** `memory/builds/aSiftedPlaybook/build/2026-08-16-build-aSiftedPlaybook-1-playbook-audit.md`
  files the line under "what this audit did not cover" as a follow-up: "`WIRE-INTO-PROJECT.md:463`
  calls `agent-cap` 'the review protocol's TWO rules' against four". The bullet is replaced with the
  measurement that refutes it, marked the way that report already marks its withdrawn `R2`
  ("REFUTATION WITHDRAWN"), so the file keeps one convention for a verdict that moved.
- **S2 — `PLAY-aSiftedPlaybook-1` §3.** The same claim sits in that spec's Non-goals as a deferred
  follow-up. It gains the refutation in place. The spec is CLOSED, so this is an append to a
  terminal record's §3 and a `rev` bump with its §9 line — not a rewrite of what the unit did.
- **S3 — the backlog row closes as refuted.** `PLAY-aDeclaredCeiling-1` in `memory/backlog/PLAY.md`
  moves to CLOSED with the measurement, because a row that says "record the refutation" is not
  discharged by recording it somewhere else and leaving the row open.

## 3. Non-goals (OUT)

- **Editing `WIRE-INTO-PROJECT.md:464`.** There is nothing wrong with it. This unit exists because
  two records say otherwise.
- **Auditing the rest of the audit report.** Earlier rounds already re-adjudicated one of its rows
  and corrected a commit citation in another — the round numbers are deliberately not spelled here,
  because a first draft of this line got both wrong in the spec whose subject is provenance drift.
  A third pass over a landed report is a different unit and would have no acceptance criterion
  short of re-running the whole audit.
- **Making the protocol's rule count machine-checked.** `tools/check-playbook-parity.sh`'s S2 pair
  list is where a claim like this would be pinned, and adding a pair whose extraction is "count the
  `##` sections of a protocol document" is a real design question, not a records fix. Recorded as a
  candidate in §4, not built.

## 4. Design

### The measurement

`WIRE-INTO-PROJECT.md:465-467` reads, in full: "This is the mechanical enforcement of the review
protocol's TWO rules: route fan-out through the cap-5 helpers, AND a review's verify stage spawns at
most 5 agents TOTAL."

`memory/guides/REVIEW-PROTOCOL.md` binds exactly two rules, and its own `##` headings name them:
`## The hard cap — ≤5 verify-stage agents TOTAL` and `## Concurrency — ≤5 agents at once, always`.
The runbook's sentence names those two, in that order, correctly.

The "four" comes from `tools/hooks/agent-cap.js`, which numbers four implementation RULES — the
raw-primitive ban, the verifier-arity rule, the bound-resolution rule, and the direct-spawn count.
Those are how the hook enforces the protocol's two rules; they are not a second count of the rules
themselves. The audit compared a sentence about the PROTOCOL to a population in the HOOK.

### Why this is worth a unit rather than a deletion

The cheap option is to delete both bullets. Rejected: a deleted follow-up is indistinguishable from
one that was never written, and this exact claim survived an eleven-defect audit, five spec-review
rounds and a closing review without anyone opening the sentence. A reader who finds `:464` and
counts four hook rules will re-derive it. The refutation has to be findable from the place the claim
was made.

### The candidate this leaves behind

A pair in `check-playbook-parity.sh` that compared "the number the runbook states the protocol
binds" against "the count of the protocol's rule headings" would have caught the claim if it were
true, and would catch a real future drift. It is not built here because the extraction on the
protocol side is a heading count over prose, which is exactly the kind of selector that matches the
empty set when a heading is reworded — the vacuity class that gate's own header is about. Deciding
whether it can be written non-vacuously is a design question this Tier-1 unit will not answer.

### Files touched

| File | Change |
|---|---|
| `memory/builds/aSiftedPlaybook/build/2026-08-16-build-aSiftedPlaybook-1-playbook-audit.md` | S1 — the bullet, marked withdrawn |
| `memory/builds/aSiftedPlaybook/spec/2026-08-16-spec-PLAY-aSiftedPlaybook-1.md` | S2 — §3 + rev bump |
| `memory/backlog/PLAY.md` | S3 — the row closes |

All three are inside `memory/` and none is a product glob, so no spec id in this build risks the
zero-tolerance citation signal. Checked rather than assumed: `memory/guides/SESSION-KICKOFF.md` is
the one `memory/` path that IS a product glob and this unit does not touch it.

## 5. Production-readiness checklist

Tier-1: the sections that do not apply are named rather than dropped. Security, perf, a11y, i18n,
error states, observability, migration — all N/A, three markdown records and no executable change.

- risks — the one real risk is editing a CLOSED spec. S2 appends to §3 and bumps the rev; it does
  not restate what the unit built, because a terminal record that changes its own scope is worse
  than a stale follow-up.
- testing + left-shift gates — there is no gate for "a record's claim about another file is true",
  and §4 says why the obvious one is not built here. That is the honest disposition, not a gap left
  unstated.
- user docs — the audit report and the spec ARE the docs.

## 6. Acceptance criteria

- **AC1** — When the audit report's follow-up bullet is read, it states the measurement and is
  marked withdrawn in the same form the report already uses for `R2`, and it no longer asserts a
  defect at `:464`.
- **AC2** — When `PLAY-aSiftedPlaybook-1` §3 is read, the `:464` bullet carries the refutation, and
  the spec's `rev` and §9 have both moved.
- **AC3** — When `grep -n "TWO rules" WIRE-INTO-PROJECT.md` runs it returns exactly ONE hit, that
  hit's text names the two rules the protocol binds, and `git diff --stat` names
  `WIRE-INTO-PROJECT.md` nowhere in this diff. The claim is correct, so the acceptance is that the
  subject was NOT edited.

  **This criterion deliberately pins no LINE NUMBER, and that is the finding it was rewritten
  from.** It read `:464`, which was wrong: the line sits at `:465` at HEAD and at BASE, having moved
  `464 -> 465` at `d3bd21b` one commit after a review round corrected the same anchor `463 -> 464`.
  A criterion that pins a line number in a file its own §3 forbids editing can only ever go stale,
  and this one had gone stale twice before it was written. The unit's whole deliverable is a
  measurement about that line; it is anchored by CONTENT so the record survives the next insertion
  above it.
- **AC4** — When `grep -c "## The hard cap\|## Concurrency" memory/guides/REVIEW-PROTOCOL.md` runs
  it returns 2, which is the measurement both records now cite. **Its reach is limited and stated:**
  it is pinned to two literal headings, so a THIRD rule added under a new heading passes it
  unnoticed, and a rewording of either existing heading reds it for the wrong reason. It makes the
  refutation re-checkable, not future-proof, and a real guard is the `check-playbook-parity.sh`
  pair §4 declines to build.
- **AC5** — When `memory/backlog/PLAY.md` is read, `PLAY-aDeclaredCeiling-1` is CLOSED.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs it exits 0, so the edited
  records still satisfy the row grammar and the index caps.

## 7. Gates

- `bash tools/memory-tree/check-memory-hygiene.sh` — three record files change.
- `python tools/memory-tree/gotchas.py --for-diff` — the bug-class checklist for a records diff.
- `python tools/drift-audit/drift_report.py --check` — a CLOSED spec is edited; confirm no signal
  moves.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-2 · 2026-08-16 · folded the round-1 spec audit. **B1**: AC3 pinned `:464` — the line is at
  `:465` and has moved twice under two separate corrections, so the criterion is now anchored by
  CONTENT and says why. The unit whose only deliverable is a measurement had shipped a draft with a
  wrong one. **L1**: the round numbers in §3 were both wrong and are now stated without them.
  **L3**: AC4's caveat records what a two-heading grep cannot protect against.
- rev-1 · 2026-08-16 · initial draft. Written after the design pass measured the claim instead of
  inheriting it. The follow-up had been carried by two landed records and named in a wrap-up, and no
  reader had opened `WIRE-INTO-PROJECT.md:464` — including me, until this pass.

## 10. Reuse audit

Not required: `memory/TEMPLATE-SPEC.md` gates §10 on `SPEC10_CUTOFF` for the ten-section canon and
this is a Tier-1 spec, which the same file says may write "the few sections that matter". It is
written anyway because the probes were run for the build and their result bears on this unit
specifically.

`reuse_lookup.py "declared byte budget pin justified beside its value"` surfaced no seam relevant
to a records correction, which is the expected answer for a unit that ships no mechanism — recorded
because M5 says a miss is an answer to record, never a failure to retry with softer words.

The prior art that DOES bind here is the audit report's own `R2` row, which was refuted, then had
its refutation WITHDRAWN in round 3 when the measurement moved. That row is the precedent for how
this file marks a verdict that changed, and S1 follows it rather than inventing a second convention.

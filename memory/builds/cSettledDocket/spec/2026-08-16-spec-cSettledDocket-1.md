# TOOL-cSettledDocket-1 — a `--park` verb, so a refused decision has somewhere the gate reads

**Status:** OPEN · rev-1 · 2026-08-16 · node c · Tier-2 · base 1da67d9c · streams tooling

## 1. Goal

`memory/guides/UNATTENDED-PROTOCOL.md` tells a run to park what it refuses to decide, and §2 declares
four parked kinds. The driver writes a parked entry from exactly three places — `--close --override`,
`--abort`, and `--preflight --waive` — and none of them is available mid-run. So an agent that
refuses a decision at pass four has no route to the record, and the instruction the protocol gives is
one the kit cannot obey.

Measured on this tree: `grep -c -- '--park' tools/unattended/unattended.sh` returns 0. It was hit
during cBriefedPilot's own fold, where the workaround was a backlog row — which is a different
document, read by different people, at a different time.

## 2. Scope (IN)

- **S1** — `--park <slug> --item <handle> --reason <text>`, dispatched like the other verbs, writing
  through the existing `park()` with kind `fork`.
- **S2** — the reason is REQUIRED and non-empty, refused with the same argument unit 3 made for
  `--waive`: an entry recording no reason is indistinguishable from one nobody meant.
- **S3** — refused on a TERMINAL record, through the existing `refuse_if_terminal`. A finished run
  parks nothing; `--abort` is the verb for a decision that stops the run.
- **S4** — the item is free text, NOT joined to the directive registry. A parked fork names a
  QUESTION, not a handle, and every other parked kind that names a handle has a registry to join to.
  §4 records why the join would be wrong here rather than merely absent.
- **S5** — IDEMPOTENT on a byte-identical `(item, reason)` pair, matching `--waive`'s re-preflight
  rule, so a resumed run that re-parks the same refusal does not duplicate the row.
- **S6** — arms in `tools/unattended/unattended.test.sh`: the happy path writes one row; a missing
  reason refuses; a terminal record refuses; a repeat is a no-op; and the parked row is visible to
  `--status`.
- **S7** — the protocol's §2 gains the verb beside the kind it writes, in both copies.

## 3. Non-goals (OUT)

- **A fifth parked kind.** `fork` is already declared in §2 and already written by nothing. This unit
  gives it a writer; inventing a kind would be answering a question §2 already answered.
- **Blocking `--close` on unresolved forks.** A parked fork is a record for the wrap-up, not a gate.
  `build-complete` and the roster already decide what blocks a landing, and a second gate over the
  same question is the two-answers defect.
- **A `--unpark`.** The parked region is append-only by design; a fork that gets resolved is recorded
  as resolved in the spec's §8, which is where `--plan` already reads resolution from.
- **Surfacing parked entries in `--plan`.** `--status` reads the record; `--plan` reads spec headers.
  Mixing them puts one answer in two verbs.

## 4. Design

### Where it hooks

`park()` at the driver's tail already takes `(file, kind, item, reason)` and appends one timestamped
line. Three verbs call it. This unit adds a fourth caller and no new writer, so the grammar leg check
17 reads is unchanged and the arms that grade it stay valid.

Dispatch mirrors `--waive`'s accumulator rather than the scalar form unit 1 replaced: one `--item`
and one `--reason` per invocation, and a pair left without its reason is refused before anything is
written.

### Why the item is NOT joined to the directive registry

Check 17 joins a WAIVER's item to `DIRECTIVES_CORE` because a waiver names a rule being relaxed, and
that rule has a registry. A fork names a question the agent refused — "do facts 5 through 7 pin with
fact 4?" — and there is no enumeration of questions a build might raise, nor should there be: the
value of the record is that it captures something nobody anticipated. A join here would either refuse
every honest park or need a registry that grows on every use, which is not a registry.

That asymmetry is worth stating in source, because the next reader will see check 17 joining one kind
and ask why the sibling does not.

### Idempotence, and why it is the same rule as `--waive`'s

The protocol's recovery instruction after a compaction is to re-run `--preflight`, and an agent that
re-derives its position will re-park the same refusal. `--waive` already refuses to re-park a
byte-identical set for exactly that reason. A `--park` without the rule turns every compaction into a
duplicate row, and the wrap-up derivation counts parked entries.

### Files touched

`tools/unattended/unattended.sh` (dispatch, `verb_park`, usage) · `tools/unattended/unattended.test.sh`
(six arms) · `tools/unattended/PROTOCOL.template.md` + `memory/guides/UNATTENDED-PROTOCOL.md` (§2) ·
`tools/unattended/SKILL.template.md` and its render (the parking instruction gains its command).

### Alternatives rejected

- **Overloading `--phase` with a `--park` flag.** The phase verb writes a position; a park writes a
  decision. Both would then share a refusal path and a witness field that means nothing for one of
  them.
- **Letting `--status` accept the park.** A read verb that writes is the exact risk `govkit`'s
  read-only `plan`/`check` arms were built to catch, and this repo already found one such defect.

## 5. Production-readiness checklist

No new dependency and no new file. One dispatch arm, one verb function, six test arms. The rendered
Skill changes, so `adopt-unattended.sh --check` must be re-run and the render committed; the leg
that pairs them is already on the bar.

## 6. Acceptance criteria

- **AC1** — `--park tRun --item q --reason r` appends exactly one line matching the parked grammar
  with kind `fork`, verified by `grep -c 'fork · item '` over the record.
- **AC2** — `--park` with no `--reason` prints a refusal naming `--park requires --reason` and the
  record is byte-identical afterwards, asserted with `git hash-object`.
- **AC3** — `--park` on a record whose phase is `ABORTED` is refused by `refuse_if_terminal` and
  writes nothing.
- **AC4** — a second `--park` with the same `(item, reason)` leaves the row count at 1.
- **AC5** — `bash tools/unattended/check-unattended.sh` stays silent on a tree carrying a parked
  fork, proving check 17's waiver selector does not mis-read the new kind.
- **AC6** — `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` stay byte-identical, per the existing parity leg.

## 7. Gates

`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/check-unattended.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`python tools/memory-tree/check-arms.py` · `bash tools/run-gates.sh`.

## 8. Open questions

none — the one decision this unit could have deferred is whether the item joins the directive
registry, and §4 settles it against the asymmetry between a rule and a question. AC5 is what proves
the new kind does not disturb the one kind that IS joined.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-30`, filed when this gap was hit during
  cBriefedPilot's fold and worked around with a backlog row.

## 10. Reuse audit

`park()` is reused unchanged — this unit adds a caller, not a writer, which is what keeps check 17's
grammar and its arms valid. `refuse_if_terminal` is reused for S3 rather than adding a phase test;
it is already the single answer to "may this verb touch this record", called by all five verbs. The
paired-flag accumulator from `TOOL-cBriefedPilot-1` is reused for `--item`/`--reason` rather than a
scalar, because the scalar form is the defect that unit removed. No new marker, no new conf key, no
new gate leg: the entry is graded by the checks that already read the parked region.

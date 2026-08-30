# TOOL-aGradedMandate-5 — a retirement becomes a `surfaced`-class parked act

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

`rescope` is one parked KIND covering three ACTS, and it sits outside `PARK_KINDS_OWED`, so the
mechanism that lets a run GROW its build silently drops units from it too. The owner authorized N
units and reads a wrap-up, complete by its own test, about N-1. This unit splits the owed set by ACT
so `retire` and `supersede` reach the owner's one turn while `add` stays history.

## 2. Scope (IN)

- **S1** — Teach the owed-class predicate to discriminate a `rescope` row by its ACT. The act is
  already the first token of the item field (`item retire TOOL-…`), written by `park()`, so this is
  one predicate over bytes that already exist and no second list.
- **S2** — Make `parked-decisions-surfaced`'s counting arm count a `rescope retire` and a
  `rescope supersede` row as surfaced, and a `rescope add` row as history.
- **S3** — Make `verb_status`'s owed count agree, since it reads the same split and two readers of
  one taxonomy disagreeing is the defect this kit names.
- **S4** — Correct the driver comment that defends the whole kind's exclusion: the argument it makes
  — "an amendment it took under a delegated authority" — is about whether the owner must ANSWER, not
  whether they must be TOLD, and M3 delegates scope RESOLUTION rather than scope abandonment.
- **S5** — Correct `memory/guides/UNATTENDED-PROTOCOL.md` §2 fact 3 and its template, which
  enumerate FIVE parked kinds against the driver's eight and state that all four listed kinds are
  surfaced.

## 3. Non-goals (OUT)

- **No new kind and no new field.** `PARK_KINDS` stays eight members; only the OWED membership test
  changes shape, from a word match to a word-plus-act match.
- **No cap on retirement volume.** A ratio or count bound is a policy nobody has ruled on, and a
  build legitimately retiring several units is not obviously wrong. Visibility is the fix; a bound
  is a separate question and is backlogged.
- **No change to `verb_rescope`'s refusals.** Its arity, id-shape, separator, newline and bypass
  guards are correct and untouched.

## 4. Design

### Data model

`PARK_KINDS_OWED` becomes a set of MEMBERS where a member is either a bare kind (`decision`,
`abort`, `override`, `waiver`) or a `kind:act` pair (`rescope:retire`, `rescope:supersede`). The
complement rule is preserved exactly: absent from the set IS history, so there is still no second
list to keep in step.

### Inventory

| Site | Change |
|---|---|
| `unattended.sh` `PARK_KINDS_OWED` | two `kind:act` members added |
| `unattended.sh` `park_kinds_unowed` and `kinds_re` | the membership test widened to the pair form |
| `unattended.sh` `dod_met` `parked-decisions-surfaced` | the count regex reads the pair form |
| `unattended.sh` `verb_status` | the same split |
| `check-unattended.sh` | the both-directions taxonomy check accepts the pair form |
| `PROTOCOL.template.md` §2 · `memory/guides/UNATTENDED-PROTOCOL.md` §2 | fact 3's kind enumeration |
| `unattended.test.sh` | arms for a retire row counted, an add row not counted, and the pair round-trip |

### Migration

Records already in the tree gain surfaced rows retroactively only if they are re-closed, which no
terminal record can be. The one live record, `memory/builds/aThawedCorpus/RUN.md`, carries two
`retire` rows and an attested `parked-surfaced: yes, 2 surfaced`; it is at `LANDING` with `--close`
already run, so nothing re-evaluates it. Stated rather than assumed.

### Alternatives rejected

A separate `retire` KIND. Rejected: it would need a `park()` call site, a `PARK_KINDS` entry, a
`--rescope` branch and a leg arm, to express a distinction the act field already carries.

## 5. Production-readiness checklist

- security — N/A. A classification of rows the run already writes.
- perf / scale — N/A. One widened regex.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — a malformed act token is not silently owed or unowed: the
  membership test matches the pair exactly and anything else falls to history, which is the
  pre-change behaviour and is announced in the check's message.
- observability — `--status` reports the two counts apart, as it already does for proposals.
- risks — an attested count that was correct before this lands becomes wrong after it, for a run
  closed across the change. Only a live record can be affected and the tree holds one, examined
  above.
- testing + left-shift gates — three arms, each observed RED first.
- migration / rollback — reverting the two members restores the old classification exactly.
- user docs — `TOOL-aGradedMandate-8` names the split in the Skill's `--rescope` paragraph.

## 6. Acceptance criteria

- **AC1** — When a run-state file carries one `rescope · item retire …` row and the run attests
  `parked-decisions-surfaced` with a count that excludes it, `--close` blocks with the mismatch
  message, verified by an arm in `unattended.test.sh`.
- **AC2** — When the same record's row is `rescope · item add …`, the excluding count is accepted.
- **AC3** — `bash tools/unattended/unattended.sh --status <slug>` counts a retire row among the
  decisions the owner is owed and an add row among the notes.
- **AC4** — `bash tools/unattended/check-unattended.sh` stays green: its both-directions check over
  `PARK_KINDS_OWED` accepts a `kind:act` member and still refuses a member whose kind is outside
  `PARK_KINDS`.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh --checks` reports the protocol pair
  byte-identical after fact 3 is corrected in both copies.

## 7. Gates

`unattended kit gate` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F4 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`, the driver half.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `park_kinds_unowed` at `tools/unattended/unattended.sh:3348`, which already computes the
history class as the COMPLEMENT of `PARK_KINDS_OWED` — so widening the owed set is the only edit the
split needs, and the history side follows without a second declaration. `kinds_re` at `:3340` is the
one place a word-list becomes an alternation and is the single site where the pair form has to be
understood.

The leg's both-directions taxonomy check at `check-unattended.sh:1943-1951` is the reader that would
otherwise refuse the new member shape; it is extended rather than exempted, because an exemption
would remove the very check that catches a kind with no writer.

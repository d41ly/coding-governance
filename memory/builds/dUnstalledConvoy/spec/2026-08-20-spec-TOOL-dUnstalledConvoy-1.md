# TOOL-dUnstalledConvoy-1 — `verb_landed` accepts a local-main witness, and records which kind it took

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

A build merged to local `main` that cannot push has no terminal phase it can reach, so it aborts with
the work complete. This unit lets `--landed` accept an ancestry assertion against the LOCAL default
branch when the remote assertion fails, and records which of the two anchored the claim so a reader
can tell an observation from a record.

## 2. Scope (IN)

- **S1** — `verb_landed` keeps its current remote test as the FIRST arm. When `HEAD` is an ancestor of
  the tip the remote advertises, nothing about today's behaviour changes and the recorded anchor kind
  is `remote`.
- **S2** — when that arm fails, a SECOND arm tests whether `HEAD` is an ancestor of the local branch
  named by the advertised symref, resolved as the ref `observe_anchor` already returns in `AREF`. On
  success the phase moves to `LANDED` and the recorded anchor kind is `local`.
- **S3** — a new authored fact `landed-anchor` carries `remote` or `local`, written by the same
  `set_fact` path as `phase` and `witness`. It is written on every successful `--landed` and never
  defaulted, because an absent value would read as `remote` to any later reader.
- **S4** — a second new fact `unpushed-at-landing` carries the count of commits reachable from the
  local default branch but not from the advertised tip, and the abbreviated sha of the oldest such
  commit. It is written on both arms.
- **S5** — `verb_landed`'s stdout names the anchor kind and, on the local arm, the S4 pair. The
  refusal message for a failure of BOTH arms names both tests rather than only the remote one.
- **S6** — `observe_anchor` stays MANDATORY on both arms. It is what supplies `AREF`, and its checks
  22 through 30 are integrity tripwires that a local landing needs at least as much as a remote one.

## 3. Non-goals (OUT)

- The leg-side grading of the two witness kinds. That is `TOOL-dUnstalledConvoy-2`, and it must be a
  second opinion rather than a second copy of this arm.
- Any change to `PHASES_TERMINAL`. `LANDED` is already terminal; this unit changes how a run REACHES
  it, not what the set contains.
- Any change to `--close` or the Definition-of-Done set. A run still passes the full bar before it
  may reach `LANDING`, and this unit sits after that.
- Deciding whether the lander should be runnable from a linked worktree. That coupling is the open
  row this build cites as adjacent, and it is not reopened here.
- Refusing a landing because local `main` carries other builds' unpushed commits. S4 REPORTS that
  number; making it a refusal would re-create the wedge this build exists to remove.

## 4. Design

### Data model

Two authored facts join `phase` and `witness` in the run-state file:

```
landed-anchor: remote|local
unpushed-at-landing: <n> [oldest <sha8>]
```

`landed-anchor` is a closed two-member set. A value outside it is a refusal at read time rather than
a default, for the reason `.unattended.conf` gives for `ANCHOR_SCOPE`: a misspelling that silently
selects a member hides a misconfiguration, and this one would silently upgrade a local record into a
remote claim.

### Inventory

| Arm | Test | Anchor kind | Today |
|---|---|---|---|
| 1 | `merge-base --is-ancestor HEAD $ASHA` | `remote` | the whole verb |
| 2 | `merge-base --is-ancestor HEAD refs/heads/${AREF#refs/heads/}` | `local` | absent, and the reason the verb is unreachable |
| — | both fail | none, `fail 32` | today's message, widened to name both tests |

### What the local arm cannot buy, stated here because it is the cost of the owner's pick

The owner chose to relax `LANDED` rather than add a distinct terminal, over a recommendation that
preserved `LANDED` as the remote-observed claim. The cost is precise and is not a reason to revisit
the decision, but it must be written where a reader meets it.

A local ref is inside the run's own reach. `git update-ref refs/heads/main <sha>` moves it with no
network and no push, which is the same lever an open row in this tree already records as a reproduced
bypass against a remote-tracking ref. So a `local`-anchored `LANDED` is a RECORD that a merge
happened, not an OBSERVATION that it did. The remote arm remains an observation and remains first.

This is the repo's own `inputs-inside-the-subjects-reach` class: the ref the check reads is supplied
by the subject of the check. The mitigation that costs nothing is the one this unit ships — record
WHICH arm answered, so the two claims never have to be told apart by guessing. The mitigation that
would cost the wedge back is refusing the local arm, and that is what the owner declined.

Protocol section 9 already states what a check running under the run's own uid can and cannot buy.
`TOOL-dUnstalledConvoy-3` extends it with this case rather than restating it here.

### Why S4 exists

Local `main` is shared by every build on the node. An open row in this tree records a run whose
primary tree was clean and on `main` while carrying eleven unpushed commits, three of them a
different build entirely, mid-flight and unreviewed. A `local` landing claim sits on top of whatever
else is there, and a record that does not say how much else is there is not readable.

S4 reports rather than refuses, deliberately. A refusal here would make one build's mid-flight work
block another build's terminal, which is the exact shape of the deadlock this build is removing.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `verb_landed`: the second arm, two `set_fact` calls, the widened `fail 32` message |
| `tools/unattended/unattended.test.sh` | four cases below, plus the `ARMS_FLOORS` bump the new `fail` signature costs |

### Alternatives rejected

- **A distinct `MERGED` terminal phase.** The recommendation the owner declined. Recorded here as
  rejected by owner decision, not by test, so a later reader does not re-derive it as unconsidered.
- **Trusting `GOV_DEFAULT_BRANCH` to name the local branch when the remote is unreachable.** Refused:
  `observe_anchor` already demotes that variable to a cross-check that can only refuse, precisely
  because it was route 2 of a reproduced bypass. Reading it as an INPUT here would re-open that route
  on the terminal claim.

## 5. Production-readiness checklist

- security — the local arm is forgeable by the run and this is stated in §4, in the driver's own
  header, and in the protocol via `TOOL-dUnstalledConvoy-3`. The remote arm is unchanged.
- perf / scale — one extra `merge-base` and one `rev-list --count`. Negligible against the
  `ls-remote` the verb already performs.
- a11y — N/A — a shell verb with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — the both-arms-fail refusal names both tests. A `rev-list` that
  cannot resolve the local branch writes `unpushed-at-landing: unknown` rather than `0`, because a
  zero that means "could not measure" is this repo's named green-by-absence class.
- observability — the two facts ARE the observability, and the verb prints them.
- risks (concurrency, data-loss, rollback hazards) — no data loss: the verb only writes the
  run-state file. The concurrency risk is S4's subject and is reported rather than gated.
- testing + left-shift gates — the four cases in §6, all in `unattended.test.sh`.
- migration / rollback — existing terminal records carry no `landed-anchor`. They are frozen and must
  not be rewritten, so the READER in `TOOL-dUnstalledConvoy-2` treats an absent value on a record
  predating this unit as `remote`, which is what every existing `LANDED` record actually is.
- user docs — `TOOL-dUnstalledConvoy-3` owns the protocol and Skill text.

## 6. Acceptance criteria

- **AC1** — When `HEAD` is an ancestor of the advertised tip, `bash tools/unattended/unattended.sh
  --landed <slug>` behaves as it does today and the record carries `landed-anchor: remote`.
- **AC2** — When `HEAD` is NOT an ancestor of the advertised tip but IS an ancestor of the local
  default branch, `--landed` succeeds, the phase reads `LANDED`, and the record carries
  `landed-anchor: local`.
- **AC3** — When `HEAD` is an ancestor of neither, `--landed` refuses with `fail 32` and the message
  names BOTH the advertised tip and the local branch it tested.
- **AC4** — A fixture whose local default branch is three commits ahead of the advertised tip records
  `unpushed-at-landing: 3` with the oldest sha, observed in `unattended.test.sh`.
- **AC5** — A fixture where the local default branch cannot be resolved records
  `unpushed-at-landing: unknown`, never `0`.
- **AC6** — The failing case of each new arm is observed RED before the unit lands, and
  `bash tools/unattended/check-unattended.sh` stays green across the change.

## 7. Gates

`unattended driver selftest` · `unattended kit gate` · `harness arms` · the full bar via
`GATE_FULL=1 bash tools/run-gates/run-gates.sh` at the push boundary. The `ARMS_FLOORS` entry
`tools/unattended/unattended.sh` moves by one arm per new `fail` call site, not per new branch.

## 8. Open questions

- **F1 — should a run whose remote is UNREACHABLE be able to land locally?** `observe_anchor` refuses
  at check 27 when the remote does not answer, so under S6 the local arm is unreachable in exactly
  the case a local landing sounds most useful. Options: keep S6 as written and let such a run abort;
  or let `AREF` fall back to a local symref when the remote is unreachable. **Recommendation: keep
  S6.** The fallback would let a run with no network reach a terminal phase on a branch name it chose
  itself, and every integrity tripwire in `observe_anchor` is skipped on that path. A run that cannot
  see the remote it is supposed to land on should abort with a reason, which is a verb it already has.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an unattended run marks itself landed against an anchor"`
returns the `unattended` dossier and `.unattended.conf` as the affordance seam, and no function seam
above the fan-in threshold. The seam this unit extends is `verb_landed` itself, at
`tools/unattended/unattended.sh`, together with `observe_anchor`, which already computes `AREF` and
`ASHA` and is the only producer of both. No new helper is introduced: the second arm is one
`merge-base` call against a ref that function already names.

`python tools/memory-recall/query.py "how does an unattended run prove it landed and why must the
anchor be observed rather than read" --terms "landed anchor witness remote advertised tip ancestor
merge-base local ref update-ref bypass terminal phase run-state"` returns the anchor-observation
records and the reproduced-bypass row against a remote-tracking ref. Both were read and both bear on
§4: the bypass row is the evidence for the cost statement, not a reason to refuse the owner's pick.

Recall terms used: landed anchor witness remote advertised tip ancestor merge-base local ref
update-ref bypass terminal phase run-state.

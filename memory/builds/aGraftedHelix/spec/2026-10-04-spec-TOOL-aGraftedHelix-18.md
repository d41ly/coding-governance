# TOOL-aGraftedHelix-18 — the holder row decides `mine` before its `write_lease` and copies the claim's identity after it

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-19 |

<!-- /gen:spec-records -->

## 1. Goal

`--resume`'s holder row calls `write_lease` when the record carries no `lease-utc`, or names another
session or pid than the harness exposes (`tools/unattended/unattended.sh:6596-6599`). `write_lease`
resets `session`, `pid`, `host` and `lease-utc` (`tools/unattended/unattended.sh:5557-5572`).
`TOOL-aGraftedHelix-11` makes every claim write after a take copy its identity from those lease
facts, and states the before-and-after order only for the `--replaces` block. A builder who copies
the facts before the holder row's `write_lease` writes the OLD session into the claim, and
`write_lease` then moves the record's. The holder's next call finds a claim matching neither `mine`
nor `same session`, reads it as foreign `live`, refuses with check 90, and must
`--abort --code claim-lost`: a live run declared lost. This unit pins the order at the holder row and
observes it under a changed session. It closes finding 22 (HIGH) of the round-1 spec audit of units
10 to 15.

## 2. Scope (IN)

- **S1** — At the holder row of `--resume`, the claim's `mine` test reads the record's lease facts as
  they stood BEFORE the row's `write_lease`, which is where unit 1 S7 already puts the claim read and
  check 90. The claim write that follows copies the facts AFTER it, and unit 11 S2's "a field the
  write would set differs" compares the claim with those after-facts. Observed by AC1 and AC2.
- **S2** — A comment above the holder row states that order in the words S1 uses, as the comment
  above the `--replaces` block states its own. NOT OBSERVED by a criterion: it is a comment, and S1's
  behaviour is what AC1 drives.
- **S3** — `tools/unattended/unattended.test.sh` gains an arm: the holder's `--resume` under a
  changed `CLAUDE_CODE_SESSION_ID`, then a second call under the same changed session. NOT OBSERVED
  by a criterion here: the suite is the main loop's to run at VERIFYING, and the arm's red on a
  staged break is observed there (§7).
- **S4** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **The rule's other rows.** Every other writer of unit 11's §4 table keeps the source that table
  names. `--dispatch` and `--close` run no `write_lease`, so their before and after are one state.
- **The throttle.** A holder-row `write_lease` that moved a fact the claim carries makes a claim write
  due in the same call. That is the claim following the record, and it fires only when
  `write_lease` does, which the holder row already limits to a changed session, a changed pid or a
  missing stamp.
- **The `same session` row.** It still recognises the holder's own restart from the environment, as
  unit 11 §3 states.
- **The claim's `lease-utc` on a holder renewal.** A holder-row `write_lease`, like the `--replaces`
  block under unit 11 S1, resets the record's `lease-utc`, and the claim write that follows copies the
  new stamp, so AC2 expects the two equal. That supersedes unit 1 §4 "The claim record"'s "kept
  across a holder's renewals" for a renewal whose `write_lease` moved a fact. No verdict, age or
  take-over line reads the claim's `lease-utc`; only the renewal comparison does, and it follows the
  record.
- **A claim write that does not complete.** This unit pins the order for a push that lands. What the
  record holds when the holder's claim push times out or the remote is unreachable, and the lost race
  reaching check 90 before any local write, are `TOOL-aGraftedHelix-20`'s (§3 Edges).

### Edges

- **consumes-from** `TOOL-aGraftedHelix-11` — the rule that a renewal copies its identity from the
  record's lease facts, its renewal comparison, and the before-and-after order it states for the
  `--replaces` block, which this unit extends to the holder row; without it the holder row reads its
  identity from the environment and there is no order to pin.
- **hands-off** `TOOL-aGraftedHelix-20` — the claim write's place in §4 "The order" when its push may
  not complete: the CAS moved ahead of `write_lease` under one shared stamp, a lost race refused
  before any local write, and the `prior-session` lease fact the widened `mine` test accepts
  (finding 9 of the round-1 audit of units 16 to 19).

## 4. Design

### Evidence

- The holder row writes nothing unless `lease-utc` is absent, or the recorded session or pid
  differs from the harness's; then it calls `write_lease` and stages the record
  (`tools/unattended/unattended.sh:6591-6600`).
- `write_lease` takes the file and the keepalive id, and reads `CLAUDE_CODE_SESSION_ID` and
  `CLAUDE_PID` from its environment (`tools/unattended/unattended.sh:5557`).
- Unit 1 S7 puts the holder row's claim read and its check 90 before any local write, so `mine` is
  decided before `write_lease` runs. Unit 11 §4 "The rule" gives the holder row "the record's lease
  facts" with no order.

### The order

| step | reads | writes |
|---|---|---|
| claim read, `mine` test, check 90 | the record's facts before the call | nothing |
| `write_lease`, when due | the environment | the record's lease facts |
| claim write, when due | the record's facts after `write_lease` | the claim |

With an unchanged session the first and third reads are the same state and nothing moves. With a
changed session the claim is `mine` against the old facts, then follows the new ones, so the next
holder call reads `mine` again. That holds for a push that lands. `TOOL-aGraftedHelix-20`, built
next, swaps the second and third rows so the CAS precedes the local write, and states what the
record holds when the push does not land.

### Inventory

No new function, check, conf key or file. The holder row's claim write reads the record after its
`write_lease` instead of before it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Decide `mine` after `write_lease`.** It reads the new session against a claim carrying the old
  one, so the holder refuses its own claim on the very call that moved the session. Unit 1 S7 also
  rules it out, because check 90 must fire before any local write.
- **Skip `write_lease` while a claim is held.** The lease record is what the hooks and the tick bind
  to, and a stale session there makes `--liveness` misread the run.

## 5. Production-readiness checklist

- security — No new surface. The claim publishes the lease facts the run branch already carries.
- perf / scale — At most one extra claim push, on the call whose `write_lease` moved a fact.
- error / empty / loading states — A claim write that does not complete is unit 1's announce row
  here. Under this unit's order it leaves the record and the claim naming different sessions, which
  `TOOL-aGraftedHelix-20` closes.
- observability — The holder row's existing `lease recorded` line names the session move, and the
  claim then shows the new session.
- risks — A harness that changes `CLAUDE_PID` on every call would make a claim write due on every
  call. No harness here does; `write_lease`'s own line reports each move.
- testing — S3's arm, observed RED with the claim write reading the facts before `write_lease`.
- migration — None: no claim exists before unit 1 lands.
- user docs — N/A: the claim's fields are unchanged.

## 6. Acceptance criteria

The fixture is unit 1's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, `RUN_CLAIMS` on, and a run whose record and claim both name session
`s1` and the recorded keepalive.

- **AC1** — When `--resume <slug> --keepalive-id <recorded id>` runs with `CLAUDE_CODE_SESSION_ID`
  set to `s2`, it exits 0 and prints the `lease recorded` line naming `s1 -> s2`, and the claim read
  with `git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p` carries `session: s2`. A
  second identical call exits 0 and prints no `UNATTENDED check 90 FAILED`.
  Red when: the claim still names `s1`, or the second call refuses with check 90.
- **AC2** — When the same call runs with the session unchanged and `CLAUDE_PID` changed, it exits 0
  and the claim's `lease-utc` equals the record's `lease-utc` byte for byte. A following call with
  the same pid leaves the claim ref's sha unchanged.
  Red when: the claim carries the stamp from before `write_lease`, or a call that moved nothing
  pushes.
- **AC3** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the holder's --resume under a changed session, then again under that session; stage the claim write reading the lease facts before write_lease · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs the block as a
slice, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 22 of the round-1 spec audit of units 10
  to 15, grounded against `write_lease` and the holder row at base `5266d22e`.
- rev-2 · 2026-10-04 · §3 §4 §5 · folded the round-1 spec audit of units 16 to 19 on this unit.
  Finding 15: §3 records that a holder-row `write_lease` resets the claim's `lease-utc`, superseding
  unit 1 §4's "kept across a holder's renewals" for such a renewal; AC2 is unchanged. Finding 9 is
  promoted to `TOOL-aGraftedHelix-20`: §3 gains its hands-off and a non-goal, and §4 "The order" and
  §5 point at it for a push that does not complete.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "copy lease facts after the lease record is rewritten in
the same call"` ranked name-stem neighbours only, `records` in `gotchas.py` and `resolveLease` in
`tools/unattended/run-lease.js`, and printed `unscanned layers: .sh`, so its miss is no evidence. No
existing seam fits beyond the lease record itself: the seams were read from source, `write_lease`
and the holder row in `tools/unattended/unattended.sh`, and the order unit 11 states for the
`--replaces` block. The recall probe returned `TOOL-dDerivedDocket-61`, the ruling that the lease is
one record of run-state facts, and unit 11's §8 F1, and no record that orders a read around a lease
rewrite.

Recall terms used: write_lease holder resume lease-utc session keepalive claim renewal record facts order mine

The question passed with them: "when a resume rewrites the lease record, which facts does a later
write in the same call read".

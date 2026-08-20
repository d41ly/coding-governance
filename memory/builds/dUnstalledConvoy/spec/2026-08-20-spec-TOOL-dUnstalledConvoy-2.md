# TOOL-dUnstalledConvoy-2 — leg check 15 grades both witness kinds, and announces the case it cannot reach

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling · ratified 2026-08-20

## 1. Goal

Check 15's second half asserts that a `LANDED` witness is an ancestor of the tip the remote
advertises. Once `TOOL-dUnstalledConvoy-1` lets a run land on a local witness, that assertion reds
every locally-landed record. This unit teaches the check the two witness kinds without letting it
become a second copy of the driver's arm.

## 2. Scope (IN)

- **S1** — check 15's ancestry half reads the record's `landed-anchor` fact and branches on it. A
  `remote` value keeps today's assertion against the advertised tip, unchanged.
- **S2** — a `local` value asserts the witness is an ancestor of the LOCAL default branch instead,
  and **S2b supplies the branch NAME, which the leg does not currently hold.** It
  does NOT assert the witness is absent from the remote: a local landing that was later pushed is an
  upgrade, not a defect, and refusing it would red a record that became MORE true.
- **S3** — a value outside the closed set `remote local` is a refusal naming the value, never a
  default. A default here would silently promote an unreadable record to the stronger claim.
- **S4** — an ABSENT `landed-anchor` on a record whose first commit is dated at or after a new
  `LANDED_ANCHOR_CUTOFF` in `.unattended.conf` is a refusal. Before that date it is read as `remote`,
  which is what every `LANDED` record in this tree today actually is.
- **S2b** — the leg gains ONE new resolution: the symref NAME is parsed out of the remote
  advertisement it already runs, into its own variable beside the sha it already keeps. Review fold:
  H9. The first draft's §10 claimed the name was already to hand; it is not — the leg keeps only the
  sha, and grepping it for a default-branch name, a heads or remotes ref, or the environment override
  returns two COMMENTS, one recording that those reads were deliberately purged from this path because
  the run can write both. A builder reaching for either substitute would re-open a reproduced bypass
  on the check that grades a terminal claim.
- **S2c** — the local arm is **scoped to the node that wrote the record**, and SKIPS elsewhere through
  the announced-skip mechanism this unit already adds. Review fold: H9, second half. The run-state
  file is tracked and travels to every node; a local default-branch ref does not. Without this, node
  `d` lands locally and commits a `local`-witness record, node `b` pulls the branch without
  fast-forwarding its own default branch, and the same leg reds there on a record that is green where
  it was written — while the leg's own header states the intent this would defeat, that its value
  comes from running in a clone the run never touched.
- **S5** — the check ANNOUNCES the case it cannot reach. Where no default branch resolves, the
  ancestry half is skipped today in silence, inherited from check 9. This unit prints a named skip
  line instead, stating which arm went unexercised and why — **through the report channel
  `TOOL-dUnstalledConvoy-6` establishes, and specifying no contract change of its own.** Review
  fold: H1, owner decision: that unit lands first among the four and owns the leg output contract.
- **S6** — `.unattended.conf` gains `LANDED_ANCHOR_CUTOFF`, and **this unit owns ALL THREE carriers**
  — the project conf, the shipped `.unattended.conf.example`, and the protocol's key table — because
  it is the unit that adds the READER. Review fold: M9. The first draft split them across two units
  and leaned on a conf-axis check that does not exist: the only arm reading the shipped example
  iterates key names and asserts the DRIVER defaults each one, so a key read by the LEG is skipped
  entirely, and nothing anywhere joins a conf key to the protocol's key table. Two live keys are
  missing from that table today with the bar green, and the OPEN row proposing that gate is cited in
  §10 rather than assumed closed.
- **S6a** — the key's BLANK and ABSENT semantics are stated, and the key is added to the leg's
  conf-init block. Review fold: M10. The leg runs with unset variables fatal and pre-declares every
  conf key it reads in one init block that names neither new key, so an adopter whose conf predates
  the key would meet an unbound-variable death rather than a named refusal. Blank resolves FORWARD to
  the shipped date, matching the memory-tree conf's sibling date key and for its stated reason — an
  empty string compares earlier than every date, so blank-as-empty would silently mean always-required.
  The leg's sibling test gains an arm mirroring the driver's defaulted-key arm.

## 3. Non-goals (OUT)

- Re-deriving the driver's pick. This check grades the RECORDED anchor against history and against
  the record's own well-formedness. It never re-runs the driver's two arms to see which it would have
  chosen, because a gate that recomputes the driver's answer from the driver's inputs confirms it
  rather than checks it.
- Closing the open row about check 9's silent exits. S5 announces THIS check's skip; the other silent
  exits in that block stay as they are and the row stays open.
- Any change to check 15's FIRST half. A sha-shaped witness is still required at `LANDED`, for both
  kinds, and that half correctly sits outside the anchor loop.
- Any change to check 7 or to `PHASES_TERMINAL`.

## 4. Design

### Inventory

| Recorded `landed-anchor` | Assertion | On failure |
|---|---|---|
| `remote` | witness is an ancestor of the advertised tip | today's `fail 15` message |
| `local` | witness is an ancestor of the local default branch | a new `fail 15` message naming the local branch |
| absent, record at or after the cutoff | none — the absence IS the refusal | a `fail 15` naming the cutoff and the repair |
| absent, record before the cutoff | read as `remote`, then as row 1 | today's message |
| anything else | none — the value IS the refusal | a `fail 15` naming the value and the closed set |
| no default branch resolves | none | a named SKIP line, not silence |

### Why this is a second opinion and not a second implementation

The driver CHOOSES an anchor by testing ancestry and writes what it chose. The leg does not repeat
that choice. It takes the written claim as an input it distrusts and asks two questions the driver
never asked: is this record well-formed at all, and does the history still support the claim it
makes. Both can fail on a record the driver wrote happily — a hand-edited fact, a record retired and
edited afterwards, a `local` claim whose branch was later reset behind the witness.

What it cannot buy is stated in the check's own header, per the rule that a gate's header states what
it does NOT check: a `local` claim is anchored on a ref inside the run's reach, so this check grades
the claim's CONSISTENCY and never its truth. The remote arm is the only one of the two that is an
observation, and it stays first in the driver for that reason.

### Migration

The eight `LANDED` records already in this tree carry no `landed-anchor`. They are terminal and
frozen, and rewriting them would edit a finished record — the thing the kit refuses everywhere else.
`LANDED_ANCHOR_CUTOFF` is set to the day this unit lands, exactly as `UNITS_REGION_CUTOFF` is set to
the day its migration render landed and for the same reason: without a cutoff, the unit is unlandable
by any run, because the run that lands it has records older than itself in the tree.

Moving the cutoff later re-admits an absent fact for every record in between. Moving it earlier reds
records that can never carry the key. The conf comment states both, in the idiom the file already
uses for its three other cutoffs.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | check 15's ancestry half, the skip announcement, the cutoff read |
| `tools/unattended/check-unattended.test.sh` | six cases, plus the `ARMS_FLOORS` bump per new `fail` call site |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |
| `.unattended.conf` | `LANDED_ANCHOR_CUTOFF` with its comment |
| `tools/unattended/.unattended.conf.example` | the same key, so the catalogue check stays satisfied |
| `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` | the key table row, moved as a pair by `TOOL-dUnstalledConvoy-3` |

### Alternatives rejected

- **Dropping check 15's ancestry half entirely.** It would make `LANDED` unjudgeable for both kinds,
  and the remote arm is the one honest observation in the whole terminal claim.
- **Refusing a `local` record whose witness IS on the remote.** Rejected in S2: that record describes
  work which reached the remote after the fact, and refusing it punishes the good outcome.

## 5. Production-readiness checklist

- security — this check grades a claim anchored on a ref the run can move, and its header says so.
- perf / scale — one extra `merge-base` per `LANDED` record, inside a loop that already runs one.
- a11y — N/A — a shell gate with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — S5 is exactly this: the unreachable case gets a line rather than
  silence, so a green row is never misread as a verified one.
- observability — the skip line and the four distinct refusal messages.
- risks (concurrency, data-loss, rollback hazards) — read-only. No write path.
- testing + left-shift gates — the six cases in §6. Each new `fail` branch needs its entire literal
  signature armed, and adding branches renumbers the per-check ordinals below the insertion point.
- migration / rollback — the cutoff, above. Rollback is reverting the conf key and the branch.
- user docs — the protocol key table, owned by `TOOL-dUnstalledConvoy-3`.

## 6. Acceptance criteria

- **AC1** — A fixture record with `landed-anchor: remote` and a witness off the advertised tip reds
  with today's message, observed in `check-unattended.test.sh`.
- **AC2** — A fixture record with `landed-anchor: local` and a witness on the local default branch
  but NOT on the advertised tip passes, where today it reds.
- **AC3** — A fixture record with `landed-anchor: local` and a witness on NEITHER branch reds with a
  message naming the local branch.
- **AC4** — A fixture record with `landed-anchor: sideways` reds with a message naming the value and
  the closed set.
- **AC5** — A fixture record with no `landed-anchor`, first-committed at or after
  `LANDED_ANCHOR_CUTOFF`, reds; the same record committed before the cutoff passes.
- **AC6** — A fixture clone whose remote advertises no default branch prints a named skip line for
  this arm, and `bash tools/unattended/check-unattended.sh` exits 0 with that line present.
- **AC7** — `LANDED_ANCHOR_CUTOFF` appears in `.unattended.conf`, in
  `tools/unattended/.unattended.conf.example`, and in the protocol's key table — each asserted
  SEPARATELY by `grep`, not through a pairing check. Review fold: M9; no such pairing check exists.
- **AC8** — A fixture whose conf omits the key entirely runs the leg to a normal verdict rather than
  dying on an unbound variable, and a fixture whose key is BLANK behaves as the shipped date. Both
  observed in `tools/unattended/check-unattended.test.sh`. Review fold: M10.
- **AC9** — A fixture parsing the advertisement yields the branch NAME in its own variable, and a
  `local` record evaluated on a clone whose default branch is behind the witness prints the announced
  node-scope skip rather than redding. Both in `tools/unattended/check-unattended.test.sh`. Review
  fold: H9.
- **AC10** — The check's header STATES what it cannot buy, observed by `grep` over
  `tools/unattended/check-unattended.sh`. Review fold: L1.

## 7. Gates

`unattended kit gate` · `unattended kit selftest` · `harness arms` · the full bar at the push
boundary. `ARMS_FLOORS` moves for `tools/unattended/check-unattended.sh`.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): a DATE, matching the three cutoffs this conf already carries. A first-blob presence test would need no key at all and would grandfather correctly, but it makes the grandfathering invisible to anyone reading the conf, and a declared cutoff is readable where a derived one is not.**

  The question this settles: should the cutoff be a DATE or the presence of the key in the record's first blob? A date
  is the idiom this conf already uses three times and is what S4 specifies. A first-blob presence
  test would need no conf key at all and would grandfather correctly with no value to maintain, but
  it makes the grandfathering invisible to anyone reading the conf. **Recommendation: the date**, for
  consistency with `UNITS_REGION_CUTOFF` and because a declared cutoff is readable and a derived one
  is not. Resolve before building; it changes S4 and S6 and nothing else.

## 9. Revision log

- rev-2 · 2026-08-20 · folded the spec audit: H9 (the leg holds no default-branch NAME — S2b parses it out of
  the advertisement, and S2c scopes the local arm to the writing node so the record does not red on
  another clone), M9 (this unit owns all three carriers of the new key, and AC7 stops leaning on a
  pairing check that does not exist), M10 (blank and absent semantics stated, key added to the leg's
  init block), H1 (the skip rides the channel unit 6 establishes), L1. Four new criteria.
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a gate grades a terminal phase claim against git
ancestry"` returns the `unattended` dossier and no function seam above the fan-in threshold. The seam
this unit extends is check 15's existing two halves in `tools/unattended/check-unattended.sh`,
together with the anchor loop that already computes `$b`. **A new resolution path IS introduced, and S2b owns it.** The first draft claimed the branch name was
already to hand; the leg keeps only the sha from its advertisement and holds no default-branch name
anywhere. The name derives from the remote advertisement and from nothing local, which is the only
admissible source — the environment override and the remote-tracking ref were both deliberately
purged from this path as a reproduced bypass. Review fold: H9.

`python tools/memory-recall/query.py "why must a gate be a second opinion rather than a second
implementation of the driver it grades" --terms "second opinion implementation driver gate recompute
inputs subject reach anchor witness ancestry cutoff grandfather"` returns the second-opinion class
record and the cutoff-idiom records. Verified against source at writing time: check 15's two halves
are at the lines this spec describes, and the silent-skip inheritance from check 9 is stated in the
existing comment rather than assumed.

Recall terms used: second opinion implementation driver gate recompute inputs subject reach anchor
witness ancestry cutoff grandfather.

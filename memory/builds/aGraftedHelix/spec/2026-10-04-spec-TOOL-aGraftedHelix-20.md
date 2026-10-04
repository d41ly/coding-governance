# TOOL-aGraftedHelix-20 — the holder row's claim CAS runs before its `write_lease` under one stamp, and a CAS that does not land leaves a `prior-session` fact the `mine` test accepts

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-18` orders the `--resume` holder row as: decide `mine` against the record's facts
before the call, run `write_lease`, then write the claim from the facts after it. Unit 1's call-site
table keeps a holder claim write that does not complete as "announce, continue". Take a holder call
whose session changed from `s1` to `s2` and whose claim push times out, or that runs offline, which
unit 1 supports on the holder path. Afterwards the record names `s2` and the claim names `s1`. On the
next `s2` call the claim is not `mine`, which needs the record's keepalive AND session, and not
`same session`, because the claim's `s1` differs from the environment's `s2`. It reads as foreign, the
holder column answers check 90, and a live run is forced to `--abort --code claim-lost`. A lost race
on that call likewise reaches check 90 only after `write_lease` has rewritten and staged the record,
which breaks unit 1's rule that the CAS precedes every local write. This unit moves the claim CAS
ahead of `write_lease` under one lease stamp, and records what the claim still carries when the CAS
does not land. It closes finding 9 (HIGH) of the round-1 spec audit of units 16 to 19.

## 2. Scope (IN)

- **S1** — At the `--resume` holder row, when `write_lease` is due, the claim read, the `mine` test
  and check 90 run against the record's facts as they stood before the call, as unit 18 S1 has
  them. The row then computes the lease stamp ONCE, writes the claim by CAS with the values the call
  is about to record (`session` from `CLAUDE_CODE_SESSION_ID`, `host` from `read_host_name`, the
  unchanged `keepalive`, and the stamp as `lease-utc`), and only then calls `write_lease` with that
  stamp as its third argument. A LOST race is check 90 with the run-state file's bytes and the index
  untouched. Observed by AC1 and AC3.
- **S2** — When the CAS does not complete, or the claim could not be read, the row still runs
  `write_lease`, and records a lease fact `prior-session` holding the record's `session` fact from
  before the call. The fact is written only while it reads `absent` or is missing, so a second call
  that also fails to land keeps the session the published claim still carries. The next holder-row
  claim write that lands sets it `absent`. Observed by AC2.
- **S3** — The `mine` test, wherever it compares the claim with the record's facts, also accepts a
  claim whose `keepalive` equals the record's and whose `session` equals the record's
  `prior-session` fact when that fact is not `absent`. Those are the holder and status-write
  columns of unit 1's table; `--preflight` and a take-over compare with the values they are about to
  record and are unchanged. Observed by AC2.
- **S4** — `check_lease_only_diff` in `tools/unattended/lib-unattended.sh` admits `prior-session`
  as a lease-fact line, because it is written beside `write_lease`'s six. The lease section of
  `tools/unattended/STOPS.template.md` names it, re-rendered into `memory/guides/UNATTENDED-STOPS.md`
  in the same commit. Observed by AC4.
- **S5** — `tools/unattended/unattended.test.sh` gains three arms over unit 18's changed-session
  arm: the claim push made to exit 124, the remote unreachable, and the lost race, each on the `s2`
  call. NOT OBSERVED by a criterion here: the suite is the main loop's to run at VERIFYING, and each
  arm's red on a staged break is observed there (§7).
- **S6** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC5.

## 3. Non-goals (OUT)

- **The take sites.** `--preflight` and `run_takeover` already CAS before `write_lease` (unit 1's
  call-site table) and share one stamp (unit 11 S6). `--dispatch` and `--close` run no
  `write_lease`.
- **`RUN_CLAIMS` off.** No claim is read or written, the row runs `write_lease` as it does at base,
  and `prior-session` is never written.
- **The `--replaces` block.** It moves the keepalive, not only the session, and an incomplete CAS
  there leaves a claim the holder's own `same session` row takes back while the session is
  unchanged. This unit does not reorder it; a session AND keepalive change with an incomplete push
  is a follow-up for that block's own order.
- **Clearing the fact from other writers.** `--beat`, `--dispatch`, `--close` and the status writes
  copy their identity from the record, so a write of theirs that lands publishes `s2` too, but they
  leave `prior-session` as it is. A stale value widens `mine` only to a claim carrying this run's
  own keepalive, and the next holder-row write that lands clears it.
- **Supersessions this unit records.** It supersedes unit 1 §4 "Who may write a claim"'s `mine`
  definition, and unit 11 §3's "The `mine` test ... is unchanged", for the holder and status-write
  columns (S3). It swaps the second and third rows of unit 18 §4 "The order" (S1). It moves the
  `--resume` holder row of unit 11 §4 "The rule" from "the record's lease facts" to the values the
  call records, whenever `write_lease` is due.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-18` — the holder row's order with `mine` decided against the
  facts before the call, and its changed-session arm, which this unit's arms extend; without it the
  rows this unit swaps are not pinned.
- **consumes-from** `TOOL-aGraftedHelix-11` — `write_lease`'s optional third argument, the lease
  stamp, and the rule that a claim write copies its identity from the lease; without the argument
  the claim's stamp and the record's cannot be one value.
- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable`'s `mine` test, the holder row's
  claim read and check 90, the "announce, continue" row for an incomplete holder write, and the
  lost-race `git` shim of its suite; without them there is no test to widen and no fixture to drive.

## 4. Design

### Evidence

- `write_lease` takes the run-state file and the keepalive id at base, and stamps `lease-utc` with
  `date -u` itself (`tools/unattended/unattended.sh:5557-5572`). Unit 11 S6 gives it an optional
  third argument, the stamp, read in place of the clock when present; that is how the shared stamp
  reaches it.
- The holder row runs `write_lease` and `stage_or_fail` only when `lease-utc` is absent or the
  recorded session or pid differs from the harness's (`tools/unattended/unattended.sh:6591-6600`).
- Unit 1's §5 risks line names the class: "the CAS precedes every local write". Unit 18 §4
  "Alternatives rejected" cites the same premise.
- `check_lease_only_diff` (`tools/unattended/lib-unattended.sh:1172`) accepts a working-copy
  difference confined to the six lines `write_lease` writes, and `read_landing_commit` relies on it
  for a re-bind of a pushed landing. A seventh fact written beside them would read as a non-lease
  difference without S4.
- The claim carries no pid, so a pid-only change still moves `lease-utc`, and the claim follows the
  record's stamp (unit 18 §3). Whenever `write_lease` is due, a claim write is due too.

### The order

| step | reads | writes |
|---|---|---|
| claim read, `mine` test, check 90 | the record's facts before the call, `prior-session` included | nothing |
| the stamp, when `write_lease` is due | the clock, once | nothing |
| claim CAS, when due | the values `write_lease` is about to record, and the stamp | the claim |
| `write_lease`, when due | the environment, and the stamp as its third argument | the record's lease facts |
| `prior-session` | the CAS outcome | set or cleared per the table below |

### What each outcome leaves

| CAS outcome on the `s2` call | claim | record `session` | record `prior-session` | the call |
|---|---|---|---|---|
| landed | `s2` | `s2` | `absent` | continues |
| lost | another writer's | `s1`, untouched | untouched | check 90 |
| not completed, or the claim unreadable | `s1` | `s2` | `s1` | announces, continues |

After the third row, the next `s2` call reads the claim as `mine` through `prior-session`, finds the
`session` field differing, writes, and on landing sets the fact `absent`.

### Inventory

One new run-state fact, `prior-session`. No new function, check, conf key or file. A fact key is
not a lexicon cell here, and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-STOPS.md`, by the render
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Keep `write_lease` first and let the next call's `same session` row take the claim.** The
  `same session` row compares the claim's session with the environment's. After the incomplete call
  the claim names `s1` and the environment `s2`, so it misses; that is finding 9.
- **Skip `write_lease` when the CAS does not complete.** The lease record is what the hooks and the
  tick bind to, so an outage would leave `--liveness` reading the old session for as long as it lasts.
  Unit 18 rejects skipping it for the same reason.
- **Retry the push inside the call until it lands.** A bounded call cannot wait out an outage, and
  unit 1 keeps the holder path working offline on purpose.

## 5. Production-readiness checklist

- security — No new surface. The fact names a session id the run branch already publishes in the
  record's `session` line.
- perf / scale — None added: the claim write was already due on a call whose `write_lease` ran.
- error / empty / loading states — The three outcomes of §4 "What each outcome leaves". An
  incomplete push keeps unit 1's announce line.
- observability — The announce line names the write that did not land, and `prior-session` in
  the run-state file shows which session the published claim still carries.
- risks — A reader matching the lease's lines by an explicit list. `check_lease_only_diff` is the
  one in the tree and S4 extends it; the builder greps the kit for the six-name list before landing.
  A stale `prior-session` widens `mine` only to a claim under this run's own keepalive.
- testing — S5's arms, each observed RED on a staged break first: the incomplete-push arms with the
  CAS moved back after `write_lease`, and the lost-race arm with the record staged before the CAS.
  The lost race is staged by unit 1's `git` shim on `PATH`, never by a sleep.
- migration — None: no claim exists before unit 1 lands, and a record without the fact reads
  `absent`.
- user docs — The lease section of the stops guide, re-rendered in the same commit.

## 6. Acceptance criteria

The fixture is unit 18's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, `RUN_CLAIMS` on, and a run whose record and claim both name session
`s1` and the recorded keepalive. Each call below is `--resume <slug> --keepalive-id <recorded id>`
with `CLAUDE_CODE_SESSION_ID` set to `s2`.

- **AC1** — When the call runs with unit 1's lost-race `git` shim on `PATH`, which moves the claim
  ref before forwarding the push, it prints `UNATTENDED check 90 FAILED`, the run-state file's
  `session:` fact still reads `s1`, and `git diff --name-only` and `git diff --cached --name-only`
  name no run-state file.
  Red when: `write_lease` ran before the refusal, so the record moved on a call that lost its claim.
  fixture: the shim is unit 1's and exists once unit 1 is built.
- **AC2** — When the call runs with a `git` shim on `PATH` that makes the claim push exit 124, it
  exits 0, the run-state file reads `session: s2` and `prior-session: s1`, and the claim read with
  `git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p` still names `session: s1`. A
  second call with no shim exits 0, prints no `UNATTENDED check 90 FAILED`, leaves a claim naming
  `session: s2`, and leaves `prior-session: absent`. The same holds when the bare repository is
  renamed away for the first call and restored for the second.
  Red when: the second call refuses its own claim with check 90.
- **AC3** — When the call runs with no shim and the push lands, the claim's `lease-utc` equals the
  record's `lease-utc` byte for byte, and the record's `prior-session` is missing or reads
  `absent`.
  Red when: the claim and the record carry stamps read from two clocks.
- **AC4** — When `check_lease_only_diff`, sourced from `tools/unattended/lib-unattended.sh`, runs in
  a scratch repository whose committed run-state file differs from its working copy only by an added
  `prior-session: s1` line, it returns 0. With a `phase:` line changed as well, it returns 1.
  Red when: the new fact reads as a non-lease difference, so a re-bind of a pushed landing stops
  finding its landing commit.
- **AC5** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the s2 holder call whose claim push exits 124, then a second s2 call; stage the CAS moved back after write_lease · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · the s2 holder call with the remote unreachable, then a second s2 call with it restored; stage prior-session left unwritten · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · the s2 holder call that loses the race leaves the run-state file and the index untouched; stage write_lease run before the CAS · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 9 of the round-1 spec audit of units 16
  to 19, grounded against `write_lease`, the holder row and `check_lease_only_diff` at base
  `5266d22e`, and against units 1, 11 and 18 as specced.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write the claim before the lease record and remember the
replaced session when the push does not complete"` ranked name-stem neighbours only, `write` in
`tools/memory-tree/gotchas.py` and `records`, and printed `unscanned layers: .sh`, so its miss is no
evidence. The seams were read from source: `write_lease` with unit 11 S6's stamp argument, the
holder row in `tools/unattended/unattended.sh`, and `check_lease_only_diff` in
`tools/unattended/lib-unattended.sh`. No existing seam records what a published record still carries
when its push did not land. The recall probe returned unit 18, the audit's H1 row, unit 11, and
`TOOL-dDerivedDocket-61`, the ruling that the lease is one record of run-state facts.

Recall terms used: claim CAS write_lease incomplete push announce continue lease record session holder mine order

The question passed with them: "when a compare-and-swap push of a claim does not complete, what does
the local lease record hold".
